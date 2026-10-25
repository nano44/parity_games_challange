#!/usr/bin/env python3
"""REFEREE succ. 9: climb toward the P-N5-LV setting (in-scope THR fallbacks with M = -1), own code (lv_probe.run, neb_climb.mutate).
Score = 100 #(THR, M = -1) + #(in-scope THR fallbacks with M <= 1 at low level) ; any *_FAIL instance is written out.
Usage: lv_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, lv_probe as LV, neb_climb as NC


def low(g):
    o, st = P.states(g); P.OO[0] = o; inph, runs = P.scope_runs(st); c = 0
    for S in runs:
        for k in S:
            a = st[k]
            if a["fb"] and a["Is"] and a["Xi"][o] != a["W"][o] and a["M"] <= 1: c += 1
    return c


def score(g):
    c = Counter(); LV.EX.clear()
    try: LV.run(g, c, "climb"); l = low(g)
    except (RuntimeError, AssertionError): return None, c
    return 100 * (c["fb_THRr>=0_M-1"] + c["fb_THRr=-1_M-1"]) + l, c


def main(seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur, _ = score(g); cur = cur or 0; best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes)
    while time.time() < end:
        i += 1
        try: h = NC.mutate(g, rng)
        except AssertionError: continue
        s, c = score(h)
        if s is None: continue
        for k, v in c.items(): tot[k] += v
        if any(k.endswith("_FAIL") and v for k, v in c.items()): NC.write(h, os.path.join(out, "fail_%s_%d.pg" % (rs, i))); tot["fail_files"] += 1
        if c["fb_THRr>=0_M-1"] + c["fb_THRr=-1_M-1"]: NC.write(h, os.path.join(out, "hit_%s_%d.pg" % (rs, i))); tot["hit_files"] += 1
        if s >= cur:
            g, cur = h, s
            if s > best: best = s; NC.write(g, os.path.join(out, "best_%s.pg" % rs))
    tot["iters"] = i; tot["best_score"] = best
    for k in sorted(tot): print("%-26s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
