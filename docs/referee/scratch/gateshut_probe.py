#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-MPGS Part (B), Lemma GATE-SHUT (docs/lit/P-N5-MPGS.md, sha1 24913a7f..., freeze l-lit a23179b0).
Own engine only (rl_engine; no L-COMP / L-LIT import). On EVERY game: at every state t of an N5 run, for every Odd e with h := tau(e), every
successor d != h, search a simple route pi of EVEN vertices from d with an edge pi_m -> e such that (H1) every vertex of Q = pi + {e} ranks above
c_h (cycle node of Xi_tau(h)), (H2) the (taubar, tau)-play rho from h meets no vertex of Q, (H3) the top-ranked vertex of Q has even priority.
If one exists: LEMMA (e, d) not in I_tau(t); COR tau_{t+1}(e) != d. Also B1 (dual order reverses the set order on equal cycle nodes) on every
pair of dual valuations at the state with equal cycle nodes, and B2 (Xi_tau(d) <=_d V^d_{tau, sigma'}(d) for the deviation sigma') at each hit.
Mutations (search relaxed, so the hypothesis no longer holds): MUT=1 drop (H3); MUT=2 drop (H2); MUT=3 drop (H1).
Usage: gateshut_probe.py rand N nmin nmax kmax seed | files...  (RANDSTARTS 2, MAXN 40, BUDGET 4000 DFS nodes per (e, d))"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, core_probe as CP
MUT = int(os.environ.get("MUT", "0")); BUDGET = int(os.environ.get("BUDGET", "4000"))
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 20: EX.append((key,) + info)


def find_route(g, d, e, rho, rc):
    """a simple route of Even vertices pi_1 = d, ..., pi_m with pi_m -> e, satisfying the (possibly relaxed) hypotheses"""
    ok_rank = lambda u: MUT == 3 or g.rank[u] > rc
    ok_rho = lambda u: MUT == 2 or u not in rho
    if g.owner[d] != 0 or not ok_rank(e) or not ok_rho(e): return None
    budget = [BUDGET]
    def top_even(path):
        top = max(path + [e], key=lambda u: g.rank[u]); return g.prio[top] % 2 == 0
    def dfs(path, seen):
        budget[0] -= 1
        if budget[0] < 0: return None
        x = path[-1]
        if e in g.succ[x] and (MUT == 1 or top_even(path)): return list(path)
        for y in g.succ[x]:
            if y not in seen and g.owner[y] == 0 and ok_rank(y) and ok_rho(y):
                seen.add(y); r = dfs(path + [y], seen); seen.discard(y)
                if r: return r
        return None
    if not ok_rank(d) or not ok_rho(d): return None
    return dfs([d], {d, e})


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n; gd = g.dual()
    for k, x in enumerate(st):
        t = x["t"]; tt = [t[v] if g.owner[v] == 1 else None for v in range(n)]
        Ut, tb = RE.evaluate(gd, tt)
        if Ut != x["Ut"]: fail(cnt, "UT", name, k)
        It = {(v, w) for (v, w) in x["It"]}
        nx = [tb[v] if g.owner[v] == 0 else t[v] for v in range(n)]   # (taubar, tau)
        # B1 on the state's dual valuations with equal cycle nodes
        byc = {}
        for v in range(n): byc.setdefault(Ut[v][0], []).append(Ut[v])
        for c, vals in byc.items():
            for i in range(len(vals)):
                for j in range(i + 1, min(len(vals), i + 6)):
                    X, Y = vals[i], vals[j]
                    if X[1] == Y[1]: continue
                    cnt["B1_chk"] += 1
                    if (gd.key(X) < gd.key(Y)) != (g.key(Y) < g.key(X)): fail(cnt, "B1", name, k, c)
        for e in range(n):
            if g.owner[e] != 1 or len(g.succ[e]) < 2: continue
            h = t[e]; ch = Ut[h][0]; rc = g.rank[ch]
            pre, cy = RE.lasso(nx, h); rho = set(pre) | set(cy)
            for dd in g.succ[e]:
                if dd == h: continue
                cnt["PAIRS"] += 1
                pi = find_route(g, dd, e, rho, rc)
                if pi is None: continue
                cnt["HYP"] += 1
                if (e, dd) in It: fail(cnt, "LEMMA" + ("_MUT%d" % MUT if MUT else ""), name, k, e, dd, pi)
                if k + 1 < len(st):
                    cnt["COR_chk"] += 1
                    if st[k + 1]["t"][e] == dd: fail(cnt, "COR" + ("_MUT%d" % MUT if MUT else ""), name, k, e, dd)
                if MUT == 0:   # B2: the deviation sigma' and its dual value at d
                    sp = list(nx)
                    for a, b in zip(pi, pi[1:] + [e]): sp[a] = b
                    V = RE.play_value(gd, sp, dd); cnt["B2_chk"] += 1
                    if not gd.key(Ut[dd]) <= gd.key(V): fail(cnt, "B2", name, k, e, dd)
                    if not gd.key(V) < gd.key(Ut[h]): fail(cnt, "STEP4", name, k, e, dd)
                    if len(pi) >= 2: cnt["HYP_m2"] += 1


def main(a):
    cnt = Counter(); rng = random.Random(3434); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"
            ex = CP.parse_start(g, sp) if os.path.exists(sp) else None
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
