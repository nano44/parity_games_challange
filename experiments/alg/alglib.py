"""Shared test helpers for L-ALG candidates: status of a partial answer against Zielonka, smallest level k that solves
a game, random games (harness gen.py, reproducible), record formatting."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, verify, gen
import ne


def status(win, ref):
    """'UNSOUND' if a decided vertex disagrees with ref, else 'solved' / 'undecided'."""
    if any(w is not None and w != r for w, r in zip(win, ref)):
        return "UNSOUND"
    return "solved" if all(w is not None for w in win) else "undecided"


def k_needed(g, ref, kmax, with_strat=False):
    """(smallest k <= kmax with NE(k) complete and sound, or None; per-k undecided counts; strategy verdicts)."""
    undec, verd = [], {}
    for k in range(kmax + 1):
        if with_strat:
            win, strat, res, info = ne.solve_with_strategy(g, k, "oracle")
        else:
            win, _, _ = ne.solve(g, k)
            res = {v for v in range(g.n) if win[v] is None}
        st = status(win, ref)
        if st == "UNSOUND":
            return "UNSOUND", undec + [len(res)], verd
        undec.append(len(res))
        if not res:
            if with_strat:
                errs = verify.check(g, win, strat)
                verd = dict(k=k, strat_fail=info["strat_fail"], verify=errs)
            return k, undec, verd
    return None, undec, verd


def random_game(n, d, dmin, dmax, seed, peven=0.5, selfloops=True):
    return gen.random_game(n, d, dmin, dmax, seed, peven, selfloops)


def game_record(g, ref=None, **kw):
    rec = dict(n=g.n, m=g.m, prio=list(g.prio), owner=list(g.owner), succ=[sorted(set(s)) for s in g.succ])
    if ref is not None:
        rec["ref"] = ref
    rec.update(kw)
    return rec


def from_record(rec):
    return pg.Game(rec["prio"], rec["owner"], rec["succ"])
