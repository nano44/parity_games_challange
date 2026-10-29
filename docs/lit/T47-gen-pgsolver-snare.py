#!/usr/bin/env python3
"""T47 reference generator (L-LIT): transcription of two PGSolver generators, github.com/tcsprojects/pgsolver commit
d3cd624b61cd66739c45aff9554f6bbdcdd05401, read only:
  friedmannsubexp  = src/lib/generators/policyiter/generators/friedmannsubexp.ml l.34-82  («Friedmann's Subexponential Lower Bound for
                     snare-based rules», l.86-87)
  fearnleysubexp   = src/lib/generators/policyiter/generators/fearnleysubexp.ml l.31-78   («Subexponential Lower Bound for Fearnley's
                     rule», l.82-83); option -nogadget (l.36) = withfearnley false
Symbol indexing and output, as PGSolver:
  stratimprgenerators.ml l.27-45 (SymbolicParityGame): a symbol gets the next index the first time it is MENTIONED, as a node (add) or as an
  edge target (touch, in list order, after the node itself); add_node overrides the data of an already touched symbol; successors are a
  TreeSet (sorted, duplicates merged; to_paritygame l.16-25).
  paritygame.ml l.365-386 (output_game): 'parity <n-1>;' then 'i pr pl succ,succ,... "desc";' (pl: 0 = Even, 1 = Odd), nodes with pr < 0
  skipped (none here: asserted).
Written independently of experiments/hard-families/pgsolver_port.py (same conventions, not its code).
Usage: python3 -I docs/lit/T47-gen-pgsolver-snare.py friedmannsubexp|fearnleysubexp|fearnleysubexp-nogadget N > game.pg"""
import sys

EVEN, ODD = 0, 1


class SPG:
    def __init__(self):
        self.ind, self.node, self.succ = {}, [], []

    def _get(self, sym, data, override):
        if sym in self.ind:
            i = self.ind[sym]
            if override: self.node[i] = data
            return i
        i = len(self.node); self.ind[sym] = i; self.node.append(data); self.succ.append(set())
        return i

    def add(self, sym, pr, pl, li):
        i = self._get(sym, (pr, pl, name(sym)), True)
        for t in li: self.succ[i].add(self._get(t, (-1, EVEN, None), False))

    def dumps(self):
        assert all(pr >= 0 for pr, _, _ in self.node), "a mentioned symbol was never added"
        out = [f"parity {len(self.node) - 1};"]
        for i, (pr, pl, d) in enumerate(self.node):
            out.append(f'{i} {pr} {pl} {",".join(map(str, sorted(self.succ[i])))} "{d}";')
        return "\n".join(out) + "\n"


def name(s):  # symb_to_str (friedmannsubexp.ml l.29; fearnleysubexp.ml l.26)
    k = s[0]; a = s[1:]
    short = {"DecLaneEven": "a", "DecLaneOdd": "t", "CycleCenter": "e", "CycleCenterBadEntry": "m", "CycleCenterBadEntryX": "q",
             "CycleAccess": "f", "CycleSelector": "g", "CycleLeaver": "h", "UpperSelector": "k"}
    pair = {"CycleNode": "d", "CycleNodeCho": "u", "CycleNodeSpecial": "b", "CycleNodeSpecialX": "l", "CycleNodeSpecialY": "p",
            "CycleBadEntrySel": "v", "CycleBadEntrySelX": "w"}
    const = {"DecLaneRoot": "c", "FinalSink": "z", "FinalCycle": "x", "StartEven": "s", "BitSelector": "r"}
    if k in const: return const[k]
    if k in short: return short[k] + str(a[0])
    return f"{pair[k]}({a[0]},{a[1]})"


def mkli(n, f): return [f(j) for j in range(n)]


