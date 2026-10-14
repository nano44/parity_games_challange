#!/usr/bin/env python3
"""Rule extraction for SL8-min: for every MINIMAL weak separator (k = w) at the given cell that is not strong, list ALL
one-transition rewires giving a strong separator (state, letter, old target, new target), together with the odd simple
cycles of the weak automaton and whether the rewired transition lies on an odd cycle."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pysat.solvers import Solver
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import check_separator, language_in_limsup_even
from lasso_analysis import odd_cycles
n, d, conv, k = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
evens = maximal_graphs(n, d, conv, 0, verify=False); odds = maximal_graphs(n, d, conv, 1, verify=False)
enc = Encoder(n, d, k, False)
for g in evens: enc.add_even(g)
for g in odds: enc.add_odd(g)
def all_single_rewires(delta):
    out = []
    for q in range(k):
        for a in range(d):
            for new in list(range(k)) + [None]:
                if new == delta[q][a]: continue
                d2 = [row[:] for row in delta]; d2[q][a] = new
                aut = {'k': k, 'd': d, 'delta': d2}
                if not check_separator(aut, evens, [], True): out.append((q, a + 1, delta[q][a], new))
    return out
res = []
while True:
    aut = enc.solve()
    if aut is None: break
    delta = aut['delta']
    enc.add([-enc.t[q][a][(k if delta[q][a] is None else delta[q][a])] for q in range(k) for a in range(d)])
    if language_in_limsup_even(aut): continue
    cyc, _ = odd_cycles(aut)
    cyc_edges = set()
    for states, labels in cyc:
        for i, q in enumerate(states): cyc_edges.add((q, labels[i]))
    rew = all_single_rewires(delta)
    res.append({'delta': delta, 'odd_cycles': [(list(s), list(l)) for s, l in cyc],
                'rewires': [{'q': q, 'letter': p, 'old': o, 'new': nw, 'on_odd_cycle': (q, p) in cyc_edges} for q, p, o, nw in rew]})
    print(f"weak {conv} ({n},{d}) k={k}: {delta}\n   odd cycles {[(s,l) for s,l in cyc]}\n   one-transition strong rewires: {[(r['q'],r['letter'],r['old'],r['new'],'cyc' if r['on_odd_cycle'] else 'off') for r in res[-1]['rewires']]}")
pathlib.Path('results/sl8').mkdir(exist_ok=True)
json.dump(res, open(f'results/sl8/rules_min_{conv}_n{n}_d{d}_k{k}.json', 'w'), indent=1)
print(f"{len(res)} non-strong minimal weak separators; with >=1 single rewire: {sum(1 for r in res if r['rewires'])}")
