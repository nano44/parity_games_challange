#!/usr/bin/env python3
"""REFEREE succ. 8 probe for packet P-N5-P1 (docs/si/P-N5-P1-box10.md, pin 48a8a4c, sha1 b98ca794...). Own code (rl_engine.py for
play values, ranks and SPEC S1's key; no si.py). On random one-player games (every Odd vertex out-degree 1, asserted):
 ORD     the packet's REAL order (clauses (i)-(iii), symmetric-difference form) equals SPEC S1's key order, on all value pairs that occur
 LB      Lemma B: extended order via the packet's vector map is total/antisymmetric on random extended values, and equals the real order
         on set-valued ones; Lemma M on random pairs
 ENG     SPEC's Xi_sigma (own VJ procedure) equals the play valuation V_sigma (one-player game)
 P1      every positional Even strategy with no improving edge (SPEC S2) is pointwise >= every positional Even strategy (all enumerated)
 S3/S5   for improvement-free sigma: rew(c(y)) <= rew(c(x)) on every edge; every simple cycle of H with constant c(.) = c0 has top t
         with rew(t) <= rew(c0), equality only if t = c0
 CTRL    a control: strategies WITH an improving edge that are not optimal (must exist; shows the check can fail)
Usage: p1_probe.py N nmin nmax seed [maxstrat]"""
import sys, os, random, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE


def real_lt(g, a, b):
    """packet §1: a < b (b better for Even)"""
    (c, P, l), (c2, P2, l2) = a, b
    if g.rew[c] != g.rew[c2]: return g.rew[c] < g.rew[c2]
    if P != P2:
        d = P ^ P2; r = d.bit_length() - 1; h = g.byrank[r]
        return (g.prio[h] % 2 == 0 and (P2 >> r) & 1) or (g.prio[h] % 2 == 1 and (P >> r) & 1)
    if l != l2: return l < l2 if g.prio[c] % 2 else l > l2
    return False


def vec(g, x):
    """packet Lemma B (a): (rew(c), eps_1 mu(h_1), ..., eps_c l), h_i by decreasing rank above c; mu = dict rank->mult"""
    c, mu, l = x
    hs = [r for r in range(g.n - 1, g.rank[c], -1)]
    return (g.rew[c],) + tuple((1 if g.prio[g.byrank[r]] % 2 == 0 else -1) * mu.get(r, 0) for r in hs) + \
        ((-1 if g.prio[c] % 2 == 0 else 1) * l,)


def ext_lt(g, a, b):
    """packet (i), (ii'), (iii) on extended values"""
    (c, mu, l), (c2, mu2, l2) = a, b
    if g.rew[c] != g.rew[c2]: return g.rew[c] < g.rew[c2]
    diff = [r for r in set(mu) | set(mu2) if mu.get(r, 0) != mu2.get(r, 0)]
    if diff:
        r = max(diff); h = g.byrank[r]
        return (g.prio[h] % 2 == 0 and mu.get(r, 0) < mu2.get(r, 0)) or (g.prio[h] % 2 == 1 and mu.get(r, 0) > mu2.get(r, 0))
    if l != l2: return l < l2 if g.prio[c] % 2 else l > l2
    return False


def rand_1p(rng, n):
    prio = rng.sample(range(2 * n), n); owner = [rng.randrange(2) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, min(3, n))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = RE.Game(prio, owner, succ)
    assert all(len(g.succ[v]) == 1 for v in range(n) if g.owner[v] == 1)
    return g


def simple_cycles(g, limit=4000):
    out = []
    n = g.n
    def dfs(start, v, path, onp):
        if len(out) >= limit: return
        for w in g.succ[v]:
            if w == start: out.append(list(path))
            elif w > start and w not in onp:
                onp.add(w); path.append(w); dfs(start, w, path, onp); path.pop(); onp.discard(w)
    for s in range(n): dfs(s, s, [s], {s})
    return out


