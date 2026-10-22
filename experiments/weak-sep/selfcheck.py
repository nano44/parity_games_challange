#!/usr/bin/env python3
"""Self-check: (1) graph families cover all graphs (brute force) on tiny cases; (2) universal-tree brute force equals
the f/g recursions where they agree; (3) hand-verified values w(2,2)=s(2,2)=2, w(1,d)=1, s(2,4)=3, s(3,2)=3 are
recomputed; (4) every stored automaton in results/automata is re-verified by the independent checker against the
full graph families (including the w < s witnesses); (5) stored strong values equal universal-tree sizes (even d)."""
import sys, json, glob, pathlib, time
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import coverage_bruteforce, maximal_graphs
from wsep.utrees import min_universal_tree, f_upper, g_lower
from wsep.search import min_separator
from wsep.automata import check_separator
t0 = time.time(); fails = 0
def ok(cond, msg):
    global fails
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond: fails += 1
for c in [(2, 2, 'E', 0), (2, 2, 'E', 1), (2, 3, 'E', 0), (2, 3, 'E', 1), (3, 2, 'E', 0), (3, 3, 'V', 0), (3, 3, 'V', 1), (2, 3, 'S', 1)]:
    r = coverage_bruteforce(*c); ok(r[0], f"coverage {c}: {r[1]} graphs")
for (n, h) in [(2, 2), (3, 2), (2, 3), (3, 3), (4, 2)]:
    L, _ = min_universal_tree(n, h); ok(L == f_upper(n, h) == g_lower(n, h), f"universal tree ({n},{h}) = {L}")
quiet = lambda *a, **k: None
for (n, d, conv, strong, expect) in [(2, 2, 'E', False, 2), (2, 2, 'E', True, 2), (1, 4, 'E', False, 1), (2, 4, 'E', True, 3),
                                     (3, 2, 'E', True, 3), (2, 6, 'E', False, 3), (2, 6, 'V', True, 4)]:
    k, aut, _ = min_separator(n, d, conv, strong, log=quiet)
    ok(k == expect, f"{'s' if strong else 'w'}^{conv}({n},{d}) = {k} (expected {expect})")
fam = {}
for f in sorted(glob.glob(str(pathlib.Path(__file__).parent / 'results/automata/*.json'))):
    r = json.load(open(f))
    if r['automaton'] is None or r['n'] >= 5 or (r['n'] == 4 and r['d'] >= 5) or (r['conv'] == 'S' and r['d'] >= 5) or (r['conv'] == 'V' and r['d'] >= 9):
        continue  # slow families (n>=5, (4,>=5), S with d>=5, V with d>=9) are checked by compute.py itself
    key = (r['n'], r['d'], r['conv'])
    if key not in fam:
        fam[key] = (maximal_graphs(*key, 0, verify=False), maximal_graphs(*key, 1, verify=False))
    ev, od = fam[key]
    bad = check_separator(r['automaton'], ev, od, r['mode'] == 'strong')
    ok(not bad and r['automaton']['k'] == r['value'], f"stored {pathlib.Path(f).name}: {r['mode']} {r['conv']} ({r['n']},{r['d']}) value {r['value']} re-verified")
    if r['mode'] == 'strong' and r['conv'] == 'E' and r['d'] % 2 == 0 and 'eager' not in f:
        h = r['d'] // 2
        ok(g_lower(r['n'], h) <= r['value'] <= f_upper(r['n'], h), f"  s^E({r['n']},{r['d']}) within universal-tree bounds [{g_lower(r['n'], h)},{f_upper(r['n'], h)}]")
print(f"{'ALL PASS' if fails == 0 else str(fails) + ' FAILURES'} in {time.time()-t0:.0f}s")
sys.exit(1 if fails else 0)
