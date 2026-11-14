#!/usr/bin/env python3
"""L-COMP box 27: replay of a FREE0 (external level-0) witness with sim.py's literal R104 rules, independent of bfk.c.
Level-0 movers are set from outside at every step; upper movers: A-sets read at s_(t-1) (sim.chain / sim.better), keys under the
new state (literal gate tuples, lowest level first). b_0(s) = [key(mover 0) < key(mover 1)]. Longest run with <= k changes of b_0
over s_0..s_T, every step moving an upper mover, by memoised search over (state, flips left).
Usage: free0.py m 'witness line from bfk' [k]  -> prints the genome's T_k for that start and for its best start."""
import sys, json, functools
sys.setrecursionlimit(10000)
import sim

def genome(m, w):
    w = w.split(); NO = 4 * m
    def grab(tag, n): i = w.index(tag); return [int(v) for v in w[i + 1:i + 1 + n]]
    xt, rk, par = grab("xt", NO), grab("rank", NO), grab("par", NO)
    gate = grab("gate", 4 * (m + 1)); st = grab("start", 1)[0]; k = grab("k", 1)[0]; T = grab("T", 1)[0]
    N = 2 * (m + 1); lev = [x // 2 for x in range(N)]
    opts = [[[-1, -1, 2 * x + kk] for kk in range(2)] for x in range(2)]
    br = list(range(4)) + [4 + r for r in rk]; bp = [0] * 4 + par
    for x in range(2, N):
        opts.append([[2 * (lev[x] - 1) + kk, xt[2 * (x - 2) + kk], 2 * x + kk] for kk in range(2)])
    G = {"N": N, "lev": lev, "opts": opts, "gate": [[gate[2 * x], gate[2 * x + 1]] for x in range(N)], "br": br, "bp": bp,
         "start": [(st >> x) & 1 for x in range(N)]}
    return G, k, T

def step_forced(G, s, c):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    ns = list(s); key = [None] * N
    for x in sorted(range(N), key=lambda v: lev[v]):
        if lev[x] == 0: ns[x] = c[x]; key[x] = (gate[x][c[x]],); continue
        cur = sim.chain(G, s, x, s[x])
        A = [k for k in range(2) if k == s[x] or sim.better(G, sim.chain(G, s, x, k), cur)]
        best = min(((key[opts[x][k][0]] + (gate[x][k],), k) for k in A))
        key[x], ns[x] = best
    return tuple(ns)

def longest(G, kmax):
    N = G["N"]
    b0 = lambda s: gate0(G, s)
    @functools.lru_cache(None)
    def Lr(s, r, depth=0):
        if depth > 200: raise RuntimeError("cycle?")
        best = 0
        for c in [(a, b) for a in range(2) for b in range(2)]:
            ns = step_forced(G, s, c)
            if ns[2:] == s[2:]: continue
            fl = int(b0(ns) != b0(s))
            if fl > r: continue
            best = max(best, 1 + Lr(ns, r - fl, depth + 1))
        return best
    return Lr

def gate0(G, s): return G["gate"][0][s[0]] < G["gate"][1][s[1]]

if __name__ == "__main__":
    m = int(sys.argv[1]); G, k, T = genome(m, sys.argv[2])
    if len(sys.argv) > 3: k = int(sys.argv[3])
    Lr = longest(G, k); s0 = tuple(G["start"])
    allb = max(Lr(tuple((s >> x) & 1 for x in range(G["N"])), k) for s in range(1 << G["N"]))
    print(f"m {m} k {k}: C witness T {T}; python replay from its start {Lr(s0, k)}; best start {allb}")
