#!/usr/bin/env python3
"""L-COMP box 38: U(G), implemented from the TEXT of P-N5-ASC §6 l. 179-180 (Corollary UP-B; landed as RESULTS R121 (g),
docs/RESULTS.md l. 14320 / l. 14505-14506 on trunk 86f62c26): «Let U(G) := the number of options (x, k) whose Ξ-target is a mover of
level > lev(x).» Genome format (R104 / eg195): opts[x][k] = [wt, xt, b]; xt = -1 is K0 (not a mover), xt >= 0 a mover.
Cross-check: L-NEW's ug193.py / qt3_196.py use the same one-line formula (compared in check38: equal on every pinned file)."""
def U(G):
    lev = G["lev"]
    return sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])

def NM(G): return G["N"] + sum(len(o) for o in G["opts"])

if __name__ == "__main__":
    import sys, json, os
    for f in sys.argv[1:]:
        G = json.load(open(f)); print(f"{os.path.basename(f)} U {U(G)} N+M {NM(G)}")
