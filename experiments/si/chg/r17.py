#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §14): where R17's one-player phase bound breaks in two-player N5. Per PHASE (λ, τ constant):
  L       transitions;  ESW  Even switches;  WCH  W-value-changing transitions (W = valuation of the (σ, τ)-play, S4a's objective);
  SBCH    transitions at which σ̄ (Odd's optimal counterstrategy, the honest frame) changes at some vertex;
  BLOCK   pairs (t, x), x Even, for which some successor y gives x a strictly better W-value than S4a's choice at t + 1
          (x ⊕ W_(t+1)(y) ▷ W_(t+1)(x), y's play avoiding x) although (x, y) is not in x's arena at t: R17's Lemma P needs every
          W-better edge to be in the arena (one player: improving = W-better); here the arena is cut by Ξ (σ̄), not by W.
  STALL   pairs (t, x) with an honest-improving (x, z) ∈ Iσ_t not taken whose Ξ-value x ⊕ Ξ_t(z) beats Ξ_(t+1)(x): Case B of Lemma P
          fails there in the Ξ-reading (the arena optimum is taken against τ, not against σ̄).
D0_V: a phase with σ̄_t = τ at every Odd vertex and state (D = ∅) and more than n − 1 W-changing transitions or ≥ n + m transitions
(Corollary R17-D0 says never). Candidates: WCHD_V / ESWD_V (W-changing transitions / Even switches > n (|D| + 1), D = Odd vertices with σ̄ ≠ τ in the phase), ESWSB_V (ESW > n (SBCH + 1)), WCHSB_V (WCH > n (SBCH + 1)). Usage: r17.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from n5x import Engine
C = Counter(); EX = []; TOP = []

def _run(E, g, R, name):
    n = g.n; EN = Engine(g)
    for i, j in phases(R):
        L = j - i; esw = wch = sbch = blk = 0; first = None; Du = set(); stall = 0; sfirst = None
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            esw += sum(1 for v in range(n) if g.owner[v] == 0 and A["s"][v] != B["s"][v])
            wch += A["W"] != B["W"]; sbch += any(A["sb"][u] != B["sb"][u] for u in range(n) if g.owner[u] == 1)
            I = set(EN.improving(tuple(A["s"]), A["vs"]))
            Du |= {u for u in range(n) if g.owner[u] == 1 and A["sb"][u] != A["t"][u]}
            for (x, z) in I:                                   # K1-type stall: the honest switch x -> z beats S4a's choice in Ξ
                if B["s"][x] == z or A["vs"][z][0] == x: continue
                if E.key(E.extend(x, A["vs"][z])) > E.key(B["vs"][x]):
                    stall += 1
                    if sfirst is None: sfirst = (t, x, z, A["s"][x], B["s"][x])
            for x in range(n):
                if g.owner[x] != 0: continue
                for y in set(g.succ[x]):
                    if y == B["s"][x] or y == A["s"][x] or (x, y) in I: continue
                    wy = B["W"][y]
                    if wy[0] == x: continue                      # y's play passes x: the one-step comparison is not a prefix extension
                    if E.key(E.extend(x, wy)) > E.key(B["W"][x]):
                        blk += 1
                        if first is None: first = (t, x, y, A["s"][x], B["s"][x])
                        break
        C["phases"] += 1
        if esw > n * (sbch + 1): C["ESWSB_V"] += 1; EX.append(("ESWSB", name, i, j, esw, sbch, n))
        if wch > n * (sbch + 1): C["WCHSB_V"] += 1; EX.append(("WCHSB", name, i, j, wch, sbch, n))
        if wch > n * (len(Du) + 1): C["WCHD_V"] += 1; EX.append(("WCHD", name, i, j, wch, len(Du), n))
        if esw > n * (len(Du) + 1): C["ESWD_V"] += 1; EX.append(("ESWD", name, i, j, esw, len(Du), n))
        C["stall_pairs"] += stall
        Dfull = any(R[t]["sb"][u] != R[t]["t"][u] for t in range(i, j + 1) for u in range(n) if g.owner[u] == 1)
        if not Dfull:                                    # Corollary R17-D0: σ̄ = τ everywhere on the phase, so Ξ = W and R17 applies on G_τ
            C["phases_D0"] += 1; m = sum(len(set(g.succ[v])) for v in range(n))
            if wch > n - 1 or L >= n + m: C["D0_V"] += 1; EX.append(("D0", name, i, j, wch, L, n, m))
        TOP.append((L, name, i, j, esw, wch, sbch, blk, first, n, len(Du), stall, sfirst))

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

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
    print("columns: L, game, i, j, Even switches, W-changing transitions, σ̄-changing transitions, BLOCK pairs, first BLOCK (t, x, y, σ_t x, σ_(t+1) x), n, |D| (Odd u with σ̄ ≠ τ somewhere in the phase), STALL pairs, first STALL")
    for z in sorted(TOP, key=lambda z: -z[0])[:4]: print("TOP", z)
    if TOP:
        z = max(TOP, key=lambda z: (z[5] / ((z[10] + 1) * (z[9] - 1)), z[1])); print("RATIO max WCH / ((|D| + 1)(n - 1)) = %.3f" % (z[5] / ((z[10] + 1) * (z[9] - 1))), z[:11])
        z = max(TOP, key=lambda z: (z[5] / (z[9] - 1), z[1])); print("RATIO max WCH / (n - 1) = %.3f" % (z[5] / (z[9] - 1)), z[:11])
    if TOP: print("RATIO max ESW / (SBCH + 1) / n = %.3f" % max(z[4] / (z[6] + 1) / z[9] for z in TOP))
    for z in EX[:5]: print("EXAMPLE", z)
    for k in ("D0", "ESWSB", "WCHSB", "WCHD", "ESWD"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
