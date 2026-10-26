#!/usr/bin/env python3
"""REFEREE succ. 8: hill climb for the case TEV-RED (1) leaves open: an Ev vertex (evicted at an in-scope fallback k0 of level
L >= 0) on the cycle of c at a state t in (k0, next fallback of S] with r > L on [k0+1, t]; best of all on the cycle of x_t's play.
Fitness = 1000 [Ev on x_t's cycle] + 100 [Ev on c's cycle] + 10 [A empty at k0] + sum over states of 1/(1 + dist(Ev -> c's cycle)).
C^1O is asserted for every candidate. Usage: rl_climb.py seed.pg seconds rngseed outdir"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P


def fitness(g):
    o, st = P.states(g); P.OO[0] = o
    inph, runs = P.scope_runs(st); best = 0.0
    for S in runs:
        fbs = [k for k in S if st[k]["fb"]]
        for i, k0 in enumerate(fbs):
            L = st[k0]["M"]
            if L < 0: continue
            Ev = st[k0 + 1]["F"] - st[k0]["F"]; c = st[k0]["Xi"][o][0]
            Hs = {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
            Aempty = not any(st[k0]["Xi"][o][1] >> g.rank[v] & 1 for v in Hs)
            last = fbs[i + 1] if i + 1 < len(fbs) else S[-1]
            sc = 10.0 * Aempty
            for t in range(k0 + 1, last + 1):
                b = st[t]
                if not (b["r"] > L and b["r"] < P.INF and b["h"]): break
                C = set(RE.lasso(b["nx"], c)[1]); pre, cyc = RE.lasso(b["nx"], b["sb"][o])
                if set(cyc) & Ev: sc += 1000
                if C & Ev: sc += 100
                for v in Ev:
                    vp, vc = RE.lasso(b["nx"], v)
                    if set(vc) == C: sc += 1.0 / (1 + len(vp))
            best = max(best, sc)
    return best


def mutate(g, rng, o):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n
    r = rng.random(); v = rng.randrange(n)
    if r < 0.45:
        if owner[v] == 1 and v != o: succ[v] = [rng.randrange(n)]
        else:
            i = rng.randrange(len(succ[v])); succ[v][i] = rng.randrange(n)
    elif r < 0.6:
        if owner[v] == 0 or v == o: succ[v].append(rng.randrange(n))
    elif r < 0.7:
        if (owner[v] == 0 or v == o) and len(succ[v]) > (2 if v == o else 1): succ[v].pop(rng.randrange(len(succ[v])))
    elif r < 0.9:
        u = rng.randrange(n); prio[u], prio[v] = prio[v], prio[u]
    else:
        if v != o:
            if owner[v] == 0: owner[v] = 1; succ[v] = [succ[v][0]]
            else: owner[v] = 0
    return RE.Game(prio, owner, succ)


def save(g, path):
    with open(path, "w") as fh:
        fh.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): fh.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))


def main():
    seed, secs, rs, outd = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(rs); g = RE.parse(seed); o = P.assert_c1o(g); f = fitness(g); t0 = time.time(); it = 0
    print("start", seed, f, flush=True)
    while time.time() - t0 < secs:
        it += 1; h = mutate(g, rng, o)
        try:
            if P.assert_c1o(h) != o: continue
            fh = fitness(h)
        except (AssertionError, RuntimeError, RecursionError): continue
        if fh >= f:
            if fh > f:
                print("it %d t %.0f fit %.3f" % (it, time.time() - t0, fh), flush=True)
                save(h, os.path.join(outd, "rlc_best_%d.pg" % rs))
            g, f = h, fh
    print("end it", it, "best", f, flush=True)


if __name__ == "__main__":
    main()
