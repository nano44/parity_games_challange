#!/usr/bin/env python3
"""N8d step 4 (docs/new/N8d-proofs.md §3): test of Lemma M along N8d-R2 runs (kl_single.py machinery, unchanged).
M(mu) = #{(v, j): prefix_j(mu(v)) = prefix_j(mu*(v)), j = 0..h} (prefix_0 = 'is TOP'); mu* = the final labelling.
At every state of an R2 run (seed S) and for every candidate node v (Odd node with an admissible arc), pivot v to its largest-Tighten
admissible arc (the arc R2 would take), recompute the least fixed point, and record whether M increases.
A state with candidates but NO M-raising candidate refutes Lemma M (§3.2). Also records Psi = sum of rank gaps (§3.1) and the best
candidate's rank gain. Usage: mlemma.py game.pg [--seed S] [--dual] [--side primal|dual|both] -> one CSV line per run side + 'BAD' lines."""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(HERE, "..")
sys.path[:0] = [K, os.path.join(K, "..", "..", "harness")]
import kl, kl_single, pg


def rank(G, x):
    if x is kl.TOP: return G.base ** G.h
    r = 0
    for c in x: r = r * G.base + c
    return r


def pref(x, j):
    return "T" if x is kl.TOP else tuple(x[:j])


def M(G, mu, star):
    return sum(1 for v in range(G.n) for j in range(G.h + 1) if (j == 0 and (mu[v] is kl.TOP) == (star[v] is kl.TOP))
               or (j > 0 and pref(mu[v], j) == pref(star[v], j)))


def run(G, seed, name, side):
    star, _, it = kl_single.strategy_iteration(G, kl_single.rule_r2, seed)
    rng = random.Random(seed)
    tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
    mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)])
    states = bad = 0; minfrac = None; out = []; gap = maxgap = 0; ups = 0
    while True:
        cand = kl_single.candidates(G, mu)
        if not cand: break
        m0 = M(G, mu, star); psi = sum(rank(G, star[v]) - rank(G, mu[v]) for v in range(G.n))
        raising = 0; bestgain = 0
        for v in cand:
            t2 = list(tau); t2[v] = kl_single.best_arc(G, mu, v)
            mu2 = kl.label_setting(G, kl.edges_tau(G, t2), mu)
            if M(G, mu2, star) > m0: raising += 1
            bestgain = max(bestgain, sum(rank(G, mu2[u]) - rank(G, mu[u]) for u in range(G.n)))
        states += 1
        fr = bestgain / psi if psi else 1.0
        minfrac = fr if minfrac is None else min(minfrac, fr)
        if raising == 0:
            bad += 1
            if bad <= 3: out.append(f"BAD,{name},{side},seed{seed},state{states},cands={cand},M={m0}")
        tau = kl_single.rule_r2(G, mu, tau, rng)      # the actual R2 step (same generator sequence as kl_single)
        mu = kl.label_setting(G, kl.edges_tau(G, tau), mu)
        if M(G, mu, star) > m0: ups += 1; gap = 0
        else: gap += 1; maxgap = max(maxgap, gap)
    assert states == it, (states, it)
    return [f"{name},{side},seed{seed},n={G.n},h={G.h},pivots={it},states_without_M_raise={bad},M_raises_on_run={ups},max_run_gap={maxgap},min_bestgain_over_psi={minfrac}"] + out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--side", default="both"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    name = os.path.basename(a.game)
    for side in (["primal", "dual"] if a.side == "both" else [a.side]):
        for line in run(kl.Game(g, dual=(side == "dual")), a.seed, name, side): print(line, flush=True)
