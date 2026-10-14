"""Structural analysis of a computed separator: is it strong?  Is its even-used part (Live) free of odd cycles
(i.e. can it be pruned to a strong separator of the same size)?"""
from __future__ import annotations
from .graphs import Graph, is_parity_graph, maximal_graphs
from .automata import language_in_limsup_even


def live_transitions(aut, evens):
    """transitions (q, p, q2) used by the run of A on some finite path of some even graph with <= n vertices."""
    delta = aut['delta']; live = set()
    for g in evens:
        start = [(v, 0) for v in range(g.n)]
        seen = set(start); st = list(start)
        while st:
            v, q = st.pop()
            for (p, v2) in g.out(v):
                q2 = delta[q][p - 1]
                assert q2 is not None
                live.add((q, p, q2))
                if (v2, q2) not in seen:
                    seen.add((v2, q2)); st.append((v2, q2))
    return live


def analyze(res):
    aut = res['automaton']; n, d, conv = res['n'], res['d'], res['conv']
    evens = maximal_graphs(n, d, conv, 0, verify=False)
    live = live_transitions(aut, evens)
    k = aut['k']
    live_even = is_parity_graph(Graph(k, frozenset(live)), 0)
    return {'strong': language_in_limsup_even(aut), 'live_transitions': len(live),
            'all_transitions': sum(1 for row in aut['delta'] for x in row if x is not None),
            'live_has_no_odd_cycle': live_even}
