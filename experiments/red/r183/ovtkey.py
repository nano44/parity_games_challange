#!/usr/bin/env python3
"""L-RED R183 OVTKEY: check of Lemma OVT-KEY (docs/red/R183-fvch.md section 2) on every maximal FL run (fvch.py run detection).
For Even x not in CN: T_x tight options (packet); B_x := Even vertices v not in CN... reachable from T_x along W-tight edges
(T_v at Even, tau_a at Odd), x excluded, stopping at CN. A KEY-STRETCH of x is a maximal set of consecutive states of the run with
sigma constant on B_x. A move at transition j belongs to the stretch of its NEW state j (its keys kappa_j). Lemma: per stretch, x
moves at most |T_x| - 1 times and never moves back to an option it left in that stretch. Reports
MOVES, RETURNS (x moves back to an option it left earlier in the same run), RET_IN (returns inside one key-stretch: lemma says 0),
OVER (stretches with more than |T_x| - 1 moves: lemma says 0), NOB (returns at x with B_x empty: lemma says 0),
KBOUND (vertices x with moves > (|T_x| - 1)(1 + KCH_x), KCH_x = stretches - 1: Corollary KEY-CHARGE says 0),
FL (transitions in FL runs), CNONLY (FL transitions at which only W-cycle nodes move).
Usage: ovtkey.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "r170"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
def analyse(g, st=None, cap=10 ** 5):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); n, own, pr = g.n, g.owner, g.prio
    Wc, WV = {}, {}
    def wval(j):
        if j not in WV:
            tau = T[j]
            if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
            WV[j] = Wc[tau].evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        return WV[j]
    runs = []; cur = None
    for j in range(1, len(S)):
        if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
            if cur and cur[1] == j - 1: cur[1] = j
            else: cur = [j - 1, j]; runs.append(cur)
    R = dict(runs=len(runs), moves=0, returns=0, ret_in=0, over=0, nob=0, kbound=0, fl=0, cnonly=0)
    for a, b in runs:
        tau = T[a]; W = wval(a); CN = {v for v in range(n) if W[v][2] == 0}
        Tx = {}
        for x in range(n):
            if own[x]: continue
            Tx[x] = [y for y in g.succ[x] if W[y][0] == x] if x in CN else [y for y in g.succ[x] if E.extend(x, W[y]) == W[x]]
        R["fl"] += b - a
        R["cnonly"] += sum(1 for j in range(a + 1, b + 1) if all(x in CN for x in range(n) if own[x] == 0 and S[j][x] != S[j - 1][x]))
        for x in range(n):
            if own[x] or x in CN: continue
            B = set(); st_ = list(Tx[x]); seen = set(st_)
            while st_:
                u = st_.pop()
                if u in CN: continue
                if own[u] == 0: B.add(u); nx = Tx[u]
                else: nx = [tau[u]]
                for w in nx:
                    if w not in seen: seen.add(w); st_.append(w)
            B.discard(x)
            left = set(); stretch = {}; sid = 0
            for j in range(a, b + 1):
                if j > a and any(S[j][v] != S[j - 1][v] for v in B): sid += 1
                stretch[j] = sid
            cnt = {}; leftin = {}
            for j in range(a + 1, b + 1):
                if S[j][x] == S[j - 1][x]: continue
                R["moves"] += 1; z, y = S[j - 1][x], S[j][x]
                if y in left:
                    R["returns"] += 1; R["nob"] += not B
                    if y in leftin.get(stretch[j], set()): R["ret_in"] += 1
                left.add(z); leftin.setdefault(stretch[j], set()).add(z); cnt[stretch[j]] = cnt.get(stretch[j], 0) + 1
            R["over"] += sum(1 for k, c in cnt.items() if c > max(len(Tx[x]) - 1, 0))
            R["kbound"] += len(cnt) and sum(cnt.values()) > max(len(Tx[x]) - 1, 0) * (1 + sid)
    return R
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R = analyse(g, st); print(f"OVTKEY {os.path.basename(sys.argv[1])} n {g.n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
