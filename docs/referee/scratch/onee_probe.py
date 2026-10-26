#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-1E (docs/si/P-N5-1E-box16.md, pin 7fef9699, sha1 e613db13...). Own code only (rl_engine via
dual_probe.run5 = plain N5 with a start pair; onecheck's Zielonka and one-player reachability). Any game.
 OUTG_W    at EVERY state with I_sigma = {} (OUT-G needs only that, not I_tau = {}): W := {v : Omega(cycle node of Xi_sigma(v)) even}
           equals own Zielonka's W_E
 OUTG_SIG  there: sigma wins every v in W (in G_sigma no vertex of W reaches a cycle whose top priority is odd)
 OUTG_BAR  there: sigma-bar (S1's counterstrategy at sigma) wins every v not in W (in G_sigmabar no vertex of V - W reaches an even-top cycle)
 STOP      the run stops with I_sigma = I_tau = {} (S5) - the OUTG checks above include the stop state
 ITER1E    on C^1E: iterations <= (n(n-1)+d_e)(T*(n,m,Delta,d_e)+1)   (onecheck.bound with d := d_e)
 SIGCH     on C^1E: sigma changes along the run <= d_e - 1 (MIRROR (a), landed R54 (b))
 MUT       control: the same three checks with the output read at the START state (must fail often; not a failure of the packet)
Usage: onee_probe.py lib | rand N nmin nmax seed CLASS | files...   CLASS: any | 1e  (env RANDSTARTS=N; seeds = relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D, onecheck as OC
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def even_choice(g):
    return [v for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) > 1]


def out_ok(g, s, ZE):
    """(W == W_E, sigma wins W, sigma-bar wins V - W) at Even strategy s"""
    Xi, sb = RE.evaluate(g, s)
    n = g.n; W = {v for v in range(n) if g.prio[Xi[v][0]] % 2 == 0}
    gs = [[s[v]] if g.owner[v] == 0 else list(g.succ[v]) for v in range(n)]
    gb = [list(g.succ[v]) if g.owner[v] == 0 else [sb[v]] for v in range(n)]
    return W == ZE, not (OC.bad_reach(g, gs, 1) & W), not (OC.bad_reach(g, gb, 0) & (set(range(n)) - W))


def check(g, start, cnt, name, ZE):
    A = D.run5(g, start)
    n = g.n; cnt["runs"] += 1
    if A[-1]["Is"] or A[-1]["It"]: fail(cnt, "STOP", name)
    for k, st in enumerate(A):
        if st["Is"]: continue
        cnt["states_Is_empty"] += 1; cnt["states_Is_empty_It_nonempty"] += bool(st["It"])
        for key, ok in zip(("OUTG_W", "OUTG_SIG", "OUTG_BAR"), out_ok(g, st["s"], ZE)):
            if not ok: fail(cnt, key, name, k)
    mut = out_ok(g, A[0]["s"], ZE)
    cnt["MUT_bites"] += not all(mut)
    it = len(A) - 1; cnt["max_iter"] = max(cnt["max_iter"], it)
    E = even_choice(g)
    if len(E) == 1:
        e = E[0]; de = len(g.succ[e]); cnt["runs_1e"] += 1
        m = sum(len(x) for x in g.succ); Dl = max(len(x) for x in g.succ)
        if it > OC.bound(n, m, de, Dl): fail(cnt, "ITER1E", name, it)
        ch = sum(1 for k in range(it) if A[k]["s"] != A[k + 1]["s"])
        if ch > de - 1: fail(cnt, "SIGCH", name, ch, de)
        cnt["max_iter_1e"] = max(cnt["max_iter_1e"], it); cnt["max_sigch_1e"] = max(cnt["max_sigch_1e"], ch)
        cnt["sigch_eq_de_minus_1"] += ch == de - 1


def rand_1e(rng, n):
    """a random C^1E game: the dual of a random C^1O game (owners swapped, priorities + 1)"""
    return D.rand_ck(rng, n, 1).dual()


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); cls = a[5]; rng = random.Random(seed)
        gs = []
        for i in range(N):
            nn = rng.randint(lo, hi)
            gs.append(("rand%d_%d" % (seed, i), rand_1e(rng, nn) if cls == "1e" else D.rand_ck(rng, nn, rng.randint(0, 4))))
    else:
        files = RP.lib() if a == ["lib"] else a
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in files]
    for name, g in gs:
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1; cnt["games_1e"] += len(even_choice(g)) == 1
        ZE, _ = OC.zielonka(g, set(range(g.n)))
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: check(g, st, cnt, name + ("@r%d" % i if i else ""), ZE)
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main(sys.argv[1:])
