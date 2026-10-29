#!/usr/bin/env python3
"""REFEREE succ. 17 (SDPRIME §C, SDP-N2): W-MONO (W_{t+1} >= W_t pointwise) and Xi-SUCC (Xi_{t+1}(sigma_{t+1} v) >= Xi_t(sigma_t v), Even v)
at in-phase S4a transitions (no fallback) where lambda_W changes. Own engine. Usage: lw_facts.py list FILE BASE | files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, epr_probe as E, core_probe as CP
cnt = Counter()
def run(g, s0):
    st = RE.run(g, s0); n = g.n
    W = [E.wval(g, x["s"], x["t"]) for x in st]
    for t in range(len(st) - 1):
        x0, x1 = st[t], st[t + 1]
        if x0["fb"] or x0["t"] != x1["t"] or [v[0] for v in x0["Xi"]] != [v[0] for v in x1["Xi"]]: continue
        lw = [w[0] for w in W[t]] != [w[0] for w in W[t + 1]]
        tag = "lw" if lw else "const"
        cnt["trans_" + tag] += 1
        if any(g.key(W[t + 1][v]) < g.key(W[t][v]) for v in range(n)): cnt["WMONO_FAIL_" + tag] += 1
        if any(g.owner[v] == 0 and g.key(x1["Xi"][x1["s"][v]]) < g.key(x0["Xi"][x0["s"][v]]) for v in range(n)): cnt["XSUCC_FAIL_" + tag] += 1
a = sys.argv[1:]
if a[0] == "list":
    for l in open(a[1]):
        p = l.split()
        g = RE.parse(os.path.join(a[2], p[0]))
        if g.n > 600: continue
        ex = CP.parse_start(g, os.path.join(a[2], p[1])) if len(p) > 1 else None
        run(g, ex or RE.best_reward_start(g))
else:
    for f in a:
        g = RE.parse(f)
        if g.n > 48: continue
        run(g, RE.best_reward_start(g))
for k in sorted(cnt): print(k, cnt[k])
