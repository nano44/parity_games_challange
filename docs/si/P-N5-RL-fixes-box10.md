# Fixes to packet P-N5-RL, part 1: REFEREE's items (RL-1 to RL-4), the TEV dead ends, and the k0-quantifier point
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~12:50Z (date -u), at the Lead's request (12:34Z).
- Object: docs/si/P-N5-RL-box10.md, sha1 0a3c70cbf873b2e011a5a00be54d38926f7861f1, pinned trunk 2fb698d. FROZEN, not edited.
- Source: REFEREE successor 8, docs/referee/R-N5-RL.md on origin/claude/referee (b7419da, §8.1 257c3d8), section "Fixes-file lines".
  REFEREE-2's report (R2-N5-RL) is not read here; its items go to a part 2 (docs/si/P-N5-RL-fixes2-box10.md).
- A record of repairs, not itself refereed text. Labels: PROVED (L-SI succ. 6) = no (P); CONDITIONAL on (P); FALSE; DATA.

## RL-1 (§6 TEV-RED (1), proof gap; REFEREE: NOT SIGNED as stated, TEV-RED′ signed)
- The gap, as REFEREE states it: "the last Ev vertex e" and "f's play lies in F_{k0}" need that no Ev vertex lies on the cycle of x_t's
  σ_t-play. The packet does not prove this.
