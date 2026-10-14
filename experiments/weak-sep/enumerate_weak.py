#!/usr/bin/env python3
"""Falsification test for SL8 (Lead 21:40Z), in the contentful Hamming form: enumerate ALL deterministic weak
(n,d)-separators with exactly k reachable states (BFS-canonical numbering via the encoder's symmetry breaking, blocking
clauses on the transition variables), and for each compute the least t such that a STRONG (n,d)-separator on the same
states and initial state exists within Hamming distance t (t <= TMAX; 'none' otherwise).  Also reports how many of the
weak separators are themselves strong (t = 0).  Usage: enumerate_weak.py n d conv k [tmax] [max_solutions]"""
import sys, pathlib, time, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pysat.solvers import Solver
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import check_separator, language_in_limsup_even
n, d, conv, k = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
TMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 3
MAXSOL = int(sys.argv[6]) if len(sys.argv) > 6 else 100000
evens = maximal_graphs(n, d, conv, 0, verify=False); odds = maximal_graphs(n, d, conv, 1, verify=False)
enc = Encoder(n, d, k, False)
for g in evens: enc.add_even(g)
for g in odds: enc.add_odd(g)

def least_t(delta):
    for t in range(0, TMAX + 1):
        e = Encoder.__new__(Encoder); e.n, e.d, e.k, e.strong = n, d, k, True; e.nv = 0; e.solver = Solver(name='cadical153'); e.nclauses = 0
        e.t = [[[e.new() for _ in range(k + 1)] for _ in range(d)] for _ in range(k)]
        for q in range(k):
            for a in range(d): e.exactly_one(e.t[q][a])
        e.strong_condition(); e.require_close_to(delta, t)
        for g in evens: e.add_even(g)
        aut = e.solve(); e.delete()
        if aut is not None:
            assert not check_separator(aut, evens, [], True); return t
    return None

t0 = time.time(); count = 0; hist = {}; worst = []
while count < MAXSOL:
    aut = enc.solve()
    if aut is None: break
    bad = check_separator(aut, evens, odds, False)
    assert not bad, "enumerated automaton fails the checker: encoding bug"
    count += 1
    t = least_t(aut['delta']); hist[t] = hist.get(t, 0) + 1
    if t is None or t >= 2: worst.append((t, aut['delta']))
    # block this exact transition function
    enc.add([-enc.t[q][a][(enc.k if aut['delta'][q][a] is None else aut['delta'][q][a])] for q in range(k) for a in range(d)])
res = {'n': n, 'd': d, 'conv': conv, 'k': k, 'weak_separators_enumerated': count, 'complete': count < MAXSOL,
       'least_rewiring_histogram': {str(a): b for a, b in sorted(hist.items(), key=lambda x: (x[0] is None, x[0]))},
       'instances_with_t_ge_2_or_none': worst[:20], 'seconds': round(time.time() - t0, 1)}
out = pathlib.Path(f'results/sl8/enum_{conv}_n{n}_d{d}_k{k}.json'); out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(res, indent=1))
print(f"SL8 test {conv} ({n},{d}) k={k}: {count} weak separators{'' if res['complete'] else ' (capped)'}; least-t histogram {res['least_rewiring_histogram']}; {res['seconds']}s")
