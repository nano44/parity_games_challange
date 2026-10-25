#!/usr/bin/env python3
"""Box 33: classify every crossing (R_k != R_{k+1}) inside a phase (box32 rows_w, key (λ_Ξ, λ_U, τ(o))): direction (R grows / shrinks / both),
H1 at k and k+1, tame or not (R25: COARSE_{M_k}(Ξ) unchanged), whether it is in the interval [k, k'] of a rise of the used level with no
fallback (the X-charged rises of Corollary OX (iii)), the crossing switches (Even y: a -> z with a, z on different sides) and their Ξ-level
vs L_k and M_k. Usage: xclass.py game.pg ... (prints totals; -v prints every crossing)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def classify(g, acc, name, verbose=False):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    inrise = set(); prev = None
    for k in range(len(Ls)):
        if Ls[k] is None: prev = None; continue
        if Ls[k] == -2: continue
        if prev is not None and Ls[k] > Ls[prev] and not any(rows[j]["fb"] for j in range(prev, k + 1)):
            for j in range(prev, k + 1):
                if rows[j]["R"] != rows[j + 1]["R"]: inrise.add(j)
        prev = k
    for k in range(len(Ls)):
        if Ls[k] is None: continue
        a, c = rows[k], rows[k + 1]
        if a["R"] == c["R"]: continue
        R0, R1 = set(a["R"]) | {o}, set(c["R"]) | {o}
        d = ("grow" if R1 > R0 else "shrink" if R1 < R0 else "both")
        tame = all(coarse(ev[k + 1][0][v], a["M"]) == coarse(ev[k][0][v], a["M"]) for v in range(n))
        sw = []
        for y in range(n):
            if g.owner[y] == 0 and a["s"][y] != c["s"][y]:
                p, q = a["s"][y], c["s"][y]
                if (p in R0) != (q in R1) or (y in R0) != (y in R1):
                    sw.append((y, p, q, "R" if p in R0 else "F", "R" if q in R1 else "F", lev(ev[k][0][p], ev[k][0][q])))
        maxl = max([s[5] for s in sw] + [-2])
        key = f"{d}_{'H1' if a['h1'] else 'nH1'}>{'H1' if c['h1'] else 'nH1'}_{'tame' if tame else 'NONTAME'}_{'rise' if k in inrise else 'norise'}_{'fb' if a['fb'] else 'S4a'}"
        acc[key] = acc.get(key, 0) + 1
        acc["X"] = acc.get("X", 0) + 1
        lk = "xlev>L" if maxl > Ls[k] else ("xlev=L" if maxl == Ls[k] else "xlev<L")
        acc[lk] = acc.get(lk, 0) + 1
        if verbose: print(name, k, key, "L", Ls[k], "M", a["M"], "sw", sw)

if __name__ == "__main__":
    acc = {}; v = "-v" in sys.argv
    for f in [x for x in sys.argv[1:] if x != "-v"]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        try: classify(g, acc, os.path.basename(f), v)
        except Exception as e: acc["ERR"] = acc.get("ERR", 0) + 1
    for k in sorted(acc): print(k, acc[k])
