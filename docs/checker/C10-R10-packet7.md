# C10: landing gate for RESULTS R10 (packet 7: EXACT, PREFIX-MONO-X, (FALL) ⇐ (NSTEAL)) and the R9 post-landing note — CHECKER, 2026-10-17

Target: docs/agents/R10-draft.md at trunk a907c46 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk a907c46 merged by merge commit.
Sources (all ancestors of a907c46):
- GAP-A-M.md §22r at d461a76 and at 357224b. 357224b adds only the 10-line "(FALL-V) is FALSE" paragraph inside §22r.
- docs/referee/R-P7.md: 299bc58 (15:05:56Z) and §C at 1abe1d7 (15:28:19Z, +35 lines).
- docs/referee-2/R2-P7.md: a66ff93 (15:18:02Z) and §6 at 19e63f7 (15:28:26Z, +42 lines). REFEREE §C cites R2-P7 at "trunk
  4623faf", which has the same R2-P7.md as a66ff93.
- Code: Oink 8fbf0a7.

## Verdict: FAIL, one required one-phrase fix (E-1); everything else PASS (recommended N-1..N-4; notes N-5, N-6)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d) and the four named points | FAIL on E-1 ((a)'s scope); the named points PASS |
| 2 verdict quotes and independence | PASS (N-2 quote) |
| 3 gap union G-R10-1..6 | PASS (N-3) |
| 4 re-run, REFEREE p7probe.py @ 299bc58 | PASS: identical to R-P7's tables (corpus 138 files and fallv_viol_n28, both orders) |
| 5 R9 post-landing note against R-P7 §C | PASS (N-4) |

## E-1 (required): (a) states EXACT for "every region step of the code"; it is signed only for the best_vertices region loop
- Draft (a): "Lemma EXACT: every region step of the code is exactly the triggered closure Cl_{pr τ}(P(τ⁺) ∪ {τ}; T \ E_τ)".
- What §22r states: "Setting as in §22c: one pruning round in context R ... Lemma EXACT. For every processed τ, ...".
- What the referees signed:
  - REFEREE: "Setting (689-706)"; lines checked 66-101, 110-185, 198-202, 443, 689-706.
  - REFEREE-2 table: "every best_vertices region step". §1 Scope: "EXACT is about the best_vertices region loop (690-705).
    The Dom loops (878-890, 962-991) have the same shape, with X in place of Z and a nonempty initial X. They are not
    claimed and not used."
- "of the code" also reads on the Dom steps and the sptl regions. In a Dom step the tangle rule is called with Z = X, so a
  vertex in X is skipped (136-137), not rejected. X-straddling tangles therefore fire (R-P5 G-a2, R-P6 G6-b1), which is
  exactly what EXACT's exclusion E_τ forbids. So read that way, the statement is broader than signed and is false as
  worded for Dom.
- Fix (one phrase): "every best_vertices region step (dtl.cpp 690-705; the Dom loops and sptl are not claimed)".
- Same class as C3e E-1: a statement wider than its proof. It is not a judgement on the mathematics.

## 1. Statement diff
| draft | §22r at d461a76/357224b | signed | |
| --- | --- | --- | --- |
| new steal: "a tangle t of the earlier visit's T with t ∈ E′_τ \ E_τ for some top τ processed in the earlier round" | (NS): "for every τ processed in the EARLIER run, E′_τ ∩ T ⊆ E_τ, where E′_τ is computed from the later run's prefix P′(τ⁺), whether or not τ is processed there"; a new steal is its failure | REFEREE-2 §5: "a region step (round r, top τ processed in a) and a tangle t ∈ T_a such that b's round-r prefix P_b(τ⁺) meets t without containing it, while a's prefix did not exclude t"; REFEREE (NS-COUNT): "...that P_r(τ⁺) did not [meet]"; §6: same pair-level predicate | OK. t ∈ E′_τ \ E_τ with t ∈ T is exactly ¬(NS). E_τ is defined in the Object line as §22r has it. N-1: say "E′_τ computed from the later visit's prefix, whether or not τ is processed there" |
| (a) EXACT | §22r Lemma EXACT; Cl = dtl_ideal.lfp | both SIGN (REFEREE with G7-a1/a2 closed); REFEREE-2 N-a2: the triggered closure of lfp_ref | wording of Cl OK (N-a2 built in). Scope: **E-1** |
| (b) PREFIX-MONO-X | §22r verbatim in substance (V ⊆ V′, T ⊆ T′, (NS)) | both SIGN | OK |
| (c) non-rise only at a new steal, including Π-blind e*; F_R ≤ N_R^desc + N_R^e* ≤ 3·N_R; N_R = consecutive visit pairs with a new steal; (FALL) ⇐ (NSTEAL); GAP-A ⇐ (CTX⁺) ∧ (NSTEAL) given STR-DET; (NSTEAL) ⇒ (FALL), not the converse | §22r: "F_R ≤ #(visit pairs at R with a new steal)" | REFEREE-2 G-P7-c2 "F_R ≤ N_R (descents) + 2·N_R = 3·N_R", proposed text "F_R ≤ N_R^desc + N_R^e* ≤ 3·N_R"; REFEREE §C accepts: "So F_R ≤ 3·N_R"; joint: "GAP-A ⇐ (CTX⁺) ∧ (NSTEAL), given STR-DET, with F_R ≤ 3·N_R; (NSTEAL) is strictly stronger than (FALL) and open" | OK. The draft uses the corrected bound, not §22r's. "not the converse" means not proved (REFEREE "not conversely"), not refuted |
| (d) fallv_viol_n28 | §22r FALL-V paragraph (357224b) | REFEREE (d) AGREES; REFEREE-2 (d) CONFIRMED; both: same tangle (internal 2) at rounds 3 and 4 (and 5) | OK |

