#!/usr/bin/env python3
"""Box 32 adversarial climb against the PROVED statements of P-N5-LP / P-N5-SO (lcheck.py and socheck.py checks on every candidate).
Fitness = (#failures, max ρ per phase, max S_o per phase). Any failure is saved as <out>_viol.pg. Usage: lemclimb.py seed secs out seed.pg"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from mblock import *
from lcheck import check
from climb_fix import mutate
from cascclimb import save

FAILKEYS = ("U_FAIL", "U_FAIL_nu", "L_INF_FAIL", "HI_FAIL", "UL_FAIL", "GR_FAIL", "GR_LOSS_FAIL", "LP_FAIL_rel", "LP_FAIL_nu", "EPS_GT_SOrel",
            "RHO_GT_2f_SOrel_2X_K")


def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G); acc = {}
    try: check(g, acc, "c")
    except Exception: return (-1, 0, 0)
    fails = sum(acc.get(k, 0) for k in FAILKEYS)
    return (fails, acc.get("max_rho", (0,))[0], acc.get("max_So_rel", (0,))[0])

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh[0] > 0: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
