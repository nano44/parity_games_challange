#!/usr/bin/env python3
"""L-NEW box 55 (successor 33): candidate monotone quantities on sigma-bar's side along N5-SF's Even run (distinct-sigma sequence).
Per game prints: values, SBC, and
  DUALUP / DUALDN  transitions at which some vertex's G^d-valuation of sbar (sbar as Odd's strategy, valued on G^d against Even's best
                   reply, Ed.key: larger = better for Odd) goes up / down. Monotone in R15's order on G^d would need one of them = 0;
  FLIPMAX          the most sbar changes at one Odd vertex;  ENTMAX  the most entries of one Odd edge into sbar;
  BACK             sbar changes at a vertex back to a successor it used before (re-entries, summed);
  TIE              sbar-changing transitions with Xi unchanged at every vertex (tie-only changes);
  LOCTIE           sbar changes at a vertex u with Xi unchanged on every successor of u (local tie-only changes, summed);
  GAPMAX           (n+m)(1+LAM+SBC) / (values - 1), how loose SF-RED is. Usage: sbc.py GAME [START] | --list FILE"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf
from n5x import Engine, dual, load, readstart
from collections import Counter

def run(g, st, name):
    E, T = n5sf.trace(g, st); T = [x for x in T if "lam" in x]; Ed = Engine(dual(g)); n = g.n
    seq = []
    for x in T:
        if not seq or seq[-1] != x["s"]: seq.append(x["s"])
    VS = [E.evaluate(tuple(s)) for s in seq]
    SB = [[sb[v] if g.owner[v] == 1 else -1 for v in range(n)] for _, sb in VS]
    VD = [Ed.evaluate(tuple(s))[0] for s in SB]
    cls = Counter()
    for i in range(len(seq) - 1):
        u_ = any(Ed.key(VD[i + 1][v]) > Ed.key(VD[i][v]) for v in range(n)); d_ = any(Ed.key(VD[i + 1][v]) < Ed.key(VD[i][v]) for v in range(n))
        cls["MIX" if u_ and d_ else "UPONLY" if u_ else "DNONLY" if d_ else "EQ"] += 1
    valmax = max(len({tuple(VS[i][0][v]) for i in range(len(seq))}) for v in range(n))
    up = dn = sbc = tie = loctie = back = lam = 0; flips = Counter(); ent = Counter(); used = {v: {SB[0][v]} for v in range(n) if g.owner[v] == 1}
    for i in range(len(seq) - 1):
        a, b = SB[i], SB[i + 1]
        if any(Ed.key(VD[i + 1][v]) > Ed.key(VD[i][v]) for v in range(n)): up += 1
        if any(Ed.key(VD[i + 1][v]) < Ed.key(VD[i][v]) for v in range(n)): dn += 1
        if tuple(x[0] for x in VS[i][0]) != tuple(x[0] for x in VS[i + 1][0]): lam += 1
        if a != b:
            sbc += 1
            if list(VS[i][0]) == list(VS[i + 1][0]): tie += 1
            for u in range(n):
                if g.owner[u] == 1 and a[u] != b[u]:
                    flips[u] += 1; ent[(u, b[u])] += 1
                    if b[u] in used[u]: back += 1
                    used[u].add(b[u])
                    if all(VS[i][0][w] == VS[i + 1][0][w] for w in g.succ[u]): loctie += 1
    m = sum(len(set(s)) for s in g.succ)
    gap = (n + m) * (1 + lam + sbc) / max(1, len(seq) - 1)
    if os.environ.get("SHOW") and flips:
        u = max(flips, key=lambda z: (flips[z], -z)); ch = [SB[0][u]] + [SB[i + 1][u] for i in range(len(seq) - 1) if SB[i + 1][u] != SB[i][u]]
        print("FLIPVERTEX", u, "succ", sorted(set(g.succ[u])), "choices", ch)
    print("ROW", name, "n", n, "values", len(seq), "SBC", sbc, "LAM", lam, "DUALUP", up, "DUALDN", dn, "FLIPMAX", max(flips.values(), default=0),
          "ENTMAX", max(ent.values(), default=0), "VALMAX", valmax, "CLS", dict(sorted(cls.items())), "BACK", back, "TIE", tie, "LOCTIE", loctie, "GAPMAX %.1f" % gap, flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        for line in open(a[1]):
            p = line.split()
            if not p or p[0].startswith("#"): continue
            X = lambda q: os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q)
            try: run(load(X(p[0])), readstart(X(p[1])) if len(p) > 1 else None, p[0])
            except Exception as e: print("SKIP", p[0], repr(e)[:80])
    else: run(load(a[0]), readstart(a[1]) if len(a) > 1 else None, a[0])
