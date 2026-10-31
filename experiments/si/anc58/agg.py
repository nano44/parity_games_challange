#!/usr/bin/env python3
"""L-SI box 58: sum / max the ANC counters of anc_sbcg.txt + anc_alt.txt (MAX* fields: max; others: sum)."""
import sys, re
tot, mx, games = {}, {}, 0
for f in sys.argv[1:]:
    for l in open(f):
        if " ANC " not in l: continue
        games += 1; t = l.split(" ANC ")[1].split()[3:]
        for a, b in zip(t[::2], t[1::2]):
            v = int(b)
            if a.startswith("MAX") or a == "LEVELS": mx[a] = max(mx.get(a, 0), v)
            else: tot[a] = tot.get(a, 0) + v
print("games", games, " ".join(f"{a} {b}" for a, b in tot.items()), " ".join(f"{a} {b}" for a, b in mx.items()))
