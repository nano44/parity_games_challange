#!/usr/bin/env python3
"""REFEREE-2 succ. 10: hill-climb against P-N5-PFZ-ext with pfzx_check (own code; C^1O mutations of ../R2-N5-FRZ/frz_climb.py, as in frz_climb). Any violation stops the climb and dumps the game to climb/viol_<FIT>_<seed>.pg.
FIT brki: toward theta_S > (rho_S + 1) max(|U| - 2, 0) in one HN stretch (BRK-POLY' (i) as written); also dumps climb/brki_cex_<seed>.pg when it is reached.
Usage: pfz_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import out_check as OC, pfzx_check as EC, frz_check as FC, frz_climb as FCL
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    ex = m["max_BRKX_(i)_excess_plus_1000"] - 1000 if m["max_BRKX_(i)_excess_plus_1000"] else -1000
    return 1000 * ex + 50 * m["max_BRKX_rho_S"] + 5 * c["BRKX_stretches_rho>=1"] + c["TLEN_theta_changes"]

def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        mode = "own" if r < 2 else "rand"
        A, fbs = OC.run_trace(g, o, s, t, rng, mode); EC.check_run(g, o, A, fbs, st, f"{mode}:r{r}")
    return fitness(st, fit), st

def mutate(g, o, rng):
    return FCL.mutate(g, o, rng)

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else:
        while True:
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
            if FCL.ok(g, o): break
    best, st = evaluate(g, o, fit, seed); t0 = time.time(); it = acc = 0; tot = OC.Stats()
    while time.time() - t0 < secs:
        it += 1
        h = mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, s2 = evaluate(h, o, fit, seed)
        tot.c["climb_evaluations"] += 1
        for k, v in s2.c.items(): tot.c[k] += v
        for k, v in s2.mx.items(): tot.mx[k] = max(tot.mx[k], v)
        if s2.c["VIOLATIONS"]:
            FCL.dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            break
        if s2.c["RECORD_BRKX_(i)_as_stated_fails"] and not os.path.exists(os.path.join(HERE, "climb", f"brki_cex_{seed}.pg")):
            FCL.dump(h, os.path.join(HERE, "climb", f"brki_cex_{seed}.pg")); print("BRKX (i) as stated fails:", s2.ex.get("ex_i"))
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
