#!/usr/bin/env python3
"""L-SI box 25 (successor 21): growth climb for CONJECTURE G-RUN (docs/si/N5-GRUN-box25.md). Score: max over fallback-free in-phase runs of
G (sigma-bar-changing transitions) minus CN*n (env CN, default 0.9); OBJ=SEG: the REL segment count of grun/relseg.py instead of G; OBJ=LW: the L-WAVE score max (gap - (n - 1)) of grun/lwave.py (> 0 is a kill). Mutations as runlin/growclimb.py. Usage: gclimb.py SEED.pg SEED.start|-
STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")):
    sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from trace import runs
CN = float(os.environ.get("CN", "0.9")); OBJ = os.environ.get("OBJ", "G")     # OBJ=SEG: grun/relseg.py's segment count
from relseg import segcount
from lwave import maxgap

def gmax(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    if OBJ == "SEG": return segcount(g, R)
    if OBJ == "LW": return maxgap(g, R) + CN * g.n          # score = max gap - (n - 1); CN*n cancels the score's penalty
    return max((sum(R[t]["sb"] != R[t + 1]["sb"] for t in range(a, b)) for a, b, i, j in runs(R)), default=0)

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    G = gmax(g, mkst(g, st)); cur = G - CN * g.n; best = (G / g.n, G, g.n); print("seed G", G, "n", g.n, flush=True)
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res; G2 = gmax(g2, mkst(g2, st2))
        if G2 is None or G2 - CN * g2.n < cur: continue
        if G2 - CN * g2.n > cur: print("step", it, "G", G2, "n", g2.n, "G/n %.3f" % (G2 / g2.n), flush=True)
        if G2 / g2.n > best[0]: best = (G2 / g2.n, G2, g2.n); save(out, g2, st2)
        g, O, st, cur = g2, O2, st2, G2 - CN * g2.n
    print("final best G/n %.3f G %d n %d" % best)

if __name__ == "__main__":
    main()
