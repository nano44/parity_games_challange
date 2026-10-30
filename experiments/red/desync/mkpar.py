#!/usr/bin/env python3
"""L-RED R135 (exploratory): dg_k + PARITY OPENERS, an upward wait whose signal route avoids X (outside Lemma WAIT-CYCLE's hypothesis).
For every level-j vertex X (2 <= j <= k - 1) and copy c, X's gate G(X, c) (Odd, prio 0) -> {pad -> u(j - 1, c) (tau), [A_j if X = B_j],
R(X, c)}. The opener R(X, c) (Even, prio 0) -> {G(X, 1 - c) (X's OTHER gate: "X still read"), H(X, c)}; H(X, c) (Odd, prio 0) ->
{pad -> sib(X) (tau), B_(j+1)} (R lags the last reader B_(j+1) laterally, as in dg). Start: everything on its first successor.
Env OPEN0=1: the opener of the START gate (c = 0) starts on H (open), so the two-opener cycle G0 -> R0 -> G1 -> R1 -> G0 is not closed at the start.
Usage: mkpar.py K OUT.pg OUT.start"""
import sys
import os
k = int(sys.argv[1]); OPEN0 = os.environ.get("OPEN0") == "1"
prio, owner, succ, name = [], [], [], []
def add(nm, p, o, s=None):
    prio.append(p); owner.append(o); succ.append(s); name.append(nm); return len(prio) - 1
sink = add("sink", 2, 0, [0]); u = {}
for j in range(1, k + 1):
    u[j, 0] = add(f"A{j}", 0, 0); u[j, 1] = add(f"B{j}", 2 * (k - j) + 4, 0)
T = add("T", 0, 0)
G, R = {}, {}
for j in range(1, k + 1):
    for b in (0, 1):
        X = u[j, b]
        if j == 1: succ[X] = [sink]; continue
        gs = []
        for c in (0, 1):
            p = add(f"p{name[X]}_{c}", 0, 1, [u[j - 1, c]]); G[X, c] = add(f"G{name[X]}_{c}", 0, 1, [p]); gs.append(G[X, c])
            if b == 1: succ[G[X, c]].append(u[j, 0])
        succ[X] = gs
for j in range(2, k):
    for b in (0, 1):
        X = u[j, b]; sib = u[j, 1 - b]
        for c in (0, 1):
            ps = add(f"ps{name[X]}_{c}", 0, 1, [sib]); H = add(f"H{name[X]}_{c}", 0, 1, [ps, u[j + 1, 1]])
            R[X, c] = add(f"R{name[X]}_{c}", 0, 0, [G[X, 1 - c], H]); succ[G[X, c]].append(R[X, c])
succ[T] = [u[k, 0], u[k, 1]]
n = len(prio)
with open(sys.argv[2], "w") as f:
    f.write(f"parity {n - 1};\n" + "".join(f"{x} {prio[x]} {owner[x]} {','.join(map(str, succ[x]))} \"{name[x]}\";\n" for x in range(n)))
with open(sys.argv[3], "w") as f:
    st = {v: succ[v][0] for v in range(n) if owner[v] == 0}
    if OPEN0: st.update({R[X, 0]: succ[R[X, 0]][1] for (X, c) in R if c == 0})
    f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(st.items())) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{succ[v][0]}" for v in range(n) if owner[v] == 1) + "\n")
print(f"PAR k {k} n {n}")
