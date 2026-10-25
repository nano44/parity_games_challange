#!/usr/bin/env python3
"""Box 38 (L-RED): independent checker of L-SI succ. 4's Lemma NO-RF-OLD (PROVED, lane) and CONJECTURE ENT, written from
docs/si/N5-C-box9.md §8 (trunk 8b1db423), not from L-SI's norf.py. Trace: sox.trace (asserted = n5.run). Notation as sox2.py
(R_k includes o; F_k = V minus R_k; W_k the (σ_k, τ_k) valuation; scope run per P-N5-CLS §0; r_s = lev(θ_s, w_s); M_k max gate level).
For every scope run S, every fallback k0 of S with L := M_{k0} (L may be ⊥ / −1 / ≥ 0; L = ∞ skipped), k := the next fallback of S,
t* := the last state <= k with r_s > L for all s in [k0+1, t*], and every S4a step j in (k0, t*) with COARSE_L(θ_{j+1}) != COARSE_L(θ_j):
  NORF  at every t in [j+1, t*]: no gate (y, z) with y in R_j ∩ R_t and z in F_t;
  ENT   if t* = k and M_k >= 0: no gate (y, z) at k with y in R_k minus R_j and z in F_k   [CONJECTURE].
Also reported: rfb0 (rises of COARSE_L(θ) before a next fallback, any r), rfb (rises in an r > L window with a next fallback),
gap (max of t* − k over those; 0 = the window reaches the fallback), rises, post-rise states with r > L ('win'), windows that reach the next fallback ('reach'), ENT checks done.
Usage: sox3.py game.pg ..."""
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
    R, H1, H2 = [], [], []
    for k in range(N):
        R.append(frozenset({o} | {v for v in range(n) if o in play(k, v, "tau")}))
        H1.append(o not in play(k, sb[k][o], "sbar")); H2.append(o not in play(k, S[k][1][o], "tau"))
    gates = [E.improving(S[k][0], Xi[k]) for k in range(N)]
    def M(k): return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gates[k]), default=BOT)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    cw = [Wv[k][o][0] for k in range(N)]
    scope = [inph[k] and H1[k] and H2[k] and cw[k] == lam[k][o] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    C, ex = {}, {}
    def bad(nm, k): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, k)
    st = dict(runs=0, rises=0, win=0, reach=0, entchk=0, maxwin=0, rfb=0, gap=-10 ** 9)
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        st["runs"] += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]
        for i, k0 in enumerate(fbs):
            L = M(k0)
            if L == INF: continue
            kn = fbs[i + 1] if i + 1 < len(fbs) else None
            last = kn if kn is not None else e + 1          # states of S run to e + 1
            ts = k0
            while ts + 1 <= last and r[ts + 1] > L: ts += 1
            if kn is not None:
                for j in range(k0 + 1, kn):
                    if not FB[j] and coarse(Xi[j + 1][o], L) != coarse(Xi[j][o], L): st["rfb0"] = st.get("rfb0", 0) + 1
            if ts <= k0: continue
            for j in range(k0 + 1, ts):
                if FB[j] or coarse(Xi[j + 1][o], L) == coarse(Xi[j][o], L): continue
                st["rises"] += 1; st["win"] += ts - j; st["maxwin"] = max(st["maxwin"], ts - j)
                if kn is not None: st["rfb"] += 1; st["gap"] = max(st["gap"], ts - kn)
                for t in range(j + 1, ts + 1):
                    for y, z in gates[t]:
                        if y in R[j] and y in R[t] and z not in R[t]: bad("NORF", (j, t, y, z))
                if kn is not None and ts == kn:
                    st["reach"] += 1
                    if M(kn) >= 0:
                        st["entchk"] += 1
                        for y, z in gates[kn]:
                            if y in R[kn] and y not in R[j] and z not in R[kn]: bad("ENT", (j, kn, y, z))
        k = e + 1
    return dict(n=n, o=o, it=len(FB), fb=sum(FB), C=C, ex=ex, **st)

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        r = analyse(g)
        print(os.path.basename(f), {k: r[k] for k in ("n", "it", "fb", "runs", "rises", "win", "maxwin", "reach", "entchk", "rfb", "gap")}, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for k in ("rises", "win", "reach", "entchk"): tot[k] = tot.get(k, 0) + r[k]
        for k, v in r["C"].items(): tot[k] = tot.get(k, 0) + v
        tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
