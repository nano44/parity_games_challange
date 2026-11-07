#!/usr/bin/env python3
"""L-NEW box 145 THRESHOLD-CAST test. For an IDEAL-ACYC genome with N movers (deg 2, R178 §1 rule; box139/paths.py run()), compute the
one-step map Phi: {0,1}^N -> {0,1}^N (Phi(s) = the state after one step from s; s itself if the step is 'opt' or 'stuck') on ALL 2^N
states, and for every mover x test whether Phi_x is a linear threshold function of s:
- NONUNATE: number of movers x for which some variable j is neither positive nor negative unate in Phi_x (a threshold function is unate
  in every variable), with one witness (x, j, s_up, s_down);
- NONASUM2: number of movers x violating 2-asummability (f(a) = f(b) = 1, f(c) = f(d) = 0, a + b = c + d as integer vectors): a
  threshold function is k-asummable for every k.
Prints also the number of distinct one-step images. Usage: thr.py genome.json ..."""
import sys, os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
for p in sys.argv[1:]:
    G = json.load(open(p)); N = G["N"]; Phi = {}
    for s in itertools.product((0, 1), repeat=N):
        H = dict(G); H["start"] = list(s); S = run(H, cap=1)[0]; Phi[s] = S[1] if len(S) > 1 else s
    nonun = 0; wit = None; nonas = 0
    for x in range(N):
        f = {s: Phi[s][x] for s in Phi}; bad = False
        for j in range(N):
            up = dn = None
            for s in Phi:
                if s[j]: continue
                t = s[:j] + (1,) + s[j + 1:]
                if f[t] > f[s]: up = s
                if f[t] < f[s]: dn = s
            if up is not None and dn is not None:
                bad = True
                if wit is None: wit = (x, j, up, dn)
        nonun += bad
        ones = [s for s in f if f[s]]; zeros = [s for s in f if not f[s]]
        so = {tuple(a + b for a, b in zip(u, v)) for u, v in itertools.combinations_with_replacement(ones, 2)}
        sz = {tuple(a + b for a, b in zip(u, v)) for u, v in itertools.combinations_with_replacement(zeros, 2)}
        nonas += bool(so & sz)
    print(f"THR {os.path.basename(p)} N {N} STATES {2**N} IMAGES {len(set(Phi.values()))} NONUNATE {nonun} NONASUM2 {nonas} WITNESS {wit}")
