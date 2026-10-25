#!/usr/bin/env python3
"""REFEREE succ. 9: climb toward the P-FREEZE post-freeze regime with |U| >= 3 (own code; pfz_probe.run, neb_climb.mutate).
Score = max over theta-runs with |U| >= 3 of (#Even fallbacks in the run) - (|U| - 1), floored at -50; any *_FAIL is written out, and so is
every game with a |U| >= 3 post-freeze theta-run. Usage: pfz_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, pfz_probe as PZ, neb_climb as NC


def excess(g):
    o, st = P.states(g); T = len(st) - 1; best = -50; k = 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        c = st[k]["Xi"][o][0]; u = sum(1 for v in range(g.n) if st[k]["Xi"][v][0] == c)
        t = k
        while t <= j:
            e = t
            while e < j and st[e + 1]["Xi"][o] == st[t]["Xi"][o]: e += 1
            f = sum(1 for x in range(t, e) if st[x]["fb"] and st[x]["Is"])
            if u >= 3: best = max(best, f - (u - 1))
            t = e + 1
        k = j + 1
    return best


def main(seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur = excess(g); best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes)
    while time.time() < end:
        i += 1
        try: h = NC.mutate(g, rng)
        except AssertionError: continue
        try: s = excess(h)
        except RuntimeError: continue
        tot["evaluated"] += 1
        if s >= 1:
            tot["postfreeze_U3_games"] += 1
            c = Counter(); PZ.EX.clear(); PZ.run(h, c, "climb")
            for k, v in c.items():
                if k.endswith("_FAIL") or "postfreeze" in k or k.endswith("_PFC_states") or k.endswith("NXA_chk") or k.endswith("post_urise_transitions"): tot[k] += v
            if any(k.endswith("_FAIL") and v for k, v in c.items()): NC.write(h, os.path.join(out, "fail_%s_%d.pg" % (rs, i)))
            if tot["postfreeze_U3_games"] <= 5: NC.write(h, os.path.join(out, "post_%s_%d.pg" % (rs, i)))
        if s >= cur:
            g, cur = h, s
            if s > best: best = s
    tot["iters"] = i; tot["best_excess"] = best
    for k in sorted(tot): print("%-30s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
