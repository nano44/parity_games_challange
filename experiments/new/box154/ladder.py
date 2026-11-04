#!/usr/bin/env python3
"""L-NEW box 154: the explicit Xi-ladder family of P-IDEAL-CUBE Theorem LADDER-LP, and a check of its long improving path.
Genome L_K (K >= 1 pairs, N = 2K movers, all at level 0, degree 2): pair i = (u_i, v_i) = movers (2i, 2i+1), i = 0..K-1, pair 0 the
deepest. Pair 0: both options of u_0 and v_0 go to the exit X. Pair i >= 1: option 0 -> u_(i-1), option 1 -> v_(i-1). All parities
even, so a higher rank is better. Ranks (distinct): pair 0 gets the top four, w_u < w_v < b_u < b_v (u_0: option 0 = w_u, option 1
= b_u; v_0: option 0 = w_v, option 1 = b_v); pair i >= 1 gets the next four below pair i-1's, ordered u_i option 0 < u_i option 1 <
v_i option 0 < v_i option 1 (so v_i beats u_i whenever both sit on the same option). Start: u_0, v_0 on option 0; every u_i, v_i
(i >= 1) on option 1 (-> v_(i-1)). The path DFS(0) of the proof: at pair 0 switch u_0 then v_0; after every switch at pair i that
flips B_i := the better of (u_i, v_i), run «switch u_(i+1), recurse, switch v_(i+1), recurse» at pair i+1.
Checks: every switch of the path is improving (to the strictly better face) under box150's simulator values; path length
2^(K+1) - 2; the DP longest path from the start (K <= 7) is >= that; B_i flips 2^(i+1) times. Usage: ladder.py KMAX"""
import sys, os, json, functools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def genome(K):
    N = 2 * K; M = 2 * N; opts = []; br = [0] * M; top = M
    for i in range(K):
        for side in (0, 1):
            x = 2 * i + side; t = (-1, -1) if i == 0 else (2 * (i - 1), 2 * (i - 1) + 1)
            opts.append([[-1, t[0], 2 * x], [-1, t[1], 2 * x + 1]])
    for i in range(K):
        r = [top - 4, top - 3, top - 2, top - 1]; top -= 4; u, v = 2 * i, 2 * i + 1
        if i == 0: br[2 * u], br[2 * v], br[2 * u + 1], br[2 * v + 1] = r      # w_u < w_v < b_u < b_v
        else: br[2 * u], br[2 * u + 1], br[2 * v], br[2 * v + 1] = r           # u0 < u1 < v0 < v1
    start = [0, 0] + [1] * (N - 2)
    return {"N": N, "lev": [0] * N, "opts": opts, "gate": [[2 * x, 2 * x + 1] for x in range(N)], "br": br, "bp": [0] * M,
            "start": start, "xorder": list(range(N - 1, -1, -1))}
def check(K):
    G = genome(K); g = Gen(G); s = list(G["start"]); n = 0; bad = 0; flips = [0] * K
    C = lambda s, x: 1 if g.face(s, x, 1) > g.face(s, x, 0) else 0
    B = lambda s, i: 0 if g.face(s, 2 * i, s[2 * i]) > g.face(s, 2 * i + 1, s[2 * i + 1]) else 1
    def switch(x):
        nonlocal n, bad
        i = x // 2; b0 = B(s, i)
        if C(s, x) == s[x]: bad += 1
        s[x] = C(s, x); n += 1
        if B(s, i) != b0:
            flips[i] += 1
            if i + 1 < K: switch(2 * (i + 1)); switch(2 * (i + 1) + 1)
    switch(0); switch(1)
    lp = None
    if K <= 7:
        D2 = list(range(2 * K))
        @functools.lru_cache(maxsize=None)
        def LP(bits):
            st = list(bits); best = 0
            for x in D2:
                c = C(st, x)
                if c != st[x]: nb = list(bits); nb[x] = c; best = max(best, 1 + LP(tuple(nb)))
            return best
        lp = LP(tuple(G["start"]))
    T = len(g.run(G["start"])[0]) - 1
    return n, bad, flips, lp, T
if __name__ == "__main__":
    for K in range(1, int(sys.argv[1]) + 1):
        n, bad, flips, lp, T = check(K)
        ok = n == 2 ** (K + 1) - 2 and bad == 0 and flips == [2 ** (i + 1) for i in range(K)] and (lp is None or lp >= n)
        print(f"LADDER K {K} N {2 * K} path {n} = 2^(K+1)-2 {n == 2 ** (K + 1) - 2} nonimproving {bad} flips {flips} DP_longest {lp} ideal_T {T} {'OK' if ok else 'FAIL'}")
