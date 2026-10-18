# C13: landing gate for RESULTS R13 (packet 10: Lemma ENTRY-CHARGE, GAP-A ⇐ (CTX⁺) ∧ (EXIT_c)) — CHECKER, 2026-10-18

Target: docs/agents/R13-draft.md at trunk 3a9d890 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk 3a9d890 merged by merge commit.
Sources (all ancestors of 3a9d890):
- GAP-A-M.md §23q (line 3244) at the pin 1100f3a.
- The imports, §23t (l-alg 44e2bd8).
- docs/referee/R-P10.md: 8f2db93 (draft, 00:29:23Z), a09a89d (final, 00:34:28Z), aabcefd ("Written 00:27Z-00:45Z" →
  "00:27Z-00:34Z" only), and §C at 434a552 (00:44:53Z).
- docs/referee-2/R2-P10.md: 0cbe61e (00:30:28Z) and §6 at 57468a8 (00:34:43Z).
- docs/red/R37-depth-obstruction.md (l-red 59b3522).
- Code: Oink 8fbf0a7.

## Verdict: FAIL on one data clause in (e) (E-1, one-word fix); everything else PASS (notes N-1..N-3)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(e): REFORMULATION, constants, G-R13-3 | (a)-(d) PASS; (e) FAIL on E-1 |
| 2 gap union G-R13-1..6 | PASS |
| 3 re-run (e), dtl_prefexits.py unmodified, both orders | PASS on the numbers asked; they reveal E-1 |
| 4 against TARGET.md | PASS |

## E-1 (required): (e) "2 only on stealonce_viol_n76, stealonce_both_n45 and resteal34_union_n90" omits stealonce_core_n76
- REFEREE-2's probe, R2-P10/probe10_results.txt, "files with a (sigma,w) exiting twice", lists:
  - resteal34_union_n90 (stable);
  - stealonce_both_n45 (oink, stable);
  - stealonce_core_n76 (stable);
  - stealonce_viol_n76 (stable).
  The R2-P10 §5 table row lists the same four files.
- CHECKER re-run with L-ALG's dtl_prefexits.py, unmodified, on experiments/red/carry/instances/stealonce_core_n76.pg (on
  trunk since c6e0a97, sha1 4e017c28a6c8...): stable "max exits per (context, step, vertex)" = 2 (|R| 64; 30 re-entries);
  Oink 0.
- So "2 only on" three files is false as worded. Fix: add stealonce_core_n76 to the list, i.e. "2 only on
  stealonce_viol_n76, stealonce_core_n76, stealonce_both_n45 and resteal34_union_n90".
- The max-2 claim itself, "at most 2 ... on all data, both orders", is unaffected.
- Note: §23q at the pin says "only on stealonce_viol_n76 and stealonce_both_n45". Its corpus predates the wide-set probe.

