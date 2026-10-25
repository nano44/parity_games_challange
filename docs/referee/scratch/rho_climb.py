#!/usr/bin/env python3
"""REFEREE succ. 10: climb for P-N5-RHO's thin regimes (own code: rl_probe.states, rho_probe.run, neb_climb.mutate; no lane code).
MODE tail: score = max over phases with |U| >= 3 and an H1 state after the hat freeze g_{|U|-2} of 100 + 10*(P(theta)-changes after it)
           + |U|; else max over such phases of #fallbacks - (|U| - 2) (negative).
MODE ffb:  score = max over maximal fallback-free HN runs [s, e] with |U| >= 3 of (e - s) - (|U| - 2); if >= 1, + 10*(P(theta)-changes
           in [s + |U| - 2, e]).
Every candidate with a score >= 0 (tail) / >= 1 (ffb) is checked with rho_probe.run; any *_FAIL is written out.
Usage: rho_climb.py MODE seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, neb_climb as NC


def score(g, mode):
    o, st = P.states(g); T = len(st) - 1; best = -99; k = 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        c = st[k]["Xi"][o][0]; u = sum(1 for v in range(g.n) if st[k]["Xi"][v][0] == c)
        HN = [st[t]["H1"] and not st[t]["H2"] for t in range(T + 1)]
        if u >= 3:
            fbs = [t for t in range(k, j) if st[t]["fb"]]
            if mode == "tail":
                if len(fbs) >= u - 2:
                    post = range(fbs[u - 3] + 1, j + 1)
                    if any(st[t]["H1"] for t in post):
                        ch = sum(st[t]["Xi"][o][1] != st[t + 1]["Xi"][o][1] for t in post if t < j)
                        best = max(best, 100 + 10 * ch + u)
                    else: best = max(best, 0)
                else: best = max(best, len(fbs) - (u - 2))
            else:
                t = k
                while t <= j:
                    if not HN[t]: t += 1; continue
                    s = t
                    while t < j and HN[t + 1] and not st[t]["fb"]: t += 1
                    e = t; t += 1
                    sc = (e - s) - (u - 2)
                    if sc >= 1: sc += 10 * sum(st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in range(s + u - 2, e))
                    best = max(best, sc)
        k = j + 1
    return best


def main(mode, seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur = score(g, mode); best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes); saved = 0
    thr = 0 if mode == "tail" else 1
    while time.time() < end:
        i += 1
        try: h = NC.mutate(g, rng)
        except AssertionError: continue
        try: s = score(h, mode)
        except RuntimeError: continue
        tot["evaluated"] += 1
        if s >= thr:
            tot["qualifying"] += 1
            c = Counter(); RP.EX.clear(); RP.run(h, c, "climb")
            for kk, v in c.items():
                if kk.endswith("_FAIL") or kk.startswith(("HFC_chk", "RT_changes", "postfreeze", "FFB_", "FFC_changes")): tot[kk] += v
            if any(kk.endswith("_FAIL") and v for kk, v in c.items()):
                NC.write(h, os.path.join(out, "fail_%s_%s_%d.pg" % (mode, rs, i))); print("FAILCASE", RP.EX[:5], flush=True)
        if s >= cur:
            if s > best:
                best = s
                if s >= thr and saved < 8: saved += 1; NC.write(h, os.path.join(out, "best_%s_%s_%d_s%d.pg" % (mode, rs, i, s)))
            g, cur = h, s
    tot["iters"] = i; tot["best_score"] = best
    for kk in sorted(tot): print("%-34s %d" % (kk, tot[kk]))
    print("FAILS", sum(v for kk, v in tot.items() if kk.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:6])
