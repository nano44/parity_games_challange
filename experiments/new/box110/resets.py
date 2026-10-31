#!/usr/bin/env python3
"""L-NEW box 110: RESETS. Unary-length CS (box 109 climb4.py encoding: rank bits + thresholds [sl >= j], j = -n..n; the cycle coordinate
is constant on a W-run). Per W-run F: WCH = sum_v W-changes of v; GOOD = bit flips toward the Even-better value (0->1 for a +1 bit,
etc.), BAD = flips away (resets; TD_F = BAD); WCT = W-changing transitions; RT = transitions with at least one reset; ROOTRES =
transitions at which some SWITCHED Even vertex y (sigma changes at y) has a reset in W(y). Checks Lemma RESET-RED:
WCT <= n(3n+1) + TD (VIOL) and per vertex/bit: good flips <= 1 + bad flips (VB). Usage: resets.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc, Wm = {}, {}
def Wraw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def bits(x):
    c, m, l = x; sl = l if E.par[c] == 1 else -l
    # each coordinate normalised so that 1 = better for Even
    rb = tuple((1 if (m >> r) & 1 else 0) if E.rankpar[r] == 0 else (0 if (m >> r) & 1 else 1) for r in range(n - 1, -1, -1))
    return rb + tuple(int(sl >= j) for j in range(-n, n + 1))
def W(k, tau):
    if (k, tau) not in Wm: Wm[(k, tau)] = [bits(x) for x in Wraw(k, tau)]
    return Wm[(k, tau)]
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wraw(k, TAU[k])] != [x[0] for x in Wraw(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
tot = dict(WT=0, WCT=0, WCH=0, GOOD=0, TD=0, RT=0, ROOTRES=0, VIOL=0, VB=0); MAXTD = MAXWCT = 0
for run in runs:
    tau = TAU[run[0]]; td = wct = 0; gb = {}
    for k in run:
        A, B = W(k, tau), W(k + 1, tau); tot["WT"] += 1
        if A == B: continue
        wct += 1; anyres = False; rootres = False
        for v in range(n):
            if A[v] == B[v]: continue
            tot["WCH"] += 1
            for i, (a, b) in enumerate(zip(A[v], B[v])):
                if a < b: tot["GOOD"] += 1; gb[(v, i)] = gb.get((v, i), [0, 0]); gb[(v, i)][0] += 1
                elif a > b:
                    td += 1; anyres = True; gb[(v, i)] = gb.get((v, i), [0, 0]); gb[(v, i)][1] += 1
                    if own[v] == 0 and S[k][v] != S[k + 1][v]: rootres = True
        tot["RT"] += anyres; tot["ROOTRES"] += rootres
    tot["WCT"] += wct; tot["TD"] += td; MAXTD = max(MAXTD, td); MAXWCT = max(MAXWCT, wct)
    tot["VIOL"] += wct > n * (3 * n + 1) + td
    tot["VB"] += sum(1 for (gd, bd) in gb.values() if gd > 1 + bd)
print(f"RESETS {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in tot.items()) + f" MAXTD/run {MAXTD} MAXWCT/run {MAXWCT}")
