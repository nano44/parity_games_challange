#!/usr/bin/env python3
"""Independent reference: Zielonka's recursive algorithm (max-parity), written from the textbook definition
(attractor of the top priority, recurse on the complement, the opponent's dominion is removed and the call repeats).
Usage: zielonka.py game.pg [solution.sol]   (prints the solution to stdout if no output path)
Also: brute_force(g) solves tiny games by enumerating Even's positional strategies (positional determinacy),
an oracle independent of any attractor code."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg
from collections import deque

sys.setrecursionlimit(100000)


def attractor(g, alive, target, player, strat=None):
    """Vertices in `alive` from which `player` forces a visit to `target` (subset of alive), within the subgame.
    If `strat` (dict) is given, the attracting successor of every added vertex owned by `player` is stored in it."""
    attr = set(target)
    cnt = {}
    q = deque(attr)
    while q:
        w = q.popleft()
        for v in g.pred[w]:
            if v not in alive or v in attr:
                continue
            if g.owner[v] == player:
                attr.add(v); q.append(v)
                if strat is not None:
                    strat[v] = w
            else:
                if v not in cnt:
                    cnt[v] = sum(1 for x in set(g.succ[v]) if x in alive)
                cnt[v] -= 1
                if cnt[v] == 0:
                    attr.add(v); q.append(v)
    return attr


def solve_sub(g, alive, stats, strat):
    """Return (W0, W1) for the subgame induced by `alive` (a valid subgame: every vertex has a successor in alive).
    Writes winning positional strategies into `strat` for the winner's vertices (standard Zielonka construction)."""
    stats[0] += 1
    if not alive:
        return set(), set()
    d = max(g.prio[v] for v in alive)
    p = d % 2
    top = {v for v in alive if g.prio[v] == d}
    sA = {}
    A = attractor(g, alive, top, p, sA)
    W = solve_sub(g, alive - A, stats, strat)
    if not W[1 - p]:
        strat.update(sA)
        for v in top:
            if g.owner[v] == p:
                strat[v] = next(w for w in g.succ[v] if w in alive)
        res = [None, None]
        res[p] = set(alive); res[1 - p] = set()
        return tuple(res)
    sB = {}
    B = attractor(g, alive, W[1 - p], 1 - p, sB)
    strat.update(sB)  # W[1-p] keeps the sub-solution's strategies (written by the recursive call)
    W2 = solve_sub(g, alive - B, stats, strat)
    res = [None, None]
    res[p] = W2[p]
    res[1 - p] = W2[1 - p] | B
    return tuple(res)


def solve_with_strategy(g, stats=None):
    stats = stats if stats is not None else [0]
    strat = {}
    W0, W1 = solve_sub(g, set(range(g.n)), stats, strat)
    assert W0 | W1 == set(range(g.n)) and not (W0 & W1)
    win = [0 if v in W0 else 1 for v in range(g.n)]
    return win, [strat.get(v) if g.owner[v] == win[v] else None for v in range(g.n)]


def solve(g, stats=None):
    return solve_with_strategy(g, stats)[0]


def _odd_wins_one_player(n, succ, prio):
    """Single-player (Odd chooses everything) on graph succ: Odd wins from v iff v reaches a cycle whose max priority is odd."""
    good = set()
    for p in sorted({prio[v] for v in range(n) if prio[v] % 2 == 1}):
        sub = [v for v in range(n) if prio[v] <= p]
        subs = set(sub)
        for u in sub:
            if prio[u] != p:
                continue
            # is u on a cycle within prio<=p ?
            seen, st = set(), [w for w in succ[u] if w in subs]
            while st:
                x = st.pop()
                if x in seen:
                    continue
                seen.add(x)
                st.extend(w for w in succ[x] if w in subs)
            if u in seen:
                good.add(u)
    # vertices that reach `good`
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]:
            pred[w].append(v)
    win, st = set(good), list(good)
    while st:
        x = st.pop()
        for v in pred[x]:
            if v not in win:
                win.add(v); st.append(v)
    return win


def brute_force(g):
    """Even wins from v iff some positional Even strategy leaves Odd no odd-max reachable cycle from v."""
    import itertools
    ev = [v for v in range(g.n) if g.owner[v] == 0]
    choices = [sorted(set(g.succ[v])) for v in ev]
    even_win = set()
    for pick in itertools.product(*choices):
        succ = [list(set(s)) for s in g.succ]
        for v, w in zip(ev, pick):
            succ[v] = [w]
        oddw = _odd_wins_one_player(g.n, succ, g.prio)
        even_win |= set(range(g.n)) - oddw
    return [0 if v in even_win else 1 for v in range(g.n)]


if __name__ == "__main__":
    g = pg.read(sys.argv[1])
    stats = [0]
    win, strat = solve_with_strategy(g, stats)
    print(f"solved with {stats[0]} iterations.", file=sys.stderr)
    if len(sys.argv) > 2:
        pg.write_sol(win, sys.argv[2], strat)
    else:
        sys.stdout.write(f"paritysol {g.n};\n" + "".join(
            f"{v} {w}{'' if strat[v] is None else ' ' + str(strat[v])};\n" for v, w in enumerate(win)))
