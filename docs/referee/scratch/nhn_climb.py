#!/usr/bin/env python3
"""REFEREE succ. 10: climb for P-N5-NHN's thin regimes (own code: rl_probe.states, nhn_probe.run, neb_climb.mutate; no lane code).
Score = max over phases with tau(o) != o and an HN state, over EV2 ends k = g_j: 1000 * [j >= |U| - 1] + 10 * #EV2 ends of the phase
+ (j - (|U| - 1)) (so the walk is pulled toward late EV2 ends, i.e. T0-PIN); -999 if there is no EV2 end. Candidates with an EV2 end
are checked with nhn_probe.run; any *_FAIL is written out. Usage: nhn_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, nhn_probe as NP, neb_climb as NC


def score(g):
    o, st = P.states(g); T = len(st) - 1; best = -999; k = 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        t0 = st[k]["t"][o]
        if t0 != o:
            c = st[k]["Xi"][o][0]; u = sum(1 for v in range(g.n) if st[k]["Xi"][v][0] == c)
            fbs = [t for t in range(k, j) if st[t]["fb"]]
            HN = lambda t: st[t]["H1"] and not st[t]["H2"]
            ev2 = [t for t in range(k, j) if HN(t) and st[t + 1]["H1"] and st[t + 1]["H2"]]
            for e in ev2:
                jj = fbs.index(e) + 1 if e in fbs else 0
                best = max(best, 1000 * (jj >= u - 1) + 10 * len(ev2) + (jj - (u - 1)))
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
        if s > -999:
            tot["with_EV2"] += 1
            c = Counter(); NP.EX.clear(); NP.run(h, c, "climb")
            for kk, v in c.items():
                if kk.endswith("_FAIL") or kk in ("EV2_ends", "PIN_ends", "SG_chk", "H3_chk", "NHN_drops_ending_stretch"): tot[kk] += v
            tot["NHN_max"] = max(tot["NHN_max"], c["NHN_max"]); tot["EV2_max_per_phase"] = max(tot["EV2_max_per_phase"], c["EV2_max_per_phase"])
            if any(kk.endswith("_FAIL") and v for kk, v in c.items()):
                NC.write(h, os.path.join(out, "fail_%s_%d.pg" % (rs, i))); print("FAILCASE", NP.EX[:5], flush=True)
            if c["PIN_ends"] and saved < 6: saved += 1; NC.write(h, os.path.join(out, "pin_%s_%d.pg" % (rs, i)))
        if s >= cur:
            if s > best: best = s
            g, cur = h, s
    tot["iters"] = i; tot["best_score"] = best
    for kk in sorted(tot): print("%-30s %d" % (kk, tot[kk]))
    print("FAILS", sum(v for kk, v in tot.items() if kk.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
