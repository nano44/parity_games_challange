#!/usr/bin/env python3
"""L-COMP box 37 item 1: family gen37(n) extracted from the k = 1 climb bests BEST_C300_r34_C17 (30d4ea76) / BEST_B400_r34_C17 (1694d52f).
gen37(n) = MWR(n) (= L-RED R229 genmw229.py with WTGT=R, L = 2; verbatim copy in genmw229_copy.py) with TWO changes of the br order only
(nothing else; N, M, wiring, gate order, bp, start unchanged):
  (1) the option of R that goes to qz (R's last option) and (2) option 0 (the lane option, to R) of the last a-lane node a_m (m = 6n + 4)
  are moved to just above (a_1, 1), i.e. to the top of the hiX0 block of lane exits (below the hiX1 block of the b-lanes).
Usage: gen37.py n > G.json (names on stderr, as genmw229)."""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__)); n = int(sys.argv[1])
p = subprocess.run([sys.executable, os.path.join(H, "genmw229_copy.py"), str(n), "2"], env=dict(os.environ, WTGT="R"), capture_output=True, text=True, check=True)
G = json.loads(p.stdout); idx = json.loads(p.stderr); m = 6 * n + 4
R, am, a1 = idx["R"], idx[f"a{m}"], idx["a1"]
assert G["opts"][R][-1][1] == idx["qz"] and G["opts"][am][0][1] == R
bR, bam, ba1 = G["opts"][R][-1][2], G["opts"][am][0][2], G["opts"][a1][1][2]
order = sorted(range(len(G["br"])), key=lambda b: G["br"][b])
for b in (bam, bR):
    order.remove(b); order.insert(order.index(ba1) + 1, b)
for r, b in enumerate(order): G["br"][b] = r
json.dump(G, sys.stdout); print(); json.dump(idx, sys.stderr)
