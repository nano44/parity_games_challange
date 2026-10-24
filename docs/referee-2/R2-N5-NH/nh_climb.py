#!/usr/bin/env python3
"""REFEREE-2 hill climb for P-N5-NH: games with long P3' pieces (rank c_theta > c_w, both frames in route form), S4a steps there
under not H2, and single-switch checks with x on o's W-cycle (the G-NH-1 configuration). Every scored run is fully checked by
nh_check.check_run; a violation stops the climb. Fitness = 10 P3_transitions + 30 G-NH-1 on-cycle checks + 5 S4a steps under not H2
+ pieces_ct_above_cw. Usage: nh_climb.py n steps seed outprefix [initial.pg]"""
import sys, os, random
import nh_check as nc
rc = nc.rc
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate

def score(g, o, seed, st):
    rng = random.Random(seed); tot = rc.Stats()
    for r in range(5):
        s, t = rc.rand_start(rng, g)
        if r == 4: s, t = rc.rand_start(random.Random(seed), g); states, fbs = rc.n5_spec(g, o, s, t)
        else: states, fbs = rc.n5_own(g, o, s, t, rng)
        nc.check_run(g, o, states, fbs, tot, "climb")
    for k, v in tot.c.items(): st.c[k] += v
    st.viol += tot.viol; c = tot.c
    return (10 * c["P3_transitions"] + 30 * c["G-NH-1_single_switch_checks_x_on_W_cycle"] + 5 * c["G-NH-1_S4a_steps_notH2"]
            + c["pieces_ct_above_cw"]), tot

def main():
    n, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); st = rc.Stats()
    if len(sys.argv) > 5:
        g = rc.parse(open(sys.argv[5]).read()); oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]; assert len(oc) == 1, f'not C^1O: Odd choice vertices {oc}'; o = oc[0]
    else:
        g, o = rc.rand_game(rng, n)
    best, bt = score(g, o, seed, st)
    for i in range(steps):
        h = mutate(rng, g, o)
        if h is None: continue
        f, t = score(h, o, seed, st)
        if st.viol: print("VIOLATION", st.viol[:5]); break
        if f >= best:
            if f > best: print(f"step {i}: fitness {f}", flush=True)
            g, best, bt = h, f, t
    with open(out + ".pg", "w") as fh:
        fh.write(f"parity {g.n - 1};\n")
        for v in range(g.n): fh.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    keys = ("P3_transitions", "P3_pieces_nontrivial", "G-NH-1_S4a_steps_notH2", "G-NH-1_single_switch_checks",
            "G-NH-1_single_switch_checks_x_on_W_cycle", "G-NH-1_R*_arena_not_optimal(notH2)", "R3_checks", "runs")
    print("FINAL", best, {k: bt.c[k] for k in keys})
    print("over the climb:", {k: st.c[k] for k in keys})
    print("RESULT", "FAIL" if st.viol else "OK", f"violations={len(st.viol)}")

if __name__ == "__main__":
    main()
