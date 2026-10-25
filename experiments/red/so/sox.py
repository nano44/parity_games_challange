#!/usr/bin/env python3
"""Box 36 (L-RED): independent checker of P-N5-SO (docs/new/P-N5-SO-box32.md, sha1 deb5ee44) and P-N5-LP §4 J <= S_o and K
(docs/new/P-N5-LP-box32.md, sha1 d2c8121a; fixes docs/new/P-N5-LP-fixes-box32.md), written from the frozen text, not from L-NEW's
socheck.py. Trace = own copy of experiments/new/n5.py run() (asserted equal in iterations/fallbacks to n5.run). Engine = L-SI si.py
(read-only). Per phase (λ_Ξ and τ constant) on 𝒞^1O (asserted: exactly one Odd vertex o with out-degree > 1):
  TH  Θ <= (n-1) + n(X+1) + X;   SO  S_o <= Θ + (d_o-1)(Θ+1);   J <= S_o;   K = #transitions with a wake (LP §3 definition).
Sub-claims checked at every in-phase transition (each a separate counter): CAP1 (σ̄(o) is a full Ξ-minimiser, θ = o ⊕ Ξ(σ̄ o)),
TIE (relevant σ̄(o) change with θ unchanged: old choice not in T_{k+1}), TSHRINK (T_{k+1} ⊆ T_k on a θ-run), RUN (<= d_o-1 such changes
per θ-run), KEY (x in T_k ∩ T_{k+1}: H-path to c unchanged), H1C (H1 constant on crossing-free intervals), THH1 (H1, crossing-free
θ-change: x0 = σ̄_k(o) in F and Ξ(x0) changes), THN (¬H1: θ = (c, ∅, d)), J1 (non-tame: σ̄(o) changes at level > M_k).
Usage: sox.py game.pg ...   (prints one line per file and a total)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(EXP, "new")); sys.path.insert(0, os.path.join(EXP, "si")); sys.path.insert(0, os.path.join(EXP, "harness"))
import pg
from si import Engine
import n5
BOT, INF = -2, 10 ** 6

def load(p): return pg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
def oddchoice(g): return [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]

def trace(g, cap=5000):
    """States (σ_k, τ_k) and fallback flags of n5.run (same code path, own copy)."""
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best")); S = [(tuple(sigma), tuple(tau))]; FB = []
    while len(FB) < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        fb = ns == sigma and nt == tau
        if fb:
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt; S.append((tuple(sigma), tuple(tau))); FB.append(fb)
    return S, FB, E

def lev(x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1
def coarse(x, L):
    if L == BOT: return x
    if L == INF: return 0
    return (x[0], x[1] >> (L + 1))

def analyse(g, cap=5000):
    oc = oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n; d_o = len(set(g.succ[o]))
    S, FB, E = trace(g, cap)
    it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    K_ = len(S); ev = [E.evaluate(s) for s, _ in S]
    Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]; lam = [tuple(x[0] for x in X) for X in Xi]
    key = E.key
    def nxt(k, v): return S[k][0][v] if g.owner[v] == 0 else sb[k][v]
    def play(k, v, odd):   # odd = strategy for Odd: 'tau' or 'sbar'
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd == "tau" else sb[k][x])
        return out, x
    R = []
    for k in range(K_):
        r = {o}
        for v in range(n):
            p, _ = play(k, v, "tau")
            if o in p: r.add(v)
        R.append(frozenset(r))
    H1 = []
    for k in range(K_):
        p, back = play(k, sb[k][o], "sbar"); H1.append(o not in p)
    def M(k):
        Is = E.improving(S[k][0], Xi[k])
        return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in Is), default=BOT)
    def Lk(k):
        L, ev_ = BOT, []
        for v in range(n):
            if lam[k][v] == v: continue
            a, b = (S[k][0][v], S[k + 1][0][v]) if g.owner[v] == 0 else (sb[k][v], sb[k + 1][v])
            if a != b:
                l = lev(Xi[k][a], Xi[k][b]); L = max(L, l)
                if g.owner[v] == 0: ev_.append((v, a, b, l))
        return L, ev_
    def hpath(k, x, c):
        out = [x]
        while out[-1] != c and len(out) <= n: out.append(nxt(k, out[-1]))
        return tuple(out)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(K_ - 1)]
    C = {}; ex = {}
    def bad(name, k):
        C[name] = C.get(name, 0) + 1; ex.setdefault(name, k)
    phases = []; k = 0
    while k < K_ - 1:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < K_ - 1 and inph[j + 1]: j += 1
        phases.append((k, j)); k = j + 1
    rows = []
    for (a, b) in phases:
        Th = So = X = J = Kw = 0; run_changes = 0; prev_rel = None; maxrun = 0; tiepure = 0; fixch = 0
        c = lam[a][o]; lamo = c != o
        Ms = {}
        for k in range(a, b + 1):
            cross = R[k] != R[k + 1]; X += cross
            if k not in Ms: Ms[k] = M(k)
            Mk = Ms[k]; tame = all(coarse(Xi[k + 1][v], Mk) == coarse(Xi[k][v], Mk) for v in range(n))
            if not tame:
                J += 1
                if not (sb[k][o] != sb[k + 1][o] and lev(Xi[k][sb[k][o]], Xi[k][sb[k + 1][o]]) > Mk): bad("J1", k)
            if not cross and H1[k] != H1[k + 1]: bad("H1C", k)
            # wakes
            L, evs = Lk(k)
            if L != BOT:
                if prev_rel is not None:
                    pk, pL = prev_rel
                    if not any(FB[i] for i in range(pk, k + 1)) and all(R[i] == R[k] for i in range(pk, k + 2)) and any(l > pL for *_, l in evs):
                        Kw += 1
                prev_rel = (k, L)
            if lamo:
                th0, th1 = Xi[k][o], Xi[k + 1][o]
                for kk in (k, k + 1):
                    mk = min(key(Xi[kk][x]) for x in g.succ[o])
                    if key(Xi[kk][sb[kk][o]]) != mk or E.extend(o, Xi[kk][sb[kk][o]]) != Xi[kk][o]: bad("CAP1", kk)
                if th0 != th1:
                    Th += 1; run_changes = 0
                    if not cross:
                        if H1[k]:
                            x0 = sb[k][o]
                            if x0 in R[k] and x0 != o or Xi[k][x0] == Xi[k + 1][x0]: bad("THH1", k)
                        elif th0[1] != 0 or th1[1] != 0: bad("THN", k)
                mu0 = Xi[k][sb[k][o]]; mu1 = Xi[k + 1][sb[k + 1][o]]
                T0 = {x for x in g.succ[o] if Xi[k][x] == mu0}; T1 = {x for x in g.succ[o] if Xi[k + 1][x] == mu1}
                if sb[k][o] != sb[k + 1][o]:
                    So += 1
                    if th0 == th1:
                        run_changes += 1; fixch += 1; maxrun = max(maxrun, run_changes)
                        if run_changes > d_o - 1: bad("RUN", k)
                        if sb[k][o] in T1: bad("TIE", k)
                        if sb[k][o] in T0 and sb[k + 1][o] in T0 and Xi[k][sb[k + 1][o]] == mu0: tiepure += 1
                if th0 == th1:
                    if not T1 <= T0: bad("TSHRINK", k)
                    for x in T0 & T1:
                        if x != o and hpath(k, x, c) != hpath(k + 1, x, c): bad("KEY", k)
        if Th > (n - 1) + n * (X + 1) + X: bad("TH", a)
        if So > Th + (d_o - 1) * (Th + 1): bad("SO", a)
        if J > So: bad("JSO", a)
        rows.append(dict(a=a, b=b, T=b - a + 1, Th=Th, So=So, X=X, J=J, K=Kw, maxrun=maxrun, tiepure=tiepure, fixch=fixch, d_o=d_o,
                         fb=sum(FB[a:b + 1])))
    return dict(n=n, o=o, it=len(FB), fb=sum(FB), rows=rows, C=C, ex=ex)

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = load(f)
        if len(oddchoice(g)) != 1: print(os.path.basename(f), "SKIP not C^1O"); continue
        r = analyse(g); rs = r["rows"]
        mx = {k: max((x[k] for x in rs), default=0) for k in ("Th", "So", "X", "J", "K", "maxrun", "tiepure")}
        print(os.path.basename(f), f"n {r['n']} o {r['o']} it {r['it']} fb {r['fb']} phases {len(rs)} max", mx, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for k, v in r["C"].items(): tot[k] = tot.get(k, 0) + v
        tot["files"] = tot.get("files", 0) + 1; tot["phases"] = tot.get("phases", 0) + len(rs)
    print("TOTAL", tot)
