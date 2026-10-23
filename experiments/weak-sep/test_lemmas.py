#!/usr/bin/env python3
"""Data tests for the T3 proof attempt (Lead 21:50Z requirement 2), on every non-strong minimal weak separator stored in
results/sl8/rules_min_*.json and on the far instances of results/sl8/enum_*.json.
Lemma A (return edges): for every reachable odd simple cycle C with maximum p there is a transition tau on C with an EVEN
  letter e < p such that in A minus tau, restricted to letters <= p, no cycle passes through a p-labelled transition of C.
Lemma B (tree-likeness after deletion): there is a set R of even-letter transitions, one hitting each odd simple cycle,
  such that A minus R has no reachable odd simple cycle at all (so CDFJLP's resistance is finite in every class).  We
  report the least |R| (brute force over even-letter transitions lying on odd cycles) against the number of odd cycles.
Lemma C (rewire target): for every working single rewire (q,e,old)->new: is new == q (self-loop) or new == the successor
  of old on the cycle, or some other state; and is e the smallest even letter on that cycle."""
import sys, json, glob, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import Graph, is_parity_graph
from wsep.automata import aut_reachable
from lasso_analysis import odd_cycles

def trans_graph(delta, d, drop=frozenset(), maxletter=None):
    R = aut_reachable({'k': len(delta), 'd': d, 'delta': delta})
    return [(q, p, delta[q][p-1]) for q in R for p in range(1, d+1) if delta[q][p-1] is not None and (q, p) not in drop and (maxletter is None or p <= maxletter)]

def has_cycle_through(edges, k, special):
    """is there a cycle in the graph 'edges' through one of the transitions in 'special' (set of (q,p))?"""
    adj = {}
    for (q, p, q2) in edges: adj.setdefault(q, []).append(q2)
    def reach(s, t):
        seen = {s}; st = [s]
        while st:
            x = st.pop()
            if x == t: return True
            for y in adj.get(x, []):
                if y not in seen: seen.add(y); st.append(y)
        return False
    for (q, p, q2) in edges:
        if (q, p) in special and reach(q2, q): return True
    return False

def lemmaA(delta, d):
    cyc, _ = odd_cycles({'k': len(delta), 'd': d, 'delta': delta}); results = []
    for states, labels in cyc:
        p = max(labels); pedges = {(states[i], labels[i]) for i in range(len(states)) if labels[i] == p}
        found = []
        for i in range(len(states)):
            e = labels[i]
            if e % 2 == 0 and e < p:
                tau = (states[i], e)
                edges = trans_graph(delta, d, drop=frozenset([tau]), maxletter=p)
                if not has_cycle_through(edges, len(delta), pedges): found.append(tau)
        results.append((tuple(states), tuple(labels), found))
    return results

def lemmaB(delta, d):
    cyc, _ = odd_cycles({'k': len(delta), 'd': d, 'delta': delta})
    cand = sorted({(states[i], labels[i]) for states, labels in cyc for i in range(len(states)) if labels[i] % 2 == 0})
    for r in range(0, len(cand) + 1):
        for R in itertools.combinations(cand, r):
            d2 = [row[:] for row in delta]
            for (q, p) in R: d2[q][p-1] = None
            if not odd_cycles({'k': len(delta), 'd': d, 'delta': d2})[0]: return len(cyc), r, R
    return len(cyc), None, None

stats = {'A_total': 0, 'A_ok': 0, 'A_fail': [], 'B': {}, 'C': {'selfloop': 0, 'succ': 0, 'other': 0, 'smallest_even': 0, 'total': 0, 'other_examples': []}}
for f in sorted(glob.glob('results/sl8/rules_min_*.json')):
    conv, n, d = f.split('_')[2], int(f.split('_')[3][1:]), int(f.split('_')[4][1:])
    for inst in json.load(open(f)):
        delta = inst['delta']
        for states, labels, found in lemmaA(delta, d):
            stats['A_total'] += 1
            if found: stats['A_ok'] += 1
            else: stats['A_fail'].append((conv, n, d, delta, states, labels))
        ncyc, r, R = lemmaB(delta, d)
        stats['B'].setdefault((ncyc, r), 0); stats['B'][(ncyc, r)] += 1
        cycs, _ = odd_cycles({'k': len(delta), 'd': d, 'delta': delta})
        for rw in inst['rewires']:
            q, e, old, new = rw['q'], rw['letter'], rw['old'], rw['new']
            stats['C']['total'] += 1
            oncyc = [(s, l) for s, l in cycs if any(s[i] == q and l[i] == e for i in range(len(s)))]
            succ_targets = set(); smallest = False
            for s, l in oncyc:
                i = [j for j in range(len(s)) if s[j] == q and l[j] == e][0]
                succ_targets.add(s[(i + 2) % len(s)] if len(s) > 1 else s[0])
                ev = [x for x in l if x % 2 == 0]
                if ev and e == min(ev): smallest = True
            if new == q: stats['C']['selfloop'] += 1
            elif new in succ_targets: stats['C']['succ'] += 1
            else:
                stats['C']['other'] += 1
                if len(stats['C']['other_examples']) < 6: stats['C']['other_examples'].append((conv, n, d, delta, (q, e, old, new), oncyc))
            if smallest: stats['C']['smallest_even'] += 1
print("Lemma A: odd simple cycles tested", stats['A_total'], "with a return edge as defined:", stats['A_ok'], "FAILURES:", len(stats['A_fail']))
for x in stats['A_fail'][:5]: print("   A-fail:", x)
print("Lemma B: (number of odd simple cycles, least |R| of even-letter deletions killing all odd cycles) -> count:", dict(sorted(stats['B'].items(), key=lambda kv: (kv[0][0], -1 if kv[0][1] is None else kv[0][1]))))
print("Lemma C over working single rewires:", {k: v for k, v in stats['C'].items() if k != 'other_examples'})
for x in stats['C']['other_examples']: print("   C-other:", x)
json.dump({'A': {'total': stats['A_total'], 'ok': stats['A_ok'], 'fail': stats['A_fail']}, 'B': {str(k): v for k, v in stats['B'].items()}, 'C': {k: v for k, v in stats['C'].items()}}, open('results/sl8/lemma_tests.json', 'w'), indent=1, default=str)
