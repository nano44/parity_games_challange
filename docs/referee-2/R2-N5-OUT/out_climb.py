#!/usr/bin/env python3
"""REFEREE-2 succ. 9: hill-climb against P-N5-OUT with out_check (own code; C^1O mutations of ../R2-N5-FRZ/frz_climb.py, with o's
self-loop kept so that tau(o) = o phases stay reachable). Any violation stops the climb and dumps the game to climb/viol_<FIT>_<seed>.pg.
FIT caseb: case-B tau(o) = o fallbacks at HN states and their R -> Rbar gates (CASE-B-LEN's hypothesis; the lane's climbs never reached it).
FIT brk:   case-A breaks, NO-ENTRY-A (a, b) pairs with Xi changes, fallbacks in HN stretches.
FIT nea:   INV stress: R -> Rbar gates at case-A HN fallbacks, steps with Xi changes after them, TAIL steps.
Usage: out_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import out_check as OC, frz_check as FC, frz_climb as FCL
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "caseb":
        return 300 * c["CASEB_RR_gates"] + 80 * c["NEA_fallback_states_caseB"] + 20 * c["caseB_phases"] + 5 * c["HN_stretches"]
    if fit == "brk":
        return 300 * c["breaks_A"] + 100 * c["breaks_B"] + 100 * c["breaks_tau_ne_o"] + 20 * c["NEA_steps_with_Xi_change"] + 10 * m["max_f_S"] + 5 * c["fallbacks_in_stretches"]
    if fit == "nea":
        return 100 * c["NEA_base_RR_gates"] + 40 * c["NEA_steps_with_Xi_change"] + 20 * c["NEA_fallback_states_caseA"] + 2 * c["TAIL_steps"]

def evaluate(g, o, fit, seed):
    st = OC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        mode = "own" if r < 2 else "rand"
        A, fbs = OC.run_trace(g, o, s, t, rng, mode); OC.check_run(g, o, A, fbs, st, f"{mode}:r{r}")
    return fitness(st, fit), st

def mutate(g, o, rng):
    h = FCL.mutate(g, o, rng)
    if o not in h.succ[o]:
        succ = [list(s) for s in h.succ]; succ[o].append(o); h = RC.Game(h.prio, h.owner, succ)
    return h

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else:
        while True:
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
            if o not in g.succ[o]:
                succ = [list(s) for s in g.succ]; succ[o].append(o); g = RC.Game(g.prio, g.owner, succ)
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
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
