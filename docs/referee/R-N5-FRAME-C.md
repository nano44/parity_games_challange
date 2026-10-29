# R-N5-FRAME §C: joint map with REFEREE-2 on packet P-N5-FRAME (and, later, the fixes file and H0)
Written 2026-10-29T21:49Z by date -u, on the Lead's word of 21:48Z, by REFEREE successor 18, Opus 5.5 (D15). Every verdict is labelled (Opus 5.5, D15).
- My report: docs/referee/R-N5-FRAME.md (e9b32f72). REFEREE-2's: docs/referee-2/R2-N5-FRAME.md at referee-2 7571febe (sha1 4baf8c60…), read only
  after the Lead's word (my report pushed first). Independence clean on both sides; no shared code (mine frame_probe.py on rl_engine).

## 1. Verdict tables, row by row
| item | REFEREE (e9b32f72) | REFEREE-2 (7571febe) | joint |
| --- | --- | --- | --- |
| §1 setting, quotes | CHECKED (8/8 SPEC quotes + R85 (c) verbatim, own script) | well formed, 9/9 quotes verbatim (own fquote.py) | same |
| 2.1 FRAME-τ | SIGNED | SIGNED | SIGNED |
| 2.2 DUAL-ORDER | SIGNED | SIGNED | SIGNED |
| 2.3 ODD-FREEZE | SIGNED (all directions; premise FR-N1) | SIGNED (all directions; R57 (a) on G^d, N-FR-2) | SIGNED |
| 2.4 ENT-FREEZE | SIGNED | SIGNED | SIGNED |
| 2.5 COMPOSE-FREEZE (a)-(e) | SIGNED; [R86e] suffices (per vertex, λ^U-run, G^d parities) | SIGNED; [R86e] accepted as a displayed premise (N-FR-1) | SIGNED |
| 3.1 SUCC-MON | SIGNED | SIGNED (strict at every σ(y)-change, N-FR-8) | SIGNED |
| 3.2 LATE-RISE | SIGNED | SIGNED | SIGNED |
| 3.3 GP*-RUN | SIGNED (no step uses σ̄, D, λ_Ξ) | SIGNED (same check) | SIGNED |
| 3.4 R*-RISE | SIGNED | SIGNED | SIGNED |
| 3.5 STRETCH-RED + Consequence | SIGNED | SIGNED | SIGNED |
| RESULTS line (acf3234f) | "MATCHES" | MATCHES in content, but Q undefined (REQUIRED) and NM^U undefined (precision) (N-FR-7) | DOES NOT MATCH as worded: E-item (below) |
- VERDICTS IDENTICAL on every packet item; no gap; nothing FALSE in the packet. JOINT GAP MAP (packet): EMPTY.

## 2. The E-item: Q in the RESULTS line — I AGREE, and correct my own verdict
- The line reads «every τ-stretch S has at most Q + (Q + 1)((n − 1)(R*_S + 1) + FL_S) transitions, Q ≤ fb_S + n(n − 1)(fb_S + 1), fb_S ≤ …, with
  fb_S its S4c fallbacks, R*_S …, FL_S …, and ρ_S …». Q is never defined there (the packet defines it in the proof: «Q := the transitions of S
  that are a fallback or change λ_W»). My report's §6 listed "every symbol (fb_S, R*_S, FL_S, ρ_S) ✓" and missed Q: my "MATCHES" was WRONG on
  this point. Withdrawn: the line as worded does NOT match.
- Why it matters: with Q free, the clause can be read with any Q under its bound, e.g. Q = 0, i.e. |S| ≤ (n − 1)(R*_S + 1) + FL_S. That is FALSE.
  Reproduced with my own engine (scratch/frame_q.py on rl_engine; mk_6_24.pg sha1 d94fee47…, its .start 6acdeabc…, copied from l-new 938d8796):
  one τ-stretch [0, 162], |S| = 162, Q = 162 (every transition changes λ_W; so every W-run is a single state and R*_S = 0), fb_S = 0, FL_S = 0,
  n = 150: the Q = 0 reading demands 162 ≤ 149. (REFEREE-2 gives n 149 and 162 > 148 on the same file; my parser counts 150 vertices; the
  conclusion is the same.) The true Q = 162 satisfies the packet's bound 162 ≤ 0 + n(n − 1).
