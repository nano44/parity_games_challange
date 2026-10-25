#!/usr/bin/env python3
"""L-SI succ. 8, box 13 item (1): DATA for P-N5-LV2 LV-NONE (<= n*n_E + 1 THR fallbacks with r = -1 per scope run), SCOPE-FB
(<= 4*n*n_E + 3 S4c fallbacks per scope run) and SAND (COARSE_{-1}(theta) frozen after the first r = -1 state of a scope run), from
REFEREE-2's start pairs (Lead 15:59Z). Traces and state analysis are REFEREE-2's (docs/referee-2/R2-N5-OUT, -FRZ, -RE; read only,
imported, not edited); scope runs as in R2-N5-ENT/ent_check.py (insc). Starts: S3 (s3_start) in modes spec/own, plus R random starts
(rand_start) in modes own/rand/spec, rng seeded per file.
Usage: none_count.py R seed game.pg ..."""
import sys, os, random
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ", "R2-N5-ENT", "R2-N5-RE"): sys.path.insert(0, os.path.join(R2, d))
import out_check as OC, frz_check as FC
RC = FC.RC
from collections import Counter

def scope_runs(g, o, A, fbs):
    T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    k = 0
    while k < T:
        if not insc[k]: k += 1; continue
        j = k
        while j + 1 < T and insc[j + 1]: j += 1
        yield k, j; k = j + 1

def one(g, o, s, t, rng, mode, C, W, tag):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0)
    A, fbs = OC.run_trace(g, o, s, t, rng, mode); C["traces"] += 1
    for a, b in scope_runs(g, o, A, fbs):
        C["scope_runs"] += 1; nf = nn = 0; base = None; after = None
        for k in range(a, b + 1):
            S = A[k]
            if base is not None:
                for X in (A[k], A[k + 1]):
                    C["SAND_checks"] += 1
                    if FC.coarse(g, X.theta, -1) != base: C["SAND_FAIL"] += 1; W["sand"].append(tag)
            if S.r == -1 and base is None: base = FC.coarse(g, S.theta, -1)
            if not fbs[k]: continue
            nf += 1
            if after is not None: C["fb_after_a_none_fb"] += 1; W["after"].append((tag, k))
            if g.cmp(S.theta, S.w) < 0 and S.r == -1:
                nn += 1
                if after is None: after = k; C["transitions_after_first_none_fb"] += b - k
        C["fb_inscope"] += nf; C["fb_none"] += nn
        if nn: C["runs_with_none"] += 1
        bn, bf = n * nE + 1, 4 * n * nE + 3
        if nn > bn: C["LVNONE_FAIL"] += 1; W["lvnone"].append((tag, nn, bn))
        if nf > bf: C["SCOPEFB_FAIL"] += 1; W["scopefb"].append((tag, nf, bf))
        for key, v, bd in (("none", nn, bn), ("fb", nf, bf)):
            if v > C[f"max_{key}_per_run"]: C[f"max_{key}_per_run"] = v
            if v / bd > W[f"ratio_{key}"][0]: W[f"ratio_{key}"] = (v / bd, tag, v, bd)

def main():
    Rn, seed, files = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    C = Counter(); W = {"after": [], "sand": [], "lvnone": [], "scopefb": [], "ratio_none": (0,), "ratio_fb": (0,)}
    for p in files:
        g = RC.parse(open(p).read()); o = FC.odd_vertex(g); rng = random.Random(f"{seed}:{os.path.basename(p)}")
        C["files"] += 1; nm = os.path.basename(p)
        s, t = FC.s3_start(g)
        for mode in ("spec", "own"): one(g, o, s, t, rng, mode, C, W, (nm, "S3", mode))
        for i in range(Rn):
            s, t = RC.rand_start(rng, g)
            for mode in ("own", "rand", "spec"): one(g, o, s, t, rng, mode, C, W, (nm, f"rnd{i}", mode))
    print("TOTAL", dict(sorted(C.items())))
    print("WORST none/(n n_E + 1):", W["ratio_none"]); print("WORST fb/(4 n n_E + 3):", W["ratio_fb"])
    print("AFTER (fallbacks after a none fallback in the same run, first 5):", W["after"][:5])
    for k in ("sand", "lvnone", "scopefb"): print(f"{k.upper()} failures (first 5):", W[k][:5])
    print("RESULT", "FAIL" if (C["SAND_FAIL"] or C["LVNONE_FAIL"] or C["SCOPEFB_FAIL"]) else "OK")

if __name__ == "__main__":
    main()
