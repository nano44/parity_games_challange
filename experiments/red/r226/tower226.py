#!/usr/bin/env python3
"""L-RED 60 R226 (Lead 14:45Z design attempt): TOWER HIGH under GROW7's replaying low race.
G = union(GROW7, HP) (compose226.union, gate / beta placement gm); then rewire ONE option of GROW7's High source x17 (or of x18) so its
Xi-target is a tower mover y (every y). Score A (= max(1, maxalt)), #tops, T (own.py, [E-LEV], cap 3000). Prints the top rows and the
A histogram; freezes the best to out/tower_<tag>.json. Usage: tower226.py GROW7.json HP.json TAG"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import union, rewire, check
import own
from asc226 import alt
def ascore(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; best = (0, 0)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            prev = None; tops = []
            for i in range(t, u + 1):
                E = frozenset(e for e in out[i][1][v][1] if e in evs)
                if prev is not None and E != prev: tops.append(max(E ^ prev, key=lambda e: rk[e]))
                prev = E
            if tops: best = max(best, (max(1, alt(tops)), len(tops)))
            t = u + 1
    return best[0], best[1], T
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); TAG = sys.argv[3]; NA = A["N"]; rows = []; best = None
for gm in ("below", "above"):
    G0 = union(A, B, gm); a0 = ascore(G0); rows.append((a0, gm, "base"))
    for x in (17, 18):
        for k in range(len(G0["opts"][x])):
            for y in range(NA, G0["N"]):
                G = rewire(G0, x, k, 1, y)
                try: check(G); a = ascore(G)
                except Exception: continue
                rows.append((a, gm, (x, k, y)))
                if best is None or a > best[0]: best = (a, gm, (x, k, y)); json.dump(G, open(f"out/tower_{TAG}.json", "w")); print("NEW", a, gm, (x, k, y), flush=True)
rows.sort(key=lambda r: r[0], reverse=True)
print("TOP", rows[:10]); print("A hist", sorted(collections.Counter(r[0][0] for r in rows).items())); print("BEST", best, flush=True)
