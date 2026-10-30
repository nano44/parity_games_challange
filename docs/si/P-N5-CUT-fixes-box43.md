# P-N5-CUT fixes (box 43): answers to REFEREE 19 (CUT-N1..N7) and REFEREE-2 21 (N-CUT-1..10, §8 Addendum on the RESULTS line)
L-SI successor 31 (Opus 5.5; D15 / D18, Lead reading L40). Object: docs/si/P-N5-CUT-box43.md, FROZEN at l-si 2678f6c6, sha1
d6519d3d72d67d25bafd21b7034092eaa4315457 (unchanged; this file never edits it). Reports: docs/referee/R-N5-CUT.md (origin/claude/referee
ff5a6f81), docs/referee-2/R2-N5-CUT.md (origin/claude/referee-2 335814dc). Both: every PROVED item SIGNED, no gap, nothing FALSE.
Every item below is a CLARIFICATION or a READING unless marked "to sign"; no signed statement of the packet changes.

## K0. The corrected RESULTS line (REQUIRED items of REFEREE-2 §8; REFEREE §10's list)
Proposed line (replaces the 00:56Z proposal at docs/agents/P-N5-CUT-line-proposal.md):
«N5 on EVERY game, under the standing SPEC premise of RESULTS R57 (S1's procedure realises the optimal counterstrategy): T ≤ 2n(n−1) +
(n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1), where T is the number of transitions
(iterations) of the run, n = |V|, m_E the number of edges leaving Even vertices, λ-runs and λ^U-runs are as in RESULTS R86, W-runs as in
RESULTS R89 and late adoptions as in RESULTS R88 / R89; B* := the largest number of transitions inside one λ-run that are Even S4c
fallbacks or change τ; REP* := the largest number of REPEAT late adoptions (a second or later late adoption of the same Even edge) inside
one W-run; SC* := the largest number, over λ-runs R, of re-entries of Even edges in R of class S (W-silent) or C (own-cycle) of
P-N5-CUT §4 (W read against τ_{j−1}, smallest anchor); O* := the largest number of τ-changing transitions inside one λ^U-run (Theorem
CUT-RED, via Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT (first late adoptions ≤ m_E per W-run, R*_T ≤ m_E + REP_F), WV-R and Corollary
CUT-CHARGE); so T is polynomial if and only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1) — a REDUCTION
(none of B*, REP*, SC*, O* is bounded here; CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32); not M3, not a step-4 pass, not a
TARGET.md claim; G-N5-TIME stays open)»
- Changes from the 00:56Z text: the standing premise named; T, n, m_E defined; citations for λ-run / λ^U-run (R86), W-run (R89), late
  adoption (R88 / R89); SC* defined by §4's classes with the frame and the smallest anchor; "iff" now backed by K1; REP-LIN DEAD stated.

## K1. Converse of CUT-POLY (to sign; REFEREE-2 §8 gave it and signs it as stated there)
- Statement. For every run: B* ≤ T, O* ≤ T, REP* ≤ n·T, SC* ≤ n·T. So T ≤ q(n) implies all four ≤ n·q(n).
- Proof. B* and O* count transitions of the run. A late adoption is a switch of one Even vertex at one transition, so a transition holds at
  most |V_Even| ≤ n of them (REP* ≤ n·T). A re-entry of an Even edge is a switch of one Even vertex at one transition (SC* ≤ n·T). □

