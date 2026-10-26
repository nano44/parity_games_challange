#!/usr/bin/env python3
"""REFEREE succ. 9: climb on in-scope THR fallbacks with r = -1 (u* = none), for P-N5-LV (LV-SHAPE at r = -1) and P-N5-LV2
(FLAT-ALL_-1^none, LV-NONE, SAND, SCOPE-FB). Own code (lv_probe.run, lv2_probe.c1o, neb_climb.mutate). Score = max over scope runs of
#(r = -1 fallbacks) + 0.01 * total. Usage: lvn_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, lv_probe as LV, lv2_probe as L2, neb_climb as NC


def score(g):
    c = Counter(); LV.EX.clear(); L2.EX.clear()
    try:
        LV.run(g, c, "c"); L2.c1o(g, c, "c")
        o, st = P.states(g); P.OO[0] = o; _, runs = P.scope_runs(st)
    except (RuntimeError, AssertionError): return None, c
    best = 0
    for S in runs:
        best = max(best, sum(1 for k in S if st[k]["fb"] and st[k]["Is"] and st[k]["Xi"][o] != st[k]["W"][o] and st[k]["r"] == -1))
    return best + 0.01 * c["fb_THRr=-1_M-1"], c


def main(seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur, _ = score(g); best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes)
    while time.time() < end:
        i += 1
        try: h = NC.mutate(g, rng)
        except AssertionError: continue
        s, c = score(h)
        if s is None: continue
        tot["evaluated"] += 1
        for k, v in c.items():
            if k.endswith("_FAIL") or k.startswith("SHAPE") or k.startswith("FLATN") or k.startswith("NONE") or k == "fb_THRr=-1_M-1" or k == "SAND_chk": tot[k] += v
        if any(k.endswith("_FAIL") and v for k, v in c.items()): NC.write(h, os.path.join(out, "fail_%s_%d.pg" % (rs, i)))
        if s >= cur:
            g, cur = h, s
            if s > best: best = s; NC.write(g, os.path.join(out, "best_%s.pg" % rs))
    tot["iters"] = i; tot["best_x100"] = int(100 * best)
    for k in sorted(tot): print("%-26s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
