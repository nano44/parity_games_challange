"""Deterministic safety automata and the independent checker for (W1), (W2), (S2) (docs/struct/S1-statement.md D4, D5).
An automaton is a dict {'k': k, 'd': d, 'delta': [[q' or None (= bottom) for p in 1..d] for q in 0..k-1]}, initial state 0.
"""
from __future__ import annotations
from .graphs import Graph


def product_reach(aut, g: Graph):
    """Reachable non-bottom product states from V(H) x {q0}; returns (states, edges, hit_bottom)."""
    delta = aut['delta']
    start = [(v, 0) for v in range(g.n)]
    seen = set(start); st = list(start); edges = []; hit = False
    while st:
        v, q = st.pop()
        for (p, v2) in g.out(v):
            q2 = delta[q][p - 1]
            if q2 is None:
                hit = True
                continue
            edges.append(((v, q), (v2, q2)))
            if (v2, q2) not in seen:
                seen.add((v2, q2)); st.append((v2, q2))
    return seen, edges, hit


def has_cycle(nodes, edges):
    adj = {x: [] for x in nodes}
    for a, b in edges:
        adj[a].append(b)
    WHITE, GREY, BLACK = 0, 1, 2
    col = {x: WHITE for x in nodes}
    for s in nodes:
        if col[s] != WHITE:
            continue
        stack = [(s, iter(adj[s]))]; col[s] = GREY
        while stack:
            x, it = stack[-1]
            for y in it:
                if col[y] == GREY:
                    return True
                if col[y] == WHITE:
                    col[y] = GREY; stack.append((y, iter(adj[y]))); break
            else:
                col[x] = BLACK; stack.pop()
    return False


def accepts_all(aut, g: Graph) -> bool:
    """(W1): no path of g drives A into bottom."""
    return not product_reach(aut, g)[2]


def rejects_all(aut, g: Graph) -> bool:
    """(W2): every infinite path of g is rejected, i.e. the reachable non-bottom product is acyclic."""
    nodes, edges, _ = product_reach(aut, g)
    return not has_cycle(nodes, edges)


def aut_reachable(aut):
    delta = aut['delta']; seen = {0}; st = [0]
    while st:
        q = st.pop()
        for q2 in delta[q]:
            if q2 is not None and q2 not in seen:
                seen.add(q2); st.append(q2)
    return seen


def language_in_limsup_even(aut) -> bool:
    """(S2): every cycle of the reachable transition graph of A has even maximum letter."""
    delta = aut['delta']; R = aut_reachable(aut)
    edges = [(q, p, delta[q][p - 1]) for q in R for p in range(1, aut['d'] + 1) if delta[q][p - 1] is not None]
    return Graph.__new__(Graph) and _is_even_labelled(len(delta), edges)


def _is_even_labelled(k, edges):
    from .graphs import is_parity_graph
    return is_parity_graph(Graph(k, frozenset(edges)), 0)


def check_separator(aut, evens, odds, strong: bool):
    """Returns list of violations ('W1', g) / ('W2', g) / ('S2', None)."""
    bad = []
    for g in evens:
        if not accepts_all(aut, g):
            bad.append(('W1', g))
    if strong:
        if not language_in_limsup_even(aut):
            bad.append(('S2', None))
    else:
        for g in odds:
            if not rejects_all(aut, g):
                bad.append(('W2', g))
    return bad


def run_word_prefix(aut, word):
    q = 0
    for p in word:
        q = aut['delta'][q][p - 1]
        if q is None:
            return None
    return q
