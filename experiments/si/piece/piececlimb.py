#!/usr/bin/env python3
"""L-SI box 25 (successor 21): kill search for CONJECTURE PIECE (docs/si/N5-PIECE-box25.md §3). Score of a game: max over its
sigma-bar-constant pieces of (length - CN*(n - 1)) (env CN, default 1), with env ONLYOUT=1 restricted to pieces OUTSIDE Theorem STATIC-DEPTH' ((H3') or (H4')
fails; piece/sdprime.py). Mutations as runlin/growclimb.py (box43 climb.mutate + CLONE). Keeps a move if the score does not drop.
Usage: piececlimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in (HERE, os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")):
    sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from pieceh import pieces, cyc
from sdprime import depths
ONLYOUT = os.environ.get("ONLYOUT") == "1"; CN = float(os.environ.get("CN", "1"))   # score uses CN*(n - 1)

def outside(g, R, a, b):
    n = g.n; B = R[b]; cwb, chb = cyc(B["wn"], n), cyc(B["nxt"], n)
    if not all(cwb <= cyc(R[t]["wn"], n) and chb <= cyc(R[t]["nxt"], n) for t in range(a, b + 1)): return True
    try: depths(g, B, {v for c in cwb for v in c}, {v for c in chb for v in c}); return False
    except (ValueError, RecursionError): return True

def score(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    best = -10 ** 6
    for a, b in pieces(R):
        if b - a - CN * (g.n - 1) <= best: continue
        if ONLYOUT and not outside(g, R, a, b): continue
        best = b - a - CN * (g.n - 1)
    return best

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = score(g, mkst(g, st)); print("seed score", cur, "n", g.n, flush=True)
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res
        sc = score(g2, mkst(g2, st2))
        if sc is None or sc < cur: continue
        if sc > cur:
            print("step", it, "score", sc, "n", g2.n, flush=True); save(out, g2, st2)
            if sc + (CN - 1) * (g2.n - 1) > 0: print("PIECE KILL CANDIDATE", out, flush=True)
        g, O, st, cur = g2, O2, st2, sc
    print("final score", cur, "n", g.n)

if __name__ == "__main__":
    main()
