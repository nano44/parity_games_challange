#!/usr/bin/env python3
"""REFEREE-2 hill climb for P-N5-U1: games with long U1 pieces, kappa_w changes inside U1 pieces, U1 pieces with fallbacks, many
CASC switches, tight CASC steps (step close to level - 2), and many w-changes under not-H2. Every scored run is fully checked by
u1_check (Lemma R on every S4a evaluation, TB, CASC, U1, WC); a violation is saved and stops the climb.
Usage: u1_climb.py steps seed outprefix initial.pg"""
import sys, os, random
import u1_check as U
RC = U.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
from collections import Counter

def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")

def score(g, o, seed):
    st = RC.Stats(); st.mx = Counter(); rng = random.Random(seed)
    for r in range(4):
        s, t = U.br_start(g) if r == 0 else RC.rand_start(rng, g)
        U.run_one(g, o, s, t, st, f"climb#{r}")
    c, m = st.c, st.mx
    f = (10 * m["U1_max_Rch"] + 25 * c["U1_kappa_w_change_transitions"] + 30 * c["U1_with_fallback"] + 2 * c["CASC_switches_U1"]
         + 15 * m["WC_max"] + 5 * max(m.get("CASC_max(step-level+2)", -10), -10) + c["TB_step2 x_on_play:True"])
    if os.environ.get("FIT") == "b":   # second objective: TB-odd cases, U1 pieces with fallbacks, kappa_w changes, x on play
        f = (50 * c["TB_odd"] + 80 * c["U1_with_fallback"] + 10 * c["U1_kappa_w_change_transitions"] + 5 * m["U1_max_Rch"]
             + c["LR_setopt_deleted_xney"] * 20)
    if os.environ.get("FIT") == "c":   # third objective: W-changes on R inside U1 pieces, K, U1 fallbacks, w-changes
        f = (40 * c["U1_W_change_transitions"] + 200 * m["U1_max_K"] + 100 * c["U1_with_fallback"] + 50 * m["WC_max"]
             + 3 * m["U1_max_Rch"] + 10 * sum(v for k, v in c.items() if k.startswith("WC_fallback")))
    return f, st

def main():
    steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
    rng = random.Random(seed)
    g = RC.parse(open(init).read()); o = U.one_odd(g)
    best, st = score(g, o, seed); tot = Counter(); nviol = 0
    print("start", best, flush=True)
    for i in range(steps):
        h = mutate(rng, g, o)
        if h is None: continue
        try: U.one_odd(h)
        except AssertionError: continue
        f, st = score(h, o, seed)
        for k, v in st.c.items(): tot[k] += v
        if st.c["VIOLATIONS"]:
            write_pg(h, f"{out}_VIOL_{i}.pg"); print("VIOLATION", st.viol[:5], flush=True); nviol += 1; break
        if f >= best:
            g = h
            if f > best:
                best = f; write_pg(g, f"{out}_best.pg")
                print(i, best, dict((k, st.mx[k]) for k in ("U1_max_Rch", "WC_max", "CASC_max(step-level+2)") if k in st.mx),
                      st.c["U1_kappa_w_change_transitions"], st.c["U1_with_fallback"], st.c["CASC_switches_U1"], flush=True)
    print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nviol else "OK", "violations", nviol)

if __name__ == "__main__":
    main()
