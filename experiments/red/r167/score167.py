#!/usr/bin/env python3
"""L-RED successor 39 (R167): run n5b SPEC on a labelled game + start; print n, iterations, fallbacks, tau moves, W-runs, |F| (longest
W-run), |F|/n^2, and Even switches per vertex class inside the longest W-run (class = label with trailing digits stripped).
TRACE=1 also prints, per transition of the longest W-run, the switched Even vertices (labels). Usage: score167.py G.pg START"""
import sys, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn")); sys.path.insert(0, os.path.join(HERE, "..", "startck"))
import xcn, n5b, startck
if startck.check(sys.argv[1], sys.argv[2]): sys.exit(f"BAD START {startck.check(sys.argv[1], sys.argv[2])[:3]}")
g = xcn.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
lab = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
tr, fb = xcn.trace(g, s0, t0, cap=int(os.environ.get("CAP", "200000"))); runs, W = xcn.wruns(g, tr, fb)
taum = sum(1 for k in range(len(tr) - 1) if tr[k][1] != tr[k + 1][1])
F = max(runs, key=len); L = len(F) - 1
cls = collections.Counter(); per = collections.Counter()
for k in F[:-1]:
    s, s2 = tr[k][0], tr[k + 1][0]
    sw = [v for v in range(g.n) if g.owner[v] == 0 and s[v] != s2[v]]
    for v in sw: cls[re.sub(r"\d+$", "", lab[v])] += 1; per[lab[v]] += 1
    if os.environ.get("TRACE"): print("k", k, " ".join(f"{lab[v]}->{lab[s2[v]]}" for v in sw))
print(f"n {g.n} iterations {len(tr) - 1} fallbacks {sum(fb)} taumoves {taum} wruns {[(R[0], R[-1]) for R in runs if len(R) > 1]} |F| {L} |F|/n^2 {L / g.n ** 2:.4f}")
print("switches by class:", dict(sorted(cls.items())))
if os.environ.get("PER"): print("per vertex:", dict(sorted(per.items())))
