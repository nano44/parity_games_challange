#!/usr/bin/env python3
"""L-NEW box 107: N5's winner regions at its stop (n5x trace; winner of v = parity of the cycle node of Xi(v)) against an Oink .sol
(lines 'v w ...', w = winner). Prints PINWIN <game> n <n> states <S> W0 <|W_0|> AGREE True/False.  Usage: pinwin.py GAME.pg START SOL"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, trace, readstart, Engine
g = load(sys.argv[1]); st = readstart(sys.argv[2]); states, fb = trace(g, st)
E = Engine(g); X = E.evaluate(states[-1][0])[0]; mine = {v for v in range(g.n) if E.par[X[v][0]] == 0}
oink = set()
for l in open(sys.argv[3]):
    x = re.match(r"^(\d+)\s+([01])\b", l.strip())
    if x and x.group(2) == "0": oink.add(int(x.group(1)))
print(f"PINWIN {os.path.basename(sys.argv[1])} n {g.n} states {len(states)} fallbacks {fb} W0 {len(mine)} AGREE {mine == oink}")
