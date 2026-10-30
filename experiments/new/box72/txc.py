#!/usr/bin/env python3
"""L-NEW box 72 §6: L-SI's TXC (l-si 4fb0bfba docs/si/N5-ADD-box50.md §6, odd/tied.py) against box 70's GXC on the same run.
W-run as in tied.py: consecutive transitions with tau fixed, no S4c fallback, sigma changing, W's cycle-node map (under tau) unchanged.
TXC event (z, s): s in a W-run, Xi_{s+1}(z) > Xi_s(z) strictly, W_{s+1}(z) = W_s(z) (any vertex z; no switch of z needed).
GXC event (v, s): box 70 §3 (v Even switched, tau and lambda_Xi fixed, v in Z_s, strict Xi-rise, W not rising).
SOURCE of a TXC event: follow z's successor while the tie is inherited (Even x not switched -> sigma(x); Odd x with sbar_s(x) = sbar_{s+1}(x)
= tau(x) -> tau(x)), ending at: EVEN-TIE (an Even x switched: Xi(x) rises, W(x) fixed), SBAR (Odd x with sbar_s(x) != sbar_{s+1}(x)),
WIT (Odd x with sbar(x) = sbar' != tau(x): the Xi-play leaves the W-play at x), CYC (x its own Xi- or W-cycle node at s or s+1, or a repeat),
BRK (the next vertex does not carry a tied climb: [V1]/[V2] avoidance fails). Usage: txc.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, HERE); from n5lz import step
import pg
from collections import Counter
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1
EV = [E.evaluate(x) for x in S]; XI = [e[0] for e in EV]; SB = [e[1] for e in EV]
XK = [[E.key(v) for v in x] for x in XI]; LX = [tuple(v[0] for v in x) for x in XI]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
wrun = [None] * T; rid = 0
for k in range(T):
    tau = TAU[k]
    ok = TAU[k + 1] == tau and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, tau)] == [x[0] for x in Wv(k + 1, tau)]
    if ok:
        if k == 0 or wrun[k - 1] is None: rid += 1
        wrun[k] = rid
def tiedat(k, x, w0, w1): return XK[k + 1][x] > XK[k][x] and w0[x] == w1[x]
def source(k, z, w0, w1):
    x, seen = z, set()
    while True:
        if x in seen: return "CYC"
        seen.add(x)
        if XI[k][x][0] == x or XI[k + 1][x][0] == x or w0[x][0] == x or w1[x][0] == x: return "CYC"
        if g.owner[x] == 0:
            if S[k][x] != S[k + 1][x]: return "EVEN-TIE"
            y = S[k][x]
        else:
            if SB[k][x] != SB[k + 1][x]: return "SBAR"
            if SB[k][x] != TAU[k][x]: return "WIT"
            y = TAU[k][x]
        if not tiedat(k, y, w0, w1): return "BRK"
        x = y
txc = []; gxc = set()
for k in range(T):
    tau = TAU[k]
    if TAU[k + 1] == tau and LX[k + 1] == LX[k]:
        w0, w1 = Wv(k, tau), Wv(k + 1, tau); Ek = Wc[tau]
        for v in range(n):
            if g.owner[v] == 0 and S[k][v] != S[k + 1][v] and XI[k][v] != w0[v] and XK[k + 1][v] > XK[k][v] and not Ek.key(w1[v]) > Ek.key(w0[v]):
                gxc.add((v, k))
    if wrun[k] is None: continue
    w0, w1 = Wv(k, tau), Wv(k + 1, tau)
    for z in range(n):
        if tiedat(k, z, w0, w1): txc.append((z, k, source(k, z, w0, w1)))
src = Counter(x[2] for x in txc)
per = Counter((wrun[k], z) for z, k, _ in txc); perrun = Counter(wrun[k] for z, k, _ in txc)
both = sum(1 for z, k, _ in txc if (z, k) in gxc)
gx_in_wrun = sum(1 for v, k in gxc if wrun[k] is not None)
gx_fb = sum(1 for v, k in gxc if FB[k])
mx = lambda c: max(c.values()) if c else 0
print(f"TXC {os.path.basename(args[0])} n {n} iters {T} txc {len(txc)} max-per-z-wrun {mx(per)} max-per-wrun {mx(perrun)} gxc {len(gxc)} "
      f"gxc-in-wrun {gx_in_wrun} gxc-at-fb {gx_fb} txc-and-gxc {both} src {dict(src)}")
