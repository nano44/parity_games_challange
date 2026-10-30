#!/usr/bin/env python3
"""L-RED successor 32 (R131): second TIED-RB counter, on L-COMP's n5b SPEC trace and its PGSolver-port valuations (as span/latec.py),
written from L-SI box 50 §6's definitions, not from tied.py's code. W_t = val(sigma_t, tau_t) on G_tau; Xi_t = val(sigma_t, Odd best
response) (n5b's SG). W-run: tau constant, no fallback, W cycle-node map constant. BLOCKED, late, REPEAT, k, RE-BLOCKED, TIED as in box 50
§6 (tied: s in [k, u-1], Xi_(s+1)(z) > Xi_s(z) and W_(s+1)(z) = W_s(z)). Prints the counts and every untied re-blocked REPEAT by name.
Usage: tiedc.py GAME.pg START"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/n5-second", "experiments/hard-families", "experiments/harness"): sys.path.insert(0, os.path.join(R, p))
import n5b, pg
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
names = {}
for l in open(sys.argv[1]):
    if '"' in l: names[int(l.split()[0])] = l.split('"')[1]
N = n5b.N5(g, mode="spec"); tr = []; fb = []; N.run(s0, t0, trace=tr, fbtrace=fb)
fbs = {k for k, x in enumerate(fb) if x}; SG = N.SG; T = len(tr) - 1; WE = {}
def Wv(t):
    tau = tuple(tr[t][1])
    if tau not in WE: WE[tau] = n5b.SpecSI(pg.Game(g.prio, g.owner, [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]))
    return WE[tau], WE[tau].evaluate(list(tr[t][0]))
ev = [v for v in range(g.n) if g.owner[v] == 0]
X, W, WS, BL = [], [], [], []
for t in range(T + 1):
    sig = list(tr[t][0]); xv = SG.evaluate(sig); I = n5b.N5.improving(SG, sig, xv); si, wv = Wv(t)
    X.append(xv); W.append(wv); WS.append(si)
    BL.append({(v, c) for v in ev for c in g.succ[v] if c != sig[v] and si.nvo(wv[sig[v]], wv[c]) < 0 and c not in I.get(v, [])})
cut = [tuple(tr[t][1]) != tuple(tr[t + 1][1]) or tuple(W[t][v][0] for v in range(g.n)) != tuple(W[t + 1][v][0] for v in range(g.n))
       or t in fbs or tr[t][0] == tr[t + 1][0] for t in range(T)]
c = dict(rep=0, tied=0, untied=0, reblk=0, untied_reblk=0); bad = []
a = 0
while a <= T:
    b = a
    while b < T and not cut[b]: b += 1          # W-run = states a..b
    seen = set(); adopted = set(); leave = {}
    for t in range(a, b):
        seen |= BL[t]
        for y in ev:
            z0, z = tr[t][0][y], tr[t + 1][0][y]
            if z == z0: continue
            leave[(y, z0)] = t
            if (y, z) not in seen: continue
            if (y, z) in adopted:
                c['rep'] += 1; k = leave[(y, z)]
                tied = any(SG.nvo(X[s][z], X[s + 1][z]) < 0 and WS[s].nvo(W[s][z], W[s + 1][z]) == 0 for s in range(k, t))
                rb = any((y, z) in BL[s] for s in range(k + 1, t + 1))
                c['reblk'] += rb; c['tied'] += tied; c['untied'] += not tied; c['untied_reblk'] += rb and not tied
                if rb and not tied: bad.append(f"{names.get(y, y)}->{names.get(z, z)} k {k} u {t}")
            adopted.add((y, z))
    a = b + 1
print(f"TIEDC {os.path.basename(sys.argv[1])} n {g.n} iter {T} fallbacks {len(fbs)} runs {sum(cut) + 1} " + " ".join(f"{k} {v}" for k, v in c.items()))
for x in bad: print("  untied re-blocked REPEAT", x)
