# C12: landing gate for RESULTS R12 (packet 9: R11 (d) with the factor k, Lemma CHARGE, depth) — CHECKER, 2026-10-17

Target: docs/agents/R12-draft.md at trunk 4ca9b07 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk 4ca9b07 merged by merge commit.
Sources (all ancestors of 4ca9b07):
- GAP-A-M.md §23f (line 2904) and §23g (line 2944) at the pin c5e2b4d.
- The imports, §23k (line 3043, l-alg 67b9e05).
- docs/referee/R-P9.md: 72313f3 (20:16:12Z), a3e9566 (20:20:07Z; "Written 20:12Z-20:25Z" → "20:12Z-20:19Z" only), and §C at
  3785d3f (20:30:05Z).
- docs/referee-2/R2-P9.md: 2612634 (20:18:20Z) and §5 at 19a94b8 (20:22:03Z).
- docs/referee-2/R2-P8.md at c2ac652.
- Code: Oink 8fbf0a7.

## Verdict: FAIL on one inequality in (c) (E-1, one-token fix); everything else PASS (recommended N-1, N-2; notes N-3..N-5)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d), two forms of STEAL-POLY, constant D | (a), (b), (d) PASS; (c) FAIL on E-1 |
| 2 gap union G-R12-1..8, incl. G-R12-4 | PASS (N-1, N-2) |
| 3 re-run (d): pinned Oink plus dtl_stealdepth.py, both orders | PASS: reproduced exactly (N-3) |
| 4 against TARGET.md | PASS |

## E-1 (required): (c) "Depth ≤ #steps ≤ (|R|+1)|R| − 1"
- REFEREE (c): "depth ≤ #steps − 1 ≤ (|R| + 1)|R| − 1 (PROVED, given CHARGE)".
- REFEREE-2 §3: "depth ≤ #steps − 1 ≤ (|R| + 1)|R| − 1 ... the number of steps is ≤ (|R|+1)·|R|".
- §23g at the pin: "depth ≤ (|R| + 1)|R| − 1".
- The draft's middle term, "#steps ≤ (|R|+1)|R| − 1", is not what was signed: the signed step count is ≤ (|R|+1)|R|. The
  final depth bound is right, but the chain as written asserts an unsigned, one-smaller step bound.
- Fix: "Depth ≤ #steps − 1 ≤ (|R|+1)|R| − 1".

## 1. Statement diff
| draft | §23f/§23g (c5e2b4d) and §23k | signed | |
| --- | --- | --- | --- |
| Object: q, k_q, Q, "Q bounds the number of q with k_q > 0", RE-STEAL, P(τ⁺) = the prefix before τ | §23f (1); §23g; P(τ⁺) is G9-b1's correction (§23k) | REFEREE-2 §1 "The number of q with k_q > 0 is at most Q"; both G9-b1 | OK |
| (a) F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·Q; GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum) [no FIRED-R]; GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_k) ∧ (FIRED-R) | §23f (1); forms named in §23k ("SUM form ... with no (FIRED-R)"; "k_R form ... needs (FIRED-R)") | REFEREE (a) SIGN; REFEREE-2 (a) SIGN with N9-a1 ("In the sum form ... (FIRED-R) is redundant"); REFEREE §C "R2's N9-a1: ACCEPTED ... (FIRED-R) is redundant for (a)" | OK. Both forms are stated correctly, and each has two signatures |
| (b) Lemma CHARGE: cause at a pair m, j < m < i, at a strictly earlier step (rounds ascending, tops descending); distinct re-steals have distinct causes | §23g Lemma CHARGE (verbatim in substance) | REFEREE SWG (G9-b1, G9-b2 closed; G23g-1/2 checked); REFEREE-2 SWG (G9-b1, G9-b2 closed) | OK. The statement is unchanged by G9-b1 (a proof-text fix); P(τ⁺) is defined in the Object line |
| (c) depth; E_0 ≤ Q, E_d ≤ Q·E_{d−1}; Σ_q k_q ≤ 2Q^{D+1}; (STEAL-POLY_sum) "for CONSTANT D only (D = O(log n) gives quasi-polynomial)"; proved depth bound gives "only exp(Θ(n² log n))"; GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D constant) ∧ (FIRED-R), given STR-DET | §23g Depth, Counting | REFEREE (c) SWG G9-c1 (closed): "STEAL-POLY follows only for CONSTANT D"; REFEREE-2 (c) SIGN, "Only for CONSTANT D", "exp(Θ(n² log n))", "D = Θ(log n) ... quasi-polynomial and excluded by TARGET §4"; joint conclusion identical | OK apart from **E-1**. "Constant D only" is correct, and FIRED-R is used where needed (G9-c1) |
| (d) stealonce_viol_n76: one re-steal (stable; tangle 7 at (round 4, top 18), k = 2, depth 1, single cause: the depth-0 relevant steal of tangle 9 at (round 4, top 66)); none in the Oink order | §23g G23g-3 | REFEREE (d) CONFIRMED; REFEREE-2 §4 (same re-steal, internal tops 31 / 74) | OK. Reproduced (§3) |

