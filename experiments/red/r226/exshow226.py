#!/usr/bin/env python3
"""L-RED 60 R226: GENERATED from r225/leap225.py census (same unit + PRIV/NODE logic); prints every unit with #events >= |E_U|.
Usage: exshow226.py G.json ..."""

import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
def lexgt(a, b, rk):
    d = a ^ b
    return bool(d) and max(d, key=lambda u: rk[u]) in a
DUMP = []; THR = 0
def census(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk
    evs = {V[("e", q)] for q in O}; inv = {v: kk for kk, v in V.items()}; K1, K2 = V["K1"], V["K2"]
    tot = dict(units=0, units_hyp=0, ev=0, typeI=0, typeII=0, maxk=0, boundfail=0, F2fail=0, Afail=0, Bfail=0, Cfail=0,
               maxdepth=0, ev_nohyp=0, maxexcess_nohyp=-99, maxexcess=-99)
    plays = []
    for (s, vals, tau) in out:
        nxt = lambda u, s=s, tau=tau: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]))
        plays.append(nxt)
    def play(t, v):
        nxt = plays[t]; seq = []; seen = set()
        while v not in seen: seen.add(v); seq.append(v); v = nxt(v)
        return seq
    def eseq(t, v, pl=None):
        Pi = out[t][1][v][1]; return [u for u in (pl or play(t, v)) if u in evs and u in Pi]
    for B in range(N):
        for k, o in enumerate(G["opts"][B]):
            if o[1] != B: continue
            gS = V[("g", (B, k))]; eS = V[("e", (B, k))]; w = succ[eS][0]
            gos = [V[("g", (B, j))] for j in range(len(G["opts"][B])) if j != k]
            EU = {e for e in evs if rk[e] >= rk[eS]}
            key = lambda t: (out[t][1][B][0], out[t][1][w][0]) + tuple(out[t][1][g][0] for g in gos)
            t = 0
            while t < len(out):
                if out[t][1][B][0] not in (K1, K2): t += 1; continue
                u = t
                while u + 1 < len(out) and key(u + 1) == key(t): u += 1
                I = range(t, u + 1); lam = out[t][1][B][0]
                priv = all(B not in play(i, x) for i in I for x in [w] + gos)
                node = all(out[t][1][g][0] == lam or vj.rew(out[t][1][g][0]) < vj.rew(lam) for g in gos)
                A = {}; Bv = {}; arg = {}
                for i in I:
                    A[i] = frozenset([eS] + [e for e in eseq(i, w) if e in EU])
                    best = frozenset(); bg = None
                    for g in gos:
                        if out[i][1][g][0] != lam: continue
                        x = frozenset(e for e in eseq(i, g) if e in EU)
                        if bg is None or lexgt(x, best, rk): best, bg = x, g
                    Bv[i] = best; arg[i] = bg
                evl = []
                for i in range(t, u):
                    on0, on1 = out[i][0][B] == gS, out[i + 1][0][B] == gS
                    if on0 != on1: evl.append((i, "ON" if on1 else "OFF"))
                tot["units"] += 1
                if not (priv and node):
                    tot["ev_nohyp"] += len(evl)
                    tot["maxexcess_nohyp"] = max(tot["maxexcess_nohyp"], len(evl) - len(EU))
                    t = u + 1; continue
                tot["units_hyp"] += 1; kk = 0; prevI = None; heads = set(); Ms = []
                for (i, d) in evl:
                    a, b = A[i], Bv[i]
                    if d == "ON" and not lexgt(a, b, rk): tot["F2fail"] += 1
                    if d == "OFF" and not lexgt(b, a, rk): tot["F2fail"] += 1
                    dd = a ^ b
                    if not dd: continue
                    z = max(dd, key=lambda e: rk[e]); M = max(a | b, key=lambda e: rk[e]); Ms.append(rk[M])
                    Hh = [e for e in (a & b) if rk[e] > rk[z]]
                    if Hh:
                        kk += 1; heads.add(min(Hh, key=lambda e: rk[e]))
                        # Claim C: the e-sequence holding z visits z before a more relevant e
                        sq = [eS] + eseq(i, w) if z in a else eseq(i, arg[i])
                        if z not in sq or not any(rk[e] > rk[z] for e in sq[sq.index(z) + 1:]): tot["Cfail"] += 1
                        prevI = None
                    else:
                        if prevI is not None and prevI[1] != d and not (rk[M] > prevI[0]): tot["Bfail"] += 1
                        prevI = (rk[M], d)
                if any(Ms[j + 1] < Ms[j] for j in range(len(Ms) - 1)): tot["Afail"] += 1
                tot["ev"] += len(evl); tot["typeII"] += kk; tot["typeI"] += len(evl) - kk; tot["maxk"] = max(tot["maxk"], kk)
                tot["maxdepth"] = max(tot["maxdepth"], len(heads))
                tot["maxexcess"] = max(tot["maxexcess"], len(evl) - len(EU))
                if len(evl) - len(EU) >= THR: DUMP.append(dict(kII=kk, Mrk=list(Ms), eSrk=rk[eS], B=B, k=k, I=(t, u), lam=inv.get(lam, lam), EU=sorted(inv[e][1] for e in EU), ev=[(i, d, sorted(inv[e][1] for e in A[i]), sorted(inv[e][1] for e in Bv[i]), inv[arg[i]][1] if arg[i] is not None else None) for (i, d) in evl], opts=G["opts"][B], start=G["start"][B], T=len(out) - 1))
                if len(evl) > len(EU) + 2 * kk: tot["boundfail"] += 1
                t = u + 1
    return tot
if __name__ == "__main__":
    for f in sys.argv[1:]:
        DUMP.clear(); c = census(json.load(open(f))); print(os.path.basename(f), "maxexcess", c["maxexcess"])
        for d in DUMP: print("  ", d)
