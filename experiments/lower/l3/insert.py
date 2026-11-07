#!/usr/bin/env python3
"""Insert a static pass-through level at level L into a text genome (xt/br/bp/gate/start, R110 wiring).
Old movers of level >= L shift up one level (index + 2); Xi-targets are remapped. New movers 2L, 2L+1: both options Xi-target X,
start (0, 1) (a differ pair: c_(L+1) = s(2L) xor c_L = c_L, an identity wire), the current option of each with even parity and
the other with odd parity, all four ranks below every old rank (old ranks shifted up by 4), so neither new mover ever has a
better option and never moves; gates fresh, with gamma irrelevant (the pair never becomes equal). The old run is preserved
exactly on the old movers (checked by the caller). Usage: insert.py in.txt L out.txt"""
import sys
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] in ("xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
    return D
D = rd(sys.argv[1]); L = int(sys.argv[2]); N = len(D["start"]); d = N // 2
mp = lambda x: x if x < 0 or x < 2 * L else x + 2
xt, br, bp, gt, st = [], [], [], [], []
g0 = max(D["gate"]) + 1
for x in range(N + 2):
    if 2 * L <= x < 2 * L + 2:
        p = x - 2 * L; cur = p  # start option: mover 2L on 0, mover 2L+1 on 1
        for k in range(2):
            xt.append(-1); br.append(2 * p + k); bp.append(0 if k == cur else 1); gt.append(g0 + 2 * k + p)
        st.append(cur); continue
    ox = x if x < 2 * L else x - 2
    for k in range(2):
        xt.append(mp(D["xt"][2 * ox + k])); br.append(D["br"][2 * ox + k] + 4); bp.append(D["bp"][2 * ox + k]); gt.append(D["gate"][2 * ox + k])
    st.append(D["start"][ox])
with open(sys.argv[3], "w") as f:
    f.write("d %d\n" % (d + 1))
    for key, v in (("xt", xt), ("br", br), ("bp", bp), ("gate", gt), ("start", st)): f.write(key + " " + " ".join(map(str, v)) + "\n")
