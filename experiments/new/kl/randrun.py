#!/usr/bin/env python3
"""N8a random corpus run (gauntlet step 2, random part): for every game of a gen.py corpus slice, run kl.solve with the given rule,
check strategies with harness/verify.py and regions against Oink zlk (pinned build; tl on zlk failure, labelled).
Usage: randrun.py DIR rule start end out.csv"""
import sys, os, csv, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg, verify
OINK = os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink")
OINK = os.path.normpath(os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink"))
d, rule, a, b, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
files = sorted(f for f in os.listdir(d) if f.endswith(".pg"))[a:b]
with open(out, "w") as fo:
    w = csv.writer(fo); w.writerow(["file", "n", "d", "rule", "iterations", "iterations_dual", "verify", "oink"])
    for f in files:
        p = os.path.join(d, f)
        g = pg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
        r = kl.solve(g, rule)
        e = verify.check(g, r["win"], r["strat"])
        ref, name = None, "none"
        for solver in ("--zlk", "--tl"):
            with tempfile.NamedTemporaryFile("r", suffix=".sol") as t:
                try:
                    subprocess.run([OINK, solver, p, t.name], capture_output=True, timeout=120, check=True)
                    ref = pg.read_sol(open(t.name).read(), g.n); name = solver[2:]; break
                except Exception:
                    continue
        w.writerow([f, g.n, r["d"], rule, r["it"], r["it_dual"], "verified" if not e else "FAIL:" + e[0],
                    ("OK-" + name) if ref == r["win"] else ("MISMATCH-" + name if ref is not None else "NOREF")])
        fo.flush()
