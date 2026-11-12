#!/usr/bin/env python3
"""L-COMP box 44: N5'-xi (and N5) on ANY parity game from SPEC's default start S3, run to the end; MY engine.
This is box38/full38.py's loop (itself box34/own34.py's S4a with [N5XI] + n5b's fallback, readings A1-A9 of experiments/n5-second/n5b.py)
without the genome: the game is any pg.Game. Algorithm text: SPEC S1-S5 with FIX 1-4 (docs/new/N5-ssi-global.md) via my n5b SpecSI;
[N5XI] (RESULTS R118 / P-N5-XICYC, box 190 §1): «SPEC S1-S5 with ONE change in S4a. At every Even v with |A(v)| >= 2 that is not its own
H-cycle node, sigma_new(v) := the Xi_sigma-best element of TIE(v) := {w in A(v) : W*(v) = v (+) W*(w)}. Ties go by SPEC's choice, then
the larger index.» No code of L-NEW's n5v / n5bxi, of L-SI's wrap104 / free104 or of L-RED's n5x236 is used.
Counters (unit: one run): Ttot = passes through steps 2-5 (the final pass with I_sigma = I_tau = {} not counted; n5b A8) = iterations;
F = fallback passes; first = pass index of the first fallback.
run(g, mode, hook, ck): hook(t, sigma, tau, vs, Is, It, F) is called at every state t = 0, 1, ... (t = passes made so far), BEFORE the
pass from it; ck = a checkpoint path (pickle; written every CKEVERY passes; the run resumes from it; the hook's own state is the
caller's to save through ckget / ckset).
Tie-rule census, returned as r["use"] (passes BEFORE the first fallback) and r["useall"] (every pass): s4b = passes in which S4b ran
(I_tau != {}); s4bchoice = (pass, Odd vertex) pairs with two or more arena options in S4b (where SPEC's FIX 4 choice can matter); owncyc =
(pass, Even vertex) pairs with |A(v)| >= 2 at which v is its own H-cycle node (where SPEC's S1 (v) / FIX 2 choice decides, [N5XI] not
applying); xities = (pass, Even vertex) pairs at which two or more elements of TIE(v) are Xi_sigma-best (where «SPEC's choice, then the
larger index» decides): xispec of them by SPEC's choice, xiidx by the index; xidiff = pairs at which [N5XI]'s pick is not SPEC's.
Memo: Xi_sigma depends on sigma alone and Xi_tau on tau alone, so an evaluation is reused while its strategy has not changed.
Repeated states are detected through sha1 digests of (sigma, tau).
Usage: n5xi44.py GAME.pg [--mode xi|spec]  -> 'n5xi44 <mode> n <n> iterations <Ttot> fallbacks <F> first <first> regions_even <k>'"""
import sys, os, pickle, hashlib, array
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg
from n5b import SpecSI, dual, restrict
EVEN, ODD = 0, 1
CKEVERY = int(os.environ.get("CKEVERY", "25"))
USE = ("s4b", "s4bchoice", "owncyc", "xities", "xispec", "xiidx", "xidiff")
XCTRL = os.environ.get("N5XI44_CTRL", "0")   # 1: TIE ties to the SMALLER index, SPEC's choice ignored (a different tie rule, for the tie census)


def ext(si, v, val):
    L, P, k = val
    return (L, P | {v} if si.rel(v, L) > 0 else P, k + 1)


def digest(sigma, tau):
    return hashlib.sha1(array.array("i", sigma).tobytes() + array.array("i", tau).tobytes()).digest()


def improving(si, strat, valu):
    I = {}
    for v in range(si.g.n):
        if strat[v] == -1: continue
        ws = [w for w in si.succ[v] if si.nvo(valu[strat[v]], valu[w]) < 0]
        if ws: I[v] = ws
    return I


