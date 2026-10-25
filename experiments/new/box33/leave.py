#!/usr/bin/env python3
"""Box 33: Lemma LEAVE (docs/new/N5-K-box33.md §12). At an S4a transition s -> s+1 (no fallback) of a phase with H1 at s, a vertex q in
R_s that leaves (q not in R̄_{s+1}) needs (h) at s (else R-STICK), and q's H_{s+1}-path before its cycle node carries a relevant change of
level >= r_s := lev(θ_s, w_s). Checks both at every leave; counts leaves by class. Usage: leave.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from scopecov import h2
from dormant import *

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    for s in range(len(rows) - 1):
        a, b = rows[s], rows[s + 1]
        if a["ph"] != b["ph"] or a["fb"]: continue
        R0, R1 = set(a["R"]), set(b["R"]) | {o}
        lv = [v for v in R0 if v != o and v not in R1]
        if not lv: continue
        hh = a["h1"] and h2(a["nxt"], o) and a["Xi"][o][0] == a["W"][o][0]
        key = ("H1" if a["h1"] else "nH1") + ("_h" if hh else "_noh")
        acc["leave_" + key] = acc.get("leave_" + key, 0) + len(lv)
        if a["h1"] and not hh: acc["LEAVE_noh_FAIL"] = acc.get("LEAVE_noh_FAIL", 0) + 1; acc.setdefault("ex_noh", (name, s))
        if not hh: continue
        r = lev(a["Xi"][o], a["W"][o]); X0 = ev[s][0]; sb0, sb1 = ev[s][1], ev[s + 1][1]
        nxt1 = [b["s"][v] if g.owner[v] == 0 else sb1[v] for v in range(n)]
        for q in lv:
            c = ev[s + 1][0][q][0]; u = q; mx = -2; seen = set()
            while u != c and u not in seen:
                seen.add(u)
                if X0[u][0] != u:
                    if g.owner[u] == 0 and a["s"][u] != b["s"][u]: mx = max(mx, lev(X0[a["s"][u]], X0[b["s"][u]]))
                    if g.owner[u] == 1 and sb0[u] != sb1[u]: mx = max(mx, lev(X0[sb0[u]], X0[sb1[u]]))
                u = nxt1[u]
            if not mx >= r: acc["LEAVE_lev_FAIL"] = acc.get("LEAVE_lev_FAIL", 0) + 1; acc.setdefault("ex_lev", (name, s, q, mx, r))
            acc["leave_checked"] = acc.get("leave_checked", 0) + 1

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
    acc.setdefault("leave_checked", 0)
    for k in sorted(acc): print(k, acc[k])