def main():
    N, lo, hi, seed = map(int, sys.argv[1:5]); maxs = int(sys.argv[5]) if len(sys.argv) > 5 else 5000
    rng = random.Random(seed); cnt = Counter()
    for _ in range(N):
        g = rand_1p(rng, rng.randint(lo, hi)); n = g.n
        Ev = [v for v in range(n) if g.owner[v] == 0]
        nstrat = 1
        for v in Ev: nstrat *= len(g.succ[v])
        if nstrat > maxs: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        strats, vals = [], []
        for ch in itertools.product(*[g.succ[v] for v in Ev]):
            s = [None] * n
            for v, w in zip(Ev, ch): s[v] = w
            nx = [s[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(n)]
            strats.append(s); vals.append([RE.play_value(g, nx, v) for v in range(n)])
        cnt["strategies"] += len(strats)
        # ORD on occurring values
        allv = list({x for V in vals for x in V})
        for _ in range(min(200, len(allv) ** 2)):
            a, b = rng.choice(allv), rng.choice(allv)
            cnt["ORD_chk"] += 1
            if real_lt(g, a, b) != (g.key(a) < g.key(b)): cnt["ORD_FAIL"] += 1
        # best = pointwise max by key
        best = [max((V[v] for V in vals), key=g.key) for v in range(n)]
        for i, (s, V) in enumerate(zip(strats, vals)):
            if i < 20:  # ENG: own VJ evaluate equals play values
                Xi, _ = RE.evaluate(g, s); cnt["ENG_chk"] += 1
                if Xi != V: cnt["ENG_FAIL"] += 1
            imp = any(w != s[v] and g.key(V[w]) > g.key(V[s[v]]) for v in Ev for w in g.succ[v])
            opt = all(V[v] == best[v] for v in range(n))
            if not imp:
                cnt["P1_impfree"] += 1
                if not opt: cnt["P1_FAIL"] += 1; print("P1 violation", g.prio, g.owner, g.succ, s)
                # S3
                c = [V[v][0] for v in range(n)]
                for x in range(n):
                    for y in g.succ[x]:
                        cnt["S3_chk"] += 1
                        if g.rew[c[y]] > g.rew[c[x]]: cnt["S3_FAIL"] += 1
                for C in simple_cycles(g):
                    if len({c[y] for y in C}) != 1: continue
                    c0 = c[C[0]]; t = max(C, key=lambda u: g.rank[u]); cnt["S5_chk"] += 1
                    if g.rew[t] > g.rew[c0] or (g.rew[t] == g.rew[c0] and t != c0): cnt["S5_FAIL"] += 1
                    cnt["S5_c0_in_C"] += c0 in C
            else:
                cnt["CTRL_imp"] += 1; cnt["CTRL_imp_nonopt"] += not opt
                cnt["imp_but_opt"] += opt
        # Lemma B / M on random extended values over this game's ranks
        for _ in range(100):
            c = rng.randrange(n); above = list(range(g.rank[c] + 1, n))
            def rx():
                cc = c if rng.random() < 0.8 else rng.randrange(n)
                ab = list(range(g.rank[cc] + 1, n))
                return (cc, {r: rng.randint(0, 2) for r in rng.sample(ab, rng.randint(0, len(ab)))} if ab else {}, rng.randint(0, 5))
            a, b = rx(), rx()
            for x in (a, b):
                for r in [r for r in x[1] if x[1][r] == 0]: del x[1][r]
            cnt["LB_chk"] += 1
            la, lb = ext_lt(g, a, b), ext_lt(g, b, a)
            same = (a[0] == b[0] and a[1] == b[1] and a[2] == b[2])
            if la and lb: cnt["LB_ANTISYM_FAIL"] += 1
            if not la and not lb and not same: cnt["LB_TOTAL_FAIL"] += 1
            if la != (vec(g, a) < vec(g, b)) and g.rew[a[0]] == g.rew[b[0]]: cnt["LB_VEC_FAIL"] += 1
            if all(m <= 1 for m in a[1].values()) and all(m <= 1 for m in b[1].values()):
                cnt["LB_set_chk"] += 1
                ma = sum(1 << r for r in a[1]); mb = sum(1 << r for r in b[1])
                if la != real_lt(g, (a[0], ma, a[2]), (b[0], mb, b[2])): cnt["LB_SET_FAIL"] += 1
            if a[0] == b[0]:
                u = rng.randrange(n); cnt["LM_chk"] += 1
                def px(x):
                    mu = dict(x[1])
                    if g.rank[u] > g.rank[x[0]]: mu[g.rank[u]] = mu.get(g.rank[u], 0) + 1
                    return (x[0], mu, x[2] + 1)
                if la and not ext_lt(g, px(a), px(b)): cnt["LM_FAIL"] += 1
    for k in sorted(cnt): print("%-20s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main()
