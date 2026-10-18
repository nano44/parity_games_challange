#!/usr/bin/env python3
"""N1 agreement test: anneal.solve on harness/gen.py corpus games vs Zielonka (harness/zielonka.py) and the strategy
check (harness/verify.py). Usage: anneal_random.py DIR COUNT SEED [--nmin A --nmax B]; prints AGREE k/k or the first mismatch."""
import sys, os, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(HERE, "..", "harness")
sys.path.insert(0, H); sys.path.insert(0, HERE)
import pg, zielonka, verify, anneal
anneal.COMPRESS = False   # N1 as specified: no priority merging
d, cnt, seed = sys.argv[1], int(sys.argv[2]), sys.argv[3]
extra = sys.argv[4:]
subprocess.run([sys.executable, os.path.join(H, "gen.py"), "corpus", d, str(cnt), seed] + extra, check=True, capture_output=True)
files = sorted(f for f in os.listdir(d) if f.endswith(".pg")); ok = 0; t0 = time.time(); maxj = maxe = 0
for f in files:
    g = pg.read(os.path.join(d, f))
    (win, strat), J, E, O, per = anneal.solve(g)
    zw = zielonka.solve(g); errs = verify.check(g, win, strat)
    if win != zw or errs:
        print("MISMATCH", f, "zielonka" if win != zw else "", errs[:2]); sys.exit(1)
    ok += 1; maxj = max(maxj, J); maxe = max(maxe, E)
print(f"AGREE {ok}/{len(files)} seed={seed} max_phases={maxj} max_even_iters={maxe} secs={time.time()-t0:.0f}")