- Fix (both parts below together):
  - (i) At t = k, in the ENT setting, the hypothesis is PROVED (Lemma CYC-EV below, no (P)). So TEV-RED (1)-(5) at t = k, and the
    Consequence, hold as stated (with RL-3's wording).
  - (ii) For t ∈ (k0, k), TEV-RED is restricted to TEV-RED′: TEV-RED with REFEREE's added hypothesis "no Ev vertex lies on the cycle of
    x_t's σ_t-play". CYC-EV is not claimed at S4a states. There gates of level > L into R̄ are allowed, which is what its proof excludes.
  - Replacement statement: "Proposition TEV-RED. Let t ∈ (k0, k] be a state after the rise, and suppose the σ_t-play of x_t meets Ev.
    If t < k, assume also that no Ev vertex lies on the cycle of that play; if t = k, this holds by Lemma CYC-EV. Let e be the last Ev
    vertex on the play's prefix before its first visit to c, … (1)-(5) as in the packet, (3) as in RL-3."
- Lemma CYC-EV (PROVED, L-SI succ. 6; proof in docs/si/N5-TEV-box11.md §3 Step 1′, sha1 58a0b3cf, with §1-§2 there). In the ENT setting,
  no vertex of Ev ∩ F_k lies on C_k, the σ_k-cycle of c (the cycle of x_k's play).
  - Setting (Σ) of N5-TEV-box11.md §0: k0 < k consecutive fallbacks of S, L = M_{k0} ≥ 0, r > L on [k0+1, k]. Then (A_s), no leave, and
    M_k ≤ L (CLS2). The ENT setting adds M_k = L and a rise, so B ≠ A.
  - Proof, self-contained:
    - FZ: a vertex free at k is free on [k0+1, k], and its COARSE_L(Ξ) is the same at k0 and at k (FLAT-ALL (iii) across k0; NL (i) at the
      S4a steps of (k0, k)).
    - BF: for Even v ∈ R_{k0} ∩ F_k, COARSE_L(b_k v) = COARSE_L(Ξ_{k0} σ_{k0}(v)). Both have cycle node c. Remove v from FZ's path sets
      via (P2) and (C4). v is not on the pre-c path of its successor's play, and v ≠ c since c ∈ F_{k0}.
    - RB: if moreover a := σ_{k0}(v) ∈ R̄_k, then COARSE_L(Ξ_k a) = COARSE_L(Ξ_{k0} a). Otherwise R15 (a), (C1) and BF make (v, a) a gate
      at k of level > L ≥ M_k.
    - WALK: from v0 ∈ R_{k0} ∩ F_k, follow the k0-route to its first vertex a_j ∈ R̄_k. Its predecessor is Even (an Odd vertex other than
      o with its only successor in R̄_k is in R̄_k), and RB applies there. By Lemma G at k0 and at k:
      (π^k_{a_j} ∩ H) ⊔ B = (π^{k0}_{a_j} ∩ H) ⊔ A. So if the route after v0 is low, then B ⊆ A.
    - CYC-EV: let v ∈ Ev ∩ F_k lie on C_k. Then v ≠ c, and c tops C_k, so COARSE_L(Ξ_k v) = (c, ∅). By FZ and Lemma G at k0,
      (c, (π^{k0}_v ∩ H) ⊔ A) = (c, ∅). So A = ∅, and v's route is low. WALK from v gives B ⊆ A = ∅, against B ≠ A. □
- REFEREE's remark (no gap) on EV's bookkeeping when q lies on the cycle after c: accepted. In the ENT setting, CYC-EV also shows that
  case does not occur for z's play: z's value has cycle node c, so its cycle is C_k.
- DATA: REFEREE's probe found 0 states with Ev ∩ C_t ≠ ∅ in 732 + 1,353 TEV states, and 0 after 3 × 1,500 s climbs. This is consistent
  with CYC-EV at t = k and does not test t < k.

## RL-2 (§5 MERGE, scope; wording)
- Replace "Let (y, z) be a window gate of level ℓ ≥ −1" with "Let (y, z) be a window gate of level −1 ≤ ℓ < ∞ (equivalently ℓ ≤ n − 1)".
- At ℓ = ∞ (z's cycle node ≠ c), H = ∅, and (c) has no common vertex: experiments/si/orlens/instances/inr2_n32.pg, state 0, gate
  (6, 29), whose plays are disjoint (REFEREE §5).
- Every use of MERGE (EV, EV+) is at the finite level L ≥ 0, so §6 is unaffected.

## RL-3 (§6 TEV-RED (3) and the Consequence's third bullet; wording)
- (3): replace "B_t = A ⊔ (the H-vertices of x_t's play before e)" with "B_t = A ⊔ (the H-vertices of x_t's play up to and including e)".
- Consequence, third bullet: replace "the rise vertices B ∖ A lie on the threat's play before e" with "… up to and including e".
- The proof already computes Ξ_t(x_t) = (x_t's play up to e) ⊕ Ξ_t(f), with e included. e ∈ H is not excluded.
- It occurs: on L-RED's tevlast_cex_n40 (below), B ∖ A = {15} = e itself (L-RED 16, tevred16.py, via the Lead 12:27Z). (4) and (5) need
  only B_t ⊋ A and are unaffected.

## RL-4 (§6 EV, citation)
- Replace "By ENT-SHAPE (signed), there is a level-L window gate (y, z) at k" with "By P-N5-NJB §3's Corollary to NO-RF-OLD (RESULTS
  R35), there is a level-L window gate (y, z) at k: the level-L tail of R25 FB step (2) switches along a gate of level L ≥ 0, which is
  R → F by FBL. ENT-SHAPE (1)-(4) then apply to it."

## §7 TEV: FALSE in both forms (dead end; recorded in docs/si/DEAD.md)
- CONJECTURE TEV ("after an in-scope THR fallback k0", any earlier k0): FALSE on experiments/red/so/instances/tev_cex_n40.pg
  (sha1 17078f78; L-RED 16; Lead re-run: n5 27 / 16, Oink OK).
  - k0 = 4 (L = 33, Ev = {5, 8, 12, 15}). At t = 23 the threat x_23 = 5 ∈ Ev. 15 fallbacks lie between k0 and t.
- TEV-LAST (k0 the last fallback before t): FALSE on experiments/red/so/instances/tevlast_cex_n40.pg (sha1 ff1e9cb4; L-RED 16; Lead re-run:
  n5 11 / 1, Oink zlk OK, strategies verified; L-SI succ. 6 re-ran threv.py: thr_ev_rise 1 at (k0, t, L) = (3, 7, 32)).
  - At t = 7 (an S4a state after the rise at 6 → 7) the threat's play is 5 → 15 → 35 → 26 → 28 → 11. It starts in Ev and passes 15.
  - Obstruction (checked by L-SI succ. 6): the walk of CYC-EV's proof from e = 15 ends at v = 15, with the gate (15, 21) of level 33 > L
    at t = 7 (M_7 = 33). 15 lies in R at 8: the threat through Ev is absorbed back at the next S4a step. A fallback state forbids such a
    gate, which is why TEV holds at fallback states (N5-TEV-box11.md §3 Remarks, no (P)).
- Neither instance has a second fallback after the rise, so NJB / ENT are not refuted, and nothing signable in the packet is affected.

## The k0-quantifier point (L-RED 16's diagnosis, via the Lead 12:19Z)
- L-RED: "no vertex leaves R in (k0, t]" fails when fallbacks lie between k0 and t.
- The packet's signable items checked against that:
  - FREE-FREEZE (§3) quantifies over any later state t of the phase with (h). Its proof uses no "no leave" step. It uses only
    R15 (a), Lemma G at t, σ′ ∈ G_τ[F_{k0}], F1 and BL (c) at k0, and REFEREE checked it in that generality (R-N5-RL §3). Unaffected.
  - BL, BL-FORM, CONF-MONO, MERGE, EQ-END are single-state or single-scope-run statements with no k0 / t pair. Unaffected.
  - EV, EV+, TEV-RED (§6) are stated in the ENT setting: k0 < k CONSECUTIVE fallbacks of S, t ∈ (k0, k]. So no fallback lies in (k0, t),
    and every step in (k0, t] is an S4a step, where NL (ii) applies. Unaffected.
- Only §7's CONJECTURE TEV (and docs/si/N5-RL-box10.md §5's copy) quantifies over an arbitrary earlier fallback k0. That is the form
  tev_cex_n40 refutes.
- Suggested wording for §7, record only (the conjecture is dead either way): "after an in-scope THR fallback k0 of level L ≥ 0 and
  before the next fallback of S".

## Concordance (REFEREE's rows; REFEREE-2's rows will be added in part 2)

| row | REFEREE (R-N5-RL) | status after this file | governing line |
| --- | --- | --- | --- |
| 1 | RL-1 (TEV-RED (1), proof gap) | closed at t = k in the ENT setting by Lemma CYC-EV (no (P)); TEV-RED′ for t < k | RL-1 above |
| 2 | RL-2 (MERGE, scope) | wording | RL-2 above |
| 3 | RL-3 (TEV-RED (3), Consequence) | wording | RL-3 above |
| 4 | RL-4 (EV, citation) | citation | RL-4 above |
| — | TEV, TEV-LAST (§7, not to sign) | FALSE (tev_cex_n40, tevlast_cex_n40) | §7 above; docs/si/DEAD.md |
