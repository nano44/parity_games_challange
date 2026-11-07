#!/usr/bin/env python3
"""Membership checklist for candidate kill instances (docs/lower/L3-families.md §9; kill/README.md). One line per condition:
(i) IDEAL genome per R104 (every option has a W-target of level lev-1 (none at level 0), a Xi-target (mover or X), a rank, a
    parity, a gate; a start); (ii) L^R_d per R110 (movers 2l, 2l+1 on level l, all of degree 2, no other movers, option k of a
    level-l>=1 mover W-points to 2(l-1)+k); (iii) ISO (reported only: R110 defines ISO as a separate property, not part of L^R_d);
    (iv) Xi-graph acyclic; (v) ranks a permutation of 0..M-1 (distinct), gates distinct, parities in {0,1}, lev[x] = x//2;
    (vi) start: one option index in {0,1} per mover; (vii) moves(z) = #{t in [1,T] : s_t(z) != s_(t-1)(z)} for the named z, z a
    Xi-target of level >= 1, from the stored start, by sim.py and by box150 Gen (trunk experiments/new/box150/check.py).
Usage: memcheck.py file.json mover"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from sim import run, moves
P0 = os.path.join(H, "..", "..", "new", "box150", "check.py")
ns = {"__file__": os.path.abspath(P0), "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns)
G = json.load(open(sys.argv[1])); z = int(sys.argv[2]); N = G["N"]; d = N // 2; opts = G["opts"]; M = sum(len(o) for o in opts)
ok = lambda b: "PASS" if b else "FAIL"
c1 = all(len(o) >= 1 for o in opts) and all((o[0] == -1) if G["lev"][x] == 0 else (o[0] >= 0 and G["lev"][o[0]] == G["lev"][x] - 1)
         for x in range(N) for o in opts[x]) and all(o[1] == -1 or 0 <= o[1] < N for x in range(N) for o in opts[x]) and len(G["start"]) == N
print("(i)   IDEAL genome (R104): W-targets one level down / none at level 0, Xi-targets movers or X, start present:", ok(c1))
c2 = N % 2 == 0 and all(len(opts[x]) == 2 for x in range(N)) and all(opts[x][k][0] == (2 * (x // 2 - 1) + k if x >= 2 else -1) for x in range(N) for k in range(2))
print("(ii)  L^R_d (R110): 2d movers, movers 2l,2l+1 on level l, all degree 2, option k W-points to 2(l-1)+k:", ok(c2), "d =", d)
iso = all(o[1] not in (0, 1) for x in range(N) for o in opts[x])
print("(iii) ISO (R110: no option has Xi-target 0 or 1) - not required by L^R_d; this instance:", "ISO" if iso else "not ISO")
col = [0] * N
def dfs(v):
    col[v] = 1
    for o in opts[v]:
        w = o[1]
        if w >= 0 and (col[w] == 1 or (col[w] == 0 and not dfs(w))): return False
    col[v] = 2; return True
c4 = all(col[v] or dfs(v) for v in range(N))
print("(iv)  Xi-graph acyclic (edge x -> xt(x,k) for every option with a mover as Xi-target):", ok(c4))
ms = [o[2] for x in range(N) for o in opts[x]]
c5 = sorted(G["br"][m] for m in ms) == list(range(M)) and len({g for x in range(N) for g in G["gate"][x]}) == M and \
     set(G["bp"][m] for m in ms) <= {0, 1} and G["lev"] == [x // 2 for x in range(N)] and len(set(ms)) == M
print("(v)   ranks a permutation of 0..M-1, gates distinct, parities 0/1, lev[x] = x//2, one beta per option:", ok(c5), "M =", M)
c6 = all(G["start"][x] in range(len(opts[x])) for x in range(N))
print("(vi)  start: an option index per mover (R104: 'and a start'; every state is a legal start):", ok(c6))
S = run(G, G["start"]); m = moves(S, N); S2 = ns["Gen"](G).run(G["start"])[0]
Z = {o[1] for x in range(N) for o in opts[x]} - {-1}
c7 = z in Z and G["lev"][z] >= 1 and [tuple(s) for s in S] == [tuple(s) for s in S2]
print(f"(vii) moves(z) per mover per run (P-IDEAL-MOVES §0 binder): z = {z}, level {G['lev'][z]}, Xi-target: {z in Z};",
      f"moves = {m[z]} (sim.py) = {sum(1 for t in range(1, len(S2)) if S2[t][z] != S2[t-1][z])} (box150 Gen); T = {len(S) - 1}; 2d = {2 * d}:",
      ok(c7 and m[z] > 2 * d))
print("ALL", ok(c1 and c2 and c4 and c5 and c6 and c7 and m[z] > 2 * d))
