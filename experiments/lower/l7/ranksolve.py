#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7): exact rank/sign feasibility for a fixed wiring and a fixed target trajectory.
Model = l6/sim6.py (R104 rules). For a wiring xt, gates, start and a target state sequence S[0..T], the run reproduces S iff at
every step t and every mover x whose move is not blocked (level >= 1: s_(t-1)[x] != c_x(t); level 0: the gate allows the switch),
pref_x(s_(t-1)) = s_t[x]. pref_x(s) is the sign of the top-rank option in chain_s(x,0) △ chain_s(x,1) (ENC; distinct ranks).
So each constraint says «the top element of the set Δ has a prescribed sign». Greedy (decision-list learning, complete for this
form): repeatedly take an option e on which every open constraint containing e agrees, give it the next highest rank and that
sign, close those constraints. Stuck = infeasible; the open constraints are an obstruction core (every option in them is pulled
both ways). Importable: constraints(D, S), solve(cons, nopt) -> (br, bp) or (None, core)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, wr, run, Fprof, caps, okeys
def chainset(D, s, x, k):
    out = []
    while True:
        m = 2 * x + k; out.append(m); y = D['xt'][m]
        if y < 0: return out
        x, k = y, s[y]
def constraints(D, S):
    """list of (t, x, p, A, B): at pre-state S[t-1] mover x must prefer p; A = chain options of x:0, B = of x:1"""
    d = D['d']; N = 2 * d; g = D['gate']; cons = []
    for t in range(1, len(S)):
        s, ns = S[t - 1], S[t]; o = okeys(D, ns)
        for x in range(N):
            l = x // 2
            if l == 0: free = g[2 * x + 1 - s[x]] < g[2 * x + s[x]]
            else: free = s[x] != o[l - 1]
            if not free: continue
            A = set(chainset(D, s, x, 0)); B = set(chainset(D, s, x, 1)); cons.append((t, x, ns[x], A, B))
    return cons
def solve(cons, nopt):
    # each constraint: dict option -> required sign (1 = positive)
    C = []
    for t, x, p, A, B in cons:
        req = {}
        for m in A ^ B: req[m] = 1 if ((m in B) == (p == 1)) else 0
        C.append(req)
    openc = set(range(len(C))); by = {m: set() for m in range(nopt)}
    for i, r in enumerate(C):
        for m in r: by[m].add(i)
    rank = nopt - 1; br = [None] * nopt; bp = [0] * nopt; left = set(range(nopt))
    while openc:
        pick = None
        for m in sorted(left):
            sg = {C[i][m] for i in by[m] if i in openc}
            if len(sg) == 1: pick = (m, sg.pop()); break
        if pick is None: return None, [cons[i][:3] for i in sorted(openc)]
        m, sgn = pick; br[m] = rank; bp[m] = 0 if sgn == 1 else 1; rank -= 1; left.discard(m)
        openc -= by[m]
    for m in sorted(left): br[m] = rank; rank -= 1
    return (br, bp), None
if __name__ == '__main__':
    D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1; cons = constraints(D, S)
    res, core = solve(cons, 4 * D['d'])
    if res is None: print('INFEASIBLE, core', len(core)); sys.exit(1)
    E = dict(D); E['br'], E['bp'] = res; S2, O2 = run(E)
    same = S2[:T + 1] == S
    print(sys.argv[1].split('/')[-1], 'T', T, 'constraints', len(cons), 'solved; rebuilt run reproduces trajectory:', same,
          'F old', Fprof(D, O)[:8], 'F new', Fprof(E, O2)[:8])
    if len(sys.argv) > 2: wr(E, sys.argv[2])
