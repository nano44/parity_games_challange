#!/usr/bin/env python3
"""Cross-check anneal_c (C++) against anneal.py (no merging, Odd = Dantzig) on a harness/gen.py corpus: same phases, Even
and Odd switch counts, regions and strategies; the C++ solution also passes harness/verify.py and equals Zielonka.
Usage: xcheck_c.py DIR COUNT SEED [gen.py corpus options]"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(HERE, "..", "harness")
sys.path.insert(0, H); sys.path.insert(0, HERE)
import pg, zielonka, verify, anneal
anneal.COMPRESS = False
d, cnt, seed = sys.argv[1], int(sys.argv[2]), sys.argv[3]
subprocess.run([sys.executable, os.path.join(H, "gen.py"), "corpus", d, str(cnt), seed] + sys.argv[4:], check=True, capture_output=True)
files = sorted(f for f in os.listdir(d) if f.endswith(".pg")); bad = 0
for f in files:
    p = os.path.join(d, f); g = pg.read(p); sol = p + ".sol"
    out = subprocess.run([os.environ.get("ANNEAL_C", os.path.join(HERE, "anneal_c")), p, sol], capture_output=True, text=True).stdout
    kv = dict(t.split("=", 1) for t in out.split() if "=" in t and not t.startswith("nonzero"))
    (win, strat), J, E, O, per = anneal.solve(g)
    text = open(sol).read(); cw = pg.read_sol(text, g.n); cs = verify.read_strategy(text, g.n)
    ok = (int(kv["phases"]), int(kv["even_iters"]), int(kv["odd_iters"])) == (J, E, O) and cw == win and cs == strat \
         and cw == zielonka.solve(g) and not verify.check(g, cw, cs)
    if not ok:
        bad += 1; print("DIFF", f, out.strip()[:80], (J, E, O)); 
        if bad > 5: break
print(f"XCHECK-C {'PASS' if not bad else 'FAIL'} {len(files) - bad}/{len(files)} seed={seed}")
