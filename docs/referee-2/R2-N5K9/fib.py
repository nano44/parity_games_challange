"""Candidate family FIB(m): t = vertex 0 (priority 0, self-loop, Even); v_i = vertex i, i = 1..m, Even, priority given by PR;
succ(v_1) = {t}, succ(v_2) = {t, v_1}, succ(v_i) = {v_{i-2}, v_{i-1}}. One-player (no Odd vertices). Prints longest chains."""
import sys, os, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onep import *
def fib(m, pr):
    prio = [0] + [pr(i) for i in range(1, m + 1)]
    succ = [[0]] + [[0]] + ([[0, 1]] if m >= 2 else []) + [[i - 2, i - 1] for i in range(3, m + 1)]
    return Game(prio, [0] * (m + 1), succ)
modes = sys.argv[1].split(',') ; mmax = int(sys.argv[2]); prname = sys.argv[3] if len(sys.argv) > 3 else 'even'
PR = {'even': lambda i: 2 * i, 'alt': lambda i: i + 1}[prname]
for m in range(2, mmax + 1):
    g = fib(m, PR); row = [m]
    for md in modes:
        t0 = time.time(); row.append((md, longest(OneP(g), md)))
    print('FIB', prname, *row, flush=True)
