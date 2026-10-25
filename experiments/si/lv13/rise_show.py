#!/usr/bin/env python3
"""L-SI succ. 8, box 13 item (3): print the scope run around every rise (REFEREE-2 rise_end.py's definition: k0 an in-scope fallback,
L = M_k0 >= 0, first S4a step j > k0 with r > L that changes COARSE_L(theta), no fallback in between), from k0 to the end of S.
Per state: r, M, fallback flag, Is (gates with levels), sigma changes, theta. Traces: REFEREE-2's (read only). Usage: rise_show.py mode file.pg"""
import sys, os, random
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ", "R2-N5-ENT", "R2-N5-RE"): sys.path.insert(0, os.path.join(R2, d))
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
mode, p = sys.argv[1], sys.argv[2]; lim = int(sys.argv[3]) if len(sys.argv) > 3 else 3
g = RC.parse(open(p).read()); o = FC.odd_vertex(g); rng = random.Random(7); shown = 0
print("n", g.n, "o", o, "rank o", g.rank[o], "succ o", g.succ[o])
for rr in range(3):
    s, t = FC.s3_start(g) if rr == 0 else RC.rand_start(rng, g)
    A, fbs = OC.run_trace(g, o, s, t, rng, mode); T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    for k0 in range(T):
        if not (insc[k0] and fbs[k0]): continue
        L = EC.M(A[k0])
        if L < 0: continue
        j = None
        for s_ in range(k0 + 1, T):
            if not insc[s_] or fbs[s_] or A[s_].r <= L: break
            if FC.coarse(g, A[s_ + 1].theta, L) != FC.coarse(g, A[s_].theta, L): j = s_; break
        if j is None: continue
        shown += 1
        if shown > lim: continue
        print(f"=== start {rr} k0={k0} L={L} rise at j={j}  w={A[k0].w}")
        u = k0
        while u <= T:
            S = A[u]
            gl = [(y, z, FC.lev(g, S.Xi[S.sg[y]], S.Xi[z])) for (y, z) in S.Is] if hasattr(S, "Is") else []
            ch = [(v, A[u - 1].sg[v], S.sg[v]) for v in range(g.n) if u > k0 and A[u - 1].sg[v] != S.sg[v]]
            print(f" s={u} insc={insc[u] if u < T else '-'} fb={fbs[u] if u < T else '-'} hh={S.hh} r={S.r} M={EC.M(S)} "
                  f"theta={S.theta} cL={FC.coarse(g, S.theta, L)} tu_o={S.tu[o]} chg={ch} gates={gl[:8]}")
            if u >= T or not insc[u]: break
            u += 1
print("rises", shown)
