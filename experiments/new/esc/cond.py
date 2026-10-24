#!/usr/bin/env python3
"""N10c (box 19, docs/new/N10-screen.md §3): rounding by conditioning on the N10b oracle (ESC-tau cut loop).
Query "Even wins every vertex". For the Even vertices with >= 2 successors, in index order: try the successors in order of
decreasing LP value s_vu (from the oracle's final LP; ties by index); keep the first one for which the oracle on the game with
v's edges cut to that one is still feasible; if none is, answer NO (STUCK). When every Even vertex is fixed the game is
Odd-only, where ACYC has no binaries and is exact, so a YES answer is always correct (a winning sigma is returned and checked).
Errors are one-sided: a STUCK run on a game Even wins everywhere."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sa"))
import pg, zielonka
from esc import esc_feasible
from peel import region_lp_sigma


def taus_for(h):
    if all(o == 0 for o in h.owner):
        return []
    succ = [sorted(set(x)) for x in h.succ]; out = []
    for lev in (0, 1):
        sig, _ = region_lp_sigma([p + 1 for p in h.prio], [1 - o for o in h.owner], succ, lev)
        if sig not in out:
            out.append(sig)
    return out


def oracle(h):
    f, _, _, s = esc_feasible(h, taus=taus_for(h), return_s=True)
    return f, s


def condition(g):
    succ = [sorted(set(x)) for x in g.succ]
    ok, s = oracle(g)
    if not ok:
        return None, 0
    calls = 1
    for v in range(g.n):
        if g.owner[v] != 0 or len(succ[v]) < 2:
            continue
        order = sorted(succ[v], key=lambda u: (-s.get((v, u), 0.0), u))
        for u in order:
            trial = [list(x) for x in succ]; trial[v] = [u]
            h = pg.Game(g.prio, g.owner, trial)
            ok2, s2 = oracle(h); calls += 1
            if ok2:
                succ, s = trial, s2
                break
        else:
            return None, calls
    sigma = {v: succ[v][0] for v in range(g.n) if g.owner[v] == 0}
    s1 = [[sigma[v]] if g.owner[v] == 0 else succ[v] for v in range(g.n)]
    assert not zielonka._odd_wins_one_player(g.n, s1, g.prio), "YES without a winning sigma: bug"
    return sigma, calls
