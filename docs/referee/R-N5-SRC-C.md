# R-N5-SRC-C: REFEREE §C on P-N5-SRC: cross-map against REFEREE-2 (R2-N5-SRC, claude/referee-2 e8c1b62d), joint gap map, line L-2
Referee: REFEREE (successor 21), Opus 5.5 (D15). Written from 23:11Z (2026-10-30, by date -u).
- My report is R-N5-SRC.md (claude/referee 81f6b89c), with R-N5-SETTLE.md Addendum 1 (8951ef7c). Both were written by successor 20
  before it opened any docs/referee-2/ file on SRC.
- The Lead's brief (23:11Z) gave the §C word and named R2-N5-SRC.md @ e8c1b62d (169 lines). I read it after both of my reports were on
  origin. REFEREE-2 24's own §C (R2-N5-SRC-C, referee-2 824651dd) was not opened before this section was written (§5).
- Object: docs/red/P-N5-SRC.md @ l-red 0521fb82, sha1 3caae56e3afdfaab80739c0e12e397b3d6cc7a8b. Both reports re-hashed it and agree.
- Scope (D1): a REDUCTION and an EQUIVALENCE inside W-runs of N5. Nothing is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.

## 1. Cross-map
| item | REFEREE (R-N5-SRC + SETTLE Add. 1) | REFEREE-2 (R2-N5-SRC) | joint reading |
| --- | --- | --- | --- |
| §1 (R1), (R2), definitions | CHECKED | checked ✓ | agree. Both: no vertex before c on a W-path to c is in C, so W(b) reads nothing of σ(c) |
| §2 PLAY-CAUSE^S | SIGNED | SIGNED | agree. Both note that it strengthens [SET]'s PLAY-CAUSE, because D_k ∪ D_(k+1) ∪ C ⊆ S_k |
| §3 (S_j)/(X_j), C1-C7 | SIGNED | SIGNED | agree, item by item (C5 (PATH) up to c; C7 u before c; σ_k(c) and σ_(k+1)(c) never compared) |
| G-SRC-1 (the ρ-play from y re-enters c's cycle in [SET] §5 Cases 2 and 2b) | found (§3), closed by a four-way split | found (§3.2), closed by Lemma ONE-STEP | found independently by both. The two repairs are the same split: the top of the new cycle is c / even ≠ c / odd ≠ c |
| Lemma ONE-STEP | SIGNED (SETTLE Add. 1 (2)) | PROVED (referee-originated) | double-signed. G-SRC-1 is CLOSED |
| §4 TAIL (T0), (T1) | SIGNED | SIGNED | agree. Same LEX induction on L. My note «(T1) needs only k → k + 1 source-free» = R2's «k + 1 → k + 2 ∈ F is assumed» |
| §5 SRC-SETTLE, SRC-COUNT, EQUIVALENCE | SIGNED | SIGNED | agree |
| §6-7 F1, F2, DATA | not signed | not signed (READING) | agree |
| line: \|F\| undefined | SRC-L1 REQUIRED | SRC-L1 REQUIRED | same |
| line: t free in the R57 gloss | SRC-L2 REQUIRED (t) | SRC-L2 REQUIRED (t, and σ_new not a line symbol) | R2's form is stricter. I agree that σ_new is unbound too (it bears on SETTLE, see R-N5-SETTLE-C §6) |
| line: proof note cites RUN-SETTLE without the G-SRC-1 repair | SRC-L3 second bullet, precision | SRC-L3 REQUIRED | I upgrade it to REQUIRED. The note cites a proof that needs ONE-STEP |
| line: V not named («n := \|V\|») | SRC-L3 first bullet, precision | not raised | precision only. V is the game's vertex set in every landed N5 line |
| line: «… are not events» → «not source events (unless …)» | not raised | N-1 precision | I agree (applied in L-2) |

## 2. Data reconciliation (G-SRC-1's configuration)
- The two counts look different, but they count different predicates. There is no engine disagreement.
  - Mine (R-N5-SRC §7): a SWITCHED y ∉ C with b ∈ H_(k−1)(y), y on c's σ_k-cycle. These are actual Case 2 configurations.
    Count: 3, all with top c, on 813 runs, n ≤ 100.
  - REFEREE-2's (OS): every ONE-STEP precondition (y ∉ C Even, z ∈ H_t(y), λ_W(z) = c, z's path avoids y), whether or not y switches.
    Count: 852,572 instances; y on c's cycle 9,055 (3,457 + 671 + 2,151 + 2,776); new top ≠ c 4, all odd (ret22_n40 with its start, t = 2-5).
    REFEREE-2 states that y does not switch to z in any of the 4.
- Both counts agree with the lemma. An even new top never occurs (both: 0). An odd new top makes ONE-STEP strict. In a Case 2 configuration
  that is excluded: the chain W_k(y) ▷ y ⊕ W_k(b) = W_(k+1)(y) ⊵ W_k(y) is a contradiction (my §3 (iv)). This matches REFEREE-2's finding that
  none of its 4 states is a switch.
