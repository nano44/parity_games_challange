#!/usr/bin/env python3
"""L-SI box 52: the cases of the BF-W proof (note §3). In each event-free window of a W-run (rwin.py), for each Even switch y: a -> b at
transition k -> k+1 with offset j = k - k0 >= 1, H_t(y) := {sigma_t(y)} u {w : Xi_t(w) > Xi_t(sigma_t(y))}:
  NE  b not in H_(k-1)(y) (a new arena entry);   WR  else, W_(k+1)(b) != W_k(b);
  TT  else, a is W_(k+1)-tight at y (y (+) W_(k+1)(a) = W_(k+1)(y));   RR  else, the (sigma_(k+1), tau)-path from a to its cycle node
  contains y;   OT  anything else.
V<case>: those with W-length l_(k+1)(y) <= j (BF-W violations). J0: switches at offset 0 (not classified). Also MINJ: the least
l_(k+1)(y) - j over all classified switches.  Usage: swcase.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a_ = sys.argv[1:]; g = load(a_[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a_[1]) if len(a_) > 1 else None)
S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; EV = [E.evaluate(x) for x in S]; XK = [[E.key(y) for y in e[0]] for e in EV]
Wc = {}
def WE(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def Wv(k, tau): return WE(tau).evaluate(S[k])[0]
runs, cur = [], None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = dict(J0=0, NE=0, WR=0, TT=0, RR=0, OT=0, VNE=0, VWR=0, VTT=0, VRR=0, VOT=0, MINJ=10 ** 9)
def H(k, y):
    cur = S[k][y]; kc = XK[k][cur]
    return {cur} | {w for w in g.succ[y] if XK[k][w] > kc}
for p, q in runs:
    tau = TAU[p]; C = {x for x in range(n) if Wv(p, tau)[x][0] == x}; We = WE(tau)
    def U(k):
        sb = EV[k][1]
        return {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
    k0 = p
    for k in range(p, q):
        ev = EV[k][1] != EV[k + 1][1] or any(S[k][x] != S[k + 1][x] for x in C if own[x] == 0) or \
             any(XK[k][u] != XK[k + 1][u] for u in U(k) | U(k + 1))
        if ev: k0 = k + 1; continue
        j = k - k0; W0, W1 = Wv(k, tau), Wv(k + 1, tau)
        for y in range(n):
            if own[y] != 0 or S[k][y] == S[k + 1][y]: continue
            if j == 0: c['J0'] += 1; continue
            a, b = S[k][y], S[k + 1][y]
            if b not in H(k - 1, y): cs = 'NE'
            elif W1[b] != W0[b]: cs = 'WR'
            elif We.extend(y, W1[a]) == W1[y]: cs = 'TT'
            else:
                x, seen, hit = a, set(), False
                while x not in seen and W1[x][0] != x:
                    if x == y: hit = True; break
                    seen.add(x); x = S[k + 1][x] if own[x] == 0 else tau[x]
                cs = 'RR' if hit else 'OT'
            c[cs] += 1; lv = W1[y][2]; c['MINJ'] = min(c['MINJ'], lv - j)
            if lv <= j: c['V' + cs] += 1
print(f"SWC {os.path.basename(a_[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
