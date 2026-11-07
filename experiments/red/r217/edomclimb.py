#!/usr/bin/env python3
"""L-RED 54 R217: climb the PRIORITY ORDER of switchallexp G_n's fixed graph under E-DOM (CycleLeavers m_i form the top band below the
sink p; their internal order free; every other node's rank and parity free), scoring Howard T (switch-all VJ, best-reward start) on
the ORIGINAL game at n = NA (ties by T at NB). Mutations: swap two non-m ranks; flip one non-m parity; swap two m ranks.
Resumable: OUT.json holds {order, par}. Usage: edomclimb.py NA NB seed OUT"""
import sys, os, json, random, time
from fried import game, howard
NA, NB, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
SECS = int(os.environ.get("SECS", "1800")); t0 = time.time()
GA, GB = game(NA), game(NB)
def apply(V, order, par):
    # order: list of names (non-m, non-p) low -> high; then m's in order 'morder'; p on top
    nmv = {v[4]: v for v in V}; newp = {}; cur = -1
    for nm in order["low"] + order["m"]:
        if nm not in nmv: continue
        p = par.get(nm, nmv[nm][1] % 2); cur += 1
        if cur % 2 != p: cur += 1
        newp[nm] = cur
    top = cur + 2 + (cur % 2); newp["p"] = top if nmv["p"][1] % 2 == 0 else top + 1
    return [(v[0], newp[v[4]], v[2], v[3], v[4]) for v in V]
def generic(nm):  # name class, so that an order learned at NA transfers to NB by node class/index
    return nm
def init(V):
    low = [v[4] for v in sorted(V, key=lambda v: v[1]) if v[4][0] != "m" and v[4] != "p"]
    m = [v[4] for v in sorted(V, key=lambda v: v[1]) if v[4][0] == "m"]
    return {"low": low, "m": m}, {}
def score(order, par):
    try:
        TA, _ = howard(apply(GA, order, par), cap=20000)
    except Exception: return (-1, -1)
    return (TA, 0)
if os.path.exists(out + ".json"): d = json.load(open(out + ".json")); order, par = d["order"], d["par"]
else: order, par = init(GA)
best = score(order, par); print("start", best, flush=True); it = 0
while time.time() - t0 < SECS:
    it += 1; o = {"low": list(order["low"]), "m": list(order["m"])}; p = dict(par); r = rng.random()
    if r < 0.6:
        i, j = rng.randrange(len(o["low"])), rng.randrange(len(o["low"])); o["low"][i], o["low"][j] = o["low"][j], o["low"][i]
    elif r < 0.9:
        nm = rng.choice(o["low"]); base = next(v[1] for v in GA if v[4] == nm) % 2; p[nm] = 1 - p.get(nm, base)
    else:
        i, j = rng.randrange(len(o["m"])), rng.randrange(len(o["m"])); o["m"][i], o["m"][j] = o["m"][j], o["m"][i]
    s = score(o, p)
    if s >= best:
        if s > best: json.dump({"order": o, "par": p}, open(out + ".json", "w")); print(f"it {it} T {s[0]}", flush=True)
        order, par, best = o, p, s
print("SLICE end", it, best, flush=True)
