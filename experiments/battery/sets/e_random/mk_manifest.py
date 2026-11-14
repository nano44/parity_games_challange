#!/usr/bin/env python3
"""Set e: 10,000 seeded random games (agreement only). Writes MANIFEST.tsv: one line per game with its generator arguments
(the seed is the last one) and the sha1 of the generated file. The generator is rngame_seeded.cpp = Oink's rngame.cpp @ 8fbf0a7
with a seed argument (Oink's own rngame seeds from std::random_device and cannot be reproduced). Run once; the battery
regenerates each game into its cache from these arguments and checks the sha1 pin.
Sizes n and games per size: SIZES. Per game j of a size: maxPrio = PRIOS[j % 7](n), degrees (min, max) = DEGS[(j // 7) % 8](n),
self-loops allowed iff (j // 56) % 2 == 0; seed = running index 1..10000."""
import os, sys, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); CACHE = os.path.join(HERE, "..", "..", ".cache")
SIZES = [(8, 1200), (12, 1200), (16, 1200), (24, 1200), (32, 1000), (48, 1000), (64, 900), (100, 800), (150, 600), (200, 500), (300, 250), (500, 150)]
PRIOS = [lambda n: 1, lambda n: 2, lambda n: 3, lambda n: max(4, n // 4), lambda n: n // 2, lambda n: n, lambda n: 2 * n]
DEGS = [lambda n: (1, 2), lambda n: (1, 3), lambda n: (2, 2), lambda n: (2, 3), lambda n: (1, 5), lambda n: (2, 6), lambda n: (3, 8), lambda n: (1, min(n, 16))]
exe = os.path.join(CACHE, "rngame_seeded"); os.makedirs(CACHE, exist_ok=True)
subprocess.run(["g++", "-O2", "-o", exe, os.path.join(HERE, "rngame_seeded.cpp")], check=True)
assert sum(c for _, c in SIZES) == 10000
out = ["# set e: 10,000 seeded random games, agreement only (no growth reading). Generator: rngame_seeded.cpp (this directory) = Oink rngame.cpp @ 8fbf0a7 + a seed argument.",
       "# gen = 'rngame' + the arguments of rngame_seeded: nNodes maxPrio minDeg maxDeg [x = no self-loops] seed. Written by mk_manifest.py; sha1 = sha1 of the generated file.",
       "# family\tparam\tfile\tsha1\tkind\tref\tgen"]
seed = 0
for n, count in SIZES:
    for j in range(count):
        seed += 1; p = PRIOS[j % 7](n); lo, hi = DEGS[(j // 7) % 8](n); sl = (j // 56) % 2 == 0
        hi = min(hi, n if sl else n - 1); lo = min(lo, hi)
        args = [str(n), str(p), str(lo), str(hi)] + ([] if sl else ["x"]) + [str(seed)]
        r = subprocess.run([exe] + args, capture_output=True, check=True)
        assert r.stdout.startswith(b"parity %d;" % n), r.stdout[:80]
        out.append("random\t%d\trn%05d_n%d_p%d_deg%d-%d_sl%d.pg\t%s\tagree\tzlk\t%s" % (n, seed, n, p, lo, hi, int(sl), hashlib.sha1(r.stdout).hexdigest(), "rngame " + " ".join(args)))
open(os.path.join(HERE, "MANIFEST.tsv"), "w").write("\n".join(out) + "\n")
print("wrote", len(out) - 3, "games")
