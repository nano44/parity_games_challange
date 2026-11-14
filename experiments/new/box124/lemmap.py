#!/usr/bin/env python3
"""L-NEW box 124: R17 (b) Lemma P's CONCLUSION inside TWO-FIX pieces. A PIECE := a maximal run of consecutive transitions of a TWO-FIX
window (tau, sbar fixed) with no S4c fallback and with lambda_W (cycle-node map of W, W := the valuation in G_tau) constant at every state.
For the piece's first state rho_0 and each later state k of the piece (k := transitions since the piece start), test
    W_k(x) >= value(r)  for every vertex x and every simple path r of G_tau from x to a cycle node u of rho_0 with L <= k edges,
value(r) := (u, P(r), L) as in docs/new/N5-phase-bound-box10.md §2 (best path per (u, x, L) by DFS, as tail/segP_check.py).
Violations are classified by the first hop (x, z) of the violating path: BLK if (x, z) is W-improving but not Xi-improving at the previous
state (the gate blocks the switch Lemma P's case B needs), with INX / INZ := x / z in D (play through an ODIFF vertex).
Usage: lemmap.py G.pg [START|-] [NMAX]   (games with n > NMAX, default 32, are skipped)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
NMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 32
n = g.n; own = g.owner; base = os.path.basename(sys.argv[1])
if n > NMAX: print(f"LEMMAP {base} n {n} SKIP"); sys.exit(0)
E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1
SB = [tuple(-1 if own[v] == 0 else E.evaluate(x)[1][v] for v in range(n)) for x in S]
Wc = {}
def eng(o):
    if o not in Wc: Wc[o] = Engine(pg.Game(list(g.prio), list(own), [[o[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[o]
def best_paths(et, tau, cyc, kmax):
    succ = [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]; best = {}
    for u in cyc:
        def dfs(x0, x, path, seen):
            if len(path) >= kmax: return
            for w in succ[x]:
                if w == u:
                    P = 0
                    for v in path + [x]:
                        if et.rank[v] > et.rank[u]: P |= et.bit[v]
                    L = len(path) + 1; val = (u, P, L); key = (u, x0, L)
                    if key not in best or et.key(val) > et.key(best[key][0]): best[key] = (val, path + [x, u])
                elif w not in seen: dfs(x0, w, path + [x], seen | {w})
        for x in range(n):
            if x != u: dfs(x, x, [], {x})
    return best
checks = viol = pieces = 0; cls = dict(BLK=0, NOTBLK=0, INX=0, INZ=0); longest = 0
k = 0
while k < K:
    if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
    a = k
    while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
    b = k; tau = T[a]; o = SB[a]; et = eng(tau); O = {v for v in range(n) if own[v] == 1 and o[v] != tau[v]}
    W = {j: et.evaluate(S[j])[0] for j in range(a, b + 1)}; lam = {j: tuple(w[0] for w in W[j]) for j in W}
    def D(j):
        f = lambda v: S[j][v] if own[v] == 0 else o[v]; out = set()
        for x in range(n):
            y = x; seen = set()
            while y not in seen:
                if y in O: out.add(x); break
                seen.add(y); y = f(y)
        return out
    j = a
    while j < b:   # pieces: start at j, extend while transition j' is fallback-free and lambda equal at both ends
        p0 = j
        while j < b and not FB[j] and lam[j + 1] == lam[p0]: j += 1
        if j > p0:
            pieces += 1; longest = max(longest, j - p0)
            cyc = sorted(set(lam[p0])); best = best_paths(et, tau, cyc, j - p0)
            for q in range(p0 + 1, j + 1):
                kk = q - p0
                for (u, x, L), (val, path) in best.items():
                    if L > kk: continue
                    checks += 1
                    if et.key(W[q][x]) < et.key(val):
                        viol += 1; z = path[1]
                        Xp = E.evaluate(S[q - 1])[0]; Wp = W[q - 1]
                        wimp = own[x] == 0 and et.key(Wp[z]) > et.key(Wp[S[q - 1][x]]); ximp = own[x] == 0 and E.key(Xp[z]) > E.key(Xp[S[q - 1][x]])
                        if wimp and not ximp: cls["BLK"] += 1
                        else: cls["NOTBLK"] += 1
                        Dq = D(q - 1); cls["INX"] += x in Dq; cls["INZ"] += z in Dq
                        if viol <= int(os.environ.get("SHOW", "0")): print("VIOL", dict(q=q, piece=(p0, j), x=x, u=u, L=L, path=path, W=W[q][x], val=val, wimp=wimp, ximp=ximp))
        if j == p0: j += 1
print(f"LEMMAP {base} n {n} K {K} pieces {pieces} longest {longest} checks {checks} viol {viol} " + " ".join(f"{a} {b}" for a, b in cls.items()))
