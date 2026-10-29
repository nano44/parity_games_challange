#!/usr/bin/env python3
"""L-NEW box 62: is F (N5-SF's Even map, box55/pcheck.F) equal to I^glo (box56/hybrid.py's glo: switch-all to the optimum of the arena
{sigma(v)} + I_sigma(v) against Odd's TRUE best replies) step by step from the S3 start? Prints the step counts and the first divergence.
Usage: fglo.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box55")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import pcheck, pg
from n5x import load, Engine, dual, start_pair
g = load(sys.argv[1]); n = g.n; E = Engine(g)
def glo(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None
    keep = [sorted({s[v]} | {w for (x, w) in Is if x == v}) if g.owner[v] == 0 else sorted(set(g.succ[v])) for v in range(n)]
    EH = Engine(pg.Game(list(g.prio), list(g.owner), keep)); t = tuple(s)
    while True:
        val, _ = EH.evaluate(t); imp = EH.improving(t, val)
        if not imp: return list(t)
        t = EH.rule_switch_all(t, val, imp, None)
s0, _ = start_pair(g, E, Engine(dual(g)), None); s0 = [s0[v] if g.owner[v] == 0 else -1 for v in range(n)]
def run(step):
    s = list(s0); out = [tuple(s)]
    while True:
        nx = step(s)
        if nx is None or list(nx) == s: return out
        s = list(nx); out.append(tuple(s))
A, B = run(lambda s: pcheck.F(g, E, s)), run(glo)
div = next((k for k in range(min(len(A), len(B))) if A[k] != B[k]), None)
print(f"FGLO {os.path.basename(sys.argv[1])} F_steps {len(A) - 1} GLO_steps {len(B) - 1} first_divergence {div} {'EQUAL' if A == B else 'DIFFER'}")
