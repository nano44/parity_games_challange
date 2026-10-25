#!/usr/bin/env python3
"""Box 33 climb: raise K (transitions with a wake) per phase. Fitness = (max K in one phase, total K over the run, #finite dormant R -> R edges at checked steps).
Also flags any wake with Ω(λ_W(y)) odd and W unchanged at a and z (would refute Lemma WK (a)): saved as <out>_wk.pg.
Env THIRD=sparse: third key = -(number of edges) instead. Usage: kclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from wakes import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0), 0
    g = pg.Game(*G)
    try: ws, rows, o = wakes(g)
    except Exception: return (-1, 0, 0), 0
    per = {}
    for w in ws: per.setdefault(w["ph"], set()).add(w["k"])
    per = {p: len(v) for p, v in per.items()}
    wk = sum(1 for w in ws if w["cwodd"] == 1 and not w["wAZ"])
    E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; rr = 0
    for k in range(len(rows) - 2):
        if rows[k]["ph"] != rows[k + 1]["ph"] or rows[k + 1]["ph"] != rows[k + 2]["ph"] or rows[k]["fb"] or rows[k + 1]["fb"]: continue
        if not (rows[k]["R"] == rows[k + 1]["R"] == rows[k + 2]["R"]): continue
        L = relL(g, ev, rows, k)
        if L == -2: continue
        s = rows[k + 1]["s"]; Xi = ev[k + 1][0]; R = set(rows[k + 1]["R"]) | {o}
        for y, z in E.improving(tuple(s), Xi):
            l = lev(Xi[s[y]], Xi[z])
            if L < l < 99 and s[y] in R and z in R: rr += 1
    if os.environ.get("THIRD") == "sparse": rr = -sum(len(set(x)) for x in G[2])
    return (max(per.values()) if per else 0, sum(per.values()), rr), wk

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, _ = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, wk = fit(H)
        if wk: print(f"WK VIOLATION it {it}", flush=True); save(out + "_wk.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
