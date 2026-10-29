#!/usr/bin/env python3
"""Faithful Python port of PGSolver generators (Friedmann's lower-bound families).

Source: github.com/tcsprojects/pgsolver, commit d3cd624b61cd66739c45aff9554f6bbdcdd05401 (2026-01-10).
Each function cites the OCaml file and line numbers it transcribes. Conventions taken from the same commit:
  src/lib/paritygame/paritygame.ml:130-139  plr_Even = 0, plr_Odd = 1, plr_benefits pr = pr mod 2
  src/lib/paritygame/paritygame.ml:33-53    successor sets are TreeSets (printed sorted, duplicates merged)
  src/lib/paritygame/paritygame.ml:365-386  output: 'parity <n-1>;' then 'i pr pl succs "desc";'
  src/lib/generators/policyiter/stratimprgenerators.ml:11-50  SymbolicParityGame: a symbol gets the next index
      the first time it is mentioned (as a node or as an edge target); add_node overrides the data of a touched symbol.
Usage: pgsolver_port.py GENERATOR N   (GENERATOR in: recursiveladder switchallexp switchbestexp friedmannsubexp fearnleysubexp
       fearnleysubexp-nogadget; the last three added 2026-10-29, L-COMP box 21)
Checked 2026-10-15 against the original binaries at d3cd624: byte-identical output for N = 1..6, 8, 10, 16
(pgsolver-binary-diff.md)."""
import sys


class SymbolicPG:
    """Port of stratimprgenerators.ml:11-50 (SymbolicParityGame)."""
    def __init__(self):
        self.idx, self.data, self.succ = {}, [], []

    def _internal_add(self, sym, pr, pl, desc, override):  # lines 30-38
        if sym in self.idx:
            i = self.idx[sym]
            if override:
                self.data[i] = (pr, pl, desc)
            return i
        i = len(self.idx)
        self.idx[sym] = i
        self.data.append((pr, pl, desc)); self.succ.append(set())
        return i

    def add_node(self, sym, pr, pl, tr, desc):  # lines 43-48
        i = self._internal_add(sym, pr, pl, desc, True)
        for s2 in tr:
            j = self._internal_add(s2, -1, 0, None, False)
            self.succ[i].add(j)

    def dumps(self):  # to_paritygame (lines 20-28) + output_game (paritygame.ml:365-386)
        n = len(self.data)
        out = [f"parity {n - 1};"]
        for i in range(n):
            pr, pl, desc = self.data[i]
            if pr >= 0 and 0 <= pl <= 1:
                d = f' "{desc}"' if desc else ""
                out.append(f"{i} {pr} {pl} {','.join(map(str, sorted(self.succ[i])))}{d};")
        return "\n".join(out) + "\n"


def mkli(n, f):
    return [f(j) for j in range(n)]


EVEN, ODD = 0, 1


def recursiveladder(arg):
    """src/lib/generators/recursiveladder.ml:3-46 ("Recursive Ladder Game"), Friedmann's lower bound for the
    recursive (Zielonka) algorithm (paper reference: awaiting source). Uses pg_create, not SymbolicParityGame."""
    height = 1 + arg                                     # line 13
    w = 5                                                # line 15
    size = 5 * height - 5                                # line 17
    prio, own, succ, desc = [-1] * size, [-1] * size, [set() for _ in range(size)], [None] * size
    for i in range(height):                              # line 19
        start_idx = i * w - 2                            # line 20
        p = (i + 1) * 3 + 2                              # line 21
        start_pl = i % 2                                 # line 22
        o = 1 - start_pl                                 # line 23
        mx = i == height - 1                             # line 24
        mfx = i == height - 2                            # line 25
        mn = i == 0                                      # line 26

        def prnt(j, pr, pl, succs):                      # lines 28-33
            j2 = start_idx + j
            prio[j2] = pr
            own[j2] = (start_pl + pl) % 2                # plr_benefits (start_pl + pl)
            desc[j2] = str(start_idx + j)                # nd_show
            for x in succs:
                succ[j2].add(x + start_idx)
        if not mn:                                       # lines 36-39
            prnt(0, o, 1, [3 - w, 1])
            prnt(1, o, 0, [0] if mx else [0, 2])
        if not mx:                                       # lines 40-44
            prnt(2, p, 1, [w + 1, 3])
            prnt(3, p - 1, 0, ([] if mn else [3 - w]) + ([] if mfx else [w + 3]) + [4])
            prnt(4, p - 2, 1, [3] if mx else [3, w + 1])
    out = [f"parity {size - 1};"]
    for i in range(size):
        if prio[i] >= 0 and 0 <= own[i] <= 1:
            out.append(f'{i} {prio[i]} {own[i]} {",".join(map(str, sorted(succ[i])))} "{desc[i]}";')
    return "\n".join(out) + "\n"


