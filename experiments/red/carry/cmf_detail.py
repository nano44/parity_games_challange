#!/usr/bin/env python3
"""L-RED successor 3: anatomy of each (CM) case found by cmf.py: parent piece j-1 actual/ideal results, child contexts
(added/removed vertices), child actual round sets and deaths, all in ORIGINAL ids. Usage: DTL_ORDER=.. LALG_DIR=.. cmf_detail.py G.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cmf
sys.setrecursionlimit(100000)
cases, d = cmf.analyse(sys.argv[1]); o = lambda S: sorted(d.idx[v] for v in S)
byS = {}
for key, occ in d.calls.items():
    for (s, r, v, h, tl) in occ: byS[(s, key[0], key[1])] = (r, h, tl)
for c in cases:
    k = c["s"] - 1; a, b = d.trace[k], d.trace[k + 1]; j = c["j"]; pa, pb = a["pieces"], b["pieces"]
    print(f"== s{c['s']}->s{c['s']+1} player {a['p']} child j={j} M {c['Ma']}->{c['Mb']} death_drops={c['dd']}")
    for i in range(j + 1):
        x, y = pa[i], pb[i]
        print(f"  piece {i}: |ctx| {len(x[0])}->{len(y[0])} actual {x[1]} {o(x[2])} -> {y[1]} {o(y[2])} ; ideal {x[3]} {o(x[4])} -> {y[3]} {o(y[4])}")
    print(f"  child ctx removed {o(pa[j][0] - pb[j][0])} added {o(pb[j][0] - pa[j][0])}")
    for s, R in ((c['s'], pa[j][0]), (c['s'] + 1, pb[j][0])):
        r, h, tl = byS[(s, a['p'], R)]
        print(f"  s{s} child rounds (|V| per round) {[len(x) for x in r]}; alive tangles {len(tl)}; last nonempty {o([x for x in r if x][-1])}")
    ra = byS[(c['s'], a['p'], pa[j][0])][0]; rb = byS[(c['s'] + 1, a['p'], pb[j][0])][0]
    Da, Db = cmf.deaths(ra), cmf.deaths(rb)
    print("  deaths a/b on common vertices that changed:", {d.idx[v]: (Da[v], Db[v]) for v in set(Da) & set(Db) if Da[v] != Db[v]})