## 1. Statement diff
| draft | §23q (1100f3a) | signed | |
| --- | --- | --- | --- |
| Object: FIXED σ set (every round r ≤ \|R\|+1 with G-R13-1's convention, every p-vertex τ); P_i(σ⁺); EVENT; ENTRY/EXIT; N_ent, X_R | §23q Setting ("defined for every τ ∈ V_r") | both G10-a1 halves (REFEREE-2: fixed σ set; REFEREE: round convention), joint in REFEREE §C; §23t | OK. The corrected (fixed-grid) setting is used, not §23q's per-visit "τ ∈ V_r" |
| (a) Σ_q k_q ≤ \|R\|·N_ent ≤ \|R\|·(X_R + (\|R\|+1)\|R\|²); steps 1-3 with line cites | §23q Lemma, steps 1-3 | REFEREE SWG G10-a1 closed ("Step 2 checked hard: it holds"); REFEREE-2 SWG G10-a1 closed ("fan-out step (2) is CORRECT") | OK. The constants match. Step-2 cites "142-146, 153-157, 169-172, 693" are REFEREE-2 §6's ("line-for-line the same (142-146, 153-157, 169-172, 693)"); REFEREE §C writes 143-146 (N-1) |
| (b) C1: GAP-A ⇐ (CTX⁺) ∧ (EXITS-POLY), given STR-DET; no FIRED-R, no STEAL-DEPTH | §23q (C1) | both SIGN with N10-b1 | OK. G-R13-2 carries N10-b1 |
| (c) C2: (EXIT_c) ⇒ Σ_q k_q ≤ (c+1)(\|R\|+1)\|R\|³; GAP-A ⇐ (CTX⁺) ∧ (EXIT_c), any constant c, given STR-DET | §23q (C2): "X_R ≤ c(\|R\|+1)\|R\|², ... Σ_q k_q ≤ (c+1)(\|R\|+1)\|R\|³ and F_R ≤ 3(c+1)(\|R\|+1)\|R\|³" | REFEREE (c) SIGN, constants "X_R ≤ c(\|R\|+1)\|R\|²; Σ_q k_q ≤ (c+1)(\|R\|+1)\|R\|³; F_R ≤ 3(c+1)(\|R\|+1)\|R\|³"; REFEREE-2 (c) SIGN, "CHECKED" | OK. Constants verified: c·(\|R\|+1)\|R\|·\|R\| = c(\|R\|+1)\|R\|²; \|R\|·(c+1)(\|R\|+1)\|R\|² = (c+1)(\|R\|+1)\|R\|³ |
| (d) C3: X_R ≤ N*_R·\|R\|·#steps; (EXITS-POLY) ⇔ (STEAL-POLY_sum) ⇔ (RELSTEAL) up to polynomial factors; "a REFORMULATION of a premise already in R10/R11/R12, not a reduction"; new = the LOCAL (EXIT_c) | §23q (C3): "an equivalence up to polynomial factors and not a reduction of the count" | REFEREE (d) SIGN: "C1 is a REFORMULATION of an already-signed premise ... no stronger and no weaker"; REFEREE-2 (d) CONFIRMED: "a reformulation, not a reduction" | OK. It is called a REFORMULATION, with the equivalence and "not a reduction". The heading also says "partial step-4 reformulation" |
| (e) at most 2 exits per (step, vertex), all data, both orders; 2 only on [three files] | §23q DATA | REFEREE (e) CONFIRMED; REFEREE-2 §5 | **E-1** |

The Lead's named points:
- (d) is a REFORMULATION with the equivalence up to polynomial factors and "not a reduction": yes, verbatim in (d). The
  Scope also says "a reformulation, not a bound".
- The constants in (a) and (c) are correct (table).
- REFEREE's F_R ≤ 3(c+1)(|R|+1)|R|³ against the shorter route's |R|²: both are correct. The |R|³ bound (REFEREE (c), in the
  Signatures line) goes via Σ_q k_q.
- G-R13-3's shorter route "F_R ≤ 3(X_R + (|R|+1)|R|²) ... with (EXIT_c), F_R ≤ 3(c+1)(|R|+1)|R|²" is REFEREE-2 N10-b1 and §3,
  and REFEREE §C ("R2's shorter route (the Lead's question): CONFIRMED ... R2's route is the better statement of C2"). So
  "two signatures" is right.
- The draft keeps (c) in the Σ_q k_q form and puts the tighter F_R bound in G-R13-3. That is consistent with both reports.

## 2. Verdict quotes, independence, gap union
- REFEREE table plus §C: (a) SWG G10-a1 closed; (b) SIGN N10-b1; (c) SIGN; (d) SIGN; (e) CONFIRMED. This equals the
  draft. "140 files" = REFEREE's 138-file corpus plus the two DE20 instances.
- REFEREE-2 table plus §6: (a) SWG G10-a1 closed; (b) SIGN N10-b1; (c) SIGN; (d) CONFIRMED; (e) probe, 268 files, 0
  failures. This equals the draft.
- Independence:
  - REFEREE: "docs/referee-2/R2-P10.md was not read"; §C "read after R-P10 was pushed and merged".
  - REFEREE-2: "docs/referee/R-P10.md was not read before this report was pushed"; §6 read REFEREE's 8f2db93 "after
    0cbe61e was pushed".
  - No REJECT.
- N-2 (label). REFEREE's final a09a89d (00:34:28Z) post-dates REFEREE-2's 0cbe61e (00:30:28Z). REFEREE states it did not
  read R2-P10, and the a09a89d change is "corpus data; final". REFEREE-2 §6 compares against REFEREE's draft 8f2db93, not the
  final. The verdicts are the same in both. Independence is as stated, and the timeline is recorded here for the file.
| referee item | draft |
| --- | --- |
| REFEREE G10-a1 (round convention) + REFEREE-2 G10-a1 (fixed σ set) | G-R13-1 (joint convention, as in REFEREE §C and §23t) |
| N10-b1 (both: FIRED-freeness not new) | G-R13-2 |
| REFEREE-2 shorter route, confirmed by REFEREE §C | G-R13-3 |
| (EXIT_c) OPEN, DATA c = 2 | G-R13-4 |
| (CTX⁺) OPEN | G-R13-5 |
| REFEREE-2 Gaps: G-S5-6 (ACYC) open | G-R13-6 ("also open, inherited") |
- "Closed" applies only to G-R13-1..3; G-R13-4..5 are OPEN; G-R13-6 lists dependencies. Correct.
- The import is on trunk: §23t (44e2bd8) has the joint convention, N10-b1, the shorter route "(signed)", and REFEREE's
  constants. "§23q not rewritten" holds.
- G-R13-4: "L-RED's exit climb stayed at 2 (R37 addendum, l-red 59b3522)". R37's 00:07Z addendum says "max exits stayed at
  2 ... Oink order: max 1 ... no EXIT 3". 59b3522 is on trunk. OK.
- G-R13-5: "PIECES-LAMINAR dead" is GAP-A-M §23l ("(PIECES-LAMINAR) KILLED"), an L-ALG self-kill, status only. OK.

## 3. Re-run (e): experiments/alg/dtl_prefexits.py (unmodified; last changed 3248d1f, 00:18:45Z, before the pin), RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0
| instance (sha1) | stable: max exits per (σ, w); max total/\|R\| | Oink: max exits; max total/\|R\| |
| --- | --- | --- |
| stealonce_viol_n76 (32c2da0b6ff0) | 2; 1.01 | 1; 0.16 |
| stealonce_both_n45 (ee52c4a3e47a) | 2; 2.21 | 2; 2.56 |
| resteal34_union_n90 (e59314d0c47a; experiments/alg/instances, ON trunk) | 2; 4.62 | 1; 0.06 |
| stealonce_core_n76 (4e017c28a6c8; on trunk) | 2; 2.39 | 0 |
- REFEREE's figures are reproduced: stealonce_both_n45 2.21 (stable) and 2.56 (Oink); stealonce_viol_n76 at 1 in Oink.
- "max 2 exits per (step, vertex)" holds everywhere tested. In the Oink order it is 2 only on stealonce_both_n45.
- resteal34_union_n90 is on trunk (experiments/alg/instances/resteal34_union_n90.pg). It reaches 2 (stable) with L-ALG's own
  tool too, so the claim does not rest on REFEREE-2's an10 alone.
- N-3. L-ALG's tool uses a narrower σ set than REFEREE-2's wide grid (R2-P10 §5: "the wide set includes tops no longer in
  V_r"). The per-(σ, w) maximum is 2 under both; totals differ by definition.

## 4. Against TARGET.md
- Heading: "partial step-4 reformulation (not M3, not a step-4 pass)".
- Scope: "a reformulation, not a bound. GAP-A stays OPEN ... Not the L32 single-statement criterion ... Gauntlet step 4 stays
  open".
- (d) states the equivalence and that nothing is reduced.
- No bound is claimed, so TARGET §4's exclusions are not triggered. No overstatement.

## Notes
- N-1. Step-2 line cites. The draft's "142-146" is REFEREE-2's. REFEREE §C and §23t write "143-146". Line 142 is part of
  the same condition block (`} else {` before 143 sets can_attract_new). This does not matter.

## Fix list
Required:
- E-1: add stealonce_core_n76 to (e)'s "2 only on" list.
With E-1, R13 passes. I re-diff the text only.

## Addendum: R13 draft re-diff, 3a9d890 → c886ff9 (Lead 01:14Z), text only: PASS
- History: 3a9d890 is an ancestor of c886ff9. R13-draft.md: 3 insertions, 3 deletions.
- Word diff:
  - (e) now reads "2 only on stealonce_viol_n76, stealonce_both_n45, stealonce_core_n76 and resteal34_union_n90". E-1 is
    fixed and matches §3 of this report and REFEREE-2's probe file list.
  - The header carries a revision stamp.
- Nothing else moved. R13 PASSES as at c886ff9.

## Addendum 2: post-landing text check, trunk 4a47fb3 (Lead 01:26Z): PASS (one note)
- c886ff9 is an ancestor of 4a47fb3.
- RESULTS R13 against R13-draft.md at c886ff9, from "### R13": identical except for two things.
  - The heading stamp: "CHECKER PASS (docs/checker/C13-R13-packet10.md, checker 1bd345d + re-diff 8886315)".
  - One trailing blank line.
- GAPS GAP-A row: one sentence added.
  - "RESULTS R13 (packet 10, ENTRY-CHARGE): GAP-A ⇐ (CTX⁺) ∧ (EXIT_c), given STR-DET, a reformulation with a LOCAL premise
    (EXIT_c DATA: c = 2 on all data)" is accurate to landed R13 (c), (d) and (e).
- Note (recommended). The same sentence continues "packet 11 (CHANGE-NEW, R14 draft): F_R ≤ 3·#fired⁺(R) unconditionally and
  GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to poly".
  - R14 is NOT landed: docs/agents/R14-draft.md says "awaiting L-ALG imports, CHECKER gate". It has not passed the gate.
  - "R14 draft" is stated, but the claims read as facts in the truth file GAPS.md.
  - Suggest "(R14 draft; refereed, not yet gated)" until C14 passes. If the draft text changes at the gate, the GAPS sentence
    needs the same change.
