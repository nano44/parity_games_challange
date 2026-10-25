#!/usr/bin/env python3
"""REFEREE-2 succ. 7 (Opus 5.5, D15): hill-climb C^1O games against P-N5-FRZ with frz_check (own code). Mutations keep exactly one Odd
vertex with out-degree > 1 (asserted) and o reachable from its exits. Fitness FIT selects what to push:
  block : BLOCK S4a leaves inside r = l blocks (BLOCK non-vacuous), r = l blocks, crossings in ff blocks
  low   : freezes at levels -1 / bot, X-RUN level -1 segments, transitions after F(bot)
  leave : S4a leaves at (h) states after a freeze, at r = l, inside / at the exit of r = l blocks
  fb    : FREEZE later states across fallbacks / theta-changes / w-changes / not-(h) states; leaves at the transition leaving P; SUB re-entries
Any violation stops the climb and writes the instance. Usage: frz_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import frz_check as FC
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    if fit == "block":
        return 200 * c["BLOCK_S4a_leaves"] + 20 * c["BLOCK_blocks"] + 10 * m["BLOCK_max_crossings_in_ff_block"] + 3 * c["FREEZE_F_level_>=0"] + m["max_consecutive_h_over_n_x100"] / 10
    if fit == "leave":
        return (500 * c["BLOCK_S4a_leaves"] + 100 * c["BLOCK_S4a_leaves_at_block_exit (no claim)"] + 50 * c["LEAVE_S4a_(h)_after_F_with_r=l"]
                + 20 * c["LEAVE_S4a_(h)_after_F(l>=0)"] + c["BLOCK_blocks"] + m["max_consecutive_h_over_n_x100"] / 10)
    if fit == "low":
        return 100 * (c["FREEZE_F_level_bot"] + c["FREEZE_F_level_-1"]) + 50 * c["XRUN_segments_l=-1"] + 20 * c["XRUN_after_Fbot_transitions"] + 5 * c["XRUN_segments_l>=0"] + m["max_consecutive_h_over_n_x100"] / 5
    return (c["FREEZE_a_after_fallback"] + c["FREEZE_a_after_theta_change"] + 2 * c["FREEZE_a_after_w_change"] + 5 * c["FREEZE_a_after_not_h_state"]
            + 100 * c["XRUN_leaves_at_transition_leaving_P"] + 30 * c["SUB_iii_reentries"] + 10 * c["FREEZE_levels_with_F"] + m["max_consecutive_h_over_n_x100"] / 5)

def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed)
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2)
        FC.check_run(g, o, A, fbs, rng, st, f"r{r}")
    return fitness(st, fit), st

def ok(g, o):
    if [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1] != [o]: return False
    reach, stk = set(), list(g.succ[o])
    while stk:
        x = stk.pop()
        if x in reach: continue
        reach.add(x); stk.extend(g.succ[x])
    return o in reach

def mutate(g, o, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n
    for _ in range(rng.randint(1, 3)):
        op = rng.random(); v = rng.randrange(n)
        if op < 0.3: prio[v] = rng.randrange(0, n + 1)
        elif op < 0.6:
            if owner[v] == 1 and v != o: succ[v] = [rng.randrange(n)]
            else:
                i = rng.randrange(len(succ[v])); succ[v][i] = rng.randrange(n)
        elif op < 0.8:
            if owner[v] == 0 or v == o:
                if len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif op < 0.9:
            if (owner[v] == 0 or v == o) and len(set(succ[v])) > (2 if v == o else 1): succ[v].pop(rng.randrange(len(succ[v])))
        else:
            if v != o:
                if owner[v] == 0: owner[v] = 1; succ[v] = [rng.choice(succ[v])]
                else: owner[v] = 0
    return RC.Game(prio, owner, succ)

def dump(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
    else:
        g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
    best, st = evaluate(g, o, fit, seed); t0 = time.time(); it = acc = 0; tot = FC.Stats()
    while time.time() - t0 < secs:
        it += 1
        h = mutate(g, o, rng)
        if not ok(h, o): continue
        f, s2 = evaluate(h, o, fit, seed)
        tot.c["climb_evaluations"] += 1; tot.c["climb_runs"] += s2.c["runs"]
        for k, v in s2.c.items(): tot.c[k] += v
        for k, v in s2.mx.items(): tot.mx[k] = max(tot.mx[k], v)
        if s2.c["VIOLATIONS"]:
            dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            break
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)

if __name__ == "__main__":
    main()
