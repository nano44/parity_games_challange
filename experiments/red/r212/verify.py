#!/usr/bin/env python3
"""L-RED R212 VERIFY: independent re-computation of T_0..T_K of an E_m genome (fk.c text format) and replay of an optimal schedule.
 Engine A: one step = r187/ideal.py traj (r178 fastcyc values) on the genome with level 0 restricted to q_b (box 150 restrict).
 DP over engine A gives T_k for k = 0..K and an optimal schedule (start u, initial bit, segment lengths).
 Replay: each segment re-run with L-NEW box 150 Gen on the restricted genome (first p steps; the last segment runs to its end and must
 have exactly p steps). Prints T_k (engine A), the schedule, Gen replay result, and the expected values if given.
Usage: verify.py genome.txt K [expected T_0,..,T_K]  -> exit 1 on any mismatch."""
import sys, os, json, itertools
from functools import lru_cache
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187")]
import conv, ideal
ns = {"__file__": os.path.join(H, "ref", "box150", "check.py")}
exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns); Gen, restrict = ns["Gen"], ns["restrict"]
sys.setrecursionlimit(100000)
p, K = sys.argv[1], int(sys.argv[2]); exp = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None
G = conv.read_txt(p) if p.endswith(".txt") else json.load(open(p)); N = G["N"]; UP = list(range(2, N))
q = {}
for a, c in itertools.product(range(2), range(2)):
    q.setdefault(int(G["gate"][0][a] < G["gate"][1][c]), (a, c))
def full(u, b): return [q[b][0], q[b][1]] + list(u)
@lru_cache(None)
def nxt(u, b):
    Hh = restrict(G, [0, 1], full(u, b)); S, _ = ideal.traj(Hh, cap=1)
    return tuple(S[1][2:]) if len(S) > 1 else u
states = list(itertools.product(range(2), repeat=len(UP)))
@lru_cache(None)
def T(k, u, b):
    w = nxt(u, b); best = (1 + T(k, w, b)[0], "s") if w != u else (0, "e")
    if k > 0:
        x = T(k - 1, u, 1 - b)[0]
        if x > best[0]: best = (x, "f")
    return best
res = []; bad = 0
for k in range(K + 1):
    best = max(((T(k, u, b)[0], u, b) for u in states for b in (0, 1)))
    res.append(best[0])
    # extract schedule
    tk, u, b = best; kk = k; segs = []; cur = 0; start = (u, b)
    while True:
        v, how = T(kk, u, b)
        if how == "s": cur += 1; u = nxt(u, b)
        elif how == "f": segs.append((b, cur)); cur = 0; b = 1 - b; kk -= 1
        else: segs.append((b, cur)); break
    # Gen replay
    u, b0 = start; tot = 0; okr = True
    for i, (b, L) in enumerate(segs):
        Hh = restrict(G, [0, 1], full(u, b)); g = Gen(Hh); S, _ = g.run(Hh["start"])
        if i == len(segs) - 1 and len(S) - 1 != L: okr = False
        if len(S) - 1 < L: okr = False; break
        u = tuple(S[L][2:]); tot += L
    if tot != best[0]: okr = False
    if not okr: bad += 1
    print("k", k, "T_k", best[0], "start", "".join(map(str, start[0])), "b", start[1], "segments", [L for _, L in segs], "Gen-replay", "OK" if okr else "FAIL")
print("T_0..T_%d" % K, res, "expected", exp, "MATCH" if exp is None or exp == res else "MISMATCH")
if exp is not None and exp != res: bad += 1
sys.exit(1 if bad else 0)
