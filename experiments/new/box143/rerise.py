#!/usr/bin/env python3
"""L-NEW box 143: test of the Lead's charging hint «a face that rose cannot rise again until a carry passes above it», read literally:
for every option face (x, k) and consecutive strict rises at steps t1 < t2, is there a carry (L_m changes) at some level m >= lev(x)
at a step in (t1, t2]? RERISEVIOL counts the pairs without one; STRICT variant: m >= lev(x) and step in (t1, t2) (open). Also
MAXRISES = max rises of one face. Usage: rerise.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]; fc = ns["fc"]
for p in sys.argv[1:]:
    G = json.load(open(p)); S, CUR, KEY, why = run(G, cap=5000); N = G["N"]; d = N // 2; lev = G["lev"]; T = len(S) - 1
    F = []
    for t in range(T + 1):
        val, idx, _, M = fc.values(G, list(S[t])); F.append([[val(N + idx[(v, k)]) for k in range(2)] for v in range(N)])
    def L(t, l):
        K = KEY[min(t, len(KEY) - 1)]; return 0 if K[2 * l] < K[2 * l + 1] else 1
    car = [[L(t, l) != L(t - 1, l) for l in range(d)] if t else [False] * d for t in range(T + 1)]
    v1 = v2 = 0; mr = 0; pairs = 0
    for x in range(N):
        for k in range(2):
            r = [t for t in range(1, T + 1) if F[t][x][k] > F[t - 1][x][k]]; mr = max(mr, len(r))
            for a, b in zip(r, r[1:]):
                pairs += 1
                if not any(car[t][m] for t in range(a + 1, b + 1) for m in range(lev[x], d)): v1 += 1
                if not any(car[t][m] for t in range(a + 1, b) for m in range(lev[x], d)): v2 += 1
    print(f"RERISE {os.path.basename(p)} d {d} STEPS {T} PAIRS {pairs} RERISEVIOL {v1} STRICTVIOL {v2} MAXRISES {mr}")
