#!/usr/bin/env python3
"""Test of hypothesis UG (theory box 2026-10-22, docs/struct/S5-weak-strong.md §3), convention E, d even.

For a deterministic automaton W over Sigma_d let U_G(W) be the set of transitions (q, p, q') that W takes on some path
(starting anywhere) of some CDFJLP graph G_t (1807.10546v2 §5.2 "Construction of G_t"), t an ordered tree with exactly
n leaves, all at depth d/2.  G_t: vertices v_1..v_n = leaves in lexicographic order; for i < j whose leaves share a
prefix of length c, an edge v_i -> v_j with priority d - 2c and v_j -> v_i with priority d - 2c - 1; a self-loop with
every even priority at every vertex.  UG(W): the transitions U_G(W) form no cycle with odd maximum.
S5 Prop. W: UG(W) for a weak (n,d)-separator W implies |W| >= C(floor(lg n) + d/2 - 1, floor(lg n)) (CDFJLP Thm 5.1).
Inputs: every weak separator with exactly k states of the cell (enumerated, capped), or one automaton file.
Usage: ug_test.py n d k [--max M]   |   ug_test.py --file results/....json n"""
import sys, pathlib, argparse, json, itertools
from math import comb, floor, log2
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import Graph, trees, is_parity_graph, maximal_graphs
from wsep.encode import Encoder
from wsep.automata import language_in_limsup_even


def G_t(leaves, d):
    n = len(leaves); edges = set()
    for i, j in itertools.combinations(range(n), 2):
        c = next((x for x in range(len(leaves[i])) if leaves[i][x] != leaves[j][x]), len(leaves[i]))
        p = d - 2 * c
        edges.add((i, p, j)); edges.add((j, p - 1, i))
    for i in range(n):
        for p in range(2, d + 1, 2):
            edges.add((i, p, i))
    g = Graph(n, frozenset(edges))
    assert is_parity_graph(g, 0), "G_t must be even"
    return g


def used_transitions(W, graphs):
    used = set(); delta = W['delta']
    for g in graphs:
        start = [(v, 0) for v in range(g.n)]
        seen = set(start); st = list(start)
        while st:
            v, q = st.pop()
            for (p, v2) in g.out(v):
                q2 = delta[q][p - 1]
                assert q2 is not None, "W rejects a path of an even graph G_t: not a separator"
                used.add((q, p, q2))
                if (v2, q2) not in seen:
                    seen.add((v2, q2)); st.append((v2, q2))
    return used


def ug(W, graphs):
    U = used_transitions(W, graphs)
    return is_parity_graph(Graph(len(W['delta']), frozenset(U)), 0), len(U)


ap = argparse.ArgumentParser()
ap.add_argument('args', nargs='*'); ap.add_argument('--file'); ap.add_argument('--max', type=int, default=20000)
a = ap.parse_args()
if a.file:
    n = int(a.args[0]); W = json.load(open(a.file)); W = W.get('automaton', W)
    d = W['d']; assert d % 2 == 0
    graphs = [G_t(t, d) for t in trees(n, d // 2)]
    ok, size = ug(W, graphs)
    bound = comb(floor(log2(n)) + d // 2 - 1, floor(log2(n)))
    print(f"{a.file}: n={n} d={d} k={len(W['delta'])} strong={language_in_limsup_even(W)} |U_G|={size} UG={ok} "
          f"CDFJLP bound={bound}{'  (UG would force k >= bound: ' + ('consistent' if len(W['delta']) >= bound else 'VIOLATED -> Prop. W wrong') + ')' if ok else ''}")
    sys.exit(0)
n, d, k = map(int, a.args)
assert d % 2 == 0
graphs = [G_t(t, d) for t in trees(n, d // 2)]
evens = maximal_graphs(n, d, 'E', 0, verify=False); odds = maximal_graphs(n, d, 'E', 1, verify=False)
enc = Encoder(n, d, k, False)
for g in evens: enc.add_even(g)
for g in odds: enc.add_odd(g)
cnt = {'weak': 0, 'nonstrong': 0, 'UG_nonstrong': 0, 'UG_strong': 0}; fails = []
while cnt['weak'] < a.max:
    W = enc.solve()
    if W is None: break
    cnt['weak'] += 1
    s = language_in_limsup_even(W); ok, _ = ug(W, graphs)
    if s:
        cnt['UG_strong'] += ok
    else:
        cnt['nonstrong'] += 1; cnt['UG_nonstrong'] += ok
        if not ok: fails.append(W['delta'])
    enc.add([-enc.t[q][x][(W['delta'][q][x] if W['delta'][q][x] is not None else k)] for q in range(k) for x in range(d)])
print(f"E ({n},{d}) k={k}: {len(graphs)} trees; weak {cnt['weak']}, non-strong {cnt['nonstrong']}; "
      f"UG holds on {cnt['UG_nonstrong']}/{cnt['nonstrong']} non-strong and {cnt['UG_strong']}/{cnt['weak']-cnt['nonstrong']} strong (control: all)")
for f in fails[:3]: print("  UG fails:", f)
out = pathlib.Path(__file__).parent / 'results' / 'partition' / f"UG_E_n{n}_d{d}_k{k}.json"
out.write_text(json.dumps({'n': n, 'd': d, 'k': k, 'trees': len(graphs), **cnt, 'fail_examples': fails[:20]}, indent=1))
