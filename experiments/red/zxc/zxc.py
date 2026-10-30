#!/usr/bin/env python3
"""L-RED successor 32 (R134): ZXC per W-run (L-SI box 51 §3, l-si 7dd85b02: ZXC_F(z) := transitions s -> s+1 of F with z in Z_s, i.e.
Xi_s(z) != W_s(z), and Xi_(s+1)(z) > Xi_s(z)), on L-NEW's n5x step (--lzc: box72 n5lz.step from env LNEW, default /tmp/claude-0/lnew).
W-run: tau fixed, sigma moves, no S4c, W cycle-node map fixed (as tied.py). Prints per game: iterations, longest W-run |F|, and the top
vertices by ZXC_F(z) in their W-run (name, ZXC, |F|, Even/Odd). Also TXC (climbs with W(z) fixed). Usage: zxc.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5x
from n5x import load, start_pair, readstart, Engine, dual
step = n5x.step
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(os.environ.get("LNEW", "/tmp/claude-0/lnew"), "experiments", "new", "box72")); import n5lz; step = n5lz.step
import pg
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; st = readstart(args[1]) if len(args) > 1 else None
names = {}
for l in open(args[0]):
    if '"' in l: names[int(l.split()[0])] = l.split('"')[1]
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); s, t = tuple(s), tuple(t)
WE = {}
def W(s, t):
    if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    return WE[t].evaluate(s)[0]
def keys(e, vals): return [e.key(x) for x in vals]
S = [(s, t)]; FB = []
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    s, t = tuple(r[0]), tuple(r[1]); S.append((s, t)); FB.append(r[4])
T = len(S) - 1
XK = []; WV = []; WK = []
for (s, t) in S:
    xv = E.evaluate(s)[0]; XK.append(keys(E, xv)); w = W(s, t); WV.append(w); WK.append(keys(WE[t], w))
# gap: Xi_s(z) != W_s(z) as valuations (both are (cycle, pathmask, len) on the same vertex set)
XV = [E.evaluate(s)[0] for s, _ in S]
cut = [S[k][1] != S[k + 1][1] or S[k][0] == S[k + 1][0] or FB[k] or any(WV[k][x][0] != WV[k + 1][x][0] for x in range(n)) for k in range(T)]
best = []; longest = 0; a = 0
while a < T:
    b = a
    while b < T and not cut[b]: b += 1          # transitions a..b-1 form the W-run
    L = b - a; longest = max(longest, L)
    if L:
        for z in range(n):
            zx = sum(1 for k in range(a, b) if tuple(XV[k][z]) != tuple(WV[k][z]) and XK[k + 1][z] > XK[k][z])
            tx = sum(1 for k in range(a, b) if XK[k + 1][z] > XK[k][z] and WK[k + 1][z] == WK[k][z])
            best.append((zx, tx, names.get(z, str(z)), L, "EO"[g.owner[z]]))
    a = b + 1
best.sort(reverse=True)
print(f"ZXC {os.path.basename(args[0])} n {n} iter {T} fallbacks {sum(FB)} longest-W-run {longest} top " + " ".join(f"{nm}:{zx}/{L}{o}(TXC {tx})" for zx, tx, nm, L, o in best[:4]))