def switchallexp(n):
    """src/lib/generators/policyiter/generators/switchallexp.ml:33-67, ident "switchallexp",
    "Exponential Lower Bound for (Voege's) switch-all rule" (line 72)."""
    S = lambda *a: a
    lab = {"DecLaneEven": "a", "DecLaneOdd": "b", "DecLaneOddRoot": "d", "CycleNode": "e", "CycleToLaneEven": "f",
           "CycleToLaneOdd": "g", "CycleCenter": "h", "CycleAccess": "k", "CycleSelector": "l",
           "CycleSelectorDecelerator": "r", "CycleLeaver": "m", "UpperSelector": "z", "UpperSelectorHelper": "v",
           "FinalSink": "p", "FinalCycle": "q", "StartEven": "s", "StartSelector": "t", "HighEntryBit": "w",
           "LowestBit": "y", "BitSelector": "x"}                       # symb_to_str, line 26
    g = SymbolicPG()  # SymbolicParityGame.create_new FinalCycle (line 39): the argument is unused, tables start empty
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, lab[sy[0]] + (str(sy[1]) if len(sy) > 1 else ""))
    FinalCycle, StartEven, StartSelector, LowestBit, HighEntryBit = S("FinalCycle"), S("StartEven"), S("StartSelector"), S("LowestBit"), S("HighEntryBit")
    DecLaneOddRoot, BitSelector, FinalSink = S("DecLaneOddRoot"), S("BitSelector"), S("FinalSink")
    DLE = lambda i: S("DecLaneEven", i); DLO = lambda i: S("DecLaneOdd", i); CN = lambda i: S("CycleNode", i)
    CTE = lambda i: S("CycleToLaneEven", i); CTO = lambda i: S("CycleToLaneOdd", i); CC = lambda i: S("CycleCenter", i)
    CL = lambda i: S("CycleLeaver", i); US = lambda i: S("UpperSelector", i); CA = lambda i: S("CycleAccess", i)
    CS = lambda i: S("CycleSelector", i); CSD = lambda i: S("CycleSelectorDecelerator", i); USH = lambda i: S("UpperSelectorHelper", i)
    add(FinalCycle, 1, ODD, [FinalCycle])                                                     # line 41
    add(StartEven, 2, EVEN, [FinalSink] + mkli(n, CA))                                        # line 42
    add(StartSelector, 3, EVEN, [BitSelector, StartEven])                                     # line 43
    add(LowestBit, 5, EVEN, [HighEntryBit, CS(0)])                                            # line 44
    add(HighEntryBit, 7, EVEN, [LowestBit, FinalSink] + mkli(n - 1, lambda j: CS(j + 1)))    # line 45
    add(DecLaneOddRoot, 12 * n + 8, EVEN, [StartSelector, BitSelector])                       # line 46
    add(BitSelector, 12 * n + 10, EVEN, [HighEntryBit, LowestBit])                            # line 47
    add(FinalSink, 16 * n + 12, ODD, [FinalCycle])                                            # line 48
    for i in range(2 * n):                                                                    # lines 50-53
        add(DLE(i), 8 * n + 2 * i + 8, ODD, [DLO(i)])
        add(DLO(i), 8 * n + 2 * i + 7, EVEN, [DecLaneOddRoot if i < 2 else DLO(i - 1), BitSelector, StartEven])
    for i in range(n):                                                                        # lines 55-66
        add(CN(i), 6 * n + 2 * i + 7, EVEN, [DLE(0), BitSelector, StartEven, CC(i), CTE(i), CTO(i)])
        add(CTE(i), 6 * i + 8, EVEN, ([] if i == 0 else [CTE(i - 1)]) + [DecLaneOddRoot, DLE(2 * i)])
        add(CTO(i), 6 * i + 10, EVEN, ([] if i == 0 else [CTO(i - 1)]) + [DecLaneOddRoot, DLE(2 * i + 1)])
        add(CC(i), 6 * n + 2 * i + 8, ODD, [CN(i), CL(i)])
        add(CL(i), 12 * n + 4 * i + 14, ODD, [US(i)])
        add(US(i), 12 * n + 4 * i + 11, EVEN, [FinalSink] if i == n - 1 else [FinalSink, USH(i)])
        add(CA(i), 12 * n + 4 * i + 13, ODD, [CC(i)])
        add(CS(i), 6 * i + 11, EVEN, [CA(i), US(i)])
        add(CSD(i), 6 * i + 12, EVEN, [CS(i), US(i)])
        if i < n - 1:
            add(USH(i), 6 * i + 9, EVEN, [FinalSink, CSD(n - 1)] if i == n - 2 else [USH(i + 1), CSD(i + 1)])
    return g.dumps()


