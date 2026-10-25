#!/usr/bin/env python3
"""Box 43 (L-NEW successor 22): N5 on games with k >= 1 Odd choice vertices (C^kO). Read-only use of box21/n5x.py (N5 step = SPEC
S1-S5, asserted equal to n5.py's counts by n5x.trace(check=True) in --check mode) and L-SI's si.py Engine.
Per run, measures (all DATA):
  it, fb          iterations, fallbacks
  J               joint lambda-runs (maximal runs with (lambda, lambda^U) constant; R47 Lemma Phi: J <= 2n(n-1)+1 on every game)
  T, Tv           transitions that change tau; per Odd choice vertex, the number of transitions changing tau(o_i)
  dtau            distinct tau's on the run (R15 (c),(d) on G^d: no tau repeats, so dtau = T + 1)
  TJ              max tau-changing transitions inside one joint lambda-run
  P, maxP, maxF   phases ((lambda, tau) constant), longest phase (transitions inside it), max fallbacks inside one phase
  prodeg          prod over Odd choice vertices of deg(o_i)  (bound dtau <= prodeg)
Usage: multi.py file.pg [file.pg ...] [--check]     multi.py --rand COUNT NLO NHI K SEED [--forced F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, trace, Engine, pg, dual

def odd_choices(g):
    return [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]

def run(g, start=None, cap=10 ** 5):
    E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = start_pair(g, E, Ed, start)
    states, lam, lamU, fbs = [], [], [], []
    while True:
        vs, _ = E.evaluate(tuple(sigma)); vt, _ = Ed.evaluate(tuple(tau))
        states.append((tuple(sigma), tuple(tau))); lam.append(tuple(x[0] for x in vs)); lamU.append(tuple(x[0] for x in vt))
        if len(states) > cap: break
        r = step(g, E, Ed, sigma, tau)
        if r is None: break
        sigma, tau, _, _, fb, _, _ = r; fbs.append(fb)
    return states, lam, lamU, fbs

def measure(g, states, lam, lamU, fbs):
    O = odd_choices(g); K = len(states) - 1
    m = dict(n=g.n, k=len(O), it=K, fb=sum(fbs))
    tch = [states[i][1] != states[i + 1][1] for i in range(K)]
    m["T"] = sum(tch); m["Tv"] = [sum(states[i][1][o] != states[i + 1][1][o] for i in range(K)) for o in O]
    m["dtau"] = len({s[1] for s in states})
    J = 1; cur = 0; TJ = 0
    P = 1; plen = 0; maxP = 0; pf = 0; maxF = 0
    for i in range(K):
        if (lam[i], lamU[i]) != (lam[i + 1], lamU[i + 1]): J += 1; cur = 0
        elif tch[i]: cur += 1
        TJ = max(TJ, cur)
        if lam[i] != lam[i + 1] or tch[i]: P += 1; plen = 0; pf = 0
        else: plen += 1; pf += fbs[i]
        maxP = max(maxP, plen); maxF = max(maxF, pf)
    p = 1
    for o in O: p *= len(g.succ[o])
    m.update(J=J, TJ=TJ, P=P, maxP=maxP, maxF=maxF, prodeg=p)
    assert m["dtau"] == m["T"] + 1, m        # R15 (c),(d) on G^d: no tau repeats
    return m

def rand_ckO(rng, lo, hi, k, forced=0.15):
    n = rng.randint(max(lo, k + 1), hi); owner = [0] * n
    O = rng.sample(range(n), k)
    for v in O: owner[v] = 1
    for v in range(n):
        if v not in O and rng.random() < forced: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v not in O: succ[v] = succ[v][:1]
    for v in O:
        succ[v] = sorted(set(rng.sample(range(n), min(n, rng.choice((2, 2, 3))))))
        if len(succ[v]) < 2: return None
    return pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ)

def fmt(m): return " ".join(f"{a}={m[a]}" for a in ("n", "k", "it", "fb", "J", "T", "Tv", "TJ", "P", "maxP", "maxF", "prodeg"))

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        cnt, lo, hi, k, seed = map(int, a[1:6]); rng = random.Random(seed)
        forced = float(a[a.index("--forced") + 1]) if "--forced" in a else 0.15
        best = {}
        for c in range(cnt):
            g = rand_ckO(rng, lo, hi, k, forced)
            if g is None: continue
            m = measure(g, *run(g))
            for key in ("it", "T", "TJ", "maxP", "maxF"):
                if key not in best or m[key] > best[key][0]: best[key] = (m[key], fmt(m))
        for key, (v, s) in best.items(): print(f"max {key} = {v}: {s}")
    else:
        for f in [x for x in a if not x.startswith("--")]:
            g = load(f)
            if "--check" in a: trace(g, check=True)
            print(f, fmt(measure(g, *run(g))))
