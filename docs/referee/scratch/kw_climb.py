#!/usr/bin/env python3
"""REFEREE succ. 11 hill-climb for the K note (kw_probe checks). Random C^1O games, edge / priority / owner mutations that keep
exactly one Odd choice vertex; score = weighted counts of the thin hypotheses (post-freeze kind changes, c_w switches inside CW-INT
windows, kind-B switches, Xi-flat S4a pairs, post-freeze state checks). Any *_FAIL is printed and its game saved to kw_logs/.
Usage: kw_climb.py SECONDS SEED NMIN NMAX [start.pg ...]   (restarts pick a start file when given)"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, kw_probe as KP

W = dict(KIND_postfrz_changes=50, CWINT_switches=20, CASCB_switches=5, WONCE_chk=2, FRZ_chk=1, u3_runs=1)


def score(g):
    c = Counter(); KP.EX.clear()
    try: KP.run_game(g, c, "climb")
    except RuntimeError: return -1, c
    return sum(W[k] * c[k] for k in W), c


def mutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; o = P.assert_c1o(g)
    for _ in range(rng.randint(1, 3)):
        v = rng.randrange(n); m = rng.random()
        if m < 0.5:
            if v == o or owner[v] == 0:
                if rng.random() < 0.5 and len(succ[v]) > (2 if v == o else 1): succ[v].remove(rng.choice(succ[v]))
                else: succ[v] = sorted(set(succ[v] + [rng.randrange(n)]))
            else: succ[v] = [rng.randrange(n)]
        elif m < 0.85:
            u = rng.randrange(n); prio[v], prio[u] = prio[u], prio[v]
        elif v != o:
            owner[v] = 1 - owner[v]
            if owner[v] == 1: succ[v] = [rng.choice(succ[v])]
    h = RE.Game(prio, owner, succ)
    P.assert_c1o(h)
    return h


def save(g, tag):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kw_logs", "fail_%s.pg" % tag)
    with open(p, "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
    return p


def main(a):
    secs, seed, lo, hi = int(a[0]), int(a[1]), int(a[2]), int(a[3])
    rng = random.Random(seed); t0 = time.time(); tot = Counter(); evals = 0
    starts = [RE.parse(f) for f in a[4:]]
    fresh = (lambda: rng.choice(starts)) if starts else (lambda: P.rand_c1o(rng, rng.randint(lo, hi)))
    g = fresh(); best, c = score(g)
    while time.time() - t0 < secs:
        if rng.random() < 0.02: h = fresh()
        else:
            try: h = mutate(g, rng)
            except AssertionError: continue
        s, c = score(h); evals += 1
        for k, v in c.items():
            if not k.endswith("_max"): tot[k] += v
        fails = {k: v for k, v in c.items() if k.endswith("_FAIL")}
        if fails:
            print("FAIL", fails, save(h, "%d_%d" % (seed, evals)), KP.EX[:3], flush=True)
        if s >= best: g, best = h, s
    tot["evals"] = evals; tot["best"] = best
    for k in sorted(tot): print("%-34s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(sys.argv[1:])