def switchbestexp(n):
    """src/lib/generators/policyiter/generators/switchbestexp.ml:35-73 (its description string at line 79 reads
    "Exponential Lower Bound for (Voege's) switch-all rule", apparently copied; the ident is "switchbestexp")."""
    lab = {"DecLaneEven": "a", "DecLaneOdd": "b", "DecLaneOddRoot": "d", "CycleNode0": "e", "CycleNode1": "f",
           "CycleNode2": "g", "CycleNodeToLane0": "e'", "CycleNodeToLane1": "f'", "CycleNodeToLane2": "g'",
           "CycleCenter": "h", "CycleAccessDistributer": "c", "CycleAccess": "k", "CycleSelector": "l",
           "CycleSelectorDecelerator": "r", "CycleLeaver": "m", "UpperSelector": "z", "UpperSelectorHelper": "v",
           "FinalSink": "p", "FinalCycle": "q", "StartEven": "s", "StartSelector": "t", "HighEntryBit": "w",
           "LowestBit": "y", "BitSelector": "x"}                       # symb_to_str, line 29
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, lab[sy[0]] + (str(sy[1]) if len(sy) > 1 else ""))
    S = lambda *a: a
    FinalCycle, StartEven, StartSelector, LowestBit, HighEntryBit = S("FinalCycle"), S("StartEven"), S("StartSelector"), S("LowestBit"), S("HighEntryBit")
    DecLaneOddRoot, BitSelector, FinalSink, CAD = S("DecLaneOddRoot"), S("BitSelector"), S("FinalSink"), S("CycleAccessDistributer")
    f = lambda name: (lambda i: S(name, i))
    DLE, DLO, CN0, CN1, CN2 = f("DecLaneEven"), f("DecLaneOdd"), f("CycleNode0"), f("CycleNode1"), f("CycleNode2")
    CL0, CL1, CL2, CC = f("CycleNodeToLane0"), f("CycleNodeToLane1"), f("CycleNodeToLane2"), f("CycleCenter")
    CLv, US, CA, CS, CSD, USH = f("CycleLeaver"), f("UpperSelector"), f("CycleAccess"), f("CycleSelector"), f("CycleSelectorDecelerator"), f("UpperSelectorHelper")
    add(FinalCycle, 1, ODD, [FinalCycle])                                                     # line 43
    add(StartEven, 2, EVEN, [FinalSink, CAD])                                                 # line 44
    add(StartSelector, 3, EVEN, [BitSelector, StartEven])                                     # line 45
    add(CAD, 4, EVEN, mkli(n, CA))                                                            # line 46
    add(LowestBit, 5, EVEN, [HighEntryBit, CS(0)])                                            # line 47
    add(HighEntryBit, 7, EVEN, [LowestBit, FinalSink] + mkli(n - 1, lambda j: CS(j + 1)))    # line 48
    add(DecLaneOddRoot, 24 * n + 12, EVEN, [StartSelector, BitSelector])                      # line 49
    add(BitSelector, 24 * n + 14, EVEN, [HighEntryBit, LowestBit])                            # line 50
    add(FinalSink, 26 * n + 16, ODD, [FinalCycle])                                            # line 51
    for i in range(6 * n + 1):                                                                # lines 53-56 (0..6n inclusive)
        add(DLE(i), 12 * n + 2 * i + 10, ODD, [DLO(i)])
        add(DLO(i), 12 * n + 2 * i + 9, EVEN, [DecLaneOddRoot if i < 2 else DLO(i - 1), BitSelector, StartEven])
    for i in range(n):                                                                        # lines 58-72
        add(CN0(i), 6 * n + 6 * i + 9, EVEN, [CN1(i), DecLaneOddRoot, CL0(i)])
        add(CN1(i), 6 * n + 6 * i + 11, EVEN, [CN2(i), CAD, CL1(i), DLE(6 * i + 4)])
        add(CN2(i), 6 * n + 6 * i + 13, EVEN, [DLE(0), CC(i), CL2(i)])
        add(CL0(i), 6 * i + 8, EVEN, ([] if i == 0 else [CL0(i - 1)]) + [DecLaneOddRoot, DLE(6 * i + 2), DLE(6 * i + 5)])
        add(CL1(i), 6 * i + 10, EVEN, ([] if i == 0 else [CL1(i - 1)]) + [DecLaneOddRoot, DLE(6 * i + 1)] + ([DLE(6 * i + 4)] if i < n - 1 else []))
        add(CL2(i), 6 * i + 12, EVEN, ([] if i == 0 else [CL2(i - 1)]) + [DecLaneOddRoot, DLE(6 * i + 3), DLE(6 * i + 6)])
        add(CC(i), 6 * n + 6 * i + 14, ODD, [CN0(i), CLv(i)])
        add(CLv(i), 24 * n + 4 * i + 18, ODD, [US(i)])
        add(US(i), 24 * n + 4 * i + 15, EVEN, [FinalSink] if i == n - 1 else [FinalSink, USH(i)])
        add(CA(i), 24 * n + 4 * i + 17, ODD, [CC(i)])
        add(CS(i), 6 * i + 11, EVEN, [CA(i), US(i)])
        add(CSD(i), 6 * i + 13, EVEN, [CS(i), US(i)])
        if i < n - 1:
            add(USH(i), 6 * i + 9, EVEN, [FinalSink, CSD(n - 1)] if i == n - 2 else [USH(i + 1), CSD(i + 1)])
    return g.dumps()