def friedmannsubexp(n):  # friedmannsubexp.ml l.34-82
    pg = SPG(); add = pg.add
    S = lambda *a: tuple(a)
    add(S("FinalCycle"), 1, ODD, [S("FinalCycle")])                                                        # l.43
    add(S("StartEven"), 10 * n + 8, EVEN, [S("FinalSink")] + mkli(n, lambda j: S("CycleAccess", j)))      # l.44
    add(S("DecLaneRoot"), 10 * n + 6, EVEN, [S("StartEven"), S("BitSelector")])                           # l.45
    add(S("BitSelector"), 10 * n + 10, EVEN, [S("FinalSink")] + mkli(n, lambda j: S("CycleSelector", j))) # l.46
    add(S("FinalSink"), 18 * n + 12, ODD, [S("FinalCycle")])                                              # l.47
    for i in range(3 * n):                                                                                # l.49-52
        add(S("DecLaneEven", i), 4 * n + 2 * i + 6, ODD, [S("DecLaneOdd", i)])
        add(S("DecLaneOdd", i), 4 * n + 2 * i + 5, EVEN,
            [S("DecLaneRoot"), S("BitSelector"), S("StartEven")] if i == 0 else [S("DecLaneOdd", i - 1), S("BitSelector"), S("StartEven")])
    for i in range(n):                                                                                    # l.54-80
        for j in range(i):                                                                                # l.55-63
            add(S("CycleNodeCho", i, j), 3, EVEN, [S("CycleBadEntrySel", i, j), S("CycleBadEntrySelX", i, j), S("CycleNodeSpecial", i, j)])
            x = S("CycleCenter", i) if j == 0 else S("CycleNodeCho", i, j - 1)
            add(S("CycleNodeSpecial", i, j), 5, EVEN, [S("CycleNodeSpecialX", i, j), S("CycleNodeSpecialY", i, j), x])
            add(S("CycleNodeSpecialX", i, j), 4, EVEN, [S("CycleBadEntrySel", i, j)])
            add(S("CycleNodeSpecialY", i, j), 4, EVEN, [S("CycleBadEntrySelX", i, j)])
            add(S("CycleBadEntrySel", i, j), 3, ODD, [S("CycleCenterBadEntry", j), x])
            add(S("CycleBadEntrySelX", i, j), 2, ODD, [S("CycleCenterBadEntryX", j), x])
        for j in range(i + 1, n):                                                                         # l.64-69
            add(S("CycleNodeCho", i, j), 3, EVEN, [S("CycleBadEntrySel", i, j), S("CycleBadEntrySelX", i, j)])
            if j == i + 1:
                x = S("CycleCenter", i) if i == 0 else S("CycleNodeCho", i, j - 2)
            else:
                x = S("CycleNodeCho", i, j - 1)
            add(S("CycleBadEntrySel", i, j), 3, ODD, [S("CycleCenterBadEntry", j), x])
            add(S("CycleBadEntrySelX", i, j), 2, ODD, [S("CycleCenterBadEntryX", j), x])
        lane = mkli(3 * i + 3, lambda j: S("DecLaneEven", j))
        add(S("CycleNode", i, 1), 4 * i + 3, EVEN, [S("StartEven"), S("CycleNode", i, 0)] + lane + [S("BitSelector")])   # l.70
        c0 = S("CycleCenter", i) if n == 1 else (S("CycleNodeCho", i, n - 2) if i == n - 1 else S("CycleNodeCho", i, n - 1))
        add(S("CycleNode", i, 0), 4 * i + 3, EVEN, [S("StartEven"), c0] + lane + [S("BitSelector")])                     # l.71-72
        add(S("CycleCenter", i), 4 * i + 6, ODD, [S("CycleNode", i, 1), S("CycleLeaver", i)])                            # l.73
        add(S("CycleCenterBadEntry", i), 10 * n + 11 + 2 * i, ODD, [S("CycleCenter", i)])                                 # l.74
        add(S("CycleCenterBadEntryX", i), 12 * n + 6 * i + 15, ODD, [S("CycleLeaver", i)])                                # l.75
        add(S("CycleLeaver", i), 12 * n + 6 * i + 16, ODD, [S("UpperSelector", i)])                                       # l.76
        add(S("UpperSelector", i), 12 * n + 6 * i + 11, EVEN,
            [S("FinalSink")] + mkli(n - i - 1, lambda j: S("CycleSelector", n - j - 1)))                                # l.77
        add(S("CycleAccess", i), 12 * n + 6 * i + 13, ODD, [S("CycleCenter", i)])                                         # l.78
        add(S("CycleSelector", i), 4 * i + 8, EVEN, [S("CycleAccess", i), S("UpperSelector", i)])                         # l.79
    return pg


