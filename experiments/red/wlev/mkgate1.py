#!/usr/bin/env python3
"""L-RED R154: a SHARED-GATE selector on a real quadratic supply. Input: an n5b game + start whose vertex OBS (an observer, Xi rising
many times in one W-run) and vertex MV (a fixed-valued marker on every value of OBS) are given. Priorities are rescaled p -> 4p + (p % 2)
(parity and order kept, gaps opened). Added: Even h (priority 0) -> l_1 .. l_K; Odd l_j (priority 0) -> {lam_j (tau), OBS}; lam_j (Odd,
priority 0) -> m_j -> MV, m_j odd priority 4 a_j + 3 just above the rescaled odd priority a_j. So Xi(l_j) = min(Lambda_j, Xi(OBS)) with
Lambda_j = (., {m_j, MV, ...}, .) static, and the gate on l_j opens when OBS's second-most-relevant odd vertex drops to <= a_j.
Levels: a_1 > a_2 > ... (l_K the W-best). Start: sigma(h) = l_1, tau(l_j) = lam_j. OBS may be a comma list of r signal vertices: level j escapes to OBS[j mod r] (round robin).
Usage: mkgate1.py IN.pg IN.start OBS[,OBS2,...] MV a_1,a_2,... OUT"""
import sys, re
src, sst, OBSL, MV, AS, out = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")], int(sys.argv[4]), [int(x) for x in sys.argv[5].split(",")], sys.argv[6]
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
rows.sort(); n = len(rows); assert [r[0] for r in rows] == list(range(n))
for r in rows: r[1] = 4 * r[1] + (r[1] % 2)
K = len(AS); h = n; L = [n + 1 + j for j in range(K)]; LAM = [n + 1 + K + j for j in range(K)]; MM = [n + 1 + 2 * K + j for j in range(K)]
rows.append([h, 0, 0, L, "h"])
for j in range(K):
    rows.append([L[j], 0, 1, sorted([LAM[j], OBSL[j % len(OBSL)]]), f"l{j+1}"])
for j in range(K):
    rows.append([LAM[j], 0, 1, [MM[j]], f"lam{j+1}"])
for j in range(K):
    rows.append([MM[j], 4 * AS[j] + 3, 1, [MV], f"m{j+1}"])
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for r in rows: f.write(f'{r[0]} {r[1]} {r[2]} {",".join(map(str, r[3]))} "{r[4]}";\n')
st = open(sst).read().split("\n"); S = [l for l in st if l.startswith("SIGMA0")][0]; T = [l for l in st if l.startswith("TAU0")][0]
S += f" {h}:{L[0]}"; T += "".join(f" {L[j]}:{LAM[j]} {LAM[j]}:{MM[j]} {MM[j]}:{MV}" for j in range(K))
open(out + ".start", "w").write(S + "\n" + T + "\n")
