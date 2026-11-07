#!/usr/bin/env python3
"""L-LOWER 4 fast regression (BOX L4; run by experiments/lower/check.sh, < 60 s).
1. DRV-RELAX: the driven block (drvpath.py's transition, written separately from l3/sim.py) reproduces the run of levels >= 1 of
   REC_d10_tower_mu30 and RECT_d13_T99 state for state with e(t) = c_1(s_t) (blk.py export); the block DP values of docs §1.
2. DOUBLE-EQ', FROZEN-WINDOW and LATE-PREF (docs/lower/L4-tower.md §3, §4, §4b): fwcheck.py, 0 violations on the kill/ records, the L4 records and
   200 random hypothesis-rich genomes (all starts).
3. L4 records: sha1 pins, T and F(4) by l3/sim.py."""
import os, sys, json, hashlib, subprocess
H = os.path.dirname(os.path.abspath(__file__)); L3 = os.path.join(H, "..", "l3")
sys.path.insert(0, L3)
from sim import run
from trace import keys
def sh(c, env=None):
    e = dict(os.environ); e.update(env or {})
    return subprocess.run(c, shell=True, cwd=H, capture_output=True, text=True, env=e, check=True).stdout
import tempfile
tmp = tempfile.mkdtemp()
for g, Texp in (("REC_d10_tower_mu30", 35), ("RECT_d13_T99", 99)):
    gp = os.path.join(L3, "kill", g + ".json"); gen = os.path.join(tmp, g + ".gen")
    e = sh(f"python3 -I blk.py {gp} {gen}").strip()
    G = json.load(open(gp)); S = run(G, G["start"]); assert len(S) - 1 == Texp
    # replay with the Python driven block (drvpath.py's step) along e
    import importlib.util
    src = open(os.path.join(H, "drvpath.py")).read().split("@lru_cache")[0]
    ns = {}; sys.argv = ["drvpath.py", gen, "0"]; exec(compile(src, "drvpath", "exec"), ns)
    s = ns["s0"]
    for t in range(1, len(S)):
        s = ns["step"](s, int(e[t - 1])); assert s == tuple(S[t][2:]), (g, t)
    print(f"DRV-RELAX replay {g}: {len(S) - 1} steps state-identical")
out = sh("python3 -I fwcheck.py " + " ".join(os.path.join(L3, "kill", f) for f in sorted(os.listdir(os.path.join(L3, "kill"))) if f.endswith(".json"))
         + " rec/RECF4_d14_F52.json rec/RECF4_d16_F53.json rec/RECF4_d20_F56.json", {"RANDOMCROSS": "200"})
w = dict(zip(out.split()[0::2], map(int, out.split()[1::2])))
assert w["late_viol"] == 0 and w["late_windows"] > 0 and w["eq_viol"] == 0 and w["fw_viol"] == 0 and w["adj_viol"] == 0 and w["dbl_levels"] > 0, out
print("DOUBLE-EQ'/FROZEN-WINDOW:", out.strip())
PIN = {"RECF4_d14_F52.json": ("PIN14", 73, 52), "RECF4_d16_F53.json": ("PIN16", 73, 53), "RECF4_d20_F56.json": ("PIN20", 71, 56)}
for f, (pin, Texp, F4) in PIN.items():
    p = os.path.join(H, "rec", f); G = json.load(open(p)); S = run(G, G["start"])
    O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(G["N"] // 2)] for k in (keys(G, s) for s in S)]
    F = [sum(O[t][l] != O[t-1][l] for t in range(1, len(S))) for l in range(G["N"] // 2)]
    assert len(S) - 1 == Texp and F[4] == F4, (f, len(S) - 1, F)
    print(f"{f}: sha1 {hashlib.sha1(open(p, 'rb').read()).hexdigest()[:8]} T {Texp} F {F}")
print("L4 CHECK PASS")
