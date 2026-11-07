#!/usr/bin/env python3
"""over all files and all same-level pairs: the largest flips - |W(r)| and flips / |W(r)|, and check LEMMA PAIR-KF at degree 2:
KF_x = flips(wt(x,0), wt(x,1)) if the W-targets differ, 0 if equal. Usage: pairstat.py file.json ..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box167", "pmprime.py")).read().split("\nif __name__")[0])
bx = (-99, None); br = (0, None); viol = 0; checked = 0
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; g = Gen(G); S, _ = g.run(G["start"])
    except Exception: continue
    W = wclos(G); keys = [g.keys(s) for s in S]; r = measure(G)
    def fl(p, q):
        o = [k[p] < k[q] for k in keys]; return sum(a != b for a, b in zip(o, o[1:]))
    for L in set(G["lev"]):
        ms = [v for v in range(G["N"]) if G["lev"][v] == L]
        for p, q in itertools.combinations(ms, 2):
            n = fl(p, q); w = len({p, q} | W[p] | W[q])
            if n - w > bx[0]: bx = (n - w, (os.path.basename(f), p, q, n, w))
            if n / w > br[0]: br = (n / w, (os.path.basename(f), p, q, n, w))
    for x in range(G["N"]):
        if len(G["opts"][x]) != 2 or G["lev"][x] == 0: continue
        a, b = G["opts"][x][0][0], G["opts"][x][1][0]; want = fl(a, b) if a != b else 0; checked += 1
        if r["kf"][x] != want: viol += 1; print("PAIR-KF mismatch", os.path.basename(f), x, r["kf"][x], want)
print("max flips - |W|:", bx); print("max flips / |W|:", br); print("PAIR-KF checked movers", checked, "mismatches", viol)
