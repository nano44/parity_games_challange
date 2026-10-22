"""Labelled graphs over Sigma_d = {1..d} and enumeration of the MAXIMAL even / odd graphs on n vertices.

Conventions (docs/struct/S1-statement.md D1):
  'E': edge-labelled, E subset of V x Sigma_d x V (parallel edges with distinct labels allowed; CFGO 2104.05262 §2.1).
  'S': simple edge-labelled, at most one label per ordered pair (u,v) (CDFJLP read as E a set of edges with pi: E -> N).
  'V': vertex-labelled, pr: V -> Sigma_d, edge (u,v) carries pr(u) (TARGET.md vertex priorities, shifted).
Classes: V subset of S subset of E, so w^V <= w^S <= w^E and the same for s.
A graph is stored as Graph(n, edges, pr) with edges a frozenset of (u, p, v); pr is None for 'E', a tuple for 'V'.

Enumeration method: every even graph admits a progress measure, i.e. a map mu from V to the leaves of an ordered tree
of height h = ceil(d/2) (one level per odd letter) such that each edge (u,p,v) satisfies
    trunc(mu(u), p) >= trunc(mu(v), p)   (p even)      trunc(mu(u), p) > trunc(mu(v), p)   (p odd)
in lexicographic order (CDFJLP 1807.10546 Thm 2.1 with [25, Lemma 2]; CFGO Lemma 6.4/6.5, G(T)). Conversely every graph
G_mu of all edges satisfying the condition is even. So the family {G_mu} covers every even graph; we enumerate ordered
trees with exactly n leaves, build G_mu, canonicalise under vertex permutations, and keep the maximal ones.
Odd graphs: shift labels by +1 (odd graphs over Sigma_d = even graphs over {2..d+1}), restrict, shift back.
Both the parity of every generated graph and its maximality are re-verified by brute force (is_parity_graph, is_maximal),
and for tiny parameters `coverage_bruteforce` checks the covering claim against ALL graphs.
"""
from __future__ import annotations
import itertools
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Graph:
    n: int
    edges: frozenset  # of (u, p, v)
    pr: tuple | None = None  # vertex labels for convention 'V'
    simple: bool = False  # convention 'S': at most one label per ordered pair

    def out(self, u):
        return [(p, v) for (x, p, v) in self.edges if x == u]


def reach(n, adj, src):
    seen = {src}
    st = [src]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); st.append(y)
    return seen


def is_parity_graph(g: Graph, win: int) -> bool:
    """win=0: every cycle has even maximum; win=1: odd maximum.  Brute force, independent of the enumeration."""
    bad = [p for p in {e[1] for e in g.edges} if p % 2 != win]
    for p in bad:
        adj = [[] for _ in range(g.n)]
        for (u, q, v) in g.edges:
            if q <= p:
                adj[u].append(v)
        for (u, q, v) in g.edges:
            if q == p and u in reach(g.n, adj, v):  # cycle through (u,p,v) with all labels <= p: maximum p
                return False
    return True


def all_possible_edges(g: Graph, d: int):
    if g.pr is None and not g.simple:
        return [(u, p, v) for u in range(g.n) for p in range(1, d + 1) for v in range(g.n)]
    if g.simple:
        used = {(u, v) for (u, p, v) in g.edges}
        return [(u, p, v) for u in range(g.n) for p in range(1, d + 1) for v in range(g.n) if (u, v) not in used]
    return [(u, g.pr[u], v) for u in range(g.n) for v in range(g.n)]


def is_maximal(g: Graph, d: int, win: int) -> bool:
    assert is_parity_graph(g, win)
    for e in all_possible_edges(g, d):
        if e not in g.edges and is_parity_graph(Graph(g.n, g.edges | {e}, g.pr), win):
            return False
    return True


def canon(g: Graph) -> Graph:
    """Canonical form under vertex permutations (n <= 6)."""
    best = None
    for perm in itertools.permutations(range(g.n)):
        es = tuple(sorted((perm[u], p, perm[v]) for (u, p, v) in g.edges))
        pr = None if g.pr is None else tuple(g.pr[perm.index(i)] for i in range(g.n))
        key = (pr, es)
        if best is None or key < best:
            best = key
    pr, es = best
    return Graph(g.n, frozenset(es), pr, g.simple)


@lru_cache(maxsize=None)
def trees(n: int, h: int):
    """Ordered trees of height h with exactly n leaves, as tuples of leaf tuples (child indices from the root)."""
    if h == 0:
        return [((),)] if n == 1 else []
    out = []
    for k in range(1, n + 1):
        for comp in compositions(n, k):
            for subs in itertools.product(*[trees(c, h - 1) for c in comp]):
                leaves = tuple((i,) + leaf for i, sub in enumerate(subs) for leaf in sub)
                out.append(leaves)
    return out


