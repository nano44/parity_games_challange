"""REFEREE throwaway: one pass over ALL edge-labelled multigraphs on 2 vertices with labels 1..6 (64^4 = 16,777,216;
one-vertex graphs are the ones whose second vertex is pruned), classifying each as even/odd/other by brute force and
checking (W1) on even graphs and (W2) on odd graphs for several automata at once. Independent of wsep/."""
import sys, json, itertools, time
sys.path.insert(0, '/home/user/parity_games_challange/docs/referee/scratch')
import wsepref as W
d = 6
auts = {'witness(3 states)': W.WITNESS}
for name in sys.argv[1:]:
    r = json.load(open(name)); auts[name.split('/')[-1]] = r['automaton']['delta']
subsets = [[p for p in range(1, d + 1) if m >> (p - 1) & 1] for m in range(1 << d)]
pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
cnt = {'even': 0, 'odd': 0, 'other': 0}; bad = {a: {} for a in auts}; t0 = time.time(); i = 0
# classification tables: self-loop subset class; cross pair class (all max even / all max odd / mixed / none)
loopcls = ['none' if not s else ('even' if all(p % 2 == 0 for p in s) else ('odd' if all(p % 2 for p in s) else 'mixed')) for s in subsets]
def crosscls(a, b):
    if not a or not b: return 'none'
    par = {max(p, q) % 2 for p in a for q in b}
    return 'mixed' if len(par) == 2 else ('even' if 0 in par else 'odd')
cross = [[crosscls(subsets[a], subsets[b]) for b in range(1 << d)] for a in range(1 << d)]
def combine(*cs):
    cs = [c for c in cs if c != 'none']
    if not cs: return 'none'
    if 'mixed' in cs or len(set(cs)) > 1: return 'mixed'
    return cs[0]
for ms in itertools.product(range(1 << d), repeat=4):
    i += 1
    c = combine(loopcls[ms[0]], loopcls[ms[3]], cross[ms[1]][ms[2]])
    if c == 'even' or c == 'odd':
        edges = [(u, p, w) for (u, w), m in zip(pairs, ms) for p in subsets[m]]
        assert W.cycle_class(2, edges) == c if i % 997 == 0 else True   # spot-check the table classification
        cnt[c] += 1
        for a, delta in auts.items():
            if c == 'even':
                if 'W1' not in bad[a] and not W.accepts_all(delta, 2, edges): bad[a]['W1'] = edges
            else:
                if 'W2' not in bad[a] and not W.rejects_all(delta, 2, edges): bad[a]['W2'] = edges
    else:
        cnt['other'] += 1
print(f"conv E, all {i} multigraphs on <=2 vertices, d=6: even={cnt['even']} odd={cnt['odd']} other={cnt['other']} ({time.time()-t0:.0f}s)")
for a in auts:
    strong = 'strong' in a
    s2 = W.strong_S2(auts[a], d)
    print(f"  {a}: W1 {'ok' if 'W1' not in bad[a] else 'VIOLATED ' + str(bad[a]['W1'])}; W2 {'ok' if 'W2' not in bad[a] else 'violated ' + str(bad[a]['W2'])}; S2 {'ok' if s2 else 'violated'}")
