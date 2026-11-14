#!/usr/bin/env python3
"""L-RED 71 R247: where RF leaves Howard's run. Howard (switch-best everywhere) is run on a labelled game from its '% start' line; at every
step RF's dependency digraph is computed and the improvable vertices that RF would NOT switch (not in a sink component) are listed with
their blockers. Counters: steps with a blocked vertex; pairs (step, blocked type, blocker type) by vertex type (label without its index).
Usage: viol247.py GAME.pg [steps to print]"""
import sys, re, collections, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..")]
import si247, rf247
fn = sys.argv[1]; show = int(sys.argv[2]) if len(sys.argv) > 2 else 12
lab = {}
for line in open(fn):
    m = re.match(r'(\d+) \d+ \d+ [\d,]+ "([^"]+)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
e = si247.SI(*si247.parse(fn)); st = e.s3(); g = si247.read_start(fn)
if g: st.update(g)
L = lambda v: lab.get(v, str(v)); typ = lambda v: re.sub(r"\d+", "", L(v))
cnt = collections.Counter(); steps = [0, 0]
def hook(it, sigma, val, sbar, I, ch):
    D = rf247.dep(e, sigma, val, sbar, I); S, comp = rf247.sinks(D)
    blocked = [v for v in I if v not in S]; steps[0] += 1; steps[1] += bool(blocked)
    for v in blocked:
        for u in D[v]:
            if comp[u] != comp[v]:
                # through which target?
                cnt[(typ(v), typ(u))] += 1
    if it < show:
        print(f"it {it+1}: switch " + " ".join(f"{L(v)}->{L(w)}" for v, w in sorted(ch.items())) + " | BLOCKED under RF: " + " ".join(f"{L(v)}[{','.join(L(u) for u in sorted(D[v]) if comp[u] != comp[v])}]" for v in sorted(blocked)))
r = e.run("howard", st, hook=hook)
print("howard iterations", r["its"], "steps with a blocked vertex", steps[1], "of", steps[0])
for k, c in cnt.most_common(): print("  blocked", k[0], "by", k[1], c)
