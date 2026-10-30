#!/usr/bin/env python3
"""L-NEW box 72: anatomy of GXC events (box 70 §3: v Even switched, tau and lambda_Xi fixed, v in Z_t, Xi(v) strict rise, W(v) not rising;
W read with tau_t). Plain N5 (box21/n5x.step), S3 start or START file. Same run and W engine as box70/silent.py.
Per event: GAP LEVEL before/after = where Xi(v) and W(v) first differ in the [S1-ord] order: 'C' (cycle node), rank r of the top vertex
of P_Xi xor P_W, or 'L' (length only); '=' if equal. WITNESS o(x) = first Odd vertex on x's (sigma, tau)-play with sigmabar(o) != tau(o)
(the plays of Xi and W from x agree up to o). Checks: (M) the gap level of v never rises in rank while v stays in Z with W(v) fixed
(lex-monotonicity), (I) inheritance: off-cycle x has level(x) = level(sigma x) (both plays avoid x).
Output one line per game; --verbose prints events."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lz" in sys.argv:
    sys.path.insert(0, HERE); from n5lz import step
import pg
from collections import Counter, defaultdict
args = [a for a in sys.argv[1:] if not a.startswith("--")]; VERB = "--verbose" in sys.argv
g = load(args[0]); n = g.n
start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; S.append(tuple(ns)); TAU.append(tuple(nt)); FB.append(fb)
T = len(S) - 1
EV = [E.evaluate(x) for x in S]; XI = [e[0] for e in EV]; SB = [e[1] for e in EV]; LX = [tuple(v[0] for v in x) for x in XI]
lam = [0] * (T + 1)
for k in range(1, T + 1): lam[k] = lam[k - 1] + (LX[k] != LX[k - 1])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def level(a, b):
    if a == b: return '='
    if a[0] != b[0]: return 'C'
    x = a[1] ^ b[1]
    if x: return x.bit_length() - 1
    return 'L'
def lv(l): return {'C': 10**6, 'L': -1, '=': -2}.get(l, l)   # numeric depth: higher = more significant difference
def witness(k, x):
    seen = set()
    while x not in seen:
        seen.add(x)
        if g.owner[x] == 0: x = S[k][x]
        else:
            if SB[k][x] != TAU[k][x]: return x
            x = TAU[k][x]
    return None
ev = [v for v in range(n) if g.owner[v] == 0]
events = []; viol_M = 0; viol_I = 0; checks_I = 0
for k in range(T):
    if TAU[k + 1] != TAU[k] or lam[k + 1] != lam[k]: continue
    tau = TAU[k]; w0, w1 = Wv(k, tau), Wv(k + 1, tau); Ek = Wc[tau]
    for v in ev:
        if S[k][v] == S[k + 1][v]: continue
        if XI[k][v] != w0[v] and E.key(XI[k + 1][v]) > E.key(XI[k][v]) and not Ek.key(w1[v]) > Ek.key(w0[v]):
            l0, l1 = level(XI[k][v], w0[v]), level(XI[k + 1][v], w1[v])
            if w0[v] == w1[v] and lv(l1) > lv(l0): viol_M += 1
            dP = XI[k][v][1] != XI[k + 1][v][1]
            top = (XI[k][v][1] ^ XI[k + 1][v][1]).bit_length() - 1 if dP else 'L'
            events.append(dict(k=k, run=lam[k], v=v, l0=l0, l1=l1, dP=dP, top=top, close=XI[k + 1][v] == w1[v],
                               fb=FB[k], o0=witness(k, v), o1=witness(k + 1, v), d=S[k][v], c=S[k + 1][v], W=w0[v], Wsame=w0[v] == w1[v]))
# inheritance check (I) on states that host events
for k in sorted({e['k'] for e in events}):
    w = Wv(k, TAU[k])
    for x in range(n):
        y = S[k][x] if g.owner[x] == 0 else None
        if y is None: continue
        if XI[k][x][0] == x or w[x][0] == x: continue
        checks_I += 1
        if level(XI[k][x], w[x]) != level(XI[k][y], w[y]): viol_I += 1
per_rv = Counter((e['run'], e['v']) for e in events)
per_rvW = Counter((e['run'], e['v'], e['W']) for e in events)
per_rvl = Counter((e['run'], e['v'], e['l0']) for e in events)
per_run = Counter(e['run'] for e in events)
per_ro1 = Counter((e['run'], e['o1']) for e in events)
per_rvo1 = Counter((e['run'], e['v'], e['o1']) for e in events)
mx = lambda c: max(c.values()) if c else 0
print(f"GXC {os.path.basename(args[0])} n {n} iters {T} fallbacks {sum(FB)} events {len(events)} run {mx(per_run)} per-v-run {mx(per_rv)} per-v-run-W {mx(per_rvW)} "
      f"per-v-run-level {mx(per_rvl)} per-run-witness {mx(per_ro1)} per-v-run-witness {mx(per_rvo1)} dP {sum(e['dP'] for e in events)} "
      f"close {sum(e['close'] for e in events)} Wsame {sum(e['Wsame'] for e in events)} levels {dict(Counter(str(e['l0']) for e in events).most_common(3))} "
      f"cat {dict(Counter((('fb' if e['fb'] else 's4a'), ('Wsame' if e['Wsame'] else 'Wfell'), ('close' if e['close'] else 'open')) for e in events))} "
      f"s4a-per-run {mx(Counter(e['run'] for e in events if not e['fb']))} fb-per-run {mx(Counter(e['run'] for e in events if e['fb']))} "
      f"s4a-per-v-run {mx(Counter((e['run'], e['v']) for e in events if not e['fb']))} "
      f"violM {viol_M} violI {viol_I}/{checks_I}")
if VERB:
    for e in events: print("  ", e)
# --- box 72 checks TIE and CLOSE (appended) ---
ph = [0] * (T + 1)
for k in range(1, T + 1): ph[k] = ph[k - 1] + (LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1])
tie_ok = tie_bad = tie_cyc = 0
for e in events:
    if e['fb']: continue
    k, v, d = e['k'], e['v'], e['d']; w1 = Wv(k + 1, TAU[k]); Ek = Wc[TAU[k]]
    if w1[v][0] == v or XI[k][v][0] == v or XI[k + 1][v][0] == v: tie_cyc += 1; continue
    if Ek.extend(v, w1[d]) == w1[v]: tie_ok += 1
    else: tie_bad += 1
Z = [None] * (T + 1)
def Zof(k): 
    if Z[k] is None: w = Wv(k, TAU[k]); Z[k] = frozenset(x for x in range(n) if XI[k][x] != w[x])
    return Z[k]
close_viol = 0; close_max_ratio = 0.0; phases = sorted(set(ph))
for p in phases:
    ks = [k for k in range(T + 1) if ph[k] == p]; a = ks[0]
    cl = sum(1 for e in events if ph[e['k']] == p and ph[e['k'] + 1] == p and e['v'] not in Zof(e['k'] + 1))
    if not cl: continue
    rises = 0; zent = 0
    for k in ks[:-1]:
        if FB[k]: 
            zent += len(Zof(k + 1) - Zof(k)); continue
        w0, w1 = Wv(k, TAU[k]), Wv(k + 1, TAU[k]); Ek = Wc[TAU[k]]
        rises += sum(1 for x in range(n) if Ek.key(w1[x]) > Ek.key(w0[x]))
    bound = len(Zof(a)) + rises
    if cl > bound or zent: close_viol += 1
    close_max_ratio = max(close_max_ratio, cl / max(1, bound))
fbo = Counter((ph[e['k']], e['v']) for e in events if e['fb'] and e['v'] in Zof(e['k'] + 1))
fbo_run = Counter(ph[e['k']] for e in events if e['fb'] and e['v'] in Zof(e['k'] + 1))
print(f"CHK {os.path.basename(args[0])} tie_ok {tie_ok} tie_bad {tie_bad} tie_cyc {tie_cyc} close_viol {close_viol} close_ratio {close_max_ratio:.3f} "
      f"fbopen {sum(fbo.values())} fbopen-per-phase {mx(fbo_run)} fbopen-per-v-phase {mx(fbo)} phases {len(phases)}")
