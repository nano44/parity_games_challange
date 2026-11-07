#!/usr/bin/env python3
"""L-RED successor 39 (R167): at state k of the n5b SPEC run, print for each named vertex its Xi value (cycle node label, the path set as
labels sorted by priority descending, length), sigma-bar choice (Odd) or sigma (Even), and its W value (vs the current tau).
Usage: xiprobe.py G.pg START k name1 name2 ..."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
g = xcn.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); k = int(sys.argv[3])
lab = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
ix = {v: i for i, v in lab.items()}
tr, fb = xcn.trace(g, s0, t0, cap=int(os.environ.get("CAP", "200000"))); runs, W = xcn.wruns(g, tr, fb)
s, t = tr[k]; xv, ch = n5b.SpecSI(g).evaluate_choice(list(s)); wv = W(s, t)
def fmt(val):
    c, P, l = val
    return f"{lab[c]}|" + ",".join(f"{lab[u]}{'+' if g.prio[u] % 2 == 0 else '-'}" for u in sorted(P, key=lambda u: -g.prio[u])) + f"|{l}"
for name in sys.argv[4:]:
    v = ix[name]
    nx = lab[s[v]] if g.owner[v] == 0 else f"bar:{lab[ch[v]]} tau:{lab[t[v]]}"
    print(f"{name:8s} {nx:24s} Xi {fmt(xv[v])}\n{'':33s} W  {fmt(wv[v])}")
