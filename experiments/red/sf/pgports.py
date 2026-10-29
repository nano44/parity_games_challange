#!/usr/bin/env python3
"""L-RED: line-by-line Python ports of nine PGSolver strategy-improvement generators (parity_game part only;
the generalized_mdp parts are not ported).

Source: github.com/tcsprojects/pgsolver at d3cd624, directory src/lib/generators/policyiter/generators/:
  cunninghamexp.ml      104 lines   "Binary-Case Exponential Lower Bound for Cunningham's rule"   flags -tiefree -indexone
  cunninghamsubexp.ml    80 lines   "Binary Subexponential Lower Bound for Cunningham's rule"      flag  -binary
  randomedgeexptest.ml  170 lines   "Experimental Exponential Lower Bound for the random-edge rule" flags -cl -al -pl -int
  randomedgesubexp.ml    94 lines   "Subexponential Lower Bound for the random-edge rule"
  randomfacetsubexp.ml  148 lines   "Subexponential Lower Bound for the Random Facet rule"   flags -bp -ap -ac -re -bcn -ban -bun
  switchallsubexp.ml     87 lines   "Binary-Case Subexponential Lower Bound for (Voege's) switch-all rule"  flag -binary
  switchbestsubexp.ml    95 lines   "Binary-Case Subexponential Lower Bound for (Schewe's) switch-best rule" flag -binary
  zadehexp.ml           103 lines   "Exponential Lower Bound for Zadeh's rule"
  zadehsubexp.ml         94 lines   "Subexponential Lower Bound for Zadeh's rule"
SymbolicPG / mkli come from experiments/hard-families/pgsolver_port.py (port of stratimprgenerators.ml:11-50; a symbol
gets the next index the first time it is mentioned, add_node indexes the node first, then successors in list order;
symbols mentioned but never added keep priority -1 and are not printed, exactly as to_paritygame + output_game).
Notes on translation:
  * OCaml evaluates the elements of a list literal right to left (ocamlopt and bytecode). This matters only where an
    element has side effects: randomfacetsubexp make_tree ([make_tree left; make_tree right]), reached only with -bun.
    The port evaluates right first.
  * Flags are processed in argument order as Arg does; in randomedgeexptest the anonymous N multiplies -cl/-al/-pl values
    set BEFORE it (and defaults), a flag given after N overrides the scaled value, as in the OCaml.
  * randomedgeexptest line 115 matches `(Some str, plr_Even)`: plr_Even there is a fresh pattern variable, so with -int
    every node (both players) gets the "[strategy]" suffix. Ported as such.
Usage: pgports.py NAME N [flags]   (NAME in GENS)"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "hard-families"))
from pgsolver_port import SymbolicPG, mkli

EVEN, ODD = 0, 1


def _mkli_pos(n, f):  # `let mkli n f = if n < 1 then [] else ...` (same as mkli for n >= 0)
    return [] if n < 1 else [f(j) for j in range(n)]


def _parse(args, flags):
    """Arg-style parsing in order. flags: name -> ('unit', fn) | ('int', fn) | ('str', fn); anon handled by flags[None]."""
    k = 0
    while k < len(args):
        a = args[k]
        if a in flags:
            kind, fn = flags[a]
            if kind == "unit":
                fn()
            else:
                k += 1
                fn(int(args[k]) if kind == "int" else args[k])
        elif a.startswith("-") and not a.lstrip("-").isdigit():
            raise SystemExit(f"unknown option {a}")
        else:
            flags[None](a)
        k += 1


# ---------------------------------------------------------------- cunninghamexp.ml
def cunninghamexp(args):
    st = {"auso": False, "one": False, "bits": 0}                                  # lines 7-9
    def setv(k, v): st[k] = v
    _parse(args, {"-tiefree": ("unit", lambda: setv("auso", True)), "-indexone": ("unit", lambda: setv("one", True)),
                  None: lambda s: setv("bits", int(s))})                           # lines 40-45
    n, auso_compat = st["bits"], st["auso"]
    mapindex = lambda i: str(i + 1 if st["one"] else i)                            # line 10
    lab = {"CycleCenter": "x", "CycleNodePaced": "e", "CycleNodeLaned": "d", "PacerNode": "c", "CycleExit": "y",
           "CycleEntry": "q", "CycleSelector": "b", "UpperSelector": "a", "PacerEntry": "p", "AusoHelper": "z"}
    s2s = lambda sy: "t" if sy[0] == "FinalCycle" else lab[sy[0]] + mapindex(sy[1])  # lines 25-36
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    touch = lambda sy: g._internal_add(sy, -1, EVEN, None, False)                  # touch_node
    FC = ("FinalCycle",)
    CE, US, CS, CC = (lambda i: ("CycleExit", i)), (lambda i: ("UpperSelector", i)), (lambda i: ("CycleSelector", i)), (lambda i: ("CycleCenter", i))
    CNP, CNL, CEn = (lambda i: ("CycleNodePaced", i)), (lambda i: ("CycleNodeLaned", i)), (lambda i: ("CycleEntry", i))
    PN, PE, AH = (lambda i: ("PacerNode", i)), (lambda i: ("PacerEntry", i)), (lambda i: ("AusoHelper", i))
    if True:                                                                       # lines 53-71
        for i in range(n):
            if i > 0: touch(US(i))
        for i in range(n):
            if i > 0: touch(CS(i))
        for i in range(n):
            touch(PN(i))
        for i in range(n):
            if i > 0: touch(CNL(i))
        for i in range(n):
            touch(CNP(i))
    add(FC, 1, ODD, [FC])                                                          # line 73
    add(US(n), 3, ODD, [FC])
    add(PE(0), 8, ODD, [AH(0) if auso_compat else PN(n - 1)])
    add(PE(1), 3, ODD, [PE(0)])
    for i in range(n):                                                             # lines 78-90
        if auso_compat: add(AH(i), 3, ODD, [PN(n - 1) if i == n - 1 else AH(i + 1)])
        add(CE(i), 2 * i + 10, ODD, [US(i + 1)])
        add(CEn(i), 2 * i + 9, ODD, [CC(i)])
        add(CC(i), 6, ODD, [CNP(i), CNL(i), CE(i)] if i > 0 else [CNP(i), CE(i)])
        add(CC(i + n), 5, ODD, [CC(i)])
        if i < n - 1: add(US(i + 1), 3, EVEN, [US(i + 2), CEn(i + 1)])
        if i < n - 1: add(CS(i + 1), 3, EVEN, [CS(i), CEn(i)] if i > 0 else [CEn(0)])
        add(PN(i), 3, EVEN, [CEn(0)] if i == 0 else [PN(i - 1), CEn(i)])
        add(CNP(i), 5, EVEN, [PE(1) if i == 0 else PE(0), CC(i)])
        if i > 0: add(CNL(i), 5, EVEN, [CS(i), CC(i + n)])
    return g.dumps()


# ---------------------------------------------------------------- cunninghamsubexp.ml
def cunninghamsubexp(args):
    st = {"n": None, "binary": False}
    _parse(args, {"-binary": ("unit", lambda: st.update(binary=True)), None: lambda s: st.update(n=int(s))})  # 26-30
    n, binary = st["n"], st["binary"]
    def s2s(sy):                                                                   # lines 19-28
        k = sy[0]
        if k == "CycleNode": return f"d({sy[1]},{sy[2]})"
        if k in ("FinalSink", "FinalCycle", "LowSel"): return {"FinalSink": "s", "FinalCycle": "t", "LowSel": "p"}[k]
        return {"CycleCenter": "e", "CycleExit": "y", "CycleEntry": "q", "CycleSelector": "u", "UpperSelector": "w"}[k] + str(sy[1])
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    FC, FS, LS = ("FinalCycle",), ("FinalSink",), ("LowSel",)
    CE, US, CS, CC = (lambda i: ("CycleExit", i)), (lambda i: ("UpperSelector", i)), (lambda i: ("CycleSelector", i)), (lambda i: ("CycleCenter", i))
    CN, CEn = (lambda i, k: ("CycleNode", i, k)), (lambda i: ("CycleEntry", i))
    add(FC, 1, ODD, [FC])                                                          # lines 45-49
    add(FS, 2 * n + 10, ODD, [FC])
    add(US(n), 3, EVEN, [FS])
    add(CS(n), 3, EVEN, [FS])
    add(LS, 8, ODD, [CEn(0)])
    for i in range(n):                                                             # lines 51-66
        add(CE(i), 2 * i + 10, ODD, [US(i + 1)])
        add(CEn(i), 2 * i + 9, ODD, [CC(i)])
        add(CC(i), 6, ODD, [CN(i, 0), CE(i)])
        add(US(i), 3, EVEN, [US(i + 1), CEn(i)])
        add(CS(i), 3, EVEN, [CS(i + 1), CEn(i)])
        if binary:
            for j in range(2 * i + 2):
                add(CN(i, j), 5, EVEN, [FS, LS if j % 2 == 0 else CS(0), CN(i, j + 1) if j < 2 * i + 1 else CC(i)])
        else:
            for j in range(i + 1):
                add(CN(i, j), 5, EVEN, [CS(0), FS, LS, CN(i, j + 1) if j < i else CC(i)])
    return g.dumps()


# ---------------------------------------------------------------- randomedgeexptest.ml
def randomedgeexptest(args):
    st = {"n": 0, "al": 2, "pl": 6, "cl": 8, "strat": None}                        # lines 10-13
    def anon(s):                                                                   # lines 97-101
        st["n"] = int(s); st["al"] *= st["n"]; st["pl"] *= st["n"]; st["cl"] *= st["n"]
    _parse(args, {"-cl": ("int", lambda i: st.update(cl=i)), "-al": ("int", lambda i: st.update(al=i)),
                  "-pl": ("int", lambda i: st.update(pl=i)), "-int": ("str", lambda s: st.update(strat=s)), None: anon})
    n, uu, ss, tt = st["n"], st["al"], st["pl"], st["cl"]
    cyclelen = st["cl"]
    def s2s(sy):                                                                   # lines 37-57
        k = sy[0]
        fixed = {"Sink": "T", "SinkEntry": "t", "PacerExit": "L", "SelectorHighEntry": "Q"}
        if k in fixed: return fixed[k]
        if k == "AccessNode": return f"a({sy[1]},{sy[2]})"
        if k == "CountingLowNode": return f"d({sy[1]},0,{sy[2]})"
        if k == "CountingLowLeaver": return f"M({sy[1]},{sy[2]})"
        if k == "CountingLowLane": return f"P({sy[1]},{sy[2]})"
        if k == "PacedNode": return f"d({sy[1]},1,{sy[2]})"
        if k == "CountingHighNode": return f"d({sy[1]},0,{cyclelen})"
        return {"SuccessorLane": "c", "SelectorLane": "q", "SelectorLowEntry": "G", "AccessCenter": "A", "AccessLeaver": "K",
                "CountingEntry": "H", "CountingCenter": "e", "CountingExit": "C", "CountingHighLeaver": "F",
                "CountingHighLane": "W"}[k] + str(sy[1])
    T, t, L, Q = ("Sink",), ("SinkEntry",), ("PacerExit",), ("SelectorHighEntry",)
    c, q, G, A = (lambda i: ("SuccessorLane", i)), (lambda i: ("SelectorLane", i)), (lambda i: ("SelectorLowEntry", i)), (lambda i: ("AccessCenter", i))
    a, K, H, B = (lambda i, j: ("AccessNode", i, j)), (lambda i: ("AccessLeaver", i)), (lambda i: ("CountingEntry", i)), (lambda i: ("CountingCenter", i))
    b, M, P, C = (lambda i, j: ("CountingLowNode", i, j)), (lambda i, j: ("CountingLowLeaver", i, j)), (lambda i, j: ("CountingLowLane", i, j)), (lambda i: ("CountingExit", i))
    z, f, F, W = (lambda i, j: ("PacedNode", i, j)), (lambda i: ("CountingHighNode", i)), (lambda i: ("CountingHighLeaver", i)), (lambda i: ("CountingHighLane", i))

    def mystrat(s, n, node):                                                       # lines 66-79
        aa = [[ch == "1" for ch in part] for part in s.split("|")]
        bb = [all(aa[i]) for i in range(n)]
        k = node[0]
        if k == "SuccessorLane":
            i = node[1]; return t if i == n else (A(i) if bb[i] else c(i + 1))
        if k == "SelectorLane":
            i = node[1]; return t if i == n else (H(i) if bb[i] else q(i + 1))
        if k == "AccessNode":
            i, j = node[1], node[2]
            if j == 0: return A(i) if bb[i] else t
            return a(i, j - 1) if bb[i] else t
        if k == "PacedNode":
            i, j = node[1], node[2]
            if j == 0: return B(i) if bb[i] else L
            return z(i, j - 1) if bb[i] else L
        if k == "CountingLowNode":
            i, j = node[1], node[2]
            if j == 0: return B(i) if aa[i][0] else M(i, 0)
            return b(i, j - 1) if aa[i][j] else M(i, j)
        if k == "CountingHighNode":
            i = node[1]; return b(i, cyclelen - 1) if aa[i][cyclelen] else F(i)
        return t
    g = SymbolicPG()
    def add(sy, pr, pl, li):                                                       # lines 113-119 (see module note)
        if st["strat"] is not None:
            g.add_node(sy, pr, pl, li, s2s(sy) + "[" + s2s(mystrat(st["strat"], n, sy)) + "]")
        else:
            g.add_node(sy, pr, pl, li, s2s(sy))
    add(T, 1, ODD, [T])                                                            # lines 121-126
    add(t, 2 * tt * n + 6 * n + 12, ODD, [T])
    add(L, 2 * tt * n + 2 * n + 10, ODD, [c(0)])
    add(Q, 2 * tt * n + 2 * n + 8, ODD, [q(0)])
    for i in range(n + 1):                                                         # lines 128-131
        add(c(i), 3, EVEN, [t] if i == n else [A(i), c(i + 1)])
        add(q(i), 3, EVEN, [t] if i == n else [H(i), q(i + 1)])
    for i in range(n):                                                             # lines 133-159
        add(G(i), 2 * tt * n + 2 * i + 8, ODD, [q(0)])
        add(A(i), 6, ODD, [H(i), a(i, uu - 1)])
        for j in range(uu):
            add(a(i, j), 5, EVEN, [t, K(i), A(i) if j == 0 else a(i, j - 1)])
        add(K(i), 2 * tt * n + 2 * n + 4 * i + 11, ODD, [q(0)])
        add(H(i), 2 * tt * n + 2 * n + 4 * i + 13, ODD, [B(i)])
        add(B(i), 6, ODD, [C(i), f(i), z(i, ss - 1)])
        add(f(i), 5, EVEN, [F(i), b(i, tt - 1)])
        add(F(i), 7, ODD, [Q] if i == 0 else [Q, W(i - 1)])
        add(W(i), 3, ODD, [b(i, tt - 1)] if i == 0 else [b(i, tt - 1), W(i - 1)])
        for j in range(tt):
            add(b(i, j), 5, EVEN, [t, M(i, j), B(i) if j == 0 else b(i, j - 1)])
            add(M(i, j), 2 * tt - 2 * j + 2 * tt * i + 7, ODD, [G(i)] if i == 0 else [P(i - 1, j), G(i)])
            add(P(i, j), 3, ODD, [b(i, j)] if i == 0 else [b(i, j), P(i - 1, j)])
        add(C(i), 2 * tt * n + 2 * n + 4 * i + 14, ODD, [c(i + 1)])
        for j in range(ss):
            add(z(i, j), 5, EVEN, [t, L, B(i) if j == 0 else z(i, j - 1)])
    return g.dumps()


# ---------------------------------------------------------------- randomedgesubexp.ml
def randomedgesubexp(args):
    if len(args) != 1: raise SystemExit("specify index of game")                   # line 38
    n = int(args[0])
    access_cycle, intermediate_cycle = 2 * n, 4 * n                                # lines 41-44
    counting_cycle = lambda i: (i + 2) * n * 4
    def s2s(sy):                                                                   # lines 20-24
        if sy[0] == "CycleCenter": return "e" + str(sy[1])
        if sy[0] == "CycleNode": return f"d({sy[1]},0,{sy[2]})"
        if sy[0] == "IntermediateNode": return f"d({sy[1]},1,{sy[2]})"
        return ""
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))               # with_strategy = false
    FC, FS, UR, SR = ("FinalCycle",), ("FinalSink",), ("UpperRoot",), ("SelectorRoot",)
    CE, US, CS, CC = (lambda i: ("CycleExit", i)), (lambda i: ("UpperSelector", i)), (lambda i: ("CycleSelector", i)), (lambda i: ("CycleCenter", i))
    CN, IN, CEn = (lambda i, k: ("CycleNode", i, k)), (lambda i, k: ("IntermediateNode", i, k)), (lambda i: ("CycleEntry", i))
    AC, AN, AE = (lambda i: ("AccessCenter", i)), (lambda i, k: ("AccessNode", i, k)), (lambda i: ("AccessExit", i))
    add(FC, 1, ODD, [FC])                                                          # lines 59-64
    add(FS, 4 * n + 10, ODD, [FC])
    add(US(n), 3, EVEN, [FS])
    add(CS(n), 3, EVEN, [FS])
    add(UR, 8, ODD, [US(0)])
    add(SR, 3, ODD, [CS(0)])
    for i in range(n):                                                             # lines 66-83
        add(CE(i), 4 * i + 12, ODD, [US(i + 1)])
        add(AE(i), 4 * i + 9, ODD, [SR])
        add(CEn(i), 4 * i + 11, ODD, [CC(i)])
        add(AC(i), 6, ODD, [CEn(i), AN(i, 0)])
        add(CC(i), 6, ODD, [CN(i, 0), CE(i)])
        add(US(i), 3, EVEN, [US(i + 1), FS, AC(i)])
        add(CS(i), 3, EVEN, [CS(i + 1), FS, CEn(i)])
        for j in range(counting_cycle(i)):
            add(CN(i, j), 5, EVEN, [SR, FS, CN(i, j + 1) if j < counting_cycle(i) - 1 else IN(i, 0)])
        for j in range(intermediate_cycle):
            add(IN(i, j), 5, EVEN, [UR, FS, IN(i, j + 1) if j < intermediate_cycle - 1 else CC(i)])
        for j in range(access_cycle):
            add(AN(i, j), 5, EVEN, [AE(i), FS, AN(i, j + 1) if j < access_cycle - 1 else AC(i)])
    return g.dumps()


# ---------------------------------------------------------------- randomfacetsubexp.ml
def randomfacetsubexp(args):
    o = {"bc": -1, "bp": -1, "ap": -1, "ac": -1, "re": -1, "bcn": False, "ban": False, "bun": False}  # lines 32-39
    _parse(args, {"-bp": ("int", lambda i: o.update(bp=i)), "-ap": ("int", lambda i: o.update(ap=i)),
                  "-ac": ("int", lambda i: o.update(ac=i)), "-re": ("int", lambda i: o.update(re=i)),
                  "-bcn": ("unit", lambda: o.update(bcn=True)), "-ban": ("unit", lambda: o.update(ban=True)),
                  "-bun": ("unit", lambda: o.update(bun=True)), None: lambda s: o.update(bc=int(s))})
    if o["bc"] < 0: raise SystemExit("Index not specified.")                       # line 60
    n = o["bc"]
    binlog = lambda n: int(math.ceil(math.log(float(n)) / math.log(2.)))           # line 27
    d = o["ap"] if o["ap"] > 0 else binlog(n)                                      # lines 62-73
    cd = o["bp"] if o["bp"] > 0 else binlog(n) * d
    m = o["ac"] if o["ac"] > 0 else binlog(n)
    r = o["re"] if o["re"] > 0 else binlog(n)
    d = r * d if o["ban"] else d
    r_d = 1 if o["bcn"] else r
    cd = r * cd if o["bcn"] else cd
    r_cd = 1 if o["bcn"] else r
    def s2s(sy):                                                                   # line 21
        k, x = sy[0], sy[1:]
        tup = lambda: "(" + ",".join(map(str, x)) + ")"
        if k == "FinalCycle": return "q"
        if k == "FinalSink": return "p"
        if k in ("CycleCenter", "UpperNode", "Helper"): return {"CycleCenter": "e", "UpperNode": "k", "Helper": "h"}[k] + str(x[0])
        if k == "LaneEntryAccess": return ""
        return {"CycleNode": "d", "AccessNode": "b", "AccessCenter": "a", "CycleEntry": "c", "AccessEntry": "r", "LaneEntry": "c"}[k] + tup()
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    hc = [0]
    def addhelper(pr, pl, li):                                                     # lines 79-84
        hc[0] += 1
        add(("Helper", hc[0]), pr, pl, li)
        return ("Helper", hc[0])
    def divide(l):                                                                 # lines 86-91
        if not l: return [], []
        if len(l) == 1: return [l[0]], []
        a, b = divide(l[2:])
        return [l[0]] + a, [l[1]] + b
    def make_tree(l):                                                              # lines 93-99
        if not l: raise RuntimeError("impossible")
        if len(l) == 1: return l[0]
        if len(l) == 2: return addhelper(3, EVEN, [l[0], l[1]])
        left, right = divide(l)
        rt = make_tree(right)   # OCaml list literal: right-to-left evaluation
        lt = make_tree(left)
        return addhelper(3, EVEN, [lt, rt])
    FC, FS = ("FinalCycle",), ("FinalSink",)
    CN, CC, CEn = (lambda i, j: ("CycleNode", i, j)), (lambda i: ("CycleCenter", i)), (lambda i, j: ("CycleEntry", i, j))
    AN, AC, AE = (lambda i, j, k: ("AccessNode", i, j, k)), (lambda i, j: ("AccessCenter", i, j)), (lambda i, j, k: ("AccessEntry", i, j, k))
    LE, LEA, UN = (lambda i, j: ("LaneEntry", i, j)), (lambda i, j: ("LaneEntryAccess", i, j)), (lambda i: ("UpperNode", i))
    add(FC, 1, ODD, [FC])                                                          # lines 101-102
    add(FS, 6 + 2 * n, ODD, [FC])
    for i in range(n):                                                             # lines 104-132
        add(CC(i), 2, ODD, [UN(i)] + mkli(cd, lambda j: CN(i, j)))
        if i == n - 1:
            add(UN(i), 6 + 2 * i, EVEN, [FS])
        elif not o["bun"]:
            add(UN(i), 6 + 2 * i, EVEN, [x for k in range(m) for x in mkli(r, lambda s: AE(i + 1, k, s))])
        else:
            add(UN(i), 6 + 2 * i, EVEN, [make_tree(mkli(r, lambda s: make_tree(mkli(m, lambda k: AE(i + 1, k, s)))))])
        for j in range(cd):
            add(CN(i, j), 0, EVEN, [FS, CC(i)] + mkli(r_cd, lambda s: LE(i, s)))
        for k in range(m):
            add(AC(i, k), 2, ODD, [CEn(i, 0)] + mkli(d, lambda j: AN(i, k, j)))
            for j in range(d):
                add(AN(i, k, j), 0, EVEN, [FS, AC(i, k)] + mkli(r_d, lambda s: LEA(i, s)))
            for s in range(r):
                add(AE(i, k, s), 0, ODD, [AC(i, k)])
        for s in range(r):
            add(LE(i, s), 0, ODD, [FS if i == n - 1 else CN(i + 1, 0)])
            add(LEA(i, s), 4, ODD, [FS if i == n - 1 else CN(i + 1, 0)])
            add(CEn(i, s), 2, ODD, [CC(i)])
    return g.dumps()


# ---------------------------------------------------------------- switchallsubexp.ml / switchbestsubexp.ml helpers
def _lexp_factory(g, add, od2):                                                    # lines 49-60 / 49-60
    hc = [0]
    def left_exp(l):
        if not l: raise RuntimeError("imp")
        while len(l) > 1:
            a, b, rest = l[0], l[1], l[2:]
            hc[0] += 1
            add(("Helper", hc[0]), 0, EVEN, [a, b])
            l = [("Helper", hc[0])] + rest
        return l[0]
    def left_exp_(l):
        if len(l) <= 2: return l
        return [left_exp(l[:-1]), l[-1]]
    return (lambda l: left_exp_(l)) if od2 else (lambda l: l)


def switchallsubexp(args):
    st = {"n": None, "od2": False}
    _parse(args, {"-binary": ("unit", lambda: st.update(od2=True)), None: lambda s: st.update(n=int(s))})  # 33-38
    n = st["n"]
    lab = {"DecLaneEven": "a", "DecLaneOdd": "b", "CycleNode": "d", "CycleCenter": "e", "CycleAccess": "f", "CycleSelector": "g",
           "CycleLeaver": "h", "UpperSelector": "k", "Helper": "h"}
    fixed = {"DecLaneRoot": "c", "FinalSink": "p", "FinalCycle": "q", "StartEven": "s", "BitSelector": "r"}
    s2s = lambda sy: fixed[sy[0]] if sy[0] in fixed else lab[sy[0]] + str(sy[1])   # line 16
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    lexp = _lexp_factory(g, add, st["od2"])
    FC, SE, DLR, BS, FS = ("FinalCycle",), ("StartEven",), ("DecLaneRoot",), ("BitSelector",), ("FinalSink",)
    DLE, DLO, CN, CC = (lambda i: ("DecLaneEven", i)), (lambda i: ("DecLaneOdd", i)), (lambda i: ("CycleNode", i)), (lambda i: ("CycleCenter", i))
    CL, US, CA, CS = (lambda i: ("CycleLeaver", i)), (lambda i: ("UpperSelector", i)), (lambda i: ("CycleAccess", i)), (lambda i: ("CycleSelector", i))
    add(FC, 1, ODD, [FC])                                                          # lines 58-62
    add(SE, 8 * n + 6, EVEN, lexp([FS] + mkli(n, CA)))
    add(DLR, 8 * n + 4, EVEN, [SE, BS])
    add(BS, 8 * n + 8, EVEN, lexp([FS] + mkli(n, CS)))
    add(FS, 12 * n + 10, ODD, [FC])
    for i in range(2 * n):                                                         # lines 64-67
        add(DLE(i), 4 * n + 2 * i + 4, ODD, [DLO(i)])
        add(DLO(i), 4 * n + 2 * i + 3, EVEN, lexp([DLR, BS, SE]) if i == 0 else lexp([DLO(i - 1), BS, SE]))
    for i in range(n):                                                             # lines 69-76
        add(CN(i), 4 * i + 3, EVEN, lexp([SE, CC(i)] + mkli(2 * i + 2, DLE) + [BS]))
        add(CC(i), 4 * i + 4, ODD, [CN(i), CL(i)])
        add(CL(i), 8 * n + 4 * i + 12, ODD, [US(i)])
        add(US(i), 8 * n + 4 * i + 9, EVEN, lexp([FS] + mkli(n - i - 1, lambda j: CS(n - j - 1))))
        add(CA(i), 8 * n + 4 * i + 11, ODD, [CC(i)])
        add(CS(i), 4 * i + 6, EVEN, [CA(i), US(i)])
    return g.dumps()


def switchbestsubexp(args):
    st = {"n": None, "od2": False}
    _parse(args, {"-binary": ("unit", lambda: st.update(od2=True)), None: lambda s: st.update(n=int(s))})  # 35-40
    n = st["n"]
    lab = {"DecLaneEven": "a", "DecLaneOdd": "b", "CycleNode0": "e", "CycleNode1": "f", "CycleNode2": "g", "CycleCenter": "h",
           "CycleAccess": "k", "CycleSelector": "l", "CycleSelectorX": "y", "CycleLeaver": "m", "UpperSelector": "z", "Helper": "h"}
    fixed = {"DecLaneRoot": "c", "FinalSink": "p", "FinalCycle": "q", "StartEven": "s", "BitSelector": "u"}
    s2s = lambda sy: fixed[sy[0]] if sy[0] in fixed else lab[sy[0]] + str(sy[1])   # line 26
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    lexp = _lexp_factory(g, add, st["od2"])
    FC, SE, DLR, BS, FS = ("FinalCycle",), ("StartEven",), ("DecLaneRoot",), ("BitSelector",), ("FinalSink",)
    f = lambda name: (lambda i: (name, i))
    DLE, DLO, CN0, CN1, CN2, CC = f("DecLaneEven"), f("DecLaneOdd"), f("CycleNode0"), f("CycleNode1"), f("CycleNode2"), f("CycleCenter")
    CA, CS, CSX, CL, US = f("CycleAccess"), f("CycleSelector"), f("CycleSelectorX"), f("CycleLeaver"), f("UpperSelector")
    add(FC, 1, ODD, [FC])                                                          # lines 62-68
    add(DLR, 20 * n, ODD, [BS])
    add(SE, 20 * n + 2, EVEN, lexp([FS] + mkli(n, CA)))
    add(BS, 20 * n + 4, EVEN, lexp([FS] + mkli(n, CSX)))
    add(FS, 24 * n + 6, ODD, [FC])
    for i in range(6 * n - 2):                                                     # lines 70-73 (0..6n-3)
        add(DLE(i), 8 * n + 4 + 2 * i, ODD, [DLO(i)])
        add(DLO(i), 8 * n + 3 + 2 * i, EVEN, lexp([DLR if i == 0 else DLO(i - 1), BS, SE]))
    for i in range(n):                                                             # lines 75-85
        add(CN0(i), i * 8 + 3, EVEN, lexp([SE, CN1(i), DLR] + mkli(2 * i + 1, lambda j: DLE(3 * j + 2))))
        add(CN1(i), i * 8 + 5, EVEN, lexp([CN2(i)] + mkli(2 * i + 1, lambda j: DLE(3 * j + 1))))
        add(CN2(i), i * 8 + 7, EVEN, lexp([CC(i)] + mkli(2 * i + 2, lambda j: DLE(3 * j))))
        add(CC(i), i * 8 + 8, ODD, [CN0(i), CL(i)])
        add(CS(i), i * 8 + 9, EVEN, [CA(i), US(i)])
        add(CSX(i), i * 8 + 10, EVEN, [CS(i), US(i)])
        add(US(i), 20 * n + 5 + 4 * i, EVEN, lexp([FS] + mkli(n - i - 1, lambda j: CSX(n - j - 1))))
        add(CA(i), 20 * n + 7 + 4 * i, ODD, [CC(i)])
        add(CL(i), 20 * n + 8 + 4 * i, ODD, [US(i)])
    return g.dumps()


# ---------------------------------------------------------------- zadehexp.ml
_ZLAB = {"PairSelector": "d", "CycleCenter1": "E", "CycleCenter2": "X", "CycleNodeX1": "a", "CycleNodeX2": "w",
         "CycleNodeY1": "b", "CycleNodeY2": "v", "CycleNodeX1T": "o", "CycleNodeX2T": "q", "CycleNodeY1T": "p",
         "CycleNodeY2T": "r", "UpperSelector1": "c", "UpperSelector2": "z", "Selector": "m", "UpDown1": "g",
         "UpDown2": "s", "Helper": "u"}                                            # zadehexp.ml lines 28-47


def zadehexp(args):
    if len(args) != 1: raise SystemExit("specify index of game")                   # line 52
    n = int(args[0])
    s2s = lambda sy: {"FinalCycle": "Z", "FinalSink": "Y"}[sy[0]] if len(sy) == 1 else _ZLAB[sy[0]] + str(sy[1])
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    add1 = lambda sy, pr, li: add(sy, pr, ODD, li)
    add0 = lambda sy, pr, li: add(sy, pr, EVEN, li)
    f = lambda name: (lambda i: (name, i))
    FC, FS = ("FinalCycle",), ("FinalSink",)
    PS, CC1, CC2, X1, X2, Y1, Y2 = f("PairSelector"), f("CycleCenter1"), f("CycleCenter2"), f("CycleNodeX1"), f("CycleNodeX2"), f("CycleNodeY1"), f("CycleNodeY2")
    X1T, X2T, Y1T, Y2T = f("CycleNodeX1T"), f("CycleNodeX2T"), f("CycleNodeY1T"), f("CycleNodeY2T")
    UD1, UD2, US1, US2, Sel, Hl = f("UpDown1"), f("UpDown2"), f("UpperSelector1"), f("UpperSelector2"), f("Selector"), f("Helper")
    add1(FC, 1, [FC])                                                              # lines 63-64
    add1(FS, 2 * n + 12, [FC])
    for i in range(n):                                                             # lines 67-88
        add0(X1(i), 3, [CC1(i), X1T(i)])
        add0(X1T(i), 3, [PS(0), Sel(1)])
        if i < n - 1: add0(X2(i), 3, [CC2(i), X2T(i)])
        if i < n - 1: add0(X2T(i), 3, [PS(0), Sel(1)])
        add0(Y1(i), 3, [CC1(i), Y1T(i)])
        add0(Y1T(i), 3, [PS(0), Sel(1)])
        if i < n - 1: add0(Y2(i), 3, [CC2(i), Y2T(i)])
        if i < n - 1: add0(Y2T(i), 3, [PS(0), Sel(1)])
        add0(PS(i), 2 * i + 11, [CC1(i), CC2(i)] if i < n - 1 else [CC1(i)])
        add0(Sel(i), 3, [PS(i), Sel(i + 1) if i < n - 1 else FS])
        add1(CC1(i), 6, [X1(i), Y1(i), UD1(i)])
        if i < n - 1: add1(CC2(i), 4, [X2(i), Y2(i), UD2(i)])
        add0(UD1(i), 10, [US1(i), Sel(0)])
        if i < n - 1: add0(UD2(i), 8, [Hl(i), Sel(0)])
        add0(US1(i), 2 * i + 12, [Sel(i + 2) if i < n - 2 else FS])
        if i < n - 1:
            add1(Hl(i), 5, [US2(i)])
            add0(US2(i), 2 * i + 12, [PS(i + 1)])
    return g.dumps()


# ---------------------------------------------------------------- zadehsubexp.ml
def zadehsubexp(args):
    if len(args) != 1: raise SystemExit("specify index of game")                   # line 52
    n = int(args[0])
    lab = {"PairSelector": "d", "CycleEntry1": "h", "CycleEntry2": "k", "CycleCenter1": "E", "CycleCenter2": "X",
           "CycleNodeX1": "a", "CycleNodeX2": "w", "CycleNodeY1": "b", "CycleNodeY2": "v", "UpperSelector1": "c",
           "UpperSelector2": "u", "UpDown1": "g", "UpDown2": "s"}                  # lines 28-44
    s2s = lambda sy: {"FinalCycle": "Z", "FinalSink": "Y", "Selector": "f"}[sy[0]] if len(sy) == 1 else lab[sy[0]] + str(sy[1])
    g = SymbolicPG()
    add = lambda sy, pr, pl, li: g.add_node(sy, pr, pl, li, s2s(sy))
    add1 = lambda sy, pr, li: add(sy, pr, ODD, li)
    add0 = lambda sy, pr, li: add(sy, pr, EVEN, li)
    f = lambda name: (lambda i: (name, i))
    FC, FS, Sel = ("FinalCycle",), ("FinalSink",), ("Selector",)
    PS, CE1, CE2, CC1, CC2 = f("PairSelector"), f("CycleEntry1"), f("CycleEntry2"), f("CycleCenter1"), f("CycleCenter2")
    X1, X2, Y1, Y2 = f("CycleNodeX1"), f("CycleNodeX2"), f("CycleNodeY1"), f("CycleNodeY2")
    UD1, UD2, US1, US2 = f("UpDown1"), f("UpDown2"), f("UpperSelector1"), f("UpperSelector2")
    allPS = lambda: _mkli_pos(n, PS)
    add1(FC, 1, [FC])                                                              # lines 63-66
    add1(FS, 2 * n + 14, [FC])
    add0(Sel, 3, [FS] + allPS())
    add1(PS(n), 2 * n + 13, [FS])
    for i in range(n):                                                             # lines 68-82
        add0(PS(i), 2 * i + 13, [FS, CC1(i), CC2(i)] + allPS())
        add1(CE1(i), 11, [CC1(i)])
        add1(CE2(i), 11, [CC2(i)])
        add1(CC1(i), 6, [X1(i), Y1(i), UD1(i)])
        add1(CC2(i), 4, [X2(i), Y2(i), UD2(i)])
        add0(X1(i), 3, [FS, CC1(i)] + allPS())
        add0(X2(i), 3, [FS, CC2(i)] + allPS())
        add0(Y1(i), 3, [FS, CC1(i)] + allPS())
        add0(Y2(i), 3, [FS, CC2(i)] + allPS())
        add0(UD1(i), 10, [US1(i), Sel])
        add0(UD2(i), 8, [US2(i), Sel])
        add0(US1(i), 2 * i + 14, [FS] + _mkli_pos(n - (i + 2), lambda j: PS(i + 2 + j)))  # mkli2 (i+2) n
        add0(US2(i), 2 * i + 14, [PS(i + 1)])
    return g.dumps()


def _accept_int(fn):
    """GENS[name](N) or GENS[name](["N", flags...]) (argument array exactly as PGSolver passes it)."""
    def w(args):
        return fn([str(args)] if isinstance(args, int) else list(args))
    w.__name__, w.__doc__ = fn.__name__, fn.__doc__
    return w


GENS = {"cunninghamexp": cunninghamexp, "cunninghamsubexp": cunninghamsubexp, "randomedgeexptest": randomedgeexptest,
        "randomedgesubexp": randomedgesubexp, "randomfacetsubexp": randomfacetsubexp, "switchallsubexp": switchallsubexp,
        "switchbestsubexp": switchbestsubexp, "zadehexp": zadehexp, "zadehsubexp": zadehsubexp}
GENS = {k: _accept_int(v) for k, v in GENS.items()}

if __name__ == "__main__":
    sys.stdout.write(GENS[sys.argv[1]](sys.argv[2:]))
