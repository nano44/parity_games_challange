#!/usr/bin/env python3
"""L-SI box 31 (docs/si/N5-SPC-box31.md §5): kill search in the SAME-PAIR CORE (frozen W-phases with D != {} and lambda_Xi(d) = lambda_W(d)
at every gate). SCORE=wch (default): 1000 * kill + floor(1000 * max WCH / (n - 1)), kill := WCH > n - 1 (FW-BF in the core) or R > n - 1;
SCORE=r: the same with R / (n - 1) (CONJECTURE R-LIN, DEAD; R = late adoptions, core/late.py); SCORE=rstar: R*_T / (n - 1) (note §6). Mutations, acceptance, saving as frz/fwclimb.py.
Usage: spclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUT"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "tord"))
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart, phases
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from fwphase import fwphases
from gates import basins
MODE = os.environ.get("SCORE", "wch")

def late(E, g, R, a, b, D, star=False):
    """late adoptions (star=False, ALLOWED+ notion, core/gp.py PLUS) or the number of TRANSITIONS with a late adoption* (star=True,
    blocked edges only, note §6)."""
    n = g.n; REF = set(); r = 0; rT = 0
    for k in range(a, b):
        Fk = basins(R[k]["wn"], D, n); G3k = {d for d in D if Fk[R[k]["t"][d]] != d and Fk[R[k]["sb"][d]] != d}; Is = {}
        for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): Is.setdefault(x, set()).add(z)
        r0 = r
        for x in range(n):
            if g.owner[x] != 0: continue
            if R[k + 1]["s"][x] != R[k]["s"][x] and (x, R[k + 1]["s"][x]) in REF: r += 1
            al = {R[k]["s"][x]} | Is.get(x, set()) | {w for w in g.succ[x] if Fk[w] == -1}
            if Fk[x] != -1 and Fk[x] in G3k: al |= {w for w in g.succ[x] if Fk[w] == Fk[x]}
            if star:
                kr = E.key(R[k]["W"][R[k]["s"][x]])
                al = {w for w in g.succ[x] if w in Is.get(x, set()) or w == R[k]["s"][x] or E.key(R[k]["W"][w]) <= kr}
            REF |= {(x, w) for w in g.succ[x] if w not in al}
        rT += r > r0
    return rT if star else r

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    n = g.n; best = 0.0; kill = 0
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D or not all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D): continue
            wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            v = wch
            if MODE == "r": v = late(E, g, R, a, b, D)
            if MODE == "rstar": v = late(E, g, R, a, b, D, star=True)
            if wch > n - 1 or v > n - 1: kill = 1
            best = max(best, v / (n - 1))
    return (1000 * kill + int(1000 * best), int(1000 * best), kill)

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
