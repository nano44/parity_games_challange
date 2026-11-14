#!/usr/bin/env python3
"""Set d: the harness instances (experiments/harness, L-COMP). Writes the files and MANIFEST.tsv; run once.
 tiny300: the 300 tiny games (n <= 7) of experiments/harness/selftest.py step 2 (same generator calls, same order); the harness
   checks them against brute force (enumeration of Even's positional strategies: an oracle with no attractor code).
 regressions: experiments/harness/regressions/*.pg, copied byte for byte.
 bench: experiments/harness/bench/hkp_*.pg (Huth-Kuo-Piterman incompleteness witnesses, arXiv 1405.0386v2), copied byte for byte.
All agreement only (no growth reading)."""
import os, sys, glob, shutil, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.abspath(os.path.join(HERE, "..", "..", "..", "harness"))
sys.path.insert(0, H)
import gen, pg, zielonka
out = ["# set d: harness instances (experiments/harness at this commit): tiny300 = the 300 tiny games of selftest.py step 2 (written by mk_set.py, brute-force checked there);",
       "# regressions and bench (hkp) copied byte for byte. Agreement only.", "# family\tparam\tfile\tsha1\tkind\tref\tgen"]
rnd = gen.Rng("selftest-tiny"); bad = 0
for i in range(300):
    n = rnd.randint(1, 7)
    g = gen.random_game(n, rnd.randint(1, n + 1), 1, rnd.randint(1, 3), i, rnd.choice([0.3, 0.5, 0.7]), rnd.random() < 0.6 or n == 1)
    w, _ = zielonka.solve_with_strategy(g); bad += zielonka.brute_force(g) != w
    f = "tiny300/t%03d_n%d.pg" % (i, g.n); pg.write(g, os.path.join(HERE, f))
    out.append("tiny300\t%d\t%s\t%s\tagree\tzlk\t-" % (g.n, f, hashlib.sha1(open(os.path.join(HERE, f), "rb").read()).hexdigest()))
assert bad == 0, "brute force != Zielonka on a tiny game"
for fam, pat in (("regressions", "regressions/*.pg"), ("bench", "bench/hkp_*.pg")):
    for src in sorted(glob.glob(os.path.join(H, pat))):
        f = fam + "/" + os.path.basename(src); shutil.copyfile(src, os.path.join(HERE, f)); g = pg.read(src)
        out.append("%s\t%d\t%s\t%s\tagree\tzlk\t-" % (fam, g.n, f, hashlib.sha1(open(src, "rb").read()).hexdigest()))
open(os.path.join(HERE, "MANIFEST.tsv"), "w").write("\n".join(out) + "\n"); print("wrote", len(out) - 3, "instances; brute force = Zielonka on the 300 tiny games")
