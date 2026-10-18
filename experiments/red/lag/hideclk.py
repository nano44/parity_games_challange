#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5), R39 §9 probe: chainfam UP clock (k) where every x_j also has an edge to an Odd-won
vertex o (Odd-owned, pr O, edge o -> W, W an Odd sink), so the clock's tangles get an escape the root's threshold attractor
can never contain. MODE selects o's priority: low (1) or high (2k+3). Usage: hideclk.py k out.pg [low|high]"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from gb import GB
def build(k, mode="low"):
    g = GB(); g.v("a", 2*k+1, 0); g.v("b", 2*k, 1); g.v("z", 2*k, 1)
    for j in range(1, k+1): g.v(f"x{j}", 2*(j-1), 1)
    g.v("W", 2*k+5, 1); g.e("W", "W"); g.v("o", 1 if mode == "low" else 2*k+3, 1); g.e("o", "W")
    g.e("a", "b", "a"); g.e("b", "z", "b"); g.e("z", "z", f"x{k}")
    for j in range(1, k+1): g.e(f"x{j}", f"x{j}", "a" if j == 1 else f"x{j-1}", "o")
    return g
if __name__ == "__main__": build(int(sys.argv[1]), sys.argv[3] if len(sys.argv) > 3 else "low").write(sys.argv[2])
