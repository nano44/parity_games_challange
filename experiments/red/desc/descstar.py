#!/usr/bin/env python3
"""L-RED successor 38 (R163): DESC* per W-run = min over WITNESS sets U (every W-changing transition of the run changes W at some
u in U) of DESC_U = sum_{u in U} DESC(u). A weighted set cover, solved exactly as a 0/1 ILP (scipy.optimize.milp, HiGHS); secondary
objective min |U| (weight 1 / (n + 1)). Vertex descents are those of desc2.py (L-NEW box 111 desc.py), which do not depend on U.
Runs desc2.py's setup code verbatim (exec of its text up to the counting loop). Prints per run: length, DESC (U = V), DESC*, |U*|,
LP bound, and the descending vertices of U*. Usage: descstar.py G.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "desc2.py")).read(); src = src[:src.index("T = dict(")]
exec(compile(src, "desc2.py", "exec"))
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds, linprog
out = []
for run in runs:
    tau = TAU[run[0]]; last = {}; desc = {}; chg = []
    for k in run:
        A, B = W(k, tau), W(k + 1, tau); c = []
        for v in range(n):
            if A[v] == B[v]: continue
            q = next(i for i in range(len(A[v])) if A[v][i] != B[v][i]); c.append(v)
            if v in last and q > last[v]: desc[v] = desc.get(v, 0) + 1
            last[v] = q
        if c: chg.append(c)
    vs = sorted({v for c in chg for v in c}); ix = {v: i for i, v in enumerate(vs)}
    cost = np.array([desc.get(v, 0) + 1.0 / (n + 1) for v in vs])
    M = np.zeros((len(chg), len(vs)))
    for r, c in enumerate(chg):
        for v in c: M[r, ix[v]] = 1
    res = milp(cost, constraints=LinearConstraint(M, lb=np.ones(len(chg))), integrality=np.ones(len(vs)), bounds=Bounds(0, 1))
    lp = linprog(cost, A_ub=-M, b_ub=-np.ones(len(chg)), bounds=(0, 1))
    U = [vs[i] for i in range(len(vs)) if res.x[i] > 0.5]; ds = sum(desc.get(v, 0) for v in U)
    out.append((len(run), sum(desc.values()), ds, len(U), lp.fun, sorted((desc[v], LAB[v]) for v in U if desc.get(v, 0))[::-1][:8], res.status))
for o in out: print(f"RUN len {o[0]} DESC {o[1]} DESC* {o[2]} |U*| {o[3]} LP {o[4]:.2f} status {o[6]} U*-descenders {o[5]}")
print(f"DESCSTAR {os.path.basename(sys.argv[1])} n {n} runs {len(out)} longest {max([o[0] for o in out] or [0])} DESC {sum(o[1] for o in out)} DESC* {sum(o[2] for o in out)} maxrunDESC* {max([o[2] for o in out] or [0])}")
