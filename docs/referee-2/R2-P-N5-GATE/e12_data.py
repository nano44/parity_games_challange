#!/usr/bin/env python3
# REFEREE-2 successor 38: reads the lane DATA that line L-5's E-1 / E-2 strings cite, by column name, from `git show COMMIT:…`.
# Files: experiments/si/box90/out/mw90.out, fw90.out; box91/out/own91.out, g391.out; box93/out/mwr93_own.out, mwr93_g3.out.
# A table is a header line «engine ENG instance COL …» followed by rows «ENG NAME.json VAL …». No lane code is imported or run.
# Usage: e12_data.py COMMIT        (run inside the repository)
import sys, subprocess
commit = sys.argv[1]; fails = 0
def show(p): return subprocess.run(["git", "show", f"{commit}:experiments/si/{p}"], capture_output=True, text=True, check=True).stdout
def added(p):
    o = subprocess.run(["git", "log", "--format=%h", commit, "--", f"experiments/si/{p}"], capture_output=True, text=True, check=True).stdout.split()
    return o[-1], o[0], len(o)
def tables(txt):                       # {(engine, instance): {col: value}}
    out = {}; cols = None
    for ln in txt.splitlines():
        w = ln.split()
        if len(w) > 3 and w[0] == "engine" and w[2] == "instance": eng = w[1]; cols = w[3:]; continue
        if cols and w and w[0] == eng and len(w) == len(cols) + 2: out[(eng, w[1].replace(".json", ""))] = dict(zip(cols, w[2:]))
    return out
def ck(n, ok, info=""):
    global fails; fails += not ok; print(("PASS " if ok else "FAIL ") + n + (" :: " + info if info else ""))
def want(tab, eng, inst, col, v):
    got = tab.get((eng, inst), {}).get(col); ck(f"{eng} {inst} {col} = {v}", got == str(v), f"got {got}")
mw, fw = tables(show("box90/out/mw90.out")), tables(show("box90/out/fw90.out"))
for p in ("box90/out/mw90.out", "box90/out/fw90.out"): print(p, "first / last commit, #commits:", added(p))
for e in ("own", "g3"):
    for inst, m, c in (("MW8_2", 8, 17), ("MW32_2", 32, 65)): want(mw, e, inst, "maxm", m); want(mw, e, inst, "C", c)
    for inst, p, d in (("FW8_2", 54, 8), ("FW16_2", 2583, 16)): want(fw, e, inst, "maxP", p); want(fw, e, inst, "depth", d); want(fw, e, inst, "C", 3)
F = [0, 1, 1]
while len(F) < 20: F.append(F[-1] + F[-2])
ck("F_10 − 1 = 54 and F_18 − 1 = 2583 (F_1 = F_2 = 1; d + 2 at d = 8, 16)", F[10] - 1 == 54 and F[18] - 1 == 2583, f"{F[10]} {F[18]}")
o91, g91 = tables(show("box91/out/own91.out")), tables(show("box91/out/g391.out"))
for e, t in (("own", o91), ("g3", g91)):
    for inst, c, fl in (("MW8_2", 17, 34), ("MW32_2", 65, 130)): want(t, e, inst, "C", c); want(t, e, inst, "maxflip", fl)
    for inst in ("FW8_2", "FW16_2"): want(t, e, inst, "C", 3)
ck("box 91 rows equal on the two engines", {k[1]: v for k, v in o91.items()} == {k[1]: v for k, v in g91.items()}, f"{len(o91)} rows")
print("box 91 maxa on MW8_2 / MW32_2 / FW16_2:", [o91[("own", i)]["maxa"] for i in ("MW8_2", "MW32_2", "FW16_2")], "(not A*_all: C 65 > 33)")
om, gm = tables(show("box93/out/mwr93_own.out")), tables(show("box93/out/mwr93_g3.out"))
for e, t in (("own", om), ("g3", gm)):
    for inst, fl, cd in (("MWR4_2", 9, 4), ("MWR8_2", 17, 8), ("MWR16_2", 33, 16)):
        want(t, e, inst, "mx_flips", fl); want(t, e, inst, "mx_ch_D", cd); want(t, e, inst, "mx_lam_pe", 0); want(t, e, inst, "mx_lam_pb", 0)
        r = t[(e, inst)]; ck(f"{e} {inst} flips = 2·ch_D + 1 and = 2·min(mx_ch_pe, mx_ch_pb) + 1", fl == 2 * cd + 1 == 2 * min(int(r["mx_ch_pe"]), int(r["mx_ch_pb"])) + 1,
                             f"mx_ch_pe {r['mx_ch_pe']} mx_ch_pb {r['mx_ch_pb']}")
ck("box 93 MWR rows equal on the two engines", {k[1]: v for k, v in om.items()} == {k[1]: v for k, v in gm.items()}, f"{len(om)} rows")
print("FAILS", fails)
