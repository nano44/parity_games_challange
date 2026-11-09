#!/usr/bin/env python3
"""L-RED 63 R229 item 8: L-NEW 68 BOX 203 §5 (claude/l-new 0f026a64) on R221 own.py (IDEAL-CYC; cap 3000). Own code.
  k      = min FVS of the Xi-graph (seg228.fvs)
  maxL   = max over states of #distinct Λ_t(v) over all v except c_W, c_X and the e-vertices whose successor is c_W   [Lemma (k+1)-Λ: <= k + 1]
  lfail  = #states with more than k + 1 values (must be 0)
  asc    = max over states and vertices of the ascents of seq_t(v) (the e-vertices of v's play in play order; an ascent = a position where
           the next e-vertex is more relevant than the current one)  [DEAD «asc <= k + 1» by ST(m)]
Usage: lam229.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r228"), os.path.join(H, "..", "r221")]
import own, seg228
print("instance N+M T k maxL lfail asc", flush=True)
for f in sys.argv[1:]:
    G = json.load(open(f)); G = G.get("genome", G); k = seg228.fvs(G)
    out, V, O, _ = own.run(G, 3000); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]; rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}; exc = {V["cW"], V["cX"]} | {e for e in evs if succ[e][0] == V["cW"]}
    kk = int(k) if k.isdigit() else 10 ** 9; maxL = lfail = asc = 0
    for (s, vals, tau) in out:
        L = {vals[v][0] for v in range(n) if v not in exc}; maxL = max(maxL, len(L)); lfail += len(L) > kk + 1
        nxt = [s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)]
        for v in range(n):
            seen = set(); u = v; seq = []
            while u not in seen:
                seen.add(u)
                if u in evs: seq.append(u)
                u = nxt[u]
            asc = max(asc, sum(rk[b] > rk[a] for a, b in zip(seq, seq[1:])))
    print(os.path.basename(f), N + sum(len(o) for o in G["opts"]), len(out) - 1, k, maxL, lfail, asc, flush=True)
