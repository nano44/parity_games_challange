#!/usr/bin/env python3
"""L-LOWER 9: for sched(h, alpha) (core movers only, no helpers): for each core mover x, the free pre-states and required preference,
as a function of the OTHER core movers' states (pref_x cannot depend on s_x: acyclic wiring). Reports conflicts (same other-state,
different required pref): each one forces a helper (or a lower/higher mover outside the core) whose state differs between the two
pre-states. Usage: selfconf.py h alpha(comma list)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l7'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sched import schedule
from sim6 import okeys
h = int(sys.argv[1]); al = list(map(int, sys.argv[2].split(',')))
D, S = schedule(h, alpha=al); g = D['gate']; N = 2 * h; tot = 0
for x in range(N):
    req = {}
    for t in range(1, len(S)):
        s, ns = S[t - 1][:N], S[t][:N]; o = okeys(D, S[t]); l = x // 2
        free = (g[2 * x + 1 - s[x]] < g[2 * x + s[x]]) if l == 0 else s[x] != o[l - 1]
        if free: req.setdefault(s[:x] + s[x + 1:], set()).add((ns[x], t))
    conf = [(''.join(map(str, k)), sorted(v)) for k, v in req.items() if len({p for p, _ in v}) > 1]
    tot += len(conf); print('mover', x, 'free pre-states', sum(len(v) for v in req.values()), 'conflicts', len(conf), conf[:4])
print('total conflicts', tot)
