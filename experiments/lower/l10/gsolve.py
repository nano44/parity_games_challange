#!/usr/bin/env python3
"""L-LOWER 10: greedy decision list WITH errors (score for search). Constraints as l7/ranksolve.constraints. Repeatedly give the
next highest rank to the unassigned option whose open constraints disagree least (violations = open constraints wanting the other
sign; ties: most satisfied), with the majority sign; close them. Returns (violations, br, bp). violations = 0 iff ranksolve's exact
greedy succeeds on the same constraints (both are decision-list learning; the exact one is complete)."""
def gsolve(cons, nopt):
    C = []
    for t, x, p, A, B in cons:
        C.append({m: (1 if ((m in B) == (p == 1)) else 0) for m in A ^ B})
    by = [[] for _ in range(nopt)]
    for i, r in enumerate(C):
        for m in r: by[m].append(i)
    pos = [0] * nopt; neg = [0] * nopt
    for i, r in enumerate(C):
        for m, s in r.items():
            if s: pos[m] += 1
            else: neg[m] += 1
    openc = [True] * len(C); left = set(range(nopt)); br = [0] * nopt; bp = [0] * nopt; rank = nopt - 1; viol = 0
    while left:
        best = None
        for m in left:
            p, n = pos[m], neg[m]
            if p + n == 0: continue
            key = (min(p, n), -max(p, n))
            if best is None or key < best[0]: best = (key, m)
        if best is None: break
        m = best[1]; sg = 1 if pos[m] >= neg[m] else 0; viol += min(pos[m], neg[m])
        br[m] = rank; bp[m] = 0 if sg == 1 else 1; rank -= 1; left.discard(m)
        for i in by[m]:
            if openc[i]:
                openc[i] = False
                for mm, s in C[i].items():
                    if s: pos[mm] -= 1
                    else: neg[mm] -= 1
    for m in sorted(left): br[m] = rank; rank -= 1
    return viol, br, bp
