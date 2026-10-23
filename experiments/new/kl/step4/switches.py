#!/usr/bin/env python3
"""N8d step 4 (docs/new/N8d-proofs.md §3.3): per-node switch counts along N8d-R2 runs (kl_single.py, unchanged; same generator use).
Also checks Lemma 3.0(c) on every switch: the switched node's own truncation mu(v)|_pi(v) strictly increases.
Usage: switches.py game.pg [--seed S] -> side,n,odd_nodes,pivots,max_switches_per_node,mean_over_switching_nodes,lemma_c_violations"""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(HERE, "..")
sys.path[:0] = [K, os.path.join(K, "..", "..", "harness")]
import kl, kl_single, pg


def run(G, seed):
    rng = random.Random(seed)
    tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
    mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)])
    cnt = [0] * G.n; it = 0; bad = 0
    while kl_single.candidates(G, mu):
        new = kl_single.rule_r2(G, mu, tau, rng); v = next(u for u in range(G.n) if new[u] != tau[u])
        tau = new; nmu = kl.label_setting(G, kl.edges_tau(G, tau), mu)
        if not kl.gt(kl.trunc(G, nmu[v], G.pi[v]), kl.trunc(G, mu[v], G.pi[v])): bad += 1
        mu = nmu; cnt[v] += 1; it += 1
    sw = [c for c in cnt if c]
    return it, max(sw or [0]), (sum(sw) / len(sw)) if sw else 0, bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    for side in ("primal", "dual"):
        G = kl.Game(g, dual=(side == "dual")); it, mx, mean, bad = run(G, a.seed)
        print(f"{os.path.basename(a.game)},{side},seed{a.seed},n={G.n},odd={sum(G.owner)},pivots={it},max_sw={mx},mean_sw={mean:.2f},lemma_c_viol={bad}", flush=True)
