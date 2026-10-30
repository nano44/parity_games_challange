#!/usr/bin/env python3
"""L-NEW box 79: FLAT-SRC data. Per phase (lambda_Xi, tau constant), DEPTH as in box77/fixdepth.py (lcp with the end-of-phase Xi).
FLATTR := Xi-changing transitions with no DEPTH rise (PHASE-RED needs only these: CH_P <= n(n+2) + FLATTR_P). For each flat transition:
does some SWITCHED Even vertex x change Xi(x) (necessarily flat)? [FSW]; else classify by the inheritance source of one changed vertex
(chain: Even unswitched -> sigma(x); Odd with sbar unchanged -> sbar(x)): SBAR (Odd sbar change), CYC/BRK. Per (x, phase): flat switches
FLATSW(x) (switches of x whose Xi(x)-change is flat). Usage: flatsrc.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
from collections import Counter
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
T = len(S) - 1
EV = [E.evaluate(x) for x in S]; XI = [e[0] for e in EV]; SB = [e[1] for e in EV]; LX = [tuple(v[0] for v in x) for x in XI]
ph = [0] * (T + 1)
for k in range(1, T + 1): ph[k] = ph[k - 1] + (LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1])
def depth(a, b):
    if a == b: return n + 2
    if a[0] != b[0]: return 0
    x = a[1] ^ b[1]
    return 1 + (n - 1 - (x.bit_length() - 1)) if x else n + 1
def source(k, z):
    x, seen = z, set()
    while True:
        if x in seen or XI[k][x][0] == x or XI[k + 1][x][0] == x: return "CYC"
        seen.add(x)
        if g.owner[x] == 0:
            if S[k][x] != S[k + 1][x]: return "EVEN"
            y = S[k][x]
        else:
            if SB[k][x] != SB[k + 1][x]: return "SBAR"
            y = SB[k][x]
        if XI[k][y] == XI[k + 1][y]: return "BRK"
        x = y
c = Counter(); flatsw = Counter(); flattr_max = 0
for p in range(ph[-1] + 1):
    ks = [k for k in range(T + 1) if ph[k] == p]
    if len(ks) < 2: continue
    fin = XI[ks[-1]]; ft = 0
    for k in ks[:-1]:
        ch = [v for v in range(n) if XI[k][v] != XI[k + 1][v]]
        if not ch: c['xi-flat'] += 1; continue
        if any(depth(XI[k + 1][v], fin[v]) > depth(XI[k][v], fin[v]) for v in ch): c['K-rise'] += 1; continue
        ft += 1; c['FLATTR'] += 1
        sw = [x for x in ch if g.owner[x] == 0 and S[k][x] != S[k + 1][x]]
        for x in sw: flatsw[(p, x)] += 1
        if sw: c['FSW'] += 1
        else: c['src-' + Counter(source(k, v) for v in ch).most_common(1)[0][0]] += 1
    flattr_max = max(flattr_max, ft)
print(f"FLATSRC {os.path.basename(args[0])} n {n} iters {T} {dict(c)} max-FLATTR-phase {flattr_max} max-FLATSW-(x,phase) {max(flatsw.values(), default=0)}")
