# N5-HN (box 95): why Friedmann's H_n (switchbestexp) dies in N5. DATA: N5's Even sequence EQUALS I^glo's for the first 13 iterations (N = 3..8), N5 changes τ for the first time at 12 → 13 (h2 → m2), and the sequences split at 13 → 14, where N5 also sends e1, e2 to d. I^glo doubles (134, 286, 590, 1198); the arena optimum against the frozen best response σ̄_t (V1 = N5-SF's Even step) is not exponential (135 … 489 at N = 3..8) but splits from I^glo only at iteration 71; N5 is linear (41 … 77). So the first killer is the τ frame (S4a against τ_t, τ moved by Odd's own step), not ARENA-MAX and not σ̄-freezing. No lemma; the mechanism is OPEN
L-NEW successor 39 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 18:43Z: «BOX 95: "why Friedmann's H_n dies in N5". L-LIT T59
(l-lit c7dc03db, docs/lit/T59-elimination-windows.md) found that H_n's rule I^glo is an arena optimum by definition, so ARENA-MAX alone does
not kill it. What else in N5 (the τ frame, σ̄ optimality) does is OPEN, and is likely the lemma ELIM-WIN needs.» Written 2026-10-30
18:53Z-18:56Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources and tools
- L-LIT T59 §3.2 (read in full): «Friedmann H_n ([F11] §8, Thm 8.4; PGSolver switchbestexp). Rule and count: I^glo (Schewe's globally
  optimal). I^glo is an arena optimum by definition ([F11] p.7)»; mechanism «stubborn cycles. Three Even nodes; two leave to the lane and
  one enters per iteration … The closure is never inside the arena»; «READING: (i) S4a is against τ_t, while I^glo lets Odd best-respond …
  (ii) N5's own τ-steps. Not separated here (OPEN)». I did not open [F11] myself; the I^glo definition used below is T59's quote
  («Ξσ′ ⊑ Ξσ* for every σ′ in A_{G,σ}»).
