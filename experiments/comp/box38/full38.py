#!/usr/bin/env python3
"""L-COMP box 38: N5'-xi on Gamma3 from S3 RUN TO THE END (my engine). Game, start, S4a with [N5XI] and S4b: box34/own34.py (my
independent text engine, unchanged; imported). Added here, from SPEC (docs/new/N5-ssi-global.md) as read by my n5b
(experiments/n5-second/n5b.py readings A7, A8): step 4 FALLBACK when S4a/S4b change nothing: if I_sigma != {} every Even vertex with an
improving edge switches to its best successor under Xi_sigma (SpecSI.best), else the same for Odd on the dual; the run continues.
Counters (unit: one run): T3 = non-fallback iterations before the first fallback (own34's T3); Ttot = number of passes through
steps 2-5 (the final pass with I_sigma = I_tau = {} not counted; n5b A8) = N5'-xi's TOTAL iterations; F = number of fallback passes;
first = pass index of the first fallback (= T3 + 1 when there is one).
ENDGAME-3 (P-N5-END, lane-proved, REFEREE 29 SIGN) predicts F = 1 and Ttot = T3 + 3; checked, not assumed.
Usage: full38.py G.json [...] [--noelev]"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box34")]
import own34
from own34 import build, standard, SpecSI, dual, restrict, ext, EVEN, ODD


def full(G, elev=True, cap=100000):
    g, V = build(G, elev); n = g.n
    SG, SD = SpecSI(g), SpecSI(dual(g))
    sigma = SG.initial_strategy_by_best_reward(); tau = SD.initial_strategy_by_best_reward()
    s0, t0 = standard(G, V, g)
    assert all(sigma[v] == s0[v] for v in range(n) if g.owner[v] == EVEN) and all(tau[v] == t0[v] for v in range(n) if g.owner[v] == ODD)
    passes = F = 0; first = None; seen = set()
    while True:
        key = (tuple(sigma), tuple(tau))
        if key in seen: raise RuntimeError(f"repeated state at pass {passes}")
        seen.add(key)
        vs = SG.evaluate(sigma); vt = SD.evaluate(tau)
        Is = {v: [w for w in SG.succ[v] if SG.nvo(vs[sigma[v]], vs[w]) < 0] for v in range(n) if sigma[v] != -1}
        Is = {v: w for v, w in Is.items() if w}
        It = {v: [w for w in SD.succ[v] if SD.nvo(vt[tau[v]], vt[w]) < 0] for v in range(n) if tau[v] != -1}
        It = {v: w for v, w in It.items() if w}
        if not Is and not It: break
        passes += 1
        if passes > cap: raise RuntimeError("cap")
        if Is:   # S4a (SPEC) + [N5XI]: verbatim own34.run
            A = [([sigma[v]] + Is.get(v, [])) if g.owner[v] == EVEN else [tau[v]] for v in range(n)]
            hg = restrict(g, A); d2 = SpecSI(dual(hg))
            _, c2 = d2.evaluate_choice([tau[v] if g.owner[v] == ODD else -1 for v in range(n)])
            sig_spec = [c2[v] if g.owner[v] == EVEN else -1 for v in range(n)]
            Wst = SpecSI(hg).evaluate([sig_spec[v] if g.owner[v] == EVEN else -1 for v in range(n)])
            sig2 = list(sig_spec)
            for v in range(n):
                if g.owner[v] != EVEN or len(A[v]) < 2 or Wst[v][0] == v: continue
                tie = [w for w in sorted(set(A[v])) if ext(SG, v, Wst[w]) == Wst[v]]
                assert tie, "empty TIE"
                bestv = None; cand = []
                for w in tie:
                    if bestv is None or SG.nvo(vs[w], bestv) > 0: bestv = vs[w]; cand = [w]
                    elif SG.nvo(vs[w], bestv) == 0: cand.append(w)
                sig2[v] = sig_spec[v] if sig_spec[v] in cand else max(cand)
        else:
            sig2 = list(sigma)
        if It:   # S4b (SPEC)
            A = [([tau[v]] + It.get(v, [])) if g.owner[v] == ODD else [sigma[v]] for v in range(n)]
            s3 = SpecSI(restrict(g, A)); _, c3 = s3.evaluate_choice(sigma)
            tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(n)]
        else:
            tau2 = list(tau)
        if sig2 == sigma and tau2 == tau:   # step 4 fallback (n5b A7)
            F += 1
            if first is None: first = passes
            if Is:
                sig2 = list(sigma)
                for v in Is: sig2[v] = SG.best(vs, v)
            else:
                tau2 = list(tau)
                for v in It: tau2[v] = SD.best(vt, v)
        sigma, tau = sig2, tau2
    T3 = (first - 1) if first is not None else passes
    return dict(T3=T3, Ttot=passes, F=F, first=first, n=n)


if __name__ == "__main__":
    import json
    el = "--noelev" not in sys.argv
    for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
        r = full(json.load(open(f)), el); print(os.path.basename(f), json.dumps(r))
