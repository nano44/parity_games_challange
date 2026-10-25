#!/usr/bin/env python3
"""Box 39 (L-RED successor 16): own checker for (2) RISE-LAST (R68 §6), (3) XSN-RUN (R68 §2) and (4) P-N5-TOG §6 RESTARTS
(docs/new/P-N5-TOG-box35.md, trunk; with P-N5-L2 §1 H3-CONST, §2 H2-STICK + fix L2-1), written from the texts. Trace = sox.trace
(asserted = n5.run). Notation (P-N5-TOG §0, P-N5-L2): phase = maximal run of transitions with λ_Ξ and τ constant (states a..b+1);
H1: o on no honest cycle; H2: o on no W-cycle (o not on the (σ,τ)-play from τ(o)); H3: c_w = c_θ (c_w = W(o)'s cycle node, c_θ = λ(o));
(h) = H1 ∧ H2 ∧ H3; R = {o} ∪ {v : the (σ,τ)-play of v meets o}; crossing = R_k != R_{k+1}.
  RESTARTS  per phase: #maximal (h)-runs <= 1 + T + f, T = |U|(n+1) + n − 1; also the sharp form <= 1 + toggles + f, and each restart
            k -> k+1 (¬(h) at k, (h) at k+1) is an H1-toggle or an Even fallback (RCLASS)
  H3CONST   per phase: H3 at all H2 states or at none;   H2STICK: S4a step with H1 ∧ ¬H2 at s keeps ¬H2 at s+1
  XSNRUN    per maximal fallback-free run of a phase: crossings s -> s+1 with c_w(s) = c_θ (the SN prefix, INCLUDING the exit
            transition from the last prefix state) <= n − 1; exitx = how many runs have a crossing at that exit transition
  RISE      rfb0 (sox3 definition): S4a step strictly between consecutive in-scope fallbacks k0 < k with COARSE_{M_k0}(θ) changing;
            thin = θ-changes (any level) at those S4a steps (the near-miss count)
  TEV       (docs/si/N5-RL-box10.md §5, CONJECTURE TEV): in-scope fallback k0, L = M_k0 >= 0, Ev = F_{k0+1} minus F_{k0} = R_k0 minus R_{k0+1};
            at every state t of the scope run with r_s > L for s in [k0+1, t] that comes after an S4a COARSE_L(θ) rise j in (k0, t),
            the honest play of x_t = σ̄_t(o) avoids Ev (r_s = lev(θ_s, w_s)). tev = post-rise states checked, tevpre / tevmeetpre =
            pre-rise states / those whose threat meets Ev. TEVLAST: the same failure with no fallback in (k0, t), i.e. k0 the last
            fallback before t (the form EV+ / TEV-RED use); tevlast = post-rise states checked in that form. TEVCONF: a TEVLAST failure
            at an in-scope fallback state t (TEV-RED (5)'s configuration, the one NJB needs excluded)
Usage: rx16.py game.pg ..."""
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
    R = [frozenset({o} | {v for v in range(n) if o in play(k, v, "tau")}) for k in range(N)]
    H1 = [o not in play(k, sb[k][o], "sbar") for k in range(N)]; H2 = [o not in play(k, S[k][1][o], "tau") for k in range(N)]
    cw = [Wv[k][o][0] for k in range(N)]; H3 = [cw[k] == lam[k][o] for k in range(N)]
    h = [H1[k] and H2[k] and H3[k] for k in range(N)]
    oddfb = [FB[k] and S[k][0] == S[k + 1][0] for k in range(N - 1)]
    def M(k):
        gs = E.improving(S[k][0], Xi[k])
        return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gs), default=BOT)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    C, ex = {}, {}
    def bad(nm, k): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, k)
    st = dict(n=n, it=len(FB), fb=sum(FB), phases=0, maxruns=0, maxslack=-10 ** 9, maxrst=0, rfb=0, rst_tog=0, rst_fb=0,
              maxpre=0, exitx=0, xruns=0, rfb0=0, rfbchk=0, thin=0, tev=0, tevpre=0, tevmeetpre=0, tevfail=0, tevlast=0, tevlastfail=0)
    th = [Xi[k][o] for k in range(N)]; r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    k = 0
    while k < N - 1:
        if not inph[k]: k += 1; continue
        b = k
        while b + 1 < N - 1 and inph[b + 1]: b += 1
        a = k; st["phases"] += 1; states = range(a, b + 2); c = lam[a][o]
        U = sum(1 for v in range(n) if lam[a][v] == c); T = U * (n + 1) + n - 1; f = sum(FB[a:b + 1])
        tog = sum(H1[s] != H1[s + 1] for s in range(a, b + 1))
        runs = sum(1 for s in states if h[s] and (s == a or not h[s - 1]))
        if runs > 1 + T + f: bad("RESTARTS", a)
        if runs > 1 + tog + f: bad("RESTARTS_SHARP", a)
        st["maxruns"] = max(st["maxruns"], runs); st["maxslack"] = max(st["maxslack"], runs - (1 + tog + f)) if runs else st["maxslack"]
        for s in range(a, b + 1):
            if not h[s] and h[s + 1]:
                if H1[s] != H1[s + 1]: st["rst_tog"] += 1
                elif FB[s] and not oddfb[s]: st["rst_fb"] += 1
                else: bad("RCLASS", s)
            if not FB[s] and H1[s] and not H2[s] and H2[s + 1]: bad("H2STICK", s)
        h2s = [H3[s] for s in states if H2[s]]
        if h2s and any(h2s) and not all(h2s): bad("H3CONST", a)
        # XSN-RUN: maximal fallback-free runs of the phase
        s = a
        while s <= b:
            if FB[s]: s += 1; continue
            j = s
            while j + 1 <= b and not FB[j + 1]: j += 1
            ss = list(range(s, j + 2)); p = 0
            while p < len(ss) and cw[ss[p]] == c: p += 1
            if any(cw[x] == c for x in ss[p:]): bad("PREFIX", s)
            pre = sum(R[x] != R[x + 1] for x in ss[:p] if x < ss[-1])
            st["xruns"] += 1; st["maxpre"] = max(st["maxpre"], pre)
            if pre > n - 1: bad("XSNRUN", s)
            if 0 < p < len(ss) and R[ss[p - 1]] != R[ss[p]]: st["exitx"] += 1
            s = j + 1
        k = b + 1
    # RISE-LAST on scope runs (sox3 definition)
    scope = [inph[k] and H1[k] and H2[k] and H3[k] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]
        for k0 in fbs:   # TEV (N5-RL-box10 §5, l-si 90b5fb3f): post-rise states t with r > L on [k0+1, t]: x_t's honest play avoids Ev
            L = M(k0)
            if L == INF or L < 0: continue
            Ev = R[k0] - R[k0 + 1]; risen = False; t = k0 + 1
            while t <= e + 1 and r[t] > L:
                if Ev:
                    meet = bool(set(play(t, sb[t][o], "sbar")) & Ev)
                    if risen:
                        st["tev"] += 1; last = not any(FB[s] for s in range(k0 + 1, t))
                        st["tevlast"] += last
                        if meet: st["tevfail"] += 1; bad("TEV", (k0, t, L))
                        if meet and last:
                            bad("TEVLAST", (k0, t, L)); st["tevlastfail"] += 1; st.setdefault("tevlist", []).append((k0, t, L))
                            if t <= e and FB[t]: bad("TEVCONF", (k0, t, L, M(t)))   # TEV-RED (5): the failure at the next fallback
                    else: st["tevpre"] += 1; st["tevmeetpre"] += meet
                if t <= e and not FB[t] and coarse(th[t + 1], L) != coarse(th[t], L): risen = True
                t += 1
        for i in range(len(fbs) - 1):
            k0, kn = fbs[i], fbs[i + 1]; L = M(k0)
            if L == INF: continue
            st["rfbchk"] += 1
            for j in range(k0 + 1, kn):
                if not FB[j] and th[j + 1] != th[j]: st["thin"] += 1
                if not FB[j] and coarse(th[j + 1], L) != coarse(th[j], L): st["rfb0"] += 1; bad("RISE", (k0, j, kn))
        k = e + 1
    return dict(C=C, ex=ex, **st)

KEYS = ("n", "it", "fb", "phases", "maxruns", "maxslack", "rst_tog", "rst_fb", "maxpre", "exitx", "xruns", "rfbchk", "rfb0", "thin", "tev", "tevpre", "tevmeetpre", "tevlast", "tevlastfail")
if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        try: r = analyse(g)
        except AssertionError as e: print(os.path.basename(f), "ASSERT", e, flush=True); continue
        print(os.path.basename(f), {k: r[k] for k in KEYS}, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for kk in ("rst_tog", "rst_fb", "exitx", "xruns", "rfbchk", "rfb0", "tev", "tevpre", "tevmeetpre", "tevlast"): tot[kk] = tot.get(kk, 0) + r[kk]
        for kk, v in r["C"].items(): tot[kk] = tot.get(kk, 0) + v
        tot["maxpre-(n-1)"] = max(tot.get("maxpre-(n-1)", -10 ** 9), r["maxpre"] - (r["n"] - 1)); tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
