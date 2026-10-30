#!/usr/bin/env python3
"""L-RED R136: dg_k + a SHARED pattern clock. Every leader A_j (2 <= j <= k - 1) reads level j - 1 through Odd gates
G(A_j, c) -> {pad -> u(j - 1, c) (tau), e(j, c)}, where e(j, c) is an Odd vertex with ODD priority PE (env, default 2(k - j) + 3: between the
level-j and level-(j+1) markers) and the single successor T. The route e -> T -> ... -> A_j is T's own play (the upper ladder's choices = the
pattern clock), so the patterns need not recur; Lemma ALT-ESCAPE says the shared entry still kills every wait.
Usage: mkte.py K OUT.pg OUT.start"""
import sys, os
k = int(sys.argv[1])
prio, owner, succ, name = [], [], [], []
def add(nm, p, o, s=None):
    prio.append(p); owner.append(o); succ.append(s); name.append(nm); return len(prio) - 1
sink = add("sink", 2, 0, [0]); u = {}
for j in range(1, k + 1):
    u[j, 0] = add(f"A{j}", 0, 0); u[j, 1] = add(f"B{j}", 2 * (k - j) + 4, 0)
T = add("T", 0, 0); esc = []
for j in range(1, k + 1):
    if j == 1: succ[u[1, 0]] = [sink]; succ[u[1, 1]] = [sink]; continue
    gs = []
    for c in (0, 1):
        p = add(f"p{j}_{c}", 0, 1, [u[j - 1, c]]); gs.append(add(f"g{j}_{c}", 0, 1, [p, u[j, 0]]))
    succ[u[j, 1]] = gs
    if j < k:
        hs = []
        for c in (0, 1):
            q = add(f"q{j}_{c}", 0, 1, [u[j - 1, c]]); e = add(f"e{j}_{c}", int(os.environ.get("PE", 2 * (k - j) + 3)), 1, [T])
            hs.append(add(f"h{j}_{c}", 0, 1, [q, e]))
        succ[u[j, 0]] = hs
    else: succ[u[j, 0]] = [u[j - 1, 0], u[j - 1, 1]]
succ[T] = [u[k, 0], u[k, 1]]; n = len(prio)
with open(sys.argv[2], "w") as f:
    f.write(f"parity {n - 1};\n" + "".join(f"{x} {prio[x]} {owner[x]} {','.join(map(str, succ[x]))} \"{name[x]}\";\n" for x in range(n)))
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{succ[v][0]}" for v in range(n) if owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{succ[v][0]}" for v in range(n) if owner[v] == 1) + "\n")
print(f"TE k {k} n {n}")
