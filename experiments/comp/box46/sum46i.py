#!/usr/bin/env python3
"""L-COMP box 46, successor 22: summary of WORK item 1 (run46i.sh; climb46e.py seeded at BEST_B3_WU151_NM163_e934d333, objective W_ess /
(N + M)). Per climb log: seed line, every BEST (W_ess, N + M, ratio, T_key, must0, agree), ALERT count, evals, the final best; then, over
all bests of all logs, the maximum W_ess per N + M (the only growth data this item has). Columns of climb46e's log: «Wused» = W_ess,
«Wkey» = Wused, «run_used» = wess_max. Usage: sum46i.py  (reads out/climb46e_S*.log)"""
import os, re, glob
H = os.path.dirname(os.path.abspath(__file__)); per = {}
for p in sorted(glob.glob(os.path.join(H, "out", "climb46e_S*.log"))):
    L = open(p).read().splitlines(); b = [l for l in L if re.match(r"(ALERT )?BEST ", l)]
    print("%s: lines %d, BEST %d, ALERT %d, agree True %d, %s" % (os.path.basename(p), len(L), len(b), sum(1 for l in L if l.startswith("ALERT")),
          sum(1 for l in b if "agree True" in l), next((l for l in L if l.startswith("DONE")), "NOT DONE")))
    for l in L:
        if l.startswith("START"): print("    " + l)
    for l in b:
        m = re.search(r"BEST (\S+) Wused (\d+) NM (\d+) ratio (\S+) Tkey (\d+) Wkey (\d+) run_used (\d+) must0 (\d+)", l)
        f, we, nm, r, tk, wu, wm, m0 = m.groups(); ag = "agree True" in l
        print("    %s W_ess %s N+M %s ratio %s T_key %s Wused %s wess_max %s must0 %s agree %s" % (f, we, nm, r, tk, wu, wm, m0, ag))
        nm = int(nm); per[nm] = max(per.get(nm, 0), int(we))
print("max W_ess per N + M over all bests: " + " ".join("%d:%d" % kv for kv in sorted(per.items())))
