#!/usr/bin/env python3
"""L-SI box 104: state for state. The mover parts of the N5'-xi run from S3 on F_n (states 0..T, engine 1) against Howard's run on the
ORIGINAL game G_n (L-RED's fried.howard: VJ switch-all from the best-reward start). Counter mism: (state, Even choice vertex of G_n)
pairs at which the option chosen in F_n is not Howard's successor in G_n. CTRL=1: compare state t of F_n with state t + 1 of G_n.
Usage: xtraj104.py n..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import free104 as F
import n5v, gamma3
CTRL = int(os.environ.get("CTRL", "0"))
for n in map(int, sys.argv[1:]):
    Vf = F.fried.game(n); nm = {v[0]: v[4] for v in Vf}; sc = {v[0]: v[3] for v in Vf}; T, traj = F.fried.howard(Vf)
    g, sig, tau, V, G, ix = F.F(n); st, fb, E = n5v.run(g, "xi")
    mv = {v: ix["M_" + nm[v]] for v in nm if ("M_" + nm[v]) in ix and Vf[v][2] == 0}
    ms = [gamma3.mover_state(G, V, s[0], F.PADS) for s in st]; mism = 0; pairs = 0
    for t in range(T + 1 - CTRL):
        a = traj[t + CTRL]; b = ms[t]
        for v in mv: pairs += 1; mism += a[v] != sc[v][b[mv[v]]]
    print(f"XTRAJ104 n {n}{' CTRL' if CTRL else ''}: Howard T {T}; N5'-xi iterations {len(st) - 1}; Even choice vertices {len(mv)}; pairs {pairs}; mism {mism}", flush=True)
