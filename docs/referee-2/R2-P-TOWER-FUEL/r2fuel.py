#!/usr/bin/env python3
"""REFEREE-2 succ. 31: probe of P-TOWER-FUEL §4's reading «Lemma 4 (b) is violated in exactly those windows by a parked β of the capped
pair 4» on I-FUEL (SL41_d28), with my r2tower.py loader / simulator. For every 6-window: which members of pair 6 do not move, and for each
non-mover x whether dec(x) = option 19 at every pre-state s_(a-1)..s_(e-1); and for each member, consecutive moves t < t' with dec(x)
constant on s_(t-1)..s_(t'-1) (the conclusion of Lemma 4 (b) failing; level 6 is not doubling, so (b) does not apply).
Usage: r2fuel.py ROOT"""
import sys, os
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); ROOT = sys.argv[1]
src = open(os.path.join(H, 'r2tower.py')).read().split("# ---- §4 instances")[0]
ns = {'__name__': 'lib', '__file__': os.path.join(H, 'r2tower.py')}; sys.argv = ['x', ROOT]; exec(src, ns)
RS = ns['RS']; W, _ = RS.windows(6); C = Counter()
for a, e, mv in W:
    movers = sorted(x for _, x in mv); fail = movers != [12, 13]
    for x in (12, 13):
        if x in movers: continue
        d19 = all(RS.dec(RS.S[t], x)[0] == 19 for t in range(a - 1, e)); pref = {RS.pi(RS.S[t], x) == RS.S[t][x] for t in range(a - 1, e)}
        C[('fail' if fail else 'good', 'non-mover', x, 'dec=19 at every pre-state', d19, 'already on preferred option at every pre-state', pref == {True})] += 1
for x in (12, 13):
    ts = [t for t in range(1, RS.T + 1) if x in RS.mv[t]]
    for t, t2 in zip(ts, ts[1:]):
        decs = {RS.dec(RS.S[v], x) for v in range(t - 1, t2)}
        C[('member', x, 'consecutive-move pairs')] += 1; C[('member', x, 'dec constant between them')] += len(decs) == 1
        C[('member', x, 'dec constant and = option 19')] += decs == {(19, 0)} or decs == {(19, 1)}
for k in sorted(C, key=str): print(k, C[k])
