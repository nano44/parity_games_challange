#!/usr/bin/env python3
"""L-RED R187: write a PER-STATE variant of L-NEW's box 136 dmerge2.py (read-only source, patched copy written next to it in a scratch
copy of claude/l-new's experiments/new). The patched copy builds D'' from the edges of ONE state at a time (segment edges of that state
+ W-key edges) and reports, per run/stretch, the number of states whose own D'' is cyclic (PSCYC) and the first such cycle.
Usage: mkdm2state.py <path to box136/dmerge2.py>  -> writes box136/dm2state.py"""
import sys, os
p = sys.argv[1]; s = open(p).read()
s = s.replace("    adj = {x: set() for x in range(n) if own[x] == 0}\n    for s in range(a, b + 1):\n",
              "    adj = {x: set() for x in range(n) if own[x] == 0}; PS = []; U = {x: set() for x in range(n) if own[x] == 0}\n    for s in range(a, b + 1):\n        adj = {x: set() for x in range(n) if own[x] == 0}\n")
s = s.replace("                    v = sW[v]\n", "                    v = sW[v]\n        PS.append((s, cyclic(adj)))\n    pscyc = [q for q in PS if q[1]]\n    print('PERSTATE run', a, b, 'states', len(PS), 'PSCYC', len(pscyc), 'first', pscyc[:1])\n")
s = s.replace("def stretches(a, b):", '''def cyclic(adj):
    state = {}
    for v0 in adj:
        if v0 in state: continue
        st = [(v0, iter(adj[v0]))]; state[v0] = 1
        while st:
            v, it = st[-1]; nx = next(it, None)
            if nx is None: state[v] = 2; st.pop()
            elif state.get(nx) == 1:
                path = [u for u, _ in st]; return path[path.index(nx):] + [nx]
            elif nx not in state: state[nx] = 1; st.append((nx, iter(adj[nx])))
    return None
def stretches(a, b):''')
# PRUNE=1: keep only vertices with |T_x| >= 2 (a vertex with one tight option is constant on an FL run by FL-TIGHT, so edges into it
# are not dependencies; dmerge2 already adds x -> every Even vertex on a segment / W-play, so no path is lost)
s = s.replace("    R[\"fl\"] += b - a;", "    adj = U\n    if os.environ.get('PRUNE') == '1':\n        keep = {x for x in Tx if len(Tx[x]) >= 2}; adj = {x: {v for v in adj[x] if v in keep} for x in keep}\n    R[\"fl\"] += b - a;")
s = s.replace("        PS.append((s, cyclic(adj)))", "        if os.environ.get('PRUNE') == '1':\n            keep = {x for x in Tx if len(Tx[x]) >= 2}; adj = {x: {v for v in adj[x] if v in keep} for x in keep}\n        PS.append((s, cyclic(adj)))\n        for x in adj: U.setdefault(x, set()).update(adj[x])")
open(os.path.join(os.path.dirname(p), "dm2state.py"), "w").write(s)
