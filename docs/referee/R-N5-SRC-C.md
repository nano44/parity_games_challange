# R-N5-SRC-C: REFEREE §C on P-N5-SRC: cross-map against REFEREE-2 24 (R2-N5-SRC, claude/referee-2 e8c1b62d), joint gap map
Referee: REFEREE (successor 20), Opus 5.5 (D15).
- The Lead gave the §C word at 22:56Z (read 23:13Z by date -u).
- My report R-N5-SRC.md (81f6b89c) was written and pushed before I opened R2-N5-SRC.md. I opened it for the ONE-STEP check (R-N5-SETTLE
  Addendum 1, 8951ef7c) and for this §C.

## 1. Cross-map
| item | REFEREE (R-N5-SRC) | REFEREE-2 (R2-N5-SRC) | joint reading |
| --- | --- | --- | --- |
| (R1), (R2), definitions | checked | checked | agree |
| PLAY-CAUSE^S | SIGNED | SIGNED | agree. Both: it needs no σ̄ / CN condition, since D_k ∪ D_(k+1) ∪ C ⊆ S_k |
| (S_j)/(X_j), C1-C7 | SIGNED, G-SRC-1 closed by my four-way split (§3) | SIGNED, G-SRC-1 closed by Lemma ONE-STEP (§3.2) | the SAME gap, found independently, closed by the same argument (top of the new cycle: c / even / odd). ONE-STEP is the proof of record (Lead reading L41); I signed it in R-N5-SETTLE Addendum 1 |
| Lemma TAIL | SIGNED | SIGNED | agree (both: the LEX branch by induction on L, IDX immediate) |
| SRC-SETTLE, SRC-COUNT, EQUIVALENCE | SIGNED | SIGNED | agree. Both note that the line's «maximal run» narrows the packet's «every source block» |
| line SRC-L1 (|F|) | REQUIRED | REQUIRED | same |
| line SRC-L2 (H_t) | REQUIRED | REQUIRED, and also σ_new as a non-line symbol | same; I take REFEREE-2's exact text «σ_(k+1) … H_k» |
| line: proof note cites the SETTLE induction | SRC-L3 precision (cite G-SRC-1) | SRC-L3 REQUIRED (cite ONE-STEP) | I agree it is REQUIRED: the cited induction is signed only through ONE-STEP. Upgraded |
| line: «are not events» wording | not raised | N-1 (precision) | agree |
| DATA | n ≤ 100: 0 violations; CYC 3 actual Case-2 switches with y on c's cycle, all with top c | full corpus + 20,000 random runs: 0 violations; OS 852,572 checks, 4 «new top» configurations (ret22_n40 + start), none at an actual switch | consistent. My count is over actual Case-2 steps; REFEREE-2's OS is over all eligible z. Neither shows a wrong actual step |

## 2. Joint gap map
- Packet items to sign: no open gap. G-SRC-1 (inherited from [SET]) is CLOSED by ONE-STEP, which is signed by both referees (REFEREE-2 as
  author, mine in R-N5-SETTLE Addendum 1). Nothing FALSE.
- Line, REQUIRED: SRC-L1 (|F|), SRC-L2 (H_k / σ_(k+1) in the R57 gloss), SRC-L3 (cite ONE-STEP in the proof note, referee-originated, L41).
- Line, precision: name V; REFEREE-2's N-1 («not source events»).

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: SRC is signed by both referees; G-SRC-1 is one gap found by both and closed by ONE-STEP; the line needs SRC-L1, L2, L3.
- NEEDS: Lead: SRC L-2 with SRC-L1..L3, for successor 21 to word-diff.

## Part 2: successor 21's concurrent §C (claude/referee 957c3e90, written 23:11-23:13Z by date -u without sight of Part 1)
- Two REFEREE sessions wrote this §C concurrently: successor 20 (Part 1, 9d67aa1e, 23:13Z) and successor 21 (Part 2). Both are kept, nothing was rewritten. The verdicts agree item by item: every item SIGNED by both referees, G-SRC-1 CLOSED by ONE-STEP, SRC-L1/L2/L3 REQUIRED, the data reconciled the same way.

Referee: REFEREE (successor 21), Opus 5.5 (D15). Written from 23:11Z (2026-10-30, by date -u).
- My report is R-N5-SRC.md (claude/referee 81f6b89c), with R-N5-SETTLE.md Addendum 1 (8951ef7c). Both were written by successor 20
  before it opened any docs/referee-2/ file on SRC.
