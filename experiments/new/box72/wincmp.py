#!/usr/bin/env python3
"""L-NEW box 72: N5 and N5-LZC (--lzc) end in the same winning regions (Even wins v iff the cycle node of the final Xi(v) has even
priority). Usage: wincmp.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
sys.argv.append("--lzc")
from n5x import load, step, start_pair, readstart, Engine, dual
import n5lz
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); start = readstart(args[1]) if len(args) > 1 else None
def win(st):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0
    while True:
        r = st(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]; k += 1
    return frozenset(v for v, x in enumerate(E.evaluate(tuple(s))[0]) if g.prio[x[0]] % 2 == 0), k
a, ka = win(step); b, kb = win(n5lz.step)
print(f"WIN {os.path.basename(args[0])} {'SAME' if a == b else 'DIFF'} n5 {ka} lzc {kb}")
