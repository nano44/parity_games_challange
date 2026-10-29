#!/usr/bin/env python3
"""L-NEW box 62: my OWN rebuild of L-RED 29's dwN from the Lead's 18:39Z description (L-RED's generator not yet pushed; not byte-compared):
fcN (experiments/red/sf/sbev.py N --drop fc) plus one Even "repeater" u_i on each escape-chain edge v_i -> r_(i+1), i = 0..N-2:
v_i -> u_i replaces v_i -> r_(i+1); u_i -> {r_(i+1), v_(i+1)} (v_(N-1) does not exist: u_(N-2) -> {r_(N-1), p}); u_i has priority 3
(odd, just above q's 1); every other priority >= 2 is shifted up by 2(N-1)+2. Usage: dw.py N > out.pg"""
import sys, os, re, subprocess
N = int(sys.argv[1]); HERE = os.path.dirname(os.path.abspath(__file__))
src = subprocess.run([sys.executable, "-I", os.path.join(HERE, "..", "..", "red", "sf", "sbev.py"), str(N), "--drop", "fc"],
                     capture_output=True, text=True, check=True).stdout
rows = []
for l in src.splitlines():
    m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)\s*"([^"]*)";', l)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), list(map(int, m.group(4).split(","))), m.group(5)])
lab = {r[4]: r[0] for r in rows}; n0 = len(rows); sh = 2 * (N - 1) + 2
for r in rows:
    if r[1] >= 2: r[1] += sh
for i in range(N - 1):
    v, rr, u = lab[f"v{i}"], lab[f"r{i+1}"], n0 + i
    row = rows[v]; assert rr in row[3], (i, row)
    row[3] = [u if x == rr else x for x in row[3]]
    rows.append([u, 3, 0, [rr, lab[f"v{i+1}"] if f"v{i+1}" in lab else lab["p"]], f"u{i}"])
print(f"parity {len(rows) - 1};")
for r in rows: print(f'{r[0]} {r[1]} {r[2]} {",".join(map(str, r[3]))} "{r[4]}";')
