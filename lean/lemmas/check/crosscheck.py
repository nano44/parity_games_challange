#!/usr/bin/env python3
"""Cross-check of the Lean definitions in ../PGLemmas/Defs.lean against the fleet's valuation engine
experiments/si/si.py (class Engine: Friedmann arXiv 1106.0778 section 3).

The functions below transcribe Defs.lean line by line (OnCycle, lam, plen, pset, val, rew, setLt, Val.lt) and
Statements6.lean's OptCounter.  They are NOT the Lean code; a match shows only that the definitions, read as written,
denote the valuation and the order the fleet's runs use.

Counters (all must be 0):
  valdiff  my val(pair(sigma, tau)) at a vertex differs from Engine.evaluate(sigma)'s value (tau = the engine's counterstrategy)
  orddiff  Val.lt disagrees with the engine's key order on a pair of values
  optfail  the engine's counterstrategy is not an OptCounter (some Odd strategy gives some vertex a strictly smaller value)
Control (CTRL=1): plen is read one too long; valdiff must fire.
Usage: crosscheck.py SEED GAMES NMAX   (run from the repository root)"""
import itertools, os, random, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si"))
import pg, si

CTRL = os.environ.get("CTRL") == "1"

def iterate(s, k, v):
    for _ in range(k):
        v = s[v]
    return v

def on_cycle(s, v):                     # OnCycle s v u: (exists n, s^[n] v = u) and (exists p > 0, s^[p] u = u)
    n = len(s)
    reach = {iterate(s, k, v) for k in range(2 * n)}
    return {u for u in reach if any(iterate(s, p, u) == u for p in range(1, n + 1))}

def lam(pr, s, v):                      # a vertex of largest priority on the cycle
    return max(on_cycle(s, v), key=lambda u: pr[u])

def plen(pr, s, v):                     # Nat.find: the first n with s^[n] v = lam
    l, k = lam(pr, s, v), 0
    while iterate(s, k, v) != l:
        k += 1
    return k + 1 if CTRL else k

def pset(pr, s, v):                     # {u | pr lam < pr u and exists j < plen, s^[j] v = u}
    l = lam(pr, s, v)
    return frozenset(u for u in (iterate(s, j, v) for j in range(plen(pr, s, v))) if pr[l] < pr[u])

def val(pr, s, v):
    return (lam(pr, s, v), pset(pr, s, v), plen(pr, s, v))

def rew(pr, v):
    return pr[v] if pr[v] % 2 == 0 else -pr[v]

def set_lt(pr, M, N):                   # exists d in M symmdiff N, maximal, with (d in N and even) or (d in M and odd)
    D = M ^ N
    if not D:
        return False
    d = max(D, key=lambda u: pr[u])
    return (d in N and pr[d] % 2 == 0) or (d in M and pr[d] % 2 == 1)

def val_lt(pr, x, y):
    (xt, xs, xl), (yt, ys, yl) = x, y
    return (rew(pr, xt) < rew(pr, yt) or (xt == yt and set_lt(pr, xs, ys))
            or (xt == yt and xs == ys and xl < yl and pr[xt] % 2 == 1)
            or (xt == yt and xs == ys and yl < xl and pr[xt] % 2 == 0))

def val_le(pr, x, y):
    return val_lt(pr, x, y) or x == y

def random_game(rng, nmax):
    n = rng.randint(2, nmax)
    prio = [rng.randint(0, n) for _ in range(n)]
    owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)]
    return pg.Game(prio, owner, succ)

def main():
    seed, games, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    valdiff = orddiff = optfail = 0
    nval = nord = nopt = 0
    for _ in range(games):
        g = random_game(rng, nmax)
        e = si.Engine(g)
        n, pr = g.n, e.pp                     # e.pp: the engine's injective priorities (2*rank + parity)
        even = [v for v in range(n) if g.owner[v] == si.EVEN]
        odd = [v for v in range(n) if g.owner[v] == si.ODD]
        for _ in range(3):
            strat = tuple(rng.choice(e.succ[v]) if g.owner[v] == si.EVEN else -1 for v in range(n))
            ev, tau = e.evaluate(strat)
            s = [strat[v] if g.owner[v] == si.EVEN else tau[v] for v in range(n)]
            mine = [val(pr, s, v) for v in range(n)]
            for v in range(n):                # valuation
                w, mask, ln = ev[v]
                theirs = (w, frozenset(u for u in range(n) if mask & e.bit[u]), ln)
                nval += 1
                valdiff += mine[v] != theirs
            for a in range(n):                # order
                for b in range(n):
                    nord += 1
                    orddiff += (e.key(ev[a]) < e.key(ev[b])) != val_lt(pr, mine[a], mine[b])
            if n <= 6:                        # OptCounter: every Odd strategy along the edges
                for choice in itertools.product(*[e.succ[u] for u in odd]):
                    s2 = list(s)
                    for u, w in zip(odd, choice):
                        s2[u] = w
                    for v in range(n):
                        nopt += 1
                        optfail += not val_le(pr, mine[v], val(pr, s2, v))
    print(f"seed {seed} games {games} nmax {nmax} ctrl {int(CTRL)}: values {nval} valdiff {valdiff}; "
          f"pairs {nord} orddiff {orddiff}; optchecks {nopt} optfail {optfail}")
    return 0 if (valdiff == orddiff == optfail == 0) != CTRL else 1

if __name__ == "__main__":
    sys.exit(main())
