#!/usr/bin/env python3
"""B6 (L-RED-B successor 4): direct test of Lemma ACYC-GREEDY (docs/red-b/B6-quietkey-1p.md §2). Random ONE-PLAYER games whose only
cycle is the self-loop of a sink c (vertices 1..n-1 point only to lower indices; vertex 0 = c; random priorities and owners, an Odd
vertex keeps one successor). h = the largest number of edges of a path to c. N5 (SPEC, L-NEW's box190/n5v.py, modes spec and xi) from
S3: on such games S4a's arena values are the true values, so the lemma predicts I <= h. Must-0 counters: viol (I > h), wrong (regions
!= harness Zielonka). CONTROL (must fire): single-switch Bland (switch only the lowest-index improving edge of the lowest-index improving
vertex, from the same S3 start) is not value-greedy; ctrl counts the games on which its step count exceeds h.
Usage: b6acyc.py B3ROOT SEED COUNT NMAX    env DEG (max out-degree of an Even vertex, default 3)"""
import sys, os, random
sys.argv, rest = sys.argv[:2], sys.argv[2:]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
DEG = int(os.environ.get("DEG", "3"))
from b5lemma import pg, n5v, n5, n5x, zielonka, Engine

def gen(rng, n):
    prio = list(range(n)); rng.shuffle(prio); own = [0] + [int(rng.random() < 0.25) for _ in range(n - 1)]
    succ = [[0]]
    for v in range(1, n):
        s = sorted(set(rng.randrange(v) for _ in range(rng.randint(1, DEG))))
        succ.append(s if own[v] == 0 else [s[0]])
    return pg.Game(prio, own, succ)

def height(g):
    h = [0] * g.n
    for v in range(1, g.n): h[v] = 1 + max(h[w] for w in g.succ[v])
    return max(h)

def n5run(g, mode):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0
    while its < 10 ** 5:
        r = n5v.step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau = r[0], r[1]; its += 1
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return its, int(win != zielonka.solve(g))

def bland(g):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, _ = n5x.start_pair(g, E, Ed, None); sigma = list(sigma); its = 0
    while its < 10 ** 5:
        vs, _ = E.evaluate(tuple(sigma)); I = E.improving(tuple(sigma), vs)
        if not I: break
        v, w = min(I); sigma[v] = w; its += 1
    return its

def main():
    seed, count, nmax = int(rest[0]), int(rest[1]), int(rest[2]); rng = random.Random(seed)
    viol = {"spec": 0, "xi": 0}; wrong = 0; ctrl = 0; maxI = 0; maxh = 0
    for i in range(count):
        g = gen(rng, rng.randint(3, nmax)); h = height(g); maxh = max(maxh, h)
        for mode in ("spec", "xi"):
            I, w = n5run(g, mode); wrong += w; maxI = max(maxI, I)
            if I > h: viol[mode] += 1; print("VIOL seed %d i %d mode %s I %d h %d" % (seed, i, mode, I, h), flush=True)
        ctrl += int(bland(g) > h)
    print("B6ACYC seed %d games %d nmax %d | viol spec %d viol xi %d wrong %d | max I %d max h %d | CONTROL bland>h %d" % (
        seed, count, nmax, viol["spec"], viol["xi"], wrong, maxI, maxh, ctrl), flush=True)

if __name__ == "__main__":
    main()
