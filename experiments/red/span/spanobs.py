#!/usr/bin/env python3
"""L-RED successor 31 (R123): a leave/re-enter switcher on R120's wave observer. Input: an obs2.py game (mkr + Odd observer o,
label "obs"). Adds an Even e (priority 0, no in-edges) with edges {o, d} and d (Odd, priority 0, single successor hp = mkr's pivot h').
Start sigma(e) = o. Xi(d) = Xi(h'); Xi(o) = min_j q_j + Xi(r_j). When h' rises (V_i), the reactors still carry H_i, so d beats o and e
LEAVES o; after the flip o = q_j + V_i beats d and e RE-ENTERS o. So e leaves and re-enters o once per pivot cycle, and span(e, o) covers
the run: every P-change of the observer o lies in the span. e and d reach only o and h', so the sigma-run of mkr is unchanged.
The W step (Even's choice against tau among improving switches) needs W(d) > W(o) at a leave and W(o) > W(d) at a re-entry, and
W >= Xi everywhere, so o gets a W-route yh -> h (tau(o) = yh, marker q_h above every q_j, so Xi(o) is still the reactor minimum): then
e's W comparison is h against h', the same one the reactors make.
Usage: spanobs.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re
src, sst, out, ost = sys.argv[1:5]
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
    lab[m.group(5)] = int(m.group(1))
o, hp, h = lab["obs"], lab["hp"], lab["h"]; e, d, yh = len(rows), len(rows) + 1, len(rows) + 2
Z = rows[lab["z"]][1]; m = sum(1 for l in lab if l and re.fullmatch(r"y\d+", l))
rows.append([e, 0, 0, [o, d], "e"]); rows.append([d, 0, 1, [hp], "d"])
rows.append([yh, Z - 1 + 2 * (m + 1), 1, [h], "yh"]); rows[o][3].append(yh)   # o's W-route (tau(o) = yh): W(o) = W(h)
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, pr, ow, su, l in rows: f.write(f'{v} {pr} {ow} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("SIGMA0"): l += f" {e}:{o}"
        if l.startswith("TAU0"): l = re.sub(rf"(?<= ){o}:\d+", f"{o}:{yh}", l) + f" {d}:{hp} {yh}:{h}"
        f.write(l + "\n")
print(f"spanobs: n {len(rows)} e {e} o {o} d {d} yh {yh}")
