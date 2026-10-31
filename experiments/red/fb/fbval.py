#!/usr/bin/env python3
"""L-RED R158: print Xi and W of named vertices at given states of an n5b SPEC run (P-sets as marker names, most relevant first).
Usage: fbval.py GAME.pg START k1,k2,.. name1,name2,.."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
g = xcn.pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g)
names = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line)
    if m: names[int(m.group(1))] = m.group(2)
ix = {v: k for k, v in names.items()}
tr, fb = xcn.trace(g, *st); runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g)
fmt = lambda val: f"{names[val[0]]}|" + ",".join(names[u] for u in sorted(val[1], key=lambda u: -g.prio[u])) + f"|{val[2]}"
for k in map(int, sys.argv[3].split(",")):
    s, t = tr[k]; xv, ch = SG.evaluate_choice(list(s)); wv = W(s, t)
    print(f"state {k}")
    for nm in sys.argv[4].split(","):
        v = ix[nm]; print(f"  {nm}: Xi {fmt(xv[v])}  W {fmt(wv[v])}" + (f"  sbar->{names[ch[v]]}" if g.owner[v] == 1 else f"  sig->{names[s[v]]}"))
