#!/usr/bin/env python3
"""L-RED R184 DCYC: L-NEW box 135 dmerge.py (D' merge digraph, Theorem CASC-M) as a library, per STRETCH, for climbs.
FL runs as box 132 anchor.py; stretches as dmerge.py STRETCH=1 (sbar and every vertex's Xi cycle node constant over the gating states,
no W-cycle-node move; CN moves cut out and counted). Same D' edges as dmerge.py (pre-merge segments of equal-cycle-node option pairs,
self-edges allowed, plus W-key edges). Returns per stretch: (a, b, L, cyclic, height, selfl); and CNMOV per run.
Prints DCYC <game> n FL STRETCHES CYCST (cyclic stretches) LCYC (longest cyclic stretch) LACYC (longest acyclic) HMAX CASCVIOL SELFL
CNMOV CNMAX (max CN moves in one FL run) LFL (longest FL run). Usage: dcyc.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "r170"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
DM2 = os.environ.get("DM2") == "1"   # L-NEW box 136 dmerge2 z-world D'' with DOM cuts (C-STATIC-Xi + DOM); selfl = x on own segment
REFINE = os.environ.get("REFINE") == "1"   # D'': pairs (y, sigma_s(x)) only, x dropped from its own segments (R184 Lemma SELF-FREE)
def play(succ1, v):
    seq = []; pos = set()
    while v not in pos: pos.add(v); seq.append(v); v = succ1[v]
    return seq
def analyse(g, st=None, cap=10 ** 5):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); n, own, pr = g.n, g.owner, g.prio
    Wc, WV, EV = {}, {}, {}
    def wval(j):
        if j not in WV:
            tau = T[j]
            if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
            WV[j] = Wc[tau].evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        return WV[j]
    def ev(j):
        if j not in EV: EV[j] = E.evaluate(S[j])
        return EV[j]
    runs = []; cur = None
    for j in range(1, len(S)):
        if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
            if cur and cur[1] == j - 1: cur[1] = j
            else: cur = [j - 1, j]; runs.append(cur)
    out = []; cnr = []
    for a, b in runs:
        W0 = wval(a); CN0 = {v for v in range(n) if W0[v][2] == 0}
        def sig(j):
            vs, sb = ev(j); return (tuple(sb[o] for o in range(n) if own[o] == 1), tuple(vs[v][0] for v in range(n)))
        sts = []; s0 = a; cm = 0
        for j in range(a + 1, b + 1):
            if any(S[j][c] != S[j - 1][c] for c in CN0 if own[c] == 0):
                cm += 1
                if j - 1 > s0: sts.append((s0, j - 1))
                s0 = j; continue
            if sig(j - 1) != sig(s0):
                if j - 1 > s0: sts.append((s0, j - 1))
                s0 = j - 1
        if b > s0: sts.append((s0, b))
        cnr.append((a, b, cm))
        for a2, b2 in sts:
            tau = T[a2]; W = wval(a2); CN = {v for v in range(n) if W[v][2] == 0}
            Tx = {x: [y for y in g.succ[x] if (W[y][2] == W[x][2] - 1 and W[y][0] == W[x][0])] for x in range(n) if own[x] == 0 and x not in CN}
            adj = {x: set() for x in range(n) if own[x] == 0}; selfl = 0
            for s_ in range(a2, b2 + 1):
                vs, sb = ev(s_); succ1 = [S[s_][v] if own[v] == 0 else sb[v] for v in range(n)]
                if DM2:
                    for x, opts in Tx.items():
                        os_ = sorted(set(opts) | {S[s_][x]})
                        for z in os_:
                            sz = list(succ1); sz[x] = z
                            def cn(v):
                                seq = play(sz, v); nxt = sz[seq[-1]]; cyc_ = seq[seq.index(nxt):]
                                return max(cyc_, key=lambda u: E.rank[u]), seq
                            wz, pz = cn(z)
                            for y in os_:
                                if y == z: continue
                                wy, py = cn(y)
                                if wy != wz: continue
                                w = wz; yw = py[:py.index(w) + 1]; zw = pz[:pz.index(w) + 1]; c = 0
                                while c < min(len(yw), len(zw)) and yw[-1 - c] == zw[-1 - c]: c += 1
                                Yp, Zp = yw[:len(yw) - c], zw[:len(zw) - c]
                                def head(P):
                                    for i, v in enumerate(P):
                                        if own[v] == 0 and v != x: return P[:i + 1], P[i + 1:]
                                    return P, []
                                hy, ty = head(Yp); hz, tz = head(Zp); rw = E.rank[w]
                                Dh = [v for v in set(hy) ^ set(hz) if E.rank[v] > rw]
                                tails = [v for v in ty + tz if E.rank[v] > rw]
                                if Dh and (not tails or max(E.rank[v] for v in Dh) > max(E.rank[v] for v in tails)): continue
                                for v in Yp + Zp:
                                    if own[v] == 0 and v != x: adj[x].add(v)
                                    selfl += v == x
                for x, opts in ([] if DM2 else Tx.items()):
                    os_ = sorted(set(opts) | {S[s_][x]})
                    pairs = [(os_[i], os_[k]) for i in range(len(os_)) for k in range(i + 1, len(os_))]
                    if REFINE: pairs = [(y, S[s_][x]) for y in os_ if y != S[s_][x]]
                    for y, z in pairs:
                        if True:
                            if vs[y][0] != vs[z][0]: continue
                            py = play(succ1, y); pz = play(succ1, z); w = vs[y][0]
                            yw = py[:py.index(w) + 1]; zw = pz[:pz.index(w) + 1]; c = 0
                            while c < min(len(yw), len(zw)) and yw[-1 - c] == zw[-1 - c]: c += 1
                            for v in yw[:len(yw) - c] + zw[:len(zw) - c]:
                                if own[v] == 0:
                                    if REFINE and v == x: continue
                                    adj[x].add(v); selfl += v == x
                sW = [S[s_][v] if own[v] == 0 else tau[v] for v in range(n)]
                for x, opts in Tx.items():
                    for y in set(opts) | {S[s_][x]}:
                        v = y
                        while W[v][2] > 0:
                            if own[v] == 0 and v != x: adj[x].add(v)
                            v = sW[v]
            state = {}; h = {}; cyc = False
            for v0 in adj:
                if v0 in state: continue
                stk = [(v0, iter(adj[v0]))]; state[v0] = 1
                while stk and not cyc:
                    v, it = stk[-1]; nx = next(it, None)
                    if nx is None: state[v] = 2; h[v] = 1 + max((h[w] for w in adj[v]), default=-1); stk.pop()
                    elif state.get(nx) == 1: cyc = True
                    elif nx not in state: state[nx] = 1; stk.append((nx, iter(adj[nx])))
                if cyc: break
            if cyc and os.environ.get("SHOWCYC") == "1":
                import itertools
                # find one cycle by DFS with path
                def findcyc():
                    col = {}
                    for r in adj:
                        if r in col: continue
                        path = [r]; it = [iter(sorted(adj[r]))]; col[r] = 1
                        while path:
                            nx = next(it[-1], None)
                            if nx is None: col[path.pop()] = 2; it.pop(); continue
                            if col.get(nx) == 1: return path[path.index(nx):]
                            if nx not in col: col[nx] = 1; path.append(nx); it.append(iter(sorted(adj[nx])))
                print("CYCLE stretch", (a2, b2), findcyc(), file=sys.stderr)
            out.append((a2, b2, b2 - a2, cyc, None if cyc else max(h.values(), default=0), selfl))
    return dict(n=n, K=len(S) - 1, stretches=out, runs=cnr)
def summary(R):
    st = R["stretches"]; cy = [x for x in st if x[3]]; ac = [x for x in st if not x[3]]
    return dict(FL=sum(b - a for a, b, _ in R["runs"]), STRETCHES=len(st), CYCST=len(cy), LCYC=max((x[2] for x in cy), default=0),
                LACYC=max((x[2] for x in ac), default=0), HMAX=max((x[4] for x in ac), default=0),
                CASCVIOL=sum(1 for x in ac if x[2] > x[4] + 1), SELFL=sum(x[5] for x in st), CNMOV=sum(c for _, _, c in R["runs"]),
                CNMAX=max((c for _, _, c in R["runs"]), default=0), LFL=max((b - a for a, b, _ in R["runs"]), default=0))
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R = analyse(g, st); print(f"DCYC {os.path.basename(sys.argv[1])} n {R['n']} K {R['K']} " + " ".join(f"{k} {v}" for k, v in summary(R).items()))
