#!/usr/bin/env python3
"""L-SI succ. 8, box 13 item (1): hill-climb toward many THR r = -1 (u* = none) fallbacks in ONE scope run (LV-NONE) and many S4c
fallbacks in one scope run (SCOPE-FB). Mutations and the C^1O filter are REFEREE-2's (R2-N5-FRZ/frz_climb.py; read only, imported).
Fitness (box 13, v2) = 10^5 * max none per run + 1000 * min(50, in-scope transitions after a run's first none fallback) + 10 * max fb
per run + total none (v1, climbs 1301-1304: 1000 * max none + 10 * max fb + total none); per game: S3 start (spec, own) + R random starts.
Any bound violation dumps the game to logs/viol_<seed>.pg and stops. Usage: none_climb.py seed seconds R seed_game.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import none_count as NC
sys.path.insert(0, os.path.join(NC.R2, "R2-N5-FRZ")); import frz_climb as FCL
from collections import Counter

def evaluate(g, o, R, seed):
    C = Counter(); W = {"after": [], "sand": [], "lvnone": [], "scopefb": [], "ratio_none": (0,), "ratio_fb": (0,)}
    rng = random.Random(seed); s, t = NC.FC.s3_start(g)
    for mode in ("spec", "own"): NC.one(g, o, s, t, rng, mode, C, W, ("S3", mode))
    for i in range(R):
        s, t = NC.RC.rand_start(rng, g)
        for mode in ("own", "spec"): NC.one(g, o, s, t, rng, mode, C, W, (f"rnd{i}", mode))
    f = 10 ** 5 * C["max_none_per_run"] + 1000 * min(C["transitions_after_first_none_fb"], 50) + 10 * C["max_fb_per_run"] + C["fb_none"]
    return f, C, W

def main():
    seed, secs, R, p = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); g = NC.RC.parse(open(p).read()); o = NC.FC.odd_vertex(g)
    best, C, W = evaluate(g, o, R, seed); t0 = time.time(); it = 0; tot = Counter(); os.makedirs(os.path.join(HERE, "logs"), exist_ok=True)
    while time.time() - t0 < secs:
        it += 1; h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, C2, W2 = evaluate(h, o, R, seed); tot["evals"] += 1
        for k in ("transitions_after_first_none_fb", "fb_after_a_none_fb", "fb_none", "fb_inscope", "scope_runs", "SAND_checks", "SAND_FAIL", "LVNONE_FAIL", "SCOPEFB_FAIL"): tot[k] += C2[k]
        for k in ("max_none_per_run", "max_fb_per_run"): tot[k] = max(tot[k], C2[k])
        if C2["SAND_FAIL"] or C2["LVNONE_FAIL"] or C2["SCOPEFB_FAIL"]:
            FCL.dump(h, os.path.join(HERE, "logs", f"viol_{seed}.pg")); print("VIOLATION", W2["sand"][:3], W2["lvnone"][:3], W2["scopefb"][:3]); break
        if f >= best: g, best, C, W = h, f, C2, W2
    FCL.dump(g, os.path.join(HERE, "logs", f"best_{seed}.pg"))
    print(f"climb seed={seed} n={g.n} iterations={it} best_fitness={best}")
    print("BEST", dict(sorted(C.items()))); print("BEST worst ratios", W["ratio_none"], W["ratio_fb"])
    print("ALL-EVALS", dict(sorted(tot.items())))
if __name__ == "__main__": main()