def fearnleysubexp(n, withfearnley=True):  # fearnleysubexp.ml l.31-78
    pg = SPG(); add = pg.add
    S = lambda *a: tuple(a)
    add(S("FinalCycle"), 1, ODD, [S("FinalCycle")])                                                        # l.46
    add(S("StartEven"), 10 * n + 6, EVEN, [S("FinalSink")] + mkli(n, lambda j: S("CycleAccess", j)))      # l.47
    add(S("DecLaneRoot"), 10 * n + 4, EVEN, [S("StartEven"), S("BitSelector")])                           # l.48
    add(S("BitSelector"), 10 * n + 8, EVEN, [S("FinalSink")] + mkli(n, lambda j: S("CycleSelector", j)))  # l.49
    add(S("FinalSink"), 18 * n + 10, ODD, [S("FinalCycle")])                                              # l.50
    for i in range(3 * n):                                                                                # l.52-55
        add(S("DecLaneEven", i), 4 * n + 2 * i + 4, ODD, [S("DecLaneOdd", i)])
        add(S("DecLaneOdd", i), 4 * n + 2 * i + 3, EVEN,
            [S("DecLaneRoot"), S("BitSelector"), S("StartEven")] if i == 0 else [S("DecLaneOdd", i - 1), S("BitSelector"), S("StartEven")])
    for i in range(n):                                                                                    # l.57-76
        if withfearnley:                                                                                  # l.58-64
            for j in range(i + 1, n):
                x = S("CycleCenter", i) if j == i + 1 else S("CycleNodeCho", i, j - 1)
                add(S("CycleNodeCho", i, j), 3, EVEN, [S("CycleBadEntrySel", i, j), S("CycleBadEntrySelX", i, j)])
                add(S("CycleBadEntrySel", i, j), 3, ODD, [S("CycleCenterBadEntry", j), x])
                add(S("CycleBadEntrySelX", i, j), 2, ODD, [S("CycleCenterBadEntryX", j), x])
        lane = mkli(3 * i + 3, lambda j: S("DecLaneEven", j))
        add(S("CycleNode", i, 1), 4 * i + 3, EVEN, [S("StartEven"), S("CycleNode", i, 0)] + lane + [S("BitSelector")])   # l.65
        c0 = S("CycleCenter", i) if (i == n - 1 or not withfearnley) else S("CycleNodeCho", i, n - 1)
        add(S("CycleNode", i, 0), 4 * i + 3, EVEN, [S("StartEven"), c0] + lane + [S("BitSelector")])                     # l.66
        add(S("CycleCenter", i), 4 * i + 4, ODD, [S("CycleNode", i, 1), S("CycleLeaver", i)])                            # l.67
        if withfearnley:                                                                                  # l.68-71
            add(S("CycleCenterBadEntry", i), 10 * n + 9 + 2 * i, ODD, [S("CycleCenter", i)])
            add(S("CycleCenterBadEntryX", i), 12 * n + 6 * i + 13, ODD, [S("CycleLeaver", i)])
        add(S("CycleLeaver", i), 12 * n + 6 * i + 14, ODD, [S("UpperSelector", i)])                                       # l.72
        add(S("UpperSelector", i), 12 * n + 6 * i + 9, EVEN,
            [S("FinalSink")] + mkli(n - i - 1, lambda j: S("CycleSelector", n - j - 1)))                                # l.73
        add(S("CycleAccess", i), 12 * n + 6 * i + 11, ODD, [S("CycleCenter", i)])                                         # l.74
        add(S("CycleSelector", i), 4 * i + 6, EVEN, [S("CycleAccess", i), S("UpperSelector", i)])                         # l.75
    return pg


if __name__ == "__main__":
    gen, n = sys.argv[1], int(sys.argv[2])
    g = {"friedmannsubexp": lambda: friedmannsubexp(n), "fearnleysubexp": lambda: fearnleysubexp(n),
         "fearnleysubexp-nogadget": lambda: fearnleysubexp(n, False)}[gen]()
    sys.stdout.write(g.dumps())
