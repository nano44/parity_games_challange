#!/usr/bin/env python3
"""Lead's (a), 21:53Z: compute CDFJLP's resistance quasi-orders on A - R (R = the single even-letter deletion that kills
all odd cycles, Lemma B) and locate every working single rewire (q, e, old -> new) relative to q and old in those orders.
rank(s) = tuple over odd letters p (top first) of the resistance of s in its <=_{p+2} class; lexicographic comparison =
the D-tree order (smaller = deeper = closer to the leaves reached after reading the odd letters)."""
import sys, json, glob, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lasso_analysis import odd_cycles
from wsep.automata import aut_reachable

def resistance_orders(delta, d, R):
    k = len(delta); Rch = aut_reachable({'k': k, 'd': d, 'delta': delta})
    trans = [(q, p, delta[q][p-1]) for q in Rch for p in range(1, d+1) if delta[q][p-1] is not None and (q, p) not in R]
    odd_letters = [p for p in range(d if d % 2 == 1 else d - 1, 0, -2)]
    cls = {q: () for q in Rch}  # class key so far (tuple of resistances, top first)
    for p in odd_letters:
        new_cls = {}
        for q in Rch:
            # states in the same class with letters <= p
            same = [s for s in Rch if cls[s] == cls[q]]
            sub = [(a, l, b) for (a, l, b) in trans if a in same and b in same and l <= p]
            # resistance: max number of p-edges on paths from q in sub; infinite iff a cycle through a p-edge.
            # SCCs of sub (Tarjan); a p-edge inside an SCC -> infinite; else DP on the SCC DAG.
            nodes = same; adj = {}
            for (a, l, b) in sub: adj.setdefault(a, []).append((l, b))
            index = {}; low = {}; onst = set(); st = []; comp = {}; counter = [0]; ncomp = [0]
            def strong(v):
                index[v] = low[v] = counter[0]; counter[0] += 1; st.append(v); onst.add(v)
                for (l, w) in adj.get(v, []):
                    if w not in index: strong(w); low[v] = min(low[v], low[w])
                    elif w in onst: low[v] = min(low[v], index[w])
                if low[v] == index[v]:
                    while True:
                        w = st.pop(); onst.discard(w); comp[w] = ncomp[0]
                        if w == v: break
                    ncomp[0] += 1
            for v in nodes:
                if v not in index: strong(v)
            inf_states = set()
            for (a, l, b) in sub:
                if l == p and comp[a] == comp[b]: inf_states.add(a)
            memo = {}
            def res(s, stack=None):
                if s in memo: return memo[s]
                best = 0
                for (l, b) in adj.get(s, []):
                    if comp[b] == comp[s]:
                        continue  # same SCC: no p-edge inside (else inf), and res is constant on the SCC (handled below)
                    best = max(best, res(b) + (1 if l == p else 0))
                memo[s] = best; return best
            # res must be the max over the whole SCC's outgoing edges: compute per SCC
            scc_members = {}
            for v in nodes: scc_members.setdefault(comp[v], []).append(v)
            memo_scc = {}
            def res_scc(c):
                if c in memo_scc: return memo_scc[c]
                best = 0
                for v in scc_members[c]:
                    for (l, b) in adj.get(v, []):
                        if comp[b] != c: best = max(best, res_scc(comp[b]) + (1 if l == p else 0))
                memo_scc[c] = best; return best
            def res(s, stack=None):
                if s in inf_states or any(comp[s] == comp[a] for a in inf_states): return float('inf')
                return res_scc(comp[s])
            new_cls[q] = cls[q] + (res(q, frozenset()),)
        cls = new_cls
    return cls

def cmp(a, b):
    return 'equal' if a == b else ('deeper' if a < b else 'shallower')

rows = []; summary = {}
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
        if Rset is None: continue  # all-odd case
        rank = resistance_orders(delta, d, Rset)
        if any(float('inf') in v for v in rank.values()): rows.append((conv, n, d, delta, 'INFINITE resistance after deleting', sorted(Rset))); continue
        for rw in inst['rewires']:
            q, e, old, new = rw['q'], rw['letter'], rw['old'], rw['new']
            in_R = (q, e) in Rset
            if new is None:
                rel_old, rel_q = 'bottom', 'bottom'
            else:
                rel_old, rel_q = cmp(rank[new], rank[old]) if old is not None else 'old-bottom', cmp(rank[new], rank[q])
            key = (in_R, e % 2 == 0, rel_old, rel_q)
            summary[key] = summary.get(key, 0) + 1
            rows.append((conv, n, d, delta, (q, e, old, new), 'R' if in_R else 'notR', 'new vs old: ' + rel_old, 'new vs q: ' + rel_q, {s: rank[s] for s in sorted(rank)}))
print("summary over working single rewires: key = (rewired transition is the Lemma-B deletion, even letter, rank(new) vs rank(old), rank(new) vs rank(q)) -> count")
for kk, v in sorted(summary.items(), key=lambda x: -x[1]): print("  ", kk, v)
print("\nexamples where new is SHALLOWER than old or than q, or the rewired transition is not the deletion:")
shown = 0
for r in rows:
    if len(r) > 6 and ('shallower' in r[6] or 'shallower' in r[7] or r[5] == 'notR') and shown < 8:
        print("  ", r); shown += 1
inf = [r for r in rows if len(r) == 6]
print(f"\ninstances with infinite resistance after deleting R: {len(inf)}")
for r in inf[:3]: print("  ", r)
json.dump([list(map(str, r)) for r in rows], open('results/sl8/target_rule_rows.json', 'w'), indent=1)
