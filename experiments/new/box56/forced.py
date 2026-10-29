#!/usr/bin/env python3
"""L-NEW box 57 probe: at F-orbit states J (list), for each Even vertex g_i where F(sigma) and I^glo differ, the STALE values
val(F(sigma)[g_i -> option], sbar(sigma)) at g_i for both options (F's and I^glo's): STRICT means F's option is strictly better in the stale
frame (so F's choice there is forced by S4a', not a tie-break). Usage: forced.py GAME j1,j2,..."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("box54", "box21", "box56"): sys.path.insert(0, os.path.join(ROOT, "experiments", "new", p))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
import n5sf, pg
from n5x import load, Engine
from common import wplay
path = sys.argv[1]; Js = [int(x) for x in sys.argv[2].split(",")]
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
    EH = Engine(pg.Game(list(g.prio), list(g.owner), keep)); t = tuple(s)
    while True:
        val, _ = EH.evaluate(t); imp = EH.improving(t, val)
        if not imp: return list(t)
        t = EH.rule_switch_all(t, val, imp, None)
for J in Js:
    s, f = seq[J], seq[J + 1]; q = glo(s); sb = E.evaluate(tuple(s))[1]; odd = [sb[v] if g.owner[v] == 1 else -1 for v in range(n)]
    for v in range(n):
        if g.owner[v] != 0 or f[v] == q[v] or not L(v).startswith("g") or "'" in L(v): continue
        alt = list(f); alt[v] = q[v]
        a, _ = wplay(E, g, f, odd); b, _ = wplay(E, g, alt, odd)
        ka, kb = E.key(a[v]), E.key(b[v])
        ta, _ = E.evaluate(tuple(f)); tb, _ = E.evaluate(tuple(alt)); kta, ktb = E.key(ta[v]), E.key(tb[v])
        print(J, L(v), "F:", L(f[v]), "GLO:", L(q[v]), "| stale frame: F-option", "STRICTLY better" if ka > kb else ("TIE" if ka == kb else "worse"),
              "| true frame: F-option", "better" if kta > ktb else ("TIE" if kta == ktb else "STRICTLY worse"))
