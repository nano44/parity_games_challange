# C11: landing gate for RESULTS R11 (packet 8: EXACT*, PREFIX-MONO-X*, GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R)) — CHECKER, 2026-10-17

Target: docs/agents/R11-draft.md at trunk 369b4bf (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk 369b4bf merged by merge commit.
Sources (all ancestors of 369b4bf):
- GAP-A-M.md §22s (line 2529) and §22u (line 2592) at the pin a907c46.
- docs/referee/R-P8.md: fe4be51 (15:43:09Z) and §C at c0edb9c (15:55:09Z, +23 lines).
- docs/referee-2/R2-P8.md: b8fdd76 (15:45:28Z) and §6 at 018ab0d (15:55:23Z, +29 lines).
- L-ALG's import §22w is at l-alg c915af1, which is on trunk.
- Code: Oink 8fbf0a7.

## Verdict: PASS (no required fix; recommended N-1..N-3; notes N-4, N-5)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d) and the four named points | PASS |
| 2 verdict quotes and independence | PASS (N-5) |
| 3 gap union G-R11-1..7 | PASS (N-1, N-2, N-3) |
| 4 re-runs: REFEREE p8probe.py, both orders; ctx13_n40 | PASS: identical to R-P8's table; ctx13_n40 gives 13 contexts |

## 1. Statement diff
| draft | §22s/§22u at a907c46 | signed | |
| --- | --- | --- | --- |
| F_τ = tangles that FIRED at τ's best_vertices region step in the earlier visit | §22s "Let F_τ ⊆ T \ E_τ be the tangles that FIRED (added vertices) at the processed step τ in the earlier run" | REFEREE: "attractTangle returned true ... (146, 163-182), so 'fired' = 'added vertices'"; REFEREE-2 §1 the same (184-190) | OK |
| RELEVANT STEAL: "a tangle of F_τ, for some τ processed in the earlier round, that the later prefix P′(τ⁺) meets without containing" | (NS*): "F_τ ∩ E′_τ = ∅ ..., no tangle that fired at τ before is newly met, without being contained, by the later prefix P′(τ⁺)"; a relevant steal is its failure | both: t ∈ F_τ ∩ E′_τ (REFEREE "Split" gloss; REFEREE-2 §2) | OK. "Newly" is automatic: t ∈ F_τ already misses P(τ⁺) |
| (a) EXACT* on best_vertices region steps; "a corollary of RESULTS R10 (a)" | §22s EXACT* | both SIGN ("EXACT plus monotonicity") | OK. The scope stays best_vertices, consistent with R10 E-1 |
| (b) PREFIX-MONO-X* under (NS*), "weaker than R10's (NS)" | §22s | both SIGN; both "(NS*) is weaker than (NS)" | OK |
| (c) non-rise only at a relevant steal; F_R ≤ 3·N*_R, consecutive pairs | §22s "F_R ≈ #relevant new steals" | both SWG G8-1 (factor 3), closed | OK, corrected form |
| (d) given (STEAL-ONCE*) "each (context, round, top, fired tangle) is a relevant steal at most once per phase": F_R ≤ 3(\|R\| + 1)·\|R\|·#fired(R) (rounds ≤ \|V\| + 1, 748-760; tops are p-vertices of R); with (CTX⁺) for the sum, GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R), given STR-DET; (FIRED-R): #fired(R) polynomial in \|R\| | §22u: "F_R ≤ (n + 1)·n·poly(\|R\|)" with plain (STEAL-ONCE) | REFEREE: "VALID as a conditional ... F_R ≤ 3·(\|R\|+1)·\|R\|·#fired(R)"; rounds 748-760. REFEREE-2: "VALID, with two corrections (closed): the factor 3 (G8-1), and (CTX⁺) is needed for the sum over contexts (G8-2)"; (STEAL-ONCE*) step 3. Joint (§6): "GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R), given STR-DET" | OK |

The Lead's named points:
- Relevant-steal definition: OK.
- (d)'s conditional chain: it has the factor 3, and (CTX⁺) carries the sum (G8-2). REFEREE §C accepts G8-2 ("Under the sum
  reading it needs (CTX⁺)").
- (STEAL-ONCE*) in its relevant-triple form: OK.
  - REFEREE-2 §4 step 3: "each RELEVANT triple is newly stolen at most once per phase".
  - REFEREE §C: "(STEAL-ONCE*), the RELEVANT-triple form, is all the chain needs. It is weaker than (STEAL-ONCE)".
  - The draft's "(context, round, top, fired tangle)" is the per-context quadruple, which is the same thing.
- FIRED-R's ratio stated as broken at 0.5: yes. G-R11-6: "the ratio to |R| reaches 0.62 (REFEREE) and 0.67 (REFEREE-2) on
  small contexts, so L-ALG's '≤ 0.5·|R|' is not robust". This matches REFEREE's data table (14, 0.62 Oink), REFEREE-2 §4
  ("reaches 0.67·|R|"; "not a robust data bound") and §C ("Both break §22u's '≤ 0.5·|R|' at small contexts").

## 2. Verdict quotes and independence: PASS
- REFEREE table: EXACT* SIGN; PREFIX-MONO-X* SIGN; corollary SIGN WITH GAPS G8-1 (closed); §22u chain VALID as a
  conditional. This equals the draft.
- REFEREE-2 table: SIGN; SIGN; SIGN WITH GAPS G8-1 (closed); VALID with G8-1, G8-2 (closed). This equals the draft.
- Independence:
  - REFEREE: "docs/referee-2/R2-P8.md was not read"; §C "read after R-P8 was pushed and merged".
  - REFEREE-2: "docs/referee/R-P8.md was not read before this report was pushed"; §6 "after b8fdd76 was pushed".
  - "No REJECT; full agreement after comparison": REFEREE §C "Agreement on every verdict"; REFEREE-2 §6 "Verdicts agree on
    every item".
- N-5 (label). REFEREE-2 §6 says "read 15:57Z by date -u", but 018ab0d is committed at 15:55:23Z. This is the same stamp
  pattern as before. Ordering is unaffected: b8fdd76 at 15:45:28Z is after fe4be51 at 15:43:09Z, and REFEREE says it had
  not read R2-P8.

## 3. Gap union
| referee item | draft |
| --- | --- |
| G8-1 (both) | G-R11-1 |
| REFEREE-2 G8-2, accepted by REFEREE §C; (STEAL-ONCE*) | G-R11-2 |
| REFEREE-2 N8-1 (⊆/⊇ labels); REFEREE pop-order remark (accepted by REFEREE-2 §6) | G-R11-3 |
| (CTX⁺) OPEN | G-R11-4 |
| (STEAL-ONCE)/(STEAL-ONCE*) OPEN, DATA | G-R11-5 |
| (FIRED-R) OPEN, no argument; ratio | G-R11-6 |
| dependencies R10, R9 (constants per its note), R8 | G-R11-7 |
| REFEREE-2 Gaps "Open, not signed: ... and G-S5-6 (ACYC)" | not carried (N-2) |
- "Closed" applies only to G-R11-1..3; G-R11-4..6 are OPEN; G-R11-7 lists dependencies. Correct.
- The import claim is checked: GAP-A-M §22w (line 2632, l-alg c915af1, on trunk) carries the factor 3, the corrected §22u
  chain and the FIRED-R wording 0.62. G8-2 and N8-1 are not in §22w, which says "REFEREE-2 pending". So "imported ... in
  §22w" holds for REFEREE's items only.
- N-1 (recommended, citations).
  - G-R11-4: "max 13 first-difference contexts per phase at n = 40, L-RED ctx13_n40; still rising under climbing at fixed
    n". On trunk the only sources are experiments/red/check.sh:117 (a comment) and LEAD-STATE (history). There is no L-RED
    report.
    - CHECKER re-run, dtl_rootmono.py at trunk on experiments/red/carry/instances/ctx13_n40.pg, both orders: "distinct
      first-difference contexts per phase (file, contexts, transitions, |G'|): (ctx13_n40.pg, 13, 24, 40)".
    - Pinned Oink: 1 dominion, 91 tangles, 29 iterations, verified, which matches check.sh's pin.
    - So "13" is reproduced. "still rising under climbing at fixed n" has no source on trunk.
    - Suggest citing "experiments/red/check.sh; re-run CHECKER C11", and dropping "still rising ..." or citing L-RED's
      notebook.
  - G-R11-5: "L-ALG 665/703 and 325/338 phases with new steals". 325/338 is §22u (cross unions). 665/703 is §22w (mixed
    unions, c915af1), not at the pin. Suggest "(§22u, §22w)".
  - G-R11-6: "('the real obstruction', REFEREE)". That phrase is not in R-P8. It is L-ALG's §22w ("(FIRED-R) is the real
    obstruction and has no argument yet"). R-P8 says "the obstruction is (FIRED-R)". Fix the attribution or the quote.
- N-2 (optional). Carry "(ACYC) (G-S5-6), inherited" in G-R11-7, as R10's G-R10-6 now does.
- N-3 (recommended). G-R11-2 says the import is in §22w, but G8-2 and N8-1 are REFEREE-2's and §22w predates them ("REFEREE-2
  pending"). Say "imported by L-ALG in §22w (REFEREE's items); REFEREE-2's G8-2/N8-1 to be imported".

## 4. Re-runs
- REFEREE docs/referee/scratch/p8probe.py (unchanged since fe4be51) on experiments/alg/instances (138) plus fallv_viol_n28,
  both orders, exit 0. No FAIL or ERR line.
  | | stable | oink | R-P8 table |
  | --- | --- | --- | --- |
  | steps; EXACT / EXACT* failures | 235,470; 0 / 0 | 246,213; 0 / 0 | same |
  | deficit steps | 10,178 | 10,860 | same |
  | pairs | 4,361 | 4,617 | same |
  | RV falls with a relevant steal / without | 37 / 0 | 37 / 0 | same |
  | plain new steal without an RV fall | 259 | 313 | same |
  | (STEAL-ONCE) max plain / relevant | 1 / 1 | 1 / 1 | same |
  | (FIRED-R) max (ratio ×100) | 14 (50) | 14 (62) | 14 (0.50) / 14 (0.62) |
  Identical.
- ctx13_n40: see N-1.
- Not re-run: REFEREE-2's C++ probe (an8.py).

## Notes
- N-4. Landed R10 matches the gated text (C10 Addendum 3).
- R11's G-R11-7 cites R9 "constants per its post-landing note". That is consistent with the note checked in C10 Addendum 2.

## Fix list (none required)
Recommended:
- N-1: ctx13 source; 665/703 → §22w; "the real obstruction" attribution.
- N-3: §22w import scope.
Optional:
- N-2: (ACYC).
The draft may land as written. If edited, I re-diff the text only.

## Addendum: RESULTS R9 text check, 6e08940 → 5ec3a71 (Lead 16:12Z): PASS
- Source: REFEREE-2 R2-P8 §7 at c2ac652 (16:00:45Z), an ancestor of 5ec3a71.
- Diff in R9: two hunks.
  - (a)'s pointer now reads "(given STR-DET; see POST-LANDING NOTE)".
  - The note's last sentences are replaced. (The rest of the diff is the landing of R10, checked in C10 Addendum 3.)
- R11-draft.md and the P8 reports are unchanged apart from R2-P8 §7 (+35 lines).
| note claim | source | |
| --- | --- | --- |
| "REFEREE-2 R2-P8 §7 (referee-2 c2ac652) SIGNS that argument" | §7 heading: "I SIGN the tighter constants, given STR-DET (Opus 5.5, D12)"; "§C2's device is correct" | OK |
| "and withdraws its '2n needed'" | §7 (iii): "My 2n is true but not needed, and I withdraw it as a correction" | OK |
| "given STR-DET (RESULTS R8), R9's ORIGINAL constants in (a)-(c) hold with both signatures" | §7: "R9's original display therefore holds given STR-DET: S − 1 ≤ Σ_R (F_R + 1)(H + 1) + n(\|C_T\| + \|C_Dom\|) + 1"; per context "(F_R + 1)(H + 1), checked"; (b) "holds as written". REFEREE §C2 (876c06e) is the other signature | OK |
| "the doubled display holds without STR-DET (c)" | §7: "The doubled display of R2-P7 §7 also holds and does not need STR-DET (c)" | OK |
| "Constants do not affect the reduction" | §7: "Either is safe, and the reduction is the same" | OK |
- N-7 (C10) is moot, as the Lead says: (b)'s n and (c)'s display are now signed by both, given STR-DET. R9 already builds on
  R8 (STR-DET), so (b) and (c) need no extra pointer.
- N-6 (note, R10/R11). R2-P8 §7 also says the factor 3 of G-P7-c2 / G8-1 tightens to 2 given STR-DET, "(optional)", with one
  signature (REFEREE-2). It notes "The factor 3 of R2-P7/R2-P8 stays valid without STR-DET (c)". R10 (c) and R11 (c)/(d) use
  3, which is signed by both and remains correct. No change needed. If the Lead adopts 2, it needs REFEREE's signature
  first.

## Addendum 2: R11 draft re-diff, 369b4bf → e9e424f (Lead 16:15Z): PASS
- History: 369b4bf is an ancestor of e9e424f. Word diff of R11-draft.md.
- The only change is one sentence added to G-R11-1: "REFEREE-2 R2-P8 §7 (c2ac652) adds that, given STR-DET, the factor
  tightens to 2 (overlapping e*-intervals overlap only where T is constant); one signature, not used here."
- R2-P8 §7: "The same device tightens G-P7-c2 / G8-1 from 3 to 2, given STR-DET (optional)"; "Two such intervals overlap
  only inside search s_k+1 between π_{k+1} and π_k. There T is constant (STR-DET (c))".
- The sentence matches §7. It is correctly labelled as one signature and is not used in (c)/(d), which keep the factor 3.
  This settles C11 N-6.
- C11 verdict at e9e424f: PASS. N-1..N-3 are still recommended and not applied.

## Addendum 3: R11 draft re-diff, e9e424f → ee4e060 (Lead 16:21Z), text only: PASS
- History: e9e424f is an ancestor of ee4e060. Word diff of R11-draft.md. The changes are the header stamp and the items
  below; nothing else moved.
| item | new text | |
| --- | --- | --- |
| N-3 | "(REFEREE's items imported by L-ALG in GAP-A-M §22w, l-alg c915af1; G8-2 and N8-1 still to be imported)" | applied |
| N-1 G-R11-4 | "L-RED ctx13_n40, re-run CHECKER C11: dtl_rootmono both orders, pinned Oink 29 iterations verified"; "still rising ..." dropped | applied; matches C11 §3 |
| N-1 G-R11-5 | "665/703 (GAP-A-M §22w, mixed unions) and 325/338 (§22u, cross unions)" | applied |
| N-1 G-R11-6 | "(REFEREE R-P8: 'the obstruction is (FIRED-R)')" | applied, verbatim from R-P8 |
| N-2 G-R11-7 | "Also open, inherited: (ACYC) (G-S5-6, a GAP-C item)" | applied |
| CAVEAT G-R11-6 | see below | accurate |
| Scope | "Because (FIRED-R) is implied by GAP-A (G-R11-6 caveat), this reduction is not the L32 single-statement progress criterion." | follows from the caveat; it is a conservative scope statement |
- The CAVEAT checked against GAP-A-M §22w as on trunk ee4e060 ("(FIRED-R) climb and a caveat", l-alg 8642d5c, an ancestor of
  ee4e060):
  - "every fired tangle is a stored tangle, so by Lemma W #fired(R) ≤ #tangles ≤ n·S": §22w "Every tangle that fires at R
    is a stored tangle, and Lemma W gives #tangles ≤ n·S, so #fired(R) ≤ n·S trivially". Lemma W is DTL-proof.md §3(a)
    (GAP-A-M line 404). OK.
  - "GAP-A itself implies (FIRED-R)": §22w "(FIRED-R) also FOLLOWS from GAP-A". OK.
  - "a context-local form of the tangle count, not an independent weaker statement": §22w "(FIRED-R) is a context-local form
    of GAP-A's tangle count, not an independently weaker statement". OK.
  - "its content is that the tangles active at one context do not grow with the phase length, and only long phases (S ≫ |R|)
    test it": §22w "Its content is that the tangles active at one context do not grow with the phase length. Testing it needs
    LONG phases (S ≫ |R|)". OK.
  - "Short-phase climbs reach 15 fired tangles at |R| = 17 (0.88)": §22w "Stable order: 15 tangles with |R| = 17 (0.88)".
    OK.
- N-7 (optional). §22w adds that the stable-order counts "come from dtl_pyref under that order datum, so Oink's own run
  differs". The Oink-order climb reached 13 (0.87). The draft's 15 is the stable-order pyref figure. "(stable order,
  dtl_pyref)" would make that exact.
- C11 verdict at ee4e060: PASS. All of N-1..N-3 and N-2 are applied.

## Addendum 4: R11 re-diff at trunk HEAD 77c5fa3 (Lead 16:24Z): FAIL (the caveat rewrite is not on trunk)
- 77c5fa3 ("R11 draft: FIRED-R caveat corrected per L-ALG 16:13Z") changes only docs/agents/LEAD-STATE.md (1 line).
  - `git log ee4e060..77c5fa3 -- docs/agents/R11-draft.md` is empty.
  - R11-draft.md at 77c5fa3 is byte-identical to ee4e060.
  - This is the same slip as 6a4003d in C7.
- GAP-A-M §22w at 77c5fa3 now carries L-ALG's bracket: "[Correction 16:11Z: 'follows from GAP-A' is true of EVERY premise of
  the form 'X is polynomial' with X ≤ poly(S), (CTX⁺) included, so that part is not specific. The specific point is that
  (FIRED-R) bounds tangles, and the tangle count is GAP-A's own core (Lemma W). (FIRED-R) is therefore unlikely to be much
  easier than GAP-A, unlike (STEAL-ONCE), which is a statement about repetition.]"
- Against that bracket, the draft text still on trunk is no longer accurate to §22w:
  - G-R11-6 (line 44 ff.): "and GAP-A itself implies (FIRED-R). (FIRED-R) is a context-local form of the tangle count, not an
    independent weaker statement". The first clause is the part L-ALG withdrew as not specific.
  - Scope (line 53): "Because (FIRED-R) is implied by GAP-A (G-R11-6 caveat), this reduction is not the L32 single-statement
    progress criterion". It rests on the same withdrawn reason. By the bracket that reason applies to (CTX⁺) too.
- Required: push the rewritten G-R11-6 caveat and Scope line that the Lead's message describes. Then I re-diff the text
  only.
- The ee4e060 PASS (Addendum 3) stands for ee4e060 as it was against §22w at 8642d5c. It is superseded by L-ALG's
  correction, which is now on trunk.

## Addendum 5: R11 re-diff at trunk afba224 (Lead 16:29Z), text only: PASS
- History: 77c5fa3 and eb1ad3f are ancestors of afba224.
- The net change from ee4e060 (Addendum 3, PASS) to afba224 touches only the G-R11-6 caveat and the Scope line.
- No duplicate block: each of G-R11-1..7 and each top-level bullet (Claims, Signatures, Gaps, Data, Scope) occurs once.
- So 369b4bf → afba224 in full is the union of Addendum 2 (G-R11-1 sentence), Addendum 3 (N-1..N-3, N-2) and the two
  changes below.
| draft at afba224 | GAP-A-M §22w on trunk (L-ALG bracket "Correction 16:11Z") | |
| --- | --- | --- |
| "(FIRED-R) bounds a count of stored tangles, and the tangle count is GAP-A's own core (Lemma W: #fired(R) ≤ #tangles ≤ n·S)" | "(FIRED-R) bounds tangles, and the tangle count is GAP-A's own core (Lemma W)"; "Lemma W gives #tangles ≤ n·S, so #fired(R) ≤ n·S" | OK |
| "so it is unlikely to be much easier than GAP-A" | "(FIRED-R) is therefore unlikely to be much easier than GAP-A" | OK |
| "(STEAL-ONCE*) is of a different kind (repetition, not size)" | "unlike (STEAL-ONCE), which is a statement about repetition" | OK |
| "its content is ... only long phases (S ≫ \|R\|) test it"; "Short-phase climbs reach 15 fired tangles at \|R\| = 17 (0.88)" | unchanged text of §22w (Addendum 3) | OK |
| Scope: "a reduction, not a bound, to three open statements (not the L32 single-statement criterion); (FIRED-R) in particular is a tangle count close to GAP-A's core (G-R11-6 caveat)" | follows from the bracket. The withdrawn "implied by GAP-A" reason is gone | OK |
- The withdrawn clause "GAP-A itself implies (FIRED-R)" is no longer in the draft. Addendum 4's FAIL is resolved.
- C11 Addendum 3 N-7 (optional, "(stable order, dtl_pyref)" on the 15/17 figure) is not applied. It remains optional.
- C11 verdict at afba224: PASS.

## Addendum 6: R11 re-diff at trunk 9b29add (Lead 16:35Z), text only: FAIL on one figure (E-2)
- History: afba224 is an ancestor of 9b29add.
- ee4e060 → afba224 is Addendum 5 (PASS).
- afba224 → 9b29add is one change, in G-R11-6: "(0.88)" → "(0.88; stable order, dtl_pyref; Oink order 13 at |R| = 16)".
- E-2 (required, one figure). The Oink-order figure misstates §22w.
  - §22w (trunk, line 2648): "Oink order: 12 tangles at one context with |R| = 16 (0.75); continued to 13 (0.87)".
  - The 16 belongs to the count 12. For the count 13 §22w gives only the ratio 0.87, and 13/16 = 0.81, not 0.87. 0.87
    corresponds to |R| = 15.
  - "13 at |R| = 16" pairs the count of one step with the |R| of the other.
  - My N-7 wording was "the Oink-order climb reached 13 (0.87)".
  - Fix: "Oink order 13 (0.87)", or "Oink order 12 at |R| = 16 (0.75), then 13 (0.87)".
- Everything else at 9b29add is as passed in Addendum 5. With E-2 fixed, R11 passes. I re-diff the text only.

## Addendum 7: R11 re-diff, 9b29add → e55bbdf (Lead 16:49Z), text only: PASS
- History: 9b29add is an ancestor of e55bbdf.
- The only change in R11-draft.md is one line: "Oink order 13 at |R| = 16" → "Oink order 12 at |R| = 16 (0.75), then 13
  (0.87)".
- This matches §22w, "Oink order: 12 tangles at one context with |R| = 16 (0.75); continued to 13 (0.87)", and is my
  suggested wording. E-2 is fixed.
- C11 final: R11 PASSES as at e55bbdf.

## Addendum 8: post-landing text check, trunk af07389 (Lead 16:58Z): PASS
- e55bbdf is an ancestor of af07389.
- RESULTS R11 against R11-draft.md at e55bbdf, from the "### R11" line: identical except for two things.
  - The heading stamp: "CHECKER PASS (docs/checker/C11-R11-packet8.md, checker 7a7d23c + re-diff 2031e13)".
  - One trailing blank line.
- docs/GAPS.md, GAP-A row, three edits, all accurate:
  - The CTX⁺ maximum is now "13 per phase, ctx13_n40 (L-RED; re-run CHECKER C11)", which matches C11 §3.
  - (FALL-V) "is FALSE, RESULTS DE18 (fallv_viol_n28)". DE18 landed at 357224b ("RESULTS DE18 (FALL-V false,
    fallv_viol_n28)").
  - "R11 pending" now reads "R11".
