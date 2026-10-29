# L-LIT T40 (docs/lit/T40-frame-split.md §3). Reads L-SI's helpers read-only (experiments/si/root/common.py -> experiments/new/box21/n5x.py, si.py).
# Usage (repo root): python3 -I docs/lit/T40-dominance-check.py GAME.pg [START]
# For every in-phase transition t -> t+1 of the N5 run (phase = λ_Ξ and τ constant, R38 (a)), compare S4a's σ_{t+1} with Howard's step
# σ^H_t (switch-all on Iσ_t, each switching vertex to its best Ξ_t-valued improving successor, PGSolver tie-break, as S4c):
#   A-dom: Ξ(σ_{t+1})(v) ⊵ Ξ(σ^H_t)(v) at every v   (dominance in the IMPROVING frame Ξ, against Odd's best reply; Scherrer/HMZ-type proofs need it)
#   B-dom: W(σ_{t+1})(v) ⊵ W(σ^H_t)(v) at every v   (dominance in the SELECTION frame W, against τ; holds by S4a's optimality in the arena)
#   D-empty: σ̄_t = τ at every Odd vertex (then Ξ = W, Corollary R17-D0's case; A-dom must hold). W-mono: W(σ_{t+1}) ⊵ W(σ_t) at every v.
#   Fallback transitions (S4c, the flag fb of n5x.step via rows) are counted apart: S4c is a switch-all step in Ξ, not S4a's W-optimum.
# Prints transitions checked, transitions / (t, v) pairs violating each, and the first A-dom violation.
import os, sys
ROOT = os.getcwd(); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, wplay, load, readstart
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, R = rows(g, st, cap=20000); n = g.n
tr = a_tr = a_pairs = b_tr = b_pairs = d0_tr = d0_a = wmono = fbt = wmono_nf = d0_a_nf = 0; first = None
for i, j in phases(R):
    for t in range(i, j):
        A, B = R[t], R[t + 1]; tr += 1
        d0 = all(A["sb"][u] == A["t"][u] for u in range(n) if g.owner[u] == 1); d0_tr += d0
        fb = bool(A["fb"]); fbt += fb; wm = any(E.key(B["W"][v]) < E.key(A["W"][v]) for v in range(n)); wmono += wm; wmono_nf += wm and not fb
        imp = E.improving(tuple(A["s"]), A["vs"]); sH = list(A["s"])
        for v in {v for v, _ in imp}:
            sH[v] = E.best_succ(v, A["vs"], [w for u, w in imp if u == v])
        vH = E.evaluate(tuple(sH))[0]; WH = wplay(E, g, sH, A["t"])[0]
        bad = [v for v in range(n) if E.key(B["vs"][v]) < E.key(vH[v])]
        if bad:
            a_tr += 1; d0_a += d0; d0_a_nf += d0 and not fb; a_pairs += len(bad)
            if first is None: first = (t, bad[0], A["s"][bad[0]], B["s"][bad[0]], sH[bad[0]])
        badW = [v for v in range(n) if E.key(B["W"][v]) < E.key(WH[v])]
        if badW: b_tr += 1; b_pairs += len(badW)
print(f"{os.path.basename(sys.argv[1])}: n={n} states={len(R)} in-phase transitions={tr} | A-dom (Xi) violated at {a_tr} transitions, {a_pairs} (t,v) pairs"
      f" | D-empty transitions={d0_tr}, of them A-dom-violating={d0_a} ({d0_a_nf} non-fallback) | W-monotonicity violated at {wmono} transitions ({wmono_nf} non-fallback); fallback transitions={fbt}"
      f" | B-dom (W) violated at {b_tr} transitions, {b_pairs} pairs | first A-dom violation (t, v, sigma_t v, sigma_t+1 v, sigmaH v): {first}")
