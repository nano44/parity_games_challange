#!/usr/bin/env python3
"""L-RED successor 31 (R123 §4): CARRY-SEG-S attack. Input: an obs2.py game built with OWNER=0 ABOVE=a (Even observer o, label "obs",
o -> y_j -> r_j, q_j just above the reactor a-markers). Gives each b_j (mkr's Odd b-link r_j -> b_j -> h') an odd marker beta_j,
decreasing in j and inserted between the a-markers and the q_j (all priorities >= q_1 move up by 2m; parities and order kept). Then the observer's change at
the reactor flip adds two odd ranks (nu_(i+1), beta_m) against one higher odd rank leaving (eta_(i+1)): a carry, like every wave step.
Adds Even e (priority 0) -> {o, d}, d (Odd, priority 0) -> yd (Odd, even marker q_d just above q_m) -> h', start sigma(e) = o.
q_d is needed because N5's Even step is a best response in the restricted game: at the h'-step the reactors flip in the same step, so
W(o) already carries q_m + beta_m + W(h'); q_d > q_m makes d W-better there. e leaves o at each h'-step and re-enters at the first wave
step (Xi(o) = q_1 + a_1 + H beats q_d + V by the ladder), so span(e, o) covers the run.
Usage: carryobs.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re
src, sst, out, ost = sys.argv[1:5]
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
    lab[m.group(5)] = int(m.group(1))
m = sum(1 for l in lab if l and re.fullmatch(r"y\d+", l))
amax = max(r[1] for r in rows if re.fullmatch(r"a\d+", r[4])); q1 = rows[lab["y1"]][1]; assert q1 == amax + 1, (q1, amax)
for r in rows:
    if r[1] >= q1: r[1] += 2 * m
for j in range(1, m + 1): rows[lab[f"b{j}"]][1] = amax + 2 * (m + 1 - j)   # beta_j: odd, amax < beta_m < ... < beta_1 < q_1 (decreasing: an unflipped r_(j-1) keeps r_j on b)
o, hp = lab["obs"], lab["hp"]; e, d, yd = len(rows), len(rows) + 1, len(rows) + 2
qd = rows[lab[f"y{m}"]][1] + 2; assert all(r[1] != qd for r in rows)
rows.append([e, 0, 0, [o, d], "e"]); rows.append([d, 0, 1, [yd], "d"]); rows.append([yd, qd, 1, [hp], "yd"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, pr, ow, su, l in rows: f.write(f'{v} {pr} {ow} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("SIGMA0"): l += f" {e}:{o}"
        if l.startswith("TAU0"): l += f" {d}:{yd} {yd}:{hp}"
        f.write(l + "\n")
print(f"carryobs: n {len(rows)} e {e} o {o} d {d} yd {yd}")
