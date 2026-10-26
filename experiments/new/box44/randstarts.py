#!/usr/bin/env python3
"""Box 44 DATA: re-run the lane's checkers (rstick, altcheck, epoch, sgcheck, fbf, crd) from RANDOM start pairs (every PROVED statement
in N5-FBF / N5-DELTA / P-N5-ACCEL / P-N5-FBK is start-free). Patches each module's start_pair to draw sigma0, tau0 uniformly from the
successor lists. Usage: randstarts.py STARTS SEED (--list FILE | --rand C LO HI GSEED)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO
from n5x import load
import rstick, altcheck, epoch, sgcheck, fbf, crd
MODS = [rstick, altcheck, epoch, sgcheck, fbf, crd]
RNG = random.Random(int(sys.argv[2]))
def rand_start(g, E, Ed, st=None):
    s = [RNG.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
    t = [RNG.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(g.n)]
    return s, t
for m in MODS: m.start_pair = rand_start
a = sys.argv[3:]
if a[0] == "--list":
    R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
else:
    cnt, lo, hi, gseed = map(int, a[1:5]); rng = random.Random(gseed)
    gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
K = int(sys.argv[1])
for g in gs:
    if g.n > 64: continue
    for _ in range(K):
        for m in MODS:
            try: m.check(g)
            except RecursionError: pass
V = {"rstick": ["RS_V", "SP_V", "XB_V"], "altcheck": ["ALT_V", "TIE_V"], "epoch": ["EPF_V", "FRZ_V"], "sgcheck": ["SG_V"],
     "fbf": ["CNO_V", "EXS_V", "FEX_V", "RED_V", "REDL_V"], "crd": ["LAMD", "CRD", "CMON", "FBLD", "FRD"]}
for m in MODS:
    nm = m.__name__; print(nm, {k: m.C[k] for k in V[nm]}, "| context:", {k: v for k, v in m.C.items() if k not in V[nm]})
