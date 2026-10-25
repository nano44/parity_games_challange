#!/usr/bin/env python3
"""REFEREE-2 succ. 10: hill-climb against P-N5-LV2 with lv2_check (own code; C^1O mutations of ../R2-N5-FRZ/frz_climb.py, as in
R2-N5-LV/lv_climb.py). Any violation stops the climb and dumps the game to climb/viol_<FIT>_<seed>.pg.
FIT none: toward many THR fallbacks with r = -1 in ONE scope run (LV-NONE's count; N >= 2 makes LV-NONE (1)-(2) non-vacuous).
FIT blk:  toward the level -1 block (THR, r >= 0, M = -1; LV-PL', ENT-X_{-1}).
Usage: lv2_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
for d in ("R2-N5-OUT", "R2-N5-ENT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(HERE, "..", d))
import out_check as OC, lv2_check as EC, frz_check as FC, frz_climb as FCL
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "none":
        return (1000 * m["max_per_run_none"] + 300 * c["LVNONE_runs_N>=2"] + 30 * c["RECORD_fallbacks_none"] + 5 * c["RECORD_runs_with_r=-1"]
                + c["RECORD_fallbacks_ge0"] + c["RECORD_fallbacks_blk"])
    return 1000 * m["max_per_run_blk"] + 300 * c["LVPL_runs_N>=2"] + 50 * c["RECORD_fallbacks_blk"] + c["RECORD_fallbacks_ge0"]

def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        mode = "own" if r < 2 else "rand"
        A, fbs = OC.run_trace(g, o, s, t, rng, mode); EC.check_run(g, o, A, fbs, st, f"{mode}:r{r}")
    return fitness(st, fit), st

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else:
        while True:
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
            if FCL.ok(g, o): break
    best, st = evaluate(g, o, fit, seed); t0 = time.time(); it = acc = 0; tot = FC.Stats()
    while time.time() - t0 < secs:
        it += 1
        h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, s2 = evaluate(h, o, fit, seed)
        tot.c["climb_evaluations"] += 1
        for k, v in s2.c.items(): tot.c[k] += v
        for k, v in s2.mx.items(): tot.mx[k] = max(tot.mx[k], v)
        if s2.c["VIOLATIONS"]:
            FCL.dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            tot.c["VIOLATIONS"] += s2.c["VIOLATIONS"]; break
        for cls_ in ("blk", "none"):
            wp = os.path.join(HERE, "climb", f"witness_{cls_}_{seed}.pg")
            if s2.c[f"RECORD_fallbacks_{cls_}"] and not os.path.exists(wp): FCL.dump(h, wp)
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
