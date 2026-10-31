#!/usr/bin/env python3
"""L-RED R156: check Lemma k-SOURCE on a mksrc2.py game: in the longest W-run, the landings of h2 by class, the class DESCENTS (a
landing in class c on an option not above the previous class-c landing in c's static order) and whether each descent has a W-rise of
SRC_c in between (the lemma says it must); the bound K0 + sum_c K_c (1 + WCH(SRC_c)). Usage: src2trace.py GAME.pg GAME.start"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg; lab = {}; name = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"([^"]*)"', line)
    if m: lab[m.group(2)] = int(m.group(1)); name[int(m.group(1))] = m.group(2)
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); h = lab["h2"]
cls = {}
for l, v in lab.items():
    m = re.fullmatch(r"d(\d+)a(\d+)", l)
    if m: cls.setdefault(int(m.group(1)), []).append(v)
K0 = sum(1 for l in lab if re.fullmatch(r"sb\d+", l)); SRC = {c: g.succ[g.succ[vs[0]][0]][0] for c, vs in cls.items()}
tr, fb = xcn.trace(g, s0, t0); runs, W = xcn.wruns(g, tr, fb); F = max(runs, key=len); t = tr[F[0]][1]; SG = n5b.SpecSI(g)
Ws = {k: W(tr[k][0], t) for k in F}
wch = {c: sum(Ws[F[i]][u] != Ws[F[i - 1]][u] for i in range(1, len(F))) for c, u in SRC.items()}
last = {}; desc = 0; descbad = 0; land = []; cc = 0; prevc = None
for k in F[:-1]:
    y = tr[k + 1][0][h]
    if tr[k][0][h] == y: continue
    m = re.fullmatch(r"d(\d+)a(\d+)", name[y]); c = int(m.group(1)) if m else 0; land.append(name[y])
    if c != prevc and prevc is not None: cc += 1
    prevc = c
    if c and c in last:
        k0, y0 = last[c]
        if not SG.nvo(Ws[k + 1][y0], Ws[k + 1][y]) < 0:          # y not above y0 (static order read at k + 1)
            desc += 1; u = SRC[c]
            if not any(Ws[F[i]][u] != Ws[F[i - 1]][u] for i in range(F.index(k0 + 1) + 1, F.index(k + 1) + 1)): descbad += 1
    if c: last[c] = (k, y)
bound = K0 + sum(len(cls[c]) * (1 + wch[c]) for c in cls)
print(f"SRC2 {os.path.basename(sys.argv[1])} n {g.n} iters {len(tr)-1} wruns {len(runs)} maxL {len(F)-1} switches {len(land)} class-changes {cc} "
      f"descents {desc} descents-without-source-rise {descbad} WCH {dict(sorted(wch.items()))} bound {bound} landings {land}")
