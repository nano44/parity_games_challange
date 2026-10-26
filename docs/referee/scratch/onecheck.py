#!/usr/bin/env python3
"""REFEREE succ. 11 probe for packet P-N5-1O (docs/si/P-N5-1O-box15.md, pin 291c110d, sha1 2cf5e672...). Own code only.
At N5's stop (own engine rl_engine; S3 start and random start pairs), on C^1O games:
 OUT_W     W := {v : Omega(cycle node of Xi_sigma(v)) even} equals Zielonka's W_E (own recursive Zielonka, max-parity, TARGET.md section 1)
 OUT_SIG   sigma wins every v in W: in G_sigma no vertex of W reaches a cycle whose top priority is odd
 OUT_BAR   sigma-bar wins every v not in W: in G_sigmabar no vertex of V \\ W reaches a cycle whose top priority is even
 ITER      iterations <= (n(n-1)+d_o)(T*+1) with T* from the packet's section 2 chain (F = 2n^2)
 FMAX      per phase, in-phase fallbacks <= 2n^2
Usage: onecheck.py lib | rand N nmin nmax seed | files...   (env RANDSTARTS=N)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def attr(g, A, player, sub):
    A = set(A); changed = True
    while changed:
        changed = False
        for v in sub - A:
            ss = [w for w in g.succ[v] if w in sub]
            if (g.owner[v] == player and any(w in A for w in ss)) or (g.owner[v] != player and ss and all(w in A for w in ss)):
                A.add(v); changed = True
    return A


def zielonka(g, sub):
    if not sub: return set(), set()
    p = max(g.prio[v] for v in sub); pl = p % 2
    U = {v for v in sub if g.prio[v] == p}
    A = attr(g, U, pl, sub)
    W0, W1 = zielonka(g, sub - A)
    Wopp = W1 if pl == 0 else W0
    if not Wopp:
        return (set(sub), set()) if pl == 0 else (set(), set(sub))
    B = attr(g, Wopp, 1 - pl, sub)
    W0, W1 = zielonka(g, sub - B)
    if pl == 0: return W0, W1 | B
    return W0 | B, W1


def bad_reach(g, nx_choices, parity):
    """one-player graph: succ lists nx_choices[v]; vertices that can reach a cycle whose top priority has the given parity"""
    n = g.n; bad = set()
    for t in range(n):
        if g.prio[t] % 2 != parity: continue
        sub = {v for v in range(n) if (g.prio[v], v) <= (g.prio[t], t)}
        # t on a cycle inside sub?
        seen, stack = set(), [w for w in nx_choices[t] if w in sub]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); stack.extend(w for w in nx_choices[x] if w in sub)
        if t in seen: bad.add(t)
    # backward reachability to bad
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in nx_choices[v]: pred[w].append(v)
    R, stack = set(bad), list(bad)
    while stack:
        x = stack.pop()
        for y in pred[x]:
            if y not in R: R.add(y); stack.append(y)
    return R


def bound(n, m, do, Dl):
    F = 2 * n * n; TH = n * n + 2 * n - 1
    XSN = 13 * (do + 1) * n ** 3 * (F + 1 + TH) + TH
    X = (F + 1) * (n - 1) + F + XSN
    Th = (n - 1) + n * (X + 1) + X
    So = do * (Th + 1)
    Wch = (F + X + 1) * n * n
    Nst = 1 + X + Th + Wch
    NX = F + Nst + (X + 1) * (n - 1) + (Nst + F) * 3 * Dl * n ** 4
    Ts = (m - n + 1) * (So + NX + 1)
    return (n * (n - 1) + do) * (Ts + 1)


def check(g, cnt, name):
    o = P.assert_c1o(g); n = g.n
    _, st = P.states(g)
    fin = st[-1]; s, Xi, sb = fin["s"], fin["Xi"], fin["sb"]
    W = {v for v in range(n) if g.prio[Xi[v][0]] % 2 == 0}
    ZE, ZO = zielonka(g, set(range(n)))
    cnt["games_runs"] += 1
    if W != ZE: fail(cnt, "OUT_W", name)
    gs = [[s[v]] if g.owner[v] == 0 else list(g.succ[v]) for v in range(n)]
    if bad_reach(g, gs, 1) & W: fail(cnt, "OUT_SIG", name)
    gb = [list(g.succ[v]) if g.owner[v] == 0 else [sb[v]] for v in range(n)]
    if bad_reach(g, gb, 0) & (set(range(n)) - W): fail(cnt, "OUT_BAR", name)
    it = len(st) - 1; m = sum(len(x) for x in g.succ)
    if it > bound(n, m, len(g.succ[o]), max(len(x) for x in g.succ)): fail(cnt, "ITER", name, it)
    cnt["max_iter"] = max(cnt["max_iter"], it)
    k = 0; T = len(st) - 1
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        f = sum(st[x]["fb"] for x in range(k, j))
        if f > 2 * n * n: fail(cnt, "FMAX", name, k, f)
        cnt["max_fb_phase"] = max(cnt["max_fb_phase"], f); cnt["phases"] += 1
        k = j + 1
    cnt["W_nonempty_both"] += bool(W) and len(W) < n


def main(a):
    if a and a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [("rand%d" % i, P.rand_c1o(rng, rng.randint(lo, hi))) for i in range(N)]
    else:
        files = RP.lib() if a == ["lib"] else a
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in files]
    cnt = Counter(); nr = int(os.environ.get("RANDSTARTS", "0"))
    for name, g in gs:
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        cnt["games"] += 1
        orig = RE.best_reward_start
        starts = [None] + [random.Random(name + str(i)) for i in range(nr)]
        for r in starts:
            if r is not None:
                s0 = [r.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)]
                t0 = [r.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)]
                RE.best_reward_start = lambda h, s0=s0, t0=t0: (s0, t0)
            try: check(g, cnt, name + ("@rand" if r else ""))
            except RuntimeError: cnt["maxit"] += 1
            RE.best_reward_start = orig
    for k in sorted(cnt): print("%-28s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main(sys.argv[1:])
