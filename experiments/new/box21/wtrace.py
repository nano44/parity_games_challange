#!/usr/bin/env python3
"""Box 21: along the N5 run from (sigma_0, tau*) print per iteration: W-changing (play values vs tau*), honest-changing,
W-improving edges missing from the gate Iσ (H1 violations), and whether W already equals the optimum W* (= Ξ* by saddle reading).
Usage: wtrace.py game.pg"""
import sys
from n5x import *
from h1 import wvals
def main(path):
    g = load(path); E = Engine(g); n = g.n
    states, _ = trace(g); s0, ts = states[0][0], states[-1][1]
    st = ({v: s0[v] for v in range(n) if g.owner[v] == 0}, {v: ts[v] for v in range(n) if g.owner[v] == 1})
    fs, _ = trace(g, st)
    Wend = wvals(g, fs[-1][0], ts)[1]; Xend = E.evaluate(fs[-1][0])[0]
    print("final W == final Ξ:", Wend == Xend)
    prevW = prevX = None; wc = xc = 0
    for k, (s, t) in enumerate(fs):
        Eg, W = wvals(g, s, t); X, _ = E.evaluate(s); Is = set(E.improving(s, X))
        miss = [(v, w) for v in range(n) if g.owner[v] == 0 for w in g.succ[v] if w != s[v] and Eg.key(W[w]) > Eg.key(W[s[v]]) and (v, w) not in Is]
        wimp = [(v, w) for v in range(n) if g.owner[v] == 0 for w in g.succ[v] if w != s[v] and Eg.key(W[w]) > Eg.key(W[s[v]])]
        if k:
            wc += W != prevW; xc += X != prevX
        print(f"state {k}: W-chg {int(k>0 and W != prevW)} Ξ-chg {int(k>0 and X != prevX)} W-opt {int(W == Wend)} W-improving {len(wimp)} not-gated {miss}")
        prevW, prevX = W, X
    print(f"iterations {len(fs)-1}: W-changing {wc}, Ξ-changing {xc}")
if __name__ == "__main__": main(sys.argv[1])
