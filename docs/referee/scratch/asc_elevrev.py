#!/usr/bin/env python3
"""REFEREE successor 27: second route for P-N5-ASC L-1's «[E-LEV] is NECESSARY» clause. Own Γ builder / VJ engine (xicyc_replay.build,
xicyc_vj.VJ); after building, the e-priorities are re-assigned among themselves in the order (−level, gate) (EORD rev; still R104's
shape: even, above every β, below c_W). IDEAL-CYC Howard run from the stored start (same loop as xicyc_replay.howard).
Prints U(G), max ascents of seq_t(v) over all (state, vertex), the number of (t, v) with that max, and with >= 1 ascent.
Usage: asc_elevrev.py [rev|lev] FILE.json..."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import build
from xicyc_vj import VJ

def run(G, mode):
    prio, own, succ, sig, movers, idx, _ = build(G)
    lev = G["lev"]; gate = G["gate"]
    es = [(q, v) for q, v in idx.items() if isinstance(q, tuple) and q[0] == "e"]
    vals = sorted(prio[v] for _, v in es)
    key = (lambda q: (-lev[q[1][0]], gate[q[1][0]][q[1][1]])) if mode == "rev" else (lambda q: (lev[q[1][0]], gate[q[1][0]][q[1][1]]))
    for (q, v), p in zip(sorted(es, key=lambda e: key(e[0])), vals): prio[v] = p
    E = VJ(prio, own, succ); evs = {v for _, v in es}
    s = [sig.get(v) for v in range(E.n)]; st, val = E.best_reply(s); states = [(st, val)]; ties = 0
    while True:
        ns = list(s)
        for x in movers:
            b = s[x]
            for w in E.succ[x]:
                if E.cmp(val[w], val[b]) > 0: b = w
            tops = [w for w in E.succ[x] if E.cmp(val[w], val[b]) == 0]
            if s[x] not in tops: ties += len(tops) > 1; ns[x] = max(tops)
        if ns == s: break
        st, val = E.best_reply(ns, st); s = ns; states.append((st, val))
    U = sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    mx = 0; cnt = {}; pos = 0; wit = None
    for t, (st, val) in enumerate(states):
        for v in range(E.n):
            P = val[v][1]; seen = set(); u = v; seq = []
            while u not in seen:
                seen.add(u)
                if u in evs and u in P: seq.append(u)
                u = st[u]
            a = sum(1 for p, q in zip(seq, seq[1:]) if E.rk[q] > E.rk[p])
            if a > mx: mx = a; wit = (t, v)
            cnt[a] = cnt.get(a, 0) + 1; pos += a >= 1
    return U, mx, cnt.get(mx, 0), pos, len(states) - 1, ties, wit

if __name__ == "__main__":
    mode = sys.argv[1]
    for f in sys.argv[2:]:
        U, mx, nmx, pos, T, ties, wit = run(json.load(open(f)), mode)
        print(os.path.basename(f), "EORD", mode, "T", T, "U(G)", U, "max ascents", mx, "(t, v) pairs at max", nmx, "with >= 1 ascent", pos,
              "first witness (t, v)", wit, "Howard ties", ties)
