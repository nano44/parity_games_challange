#!/usr/bin/env python3
"""Box 9b (Lead 05:05Z item 2): hill climb for a FRZ-U_D-non-vacuous run: a maximal fallback-free run inside one phase with (NC) and
(h3_D) at every state, of at least n states (n - 1 transitions), so that FRZ-U_D's freeze "COARSE_L(W) constant from the (n-1)-th state"
is actually tested. Every scored run is fully checked by gdnc_check.check_run (b', c1', c2', FRZ); a violation is saved and stops.
Fitness (own): 1000 * (longest qualifying run in states - (n - 1)) + 10 * FRZ_checks + longest qualifying run, max over the canonical start
and 3 seeded random start pairs. Mutation (own): keeps n and at least 2 Odd vertices with out-degree >= 2.
FIT=nh (env): 10000 * (states with not (h_D) in checked runs) + 2000 * (states with |D_k| >= 2 in checked runs) + min(fitness, 2000).
FIT=nh2: the nh terms count only if the longest qualifying run has >= n + 1 states; + 3000 * min(longest - (n - 1), 3).
Usage: frz_climb.py steps seed OUTPREFIX INIT.pg"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gdnc_check as G  # noqa: E402

F = G.F
FIT = os.environ.get("FIT", "len")


def n_odd_choice(g):
    return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1)


def mutate(rng, g):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; r = rng.random(); v = rng.randrange(n)
    if r < 0.55:
        k = len(succ[v])
        if rng.random() < 0.4 and k > 1:
            succ[v].pop(rng.randrange(k))
        elif k < 3:
            succ[v].append(rng.randrange(n))
        else:
            succ[v][rng.randrange(k)] = rng.randrange(n)
        succ[v] = sorted(set(succ[v]))
    elif r < 0.85:
        prio[v] = rng.randrange(0, n + 1)
    else:
        owner[v] = 1 - owner[v]
    h = F.lpg.Game(prio, owner, succ)
    return h if n_odd_choice(h) >= 2 else None


def write_pg(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n):
            f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")


def score(g, seed):
    rng = random.Random(seed); E, Ed = F.Engine(g), F.Engine(F.n5.dual(g))
    starts = [(list(E.initial("best")), list(Ed.initial("best")))] + [G.rand_start(g, rng) for _ in range(3)]
    c, mx, viol = Counter(), Counter(), []
    best = 0
    for i, (s, t) in enumerate(starts):
        b = G.check_run(g, s, t, c, mx, viol.append, f"s{i}")
        best = max(best, b)
    f = 1000 * (best - (g.n - 1)) + 10 * c["FRZ_checks"] + best
    if FIT == "nh":   # aim at the (NC)-only case: qualifying runs that contain (NC) and not (h_D) states, or two gates in D
        f = 10000 * c["FRZ_checked_states_not_hD"] + 2000 * c["FRZ_checked_states_D_ge2"] + min(f, 2000)
    if FIT == "nh2":  # as nh, but the checked run must reach n + 1 states (non-vacuous also under the 0-based reading of "(n-1)-th")
        f = (10000 * c["FRZ_checked_states_not_hD"] + 2000 * c["FRZ_checked_states_D_ge2"]) * (best >= g.n + 1) + 3000 * min(best - (g.n - 1), 3) + 10 * best
    return f, c, viol, starts


def main():
    steps, seed, out, init = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
    rng = random.Random(seed)
    g = F.lpg.parse("".join(l for l in open(init) if not l.lstrip().startswith("%")))
    best, c, viol, _ = score(g, seed); tot = Counter(c)
    print("start", best, "n", g.n, flush=True)
    for i in range(steps):
        h = mutate(rng, g)
        if h is None:
            continue
        f, c, viol, starts = score(h, seed + i)
        tot.update(c)
        if viol:
            write_pg(h, out + "_VIOLATION.pg"); print("VIOLATION", viol[:5], "step", i, "seed", seed + i, flush=True); break
        if f >= best:
            if f > best:
                print(i, f, "FRZ_checks", c["FRZ_checks"], "seed", seed + i, flush=True)
            best, g = f, h
            write_pg(g, out + "_best.pg")
    print("TOTALS", dict(sorted(tot.items())), flush=True)
    print("RESULT", "VIOLATION" if viol else "OK", "best", best, flush=True)


if __name__ == "__main__":
    main()