The Lead's named points:
- (a) states the two forms correctly:
  - the sum form needs no (FIRED-R);
  - the k_R form needs (FIRED-R).
  Both have two signatures (REFEREE-2 N9-a1, accepted in REFEREE §C).
- (c) says "CONSTANT D only", and spells out the O(log n) and proved-bound cases. Correct.

## 2. Verdict quotes, independence, gap union
- REFEREE (table plus §C): (a) SIGN, N9-a1 WITHDRAWN in §C ("My N9-a1 is WITHDRAWN. R2-P8 §7 exists (c2ac652, line 139)"),
  and R2's N9-a1 ACCEPTED; (b) SWG closed; (c) SWG closed (G9-c1); (d) CONFIRMED. This equals the draft.
- REFEREE-2 (table plus §5): (a) SIGN (N9-a1); (b) SWG closed; (c) SIGN (N9-c1); (d) probe. This equals the draft.
- Independence:
  - REFEREE: "docs/referee-2/R2-P9.md was not read"; §C read it "from claude/referee-2".
  - REFEREE-2: "docs/referee/R-P9.md was not read before this report was pushed"; §5 read 72313f3 "after 2612634 was
    pushed".
  - No REJECT.
- G-R12-4 checked:
  - c2ac652:docs/referee-2/R2-P8.md line 139 is "## 7. REFEREE's R-P7 §C2 on R9's constants ... I SIGN the tighter
    constants".
  - Line 166 is "The same device tightens G-P7-c2 / G8-1 from 3 to 2, given STR-DET (optional)".
  - So "line 139ff" is right.
  - REFEREE §C: "I read R2-P8 at b8fdd76, before §7 was added". The draft's account is exact.
| referee item | draft |
| --- | --- |
| G9-b1 (both) | G-R12-1 |
| REFEREE G9-b2 = REFEREE-2 round convention (R2-P7 §3) | G-R12-2 |
| REFEREE-2 N9-a1 + REFEREE G9-c1 (forms); REFEREE N9-b1 = REFEREE-2 G9-b2 (cite dtl.cpp 136-139) | G-R12-3 |
| REFEREE N9-a1 (withdrawn) / R2-P8 §7 citation | G-R12-4 |
| G23g-3 (STEAL-DEPTH_D) OPEN | G-R12-5 |
| (FIRED-R), (CTX⁺) OPEN | G-R12-6, G-R12-7 |
| dependencies R8-R11 | G-R12-8 |
| REFEREE-2 N9-c1 (Q = 1) = REFEREE's Q = 1 remark | not listed. Wording only; already true in (c)'s bound. OK |
| REFEREE-2 "Open, not signed: ... G-S5-6 (ACYC)" | not carried (N-2) |
- "Closed" applies to G-R12-1..4; G-R12-5..7 are OPEN; G-R12-8 lists dependencies. Correct.
- The imports are on trunk: §23k (67b9e05) carries G9-b1, G9-b2, the citation, G23g-1/2, the named forms of (STEAL-POLY),
  constant D, N9-c1 and the R2-P8 §7 citation. "§23f-§23g not rewritten" is correct (§23k says so).
