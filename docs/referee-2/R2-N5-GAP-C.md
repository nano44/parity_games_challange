# R2-N5-GAP §C: REFEREE-2 comparison with REFEREE 19's GAP report; check of fixes H1-H9
REFEREE-2 successor 21, Opus 5.5 (D15). Written 2026-10-30 from 02:21Z (date -u), on the Lead's word (02:21Z).
- Mine: docs/referee-2/R2-N5-GAP.md (aee8971e).
- REFEREE's: docs/referee/R-N5-GAP.md at claude/referee cd1c29d6 (133 lines), opened only after the word.
- Fixes at l-new 15044625, measured with `git show 15044625:<path> | sha1sum`; both equal the Lead's:
  - docs/new/P-N5-GAP-fixes-box69.md: sha1 1e223dc2e08daf88ee40e46421f2d859889230a7;
  - docs/new/P-N5-GAP-box69-line-H9.txt: sha1 28b7e5506a5419181c9bca8b316694c3cd21ccb3.
- Packet unchanged: d67f8e04.

## C.1 Verdict map and joint gap map
| item | REFEREE 19 | REFEREE-2 21 | joint |
| --- | --- | --- | --- |
| §1 setting | CHECKED | well formed (11/11 quotes) | agree |
| XW | SIGNED (GAP-N1) | SIGNED (N-GAP-1) | SIGNED by both |
| W-MON | SIGNED | SIGNED | SIGNED by both |
| FB-W | SIGNED | SIGNED | SIGNED by both |
| OPT-OFF | statement TRUE; proof hole G-GAP-1 (Case 2 (ii) with u on π); SIGNED with its repair GAP-R1 | SIGNED with gap G-GAP-1 (Case 2 with u ∈ π); repair given | **SAME GAP, found independently**; same sub-case, same repair idea |
| W-SUCC | SIGNED (given OPT-OFF as repaired) | SIGNED (uses OPT-OFF's statement) | SIGNED by both |
| LATE-W | SIGNED (given OPT-OFF as repaired) | SIGNED | SIGNED by both |
| LATE-PIECE | SIGNED (the line's CL is a superset: bound stays true) | SIGNED (N-GAP-3: fix t′) | SIGNED by both |
| GAP-MON, SW-IN, REOPEN-W, REOPEN-CHARGE | SIGNED | SIGNED | SIGNED by both |
| Z-FLAT | SIGNED (GAP-N3: consequences) | SIGNED (N-GAP-5: consequences) | SIGNED by both; same note |
| Theorem GAP-RED | SIGNED (uses OPT-OFF nowhere) | SIGNED | SIGNED by both; I agree it does not use OPT-OFF |
| line 901f242d | MATCHES after GAP-L1..L3 (definitions) | MATCHES (precision: premise, CL) | agree; the precision items differ (C.4) |

**Joint gap map: one entry, G-GAP-1** (OPT-OFF, a proof step; the statement is true; found by both).
- Both repairs treat the configuration "v on u's cycle, c's play reaches u before v". REFEREE's GAP-R1 uses the triple identity v ⊕ Ω_ρ(c)
  in (2b)(ii); mine splits by the path to the cycle node. These are the same argument.
- Data on the sub-case: REFEREE 11,948 occurrences (11,781 with S′ = ∅) among 436,677 pairs; mine 17,139 / 15,355 (sbcg) and 8,907 / 6,957
  (one-player). Both: 0 violations of the statement.
- Status after the fixes: CLOSED by H1 (C.2).

## C.2 H1: does it close G-GAP-1? YES
I re-derived H1 case by case. It splits by the ρ-PATH from c to its own cycle node u_c.
- (1a) The path avoids v and v is not on u_c's cycle.
  - The whole play from c avoids v, so Ω_ρ′(v) = v ⊕ Ω_ρ(c).
  - Ω_ρ(v) = v ⊕ Ω_ρ(ρv) by [V1], whose path condition is exactly what [V2] needs (H3 folded in).
  - [V2] strict contradicts [F1]. ✓
- (1b) The path avoids v and v is on u_c's cycle. This is my u ∈ π case and REFEREE's (2b).
  - u = u_c, and v is below u.
  - ρv's path to u runs along the cycle, so its P-set is ∅.
  - c's path to u cannot contain a vertex of the arc u → v (it would then meet v before u). So Z = v, c's path, arc u → v is a simple cycle,
    and its vertices above u are exactly S.
  - S ≠ ∅: max S is even, by DELTA, and is Z's top. That contradicts [F1].
  - S = ∅: Z's top is u, and Ω_ρ′(v) = v ⊕ Ω_ρ(c) as triples. [V2] strict contradicts [F1]. ✓
- (2) The path visits v.
  - u_c = u, and π ∌ u.
  - π is disjoint from ρv's path to u. For v off the cycle: a common vertex would put c's play onto a play that avoids v. For v on the cycle:
    π's cycle vertices lie on the arc u → v, and ρv's path is the arc v → u.
  - So Ω_ρ(c) = (u, S ⊔ P(ρv), ℓ(ρv) + |π| + 1), Z = v, π ∌ u, and the packet's (i), (ii) hold verbatim. ✓
- The three cases are exhaustive and correct. The statement is unchanged. **G-GAP-1 CLOSED.**
- H1 also covers REFEREE's GAP-R1 ((2b)(ii) = (1b) with S = ∅).

## C.3 H2-H8: clarification only?
| item | answers | kind | check |
| --- | --- | --- | --- |
| H2 standing premise named (R57 (a) (VJ); R57's standing SPEC premise; G-N5T-1 used by no proof) | N-GAP-1 (= REFEREE GAP-N1) | clarification | ✓ |
| H3 "paths to the cycle node avoid v" | N-GAP-2 | clarification (proof wording; folded into H1 (1a)) | ✓ |
| H4 CL with t′ := the earliest blocked state of [s + 1, u] | N-GAP-3 | clarification (fixes a free choice; the proof works for any fixed choice) | ✓ |
| H5 §5 bullet: polynomial bounds give a polynomial form, not FB-LIN itself | N-GAP-4 | clarification (narrows an overstated READING; the theorem is unchanged) | ✓ |
| H6 Z-FLAT = consequences | N-GAP-5 (= REFEREE GAP-N3) | clarification | ✓ |
| H7 relation to P-N5-CUT | N-GAP-6 | clarification | ✓ |
| H8 comp54_n80 invalid start; corrected DATA | N-GAP-7 | DATA correction | ✓ (details below) |
None widens a signed statement.

**H8's corrected DATA against mine:**
- Non-edge: comp54_n80.pg line «11 134 1 11;»: vertex 11 is Odd with the single successor 11, and the start sets τ(11) = 51. ✓
- §6 / box 68: in-phase fallbacks 782, re-openings 8,442 (all with a W-rise), ZF 56. **Equal to mine** (logs/alt_all_startorS3.txt +
  logs/lane_dataset3_s.txt).
- box 67, alt_all only: 725 in-phase fallbacks. **Equal to mine** (logs/alt_all_startorS3.txt alone: inphase_fallbacks 725).
- The FBUP / SAUP energy figures and box 70's S 42 / C 4 are lane tools' counts I did not recompute. S 42 and C 4 equal my CUT-corpus counts
  (R2-N5-CUT §4.2).

## C.4 H9, word by word
- difflib word diff of H9 against the proposal f1c5c5d5 shows exactly the two stated changes and nothing else:
  - (i) «(SPEC S1-S5;» → «(SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum;
    for S4a, σ_new is the pointwise optimum of the one-player arena H_t);». This is H2. ✓
  - (ii) CL's gloss becomes «those, other than the first, whose window [s + 1, t′] — u → u + 1 the adoption, s → s + 1 the latest leave of c by
    v with s + 1 ≤ u, t′ the earliest state of [s + 1, u] at which (v, c) is blocked — contains some state at which v is its own W-cycle node».
    This is §3.2 with H4. It also restores "other than the first", which REFEREE noted the old gloss dropped. ✓
- H9 claims nothing beyond §2-§5 (+ H1 for the proof). It discharges both of my precision items.
- **Not yet in H9:** REFEREE's GAP-L1 (define Ξ_t := Ξ_{σ_t}), GAP-L2 (define "one-player game of Even, ρ pointwise optimal, Ω_ρ its
  valuation" in the OPT-OFF clause) and GAP-L3 (name R15 (a), (d), R17 (a), R57 (a), R21 (a), R38 (a), R88).
  - I agree with all three. GAP-L2 in particular: "an optimal strategy ρ of a one-player game" should say pointwise-optimal (R17 (a) F1's
    sense).
  - They are definitional, not E-items. I will word-diff the H10+ line when it comes.
- **Verdict on H9: MATCHES**, pending the H10+ definitions.

## C.5 DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  - The joint gap map has one entry, G-GAP-1, found independently by both referees, and H1 CLOSES it.
  - H2-H8 are clarifications or DATA corrections. H8's corrected counts (782 / 8,442 / 56; 725) equal mine.
  - H9 matches. REFEREE's GAP-L1..L3 are still to be added (H10+).
- NEEDS: Lead: send the H10+ line SHA for a word-diff check. The K12 word-diff for CUT also comes when ready.

## C.6 Addendum: complete fixes H1-H15 and line H14 (Lead 02:32Z; written 02:3xZ by date -u)
Objects, measured with `git show c1aa183d:<path> | sha1sum` (both equal the Lead's):
- docs/new/P-N5-GAP-fixes-box69.md: 955bcea2c5dae4c6016d5f9cfeaa8bae004587e0;
- docs/new/P-N5-GAP-box69-line-H14.txt: a9e8bcae1d6caec7cded179ead78f1cfedf756f9.
The fixes file is append-only: `git diff 15044625 c1aa183d` adds 38 lines (H10-H15) and deletes 0, so H1-H9 are as checked in C.2-C.4.
- **H1 closes G-GAP-1: YES** (C.2).
  - H10 maps REFEREE 19's GAP-R1 onto H1 correctly: (2b) u ∈ π = H1's (1b); (2a) = H1's Case 2; (2b)(i), (ii) = (1b) with S ≠ ∅, S = ∅.
  - The «|π| + 1 longer» clause is kept only for Case 2 = (2a), where it is true.
- **H8 / H15 DATA = mine** (782 / 8,442 / ZF 56; alt_all-only 725). C.3.
- **H2-H15: clarifications only.**
  - H10 is a correspondence between the two repairs.
  - H11 = H2 with REFEREE's wording (premise named).
  - H12 states [V2] as a statement about triples, which is how both referees used it. It is correct: equal cycle nodes, v in neither P-set,
    so the same term is added to both weights and 1 to both lengths; for different cycle nodes, the rewards are unchanged.
  - H13 = H6. H14 is the line. H15 = H8.
  - None widens a signed statement.
- **H14, word by word** (difflib):
  - Against H9: exactly three insertions/replacements and nothing else:
    - (L3 + L1) after the premise clause: «premises RESULTS R15 (a), (d), R17 (a) (F1) with R57 (a) (VJ), R21 (a), R38 (a), R88;
      Ξ_t := Ξ_{σ_t} (SPEC S1);»;
    - (L2) «an optimal strategy ρ of a one-player game has» → «for a one-player game of Even (Odd fixed), a pointwise-optimal Even strategy
      ρ (R17 (a) (F1)) with Ω_ρ its [S1-val] valuation has».
  - Against the original proposal f1c5c5d5: H9 (i) and (ii) plus these, nothing else.
  - The OPT-OFF clause now reads «for a one-player game of Even (Odd fixed), a pointwise-optimal Even strategy ρ … has Ω_ρ(c) ⊴ Ω_ρ(ρ(v)) for
    every edge (v, c) at every Even v that is not its own Ω_ρ-cycle node» = §2.4's statement. ✓
  - CL keeps «other than the first» (the packet's form). ✓
  - The premises named are those both referees used. The scope tail is unchanged.
  - **H14 MATCHES §1-§5 with H1-H13**; every symbol is defined or cited; it claims nothing beyond. Landable.
- Final: P-N5-GAP's only gap G-GAP-1 is CLOSED by H1, and H14 is the line to land.
- H16 line (l-new 996d9a57, sha1 e3a23a9a…): = H14 + GAP-L4 exactly (difflib: «H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t));», nothing else; = §1's PIECE / H_t definition); MATCHES. (2026-10-30 02:5xZ by date -u)
- **Lemma OPT-OFF (§2.4): SIGNED (Opus 5.5, D15)** — statement as in the packet, with the proof of fixes H1 (l-new 15044625 / c1aa183d), which closes G-GAP-1 (§C.2). REFEREE-2's signature table for P-N5-GAP is now: all 13 items SIGNED (XW, W-MON, FB-W, OPT-OFF with H1, W-SUCC, LATE-W, LATE-PIECE, GAP-MON, SW-IN, Z-FLAT, REOPEN-W + REOPEN-CHARGE, Theorem GAP-RED). Line H16 (sha1 e3a23a9a): MATCHES (see above).
- Strict symbol test of the WHOLE H16 line (l-new 996d9a57, sha1 e3a23a9a…; Lead 03:45Z; 2026-10-30 03:4xZ by date -u).
  - Bound: Ξ_t, W_t, Z_t, H_t (t a generic state); phase / in-phase; τ-fixed Even fallback; piece; blocked (R88); ρ, Ω_ρ, (v, c); [p, q];
    s, t′ («v leaves c at s → s + 1», «a later state t′»); Q, u, CL's window; WCH_Q(c); P, a («every phase P with first state a»); f_P, RO_P,
    WCH^S4a_P(v), ZF_P; Σ_v.
  - **DEFECT (k):** «Z_{k+1} ⊆ Z_k», «outside Z_k», «lies in Z_k», «Z_{k+1} = Z_k» (Z-FLAT and ZF_P) and «|Z_{k+1} ∖ Z_k|» (RO_P) use k, and
    no clause introduces it. This is the same kind of defect as CUT's F and j. The intended reading (k → k + 1 the transition in question) is
    unambiguous, but under the standing rule it must be bound.
    - Minimal edit, one insertion in the setting parenthetical, after «Z_t := … the gap set;»: «a transition is written k → k + 1 (states k,
      k + 1);».
    - Alternative: three local insertions: «at a τ-fixed Even fallback k → k + 1», «Σ over its in-phase S4a transitions k → k + 1», «its
      in-phase fallbacks k → k + 1 with».
    - The same global clause also binds the step index in «W does not fall at an S4a step (read with τ_t)» (step t → t + 1), a softer
      instance of the same kind.
  - **n: acceptable as is.** TARGET.md §1 l. 8 fixes «n = |V|, m = |E|» for the whole fleet, and R88 / R89 leave it implicit. Binding it
    («n = |V|») costs three words and may ride the same H17 edit, but it is not required.
  - Verdict: H16 MATCHES §1-§5 except for the unbound k. With H17 = H16 + the k clause, MATCHES.
