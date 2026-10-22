#!/usr/bin/env python3
"""Labelled trace of the S7 most-improved rule (vj.py) on a labelled .pg: per step the gate states (d_i -> e_i = closed),
the improving edges with their counts and new valuation key at v, and the switch taken.  Usage: trace_mi.py game.pg [--start spec:...]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
path = sys.argv[1]; start = "best"
if "--start" in sys.argv: start = sys.argv[sys.argv.index("--start") + 1]
if start == "file":
    start = "spec:" + [l for l in open(path) if l.startswith("% start")][0].split("start")[1].strip()
lab = {}
for line in open(path):
    m = re.match(r'^(\d+) .*"([^"]*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
e = vj.VJ(*vj.read_pg(path)); L = lambda v: lab.get(v, str(v))
gates = sorted([v for v in lab if lab[v].startswith("d")], key=lambda v: int(lab[v][1:]))
def hook(it, sigma, val, tau, v, w, lv, cyc, ch):
    imp = e.improving(sigma, val); info = []
    for a, b in imp:
        s2 = list(sigma); s2[a] = b; val2, _ = e.evaluate(tuple(s2))
        cnt = sum(1 for x in range(e.n) if e.key(val2[x]) > e.key(val[x]))
        info.append(f"{L(a)}->{L(b)}:{cnt}")
    bits = "".join("1" if lab.get(sigma[g], "") == "e" + lab[g][1:] else "0" for g in reversed(gates))
    print(f"step {it} gates {bits}: take {L(v)}->{L(w)} (count {lv[1]}); improving {' '.join(info)}")
sigma, it, st = e.run("most-improved", e.initial(start), hook=hook)
print("iterations", it)
