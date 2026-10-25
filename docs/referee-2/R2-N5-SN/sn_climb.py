#!/usr/bin/env python3
"""REFEREE-2 succ. 6 hill climb against P-N5-SN. FIT=absc: max over fallback-free runs of eps_H1 - REL_run - (d_o - 1) (target > 0, the
packet's ABS-COUNT form), then #H1 eps; FIT=leave: H1 leaves (LEAVE) with tight cases weighted; FIT=stick: crossings after the c_w = c_theta
prefix (R-STICK / SN-PREFIX). Every scored run (S3 start + 3 random starts) is fully checked by sn_check; a violation is saved and stops the
climb; an ABS-COUNT packet-form failure is saved as _ABSC_<i>.pg (it is not a violation of the d_o form). Usage: sn_climb.py steps seed out init.pg"""
import sys, os, random
from collections import Counter
import sn_check as C
F = C.F; RC = F.RC
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
from re_climb import mutate
def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
def score(rg, o, seed):
    g = F.to_lpg(rg); st = F.Stats(); st.ex = {}; rng = random.Random(seed)
    for r in range(4):
        s, t = F.start(g, rng, r > 0); C.check_run(g, s, t, st, f"c#{r}", o, rng)
    c, m = st.c, st.mx; fit = os.environ.get("FIT", "absc")
    if fit == "absc": f = 100 * (m.get("max(eps_H1-REL_run-(d_o-1))+100", 0) - 100) + c["OR_eps_H1"]
    elif fit == "leave": f = c["LEAVE_checks(H1)"] + 5 * c["LEAVE_tight(path max = r)"]
    else: f = 10 * m["max_crossings_after_prefix"] + c["PREFIX_crossings_after"]
    return f, st
steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
rng = random.Random(seed); g = RC.parse(open(init).read()); o = F.one_odd(F.to_lpg(g))
best, st = score(g, o, seed); tot = Counter(); nv = 0; nabs = 0
print("start", best, flush=True)
for i in range(steps):
    h = mutate(rng, g, o)
    if h is None: continue
    try: F.one_odd(F.to_lpg(h))
    except AssertionError: continue
    f, st = score(h, o, seed)
    for k, v in st.c.items(): tot[k] += v
    if st.c["VIOLATIONS"]:
        write_pg(h, f"{out}_VIOL_{i}.pg"); print("VIOLATION", st.viol[:5], flush=True); nv += 1; break
    if st.c["ABSC_packet_bound_fails(eps_H1 > d_o-1+REL_run)"] and nabs < 3:
        write_pg(h, f"{out}_ABSC_{i}.pg"); print("ABSC", i, st.ex.get("absc"), flush=True); nabs += 1
    if f >= best:
        g = h
        if f > best:
            best = f; write_pg(g, f"{out}_best.pg"); print(i, best, flush=True)
print("TOTALS", dict(tot)); print("RESULT", "FAIL" if nv else "OK", "violations", nv, "absc_saved", nabs)
