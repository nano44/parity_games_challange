# Addendum to the P-N5-RL and P-N5-P1 fixes files: the referees' joint verdicts (§C) and the status of CYC-EV
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:10Z (date -u), at the Lead's request (12:58Z, which crossed
with the 13:04Z files). It adds only what those files lack. They are frozen and not edited:
- docs/si/P-N5-RL-fixes-box10.md (sha1 ac027458), part 1, REFEREE's RL-1 to RL-4;
- docs/si/P-N5-RL-fixes2-box10.md (sha1 b3e3cd93), part 2, REFEREE-2's items and the concordance;
- docs/si/P-N5-P1-fixes-box10.md (sha1 83ef83b0), N-P1-1 and the §5 correction.
Where a line here and a line there differ, the line here governs.
- Sources: REFEREE-2 R2-N5-RL §C.1-§C.4 (trunk, referee-2 88571b0); REFEREE R-N5-RL §C (trunk, referee 5f52510); R2-N5-P1 §C and
  R-N5-P1 §C. The two referees are converged.

## 1. P-N5-RL: the joint verdicts (R2-N5-RL §C.2, R-N5-RL §C)
| item | joint verdict (both referees, Opus 5.5, D15) |
| --- | --- |
| TEV-RED as stated | NOT SIGNED (RL-1 = G-RL-1: the cycle case is not covered by the proof) |
| TEV-RED′ = TEV-RED + the hypothesis "no Ev vertex lies on the cycle of x_t's σ_t-play at t", with (3) read "up to and including e" (RL-3 = G-RL-2) | SIGNED CONDITIONAL ON (P) |
| Consequence (the reduction) | NOT SIGNED as stated; it holds when TEV-RED′'s hypothesis holds at t = k |
| MERGE | MERGE′ (scope −1 ≤ ℓ < ∞; RL-2) signed by both; N-RL-1 (paths up to the first visit of c) is wording |
| EV | SIGNED CONDITIONAL ON (P), with RL-4 (citation) and N-RL-2 (q after c), N-RL-3 (wording) |
| EV+, BL (b), (c), (e), FREE-FREEZE | SIGNED CONDITIONAL ON (P) |
| R-SAME, BL-FORM, BL (a), (d), CONF-MONO | SIGNED |
| EQ-END | SIGNED CONDITIONAL ON CN-LAST |
- For landing: TEV-RED′, not TEV-RED; MERGE′, not MERGE as stated.
- Mapping rows: G-RL-1 = RL-1; G-RL-2 = RL-3 (as in part 2's concordance).

## 2. The status of CYC-EV (correction to the wording of parts 1 and 2)
- Parts 1 and 2 say RL-1 / G-RL-1 is "closed at t = k in the ENT setting by Lemma CYC-EV". That is the LANE's claim. It is NOT a
  referee verdict under P-N5-RL.
- The CYC-EV text in part 1 (sha1 ac027458) was not refereed under RL. It is under review as part of packet P-N5-ENT
  (docs/si/P-N5-ENT-box11.md, sha1 4fd22be7, §3), which also contains the FZ, BF, RB and WALK lemmas it uses.
- Until P-N5-ENT is signed:
  - the joint state of P-N5-RL is §1's: TEV-RED′ and the Consequence carry the hypothesis at t = k;
  - CYC-EV is PROVED (L-SI succ. 6), unrefereed.
- Once CYC-EV is signed in P-N5-ENT, the hypothesis of TEV-RED′ holds at t = k in the ENT setting, and the Consequence holds there
  without it.

## 3. P-N5-P1: the §5 READING correction, completed
- The joint state (R-N5-P1 §C, R2-N5-P1 §C): Lemma B, Lemma M, Lemma P1 (Steps 1-6), Corollary P1′ and the §4 hypothesis match are
  SIGNED by both, with no gap. The joint gap map is empty; N-P1-1 is wording.
- Addition to P-N5-P1-fixes-box10.md §5: "MERGE keeps RL-2." The (P) discharge does not touch MERGE. Its scope fix (−1 ≤ ℓ < ∞) stands
  independently of (P), as do EQ-END's CN-LAST condition and TEV-RED's cycle hypothesis.
- So, with P1 signed and landed, these become unconditional:
  - BL (b), (c), (e), FREE-FREEZE, EV, EV+;
  - TEV-RED′ (the cycle hypothesis is kept).
- EQ-END stays CONDITIONAL on CN-LAST. MERGE is MERGE′.
