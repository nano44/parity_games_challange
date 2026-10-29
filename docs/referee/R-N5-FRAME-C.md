# R-N5-FRAME §C: joint map with REFEREE-2 on packet P-N5-FRAME (and, later, the fixes file and H0)
Written 2026-10-29T21:52Z by date -u, on the Lead's word of 21:48Z, by REFEREE successor 18, Opus 5.5 (D15). Every verdict is labelled (Opus 5.5, D15).
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

## 4. Fixes file and H0
PENDING: the Lead will send the SHA of docs/new/P-N5-FRAME-fixes-box65.md (H0 corrected line; H1-H6 for FR-N1..N6; H7-H16 for N-FR-1..10).

## DONE / FINDINGS / NEEDS
- DONE: this §C; scratch/frame_q.py (Q instance reproduced).
- FINDINGS: verdicts identical, packet map empty. E-item on the RESULTS line: Q undefined (REFEREE-2's catch; my "MATCHES" withdrawn on that
  point; Q = 0 reading false on mk_6_24, reproduced). NM^U definition recommended.
- NEEDS: Lead: the fixes-file SHA (H0-H16) for §4.
