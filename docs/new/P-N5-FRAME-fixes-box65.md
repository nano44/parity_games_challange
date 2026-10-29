# P-N5-FRAME fixes (box 65): answers to REFEREE 18 (FR-N1..N6) and REFEREE-2 21 (N-FR-1..10); APPEND-ONLY
L-NEW successor 35 (Opus 5.5), D14 / D18. Lead 2026-10-29 21:48Z: «P-N5-FRAME is SIGNED IN FULL by both referees, with no gap … Please create
docs/new/P-N5-FRAME-fixes-box65.md. Append-only; the packet stays frozen.» Written from 21:50Z (date -u).
- Packet: docs/new/P-N5-FRAME-box65.md, FROZEN at l-new 938d8796, sha1 ce8c4803ee18dc90ee761863d006d0aca0476542 (unchanged; re-measured).
- Reports: REFEREE 18, referee e9b32f72, docs/referee/R-N5-FRAME.md; REFEREE-2 21, referee-2 7571febe, docs/referee-2/R2-N5-FRAME.md.
- Status: H0 is the one REQUIRED correction (of the RESULTS line, not of the packet). H1-H16 are clarifications. Every sharpening below is
  a READING, not a widening, unless both referees sign it. No signed statement of the packet changes.

## H0 (REQUIRED; REFEREE-2 N-FR-7 / §5; the Lead's 20:47Z approval missed it): the RESULTS line defines Q and NM^U_R(e)
- Defect: in the approved line (P-N5-FRAME-box65-line.txt, sha1 acf3234f…) Q is undefined. Read as "any Q under its bound", Q = 0 makes
  the line FALSE: REFEREE-2 §5, mk_6_24, one τ-stretch with |S| = 162 > 148 = Q + (Q + 1)((n − 1)(R*_S + 1) + FL_S) at Q = 0, R*_S = FL_S = 0.
  The true Q there is 162 (every transition changes λ_W), within the packet's bound.
- Corrected line: docs/new/P-N5-FRAME-box65-line-H0.txt = the approved line with exactly two insertions (the Lead's 21:48Z wording):
  - (i) after «every τ-stretch S has at most Q + (Q + 1)((n − 1)(R*_S + 1) + FL_S) transitions, » insert «where Q := the transitions of S
    that are an S4c fallback or change λ_W, and »;
  - (ii) after «PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e)» insert « (NM^U_R(e) := the carries of U(e) in R, read with G^d's parities,
    RESULTS R86 (e) F3)».
- Measured: `git diff --no-index --word-diff` of the two files shows exactly these two insertions and nothing else (2567 → 2729 bytes).
- Word-by-word check against the packet:
  - (i) against §3.5's proof, first bullet: «Q := the transitions of S that are a fallback or change λ_W». In the packet "fallback" is the S4c
    fallback ([S4c], §1). Same set, same name. The remaining text of the clause («Q ≤ fb_S + n(n − 1)(fb_S + 1), fb_S ≤ …, with fb_S its S4c
    fallbacks, R*_S …, FL_S …, ρ_S …») is unchanged and matches §3.5's displayed bound and definitions.
  - (ii) against §2.5 (e) and premises [R85c] / [R86e]: (e) bounds PCH^U_R(e) by (n²/2)(NM^U_R(e) + 1) + NM^U_R(e); [R85c] glosses NM as
    «v's carries» (R86 (e), l. 5350-5351); [R86e] reads NM^U «with G^d's parities (F3)». The inserted definition says exactly that, for e
    on one λ^U-run R.
- So the corrected line claims nothing beyond §2-§3, and every symbol in it is now defined there or in the cited RESULTS items.

## Answers to REFEREE 18 (docs/referee/R-N5-FRAME.md §8)
- H1 (FR-N1, standing premise). ODD-FREEZE's third proof step uses two facts about τ̄ := τ̄(τ), both from [S1-dual] / [S1-Xi] read on G^d:
  τ̄ is the G^d-Odd player's optimal counterstrategy to τ AT EVERY VERTEX AT ONCE, and U is REALISED by it, i.e. U(v) is the triple of the
  (τ, τ̄)-play from v. This is RESULTS R57 (b)'s premise, mirrored on G^d (as in P-N5-SF fixes F7). The packet uses both: "U(e) (the
  (τ, τ̄)-play from e)" and "U(τ(o)) = π_o" are the realisation; "at least as good for Even as the (τ, σ_e)-play" is the optimality.
- H2 (FR-N2, (H2)). Agreed: (H2) is used by the proof (the play decomposition P_e · π_o and the disjointness w ∉ P_e). Its necessity is
  not exhibited (REFEREE MUT 2: 0; REFEREE-2 X_OF_noH2 = 0, see H10). As with GATE-SHUT (RESULTS R85, MPGS J1), it stays as a hypothesis.
  Nothing changes.
- H3 (FR-N3, Even fallbacks). Every S4c transition inside a τ-stretch is an EVEN fallback: S4c's Odd branch sets τ_new(v) to an improving
  w ≠ τ(v) ([S4c], [S2]), so it changes τ and ends the stretch. That is what lets [R56], which counts Even in-phase fallbacks, bound fb_S
  in §3.5. (REFEREE-2 N-FR-5 says the same.)
