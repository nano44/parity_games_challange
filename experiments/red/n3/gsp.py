#!/usr/bin/env python3
"""Random 'gated shortest path' games (the shape of long121_n40): sink s (Odd-owned, even priority, self-loop, low rank), N Even
vertices with ODD priorities (costs) and out-degree 2-3 into a layered network that reaches s, and k Odd gates with even priority whose
tau is s (start) and with 2-4 options into the network; Even vertices also get edges into gates with prob PG.
Samples games, runs N5 from the start (sigma random, tau(gate) = s), reports the longest phase. Usage: gsp.py SEED SECONDS N K [PG] OUTDIR"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
from phclimb import fit, save

def make(rng, N, K, PG):
    n = N + K + 1; s = 0; gates = list(range(1, K + 1)); ev = list(range(K + 1, n))
    prio = [0] * n; owner = [0] * n; succ = [[] for _ in range(n)]
    pr = rng.sample(range(1, 4 * n), n)
    owner[s] = 1; prio[s] = 2; succ[s] = [s]
    for gt in gates:
        owner[gt] = 1; prio[gt] = 2 * pr[gt]                              # even
        succ[gt] = sorted(set([s] + rng.sample(ev, rng.randint(2, 4))))
    order = ev[:]; rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    for v in ev:
        prio[v] = 2 * pr[v] + 1                                          # odd
        later = [w for w in ev if pos[w] < pos[v]] + [s]                 # edges toward the sink (acyclic part)
        d = rng.randint(2, 3); t = set(rng.sample(later, min(d, len(later))))
        if rng.random() < PG: t.add(rng.choice(gates))
        if rng.random() < 0.15: t.add(rng.choice(ev))                    # a few back edges
        succ[v] = sorted(t)
    st = ({v: rng.choice(succ[v]) for v in ev}, {gt: s for gt in gates})
    return pg.Game(prio, owner, succ), st

def main():
    seed, secs, N, K = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    PG = float(sys.argv[5]); out = sys.argv[6]; os.makedirs(out, exist_ok=True)
    rng = random.Random(seed); t0 = time.time(); best = (0,); it = 0
    while time.time() - t0 < secs:
        it += 1; g, st = make(rng, N, K, PG); f = fit(g, st, 10 ** 9)
        if f and f > best: best = f; save(g, st, os.path.join(out, f"gsp_{N}_{K}_{seed}.pg")); print(f"{time.time()-t0:.0f}s it {it} n {g.n} best {f}", flush=True)
    print("done", it, best)

if __name__ == "__main__":
    main()
