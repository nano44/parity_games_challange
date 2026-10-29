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
