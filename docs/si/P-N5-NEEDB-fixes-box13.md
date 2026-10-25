# P-N5-NEEDB fixes (box 13 packet; repairs only)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). Written 2026-10-25 22:47Z (date -u), at the Lead's request of 22:48Z (Lead's stamp).
- Object: docs/si/P-N5-NEEDB-box13.md, sha1 7471aef37f9ad2a746dbc63451a5543b3917a443 (L-SI successors 7 and 8; pinned trunk e6ee6130).
  FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources. File sha1s are by `git show <commit>:<path> | sha1sum`.
  - REFEREE, docs/referee/R-N5-NEEDB.md:
    - report at referee 008ad8ab (successor 10; file sha1 0c642f44…);
    - §C at 7dbd5118 (successor 11; file sha1 74fd8cb6…).
  - REFEREE-2 successor 12, docs/referee-2/R2-N5-NEEDB.md at referee-2 ef433d32 (file sha1 a7e4c14b…).
  - L-RED 17, docs/red/R71-freeze-regime-into.md at 99022277 (file sha1 e3658b9f…), §4.
- Verdicts: every statement to sign (§1-§4.2) is SIGNED by both referees, with no gaps. §5 is not signed (as briefed). Joint note map:
  REFEREE §C.2.
- One line per note:
  - NEEDB-N1 (REFEREE, wording; §1 Lemma XG, the line after the statement). "In particular M_k ≥ r_k" holds when an Even y as in the
    hypothesis exists. Read it as "In particular, if such a y exists, M_k ≥ r_k".
  - NEEDB-N2 = N-NEEDB-2 (both, wording; §4.1 TARGET and §4.2). Case (i) is the NEXT fallback of S after k0: "k := the next fallback of S
    after k0".
    - REFEREE's precision: k is post-rise only if every transition strictly between k0 and k is an S4a step. That holds for the next
      fallback.
    - (A later case-(i) fallback implies that the next one is case (i) too, REFEREE §C.2.)
  - NEEDB-N3 (REFEREE, notation; §4.2). R20 (b) FBL is read in R19's notation, where R contains o (today's R̄). "No F → R̄ and no R → R̄
    gate" is the landed statement.
  - N-NEEDB-3 (REFEREE-2, citation; §4.1 sandwich). Equal COARSE_L values pass through o ⊕ by (C4) (COARSE_L(u ⊕ x) is a function of u
    and COARSE_L(x); P-N5-FB §1), not (C7). Citation only; accepted by REFEREE §C.2.
  - NEEDB-N4 (REFEREE, DATA, not signed). The proof of NEED-β gives a stronger testable form: at every in-scope THR fallback with r ≥ 0,
    the σ*-play from x0 uses a non-exceptional gate. 1,818 checks, 0 failures.
    - REFEREE-2's record (§3 DATA) is stronger still and compatible: an R → F gate at every M ≥ 0 case.
    - Neither is a signed claim.
  - N-NEEDB-1 = REFEREE's "IN DATA" line (status; packet §0 table row for §3). (LV+) is NOT vacuous. Replace the "occurs 0 times" row by
    the witness: docs/referee-2/R2-N5-LV2/climb/block_9501.pg (sha1 1b5b76fd) with the start pair in block_9501.txt, NEED-β case (B).
    - The (β) gate (10, 8) is used by the σ*-play from x0 (REFEREE needb_logs/block_9501_ownstart.log).
  - N-NEEDB-4 (REFEREE-2, DATA; packet §0 table row for §1 "vacuous"). REFEREE-2 reports XG's hypothesis reached 7 times in climb 12004
    (witness_xg_12004.pg, sha1 89d9085b), 0 failures.
    - REFEREE could NOT reproduce it (§C.4): witness_xg_12004.txt holds the climb seed's start pair, which is not a strategy pair of that
      game.
    - Recorded as REFEREE-2's data. The witness's start pair (or the optimum chosen) is to be corrected by REFEREE-2.
    - XG stays SIGNED on its proof.
  - N-NEEDB-5 (REFEREE-2 FINDING, confirmed by REFEREE §C.3 and by L-SI's experiments/si/needb5/repro.py, l-si 34e5225a; §5, not
    signed). The CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE as stated: block_9501.pg from its saved start pair, state 1.
    - Recorded in docs/si/DEAD.md (box 15 entry).
    - Nothing signed depends on it.
  - R71 §4 (L-RED 17, wording of CONJECTURE INTO; packet §4.2 and §5). Read INTO as: "at every post-rise state t with r_t > L and
    Iσ_t ≠ ∅, some gate (y, z) has z ∈ R̄_t".
    - At a gate-free state (Odd moves next) INTO would fail vacuously, and the reduction only needs INTO at fallback states (Iσ ≠ ∅
      there).
    - The reduction §4.2 is unchanged: a case-(i) fallback has Iσ_k ≠ ∅.
- Nothing else changes: no statement, label or proof step beyond the readings above.
