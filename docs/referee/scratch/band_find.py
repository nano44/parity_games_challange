#!/usr/bin/env python3
"""REFEREE succ. 9: random walk from a seed (neb_climb.mutate) keeping mutants with case-A c_w != o bases; saves the first mutant with an
R -> Rbar gate AT the base state at level >= rank(c_w(a)) (CONJECTURE BAND, gates form at the base). Usage: band_find.py seed.pg rngseed minutes out.pg"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, neb_probe as NP, neb_climb as NC
seed, rs, mins, out = sys.argv[1:5]
rng = random.Random(int(rs)); g = RE.parse(seed); end = time.time() + 60 * float(mins); i = 0
while time.time() < end:
    i += 1
    try: h = NC.mutate(g, rng)
    except AssertionError: continue
    c = Counter(); NP.EX.clear()
    try: NP.run(h, c, "bf")
    except (RuntimeError, AssertionError): continue
    if c[os.environ.get("BANDKEY", "BAND_gate_viol_at_base")]:
        NC.write(h, out); print("FOUND after", i, [e for e in NP.EX if e[1] == "BANDgate"][:4]); sys.exit(0)
    if c["BAND_runs"]: g = h
print("not found", i)
