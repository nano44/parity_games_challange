#!/usr/bin/env python3
"""REFEREE-2 hill climb for P-N5-XA: C^1O games whose N5 runs have long throttled stretches, fallbacks inside them, re-entries
after S4a leaves (Theorem XA) and fallbacks with u* = none and an F->R gate edge (the FBL case of R2-N5-XA §3).
Fitness = XA_WN (env, default 0) * (S_ustar_none + 3 FB_in_S_ustar_none) + 0.2 thr_states + S_transitions + 5 FB_in_S + 20 XA re-entries after arena leaves + 30 F->R gate edges at fallbacks (u* none)
+ 100 FBL OTHER edges. Every scored run is fully checked (xa_check.check_run); a violation stops the climb.
Usage: xa_climb.py n steps seed outprefix [initial.pg]"""
import sys, os, random
import xa_check as xc
import re_climb_shim as sh
rc = xc.rc

WN = float(os.environ.get('XA_WN', '0'))

def score(g, o, seed, st):
    rng = random.Random(seed); tot = rc.Stats()
    for r in range(5):
        s, t = rc.rand_start(rng, g)
        if r == 4:
            s, t = rc.rand_start(random.Random(seed), g); states, fbs = rc.n5_spec(g, o, s, t)
        else:
            states, fbs = rc.n5_own(g, o, s, t, rng)
        xc.check_run(g, o, states, fbs, tot, "climb")
    for k, v in tot.c.items(): st.c[k] += v
    st.viol += tot.viol
    c = tot.c
    f = (0.2 * c["thr_states"] + c["S_transitions"] + WN * (c["S_ustar_none"] + 3 * c["FB_in_S_ustar_none"]) + 5 * c["FB_in_S"] + 20 * c["XA_reentry_after_arena_leave"] + 30 * c["gate_FR_at_fb(u*=none)"]
         + 100 * (c["FBL_OTHER(u*=none)"] + c["FBL_OTHER(u*=some)"]))
    return f, tot

def main():
    n, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); st = rc.Stats()
    if len(sys.argv) > 5:
        g = rc.parse(open(sys.argv[5]).read()); o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
    else:
        g, o = rc.rand_game(rng, n)
    best, bt = score(g, o, seed, st)
    for i in range(steps):
        h = sh.mutate(rng, g, o)
        if h is None: continue
        f, t = score(h, o, seed, st)
        if st.viol: print("VIOLATION", st.viol[:5]); break
        if f >= best:
            if f > best: print(f"step {i}: fitness {f} " + " ".join(f"{k}={t.c[k]}" for k in ("S_transitions", "FB_in_S",
                               "XA_reentry_after_arena_leave", "gate_FR_at_fb(u*=none)", "FBL_OTHER(u*=none)")), flush=True)
            g, best, bt = h, f, t
    with open(out + ".pg", "w") as fh:
        fh.write(f"parity {g.n - 1};\n")
        for v in range(g.n): fh.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    print("FINAL", best, {k: bt.c[k] for k in sorted(bt.c) if k.startswith(("S_", "FB", "XA", "gate", "Pc"))})
    print("over the climb:", st.c["runs"], "runs,", st.c["S_stretches"], "stretches,", st.c["S_transitions"], "stretch transitions,",
          st.c["FB_in_S"], "fallbacks in S,", st.c["XA_reentry_after_arena_leave"], "XA re-entries,", st.c["Pc_checks"], "P^c checks,",
          st.c["gate_FR_at_fb(u*=none)"], "F->R gate edges (u* none),", st.c["FBL_OTHER(u*=none)"], "FBL other (u* none)")
    print("RESULT", "FAIL" if st.viol else "OK", f"violations={len(st.viol)}")

if __name__ == "__main__":
    main()
