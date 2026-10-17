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
