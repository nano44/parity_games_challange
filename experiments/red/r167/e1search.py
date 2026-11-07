#!/usr/bin/env python3
"""L-RED successor 39 (R169): random search over the markers OUTSIDE a srz3c model (E1: MU_1, MU_2, GM_2, BE_1, BE_2; the t2 marker T2;
E3 BA3 / BBB as given by the model) for a mk169.py build: objective (E3 switches in the longest W-run, |F|). Keys on the model's rank
scale (lo..hi), parity free, or inert. Usage: e1search.py MODEL.json K m2 m3 N seed"""
import sys, os, json, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn
M = json.load(open(sys.argv[1])); K, m2, m3, N, seed = map(int, sys.argv[2:7]); rng = random.Random(seed)
ranks = [v for k, v in M["rank"].items() if M["present"][k] and k not in ("T", "QS", "T2S")]; lo, hi = min(ranks) - 50, max(ranks) + 50
best = (-1, 0); td = os.environ.get("TMPD", "/tmp")
for it in range(N):
    e1 = []
    for nm in ("MU_1", "MU_2", "GM_2", "BE_1", "BE_2", "T2"):
        if rng.random() < 0.8: e1.append(f"{nm}:{rng.uniform(lo, hi):.1f}:{rng.randrange(2)}")
    env = dict(os.environ, E1=",".join(e1))
    subprocess.run([sys.executable, os.path.join(HERE, "mk169.py"), sys.argv[1], str(K), str(m2), str(m3), f"{td}/e.pg", f"{td}/e.start"], env=env, check=True, capture_output=True)
    g = xcn.pg.read(f"{td}/e.pg"); s0, t0 = xcn.n5b.read_start(f"{td}/e.start", g)
    lab = [l.split('"')[1] for l in open(f"{td}/e.pg") if '"' in l]
    try: tr, fb = xcn.trace(g, s0, t0, cap=20000); runs, W = xcn.wruns(g, tr, fb)
    except Exception: continue
    F = max(runs, key=len); E3 = [v for v in range(g.n) if lab[v].startswith("rrr")]
    e3 = sum(1 for k in F[:-1] for v in E3 if tr[k][0][v] != tr[k + 1][0][v]); sc = (e3, len(F) - 1)
    if sc > best: best = sc; print(it, "E3", e3, "|F|", len(F) - 1, "iters", len(tr) - 1, "E1", ",".join(e1), flush=True)
print("BEST", best)
