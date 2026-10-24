#!/usr/bin/env python3
"""L-SI box 4 (b)/(d), exact version of correct.py/rstar.py (gadget-free, hterm.py). Per state k of the longest phase:
R*_k = vertices whose H(θ_k)-optimal play reaches o; CORR_k = #{y ≠ o : Ξ_k(y) has the same Engine.key as y's H(θ_k)-optimum}.
Prints per phase: |R*| values, θ-changes moving R*, CORR sequence summary, CORR drops and where (fallback or not), crossings
without a strict CORR rise. Usage: correct2.py game.pg [--seq] ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hterm import *

def annotate_opt(g, rows, o, E):
    ovs = 0
    for r in rows:
        Xi, sb = E.evaluate(tuple(r["s"])); th = Xi[o]
        s, vals = hopt(g, E, r["t"], o, th, r["s"])
        r["Rs"] = {y for y in range(g.n) if y != o and vals[y][1]}
        r["C"] = {y for y in range(g.n) if y != o and E.key(vals[y][0]) == E.key(Xi[y])}
        r["ov"] = sum(1 for y in range(g.n) if vals[y][2]); ovs += r["ov"]
        r["above"] = [y for y in range(g.n) if E.key(Xi[y]) > E.key(vals[y][0])]   # must be empty if H dominates
    return ovs

def scan(path, seq=False):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    ovs = annotate_opt(g, rows, o, E); out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), T=y - x, Rs=sorted({len(rows[k]["Rs"]) for k in range(x, y + 1)}), tc=0, tcRs=0, X=0, X_noCrise=0,
                  drops_fb=0, drops_arena=0, maxdrop=0, above=sum(len(rows[k]["above"]) for k in range(x, y + 1)))
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if a["th"] != b["th"]: st["tc"] += 1; st["tcRs"] += a["Rs"] != b["Rs"]
            d = len(a["C"]) - len(b["C"])
            if len(a["C"] - b["C"]):
                st["drops_fb" if a["fb"] else "drops_arena"] += 1; st["maxdrop"] = max(st["maxdrop"], len(a["C"] - b["C"]))
            if a["R"] != b["R"]: st["X"] += 1; st["X_noCrise"] += not (len(b["C"]) > len(a["C"]))
        if seq: st["C"] = [len(rows[k]["C"]) for k in range(x, y + 1)]; st["R"] = [len(rows[k]["R"]) for k in range(x, y + 1)]
        out.append(st)
    return g.n, out, ovs

if __name__ == "__main__":
    seq = "--seq" in sys.argv
    for p in [a for a in sys.argv[1:] if not a.startswith("--")]:
        n, out, ovs = scan(p, seq); best = max(out, key=lambda s: (s["X"], s["T"]))
        print(os.path.basename(p), "n", n, "overlaps", ovs, best)
