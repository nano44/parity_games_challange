#!/usr/bin/env python3
"""L-RED R184 CNIDX: every W-cycle-node move inside an FL run (box 132 runs; c Even with W-length 0, sigma_j(c) != sigma_(j-1)(c)):
UP = moves to a LARGER successor index, DOWN = to a smaller one; RET = returns to an option c left earlier in the same run. DOWN_NOSHORT = down moves (not to c's self-loop) with no other successor
of c on sigma_(j-1)(c)'s W-cycle path (sigma_(j-1), tau) back to c: Lemma CN-UP says 0.
Usage: cnidx.py G.pg [START|-]"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21")]
import dcyc
from n5x import load, readstart, start_pair, Engine, dual
from freeze import run
import pg
def analyse(g, st=None):
    s, t = start_pair(g, Engine(g), Engine(dual(g)), st); S, T, F, E = run(g, s, t); n, own = g.n, g.owner
    Wc = {}
    def wval(j):
        tau = T[j]
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        return Wc[tau].evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
    R = dict(cnmoves=0, up=0, down=0, ret=0, down_noshort=0); ex = []
    left = {}; cur = None
    for j in range(1, len(S)):
        fl = not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1)
        if not fl: left = {}; continue
        W = wval(j)
        for c in range(n):
            if own[c] or W[c][2] != 0 or S[j][c] == S[j - 1][c]: continue
            R["cnmoves"] += 1; o, y = S[j - 1][c], S[j][c]
            if y > o: R["up"] += 1; ex.append((j, c, o, y))
            else:
                R["down"] += 1
                # Lemma CN-UP (R185): a down move needs another successor of c on sigma_(j-1)(c)'s W-cycle path back to c
                sW = [S[j - 1][v] if own[v] == 0 else T[j - 1][v] for v in range(n)]; q = sW[o]; path = []; seen = set()
                while q != c and q not in seen: seen.add(q); path.append(q); q = sW[q]
                if not (set(path) & (set(g.succ[c]) - {o})) and y != c: R["down_noshort"] += 1
            if y in left.get(c, set()): R["ret"] += 1
            left.setdefault(c, set()).add(o)
    return R, ex
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R, ex = analyse(g, st); print(f"CNIDX {os.path.basename(sys.argv[1])} n {g.n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()) + (f" EX {ex[:4]}" if ex else ""))