- H4 (FR-N4, NM^U parities). Covered by H0 (ii).
- H5 (FR-N5, the Consequence's parenthetical). Agreed. RISE_F(z) over a W-run F that meets several λ-runs is the sum of RISE over its
  λ-run pieces PLUS at most n(n − 1) λ_Ξ-changing transitions ([R47a]). The parenthetical omits that additive term. The Consequence
  ("polynomial in n, m_E and the largest PCH_R(z)") is unaffected: the term is polynomial.
- H6 (FR-N6, GP*-RUN's inherited hypotheses). GP*-RUN inherits R88's FINAL (G12) hypotheses verbatim, read on the W-run F = [a, b]:
  a path r = (x = r_0, …, r_L = u) of G_τ (Odd r_i: r_{i+1} = τ(r_i)), simple, with L ≤ k − a edges, ending at a W-cycle node u of F's
  first state a (λ_W(u) = u), none of whose Even edges (r_i, r_{i+1}) is blocked at state k − 1 − i; and FW-R* with R*_T counted on F.
  §3.3's "verbatim, with F in place of the frozen W-phase" means exactly these, as R88's object §3 (l. 86-87) states them; the RESULTS R88
  line (G12) carries the same three («simple path r of G_τ (Odd steps follow τ) with at most k − a edges», «a W-cycle node u of F's first
  state a (λ_W(u) = u)»).

## Answers to REFEREE-2 21 (docs/referee-2/R2-N5-FRAME.md §6)
- H7 (N-FR-1). Accepted with thanks. [R86e] is displayed in RESULTS: in R86's headline and in body (e), l. 5345-5357. The brief's (and my
  packet's) "not a displayed RESULTS statement" was inaccurate. The per-vertex λ^U-run form IS the premise, since [MΦ] is per vertex.
- H8 (N-FR-2, citation). ODD-FREEZE's step "τ̄ maximises G's order for Even among plays (τ, α) from e" is [S1-Xi]'s «minimising … at every
  vertex at once» on G^d, i.e. RESULTS R57 (a) (VJ) on G^d, the citation RESULTS R85's Fact B2 uses for the same step. Read §2.3's third
  bullet with that citation added (together with H1's realisation premise).
- H9 (N-FR-3, (H1′) as a path condition). READING: (H1′) ⇔ there is a simple path from e to o in G_τ (Odd vertices other than o follow τ;
  Even vertices free). (⇒) The (τ, σ_e)-play up to o is such a path. (⇐) Given the path, let σ_e follow it on its Even vertices and equal
  τ̄ elsewhere; the play from e follows the path to o and never meets a vertex off it. REFEREE-2's brute force (OFBF, n ≤ 7-8) agrees. Not
  a change to the signed statement.
- H10 (N-FR-4, (H2) never needed). Noted: X_OF_noH2 = 0 on every run state and on every τ of 1,650 small games (27,435 τ). CONJECTURE (OPEN,
  REFEREE-2's): ODD-FREEZE holds without (H2). Not needed for any signature; see H2.
- H11 (N-FR-5). Agreed (= H3): the phases meeting S lie inside S by maximality (τ is part of a phase's key), and an in-S fallback is Even
  and either λ_Ξ-changing or in-phase.
- H12 (N-FR-6, looseness). READING: the proof of §3.5 gives |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S (FL_S counts W-flat transitions of all
  of S once). The stated bound multiplies FL_S by Q + 1 and is implied. REFEREE-2's data: the sharper form never fails (SR1_sharp_fails 0).
  The signed statement and the RESULTS line keep the stated (weaker) form.
- H13 (N-FR-7). = H0.
- H14 (N-FR-8, SUCC-MON strict). READING: at every transition where σ(y) changes, Ξ_{t+1}(σ_{t+1} y) ▷ Ξ_t(σ_t y) strictly. The last chain
  of §3.1's proof is ⊵ followed by ▷. Not signed as a separate item.
- H15 (N-FR-9). Agreed: in COMPOSE-FREEZE (b), 1 + RISE ≤ 1 + PCH + (PCH + 1)(n − 1), and 1 + PCH + (PCH + 1)(n − 1) = n(PCH + 1) is an
  identity, so the second "≤" is "=".
- H16 (N-FR-10, DATA). Correction to §4's DATA attribution: freeze2.py's 81 ODD-FREEZE hits on dw_3 cover states 0-40; over all 42 states
  REFEREE-2 counts 84. DATA only, not signed; the pinned check.sh line ("states 42 hyp-hits 81") stays as the tool's own count.

## DONE / FINDINGS / NEEDS
- DONE: this file; docs/new/P-N5-FRAME-box65-line-H0.txt (corrected RESULTS line).
- FINDINGS: one required line fix (Q and NM^U_R(e) defined); 16 clarifications; no signed statement changes; the packet stays frozen.
- NEEDS: none from the owner.
