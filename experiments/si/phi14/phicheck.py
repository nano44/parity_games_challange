#!/usr/bin/env python3
"""L-SI succ. 9, box 14: DATA for P-N5-PHI. On C^1O traces (SPEC, REFEREE-2's tracer, read only): (a) reward(lambda_k(v)) never decreases;
lambda changes per vertex <= n-1; (Phi-1O) tau changes <= d-1 and #phases <= n(n-1)+d. Usage: phicheck.py R seed game.pg ..."""
import sys, os, random
from collections import Counter
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(R2, d))
import out_check as OC
FC, RC = OC.FC, OC.RC
C, M = Counter(), Counter()
Rn, seed = int(sys.argv[1]), int(sys.argv[2])
for p in sys.argv[3:]:
    g = RC.parse(open(p).read())
    try: o = FC.odd_vertex(g)
    except AssertionError: continue
    rng = random.Random(f"{seed}:{os.path.basename(p)}"); n = g.n; d = len(set(g.succ[o])); C["files"] += 1
    for (s, t) in [FC.s3_start(g)] + [RC.rand_start(rng, g) for _ in range(Rn)]:
        A, fbs = OC.run_trace(g, o, s, t, rng, "spec"); C["traces"] += 1
        ch = Counter(); tch = 0; ph = 1
        for k in range(len(A) - 1):
            for v in range(n):
                a, b = A[k].Xi[v][0], A[k + 1].Xi[v][0]
                C["reward checks"] += 1
                if OC.reward(g, b) < OC.reward(g, a): C["FAIL reward drop"] += 1
                if a != b: ch[v] += 1
            if A[k].tu != A[k + 1].tu: tch += 1
            if OC.key(A[k], o) != OC.key(A[k + 1], o): ph += 1
        if ch and max(ch.values()) > n - 1: C["FAIL lambda changes > n-1"] += 1
        if tch > d - 1: C["FAIL tau changes > d-1"] += 1
        if ph > n * (n - 1) + d: C["FAIL phases"] += 1
        M["max lambda changes/vertex /(n-1)"] = max(M["max lambda changes/vertex /(n-1)"], (max(ch.values()) if ch else 0) / (n - 1))
        M["max tau changes"] = max(M["max tau changes"], tch); M["max phases/(n(n-1)+d)"] = max(M["max phases/(n(n-1)+d)"], ph / (n * (n - 1) + d))
print(dict(C)); print({k: round(v, 3) for k, v in M.items()}); print("RESULT", "FAIL" if any("FAIL" in k for k in C) else "OK")
