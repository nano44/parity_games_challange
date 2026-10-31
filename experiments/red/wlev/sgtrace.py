#!/usr/bin/env python3
"""L-RED R154: trace a mkgate1.py selector: per W-run, the switches of h (state, from, to) and, at each, which l_j are in Isigma(h) and
Xi(OBS) vs Lambda_j; also the number of Xi(OBS) changes in that W-run. Usage: sgtrace.py GAME.pg GAME.start"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
lab = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"([^"]*)"', line)
    if m: lab[m.group(2)] = int(m.group(1))
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); h = lab["h"]; OBS = [v for v in g.succ[lab["l1"]] if v != lab["lam1"]][0]; SIG = sorted({v for j in range(1, 100) if f"l{j}" in lab for v in g.succ[lab[f"l{j}"]] if v != lab[f"lam{j}"]})
L = [lab[f"l{j}"] for j in range(1, 100) if f"l{j}" in lab]
tr, fb = xcn.trace(g, s0, t0); runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g); X = {}
def xi(k):
    if k not in X: X[k] = SG.evaluate_choice(list(tr[k][0]))[0]
    return X[k]
F = max(runs, key=len); oc = sum(xi(k)[OBS] != xi(k + 1)[OBS] for k in F[:-1])
print(f"SGATE {os.path.basename(sys.argv[1])} n {g.n} iters {len(tr)-1} fallbacks {sum(fb)} wruns {len(runs)} maxL {len(F)-1} XICH(OBS) {oc} signals {SIG} "
      f"tau-changes {sum(tr[k][1] != tr[k+1][1] for k in range(len(tr)-1))}")
sw = 0
for k in range(len(tr) - 1):
    a, b = tr[k][0][h], tr[k + 1][0][h]
    if a != b:
        sw += 1; x = xi(k); cur = x[a]
        imp = [j + 1 for j, l in enumerate(L) if SG.nvo(cur, x[l]) < 0]
        print(f"  switch at {k}: l{L.index(a)+1} -> l{L.index(b)+1}; improving at k: {imp}")
print("h switches", sw, "levels", len(L))
