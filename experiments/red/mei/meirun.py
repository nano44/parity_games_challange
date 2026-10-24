#!/usr/bin/env python3
"""T31 checklist (i)-(iii) on the Mei port: Dantzig-SSI control and N5 from Mei's start pair and from the canonical start.
Dantzig-SSI = single switch at the most significant valuation difference (si.py rule_single_level, most=True = MSF), Odd = exact
best reply sigma-bar, from Mei's sigma_0. N5 = experiments/new/n5.py run(); elim windows and phases by L-SI's orlens/elim.py
(unmodified). Usage: meirun.py game.pg [game.pg.start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for d in ("../../harness", "../../si", "../../new", "../../si/orlens"): sys.path.insert(0, os.path.join(HERE, d))
import pg, n5, elim
from si import Engine
import ortrace as OT

def dantzig(g, s0):
    E = Engine(g)
    st = [-1] * g.n
    for v in range(g.n):
        if g.owner[v] == 0: st[v] = s0.get(v, g.succ[v][0])
    seq = [tuple(st)]; strat = tuple(st)
    while True:
        val, _ = E.evaluate(strat); imp = E.improving(strat, val)
        if not imp: break
        strat = E.rule_single_level(strat, val, imp, None); seq.append(strat)
    # elim.py's sigma-only definition, applied to the whole Dantzig run: transition k eliminating iff some abandoned Even edge never recurs
    last = {}
    for i, s in enumerate(seq):
        for x in range(g.n):
            if g.owner[x] == 0: last[(x, s[x])] = i
    el = [any(seq[i][x] != seq[i + 1][x] and last[(x, seq[i][x])] == i for x in range(g.n) if g.owner[x] == 0) for i in range(len(seq) - 1)]
    best = cur = 0
    for b in el:
        cur = 0 if b else cur + 1; best = max(best, cur)
    return len(seq) - 1, best

if __name__ == "__main__":
    path = sys.argv[1]; sp = sys.argv[2] if len(sys.argv) > 2 else path + ".start"
    g, st = OT.load(path, sp)
    print(f"{os.path.basename(path)} n={g.n}")
    it, ne = dantzig(g, st[0]); print(f"  dantzig-ssi from mei sigma0: iterations={it} noelimrun={ne}")
    for lab, s in (("mei-start", st), ("canonical", None)):
        it, fb, win, ws, ev = n5.run(g, "n5", s)
        _, it2, rows = elim.elim_g(g, s)
        r = max(rows, key=lambda q: q["trans"])
        print(f"  n5 {lab}: iterations={it} fallback={fb} phases={len(rows)} longest={r['trans']} noelimrun={r['noelimrun']} "
              f"both={r['noelimrun_both']} st={r['noelimrun_st']} (elim it={it2})")
        sol = path + f".{lab}.sol"
        with open(sol, "w") as f:
            f.write(f"paritysol {g.n - 1};\n")
            for v in range(g.n): f.write(f"{v} {win[v]} {ws[v]};\n" if ws[v] is not None else f"{v} {win[v]};\n")
