#!/usr/bin/env python3
"""REFEREE-2 succ. 8: hill-climb against P-N5-SCOPE with scope_check (own code; C^1O mutations of ../R2-N5-FRZ/frz_climb.py; general
games use a general mutation). Any violation stops the climb and dumps the game to climb/viol_<FIT>_<seed>.pg.
FIT scope: scope runs per phase (case 2 weighted), WCH per phase and per crossing-free interval, (h)-runs.
FIT fb:    fallbacks per crossing-free run, not-H1 fallbacks per phase, case-A fallbacks per not-H1 run, out-of-SN fallbacks per phase.
FIT cnl:   (general games) CN-LAST hypothesis cases followed by a tau change, and control cases (level -1, non-cycle-node tail).
Usage: scope_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import scope_check as SC, frz_check as FC, frz_climb as FCL
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "scope":
        return 100 * m["max_scope_runs_per_phase"] + 60 * m["max_scope_case2_per_phase"] + 20 * m["max_WCH_per_phase"] + 20 * m["max_WCH_per_crossing_free_interval"] + 10 * m["max_h_runs_per_phase"]
    if fit == "fb":
        return 100 * m["max_fallbacks_per_crossing_free_run"] + 60 * m["max_NH1_fallbacks_per_phase"] + 60 * m["max_caseA_fallbacks_per_notH1_run"] + 40 * m["max_out_of_SN_fallbacks_per_phase"]
    if fit == "cnl":
        ctl = sum(v for k, v in c.items() if k.startswith("CNL_control"))
        return 200 * c["CNL_hyp_followed_by_tau_change"] + 20 * c["CNL_hypothesis_cases"] + 10 * ctl

def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        if fit == "cnl":
            A, fbs = SC.run_general(g, s, t, rng, r >= 2); SC.check_general(g, A, fbs, st, f"r{r}")
        else:
            A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); SC.check_run(g, o, A, fbs, st, f"r{r}")
    return fitness(st, fit), st

def gmutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n
    for _ in range(rng.randint(1, 3)):
        op = rng.random(); v = rng.randrange(n)
        if op < 0.3: prio[v] = rng.randrange(0, n + 1)
        elif op < 0.6: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
        elif op < 0.8:
            if len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif op < 0.9:
            if len(set(succ[v])) > 1: succ[v].pop(rng.randrange(len(succ[v])))
        else: owner[v] = 1 - owner[v]
    return RC.Game(prio, owner, succ)

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    o = None
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read())
        if fit != "cnl": o = FC.odd_vertex(g)
    elif fit == "cnl": g = SC.rand_general(rng, rng.randint(nmin, nmax))
    else: g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
    best, st = evaluate(g, o, fit, seed); t0 = time.time(); it = acc = 0; tot = FC.Stats()
    while time.time() - t0 < secs:
        it += 1
        if fit == "cnl": h = gmutate(g, rng)
        else:
            h = FCL.mutate(g, o, rng)
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
