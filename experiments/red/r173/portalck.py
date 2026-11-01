#!/usr/bin/env python3
"""L-RED R173 check of Lemma PORTAL (docs/red/R173-portal.md).
For every TWO-FIX window of the N5 run (freeze.py's windows: tau and sbar constant), G_F = freeze.frozen (Odd vertices off D cut to
their single edge). For an Even vertex h and a successor x, class(h, x) := the first vertex of out-degree > 1 in G_F on the walk
x, succ_F(x), ... through out-degree-1 vertices (None if the walk returns to h or closes a cycle first).
A PAIR is two consecutive moves of h, i0 -> i1 at transition j1 and i1 -> i2 at transition j2 (state j-1 -> j), no S4c fallback at
transitions j1..j2, with class(h, i1) = class(h, i2) = X != None. Premises checked per pair:
  ZC: the cycle node of Xi_t(X) (Odd best reply sbar, values of sigma_t) is the same for t = j1-1 .. j2-1;
  NR: neither h nor a prefix vertex of i1 / i2 (the out-degree-1 walk before X) is on the Xi-play (sigma_t, sbar) from X, t = j1-1 .. j2-1, nor on the W-play (sigma_t, tau) from X, t = j1 .. j2.
Lemma PORTAL predicts for every pair with ZC and NR: the move at j2 is an exact tau-tie (key(W_j2(i1)) = key(W_j2(i2))), and
theta1 := cycle node of W_j1(X), theta2 := cycle node of W_j2(X) are both even.
Prints one summary line per game: pairs, pairs meeting ZC, NR, both (premised), odd_even (theta odd then even), tie, VIOLATIONS
(premised pairs that are not an exact tie with both thetas even; must be 0).
Usage: portalck.py G.pg [START|-]   (env VERB=1: one line per checked pair)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen

def play(succ1, x, cap):
    seen = []; s = set(); v = x
    while v not in s and len(seen) <= cap:
        seen.append(v); s.add(v); v = succ1[v]
    return s

def analyze(g, st, verb=False, cap=10 ** 6):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); W, SB = windows(g, S, T, E)
    n, own, pr = g.n, g.owner, g.prio
    tot = ok = oe = tie = bad = zc = nrc = 0
    for a, b in W:
        if b - a < 2: continue
        gf = frozen(g, SB[a], T[a]); tau = T[a]; sb = SB[a]
        gw = pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)])
        gx = pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)])
        EW, EX = Engine(gw), Engine(gx)
        def wv(j): return EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        def xv(j): return EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        def cls(h, x):
            v, seen = x, {h}
            while len(gf.succ[v]) == 1:
                if v in seen: return None
                seen.add(v); v = gf.succ[v][0]
            return None if v in seen else v
        def prefix(h, x):
            v, seen = x, set()
            while len(gf.succ[v]) == 1 and v not in seen and v != h:
                seen.add(v); v = gf.succ[v][0]
            return seen
        def s1(j, world):
            return [S[j][v] if own[v] == 0 else (tau[v] if world == "W" else sb[v]) for v in range(n)]
        moves = {}
        for j in range(a + 1, b + 1):
            for h in range(n):
                if own[h] == 0 and S[j][h] != S[j - 1][h]: moves.setdefault(h, []).append((j, S[j - 1][h], S[j][h]))
        for h, mv in moves.items():
            for (j1, i0, i1), (j2, i1b, i2) in zip(mv, mv[1:]):
                assert i1b == i1
                if any(F[j] for j in range(j1, j2 + 1)): continue
                X = cls(h, i1)
                if X is None or cls(h, i2) != X: continue
                tot += 1
                zs = {xv(j)[X][0] for j in range(j1 - 1, j2)}
                pre = {h} | prefix(h, i1) | prefix(h, i2)
                nr = all(not (pre & play(s1(j, "X"), X, n)) for j in range(j1 - 1, j2)) and \
                     all(not (pre & play(s1(j, "W"), X, n)) for j in range(j1, j2 + 1))
                zc += len(zs) == 1; nrc += nr
                if len(zs) != 1 or not nr:
                    if verb:
                        th1, th2 = wv(j1)[X][0], wv(j2)[X][0]; w2 = wv(j2)
                        zl = [pr[xv(j)[X][0]] for j in range(j1 - 1, j2)]
                        print(f"  pair h {h} moves {i0}->{i1}@{j1} {i1}->{i2}@{j2} X {X} premise ZC {len(zs) == 1} NR {nr} theta {pr[th1]}->{pr[th2]} Z {zl} Wtie {EW.key(w2[i1]) == EW.key(w2[i2])} Wstrict {EW.key(w2[i2]) > EW.key(w2[i1])}")
                    continue
                ok += 1
                th1, th2 = wv(j1)[X][0], wv(j2)[X][0]
                w2 = wv(j2); istie = EW.key(w2[i1]) == EW.key(w2[i2])
                good = istie and pr[th1] % 2 == 0 and pr[th2] % 2 == 0
                oe += (pr[th1] % 2 == 1 and pr[th2] % 2 == 0); tie += istie
                if not good: bad += 1
                if verb or not good:
                    print(f"  pair h {h} moves {i0}->{i1}@{j1} {i1}->{i2}@{j2} X {X} theta {pr[th1]}->{pr[th2]} Z {pr[next(iter(zs))]} tie {istie} {'OK' if good else 'VIOLATION'}")
    return dict(n=n, K=len(S) - 1, zc=zc, nr=nrc, pairs=tot, premised=ok, odd_even=oe, tie=tie, bad=bad)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    r = analyze(g, st, os.environ.get("VERB") == "1")
    print(f"PORTAL {os.path.basename(sys.argv[1])} n {r['n']} K {r['K']} pairs {r['pairs']} premised {r['premised']} odd_even {r['odd_even']} tie {r['tie']} VIOLATIONS {r['bad']}")

if __name__ == "__main__":
    main()
