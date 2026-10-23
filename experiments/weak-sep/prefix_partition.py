#!/usr/bin/env python3
"""Notebook queue 2 (theory box 2026-10-22): do a minimal weak separator W and some minimal strong separator S of the
same cell split the even prefixes the same way?

Even prefixes: finite words read along paths (from any vertex) of even X-graphs with <= n vertices (= of the maximal
even graphs, by the coverage of wsep.graphs). For automata A, B let
    R(A,B) = { (delta_A(u), delta_B(u)) : u an even prefix }   (computed by product reachability over the even graphs).
R(W,S) is a BIJECTION of the state sets  <=>  W and S induce the same partition of the even prefixes (up to renaming).
CDFJLP's Lemma 5.3 (1807.10546v2 §5.2, Claim 5.1) reads only runs on even words (alpha_t); strongness enters only in
Lemma 5.2. So "R(W,S) is a bijection for some strong S" says that W's states carry exactly a strong separator's
even behaviour.
Enumeration: all automata with exactly k reachable states (BFS-canonical numbering, encoder symmetry breaking),
blocking clauses on the transition variables, capped at --max. Prints per cell: #weak, #non-strong weak, #strong,
and for each non-strong W whether some S gives a bijection (and the least |R| otherwise).
Usage: prefix_partition.py n d conv k [--max M]"""
import sys, pathlib, argparse, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import language_in_limsup_even

ap = argparse.ArgumentParser()
ap.add_argument('n', type=int); ap.add_argument('d', type=int); ap.add_argument('conv'); ap.add_argument('k', type=int)
ap.add_argument('--max', type=int, default=20000)
a = ap.parse_args()
evens = maximal_graphs(a.n, a.d, a.conv, 0, verify=False)
odds = maximal_graphs(a.n, a.d, a.conv, 1, verify=False)


def enumerate_all(strong):
    enc = Encoder(a.n, a.d, a.k, strong)
    for g in evens:
        enc.add_even(g)
    if not strong:
        for g in odds:
            enc.add_odd(g)
    out = []
    while len(out) < a.max:
        aut = enc.solve()
        if aut is None:
            return out, True
        out.append(aut)
        block = [-enc.t[q][x][(aut['delta'][q][x] if aut['delta'][q][x] is not None else a.k)]
                 for q in range(a.k) for x in range(a.d)]
        enc.add(block)
    return out, False


def relation(A, B):
    """R(A,B) over all paths of all even graphs, starting anywhere in state (0,0)."""
    R = set()
    for g in evens:
        start = [(v, 0, 0) for v in range(g.n)]
        seen = set(start); st = list(start)
        while st:
            v, p, q = st.pop()
            R.add((p, q))
            for (x, v2) in g.out(v):
                p2, q2 = A['delta'][p][x - 1], B['delta'][q][x - 1]
                assert p2 is not None and q2 is not None, "a separator rejected an even path"
                if (v2, p2, q2) not in seen:
                    seen.add((v2, p2, q2)); st.append((v2, p2, q2))
    return R


def is_bijection(R, k):
    f, g = {}, {}
    for p, q in R:
        if f.setdefault(p, q) != q or g.setdefault(q, p) != p:
            return False
    return len(f) == k and len(g) == k


W, wc = enumerate_all(False)
S, sc = enumerate_all(True)
nonstrong = [x for x in W if not language_in_limsup_even(x)]
print(f"cell ({a.n},{a.d}) {a.conv} k={a.k}: weak {len(W)}{'' if wc else '+ (capped)'}, non-strong {len(nonstrong)}, "
      f"strong {len(S)}{'' if sc else '+ (capped)'}")
# control: every strong S is itself weak, so R(S,S) is the identity bijection; and R(W,S) for strong W is checked too
res = {'n': a.n, 'd': a.d, 'conv': a.conv, 'k': a.k, 'weak': len(W), 'weak_complete': wc, 'strong': len(S),
       'strong_complete': sc, 'nonstrong': len(nonstrong), 'nonstrong_with_bijection': 0, 'strong_weak_with_bijection': 0,
       'failures': []}
for x in W:
    best = None
    for s in S:
        R = relation(x, s)
        if is_bijection(R, a.k):
            best = 'bij'; break
        best = len(R) if best is None else min(best, len(R))
    if x in nonstrong:
        if best == 'bij':
            res['nonstrong_with_bijection'] += 1
        else:
            res['failures'].append({'delta': x['delta'], 'least_R': best})
    elif best == 'bij':
        res['strong_weak_with_bijection'] += 1
print(f"  non-strong W with a bijective R to some minimal strong S: {res['nonstrong_with_bijection']} / {len(nonstrong)}")
print(f"  (control) strong W with a bijection: {res['strong_weak_with_bijection']} / {len(W) - len(nonstrong)}")
for f in res['failures'][:5]:
    print("  FAIL:", f)
out = pathlib.Path(__file__).parent / 'results' / 'partition' / f"{a.conv}_n{a.n}_d{a.d}_k{a.k}.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(res, indent=1))
