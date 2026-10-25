#!/usr/bin/env python3
"""Box 32 climb against CONJECTURE NO-WAKE (nowake.py). Fitness = (#NO-WAKE failures, #checked steps that carry a dormant gate edge of
level > L_{i-1}, #checked steps). Any failure is saved as <out>_viol.pg. Usage: nwclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from rises import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G)
    try:
        rows, o = rows_w(g)
    except Exception: return (-1, 0, 0)
    E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; fail = dorm = chk = 0; Ls = []
    for i in range(len(rows) - 1):
        Ls.append(None if rows[i]["ph"] != rows[i + 1]["ph"] else usedL(g, rows, ev, i)[0])
    for i in range(1, len(Ls)):
        if Ls[i] is None or Ls[i - 1] is None or rows[i - 1]["fb"] or rows[i]["fb"]: continue
        if not (rows[i - 1]["R"] == rows[i]["R"] == rows[i + 1]["R"]): continue
        chk += 1; a, c = rows[i], rows[i + 1]; Xi = ev[i][0]
        if any(lev(Xi[a["s"][y]], Xi[z]) > Ls[i - 1] for y, z in E.improving(tuple(a["s"]), Xi)): dorm += 1
        if any(g.owner[y] == 0 and a["s"][y] != c["s"][y] and lev(Xi[a["s"][y]], Xi[c["s"][y]]) > Ls[i - 1] for y in range(n)): fail += 1
    return (fail, dorm, chk)

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