def _desc(sy):
    """symb_to_str of friedmannsubexp.ml:31 / fearnleysubexp.ml:28 (same letters; b, l, p only in friedmannsubexp)."""
    k = sy[0]
    if k in ("c", "z", "x", "s", "r"):
        return k
    if len(sy) == 2:
        return f"{k}{sy[1]}"
    return f"{k}({sy[1]},{sy[2]})"


def friedmannsubexp(n):
    """src/lib/policyiter/generators/friedmannsubexp.ml (d3cd624): "Friedmann's Subexponential Lower Bound for snare-based rules".
    Symbols are tuples (letter, ints) with the .ml's letters: a DecLaneEven, t DecLaneOdd, c DecLaneRoot, d CycleNode, e CycleCenter,
    m CycleCenterBadEntry, q CycleCenterBadEntryX, u CycleNodeCho, v CycleBadEntrySel, w CycleBadEntrySelX, f CycleAccess,
    g CycleSelector, h CycleLeaver, k UpperSelector, z FinalSink, x FinalCycle, r BitSelector, s StartEven, b CycleNodeSpecial,
    l CycleNodeSpecialX, p CycleNodeSpecialY."""
    g = SymbolicPG()  # create_new FinalCycle: argument unused (stratimprgenerators.ml)
    X, S, C, R, Z = ("x",), ("s",), ("c",), ("r",), ("z",)
    a = lambda i: ("a", i); t = lambda i: ("t", i); d = lambda i, j: ("d", i, j); e = lambda i: ("e", i); m = lambda i: ("m", i)
    q = lambda i: ("q", i); u = lambda i, j: ("u", i, j); v = lambda i, j: ("v", i, j); w = lambda i, j: ("w", i, j); f = lambda i: ("f", i)
    gs = lambda i: ("g", i); h = lambda i: ("h", i); k = lambda i: ("k", i); b = lambda i, j: ("b", i, j); l = lambda i, j: ("l", i, j)
    p = lambda i, j: ("p", i, j)

    def add(sy, pr, pl, li):
        g.add_node(sy, pr, pl, li, _desc(sy))
    add(X, 1, ODD, [X])
    add(S, 10 * n + 8, EVEN, [Z] + mkli(n, f))
    add(C, 10 * n + 6, EVEN, [S, R])
    add(R, 10 * n + 10, EVEN, [Z] + mkli(n, gs))
    add(Z, 18 * n + 12, ODD, [X])
    for i in range(3 * n):
        add(a(i), 4 * n + 2 * i + 6, ODD, [t(i)])
        add(t(i), 4 * n + 2 * i + 5, EVEN, [C, R, S] if i == 0 else [t(i - 1), R, S])
    for i in range(n):
        for j in range(i):
            add(u(i, j), 3, EVEN, [v(i, j), w(i, j), b(i, j)])
            x = e(i) if j == 0 else u(i, j - 1)
            add(b(i, j), 5, EVEN, [l(i, j), p(i, j), x])
            add(l(i, j), 4, EVEN, [v(i, j)])
            add(p(i, j), 4, EVEN, [w(i, j)])
            add(v(i, j), 3, ODD, [m(j), x])
            add(w(i, j), 2, ODD, [q(j), x])
        for j in range(i + 1, n):
            add(u(i, j), 3, EVEN, [v(i, j), w(i, j)])
            x = (e(i) if i == 0 else u(i, j - 2)) if j == i + 1 else u(i, j - 1)
            add(v(i, j), 3, ODD, [m(j), x])
            add(w(i, j), 2, ODD, [q(j), x])
        add(d(i, 1), 4 * i + 3, EVEN, [S, d(i, 0)] + mkli(3 * i + 3, a) + [R])
        add(d(i, 0), 4 * i + 3, EVEN, [S, e(i) if n == 1 else (u(i, n - 2) if i == n - 1 else u(i, n - 1))] + mkli(3 * i + 3, a) + [R])
        add(e(i), 4 * i + 6, ODD, [d(i, 1), h(i)])
        add(m(i), 10 * n + 11 + 2 * i, ODD, [e(i)])
        add(q(i), 12 * n + 6 * i + 15, ODD, [h(i)])
        add(h(i), 12 * n + 6 * i + 16, ODD, [k(i)])
        add(k(i), 12 * n + 6 * i + 11, EVEN, [Z] + mkli(n - i - 1, lambda j: gs(n - j - 1)))
        add(f(i), 12 * n + 6 * i + 13, ODD, [e(i)])
        add(gs(i), 4 * i + 8, EVEN, [f(i), k(i)])
    return g.dumps()


