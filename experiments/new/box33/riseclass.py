#!/usr/bin/env python3
"""Box 33: classify the rises of the used level (consecutive relevant k < k', L_{k'} > L_k) with no fallback in [k, k'] by:
crossing at k / at k' / at an NU transition between; who attains L_{k'} (E: an Even switch; O: σ̄(o)); for Even, whether the attaining
switch is itself a crossing switch (ends on different sides of R) and the sides of its ends; whether the transition is tame; H1 at k'.
Usage: riseclass.py game.pg ... (-v prints each X-rise)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def rclass(g, acc, name, verbose=False):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    X = lambda j: rows[j]["R"] != rows[j + 1]["R"]
    prev = None
    for k in range(len(Ls)):
        if Ls[k] is None: prev = None; continue
        if Ls[k] == -2: continue
        if prev is not None and Ls[k] > Ls[prev] and not any(rows[j]["fb"] for j in range(prev, k + 1)):
            xs = [j for j in range(prev, k + 1) if X(j)]
            if not xs: acc["rise_noX"] = acc.get("rise_noX", 0) + 1
            else:
                a, c = rows[k], rows[k + 1]; R0, R1 = set(a["R"]) | {o}, set(c["R"]) | {o}; X0 = ev[k][0]
                att = []
                for y in range(n):
                    if g.owner[y] == 0 and a["s"][y] != c["s"][y] and X0[y][0] != y and lev(X0[a["s"][y]], X0[c["s"][y]]) == Ls[k]:
                        p, q = a["s"][y], c["s"][y]; att.append("E:" + ("R" if p in R0 else "F") + ("R" if q in R1 else "F") + ("y" + ("R" if y in R0 else "F") + ("R" if y in R1 else "F")))
                if ev[k][1][o] != ev[k + 1][1][o] and X0[o][0] != o and lev(X0[ev[k][1][o]], X0[ev[k + 1][1][o]]) == Ls[k]: att.append("O")
                tame = all(coarse(ev[k + 1][0][v], a["M"]) == coarse(X0[v], a["M"]) for v in range(n))
                where = "+".join(sorted(set("k" if j == prev else "k'" if j == k else "nu" for j in xs)))
                key = f"riseX_at[{where}]_by[{','.join(sorted(set(att)))}]_{'tame' if tame else 'NONTAME'}_{'H1' if a['h1'] else 'nH1'}"
                acc[key] = acc.get(key, 0) + 1
                if verbose: print(name, prev, k, Ls[prev], Ls[k], key)
        prev = k

if __name__ == "__main__":
    acc = {}; v = "-v" in sys.argv
    for f in [x for x in sys.argv[1:] if x != "-v"]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        try: rclass(g, acc, os.path.basename(f), v)
        except Exception: acc["ERR"] = acc.get("ERR", 0) + 1
    for k in sorted(acc): print(k, acc[k])
