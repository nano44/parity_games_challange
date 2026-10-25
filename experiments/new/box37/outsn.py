#!/usr/bin/env python3
"""Box 37 (b): out-of-SN stretches of N5 on C^1O (docs/new/N5-OUT-box37.md). An OUT state is an in-phase state with H1 and c_w != c_θ
(H1 ∧ ¬H2, or H1 ∧ H2 ∧ ¬H3). An OUT STRETCH is a maximal run of consecutive OUT states of one phase. Per stretch: transitions, S4a / S4c,
crossings, entries / exits of R, RE-ENTRIES (v enters R after having left R earlier in the same phase), whether τ(o) = o, and for every
re-entry whether Ξ(v) at re-entry is strictly above Ξ(v) at the state before its last exit (checked; lane claim EXIT-UP). Per phase:
OUT fallbacks f_out (fallback at an OUT state), and the same counts. Usage: outsn.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box32")); sys.path.insert(0, os.path.join(HERE, "..", "box33"))
sys.path.insert(0, os.path.join(HERE, "..", "box25"))
from dormant import *
from scopecov import h2
from common import rand_c1o

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def analyse(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); E = Engine(g); N = len(rows)
    H2 = [h2(r["nxt"], o) for r in rows]
    out = [r["h1"] and r["cw"] != r["Xi"][o][0] for r in rows]
    k = 0
    while k < N:
        j = k
        while j + 1 < N and rows[j + 1]["ph"] == rows[k]["ph"]: j += 1
        # phase = states k..j
        left = {}          # v -> state index before its last exit
        fout = reent = 0; st = None
        for s in range(k, j + 1):
            if s < j:
                R0, R1 = set(rows[s]["R"]), set(rows[s + 1]["R"])
                for v in R0 - R1: left[v] = s
                if out[s]:
                    if st is None: st = dict(a=s, tr=0, fb=0, s4a=0, x=0, ent=0, ex=0, re=0, too=rows[s]["nxt"][o] == o, h2=H2[s])
                    st["tr"] += 1; fb = rows[s]["fb"]; st["fb"] += fb; st["s4a"] += 1 - fb; fout += fb
                    if R0 != R1: st["x"] += 1
                    st["ent"] += len(R1 - R0); st["ex"] += len(R0 - R1)
                    if fb and R1 - R0: bump(acc, "OUT_fb_with_entry")
                    if not fb and R0 - R1: bump(acc, "OUT_s4a_with_exit")
                    for v in R1 - R0:
                        if v in left:
                            st["re"] += 1; reent += 1; a = left[v]
                            up = E.key(rows[s + 1]["Xi"][v]) > E.key(rows[a]["Xi"][v])
                            bump(acc, "reentry_XiUP" if up else "reentry_XiNOTUP")
                            bump(acc, "reentry_active" if rows[s]["s"][v] != rows[s + 1]["s"][v] else "reentry_passive")
            if st is not None and (s == j or not out[s + 1] or s + 1 > j):
                bump(acc, "stretches"); bump(acc, "stretches_tauo_o" if st["too"] else "stretches_tauo_other")
                for f in ("tr", "fb", "s4a", "x", "ent", "ex", "re"): bump(acc, "sum_" + f, st[f])
                mx(acc, "max_stretch_fb", st["fb"], g.n, st["re"], st["too"], name, st["a"])
                mx(acc, "max_stretch_re", st["re"], g.n, st["fb"], st["too"], name, st["a"])
                if st["too"]: mx(acc, "max_stretch_fb_tauo_o", st["fb"], g.n, st["re"], name, st["a"])
                st = None
        mx(acc, "max_phase_fout", fout, g.n, reent, name, k)
        mx(acc, "max_phase_reentries_out", reent, g.n, fout, name, k)
        bump(acc, "phases")
        k = j + 1
    return acc

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for d in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is not None: analyse(g, acc, f"rand{seed}_{d}")
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: bump(acc, "skipped_not_C1O"); continue
            analyse(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