## K2. Standing premise (CUT-N1; N-CUT-2)
- OPT-OFF (i) uses: S4a's σ_new is the pointwise optimum of the one-player arena A = G_{τ*}|H_t and its values are those of the
  (σ_new, τ*)-plays. That is RESULTS R17 (a) (F1) on A with R57 (a) (VJ: S1's Ξ is VJ00's Ω), under the standing SPEC premise of R57 /
  R51 (d) (1E-N3: S1's procedure realises the optimal counterstrategy). Every later item uses OPT-OFF (i), so the whole packet carries this
  premise, as R88's W-MON and R89's ODD-FREEZE do (R89 FR-N1 / H1).
- G-N5T-1 (code = SPEC) is used only by §9's DATA, by no proof (REFEREE-2 §8; agreed).

## K3. Citations (N-CUT-1)
- [DO], [GPR], [SR-λ]: read "RESULTS R89 (landed, RESULTS 4d85668e)" for "R89 draft". The quoted lines are those of the frozen P-N5-FRAME at
  l-new 938d8796, unchanged.

## K4. OPT-OFF (ii), first bullet (N-CUT-3; CUT-N2)
- Add: if v lies on its own W-cycle below the top c, "σ′v's play avoids v" is false; the identity W(v) = ext(v, W(σ′v)) still holds, since
  v is less relevant than c (in no P-set) and ℓ adds 1, and ext preserves and reflects ⊴ between the valuations compared there.
- The ext step uses injective rewards (SPEC S1: distinct vertices have distinct relevance) and the top-dominance of signed weights (RESULTS
  R84 (a) Fact DELTA). In Case 3, "as in Case 1" means the triple identity W″(v) = ext(v, W(y)) (y's play contains v there; the literal
  "plays avoid v" is not needed).

## K5. §0 table wording (N-CUT-4)
- Read §0's §6 row as: «a REPEAT needs a W-rise of z, or is W-silent, or y is its own cycle node on the interval». The body (§6 (ii)) is the
  signed form; any RESULTS wording of LATE-SPLIT uses the body's form.

## K6. §8 READING note on [P-REP] (CUT-N3; N-CUT-5)
- Replace «[P-REP]: CONJECTURE REP-LIN (REP_F ≤ n)» by: «REP-LIN is DEAD (L-RED R128; also L-SI box 46, docs/si/N5-SUB-box46.md:
  latew_K20_m32, 570 > n = 538 REPEATs in one W-run). [P-REP] (REP* ≤ p(n), any polynomial) is OPEN and not implied by the packet.»

## K7. CUT-POLY's polynomial (N-CUT-6; CUT-N5)
- "T ≤ q(n)" uses m_E ≤ n² (E ⊆ V × V). The order "about n²·m_E·p·n³m_E p" is an upper estimate; the leading term is n²·m_E·(B* + 1)·K ≈
  n²·m_E·p·n³(m_E + p) (REFEREE's form). Neither changes the statement.

## K8. Frame (N-CUT-7)
- Agreed: every W* in §3-§5, including W*_j, is read against τ* = τ_{j−1}. K0's SC* definition says so.

## K9. FRESH-SPLIT's LATE (N-CUT-8)
- Agreed: the conclusion is "BLOCKED at j − 2 for τ*" (R88's sense with τ_{j−2} = τ*). It is a late adoption in R89's W-run sense only if
  j − 2, j − 1, j lie in one W-run (no λ_W change, τ_j = τ*). §5 claims no more; §8 does not use §5.

## K10. Names (CUT-N4; N-CUT-9)
- Rename §6's per-W-run classes SIL_F / CYC_F to SIL^REP_F / CYC^REP_F. SIL_R / CYC_R (§4, the ones SC* sums) keep their names. §8 uses
  only §4's.

## K11. Data notes (CUT-N6, CUT-N7, N-CUT-10)
- CUT-N7: thanks; with the S3 start the referee reproduces every §9 count. The pins use the S3 start except where a .start is passed.
- CUT-N6 / N-CUT-10: no REPEAT that is W-silent or own-cycle occurs in any corpus (sbcg, pins, red/, hntop, latew, random). The corrected
  form of LATE-SPLIT (ii) is required by the proof, not by data. N-CUT-10's question ("is every REPEAT W-paid?") is recorded as an open
  CONJECTURE of the lane (REP-WPAID), not used anywhere.

## DONE / FINDINGS / NEEDS
- DONE: K0-K11 (one REQUIRED line correction K0, one to-sign converse K1, clarifications K2-K11).
- FINDINGS: no gap; the line now defines every symbol and its "iff" rests on K1.
- NEEDS: none from the owner. Lead: route K0 / K1 to both referees for §C.

## K12. K0 with REFEREE 19's three optional precisions (R-N5-CUT-C.md §2: K0-P1, K0-P2, K0-P3) and nothing else (Lead 02:21Z)
Line:
«N5 (SPEC S1-S5) on EVERY game, under the standing SPEC premise of RESULTS R57 (S1's procedure realises the optimal counterstrategy), with RESULTS R15 (d), R17 (a) and R47 (a): T ≤ 2n(n−1) +
(n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1), where T is the number of transitions
(iterations) of the run, n = |V|, m_E the number of edges leaving Even vertices, λ-runs and λ^U-runs are as in RESULTS R86, W-runs as in
RESULTS R89 and late adoptions as in RESULTS R88 / R89; B* := the largest number of transitions inside one λ-run that are Even S4c
fallbacks or change τ; REP* := the largest number of REPEAT late adoptions (a second or later late adoption of the same Even edge) inside
one W-run; SC* := the largest number, over λ-runs R, of re-entries of Even edges in R of class S (W-silent) or C (own-cycle) of
P-N5-CUT §4 (W read against τ_{j−1}, smallest anchor); O* := the largest number of τ-changing transitions inside one λ^U-run (Theorem
CUT-RED, via Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT (first late adoptions ≤ m_E per W-run, R*_T ≤ m_E + REP_F; REP_F the REPEATs in F, R*_T as in R88), WV-R and Corollary
CUT-CHARGE); so T is polynomial if and only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1) — a REDUCTION
(none of B*, REP*, SC*, O* is bounded here; CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32); not M3, not a step-4 pass, not a
TARGET.md claim; G-N5-TIME stays open)»
- Word diff against K0 (git diff --no-index --word-diff=plain on the two lines, whitespace-normalised; [-removed-] {+added+}):
  - K0-P1: «N5 {+(SPEC S1-S5)+} on EVERY game»
  - K0-P3: «optimal [-counterstrategy):-] {+counterstrategy), with RESULTS R15 (d), R17 (a) and R47 (a):+}»
  - K0-P2: «R*_T ≤ m_E + [-REP_F),-] {+REP_F; REP_F the REPEATs in F, R*_T as in R88),+}»
- No other word changes. K0 itself (above) is unchanged; K12 supersedes it as the line to land.
