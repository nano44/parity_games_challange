#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §11: R1 events (L-RED R101's CONJECTURE R1-ZERO). In a phase, a
single-switch in-phase fallback at t' that re-switches an Even w already switched by an earlier single-switch in-phase fallback t of the phase.
For each event: the target y' = σ_{t'+1}(w); whether y' was itself switched (if Even) or changed σ̄ (if Odd) at some transition in (t, t');
whether Ξ(y') changed in (t, t']; and whether some fallback in (t, t') switched a vertex on y′'s honest play at t'.
Usage: r1scan.py (--random N NMIN NMAX SEED | files...)   (random games via experiments/si/si.py's generator, S3 start)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter
C = Counter(); EV = []

def play(nx, z):
    out, seen, x = [], set(), z
    while x not in seen: seen.add(x); out.append(x); x = nx[x]
    return out

def scan(g, st, nm):
    E, R = rows(g, st); n = g.n
    for i, j in phases(R):
        singles = []
        for t in range(i, j):
            if not R[t]["fb"]: continue
            sw = [v for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]]
            C["fb"] += 1
            if len(sw) != 1: continue
            C["fb_single"] += 1; w = sw[0]
            prev = [t0 for (t0, w0) in singles if w0 == w]
            if prev:
                t0 = prev[-1]; y = R[t + 1]["s"][w]
                chg = any((R[k]["s"][y] != R[k + 1]["s"][y]) if g.owner[y] == 0 else (R[k]["sb"][y] != R[k + 1]["sb"][y]) for k in range(t0 + 1, t))
                xich = any(R[k]["vs"][y] != R[k + 1]["vs"][y] for k in range(t0 + 1, t))
                pl = set(play(R[t]["nxt"], y))
                fbpl = any(R[k]["fb"] and any(R[k]["s"][v] != R[k + 1]["s"][v] for v in pl if g.owner[v] == 0) for k in range(t0 + 1, t))
                C["R1"] += 1; C["R1_target_changed"] += chg; C["R1_target_xi_changed"] += xich; C["R1_fb_on_target_play"] += fbpl
                EV.append((nm, (i, j), n, w, t0, t, y, chg, xich, fbpl))
            singles.append((t, w))

def rgame(rng, n):
    import pg
    prio = list(range(n)); rng.shuffle(prio); owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, min(3, n))))) for _ in range(n)]
    return pg.Game(prio, owner, succ)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        sys.path.insert(0, os.path.join(ROOT, "experiments", "harness")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new"))
        for k in range(N):
            g = rgame(rng, rng.randint(lo, hi))
            try: scan(g, None, f"rand{seed}_{k}"); C["games"] += 1
            except (RecursionError, RuntimeError, AssertionError): C["ERR"] += 1
    else:
        for f in a:
            try:
                g = load(f); sf = f[:-3] + ".start"
                if g.n > 200: continue
                scan(g, readstart(sf) if os.path.exists(sf) else None, os.path.relpath(f, ROOT)); C["games"] += 1
            except Exception: C["ERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for e in EV[:15]: print("R1", e)
