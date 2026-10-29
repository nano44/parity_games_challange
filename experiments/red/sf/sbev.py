#!/usr/bin/env python3
"""L-RED: switchbestexp (PGSolver d3cd624 switchbestexp.ml, via experiments/hard-families/pgsolver_port.py) with a LANE-SPACING
parameter c (lane length c*n+1; cycle i's lane entries at c*i + r instead of 6i + r; the upper priority block shifted by (2c-12)n so
all priorities keep their relative order). c = 6 reproduces pgsolver_port.py switchbestexp byte for byte (checked by --selftest).
Usage: sbev.py N [c] [mode]   mode 'scale' maps entry r -> round(r*c/6) instead of r."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "hard-families"))
from pgsolver_port import SymbolicPG, mkli, switchbestexp

EVEN, ODD = 0, 1


def sbev(n, c=6, mode="shift", drop=()):
    """drop also takes 'dp' = ADD a vertex d' (prio of d, single edge to s) and an edge from every CL node to it.
    drop: edge classes removed: fc (f_i -> c), ed (e_i -> d), ga (g_i -> a0), fa (f_i -> a_(c i + 4)), fl1 (f'_i -> a_(c i+4))."""
    R = (lambda r: r) if mode == "shift" else (lambda r: (r * c + 3) // 6)
    up = 2 * c * n - 12 * n            # shift for the 24n-block
    lab = {"DecLaneEven": "a", "DecLaneOdd": "b", "DecLaneOddRoot": "d", "CycleNode0": "e", "CycleNode1": "f",
           "CycleNode2": "g", "CycleNodeToLane0": "e'", "CycleNodeToLane1": "f'", "CycleNodeToLane2": "g'",
           "CycleCenter": "h", "CycleAccessDistributer": "c", "CycleAccess": "k", "CycleSelector": "l",
           "CycleSelectorDecelerator": "r", "CycleLeaver": "m", "UpperSelector": "z", "UpperSelectorHelper": "v",
           "FinalSink": "p", "FinalCycle": "q", "StartEven": "s", "StartSelector": "t", "HighEntryBit": "w",
           "LowestBit": "y", "BitSelector": "x"}
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, lab[sy[0]] + (str(sy[1]) if len(sy) > 1 else ""))
    S = lambda *a: a
    FinalCycle, StartEven, StartSelector, LowestBit, HighEntryBit = S("FinalCycle"), S("StartEven"), S("StartSelector"), S("LowestBit"), S("HighEntryBit")
    DecLaneOddRoot, BitSelector, FinalSink, CAD = S("DecLaneOddRoot"), S("BitSelector"), S("FinalSink"), S("CycleAccessDistributer")
    f = lambda name: (lambda i: S(name, i))
    DLE, DLO, CN0, CN1, CN2 = f("DecLaneEven"), f("DecLaneOdd"), f("CycleNode0"), f("CycleNode1"), f("CycleNode2")
    CL0, CL1, CL2, CC = f("CycleNodeToLane0"), f("CycleNodeToLane1"), f("CycleNodeToLane2"), f("CycleCenter")
    CLv, US, CA, CS, CSD, USH = f("CycleLeaver"), f("UpperSelector"), f("CycleAccess"), f("CycleSelector"), f("CycleSelectorDecelerator"), f("UpperSelectorHelper")
    add(FinalCycle, 1, ODD, [FinalCycle])
    add(StartEven, 2, EVEN, [FinalSink, CAD])
    add(StartSelector, 3, EVEN, [BitSelector, StartEven])
    add(CAD, 4, EVEN, mkli(n, CA))
    add(LowestBit, 5, EVEN, [HighEntryBit, CS(0)])
    add(HighEntryBit, 7, EVEN, [LowestBit, FinalSink] + mkli(n - 1, lambda j: CS(j + 1)))
    add(DecLaneOddRoot, 24 * n + 12 + up, EVEN, [StartEven] if 'ds' in drop else [StartSelector] if 'dt' in drop else [StartSelector, BitSelector])
    add(BitSelector, 24 * n + 14 + up, EVEN, [HighEntryBit, LowestBit])
    add(FinalSink, 26 * n + 16 + up, ODD, [FinalCycle])
    DP = S("DPrime")
    if 'dp' in drop:
        lab["DPrime"] = "d'"
        add(DP, 24 * n + 12 + up, EVEN, [StartEven])
    dpl = [DP] if 'dp' in drop else []
    for i in range(c * n + 1):
        add(DLE(i), 12 * n + 2 * i + 10, ODD, [DLO(i)])
        add(DLO(i), 12 * n + 2 * i + 9, EVEN, [DecLaneOddRoot if i < 2 else DLO(i - 1), BitSelector, StartEven])
    for i in range(n):
        add(CN0(i), 6 * n + 6 * i + 9, EVEN, [CN1(i)] + ([] if 'ed' in drop else [DecLaneOddRoot]) + [CL0(i)])
        add(CN1(i), 6 * n + 6 * i + 11, EVEN, [CN2(i)] + ([] if ('fc' in drop or os.environ.get('FCMASK', '1' * n).ljust(n, '1')[i] == '0') else [CAD]) + [CL1(i)] + ([] if 'fa' in drop else [DLE(c * i + R(4))]))
        add(CN2(i), 6 * n + 6 * i + 13, EVEN, ([] if 'ga' in drop else [DLE(0)]) + [CC(i), CL2(i)])
        add(CL0(i), 6 * i + 8, EVEN, ([] if i == 0 else [CL0(i - 1)]) + [DecLaneOddRoot] + dpl + [DLE(c * i + R(2)), DLE(c * i + R(5))])
        add(CL1(i), 6 * i + 10, EVEN, ([] if i == 0 else [CL1(i - 1)]) + [DecLaneOddRoot] + dpl + [DLE(c * i + R(1))] + ([DLE(c * i + R(4))] if i < n - 1 else []))
        add(CL2(i), 6 * i + 12, EVEN, ([] if i == 0 else [CL2(i - 1)]) + [DecLaneOddRoot] + dpl + [DLE(c * i + R(3)), DLE(c * i + R(6))])
        add(CC(i), 6 * n + 6 * i + 14, ODD, [CN0(i), CLv(i)])
        add(CLv(i), 24 * n + 4 * i + 18 + up, ODD, [US(i)])
        add(US(i), 24 * n + 4 * i + 15 + up, EVEN, [FinalSink] if i == n - 1 else [FinalSink, USH(i)])
        add(CA(i), 24 * n + 4 * i + 17 + up, ODD, [CC(i)])
        add(CS(i), 6 * i + 11, EVEN, [CA(i), US(i)])
        add(CSD(i), 6 * i + 13, EVEN, [CS(i), US(i)])
        if i < n - 1:
            add(USH(i), 6 * i + 9, EVEN, [FinalSink, CSD(n - 1)] if i == n - 2 else [USH(i + 1), CSD(i + 1)])
    if 'obs' in drop:                                     # observer: Odd o -> {P0, P1}; P0/P1 Even -> even/odd lane entries
        lab["Obs"] = "o"; lab["ObsP0"] = "P0"; lab["ObsP1"] = "P1"
        add(S("ObsP0"), 0, EVEN, [DLE(i) for i in range(0, c * n + 1, 2)])
        add(S("ObsP1"), 0, EVEN, [DLE(i) for i in range(1, c * n + 1, 2)])
        add(S("Obs"), 0, ODD, [S("ObsP0"), S("ObsP1")])
    return g.dumps()


if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        for N in range(1, 11):
            assert sbev(N) == switchbestexp(N), N
        print("selftest OK: c=6 == switchbestexp N=1..10"); sys.exit()
    a = sys.argv[1:]; drop = tuple(a[a.index("--drop") + 1].split(",")) if "--drop" in a else ()
    a = [x for x in a if x != "--drop" and (not drop or x != ",".join(drop))]
    sys.stdout.write(sbev(int(a[0]), int(a[1]) if len(a) > 1 else 6, a[2] if len(a) > 2 else "shift", drop))
