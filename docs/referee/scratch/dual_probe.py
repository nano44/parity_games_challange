#!/usr/bin/env python3
"""REFEREE succ. 11 probe for packet P-N5-DUAL (docs/new/P-N5-DUAL-box43.md, pin df073cb5, sha1 a51f7c30...).
Own engine only (rl_engine: SPEC S1-S5 from the text; no lane code). run5(g, start, odd_first) is rl_engine.run with S4c's side rule
as a parameter: N5 (Even first) or N5^OF (Odd first). Checks:
 DUAL    N5 on G from (s0, t0) == mirror of N5^OF on G^d from (t0, s0), statewise, same length
 PLAIN   N5 on G^d from (t0, s0) vs that mirror: first differing state; must be > j where j -> j+1 is G's first two-sided fallback
         (and no difference if G's run has none)
 OM2     Omega + 2 invariance: N5 on G and on G with Omega + 2 give the same run
 MIR_A   on C^1E games: sigma changes <= d_e - 1, dual phases <= n(n-1) + d_e
 PHIK    every game: distinct tau's <= prod deg(o_i), phases <= n(n-1) + prod deg(o_i)
 END     ENDGAME: I_sigma = {} at k => sigma constant from k on; I_tau = {} at k => tau constant from k on
 MOFC    MIRROR (c): on C^1O games, the first N5^OF phase from a state is a prefix of the first N5 phase from it (sampled states)
Usage: dual_probe.py lib | rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run5(g, start, odd_first=False, maxit=100000):
    """rl_engine.run, verbatim except that S4c's side is Odd's first when odd_first and I_tau != {}."""
    gd = g.dual()
    s, t = list(start[0]), list(start[1])
    out = []
    for _ in range(maxit):
        Xi, sb = RE.evaluate(g, s)
        tt = [t[v] if g.owner[v] == 1 else None for v in range(g.n)]
        Ut, tb = RE.evaluate(gd, tt)
        Is = RE.improving(g, Xi, s, 0)
        It = [(v, w) for v in range(g.n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
        st = dict(s=list(s), t=list(t), Is=Is, It=It, Xi=Xi, Ut=Ut, fb=None)
        out.append(st)
        if not Is and not It: return out
        if Is:
            A = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
            for v, w in Is: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
            _, ch = RE.evaluate(g.restrict(keep).dual(), [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
            sn = [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]
        else: sn = list(s)
        if It:
            A = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
            for v, w in It: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
            _, ch = RE.evaluate(g.restrict(keep), s)
            tn = [ch[v] if g.owner[v] == 1 else None for v in range(g.n)]
        else: tn = list(t)
        if sn == s and tn == t:
            even = bool(Is) and not (odd_first and It)
            st["fb"] = ("E" if even else "O") + ("2" if Is and It else "1")
            if even:
                for v in range(g.n):
                    cand = [w for (x, w) in Is if x == v]
                    if cand: sn[v] = max(cand, key=lambda w: (g.key(Xi[w]), w))
            else:
                for v in range(g.n):
                    cand = [w for (x, w) in It if x == v]
                    if cand: tn[v] = max(cand, key=lambda w: (gd.key(Ut[w]), w))
        s, t = sn, tn
    raise RuntimeError("maxit")


def mirror(st):
    return [(a["t"], a["s"]) for a in st]


def norm(g, s, t):
    return (tuple(s[v] if g.owner[v] == 0 else None for v in range(g.n)), tuple(t[v] if g.owner[v] == 1 else None for v in range(g.n)))


def check(g, start, cnt, name, rng):
    n = g.n; gd = g.dual()
    A = run5(g, start)
    dstart = ([start[1][v] if gd.owner[v] == 0 else None for v in range(n)], [start[0][v] if gd.owner[v] == 1 else None for v in range(n)])
    B = run5(gd, dstart, odd_first=True)
    C = run5(gd, dstart)
    cnt["runs"] += 1
    ma = [norm(g, a["s"], a["t"]) for a in A]
    mb = [norm(g, b["t"], b["s"]) for b in B]
    mc = [norm(g, c["t"], c["s"]) for c in C]
    if ma != mb: fail(cnt, "DUAL", name, len(A), len(B))
    two = [k for k, a in enumerate(A) if a["fb"] and a["fb"].endswith("2")]
    cnt["two_sided_fb"] += len(two); cnt["runs_with_two_sided"] += bool(two)
    first = next((k for k in range(min(len(ma), len(mc))) if ma[k] != mc[k]), None)
    if first is None and len(ma) != len(mc): first = min(len(ma), len(mc))
    if first is not None:
        cnt["plain_differs"] += 1
        if not two or first <= two[0]: fail(cnt, "PLAIN_early", name, first, two[:1])
        if two and first != two[0] + 1: cnt["plain_first_diff_later_than_j+1"] += 1
    # Omega + 2
    g2 = RE.Game([p + 2 for p in g.prio], g.owner, g.succ)
    if [norm(g, a["s"], a["t"]) for a in run5(g2, start)] != ma: fail(cnt, "OM2", name)
    # ENDGAME
    for k, a in enumerate(A):
        if not a["Is"] and any(A[j]["s"] != a["s"] for j in range(k, len(A))): fail(cnt, "END_s", name, k)
        if not a["It"] and any(A[j]["t"] != a["t"] for j in range(k, len(A))): fail(cnt, "END_t", name, k)
    # phases, tau's, Phi-kO
    odd_ch = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    ev_ch = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
    lam = [tuple(x[0] for x in a["Xi"]) for a in A]; lamU = [tuple(x[0] for x in a["Ut"]) for a in A]
    ph = 1 + sum(lam[k] != lam[k + 1] or A[k]["t"] != A[k + 1]["t"] for k in range(len(A) - 1))
    dph = 1 + sum(lamU[k] != lamU[k + 1] or A[k]["s"] != A[k + 1]["s"] for k in range(len(A) - 1))
    pO = 1
    for v in odd_ch: pO *= len(g.succ[v])
    pE = 1
    for v in ev_ch: pE *= len(g.succ[v])
    taus = len({tuple(a["t"]) for a in A}); sigs = len({tuple(a["s"]) for a in A})
    cnt["PHIK_chk"] += 1
    if taus > pO or ph > n * (n - 1) + pO: fail(cnt, "PHIK", name, taus, ph, pO)
    if sigs > pE or dph > n * (n - 1) + pE: fail(cnt, "PHIK_mirror", name, sigs, dph, pE)
    if len(ev_ch) == 1:
        cnt["MIR_A_chk"] += 1
        sch = sum(A[k]["s"] != A[k + 1]["s"] for k in range(len(A) - 1))
        if sch > len(g.succ[ev_ch[0]]) - 1 or dph > n * (n - 1) + len(g.succ[ev_ch[0]]): fail(cnt, "MIR_A", name, sch, dph)
    # MIRROR (c) on C^1O, sampled states as starts
    if len(odd_ch) == 1:
        for k in rng.sample(range(len(A)), min(3, len(A))):
            x = (A[k]["s"], A[k]["t"])
            N = run5(g, x); O = run5(g, x, odd_first=True)
            def first_phase(R):
                L = [tuple(y[0] for y in a["Xi"]) for a in R]; j = 0
                while j + 1 < len(R) and L[j + 1] == L[j] and R[j + 1]["t"] == R[j]["t"]: j += 1
                return [norm(g, a["s"], a["t"]) for a in R[:j + 1]]
            fN, fO = first_phase(N), first_phase(O)
            cnt["MOFC_chk"] += 1
            if fO != fN[:len(fO)]: fail(cnt, "MOFC", name, k)
    cnt["max_len"] = max(cnt["max_len"], len(A))


def rand_ck(rng, n, k):
    while True:
        prio = rng.sample(range(2 * n), n); owner = [rng.randrange(2) for _ in range(n)]
        succ = [rng.sample(range(n), rng.randint(1, min(4, n))) for _ in range(n)]
        g = RE.Game(prio, owner, succ)
        if sum(1 for v in range(n) if owner[v] == 1 and len(g.succ[v]) > 1) == k: return g


def rand_start(g, rng):
    return ([rng.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)],
            [rng.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)])


def main(a):
    rng = random.Random(4301); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        gs = []
        for i in range(N):
            g = rand_ck(r2, r2.randint(lo, hi), r2.randint(0, km))
            if r2.random() < 0.3:  # also C^1E games: flip owners of a C^1O-like draw
                g = g.dual()
            gs.append(("rand%d" % i, g))
    else:
        files = RP.lib() if a == ["lib"] else a
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in files]
    nr = int(os.environ.get("RANDSTARTS", "0"))
    for name, g in gs:
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        starts = [RE.best_reward_start(g)] + [rand_start(g, random.Random(name + str(i))) for i in range(nr)]
        for st in starts:
            try: check(g, st, cnt, name, rng)
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-36s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
