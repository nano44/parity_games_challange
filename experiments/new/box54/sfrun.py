#!/usr/bin/env python3
"""L-NEW box 54: N5-SF against N5 per game. Columns: n, N5 iterations (common.rows), N5 phases, N5-SF iterations, SF fallbacks, SF cycle,
SBC (SF transitions changing sigma-bar), LAM (SF transitions changing lambda_Xi), SEG (maximal stretches with sigma-bar and lambda_Xi constant),
SEGMAX (most Even-changing transitions in one SEG), and checks:
  WIN_V    SF's final winning regions (S5: Even wins v iff the cycle node of Xi_sigma(v) is even) differ from N5's;
  OPT_V    SF stops with Is != empty (impossible by S5) or the final sigma has an improving edge;
  R17_V    some SEG has > n - 1 Even-changing transitions (Lemma SEG-R17, docs/new/N5-SF-box54.md);
  FB_V     an S4c fallback fired in SF (Lemma NOFB says never);  CYC_V  SF revisited a state.
MODE=w runs N5-SFW instead (checks then mean: does the W-frame variant cycle / err). Usage: sfrun.py --list FILE | GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
import n5sf
from common import rows, phases, load, readstart
C = Counter(); TOP = []

def win(E, s):
    vs, _ = E.evaluate(tuple(s)); return tuple(E.par[x[0]] == 0 for x in vs)

def run(g, st, name):
    E0, R = rows(g, st, cap=20000); E, T = n5sf.trace(g, st)
    n = g.n; nph = len(list(phases(R)))
    cyc = T[-1].get("cycle", False); T2 = [x for x in T if "lam" in x]
    sbc = sum(1 for i in range(len(T2) - 1) if T2[i]["sb"] != T2[i + 1]["sb"])
    lam = sum(1 for i in range(len(T2) - 1) if T2[i]["lam"] != T2[i + 1]["lam"])
    seg = 1; cur = 0; segmax = 0
    for i in range(len(T2) - 1):
        if (T2[i]["sb"], T2[i]["lam"]) != (T2[i + 1]["sb"], T2[i + 1]["lam"]): seg += 1; segmax = max(segmax, cur); cur = 0
        if T2[i]["s"] != T2[i + 1]["s"]: cur += 1
    segmax = max(segmax, cur)
    fb = sum(x.get("fb", 0) for x in T2)
    if cyc: C["CYC_V"] += 1
    if fb: C["FB_V"] += 1
    if segmax > n - 1: C["R17_V"] += 1
    if not cyc:
        if win(E, T2[-1]["s"]) != win(E0, R[-1]["s"]): C["WIN_V"] += 1
        vs, _ = E.evaluate(tuple(T2[-1]["s"]))
        if E.improving(tuple(T2[-1]["s"]), vs): C["OPT_V"] += 1
    C["games"] += 1; C["n5_it"] += len(R) - 1; C["sf_it"] += len(T2) - 1
    row = (name, n, len(R) - 1, nph, len(T2) - 1, fb, cyc, sbc, lam, seg, segmax)
    TOP.append(row); print("ROW", *row)

def main():
    a = sys.argv[1:]
    if a[0] == "--list":
        for line in open(a[1]):
            p = line.split()
            if not p or p[0].startswith("#"): continue
            X = lambda q: os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q)
            try: run(load(X(p[0])), readstart(X(p[1])) if len(p) > 1 else None, p[0])
            except Exception as e: C["SKIPPED"] += 1; print("SKIP", p[0], repr(e)[:80])
    else: run(load(a[0]), readstart(a[1]) if len(a) > 1 else None, a[0])
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: game, n, N5 it, N5 phases, SF it, SF fb, SF cycle, SBC, LAM, SEG, SEGMAX")
    for k, lab in ((4, "SF it"), (7, "SBC"), (9, "SEG"), (10, "SEGMAX")):
        z = max(TOP, key=lambda z: (z[k] / z[1], z[0])); print("max %s/n = %.3f" % (lab, z[k] / z[1]), z)
    z = max(TOP, key=lambda z: (z[4] / max(1, z[2]), z[0])); print("max SF/N5 =", round(z[4] / max(1, z[2]), 3), z)
    for k in ("WIN", "OPT", "R17", "FB", "CYC"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