def fearnleysubexp(n, withfearnley=True):
    """src/lib/policyiter/generators/fearnleysubexp.ml (d3cd624): "Subexponential Lower Bound for Fearnley's rule"; withfearnley=False is
    its -nogadget option. Letters as friedmannsubexp."""
    g = SymbolicPG()
    X, S, C, R, Z = ("x",), ("s",), ("c",), ("r",), ("z",)
    a = lambda i: ("a", i); t = lambda i: ("t", i); d = lambda i, j: ("d", i, j); e = lambda i: ("e", i); m = lambda i: ("m", i)
    q = lambda i: ("q", i); u = lambda i, j: ("u", i, j); v = lambda i, j: ("v", i, j); w = lambda i, j: ("w", i, j); f = lambda i: ("f", i)
    gs = lambda i: ("g", i); h = lambda i: ("h", i); k = lambda i: ("k", i)

    def add(sy, pr, pl, li):
        g.add_node(sy, pr, pl, li, _desc(sy))
    add(X, 1, ODD, [X])
    add(S, 10 * n + 6, EVEN, [Z] + mkli(n, f))
    add(C, 10 * n + 4, EVEN, [S, R])
    add(R, 10 * n + 8, EVEN, [Z] + mkli(n, gs))
    add(Z, 18 * n + 10, ODD, [X])
    for i in range(3 * n):
        add(a(i), 4 * n + 2 * i + 4, ODD, [t(i)])
        add(t(i), 4 * n + 2 * i + 3, EVEN, [C, R, S] if i == 0 else [t(i - 1), R, S])
    for i in range(n):
        if withfearnley:
            for j in range(i + 1, n):
                add(u(i, j), 3, EVEN, [v(i, j), w(i, j)])
                x = e(i) if j == i + 1 else u(i, j - 1)
                add(v(i, j), 3, ODD, [m(j), x])
                add(w(i, j), 2, ODD, [q(j), x])
        add(d(i, 1), 4 * i + 3, EVEN, [S, d(i, 0)] + mkli(3 * i + 3, a) + [R])
        add(d(i, 0), 4 * i + 3, EVEN, [S, e(i) if (i == n - 1 or not withfearnley) else u(i, n - 1)] + mkli(3 * i + 3, a) + [R])
        add(e(i), 4 * i + 4, ODD, [d(i, 1), h(i)])
        if withfearnley:
            add(m(i), 10 * n + 9 + 2 * i, ODD, [e(i)])
            add(q(i), 12 * n + 6 * i + 13, ODD, [h(i)])
        add(h(i), 12 * n + 6 * i + 14, ODD, [k(i)])
        add(k(i), 12 * n + 6 * i + 9, EVEN, [Z] + mkli(n - i - 1, lambda j: gs(n - j - 1)))
        add(f(i), 12 * n + 6 * i + 11, ODD, [e(i)])
        add(gs(i), 4 * i + 6, EVEN, [f(i), k(i)])
    return g.dumps()


GENS = {"recursiveladder": recursiveladder, "switchallexp": switchallexp, "switchbestexp": switchbestexp,
        "friedmannsubexp": friedmannsubexp, "fearnleysubexp": fearnleysubexp,
        "fearnleysubexp-nogadget": lambda n: fearnleysubexp(n, False)}

if __name__ == "__main__":
    sys.stdout.write(GENS[sys.argv[1]](int(sys.argv[2])))
