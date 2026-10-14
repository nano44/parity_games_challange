#!/usr/bin/env python3
"""Candidate target rules, tested against ALL working single rewires per (q, e) (rules_min data) using the A - R orders:
  interval I(q,e) = { x : rank(old) > rank(x) >= rank(q) }  (strictly deeper than old, not deeper than q)
  R-int:  working targets == I            R-sup: working targets ⊇ I          R-sub: working targets ⊆ I ∪ {q}
  R-top:  the shallowest state of I works   R-bot: the deepest state of I works   R-self: q works"""
import sys, json, glob, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lasso_analysis import odd_cycles
from target_rule import resistance_orders
stats = {k: [0, 0] for k in ['R-int', 'R-sup', 'R-sub', 'R-top', 'R-bot', 'R-self', 'I-empty']}
fails = {k: [] for k in stats}
for f in sorted(glob.glob('results/sl8/rules_min_*.json')):
    conv, n, d = f.split('_')[2], int(f.split('_')[3][1:]), int(f.split('_')[4][1:])
    for inst in json.load(open(f)):
        delta = inst['delta']; k = len(delta)
        cyc, _ = odd_cycles({'k': k, 'd': d, 'delta': delta})
        cand = sorted({(s[i], l[i]) for s, l in cyc for i in range(len(s)) if l[i] % 2 == 0})
        Rset = None
        for r in range(1, len(cand) + 1):
            for R in itertools.combinations(cand, r):
                d2 = [row[:] for row in delta]
                for (q, p) in R: d2[q][p-1] = None
                if not odd_cycles({'k': k, 'd': d, 'delta': d2})[0]: Rset = set(R); break
            if Rset is not None: break
        if Rset is None: continue
        rank = resistance_orders(delta, d, Rset)
        if any(float('inf') in v for v in rank.values()): continue
        # group working rewires by (q, e), even letters only, old not bottom
        groups = {}
        for rw in inst['rewires']:
            if rw['letter'] % 2 == 0 and rw['old'] is not None and rw['new'] is not None:
                groups.setdefault((rw['q'], rw['letter']), set()).add(rw['new'])
        for (q, e), W in groups.items():
            old = delta[q][e-1]
            I = {x for x in rank if rank[old] > rank[x] >= rank[q]}
            tests = {'R-int': W == I, 'R-sup': W >= I, 'R-sub': W <= I | {q}, 'I-empty': len(I) == 0,
                     'R-top': (max(I, key=lambda x: rank[x]) in W) if I else None, 'R-bot': (min(I, key=lambda x: rank[x]) in W) if I else None, 'R-self': q in W}
            for name, ok in tests.items():
                if ok is None: continue
                stats[name][0 if ok else 1] += 1
                if not ok and len(fails[name]) < 3: fails[name].append((conv, n, d, delta, (q, e, old), 'working', sorted(W), 'interval', sorted(I), {s: rank[s] for s in sorted(rank)}))
print("rule -> (holds, fails) over (q,e) groups of working even-letter rewires:")
for name, (a, b) in stats.items(): print(f"   {name}: {a} / {b}")
for name in ['R-sup', 'R-sub', 'R-top', 'R-bot']:
    for x in fails[name][:2]: print(f"  {name} FAIL:", x)
