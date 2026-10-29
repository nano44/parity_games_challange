# N5-ODD (box 33): Odd's re-entries on plain N5 in R86 COMPOSE's terms
L-SI successor 29 (Opus 5.5), D15 / D18, Lead reading L40. Lead's brief 2026-10-29 19:31Z (BOX 33 (a)-(c)). Written from 19:40Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Read: RESULTS R86 (COMPOSE; signed items (a)-(e)), R85 (MATCHED / CARRY, MATCH-Φ); L-NEW box 63 (docs/new/N5-FREEZE-box63.md, l-new),
  box 62 §5-§6 (FRAME-τ, FRAME-STRETCH); L-RED R111 (dual runs are mirrors), R109 / R106 (hntop / runquad families).
- Engine: L-NEW's box21/n5x.trace (plain N5, read only). U_t, τ̄_t := Even's optimal counter to τ_t on G^d (R86's U). Carries are read on
  G^d (R86 F3). Tool: experiments/si/odd/reent.py; outputs experiments/si/odd/out/; pinned in experiments/si/check.sh «box 33».
- Notation. An ENTRY of Odd o into e: a transition r → r+1 with τ_r(o) ≠ e = τ_{r+1}(o). A RE-ENTRY: an entry into an e that o held
  before; s < r is the transition at which o last left e. Its WINDOW: the transitions t ∈ [s, r − 1]. The CHARGE of a change of U(e) at t:
  LAM (cycle node changes), CAR (a carry: P changes, not MATCHED), MAT (matched P-change), LEN (length only). A re-entry's charge class is
  the strongest kind in its window (LAM > CAR > MAT > LEN). PROTECTED at state r: box 63's H1, H2, H3 at r (exact H1 form).
  Unprotected classes: X (H1 fails: e's play never returns to o), Y (H1 holds, H2 fails), Z (H1, H2 hold, H3 fails).

## 1. (a) What an unprotected re-entry is in R86's terms
- Lemma RE-CHARGE (PROVED, lane; R86 (a) SW-RETURN on the Odd side, signed, plus box 63's ODD-FREEZE):
  - Every re-entry of o into e has a change of U(e) in its window. For a fixed pair (o, e), different re-entries use disjoint windows.
  - So for every stretch R: ENT_R(o, e) ≤ 1 + RISE^U_R(e). An edge (o, e) that is protected at every state of the run has no entry at
    all (ODD-FREEZE).
  - Proof. SW-RETURN's chain is U_{r}(e) ▷ U_r(τ_r o) ⊵ U_{s+1}(τ_{s+1} o) ⊵ U_s(τ_{s+1} o) ▷ U_s(e). So U(e) changes between s and r.
    This is R86 (a)'s proof verbatim on G^d. The second sentence is box 63 §1. □
- The exact correspondence asked for: a re-entry is charged to a RISE of the OPTION's valuation U(e), not of o's.
  - Inside a λ^U-run that rise is a carry, a matched P-change or a length-only change of U(e). Across runs it can be a λ^U-change.
  - So a re-entry is a carry exactly when its window contains a carry of U(e) and no λ^U(e)-change.
  - Several Odd vertices that share an option e are charged to the same rises of U(e). That is R86's m_O factor.
- DEAD: "every unprotected re-entry is charged to a carry of U(e)".
  - Kill: d_runquad_K2_m30 (n 120, dual of mkr.py 2 30). 61 of its 90 re-entries have no carry and no λ^U(e)-change in the window; all
    their U(e)-changes are MATCHED.
  - The same holds on every runquad K: 247 of 450 at K = 8.
- DEAD: CONJECTURE ENT-NM, "ENT_R(o, e) ≤ 1 + NM^U_R(e) per λ^U-run".
  - Kill: d_runquad_K3_m30, λ^U-run [0, 99], o = 42, e = 43: 3 entries, NM^U(e) = 1.
  - It fails on every runquad K ≥ 3, and in 8 corpus games.
- DEAD: CONJECTURE ENT-PCH, "ENT_R(o, e) ≤ 1 + PCH^U_R(e)". It would drop LEN-MONO's factor n.
  - Kill: lev74_n40 (red/fbr, S3 start), run [0, 18], o = 6, e = 0: 2 entries, PCH^U(e) = 0. Also nep87_n40 and nep92_n40.
  - In all three the re-entry is charged to length only.
- Lemma LEN-REENTRY (PROVED, lane). Suppose a re-entry's window has no λ^U(e)-change and no P-change of U(e). Then on [s, r] the choice
  value V_t := U_t(τ_t o) has the same (cycle node, P) as U_s(e).
  - So o ping-pongs between options that tie on (c, P), and only lengths decide.
  - Proof. V is non-decreasing (Ξ-SUCC on G^d, R86 (a)'s proof). V_s = U_s(e) and V_r ◁ U_r(e), and U_r(e) has U_s(e)'s (c, P).
    The order key on (c, P) is injective (rewards and P-weights are injective), and S1's order compares (c, P) before length. So the
    sandwich fixes V's (c, P). □
- Corollary LEN-COUNT (PROVED, lane; same argument).
  - At every re-entry V rises strictly: V_{r+1} = U_{r+1}(e) ⊵ U_r(e) ▷ V_r.
  - Inside a stretch where V's (c, P) is constant, a rise is a strict length move in one direction. The (c, P)-key of V is monotone, so
    each class is one contiguous stretch.
  - Hence #LEN-charged re-entries of o ≤ (n − 1)·(1 + #(c, P)-changes of V along the run).
- DATA (corpus box59/sbcg.lst, 719 games, S3; 1684 re-entries, equal to box 63's 1684 returns):
  - Charge classes: LAM 1403, CAR 171, MAT 70, LEN 40. Protection classes: X 1349, Y 122, Z 213.
  - PROT_V 0 (no protected re-entry) and SWR_V 0 (no window without a U(e)-change).
  - LEN-REENTRY: 0 violations on the 40 LEN re-entries (25 games). The MUT control flips the test and fires (lev74_n40: LENTIE_V 1).
- Composes toward G-N5-TIME (one line): τ-changes ≤ n(n − 1) + Σ_{λ^U-runs R} Σ_{(o,e) not always protected} (1 + RISE^U_R(e)) ≤
  n(n − 1) + (n(n − 1) + 1)·n·m_O^u·(P*^U + 1), with m_O^u the Odd edges that are unprotected at some state.
  - This is the Odd half of R86 (d), with ODD-FREEZE removing the always-protected edges.

## 2. (b) The mirror of ODD-FREEZE in R86's terms
- Lemma GAP (PROVED, lane; box 63's proof read as an equivalence). Suppose H1 and H2 hold for (o, e) at state t, with f := τ_t(o) and w
  the cycle node of f's play. Then:
  - U_t(e) and U_t(f) have the same cycle node w.
  - P(U_t e) = P(U_t f) ⊎ D_t, with D_t := the vertices of P_e more relevant than w (disjoint by H2).
  - ℓ(U_t e) = ℓ(U_t f) + |P_e|.
  - So (o, e) ∈ Iτ_t iff the top of D_t has odd priority in G (H3 fails with D_t ≠ ∅), or D_t = ∅ and the length term favours Odd.
- Consequence (PROVED, lane). Take a stretch where H1 and H2 hold and D_t is fixed. Then every change of U(e) is a COPY of a change of
  U(f): the same cycle node and the same P-difference. MATCHED depends only on A ∖ B, B ∖ A and the cycle node's rank, so it also has
  the same carry status.
  - Protection therefore excludes NO carry. It turns e's carries into copies of f's carries, and those cannot change whether (o, e) is
    improving.
  - A re-entry needs a non-copy event in its window: D changes (σ̄ or τ along P_e moves), or H1 or H2 fails (class X or Y).
- No bound on NM*^U for any class from this:
  - NM^U is a property of vertices' valuations, and protection is a property of edges.
  - On the dualised families the carries sit on class-X options (e's play leaves o's orbit), where U(e) and U(o) are unrelated.
  - The only class with a bound is box 63's "every non-final option protected": τ changes ≤ m_O there, and NM^U is irrelevant.
- DATA: copies are 537 of 6323 window changes on d_hntop_n8 (8.5%) and 0 on every runquad. Class X is 3073 of 3276 re-entries on
  d_hntop_n8 and 450 of 450 on d_runquad_K8.
- Composes (one line): nothing beyond §1's m_O^u. The Odd side of G-N5-TIME stays exactly R86's Odd problem, i.e. bounding NM*^U.

## 3. (c) The dualised families (DATA; regenerated with L-RED's own generators, pins reproduced: d_hntop_n8 23964cf1 / de02eb95,
## d_runquad_K8_m30 f9baf3f5)
| family (param) | n | N5 iter = τ-changes | λ^U-runs | re-entries | Odd vertices re-entering | max per Odd o | max per (o, e) | NM^U max (per vertex per λ^U-run) | charges LAM / CAR / MAT / LEN | classes X / Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| d_hntop N = 2 | 42 | 33 | 5 | 84 | 18 | 9 | 6 | 13 | 37 / 47 / 0 / 0 | 82 / 2 |
| N = 3 | 63 | 61 | 5 | 251 | 29 | 22 | 13 | 28 | 67 / 184 / 0 / 0 | 248 / 3 |
| N = 4 | 84 | 95 | 5 | 532 | 40 | 39 | 22 | 47 | 102 / 430 / 0 / 0 | 523 / 9 |
| N = 5 | 105 | 135 | 5 | 951 | 51 | 60 | 33 | 70 | 143 / 808 / 0 / 0 | 925 / 26 |
| N = 6 | 126 | 181 | 5 | 1532 | 62 | 85 | 46 | 97 | 190 / 1342 / 0 / 0 | 1472 / 60 |
| N = 8 | 168 | 291 | 5 | 3276 | 84 | 147 | 78 | 163 | 302 / 2974 / 0 / 0 | 3073 / 203 |
| d_runquad K = 2 (m 30) | 120 | 66 | 2 | 90 | 30 | 3 | 2 | 2 | 0 / 29 / 61 / 0 | 90 / 0 |
| K = 3 | 132 | 99 | 2 | 150 | 30 | 5 | 3 | 3 | 0 / 58 / 92 / 0 | 150 / 0 |
| K = 4 | 144 | 132 | 2 | 210 | 30 | 7 | 4 | 4 | 0 / 87 / 123 / 0 | 210 / 0 |
| K = 6 | 168 | 198 | 2 | 330 | 30 | 11 | 6 | 6 | 0 / 145 / 185 / 0 | 330 / 0 |
| K = 8 | 192 | 264 | 2 | 450 | 30 | 15 | 8 | 8 | 0 / 203 / 247 / 0 | 450 / 0 |
- Exact fits on these points (DATA; the hntop N = 7 point was not run):
  - d_hntop (n = 21N): τ-changes = 3N² + 13N − 5 (R109); re-entries = 4N³ + 21N² − 14N − 4; per Odd o ≤ 2N² + 3N − 5; per (o, e)
    ≤ N² + 2N − 2; NM^U = 2N² + 5N − 5 (R111's figure).
  - d_runquad (m = 30): τ-changes = 33K; re-entries = 30(2K − 1); per o = 2K − 1; per (o, e) = K = NM^U.
- Growth (READING): per Odd vertex, unprotected re-entries grow quadratically in the family parameter (Θ(n²) in the game size for
  hntop), and in total cubically. That is polynomial, and it tracks NM^U. Re-entries exceed τ-changes because N5 switches many Odd
  vertices in one iteration.
- 0 protected re-entries in all 11 (ODD-FREEZE). The data matches R111: the Odd side of these families is the Even side of R109 / R106
  mirrored.

## 4. Composition toward G-N5-TIME (implication, PROVED lane, conditional on CONJECTURE FRAME-STRETCH)
- Statement. If FRAME-STRETCH holds (#σ-changes < (n + m)(#τ-changes + 1)), then:
  - T ≤ (n + m + 1)(τch + 1), because every transition changes σ or τ ([STEP]).
  - τch ≤ n(n − 1) + (n(n − 1) + 1)·n·m_O·(P*^U + 1), the Odd half of R86 (d). Every τ-changing transition either changes λ^U
    (≤ n(n − 1), R47 (a) Φ (c)) or holds an Odd switch inside one λ^U-run (R86 (c) on G^d).
  - With R85 / R86 (e): P*^U ≤ (n²/2)(NM*^U + 1) + NM*^U.
- So FRAME-STRETCH + a polynomial bound on Odd's carries NM*^U alone gives G-N5-TIME. Even's NM* drops out.
- §1 sharpens m_O to m_O^u, the edges that are not always protected.
- Honest limits:
  - FRAME-STRETCH is a CONJECTURE (L-NEW 35 is proving it).
  - NM*^U is not bounded by anything here. On the dualised families it is Θ(n²) per vertex per λ^U-run (polynomial).
  - Protection gives no carry bound (§2).

## DONE / FINDINGS / NEEDS
- DONE: experiments/si/odd/reent.py; inst/ (d_hntop N = 2..6, 8; d_runquad K = 2, 3, 4, 6, 8, regenerated, pins reproduced);
  out/reent_fam.txt, reent_corpus.txt (719), reent_len.txt; sbcg.lst (copy of L-NEW's box59 list); check.sh «box 33»; this note.
- FINDINGS:
  1. PROVED (lane) RE-CHARGE: a re-entry is a rise of the option's U(e); always-protected edges never re-enter.
  2. DEAD: re-entry ⇒ carry (d_runquad_K2_m30); ENT-NM (d_runquad_K3_m30); ENT-PCH (lev74_n40).
  3. PROVED (lane) LEN-REENTRY and LEN-COUNT: a length-only re-entry is a ping-pong among options tying on (c, P).
  4. PROVED (lane) GAP: protection makes e's carries copies of f's; it excludes no carry and bounds no NM^U.
  5. DATA: §3 table and fits.
  6. Implication (PROVED lane, premise CONJECTURE FRAME-STRETCH): G-N5-TIME ⇐ FRAME-STRETCH + polynomial NM*^U.
- NEEDS: none from the owner.
