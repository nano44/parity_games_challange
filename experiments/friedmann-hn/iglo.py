#!/usr/bin/env python3
"""Faithfulness check of hn.py against [F] Theorem 8.4 / Lemma 8.3: strategy improvement with the globally optimizing
policy I^glo from ι_{H_n}, bare loop (no PGSolver preprocessing or transformations). I^glo = PGSolver's
switch_globally_best.ml policy as ported in experiments/hard-families/pgsolver_si.py (SI.policy_switchbest; [F] §8.4
end: PGSolver contains the I^glo implementation used for Figure 11). Valuations: VJ, SI.evaluate.
Prints iterations (improvement steps), Lemma 8.3 (1) (Odd wins all) and (2) (cycle component = x for every node, every step).
Usage: iglo.py N [--mode fig|table]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "hard-families")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
from pgsolver_si import SI
import hn

a = sys.argv[1:]
n = int(a[0]); mode = a[a.index("--mode") + 1] if "--mode" in a else "fig"
g, ix = hn.build(n, mode)
si = SI(g)
io = hn.iota(n, ix)
strat = [io.get(v, -1) for v in range(g.n)]
valu = si.evaluate(strat)
steps, sinkok = 0, True
improvable = lambda: any(g.owner[i] == 0 and si.nvo(valu[strat[i]], valu[si.best(valu, i)]) < 0 for i in range(g.n))
while improvable():
    sinkok &= all(valu[v][0] == ix["x"] for v in range(g.n))
    strat = si.policy_switchbest(strat, valu)
    valu = si.evaluate(strat)
    steps += 1
sinkok &= all(valu[v][0] == ix["x"] for v in range(g.n))
win = [g.prio[valu[i][0]] % 2 for i in range(g.n)]
print(f"H_{n} mode {mode}: I^glo steps {steps} (2^n = {2**n}); Odd wins all: {all(w == 1 for w in win)}; cycle comp x always: {sinkok}")
