#!/usr/bin/env python3
"""L-RED R147: random search for one-W-run CN / XCN repetitions on n5b SPEC. Random games, random start (sigma, tau).
Reports the game maximising CNmax (one Even W-cycle node) and XCNmax (one Odd own Xi-cycle node) in one W-run, and writes them.
Usage: xsearch.py SEED GAMES NMIN NMAX OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import xcn
pg = xcn.pg
seed, G, a, b = map(int, sys.argv[1:5]); od = sys.argv[5]; os.makedirs(od, exist_ok=True)
rng = random.Random(seed); best = {"CNmax": (0,), "XCNmax": (0,), "CN": (0,), "XCN": (0,)}; tot = {"CN": 0, "XCN": 0, "runs": 0}
for i in range(G):
    n = rng.randint(a, b); pr = rng.sample(range(2 * n + 2), n); ow = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    g = pg.Game(pr, ow, succ)
    s0 = [rng.choice(succ[v]) if ow[v] == 0 else -1 for v in range(n)]; t0 = [rng.choice(succ[v]) if ow[v] == 1 else -1 for v in range(n)]
    try: tr, fb = xcn.trace(g, s0, t0, cap=400)
    except Exception: continue
    out = xcn.analyse(g, tr, fb); tot["runs"] += len(out)
    for r in out:
        tot["CN"] += r["CN"]; tot["XCN"] += r["XCN"]
        for key in best:
            if r[key] > best[key][0]:
                best[key] = (r[key], i, n, r["L"])
                pg.write(g, f"{od}/{key}_{seed}.pg")
                with open(f"{od}/{key}_{seed}.start", "w") as f:
                    f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 0) + "\n")
                    f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(n) if ow[v] == 1) + "\n")
print(f"XSEARCH seed {seed} games {G} n {a}-{b} tot {tot} best " + " ".join(f"{k}={v}" for k, v in best.items()))
