#!/usr/bin/env python3
"""L-NEW box 52 (successor 32): the READER-PROOF cut of L-SI's Theorem W-SPLIT (docs/si/N5-FRZ-box29.md §2). Per phase P (lambda_Xi, tau
constant; common.phases) the transitions t -> t+1 are cut as in W-SPLIT at S4c fallbacks (FB) and at non-fallback lambda_W changes (LWCH),
but sigma-bar changes are cut ONLY when they are ARENA-RELEVANT: with a := the first state after the last cut (the reference),
  RLV cut at t -> t+1  iff  Is(t+1) != Ifr(t+1),   Is(t+1) = S2's improving set of sigma_{t+1} (from Xi, i.e. against sigma-bar_{t+1}),
                                                   Ifr(t+1) = S2's rule applied to val(sigma_{t+1}, sigma-bar_a) (sigma-bar FROZEN at a),
and after any cut the reference becomes t+1. So inside a refined frozen W-phase F every source state u has Is(u) = Ifr(u): F is a run of
"N5 with sigma-bar frozen at sigma-bar_a" (S4a depends on sigma, tau, Is only). An Odd vertex with no predecessors (a reader) never
changes Ifr, so its sigma-bar changes are never cut. Counts per phase: L, FB, LWCH, SBCH' (non-fb, lambda_W-keeping sigma-bar changes),
SBCH'' (RLV cuts), DEL (RLV cuts at transitions that do not change sigma-bar: the delayed effect of an earlier uncut change), NFW'' (refined
frozen W-phases), LFW'' (longest), WCH'' (most W-changing transitions in one of them), and the checks
  ARENA_V : at some state Is(t) != improving set of val(sigma_t, sigma-bar_t) by common.wplay (the frozen evaluator is wrong);
  SPLIT_V : L != FB + LWCH + SBCH'' + sum |F| (bookkeeping);  FWBF2_V : WCH'' > n - 1 (CONJECTURE FW-BF on the refined cut);
  FWLEN2_V: |F| >= n + m (CONJECTURE FW-LEN on the refined cut).
Usage: rlv.py --one GAME [START] | --list FILE (paths as in L-SI's lists; START=1 reads the second column)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load, readstart, phases, wplay
C = Counter(); TOP = []

def frozen_I(E, g, s, sb):
    val, _ = wplay(E, g, s, sb); return sorted(E.improving(tuple(s), val))

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); n = g.n; m = sum(len(set(x)) for x in g.succ)
    Is = [sorted(E.improving(tuple(A["s"]), A["vs"])) for A in R]
    for t, A in enumerate(R):
        if Is[t] != frozen_I(E, g, A["s"], A["sb"]): C["ARENA_V"] += 1
    for i, j in phases(R):
        fb = lw = sbp = rl = dl = 0; F = []; a = i; seg = i; wch = 0; wmax = 0
        def close(t):
            nonlocal seg, wch, wmax
            if t > seg: F.append(t - seg); wmax = max(wmax, wch)
            wch = 0
        for t in range(i, j):
            cut = None
            if R[t]["fb"]: fb += 1; cut = "fb"
            elif any(R[t]["W"][x][0] != R[t + 1]["W"][x][0] for x in range(n)): lw += 1; cut = "lw"
            else:
                sbc = R[t]["sb"] != R[t + 1]["sb"]
                if sbc: sbp += 1
                if Is[t + 1] != frozen_I(E, g, R[t + 1]["s"], R[a]["sb"]):
                    rl += 1; cut = "rl"
                    if not sbc: dl += 1
            if cut: close(t); seg = t + 1; a = t + 1
            elif R[t]["W"] != R[t + 1]["W"]: wch += 1
        close(j)
        L = j - i
        if fb + lw + rl + sum(F) != L: C["SPLIT_V"] += 1
        if wmax > n - 1: C["FWBF2_V"] += 1
        if F and max(F) >= n + m: C["FWLEN2_V"] += 1
        C["phases"] += 1; C["frozen2"] += len(F)
        TOP.append((L, name, i, j, fb, lw, sbp, rl, dl, len(F), max(F, default=0), wmax, n))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if not p: continue
            X = lambda q: os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q)
            try: run(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
            except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: L, game, i, j, FB, LWCH, SBCH', SBCH'', DEL, NFW'', LFW'', WCH'', n")
    for z in sorted(TOP, key=lambda z: -z[0])[:3]: print("TOP", z)
    for k, lab in ((6, "SBCH'"), (7, "SBCH''"), (8, "DEL"), (10, "LFW''"), (11, "WCH''")):
        z = max(TOP, key=lambda z: (z[k] / z[12], z[1])); print("max %s/n = %.3f" % (lab, z[k] / z[12]), z)
    for k in ("ARENA", "SPLIT", "FWBF2", "FWLEN2"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
