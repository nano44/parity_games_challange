#!/usr/bin/env python3
"""REFEREE-2 succ. 8: hill-climb C^1O games against P-N5-RL with rl_check (own code; mutations of ../R2-N5-FRZ/frz_climb.py).
FIT cyc: c's honest cycle meeting Ev after an in-scope fallback (the TEV-RED probe), its preconditions (P(theta_k0) = {}, c switched into
Rbar_k0), ENT settings, THR fallbacks. A violation stops the climb (climb/viol_<FIT>_<seed>.pg).
Usage: rl_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import rl_check as RL, frz_check as FC, frz_climb as FCL
RC = FC.RC
def fitness(st):
    c = st.c
    return (1000 * c["CYC_c_cycle_meets_Ev"] + 500 * c["ENT_settings"] + 100 * c["CYC_precond_c_switched_into_Rbar_k0"]
            + 50 * c["CYC_precond_P(theta_k0)=empty"] + 2 * c["BL_THR_fallbacks"] + c["CYC_threat_meets_Ev"])
def evaluate(g, o, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); RL.check_run(g, o, A, fbs, st, f"r{r}")
    return fitness(st), st
def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6: g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else: g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
    best, st = evaluate(g, o, seed); t0 = time.time(); it = acc = 0; tot = FC.Stats()
    while time.time() - t0 < secs:
        it += 1; h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, s2 = evaluate(h, o, seed)
        tot.c["climb_evaluations"] += 1
        for k, v in s2.c.items(): tot.c[k] += v
        if s2.c["VIOLATIONS"]:
            FCL.dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            break
        if s2.c["CYC_c_cycle_meets_Ev"] and not tot.c.get("dumped"):
            FCL.dump(h, os.path.join(HERE, "climb", f"cyc_{seed}.pg")); tot.c["dumped"] = 1
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