- N-1 (recommended, G-R12-5).
  - "L-ALG: k max 1 on big unions (n ≤ 120, Oink order)": §23g's table has k max 1 in BOTH orders (seeds 7/8, Oink and
    stable). Say "both orders".
  - "Attack in progress (L-RED; L-ALG dtl_depthclimb)" is a status line. experiments/alg/dtl_depthclimb.py exists on trunk,
    but there is no result. Fine as status.
- N-2 (optional). Carry "(ACYC) (G-S5-6), inherited" in G-R12-8, as R10/R11 do.
- G-R12-6/7 status names checked on trunk:
  - FIRED-STEP, FIRED-LAMINAR, FIRED-TOP-INJ: §23e;
  - NO-RETURN: §23h;
  - CTX-LAMINAR: §23i.
  All are L-ALG self-kills, unrefereed, and quoted as status only. OK.

## 3. Re-run (d)
- Instance: experiments/red/carry/instances/stealonce_viol_n76.pg, sha1 32c2da0b6ff0ad87b3f7d725e351356bd8e14172.
- Pinned Oink `--dtl --no-single --no-wcwc --no-loops -v`: "found 1 dominions and 50 tangles", "solved in 7 iterations",
  "solution verified (33 strategies)".
- experiments/alg/dtl_stealdepth.py, unmodified, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0:
  - stable: "RE-STEAL ... |R| 76 pair 5 step (r4, top 18) t 7 k 2 depth 1 | previous 2 | causes (pair, step, tangle,
    depth): [(3, (4, 66), 9, 0)]"; "max k 2; max depth 1".
  - oink: "max k 1; max depth 0".
  - Identical to the draft's (d) and to REFEREE (d).
- N-3 (tool version). dtl_stealdepth.py and dtl_rootmono.py changed after the pin: 931fc22 at 20:17:17Z, "CLI output
  unchanged". I ran both the trunk version and the pin c5e2b4d version (git archive into scratch). Their outputs are
  byte-identical in both orders.

## 4. Against TARGET.md
- Heading: "partial step-4 reduction (not M3, not a step-4 pass)". Scope: "a reduction, not a bound ... GAP-A stays OPEN ...
  Not the L32 single-statement criterion ... Gauntlet step 4 stays open". No claim of a bound.
- TARGET §4 lists "Any bound that hides a quasi-polynomial or exponential term" as not counting. (c) explicitly excludes
  D = O(log n) (quasi-polynomial) and the proved depth bound (exponential). Consistent.
- Every claim is conditional on DATA-only premises, labelled as such. No overstatement.

## Notes
- N-4 (label). REFEREE's header says "Written 20:12Z-20:19Z" (after a3e9566), but 72313f3 is committed at 20:16:12Z. This
  is the same stamp pattern as before. Independence is unaffected: REFEREE says R2-P9 was not read, and 2612634 is at
  20:18:20Z.
- N-5. (d) uses dtl_stealdepth's top numbering (18, 66). Both referees' own probes report internal tops 31 / 74 for the
  same vertices (REFEREE: "a different internal numbering"). No change needed.

## Fix list
Required:
- E-1: "Depth ≤ #steps − 1 ≤ (|R|+1)|R| − 1".
Recommended:
- N-1: "both orders" in G-R12-5.
Optional:
- N-2: (ACYC).
With E-1 applied, R12 passes. I re-diff the text only.
