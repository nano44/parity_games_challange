"""Even / odd labelled graphs (convention E: edge-labelled multigraphs over letters 1..d, max-parity) for separator
bounds. Independent of experiments/weak-sep (L-STRUCT): own generator and own brute-force parity check.

Generator (progress measures; CDFJLP 1807.10546 Thm 2.1 as summarised by L-STRUCT, used only to PRODUCE candidate
graphs: every produced graph is re-checked by brute force, so lower bounds below rely only on that check):
  vertices = leaves of an ordered tree of height h; leaf = tuple of child indices, most significant level first;
  level i (0-based from the top) belongs to the odd letter 2(h-i)-1. For letter p keep the levels of odd letters >= p;
  edge (u,p,v) is present iff trunc(u) >= trunc(v) (p even) or trunc(u) > trunc(v) (p odd), lexicographically.
Odd graphs: even graphs over letters 2..d+1 (height ceil((d+1)/2)) shifted down by one."""
from __future__ import annotations
import itertools
from functools import lru_cache


def is_parity(n, edges, win):
    """win 0: every cycle has even max letter; win 1: odd. Brute force: for each letter p of the wrong parity,
    a cycle with max p exists iff some edge (u,p,v) has v ->* u using letters <= p."""
    for p in {e[1] for e in edges if e[1] % 2 != win}:
        adj = [[] for _ in range(n)]
        for (u, q, v) in edges:
            if q <= p:
                adj[u].append(v)
        for (u, q, v) in edges:
            if q == p:
                seen, st = {v}, [v]
                while st:
                    x = st.pop()
                    for y in adj[x]:
                        if y not in seen:
                            seen.add(y); st.append(y)
                if u in seen:
                    return False
    return True


@lru_cache(maxsize=None)
def trees(nleaves, h):
    if h == 0:
        return [((),)] if nleaves == 1 else []
    out = []
    for parts in range(1, nleaves + 1):
        for comp in _comps(nleaves, parts):
            for subs in itertools.product(*[trees(c, h - 1) for c in comp]):
                out.append(tuple((i,) + leaf for i, sub in enumerate(subs) for leaf in sub))
    return out


@lru_cache(maxsize=None)
def _comps(n, k):
    if k == 1:
        return [(n,)]
    return [(a,) + r for a in range(1, n - k + 2) for r in _comps(n - a, k - 1)]


def _graph(leaves, letters, h):
    n = len(leaves)
    E = set()
    for p in letters:
        keep = sum(1 for i in range(h) if 2 * (h - i) - 1 >= p)  # levels 0..keep-1
        for u in range(n):
            for v in range(n):
                a, b = leaves[u][:keep], leaves[v][:keep]
                if (p % 2 == 0 and a >= b) or (p % 2 == 1 and a > b):
                    E.add((u, p, v))
    return E


def family(n, d, win):
    """Distinct (as labelled edge sets) parity graphs with exactly n vertices from trees with n leaves; each checked."""
    out = set()
    if win == 0:
        h = (d + 1) // 2
        for t in trees(n, h):
            E = _graph(t, range(1, d + 1), h)
            out.add(frozenset(E))
    else:
        h = (d + 2) // 2
        for t in trees(n, h):
            E = _graph(t, range(2, d + 2), h)
            out.add(frozenset((u, p - 1, v) for (u, p, v) in E))
    res = sorted(out, key=lambda e: sorted(e))
    for E in res:
        assert is_parity(n, E, win), "generator produced a graph of the wrong parity"
    return [(n, E) for E in res]
