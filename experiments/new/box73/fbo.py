#!/usr/bin/env python3
"""L-NEW box 73: anatomy of FBO events (box 72 §5: GXC events at in-phase Even S4c fallbacks with v in Z_{t+1}) on N5 (or N5-LZC, --lzc).
GAP LEVEL of v at a state = where Xi(v) and W(v) first differ in [S1-ord]: as a tuple key, ('C', rew(W cycle node)) at the cycle level,
('P', r) at rank r of the top vertex of P_Xi xor P_W, ('L',) at the length. Depth order: C > P(r) by r > L (more significant first).
Per FBO event: rel = how the level moves from t to t+1: DOWN (strictly less significant), SAME, UP; at level C, whether W's cycle node
changed. Also per (phase, v): longest run of consecutive FBO events of v at the SAME level with no W-rise of v between them (SAMERUN).
Usage: fbo.py GAME.pg [START] [--lzc] [--verbose]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
import pg
from collections import Counter, defaultdict
args = [a for a in sys.argv[1:] if not a.startswith("--")]; VERB = "--verbose" in sys.argv
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1
XI = [E.evaluate(x)[0] for x in S]; XK = [[E.key(v) for v in x] for x in XI]; LX = [tuple(v[0] for v in x) for x in XI]
ph = [0] * (T + 1)
for k in range(1, T + 1): ph[k] = ph[k - 1] + (LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def level(a, b):
    if a == b: return None
    if a[0] != b[0]: return (3, E.rew[b[0]])
    x = a[1] ^ b[1]
    if x: return (2, x.bit_length() - 1)
    return (1, 0)
ev = [v for v in range(n) if g.owner[v] == 0]
events = []; rel = Counter(); wrise = defaultdict(list)
for k in range(T):
    if ph[k + 1] != ph[k]: continue
    tau = TAU[k]; w0, w1 = Wv(k, tau), Wv(k + 1, tau); Ek = Wc[tau]
    for x in range(n):
        if Ek.key(w1[x]) > Ek.key(w0[x]): wrise[(ph[k], x)].append(k)
    if not FB[k]: continue
    for v in ev:
        if S[k][v] == S[k + 1][v]: continue
        if XI[k][v] != w0[v] and XK[k + 1][v] > XK[k][v] and not Ek.key(w1[v]) > Ek.key(w0[v]) and XI[k + 1][v] != w1[v]:
            l0, l1 = level(XI[k][v], w0[v]), level(XI[k + 1][v], w1[v])
            a0, a1 = (l0[0], l0[1] if l0[0] != 3 else 0), (l1[0], l1[1] if l1[0] != 3 else 0)
            rl = "DOWN" if a1 < a0 else ("SAME" if a1 == a0 else "UP")
            if l0[0] == 3 and l1[0] == 3: rl += "-C-" + ("Wcyc" if w0[v][0] != w1[v][0] else "fixed")
            rel[rl] += 1
            events.append(dict(k=k, ph=ph[k], v=v, l0=l0, l1=l1, rel=rl, Wfell=w0[v] != w1[v], Wcyc=w0[v][0] != w1[v][0]))
samerun = 0
by = defaultdict(list)
for e in events: by[(e['ph'], e['v'])].append(e)
for key, es in by.items():
    run = 1
    for a, b in zip(es, es[1:]):
        paid = any(a['k'] < r <= b['k'] for r in wrise[key])
        if not paid and b['l0'] == a['l1'] and (b['l1'][0], b['l1'][1] if b['l1'][0] != 3 else 0) == (a['l1'][0], a['l1'][1] if a['l1'][0] != 3 else 0): run += 1
        else: run = 1
        samerun = max(samerun, run)
mx = lambda c: max(c.values()) if c else 0
# worst phase: in-phase fallbacks, rho (R56: pairs (transition of the phase, Odd vertex of out-degree >= 2) with Xi changing), R56 bound
pc = Counter(e['ph'] for e in events); wp = max(pc, key=pc.get) if pc else None
Q = [x for x in range(n) if g.owner[x] == 1 and len(set(g.succ[x])) >= 2]
fbin = sum(1 for k in range(T) if ph[k] == ph[k + 1] == wp and FB[k]); rho = sum(1 for k in range(T) if ph[k] == ph[k + 1] == wp for q in Q if XI[k][q] != XI[k + 1][q])
plen = sum(1 for k in range(T) if ph[k] == wp)
nE = sum(1 for x in range(n) if g.owner[x] == 0)
worst = f"worst-phase len {plen} fb {fbin} rho {rho} R56 {1 + (n - 1) * (2 + rho)} nE*R56 {nE * (1 + (n - 1) * (2 + rho))} |Q| {len(Q)}" if wp is not None else "worst-phase none"
print(f"FBO {os.path.basename(args[0])} n {n} iters {T} fbo {len(events)} per-phase {mx(Counter(e['ph'] for e in events))} "
      f"per-v-phase {mx(Counter((e['ph'], e['v']) for e in events))} rel {dict(rel)} samerun {samerun} {worst}")
if VERB:
    for e in events: print("  ", e)
