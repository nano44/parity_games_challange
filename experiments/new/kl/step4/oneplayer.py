#!/usr/bin/env python3
"""N8d step 4 (docs/new/N8d-proofs.md §3.6): R1 / R2 primal pivots on ONE-PLAYER games for the improver (every Even vertex has out-degree 1,
so only Odd chooses; the primal Algorithm 1 run is then the whole game for Odd). Part 1: random games. Part 2: hill-climb on the game
(priority / owner / edge mutations keeping Even out-degree 1) maximising primal pivots under a rule. Every reported game is solved by
kl_single.solve and both strategies checked with experiments/harness/verify.py (Oink not built in this container: no zlk cross-check).
Usage: oneplayer.py random NMAX COUNT SEED | oneplayer.py climb n rule seconds SEED OUT.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(HERE, "..")
sys.path[:0] = [K, os.path.join(K, "..", "..", "harness")]
import kl, kl_single, pg, verify


def rgame(rng, n):
    owner = [rng.randint(0, 1) for _ in range(n)]
    prio = [rng.randint(0, n) for _ in range(n)]
    succ = [[rng.randrange(n)] if owner[v] == 0 else rng.sample(range(n), rng.randint(1, min(4, n))) for v in range(n)]
    return prio, owner, succ


def piv(prio, owner, succ, rule, seed=1):
    g = pg.Game(prio, owner, succ, [None] * len(prio)); r = kl_single.solve(g, rule, seed)
    assert not verify.check(g, r["win"], r["strat"]), "verify failed"
    return r["it"], g


if sys.argv[1] == "random":
    nmax, cnt, rng = int(sys.argv[2]), int(sys.argv[3]), random.Random(int(sys.argv[4])); worst = {}
    for t in range(cnt):
        n = rng.randint(2, nmax); pr, ow, su = rgame(rng, n)
        for rule in ("r1", "r2"):
            p, _ = piv(pr, ow, su, rule); b = (n - 1) // 10
            worst[(rule, b)] = max(worst.get((rule, b), 0), p)
    for k in sorted(worst): print(f"{k[0]},n_bin={10*k[1]+1}-{10*k[1]+10},max_primal_pivots={worst[k]}")
else:
    n, rule, secs, rng, outp = int(sys.argv[2]), sys.argv[3], float(sys.argv[4]), random.Random(int(sys.argv[5])), sys.argv[6]
    pr, ow, su = rgame(rng, n); best, _ = piv(pr, ow, su, rule); t0 = time.time(); steps = 0
    while time.time() - t0 < secs:
        p2, o2, s2 = list(pr), list(ow), [list(x) for x in su]; v = rng.randrange(n); m = rng.randrange(4)
        if m == 0: p2[v] = rng.randint(0, n)
        elif m == 1:
            o2[v] = 1 - o2[v]
            if o2[v] == 0: s2[v] = [s2[v][0]]
        elif m == 2: s2[v][rng.randrange(len(s2[v]))] = rng.randrange(n)
        elif o2[v] == 1: s2[v].append(rng.randrange(n))
        s2 = [list(dict.fromkeys(x)) for x in s2]
        f, _ = piv(p2, o2, s2, rule); steps += 1
        if f >= best: best, pr, ow, su = f, p2, o2, s2
    _, g = piv(pr, ow, su, rule)
    with open(outp, "w") as fh:
        fh.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, su[v]))};\n" for v in range(n)))
    print(f"climb,n={n},rule={rule},secs={secs},steps={steps},best_primal_pivots={best},odd_vertices={sum(ow)},file={os.path.basename(outp)}")
