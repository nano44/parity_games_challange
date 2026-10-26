#!/usr/bin/env python3
"""Box 9 (Lead GO 2026-10-26 01:53Z): hill climbs that make the checks vacuous in box 8 non-vacuous, every scored run fully checked by the
referees' checkers UNMODIFIED (REFEREE-2 oe_check, cls_check, sn_check, h1_check.check_run; a violation is saved and stops the climb).
Mutation: REFEREE-2 re_climb.mutate (unmodified; keeps exactly one Odd vertex with out-degree > 1). Each score = 4 runs (canonical start
+ 3 seeded random starts, fb_check.start), as REFEREE-2's cls_climb.
FIT (own):
  wk   1000 * WK_checks + 10 * wakes + K_total  (sn_check: wakes, and WK's hypothesis: y not its own W-cycle node, W unchanged at a and z)
  cls  20 * CLS1_case_r>L + 3 * CLS1_checks + scope_fallbacks_THR_u*!=none  (= REFEREE-2 cls_climb FIT=gt) + 0.1 scope_fallbacks + 0.01 fallbacks, at FIXED n
  absl 100 * ABSL_theta_changes_above_L + ABSL_intervals
Usage: climb9.py FIT steps seed OUTPREFIX (INIT.pg | rand:N)"""
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("docs/referee-2/R2-N5-OE", "docs/referee-2/R2-N5-CLS", "docs/referee-2/R2-N5-SN", "docs/referee-2/R2-N5-RE"):
    sys.path.insert(0, os.path.join(ROOT, p))
import oe_check  # noqa: E402
import cls_check  # noqa: E402
import sn_check  # noqa: E402
import h1_check  # noqa: E402
from re_climb import mutate  # noqa: E402

F = oe_check.F; RC = F.RC


def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n):
            f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")


def score(rg, o, seed, fit):
    g = F.to_lpg(rg); rng = random.Random(seed); S = {k: F.Stats() for k in ("OE", "CLS", "SN", "H1")}
    for r in range(4):
        s, t = F.start(g, rng, r > 0)
        oe_check.check_run(g, s, t, S["OE"], f"oe#{r}", o)
        cls_check.check_run(g, s, t, S["CLS"], f"cls#{r}", o, rng)
        sn_check.check_run(g, s, t, S["SN"], f"sn#{r}", o, rng)
        h1_check.check_run(g, s, t, S["H1"], f"h1#{r}", o)
    c = Counter()
    for st in S.values():
        c.update(st.c)
    if fit == "wk":
        f = 1000 * c["WK_checks"] + 10 * c["wakes"] + c["K_total"]
    elif fit == "cls":
        f = 20 * c["CLS1_case_r>L"] + 3 * c["CLS1_checks"] + c["scope_fallbacks_THR_u*!=none"] + 0.1 * c["scope_fallbacks"] + 0.01 * c["f_total"]
    else:
        f = 100 * c["ABSL_theta_changes_above_L"] + c["ABSL_intervals"]
    viol = [m for st in S.values() for m in st.viol]
    return f, c, viol


def main():
    fit, steps, seed, out, init = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
    rng = random.Random(seed)
    if init.startswith("rand:"):
        g, o = RC.rand_game(rng, int(init[5:]), cyc=True)
    else:
        g = RC.parse(open(init).read()); o = F.one_odd(F.to_lpg(g))
    best, c, viol = score(g, o, seed, fit); tot = Counter(c)
    print("start", best, dict((k, c[k]) for k in ("WK_checks", "wakes", "CLS1_checks", "CLS1_case_r>L", "ABSL_intervals")), flush=True)
    for i in range(steps):
        h = mutate(rng, g, o)
        if h is None:
            continue
        try:
            if F.one_odd(F.to_lpg(h)) != o:
                continue
            f, c, viol = score(h, o, seed + i, fit)
        except AssertionError:
            continue
        tot.update(c)
        if viol:
            write_pg(h, out + "_VIOLATION.pg"); print("VIOLATION", viol[:5], flush=True); break
        if f >= best:
            if f > best:
                print(i, f, dict((k, c[k]) for k in ("WK_checks", "wakes", "CLS1_checks", "CLS1_case_r>L", "ABSL_intervals")), flush=True)
            best, g = f, h
            write_pg(g, out + "_best.pg")
    print("TOTALS", {k: v for k, v in sorted(tot.items()) if "C567" not in k}, flush=True)
    print("RESULT", "VIOLATION" if viol else "OK", "best", best, flush=True)


if __name__ == "__main__":
    main()
