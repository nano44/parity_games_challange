#!/usr/bin/env python3
"""L-SI box 104: Lemma FREE-REACH on random FREE genomes (own generator; carrier priorities = a random permutation of 6..5 + 2M, so
parities and the beta / e order are arbitrary). Runs N5'-xi (box190 n5v.step, mode xi) from S3 on Gamma3*(G) and counts, per genome:
  s3fail   S3's pair is not the standard state of the genome start                                             (unit: genomes)
  nonstd   a state before the first fallback is not standard: tau != tau0, or sigma off the movers != the standard choice (unit: states)
  nohoward a mover's choice at a non-fallback step before the first fallback is not a best successor by Xi_sigma, or it left a best
           current successor                                                                             (unit: (step, mover) pairs)
  fbwrong  the first fallback is not at iteration T3 + 1 (T3 = first state at which no mover has a strictly better successor) (genomes)
  endwrong fallbacks != 1 or iterations != T3 + 3                                                                 (unit: genomes)
  wrong    regions != harness Zielonka                                                                            (unit: genomes)
  edomok   genomes whose random priorities happen to satisfy E-DOM (every e even and above every beta); descriptive.
CTRL=1: the Howard test uses the WORST successor (nohoward must fire). CTRL=2: T3 := T3 + 1 (fbwrong and endwrong must fire).
ALG=spec (env): the same run for N5 (n5v.step mode spec); then nohoward and fbwrong are not tested (N5's mover steps follow SPEC's
root-first key), endwrong := fallbacks != 1 or iterations != F + 2 (F = the first fallback), and max F is reported.
Usage: freereach104.py SEED COUNT [DMAX WMAX DEGMAX]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import free104 as F
import n5v, n5, n5x, zielonka
from si import Engine
CTRL = int(os.environ.get("CTRL", "0")); ALG = os.environ.get("ALG", "xi")

def rand_free(rng, dmax, wmax, degmax):
    lev = []
    for l in range(rng.randint(1, dmax)): lev += [l] * rng.randint(1, wmax)
    N = len(lev); by = {}
    for x in range(N): by.setdefault(lev[x], []).append(x)
    opts = []; b = 0
    for x in range(N):
        o = []
        for k in range(rng.randint(1, degmax)):
            o.append([-1 if lev[x] == 0 else rng.choice(by[lev[x] - 1]), -1 if rng.random() < 0.15 else rng.randrange(N), b]); b += 1
        opts.append(o)
    M = b; perm = list(range(M)); rng.shuffle(perm); it = iter(perm); gate = [[next(it) for _ in o] for o in opts]
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": list(range(M)), "bp": [0] * M, "start": [rng.randrange(len(o)) for o in opts]}
    car = [("b", q) for q in F.options(G)] + [("e", q) for q in F.options(G)]; rng.shuffle(car); pb = {}; pe = {}
    for i, (kind, q) in enumerate(car): (pb if kind == "b" else pe)[q] = 6 + i
    return G, pb, pe

def check(G, pb, pe):
    g, sig, tau, V = F.build_free(G, pb, pe); E, Ed = Engine(g), Engine(n5.dual(g)); N = G["N"]
    sigma, tau_t = n5x.start_pair(g, E, Ed, None); c = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0)
    c["s3fail"] = int(not (all(sigma[v] == sig[v] for v in sig) and all(tau_t[v] == tau[v] for v in tau)))
    its = 0; fbs = 0; F1 = None; T3 = None
    while its < 20000:
        vs, _ = E.evaluate(tuple(sigma))
        key = lambda w: E.key(vs[w])
        better = [x for x in range(N) if any(key(w) > key(sigma[x]) for w in g.succ[x])]
        if F1 is None:
            c["nonstd"] += int(any(tau_t[v] != tau[v] for v in tau) or any(sigma[v] != sig[v] for v in sig if v >= N))
            if T3 is None and not better: T3 = its
        r = n5v.step(g, E, Ed, sigma, tau_t, ALG)
        if r is None: break
        ns, nt, _, _, fb = r; its += 1; fbs += fb
        if fb and F1 is None: F1 = its
        if F1 is None and ALG == "xi":
            for x in range(N):
                ref = (min if CTRL == 1 else max)(key(w) for w in g.succ[x])
                c["nohoward"] += int(key(ns[x]) != ref or (key(sigma[x]) == ref and ns[x] != sigma[x]))
        sigma, tau_t = ns, nt
    if T3 is None: T3 = -1
    if CTRL == 2: T3 += 1
    if ALG == "xi": c["fbwrong"] = int(F1 != T3 + 1); c["endwrong"] = int(fbs != 1 or its != T3 + 3)
    else: c["endwrong"] = int(fbs != 1 or F1 is None or its != F1 + 2); T3 = F1 if F1 is not None else -1
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    c["wrong"] = int(win != zielonka.solve(g))
    O = F.options(G); edom = all(pe[q] % 2 == 0 for q in O) and min(pe.values()) > max(pb.values())
    return c, T3, its, g.n, edom

if __name__ == "__main__":
    seed, cnt = int(sys.argv[1]), int(sys.argv[2]); dm, wm, gm = (int(a) for a in sys.argv[3:6]) if len(sys.argv) > 5 else (4, 3, 3)
    rng = random.Random(seed); tot = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0); mT = 0; mn = 0; ne = 0; sT = 0
    for i in range(cnt):
        c, T3, its, n, edom = check(*rand_free(rng, dm, wm, gm))
        for k in tot: tot[k] += c[k]
        mT = max(mT, T3); mn = max(mn, n); ne += edom; sT += T3
    lab = "T3" if ALG == "xi" else "F"
    print(f"FREEREACH104 alg {ALG} seed {seed} genomes {cnt} d<={dm} w<={wm} deg<={gm}{' CTRL ' + str(CTRL) if CTRL else ''}: " + " ".join(f"{k} {v}" for k, v in tot.items())
          + f" | max {lab} {mT} sum {lab} {sT} max |V| {mn} edomok {ne}", flush=True)
