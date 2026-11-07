#!/usr/bin/env python3
"""L-RED 55 R219: DATA check of Lemma FLIP-E and counts for Lemma GATE-REARM, on own.py runs (independent implementation).
For every state t and every gate g of a level >= 1 option: Lambda of both faces; RET (the beta-play passes g and then e_g); tie
(equal values). At non-RET states with Lambda(e_g) = Lambda(beta_g) = w less relevant than e_g: check
  sigma_bar(g) = e  <=>  E(e_g) <lex E(beta_g)   (E = e-vertices of Pi; lex by the most relevant element of the symmetric difference).
Per gate: flips (face changes between consecutive states), RET states and stretches, tie states, and per maximal interval with both
Lambda's fixed: D_E(y) and D_E(x') (distinct e-sets of the W-target / Xi-target movers) -> bound sum over intervals of
2*min(D_E(y), D_E(x')) + 1 (only intervals with equal Lambda's can flip). Prints totals and the worst gate.
Usage: check219.py G.json ..."""
import sys, json
import own
def run(f):
    G = json.load(open(f)); out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); N = G["N"]
    evs = {V[("e", q)] for q in O}; rk = vj.rk
    def E(val): return frozenset(u for u in val[1] if u in evs)
    def lexlt(A, B):
        d = A ^ B
        return bool(d) and max(d, key=lambda u: rk[u]) in B
    gates = [q for q in O if G["lev"][q[0]] >= 1]
    viol = chk = 0; stats = {}
    for q in gates:
        g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]; wt, xt, _ = G["opts"][q[0]][q[1]]
        y = wt; xp = xt
        faces = []; ret = []; tie = []; lam = []; Ey = []; Ex = []; hi = []
        for (s, vals, tau) in out:
            nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0]))
            v, seen = b, []
            while v not in seen: seen.append(v); v = nxt(v)
            R = g in seen and tau[g] == e
            faces.append(tau[g] == e); ret.append(R); tie.append(vals[e] == vals[b]); lam.append((vals[e][0], vals[b][0]))
            Ey.append(E(vals[y]) if y >= 0 else None); Ex.append(E(vals[xp]) if xp >= 0 else None)
            w = vals[b][0]
            hi.append(vals[e][0] == w and rk[w] > rk[e])
            if not R and vals[e][0] == w and rk[w] < rk[e] and vals[e] != vals[b]:
                chk += 1
                if (tau[g] == e) != lexlt(E(vals[e]), E(vals[b])): viol += 1
        fl = sum(faces[i] != faces[i - 1] for i in range(1, len(faces)))
        rs = sum(1 for i in range(len(ret)) if ret[i] and (i == 0 or not ret[i - 1]))
        bound = 0; i = 0
        while i < len(lam):
            j = i
            while j + 1 < len(lam) and lam[j + 1] == lam[i]: j += 1
            if lam[i][0] == lam[i][1]:
                dy = len(set(Ey[i:j + 1])); dx = len(set(Ex[i:j + 1])); bound += 2 * min(dy, dx) + 1
            i = j + 1
        hf = sum(1 for i in range(1, len(faces)) if faces[i] != faces[i - 1] and (hi[i] or hi[i - 1]))
        stats[q] = (fl, sum(ret), rs, sum(tie), bound, sum(hi), hf)
    worst = max(stats, key=lambda q: stats[q][0])
    over = sum(1 for q in stats if stats[q][0] > stats[q][4] + 2 * stats[q][2] + 2 * stats[q][3])
    print(f"{f.split('/')[-1]} N {G['N']} T {len(out) - 1} gates {len(gates)} | FLIP-E checked {chk} violations {viol} | "
          f"RET states {sum(v[1] for v in stats.values())} stretches {sum(v[2] for v in stats.values())} ties {sum(v[3] for v in stats.values())} | "
          f"hi-w states {sum(v[5] for v in stats.values())} hi-w flips {sum(v[6] for v in stats.values())} | max flips {stats[worst][0]} (bound {stats[worst][4]}, RET-str {stats[worst][2]}, ties {stats[worst][3]}) | gates over bound {over}", flush=True)
for f in sys.argv[1:]:
    J = json.load(open(f))
    if isinstance(J, dict) and "N" in J and "opts" in J: run(f)
