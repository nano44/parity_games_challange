#!/usr/bin/env python3
"""L-SI box 29 (docs/si/N5-FRZ-box29.md): kill search for CONJECTURE FW-BF (a frozen W-phase has <= n - 1 W-changing transitions) and
FW-LEN (< n + m transitions). Score: 1000 * (kill) + floor(1000 * max over frozen W-phases with |D| >= 1 of WCH / (n - 1)) (+ L / (n + m)
as a tie-break); third component = kill indicator. Mutations and acceptance as chg/cclimb.py (lay/wclimb.py's climb.mutate, growclimb.clone).
Usage: fwclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUT"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, HERE)
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart, phases
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from fwphase import fwphases

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    n = g.n; m = sum(len(set(g.succ[v])) for v in range(n)); best = 0.0; kill = 0; tie = 0.0
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            if not any(g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u] for u in range(n)): continue
            wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            if wch > n - 1 or b - a >= n + m: kill = 1
            best = max(best, wch / (n - 1)); tie = max(tie, (b - a) / (n + m))
    return (1000 * kill + int(1000 * best) + int(100 * tie), int(1000 * best), kill)

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
