#!/usr/bin/env python3
"""R2 data step (S3 §4b): for each committed minimal weak V-witness, list the reachable odd simple cycles C, and for
every simple path P from q0 into C the lasso word pi(P)·pi(C)^w; compute the least number m of vertices of an odd
V-graph realising that word (brute force over the maximal odd V-graphs with m vertices; monotone, so maximal suffices),
and the cheap filter |P|+|C|.  Writes results/lasso_analysis.md."""
import sys, json, glob, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.automata import aut_reachable

def odd_cycles(aut):
    d, delta, R = aut['d'], aut['delta'], aut_reachable(aut); out = []
    adj = {q: [(p, delta[q][p-1]) for p in range(1, d+1) if delta[q][p-1] is not None] for q in R}
    def dfs(s, q, path, labels, seen):
        for p, q2 in adj[q]:
            if q2 == s:
                if max(labels + [p]) % 2 == 1: out.append((tuple(path), tuple(labels + [p])))
            elif q2 > s and q2 not in seen:
                dfs(s, q2, path + [q2], labels + [p], seen | {q2})
    for s in sorted(R): dfs(s, s, [s], [], {s})
    return out, adj

def simple_paths_to(adj, target, maxlen):
    """all simple paths from state 0 to target (as label sequences), including the empty one if target == 0."""
    res = []
    def dfs(q, labels, seen):
        if q == target: res.append(tuple(labels))
        if len(labels) >= maxlen: return
        for p, q2 in adj[q]:
            if q2 not in seen: dfs(q2, labels + [p], seen | {q2})
    dfs(0, [], {0}); return res

def realisable(word_u, word_c, H):
    """does the odd V-graph H have an infinite path labelled u·c^w?"""
    L = len(word_u) + len(word_c); letters = list(word_u) + list(word_c)
    def nxt(t): return t + 1 if t + 1 < L else len(word_u)
    start = [(0, v) for v in range(H.n) if H.pr[v] == letters[0]]
    seen = set(start); st = list(start); edges = []
    out = {}
    for (u, p, v) in H.edges: out.setdefault(u, []).append(v)
    while st:
        t, v = st.pop()
        for v2 in out.get(v, []):
            t2 = nxt(t)
            if H.pr[v2] == letters[t2]:
                edges.append(((t, v), (t2, v2)))
                if (t2, v2) not in seen: seen.add((t2, v2)); st.append((t2, v2))
    # reachable product has a cycle?
    adj = {}
    for a, b in edges: adj.setdefault(a, []).append(b)
    col = {x: 0 for x in seen}
    for s in seen:
        if col[s]: continue
        stack = [(s, iter(adj.get(s, [])))]; col[s] = 1
        while stack:
            x, it = stack[-1]
            for y in it:
                if col[y] == 1: return True
                if col[y] == 0: col[y] = 1; stack.append((y, iter(adj.get(y, [])))); break
            else: col[x] = 2; stack.pop()
    return False

from wsep.graphs import Graph, is_parity_graph

def realisable_m(u, c, m):
    """is u·c^w the word of an infinite path in some odd V-graph with <= m vertices?  DFS over vertex sequences:
    vertices are numbered by first use (symmetry), labels fixed by the word, every added edge must keep all cycles odd;
    success when a (phase, vertex) pair repeats inside the periodic part (then the path can loop for ever)."""
    letters = list(u) + list(c); lu = len(u)
    def phase(t): return t if t < lu else lu + (t - lu) % len(c)
    best = [False]
    def dfs(t, seq, labels, edges, seen_pairs):
        if best[0]: return
        ph = phase(t); letter = letters[ph]
        cands = [v for v in range(len(labels)) if labels[v] == letter]
        if len(labels) < m: cands.append(len(labels))
        for v in cands:
            new_labels = labels if v < len(labels) else labels + [letter]
            new_edges = edges
            if seq:
                e = (seq[-1], new_labels[seq[-1]], v)
                if e not in edges:
                    new_edges = edges | {e}
                    if not is_parity_graph(Graph(len(new_labels), frozenset(new_edges), tuple(new_labels)), 1): continue
            if ph >= lu and (ph, v) in seen_pairs:
                best[0] = True; return
            dfs(t + 1, seq + [v], new_labels, new_edges, seen_pairs | ({(ph, v)} if ph >= lu else set()))
            if best[0]: return
    dfs(0, [], [], frozenset(), frozenset())
    return best[0]

def least_odd_graph(u, c, d, mmax=5):
    for m in range(1, mmax + 1):
        if realisable_m(u, c, m): return m
    return None

assert least_odd_graph((), (9,4,8), 10) == 3 and least_odd_graph((), (5,4,4), 6) == 3 and least_odd_graph((), (1,), 2) == 1
assert least_odd_graph((2,), (3,2), 4) == 2 and least_odd_graph((), (3,2), 4) == 2

if __name__ == '__main__':
    rows = ["# Lasso words of minimal weak V-witnesses: least odd V-graph realising them (R2 data step)", "",
            "m* = least number of vertices of an odd V-graph realising pi(P)·pi(C)^w (None = more than n+2). W2 forces m* > n.",
            "P ranges over ALL simple paths from q0 into C (entry point varies); one line per (C, entry, P) up to 6 per cycle.", ""]
    rows += ["| cell | w / s | cycle C (states; letters) | lasso P letters | |P|+|C| | m* |", "| --- | --- | --- | --- | --- | --- |"]
    cells = [(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4),(2,4),(2,5),(2,6),(3,5),(3,6)]
    S = {}
    for f in glob.glob('results/automata/strong_V_*.json'):
        r = json.load(open(f))
        if '_k' not in f and 'eager' not in f: S[(r['n'], r['d'])] = r['value']
    summary = []
    for (n, d) in cells:
        f = f'results/automata/weak_V_n{n}_d{d}.json'
        if not pathlib.Path(f).exists(): continue
        r = json.load(open(f)); aut = r['automaton']
        cyc, adj = odd_cycles(aut)
        mins = []
        for states, labels in cyc:
            L = len(states)
            for e in range(L):  # entry point
                entry = states[e]; cl = labels[e:] + labels[:e]
                paths = simple_paths_to(adj, entry, aut['k'])
                for P in sorted(paths, key=len)[:6]:
                    m = least_odd_graph(P, cl, d, mmax=n + 2)
                    mins.append(m if m else 99)
                    rows.append(f"| V ({n},{d}) | {r['value']} / {S.get((n,d),'-')} | {states}; {labels} entry {entry} | {P} | {len(P)+L} | {m} |")
        summary.append((n, d, r['value'], S.get((n,d),'-'), len(cyc), min(mins) if mins else None, 'gap' if S.get((n,d)) and r['value'] < S[(n,d)] else 'w=s'))
    rows += ["", "## Summary", "", "| cell | w / s | odd simple cycles | min over lassos of m* | gap? |", "| --- | --- | --- | --- | --- |"]
    for n, d, w, s, k, mn, g in summary:
        rows.append(f"| V ({n},{d}) | {w} / {s} | {k} | {mn} | {g} |")
    pathlib.Path('results/lasso_analysis.md').write_text("\n".join(rows) + "\n")
    print("\n".join(rows[-len(summary)-3:]))
