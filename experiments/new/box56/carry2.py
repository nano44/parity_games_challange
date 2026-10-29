#!/usr/bin/env python3
"""L-NEW box 57 probe: at orbit state j of F on switchbestexp_N, for the cycle C_i = e_i, f_i, g_i, h_i (CycleNode0/1/2(i), CycleCenter(i)):
which closing edges are improving; the stale-frame value val(F(sigma), sbar(sigma)) vs the true Xi_{F(sigma)} at h_i; and the true Xi of
F(sigma) with g_i's closing switch reverted (what an optimum against the NEW counterstrategy compares). Usage: carry2.py GAME j i"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
import n5sf
from n5x import load
from common import wplay
path, J, I = sys.argv[1], int(sys.argv[2]), sys.argv[3]
lab = {}; inv = {}
for l in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d\s+[\d,]+\s+"([^"]*)"', l)
    if m: lab[int(m.group(1))] = m.group(2); inv[m.group(2)] = int(m.group(1))
g = load(path); n = g.n; L = lambda v: lab.get(v, str(v))
E, T = n5sf.trace(g, None); T = [x for x in T if "lam" in x]
seq = []
for x in T:
    s = [x["s"][v] if g.owner[v] == 0 else -1 for v in range(n)]
    if not seq or seq[-1] != s: seq.append(s)
e, f, gg, h, mm = (inv[c + I] for c in "efghm")
for j in range(J - 4, J + 2):
    s = seq[j]; vs, sb = E.evaluate(tuple(s)); Is = set(E.improving(tuple(s), vs))
    imp = {a: [L(w) for (v, w) in Is if v == inv[a + I]] for a in "efg"}
    print(j, "sigma", {a: L(s[inv[a + I]]) for a in "efg"}, "improving", imp, "sbar(h)", L(sb[h]))
s, s1 = seq[J], seq[J + 1]; vs, sb = E.evaluate(tuple(s)); v1, sb1 = E.evaluate(tuple(s1))
stale, _ = wplay(E, g, s1, [sb[v] if g.owner[v] == 1 else -1 for v in range(n)])
print("step", J, "->", J + 1, ": stale value at h", stale[h], "key", E.key(stale[h])[:2], "| true Xi at h", v1[h], "key", E.key(v1[h])[:2], "| sbar_new(h)", L(sb1[h]))
r = list(s1); r[gg] = s[gg]; vr, _ = E.evaluate(tuple(r))
better = [L(v) for v in range(n) if E.key(vr[v]) > E.key(v1[v])]; worse = [L(v) for v in range(n) if E.key(vr[v]) < E.key(v1[v])]
print("revert g closing (g ->", L(s[gg]), "): true Xi higher at", len(better), better[:8], "lower at", len(worse), worse[:8])
