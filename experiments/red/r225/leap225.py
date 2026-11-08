#!/usr/bin/env python3
"""L-RED 59 R225 item 1: independent census for L-SI 45 box 87 Lemma LEAPFROG-ASC (claude/l-si 6391f53c), on IDEAL-CYC Howard runs
(R221 own.py; no L-SI code). Unit: (mover B, SET-type option S (Xi-target B), maximal interval I of states with Lambda(B) in {K1, K2}
and Lambda(B), Lambda(w), Lambda(g_o) (all o != S) constant), w = succ(e_S). Within the unit:
  PRIV ok  iff on I no play from w or any g_o passes B;  NODE ok iff every g_o has node lam or lower reward on I.
  pi = projection onto E_U (e's at least as relevant as e_S). a_t = pi({e_S} u E_t(w)); b_t = max_lex pi(E_t(g_o)) over o with node lam
  (empty set if none). Events: t -> t+1, both in I, [sigma(B) = S] changes. z = max(a Δ b); M = max(a u b); type I iff no e in a & b is
  more relevant than z.
Counters per unit: ev, k (type II), EU = |E_U|, boundfail (ev > EU + 2k), F2fail (ON with not a > b, or OFF with not b > a),
Bfail (consecutive opposite type-I events with no type-II event between and M not strictly rising), Afail (M decreasing),
Cfail (type II and the deciding e-sequence visits no e more relevant than z after z), depth (max nesting: number of distinct heads
min(H) at type-II events, H = shared e's above z).
Usage: leap225.py G.json ... | leap225.py rand SEED COUNT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
def lexgt(a, b, rk):
    d = a ^ b
    return bool(d) and max(d, key=lambda u: rk[u]) in a
def census(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk
    evs = {V[("e", q)] for q in O}; K1, K2 = V["K1"], V["K2"]
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
                if len(evl) > len(EU) + 2 * kk: tot["boundfail"] += 1
                t = u + 1
    return tot
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        import latch225
        rng = random.Random(int(sys.argv[2])); agg = {}
        for i in range(int(sys.argv[3])):
            G = latch225.rgen(rng); c = census(G)
            for kx, v in c.items(): agg[kx] = max(agg.get(kx, 0), v) if kx.startswith("max") else agg.get(kx, 0) + v
            if c["boundfail"] or c["F2fail"] or c["Afail"] or c["Bfail"] or c["Cfail"]:
                json.dump(G, open(f"out/leapwit_{sys.argv[2]}_{i}.json", "w")); print("WIT", i, c, flush=True)
        print("RAND", sys.argv[2], sys.argv[3], agg, flush=True)
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), census(json.load(open(f))), flush=True)
