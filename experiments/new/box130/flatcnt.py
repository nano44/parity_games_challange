#!/usr/bin/env python3
"""L-NEW box 130 FLATCNT: W-flat and weak Even moves per TWO-FIX window (TF-RED's F term), split by ODIFF.
Windows / stretches as box 128 pcount.py. A move of h at transition j (o -> w): STRICT / FLAT / WEAK by key(W_j(w)) vs key(W_j(o));
CORNER if o's or w's W_j-play runs through h. A transition is FL if sigma changes and W_j = W_(j-1) everywhere.
Checked (lane lemmas, box 130 note):
  FL-ONLYFLAT : every non-corner move of an FL transition is FLAT, and a transition whose moves are all FLAT non-corner is FL
                (W-changes need a W-strict origin);
  FL-OPT      : at an FL transition j, sigma_(j-1) is itself W-optimal in the arena H_(j-1) (W_(j-1)(sigma_(j-1)(v)) is max over A(v));
  FL-TIGHT    : inside a maximal run of consecutive FL transitions, every mover's chosen options keep one W-value (T_v);
  FL0_NONCORNER: FL transitions in ODIFF-0 windows with a non-corner mover (Lemma FL-ODIFF0 predicts 0);
  ODIFF0FLAT  : non-corner FLAT moves in ODIFF-0 windows (predicted 0: Xi = W there);
  XI-RISE     : at every move Xi(h) rises strictly (standard SI); XIRISE_CYC := failures where h lies on its own Xi-play cycle at
                j-1 or j (h is then a cycle vertex, the comparison corner); FLTIGHT_CYC the same for FL-TIGHT with W.
Reported: FLAT / WEAK / CORNER moves, FL transitions, MAXFLRUN (longest run of consecutive FL transitions), MAXFLWIN (most flat moves in
one window), and the ratio MAXFLWIN / n.
Usage: flatcnt.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows

def play(succ1, x):
    s = set(); v = x
    while v not in s: s.add(v); v = succ1[v]
    return s

g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
n, own, pr = g.n, g.owner, g.prio
def blank(): return dict(win=0, moves=0, strict=0, flat=0, weak=0, corner=0, flattrans=0, fl=0, onlyflat_viol=0, flopt_viol=0,
                         fltight_viol=0, xirise_viol=0, maxflrun=0, maxflwin=0, flatfirst=0)
TOT = {0: blank(), 1: blank()}
for a, b in W:
    if b - a < 1: continue
    tau, sb = T[a], SB[a]; od = sum(own[v] == 1 and sb[v] != tau[v] for v in range(n)); R = TOT[min(od, 1)]; R["win"] += 1
    EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    EX = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)]))
    WV = {j: EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    XV = {j: EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    def s1(j): return [S[j][v] if own[v] == 0 else tau[v] for v in range(n)]
    flwin = 0; run_ = 0; tightval = {}; seen_prev = set()
    for j in range(a + 1, b + 1):
        if F[j]: run_ = 0; tightval = {}; seen_prev = set(); continue
        mv = [v for v in range(n) if own[v] == 0 and S[j][v] != S[j - 1][v]]
        if not mv: continue
        kinds = []
        for h in mv:
            o, w = S[j - 1][h], S[j][h]; R["moves"] += 1
            ko, kw = EW.key(WV[j][o]), EW.key(WV[j][w]); sj = s1(j)
            cor = h in play(sj, o) or h in play(sj, w); R["corner"] += cor
            k = "strict" if kw > ko else ("flat" if kw == ko else "weak"); R[k] += 1; kinds.append((k, cor))
            if k == "flat":
                flwin += 1; R["flatfirst"] += h not in seen_prev
                if od == 0 and not cor: R["odiff0flat"] = R.get("odiff0flat", 0) + 1
            if EX.key(XV[j][h]) <= EX.key(XV[j - 1][h]):
                xc = h in play([S[j][v] if own[v] == 0 else sb[v] for v in range(n)], h) or h in play([S[j - 1][v] if own[v] == 0 else sb[v] for v in range(n)], h)
                R["xirise_viol" if not xc else "xirise_cyc"] = R.get("xirise_viol" if not xc else "xirise_cyc", 0) + 1
            seen_prev.add(h)
        fl = WV[j] == WV[j - 1]
        allflat = all(k == "flat" and not c for k, c in kinds)
        if fl:
            R["fl"] += 1
            if od == 0 and any(not c for k, c in kinds): R["fl0_noncorner"] = R.get("fl0_noncorner", 0) + 1
            if any(k != "flat" and not c for k, c in kinds): R["onlyflat_viol"] += 1
            # FL-OPT: sigma_(j-1) optimal in the arena of transition j: no arena option with a W_(j-1)-better value
            Is = {v: [w for w in g.succ[v] if EX.key(XV[j - 1][w]) > EX.key(XV[j - 1][S[j - 1][v]])] for v in range(n) if own[v] == 0}
            sj1 = s1(j - 1)
            for v in Is:
                if v in play(sj1, S[j - 1][v]): continue
                if any(EW.key(WV[j - 1][w]) > EW.key(WV[j - 1][S[j - 1][v]]) for w in Is[v] if v not in play(sj1, w)):
                    R["flopt_viol"] += 1; break
            for h in mv:
                val = WV[j][S[j][h]]
                if h in tightval and tightval[h] != val:
                    R["fltight_viol" if not (h in play(s1(j), S[j][h])) else "fltight_cyc"] = R.get("fltight_viol" if not (h in play(s1(j), S[j][h])) else "fltight_cyc", 0) + 1
                tightval[h] = val
            run_ += 1; R["maxflrun"] = max(R["maxflrun"], run_)
        else:
            run_ = 0; tightval = {}
            if allflat: R["onlyflat_viol"] += 1
    R["maxflwin"] = max(R["maxflwin"], flwin)
for od in (0, 1):
    R = TOT[od]
    for k_ in ("odiff0flat", "xirise_cyc", "fltight_cyc", "fl0_noncorner"): R.setdefault(k_, 0)
    print(f"FLATCNT {os.path.basename(sys.argv[1])} n {n} ODIFF{'0' if od == 0 else '1+'} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
