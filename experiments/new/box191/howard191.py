#!/usr/bin/env python3
"""Box 191: test HOWARD-EQ on Gamma3(G): at every non-fallback transition of N5'-xi (resp. N5) before the core phase, is sigma_new at
every mover the Xi_sigma-best successor over ALL its successors (switch-best / Howard step), and is sigma_new = sigma at every other
Even vertex? Usage: howard191.py MODE GENOME.json ...   prints per genome: iterations, #mover-phase transitions, #Howard-equal."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace191 as T

def check(G, mode):
    rows, states, fbs, g = T.trace(G, mode); _, _, _, V = T.gamma3.build(G, T.PADS); E = T.n5v.Engine(g); N = G["N"]
    movers = [V[("x", x)] for x in range(N)]; ph = eq = 0; first_bad = None
    for t in range(len(states) - 1):
        s, ns = states[t][0], states[t + 1][0]
        if rows[t + 1]["off"] or rows[t + 1]["esc"] or states[t + 1][1] != states[t][1]: break   # core / fallback phase
        ph += 1; vs, _ = E.evaluate(tuple(s))
        hw = [max(g.succ[x], key=lambda w: (E.key(vs[w]), w == s[x])) for x in movers]
        if all(ns[x] == h for x, h in zip(movers, hw)): eq += 1
        elif first_bad is None: first_bad = t
    return len(states) - 1, ph, eq, first_bad

if __name__ == "__main__":
    mode = sys.argv[1]
    for f in sys.argv[2:]:
        G = json.load(open(f)); it, ph, eq, fb = check(G, mode)
        print(f"{os.path.basename(f)} mode {mode} iterations {it} mover-phase {ph} howard-equal {eq} first-unequal {fb}")
