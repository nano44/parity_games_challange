#!/usr/bin/env python3
"""L-COMP box 43 item 1 (b): cross-checks of the lifted runs of lev43.py (game mode).
 (1) game table: my lmcs(n) (lev43.py, from T66's quote of [F11] Table 4) against L-LIT's function lmcs (claude/l-lit
     docs/lit/T66-depth-check.py; env LLIT = a checkout / archive holding docs/lit and experiments/): priorities, owners, successor sets,
     names and the start must be equal. Skipped when LLIT is not set.
 (2) second engine: at every state of MY Howard run (n5b SpecSI values, my step), L-SI's engine experiments/si/si.py re-evaluates the same
     strategy: cycle node, Pi (as a vertex set), length at every vertex and Odd's choice at every gate must be equal [valdiff, taudiff:
     unit (vertex, state)]; and si.py's own Howard run (rule_switch_all from the same start) must have the same strategy sequence
     [seqdiff: unit state] and the same T.
Usage: xgame43.py lmcs|switchall NMIN NMAX"""
import sys, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [H, os.path.join(R, "experiments", "si")]
import lev43, si


def llit_lmcs(n):
    root = os.environ["LLIT"]
    spec = importlib.util.spec_from_file_location("t66", os.path.join(root, "docs", "lit", "T66-depth-check.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.lmcs(n)


for N in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
    g, st, names = (lev43.lmcs if sys.argv[1] == "lmcs" else lev43.switchall)(N); out = []
    if sys.argv[1] == "lmcs" and os.environ.get("LLIT"):
        g2, st2, names2 = llit_lmcs(N)
        same = (list(g2.prio) == list(g.prio) and list(g2.owner) == list(g.owner) and [sorted(set(s)) for s in g2.succ] == [sorted(set(s)) for s in g.succ]
                and list(names2) == list(names) and list(st2) == list(st))
        out.append("table = L-LIT lmcs: %s" % same)
    Hs = lev43.howard(g, st); T = len(Hs) - 1
    eng = si.Engine(g); inv = [0] * g.n
    for v in range(g.n): inv[eng.rank[v]] = v
    gates = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    valdiff = taudiff = 0
    for t in range(T + 1):
        val, ch, s = Hs[t]; v2, tau2 = eng.evaluate(tuple(s))
        for v in range(g.n):
            w, mask, ln = v2[v]; pi = frozenset(inv[i] for i in range(g.n) if (mask >> i) & 1)
            if (w, pi, ln) != (val[v][0], frozenset(val[v][1]), val[v][2]): valdiff += 1
        taudiff += sum(1 for q in gates if tau2[q] != ch[q])
    # si.py's own run
    strat = tuple(st); seq = [strat]
    val, tau = eng.evaluate(strat)
    while True:
        imp = eng.improving(strat, val)
        if not imp: break
        strat = eng.rule_switch_all(strat, val, imp, None); val, tau = eng.evaluate(strat); seq.append(strat)
    seqdiff = sum(1 for t in range(min(len(seq), T + 1)) if list(seq[t]) != list(Hs[t][2])) + abs(len(seq) - (T + 1))
    print("%s N %d n %d T %d | si.py T %d seqdiff %d valdiff %d taudiff %d | %s" % (sys.argv[1], N, g.n, T, len(seq) - 1, seqdiff, valdiff, taudiff, "; ".join(out)), flush=True)
