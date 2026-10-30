#!/usr/bin/env python3
"""L-RED successor 33 (R135): the DESYNC-GATED ladder dg_k, box 82 section 3's clocked escape built in real N5.
ladder_k (l-new box 80) with level j+1 = {A_j+1 (leader, IRRELEVANT priority, direct edges), B_j+1 (follower, even marker)}.
The follower reads level j only through Odd gates g(B, c) -> {p(B, c) -> u(j, c) (tau), A (escape)}.
All gates, pads and leaders have priority 0 (< the sink's 2: never in a path set); the two gate routes have equal length.
  - A on the old child: sigma-bar routes BOTH gates of B to A, their Xi are equal (same play from A, same length): B is not offered.
  - A on the new child: the target gate's Xi = the new child's, B's current gate's Xi = the old child: B is offered, one iteration late.
  - tau-bar: escape = A's best = u(j, 1)'s best, so (g, A) is never Odd-improving (ties or worse for Odd): I_tau = {} at the gates.
Vertices: 0 sink (2, self-loop). Level 1: u(1, 0) (prio 0), u(1, 1) (marker) -> sink. T = top leader (prio 0) reading level k.
Usage: mkdg.py K OUT.pg OUT.start   [env GATE=0: plain ladder, followers read directly (control);
  UP=1: leaders A_j, 2 <= j < k, read through gates h(A_j, c) -> {q -> u(j-1, c), B_(j+1)}: an UPWARD wait (Lemma WAIT-CYCLE);
  UPTO=A: the escape goes to the irrelevant reader A_(j+1) instead (the cycle branch of WAIT-CYCLE)]"""
import sys, os
k = int(sys.argv[1]); GATE = os.environ.get("GATE", "1") == "1"; UP = os.environ.get("UP") == "1"; upg = []
prio, owner, succ, name = [], [], [], []
def add(nm, p, o, s=None):
    prio.append(p); owner.append(o); succ.append(s); name.append(nm); return len(prio) - 1
sink = add("sink", 2, 0, [0])
u = {}
for j in range(1, k + 1):
    u[j, 0] = add(f"A{j}", 0, 0)                       # leader / copy 0: irrelevant
    u[j, 1] = add(f"B{j}", 2 * (k - j) + 4, 0)         # copy 1: even marker, deeper = more relevant
T = add("T", 0, 0)
sig, tau = {}, {}
for j in range(1, k + 1):
    if j == 1:
        succ[u[1, 0]] = [sink]; succ[u[1, 1]] = [sink]; continue
    if UP and 2 <= j < k:                              # UP=1: the leader A_j waits for its last reader B_(j+1) (escape -> B_(j+1))
        gs = []
        for c in (0, 1):
            p = add(f"q{j}_{c}", 0, 1, [u[j - 1, c]])
            gq = add(f"h{j}_{c}", 0, 1, [p, None]); tau[gq] = p; gs.append(gq); upg.append((gq, j))
        succ[u[j, 0]] = gs; sig[u[j, 0]] = gs[0]
    else:
        succ[u[j, 0]] = [u[j - 1, 0], u[j - 1, 1]]; sig[u[j, 0]] = u[j - 1, 0]
    if not GATE:
        succ[u[j, 1]] = [u[j - 1, 0], u[j - 1, 1]]; sig[u[j, 1]] = u[j - 1, 0]; continue
    gs = []
    for c in (0, 1):
        p = add(f"p{j}_{c}", 0, 1, [u[j - 1, c]])
        g = add(f"g{j}_{c}", 0, 1, [p, u[j, 0]]); tau[g] = p; gs.append(g)
    succ[u[j, 1]] = gs; sig[u[j, 1]] = gs[0]
succ[T] = [u[k, 0], u[k, 1]]; sig[T] = u[k, 0]
for gq, j in upg: succ[gq][1] = u[j + 1, 0 if os.environ.get("UPTO") == "A" else 1]
n = len(prio)
for x in range(n):
    (sig if owner[x] == 0 else tau).setdefault(x, succ[x][0])
with open(sys.argv[2], "w") as f:
    f.write(f"parity {n - 1};\n" + "".join(f"{x} {prio[x]} {owner[x]} {','.join(map(str, succ[x]))} \"{name[x]}\";\n" for x in range(n)))
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(sig.items())) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(tau.items())) + "\n")
print(f"DG k {k} n {n} gate {GATE} top {T}")
