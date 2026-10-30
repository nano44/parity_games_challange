# R2-N5-CUT §C: REFEREE-2 comparison with REFEREE 19's CUT report; check of the fixes (K0-K11)
REFEREE-2 successor 21, Opus 5.5 (D15). Written 2026-10-30 from 02:06Z (date -u), on the Lead's word (02:00Z).
- Mine: docs/referee-2/R2-N5-CUT.md (report 7fd2aea8; §8 line addendum 335814dc).
- REFEREE's: docs/referee/R-N5-CUT.md at claude/referee 8a7818a0 (229 lines; = ff5a6f81 + the §10b line check, 38 added lines). Opened only
  after the word.
- Fixes: docs/si/P-N5-CUT-fixes-box43.md at l-si cc84e54c, sha1 ff9946215da949f49057fc939292b3e668e646cb (measured; = the Lead's).
- Packet: unchanged, d6519d3d.

## C.1 Verdict map
| item | REFEREE 19 | REFEREE-2 21 | joint |
| --- | --- | --- | --- |
| §1 setting, Fact B, quotes | CHECKED (13/13 by fragments) | well formed (10 strict + 3 faithful elisions) | agree |
| OPT-OFF (i) | SIGNED (CUT-N1 premise) | SIGNED (N-CUT-2 premise) | SIGNED by both |
| OPT-OFF (ii) | SIGNED (Cases 1-3 re-derived) | SIGNED (Cases 1-3 re-derived) | SIGNED by both |
| W-MON′ | SIGNED | SIGNED | SIGNED by both |
| W-SUCC | SIGNED | SIGNED | SIGNED by both |
| W-RETURN-G | SIGNED | SIGNED | SIGNED by both |
| CUT-CHARGE (+ Remark) | SIGNED | SIGNED | SIGNED by both |
| FRESH-SPLIT (+ ENT bound) | SIGNED | SIGNED | SIGNED by both |
| LATE-SPLIT (i)-(iii), Consequence, R*-REP | SIGNED | SIGNED | SIGNED by both |
| WV-R | SIGNED | SIGNED | SIGNED by both |
| Theorem CUT-RED | SIGNED | SIGNED | SIGNED by both |
| Corollary CUT-POLY | SIGNED as implication | SIGNED as implication | SIGNED by both |
| §8 notes, §9 DATA | not signed; [P-REP] note stale; pins exact | not signed; REP-LIN note stale; pins exact | agree |
| RESULTS line (00:56Z proposal) | NOT YET: CUT-E1 (SC*), CUT-E2 ("iff"), T, m_E, re-entry, W missing | NOT landable: SC* REQUIRED, citations, "iff"; T, m_E | agree; same two E-items, found independently |

**Joint gap map: EMPTY.** Every item is signed by both referees; neither lists a gap.

**The Lead's context points, both referees:**
- REP* is a premise; no proof step uses a bound on REP; REP-LIN is dead and appears only in the unsigned §8 notes.
- LATE-SPLIT carries the corrected form.
- OPT-OFF (i) carries the R57 standing premise; G-N5T-1 is used by DATA only.

## C.2 Notes cross-map
| REFEREE | REFEREE-2 | status |
| --- | --- | --- |
| CUT-N1 (premise: F1 + VJ; G-N5T-1 for DATA) | N-CUT-2; §8 addendum (premise; G-N5T-1 not used by proofs) | agree (K2) |
| CUT-N2 (ext uses injective rewards + DELTA; Case 3 "plays avoid v" not literal) | N-CUT-3 (first bullet false for v on its cycle) | agree; REFEREE adds the Case 3 instance of the same wording point (K4) |
| CUT-N3 (REP-LIN DEAD) | N-CUT-5 | agree (K6) |
| CUT-N4 (SIL/CYC name clash) | N-CUT-9 | agree (K10) |
| CUT-N5 (CUT-POLY's "about" order overestimates) | not raised | accepted; I missed it (K7) |
| CUT-N6 (LATE-SPLIT's off-cycle premise never bites) | N-CUT-10 (no own-cycle or W-silent REPEAT) | agree, found independently (K11) |
| CUT-N7 (DATA reproduced with S3) | §4.2 (DATA reproduced with S3) | agree, identical counts: 11,669; F 557 / FR 6,031 / C 4 / P 5,035 / S 42; LATE 313; late 1,141 / REPEAT 41 |
| — | N-CUT-1 (cite R89 as landed) | REFEREE-2 only (K3) |
| — | N-CUT-4 (§0 table omits own-cycle) | REFEREE-2 only (K5) |
| — | N-CUT-6 (m_E ≤ n²) | REFEREE states it in its §8 text (K7) |
| — | N-CUT-7 (τ* frame), N-CUT-8 (FRESH-LATE vs W-run) | REFEREE-2 only (K8, K9) |
| CUT-E1, CUT-E2 | §8: SC* REQUIRED, "iff" | identical findings (K0, K1) |
| MUT 2 (anchor across a cut: 313 violations) | X_WRG_cut (472 on sbcg) | the same control, both bite |

## C.3 K0, word by word (the corrected line)
Against Theorem CUT-RED, §4 and §8, with the symbol lists of REFEREE §10b and my §8:
| symbol / clause in K0 | packet | verdict |
| --- | --- | --- |
| «under the standing SPEC premise of RESULTS R57 (S1's procedure realises the optimal counterstrategy)» | K2; my N-CUT-2 | ✓ |
| formula «T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*)» | §8 (1 + B* + B* = 1 + 2B*) | ✓ |
| «K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1)» | §8 K(n, m_E, REP*) | ✓ |
| «T is the number of transitions (iterations) of the run, n = \|V\|, m_E the number of edges leaving Even vertices» | §1 | ✓ (was missing) |
| «λ-runs and λ^U-runs are as in RESULTS R86, W-runs as in RESULTS R89 and late adoptions as in RESULTS R88 / R89» | §1 [R86], [GPR] | ✓ (was missing) |
| B* «transitions inside one λ-run that are Even S4c fallbacks or change τ» | §8 B* (boundaries inside R) | ✓ |
| REP* «REPEAT late adoptions (a second or later late adoption of the same Even edge) inside one W-run» | §6, §8 | ✓ |
| SC* «re-entries of Even edges in R of class S (W-silent) or C (own-cycle) of P-N5-CUT §4 (W read against τ_{j−1}, smallest anchor)» | §4 classes S, C; §8 SC* | ✓ **E1 discharged.** It names §4's classes, the frame τ_{j−1} and the smallest anchor. Re-entry, anchor, piece and W^τ are defined in the packet's §1 / §4, which the line now cites by section (as R88's line cites N5-FRZ-box29 §0) |
| O* «τ-changing transitions inside one λ^U-run» | §8 O* | ✓ |
| «via … LATE-SPLIT (first late adoptions ≤ m_E per W-run, R*_T ≤ m_E + REP_F) …» | §6 (i), R*-REP | ✓ |
| «so T is polynomial if and only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1)» | CUT-POLY + K1 | ✓ **E2 discharged** (K1 signed below) |
| scope: REDUCTION; none bounded; REP-LIN DEAD (R128, latew_K20_m32); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME open | §8, R128 | ✓ |
- The line claims nothing beyond §2-§8 + K1. Every symbol is defined in the line or carried by a cited landed entry or by the cited packet
  section.
- Optional precision, not required: "W" inside "W-silent" is defined by the cited §4 / §1 (W^τ_t), and "polynomial" means "bounded by a
  polynomial in n on every run of every game", as in CUT-POLY.
- **K0 MATCHES.** My REQUIRED items (SC*, citations, "iff") and REFEREE's (CUT-E1, CUT-E2, T, m_E, re-entry, W) are all met.

## C.4 K1 (the converse): SIGNED (Opus 5.5, D15)
For every run:
- B* ≤ T and O* ≤ T: they count transitions of the run.
- REP* ≤ n·T: a late adoption is one Even vertex switching at one transition, so a transition carries at most |V_Even| ≤ n of them.
- SC* ≤ n·T: a re-entry of an Even edge (v, c) is v switching to c at one transition, so at most one per (transition, Even vertex).
Hence T ≤ q(n) on every run of every game gives all four ≤ n·q(n). ✓ This is the statement I gave in my §8 and REFEREE gave as CUT-E2: SIGNED
as written in K1.

## C.5 K2-K11: clarification or widening?
| item | kind | check |
| --- | --- | --- |
| K2 premise named (F1 + VJ under R57's standing premise; G-N5T-1 DATA only) | clarification | ✓ |
| K3 cite R89 as landed | clarification (citation) | ✓ |
| K4 OPT-OFF (ii) first bullet and Case 3 wording | clarification of the proof text; the statement is unchanged | ✓ |
| K5 §0 table row read with own-cycle | clarification (the summary is aligned with the signed body; no statement widened) | ✓ |
| K6 [P-REP] note: REP-LIN dead | clarification of a READING; cites docs/si/N5-SUB-box46.md as a second source (not opened by me; R128 suffices) | ✓ |
| K7 m_E ≤ n²; order estimate | clarification | ✓ |
| K8 frame τ_{j−1} | clarification | ✓ |
| K9 FRESH-LATE vs W-run late adoption | READING that claims no more than §5 ("only if": a necessary condition, not signed) | ✓ |
| K10 rename SIL_F / CYC_F → SIL^REP_F / CYC^REP_F | clarification (names) | ✓ |
| K11 data notes; CONJECTURE REP-WPAID recorded as open, unsigned | clarification; the conjecture would be a WIDENING if ever claimed, and it is correctly labelled open | ✓ |
None widens a signed statement.

## C.6 DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  - Verdicts identical; joint gap map EMPTY.
  - The same two line E-items were found independently. K0 discharges both and MATCHES §2-§8 + K1.
  - K1 SIGNED.
  - K2-K11 are clarifications or readings; none widens.
- NEEDS: Lead: K0 is landable as written (with K1). GAP §C after REFEREE 19's GAP report.
- K12 (l-si fd1cb0bc, fixes sha1 95584f7e…, +19/−0 over cc84e54c): K12 = K0 + P1-P3 exactly (difflib on the «…» line: «(SPEC S1-S5)»; «, with RESULTS R15 (d), R17 (a) and R47 (a):»; «; REP_F the REPEATs in F, R*_T as in R88),»); MATCHES. (2026-10-30 02:4xZ by date -u)
