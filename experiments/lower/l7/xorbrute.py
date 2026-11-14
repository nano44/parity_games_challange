#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §5 (ONE-READ XOR, DATA). Usage: xorbrute.py xor | ctx"""
"""exhaustive: reader x, inputs (2 options each) and fixed nodes (state 0: one live option); every acyclic wiring under every
topological order; is there a rank/sign assignment with pref_x = TABLE over the given input combos? (greedy decision-list, exact)"""
import sys, itertools
def solve(cons):
    openc = list(range(len(cons))); used = set()
    while openc:
        pick = None
        for m in {m for i in openc for m in cons[i]}:
            sg = {cons[i][m] for i in openc if m in cons[i]}
            if len(sg) == 1: pick = m; break
        if pick is None: return False
        openc = [i for i in openc if pick not in cons[i]]
    return True
def run(inputs, fixed, combos):
    nodes = inputs + fixed; cnt = 0; feas = 0; ex = None
    for order in itertools.permutations(nodes):
        pos = {n: i for i, n in enumerate(order)}
        opts = [('x', 0), ('x', 1)] + [(n, k) for n in order for k in ((0, 1) if n in inputs else (0,))]
        choices = []
        for (n, k) in opts:
            later = [None] + (list(order) if n == 'x' else list(order[pos[n] + 1:]))
            choices.append(later)
        for tg in itertools.product(*choices):
            T = dict(zip(opts, tg)); cnt += 1
            cons = []
            for st, p in combos:
                def chain(n, k):
                    out = [(n, k)]; y = T[(n, k)]
                    while y is not None:
                        kk = st[y] if y in inputs else 0; out.append((y, kk)); y = T[(y, kk)]
                    return set(out)
                A, B = chain('x', 0), chain('x', 1)
                cons.append({m: (1 if ((m in B) == (p == 1)) else 0) for m in A ^ B})
            if solve(cons): feas += 1; ex = ex or (order, T)
    return cnt, feas, ex
mode = sys.argv[1]
if mode == 'xor':
    combos = [({'a': i, 'b': j}, i ^ j) for i in (0, 1) for j in (0, 1)]
    print('pure XOR of a, b; fixed nodes m1, m2:', run(['a', 'b'], ['m1', 'm2'], combos)[:2])
if mode == 'ctx':
    # f6's table in the alpha = 1 sequential schedule: w = context (pair-4 derived), split = f5 != q5; pref = split (g = 0)
    T6 = [((1, 0, 0), 0), ((1, 1, 0), 1), ((1, 1, 1), 0), ((0, 1, 1), 0), ((0, 0, 1), 1), ((0, 0, 0), 0)]
    combos = [({'w': w, 'a': a, 'b': b}, p) for (w, a, b), p in T6]
    r = run(['w', 'a', 'b'], ['m1'], combos); print('context table (w, f5, q5) -> split, fixed node m1:', r[:2]); print('example:', r[2])
