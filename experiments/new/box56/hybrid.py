#!/usr/bin/env python3
"""L-NEW box 57 probe: one-sided runs on a game from the S3 start: F (N5-SF's Even map, box55/pcheck.F), I^glo (carry3.py's glo), or a
HYBRID that takes I^glo's step at the states (by step index) listed in USE and F's step elsewhere. Prints the CC bit patterns with step index
and the total number of steps. Usage: hybrid.py GAME MODE [i,j,...]   MODE in F, GLO, HYB"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box55")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import pcheck, pg
from n5x import load, Engine, dual, start_pair
path, mode = sys.argv[1], sys.argv[2]; USE = set(int(x) for x in sys.argv[3].split(",")) if len(sys.argv) > 3 and sys.argv[3] else set()
g = load(path); n = g.n; E = Engine(g)
lab = {}
for l in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d\s+[\d,]+\s+"([^"]*)"', l)
    if m: lab[int(m.group(1))] = m.group(2)
CLS = os.environ.get("CLS", "")   # MODE CLS: take I^glo's step iff F and I^glo differ at a vertex whose label starts with one of CLS's letters (not primed)
def cls_hit(a, b): return any(a[v] != b[v] and lab.get(v, "?")[0] in CLS and "'" not in lab.get(v, "?") for v in range(n) if g.owner[v] == 0)
def glo(s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None
    keep = [sorted({s[v]} | {w for (x, w) in Is if x == v}) if g.owner[v] == 0 else sorted(set(g.succ[v])) for v in range(n)]
    EH = Engine(pg.Game(list(g.prio), list(g.owner), keep)); t = tuple(s)
    while True:
        val, _ = EH.evaluate(t); imp = EH.improving(t, val)
        if not imp: return list(t)
        t = EH.rule_switch_all(t, val, imp, None)
s, _ = start_pair(g, E, Engine(dual(g)), None); s = [s[v] if g.owner[v] == 0 else -1 for v in range(n)]
CH = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
pats = []; k = 0
while True:
    sb = E.evaluate(tuple(s))[1]; p = "".join("1" if sb[u] == max(set(g.succ[u])) else "0" for u in reversed(CH))
    if not pats or pats[-1][1] != p: pats.append((k, p))
    if mode == "CLS":
        a, b = pcheck.F(g, E, s), glo(s); nx = b if (a is not None and b is not None and cls_hit(a, b)) else a
        if nx is not None and nx is b and a != b:
            USE.add(k)
            if os.environ.get("SHOWD"):
                sbF = E.evaluate(tuple(a))[1]; sbG = E.evaluate(tuple(b))[1]
                d = " ".join(f"{lab.get(v,v)}:{lab.get(a[v],a[v])}/{lab.get(b[v],b[v])}" for v in range(n) if g.owner[v] == 0 and a[v] != b[v])
                o = " ".join(f"{lab.get(u,u)}:{lab.get(sb[u],sb[u])}>{lab.get(sbF[u],sbF[u])}/{lab.get(sbG[u],sbG[u])}" for u in CH if sb[u] != sbF[u] or sb[u] != sbG[u])
                print("STEP", k, p, "F/GLO", d, "| sbar now>afterF/afterGLO", o)
    else:
        nx = glo(s) if (mode == "GLO" or (mode == "HYB" and k in USE)) else pcheck.F(g, E, s)
    if nx is None or nx == s: break
    s = nx; k += 1
    if k > 20000: break
print(mode, CLS, "steps", k, "glo_steps_used", len(USE) if mode == "CLS" else "", "patterns", len(pats), "distinct", len({p for _, p in pats}))
print(" ".join(f"{p}@{j}" for j, p in pats))
