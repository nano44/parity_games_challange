#!/usr/bin/env python3
"""L-SI box 104, duty (b): summary of replay209.sh's outputs (box 209's counters on this lane's 26 frozen instances under L-RED 65's
HOW3 engine). Exit 1 unless both files have 26 rows, every must-0 counter is 0, LV_CTRL=2 fires on its 3 rows and PL_CTRL=1 on the 4 rows with plateaus.
level208.py's 16 must-0 counters: monofail k3fail k4fail k5fail einF l3fail phifail stallnocyc nofvs rstall boundfail winstall wbeta
wl3fail wmid wbound (the last seven with nofvs / rstall are box 208's feedback-set statements read on Gamma3: DATA only in box 209).
plat209.py's 9: p1 pclos p2 p3 p4 p5 t1 t2 t3. Usage: replay209sum.py"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); O = lambda f: open(os.path.join(HERE, "out", f)).read().splitlines()
L16 = ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "nofvs", "rstall", "boundfail", "winstall", "wbeta", "wl3fail", "wmid", "wbound")
P9 = ("p1", "pclos", "p2", "p3", "p4", "p5", "t1", "t2", "t3")
def kv(l):
    t = l.split(); return {t[i]: int(t[i + 1]) for i in range(len(t) - 1) if re.fullmatch(r"-?\d+", t[i + 1]) and not re.fullmatch(r"-?\d+", t[i])}
lev = [kv(l) for l in O("replay209_level.out") if " monofail " in l]; pla = [kv(l) for l in O("replay209_plat.out") if " pclos " in l]
s1 = {k: sum(r.get(k, 0) for r in lev) for k in L16}; s2 = {k: sum(r.get(k, 0) for r in pla) for k in P9}
ks = sorted(set(r["k"] for r in lev))
print(f"REPLAY209 level208.py --hist: rows {len(lev)}; sum of the 16 must-0 counters {sum(s1.values())}" + ("" if not sum(s1.values()) else f" {s1}")
      + f"; k in {ks}; max T3 {max(r['T'] for r in lev)}; max levels {max(r['levels'] for r in lev)}; max Phi values {max(r['phivals'] for r in lev)}; "
        f"stalls {sum(r['stalls'] for r in lev)} (loud {sum(r['stallloud'] for r in lev)}); plateaus {sum(r['plat'] for r in lev)} (longest {max(r['platmax'] for r in lev)})")
print(f"REPLAY209 plat209.py --hist: rows {len(pla)}; sum of the 9 must-0 counters {sum(s2.values())}" + ("" if not sum(s2.values()) else f" {s2}")
      + f"; plateaus {sum(r['plateaus'] for r in pla)}; longest {max(r['maxlen'] for r in pla)}; longest tail {max(r['tail'] for r in pla)}; max T3 {max(r['T'] for r in pla)}")
lvfire = plfire = lvrows = 0
for l in O("replay209_ctrl.out"):
    d = kv(l); fired = {k: v for k, v in d.items() if k in L16 + P9 and v}
    if l.startswith("LV_CTRL"): lvrows += 1; lvfire += bool(fired)
    else: plfire += bool(fired)
    print("REPLAY209 control " + " ".join(l.split()[:4]) + ": fires " + (", ".join(f"{k} {v}" for k, v in fired.items()) or "NOTHING"))
print(f"REPLAY209 controls: LV_CTRL=2 fires on {lvfire} of {lvrows} rows; PL_CTRL=1 fires on {plfire} rows (the 4 with plateaus)")
sys.exit(0 if len(lev) == 26 and len(pla) == 26 and not sum(s1.values()) and not sum(s2.values()) and lvrows == 3 == lvfire and plfire == 4 else 1)
