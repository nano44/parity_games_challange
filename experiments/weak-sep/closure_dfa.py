#!/usr/bin/env python3
"""The canonical weak separator (theory box 2026-10-22, docs/struct/S5-weak-strong.md §8).

P_E = finite words read along paths (from any vertex) of even X-graphs with <= n vertices = prefixes of the maximal even
graphs' paths (wsep.graphs coverage).  Its closure cl(P_E) (infinite words all of whose prefixes are in P_E) is a safety
language containing EvenCycles_{n,d}, and every deterministic safety automaton accepting EvenCycles_{n,d} accepts
cl(P_E).  Hence the minimal DFA of P_E (rejecting sink not counted) is a weak (n,d)-separator whenever one exists, and
c(n,d) := its number of states satisfies w(n,d) <= c(n,d).
Computation: NFA = disjoint union of the maximal even graphs (all vertices initial; letter of a step as in the
convention), subset construction, Moore minimisation; the result is re-checked as a weak separator by wsep.automata
on the full families (W1 and W2), and its strongness is reported.
Usage: closure_dfa.py n d conv [--max-states M]"""
import sys, pathlib, argparse, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.automata import check_separator, language_in_limsup_even

ap = argparse.ArgumentParser()
ap.add_argument('n', type=int); ap.add_argument('d', type=int); ap.add_argument('conv')
ap.add_argument('--max-states', type=int, default=2_000_000)
a = ap.parse_args()
evens = maximal_graphs(a.n, a.d, a.conv, 0, verify=False)
odds = maximal_graphs(a.n, a.d, a.conv, 1, verify=False)
# NFA states: (graph index, vertex); succ[(g,v)][p] = set of (g,v2)
succ = {}
for gi, g in enumerate(evens):
    for v in range(g.n):
        succ[(gi, v)] = {}
    for (u, p, v) in g.edges:
        succ[(gi, u)].setdefault(p, set()).add((gi, v))
start = frozenset(succ)
index = {start: 0}; order = [start]; delta = []
i = 0
while i < len(order):
    S = order[i]; row = []
    for p in range(1, a.d + 1):
        T = frozenset(x for s in S for x in succ[s].get(p, ()))
        if not T:
            row.append(None); continue
        if T not in index:
            index[T] = len(order); order.append(T)
            if len(order) > a.max_states:
                sys.exit(f"subset construction exceeded {a.max_states} states")
        row.append(index[T])
    delta.append(row); i += 1
k0 = len(delta)
# Moore minimisation (all states accepting; None = sink)
part = [0] * k0
while True:
    sig = {}
    new = []
    for q in range(k0):
        key = (part[q],) + tuple(None if x is None else part[x] for x in delta[q])
        new.append(sig.setdefault(key, len(sig)))
    if len(sig) == len(set(part)):
        break
    part = new
# renumber with the initial state 0
cls = {}; cls[part[0]] = 0
for q in range(k0):
    cls.setdefault(part[q], len(cls))
k = len(cls)
mdelta = [None] * k
for q in range(k0):
    c = cls[part[q]]
    if mdelta[c] is None:
        mdelta[c] = [None if x is None else cls[part[x]] for x in delta[q]]
aut = {'k': k, 'd': a.d, 'delta': mdelta}
bad = check_separator(aut, evens, odds, False)
strong = language_in_limsup_even(aut)
print(f"c^{a.conv}({a.n},{a.d}) = {k} (subset DFA {k0} states); weak separator re-check: {'OK' if not bad else 'FAILED ' + str(bad[:1])}; strong: {strong}")
out = pathlib.Path(__file__).parent / 'results' / 'closure' / f"c_{a.conv}_n{a.n}_d{a.d}.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({'n': a.n, 'd': a.d, 'conv': a.conv, 'value': k, 'subset_states': k0, 'weak_ok': not bad,
                           'strong': strong, 'automaton': aut}, indent=1))
