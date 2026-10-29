#!/usr/bin/env python3
"""L-SI box 30 (docs/si/N5-TORD-box30.md §10): kill search for the c1 = c2 epoch count. Over |D| = 1 frozen W-phases with
λ_Ξ(o) = λ_W(o): TC = transitions that change the trapped set S, and per-vertex entries / exits. Score = 1000 * kill + floor(1000 * max
TC / (n − 1)) + 10 * max per-vertex crossings; kill := TC > n − 1 (CONJECTURE TRAP-LIN) or a vertex enters 3 times (CONJECTURE X2) or
WCH > n − 1 (FW-BF). XCR=1: score 1000 * kill + 100 * crossings + 100 * TC/(n − 1) (aims at re-entries).
Mutations as frz/fwclimb.py. Usage: xclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUT"""
import sys, os, random
from collections import Counter
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, os.path.join(HERE, "..", "frz"))
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart, phases, avoid
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from fwphase import fwphases

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    n = g.n; best = 0.0; kill = 0; cr = 0
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D: continue
            wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            if wch > n - 1: kill = 1
            if len(D) != 1: continue
            o = next(iter(D))
            if R[a]["vs"][o][0] != R[a]["W"][o][0]: continue
            Sp = [set(range(n)) - avoid(R[t]["wn"], D, n) for t in range(a, b + 1)]
            tc = sum(1 for q in range(1, len(Sp)) if Sp[q] != Sp[q - 1]); ent = Counter()
            for q in range(1, len(Sp)):
                for v in Sp[q] - Sp[q - 1]: ent[v] += 1
            mx = max(ent.values(), default=0)
            if tc > n - 1 or mx >= 3: kill = 1
            best = max(best, tc / (n - 1)); cr = max(cr, mx)
    if os.environ.get("XCR") == "1": return (1000 * kill + 100 * cr + int(100 * best), int(1000 * best), kill, cr)
    return (1000 * kill + int(1000 * best) + 10 * cr, int(1000 * best), kill, cr)

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
