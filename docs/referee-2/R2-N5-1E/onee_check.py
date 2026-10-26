#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): data for packet P-N5-1E (docs/si/P-N5-1E-box16.md sha1 e613db13 @ 7fef9699).
State sequence: own SPEC N5 loop (R2-N5-DUAL/dual_check.Runner, si.py read-only). Output checks: R2-N5-1O/onecheck.check_out (own play values,
enumerated Odd / Even strategies, own Zielonka, own strategy verifier; O1-O6) on EVERY game. The lane's experiments/si/out16/outcheck.py is
not run or imported.
Checks: OUT (O1-O6 at the stop, every game); ITER (on C^1E: ITER <= (n(n-1)+d_e)(T*(n,m,Delta,d_e)+1) and <= (n(n-1)+d_e)(T*(n,n^2,n,n)+1));
        MON (T*(n,m,Delta,d) <= T*(n,n^2,n,n) for the game's parameters); PH (dual phases <= n(n-1)+d_e; sigma changes <= d_e - 1).
Mutations ONE_MUT as onecheck (flip | sbar | early).
Usage: onee_check.py random N nmin nmax seed kind (kind 1E | kO) | files list.txt [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-1O"))
import dual_check as DC
import onecheck as OC
pg, Engine = DC.pg, DC.Engine

def run(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    g = OC.RC.Game(list(gp.prio), list(gp.owner), [list(x) for x in gp.succ])
    n = g.n; st.inc("runs"); st.inc("iterations", len(fbs))
    ec = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
    if len(ec) == 1:
        st.inc("C1E_runs")
        de = len(g.succ[ec[0]]); m = sum(len(x) for x in g.succ); D = max(len(x) for x in g.succ)
        b1 = (n * (n - 1) + de) * (OC.tstar(n, m, de, D) + 1); b2 = (n * (n - 1) + de) * (OC.tstar(n, n * n, n, n) + 1)
        if OC.tstar(n, m, de, D) > OC.tstar(n, n * n, n, n): st.bad("MON", f"{name}")
        if len(fbs) > b1 or len(fbs) > b2: st.bad("ITER", f"{name}: {len(fbs)}")
        st.mxr("C1E_max_iter", (len(fbs), name))
        Ed = DC.Runner(gp).Ed
        lamU = [tuple(DC.lam(Ed, list(x[1]), [o == 1 for o in g.owner])) for x in states]
        sig = [tuple(x[0][v] for v in range(n) if g.owner[v] == 0) for x in states]
        dph = 1 + sum(1 for k in range(len(states) - 1) if (lamU[k], sig[k]) != (lamU[k + 1], sig[k + 1]))
        cs = sum(1 for k in range(len(states) - 1) if sig[k] != sig[k + 1])
        if dph > n * (n - 1) + de or cs > de - 1: st.bad("PH", f"{name}: dual phases {dph}, sigma changes {cs}")
    sg, tu = (states[0] if OC.MUT == "early" else states[-1])
    OC.check_out(g, list(sg), list(tu), st, name)

def main():
    st = OC.Stats(); a = sys.argv[1:]
    if a[0] == "random":
        N, nmin, nmax, seed, kind = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), kind)
            if i % 2: s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
            else: s, t = list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
            run(gp, s, t, st, f"{kind}{seed}:{i}")
    else:
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(6161)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                if r == 0: s, t = list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
                else: s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
                run(gp, s, t, st, f"{path}#{r}")
    print("MODE", " ".join(a), "MUT", OC.MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
