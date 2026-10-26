#!/usr/bin/env python3
"""Box 12 add-on: hill climb against CONJECTURE HON-FF (L-NEW 25 §1a). Individual = (game, start pair), mutations as climb.py.
Fitness (lexicographic): (gaps between consecutive W-honest states of a phase that contain an in-phase fallback strictly inside,
total such inside fallbacks, in-phase fallbacks at non-honest states after the phase's first W-honest state (shaping),
in-phase fallbacks at non-honest states anywhere (shaping), W-honest states counted once such fallbacks exist (shaping)). The fitness needs no LEV; every
individual with an inside-fallback gap is checked for HON-FF with honff.lev (exact or UNK), and a failure stops the climb and is saved.
Usage: honclimb.py N K SEED --secs S [--seed-pg FILE.pg[:START]] --out OUTPREFIX"""
import argparse
import random
import sys
import time
import os

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
import honff as H  # noqa: E402
import climb as CL  # noqa: E402
from census import pg, SpecSI, EVEN, ODD  # noqa: E402

CHECKED = {"gaps": 0, "unk": 0}


def fitness(g, s, t):
    try:
        states, fbs = C.run_states(g, s, t, cap=3000)
    except Exception:   # noqa: BLE001
        return (-1, 0, 0, 0, 0), None
    SG = SpecSI(g)
    A = [C.state_info(g, SG, a, b) for a, b in states]
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    gaps = infb = hon = fbh = fbn = 0; viol = None; i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        Hs = [k for k in range(i, j + 1) if A[k]["Xi"] == A[k]["W"]]
        fbn += sum(1 for k in range(i, j) if fbs[k] and A[k]["Xi"] != A[k]["W"])   # shaping: any in-phase fallback at a non-honest state
        if Hs:   # shaping: in-phase fallbacks at non-honest states after the phase's first honest state
            fbh += sum(1 for k in range(Hs[0] + 1, j) if fbs[k] and A[k]["Xi"] != A[k]["W"])
            hon += len(Hs) if fbh else 0
        for h, h2 in zip(Hs, Hs[1:]):
            ins = [k for k in range(h + 1, h2) if fbs[k]]
            if ins:
                gaps += 1; infb += len(ins)
                l0 = H.lev(g, SG, A[h]["Xi"], A[i]["lam"], states[i][1]); l1 = H.lev(g, SG, A[h2]["Xi"], A[i]["lam"], states[i][1])
                CHECKED["gaps"] += 1
                if l0 is None or l1 is None:
                    CHECKED["unk"] += 1
                elif l1 < min(l0 + 1, g.n - 1):
                    viol = f"HON-FF gap {h}->{h2} fallbacks {ins} LEV {l0}->{l1}"
        i = j + 1
    return (gaps, infb, fbh, fbn, hon), viol


def save(g, s, t, out):
    pg.write(g, out + ".pg")
    with open(out + ".start", "w") as fh:
        fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == EVEN) + "\n")
        fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == ODD) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("k", type=int); ap.add_argument("seed", type=int)
    ap.add_argument("--secs", type=float, default=600); ap.add_argument("--seed-pg"); ap.add_argument("--out", required=True)
    a = ap.parse_args(); rng = random.Random(a.seed)
    if a.seed_pg:
        path, _, st = a.seed_pg.partition(":")
        g0 = pg.read(path); s, t = C.full_start(g0, *C.read_start(st, g0)) if st else CL.s3(g0)
        n = max(a.n, g0.n)
        g = pg.Game(list(g0.prio) + [0] * (n - g0.n), list(g0.owner) + [0] * (n - g0.n), [list(x) for x in g0.succ] + [[v] for v in range(g0.n, n)])
        s = s + list(range(g0.n, n)); t = t + [-1] * (n - g0.n)
    else:
        g = C.rand_ckO(rng, a.n, a.k); s, t = CL.s3(g)
    cur, _ = fitness(g, s, t); best = (cur, g, s, t); t0 = time.time(); step = 0
    print(f"START fit {cur} n {g.n}", flush=True)
    while time.time() - t0 < a.secs:
        step += 1
        h, hs, ht = CL.mutate(g, s, t, rng)
        f, viol = fitness(h, hs, ht)
        if viol:
            print("VIOLATION during climb:", viol, flush=True); save(h, hs, ht, a.out + "_viol"); break
        if f >= cur:
            if f > best[0]:
                print(f"BEST step {step} fit {f} t {time.time() - t0:.0f}s", flush=True); best = (f, h, hs, ht)
            g, s, t, cur = h, hs, ht, f
    f, g, s, t = best
    save(g, s, t, a.out)
    print(f"END steps {step} best {f} n {g.n} inside-gaps checked {CHECKED['gaps']} UNK {CHECKED['unk']} -> {a.out}.pg", flush=True)


if __name__ == "__main__":
    main()
