#!/usr/bin/env python3
"""Box 10 item 1 (Lead 2026-10-26 06:48Z): premise (Sigma-tau) of L-NEW's P-N5-EPR (docs/new/P-N5-EPR-box45.md, sha1 8fecca79) on data.
Runs N5^tau (n5tau.py, from the packet text, on L-COMP's SPEC second implementation n5b.py) on C^1O games and checks the landed per-phase
bounds on the N5^tau state sequence with REFEREE-2's checkers called UNMODIFIED:
  R48 (i) Theorem FB-POLY: docs/referee-2/R2-N5-FBPOLY/fbpoly_check.check_run (FB (a)-(d) and its sub-lemmas AK, KY, KH, KP, EXIT, FX, CN, TA);
  R50 (h) Corollary PHASE: docs/referee-2/R2-N5-KW/kw_check.check_run (PHASE chain: T <= (m-n+1)(T_rel+1), T_rel, N_Xi, N_st, X, X_SN,
          W_ch, S_o; and the R50 lemmas it checks along: FRZU, LEN, PAR, KMONO, CASCB, CWINT, ESEG, RUN, KWS).
The trace is fed through REFEREE-2's out_check.analyse (its own valuations on its own Game type); "phase" is the checkers' (lambda_Xi, tau)
key, i.e. "phase of N5" read as "phase of N5^tau" (the packet's (Sigma-tau)). The R51 (a) form f <= 1 + (n-2)(2n-1) is also checked here.
Divergence: per run, whether the N5^tau state sequence differs from SPEC's (n5b SPEC mode), and the number of S4b^tau keeps.
Corpus: lib (every C^1O .pg, n <= 64) | rand N NMIN NMAX SEED (REFEREE-2 re_check.rand_game) | epochs N NMIN NMAX SEED: restricted games
G'_E of every epoch with |D_E| = 1 (P-N5-EPR §0) of random C^kO runs (k 2-4), started at the epoch's first state (sigma_x, tau) | files LIST.
Each game: S3 start + 3 random start pairs (lib, rand, files); the epoch's own start pair (epochs).
Usage: tau_check.py MODE ARGS... --out OUT.json"""
import json
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
for p in ("docs/referee-2/R2-N5-KW", "docs/referee-2/R2-N5-FBPOLY", "experiments/n5-exhaustive"):
    sys.path.insert(0, os.path.join(ROOT, p))
import pg  # noqa: E402
import n5b  # noqa: E402
import n5tau  # noqa: E402
import kw_check as KW  # noqa: E402
import fbpoly_check as FBP  # noqa: E402

OC = KW.OC; RC = OC.RC; FC = OC.FC


def own_lists(g, s, t):
    """n5b convention: sigma has -1 at Odd vertices, tau has -1 at Even vertices."""
    return [s[v] if g.owner[v] == 0 else -1 for v in range(g.n)], [t[v] if g.owner[v] == 1 else -1 for v in range(g.n)]


