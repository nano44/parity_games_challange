#!/usr/bin/env python3
"""Box 33 climb against CONJECTURE ORX / EXIT-R (orx.py). Fitness = (#ORX failures + #EXIT-R failures, max O-rises in one fallback-free
segment, total O-rises). Saves the best as <out>.pg and any failure as <out>_viol.pg. Env MODE=rel: fitness (failures, min(ε, S4a exit releases), ε + releases). Usage: orxclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from orx import *
from climb_fix import mutate
from cascclimb import save

def segmax(g):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    prev = None; seg = 0; c = {}
    for k in range(len(Ls)):
        if Ls[k] is None or rows[k]["fb"]: seg += 1
        if Ls[k] is None: prev = None; continue
        if Ls[k] == -2: continue
        if prev is not None and Ls[k] > Ls[prev] and not any(rows[j]["fb"] for j in range(prev, k + 1)):
            sb0, sb1, X0 = ev[k][1], ev[k + 1][1], ev[k][0]
            if sb0[o] != sb1[o] and X0[o][0] != o and lev(X0[sb0[o]], X0[sb1[o]]) == Ls[k]: c[seg] = c.get(seg, 0) + 1
        prev = k
    return max(c.values()) if c else 0

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G); acc = {}
    try: check(g, acc, "c"); sm = segmax(g)
    except Exception: return (-1, 0, 0)
    if os.environ.get("MODE") == "rel":   # reward exits released at S4a steps next to absorptions
        rows, o = rows_w(g); so = set(g.succ[o]); rel = 0
        for k in range(len(rows) - 1):
            a, b = rows[k], rows[k + 1]
            if a["ph"] == b["ph"] and not a["fb"]: rel += sum(1 for x in so if x in a["R"] and x not in b["R"])
        return (acc.get("ORX_FAIL", 0) + acc.get("EXITR_FAIL", 0), min(acc.get("orise", 0), rel), acc.get("orise", 0) + rel)
    return (acc.get("ORX_FAIL", 0) + acc.get("EXITR_FAIL", 0), sm, acc.get("orise", 0))

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
