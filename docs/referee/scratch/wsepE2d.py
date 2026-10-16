"""REFEREE throwaway: convention E on <= 2 vertices for any d, exhaustive over the cross-edge label sets A (0->1) and
B (1->0) (all 2^d x 2^d pairs). Self-loops: an even graph's loops are even labels and adding every even loop keeps it
even (a loop is its own cycle), so for (W1) it suffices to check each (A,B) with ALL even loops at both vertices
(every even graph is a subgraph of that one with the same A,B; W1 is monotone). Symmetrically for odd graphs and (W2).
One-vertex graphs are the (A,B) = (empty, empty) cases restricted to one vertex, covered by pruning.
A 2-vertex graph is even iff all loops are even and max(a,b) is even for all a in A, b in B (its simple cycles are the
loops and the 2-cycles). Usage: wsepE2d.py automaton.json"""
import sys, json, itertools, time
sys.path.insert(0, '/home/user/parity_games_challange/docs/referee/scratch')
import wsepref as W
r = json.load(open(sys.argv[1])); delta = r['automaton']['delta']; d = r['automaton']['d']
letters = list(range(1, d + 1)); subsets = [[p for p in letters if m >> (p - 1) & 1] for m in range(1 << d)]
t0 = time.time(); cnt = {0: 0, 1: 0}; bad = {}
for win in (0, 1):
    loops = [p for p in letters if p % 2 == win]
    for ma in range(1 << d):
        A = subsets[ma]
        for mb in range(1 << d):
            B = subsets[mb]
            if any(max(a, b) % 2 != win for a in A for b in B): continue
            cnt[win] += 1
            edges = [(0, p, 0) for p in loops] + [(1, p, 1) for p in loops] + [(0, a, 1) for a in A] + [(1, b, 0) for b in B]
            if (cnt[win] % 50000 == 0): assert W.cycle_class(2, edges) == ('even' if win == 0 else 'odd')
            if win == 0:
                if 'W1' not in bad and not W.accepts_all(delta, 2, edges): bad['W1'] = (A, B)
            else:
                if 'W2' not in bad and not W.rejects_all(delta, 2, edges): bad['W2'] = (A, B)
print(f"conv E, d={d}, all (A,B) pairs: even configurations={cnt[0]} odd={cnt[1]} ({time.time()-t0:.0f}s); violations: {bad if bad else 'none'}; S2 {'holds' if W.strong_S2(delta, d) else 'fails'}")