@lru_cache(maxsize=None)
def compositions(n, k):
    if k == 1:
        return [(n,)]
    return [(a,) + rest for a in range(1, n - k + 2) for rest in compositions(n - a, k - 1)]


def trunc_len(h, p):
    return h - (p - 1) // 2 if p % 2 == 1 else h - p // 2


def graph_from_tree(leaves, d, pr=None):
    n, h = len(leaves), len(leaves[0])
    edges = set()
    for u in range(n):
        ps = [pr[u]] if pr is not None else range(1, d + 1)
        for p in ps:
            L = trunc_len(h, p)
            for v in range(n):
                a, b = leaves[u][:L], leaves[v][:L]
                if (p % 2 == 0 and a >= b) or (p % 2 == 1 and a > b):
                    edges.add((u, p, v))
    return Graph(n, frozenset(edges), pr)


def maximal_graphs(n: int, d: int, conv: str, win: int, verify: bool = True):
    """All maximal even (win=0) / odd (win=1) graphs on exactly n vertices over Sigma_d, up to isomorphism."""
    shift = win  # odd graphs over {1..d} = even graphs over {2..d+1} shifted back
    D = d + shift
    h = (D + 1) // 2
    fam = set()
    for leaves in trees(n, h):
        if conv == 'E':
            g = graph_from_tree(leaves, D)
            es = frozenset((u, p - shift, v) for (u, p, v) in g.edges if p - shift >= 1)
            fam.add(canon(Graph(n, es)))
        elif conv == 'S':
            g = graph_from_tree(leaves, D)
            allowed = {}
            for (u, p, v) in g.edges:
                if p - shift >= 1:
                    allowed.setdefault((u, v), []).append(p - shift)
            pairs = sorted(allowed)
            for choice in itertools.product(*[allowed[pv] for pv in pairs]):
                es = frozenset((u, p, v) for (u, v), p in zip(pairs, choice))
                fam.add(canon(Graph(n, es, None, True)))
        else:
            for pr in itertools.product(range(1 + shift, D + 1), repeat=n):
                g = graph_from_tree(leaves, D, pr)
                es = frozenset((u, p - shift, v) for (u, p, v) in g.edges)
                fam.add(canon(Graph(n, es, tuple(p - shift for p in pr))))
    fam = list(fam)
    # keep maximal members: g is dropped if some vertex permutation of it is a proper subgraph of another member
    by_pr = {}
    for g in fam:
        by_pr.setdefault(g.pr, []).append(g)
    keep = []
    for g in fam:
        dominated = False
        for perm in itertools.permutations(range(n)):
            es = frozenset((perm[u], p, perm[v]) for (u, p, v) in g.edges)
            pr = None if g.pr is None else tuple(g.pr[perm.index(i)] for i in range(n))
            if any(es < g2.edges for g2 in by_pr.get(pr, [])):  # for 'S' only same-shape containment is caught; harmless
                dominated = True; break
        if not dominated:
            keep.append(g)
    if verify:
        for g in keep:
            assert is_parity_graph(g, win), g
            assert is_maximal(g, d, win), g
    return sorted(keep, key=lambda g: (g.pr or (), sorted(g.edges)))


def all_graphs_bruteforce(n, d, conv):
    if conv == 'S':
        pairs = [(u, v) for u in range(n) for v in range(n)]
        for labels in itertools.product(range(0, d + 1), repeat=len(pairs)):
            yield Graph(n, frozenset((u, p, v) for (u, v), p in zip(pairs, labels) if p > 0), None, True)
    elif conv == 'E':
        cand = [(u, p, v) for u in range(n) for p in range(1, d + 1) for v in range(n)]
        for mask in range(1 << len(cand)):
            yield Graph(n, frozenset(e for i, e in enumerate(cand) if mask >> i & 1))
    else:
        pairs = [(u, v) for u in range(n) for v in range(n)]
        for pr in itertools.product(range(1, d + 1), repeat=n):
            for mask in range(1 << len(pairs)):
                yield Graph(n, frozenset((u, pr[u], v) for i, (u, v) in enumerate(pairs) if mask >> i & 1), pr)


def coverage_bruteforce(n, d, conv, win):
    """Check: every even/odd graph on n vertices is contained (up to isomorphism) in a member of maximal_graphs."""
    fam = maximal_graphs(n, d, conv, win)
    fam_by_pr = {}
    for g in fam:
        fam_by_pr.setdefault(g.pr, []).append(g)
    count = 0
    for g in all_graphs_bruteforce(n, d, conv):
        if not is_parity_graph(g, win):
            continue
        count += 1
        ok = False
        for perm in itertools.permutations(range(n)):
            es = frozenset((perm[u], p, perm[v]) for (u, p, v) in g.edges)
            pr = None if g.pr is None else tuple(g.pr[perm.index(i)] for i in range(n))
            if any(es <= g2.edges for g2 in fam_by_pr.get(pr, [])):
                ok = True; break
        if not ok:
            return False, g
    return True, count
