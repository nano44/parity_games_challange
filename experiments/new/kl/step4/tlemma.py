#!/usr/bin/env python3
"""N8d step 4 (docs/new/N8d-proofs.md §3.6): test of Lemma T along N8d-R2 runs (kl_single.py machinery, unchanged).
Lemma T: at every state where some vertex with mu*(v) = TOP is still finite, some candidate's R2 pivot creates a NEW TOP.
Also splits the run into phase 1 (until the TOP set equals mu*'s) and phase 2 (the rest).
Usage: tlemma.py game.pg [--seed S] [--side primal|dual|both]"""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(HERE, "..")
sys.path[:0] = [K, os.path.join(K, "..", "..", "harness")]
import kl, kl_single, pg


def run(G, seed):
    star, _, it = kl_single.strategy_iteration(G, kl_single.rule_r2, seed)
    TS = {v for v in range(G.n) if star[v] is kl.TOP}
    rng = random.Random(seed)
    tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
    mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)])
    k = bad = ph1 = 0; first = None
    while kl_single.candidates(G, mu):
        cur = {v for v in range(G.n) if mu[v] is kl.TOP}
        if cur != TS:
            ph1 = k + 1
            ok = False
            for v in kl_single.candidates(G, mu):
                t2 = list(tau); t2[v] = kl_single.best_arc(G, mu, v)
                m2 = kl.label_setting(G, kl.edges_tau(G, t2), mu)
                if any(m2[u] is kl.TOP for u in range(G.n) if u not in cur): ok = True; break
            if not ok:
                bad += 1; first = first or k + 1
        tau = kl_single.rule_r2(G, mu, tau, rng); mu = kl.label_setting(G, kl.edges_tau(G, tau), mu); k += 1
    assert k == it
    return it, len(TS), ph1, bad, first


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--side", default="both"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    for side in (["primal", "dual"] if a.side == "both" else [a.side]):
        it, nt, ph1, bad, first = run(kl.Game(g, dual=(side == "dual")), a.seed)
        print(f"{os.path.basename(a.game)},{side},seed{a.seed},pivots={it},top_in_mustar={nt},phase1_pivots<={ph1},"
              f"states_violating_T={bad},first_violation_state={first}", flush=True)
