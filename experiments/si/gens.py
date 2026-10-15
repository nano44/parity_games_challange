#!/usr/bin/env python3
"""Python ports of two more PGSolver strategy-improvement lower-bound generators (L-SI; same conventions and SymbolicPG as
experiments/hard-families/pgsolver_port.py, github.com/tcsprojects/pgsolver @ d3cd624b61cd66739c45aff9554f6bbdcdd05401).
  randomfacetsubexp N   src/lib/generators/policyiter/generators/randomfacetsubexp.ml:30-134, default options (no -bp/-ap/-ac/
                        -re/-bcn/-ban/-bun): d = m = r = binlog N, cd = binlog N * d, binlog = ceil(log2 N) (line 27). Needs N >= 2.
                        Description string (line 145): "Subexponential Lower Bound for the Random Facet rule" (the SODA 2011
                        construction; its bound stands for Random-Facet*, errata arXiv 1410.7871).
  zadehexp N            zadehexp.ml:50-90, "Exponential Lower Bound for Zadeh's rule" (line 100).
Usage: gens.py GENERATOR N"""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "hard-families"))
from pgsolver_port import SymbolicPG, mkli, EVEN, ODD


def randomfacetsubexp(n):
    assert n >= 2, "binlog 1 = 0 gives an empty construction"
    binlog = lambda x: int(math.ceil(math.log(x) / math.log(2)))              # line 27
    d = binlog(n); cd = binlog(n) * d; m = binlog(n); r = binlog(n)            # lines 62-68 (defaults)
    r_d, r_cd = r, r                                                            # lines 70-73 (no binary flags)
    lab = {"CycleNode": lambda s: f"d({s[1]},{s[2]})", "CycleCenter": lambda s: f"e{s[1]}", "CycleEntry": lambda s: f"c({s[1]},{s[2]})",
           "AccessNode": lambda s: f"b({s[1]},{s[2]},{s[3]})", "AccessCenter": lambda s: f"a({s[1]},{s[2]})",
           "AccessEntry": lambda s: f"r({s[1]},{s[2]},{s[3]})", "LaneEntry": lambda s: f"c({s[1]},{s[2]})",
           "LaneEntryAccess": lambda s: f"g({s[1]},{s[2]})", "UpperNode": lambda s: f"k{s[1]}", "FinalCycle": lambda s: "q",
           "FinalSink": lambda s: "p"}                                          # symb_to_str, line 21 (LaneEntryAccess falls to "")
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, lab[sy[0]](sy) if sy[0] != "LaneEntryAccess" else "")
    FinalCycle, FinalSink = ("FinalCycle",), ("FinalSink",)
    CN = lambda i, j: ("CycleNode", i, j); CC = lambda i: ("CycleCenter", i); CE = lambda i, j: ("CycleEntry", i, j)
    AN = lambda i, k, j: ("AccessNode", i, k, j); AC = lambda i, k: ("AccessCenter", i, k); AE = lambda i, k, s: ("AccessEntry", i, k, s)
    LE = lambda i, s: ("LaneEntry", i, s); LEA = lambda i, s: ("LaneEntryAccess", i, s); UN = lambda i: ("UpperNode", i)
    add(FinalCycle, 1, ODD, [FinalCycle])                                       # line 101
    add(FinalSink, 6 + 2 * n, ODD, [FinalCycle])                                # line 102
    for i in range(n):                                                          # lines 104-132
        add(CC(i), 2, ODD, [UN(i)] + mkli(cd, lambda j: CN(i, j)))              # line 105
        if i == n - 1:
            add(UN(i), 6 + 2 * i, EVEN, [FinalSink])                            # line 108
        else:
            add(UN(i), 6 + 2 * i, EVEN, [AE(i + 1, k, s) for k in range(m) for s in range(r)])   # line 110
        for j in range(cd):
            add(CN(i, j), 0, EVEN, [FinalSink, CC(i)] + mkli(r_cd, lambda s: LE(i, s)))         # line 116
        for k in range(m):
            add(AC(i, k), 2, ODD, [CE(i, 0)] + mkli(d, lambda j: AN(i, k, j)))                 # line 119
            for j in range(d):
                add(AN(i, k, j), 0, EVEN, [FinalSink, AC(i, k)] + mkli(r_d, lambda s: LEA(i, s)))   # line 121
            for s in range(r):
                add(AE(i, k, s), 0, ODD, [AC(i, k)])                                            # line 124
        for s in range(r):                                                                      # lines 127-131
            add(LE(i, s), 0, ODD, [FinalSink if i == n - 1 else CN(i + 1, 0)])
            add(LEA(i, s), 4, ODD, [FinalSink if i == n - 1 else CN(i + 1, 0)])
            add(CE(i, s), 2, ODD, [CC(i)])
    return g.dumps()


