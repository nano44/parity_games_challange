#!/usr/bin/env python3
"""N8a robustness: Algorithm 1 of kl.py with another initial Odd strategy tau_1 (the paper allows any tau_1): 'last' successor, or
'rand<seed>' (uniform per Odd node). Same pivot rules, same Algorithm 3, same verification. Imports kl.py unchanged.
Usage: kl_init.py game.pg --rule all|global --init last|rand<seed> [--sol out.sol] -> same CSV line as kl.py plus the init."""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg, verify


def make_init(mode):
    def init(G):
        if mode == "last": return [G.succ[v][-1] if G.owner[v] == 1 else None for v in range(G.n)]
        rng = random.Random(int(mode[4:]))
        return [rng.choice(G.succ[v]) if G.owner[v] == 1 else None for v in range(G.n)]
    return init


def strategy_iteration(G, rule, init):
    """kl.strategy_iteration with tau_1 = init(G) (Algorithm 1 line 3), otherwise identical."""
    tau = init(G); mu = [tuple([0] * G.h) for _ in range(G.n)]
    mu = kl.label_setting(G, kl.edges_tau(G, tau), mu); it = 0
    while any(G.owner[v] == 1 and any(kl.violated(G, mu, v, w) for w in G.succ[v]) for v in range(G.n)):
        it += 1
        tau, ch = (kl.rule_global if rule == "global" else kl.rule_all)(G, mu, tau)
        assert ch > 0
        new = kl.label_setting(G, kl.edges_tau(G, tau), mu)
        assert all(kl.lab_max(mu[v], new[v]) == new[v] for v in range(G.n))
        mu = new
    return mu, tau, it


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--rule", default="global")
    ap.add_argument("--init", default="last"); ap.add_argument("--sol"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    G = kl.Game(g); mu, _, it = strategy_iteration(G, a.rule, make_init(a.init))
    D = kl.Game(g, dual=True); mud, _, itd = strategy_iteration(D, a.rule, make_init(a.init))
    win = [0 if mu[v] is not kl.TOP else 1 for v in range(g.n)]
    assert win == [1 if mud[v] is not kl.TOP else 0 for v in range(g.n)]
    se, so = kl.even_strategy(G, mu), kl.even_strategy(D, mud)
    strat = [se[v] if g.owner[v] == 0 else so[v] for v in range(g.n)]
    errs = verify.check(g, win, strat)
    if a.sol: pg.write_sol(win, a.sol, strat)
    print(",".join(str(x) for x in (g.n, G.d, G.h, a.rule, a.init, it, itd, "verified" if not errs else "VERIFY-FAIL:" + errs[0])))
