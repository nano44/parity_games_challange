#!/usr/bin/env python3
"""T1/T4 (Lead 21:57Z): H-B(2) = the D-tree of A - tau0 (CDFJLP tree decomposition by resistance; tau0 = the single
even-letter deletion killing all odd cycles) is (n, ceil(d/2))-universal.  T1: every stored minimal non-strong weak
separator at d <= n+1 (results/sl8/rules_min_*.json).  T4: the minimal weak witnesses at the gap cells (must FAIL)."""
import sys, json, glob, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lasso_analysis import odd_cycles
from target_rule import resistance_orders
from wsep.utrees import embeds, trees
from wsep.automata import language_in_limsup_even

def dtree_universal(delta, d, n):
    k = len(delta); cyc, _ = odd_cycles({'k': k, 'd': d, 'delta': delta})
    if cyc:
        cand = sorted({(s[i], l[i]) for s, l in cyc for i in range(len(s)) if l[i] % 2 == 0})
        Rset = None
        for r in range(1, len(cand) + 1):
            for R in itertools.combinations(cand, r):
                d2 = [row[:] for row in delta]
                for (q, p) in R: d2[q][p-1] = None
                if not odd_cycles({'k': k, 'd': d, 'delta': d2})[0]: Rset = set(R); break
            if Rset is not None: break
        if Rset is None: return 'no-even-deletion', None, None
    else:
        Rset = set()
    rank = resistance_orders(delta, d, Rset)
    if any(float('inf') in v for v in rank.values()): return 'infinite-resistance', None, None
    T = tuple(sorted(set(rank.values())))  # the D-tree: leaves = classes of <=_1, coordinates = resistances per level
    h = len(T[0])
    assert h == (d + 1) // 2
    ok = all(embeds(S, T) for m in range(1, n + 1) for S in trees(m, h))
    return 'universal' if ok else 'NOT-universal', T, sorted(Rset)

print("T1: minimal non-strong weak separators at d <= n+1")
t1 = {}
for f in sorted(glob.glob('results/sl8/rules_min_*.json')):
    conv, n, d = f.split('_')[2], int(f.split('_')[3][1:]), int(f.split('_')[4][1:])
    for inst in json.load(open(f)):
        verdict, T, R = dtree_universal(inst['delta'], d, n)
        t1.setdefault((conv, n, d), {}).setdefault(verdict, []).append((inst['delta'], T, R))
for cell, vs in t1.items():
    print(f"  {cell}: " + ", ".join(f"{v}: {len(l)}" for v, l in vs.items()))
    for v, l in vs.items():
        if v != 'universal':
            for x in l[:3]: print("     ", v, x)
print("T4: minimal weak witnesses at gap cells (must fail)")
for f in ['results/automata/weak_E_n2_d5.json', 'results/automata/weak_E_n2_d6.json', 'results/automata/weak_V_n2_d5.json', 'results/automata/weak_V_n2_d6.json', 'results/automata/weak_V_n3_d5.json', 'results/automata/weak_V_n3_d6.json', 'results/automata/weak_E_n2_d8.json', 'results/automata/weak_V_n3_d8.json']:
    r = json.load(open(f)); a = r['automaton']
    verdict, T, R = dtree_universal(a['delta'], r['d'], r['n'])
    print(f"  {r['conv']} ({r['n']},{r['d']}) w={r['value']} strong={language_in_limsup_even(a)}: {verdict}; D-tree leaves {len(T) if T else None}; deletion {R}")
# control: strong minimal separators at d <= n+1 and above must be universal (CDFJLP Lemma 5.3) in E
print("control (strong witnesses, E): must be universal")
for f in ['results/automata/strong_E_n2_d4.json', 'results/automata/strong_E_n3_d4.json', 'results/automata/strong_E_n3_d6.json', 'results/automata/strong_E_n4_d4.json']:
    r = json.load(open(f)); a = r['automaton']
    verdict, T, R = dtree_universal(a['delta'], r['d'], r['n'])
    print(f"  E ({r['n']},{r['d']}) s={r['value']}: {verdict}; leaves {len(T)}")
