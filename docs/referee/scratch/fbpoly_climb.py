#!/usr/bin/env python3
"""REFEREE succ. 10: climb toward P-N5-FBPOLY's untested regime (own code: rl_probe.states, fbpoly_probe.run, neb_climb.mutate).
Score = max over phases with o != c and |U| >= 3 of f - (|U| - 1) (>= 0: a fallback g_j with j >= |U| - 1 exists, i.e. FREEZE-EXIT /
THETA-AFTER's regime; >= 0 also refutes FB-CAP f <= |U| - 2), floored at -50; -60 if no such phase has a fallback.
Candidates with score >= -1 are checked with fbpoly_probe.run; any *_FAIL or score >= 0 is written out.
Usage: fbpoly_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, fbpoly_probe as FP, neb_climb as NC


def score(g):
    o, st = P.states(g); T = len(st) - 1; best = -60; k = 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        c = st[k]["Xi"][o][0]
        if c != o:
            u = sum(1 for v in range(g.n) if st[k]["Xi"][v][0] == c)
            f = sum(1 for t in range(k, j) if st[t]["fb"])
            if u >= 3 and f: best = max(best, max(-50, f - (u - 1)))
        k = j + 1
    return best


def main(seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur = score(g); best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes); saved = 0
    while time.time() < end:
        i += 1
        try: h = NC.mutate(g, rng)
        except AssertionError: continue
        try: s = score(h)
        except RuntimeError: continue
        tot["evaluated"] += 1
        if s >= -1:
            tot["checked"] += 1
            c = Counter(); FP.EX.clear(); FP.run(h, c, "climb")
            for kk, v in c.items():
                if kk.endswith("_FAIL") or kk in ("CN_cases", "SU_nonempty", "KH_chk", "KHC_chk", "KP_chk", "TA_phases_U3plus",
                                                 "POSTFZ_phases", "FE_regime_hit"): tot[kk] += v
            bad = any(kk.endswith("_FAIL") and v for kk, v in c.items())
            if bad or (s >= 0 and saved < 10):
                saved += 1; NC.write(h, os.path.join(out, "%s_%s_%d.pg" % ("fail" if bad else "postfz", rs, i)))
                print("SAVED", "fail" if bad else "postfz", i, s, FP.EX[:3], flush=True)
        if s >= cur:
            if s > best: best = s; print("BEST", i, s, flush=True)
            g, cur = h, s
    tot["iters"] = i; tot["best_score"] = best
    for kk in sorted(tot): print("%-30s %d" % (kk, tot[kk]))
    print("FAILS", sum(v for kk, v in tot.items() if kk.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