The Lead's named points:
- New-steal definition: OK (N-1 optional).
- (c)'s F_R ≤ 3·N_R and REFEREE's withdrawal: the bound is right. The withdrawal is quoted in substance, but not
  verbatim (N-2).
- "NS-COUNT = NSTEAL" (REFEREE-2 §6): correct. §6: "(NS-COUNT) vs (NSTEAL): the same statement ... The pair-level
  predicates are therefore equal". The draft: "REFEREE's (NS-COUNT) and REFEREE-2's (NSTEAL) are the same statement".
- Scope keeps §22s-§22u out: yes. "L-ALG's later unrefereed refinement (GAP-A-M §22s-§22u: PREFIX-MONO-X* on fired
  tangles; (STEAL-ONCE), (FIRED-R), DATA) is not part of R10". On trunk, §22s (2529), §22t (2561) and §22u (2592) all lie
  after §22r, and none of them is cited in (a)-(d). The only mention is the gap header's "(L-ALG §22t imports REFEREE's)",
  which is a bookkeeping pointer, not content.

## 2. Verdict quotes and independence: PASS
- REFEREE table: (a) SIGN WITH GAPS G7-a1, G7-a2 (closed); (b) SIGN; (c) SIGN WITH GAPS G7-c1 (closed), G7-c2 ("stated,
  not a defect"); (d) AGREES. §C accepts G-P7-c2. The draft matches, with "closed" for G7-c2 a slight compression of "not
  a defect".
- REFEREE-2 table: (a) SIGN; (b) SIGN; (c) SIGN WITH GAPS G-P7-c1, G-P7-c2 (closed); (d) CONFIRMED. The draft matches.
- Independence:
  - REFEREE: "docs/referee-2/R2-P7.md was not read"; §C "read after R-P7 was pushed".
  - REFEREE-2: "docs/referee/R-P7.md was not read before this report was pushed"; §6 "read 15:28Z ..., after a66ff93 was
    pushed".
  - No REJECT.
- N-2 (recommended, quote). The draft writes: its earlier "F_R ≤ #new-steal visit pairs holds as stated" withdrawn.
  - That string is not in R-P7.
  - The (c) text is "F_R (G6-a1) ≤ #(visit pairs at R with a new steal) holds as stated".
  - The §C withdrawal is "No, my 'F_R ≤ #(new-steal visit pairs)' does NOT cover non-consecutive e*-pairs, and my claim
    that it held 'as stated' was wrong".
  - Quote one of those verbatim, or drop the quotation marks.
- N-6 (label). R2-P7's header says 15:20Z, but a66ff93 is committed at 15:18:02Z. This is the same stamp pattern as C8
  N-6 and C9 N-8. The ordering against REFEREE (299bc58 at 15:05:56Z; §C at 15:28:19Z) is unaffected.

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE G7-a1 = REFEREE-2 N-a1 (138-139, not 137) | G-R10-1 |
| REFEREE G7-a2 = REFEREE-2 single last-pop argument | G-R10-2 |
| REFEREE G7-c1 = REFEREE-2 G-P7-c1 | G-R10-3 |
| REFEREE-2 G-P7-c2 (accepted, REFEREE §C); REFEREE (b) wording note = N-b1 | G-R10-4 |
| REFEREE G7-c2 / REFEREE-2 §5 "lossy"; (NSTEAL) OPEN | G-R10-5 (9.5:1 is REFEREE-2 §0/§4; ≈13:1 is REFEREE's corpus section) |
| REFEREE-2 N-a2 (triggered closure) | built into (a) ("Cl as in dtl_ideal lfp_ref ...") |
| dependencies: (S0)/PREFIX-MONO (R7), STR-DET (R8), R9; O1 (oink.cpp 35, game.cpp 478-495, REFEREE-2 §1) | G-R10-6 |
| REFEREE-2 §1 Scope: Dom loops not claimed | **not carried** (it is E-1) |
| REFEREE-2 Gaps: "Open and unchanged: (NSTEAL) ..., (CTX⁺), and G-S5-6 (ACYC)" | (CTX⁺) and (NSTEAL) in Scope; G-S5-6 (ACYC) not named (N-3) |
| REFEREE corpus note: its probe detects non-rises only through RV falls | not carried; the Data line says "0 non-rises without a new steal in either probe" (N-5) |
- "Closed" applies only to G-R10-1..4; G-R10-5 is OPEN; G-R10-6 lists dependencies. Correct.
- N-3 (optional). REFEREE-2 lists G-S5-6 (ACYC) as open and unchanged. It is a GAP-C item, outside R10's reduction.
  Naming it is optional.
- N-5 (note, Data line).
  - "0 non-rises without a new steal in either probe" is exact, but the probes measure different things. REFEREE counts RV
    falls only ("Ψ-shrink and Φ_top non-rises are not separately detected"). REFEREE-2 counts every lex non-rise.
  - The "E_τ nonempty at 196,340 steps" and "differs ... at 24,259" figures are REFEREE-2's (§1). REFEREE's own deficit
    counts are 9,672 / 10,354 of 233,399 / 244,057.
  - Optional: attribute both.

## 4. Re-run: REFEREE docs/referee/scratch/p7probe.py @ 299bc58 (identical at HEAD)
- fallv_viol_n28 (trunk experiments/red/carry/instances/fallv_viol_n28.pg, sha1 21b235f4e680e1bf599c6623774fad0a05d41350):
  - oink: steps 2,156, deficit 506, exact_fail 0, pairs 75, falls with a new steal 17, neither 58.
  - stable: steps 2,071, deficit 506, exact_fail 0, pairs 75, falls with a new steal 17, neither 58.
  - Root falls s3→s4 and s4→s5 (vertex 15, priority 27; RV 6→5 and 5→4) have new steals of tangle [2] at rounds 4 and 5,
    tops 26, 25, 24, 20, 15, ....
  - Identical to R-P7 (d).
- Corpus (experiments/alg/instances, 138 files):
  - stable: steps 233,399, deficit 9,672, exact_fail 0, pairs 4,286, fall with a new steal 20, new steal without a fall 259,
    neither 4,007.
  - oink: 244,057, 10,354, 0, 4,542, 20, 313, 4,209.
  - Identical to R-P7's corpus table. No EXACT FAIL or ERR line.
- Not re-run: REFEREE-2's C++ probe (R2-P7/, patched pinned build).

## 5. RESULTS R9 POST-LANDING NOTE (2026-10-17 15:35Z) against R-P7 §C: PASS
| note | R-P7 §C (1abe1d7) | |
| --- | --- | --- |
| "REFEREE R-P7 §C (referee 1abe1d7) withdraws its R-P6 A4 premise that an e*-pair at R is a pair of consecutive visits of R (false when R is visited more than once per search)" | "It rests on my R-P6 A4 premise: 'a transition whose e* lies in R's call is a pair of consecutive visits of R'. That premise is false when R is visited more than once per search." | OK |
| "#(e*-transitions at R) ≤ 2(F_R + 1)(H + 1) (a consecutive pair lies in at most 2 e*-intervals)" | "#(e*-transitions at R) ≤ 2·(F′_R + 1)(H − 1) + F^e_R ... this is ≤ 2(F_R + 1)(H + 1)"; "a consecutive pair lies in at most two intervals" | OK |
| "The reduction GAP-A ⇐ (CTX⁺) ∧ (FALL) is unchanged; the per-context constant doubles" | "The reduction ... is unchanged; only the constant in R9's per-context budget changes, by a factor of 2. I ask the Lead to note this against R9." | OK |
| "REFEREE-2 confirmation pending" | R2-P7 §6 discusses G-P7-c2 for R10's F_R, not R9's budget constant. No REFEREE-2 confirmation exists on trunk at a907c46 | accurate |
- N-4 (recommended). The note sits under R9 (c) (RESULTS line 318). R9 (a) still reads "the e*-at-R transitions number at
  most (F_R + 1)(H + 1)", and the (c) display uses (F_R + 1)(H + 1). Suggest the note says "applies to (a) and to the
  per-context term of (c)", or mark (a) "(see POST-LANDING NOTE: factor 2)". Then a reader of (a) alone does not take the
  old constant.
- Status: the note is a one-referee correction of a two-signature result. It is labelled as such ("REFEREE-2 confirmation
  pending"), which is correct. When REFEREE-2 confirms or not, the note needs updating.

## Fix list
Required:
- E-1: (a) "every region step of the code" → "every best_vertices region step (dtl.cpp 690-705; the Dom loops and sptl
  are not claimed)".
Recommended:
- N-2: the withdrawal quote verbatim.
- N-4: point R9 (a) at the post-landing note.
Optional:
- N-1: E′_τ's definition in the new-steal sentence.
- N-3: G-S5-6.
- N-5: attribute the data.
With E-1 applied, R10 passes. I re-diff the text only.
