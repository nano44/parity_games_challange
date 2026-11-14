#!/usr/bin/env python3
"""Box 191: decompose the N5'-xi mover phase on Gamma3(G) into CYCLE steps (some vertex's VJ cycle node changes, under (sigma_t,
sigma-bar_t)) and PATH steps (all cycle nodes kept). Prints iterations, mover-phase length P, #cycle steps C, the longest run of
consecutive path steps (maxrun), #distinct cycle nodes used, max #e-faces in sigma-bar. Usage: segs191.py MODE GENOME.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace191 as T

def segs(G, mode):
    rows, states, fbs, g = T.trace(G, mode); _, _, _, V = T.gamma3.build(G, T.PADS); E = T.n5v.Engine(g); N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    P = 0
    for t in range(len(states) - 1):
        if rows[t + 1]["off"] or rows[t + 1]["esc"] or states[t + 1][1] != states[t][1]: break
        P += 1
    cyc = []; ef = 0
    for t in range(P + 1):
        vs, sb = E.evaluate(tuple(states[t][0])); cyc.append(tuple(vs[v][0] for v in range(g.n)))
        ef = max(ef, sum(sb[V[("g", q)]] == V[("pe", q)] for q in O))
    kinds = ["C" if cyc[t + 1] != cyc[t] else "p" for t in range(P)]
    runs = "".join(kinds).split("C"); maxrun = max(len(r) for r in runs) if runs else 0
    used = len(set(c for cc in cyc for c in cc))
    return len(states) - 1, P, kinds.count("C"), maxrun, used, ef, "".join(kinds)

if __name__ == "__main__":
    mode = sys.argv[1]
    for f in sys.argv[2:]:
        it, P, C, mr, used, ef, k = segs(json.load(open(f)), mode)
        print(f"{os.path.basename(f):30s} it {it:3d} P {P:3d} C {C:3d} maxrun {mr:3d} cyclenodes {used:3d} maxEface {ef:3d} {k}")
