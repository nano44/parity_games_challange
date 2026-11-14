#!/usr/bin/env python3
"""L-NEW box 122 (from box 121 twofix.py): ALL TWO-FIX windows, one line each. TWO-FIX: windows of an N5 run in which BOTH tau and sbar (Odd's optimal counterstrategy to sigma, si.Engine) are constant.
In such a window Xi_k = the valuation of sigma_k in the one-player game G_sbar, Is_k = G_sbar's improving set, and S4a picks the optimum
of the arena {sigma_k} u Is_k in G_tau: a gated improvement run in the one-player game G_sbar, selected by G_tau.
Per window: length L, ODIFF := Odd vertices with sbar != tau, SB := the length of R17's switch-best run on G_sbar from the window's first
sigma (to G_sbar's optimum), and whether each step equals G_sbar's switch-best step (SBSTEP count).
Per window also FB := its S4c fallbacks, MAXSEG := the most consecutive fallback-free transitions, MAXPH := the most
W-changing transitions in one lambda_W-phase (box 120's in-phase definition; W := the valuation in G_tau), PHNF := the same count inside one fallback-free run, FLATNF / LAMNF :=
fallback-free transitions with W unchanged / with the cycle-node map of W changed, O := the Odd vertices with sbar != tau (if ODIFF <= 4), and MINL := min window length printed.
Usage: windows.py G.pg [START|-] [MINL]   prints one WIN line per window of length >= MINL (default 2)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FBL = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FBL.append(r[4])
K = len(S) - 1
SB = [tuple(-1 if own[v] == 0 else E.evaluate(x)[1][v] for v in range(n)) for x in S]
Wc = {}
def eng(o):
    if o not in Wc: Wc[o] = Engine(pg.Game(list(g.prio), list(own), [[o[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[o]
def opt(sig, o, I):
    a = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in I: a[v].add(w)
    succ = [sorted(a[v]) if own[v] == 0 else [o[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(own), succ))).evaluate(tuple(o[v] if own[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 0 else sig[v] for v in range(n))
def sbrun(sig, o, cap=100000):
    e = eng(o); c = 0
    while c < cap:
        I = e.improving(sig, e.evaluate(sig)[0])
        if not I: return c
        ns = opt(sig, o, I)
        if ns == sig: return -c - 1
        sig = ns; c += 1
    return c
wins = []; k = 0
while k < K:
    if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
    a = k
    while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
    wins.append((a, k))
MINL = int(sys.argv[3]) if len(sys.argv) > 3 else 2
for a, b in wins:
    if b - a < MINL: continue
    o = SB[a]; tau = T[a]; O = [v for v in range(n) if own[v] == 1 and o[v] != tau[v]]
    e = eng(o); sbs = 0; et = eng(tau); seg = mseg = 0; ph = mph = 0; flat = lamch = 0; pn = mpn = 0
    Ws = [et.evaluate(S[j])[0] for j in range(a, b + 1)]; lam = [tuple(w[0] for w in x) for x in Ws]
    for j in range(a, b):
        I = e.improving(S[j], e.evaluate(S[j])[0]); sbs += opt(S[j], o, I) == S[j + 1]
        if FBL[j]: seg = 0
        else:
            seg += 1; mseg = max(mseg, seg); flat += Ws[j - a + 1] == Ws[j - a]; lamch += lam[j - a + 1] != lam[j - a]
        i = j - a   # in-phase lambda_W count (box 120 definition), W := tau's valuation; PHNF also resets at fallbacks
        if lam[i] != lam[i + 1]: ph = 0; pn = 0; continue
        if i > 0 and lam[i] != lam[i - 1]: ph = 0; pn = 0
        ph += Ws[i + 1] != Ws[i]; mph = max(mph, ph)
        if FBL[j]: pn = 0
        else: pn += Ws[i + 1] != Ws[i]; mpn = max(mpn, pn)
    print(f"WIN {os.path.basename(sys.argv[1])} n {n} K {K} [{a}, {b}] L {b - a} ODIFF {len(O)} FB {sum(FBL[a:b])} SB {sbrun(S[a], o)} SBSTEP {sbs} MAXSEG {mseg} MAXPH {mph} PHNF {mpn} FLATNF {flat} LAMNF {lamch}"
          + (f" O {[(v, o[v], tau[v]) for v in O]}" if len(O) <= 4 else ""))
