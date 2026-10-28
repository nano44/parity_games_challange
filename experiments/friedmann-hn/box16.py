#!/usr/bin/env python3
"""Box 16 (Lead GO 2026-10-26 19:18Z, D18): N5 on Friedmann's H_n ([F] LMCS 7(3:19) 2011, arXiv 1106.0778, §8.4 Table 7; hn.py).

Engines: n5b.py SPEC (L-COMP, experiments/n5-second) and n5.py (L-NEW, via experiments/n5-exhaustive/exh.trace and, for the ALT counter,
L-SI's experiments/si/root/common.rows on L-NEW's n5x engine). Every run: n5 state sequence = n5b state sequence (asserted), regions =
Oink zlk @ 8fbf0a7 (tl if zlk aborts), both engines' strategies pass experiments/harness/verify.py; instance + start pinned by sha1 in
instances/.
Starts:  F    = (ι_{H_n}, σ̄(ι)): [F]'s Even start (§8.4 below Table 7); Odd starts at its optimal counterstrategy to ι ([F] works with
                τ_σ = best response throughout, §3 Lemma 3.1; READING: the natural N5 analogue of [F]'s start), σ̄ by SPEC S1 (iv)/(v).
         Fs3  = (ι_{H_n}, S3's τ).        S3 = SPEC S3 for both.
         G<k> = (σ_k, σ̄(σ_k)), σ_k the I^glo strategy after k improvement steps from ι (iglo.py's loop): mid-counter starts.
Per phase (R38 (a): maximal run of states with (λ_Ξ, τ) constant; census.py's key):
  len      in-phase transitions;  end  why the phase ended: tau (τ changed, λ_Ξ not), lam (λ_Ξ changed, τ not), both, final;
  dW       in-phase transitions changing λ_W (λ_W = cycle node of the W valuation, Odd fixed to τ; census.state_info lamW);
  f        in-phase fallbacks (n5b fbtrace);  N_ep, NCONF, NCONF2: nconf.phase_stats (box 14, = L-NEW nep90 exactly);
  S        fallback-free, λ_W-constant runs of the phase (split at every fallback and every λ_W change), as N5-EXIT §9 "S";
  ALT      max over S and classes c of ALT_c(S), N5-EXIT-box22 §9 (l-si 196c7e8c) as stated there, NOT first-match:
           transition k -> k+1 of S with sbch ∩ (D_k ∪ D_{k+1}) ≠ ∅ (σ̄ changes at a gate u ∈ U_c ∩ Q_c) AND (D ∩ U_c changes (DCH) OR
           an offset of a D-direct gate changes at a gate whose σ̄ changes (OSB)); D, U_c, Q_c, D-direct, offsets from L-SI's
           gcx.state_info / gcx.offs (classes c = λ_Ξ classes with |U_c| >= 3, Q_c ≠ ∅, as evenside.py).  ALTsum = sum over S and c.
  SBG      transitions of the phase with a σ̄ change at a gate (u ∈ Q ∩ (D_k ∪ D_{k+1})), fallback or not: an upper count for ALT.
  sbQ      transitions of the phase with any σ̄ change on Q.
Landed-statement checks: census.analyse (EP0, ALT (R61 (e)), NEP, XEP, SPLIT, EPOCH, MONO, D-EPOCH) on every run; VIOLATION lines.
Usage: box16.py N START [--mode fig|table] [--no-pin]   (START in F, Fs3, S3, G<k>)"""
import hashlib
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-epoch", "n5-exhaustive", "n5-second", "harness", "hard-families", os.path.join("si", "root")):
    sys.path.insert(0, os.path.join(ROOT, "experiments", p))
import hn  # noqa: E402
import census as CE  # noqa: E402
import nconf as NC  # noqa: E402
import check_instance as CI  # noqa: E402
from check_instance import exh, n5, n5b, verify, pg  # noqa: E402
sys.modules.pop("common", None)          # exh.py imported L-NEW's experiments/new/box25 common; gcx needs L-SI's
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
import common as LC  # noqa: E402  (L-SI, read-only)
import gcx  # noqa: E402            (L-SI, read-only)
assert hasattr(LC, "rows")
from pgsolver_si import SI  # noqa: E402

EVEN, ODD = 0, 1


