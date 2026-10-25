#!/usr/bin/env python3
"""Box 39 (L-RED): independent checker of L-NEW's CONJECTURE PF-THETA (docs/new/N5-DROP-box35.md §8, trunk 3939d3b0), linear form,
written from the text, not from L-NEW's pfclimb.py / thcls.py. Trace = sox.trace (asserted = n5.run). Scope run as sox3.py (P-N5-CLS §0).
θ_k = Ξ_k(o). Fallback level of a fallback k0 = M_{k0} (max gate level, sox3.M). Statement checked, per scope run S and per level M:
  PF   #{in-run transitions j -> j+1 with θ_{j+1} != θ_j, j > the last fallback k0 < j of S (strictly before j), M_{k0} = M} <= n.
Also: pfi = the same with the fallback transition itself counted under its own level (j >= k0), pfrun = the largest count under ONE
fallback interval (consecutive, not aggregated over equal M), nfb = fallbacks in that run, rfb0 = RISE-LAST events (sox3 definition:
an S4a step strictly between consecutive in-scope fallbacks k0 < k with COARSE_{M_{k0}}(θ) changing; M_{k0} = ∞ skipped).
Usage: pfx.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg, n5
from si import Engine
from sox import BOT, INF, lev, coarse

def analyse(g, cap=5000):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n
    S, FB, E = sox.trace(g, cap)
    it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    N = len(S); ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]; Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd == "tau" else sb[k][x])
        return out
    H1 = [o not in play(k, sb[k][o], "sbar") for k in range(N)]; H2 = [o not in play(k, S[k][1][o], "tau") for k in range(N)]
    def M(k):
        gs = E.improving(S[k][0], Xi[k])
        return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gs), default=BOT)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    cw = [Wv[k][o][0] for k in range(N)]
    scope = [inph[k] and H1[k] and H2[k] and cw[k] == lam[k][o] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    th = [Xi[k][o] for k in range(N)]
    best = dict(pf=0, pfi=0, pfrun=0, nfb=0, M=None, k0=None, n=n, it=len(FB), fb=sum(FB), runs=0, fbruns=0, rfb0=0, rfbchk=0)
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        best["runs"] += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]; Mv = {t: M(t) for t in fbs}
        if fbs: best["fbruns"] += 1
        per, peri, cur, Lf, Lfi = {}, {}, 0, None, None
        for j in range(k, e + 1):
            if FB[j]: Lfi = Mv[j]
            if th[j + 1] != th[j]:
                if Lf is not None: per[Lf] = per.get(Lf, 0) + 1; cur += 1
                if Lfi is not None: peri[Lfi] = peri.get(Lfi, 0) + 1
            if FB[j]:
                if cur > best["pfrun"]: best["pfrun"] = cur
                Lf, cur = Mv[j], 0
        best["pfrun"] = max(best["pfrun"], cur)
        if per:
            Mx = max(per, key=lambda x: per[x])
            if (per[Mx], len(fbs)) > (best["pf"], best["nfb"] if best["M"] is not None else -1): best.update(pf=per[Mx], nfb=len(fbs), M=Mx, k0=k)
        if peri: best["pfi"] = max(best["pfi"], max(peri.values()))
        for i in range(len(fbs) - 1):
            k0, kn = fbs[i], fbs[i + 1]; L = Mv[k0]
            if L == INF: continue
            best["rfbchk"] += 1
            for j in range(k0 + 1, kn):
                if not FB[j] and coarse(th[j + 1], L) != coarse(th[j], L): best["rfb0"] += 1
        k = e + 1
    return best

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        r = analyse(g)
        print(os.path.basename(f), r, "VIOL" if r["pf"] > r["n"] else "", flush=True)
        for kk in ("rfb0", "rfbchk", "fbruns"): tot[kk] = tot.get(kk, 0) + r[kk]
        tot["pfmax/n"] = max(tot.get("pfmax/n", 0), r["pf"] / r["n"]); tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
