#!/usr/bin/env python3
"""L-RED 70 R244: the kill candidate G_k on L-RED's own engines. For each k: class244 clauses for G_k as generated and for its
order-preserving gate renumbering; T_key and the largest per-mover switch count on sim244 (own, Python) and on r187 ideal.traj (the lane's
older engine, other code), for both gate numberings; T against 2^k - 2; per-level best switch counts; the kill ratio T / (N + M).
Usage: gkrun244.py KMIN KMAX DIR   (files DIR/G_k.json, DIR/G_k_renum.json from gk244.py)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r187")]
import sim244, class244, ideal
bad = 0
for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    row = []
    for suf in ("", "_renum"):
        G = sim244.load(os.path.join(sys.argv[3], f"G_{k}{suf}.json")); r, M, deg, per = class244.check(G)
        T, sw, S = sim244.run(G, trace=True); S2, why = ideal.traj(G, cap=10 ** 7)
        same = [tuple(s) for s in S2] == S
        row.append((r, T, max(sw), len(S2) - 1, why, same, deg, per, G["N"], M, sw, G))
    (r, T, mx, T2, why, same, deg, per, N, M, sw, G), (rr, Tr, mxr, T2r, whyr, samer, _, _, _, _, swr, _) = row
    L = max(G["lev"]) + 1; best = [max(sw[x] for x in range(N) if G["lev"][x] == l) for l in range(L)]
    ok = T == 2 ** k - 2 and T2 == T and same and Tr == T and T2r == T and samer and sw == swr and all(rr.values())
    bad += not ok
    print(f"GKRUN244 k {k}: N {N} M {M} levels {L} degrees {sorted(deg.items())} movers/level {per} | class as generated: " + " ".join(f"{c} {'PASS' if v else 'FAIL'}" for c, v in r.items())
          + " | renumbered gates: " + " ".join(f"{c} {'PASS' if v else 'FAIL'}" for c, v in rr.items())
          + f" | T sim244 {T} ideal.traj {T2} ({why}) states equal {same}; renumbered T {Tr} / {T2r} states equal {samer} switch counts equal {sw == swr} | 2^k - 2 = {2 ** k - 2} | max sw {mx} (2^(k-2) = {2 ** (k - 2)}) | best per level {best} | T / (N + M) = {T / (N + M):.3f} | {'OK' if ok else 'MISMATCH'}", flush=True)
sys.exit(1 if bad else 0)
