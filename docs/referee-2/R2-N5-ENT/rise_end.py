#!/usr/bin/env python3
"""Record (DATA): for every rise after a fallback k0 of a scope run S (COARSE_L(theta) changes at an S4a step with r > L, L = M_k0 >= 0,
no fallback in between), how S ends: N5 stops, the phase ends, (h) fails, H2 fails at the next state, w changes, or r drops <= L first.
Own code (ent_check / out_check traces). Usage: rise_end.py MODE file.pg ..."""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
mode = sys.argv[1]; cnt = Counter()
for p in sys.argv[2:]:
    g = RC.parse(open(p).read()); o = FC.odd_vertex(g); rng = random.Random(7)
    for r in range(3):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
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
            u = j + 1
            while u < T and insc[u] and not fbs[u] and A[u].r > L: u += 1
            if u == T: why = "N5 stopped (no improving edge)"
            elif fbs[u] and insc[u]: why = "next fallback of S" + (" with r > L" if A[u].r > L else "")
            elif insc[u] and A[u].r <= L: why = "r <= L before a fallback"
            elif not inph[u]: why = "phase ends (" + ("tau" if A[u].tu[o] != A[u + 1].tu[o] else "lambda") + " changes" + (", fallback" if fbs[u] else ", S4a/S4b") + ")"
            elif not A[u].hh: why = "(h) fails at the state"
            elif not A[u + 1].H2: why = "H2 fails at the next state"
            else: why = "w changes"
            cnt[why] += 1; cnt["rises"] += 1
            cnt["steps_from_rise_to_end_total"] += u - j
for k, v in sorted(cnt.items()): print(f"{k}: {v}")
