#!/usr/bin/env python3
"""Scale a bitgadget genome over N: n, sha1, lock, fallbacks, iterations (n5.run, unmodified), check. Usage: bg_scale.py genome.json NMAX"""
import sys, os, json, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import bitgadget as B, n5, zielonka, verify, pg
gn = json.load(open(sys.argv[1]))
for N in range(2, int(sys.argv[2]) + 1):
    g = B.build(N, gn); t0 = time.time(); run, fb, it = B.lockrun(g); i2, f2, win, ws, _ = n5.run(g, cap=10**6); assert (i2, f2) == (it, fb)
    ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
    print(N, g.n, hashlib.sha1(pg.dumps(g).encode()).hexdigest()[:12], "lock", run, "fallbacks", fb, "iterations", it, "OK" if ok else "FAIL", f"{time.time()-t0:.1f}s", flush=True)
