#!/usr/bin/env python3
"""L-NEW box 140 ALT: checks on IDEAL-ACYC genomes (R178 §1 rule; values = box139/fastcyc_r178.py).
- ALTVIOL (Lemma ALTERNATION, deg-2 movers): between two consecutive moves of x (at steps t1 < t2) the face order of x's two options at
  the decision states t1 - 1 and t2 - 1 is opposite, and so is the key order read at t1 and t2 (keys from the new strategy).
- For 2-wide complete ladders (movers 2l, 2l+1 at level l, option k -> mover 2(l-1)+k): TOWARDVIOL (a level >= 1 mover moves to an
  option whose W-target is not the key-smaller mover of level l - 1 at the new state); per level: moves and LFLIPS (changes of
  L_l = key-smaller mover of level l); LFVIOL (flips(L_l) > flips(L_(l-1)) + moves at level l).
Usage: alt.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box139"))
import fastcyc_r178 as fc
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
for path in sys.argv[1:]:
    G = json.load(open(path)); S, CUR, KEY, why = run(G); N, opts, gate, lev = G["N"], G["opts"], G["gate"], G["lev"]
    order = sorted(range(N), key=lambda v: lev[v])
    def faces(s):
        val, idx, _, M = fc.values(G, list(s)); return [[val(N + idx[(v, k)]) for k in range(len(opts[v]))] for v in range(N)]
    def okeys(s):
        key = [None] * N; ok = [None] * N
        for v in order:
            ok[v] = [((gate[v][k],) if opts[v][k][0] < 0 else key[opts[v][k][0]] + (gate[v][k],)) for k in range(len(opts[v]))]
            key[v] = ok[v][s[v]]
        return key, ok
    F = [faces(s) for s in S]; KO = [okeys(s) for s in S]
    altv = tow = lfv = 0; last = {}
    lad = all(len(opts[v]) == 2 for v in range(N)) and all(lev[v] == v // 2 for v in range(N)) and \
          all(opts[v][k][0] == (-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k) for v in range(N) for k in range(2))
    d = max(lev) + 1; mvl = [0] * d; lfl = [0] * d
    for t in range(1, len(S)):
        for x in range(N):
            if S[t][x] == S[t - 1][x]: continue
            mvl[lev[x]] += 1
            if len(opts[x]) == 2:
                if x in last:
                    t1 = last[x]
                    fo = lambda tt: F[tt][x][0] > F[tt][x][1]
                    ko = lambda tt: KO[tt][1][x][0] < KO[tt][1][x][1]
                    if fo(t1 - 1) == fo(t - 1) or ko(t1) == ko(t): altv += 1
                last[x] = t
            if lad and lev[x] >= 1:
                l = lev[x]; key = KO[t][0]; Lm = 2 * (l - 1) if key[2 * (l - 1)] < key[2 * (l - 1) + 1] else 2 * (l - 1) + 1
                if opts[x][S[t][x]][0] != Lm: tow += 1
        if lad:
            for l in range(d):
                k0, k1 = KO[t][0][2 * l], KO[t][0][2 * l + 1]; p0, p1 = KO[t - 1][0][2 * l], KO[t - 1][0][2 * l + 1]
                lfl[l] += (k0 < k1) != (p0 < p1)
    if lad: lfv = sum(1 for l in range(1, d) if lfl[l] > lfl[l - 1] + mvl[l])
    print(f"ALT {os.path.basename(path)} N {N} STEPS {len(S) - 1} LADDER {lad} ALTVIOL {altv} TOWARDVIOL {tow} LFVIOL {lfv} MOVES {mvl} LFLIPS {lfl}")
