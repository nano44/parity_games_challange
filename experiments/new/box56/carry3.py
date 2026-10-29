#!/usr/bin/env python3
"""L-NEW box 57 probe: along F's orbit on a game, compare F's step with Schewe's optimal step I^glo from the SAME state: the optimum of the
arena game H (Even: {sigma(v)} + I_sigma(v); Odd FREE), computed by switch-all SI inside H from sigma (the method of L-LIT T44's sfxi, copied,
not imported). Prints the states j in [A, B] where they differ, with the differing Even vertices (label: F's choice / I^glo's choice), and
whether I^glo's strategy has a higher true Xi than F's at some vertex (GLO>F) or a lower one (GLO<F). Usage: carry3.py GAME A B"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf, pg
from n5x import load, Engine
path, A, B = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lab = {}
for l in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d\s+[\d,]+\s+"([^"]*)"', l)
    if m: lab[int(m.group(1))] = m.group(2)
L = lambda v: lab.get(v, str(v))
g = load(path); n = g.n
E, T = n5sf.trace(g, None); T = [x for x in T if "lam" in x]
seq = []
for x in T:
    s = [x["s"][v] if g.owner[v] == 0 else -1 for v in range(n)]
    if not seq or seq[-1] != s: seq.append(s)
def glo(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    keep = [sorted({s[v]} | {w for (x, w) in Is if x == v}) if g.owner[v] == 0 else sorted(set(g.succ[v])) for v in range(n)]
    H = pg.Game(list(g.prio), list(g.owner), keep); EH = Engine(H); t = tuple(s)
    while True:
        val, _ = EH.evaluate(t); imp = EH.improving(t, val)
        if not imp: return list(t)
        t = EH.rule_switch_all(t, val, imp, None)
for j in range(A, min(B, len(seq) - 2) + 1):
    s, f = seq[j], seq[j + 1]; q = glo(s)
    d = [v for v in range(n) if g.owner[v] == 0 and f[v] != q[v]]
    if not d: continue
    vf, _ = E.evaluate(tuple(f)); vq, _ = E.evaluate(tuple(q))
    up = [L(v) for v in range(n) if E.key(vq[v]) > E.key(vf[v])]; dn = [L(v) for v in range(n) if E.key(vq[v]) < E.key(vf[v])]
    print(j, "diff", len(d), " ".join(f"{L(v)}:{L(f[v])}/{L(q[v])}" for v in d[:12]), "| GLO>F at", len(up), up[:6], "| GLO<F at", len(dn), dn[:6])