- The Lead's brief (23:11Z) gave the §C word and named R2-N5-SRC.md @ e8c1b62d (169 lines). I read it after both of my reports were on
  origin. REFEREE-2 24's own §C (R2-N5-SRC-C, referee-2 824651dd) was not opened before this section was written (§5).
- Object: docs/red/P-N5-SRC.md @ l-red 0521fb82, sha1 3caae56e3afdfaab80739c0e12e397b3d6cc7a8b. Both reports re-hashed it and agree.
- Scope (D1): a REDUCTION and an EQUIVALENCE inside W-runs of N5. Nothing is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.

### 1. Cross-map
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

### 2. Data reconciliation (G-SRC-1's configuration)
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

### 3. Joint gap map
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

### 4. Line revision L-2 (l-red 77a6d979, docs/red/P-N5-SRC-line-L2.txt, sha1 9fcb57903ad64a0ab7f56acb2f651f354b3616fc)
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

### 5. After writing §1-§4: REFEREE-2 24's §C (R2-N5-SRC-C, claude/referee-2 824651dd)
- Opened after §1-§4 were written (2026-10-30 23:12Z by date -u). Its C.1, C.3 and C.4 agree with my §1, §3 and §2 item by item.
- Its two open points are now settled:
  - «REFEREE's verdict on my ONE-STEP is pending». That verdict is SIGNED, in R-N5-SETTLE.md Addendum 1 (8951ef7c, 22:47Z). So each repair
    of G-SRC-1 (my four-way split, REFEREE-2's ONE-STEP) is signed by the other referee. G-SRC-1 is CLOSED, and the joint gap map is EMPTY
    of open gaps.
  - «SRC-L3: Lead decides». I upgrade SRC-L3 to REQUIRED (§1), so the two referees now agree that it is REQUIRED. No ruling is needed.
- Its precision note on my (ii)-(iv): «b's path is disjoint from c's arc from c to y». I accept it. ONE-STEP (β) states the step, and my
  Addendum 1 relies on ONE-STEP.
- It says V is bound fleet-wide by TARGET.md l. 8. I agree: my «V» item is optional.

### DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  1. SRC: both referees SIGN every item. G-SRC-1 was found by both and is closed by Lemma ONE-STEP, which is now double-signed. The joint gap
     map is empty of open gaps.
  2. Line: the REQUIRED changes are SRC-L1, SRC-L2 and SRC-L3. L-2 MATCHES the first two; SRC-L3 is pending in L-3.
  3. The configuration counts are reconciled: they count different predicates, and there is no disagreement.
- NEEDS: Lead: the SRC L-3 SHA, for the word-diff.

## Line revision L-3 (l-red 564bef5a, docs/red/P-N5-SRC-line-L3.txt, sha1 5736d8ab828d8244c6466abbc08d4fa8d8c03b41; fixes sha1 f8d54eec…) (successor 21, 23:37Z by date -u)
- Word-diff against L-2 (9fcb5790). The changed tokens:
  - «n := |V|,» → «n := |V| (V the vertex set of the game),» (my precision item);
  - inserted into the source-block proof note, after «restricted to Even vertices outside C,»: «with Case 2 and Case 2b's comparison step
    by (Lemma ONE-STEP, REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE, claude/referee 8951ef7c), which closes
    gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c),» (SRC-L3);
  - the scope tail gains «; Lemma ONE-STEP is referee-originated» (L41);
  - the source note changes «entries 1-2» → «entries 1-3».
  Nothing else changed.
- Strict symbol test on the new tokens:
  - V is bound.
  - «Case 2», «Case 2b» are the cited RUN-SETTLE induction's cases, bound by the citation.
  - ONE-STEP and G-SRC-1 are pinned (SHA and section), and every cited SHA is on origin: e8c1b62d (referee-2), 8951ef7c and 81f6b89c
    (referee); is-ancestor checked.
  - No free symbol.
- L41: the line cites both signatures (author REFEREE-2 e8c1b62d; REFEREE 8951ef7c), and the scope tail says it is referee-originated. ✓
- Precision (optional): «by (Lemma ONE-STEP, …)» reads better as «by Lemma ONE-STEP (…)».
- Verdict on L-3: MATCHES SRC-L1, SRC-L2, SRC-L3 and N-1 (Opus 5.5, D15). No REQUIRED change remains on the SRC line.

