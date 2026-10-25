#!/usr/bin/env python3
"""REFEREE-2 succ. 7: hill-climb C^1O games against P-N5-L2 with l2_check (own code; mutations of ../R2-N5-FRZ/frz_climb.py).
FIT frz : n-state H3 windows containing not-H1 states (FREEZE' beyond FREEZE), P^c' windows with not-H1, later checks at not-H1 t
FIT tog : H1-toggles inside SN prefixes, drops per phase, (h)-runs per phase, H2-STICK steps, restarts by fallback
Usage: l2_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import l2_check as L2, frz_check as FC, frz_climb as FCL
RC = FC.RC
def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "frz":
        return 300 * c["FRZ'_freezes_window_with_notH1"] + 20 * c["FRZ'_a_checks_at_notH1_t"] + 2 * c["PC'_windows_with_notH1"] + m["PC_max_window_len_over_n_x100"] / 5
    return (50 * m["XR'_max_toggles_t_Q"] + 100 * m["ONE-DROP_max_drops_per_phase (sec.8, no claim)"] + 100 * m["ONE-H_max_h_runs_per_phase (sec.8, no claim)"]
            + 5 * c["H2S_steps"] + 300 * c["H2S_restart_by_fallback (sec.8 open (2), no claim)"] + c["GP_H3_notH1_states"] / 5)
def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); L2.check_run(g, o, A, fbs, rng, st, f"r{r}")
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
