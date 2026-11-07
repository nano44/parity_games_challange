#!/usr/bin/env python3
"""L-RED R199 BUILD: from prescribed move times of every mover of a width-2 ladder (option k of a level-l >= 1 mover has W-target
2(l-1)+k; optional extra movers «helpers» with their own levels and W-targets, nobody W-points at them), choose gates and start
bits level by level so that every move goes to the key-preferred option (W side of r199/req.py), and output a req.py target.
At width 2 / degree 2 the gates matter only through: level 0, the order of the 4 level-0 gates; level l >= 1, the two bits
[g(u_l, k) < g(v_l, k)], k = 0, 1 (Lemma K3 of R198). Exhaustive over those bits; start of a moving mover = opposite of its first
move target; non-moving movers: both starts tried (greedy, bottom-up). Usage as a library: build(L, d, moves, helpers) ->
(target dict or None, report)."""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ
def states_of(N, start, moves, L):
    S = [tuple(start)]; cur = list(start)
    for t in range(1, L + 1):
        for v in range(N):
            if t in moves.get(v, ()): cur[v] ^= 1
        S.append(tuple(cur))
    return S
def build(L, d, moves, helpers=(), want_all=False):
    """moves: {mover: set of steps}; helpers: list of (lev, [W0, W1]) appended after the 2d ladder movers."""
    N0 = 2 * d; lev = [v // 2 for v in range(N0)] + [h[0] for h in helpers]; N = len(lev)
    WT = [[-1, -1] if v // 2 == 0 else [2 * (v // 2 - 1), 2 * (v // 2 - 1) + 1] for v in range(N0)] + [list(h[1]) for h in helpers]
    M = 2 * N
    # gate numbering: levels assigned blocks; within a level choose relative orders
    def gates_for(choice):
        g = [[0, 0] for _ in range(N)]; nxt = 0
        for l in range(d):
            vs = [v for v in range(N) if lev[v] == l]
            if l == 0:
                perm = choice[0]   # order of the 4 faces of u0, v0
                fl = [(0, 0), (0, 1), (1, 0), (1, 1)]
                for rank, i in enumerate(perm): v, k = fl[i]; g[v][k] = nxt + rank
                nxt += 4
                for v in vs:
                    if v >= 2: g[v] = [nxt, nxt + 1]; nxt += 2
            else:
                b0, b1 = choice[l]; u, w = 2 * l, 2 * l + 1
                g[u][0], g[w][0] = (nxt, nxt + 1) if b0 else (nxt + 1, nxt); nxt += 2
                g[u][1], g[w][1] = (nxt, nxt + 1) if b1 else (nxt + 1, nxt); nxt += 2
                for v in vs:
                    if v >= N0: g[v] = [nxt, nxt + 1]; nxt += 2
        return g
    perms0 = [p for p in itertools.permutations(range(4)) if p.index(0) < p.index(1) and p.index(2) < p.index(3)]   # g(v,0) < g(v,1)
    best = None
    for p0 in perms0:
        for bits in itertools.product([(0, 0), (0, 1), (1, 0), (1, 1)], repeat=d - 1):
            choice = [p0] + list(bits); gate = gates_for(choice)
            # starts bottom-up: start of a mover = opposite of KP at its first move (KP depends only on lower levels)
            start = [0] * N
            for l in range(d):
                for v in range(N):
                    if lev[v] != l: continue
                    if moves.get(v):
                        t1 = min(moves[v]); S = states_of(N, start, moves, t1)
                        key = RQ.keys(lev, WT, gate, S[t1]); start[v] = 1 - RQ.kp(lev, WT, gate, key, v)
            S = states_of(N, start, moves, L)
            bad, rq = RQ.requirements(lev, WT, gate, S)
            K = [RQ.keys(lev, WT, gate, s) for s in S]
            F = [sum(1 for t in range(1, L + 1) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(d)]
            sc = (len(bad), -sum(F))
            if best is None or sc < best[0]:
                best = (sc, dict(movers=[[lev[v], WT[v]] for v in range(N)], states=[list(s) for s in S], gate=gate, F=F, bad=bad, nreq=len(rq)))
    return best[1]
if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    T = build(spec["L"], spec["d"], {int(k): set(v) for k, v in spec["moves"].items()}, [tuple(h) for h in spec.get("helpers", [])])
    print("BUILD F", T["F"], "W-violations", T["bad"], "requirements", T["nreq"]); json.dump(T, open(sys.argv[2], "w"))
