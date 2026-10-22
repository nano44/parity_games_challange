#!/usr/bin/env python3
"""REFEREE-2 code-link check for Corollary 2 (switch-best = N5 on one-player games): replays N5's loop (n5.py's own
functions and L-SI's Engine, imported read-only, trunk 26905f0) on one-player games, and checks at every iteration, with
sb1p.py's independent definitions, that
  (a) the engine's valuation Xi_sigma equals my Omega (as (cycle node, path set, length) triples) and I_sigma equals my I;
  (b) Odd's side has no improving edge (I_tau = {}), so N5 = Even's step only;
  (c) sigma_new (n5.py's arena optimum from Engine.evaluate on the dual arena) attains my pointwise maximum over all plays of
      the arena {sigma(v)} u I_sigma(v) (so it is a switch-best step), and n5's fallback fires exactly when sigma_new = sigma;
then feeds N5's actual sigma sequence (with its engine tie-breaks) to sb1p.check_run: Lemma P at every in-phase step,
Theorem PH's counts, the lambda-changing-or-flat property, (F2).  Also compares my replica's (iterations, fallbacks) with
n5.run's.  Usage: n5link.py random N NMAX [seed] | n5link.py inst game.pg [game.pg.start]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("R2_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))   # R2_ROOT = a checkout of trunk 26905f0
sys.path.insert(0, os.path.join(ROOT, "experiments", "new")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness")); sys.path.insert(0, HERE)
import pg
import n5                    # L-NEW's n5.py (read-only); n5.run and n5.dual
from si import Engine        # L-SI's engine (read-only)
import sb1p


def triple(E, val):
    c, mask, ln = val
    P = frozenset(v for v in range(E.n) if mask >> E.rank[v] & 1)
    return (c, P, ln)


def replay(g, start, st):
    """n5.run's loop (mode n5), copied step by step, with checks; returns (sigma sequence, kinds, it, fb)."""
    n = g.n
    E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    my = sb1p.Game(g.prio, g.owner, g.succ)
    rho = [sigma[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(n)]
    seq, kinds = [list(rho)], []
    it = fb = 0
    while it < 10 ** 5:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        # (a) engine valuation / improving set vs mine
        Om = my.omega(rho)
        st.inc("iterations_checked")
        for v in range(n):
            if triple(E, vs[v]) != Om[v]:
                st.bad(f"Xi_sigma != my Omega at v={v}: {triple(E, vs[v])} vs {Om[v]}")
        myI = my.improving(rho, Om)
        if sorted(Is) != sorted((x, z) for x, zs in myI.items() for z in zs):
            st.bad("I_sigma differs from my improving set")
        if It:
            st.bad("(b) Odd has an improving edge on a one-player game")
        if not Is and not It:
            break
        it += 1
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            st.bad("Odd step on a one-player game")
        fallback = False
        if ns == sigma and nt == tau:
            fb += 1; fallback = True
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        # (c) sigma_new attains my pointwise arena maximum (before the fallback rewrite, i.e. the engine's optimum)
        opts = sb1p.arena_opts(my, rho, myI)
        bp = my.best_plays(opts)
        if bp is None:
            st.inc("SKIPPED_best_plays_budget"); return None
        eng = [ (best[v] if g.owner[v] == 0 else g.succ[v][0]) for v in range(n)] if Is and not fallback else list(rho)
        if not fallback:
            Om_eng = my.omega(eng)
            st.inc("optimum_checks")
            for v in range(n):
                if my.key(Om_eng[v]) != my.key(bp[v]):
                    st.bad(f"(c) engine's sigma_new is not a pointwise arena optimum at v={v}")
                if eng[v] not in opts[v]:
                    st.bad(f"(c) engine's sigma_new leaves the arena at v={v}")
        else:
            st.inc("fallback_iterations")
            # the engine returned sigma: so sigma is itself an arena optimum = the value-flat situation
            if any(my.key(bp[v]) != my.key(Om[v]) for v in range(n)):
                st.bad("fallback fired although some arena strategy beats sigma (not the flat situation)")
        new = [ns[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(n)]
        Om2 = my.omega(new)
        if fallback:
            kinds.append("fallback")
            if Om2 != Om or my.improving(new, Om2):
                st.bad("fallback changed values or left improving edges")
        else:
            lam = any(Om2[v][0] != Om[v][0] for v in range(n))
            kinds.append("lambda" if lam else ("vc" if Om2 != Om else "flat"))
        seq.append(new); rho = new
        sigma, tau = ns, nt
    return seq, kinds, it, fb


def main():
    st = sb1p.Stats(); t0 = time.time()
    if sys.argv[1] == "random":
        N, nmax = int(sys.argv[2]), int(sys.argv[3]); seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(2, nmax)
            my = sb1p.rand_game(rng, n, dmax=rng.choice([2, 3, 4]), p_even=rng.choice([0.6, 0.8, 1.0]), prange=rng.choice([n, 2 * n, 3]))
            g = pg.Game(my.prio, my.owner, my.succ)
            st.inc("games")
            for s in range(2):
                start = ({v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {}) if s else None
                r = replay(g, start, st)
                if r is None: continue
                seq, kinds, it, fb = r
                it2, fb2, win, ws, ev = n5.run(g, "n5", start)
                if (it, fb) != (it2, fb2):
                    st.bad(f"replica (it,fb)=({it},{fb}) != n5.run ({it2},{fb2})")
                st.inc("n5_runs"); st.inc("n5_iterations", it); st.inc("n5_fallbacks", fb)
                sb1p.check_run(my, seq, kinds, st, lemmaP=(n <= 12))
    else:
        g = pg.read(sys.argv[2])
        start = None
        if len(sys.argv) > 3:
            tok = [l for l in open(sys.argv[3]) if l.startswith("SIGMA0")][0].split()[1:]
            start = ({int(a): int(b) for a, b in (t.split(":") for t in tok)}, {})
        my = sb1p.Game(g.prio, g.owner, g.succ)
        r = replay(g, start, st)
        if r is None:
            print("SKIPPED (budget)")
        else:
            seq, kinds, it, fb = r
            it2, fb2, *_ = n5.run(g, "n5", start)
            print(f"{sys.argv[2]}: n={g.n} m={my.m} replica it={it} fb={fb}; n5.run it={it2} fb={fb2}; kinds={''.join(k[0] for k in kinds)}")
            sb1p.check_run(my, seq, kinds, st, lemmaP=("--nolemmaP" not in sys.argv))
            a = 0; ph = []
            for k, kd in enumerate(kinds):
                if kd == "lambda": ph.append((a, k)); a = k + 1
            ph.append((a, len(kinds)))
            print("phases (in-phase steps, value-changing, flat):", [(b - a, kinds[a:b].count("vc"), kinds[a:b].count("flat") + kinds[a:b].count("fallback")) for a, b in ph])
    for k in sorted(st.d): print(f"  {k} = {st.d[k]}")
    for v in st.viol[:20]: print("  VIOLATION:", v)
    print(f"RESULT violations={len(st.viol)} secs={time.time() - t0:.1f}")


if __name__ == "__main__":
    main()
