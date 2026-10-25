#!/usr/bin/env python3
r"""REFEREE-2 successor 8 (Opus 5.5, D15): mechanical check of packet P-N5-P1 (docs/si/P-N5-P1-box10.md sha1 b98ca794 @ trunk 48a8a4c).
Own code: real play values and the real order from my lane's R2-N5-RE/re_check.py (Game.play, Game.key = SPEC S1: reward, signed weight,
length by parity); the extended order is coded HERE from the packet's §1 definition, independently of key(). No lane script (p1check.py,
si.py) is imported. Checks:
  B     Lemma B (b)/(c): on random pairs of REAL values of random games, extended order == real order (both directions, ties).
  BA    Lemma B (a): extended order is antisymmetric / transitive / total on random extended values (multiplicities 0..3).
  M     Lemma M: a <x b  =>  x(+)a <x x(+)b on random extended values.
  P1    Lemma P1: random one-player games, ALL positional Even strategies enumerated; every strategy without an improving edge is
        pointwise >= every strategy. Also Step 5 on every simple cycle (via every strategy's play cycle) and Step 3 on every edge.
  CTRL  negative control: a strategy WITH an improving edge that is nevertheless pointwise optimal is counted (allowed); a non-optimal
        strategy without an improving edge would be a violation.
Usage: p1_check.py N nmin nmax seed [maxstrat]"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import re_check as RC
from collections import Counter

def rew(g, c):
    pp = 2 * g.rank[c] + (0 if g.even[c] else 1)
    return pp if g.even[c] else -pp

def xcmp(g, a, b):
    """extended order (packet §1): a, b = (c, mu (Counter), l). returns -1 / 0 / 1 (1: a better for Even)."""
    (c, mu, l), (c2, mu2, l2) = a, b
    if c != c2: return 1 if rew(g, c) > rew(g, c2) else -1
    diff = [h for h in set(mu) | set(mu2) if mu.get(h, 0) != mu2.get(h, 0)]
    if diff:
        h = max(diff, key=lambda v: g.rank[v])
        better_b = (g.even[h] and mu[h] < mu2[h]) or ((not g.even[h]) and mu[h] > mu2[h])
        return -1 if better_b else 1
    if l == l2: return 0
    if g.even[c]: return 1 if l < l2 else -1
    return 1 if l > l2 else -1

def ext(val): c, P, l = val; return (c, Counter({v: 1 for v in P}), l)

def xplus(g, x, a):
    c, mu, l = a; mu = Counter(mu)
    if g.rank[x] > g.rank[c]: mu[x] += 1
    return (c, mu, l + 1)

def rand_one_player(rng, n):
    owner = [1 if rng.random() < 0.3 else 0 for _ in range(n)]
    prio = [rng.randrange(0, n + 2) for _ in range(n)]
    succ = [[rng.randrange(n)] if owner[v] else rng.sample(range(n), rng.randint(1, min(3, n))) for v in range(n)]
    return RC.Game(prio, owner, succ)

def main():
    N, nmin, nmax, seed = map(int, sys.argv[1:5]); maxs = int(sys.argv[5]) if len(sys.argv) > 5 else 4000
    rng = random.Random(seed); st = Counter(); viol = []
    def bad(m):
        st["VIOLATIONS"] += 1
        if len(viol) < 30: viol.append(m)
    for gi in range(N):
        n = rng.randint(nmin, nmax); g = rand_one_player(rng, n)
        E = [v for v in range(n) if g.owner[v] == 0]
        choices = [g.succ[v] for v in E]
        tot = 1
        for ch in choices: tot *= len(ch)
        if tot > maxs: st["games_skipped"] += 1; continue
        st["games"] += 1
        strats = []
        for pick in itertools.product(*choices):
            f = [g.succ[v][0] for v in range(n)]
            for v, z in zip(E, pick): f[v] = z
            strats.append((f, RC.vals_of(g, f)[0]))
        st["strategies"] += len(strats)
        allvals = [val for _, val in strats]
        # Lemma B (b)/(c) on real values of this game: all pairs within a sample
        sample = [allvals[rng.randrange(len(allvals))][rng.randrange(n)] for _ in range(40)]
        for a in sample:
            for b in sample:
                st["B_pairs"] += 1
                if xcmp(g, ext(a), ext(b)) != g.cmp(a, b): bad(f"g{gi} LemmaB {a} {b}")
        # Lemma B (a) and Lemma M on random extended values with a common or random cycle node
        for _ in range(30):
            c = rng.randrange(n)
            above = [v for v in range(n) if g.rank[v] > g.rank[c]]
            def rx(cc=c):
                ab = [v for v in range(n) if g.rank[v] > g.rank[cc]]
                return (cc, Counter({v: rng.randint(0, 3) for v in ab if rng.random() < 0.5}), rng.randint(0, 5))
            a, b, d = rx(), rx(), rx(rng.randrange(n))
            st["BA_triples"] += 1
            ab, ba = xcmp(g, a, b), xcmp(g, b, a)
            if ab != -ba: bad("BA antisym")
            if ab == 0 and (a[0], {k: v for k, v in a[1].items() if v}, a[2]) != (b[0], {k: v for k, v in b[1].items() if v}, b[2]): bad("BA equal but different")
            if xcmp(g, a, b) >= 0 and xcmp(g, b, d) >= 0 and xcmp(g, a, d) < 0: bad("BA transitivity")
            x = rng.randrange(n)
            if ab < 0:
                st["M_checks"] += 1
                if not xcmp(g, xplus(g, x, a), xplus(g, x, b)) < 0: bad("LemmaM")
        # Lemma P1
        for f, val in strats:
            imp = any(g.cmp(val[z], val[f[v]]) > 0 for v in E for z in g.succ[v] if z != f[v])
            opt = all(all(g.cmp(val[v], v2[v]) >= 0 for v in range(n)) for _, v2 in strats)
            if not imp:
                st["P1_no_improving_edge"] += 1
                if not opt: bad(f"g{gi} P1: no improving edge but not optimal")
                # Step 3 and Step 5 checks
                cnode = [val[v][0] for v in range(n)]
                for v in range(n):
                    for z in g.succ[v]:
                        st["P1_step3_edges"] += 1
                        if rew(g, cnode[z]) > rew(g, cnode[v]): bad(f"g{gi} Step3")
                for f2, _ in strats:
                    for v in range(n):
                        _, _, cyc = g.play(f2, v)
                        cs = {cnode[y] for y in cyc}
                        if len(cs) == 1:
                            st["P1_step5_cycles"] += 1
                            c0 = cs.pop(); t = max(cyc, key=lambda y: g.rank[y])
                            if rew(g, t) > rew(g, c0) or (rew(g, t) == rew(g, c0) and t != c0): bad(f"g{gi} Step5")
            elif opt: st["CTRL_optimal_with_improving_edge"] += 1
            else: st["CTRL_nonoptimal_with_improving_edge"] += 1
    for k in sorted(st): print(f"{k}: {st[k]}")
    for v in viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st["VIOLATIONS"] else "OK", f"violations={st['VIOLATIONS']}")

if __name__ == "__main__":
    main()
