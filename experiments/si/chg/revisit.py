#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §7): per maximal REL segment [a, b], how often one Even vertex v switches INTO one successor c
(ENTER(v, c)), and MAXV (switches of one vertex) against its out-degree. Lemma SW-RETURN: a second entry into c needs Xi(c) to rise in
between. Candidates: ENTER2 (ENTER(v, c) <= 2), DEG (MAXV(v) <= out-degree(v)), DEG2 (MAXV(v) <= 2 out-degree(v)).
Usage: revisit.py --list FILE | --one GAME [START]   (START=1 reads list column 2)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from suffix import rows, load, readstart
import seglast
C = Counter(); EX = []

def _run(g, R, name):
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        ent = Counter(); sw = Counter()
        for t in range(a, b):
            for v in range(g.n):
                if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: ent[(v, R[t + 1]["s"][v])] += 1; sw[v] += 1
        if not sw: continue
        C["segs"] += 1; m = max(ent.values()); C["enter_max_%d" % m] += 1
        if m > 2: C["ENTER2_V"] += 1; EX.append(("ENTER2", name, a, b, [k for k in ent if ent[k] == m][:3], m))
        for v, k in sw.items():
            d = len(set(g.succ[v]))
            if k > d: C["DEG_V"] += 1; EX.append(("DEG", name, a, b, v, k, d))
            if k > 2 * d: C["DEG2_V"] += 1
        C["maxv_max"] = max(C["maxv_max"], max(sw.values()))

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:8]: print("EXAMPLE", z)
    for k in ("ENTER2", "DEG", "DEG2"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
