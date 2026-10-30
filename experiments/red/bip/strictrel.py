#!/usr/bin/env python3
"""L-RED R142b: STRICT releases per Even edge per frozen-sigma-bar stretch (L-NEW box 89 CONJECTURE BIP-REL-1), on n5b SPEC.
Frozen stretch: maximal run of states with tau, the W cycle-node map and sigma-bar (Odd part) all constant, no fallback.
(y, z) BLOCKED at state q: W_q(z) better than W_q(sigma_q y) and (y, z) not in I_sigma_q. STRICT release at q' -> q'+1: sigma_(q'+1)(y) = z !=
sigma_q'(y), with a block of (y, z) at some state of the SAME stretch before q'. Prints the stretch count and the max strict releases of
one edge in one stretch (BIP-REL-1 says <= 1), with that edge's names. Usage: strictrel.py GAME.pg START"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
names = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): names[int(a[0])] = a[4].strip('"')
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb); n = g.n; Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    return Wc[t].evaluate(list(s))
info = []
for s, t in tr:
    w = W(s, t); xv = N.ev(N.SG, list(s)); I = N.improving(N.SG, s, xv); sb = N.opt(N.SG, list(s))[1]
    blk = {(v, z) for v in range(n) if g.owner[v] == 0 for z in g.succ[v]
           if z != s[v] and Wc[t].nvo(w[s[v]], w[z]) < 0 and z not in I.get(v, [])}
    info.append((tuple(sb[v] for v in range(n) if g.owner[v] == 1), tuple(x[0] for x in w), blk))
stretches = 0; best = (0, None); cnt = {}; seenblk = set()
for i in range(len(tr)):
    if i == 0 or tr[i][1] != tr[i - 1][1] or fb[i - 1] or info[i][0] != info[i - 1][0] or info[i][1] != info[i - 1][1]:
        stretches += 1; cnt = {}; seenblk = set()
    elif True:
        s, s1 = tr[i - 1][0], tr[i][0]
        for v in range(n):
            if g.owner[v] == 0 and s1[v] != s[v] and (v, s1[v]) in seenblk:
                cnt[v, s1[v]] = cnt.get((v, s1[v]), 0) + 1
                if cnt[v, s1[v]] > best[0]: best = (cnt[v, s1[v]], (names.get(v, v), names.get(s1[v], s1[v])))
    seenblk |= info[i][2]
print(f"STRICTREL {os.path.basename(sys.argv[1])} n {n} iterations {len(tr) - 1} frozen-stretches {stretches} max-strict-releases-one-edge-one-stretch {best[0]} at {best[1]}")
