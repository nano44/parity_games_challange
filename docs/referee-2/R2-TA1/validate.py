#!/usr/bin/env python3
"""Check the REFEREE-2 implementations against the worked examples of HKP arXiv 1405.0386v2 (Fig. 1 with Examples 1-4
and the psolQ example; Fig. 4(a)/(b) with Example 5; Fig. 6 'modified by neither psol, psolB nor psolQ') and against
the three instances named in docs/attr/TA1-proof.md / A1-results.md.  Games are transcribed from the tikz source in
archiv.tex (circle = V_0 = Even, square = V_1 = Odd), min-parity colours converted by pr = M - c with M even."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import *

def from_min(cols, owners, edges, M):
    n = len(cols)
    succ = [[] for _ in range(n)]
    for a, b in edges:
        succ[a].append(b)
    return Game([M - c for c in cols], owners, succ)

E, O = 0, 1
fails = 0
def check(name, cond, info=""):
    global fails
    print(("ok   " if cond else "FAIL ") + name + (("  " + str(info)) if info else ""))
    if not cond:
        fails += 1

# Fig. 1 (tex:437-480): colours and owners from the \Vertex lines, edges from \Edge lines (<-> = both directions)
cols = [9, 0, 14, 17, 6, 20, 15, 19, 4, 8, 11, 18]
own = [O, O, E, E, O, E, E, O, O, E, E, O]
ed = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 5), (5, 3), (4, 6), (6, 5), (7, 5), (5, 7), (6, 8), (8, 6), (9, 8), (8, 9),
      (10, 9), (9, 11), (10, 11), (11, 10)]
g1 = from_min(cols, own, ed, 20)
assert colours(g1) == cols
WE, WO = zielonka(g1)
check("Fig.1 Example 1 regions", WO == {3, 5, 7} and WE == set(range(12)) - {3, 5, 7}, (sorted(WE), sorted(WO)))
lg = []
win, res = psolB_hkp(g1, log=lg)
check("Fig.1 psolB: first removal at colour 8 = {v9,v10,v11}", lg[0][0] == 8 and lg[0][3] == [9, 10, 11], lg[0])
check("Fig.1 psolB: second removal at colour 4, MAttr {v2,v4,v6,v8}, plus v0,v1", lg[1][0] == 4 and lg[1][2] == [2, 4, 6, 8] and lg[1][3] == [0, 1, 2, 4, 6, 8], lg[1])
check("Fig.1 psolB residual {v3,v5,v7}", res == {3, 5, 7}, sorted(res))
lq = []
win, res = psolQ_hkp(g1, log=lq)
check("Fig.1 psolQ: fatal at b=4 removes all but v3,v5,v7; then b=19; empty residual",
      [x[0] for x in lq] == [4, 19] and lq[0][3] == sorted(set(range(12)) - {3, 5, 7}) and not res, lq)
check("Fig.1 psolB_max agrees with psolB_hkp", psolB_max(g1)[1] == {3, 5, 7})
# Example 2: MAttr(4) and MAttr(8) in the full game
c = colours(g1)
check("Fig.1 Example 2 MAttr(4) = {v2,v4,v6,v8,v9,v10,v11}", mattr_hkp(g1, c, frozenset(range(12)), {8}, 4, 0) == {2, 4, 6, 8, 9, 10, 11})
check("Fig.1 Example 2 MAttr(8) = {v9,v10,v11}", mattr_hkp(g1, c, frozenset(range(12)), {9}, 8, 0) == {9, 10, 11})
check("Fig.1 Example 2 v11 in MAttr(11), v10 not", 11 in mattr_hkp(g1, c, frozenset(range(12)), {10}, 11, 1) and 10 not in mattr_hkp(g1, c, frozenset(range(12)), {10}, 11, 1))
# PA** on Fig.1: psolB does not solve it, so T-A1 predicts PA** false
check("Fig.1 PA** false (T-A1 prediction, psolB residual non-empty)", pa2(g1, WE, WO) is False)

# Fig. 4(a) (tex:812-840)
g4a = from_min([3, 2, 0, 2, 3], [E, O, E, O, E], [(0, 1), (1, 2), (3, 2), (4, 3), (1, 0), (2, 1), (3, 4), (2, 3)], 4)
WE, WO = zielonka(g4a)
check("Fig.4(a) Even wins all", WE == set(range(5)))
check("Fig.4(a) Example 5: psolB decides no node", psolB_hkp(g4a)[1] == set(range(5)))
check("Fig.4(a) psolQ solves completely (lane's claim, used for the psolQ 'iff' counterexample)", psolQ_hkp(g4a)[1] == set())
check("Fig.4(a) PA** false", pa2(g4a, WE, WO) is False)
# Fig. 4(b)
g4b = from_min([0, 1, 0], [E, O, E], [(0, 1), (1, 0), (2, 1), (1, 2)], 2)
WE, WO = zielonka(g4b)
check("Fig.4(b) Example 5: psolB decides all nodes at d=0 for X={v0,v2}", psolB_hkp(g4b)[1] == set() and WE == {0, 1, 2})
check("Fig.4(b) PA** true", pa2(g4b, WE, WO) is True)
# Fig. 6 (tex:1104-1189), all squares = Odd
g6 = from_min([0, 1, 3, 3, 2, 1, 1, 0], [O] * 8, [(0, 1), (1, 0), (1, 2), (2, 4), (3, 4), (4, 3), (4, 5), (5, 7), (6, 7), (7, 6), (7, 1)], 4)
WE, WO = zielonka(g6)
check("Fig.6 Even wins all (1-player game for Odd, every cycle has even min colour)", WE == set(range(8)))
check("Fig.6 untouched by psolB", psolB_hkp(g6)[1] == set(range(8)))
check("Fig.6 untouched by psolQ", psolQ_hkp(g6)[1] == set(range(8)))
check("Fig.6 PA** false", pa2(g6, WE, WO) is False)
check("Fig.6 max-parity transcription matches L-ATTR's (4,3,1,1,2,3,3,4)", g6.pr == [4, 3, 1, 1, 2, 3, 3, 4])

# Instances named by the lane (transcribed from the text of A1-results.md, not read from their files)
gmin = parse_pg("0 1 0 0,1; 1 3 0 2; 2 2 0 0;")
WE, WO = zielonka(gmin)
check("psolq_min_n3_m4: Odd wins all; psolB, psolQ undecided; PA** false",
      WO == {0, 1, 2} and psolB_hkp(gmin)[1] == {0, 1, 2} and psolQ_hkp(gmin)[1] == {0, 1, 2} and pa2(gmin, WE, WO) is False)
gl = parse_pg("0 1 0 0; 1 2 1 0; 2 1 0 2,1;")      # L-LIT witness: v pr1 -> v; x pr2 Odd -> v; w pr1 Even -> w,x
WE, WO = zielonka(gl)
check("llit_witness_buchi_n3: psolB solves; PA* true; PA** true", psolB_hkp(gl)[1] == set() and pa2(gl, WE, WO, star=True) and pa2(gl, WE, WO))
gs = parse_pg("0 3 0 0; 1 1 0 0; 2 1 0 0,2;")
WE, WO = zielonka(gs)
check("SCC-constant witness: Odd wins all; psolB solves; PA* false; PA** true",
      WO == {0, 1, 2} and psolB_hkp(gs)[1] == set() and pa2(gs, WE, WO, star=True) is False and pa2(gs, WE, WO) is True)
print("validate.py:", "ALL OK" if fails == 0 else f"{fails} FAILURES")
sys.exit(1 if fails else 0)