def iglo_strat(g, io, k):
    si = SI(g); strat = [io.get(v, -1) for v in range(g.n)]; valu = si.evaluate(strat)
    for _ in range(k):
        if not any(g.owner[i] == 0 and si.nvo(valu[strat[i]], valu[si.best(valu, i)]) < 0 for i in range(g.n)):
            break
        strat = si.policy_switchbest(strat, valu); valu = si.evaluate(strat)
    return strat


def make_start(g, ix, n, lab):
    S3s = n5b.SpecSI(g).initial_strategy_by_best_reward(); S3t = n5b.SpecSI(n5b.dual(g)).initial_strategy_by_best_reward()
    io = hn.iota(n, ix)
    if lab == "S3":
        s, t = S3s, S3t
    else:
        s = [io.get(v, -1) for v in range(g.n)] if lab in ("F", "Fs3") else iglo_strat(g, io, int(lab[1:]))
        if lab == "Fs3":
            t = S3t
        else:
            _, sb = n5b.SpecSI(g).evaluate_choice(list(s)); t = [sb[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
    return ({v: s[v] for v in range(g.n) if g.owner[v] == EVEN}, {v: t[v] for v in range(g.n) if g.owner[v] == ODD})


def alt_phase(g, R, i, j, lamW_ch):
    """ALT_c(S) per N5-EXIT §9 on rows R[i..j] (one phase); runs S split at fallbacks and λ_W changes."""
    Qs = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    E = ENG[0]
    cls = {}
    for v in range(g.n):
        cls.setdefault(R[i]["vs"][v][0], set()).add(v)
    runs, s = [], i
    for k in range(i, j):
        if R[k]["fb"] or lamW_ch[k]:
            runs.append((s, k)); s = k + 1
    runs.append((s, j))
    best, tot, nruns = 0, 0, 0
    for c, U in cls.items():
        Qc = {q for q in Qs if q in U and q != c}
        if len(U) < 3 or not Qc:
            continue
        I = {k: gcx.state_info(g, R[k], U, Qc) for k in range(i, j + 1)}
        OF = {k: gcx.offs(E, R[k], I[k][3]) for k in range(i, j + 1)}
        for a, b in runs:
            if b <= a:
                continue
            nruns += 1; alt = 0
            for k in range(a, b):
                D0, D1 = I[k][0], I[k + 1][0]
                sbch = {q for q in Qc if R[k]["sb"][q] != R[k + 1]["sb"][q]}
                if not (sbch & (D0 | D1)):
                    continue
                dch = (D0 & U) != (D1 & U)
                chg = {u for u in set(OF[k]) | set(OF[k + 1]) if OF[k].get(u) != OF[k + 1].get(u)}
                if dch or (chg & sbch):
                    alt += 1
            best = max(best, alt); tot += alt
    return best, tot, nruns


ENG = [None]


def main():
    a = sys.argv[1:]
    n, lab = int(a[0]), a[1]
    mode = a[a.index("--mode") + 1] if "--mode" in a else "fig"
    g, ix = hn.build(n, mode)
    start = make_start(g, ix, n, lab)
    name = f"H{n}{'' if mode == 'fig' else 'tab'}_{lab}"
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    gp = os.path.join(HERE, "instances", f"H{n}{'' if mode == 'fig' else 'tab'}.pg"); pg.write(g, gp)
    sp = os.path.join(HERE, "instances", name + ".start")
    with open(sp, "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
    sha = hashlib.sha1(open(gp, "rb").read()).hexdigest(); ssha = hashlib.sha1(open(sp, "rb").read()).hexdigest()
    # n5.py (L-NEW) states, asserted against n5.run
    st, _ = exh.trace(g, start, check=True)
    sig = [start[0].get(v, -1) for v in range(g.n)]; tau = [start[1].get(v, -1) for v in range(g.n)]
    L, FB = [], []
    winb, wsb, itb, fbb = n5b.N5(g, mode="spec").run(list(sig), list(tau), trace=L, fbtrace=FB, max_iter=10 ** 6)
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    same = len(L) == len(st) and all(ev(x[0], 0) == ev(y[0], 0) and ev(x[1], 1) == ev(y[1], 1) for x, y in zip(L, st))
    it, fb5, win, ws, _ = n5.run(g, "n5", start)
    ref, rtag = CI.zlk(gp, g.n)
    errs = verify.check(g, win, ws); errsb = verify.check(g, winb, wsb)
    ok = same and (itb, fbb) == (it, fb5) and win == ref == winb and not errs and not errsb
    # per phase
    SG = n5b.SpecSI(g)
    A = [CE.state_info(g, SG, s, t) for s, t in L]
    S = CE.Stats(); CE.analyse(g, name, L, FB, S)
    _, _, ph = NC.phases(g, L, FB, A)
    E, R = LC.rows(g, start, cap=10 ** 6); ENG[0] = E
    rows_same = len(R) == len(L) and all(ev(R[k]["s"], 0) == ev(L[k][0], 0) and ev(R[k]["t"], 1) == ev(L[k][1], 1) for k in range(len(L)))
    ok = ok and rows_same
    Q = [v for v in range(g.n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2]
    lamW_ch = [A[k]["lamW"] != A[k + 1]["lamW"] for k in range(len(A) - 1)] + [False]
    P = []
    for pi, (x, y) in enumerate(ph):
        r, _ = NC.phase_stats(g, L, FB, SG, A, x, y)
        if y + 1 < len(L):
            dt = L[y][1] != L[y + 1][1]; dl = A[y]["lam"] != A[y + 1]["lam"]
            end = "both" if dt and dl else "tau" if dt else "lam" if dl else "?"
            ntau = sum(1 for v in range(g.n) if g.owner[v] == ODD and L[y][1][v] != L[y + 1][1][v])
        else:
            end, ntau = "final", 0
        altmax, altsum, nS = alt_phase(g, R, x, y, lamW_ch)
        sbg = sum(1 for k in range(x, y) if any(A[k]["sbar"][q] != A[k + 1]["sbar"][q] and (q in A[k]["D"] or q in A[k + 1]["D"]) for q in Q))
        sbq = sum(1 for k in range(x, y) if any(A[k]["sbar"][q] != A[k + 1]["sbar"][q] for q in Q))
        P.append(dict(p=pi, a=x, b=y, len=y - x, end=end, ntau=ntau, dW=sum(lamW_ch[k] for k in range(x, y)),
                      f=sum(FB[k] for k in range(x, y)), N_ep=r["N_ep"], NCONF=r["NCONF"], NCONF2=r["NCONF2"],
                      S=nS, ALT=altmax, ALTsum=altsum, SBG=sbg, sbQ=sbq, D=max(len(A[k]["D"]) for k in range(x, y + 1))))
    tauch = sum(1 for k in range(len(L) - 1) if L[k][1] != L[k + 1][1])
    lamch = sum(1 for k in range(len(L) - 1) if A[k]["lam"] != A[k + 1]["lam"])
    longest = max(p["len"] for p in P)
    res = dict(name=name, n=n, mode=mode, V=g.n, m=g.m, sha1=sha, start_sha1=ssha, it=it, fb=fb5, phases=len(P), longest=longest,
               tau_changes=tauch, lamXi_changes=lamch, lamW_changes=sum(lamW_ch), viol=list(CE.VIOL), ok=ok,
               checks=dict(n5_eq_n5b=same, rows_eq=rows_same, oink=rtag, oink_eq=win == ref == winb, verify_n5=not errs, verify_n5b=not errsb),
               phases_detail=P)
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    json.dump(res, open(os.path.join(HERE, "results", name + ".json"), "w"), indent=0)
    print(f"{name} sha1 {sha[:12]} start {ssha[:12]} V {g.n} it {it} fb {fb5} phases {len(P)} longest {longest} tau_ch {tauch} "
          f"lamXi_ch {lamch} lamW_ch {sum(lamW_ch)} maxNep {max(p['N_ep'] for p in P)} maxNCONF {max(p['NCONF'] for p in P)} "
          f"maxALT {max(p['ALT'] for p in P)} sumALT {sum(p['ALTsum'] for p in P)} maxSBG {max(p['SBG'] for p in P)} "
          f"viol {len(CE.VIOL)} | n5=n5b {same} rows {rows_same} oink {rtag} {win == ref == winb} verify {not errs and not errsb} | {'OK' if ok else 'FAIL'}",
          flush=True)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
