#!/usr/bin/env python3
"""Probe: given a weak (n,d) separator delta with k states, is there a STRONG (n,d) separator with k states that differs
from it in at most t transitions?  Reports the least t (states are kept in place; BFS symmetry breaking is NOT applied
because the given delta need not be BFS-numbered)."""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import check_separator
def least_rewire(n, d, conv, delta, tmax):
    k = len(delta); evens = maximal_graphs(n, d, conv, 0, verify=False)
    for t in range(0, tmax + 1):
        enc = Encoder.__new__(Encoder)
        from pysat.solvers import Solver
        enc.n, enc.d, enc.k, enc.strong = n, d, k, True; enc.nv = 0; enc.solver = Solver(name='cadical153'); enc.nclauses = 0
        enc.t = [[[enc.new() for _ in range(k + 1)] for _ in range(d)] for _ in range(k)]
        for q in range(k):
            for a in range(d): enc.exactly_one(enc.t[q][a])
        enc.strong_condition(); enc.require_close_to(delta, t)
        for g in evens: enc.add_even(g)
        aut = enc.solve(); enc.delete()
        if aut is not None:
            assert not check_separator(aut, evens, [], True)
            diff = [(q, a + 1, delta[q][a], aut['delta'][q][a]) for q in range(k) for a in range(d) if delta[q][a] != aut['delta'][q][a]]
            return t, diff
    return None, None
cases = [(2, 3, 'E', [[1, 0, 1], [None, 2, None], [1, 0, None]]),
         (3, 3, 'V', json.load(open('results/automata/weak_V_n3_d3.json'))['automaton']['delta']),
         (3, 4, 'V', [[1, 1, 1, 0], [2, 1, 3, 0], [3, 1, None, 0], [None, 4, None, 0], [2, 4, None, 0]]),
         (2, 2, 'V', [[1, 0], [None, 2], [2, 0]]),
         (2, 6, 'E', [[1, 0, 1, 0, 2, 0], [2, 1, None, 0, None, 0], [None, 1, None, 1, None, 0]]),
         (3, 6, 'V', json.load(open('results/automata/weak_V_n3_d6.json'))['automaton']['delta'])]
for n, d, conv, delta in cases:
    t, diff = least_rewire(n, d, conv, delta, 6)
    print(f"({n},{d}) {conv} k={len(delta)}: least rewiring to a strong separator of the same size: t={t}; changed (state, letter, old, new): {diff}")
