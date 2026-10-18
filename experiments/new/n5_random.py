#!/usr/bin/env python3
"""N5 agreement test on harness/gen.py corpus games: regions vs Zielonka (harness/zielonka.py) and harness/verify.py on both
strategies, in-process. Usage: n5_random.py DIR COUNT SEED [--nmin A --nmax B]  -> 'AGREE k/k max_iter=.. fallbacks=..' or the
first mismatch (file name)."""
import sys, os, subprocess, glob
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(HERE, "..", "harness"); sys.path.insert(0, H); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
d, cnt, seed = sys.argv[1], sys.argv[2], sys.argv[3]
subprocess.run([sys.executable, os.path.join(H, "gen.py"), "corpus", d, cnt, seed] + sys.argv[4:], check=True, capture_output=True)
files = sorted(glob.glob(os.path.join(d, "*.pg"))); ok = 0; mx = 0; fbs = 0
for f in files:
    g = pg.read(f); it, fb, win, ws, _ = n5.run(g)
    mx = max(mx, it); fbs += fb
    e = verify.check(g, win, list(ws))
    if win != zielonka.solve(g) or e: print("MISMATCH", f, it, e[:1]); sys.exit(1)
    ok += 1
print(f"AGREE {ok}/{len(files)} max_iter={mx} fallbacks={fbs}")
