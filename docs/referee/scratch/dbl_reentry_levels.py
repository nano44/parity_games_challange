"""REFEREE successor 26: own measurement of DEAD-REENTRY's level sets (static Xi-graph). U_l := {xt(x, k) : lev(x) <= l, xt a mover,
lev(xt) > lev(x)}. Reading A: some y in U_l has a strict Xi-descendant of level <= l. Reading B: the same with lev(y) > l required.
Prints the failing l in 0..d-1 for each reading. Usage: dbl_reentry_levels.py FILE.json..."""
import sys, json, os
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; lev = G["lev"]; o = G["opts"]; d = max(lev) + 1
    def desc(y):
        seen = set(); st = [y]
        while st:
            x = st.pop()
            for k in range(len(o[x])):
                z = o[x][k][1]
                if z >= 0 and z not in seen: seen.add(z); st.append(z)
        return seen
    D = {y: desc(y) for y in range(N)}
    res = {}
    for rd in "AB":
        bad = []
        for l in range(d):
            U = {o[x][k][1] for x in range(N) for k in range(len(o[x])) if lev[x] <= l and o[x][k][1] >= 0 and lev[o[x][k][1]] > lev[x]}
            if rd == "B": U = {y for y in U if lev[y] > l}
            if any(lev[z] <= l for y in U for z in D[y]): bad.append(l)
        res[rd] = bad
    print(os.path.basename(f), "d", d, "reading A fails at l =", res["A"], "| reading B fails at l =", res["B"])
