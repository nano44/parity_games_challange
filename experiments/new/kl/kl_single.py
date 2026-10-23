#!/usr/bin/env python3
"""N8d: Koh-Loho strategy iteration (kl.py machinery, unchanged) with the SINGLE-SWITCH pivot rules frozen in docs/new/N8d-single.md §0:
R1 = lowest-id Odd node with an admissible arc, R2 = uniformly random such node (random.Random(seed) per Algorithm 1 run); the node
switches to its largest-Tighten admissible arc (TOP largest; ties smallest successor id).
Usage: kl_single.py game.pg --rule r1|r2 [--seed S] [--sol out.sol] -> n,d,h,rule,pivots,pivots_dual,verified,secs"""
import sys, os, time, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg, verify


def best_arc(G, mu, v):
    adm = [w for w in G.succ[v] if kl.violated(G, mu, v, w)]
    best, bk = None, None
    for w in sorted(adm):
        t = kl.tighten(G, mu, v, w); key = (1,) if t is kl.TOP else (0, t)
        if bk is None or key > bk: bk, best = key, w
    return best


def candidates(G, mu):
    return [v for v in range(G.n) if G.owner[v] == 1 and any(kl.violated(G, mu, v, w) for w in G.succ[v])]


def rule_r1(G, mu, tau, rng):
    v = min(candidates(G, mu)); new = list(tau); new[v] = best_arc(G, mu, v); return new


def rule_r2(G, mu, tau, rng):
    v = rng.choice(candidates(G, mu)); new = list(tau); new[v] = best_arc(G, mu, v); return new


def strategy_iteration(G, rule, seed):
    """Algorithm 1 with a single-switch rule (copy of kl.strategy_iteration; the rule is the only difference)."""
    rng = random.Random(seed)
    tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
    mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)]); it = 0
    while candidates(G, mu):
        it += 1
        new = rule(G, mu, tau, rng)
        assert sum(1 for v in range(G.n) if new[v] != tau[v]) == 1   # exactly one switch (an admissible arc differs from tau(v))
        tau = new
        nmu = kl.label_setting(G, kl.edges_tau(G, tau), mu)
        assert all(kl.lab_max(mu[v], nmu[v]) == nmu[v] for v in range(G.n)), "mu not monotone"
        mu = nmu
    return mu, tau, it


def solve(g, rule, seed=1):
    t0 = time.time(); R = rule_r1 if rule == "r1" else rule_r2
    G = kl.Game(g); mu, _, it = strategy_iteration(G, R, seed)
    D = kl.Game(g, dual=True); mud, _, itd = strategy_iteration(D, R, seed)
    win = [0 if mu[v] is not kl.TOP else 1 for v in range(g.n)]
    assert win == [1 if mud[v] is not kl.TOP else 0 for v in range(g.n)], "primal and dual regions disagree"
    se, so = kl.even_strategy(G, mu), kl.even_strategy(D, mud)
    strat = [se[v] if g.owner[v] == 0 else so[v] for v in range(g.n)]
    return dict(n=g.n, d=G.d, h=G.h, it=it, it_dual=itd, win=win, strat=strat, secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--rule", default="r1")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--sol"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    r = solve(g, a.rule, a.seed); errs = verify.check(g, r["win"], r["strat"])
    if a.sol: pg.write_sol(r["win"], a.sol, r["strat"])
    print(",".join(str(x) for x in (r["n"], r["d"], r["h"], a.rule + ("" if a.rule == "r1" else f"s{a.seed}"), r["it"], r["it_dual"],
                                     "verified" if not errs else "VERIFY-FAIL:" + errs[0], r["secs"])))
