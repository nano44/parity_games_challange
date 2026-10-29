#!/usr/bin/env python3
"""L-RED: port of PGSolver d3cd624 src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines; "Friedmann's
Subexponential Lower Bound for snare-based rules", the family of Friedmann DAM 161 (2013) 1317-1337 per L-LIT T46), line by line,
with SymbolicPG from experiments/hard-families/pgsolver_port.py (same index-on-first-reference semantics; byte-identical there for
switchbestexp). Usage: fsubexp.py N > game.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "hard-families"))
from pgsolver_port import SymbolicPG, mkli

EVEN, ODD = 0, 1


def name(sy):
    k = sy[0]
    t = {"DLE": "a", "DLO": "t", "CN": "d", "CC": "e", "CCB": "m", "CCBX": "q", "CNC": "u", "CBS": "v", "CBSX": "w",
         "CA": "f", "CS": "g", "CL": "h", "US": "k", "CNS": "b", "CNSX": "l", "CNSY": "p"}
    if k == "DLR": return "c"
    if k == "FS": return "z"
    if k == "FC": return "x"
    if k == "BS": return "r"
    if k == "SE": return "s"
    if len(sy) == 3: return f"{t[k]}({sy[1]},{sy[2]})"
    return f"{t[k]}{sy[1]}"


def friedmannsubexp(n):
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, name(sy))
    FC, SE, DLR, BS, FS = ("FC",), ("SE",), ("DLR",), ("BS",), ("FS",)
    DLE = lambda i: ("DLE", i); DLO = lambda i: ("DLO", i); CN = lambda i, j: ("CN", i, j); CC = lambda i: ("CC", i)
    CCB = lambda i: ("CCB", i); CCBX = lambda i: ("CCBX", i); CNC = lambda i, j: ("CNC", i, j); CBS = lambda i, j: ("CBS", i, j)
    CBSX = lambda i, j: ("CBSX", i, j); CA = lambda i: ("CA", i); CS = lambda i: ("CS", i); CL = lambda i: ("CL", i)
    US = lambda i: ("US", i); CNS = lambda i, j: ("CNS", i, j); CNSX = lambda i, j: ("CNSX", i, j); CNSY = lambda i, j: ("CNSY", i, j)
    add(FC, 1, ODD, [FC])
    add(SE, 10 * n + 8, EVEN, [FS] + mkli(n, CA))
    add(DLR, 10 * n + 6, EVEN, [SE, BS])
    add(BS, 10 * n + 10, EVEN, [FS] + mkli(n, CS))
    add(FS, 18 * n + 12, ODD, [FC])
    for i in range(3 * n):
        add(DLE(i), 4 * n + 2 * i + 6, ODD, [DLO(i)])
        add(DLO(i), 4 * n + 2 * i + 5, EVEN, [DLR, BS, SE] if i == 0 else [DLO(i - 1), BS, SE])
    for i in range(n):
        for j in range(i):
            add(CNC(i, j), 3, EVEN, [CBS(i, j), CBSX(i, j), CNS(i, j)])
            x = CC(i) if j == 0 else CNC(i, j - 1)
            add(CNS(i, j), 5, EVEN, [CNSX(i, j), CNSY(i, j), x])
            add(CNSX(i, j), 4, EVEN, [CBS(i, j)])
            add(CNSY(i, j), 4, EVEN, [CBSX(i, j)])
            add(CBS(i, j), 3, ODD, [CCB(j), x])
            add(CBSX(i, j), 2, ODD, [CCBX(j), x])
        for j in range(i + 1, n):
            add(CNC(i, j), 3, EVEN, [CBS(i, j), CBSX(i, j)])
            x = (CC(i) if i == 0 else CNC(i, j - 2)) if j == i + 1 else CNC(i, j - 1)
            add(CBS(i, j), 3, ODD, [CCB(j), x])
            add(CBSX(i, j), 2, ODD, [CCBX(j), x])
        add(CN(i, 1), 4 * i + 3, EVEN, [SE, CN(i, 0)] + mkli(3 * i + 3, DLE) + [BS])
        add(CN(i, 0), 4 * i + 3, EVEN, [SE, (CC(i) if n == 1 else CNC(i, n - 2) if i == n - 1 else CNC(i, n - 1))] + mkli(3 * i + 3, DLE) + [BS])
        add(CC(i), 4 * i + 6, ODD, [CN(i, 1), CL(i)])
        add(CCB(i), 10 * n + 11 + 2 * i, ODD, [CC(i)])
        add(CCBX(i), 12 * n + 6 * i + 15, ODD, [CL(i)])
        add(CL(i), 12 * n + 6 * i + 16, ODD, [US(i)])
        add(US(i), 12 * n + 6 * i + 11, EVEN, [FS] + mkli(n - i - 1, lambda j: CS(n - j - 1)))
        add(CA(i), 12 * n + 6 * i + 13, ODD, [CC(i)])
        add(CS(i), 4 * i + 8, EVEN, [CA(i), US(i)])
    return g.dumps()


def fearnleysubexp(n, withfearnley=True):
    """PGSolver d3cd624 fearnleysubexp.ml (86 lines; "Subexponential Lower Bound for Fearnley's rule"), line by line; -nogadget =
    withfearnley False."""
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, name(sy))
    FC, SE, DLR, BS, FS = ("FC",), ("SE",), ("DLR",), ("BS",), ("FS",)
    DLE = lambda i: ("DLE", i); DLO = lambda i: ("DLO", i); CN = lambda i, j: ("CN", i, j); CC = lambda i: ("CC", i)
    CCB = lambda i: ("CCB", i); CCBX = lambda i: ("CCBX", i); CNC = lambda i, j: ("CNC", i, j); CBS = lambda i, j: ("CBS", i, j)
    CBSX = lambda i, j: ("CBSX", i, j); CA = lambda i: ("CA", i); CS = lambda i: ("CS", i); CL = lambda i: ("CL", i)
    US = lambda i: ("US", i)
    add(FC, 1, ODD, [FC])
    add(SE, 10 * n + 6, EVEN, [FS] + mkli(n, CA))
    add(DLR, 10 * n + 4, EVEN, [SE, BS])
    add(BS, 10 * n + 8, EVEN, [FS] + mkli(n, CS))
    add(FS, 18 * n + 10, ODD, [FC])
    for i in range(3 * n):
        add(DLE(i), 4 * n + 2 * i + 4, ODD, [DLO(i)])
        add(DLO(i), 4 * n + 2 * i + 3, EVEN, [DLR, BS, SE] if i == 0 else [DLO(i - 1), BS, SE])
    for i in range(n):
        if withfearnley:
            for j in range(i + 1, n):
                add(CNC(i, j), 3, EVEN, [CBS(i, j), CBSX(i, j)])
                x = CC(i) if j == i + 1 else CNC(i, j - 1)
                add(CBS(i, j), 3, ODD, [CCB(j), x])
                add(CBSX(i, j), 2, ODD, [CCBX(j), x])
        add(CN(i, 1), 4 * i + 3, EVEN, [SE, CN(i, 0)] + mkli(3 * i + 3, DLE) + [BS])
        add(CN(i, 0), 4 * i + 3, EVEN, [SE, CC(i) if (i == n - 1 or not withfearnley) else CNC(i, n - 1)] + mkli(3 * i + 3, DLE) + [BS])
        add(CC(i), 4 * i + 4, ODD, [CN(i, 1), CL(i)])
        if withfearnley:
            add(CCB(i), 10 * n + 9 + 2 * i, ODD, [CC(i)])
            add(CCBX(i), 12 * n + 6 * i + 13, ODD, [CL(i)])
        add(CL(i), 12 * n + 6 * i + 14, ODD, [US(i)])
        add(US(i), 12 * n + 6 * i + 9, EVEN, [FS] + mkli(n - i - 1, lambda j: CS(n - j - 1)))
        add(CA(i), 12 * n + 6 * i + 11, ODD, [CC(i)])
        add(CS(i), 4 * i + 6, EVEN, [CA(i), US(i)])
    return g.dumps()


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "fearnley":
        sys.stdout.write(fearnleysubexp(int(a[1]), "-nogadget" not in a))
    else:
        sys.stdout.write(friedmannsubexp(int(a[-1])))