- E-ITEM (joint, required): the line must define Q := the transitions of S that are an S4c fallback or change λ_W (L-NEW's H0, as the Lead
  describes it). Precision (joint, recommended; my FR-N4 = REFEREE-2's second half of N-FR-7): define NM^U_R(e) (carries of e in R, read on G^d
  with G^d's parities, R86 (e) F3).

## 3. Notes, paired
| note | REFEREE | REFEREE-2 | class |
| --- | --- | --- | --- |
| Q undefined in the line | — (missed) | N-FR-7 (required) | E-ITEM (§2) |
| NM^U definition in the line | FR-N4 (optional) | N-FR-7 (precision) | recommended, in H0 |
| τ̄ optimal at every vertex and realising U (direction 2 of ODD-FREEZE) | FR-N1 (R57 (b) mirrored) | N-FR-2 (R57 (a) (VJ) on G^d, R85 Fact B2) | clarification; both premises named = complete |
| (H2) never bites | FR-N2 (MUT 2: 0) | N-FR-4 (X_OF_noH2 = 0 everywhere, also under every τ) | clarification (data); (H2) stays, it is used |
| in-stretch fallbacks are Even; phases lie inside S | FR-N3 | N-FR-5 | clarification |
| Consequence parenthetical omits the n(n − 1) λ-change term | FR-N5 | — | clarification (harmless) |
| GP*-RUN should name the R88 (G12) hypotheses it inherits | FR-N6 | — | clarification |
| [R86e] stands as a displayed premise | §3 (per-vertex argument) | N-FR-1 | agree |
| (H1′) ⇔ a simple G_τ path from e to o with Even free | (my probe uses exactly this) | N-FR-3 | agree (simplification) |
| STRETCH-RED with FL_S added once | (§5: "double-counted at worst") | N-FR-6 | agree: Σ over W-runs of their W-flat transitions ≤ FL_S, so |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S holds; a strengthening, not needed |
| SUCC-MON strict at every σ(y)-change | (the chain ends with ▷) | N-FR-8 | agree (strengthening) |
| COMPOSE-FREEZE (b) second step is an identity | (§3 "=") | N-FR-9 | agree |
| dw_3: 84 ODD-FREEZE hits over 42 states (the lane's 81 are states 0-40) | — | N-FR-10 | DATA |
- Data agree: 0 violations in both controls; (H3)'s two parts bite in both; (H2) never bites in either; GP*'s blocked condition bites
  (mine MUT 4 on ccl_w48_n48; REFEREE-2 GPall on sbcg). mk_4_16's τ-stretch of 76 is reproduced by both.

## 4. Fixes file and H0 (addendum written 2026-10-29T22:08Z by date -u, on the Lead's 21:56Z message)
Objects (measured at l-new d3d98d1c): fixes file docs/new/P-N5-FRAME-fixes-box65.md sha1 b1127e579c48d4bc1213b13d21b213113bbd18d3; corrected line
docs/new/P-N5-FRAME-box65-line-H0.txt sha1 ab1ee38a45f0637216de2287c3020165cdd542f0; packet unchanged (ce8c4803). All = the Lead's figures.
- H0, character diff (difflib, own script) against the approved line acf3234f: EXACTLY two insertions, nothing else changed:
  (i) «where Q := the transitions of S that are an S4c fallback or change λ_W, and » after «… + FL_S) transitions, »;
  (ii) « (NM^U_R(e) := the carries of U(e) in R, read with G^d's parities, RESULTS R86 (e) F3)» after «PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e)».
- Word by word: (i) = §3.5's proof «Q := the transitions of S that are a fallback or change λ_W», "fallback" being the S4c fallback of [S4c]
  (§1): same set. The clause now reads «at most Q + (Q + 1)(…) transitions, where Q := …, and Q ≤ fb_S + n(n − 1)(fb_S + 1), fb_S ≤ …»: Q is
  bound, and the Q = 0 misreading (mk_6_24) is gone. (ii) = §2.5 (e) with [R85c]'s «v's carries» and [R86e]'s F3 «read with G^d's parities»,
  for e on one λ^U-run R. ✓
- H0 DISCHARGES THE E-ITEM. With it the line matches §2-§3 and every symbol is defined in the line or in the RESULTS items it cites.
- H-items:
  | item | answers | verdict | class |
  | --- | --- | --- | --- |
  | H0 | N-FR-7 / §2 E-item, FR-N4 | correct (above) | REQUIRED line correction, discharged |
  | H1 | FR-N1 | both facts named (optimality at every vertex; realisation of U by τ̄), R57 (b) mirrored | CLARIFICATION |
  | H2 | FR-N2 | (H2) stays; necessity not exhibited | CLARIFICATION |
  | H3 | FR-N3 | in-stretch S4c transitions are Even fallbacks (an Odd one changes τ) | CLARIFICATION |
  | H4 | FR-N4 | = H0 (ii) | CLARIFICATION |
  | H5 | FR-N5 | the n(n − 1) λ_Ξ-change term added to the parenthetical; Consequence unaffected | CLARIFICATION |
  | H6 | FR-N6 | names R88's G12 hypotheses (G_τ, ≤ k − a edges, W-cycle node of F's first state); matches R88's line | CLARIFICATION |
  | H7 | N-FR-1 | [R86e] is displayed; per-vertex form is the premise | CLARIFICATION (agrees with my §3) |
  | H8 | N-FR-2 | R57 (a) (VJ) on G^d cited with H1 | CLARIFICATION |
  | H9 | N-FR-3 | (H1′) ⇔ a simple G_τ path e → o (Even free); both directions correct (my probe uses this form) | READING, an equivalent reformulation, not a widening |
  | H10 | N-FR-4 | ODD-FREEZE without (H2): CONJECTURE (OPEN) | not claimed; no change |
  | H11 | N-FR-5 | = H3 | CLARIFICATION |
  | H12 | N-FR-6 | sharper |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S | READING (a true strengthening, §3; NOT part of the signed statement or the line, correctly) |
  | H13 | N-FR-7 | = H0 | — |
  | H14 | N-FR-8 | strict SUCC-MON at σ(y)-changes | READING (a true strengthening; not signed separately, correctly) |
  | H15 | N-FR-9 | the second ≤ of COMPOSE-FREEZE (b) is = | CLARIFICATION |
  | H16 | N-FR-10 | dw_3: 84 hits over 42 states; pinned line keeps the tool's 81 | DATA |
- No H-item widens a signed statement. H12 and H14 are strengthenings recorded as READINGs (both true); H9 is an equivalence. The fixes
  file's header claim («H1-H16 are clarifications … Every sharpening below is a READING, not a widening») is CONFIRMED.
- Nothing open on P-N5-FRAME.

## DONE / FINDINGS / NEEDS
- DONE: this §C; scratch/frame_q.py (Q instance reproduced).
- FINDINGS: verdicts identical, packet map empty. E-item on the RESULTS line: Q undefined (REFEREE-2's catch; my "MATCHES" withdrawn on that
  point; Q = 0 reading false on mk_6_24, reproduced). NM^U definition recommended.
- NEEDS: none (§4 addendum: H0 discharges the E-item; H1-H16 clarifications / READINGs / DATA).
