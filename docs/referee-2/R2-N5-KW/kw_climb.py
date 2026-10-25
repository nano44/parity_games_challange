#!/usr/bin/env python3
"""REFEREE-2 succ. 12: hill-climb against P-N5-KW with kw_check (own code; C^1O mutations of ../R2-N5-FRZ/frz_climb.py, as in
R2-N5-LV/lv_climb.py). Any violation stops the climb and dumps the game to climb/viol_<FIT>_<seed>.pg.
FIT kw:   toward post-freeze kind changes and c_w switches (KIND-MONO, CW-INT, E-SEG after f0), kind-B W-flat switches, freeze delay.
FIT casc: the same, plus CASC-B slack (switch step close to |pi_v| - 2).
Witnesses: climb/witness_{kindpost,cwpost}_<seed>.pg.
Usage: lv2_climb.py FIT seed nmin nmax seconds [seedgame.pg]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
for d in ("R2-N5-OUT", "R2-N5-ENT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(HERE, "..", d))
import out_check as OC, kw_check as EC, frz_check as FC, frz_climb as FCL
RC = FC.RC

def fitness(st, fit):
    c, m = st.c, st.mx
    # post-freeze kind changes / c_w switches (vacuous in the lane's data), then the pre-freeze ones, kind-B W-flat switches, freeze delay
    return (20000 * (c["RECORD_kind_change_after_freeze_cw_above"] + c["RECORD_cw_switches_after_freeze_cw_above"])
            + 2000 * (c["RECORD_kind_change_after_freeze"] + c["RECORD_cw_switches_after_freeze"])
            + 300 * (c["RECORD_kind_change_transitions_cw_above"] + c["RECORD_cw_switches_cw_above"]) + 50 * c["RECORD_runs_cw_above_notH2"]
            + 10 * (c["RECORD_kind_change_transitions"] + c["RECORD_cw_switches"]) + 20 * c["CASCB_kindB_switches"] + 50 * m["max_freeze_delay"]
            + 5 * c["ESEG_segments"]
            + (200 * max(0, m["CASCB_max_step_minus_bound_plus100"] - 95) if fit == "casc" else 0))

START = None   # the seed game's saved start pair (climb seed .txt), used as an extra run while it is valid for the mutated game

LAST = {}     # id(game) -> the start pairs evaluate() ran on it, as (label, mode, sigma0, tau0)

def evaluate(g, o, fit, seed):
    st = FC.Stats(); rng = random.Random(seed); runs = []
    if START and all(START[0][v] in g.succ[v] and START[1][v] in g.succ[v] for v in range(g.n)):
        runs.append(("start", "own", list(START[0]), list(START[1])))
        A, fbs = OC.run_trace(g, o, START[0], START[1], rng, "own"); EC.check_run(g, o, A, fbs, st, "own:start")
    for r in range(4):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        mode = "own" if r < 2 else "rand"
        runs.append((f"r{r}", mode, list(s), list(t)))
        A, fbs = OC.run_trace(g, o, s, t, rng, mode); EC.check_run(g, o, A, fbs, st, f"{mode}:r{r}")
    LAST[id(g)] = runs
    return fitness(st, fit), st

def dump(h, path):
    """the game, plus the start pairs evaluate() actually ran on it (the first one as sigma0 / tau0 for inst mode)"""
    FCL.dump(h, path)
    runs = LAST.get(id(h), [])
    with open(os.path.splitext(path)[0] + ".txt", "w") as fh:
        fh.write("start pairs evaluate() ran on this game, in order (label, trace); rand traces also depend on the rng\n")
        for lab, mode, s0, t0 in runs: fh.write(f"# {lab} {mode}: {s0} {t0}\n")
        if runs: fh.write(f"sigma0 = {runs[0][2]}\ntau0 = {runs[0][3]}\n")

def main():
    fit, seed, nmin, nmax, secs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    if len(sys.argv) > 6:
        g = RC.parse(open(sys.argv[6]).read()); o = FC.odd_vertex(g)
        sp = os.path.splitext(sys.argv[6])[0] + ".txt"
        if os.path.exists(sp):
            d = {}
            for line in open(sp):
                if line.startswith(("sigma0 =", "tau0 =")): k_, v_ = line.split("=", 1); d[k_.strip()] = eval(v_)
            if len(d) == 2:
                global START; START = (d["sigma0"], d["tau0"])
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
            dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg"))
            for v in s2.viol: print("VIOLATION", v)
            tot.c["VIOLATIONS"] += s2.c["VIOLATIONS"]; break
        for cls_ in ("kindpost", "cwpost"):
            wp = os.path.join(HERE, "climb", f"witness_{cls_}_{seed}.pg")
            key = {"kindpost": "RECORD_kind_change_after_freeze_cw_above", "cwpost": "RECORD_cw_switches_after_freeze_cw_above"}[cls_]
            if s2.c[key] and not os.path.exists(wp): dump(h, wp)
        if f >= best:
            if f > best: acc += 1
            g, best, st = h, f, s2
    dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best:.1f}")
    print("BEST-INSTANCE counters:", {k: v for k, v in sorted(st.c.items()) if v})
    print("BEST-INSTANCE maxima:", {k: v for k, v in sorted(st.mx.items()) if v})
    FC.report(tot)
if __name__ == "__main__": main()