- Longest source block:
  - REFEREE-2: 67, on gate_K64_n581 (n 581).
  - Mine: 63 at n ≤ 100. gate_K64_n581 is outside my MAXN.
  - The packet says 67. This is a run-set difference, the same one as in R-N5-SETTLE-C §2.
- Longest C-only tail: 1 on the corpus and 2 on cn3_n9, on both sides.

## 3. Joint gap map
- Packet items to sign: no open gap on either side. Nothing FALSE.
- G-SRC-1:
  - Found independently by both referees.
  - CLOSED by Lemma ONE-STEP: proved by REFEREE-2 24 (R2-N5-SRC §3.2) and signed by REFEREE (R-N5-SETTLE Addendum 1, 8951ef7c).
  - Lemma ONE-STEP is referee-originated (L41).
  - The same gap and repair apply to [SET] §5 (P-N5-SETTLE, RUN-SETTLE). That gap was a joint miss of both SETTLE reports.
- Line, REQUIRED (union):
  - SRC-L1 (|F|);
  - SRC-L2 (the R57 gloss: t free, σ_new unbound);
  - SRC-L3 (the proof note cites ONE-STEP for Cases 2 and 2b; the scope tail says it is referee-originated).
- Line, precision:
  - R2 N-1 (applied in L-2);
  - my «V» (optional).

## 4. Line revision L-2 (l-red 77a6d979, docs/red/P-N5-SRC-line-L2.txt, sha1 9fcb57903ad64a0ab7f56acb2f651f354b3616fc)
- Word-diff against the frozen line (0521fb82, sha1 3101a0c0). The changed tokens:
  - «for S4a, σ_new … H_t, …» → «for S4a at a transition k → k + 1, σ_(k+1) … H_k)» (SRC-L2, REFEREE-2's form);
  - «|F| := the number of transitions of F;» inserted after E^S_F's definition (SRC-L1);
  - «are not events,» → «are not source events (unless they change Ξ at a source),» (N-1);
  - the source note gains «; fixes docs/red/P-N5-SRC-fixes.md entries 1-2».
  Nothing else changed. This equals fixes entry 2's E2.1-E2.3 and its source-note item. L-1 (059d2733) is superseded and stays filed.
- Strict symbol test on the new tokens:
  - In the gloss, k is bound by «at a transition k → k + 1».
  - σ_(k+1) is bound by «a run is the sequence of states (σ_k, τ_k)».
  - H_k is defined later in the line, «for a state k of F». That is a forward reference to a defined symbol.
  - |F| is bound in the definitions, where F is the W-run name used by E^S_F and HXS_F.
  - No free symbol.
- Verdict on L-2: MATCHES SRC-L1, SRC-L2 and N-1 (Opus 5.5, D15).
  - SRC-L3 (REQUIRED) is not applied yet; it goes into L-3 (fixes E2.4). I word-diff L-3 when the Lead sends it.
  - For L-3: «Lemma ONE-STEP» must name its source as REFEREE-2 docs/referee-2/R2-N5-SRC.md §3.2 (e8c1b62d), signed by REFEREE in
    R-N5-SETTLE.md Addendum 1 (8951ef7c).
  - If L-3 states ONE-STEP in the line, ⊕ has to be defined there, because L-2 has no ⊕ (SETTLE L-2 does).

## 5. After writing §1-§4: REFEREE-2 24's §C (R2-N5-SRC-C, claude/referee-2 824651dd)
- Opened after §1-§4 were written (2026-10-30 23:12Z by date -u). Its C.1, C.3 and C.4 agree with my §1, §3 and §2 item by item.
- Its two open points are now settled:
  - «REFEREE's verdict on my ONE-STEP is pending». That verdict is SIGNED, in R-N5-SETTLE.md Addendum 1 (8951ef7c, 22:47Z). So each repair
    of G-SRC-1 (my four-way split, REFEREE-2's ONE-STEP) is signed by the other referee. G-SRC-1 is CLOSED, and the joint gap map is EMPTY
    of open gaps.
  - «SRC-L3: Lead decides». I upgrade SRC-L3 to REQUIRED (§1), so the two referees now agree that it is REQUIRED. No ruling is needed.
- Its precision note on my (ii)-(iv): «b's path is disjoint from c's arc from c to y». I accept it. ONE-STEP (β) states the step, and my
  Addendum 1 relies on ONE-STEP.
- It says V is bound fleet-wide by TARGET.md l. 8. I agree: my «V» item is optional.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  1. SRC: both referees SIGN every item. G-SRC-1 was found by both and is closed by Lemma ONE-STEP, which is now double-signed. The joint gap
     map is empty of open gaps.
  2. Line: the REQUIRED changes are SRC-L1, SRC-L2 and SRC-L3. L-2 MATCHES the first two; SRC-L3 is pending in L-3.
  3. The configuration counts are reconciled: they count different predicates, and there is no disagreement.
- NEEDS: Lead: the SRC L-3 SHA, for the word-diff.
