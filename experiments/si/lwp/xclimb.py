#!/usr/bin/env python3
"""L-SI box 26: climb on the GAP-DEPTH excess (lwp/gapdepth.py): score = EXW * (max gap - end-state depth) + (max gap - (n - 1)), i.e.
it grows the time an L-WAVE' gap spends beyond its end state's REL depth (what L-cuts add), not the raw gap. Reports kills (gap > n - 1)
separately. Mutations as grun/gclimb.py (runlin/growclimb.py). OBJ=KA: grow steps with a nontrivial terminal J_b-part (lwp/laststep.py), kill = K-ARENA / KSET / SEG-LAST failure.
OBJ=H4: grow segments where (H4'_rel) fails (lwp/laststep.py), kill = SEG-LAST or frontier failure.
OBJ=SL: climb on CONJECTURE SEG-LAST instead (lwp/seglast.py; third score component = failures, > 0 is a kill).
Usage: xclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from gapdepth import excess
from seglast import slscore
from laststep import h4score, kascore
EXW = float(os.environ.get("EXW", "2")); OBJ = os.environ.get("OBJ", "GD")   # OBJ=SL: SEG-LAST (score = 10 * failures + max(len - switchers))

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    if OBJ == "KA":                       # nontrivial terminal J_b-parts; third component = K-ARENA (+ KSET, KLAST, FRL) + SEG-LAST failures
        f, k, h = kascore(g, R); f2, _ = slscore(g, R); return (100 * (f + f2) + 3 * k + h, k, f + f2)
    if OBJ == "H4":                       # long segments where (H4'_rel) fails; third component = SEG-LAST + frontier failures
        f, h = h4score(g, R); f2, _ = slscore(g, R); return (100 * f2 + 10 * f + h, h, f + f2)
    if OBJ == "SL":
        f, x = slscore(g, R); return (10 * f + x, x, f)
    x, k = excess(g, R)
    return (EXW * x + k, x, k)

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = sc(g, mkst(g, st)); print("seed", cur, "n", g.n, flush=True); bestk = cur[2]
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res; s2 = sc(g2, mkst(g2, st2))
        if s2 is None or s2[0] < cur[0]: continue
        if s2[0] > cur[0]: print("step", it, "score", s2, "n", g2.n, flush=True); save(out, g2, st2)
        if s2[2] > bestk: bestk = s2[2]; save(out + "_k", g2, st2); print("step", it, "KILLSCORE", s2[2], "n", g2.n, flush=True)
        g, O, st, cur = g2, O2, st2, s2
    print("final", cur, "n", g.n, "best kill score", bestk)

if __name__ == "__main__":
    main()
