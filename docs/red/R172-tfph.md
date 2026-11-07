# R172 CONJECTURE TF-PH is DEAD: rwq_K8_m32 (n 217, ODIFF 33) has ONE λ_W-phase ∩ fallback-free run inside one TWO-FIX window with 278 > n − 1 = 216 W-changing transitions; the family gives 4K² + 3K − 2 at n = 26K + 9 (L-RED successor 40)
Started 2026-11-01 05:32Z (Lead GO, last box, date -u), written ~06:0xZ. Lead brief (R172): a counterexample to L-NEW box 122's
CONJECTURE TF-PH with D ≠ ∅; «a kill is an explicit-bound DEAD (L43-compliant)». Labels: DEAD (killed at a named, checked instance),
DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN: the family is quadratic, i.e. polynomial.

## 0. Answer
- The statement killed, verbatim from docs/new/N5-TWOFIX-box122.md §3 (claude/l-new 381e7a61): «for every N5 run on every game, every TWO-FIX
  window, every fallback-free run R of it and every λ_W-phase Φ: R ∩ Φ has at most n − 1 transitions at which W changes.»
- DEAD at r172/instances/rwq_K8_m32 (mkrw.py 8 32), from its written start:
  - n = 217. One TWO-FIX window [0, 279], ODIFF 33, 0 fallbacks, λ_W changes at 1 transition (LAMNF 1).
  - PHNF = 278 > n − 1 = 216. Measured with L-NEW's own experiments/new/box122/windows.py (claude/l-new 381e7a61), not with an L-RED tool.
  - D ≠ ∅: |D_j| ∈ [174, 176] on all 280 window states (dcheck.py).
- The bound n − 1 is EXPLICIT, and the family exceeds every linear bound. A quadratic bound is NOT refuted:

