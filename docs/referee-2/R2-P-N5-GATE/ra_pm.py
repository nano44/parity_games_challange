#!/usr/bin/env python3
# REFEREE-2 successor 38: own recount of the two E-1 numbers of line L-5 that no referee had recounted (C142 E-1): the re-arm
# multiplicity m and the RA path count P. Own engines only (r2gate.run_cyc / run_g3; no lane code; the lane's mult90.py was read for
# the units, not imported). Definitions, from P-N5-SPLIT's RA-PATHS as the line uses them: for a vertex v and a maximal Λ-interval I
# of v, tops = the most relevant e-vertex of E_(t−1)(v) Δ E_t(v) at each change t inside I; for letters y, z:
#   m(y, z) := number of gaps between consecutive y-tops whose most relevant top is z;  RA(y) := {z : m(y, z) ≥ 1};
#   P(y) := 1 + Σ_(z ∈ RA(y)) P(z);  depth(y) := 1 + max depth over RA(y);  C := max number of y-tops (c_y).
# Must-0: rafail (an RA letter not more relevant than y, or an empty gap), idfail (c_y − 1 ≠ Σ_z m(y, z)).
# Usage: ra_pm.py ENGINE(g3|cyc) FILE.json ...
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import r2gate as RG
eng = sys.argv[1]
for fn in sys.argv[2:]:
    G = RG.load(fn); R = RG.run_g3(G) if eng == "g3" else RG.run_cyc(G)
    S = R["states"]; T = len(S) - 1; val = [s[1] for s in S]; rel = R["rel"]; evs = R["evs"]; n = R["n"]
    E = lambda t, v: frozenset(u for u in val[t][v][1] if u in evs)
    rec = Counter()
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and val[u + 1][v][0] == val[t][v][0]: u += 1
            tops = []
            for s in range(t + 1, u + 1):
                a, b = E(s - 1, v), E(s, v)
                if a != b: tops.append(max(a ^ b, key=lambda q: rel[q]))
            t = u + 1
            if not tops: continue
            pos = {}
            for i, z in enumerate(tops): pos.setdefault(z, []).append(i)
            P = {}; dep = {}
            for y in sorted(pos, key=lambda q: -rel[q]):            # most relevant first: RA(y) lies above y
                m = Counter()
                for i, j in zip(pos[y], pos[y][1:]):
                    gap = tops[i + 1:j]
                    if not gap: rec["rafail"] += 1; continue
                    z = max(gap, key=lambda q: rel[q]); m[z] += 1
                    if rel[z] <= rel[y]: rec["rafail"] += 1
                if len(pos[y]) - 1 != sum(m.values()): rec["idfail"] += 1
                P[y] = 1 + sum(P.get(z, 0) for z in m); dep[y] = 1 + max([dep.get(z, 0) for z in m] + [0])
                rec["C"] = max(rec["C"], len(pos[y])); rec["maxP"] = max(rec["maxP"], P[y]); rec["depth"] = max(rec["depth"], dep[y])
                rec["fanin"] = max(rec["fanin"], len(m)); rec["maxm"] = max(rec["maxm"], max(m.values(), default=0))
    print(os.path.basename(fn), eng, "T", T, " ".join(f"{k} {rec[k]}" for k in ("C", "maxP", "depth", "fanin", "maxm", "idfail", "rafail")), flush=True)
