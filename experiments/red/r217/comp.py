#!/usr/bin/env python3
"""L-RED 54 R217: compile Friedmann's switchallexp G_n into an R104 genome (d 2) so that Howard on IDEAL-CYC mimics switch-all on G_n.
- Every node v except the sink pair (p, q) gets a level-0 HELPER h_v (one option: beta of priority pr(v), same parity, -> core(v)).
  Edges into v go to h_v; edges into p go to u (the R104 sink K0 -> K3 -> K2 -> K1 replaces p -> q).
- core(v): single-successor v (not a CycleLeaver): h_v's beta goes straight to entry(succ).
  Even v with >= 2 successors: mover M_v (level 0, or level 1 if v is a CycleNode), one option per successor (beta in the lowest band).
- CycleCenter h_i (the only Odd choice: {CycleNode e_i, CycleLeaver m_i}) becomes a GATE: the option of M_{e_i} towards h_i has
  xt = h_{e_i} (back into the cycle node), beta of priority pr(h_i), e-face = the CycleLeaver (e ranked by pr(m_i)), W-target =
  entry(succ(m_i)). CycleAccess k_i (Odd, -> h_i) becomes a level-1 mover with ONE option: a COPY gate of h_i (same xt, beta
  pr(h_i) - tie, e just below the main one, same W-target).
- Other options of level-1 movers get W-target DUMMY: a level-0 mover whose only option is a self-loop with the top even beta, so Odd
  never escapes there (escaping hands Even an even cycle above every sink play).
- Start: the best-reward start of G_n (reward p if even else -p) mapped to options.
Usage: comp.py n OUT.json"""
import sys, json
from fried import game, rew
from gdsl import Gen
import os
BONUS = os.environ.get("BONUS", "")
def compile_(n):
    V = game(n); nm = {v[0]: v[4] for v in V}; pr = {v[0]: v[1] for v in V}; ow = {v[0]: v[2] for v in V}; sc = {v[0]: v[3] for v in V}
    sink = {v[0] for v in V if v[4] in ("p", "q")}
    gate_nodes = {v for v in nm if ow[v] == 1 and len(sc[v]) == 2}                     # CycleCenters h_i
    for h in gate_nodes: assert nm[h][0] == "h", nm[h]
    cyc = {h: next(w for w in sc[h] if nm[w][0] == "e") for h in gate_nodes}           # CycleNode e_i
    lea = {h: next(w for w in sc[h] if nm[w][0] == "m") for h in gate_nodes}           # CycleLeaver m_i
    acc = {h: [v for v in nm if h in sc[v] and v != cyc[h]] for h in gate_nodes}        # CycleAccess k_i
    lev1 = {cyc[h] for h in gate_nodes} | {a for h in gate_nodes for a in acc[h]}
    g = Gen(); H = {}; M = {}
    def hname(v): return f"h_{nm[v]}"
    for v in nm:
        if v in sink or v in gate_nodes or nm[v][0] == "m": continue
        H[v] = g.mv(hname(v), 0)
        if len(sc[v]) >= 2 or v in lev1: M[v] = g.mv(f"M_{nm[v]}", 1 if v in lev1 else 0)
    D = g.mv("DUMMY", 0); g.opt(D, None, D, (10 ** 9, "dummy"), 0)
    def entry(w):
        if w in sink: return None                                    # -> u
        assert w not in gate_nodes and nm[w][0] != "m", nm[w]
        return H[w]
    tie = [0]
    def lowkey(): tie[0] += 1; return (-1, tie[0])
    for v in H:
        if v in M: g.opt(H[v], None, M[v], (pr[v], 0), pr[v] % 2)
        else: g.opt(H[v], None, entry(sc[v][0]), (pr[v], 0), pr[v] % 2)
    start = {}
    for v in M:
        if v in {a for h in gate_nodes for a in acc[h]}:                       # CycleAccess: one COPY gate
            h = sc[v][0]; assert h in gate_nodes
            g.opt(M[v], H[sc[lea[h]][0]], H[cyc[h]], (pr[h], -1), pr[h] % 2, gkey=(pr[lea[h]], 0))
            continue
        best = max(sc[v], key=lambda w: (rew(pr[w]), w))
        for k, w in enumerate(sc[v]):
            if w in gate_nodes:
                g.opt(M[v], H[sc[lea[w]][0]], H[v], (pr[w], 0), pr[w] % 2, gkey=(pr[lea[w]], 1))
            elif "l" in BONUS and nm[v][0] == "l" and nm[w][0] == "z" and nm[v][1:] != "0":
                # E-DOM repair: the odd penalty pr(k_i) on l_i -> k_i becomes an even bonus e_Z(i) on l_i -> z_i,
                # ranked where pr(k_i) sits among the CycleLeavers (between CL(i-1) and CL(i)).
                ki = next(u for u in nm if nm[u] == "k" + nm[v][1:]); bz = g.mv(f"BZ_{nm[v]}", 1)
                g.opt(bz, entry(w), bz, (10 ** 8, nm[v]), 0, gkey=(pr[ki], 0))
                g.opt(M[v], None, bz, lowkey(), 0, gkey=(-1, tie[0]))
            else:
                g.opt(M[v], D if v in lev1 else None, entry(w), lowkey(), 0, gkey=(-1, tie[0]))
            if w == best: start[M[v]] = k
    G, ix = g.genome(start)
    return G, ix
if __name__ == "__main__":
    n = int(sys.argv[1]); G, ix = compile_(n); json.dump(G, open(sys.argv[2], "w")); json.dump(ix, open(sys.argv[2][:-5] + ".names.json", "w"))
    print(f"compiled switchallexp {n}: N {G['N']} movers, levels {sorted(set(G['lev']))}, options {sum(len(o) for o in G['opts'])}")
