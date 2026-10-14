#!/usr/bin/env python3
"""Test the rewiring RULE: while the automaton has a reachable odd simple cycle, pick a transition on it with the
smallest even letter e and redirect it to a self-loop (q, e, q); report whether the result is still a weak separator
and whether it became strong.  Also tries 'redirect to the cycle's entry state'."""
import sys, json, pathlib, subprocess, copy
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.automata import check_separator, language_in_limsup_even
from lasso_analysis import odd_cycles

def apply_rule(delta, d, rule):
    delta = copy.deepcopy(delta); steps = []
    for _ in range(20):
        cyc, _ = odd_cycles({'k': len(delta), 'd': d, 'delta': delta})
        if not cyc: return delta, steps
        states, labels = min(cyc, key=lambda c: (len(c[0]), c))
        evens = [(i, p) for i, p in enumerate(labels) if p % 2 == 0]
        if not evens: return None, steps + ['odd cycle with no even letter']
        i, p = min(evens, key=lambda x: x[1])
        q = states[i]
        new = q if rule == 'selfloop' else states[0]
        steps.append((q, p, delta[q][p - 1], new)); delta[q][p - 1] = new
    return None, steps

instances = [(2,3,'E',[[1,0,1],[None,2,None],[1,0,None]]), (3,3,'V',json.load(open('results/automata/weak_V_n3_d3.json'))['automaton']['delta']),
             (3,4,'V',[[1,1,1,0],[2,1,3,0],[3,1,None,0],[None,4,None,0],[2,4,None,0]]), (2,2,'V',[[1,0],[None,2],[2,0]])]
for args,n,d,conv in [("3 3 E 6 3",3,3,'E'),("3 4 E 6 3",3,4,'E'),("4 4 V 8 3",4,4,'V'),("3 4 V 6 3",3,4,'V'),("2 3 V 4 3",2,3,'V')]:
    out = subprocess.run(['python3','probe_oddcycles.py']+args.split(), capture_output=True, text=True).stdout
    instances.append((n,d,conv,eval(out[out.index('['):])))
for n,d,conv,delta in instances:
    ev = maximal_graphs(n,d,conv,0,verify=False); od = maximal_graphs(n,d,conv,1,verify=False)
    for rule in ['selfloop','entry']:
        res, steps = apply_rule(delta, d, rule)
        if res is None: print(f"({n},{d}) {conv} k={len(delta)} rule={rule}: FAILED {steps}"); continue
        aut = {'k':len(delta),'d':d,'delta':res}
        w1 = not any(k=='W1' for k,_ in check_separator(aut, ev, od, False)); w2 = not any(k=='W2' for k,_ in check_separator(aut, ev, od, False))
        print(f"({n},{d}) {conv} k={len(delta)} rule={rule}: steps={steps} -> W1 {'ok' if w1 else 'BROKEN'}, W2 {'ok' if w2 else 'BROKEN'}, strong {language_in_limsup_even(aut)}")