## §9. Line revision L-4 (l-red 1edc2f0e, docs/red/P-N5-SRC-line-L4.txt, sha1 ec2c713989eb3075060247b714eb49a5b2abf875; fixes entry 4) (successor 21, 03:54Z 2026-10-31 by date -u)
- (1) The word-diff against L-3 (5736d8ab, which I MATCHED in 8a1ba423) is exactly the Lead's and fixes entry 4's list, and nothing else:
  - «line L-2, l-si 86becaa0)» → «R96)»;
  - «source), and» → «source); DATA: they»;
  - «W-run: pins» → «W-run (pins»;
  - «cn3_n9;» → «cn3_n9);»;
  - «1-3)» → «1-4)».
  The sha1 is re-hashed and matches.
- (2) The R96 citation is correct.
  - docs/RESULTS.md l. 7748 at trunk 38bb8320 (an ancestor of origin trunk) is «### R96 [refereed-only] …», P-N5-SETTLE, CHECKER PASS C106.
  - Its line is SETTLE L-5 (l-si ce7bdc3b), which I MATCHED (R-N5-SETTLE-C §8).
  - It contains everything the SRC proof note uses: Claim RG′, the RUN-SETTLE induction («induction on k − k0 with a least-ℓ violator»),
    its Cases 2 and 2b via Lemma ONE-STEP, and ARENA-MAX and T54 as used.
  - The proof note keeps the l-si 6a70a520 packet pin, so the cited proof text is still fixed.
  - The note's own ONE-STEP / G-SRC-1 citation now repeats R96's. It is redundant but consistent, with the same SHAs.
- (3) The DATA relabel is correct.
  - «not source events (unless they change Ξ at a source)» is definitional, so it stays a statement. A source event is defined by Ξ
    changing at some v ∈ S_k. A σ̄-change at o, or a switch at c ∈ C, is not itself a Ξ change, although o and c are in S_k. So such a
    transition is a source event exactly when Ξ changes at some source.
  - «not O(1) per W-run» is an empirical observation on the pins xcn4_n12 and cn3_n9. It is not proved in the packet (R-N5-SRC §6-7: «not
    signed»). DATA is the right label.
  - «they» refers back to the three kinds of change just named.
- Strict symbol test on the new tokens: R96 is a landed RESULTS label; «DATA» is the fleet's label. No free symbol.
- Verdict on L-4: MATCHES (Opus 5.5, D15).

## §10. Line revision L-5 (l-red a5340f2d, docs/red/P-N5-SRC-line-L5.txt, sha1 2b39581d367687ec41067d690e448541f2ac7678; fixes entry 5, E5.1) (successor 21, 05:09Z 2026-10-31 by date -u)
- Correction to §9 (my miss). I passed L-4's «DATA: they are not O(1) per W-run (pins xcn4_n12, cn3_n9)». REFEREE-2 (claude/referee-2
  5e81fc5c, R2-N5-SRC-L4.md §(3), SRC-L5) is right: «not O(1)» is an asymptotic statement over a family, and two fixed games cannot
  witness it, even as DATA. I know its point only from the Lead's 05:09Z relay; I did not open R2-N5-SRC-L4.md.
- Word-diff against L-4 (ec2c7139). Exactly the Lead's list, and nothing else:
  - «are not O(1) per» → «repeat within one»;
  - «(pins xcn4_n12, cn3_n9);» → «(xcn4_n12: 4 σ̄-flips at one own Ξ-cycle node; cn3_n9: 3 switches at one c ∈ C);»;
  - «1-4)» → «1-5)».
  The sha1 is re-hashed and matches.
- Counts, re-run with my own engine (docs/referee/scratch/src_l5_counts.py, `python3 -I`, rl_engine; inputs from a detached worktree of
  a5340f2d; start files used; sha1 xcn4_n12.pg e43dc878…, cn3_n9.pg 0d5eb838…, the same as in R-N5-SRC §7):
  - xcn4_n12: one W-run (0, 4), |F| 4, C = {0}. σ̄ changes at Odd 0 (its own Ξ-cycle node) at 4 transitions. XCN {0: 4}, CN {} ✓.
  - cn3_n9: one W-run (0, 3), |F| 3, C = {1}. Even 1 ∈ C switches at all 3 transitions. CN {1: 3}, XCN {} ✓.
  Both equal L-RED's figures (xcn.py --all, n5b).
- The new clause is a finite, checkable observation on two named games, so the DATA label fits it. «repeat within one W-run» is literally
  true: 4 > 1 and 3 > 1 changes in one W-run.
- Strict symbol test: σ̄, «own Ξ-cycle node» (used earlier in the same clause), c and C are bound in the line. No free symbol.
- Verdict on L-5: MATCHES (Opus 5.5, D15).
