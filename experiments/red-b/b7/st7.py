#!/usr/bin/env python3
"""L-RED-B B7 engine self-tests.
  bf SEED COUNT NMAX   the valuation routine against the DEFINITION: random games, random Even strategies; every positional
                       Odd strategy is enumerated, the play valuation theta_{sigma,tau,v} is computed by walking the play, and
                       the engine's (val, tau) must satisfy: val[v] = theta_{sigma,tau_engine,v} for every v, and
                       val[v] <= theta_{sigma,tau',v} for every tau' and v (pointwise minimum).  Counters bfval, bfmin (must 0).
  sol SEED COUNT NMAX  full runs (rules howard and rf, random starts) on random games: regions against own Zielonka (zwrong),
                       strategies by own check (swrong: region closed for its winner's strategy, no cycle won by the loser).
  howard NMAX [ver]    Howard (switch-best everywhere) on Friedmann's G_n from iota: iterations against 9 * 2^n - 10.
Control: B7_CTRL=1 makes the engine's Odd pick a WRONG successor at one vertex in bf (counters must fire);
         B7_CTRL=2 flips one region bit in sol (zwrong must fire)."""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from si7 import Game, Engine, howard, root_first, EVEN, ODD
import gens7

CTRL = int(os.environ.get("B7_CTRL", "0"))


def rand_game(rng, n):
    prio = [rng.randrange(0, max(2, n + 2)) for _ in range(n)]
    owner = [rng.randrange(2) for _ in range(n)]
    succ = []
    for v in range(n):
        k = rng.randint(1, min(n, 3))
        succ.append(rng.sample(range(n), k))
    return Game(prio, owner, succ)


def theta(E, sigma, tau, v):
    """the definition: walk the play, find the cycle, its most relevant vertex w1, the path to w1."""
    path = []; pos = {}
    x = v
    while x not in pos:
        pos[x] = len(path); path.append(x)
        x = sigma[x] if E.owner[x] == EVEN else tau[x]
    cyc = path[pos[x]:]
    w = max(cyc, key=lambda y: E.rank[y])
    # play = v1 .. vk (w1 .. wl)^omega with v_i != w1: k = first position of w1
    y = v; k = 0; W = 0
    while y != w:
        if E.rank[y] > E.rank[w]:
            W += E.sbit[y]
        y = sigma[y] if E.owner[y] == EVEN else tau[y]; k += 1
    return (w, W, k)


def zielonka(g):
    """own recursive Zielonka (max parity). Returns region list (0 = Even wins)."""
    n = g.n
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in g.succ[v]:
            pred[w].append(v)

    def attr(S, U, pl):
        A = set(U); cnt = {}
        st = list(U)
        while st:
            x = st.pop()
            for y in pred[x]:
                if y in S and y not in A:
                    if g.owner[y] == pl:
                        A.add(y); st.append(y)
                    else:
                        c = cnt.get(y)
                        if c is None:
                            c = sum(1 for z in g.succ[y] if z in S)
                        c -= 1; cnt[y] = c
                        if c == 0:
                            A.add(y); st.append(y)
        return A

    def solve(S):
        if not S:
            return set(), set()
        p = max(g.prio[v] for v in S); pl = p & 1
        U = {v for v in S if g.prio[v] == p}
        A = attr(S, U, pl)
        W = solve(S - A)
        if not W[1 - pl]:
            res = [set(), set()]; res[pl] = set(S); return res[0], res[1]
        B = attr(S, W[1 - pl], 1 - pl)
        W2 = solve(S - B)
        res = [set(), set()]; res[pl] = W2[pl]; res[1 - pl] = W2[1 - pl] | B
        return res[0], res[1]

    sys.setrecursionlimit(100000)
    W0, W1 = solve(set(range(n)))
    return [0 if v in W0 else 1 for v in range(n)]


