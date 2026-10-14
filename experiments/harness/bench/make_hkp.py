#!/usr/bin/env python3
"""Huth-Kuo-Piterman witnesses (arXiv 1405.0386v2, LaTeX e-print archiv.tex, opened 2026-10-14), hand-encoded from
the hidden tikz source of each figure (vertex colour, shape, edges). HKP use MIN-parity (archiv.tex:225) and draw V_0
(player 0 = Even) as circles, V_1 as squares (archiv.tex:342-343). Converted to max-parity with p = M - c, M = max
colour rounded up to even (order reversed, parity kept). Writes hkp_fig4a.pg, hkp_fig4b.pg, hkp_fig6.pg here."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import pg

FIGS = {
    # Fig. 6 (archiv.tex:1164-1194): all squares (player 1); "modified by neither psol, psolB nor psolQ"
    "hkp_fig6": dict(col=[0, 1, 3, 3, 2, 1, 1, 0], own=[1] * 8,
                     edges=[(0, 1), (1, 0), (1, 2), (2, 4), (3, 4), (4, 3), (4, 5), (5, 7), (6, 7), (7, 6), (7, 1)]),
    # Fig. 4(a) (archiv.tex:815-840): v0 circle 3, v1 square 2, v2 circle 0, v3 square 2, v4 circle 3
    "hkp_fig4a": dict(col=[3, 2, 0, 2, 3], own=[0, 1, 0, 1, 0],
                      edges=[(0, 1), (1, 2), (3, 2), (4, 3), (1, 0), (2, 1), (3, 4), (2, 3)]),
    # Fig. 4(b) (archiv.tex:846-855): v0 circle 0, v1 square 1, v2 circle 0, edges v0<->v1, v2<->v1
    "hkp_fig4b": dict(col=[0, 1, 0], own=[0, 1, 0], edges=[(0, 1), (1, 0), (2, 1), (1, 2)]),
}
for name, f in FIGS.items():
    M = max(f["col"]) + (max(f["col"]) % 2)
    succ = [[] for _ in f["col"]]
    for a, b in f["edges"]:
        succ[a].append(b)
    g = pg.Game([M - c for c in f["col"]], f["own"], succ, labels=[f"v{i}" for i in range(len(f["col"]))])
    pg.write(g, os.path.join(HERE, name + ".pg"))
    print("wrote", name)
