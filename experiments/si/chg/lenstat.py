#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §6): segment LENGTH statistics per maximal REL segment [a, b]: b - a, |E_b|, switching Even
vertices (SW), final steps (FIN), deadlock steps (DL), growth steps (GR), total Even switches (TOT), max switches of one vertex (MAXV),
and the ratio (b - a) / |E_b|. Candidate bounds checked: LEN2 b - a <= 2 SW + 1 (from DL-SEP), LENE b - a <= |E_b| (= n - 1 type),
LENG b - a <= FIN + GR + 1 (DL-SEP form), FRZLEN: a frozen run (maximal run of non-growth steps) longer than the number of
Even vertices switching in it (candidate FROZEN-COUNT). Usage: lenstat.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from suffix import segdata, rows, load, readstart
import seglast
C = Counter(); EX = []; BEST = []

def _run(g, R, name):
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        Ev, T, JW, JH, fW, fH, L = segdata(g, R, a, b)
        F = Counter(L.values()); fin = len(F); dl = (b - a) - fin
        gr = sum(1 for t in range(a, b) if any(fW[v] == t + 1 or fH[v] == t + 1 for v in Ev))
        sws = Counter(v for t in range(a, b) for v in range(g.n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v])
        sw = len(L); tot = sum(sws.values()); mx = max(sws.values())
        C["segs"] += 1; C["dl_total"] += dl
        G = {t for t in range(a, b) if any(fW[v] == t + 1 or fH[v] == t + 1 for v in Ev)}; t = a
        while t < b:                                   # frozen runs: maximal runs of non-growth steps (sinks constant, FREEZE)
            if t in G: t += 1; continue
            u = t
            while u < b and u not in G: u += 1
            fz = Counter(v for x in range(t, u) for v in range(g.n) if g.owner[v] == 0 and R[x]["s"][v] != R[x + 1]["s"][v])
            C["frozen_len_%d" % min(u - t, 9)] += 1; C["frozen_maxsw_%d" % max(fz.values())] += 1
            if u - t > len(fz): C["FRZLEN_V"] += 1; EX.append(("FRZLEN", name, a, b, t, u, len(fz)))
            t = u
        if b - a > 2 * sw + 1: C["LEN2_V"] += 1; EX.append(("LEN2", name, a, b, sw))
        if b - a > len(Ev): C["LENE_V"] += 1; EX.append(("LENE", name, a, b, len(Ev)))
        if b - a > fin + gr + 1: C["LENG_V"] += 1; EX.append(("LENG", name, a, b, fin, gr))
        BEST.append(((b - a) / max(1, len(Ev)), name, a, b, len(Ev), sw, fin, dl, gr, tot, mx, g.n))

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: ratio (b-a)/|E_b|, game, a, b, |E_b|, SW, FIN, DL, GR, TOT, MAXV, n")
    for z in sorted(BEST, reverse=True)[:8]: print("TOP", tuple(round(x, 3) if isinstance(x, float) else x for x in z))
    for z in EX[:6]: print("EXAMPLE", z)
    for k in ("LEN2", "LENE", "LENG", "FRZLEN"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()

def lscore(g, R):
    """(max over segments of (b - a) - |E_b|, max of (b - a) - SW, total deadlocks) for chg/cclimb.py OBJ=LE."""
    global C, EX, BEST
    save = (C, EX, BEST); C, EX, BEST = Counter(), [], []
    try:
        _run(g, R, "x")
        if not BEST: return -10 ** 6, -10 ** 6, 0
        return max(z[3] - z[2] - z[4] for z in BEST), max(z[3] - z[2] - z[5] for z in BEST), C["dl_total"]
    finally: C, EX, BEST = save