def run(g, mode="xi", hook=None, ck=None, ckget=None, ckset=None, cap=10 ** 6):
    n = g.n; SG, SD = SpecSI(g), SpecSI(dual(g))
    if ck and os.path.exists(ck):
        st = pickle.load(open(ck, "rb"))
        sigma, tau, passes, F, first, seen = st["sigma"], st["tau"], st["passes"], st["F"], st["first"], st["seen"]
        use, useall = st["use"], st["useall"]
        if ckset: ckset(st.get("hook"))
        resumed = passes
    else:
        sigma = SG.initial_strategy_by_best_reward(); tau = SD.initial_strategy_by_best_reward()
        passes = F = 0; first = None; seen = set(); resumed = None
        use = dict.fromkeys(USE, 0); useall = dict.fromkeys(USE, 0)
    vs = vt = None; lastsig = lasttau = None
    while True:
        if ck and passes % CKEVERY == 0 and passes != resumed:
            tmp = ck + ".tmp"
            pickle.dump(dict(sigma=sigma, tau=tau, passes=passes, F=F, first=first, seen=seen, use=use, useall=useall, hook=ckget() if ckget else None), open(tmp, "wb"))
            os.replace(tmp, ck)
        key = digest(sigma, tau)
        if key in seen and passes != resumed: raise RuntimeError("repeated state at pass %d" % passes)
        seen.add(key)
        if sigma != lastsig: vs = SG.evaluate(sigma); lastsig = list(sigma)
        if tau != lasttau: vt = SD.evaluate(tau); lasttau = list(tau)
        Is = improving(SG, sigma, vs); It = improving(SD, tau, vt)
        if hook: hook(passes, sigma, tau, vs, Is, It, F)
        if not Is and not It: break
        passes += 1
        if passes > cap: raise RuntimeError("cap")
        cnt = dict.fromkeys(USE, 0)
        if Is:   # S4a (SPEC) + [N5XI]
            A = [([sigma[v]] + Is.get(v, [])) if g.owner[v] == EVEN else [tau[v]] for v in range(n)]
            hg = restrict(g, A); d2 = SpecSI(dual(hg))
            _, c2 = d2.evaluate_choice([tau[v] if g.owner[v] == ODD else -1 for v in range(n)])
            sig_spec = [c2[v] if g.owner[v] == EVEN else -1 for v in range(n)]
            sig2 = list(sig_spec)
            if mode == "xi":
                Wst = SpecSI(hg).evaluate([sig_spec[v] if g.owner[v] == EVEN else -1 for v in range(n)])
                for v in range(n):
                    if g.owner[v] != EVEN or len(A[v]) < 2: continue
                    if Wst[v][0] == v: cnt["owncyc"] += 1; continue
                    tie = [w for w in sorted(set(A[v])) if ext(SG, v, Wst[w]) == Wst[v]]
                    assert tie, "empty TIE"
                    bestv = None; cand = []
                    for w in tie:
                        if bestv is None or SG.nvo(vs[w], bestv) > 0: bestv = vs[w]; cand = [w]
                        elif SG.nvo(vs[w], bestv) == 0: cand.append(w)
                    sig2[v] = min(cand) if XCTRL == "1" else (sig_spec[v] if sig_spec[v] in cand else max(cand))
                    if len(cand) > 1: cnt["xities"] += 1; cnt["xispec" if sig_spec[v] in cand else "xiidx"] += 1
                    if sig2[v] != sig_spec[v]: cnt["xidiff"] += 1
        else:
            sig2 = list(sigma)
        if It:   # S4b (SPEC)
            A = [([tau[v]] + It.get(v, [])) if g.owner[v] == ODD else [sigma[v]] for v in range(n)]
            cnt["s4b"] += 1; cnt["s4bchoice"] += len(It)
            s3 = SpecSI(restrict(g, A)); _, c3 = s3.evaluate_choice(sigma)
            tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(n)]
        else:
            tau2 = list(tau)
        for k in USE:
            useall[k] += cnt[k]
            if first is None: use[k] += cnt[k]
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
    win = [g.prio[vs[v][0]] % 2 for v in range(n)]                    # S5 (n5b A9)
    _, sbar = SG.evaluate_choice(sigma)
    strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(n)]
    strat = [strat[v] if win[v] == g.owner[v] else None for v in range(n)]
    if ck and os.path.exists(ck): os.remove(ck)
    return dict(Ttot=passes, F=F, first=first, win=win, strat=strat, sigma=sigma, tau=tau, n=n, use=use, useall=useall)


def usestr(r):
    return "tie rules before the first fallback (all passes): " + " ".join("%s %d (%d)" % (k, r["use"][k], r["useall"][k]) for k in USE)


if __name__ == "__main__":
    mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "xi"
    for f in [a for a in sys.argv[1:] if not a.startswith("--") and a not in ("xi", "spec")]:
        r = run(pg.read(f), mode)
        print("n5xi44 %s %s n %d iterations %d fallbacks %d first %s regions_even %d | %s" % (os.path.basename(f), mode, r["n"], r["Ttot"], r["F"], r["first"], r["win"].count(0), usestr(r)), flush=True)