def zadehexp(n):
    lab = {"FinalCycle": "Z", "FinalSink": "Y", "PairSelector": "d", "CycleCenter1": "E", "CycleCenter2": "X", "CycleNodeX1": "a",
           "CycleNodeX2": "w", "CycleNodeY1": "b", "CycleNodeY2": "v", "CycleNodeX1T": "o", "CycleNodeX2T": "q", "CycleNodeY1T": "p",
           "CycleNodeY2T": "r", "UpperSelector1": "c", "UpperSelector2": "z", "Selector": "m", "UpDown1": "g", "UpDown2": "s",
           "Helper": "u"}                                                       # symb_to_str, lines 28-47
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, lab[sy[0]] + (str(sy[1]) if len(sy) > 1 else ""))
    add1 = lambda sy, pr, li: add(sy, pr, ODD, li); add0 = lambda sy, pr, li: add(sy, pr, EVEN, li)
    S = lambda name: (lambda i: (name, i))
    FinalCycle, FinalSink = ("FinalCycle",), ("FinalSink",)
    PS, CC1, CC2, X1, X2, Y1, Y2 = S("PairSelector"), S("CycleCenter1"), S("CycleCenter2"), S("CycleNodeX1"), S("CycleNodeX2"), S("CycleNodeY1"), S("CycleNodeY2")
    X1T, X2T, Y1T, Y2T, UD1, UD2, US1, US2, Sel, H = S("CycleNodeX1T"), S("CycleNodeX2T"), S("CycleNodeY1T"), S("CycleNodeY2T"), S("UpDown1"), S("UpDown2"), S("UpperSelector1"), S("UpperSelector2"), S("Selector"), S("Helper")
    add1(FinalCycle, 1, [FinalCycle])                                           # line 63
    add1(FinalSink, 2 * n + 12, [FinalCycle])                                   # line 64
    for i in range(n):                                                          # lines 67-88
        add0(X1(i), 3, [CC1(i), X1T(i)])
        add0(X1T(i), 3, [PS(0), Sel(1)])
        if i < n - 1: add0(X2(i), 3, [CC2(i), X2T(i)])
        if i < n - 1: add0(X2T(i), 3, [PS(0), Sel(1)])
        add0(Y1(i), 3, [CC1(i), Y1T(i)])
        add0(Y1T(i), 3, [PS(0), Sel(1)])
        if i < n - 1: add0(Y2(i), 3, [CC2(i), Y2T(i)])
        if i < n - 1: add0(Y2T(i), 3, [PS(0), Sel(1)])
        add0(PS(i), 2 * i + 11, [CC1(i), CC2(i)] if i < n - 1 else [CC1(i)])
        add0(Sel(i), 3, [PS(i), Sel(i + 1) if i < n - 1 else FinalSink])
        add1(CC1(i), 6, [X1(i), Y1(i), UD1(i)])
        if i < n - 1: add1(CC2(i), 4, [X2(i), Y2(i), UD2(i)])
        add0(UD1(i), 10, [US1(i), Sel(0)])
        if i < n - 1: add0(UD2(i), 8, [H(i), Sel(0)])
        add0(US1(i), 2 * i + 12, [Sel(i + 2) if i < n - 2 else FinalSink])
        if i < n - 1:
            add1(H(i), 5, [US2(i)])
            add0(US2(i), 2 * i + 12, [PS(i + 1)])
    return g.dumps()


