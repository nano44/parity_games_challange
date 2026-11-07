#!/usr/bin/env python3
"""L-RED 55 R219 (a): detail of every RELEASE of an ascent gate in case ii / iii (asc219.py's classification): the gate, the ascent
(a, b), and at the next state which of the two premises broke: (B) the beta-play from beta_h now meets an e before b (or no longer reaches
b), (E) b left e_h's play, plus the movers that switched between t and t+1 on the two plays (PLAY-BLIND). Usage: rel219.py G.json"""
import sys, json
import own
f = sys.argv[1]; G = json.load(open(f)); out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]
evs = {V[("e", q)]: q for q in O}; gof = {V[("g", q)]: q for q in O}; emin = min(rk[e] for e in evs); rv = {v: k for k, v in V.items()}
def nm(v):
    k = rv[v]; return k if isinstance(k, str) else (f"x{k[1]}" if k[0] == "x" else f"{k[0]}{k[1][0]}.{k[1][1]}")
def P(t, v):
    s, vals, tau = out[t]; p, seen = [], set()
    while v not in seen:
        seen.add(v); p.append(v); v = s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0])
    return p
done = set()
for t in range(len(out) - 1):
    s, vals, tau = out[t]
    for v in range(N):
        if rk[vals[v][0]] >= emin: continue
        p = P(t, v); Pi = vals[v][1]; ep = [i for i, u in enumerate(p) if u in evs and u in Pi]
        for i0, i1 in zip(ep, ep[1:]):
            a, b = p[i0], p[i1]
            if rk[b] <= rk[a]: continue
            for j in range(i0 + 1, i1):
                h = p[j]
                if h not in gof or (h, t) in done: continue
                q = gof[h]; eh, bh = V[("e", q)], V[("b", q)]
                if tau[h] != bh or vals[eh][0] != vals[bh][0]: continue
                pe, pb = P(t, eh), P(t, bh); case = "ii" if b in pe else ("iii" if any(u in evs and rk[u] > rk[b] for u in pe[:next((k for k, u in enumerate(pe) if u in set(pb)), len(pe))]) else None)
                if not case: continue
                done.add((h, t))
                if out[t + 1][2][h] != eh: continue
                pe1, pb1 = P(t + 1, eh), P(t + 1, bh)
                eb = [u for u in pb1[:pb1.index(b)] if u in evs] if b in pb1 else "b not reached"
                sw = [nm(x) for x in range(N) if out[t][0][x] != out[t + 1][0][x] and (x in pe or x in pb)]
                print(f"t {t}->{t+1} gate {nm(h)} mover-lev {G['lev'][q[0]]} case {case} ascent {nm(a)}->{nm(b)} | at t+1: e's on beta-play before b {[nm(u) for u in eb] if isinstance(eb, list) else eb}; "
                      f"b on e-play {b in pe1} | switched movers on the t-plays: {sw} | flips of gate {sum(out[u][2][h] != out[u-1][2][h] for u in range(1, len(out)))}")
