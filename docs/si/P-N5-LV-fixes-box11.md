# P-N5-LV fixes (box 11 packet; repairs only)
L-SI successor 8 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 16:40Z (date -u), at the Lead's request (16:37Z, Lead's stamp).
- Objects, FROZEN, not edited:
  - docs/si/P-N5-LV-box11.md, sha1 d0d797f084904f9ce4df641e90298cac53c61356 (L-SI successor 6; pinned trunk 601df6e);
  - its not-to-sign addendum docs/si/P-N5-LV-addendum-box11.md, sha1 a15a8871024d33d1734a41cbeb9c2dd75ecdadef (l-si 84974fea).
- Repairs only. This file adds no new statement and no new proof.
- Sources, all on trunk (f7b6e68); file sha1s measured with `git show <commit>:<path> | sha1sum`:
  - REFEREE successor 9: docs/referee/R-N5-LV.md, report at referee 8054da2f (file sha1 0be5e352…) and §C at referee 46a80300
    (file sha1 e7c6a010…);
  - REFEREE-2 successor 9: docs/referee-2/R2-N5-LV.md, report at referee-2 b1038bea (file sha1 66e55e04…) and §C at referee-2 a769ff54
    (file sha1 db050f7f…).
- One file covers both reports and both §Cs. Its items are the union the two §Cs list: LV-N1, LV-N2 = N-LV-2, LV-N3, N-LV-1, N-LV-3.

## 0. Joint verdicts (as both §Cs record them; in substance)
- SIGN, by both referees (Opus 5.5, D15): §1 Proposition LV-SHAPE (no (P)); §2 Corollaries LV-CN, LV-COUNT; §3 Lemmas FLAT-ALL_{−1},
  STRETCH_{−1}; §4 Theorem PL_{−1} (a)-(c), Corollary LV-PL.
- REFEREE-2 signed §2 (and LV-PL's last sentence) CONDITIONAL ON CN-LAST; REFEREE recorded the condition as discharged by RESULTS R38 (f).
  REFEREE-2's §C agrees: the condition is discharged (see §1 below).
- §5 and the addendum: not signed (they were marked NOT TO SIGN).
- No gap in either report; the joint gap map is empty.

## 1. LV-N1 (status; REFEREE)
The packet's §0 lines 35 and 37 ("SIGNED, in landing: P-N5-RL (R37) …" and "In landing: CN-LAST …") are stale. Read:
- RESULTS R37 (P-N5-RL) has LANDED: Lemma R-SAME and BL's proof Step 2a are landed.
- RESULTS R38 (P-N5-SCOPE) has LANDED, and CN-LAST is R38 (f), with exactly LV-CN's hypotheses.
- So §2's label "PROVED CONDITIONAL on CN-LAST" (table line 14, heading line 66) and LV-PL's "(CONDITIONAL on CN-LAST)" read as PROVED:
  LV-CN, LV-COUNT and LV-PL's last sentence are unconditional.

## 2. N-LV-1 (citation; REFEREE-2, accepted by REFEREE)
§3, FLAT-ALL_{−1}, proof line "(i) uses only FBL and H2." Replace by:
- "(i) uses FBL, the phase and H1 at k + 1 (R31 FBW-1): a switched cycle node's new cycle avoids o by H1 at k + 1."
- Reason (REFEREE's §C): an honest cycle through o need not be a W-cycle (the honest and W-plays differ at o), so H2 does not exclude it.
  (h) at k + 1 is a hypothesis of the lemma, so no verdict changes.

## 3. LV-N2 = N-LV-2 (precision; both)
§3, STRETCH_{−1}: replace "among the fallbacks k of S with s ≤ k < e" by "among the fallbacks k of S with s ≤ k ≤ e". The bound n stays.
- Proof (both reports): order y's level −1 tail events k_1 < … < k_m ≤ e. Then b_{k_1}(y) ◁ … ◁ b_{k_m}(y), all with the same
  COARSE_{−1} part, so they differ in length only, and lengths lie in {0, …, n − 1}. The last event needs no state after it. So m ≤ n.
- §4 PL_{−1} (a) applies STRETCH_{−1} to the run that ends at f_N, where e = f_N is possible (when (h) fails at f_N + 1). It needs this
  form. (Same point as R31's FBW-2.)
- REFEREE-2's fill-in for step (1), adopted by REFEREE: the map x ↦ COARSE_{−1}(y ⊕ x) is injective here, because y lies on neither
  successor's pre-c path (as in P-N5-ENT Lemma BF).

## 4. LV-N3 (wording; REFEREE, accepted by REFEREE-2)
§4, PL_{−1} (a): replace "[f_1, f_N] splits into at most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ)" by "the block's fallbacks lie in at
most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ)".
- The original wording is false when a dirty interval has several COARSE_{−1} changes. The proof uses only the repaired form.

## 5. N-LV-3 (DATA; REFEREE-2, re-run by REFEREE)
§5, OPEN item "THR fallbacks with u* = none (r = −1) … DATA: 0 in scope" is no longer true. Read:
- DATA: in-scope THR fallbacks with r = −1 (M = −1) ARE reachable.
  - REFEREE-2's climbs: 173,371 (850,608 runs). Witness docs/referee-2/R2-N5-LV/climb/best_lv_9401.pg, sha1 4b74cd84…, one on the SPEC
    trace from the S3 start (state 2). The Lead re-ran it: one Odd choice vertex, Oink zlk OK, strategies verified.
  - REFEREE's climbs: 351,417 (769,515 mutants), re-counted on its own engine.
  - LV-SHAPE held at every gate there: 1,037,743 (REFEREE-2) and 1,321,606 (REFEREE), 0 failures.
- So §1-§2's setting is NOT vacuous for r = −1. The r ≥ 0 part (FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL) stays vacuous in both
  referees' data, and in §6's.
- These fallbacks are the ones PL_{−1} / LV-PL do not count (they need r ≥ 0). They are bounded separately by LV-NONE (packet P-N5-LV2,
  docs/si/P-N5-LV2-box12.md §7, in review). Neither referee's climbs found a scope run with more than one of them.
- §6's "THR with r = −1: 0" is right for the packet's own data set and stays as DATA for that set.

## 6. Addendum: NL= is FALSE (status; Lead, both §Cs)
- The addendum's CONJECTURE NL= (NL (i)-(iii) at r_j = L) is FALSE: L-RED experiments/red/so/instances/nleq_cex_n48.pg, sha1
  e72e40343b33df295d5877ff29125b154e71949c (l-red d7df76f9: an NL (ii) leave at r = L = 47, step j 6, vertex 40 → 9). The Lead re-ran it.
  This lane has not re-run it.
- The addendum's READING "NJB in full ⇐ (P) ∧ NL=" therefore gives nothing; NJB's straddling interval stays OPEN.
- NL= was NOT TO SIGN. Both §Cs confirm that no step of §1-§4 cites NL at r_j = L, so no signed item is affected.
