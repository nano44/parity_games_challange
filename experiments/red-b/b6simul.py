#!/usr/bin/env python3
"""B6 attempt 2 probe (L-RED-B successor 4): the class that N5's key rule belongs to (docs/red-b/B6-quietkey-1p.md §1), stripped to its
simplest member. SIMUL-BLAND: on an acyclic one-player game (only cycle: the sink loop at vertex 0), every Even vertex with an improving
edge (SPEC S2 values, si.Engine) switches at once to its LOWEST-INDEX improving successor. Hill climb over games (priorities, edges) on
the number of steps from the S3 start; also reports N5 (n5v spec) on the best game, which is value-greedy there (Lemma ACYC-GREEDY: I <= h).
Every best is checked against harness Zielonka (regions of the final strategy). DATA only; SIMUL-BLAND is not N5.
Usage: b6simul.py B3ROOT SEED ITERS n [deg]     Final line B6SIMUL ...; state work/b6simul_<tag>.json (resumable)."""
import sys, os, json, random, time
sys.argv, rest = sys.argv[:2], sys.argv[2:]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
from b5lemma import pg, n5v, n5, n5x, zielonka, Engine

def game(D): return pg.Game(list(D["prio"]), list(D["own"]), [list(s) if D["own"][v] == 0 else [s[0]] for v, s in enumerate(D["succ"])])

def simul(g):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, _ = n5x.start_pair(g, E, Ed, None); sigma = list(sigma); its = 0
    while its < 10 ** 5:
        vs, _ = E.evaluate(tuple(sigma)); I = E.improving(tuple(sigma), vs)
        if not I: break
        best = {}
        for v, w in I: best[v] = min(best.get(v, w), w)
        for v, w in best.items(): sigma[v] = w
        its += 1
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return its, int(win != zielonka.solve(g))

def n5its(g):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0
    while True:
        r = n5v.step(g, E, Ed, sigma, tau, "spec")
        if r is None: return its
        sigma, tau = r[0], r[1]; its += 1

def height(g):
    h = [0] * g.n
    for v in range(1, g.n): h[v] = 1 + max(h[w] for w in g.succ[v])
    return max(h)

def rand_D(rng, n, deg):
    prio = list(range(n)); rng.shuffle(prio); own = [0] * n
    return {"prio": prio, "own": own, "succ": [[0]] + [sorted(set(rng.randrange(v) for _ in range(rng.randint(1, deg)))) for v in range(1, n)]}

def mutate(rng, D, deg):
    D = json.loads(json.dumps(D)); n = len(D["prio"]); v = rng.randrange(1, n); op = rng.choice(["prio", "prio", "edge+", "edge-", "re"])
    if op == "prio": u = rng.randrange(n); D["prio"][u], D["prio"][v] = D["prio"][v], D["prio"][u]
    elif op == "edge+":
        if len(D["succ"][v]) < deg: D["succ"][v] = sorted(set(D["succ"][v] + [rng.randrange(v)]))
    elif op == "edge-":
        if len(D["succ"][v]) > 1: D["succ"][v].remove(rng.choice(D["succ"][v]))
    else: s = D["succ"][v]; s[rng.randrange(len(s))] = rng.randrange(v); D["succ"][v] = sorted(set(s))
    return D

def main():
    seed, iters, n = int(rest[0]), int(rest[1]), int(rest[2]); deg = int(rest[3]) if len(rest) > 3 else 3
    tag = "n%d_d%d_s%d" % (n, deg, seed); os.makedirs("work", exist_ok=True); sf = "work/b6simul_%s.json" % tag; rng = random.Random(seed)
    if os.path.exists(sf): S = json.load(open(sf)); D = S["D"]; it0 = S["it"]; rng.seed(seed * 7919 + it0)
    else: D = rand_D(rng, n, deg); it0 = 0
    best, w = simul(game(D)); t0 = time.time(); nw = 0
    for it in range(it0, iters):
        E = D
        for _ in range(rng.randint(1, 3)): E = mutate(rng, E, deg)
        s2, w2 = simul(game(E)); nw += w2
        if s2 >= best:
            if s2 > best: print("it %d steps %d" % (it, s2), flush=True)
            D, best = E, s2
        if it % 100 == 0: json.dump({"D": D, "it": it + 1}, open(sf, "w"))
    json.dump({"D": D, "it": iters}, open(sf, "w")); g = game(D)
    print("B6SIMUL %s steps %d | h %d | N5 spec I %d | wrong %d %.0fs" % (tag, best, height(g), n5its(g), nw, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