| K | m = 4K | n | window L | ODIFF | FB | LAMNF | PHNF | n − 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 12 | 87 | 44 | 13 | 0 | 1 | 43 | 86 |
| 4 | 16 | 113 | 75 | 17 | 0 | 1 | 74 | 112 |
| 6 | 24 | 165 | 161 | 25 | 0 | 1 | 160 | 164 |
| 8 | 32 | 217 | 279 | 33 | 0 | 1 | **278** | 216 |
| 10 | 40 | 269 | 429 | 41 | 0 | 1 | **428** | 268 |

  - PHNF = L − 1 = K(m + 3) − 2 and n = 14K + 3m + 9 (runquad's 12K + 3m + 6 plus Ω, O^hi and the 2K + 1 loop markers; = 26K + 9 at m = 4K). The first PHNF > n − 1 is at K = 7.
- Pin checks for rwq_K8_m32 (sha1 9a5f5f855d22…, start 9605f8731634…):

| check | result |
| --- | --- |
| startck | OK |
| Oink 8fbf0a7 --zlk + verify of N5's strategies (rel2/oinkcmp.sh) | «OINK OK» |
| Oink --tl -v | «solution verified (165 strategies)» |
| xeng (L-NEW n5.py driver vs n5b SPEC) | «state sequences identical: True» |
| FREEZE (R170) | REPLAY True, FRUN 280 |

## 1. The construction (mkrw.py: a post-processor of R106's seg/mkr.py)
- R106's runquad is already one fallback-free TWO-FIX window of K(m + 3) − 1 transitions (R170 §3). It escapes TF-PH only because
  λ_W changes at every reactor step: each reactor's W-play ends in the current pivot's Odd W-loop (T_i or T′_i), so a reactor move
  changes its cycle node. Box 122 recorded the same thing as s3quad's «PHNF 0».
- mkrw keeps every W-comparison of runquad but moves it from cycle nodes into the top of the path set:
  - every Odd W-loop X (C1, Cp0, T_i, Tp_i; τ(X) = X) gets X → X^hi → Ω. X^hi is a new one-edge Odd vertex with an ODD priority above all
    old priorities, in the loops' order. Ω is one new Odd self-loop of priority 1, and τ(X) := X^hi;
  - the W-sinks' old route O → M → z becomes O → {EQ, O^hi}, with O^hi → Ω the highest marker and τ(O) = O^hi (GATE=1).
- Why the dynamics are unchanged (READING, from R106 §2; checked by the run itself, 280 states, same K as mkr 8 32):
  - In G_σ̄, Odd's honest escapes still lead to the z cycle, the higher odd cycle node, which Odd prefers to Ω whatever the marker. So σ̄
    is runquad's σ̄. The new O-edge's honest branch is O → EQ → pe → M → z, which is runquad's old O-route plus EQ and pe.
  - In G_τ every play ends in Ω. The loops' old order (lower odd loop = better for Even) is the order of the X^hi markers. These sit
    above every other priority, so they decide W-comparisons as the cycle nodes did.
  - τ-stability (I_τ = ∅) uses R106's device unchanged: every honest Odd escape, and now also O's, leads to EQ or EQp, whose other edge
    goes to h′. From there Even's dual best reply reaches the lowest marker route.
- Result: λ_W ≡ Ω on the whole window after transition 0 (h's start option z). Every transition changes W, because every pivot step,
  reactor wave step and reactor flip is a W-change. So one λ_W-phase ∩ fallback-free run holds the whole climb.

## 2. What this means for box 122's reduction (READING)
- TWO-FIX-POLY ⇐ (TF-PH + F poly + FB poly) loses its first premise as stated. The quantity P (most W-changing transitions in one phase
  of one fallback-free run) is not ≤ n − 1. It reaches K(m + 3) − 2 ≈ n²/170 here.
- R17 (b) Lemma P's path-progress invariant (one more settled hop per step) is what fails. L-NEW box 124 saw the same on b5_os_n24 (blocked
  one-edge paths through D). Here the reactor chain is re-traversed once per pivot level inside one phase, so P ≈ (levels) × (chain).
- Still consistent: R170's TWO-FIX-NL (≤ 2n(ODIFF + 1)): 279 ≤ 2·217·34. A polynomial P-bound (e.g. P ≤ n(ODIFF + 1), or P ≤ n²) is
  not refuted. ODIFF is Θ(n) here, as in runquad; a small-ODIFF version is OPEN (R170 §4's obstruction applies unchanged).
- Climbs (climb172.py, PHNF scored exactly as windows.py, ODIFF ≥ 1 / ≥ 2 forced, 8,000 mutations, n 12-32, stopped before the push):
  PHNF ≤ 21 (n 32, seeded from R170's d_n32_k2_s1). Random search does not find the re-traversal pattern. The kill is by design.

## 3. Tools and pins (experiments/red/r172/)
- mkrw.py K m OUT.pg OUT.start (env GATE, default 1); lamtrace.py (per-transition λ_W changes, named); dcheck.py (|D_j| over the window);
  climb172.py + runclimb.sh (out/ph_*.txt).
- instances/rwq_K3_m12 (check.sh gate: PHNF 43, LAMNF 1) and instances/rwq_K8_m32 (the kill); pins.sha1.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r172/*; check.sh block R172; notebook PARK section. SHAs in the push / message.
- FINDINGS:
  - TF-PH DEAD (explicit bound n − 1) at rwq_K8_m32: PHNF 278 > 216, ODIFF 33, FB 0, |D| ≥ 174. Checked with L-NEW's windows.py,
    Oink zlk + tl, xeng and startck.
  - Family: PHNF = 4K² + 3K − 2 at n = 26K + 9.
  - Mechanism: runquad with its W-loops turned into top path markers over one common Ω. λ_W is then constant and the reactor chain is
    re-traversed once per level inside one phase.
- NEEDS: Lead: route to L-NEW (box 122's P needs a polynomial, not a linear, bound) and to the referees if TF-PH was cited anywhere.
  L-RED parks after this push.
