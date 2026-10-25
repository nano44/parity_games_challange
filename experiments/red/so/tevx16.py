#!/usr/bin/env python3
"""Box 39 (L-RED successor 16): own checker of L-SI succ. 6's docs/si/N5-TEV-box11.md (l-si 3f08db7, sha1 58a0b3cf) in setting (Σ),
written from the text, not from rb.py. Trace = sox.trace (asserted = n5.run). Notation (§0): R̄_s = {o} ∪ {v : (σ_s, τ)-play meets o},
R_s = R̄_s minus {o}, F_s = V minus R̄_s; π_v^s = vertex set of v's (σ_s, τ)-play from v up to o (excluded), π_o = ∅; c = θ's cycle node;
H = vertices of rank > max(L, rank c); A = P(θ_k0) ∩ H, B = P(θ_k) ∩ H (P = the path-component vertex set); b_k(v) = Ξ_k(σ_k v);
Ev = F_{k0+1} minus F_{k0}.
(Σ): S a scope run (as sox3 / rx16), k0 < k consecutive fallbacks of S, L = M_k0 >= 0 (not ∞), r_s > L for every s in [k0+1, k]. Checked:
  S3    F_k ⊆ F_s for s in [k0+1, k];                        S4   M_k <= L
  FZ    v in F_k: COARSE_L(Ξ_k v) = COARSE_L(Ξ_k0 v)
  BF    Even v in R_k0 ∩ F_k, a = σ_k0(v): COARSE_L(b_k v) = COARSE_L(Ξ_k0 a), both with cycle node c
  RB    the same v with a in R̄_k: COARSE_L(Ξ_k a) = COARSE_L(Ξ_k0 a)
  WALKa / WALKb / WALKc   Corollary WALK (a), (b) (both unions disjoint and equal), (c) for every v0 in R_k0 ∩ F_k
  CYCEV c's σ_k-cycle (the cycle of x_k = σ̄_k(o)'s honest play) has no Ev vertex: counted over all (Σ) pairs (CYCEV_ALL, a statement
        the text does not make) and over pairs with a COARSE_L(θ) change in (k0, k) (CYCEV, the text's setting)
  TEVF  pairs with a COARSE_L(θ) change in (k0, k): x_k's whole σ_k-play avoids Ev (TEV at fallback states, §3 Remarks)
Usage: tevx16.py game.pg ..."""
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
    def tplay(k, v):                      # (σ_k, τ)-play from v, up to the first repeat
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else S[k][1][x]
        return out
    def hplay(k, v):                      # honest play (σ_k, σ̄_k)
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else sb[k][x]
        return out, x                     # x = first repeated vertex: the play's cycle starts there
    def route(k, v):                      # π_v^k: vertices from v up to o, excluded
        if v == o: return set()
        p = tplay(k, v); assert o in p, "route without o"
        return set(p[:p.index(o)])
    Rb = [frozenset({o} | {v for v in range(n) if o in tplay(k, v)}) for k in range(N)]
    H1 = [o not in hplay(k, sb[k][o])[0] for k in range(N)]; H2 = [o not in tplay(k, S[k][1][o]) for k in range(N)]
    cw = [Wv[k][o][0] for k in range(N)]
    th = [Xi[k][o] for k in range(N)]; r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    def M(k):
        gs = E.improving(S[k][0], Xi[k])
        return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gs), default=BOT)
    rk = E.rank
    def ranks(mask): return {i for i in range(n) if mask >> i & 1}
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    scope = [inph[k] and H1[k] and H2[k] and cw[k] == lam[k][o] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    C, ex = {}, {}
    def bad(nm, x): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, x)
    st = dict(n=n, it=len(FB), fb=sum(FB), pairs=0, rise_pairs=0, fz=0, bf=0, rb=0, walk=0, walkc=0, cycev=0, tevf=0, evsize=0)
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]
        for i in range(len(fbs) - 1):
            k0, k1 = fbs[i], fbs[i + 1]; L = M(k0)
            if L == INF or L < 0 or not all(r[s] > L for s in range(k0 + 1, k1 + 1)): continue
            st["pairs"] += 1; c = th[k0][0]; hmin = max(L, rk[c])
            Hr = lambda s: {x for x in s if x > hmin}          # on rank sets
            A, B = Hr(ranks(th[k0][1])), Hr(ranks(th[k1][1]))
            Fk = set(range(n)) - Rb[k1]; Ev = (Rb[k0] - Rb[k0 + 1]) - {o}; st["evsize"] += len(Ev)
            rise = any(coarse(th[j + 1], L) != coarse(th[j], L) for j in range(k0 + 1, k1))
            st["rise_pairs"] += rise
            for s in range(k0 + 1, k1 + 1):
                if not Fk <= set(range(n)) - Rb[s]: bad("S3", (k0, k1, s))
            if M(k1) > L: bad("S4", (k0, k1))
            for v in Fk:
                st["fz"] += 1
                if coarse(Xi[k1][v], L) != coarse(Xi[k0][v], L): bad("FZ", (k0, k1, v))
            for v in Rb[k0] & Fk:
                if v == o or g.owner[v] != 0: continue
                a = S[k0][0][v]; st["bf"] += 1
                bk = Xi[k1][S[k1][0][v]]
                if coarse(bk, L) != coarse(Xi[k0][a], L) or bk[0] != c or Xi[k0][a][0] != c: bad("BF", (k0, k1, v))
                if a in Rb[k1]:
                    st["rb"] += 1
                    if coarse(Xi[k1][a], L) != coarse(Xi[k0][a], L): bad("RB", (k0, k1, v, a))
            for v0 in (Rb[k0] - {o}) & Fk:
                p = tplay(k0, v0); rt = p[:p.index(o)] + [o]        # a_0 .. a_m, a_{m+1} = o
                j = next(i for i in range(1, len(rt)) if rt[i] in Rb[k1]); v, aj = rt[j - 1], rt[j]; st["walk"] += 1
                if not (v in Fk and v in Rb[k0] and v != o and g.owner[v] == 0 and S[k0][0][v] == aj): bad("WALKa", (k0, k1, v0, v))
                Pk = Hr({rk[x] for x in route(k1, aj)}); P0 = Hr({rk[x] for x in route(k0, aj)})
                if (Pk & B) or (P0 & A) or (Pk | B) != (P0 | A): bad("WALKb", (k0, k1, v0, aj))
                if not Hr({rk[x] for x in route(k0, rt[1])}):
                    st["walkc"] += 1
                    if not B <= A: bad("WALKc", (k0, k1, v0))
            hp, x0 = hplay(k1, sb[k1][o]); cyc = set(hp[hp.index(x0):])
            if c not in cyc: bad("CYCNODE", (k0, k1))
            if cyc & Ev: bad("CYCEV_ALL", (k0, k1, sorted(cyc & Ev)))
            if rise:
                st["cycev"] += 1; st["tevf"] += 1
                if cyc & Ev: bad("CYCEV", (k0, k1, sorted(cyc & Ev)))
                if set(hp) & Ev: bad("TEVF", (k0, k1, sorted(set(hp) & Ev)))
        k = e + 1
    return dict(C=C, ex=ex, **st)

KEYS = ("n", "it", "fb", "pairs", "rise_pairs", "fz", "bf", "rb", "walk", "walkc", "cycev", "tevf", "evsize")
if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        try: r = analyse(g)
        except AssertionError as er: print(os.path.basename(f), "ASSERT", er, flush=True); continue
        print(os.path.basename(f), {k: r[k] for k in KEYS}, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for kk in KEYS[3:]: tot[kk] = tot.get(kk, 0) + r[kk]
        for kk, v in r["C"].items(): tot[kk] = tot.get(kk, 0) + v
        tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
