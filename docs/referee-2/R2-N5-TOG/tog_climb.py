#!/usr/bin/env python3
"""REFEREE-2 succ. 7: hill-climb C^1O games against P-N5-TOG with tog_check (own code; mutations of ../R2-N5-FRZ/frz_climb.py).
FIT tog: toggles / drops / sigma(c)- and Z-changes per phase, restarts, toggles with Z unchanged, X_SN crossings at the SN-prefix exit.
Usage: tog_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import tog_check as TG, frz_check as FC, frz_climb as FCL
RC = FC.RC
def fitness(st, fit):
    c, m = st.c, st.mx
    return (100 * m["max_toggles_per_phase"] + 100 * m["max_drops_per_phase"] + 50 * m["max_h_runs_per_phase"] + 20 * m["max_sigma(c)_changes_per_phase"]
            + 2 * m["max_Z_changes_per_phase"] + 30 * c["XSN_crossings_at_transition_leaving_SN_prefix"] + 30 * c["RST_restart_by_Even_fallback"]
            + 10 * c["TOGGLE_kind Z_changed=False next(c)_changed=True"])
def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); TG.check_run(g, o, A, fbs, st, f"r{r}")
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
        if s2.c["VIOLATIONS"]:
            FCL.dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            break
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
