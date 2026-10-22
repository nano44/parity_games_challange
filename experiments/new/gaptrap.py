#!/usr/bin/env python3
"""L-NEW: route (A) with priority-gap traps (N1-killer-sketch.md, 11:20Z) on labelled switchallexp. For each bit i, the Even
vertex e_i gets an extra edge to a trap t_i -> c_i: t_i single-successor Odd of even priority P_i = B + 2 + 2k(i+1)
(or 2k(N-i) with --rev), c_i an Odd self-loop of odd priority B + 1, B = max original priority + (B even).
The trap loses for Even (Odd-won cycle), so W_E/W_O on the original vertices are unchanged; at horizon H the trap looks
like n^P_i - H n^(B+1): it is preferred until H ~ n^(P_i - B - 1), so bit i is revealed at phase ~ (2k(i+1)+1) log2 n.
Usage: gaptrap.py game.pg k [--rev] > out.pg"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse(open(sys.argv[1]).read()); k = int(sys.argv[2]); rev = "--rev" in sys.argv
lab = {g.labels[v]: v for v in range(g.n)}; N = sum(1 for l in lab if re.fullmatch(r"e\d+", l or ""))
B = max(g.prio); B += B % 2
prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
for i in range(N):
    e = lab[f"e{i}"]; P = B + 2 + 2 * k * ((N - i) if rev else (i + 1)); t, c = len(prio), len(prio) + 1
    prio += [P, B + 1]; owner += [1, 1]; succ += [[c], [c]]
    succ[e] = sorted(succ[e] + [t])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
