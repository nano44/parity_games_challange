#!/usr/bin/env python3
"""Box 37 (b): ROUTE-FROZEN probe (docs/new/N5-OUT-box37.md §3). In an H1 ∧ ¬H2 stretch of a phase, classify every transition
k -> k+1 with θ_k = θ_{k+1} by (kind S4a / fallback) x (before / after the first fallback of the current θ-constant run) and record
whether Ξ changes at some vertex of R_k ∩ R_{k+1} (an R-value rise), at some vertex of F_k ∩ F_{k+1}, and whether R gains (entry).
One Odd choice vertex asserted. Usage: rfrozen.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from outsn import *

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]; E = Engine(g)
    seenfb = False
    for k in range(N - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"] or not a["h1"] or H2[k]: seenfb = False; continue
        if a["th"] != b["th"]: seenfb = False; continue
        R0, R1 = set(a["R"]), set(b["R"]); F0 = set(range(g.n)) - R0 - {o}; F1 = set(range(g.n)) - R1 - {o}
        rr = any(E.key(a["Xi"][v]) != E.key(b["Xi"][v]) for v in R0 & R1)
        ff = any(E.key(a["Xi"][v]) != E.key(b["Xi"][v]) for v in F0 & F1)
        tag = ("FB" if a["fb"] else "S4A") + ("_afterfb" if seenfb else "_before")
        bump(acc, tag); bump(acc, tag + "_Rrise", rr); bump(acc, tag + "_Frise", ff); bump(acc, tag + "_entry", bool(R1 - R0))
        if seenfb and rr: mx(acc, "ex_Rrise_afterfb", 1, g.n, name, k, tag)
        if seenfb and R1 - R0: mx(acc, "ex_entry_afterfb", 1, g.n, name, k, tag)
        if a["fb"]: seenfb = True

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
