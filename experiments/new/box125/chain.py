#!/usr/bin/env python3
"""L-NEW box 125: how TWO-FIX windows chain inside a tau-stretch. A tau-stretch is a maximal run of transitions with tau_k = tau_(k+1); a
SIGMA-BAR CHANGE (SBC) is a stretch transition k -> k+1 with sbar_k != sbar_(k+1) (sbar := si.Engine's optimal Odd counterstrategy).
Per stretch: T := transitions, WIN := TWO-FIX windows (maximal sbar-constant runs, length >= 1), SBC := sbar-change transitions.
Per SBC, for every Odd v with sbar(v) moved: VAL if Xi(v) changed at that transition, else TIE (= FLAT in box 125's note: Xi(v)
unchanged; a true tie, or the old choice rose while another successor attains the old value); TOW if the new sbar(v) = tau(v) (v leaves ODIFF), AWAY if the old sbar(v) = tau(v) (v joins ODIFF), else SIDE; FBX := the SBC
transition is an S4c fallback; DSW := v's old (sigma_k, sbar_k)-play visits an Even vertex switched at k (box 121 PLAY-CONTAIN form, cycle included).
MOVERS := Odd vertices whose sbar moves at some SBC, MAXFLIP := the most SBC moves of one Odd vertex (whole run).
ODIFF across consecutive windows: list of (ODIFF) per window, longest stretch only (field OD).
Usage: chain.py G.pg [START|-]   prints one CHAIN line (all stretches summed, longest stretch detailed)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1
EV = [E.evaluate(x) for x in S]
SB = [tuple(-1 if own[v] == 0 else EV[k][1][v] for v in range(n)) for k in range(K + 1)]
Odd = [v for v in range(n) if own[v] == 1]
def meets(k, z, sw):
    f = lambda v: S[k][v] if own[v] == 0 else SB[k][v]
    x = z; seen = []
    while x not in seen:
        if x in sw: return True
        seen.append(x); x = f(x)
    return False
flips = {}
tot = dict(st=0, T=0, win=0, sbc=0, val=0, tie=0, tow=0, away=0, side=0, fbx=0, dsw=0, vmoves=0)
longest = None
k = 0
while k < K:
    if T[k + 1] != T[k]: k += 1; continue
    a = k
    while k < K and T[k + 1] == T[k]: k += 1
    b = k; tau = T[a]; tot["st"] += 1; tot["T"] += b - a
    sbc = [j for j in range(a, b) if SB[j] != SB[j + 1]]; tot["sbc"] += len(sbc); tot["win"] += len(sbc) + 1
    ods = [sum(1 for v in Odd if SB[a][v] != tau[v])] + [sum(1 for v in Odd if SB[j + 1][v] != tau[v]) for j in sbc]
    for j in sbc:
        tot["fbx"] += FB[j]; sw = {v for v in range(n) if own[v] == 0 and S[j][v] != S[j + 1][v]}
        mv = [v for v in Odd if SB[j][v] != SB[j + 1][v]]; tot["vmoves"] += len(mv)
        for v in mv:
            flips[v] = flips.get(v, 0) + 1
            if EV[j][0][v] != EV[j + 1][0][v]: tot["val"] += 1
            else: tot["tie"] += 1
            if SB[j + 1][v] == tau[v]: tot["tow"] += 1
            elif SB[j][v] == tau[v]: tot["away"] += 1
            else: tot["side"] += 1
            tot["dsw"] += meets(j, v, sw)
    if longest is None or b - a > longest[1] - longest[0]: longest = (a, b, len(sbc), ods)
a, b, ns, ods = longest if longest else (0, 0, 0, [])
odtxt = ods if len(ods) <= 40 else ods[:20] + ["..."] + ods[-10:]
print(f"CHAIN {os.path.basename(sys.argv[1])} n {n} K {K} stretches {tot['st']} T {tot['T']} WIN {tot['win']} SBC {tot['sbc']} FBX {tot['fbx']} "
      f"VMOVES {tot['vmoves']} VAL {tot['val']} TIE {tot['tie']} TOW {tot['tow']} AWAY {tot['away']} SIDE {tot['side']} DSW {tot['dsw']} "
      f"MOVERS {len(flips)} MAXFLIP {max(flips.values()) if flips else 0} | longest [{a}, {b}] L {b - a} SBC {ns} OD {odtxt}")
