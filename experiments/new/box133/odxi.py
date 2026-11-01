#!/usr/bin/env python3
"""L-NEW box 133 ODXI: for every maximal FL run (box132/anchor.py's detection), the Xi-changes at ODIFF vertices inside the run and the
FL moves they release. A move of x at transition j-1 -> j is GATE-RELEASED if its new option y was not Xi-improving over x's current
option at state j-2 but is at state j-1, and an ODIFF vertex on y's Xi-play prefix (Lemma PREFIX: up to the first ODIFF vertex or
W-cycle node) changed its Xi between j-2 and j-1. Also: tau and sbar constant at every ODIFF vertex over the run (TWO-FIX), W(x)
unchanged. Prints ODXI <game> n RUNS FL XICH_ODIFF (Xi-changes at ODIFF vertices inside runs) GATEREL (gate-released FL moves)
EXAMPLES (run, j, mover, old, new, gate).
Usage: odxi.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box132", "anchor.py")).read().split("R = dict(runs")[0]
exec(src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.join(HERE, "..", "box132"))))
xich = rel = fl = 0; ex = []
for a, b in runs:
    tau = T[a]; W = wval(a); fl += b - a
    XS = {j: E.evaluate(S[j]) for j in range(max(a - 1, 0), b + 1)}
    od = lambda j: {o for o in range(n) if own[o] == 1 and XS[j][1][o] != tau[o]}
    for j in range(a + 1, b + 1):
        xich += sum(XS[j][0][o] != XS[j - 1][0][o] for o in od(j - 1) & od(j))
    for j in range(a + 2, b + 1):
        v1, sb1 = XS[j - 1]; v2, _ = XS[j - 2]
        sX = [S[j - 1][v] if own[v] == 0 else sb1[v] for v in range(n)]
        for x in range(n):
            if own[x] or S[j][x] == S[j - 1][x]: continue
            y, z = S[j][x], S[j - 1][x]
            if E.key(v2[y]) > E.key(v2[z]) or not E.key(v1[y]) > E.key(v1[z]): continue
            u = y; seen = set(); gate = None
            while u not in seen and W[u][2] > 0:
                seen.add(u)
                if u in od(j - 1):
                    gate = u if v1[u] != v2[u] else None; break
                u = sX[u]
            if gate is not None:
                rel += 1
                if len(ex) < 5: ex.append((a, j, x, z, y, gate))
print(f"ODXI {os.path.basename(sys.argv[1])} n {n} RUNS {len(runs)} FL {fl} XICH_ODIFF {xich} GATEREL {rel}" + (f" EX {ex}" if ex else ""))
