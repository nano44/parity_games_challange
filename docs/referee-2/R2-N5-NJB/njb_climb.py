#!/usr/bin/env python3
"""REFEREE-2 succ. 7: hill-climb C^1O games against P-N5-NJB with njb_check (own code; mutations of ../R2-N5-FRZ/frz_climb.py).
FIT mn  : Mn members absorbed inside intervals, small |Mn|, theta COARSE_M changes inside intervals (NJB / literal MINSET (c) would forbid)
FIT norf: rises of theta above L after a fallback, post-rise states, a fallback after a rise, ENT-SHAPE gates
FIT dirty: dirty intervals, blocks, block length
Usage: njb_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import njb_check as NJ, frz_check as FC, frz_climb as FCL
RC = FC.RC
K_CH = "MINSET_theta_coarse_changes_inside (literal (c) / NJB would forbid)"
def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "mn": return 1000 * c[K_CH] + 30 * c["MINSET_members_absorbed"] + 3 * c["MINSET_intervals"] + 1000 * c["dirty_intervals"]
    if fit == "norf": return 1000 * c["NORF_fallback_after_rise"] + 3000 * c["ENT_SHAPE_gates"] + 50 * c["NORF_rises_above_L_after_fallback"] + c["NORF_post_rise_states"]
    return 1000 * c["dirty_intervals"] + 10 * c["blocks"] + 5 * m["max_block_N"] + c["scope_fallbacks"]
def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); NJ.check_run(g, o, A, fbs, rng, st, f"r{r}")
    return fitness(st, fit), st
def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6: g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else: g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
    best, st = evaluate(g, o, fit, seed); t0 = time.time(); it = acc = 0; tot = FC.Stats()
    while time.time() - t0 < secs:
        it += 1; h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, s2 = evaluate(h, o, fit, seed)
        tot.c["climb_evaluations"] += 1
        for k, v in s2.c.items(): tot.c[k] += v
        for k, v in s2.mx.items(): tot.mx[k] = max(tot.mx[k], v)
        if s2.c["VIOLATIONS"] or s2.c[K_CH] or s2.c["dirty_intervals"]:
            FCL.dump(h, os.path.join(HERE, "climb", f"event_{fit}_{seed}_{it}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            if s2.c["VIOLATIONS"]: break
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
