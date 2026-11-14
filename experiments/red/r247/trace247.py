#!/usr/bin/env python3
"""L-RED 71 R247: trace of a one-sided rule on a labelled game (.pg with "labels" and a '% start' line, as gens_red.py writes):
per iteration the improvable vertices with their Xi-best target (* = switched by the rule) and RF's dependency sets.
Usage: trace247.py GAME.pg RULE"""
import sys, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..")]
import si247, rf247
fn, rule = sys.argv[1], sys.argv[2]
lab = {}
for line in open(fn):
    m = re.match(r'(\d+) \d+ \d+ [\d,]+ "([^"]+)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
e = si247.SI(*si247.parse(fn)); st = e.s3(); g = si247.read_start(fn)
if g: st.update(g)
L = lambda v: lab.get(v, str(v))
def hook(it, sigma, val, sbar, I, ch):
    D = rf247.dep(e, sigma, val, sbar, I); S, comp = rf247.sinks(D)
    print(f"it {it+1}: improvable " + " ".join(f"{L(v)}->{L(e.best(val, ws))}{'*' if v in ch else ''}" for v, ws in sorted(I.items())))
    print("      deps: " + "; ".join(f"{L(v)}:{{{','.join(L(u) for u in sorted(D[v]))}}}" for v in sorted(D) if D[v]))
r = e.run(si247.RULES[rule], st, hook=hook)
print("iterations", r["its"])
