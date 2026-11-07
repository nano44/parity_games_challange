#!/usr/bin/env python3
"""L-RED R155: switches of h2 (mksrc1.py) per W-run, landing classes (a = dynamic via SRC, b = static), W(h2) strictly rising at each
landing, and WCH of SRC in the longest W-run; the ONE-SOURCE bound K1 (K0 + 1) + K0. Usage: srctrace.py GAME.pg GAME.start"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg; lab = {}; name = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"([^"]*)"', line)
    if m: lab[m.group(2)] = int(m.group(1)); name[int(m.group(1))] = m.group(2)
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); h = lab["h2"]
K1 = sum(1 for l in lab if re.fullmatch(r"da\d+", l)); K0 = sum(1 for l in lab if re.fullmatch(r"sb\d+", l))
SRC = g.succ[lab["mda1"]][0]
tr, fb = xcn.trace(g, s0, t0); runs, W = xcn.wruns(g, tr, fb); F = max(runs, key=len); t = tr[F[0]][1]; SG = n5b.SpecSI(g)
Ws = {k: W(tr[k][0], t) for k in F}
wsrc = sum(Ws[F[i]][SRC] != Ws[F[i - 1]][SRC] for i in range(1, len(F)))
land = []; bad = 0
for k in F[:-1]:
    if tr[k][0][h] != tr[k + 1][0][h]:
        land.append(name[tr[k + 1][0][h]])
        if not SG.nvo(Ws[k][h], Ws[k + 1][h]) < 0: bad += 1
allsw = sum(tr[k][0][h] != tr[k + 1][0][h] for k in range(len(tr) - 1))
print(f"SRC1 {os.path.basename(sys.argv[1])} n {g.n} iters {len(tr)-1} wruns {len(runs)} maxL {len(F)-1} tau-changes {sum(tr[k][1] != tr[k+1][1] for k in range(len(tr)-1))} "
      f"WCH(SRC) {wsrc} h2-switches-in-F {len(land)} (all {allsw}) landings {land} W(h2)-not-rising {bad} bound {K1 * (K0 + 1) + K0} (K1 {K1}, K0 {K0})")
