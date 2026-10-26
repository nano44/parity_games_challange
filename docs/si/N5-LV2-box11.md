# N5 box 11, part 5 (L-SI successor 6): counting level −1 THR fallbacks per scope run (READING), and what is left
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:50Z (date -u), Lead GO 13:48Z. Lane write-up, unrefereed.
Builds on docs/si/N5-LV-box11.md (sha1 407c5520, frozen): LV-SHAPE (PROVED) and LV-CN (CONDITIONAL on CN-LAST, now landing as R38).
- Labels: PROVED (L-SI succ. 6); READING (each step names the proof it reuses; the reuse was checked against the text, not
  re-proved line by line); OPEN; DATA.
- Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.

## 1. Where R31's level-≥0 machinery uses M ≥ 0 (PROVED, by reading P-N5-FBW §3-§5)
- FLAT-ALL (P-N5-FBW §3). M ≥ 0 is used once, at "By FBW-S, r_k ≥ M ≥ 0, so k is THR with u* ≠ none". The rest uses:
  - FBL (u* ≠ none);
  - OFF at level M_k (R25 (e), stated for COARSE_{M_k} with M_k ≥ −1);
  - Lemma G, (C7), CAP-1, Lemma S (a);
  - TRANSFER (every L < ∞).
  So FLAT-ALL (i)-(iv) hold verbatim at every in-scope fallback with M_k = −1 and r_k ≥ 0, with COARSE_{−1} in place of COARSE_M.
- STRETCH (§4). Step (1) is level-free (it uses CN for cycle nodes). Steps (2)-(3) use the rank-M bit β, which does not exist at M = −1.
  - Replacement STRETCH_{−1} (PROVED here). On a stretch [s, e] with COARSE_{−1}(Ξ) constant, each Even y is a level −1 tail at most n
    times among the fallbacks of S in [s, e).
  - Proof. By step (1), COARSE_{−1}(b(y)) = (c_y, P_y) is constant on [s, e]. b(y) is ⊴-non-decreasing (R15 (a), (d)). With (c_y, P_y)
    fixed, ⊴ is the length order: shorter is better if c_y is even, longer if odd.
  - At a level −1 tail event at k, b_{k+1}(y) = Ξ_{k+1}(z) ⊵ Ξ_k(z) ▷ b_k(y), with the same COARSE_{−1}. So the length moves strictly in
    the better direction.
  - Lengths lie in [0, n − 1], so there are at most n such events. □
- PL (a) (§5). It combines FLAT-ALL (iii) with STRETCH. At M = −1 it gives N_{−1} ≤ n·n_E·(1 + D_{−1}): blocks of fallbacks of S at level
  −1 with r ≥ 0, cut into at most 1 + D_{−1} constant-COARSE_{−1} runs, and STRETCH_{−1} on each run. (READING: PL (a)'s proof with
  STRETCH_{−1}.)
- PL (b) and RDROP: they use FLAT-ALL (iv), TRANSFER, U-loc with L = M, and Lemma OR / TC-SPLIT. None needs M ≥ 0 beyond FLAT-ALL. So the
  first COARSE_{−1} change of a dirty level −1 interval is an absorption with lev(θ_j, θ_{j+1}) > −1 and r_j > −1. (READING: the U-loc
  step at L = −1 was not re-checked line by line.)
- PL (c′) (R35). Its count of absorptions against N_x (exits in R) uses NL (ii) at L = M while r > M. At M = −1 that is NL with L = −1,
  which holds while r ≥ 0 (R29 (e) needs only L < ∞ and r_j > L). So D_{−1} ≤ (d_o − 1) + REL_{−1}, plus at most 1 straddling interval
  (the one in which r drops to −1), as in P-N5-ENT's D1 argument. (READING.)

## 2. The count (READING, L-SI succ. 6)
**Reading LV-PL.** In every scope run S, the THR fallbacks with M = −1 and r ≥ 0 number at most n·n_E·(d_o + 1 + REL(S)).
- Proof sketch: §1. By CLS2 they form one block (the levels are non-increasing, and −1 is the lowest level a fallback can have).
  PL (a) with STRETCH_{−1}, then D_{−1} ≤ (d_o − 1) + REL + 1.
- With LV-CN (CN-LAST, R38 landing): of these, all but the (β)-fallbacks end their phase, so at most one per phase is not a
  (β)-fallback.
- REL(S) appears here because P-N5-ENT's ENT-X (which removed REL(S) at levels ≥ 0) uses the rank-L bit (ENT-SHAPE (4)), which has no
  level −1 analogue. A length-based ENT-SHAPE is OPEN.
**What is NOT covered (OPEN).**
- THR fallbacks with u* = none (r = −1):
  - by LV-SHAPE, all gates are (α), (β) or (γ);
  - NL at L = −1 needs r > −1, so neither NL nor the (A)-chain is available;
  - Fact R keeps r ≤ −1 for the rest of S.
  - DATA: 0 such fallbacks in scope (N5-LV §4); P-N5-FBW §6 records the same.
- "THR ⇒ M ≥ 0" itself (CONJECTURE). LV-PL makes it unnecessary for polynomiality of the r ≥ 0 part, up to REL(S).
- REL(S) at level −1.

## 3. Status summary of in-scope fallbacks after box 11 (for the Lead; each line labelled)
| fallback kind (in a scope run S) | bound | label |
| --- | --- | --- |
| level ≥ 0 | ≤ 2·n·n_E per S (no REL) | PROVED CONDITIONAL on (P) (P-N5-ENT D1, PL-S″); (P) = P1, R36 landing |
| level ≥ 0, alternative | ≤ n_E·(n·d_o + REL(S)) per S | signed, R35 PL-S′ |
| level −1, THR, r ≥ 0, no (β) gate | ≤ 1 per phase, the phase's last transition | CONDITIONAL on CN-LAST (N5-LV LV-CN) |
| level −1, THR, r ≥ 0, all | ≤ n·n_E·(d_o + 1 + REL(S)) per S | READING (§2 LV-PL) |
| level −1, THR, r = −1 (u* = none) | none | OPEN (0 in data) |
| EQ | ≤ 1 per S, the phase's last transition | CONDITIONAL on CN-LAST (P-N5-RL EQ-END, signed) |
