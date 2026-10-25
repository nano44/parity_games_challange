#!/usr/bin/env python3
"""Box 35 (b): (L2) item 2 of N5-REL-box34.md §12. At an in-phase S4c fallback s -> s+1 with H1 and ¬H2 at s, does tau(o) leave R?
Counts such fallbacks, the event (tau(o) not in R_{s+1}), H1 / H2 at s+1, and whether a vertex of o's W-cycle switched.
Usage: fbtau.py game.pg ... | --rand N lo hi seed   (library: prints per-file events)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

def wcyc(nxt, o):
    c, u = [], nxt[o]
    while u != o: c.append(u); u = nxt[u]
    return c

def events(g, rows, o):
    out = []
    for s in range(len(rows) - 1):
        a, b = rows[s], rows[s + 1]
        if not a["fb"] or a["ph"] != b["ph"] or not a["h1"] or h2(a["nxt"], o): continue
        t0 = a["nxt"][o]; cyc = wcyc(a["nxt"], o)
        sw = [v for v in cyc if g.owner[v] == 0 and a["s"][v] != b["s"][v]]
        out.append(dict(s=s, leave=t0 not in set(b["R"]) | {o}, h1b=b["h1"], h2b=h2(b["nxt"], o), sw=len(sw), loop=(t0 == o)))
    return out

def check(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g)
    for e in events(g, rows, o):
        bump(acc, "fb_H1_notH2_inphase"); bump(acc, "cycle_switch_" + ("yes" if e["sw"] else "no")); bump(acc, "tau_o_selfloop_" + str(int(e["loop"])))
        bump(acc, f"next_h1={int(e['h1b'])}_h2={int(e['h2b'])}")
        if e["leave"]: bump(acc, "TAU_LEAVES_R"); acc.setdefault("ex_leave", []).append((name, e["s"]))

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