def strat_ok(g, reg, sigma, tau):
    """own check of both strategies: on region i, player i's strategy keeps the play inside and no reachable cycle has a
    most relevant vertex of the other parity (checked per vertex: no cycle through u inside vertices of priority <= pr(u))."""
    n = g.n
    for pl in (0, 1):
        S = [v for v in range(n) if reg[v] == pl]
        Sset = set(S)
        out = {}
        for v in S:
            if g.owner[v] == pl:
                ch = sigma[v] if pl == 0 else tau[v]
                if ch not in g.succ[v] or ch not in Sset:
                    return False
                out[v] = [ch]
            else:
                if any(w not in Sset for w in g.succ[v]):
                    return False
                out[v] = g.succ[v]
        for u in S:
            if g.prio[u] % 2 == pl:
                continue
            seen = set(); st = [u]
            while st:
                x = st.pop()
                for y in out[x]:
                    if y == u:
                        return False
                    if g.prio[y] <= g.prio[u] and y not in seen:
                        seen.add(y); st.append(y)
    return True


def bf(seed, count, nmax):
    rng = random.Random(seed); bfval = bfmin = cases = taus = 0
    for _ in range(count):
        n = rng.randint(2, nmax); g = rand_game(rng, n); E = Engine(g)
        sigma = [rng.choice(g.succ[v]) if g.owner[v] == EVEN else -1 for v in range(n)]
        val, tau = E.evaluate(sigma)
        if CTRL == 1:
            cand = [v for v in range(n) if g.owner[v] == ODD and len(g.succ[v]) > 1]
            if cand:
                v = cand[0]; tau = list(tau); tau[v] = [w for w in g.succ[v] if w != tau[v]][0]
        cases += 1
        mine = [theta(E, sigma, tau, v) for v in range(n)]
        bfval += sum(1 for v in range(n) if mine[v] != val[v])
        odd = [v for v in range(n) if g.owner[v] == ODD]
        for choice in itertools.product(*[g.succ[v] for v in odd]):
            t2 = [-1] * n
            for v, w in zip(odd, choice):
                t2[v] = w
            taus += 1
            for v in range(n):
                if E.key(theta(E, sigma, t2, v)) < E.key(val[v]):
                    bfmin += 1
    print(f"B7 st7 bf seed {seed} games {cases} nmax {nmax} Odd strategies {taus} ctrl {CTRL}: bfval {bfval} bfmin {bfmin}")
    return bfval + bfmin


def sol(seed, count, nmax):
    rng = random.Random(seed); zwrong = swrong = runs = 0; maxit = 0
    for _ in range(count):
        n = rng.randint(2, nmax); g = rand_game(rng, n); E = Engine(g); ref = zielonka(g)
        for name, rule in (("howard", howard()), ("rf", root_first())):
            s0 = [rng.choice(g.succ[v]) if g.owner[v] == EVEN else -1 for v in range(n)]
            its, sigma, val, tau = E.run(s0, rule, maxit=100000)
            runs += 1; maxit = max(maxit, its)
            reg = E.regions(val)
            if CTRL == 2:
                reg[0] ^= 1
            zwrong += int(reg != ref)
            swrong += int(not strat_ok(g, reg, sigma, tau))
    print(f"B7 st7 sol seed {seed} games {count} nmax {nmax} runs {runs} max iterations {maxit} ctrl {CTRL}: zwrong {zwrong} swrong {swrong}")
    return zwrong + swrong


def how(nmax, ver):
    bad = 0
    for n in range(1, nmax + 1):
        g, s0 = gens7.lmcs(n, ver); E = Engine(g)
        res = []
        for tie in ("low", "high"):
            its, sigma, val, tau = E.run(s0, howard(tie))
            reg = E.regions(val)
            ok = reg == zielonka(g) and strat_ok(g, reg, sigma, tau) and all(r == 1 for r in reg)
            res.append((its, ok))
            bad += int(its != 9 * 2 ** n - 10) + int(not ok)
        print(f"B7 st7 howard lmcs {ver} n {n} |V| {g.n} |E| {g.m}: iterations tie-low {res[0][0]} tie-high {res[1][0]} "
              f"formula 9*2^n-10 {9 * 2 ** n - 10} regions+strategies ok {int(res[0][1] and res[1][1])}", flush=True)
    return bad


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "bf": bad = bf(int(a[1]), int(a[2]), int(a[3]))
    elif a[0] == "sol": bad = sol(int(a[1]), int(a[2]), int(a[3]))
    elif a[0] == "howard": bad = how(int(a[1]), a[2] if len(a) > 2 else "fig4")
    sys.exit(1 if bad else 0)