- L-RED R140 hybrid.py (V0 / V1 / V2 on L-SI's engine), reused in experiments/new/box95/hn.py with one new mode GLO; games from
  experiments/hard-families/pgsolver_port.py switchbestexp N (L-COMP's byte-identical PGSolver port); best-reward start.
- box95/hn.py modes, all with the SAME arena A_t(v) = {σ_t(v)} ∪ Iσ_t(v) (SPEC S2):
  - GLO = I^glo: an optimal Even strategy of the two-player game restricted to A_t (Odd unrestricted), computed by switch-all VJ iterations
    inside A_t from σ_t (ties to the larger index). Values judged by Ξ, Odd re-responding.
  - V1: Even's pointwise optimum of A_t against Odd frozen at σ̄_t. This is N5-SF's Even step (RESULTS R87; box 57's F(σ), Lemma STALE).
  - V2: against τ_0 forever (one never-ending W-run). SA: switch-all.
- box95/firstdiv.py: first state at which N5's Even strategy (experiments/new/box21/n5x.py, the reference engine of boxes 84-94) differs
  from the GLO and V1 runs; N5's τ-changes.

## 1. DATA: counts (iterations until Iσ = ∅)
| N | n | SA | GLO (I^glo) | V1 (vs σ̄_t) | V2 (vs τ_0) | N5 |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 85 | 141 | 134 | 135 | stalls at 59 | 41 |
| 4 | 110 | 301 | 286 | 258 | stalls at 65 | 47 |
| 5 | 135 | 621 | 590 | 364 | stalls at 71 | 55 |
| 6 | 160 | – | 1198 | 412 | – | 62 |
| 7 | 185 | – | – | 456 | – | 68 |
| 8 | 210 | – | – | 489 | – | 77 |
- GLO doubles (134 → 286 → 590 → 1198): our I^glo reproduces H_n's exponential behaviour (PGSolver's count at N = 4 is 289, T59; the
  small difference is the tie-break inside the restricted solve). So the arena (S2's offers) plus an arena-optimal choice really is
  exponential here, confirming T59: ARENA-MAX does not kill H_n.
- V1's increments shrink (123, 106, 48, 44, 33): not exponential on N ≤ 8. Its counts are super-linear in n so far (2.3n at N = 8).
- N5 counts equal box 59's freeze_all.txt (41, 47, 55 at N = 3, 4, 5).

## 2. DATA: where N5 leaves I^glo (box95/firstdiv.py, N = 3..8, identical for every N)
- N5's Even strategies equal GLO's AND V1's at states 0..13. N5's first τ-change is at transition 12 → 13. The first differing Even
  strategy is at state 14 (transition 13 → 14). N5 changes τ exactly N times in the run (T59: 2 W-runs on N = 4, 6, 8; the τ-changes split
  the run into τ-stretches).
- Trace, N = 3 (names from PGSolver's labels):
  - 12 → 13: both runs switch x→y, w→y, f1→g1, g′1→a12, f2→g2, e′2→a17, f′2→a13, g′2→a18. N5's Odd step: h2 → m2.
  - 13 → 14: both switch t→x, b0..b1→d, b2..b18→x and the primed lane exits e′i, f′i, g′i → d. N5 ALSO switches e1→d and e2→d (and its
    Odd step moves h1 → m1). At state 13, σ̄_13 differs from τ_13 at h0 (σ̄: m0, τ: e0) and h2 (σ̄: e2, τ: m2).
  - 14 → 15 and 15 → 16: GLO moves the stubborn triples in lock-step (e′1→e′0, g′1→g′0, e′2→e′1, g′2→g′1); N5 has already moved e1, e2
    and does not. From here the two runs separate.
- V1 (frozen best response) leaves GLO much later: first difference at iteration 71 on N = 3 (box95/hn.py trace: GLO switches v0 → v1, V1
  does not).

## 3. READING: what kills H_n in N5 (mechanism, not a proof)
- H_n's stubborn cycles keep the closing edge out of the arena and rely on the arena optimum making no progress towards the closure,
  because Odd re-responds (I^glo values by Ξ). That is exactly what V1 and GLO share for the first 70 iterations at N = 3.
- N5 values the arena against τ_t, a strategy that is NOT Odd's best response (σ̄_13 ≠ τ_13 at h0, h2) and that moves by Odd's OWN
  improvement step (S4b), not to σ̄. At 12 → 13 Odd's own step moves h2 to m2 (in Odd's interest on G^d, against σ_12). Against this τ, the
  W-optimum of the same arena commits e1, e2 → d at 13 → 14: the lane exits the I^glo counter needs to keep in lock-step are taken early,
  because τ_13's choice at h2 makes them W-optimal while their Ξ-value (with Odd re-responding at h0, h2) does not.
- So the separation T59 left open is answered in data: the FIRST killer is the τ frame (S4a against τ_t, with τ_t moved by Odd's own S4b
  step), at the first τ-change. σ̄-freezing alone (V1) also stops the doubling on N ≤ 8 but much later and with super-linear counts.
- Relation to ELIM-WIN (box 93): on these games N5 has HW ≤ 3 (T59) because its τ-changes cut the counter after N steps. A lemma would
  have to say why τ's own improvement makes stubborn closures W-attractive. No such statement is proved here.
- OPEN (stated precisely): is there a property P(τ) of Odd's strategy in S4a (for instance "τ is not Odd's best response at a choice vertex
  whose σ̄-target lies on a stubborn cycle") under which the arena W-optimum against τ closes, or abandons, every stubborn triple within
  O(1) steps? I have no proof and no counterexample.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box95/hn.py (GLO / V1 / V2 / SA), firstdiv.py; check.sh section "box 95"; this note.
- FINDINGS:
  1. DATA: our I^glo (arena optimum, Odd re-responding) doubles on switchbestexp (134, 286, 590, 1198; PGSolver 289 at N = 4). This confirms
     T59: ARENA-MAX does not kill H_n.
  2. DATA: N5 equals I^glo for 13 iterations (N = 3..8) and splits right after its first τ-change (12 → 13, h2 → m2). At 13 → 14 N5 also
     sends e1, e2 → d, breaking the stubborn triples' lock-step. N5: 41 … 77 iterations, linear.
  3. DATA: the arena optimum against the frozen best response σ̄_t (V1 = N5-SF's Even step) leaves I^glo only at iteration 71 (N = 3) and
     is not exponential on N ≤ 8 (135 … 489, shrinking increments), but super-linear.
  4. READING: the first killer is the τ frame (S4a against τ_t moved by Odd's own S4b step), not ARENA-MAX and not σ̄-freezing. OPEN: a
     lemma P(τ) ⇒ stubborn triples resolve in O(1) steps.
- NEEDS: none from the owner. Lead: L-RED could try to rebuild H_n's stubborn triples so that Odd's own τ-step never moves at the triples'
  exits (e.g. exits on Odd vertices with one successor, or τ already optimal there). That is the adversarial form of the OPEN question.
