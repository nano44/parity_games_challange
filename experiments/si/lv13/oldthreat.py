#!/usr/bin/env python3
"""L-SI succ. 8, box 13 item (3): DATA for Lemma OLD-THREAT (docs/si/N5-RISE-box13.md). k0 an in-scope fallback with L = M_k0 >= 0,
j the first S4a step after k0 (no fallback in between, every transition in scope, r > L) that changes COARSE_L(theta) (a RISE, as in
REFEREE-2 rise_end.py). For every state t > j such that every transition s -> s+1, k0 < s < t, is an in-scope S4a step with r_s > L:
(OLD-THREAT) every exit x of o with x in F_k0 and COARSE_L(Xi_k0 x) = COARSE_L(Xi_k0 x_k0) (x_k0 := sigma-bar_k0(o)) lies in Rbar_t. (GATE-ABOVE, CONJECTURE) if moreover r_t > L, then M_t > L (FALSE: library). (FEED, CONJECTURE) if r_t > L, some gate at t runs from F_t into Rbar_t (FALSE: library). (INTO, CONJECTURE) if r_t > L, some gate at t has its target in Rbar_t.
Traces and state analysis: REFEREE-2's (read only). Usage: oldthreat.py R seed game.pg ..."""
import sys, os, random
from collections import Counter
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ", "R2-N5-ENT", "R2-N5-RE"): sys.path.insert(0, os.path.join(R2, d))
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC

def scan(g, o, A, fbs, C, bad, tag):
    T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    for k0 in range(T):
        if not (insc[k0] and fbs[k0]): continue
        L = EC.M(A[k0])
        if L < 0: continue
        j = None
        for s in range(k0 + 1, T):
            if not insc[s] or fbs[s] or A[s].r <= L: break
            if FC.coarse(g, A[s + 1].theta, L) != FC.coarse(g, A[s].theta, L): j = s; break
        if j is None: continue
        C["rises"] += 1; x0 = A[k0].fh[o]; u = j + 1
        why = ("stop" if u >= T else "out_of_scope" if not insc[u] else "fallback_at_j+1" if fbs[u] else
               "r<=L_at_j+1" if A[u].r <= L else "S4a_with_r>L_at_j+1")
        C["AT_j+1: " + why] += 1
        rl = FC.lev(g, A[j].theta, A[j + 1].theta); C["rise_level==r_j" if rl == A[j].r else "rise_level<r_j"] += 1
        if u < T: C["r_{j+1}<=L" if A[u].r <= L else "r_{j+1}>L"] += 1
        if x0 in A[k0].Rbar: bad.append((tag, k0, "x_k0 not in F_k0")); continue
        cl = FC.coarse(g, A[k0].Xi[x0], L)
        mins = [x for x in set(g.succ[o]) if x != o and x not in A[k0].Rbar and FC.coarse(g, A[k0].Xi[x], L) == cl]
        t = j + 1
        while True:
            C["checks"] += 1
            if t < len(A) and A[t].r > L:
                C["GA_states"] += 1
                St = A[t]; hi = [(y, z) for (y, z), l in St.gates.items() if l > L]
                C["GA_hi_into_Rbar" if any(z in St.Rbar for y, z in hi) else "GA_hi_into_F_only" if hi else "GA_no_hi"] += 1
                if any(z in St.Rbar and y not in St.Rbar for y, z in hi): C["GA_hi_F_to_Rbar"] += 1
                fr = [(y, z) for (y, z) in St.gates if y not in St.Rbar and z in St.Rbar]
                if any(z in St.Rbar for (y, z) in St.gates): C["INTO_states_ok"] += 1
                else: C["INTO_FAIL (no gate into Rbar, r_t > L after a rise)"] += 1; bad.append(("INTO", tag, k0, j, t, sorted(St.gates.items())[:6], L))
                if fr: C["FEED_states_ok"] += 1
                else:
                    C["FEED_FAIL (no F->Rbar gate, r_t > L after a rise)"] += 1; bad.append(("FEED", tag, k0, j, t, sorted(St.gates.items())[:6], L))
                if not EC.M(A[t]) > L: C["GA_FAIL (M_t <= L with r_t > L after a rise)"] += 1; bad.append(("GA", tag, k0, j, t, EC.M(A[t]), L))
            for x in mins:
                if x not in A[t].Rbar: C["FAIL"] += 1; bad.append((tag, k0, j, t, x))
            # extend: transition t -> t+1 must be an in-scope S4a step with r_t > L
            if t >= T or not insc[t] or fbs[t] or A[t].r <= L: break
            t += 1
        C["stretch_len_after_rise"] += t - j

def main():
    Rn, seed, files = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    C = Counter(); bad = []
    for p in files:
        g = RC.parse(open(p).read()); o = FC.odd_vertex(g); rng = random.Random(f"{seed}:{os.path.basename(p)}")
        C["files"] += 1
        starts = [FC.s3_start(g)] + [RC.rand_start(rng, g) for _ in range(Rn)]
        for i, (s, t) in enumerate(starts):
            for mode in ("own", "spec"):
                A, fbs = OC.run_trace(g, o, s, t, rng, mode); C["traces"] += 1
                scan(g, o, A, fbs, C, bad, (os.path.basename(p), i, mode))
    print("TOTAL", dict(sorted(C.items()))); print("FAIL (first 5 per kind):", [b for b in bad if b[0] == "FEED"][:5], [b for b in bad if b[0] == "GA"][:3], [b for b in bad if b[0] == "INTO"][:5], [b for b in bad if b[0] not in ("FEED", "GA", "INTO")][:3]); print("RESULT", "FAIL" if C["FAIL"] else "OK", "(OLD-THREAT);", "GATE-ABOVE", "FAIL" if C["GA_FAIL (M_t <= L with r_t > L after a rise)"] else "OK", "; FEED", "FAIL" if C["FEED_FAIL (no F->Rbar gate, r_t > L after a rise)"] else "OK", "; INTO", "FAIL" if C["INTO_FAIL (no gate into Rbar, r_t > L after a rise)"] else "OK")
if __name__ == "__main__": main()
