"""L-RED box 24 (produced on Opus 5.5): lane timeline of G_zeta runs, R2 vs VJ Random-Edge.
A lane L in {A_i (a_{i,*}), B_i (b_{i,*}), C_i (c_{i,*})} is CLOSED when every lane node points inward (x_{i,1} -> A_i / B_i,
x_{i,j+1} -> x_{i,j}), i.e. the cycle through A_i / B_i is closed. Events: 'close L', 'open L' (closed -> not closed), and the
switches of w_i, u_i (counter access). Also prints, per lane, the number of switches of its nodes.
R2 = experiments/n8d-second/kl2fast.py KLFast.run's loop (same rng calls; asserted equal to KLFast.run at the end).
VJ = experiments/si/si.py Engine with rule_random_edge (vj_re.py's loop). Both read-only.
Usage: lanes.py r2|vj G.pg SEED"""
import os
import random
import re
import sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "si", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
sys.setrecursionlimit(100000)
import kl2fast  # noqa: E402
import kl2  # noqa: E402
import pg  # noqa: E402
import si  # noqa: E402

path, mode, seed = sys.argv[2], sys.argv[1], int(sys.argv[3])
NM = {}
for line in open(path):
    m = re.match(r'^\s*(\d+)\s.*"([^"]*)"', line)
    if m:
        NM[int(m.group(1))] = m.group(2)
ID = {v: k for k, v in NM.items()}
g = pg.read(path)
lanes = {}
for v, s in NM.items():
    m = re.match(r"^([abc])(\d+),(\d+)$", s)
    if m:
        L = {"a": "A", "b": "B", "c": "C"}[m.group(1)] + m.group(2)
        j = int(m.group(3))
        inward = ID[("A" if m.group(1) == "a" else "B") + m.group(2)] if j == 1 else ID[f"{m.group(1)}{m.group(2)},{j - 1}"]
        lanes.setdefault(L, []).append((v, inward))
watch = [v for v, s in NM.items() if re.match(r"^[wu]\d+$", s) and g.owner[v] == 0 and len(set(g.succ[v])) > 1]


def state(strat):
    return {L: all(strat[v] == w for v, w in ns) for L, ns in lanes.items()}


events, nsw = [], {}
cur = state(tuple(g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)))


def step(t, old, new):
    global cur
    v = next(u for u in range(g.n) if new[u] != old[u])
    for L, ns in lanes.items():
        if any(v == x for x, _ in ns):
            nsw[L] = nsw.get(L, 0) + 1
    if v in watch:
        events.append(f"{t}:{NM[v]}->{NM[new[v]]}")
    st = state(new)
    for L in sorted(lanes):
        if st[L] != cur[L]:
            events.append(f"{t}:{'close' if st[L] else 'open'} {L}")
    cur = st


if mode == "r2":
    D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
    n = D.n
    tau = dict(D.tau)
    cm, ct = kl2fast.arr([0] * (n * D.h)), kl2fast.arr([0] * n)
    D.c_lfp(tau, cm, ct)
    rng = random.Random(seed)
    cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n)
    piv = 0
    strat = tuple(tau[v] if g.owner[v] == 0 else -1 for v in range(n))
    while True:
        k = kl2fast.LIB.kl_adm(n, D.h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)
        if not k:
            break
        vs = list(cand[:k])
        i = vs.index(rng.choice(sorted(vs)))
        tau[vs[i]] = carc[i]
        D.c_lfp(tau, cm, ct)
        piv += 1
        new = tuple(tau[v] if g.owner[v] == 0 else -1 for v in range(n))
        step(piv, strat, new)
        strat = new
    ref = D.run("r2", seed)
    assert ref[0] == piv and ref[1] == tau
else:
    E = si.Engine(g)
    rng = random.Random(seed)
    strat = tuple(g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n))
    piv = 0
    while True:
        val = E.evaluate(strat)[0]
        imp = E.improving(strat, val)
        if not imp:
            break
        piv += 1
        new = E.rule_random_edge(strat, val, imp, rng)
        step(piv, strat, new)
        strat = new
print(f"{mode} {os.path.basename(path)} seed {seed}: steps {piv}; lane sizes " +
      ", ".join(f"{L} {len(ns)}" for L, ns in sorted(lanes.items())))
print("switches per lane: " + ", ".join(f"{L} {nsw.get(L, 0)}" for L in sorted(lanes)))
closes = {L: sum(1 for e in events if e.endswith(f"close {L}")) for L in lanes}
print("closings per lane: " + ", ".join(f"{L} {closes[L]}" for L in sorted(lanes)))
print("events: " + " ".join(events))