def full(g, s, t):
    """REFEREE-2 convention: full lists; own-player entries are the strategy, the other entries are CONSTANT along a run
    (out_check compares whole tau lists): filled with succ(v)[0]."""
    return ([s[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(g.n)],
            [t[v] if g.owner[v] == 1 else g.succ[v][0] for v in range(g.n)])


def one_run(rg, o, s, t, st, c, mx, name):
    hg = pg.Game(list(rg.prio), list(rg.owner), [list(x) for x in rg.succ])
    s0, t0 = own_lists(hg, s, t)
    L, F = [], []
    b = n5tau.N5tau(hg); b.run(list(s0), list(t0), trace=L, fbtrace=F)
    Ls = []; n5b.N5(hg, mode="spec").run(list(s0), list(t0), trace=Ls)
    c["runs"] += 1; c["transitions"] += len(F); c["S4b_tau_keeps"] += b.kept
    c["runs_diverged(N5tau != SPEC)"] += L != Ls; c["runs_with_keeps"] += b.kept > 0
    A = [OC.analyse(rg, o, *full(rg, sg, tu)) for sg, tu in L]
    stK, stF = OC.Stats(), OC.Stats()
    KW.check_run(rg, o, A, F, stK, name); FBP.check_run(rg, o, A, F, stF, name)
    for tag, x in (("KW", stK), ("FBP", stF)):
        st[tag].c.update(x.c)
        for k, v in x.mx.items():
            st[tag].mx[k] = max(st[tag].mx[k], v)
        st[tag].viol += x.viol[:max(0, 40 - len(st[tag].viol))]
    # R51 (a) form of R48 (i) per N5^tau phase: in-phase Even fallbacks <= 1 + (n - 2)(2n - 1)
    n = rg.n; k = 0; T = len(F)
    while k < T:
        j = k; f = 0
        while j < T and A[j].lamX == A[j + 1].lamX and A[j].tu[o] == A[j + 1].tu[o]:
            f += F[j]; j += 1
        if j > k:
            c["phases"] += 1; mx["max_f_phase"] = max(mx["max_f_phase"], f)
            if f > 1 + (n - 2) * (2 * n - 1):
                st["KW"].viol.append(f"{name} R51(a) f={f} > 1+(n-2)(2n-1)"); c["R51a_viol"] += 1
        k = max(j, k + 1)
    return b.kept


def restricted_epoch_games(rng, N, lo, hi):
    """G'_E for every epoch with |D_E| = 1 of random C^kO runs (SPEC N5, n5b), with the epoch's first state as start."""
    import gdnc_check as G
    out = []
    for i in range(N):
        n = rng.randint(lo, hi); lg = G.rand_ckO(rng, n, rng.randint(2, min(4, n - 1)))
        hg = pg.Game(list(lg.prio), list(lg.owner), [list(x) for x in lg.succ])
        E, Ed = G.F.Engine(lg), G.F.Engine(G.F.n5.dual(lg))
        s, t = (list(E.initial("best")), list(Ed.initial("best"))) if i % 2 == 0 else G.rand_start(lg, rng)
        L = []; n5b.N5(hg, mode="spec").run(*own_lists(hg, s, t), trace=L)
        a = n5b.N5(hg, mode="spec"); prev = None
        for sg, tu in L:
            _, sbar = a.opt(a.SG, list(sg))
            D = [u for u in range(n) if hg.owner[u] == 1 and sbar[u] != tu[u]]
            keyE = (tuple(sbar[u] for u in range(n) if hg.owner[u] == 1), tu)
            if keyE != prev and len(D) == 1:
                u = D[0]
                succ = [sorted({tu[v], sbar[v]}) if (hg.owner[v] == 1 and v == u) else ([tu[v]] if hg.owner[v] == 1 else list(hg.succ[v]))
                        for v in range(n)]
                gE = RC.Game(list(hg.prio), list(hg.owner), succ); out.append((gE, u, full(gE, sg, tu), f"ep{i}"))
            prev = keyE
    return out


def main():
    a = sys.argv[1:]; outp = a[a.index("--out") + 1]; a = a[:a.index("--out")]
    st = {"KW": OC.Stats(), "FBP": OC.Stats()}; c, mx = Counter(), Counter(); div = []
    mode = a[0]; jobs = []
    if mode in ("lib", "files"):
        import glob
        paths = (sorted(glob.glob(os.path.join(ROOT, "experiments", "**", "*.pg"), recursive=True)) if mode == "lib"
                 else [l.strip() for l in open(a[1]) if l.strip()])
        for p in paths:
            if "/out/" in p:
                continue
            try:
                rg = RC.parse(open(p).read())
            except Exception:  # noqa: BLE001
                continue
            if rg.n > 64 or sum(1 for v in range(rg.n) if rg.owner[v] == 1 and len(rg.succ[v]) > 1) != 1:
                continue
            o = FC.odd_vertex(rg); rng = random.Random(7)
            for r in range(4):
                jobs.append((rg, o, FC.s3_start(rg) if r == 0 else RC.rand_start(rng, rg), f"{os.path.relpath(p, ROOT)}#{r}"))
    elif mode == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            rg, o = RC.rand_game(rng, rng.randint(lo, hi))
            for r in range(4):
                jobs.append((rg, o, FC.s3_start(rg) if r == 0 else RC.rand_start(rng, rg), f"rand{seed}#{i}.{r}"))
    else:
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for rg, u, (s, t), nm in restricted_epoch_games(rng, N, lo, hi):
            jobs.append((rg, u, (s, t), nm))
    for rg, o, (s, t), nm in jobs:
        try:
            kept = one_run(rg, o, s, t, st, c, mx, nm)
        except Exception as e:  # noqa: BLE001
            c["errors"] += 1; div.append(dict(name=nm, error=repr(e)[:200])); continue
        if kept and len(div) < 200:
            div.append(dict(name=nm, prio=rg.prio, owner=rg.owner, succ=rg.succ, start=[s, t], keeps=kept))
    viol = st["KW"].viol + st["FBP"].viol
    res = dict(mode=mode, args=a[1:], counts=dict(c), maxima=dict(mx), KW=dict(st["KW"].c), KW_mx=dict(st["KW"].mx),
               FBP=dict(st["FBP"].c), FBP_mx=dict(st["FBP"].mx), violations=viol[:60], diverged=div)
    json.dump(res, open(outp, "w"), indent=1, default=str)
    print(json.dumps(dict(counts=dict(c), maxima=dict(mx), KW_viol=st["KW"].c["VIOLATIONS"], FBP_viol=st["FBP"].c["VIOLATIONS"],
                          PHASE_checked=st["KW"].c["PHASE_checked"], nviol=len(viol))))


if __name__ == "__main__":
    main()
