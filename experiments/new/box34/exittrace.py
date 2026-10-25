#!/usr/bin/env python3
"""Box 34: per-transition trace of o's exits. For each transition k -> k+1: phase id, fallback?, (h)?, r = lev(θ, w) (-2 = ⊥ = θ = w),
w changed?, exits joining R (+x), leaving R (-x), σ̄(o) old -> new, and whether the transition is an ε-transition (O_k > E_k).
Usage: exittrace.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *

def trace(g):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n; ex = sorted(set(g.succ[o])); out = []
    phs = {}
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]; X0 = ev[k][0]; sb0, sb1 = ev[k][1], ev[k + 1][1]
        pid = phs.setdefault(a["ph"], len(phs))
        Ev = max([lev(X0[a["s"][y]], X0[b["s"][y]]) for y in range(n) if g.owner[y] == 0 and a["s"][y] != b["s"][y] and X0[y][0] != y] + [-2])
        Od = lev(X0[sb0[o]], X0[sb1[o]]) if sb0[o] != sb1[o] and X0[o][0] != o else -2
        hh = a["h1"] and h2(a["nxt"], o) and a["Xi"][o][0] == a["W"][o][0]
        R0, R1 = set(a["R"]), set(b["R"])
        j = [x for x in ex if x != o and x in R1 and x not in R0]; l = [x for x in ex if x != o and x in R0 and x not in R1]
        out.append(dict(k=k, ph=pid, same=a["ph"] == b["ph"], fb=a["fb"], h=hh, r=lev(a["Xi"][o], a["W"][o]) if hh else None,
                        wch=a["w"] != b["w"], join=j, leave=l, sb=(sb0[o], sb1[o]), eps=Od > Ev, nR=len(R0), exR=sum(1 for x in ex if x in R0)))
    return out, o

if __name__ == "__main__":
    g = load(sys.argv[1]); tr, o = trace(g); print("n", g.n, "o", o, "d_o", len(set(g.succ[o])))
    for t in tr:
        print(f"{t['k']:3d} ph{t['ph']}{'' if t['same'] else '|X'} {'FB' if t['fb'] else '  '} {'h' if t['h'] else '-'} r={t['r']} "
              f"{'w*' if t['wch'] else '  '} exR={t['exR']} |R|={t['nR']} sb {t['sb'][0]}->{t['sb'][1]} {'EPS' if t['eps'] else ''} "
              f"+{t['join']} -{t['leave']}")
