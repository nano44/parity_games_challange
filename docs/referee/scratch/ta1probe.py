#!/usr/bin/env python3 -I
"""REFEREE probes for TA1-proof.md gaps G1, G3, G5 (facts F2, F6, Lemma 0) on all small games; uses ta1check.py."""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slpcheck import Game, WE, all_games, random_game
from ta1check import bits, attr_in, mattr_in, is_p, peelable, subsets

def probe(games, limit=None):
    cnt = 0; bad = {"F6mattr": 0, "F6attr": 0, "F2": 0, "L0": 0, "F6incl": 0}
    for g in games:
        cnt += 1
        W0 = WE(g); W1 = g.ALL & ~W0; P = max(g.pr)
        for p, R in ((0, W0), (1, W1)):
            if R == 0: continue
            # F6 (general X subset R, any d): MAttr^G(X,d) == MAttr^R(X,d), Attr^G(X) == Attr^R(X)
            for X in subsets(R):
                if attr_in(g, g.ALL, X, p) != attr_in(g, R, X, p): bad["F6attr"] += 1
                for d in range(P + 1):
                    a, b = mattr_in(g, g.ALL, X, d, p), mattr_in(g, R, X, d, p)
                    if a != b: bad["F6mattr"] += 1
            # F6 inclusion for an arbitrary trap R' for q (not W_p): MAttr^R' subset MAttr^G
            for Rp in subsets(g.ALL):
                ok = all((not is_p(g, v, p) and (g.succ[v] & ~Rp) == 0) or (is_p(g, v, p) and (g.succ[v] & Rp)) for v in bits(Rp))
                if not ok: continue
                for X in (Rp,):
                    for d in range(P + 1):
                        if mattr_in(g, Rp, X, d, p) & ~mattr_in(g, g.ALL, X, d, p): bad["F6incl"] += 1
            # F2: D = Attr_p^G(Y), Y subset W_p: W_p(G \ D) = W_p \ D, W_q(G \ D) = W_q
            for Y in subsets(R):
                D = attr_in(g, g.ALL, Y, p); V2 = g.ALL & ~D
                if V2 == 0: continue
                h = Game(g.n, g.VE & V2, g.pr, [s & V2 if (V2 >> v) & 1 else (1 << v) for v, s in enumerate(g.succ)])
                # vertices outside V2 are made self-loops and excluded from the comparison
                w0 = WE(h) & V2
                wp = w0 if p == 0 else V2 & ~w0
                if wp != (R & ~D): bad["F2"] += 1
                wq = V2 & ~wp
                if wq != (g.ALL & ~R): bad["F2"] += 1
            # Lemma 0: peelable at d => at d+2
            dp = P if P % 2 == p else P + 1
            if peelable(g, R, dp, p) and not peelable(g, R, dp + 2, p): bad["L0"] += 1
        if limit and cnt >= limit: break
    print(f"{cnt} games: failures {bad}")

random.seed(3)
probe(all_games(2, (0, 1, 2)))
probe(all_games(3, (0, 1, 2, 3)), limit=40000)
probe((random_game(4, (0, 1, 2, 3, 4)) for _ in range(1500)))
