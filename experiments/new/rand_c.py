#!/usr/bin/env python3
"""Gauntlet step 2 (random part) for N1 via anneal_c: COUNT harness/gen.py corpus games; each solution must equal Zielonka and
pass harness/verify.py. Writes out/rand_<seed>.csv (file,n,m,phases,even,odd,max_phase) and prints AGREE k/k.
Usage: rand_c.py DIR COUNT SEED [gen.py options]"""
import sys, os, subprocess, csv, time
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(HERE, "..", "harness"); sys.path.insert(0, H)
import pg, zielonka, verify
d, cnt, seed = sys.argv[1], int(sys.argv[2]), sys.argv[3]
subprocess.run([sys.executable, os.path.join(H, "gen.py"), "corpus", d, str(cnt), seed] + sys.argv[4:], check=True, capture_output=True)
files = sorted(f for f in os.listdir(d) if f.endswith(".pg")); ok = 0; t0 = time.time()
w = csv.writer(open(os.path.join(HERE, "out", f"rand_{seed}.csv"), "w")); w.writerow(["file", "n", "m", "phases", "even", "odd", "max_phase"])
for f in files:
    p = os.path.join(d, f); g = pg.read(p); sol = p + ".sol"
    out = subprocess.run([os.environ.get("ANNEAL_C", os.path.join(HERE, "anneal_c")), p, sol], capture_output=True, text=True).stdout
    kv = dict(t.split("=", 1) for t in out.split() if "=" in t and not t.startswith("nonzero"))
    text = open(sol).read(); win = pg.read_sol(text, g.n); st = verify.read_strategy(text, g.n)
    if win != zielonka.solve(g) or verify.check(g, win, st):
        print("MISMATCH", f); sys.exit(1)
    ok += 1; w.writerow([f, g.n, g.m, kv["phases"], kv["even_iters"], kv["odd_iters"], kv["max_phase"]]); os.unlink(sol)
print(f"AGREE {ok}/{len(files)} seed={seed} secs={time.time() - t0:.0f}")
