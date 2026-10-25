#!/usr/bin/env python3
"""Box 32 climb against NO-WAKE-RR (Lemma WAKE: the only possible wakes). Fitness = (#NO-WAKE failures (lcheck.py definition),
#finite dormant R -> R edges at U2/U3/U23 states, #finite dormant R -> R edges anywhere). Saves the best as <out>.pg and any failure as
<out>_viol.pg. Usage: rrclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from dormant import *
from lcheck import check
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G)
    try:
        acc = {}; check(g, acc, "c"); rows, o = rows_w(g)
    except Exception: return (-1, 0, 0)
    E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; nr = rr = 0
    for k in range(len(rows) - 2):
        if rows[k]["ph"] != rows[k + 1]["ph"] or rows[k + 1]["ph"] != rows[k + 2]["ph"] or rows[k]["fb"] or rows[k + 1]["fb"]: continue
        if not (rows[k]["R"] == rows[k + 1]["R"] == rows[k + 2]["R"]): continue
        L = relL(g, ev, rows, k)
        if L == -2: continue
        r = rows[k + 1]; s = r["s"]; Xi = ev[k + 1][0]; R = set(r["R"]) | {o}
        for y, z in E.improving(tuple(s), Xi):
            l = lev(Xi[s[y]], Xi[z])
            if L < l < 99 and s[y] in R and z in R:
                rr += 1; nr += not (r["rfX"] and r["rfW"])
    return (acc.get("NOWAKE_FAIL", 0), nr, rr)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh[0] > 0 and fh[0] > f[0]: print(f"VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
