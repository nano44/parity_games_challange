#!/usr/bin/env python3
"""L-NEW box 139 PATHS: check of Proposition PATHS on IDEAL genomes (R178 §1 model; values = fastcyc_r178.values, a read-only copy of
claude/l-red experiments/red/r178/fastcyc.py; step rule = r187/ideal.py traj, re-implemented here). Per mover x:
- CURVIOL: the current face value of x decreases at some step, or does not strictly increase at a move of x;
- KEYVIOL: the root-first key of x's current option increases, or does not strictly decrease at a move;
- VX(x) = number of distinct values of Xi-paths from x (needs an acyclic Xi-graph), VW(x) = number of distinct root-first keys of W-paths
  from x; BOUNDVIOL: moves(x) > min(VX, VW) - 1.
Prints per genome: N, steps, stop reason, total moves, max moves of one mover, max VX, max VW, the violations, and SLACK = max over
movers of moves / (min(VX, VW) - 1). Usage: paths.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fastcyc_r178 as fc
def run(G, cap=100000):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    order = sorted(range(N), key=lambda v: lev[v]); s = list(G["start"]); S = [tuple(s)]; CUR = []; KEY = []
    while len(S) - 1 < cap:
        val, idx, _, M = fc.values(G, s)
        face = lambda v, k: val(N + idx[(v, k)])
        cur = [face(v, s[v]) for v in range(N)]
        avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > cur[v]] for v in range(N)]
        def keys(st):
            key = [None] * N
            for v in order:
                wt = opts[v][st[v]][0]; key[v] = (gate[v][st[v]],) if wt < 0 else key[wt] + (gate[v][st[v]],)
            return key
        CUR.append(cur); KEY.append(keys(s))
        if all(len(a) == 1 for a in avail): return S, CUR, KEY, "opt"
        key = [None] * N; ns = list(s)
        for v in order:
            best = None
            for k in avail[v]:
                wt = opts[v][k][0]; kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
                if best is None or kk < best[0]: best = (kk, k)
            key[v] = best[0]; ns[v] = best[1]
        if ns == s: return S, CUR, KEY, "stuck"
        s = ns; S.append(tuple(s))
    return S, CUR, KEY, "cap"
def vx(G):
    N, opts, br, bp = G["N"], G["opts"], G["br"], G["bp"]; memo = {}
    def V(x):
        if x in memo: return memo[x]
        memo[x] = None
        out = set()
        for (wt, xt, b) in opts[x]:
            p = 4 + 2 * br[b] + bp[b]; wb = (1 << p) * (1 if p % 2 == 0 else -1)
            sub = {(0, 0)} if xt < 0 else V(xt)
            if sub is None: raise SystemExit("Xi-graph cyclic")
            out |= {(w + wb, l + 3) for (w, l) in sub}
        memo[x] = out; return out
    return [len(V(x)) for x in range(N)]
def vw(G):
    N, opts, lev = G["N"], G["opts"], G["lev"]; memo = {}
    def C(x):
        if x not in memo: memo[x] = sum(1 if wt < 0 else C(wt) for (wt, xt, b) in opts[x])
        return memo[x]
    return [C(x) for x in range(N)]
for path in sys.argv[1:]:
    G = json.load(open(path)); S, CUR, KEY, why = run(G); N = G["N"]
    VX, VW = vx(G), vw(G); mv = [0] * N; cv = kv = 0
    for t in range(1, len(S)):
        for x in range(N):
            m = S[t][x] != S[t - 1][x]; mv[x] += m
            if t < len(CUR):
                if CUR[t][x] < CUR[t - 1][x] or (m and not CUR[t][x] > CUR[t - 1][x]): cv += 1
                if KEY[t][x] > KEY[t - 1][x] or (m and not KEY[t][x] < KEY[t - 1][x]): kv += 1
    bv = sum(1 for x in range(N) if mv[x] > min(VX[x], VW[x]) - 1)
    slack = max((mv[x] / (min(VX[x], VW[x]) - 1) for x in range(N) if min(VX[x], VW[x]) > 1), default=0)
    print(f"PATHS {os.path.basename(path)} N {N} STEPS {len(S) - 1} STOP {why} MOVES {sum(mv)} MOVMAX {max(mv)} VXMAX {max(VX)} VWMAX {max(VW)} "
          f"CURVIOL {cv} KEYVIOL {kv} BOUNDVIOL {bv} SLACK {slack:.4f}")
