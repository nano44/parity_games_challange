# R2-N5-FRAME §C: REFEREE-2 comparison with REFEREE's FRAME report
REFEREE-2 successor 21, Opus 5.5 (D15). Written 2026-10-29 from 21:49Z (date -u), on the Lead's §C word (21:48Z).
- Mine: docs/referee-2/R2-N5-FRAME.md, pushed at 7571febe (21:44Z).
- REFEREE's: docs/referee/R-N5-FRAME.md at claude/referee e9b32f72 (152 lines; REFEREE successor 18), opened only after the word.
- Both review the same object: P-N5-FRAME-box65.md @ l-new 938d8796, sha1 ce8c4803; line acf3234f.

## C.1 Verdict map
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| §1 setting, premises | CHECKED (8/8 SPEC quotes) | well formed (9/9 quotes incl. [R85c]) | agree |
| 2.1 FRAME-τ | SIGNED | SIGNED | SIGNED by both |
| 2.2 DUAL-ORDER | SIGNED | SIGNED | SIGNED by both |
| 2.3 ODD-FREEZE | SIGNED (directions checked; FR-N1) | SIGNED (directions checked; N-FR-2) | SIGNED by both; directions identical (§C.2) |
| 2.4 ENT-FREEZE | SIGNED | SIGNED | SIGNED by both |
| 2.5 COMPOSE-FREEZE (a)-(d) | SIGNED | SIGNED | SIGNED by both |
| 2.5 COMPOSE-FREEZE (e) | SIGNED: [R86e] suffices | SIGNED: [R86e] accepted as premise, displayed in RESULTS | SIGNED by both; same reason (per-vertex MΦ, λ^U fixed, G^d parities) |
| 3.1 SUCC-MON | SIGNED | SIGNED | SIGNED by both |
| 3.2 LATE-RISE | SIGNED | SIGNED | SIGNED by both |
| 3.3 GP*-RUN | SIGNED (no σ̄, D, λ_Ξ in R88's proofs) | SIGNED (same line-by-line finding) | SIGNED by both |
| 3.4 R*-RISE | SIGNED | SIGNED | SIGNED by both |
| 3.5 STRETCH-RED | SIGNED (fallback count checked) | SIGNED (fallback count checked) | SIGNED by both; same argument |
| 3.5 Consequence | SIGNED | SIGNED | SIGNED by both |
| RESULTS line acf3234f | MATCHES; "every symbol (fb_S, R*_S, FL_S, ρ_S) ✓"; optional NM^U clause (FR-N4) | MATCHES in content; Q UNDEFINED (required fix); NM^U undefined (precision) | E1 (Q, mine; REFEREE missed it), E2 (NM^U, both). Lead accepted both (21:48Z) |
| §4 READING, DATA | not signed; pins reproduced exactly | not signed; pins reproduced (whole check.sh) | agree |

**Joint gap map: EMPTY.** No item is NOT SIGNED by either referee, and neither referee lists a gap.

## C.2 The Lead's four points, both referees
1. [R86e]: both accept it as the premise.
   - REFEREE §3: the per-vertex form on λ^U-runs "is exactly what was signed" (P*_R is the max of the per-vertex bound).
   - Mine §2.5 / N-FR-1 adds that RESULTS displays it, in R86's headline and in body (e).
   - Agree.
2. ODD-FREEZE directions: identical chains.
   - REFEREE: V ▷ U(τ(o)) (Direction 1); U(e) ⊵ V (Direction 2); then ◁_d.
   - Mine: steps 2, 3, 4.
   - Both name the optimality premise:
     - REFEREE FR-N1: τ̄ is the pointwise optimum AND realises U as the (τ, τ̄)-play values, R57 (b) mirrored.
     - Mine N-FR-2: R57 (a) (VJ) on G^d.
   - FR-N1 is the fuller statement, and I ACCEPT it. My checker tests its second half as UPLAY: U = my own play value of the (τ, τ̄)-plays,
     0 violations at every state.
3. STRETCH-RED's fallback count: identical argument. Every in-stretch S4c fallback is an Even fallback, the phases meeting S lie inside S, and
   fallbacks that keep λ_Ξ are in-phase. REFEREE FR-N3 asks the packet to say so; I agree (my §3.5 states it).
4. RESULTS line: see C.3.

## C.3 E-items (wording; no verdict changes)
- **E1 (REFEREE-2; required).** The line's STRETCH-RED clause uses Q without defining it.
  - Read as any Q under its bound, Q = 0 is FALSE on the lane's mkr family (mk_6_24 |S| 162 > 148; mk_8_32 280 > 196; mk_16_100 1648 > 497).
  - Fix: "Q := the transitions of S that are an S4c fallback or change λ_W".
  - REFEREE §6 lists STRETCH-RED's symbols as "every symbol (fb_S, R*_S, FL_S, ρ_S) ✓" and does not mention Q: a miss on that side.
  - The Lead accepted the fix (21:48Z; L-NEW fixes item H0).
- **E2 (both).** Define NM^U_R(e) in the line, read with G^d's parities (R86 (e) F3). REFEREE FR-N4 marks it optional; I mark it precision.
  Accepted by the Lead.

## C.4 Notes cross-map (for L-NEW's fixes file H1-H16)
| REFEREE | REFEREE-2 | status |
| --- | --- | --- |
| FR-N1 (τ̄ optimal and realising U; R57 (b) mirrored) | N-FR-2 (R57 (a) (VJ) on G^d) | agree; FR-N1 is the fuller form, accepted |
| FR-N2 ((H2) never needed; MUT 2 = 0) | N-FR-4 (X_OF_noH2 = 0 on run states and on every τ of 1,650 small games) | agree, found independently; open strengthening |
| FR-N3 (in-stretch fallbacks are Even) | §3.5 / N-FR-5 | agree |
| FR-N4 (NM^U clause in the line) | N-FR-7 second half | agree (E2) |
| FR-N5 (the Consequence's parenthetical omits the ≤ n(n − 1) λ-change term) | §3.5: I included the term and read "each λ-change is one transition" as covering it | agree; harmless |
| FR-N6 (GP*-RUN should name R88's inherited hypotheses: G_τ paths, ≤ k − a edges, W-cycle node of the W-run's first state) | not raised for the packet (I checked only that the line inherits R88's fixed line) | accepted; I missed it for the packet text |
| — | N-FR-1 (R86 (e) premise is displayed in RESULTS) | REFEREE-2 only; REFEREE §3 cites the same lines |
| — | N-FR-3 ((H1′) ⇔ a simple G_τ path from e to o; brute force agrees) | REFEREE-2 only; REFEREE's DFS uses the same reduction implicitly |
| — | N-FR-6 (STRETCH-RED with FL_S added once) | REFEREE-2 only; REFEREE §5 notes "double-counted at worst" |
| — | N-FR-7 first half (Q undefined) | E1, REFEREE-2 only |
| — | N-FR-8 (SUCC-MON strict at every σ(y)-change) | REFEREE-2 only; REFEREE adds that SUCC-MON = R86's Ξ-SUCC (signed) |
| — | N-FR-9 (COMPOSE-FREEZE (b)'s second inequality is an identity) | both state it |
| — | N-FR-10 (lane's 81 hits = states 0-40) | REFEREE-2 only; DATA |

## C.5 Data agreement
- Both reproduce the pinned blocks exactly: dw_3 81 hits; dw_3's W-run of 26 with 4 late adoptions; mk_4_16's 76-transition τ-stretch.
- Both find the widening exercised: REFEREE 224 W-runs with a σ̄-change and 10 with a λ_Ξ-change; mine 274 not-frozen W-runs on sbcg.
- Both see the (H3) controls bite and the (H2) control never bite.
- Max R*_T: REFEREE 11 (library, n ≤ 40); mine 17 (sbcg). Different corpora; both satisfy FW-R*.

## C.6 DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  - Verdicts identical (all ten items and the Consequence SIGNED by both). Joint gap map EMPTY.
  - E1: Q undefined in the line (mine, required; REFEREE missed it). E2: NM^U (both).
  - FR-N1 and FR-N6 accepted.
- NEEDS: Lead: send the SHA of L-NEW's fixes file and of the corrected line (H0); I will check H0 against E1/E2 and H7-H16 against
  N-FR-1..10.

## C.7 Addendum: fixes file and corrected line (Lead 21:56Z; written 22:0xZ by date -u)
Objects, measured with `git show d3d98d1c:<path> | sha1sum` (d3d98d1c is an ancestor of origin/claude/l-new):
- docs/new/P-N5-FRAME-fixes-box65.md: b1127e579c48d4bc1213b13d21b213113bbd18d3;
- docs/new/P-N5-FRAME-box65-line-H0.txt: ab1ee38a45f0637216de2287c3020165cdd542f0;
- the packet: still ce8c4803.
All three equal the Lead's figures.

**H0, word by word.** I diffed H0 against the approved line acf3234f by words (difflib). There are exactly two changes, and nothing else differs:
- (i) the insertion «where Q := the transitions of S that are an S4c fallback or change λ_W, and», right after «… + FL_S) transitions,» and
  before «Q ≤ fb_S + …»;
- (ii) «NM^U_R(e);» → «NM^U_R(e) (NM^U_R(e) := the carries of U(e) in R, read with G^d's parities, RESULTS R86 (e) F3);».
(i) is the packet's §3.5 definition («a fallback or change λ_W»; "fallback" is S4c's). (ii) is R86 (e)'s F3 reading.
**H0 discharges E1 and E2.** Every symbol in the line is now defined in it, in SPEC, or in the cited RESULTS items. It claims nothing beyond
§2-§3.

**Q = 0 counter-check, re-run on H0's reading** (logs/mkr_H0_recheck.txt: mk_4_16, mk_6_24, mk_8_32 with start files; mk_16_100 from
logs/mkr_big.txt). Under H0, Q is the actual count of fallback or λ_W-changing transitions of S.
| game | n | \|S\| | Q (H0) | R*_S | FL_S | H0's bound Q + (Q+1)((n−1)(R*_S+1)+FL_S) | Q's bound fb + n(n−1)(fb+1) | old Q = 0 reading |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mk_6_24 | 149 | 162 | 162 | 0 | 0 | 24,286 ✓ | 22,052 ✓ | 148 ✗ |
| mk_8_32 | 197 | 280 | 280 | 0 | 0 | 55,356 ✓ | 38,612 ✓ | 196 ✗ |
| mk_16_100 | 498 | 1,648 | 1,648 | 0 | 0 | 821,201 ✓ | 247,506 ✓ | 497 ✗ |
SR1/SR2/SR3 hold with 0 violations in the re-run (RESULT PASS). The Q = 0 reading still fails (X_SR_Q0 = 2 on mk_6_24 and mk_8_32), which is
why the definition is needed. H0 states the true reading.

**H-items: clarification or widening.**
| item | answers | kind | my check |
| --- | --- | --- | --- |
| H0 | E1 + E2 | correction of the RESULTS line (definitions added; nothing widened) | discharged (above) |
| H1 | FR-N1 | clarification (standing premise named: τ̄ optimal and realising U; R57 (b) mirrored) | ✓; my UPLAY check, 0 |
| H2 | FR-N2 | clarification ((H2) stays as a hypothesis) | ✓ |
| H3 | FR-N3 | clarification (in-stretch fallbacks are Even) | ✓ |
| H4 | FR-N4 | = H0 (ii) | ✓ |
| H5 | FR-N5 | clarification (the parenthetical gains the additive n(n − 1) term; the Consequence is unchanged) | ✓, = my §3.5 derivation |
| H6 | FR-N6 | clarification (R88's G12 hypotheses named; nothing new) | ✓, matches R88's object §3 l. 86-87 and the R88 line |
| H7 | N-FR-1 | clarification (record) | ✓ |
| H8 | N-FR-2 | clarification (citation R57 (a) (VJ) on G^d) | ✓ |
| H9 | N-FR-3 | READING, an equivalent restatement of (H1′) with both directions proved; neither a widening nor a narrowing | ✓; the (⇐) proof is correct (σ_e = the path on its Even vertices, τ̄ elsewhere) |
| H10 | N-FR-4 | CONJECTURE (ODD-FREEZE without (H2)): would be a WIDENING; correctly labelled OPEN and unsigned | ✓ |
| H11 | N-FR-5 | clarification (= H3) | ✓ |
| H12 | N-FR-6 | READING: a SHARPENING (stronger bound), proved by §3.5's own proof; kept unsigned, and the signed form is unchanged | ✓; I would sign it if offered (the proof gives it directly) |
| H13 | N-FR-7 | = H0 | ✓ |
| H14 | N-FR-8 | READING: a SHARPENING of SUCC-MON (strict at σ(y)-changes), proved by §3.1's own chain; unsigned | ✓ |
| H15 | N-FR-9 | clarification (an identity) | ✓ |
| H16 | N-FR-10 | DATA attribution: **WRONG, and the error is MINE (N-FR-10), copied by the lane** | see the correction below |

**Correction of my N-FR-10 (and so of H16).**
- I inferred that freeze2.py's 81 hits cover states 0-40 because my (H1′) count on states 0-40 is also 81. I had not read freeze2.py.
- Having read it now (938d8796:experiments/new/box59/freeze2.py l. 17-31): it loops over ALL states. It tests box 63's (H1) only, with
  σ_e = τ̄, P_e = the (τ, τ̄)-play from e cut at o, not the packet's (H1′).
- My own count (R2-N5-FRAME/h1count.py, dw_3, S3 start, uncapped):
  | | all 42 states | states 0-40 |
  | --- | --- | --- |
  | (H1) | **81** (= freeze2.py) | 78 |
  | (H1′) | 84 | 81 |
- So the lane's 81 is the (H1) count over all states. The equality with my (H1′) count on states 0-40 is a coincidence.
- Corrected N-FR-10: "freeze2.py counts box 63's (H1) (σ_e = τ̄) over all 42 states: 81; the packet's (H1′) gives 84 over all states (81 on
  0-40)."
- H16 should be replaced by that sentence (an append to the fixes file). DATA only: no verdict, no signed statement and no pinned check is
  affected. Also, the pinned line "box 63 ODD-FREEZE: dw_3 81 hypothesis hits" counts (H1) hits, a subset of the packet's protected edges,
  as box 63's name says.

**C.7 verdict.** The fixes file is accepted.
- H0 discharges E1 and E2.
- H1-H15 are clarifications, readings or sharpenings, as labelled. None widens a signed statement; H10 is a conjecture, correctly unsigned.
- H16 needs one correction (append), which comes from my own N-FR-10 error.
- H17 checked, verbatim (l-new 9631bbc5, fixes sha1 eb5bd5e1…, +4/−0 over d3d98d1c; whitespace-normalised equal to the §C.7 corrected N-FR-10 sentence); P-N5-FRAME closed at REFEREE-2 (2026-10-30 00:1xZ by date -u).
