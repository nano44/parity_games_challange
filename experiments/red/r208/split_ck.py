#!/usr/bin/env python3
"""L-RED R208 SPLIT_CK: random check of Lemma TOP-SPLIT. For random coupled top extensions (coupext.rand, C couplings) of a base:
cut the run at the steps that move a top mover; for a segment starting at state s (start, or the state after a top-moving step),
build L_q: the lower genome where every coupled option's Xi-target (a top mover u) is replaced by a fresh level-0 one-option PROXY
mover with option (W none, Xi-target xt(u, s(u)), beta(u, s(u))) (one proxy per top mover), started at s's lower part; check that
G's lower states through the segment's closing top-moving step (inclusive) are L_q's run states, and that the number of steps of
the segment that move a lower mover is <= T(L_q from s). Usage: split_ck.py base.json C n seed"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import coupext, ideal
G0 = json.load(open(sys.argv[1])); C, n, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
N0 = G0["N"]; viol = 0; segs = 0; mx = 0
for it in range(n):
    G = None
    while G is None: P = coupext.rand(G0, C, rng); G = coupext.build(G0, P)
    for _ in range(rng.randrange(0, 50)):
        Q = coupext.mutate(G0, P, rng); G2 = coupext.build(G0, Q)
        if G2 is not None: P, G = Q, G2
    S, _ = ideal.traj(G); top = [v for v in range(G["N"]) if v >= N0]
    cuts = [t for t in range(1, len(S)) if any(S[t][u] != S[t - 1][u] for u in top)]
    starts = [0] + cuts
    for i, a in enumerate(starts):
        b = cuts[i] if i < len(cuts) else len(S) - 1   # segment covers steps a+1 .. b
        s = S[a]; pmap = {}; opts = [[list(o) for o in oo] for oo in G["opts"][:N0]]; lev = list(G["lev"][:N0]); gate = [list(g) for g in G["gate"][:N0]]
        br = list(G["br"]); bp = list(G["bp"]); st = list(s[:N0]); gmax = max(max(g) for g in G["gate"]) + 1
        for v in range(N0):
            for o in opts[v]:
                if o[1] >= N0:
                    u = o[1]
                    if u not in pmap:
                        pmap[u] = len(opts); uo = G["opts"][u][s[u]]
                        opts.append([[-1, uo[1], uo[2]]]); lev.append(0); gate.append([gmax + len(pmap)]); st.append(0)
                    o[1] = pmap[u]
        L = dict(N=len(opts), lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=st)
        SL, _ = ideal.traj(L); segs += 1
        for t in range(a, b + 1):
            j = t - a
            low = tuple(S[t][:N0]); ref = tuple(SL[min(j, len(SL) - 1)][:N0])
            if low != ref: viol += 1; break
        lowsteps = sum(1 for t in range(a + 1, b + 1) if S[t][:N0] != S[t - 1][:N0])
        if lowsteps > len(SL) - 1: viol += 1
        mx = max(mx, lowsteps)
print(f"SPLIT_CK base {os.path.basename(sys.argv[1])} C {C} genomes {n} segments {segs} violations {viol} max lower steps per segment {mx}")
