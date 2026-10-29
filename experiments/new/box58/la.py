#!/usr/bin/env python3
"""L-NEW box 58 (successor 33): one-sided look-ahead variants of F (P-N5-SF §0), from the S3 start.
  F    : F(s) = arena optimum against sbar(s), S4c switch if that is s (box55/pcheck.F).
  LA1  : s1 = F(s); then re-optimise the SAME arena (edges {s(v)} + I_s(v)) against sbar(s1); S4c switch if the result is s.
  LAk  : iterate the re-optimisation k times (LA=k), keeping the arena of s.
Every step switches a non-empty set of improving edges of s (arena of s, or S4c), so every variant terminates (RESULTS R15 (c)).
Prints steps and the number of distinct sbar values. Usage: la.py GAME [K]   (K = 0 is F)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box55")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import pcheck
from n5x import load, Engine, dual, start_pair
g = load(sys.argv[1]); K = int(sys.argv[2]) if len(sys.argv) > 2 else 1; n = g.n; E = Engine(g)
LAG = int(os.environ.get("LAG", "0"))   # LAG=d: Odd fixed to sbar of the state d steps back (more stale than F)
HIST = []
def step(s):
    vs, sb = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None
    HIST.append(sb); opp = HIST[-1 - LAG] if len(HIST) > LAG else HIST[0]
    t = pcheck.arena_opt(g, s, opp, Is)
    for _ in range(K):
        t2 = pcheck.arena_opt(g, s, E.evaluate(tuple(t))[1], Is)
        if t2 == t: break
        t = t2
    if t == list(s):
        t = list(s)
        for v in {v for v, _ in Is}: t[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
    return t
s, _ = start_pair(g, E, Engine(dual(g)), None); s = [s[v] if g.owner[v] == 0 else -1 for v in range(n)]
k = 0; SB = set()
while True:
    SB.add(tuple(E.evaluate(tuple(s))[1])); nx = step(s)
    if nx is None: break
    s = nx; k += 1
print("LAG", LAG, "K", K, "steps", k, "distinct_sbar", len(SB))
