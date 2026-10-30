#!/usr/bin/env python3
"""L-SI box 51b: aggregate gate.py outputs: max of per-run maxima (key MAX_*), sums of the other counters, games with output, and the
game attaining each maximum. Usage: agg.py FILE..."""
import sys
MX = {'ZFL', 'SUB', 'PR', 'WCI', 'FLAT', 'XFL', 'FLI', 'TXC', 'TXV', 'XCV', 'DMAX'}
tot, arg, games, bad = {}, {}, 0, 0
for f in sys.argv[1:]:
    for l in open(f):
        w = l.split()
        if 'GATE' not in w: bad += 1; continue
        i = w.index('GATE'); name = w[i + 1]; kv = dict(zip(w[i + 4::2], map(int, w[i + 5::2]))); games += 1
        for k, v in kv.items():
            if k in MX:
                if v > tot.get(k, -1): tot[k], arg[k] = v, name
            else: tot[k] = tot.get(k, 0) + v
print(f"games {games} no-output {bad}")
for k, v in tot.items(): print(f"{k} {v}" + (f" ({arg[k]})" if k in MX else ""))
