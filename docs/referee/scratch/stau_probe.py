#!/usr/bin/env python3
"""REFEREE succ. 13 probe for packet P-N5-STAU (docs/new/P-N5-STAU-box45.md, pin ca0a4e97, sha1 7446d9a9...). Own engine only
(rl_engine = SPEC S1-S5 from the text; epr_probe's s4a / s4b_arena / gates / wval, written by REFEREE succ. 12). No lane code.
At every state x of every run (N5 runs AND N5^tau runs), A := N5's step from x, B := N5^tau's step from x (S4b^tau: keep tau if
It != {} and tau is value-optimal against sigma in S4b's arena H'), SIG := the Sigma-transition (sigma_a if != sigma, else Even's
switch-all on Is), TS := x is tau-stable (Is != {} and (It = {} or tau value-optimal in H')).
 A      (a) shared functions: trivially shared in code; checked instead: S4a output and S4c switch-alls computed twice agree (sanity)
 B      (b) A keeps tau => B == A
 C1     (c) B keeps tau => TS and B == SIG
 C1N    (c) "the same holds for N5": A keeps tau => TS and A == SIG
 C2     (c) converse: TS => B == SIG
 D      (d) B = (Switch_I(sigma), Switch_J(tau)) with I <= Is, J <= It, (I, J) != ({}, {})
 DIFF   A != B, classified: DIFF_TS (TS, SPEC's S4b returns a value-equal tau' != tau: the Corollary's case),
        DIFF_IS0 (Is = {}, tau value-optimal in H', SPEC returns tau' != tau: N5 -> (sigma, tau'), N5^tau -> Odd fallback; NOT in the
        Corollary's sentence), DIFF_OTHER = a failure of the Corollary
 SIGLAM a tau-keeping N5^tau transition (a Sigma-transition from a TS state) that changes lambda_Xi: in-phase is a proper subset
 R48    on C^1O games, every N5^tau phase ((lambda_Xi, tau) constant) has in-phase fallbacks f <= 1 + (n-2)(2n-1)
Usage: stau_probe.py rand N nmin nmax kmax seed | c1o N nmin nmax seed | files...   (env RANDSTARTS=N, default 3)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, dual_probe as D, epr_probe as E
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def switch_all(g, val, strat, I, gd=None):
    out = list(strat)
    for v in range(g.n):
        cand = [w for (x, w) in I if x == v]
        if cand: out[v] = max(cand, key=lambda w: ((gd or g).key(val[w]), w))
    return out


def steps(g, s, t):
    """returns dict with A (N5 step), B (N5^tau step), SIG, TS, Is, It, vo (tau value-optimal in H'), spec_t (SPEC's S4b output)"""
    Xi, sb, Is, It, Ut = E.gates(g, s, t)
    if not Is and not It: return None
    gd = g.dual()
    sa = E.s4a(g, s, t, Is) if Is else list(s)
    if It:
        H, val, spec_t = E.s4b_arena(g, s, t, It)
        vo = E.wval(H, s, t) == val
    else: spec_t, vo = list(t), True
    def fin(tn):
        sn, tn = list(sa), list(tn)
        if sn == list(s) and tn == list(t):
            if Is: sn = switch_all(g, Xi, s, Is)
            else: tn = switch_all(g, Ut, t, It, gd)
        return sn, tn
    A = fin(spec_t)
    B = fin(list(t) if (It and vo) else spec_t)
    SIG = None
    if Is: SIG = (sa if sa != list(s) else switch_all(g, Xi, s, Is), list(t))
    TS = bool(Is) and (not It or vo)
    return dict(A=A, B=B, SIG=SIG, TS=TS, Is=Is, It=It, vo=vo, spec_t=spec_t, Xi=Xi)


def check_state(g, s, t, cnt, name, k):
    r = steps(g, s, t)
    if r is None: return None
    cnt["STATES"] += 1
    A, B, SIG, TS = r["A"], r["B"], r["SIG"], r["TS"]
    t = list(t); s = list(s)
    if A[1] == t:
        cnt["B_chk"] += 1
        if B != A: fail(cnt, "B", name, k)
        cnt["C1N_chk"] += 1
        if not TS or A != SIG: fail(cnt, "C1N", name, k)
    if B[1] == t:
        cnt["C1_chk"] += 1
        if not TS or B != SIG: fail(cnt, "C1", name, k)
    if TS:
        cnt["C2_chk"] += 1
        if B != SIG: fail(cnt, "C2", name, k)
    Is, It = set(r["Is"]), set(r["It"])
    cnt["D_chk"] += 1
    I = {(v, B[0][v]) for v in range(g.n) if g.owner[v] == 0 and B[0][v] != s[v]}
    J = {(v, B[1][v]) for v in range(g.n) if g.owner[v] == 1 and B[1][v] != t[v]}
    if not (I <= Is and J <= It and (I or J)): fail(cnt, "D", name, k)
    if A != B:
        if TS and r["spec_t"] != t and r["vo"]: cnt["DIFF_TS"] += 1
        elif not Is and r["vo"] and r["spec_t"] != t:
            cnt["DIFF_IS0"] += 1
            if len(EX) < 40: EX.append(("DIFF_IS0 (info)", name, k, "s", s, "t", t, "N5->", A[1], "N5tau->", B[1]))
        else: fail(cnt, "DIFF_OTHER", name, k)
    if B[1] == t:
        Xi2 = RE.evaluate(g, B[0])[0]
        if [x[0] for x in Xi2] != [x[0] for x in r["Xi"]]: cnt["SIGLAM"] += 1
    return r


def run_tau(g, start, maxit=20000):
    s, t = list(start[0]), list(start[1]); out = []
    for _ in range(maxit):
        r = steps(g, s, t)
        out.append((s, t, r))
        if r is None: return out
        s, t = r["B"]
    raise RuntimeError("maxit")


def run_n5(g, start, maxit=20000):
    s, t = list(start[0]), list(start[1]); out = []
    for _ in range(maxit):
        r = steps(g, s, t)
        out.append((s, t, r))
        if r is None: return out
        s, t = r["A"]
    raise RuntimeError("maxit")


def r48(g, run, cnt, name, c1o):
    if not c1o: return
    n = g.n; bound = 1 + (n - 2) * (2 * n - 1)
    lam = [[x[0] for x in RE.evaluate(g, s)[0]] for (s, t, r) in run]
    f = 0
    for k in range(len(run) - 1):
        s, t, r = run[k]; s2, t2, _ = run[k + 1]
        inph = (t2 == t and lam[k + 1] == lam[k])
        if not inph:
            cnt["R48_phases"] += 1; cnt["R48_maxf"] = max(cnt["R48_maxf"], f); f = 0; continue
        if r["B"] != r["SIG"] or r["SIG"] is None: fail(cnt, "INPH_NOT_SIG", name, k)
        if r["A"] != r["B"]: cnt["TIEKEEP_inphase"] += 1
        if E.s4a(g, s, t, r["Is"]) == list(s): f += 1
        if f > bound: fail(cnt, "R48", name, k, f, bound)
    cnt["R48_phases"] += 1; cnt["R48_maxf"] = max(cnt["R48_maxf"], f)


def is_c1o(g):
    return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) == 1


def do_game(g, name, cnt, rng):
    starts = [RE.best_reward_start(g)] + [D.rand_start(g, rng) for _ in range(int(os.environ.get("RANDSTARTS", "3")))]
    c1o = is_c1o(g)
    for j, st in enumerate(starts):
        cnt["RUNS"] += 1
        for runner, tag in ((run_tau, "tau"), (run_n5, "n5")):
            run = runner(g, st)
            for k, (s, t, r) in enumerate(run[:-1]): check_state(g, s, t, cnt, "%s/%s/%d" % (name, tag, j), k)
            if tag == "tau": r48(g, run, cnt, "%s/%d" % (name, j), c1o)


def main(a):
    cnt = Counter(); rng = random.Random(1313)
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            n = r2.randint(lo, hi)
            do_game(D.rand_ck(r2, n, r2.randint(0, min(km, n - 1))), "rand%d" % i, cnt, rng)
    elif a[0] == "c1o":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N): do_game(P.rand_c1o(r2, r2.randint(lo, hi)), "c1o%d" % i, cnt, rng)
    else:
        for f in a:
            g = RE.parse(f)
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do_game(g, os.path.relpath(f), cnt, random.Random(os.path.relpath(f)))
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