def dlmm_bland(n):
    """Disser-Loho-Maat-Mosis arXiv 2512.16684 v2, Fig. 4.1 / proof of Lemma 4.4: the binary-counter sink parity game G_n for
    Bland's rule.  Levels i = 1..n: a_i (Even, priority 2i+1) -> b_{i+1} (Bland number 2i), a_{i+1} (Bland number 2i-1);
    b_i (Odd, priority 2i+2) -> b_{i+1}, a_{i+1}; b_{n+1} (Odd, 2n+4) -> sink; a_{n+1} = sink (Odd, priority 1, self-loop).
    Vertex ids: sink 0; a_i = 2i-1, b_i = 2i (i = 1..n), b_{n+1} = 2n+1.  The initial strategy sigma_0(a_i) = a_{i+1} is the
    engine's "first" start (smallest successor index), which check.sh uses; Bland numbers are not used by L-SI's rules."""
    sink = 0; A = lambda i: sink if i == n + 1 else 2 * i - 1; B = lambda i: 2 * n + 1 if i == n + 1 else 2 * i
    rows = [f"{sink} 1 1 {sink} \"sink\";"]
    for i in range(1, n + 1):
        rows.append(f"{A(i)} {2 * i + 1} 0 {A(i + 1)},{B(i + 1)} \"a{i}\";")
        rows.append(f"{B(i)} {2 * i + 2} 1 {A(i + 1)},{B(i + 1)} \"b{i}\";")
    rows.append(f"{B(n + 1)} {2 * n + 4} 1 {sink} \"b{n + 1}\";")
    return f"parity {2 * n + 1};\n" + "\n".join(rows) + "\n"


def dlmm_ML(L):
    """Sink-parity-game port of DLMM 2512.16684 Lemma 5.4's MDP M_L (Fig. 5.1), as proposed by L-LIT T12 section 4:
    levels l = 1..L+1 with Even vertices alpha_l, beta_l; for l <= L both have the actions -> alpha_{l+1} (no reward) and
    -> beta_{l+1} with reward L^l, realised as a fresh reward vertex R_l of even priority 2l+2 (increasing in l, so the
    lexicographic set order equals the arithmetic order of the rewards L^l); alpha_{L+1} -> R_{L+1} (priority 2L+4) -> sink;
    beta_{L+1} -> sink. alpha, beta have priority 0 (below the sink's 1, so they never enter a path set); the sink is Odd's
    with a self-loop and priority 1. Ids: sink 0; alpha_l = 3l-2, beta_l = 3l-1, R_l = 3l (l = 1..L+1).
    The initial strategy sigma_0 (alpha_l -> alpha_{l+1}, beta_l -> beta_{l+1}) is printed after the game as a line
    '% start v:w ...' (strip it before parsing; instances/*.start keep it separately)."""
    A = lambda l: 3 * l - 2; B = lambda l: 3 * l - 1; R = lambda l: 3 * l
    rows = ["0 1 1 0 \"sink\";"]; start = []
    for l in range(1, L + 2):
        if l <= L:
            rows.append(f"{A(l)} 0 0 {A(l + 1)},{R(l)} \"alpha{l}\";"); start.append((A(l), A(l + 1)))
            rows.append(f"{B(l)} 0 0 {A(l + 1)},{R(l)} \"beta{l}\";"); start.append((B(l), R(l)))
            rows.append(f"{R(l)} {2 * l + 2} 1 {B(l + 1)} \"R{l}\";")
        else:
            rows.append(f"{A(l)} 0 0 {R(l)} \"alpha{l}\";")
            rows.append(f"{B(l)} 0 0 0 \"beta{l}\";")
            rows.append(f"{R(l)} {2 * l + 2} 1 0 \"R{l}\";")
    return f"parity {3 * L + 3};\n" + "\n".join(rows) + "\n% start " + " ".join(f"{v}:{w}" for v, w in start) + "\n"


GENS = {"randomfacetsubexp": randomfacetsubexp, "zadehexp": zadehexp, "dlmm_bland": dlmm_bland, "dlmm_ML": dlmm_ML}
if __name__ == "__main__":
    sys.stdout.write(GENS[sys.argv[1]](int(sys.argv[2])))
