#!/usr/bin/env python3
"""L-NEW box 109: the CARRIER chain (box 108 Lemma CARRIER) of the deepest paid transition of an N5 W-run hierarchy. Prints the nested
blocks B_1 > ... > B_h, the paid transition t, every carrier v (lcp_h rises at t), its pending positions c_d (named by vertex / len),
the fix times k_d, and at each k_d the gate edges (new arena edges on v's new W-play: Lemma NEW-EDGE) and whether k_d is a source event
(R97). Usage: trace3.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB, IS = [tuple(s)], [tuple(t)], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2]))
Wc, Wm = {}, {}
def Wraw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def W(k, tau):
    if (k, tau) not in Wm: Wm[(k, tau)] = [cs(x) for x in Wraw(k, tau)]
    return Wm[(k, tau)]
byrank = {E.rank[v]: v for v in range(n)}
def nm(p): return "len" if p == n + 1 else "cyc" if p == 0 else f"u{byrank[n - p]}(p{g.prio[byrank[n - p]]})"
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
def H(j): return {(y, S[j][y]) for y in range(n) if own[y] == 0} | IS[j]
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wraw(k, TAU[k])] != [x[0] for x in Wraw(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
best = None
def block(ks, tau, lev, chain):
    global best
    if not ks: return
    ref = W(ks[-1] + 1, tau); P = lambda j: sum(lcp(x, ref[v]) for v, x in enumerate(W(j, tau)))
    sub, subs = [], []
    for k in ks:
        if P(k + 1) > P(k):
            if best is None or lev > best[0]: best = (lev, k, chain + [(ks, ks[-1] + 1)], tau)
            if sub: subs.append(sub); sub = []
        else: sub.append(k)
    if sub: subs.append(sub)
    for sb in subs: block(sb, tau, lev + 1, chain + [(ks, ks[-1] + 1)])
for run in runs:
    tau = TAU[run[0]]; block([k for k in run if W(k, tau) != W(k + 1, tau)], tau, 1, [])
h, tt, chain, tau = best
print(f"TRACE3 {os.path.basename(sys.argv[1])} n {n} depth {h} paid transition {tt}->{tt + 1}")
for d, (ks, e) in enumerate(chain, 1): print(f"  B_{d}: transitions {ks[0]}..{ks[-1]} ({len(ks)}), ref = W at state {e}")
def gates(k, v):
    if k == 0 or TAU[k - 1] != tau or FB[k - 1]: return "first"
    Nk = H(k) - H(k - 1); x, seen, out = v, set(), []
    while x not in seen:
        seen.add(x)
        if own[x] == 0:
            if (x, S[k + 1][x]) in Nk: out.append((x, S[k + 1][x]))
            x = S[k + 1][x]
        else: x = tau[x]
    return out
def src(k):
    X0, sb0 = E.evaluate(S[k]); X1, sb1 = E.evaluate(S[k + 1]); C = {x for x in range(n) if Wraw(k, tau)[x][0] == x}
    Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
    return int(any(X0[x] != X1[x] for x in Sk))
ref = [W(e, tau) for _, e in chain]
for v in range(n):
    if lcp(W(tt + 1, tau)[v], ref[-1][v]) <= lcp(W(tt, tau)[v], ref[-1][v]): continue
    line = [f"carrier v {v}: level {h} fix at {tt} pos {nm(lcp(W(tt, tau)[v], W(tt + 1, tau)[v]))} gates {gates(tt, v)} src {src(tt)}"]
    for d in range(h - 1, 0, -1):
        ks, e = chain[d - 1]; endsub = chain[d][1]; c = lcp(W(endsub, tau)[v], ref[d - 1][v])
        kd = next(k for k in ks if k >= endsub and lcp(W(k + 1, tau)[v], ref[d - 1][v]) > c)
        line.append(f"level {d} pending {nm(c)} fixed at {kd} gates {gates(kd, v)} src {src(kd)}")
    print("  " + "\n    ".join(line))
