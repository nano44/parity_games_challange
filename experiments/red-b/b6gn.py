#!/usr/bin/env python3
"""B6 (L-RED-B successor 4): the binary-counter sink parity game G_n of Disser, Loho, Maat, Mosis, arXiv 2512.16684v2, Lemma 4.4 and
Fig. 4.1 (Bland's rule: 2^n - 1 single switches from sigma0), built as written there, and N5 (SPEC, L-NEW's box190/n5v.py) run on it:
mode spec and mode xi from S3, and from the paper's sigma0 (Odd's start: S3's tau). Every output checked against harness Zielonka.
Vertices: a_i (Even, priority 2i+1) -> {a_(i+1), b_(i+1)}; b_i (Odd, 2i+2) -> {a_(i+1), b_(i+1)}, i = 1..n; b_(n+1) (Odd, 2n+4) -> T;
a_(n+1) = T, the sink: priority 1 (the lowest odd), self-loop (READING: the paper's sink; its priority is not printed in the lines read).
Usage: b6gn.py B3ROOT n...   prints one line per (n, mode, start)."""
import sys, os
sys.argv, ns = sys.argv[:2], [int(x) for x in sys.argv[2:]]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
from b5lemma import pg, n5v, n5, n5x, zielonka, Engine

def gn(n):
    A = lambda i: 2 * (i - 1); B = lambda i: 2 * (i - 1) + 1          # a_i, b_i for i = 1..n
    bn1, T = 2 * n, 2 * n + 1
    prio = [0] * (2 * n + 2); own = [0] * (2 * n + 2); succ = [None] * (2 * n + 2)
    nxtA = lambda i: A(i + 1) if i < n else T
    nxtB = lambda i: B(i + 1) if i < n else bn1
    for i in range(1, n + 1):
        prio[A(i)], own[A(i)], succ[A(i)] = 2 * i + 1, 0, sorted([nxtA(i), nxtB(i)])
        prio[B(i)], own[B(i)], succ[B(i)] = 2 * i + 2, 1, sorted([nxtA(i), nxtB(i)])
    prio[bn1], own[bn1], succ[bn1] = 2 * n + 4, 1, [T]
    prio[T], own[T], succ[T] = 1, 0, [T]
    sig0 = [nxtA(i) for i in range(1, n + 1) for _ in (0, 1)]
    sig0 = [sig0[v] if own[v] == 0 and v < 2 * n else -1 for v in range(2 * n)] + [-1, T]
    return pg.Game(prio, own, succ), sig0

def run(g, mode, start):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    if start is not None: sigma = [start[v] if g.owner[v] == 0 else sigma[v] for v in range(g.n)]
    its = 0; fl = []
    while its < 10 ** 6:
        r = n5v.step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau, _, _, fb = r; its += 1
        if fb: fl.append(its)
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return its, len(fl), int(win != zielonka.solve(g))

for n in ns:
    g, s0 = gn(n)
    for mode in ("spec", "xi"):
        for nm, st in (("S3", None), ("sigma0", s0)):
            I, k, w = run(g, mode, st)
            print("B6GN n %d |V| %d mode %s start %s | I %d k %d | wrong %d" % (n, g.n, mode, nm, I, k, w), flush=True)
