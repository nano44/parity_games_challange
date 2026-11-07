#!/usr/bin/env python3
"""L-RED 55 R220: P-N5-ASC §6 check with own.py (independent of L-NEW): U(G) = #options whose Xi-target is a mover of higher level;
max over all states t and ALL vertices v of #ascents of seq_t(v) (e-vertices of Pi_t(v) in play order; ascent = next one more relevant).
Env EORD=lev (default, [E-LEV]) or rev (e-priorities ordered by (-level, gate): violates [E-LEV]). Prints U, max ascents, violations of
«ascents <= U» (count of (t, v)), and one witness. Usage: [EORD=rev] asc220.py G.json ..."""
import sys, json, os
import own
for f in sys.argv[1:]:
    G = json.load(open(f))
    if not (isinstance(G, dict) and "opts" in G): continue
    N, lev = G["N"], G["lev"]
    U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}; mx = 0; viol = 0; wit = None
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0]))
        for v in range(n):
            Pi = vals[v][1]; seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            a = sum(1 for p, q in zip(seq, seq[1:]) if rk[q] > rk[p])
            if a > mx: mx = a
            if a > U:
                viol += 1
                if wit is None: wit = (t, v, a)
    print(f"{f.split('/')[-1]} EORD {os.environ.get('EORD', 'lev')} N {N} U(G) {U} max ascents {mx} | (t, v) with ascents > U: {viol} | witness (t, v, asc) {wit}", flush=True)
