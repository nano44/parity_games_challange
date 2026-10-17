# C5: landing gate for RESULTS R5 (eleven packet-2 lemmas on A_DTL) — CHECKER, 2026-10-17

Target: docs/agents/R5-draft.md at trunk 273c2cd (not edited). Branch: origin/claude/checker was confirmed an ancestor of the
local branch, then trunk 273c2cd was merged by merge commit. Sources:
- Packet at the pins 43d63b0 (REFEREE) and 20fe2ed (REFEREE-2). Every cited file has the same blob at both pins:
  - GAP-C.md 45db049;
  - GAP-A-M.md ba106a1;
  - SPP.md 2ad9f4c;
  - C5-DTL.md c4c59d7;
  - DTL-proof.md 34d0475.
  So the referees read identical statements.
- Signatures:
  - docs/referee/R-PROVED2.md: table, §C and §C5 at referee 88d8e4c.
  - docs/referee-2/R2-PROVED2.md: verdicts at 581902f; §13 at 72d1cd2.
- Clean detached worktrees at 88d8e4c and 581902f. Code: Oink 8fbf0a7.

## Verdict: FAIL — one required text fix (the gap header); every re-run reproduces; notes N-1..N-6
| check | verdict |
| --- | --- |
| 1 statement diff, (a)-(k) | PASS. No item overstates what was signed. The six named points all hold. Notes N-1..N-4 |
| 2 verdict quotes and independence | PASS |
| 3 gap union, and "all closed" | **FAIL (minor)**: the header "all closed in the reports" covers G-R5-8, which lists dependencies "checked in outline only", not closed gaps. The same defect was fixed in R4 (C4 O-2). Two dependencies named by REFEREE are not listed (N-5) |
| 4 re-runs | PASS: k5.pg; bthr_probe.py and fdl_random.py at 88d8e4c; REFEREE-2's probe at 581902f, corpus part |

## 1. Statement diff (draft vs cited section at the pins vs signed reading)
| item | source at pin | signed reading | draft | |
| --- | --- | --- | --- | --- |
| (a) SCC1 | GAP-C §3: every vertex of an sptl region Z_τ reaches τ in H; consequence: the SCCs reachable from τ are τ's own | REFEREE (a) SIGN; REFEREE-2 (a) SIGN ("the only SCC examined is τ's") | "in a closed sptl region Z_τ ... at most one nontrivial SCC, the set C_τ reachable from τ" | OK. The source holds for every region; the draft restricts to closed regions, which is weaker |
| (b) B-thr | GAP-C §3, (i)-(iii) with branches (a)/(b) | both: "(a) always" after F-b3; REFEREE §C5, REFEREE-2 §13.2; GAP-β = (β-a); "last escape" = the pop at which it leaves the current call's context chain (REFEREE G-b2 = REFEREE-2 G-b2) | "τ ∈ t, every escape of t lies outside the context R, and the last escape ... popped in an attractor with threshold < pr(τ). Branch (b) ... vacuous (F-b3)" | OK in the stronger form, as both signed. It omits (i)'s "pr(τ) = max pr(t)" and (a)'s "no vertex of t in the attractor's target", which is weaker, not an overstatement |
| (c) Theorem A | GAP-C §13: root call returns 1 ⇒ lowest region ⊆ W_p(G'); if closed (not (α)), a new tangle or a dominion, inside W_p(G') | REFEREE-2 G-c1: first sptl pass, premise "Z_k closed"; REFEREE §C3: "the reading I used" | "lowest region of its first sptl pass lies in W_p(G') and, if closed (no (α)), is productive" | OK (first-pass reading as signed). It omits "inside W_p(G')" for the product (weaker) |
| (d) O0, O1 | GAP-C §6 | both SIGN | as stated | OK |
| (e) OPP-EXIT | GAP-C §11: "π(o) outside the set CurR in which o was attracted, i.e. ..." | both G-e1: conclusion "π(o) ∉ Z_τ" | "with conclusion π(o) ∉ Z_τ: a learned tangle meets W_{1-p} only where ..." | OK. N-1 on the gloss |
| (f) K0 | GAP-C §18b (a)-(d) | REFEREE SIGN; REFEREE-2 SIGN WITH GAPS (edges of G') | (b) and (c) parts, "with edges of G'" | OK (subset of K0, with REFEREE-2's reading) |
| (g) phases ≤ D + 2 | C5-DTL.md 141-142 has only the run() loops (the file has 187 lines and no "D + 2"); the bound and "D = dominion-finding searches ≤ n" are in GAP-A-M §21c (line 1584) | REFEREE (g) SIGN, citing C5 141-142 and SPP.md §1's "phase"; REFEREE-2 cites "C5-DTL lines 141-142; GAP-A-M §21c" | "Phases ≤ D + 2 (C5-DTL.md lines 141-142; --dtl is non-interleaved)" | OK in substance. N-2: D undefined in the draft, citation incomplete |
| (h) FDL | GAP-A-M §21d | both: on the log with repeated sptl passes deleted (REFEREE-2 §13.1; REFEREE §C1) | "stated on the call log with repeated sptl passes (dtl.cpp 870-874) deleted" | OK, the aligned form as signed |
| (i) DV*-MONO | GAP-A-M §21h | REFEREE R-i "INF = never dropped"; REFEREE-2 §13.4 adopts R-i | "reading INF as 'never dropped'" | OK |
| (j) LRN budget | GAP-A-M §21j | REFEREE: "an LRN transition at R is by definition one where DV*_R moves" (≤ n(n+1) per distinct context per phase); REFEREE-2 §10: LRN at R = transitions whose first-difference context is R and DV*_R changes | "with REFEREE-2's reading of LRN (R2-PROVED2 §10)" | OK. N-3 |
| (k) conditional bound | SPP.md §1 (SPP for every ω); DTL-proof §3 (b)-(e), Lemma W | REFEREE: "SIGN (conditional on (SPP) for every ω)"; REFEREE-2: "(SPP) for the given ω" | "if (SPP) ... holds for every order datum, then ... ≤ n(n + 2) searches and ... O(n^10 (m + n²)) word operations, and unit cost equals bit cost" | OK, conditional on (SPP) for every ω, as named. N-4 |
The six points named by the Lead:
- (b) "(a) always": both signed it.
- (c) first sptl pass: G-c1, the same in both.
- (h) aligned log: both signed it.
- (k) conditional on (SPP) for every ω: yes.
- Scope line: "(a)-(f) support GAP-C but do not establish completeness ... (g)-(k) do not establish GAP-A: (k) is conditional
  on (SPP), which is DATA only. Gauntlet step 4 stays open."
- The K5 finding is under "Finding outside the signed statements". Both referees treat it so (REFEREE-2 §12 G-c2,
  §13.3; REFEREE §C3).
All PASS.

## 2. Verdict quotes and independence: PASS
- REFEREE table (88d8e4c): (a) SIGN; (b) SIGN WITH GAPS, ALL CLOSED (§C5); (c) SIGN; (d) SIGN, SIGN; (e) SIGN WITH GAPS (G-e1,
  G-e2 closed); (f) SIGN; (g) SIGN; (h) SIGN WITH GAPS, G-h1 CLOSED (§C1); (i) SIGN (with reading R-i); (j) SIGN; (k) SIGN
  (conditional). This equals the draft's "(a),(c),(d),(f),(g),(i),(j),(k) SIGN; (b),(e),(h) SIGN WITH GAPS, all closed".
- REFEREE-2 verdicts (581902f, revised in §13 at 72d1cd2): (a),(d),(g),(i),(j) SIGN; (b),(c),(e),(f),(h),(k) SIGN WITH GAPS. This
  equals the draft.
- Commits: REFEREE 50f2546 (report), ef6cf37 (§C), 88d8e4c (§C5); REFEREE-2 581902f (report), 72d1cd2 (§13). These are the
  commits the draft cites.
- Independence:
  - REFEREE: "docs/referee-2/ was not read"; §C was "read ... only after my report was pushed (50f2546)".
  - REFEREE-2: "docs/referee/R-PROVED2.md was not read before this report was pushed"; §13 was read "after 581902f was
    pushed".
- No REJECT in either report. "After comparison no gap of the packet is open in either report": REFEREE says "After the
  comparison with REFEREE-2 (§C, §C5) no gap of packet 2 is open". REFEREE-2's §13.4 open items are not packet gaps:
  - (SPP);
  - (α) and Case B;
  - (ACYC);
  - the K5 correction;
  - G-h1, closed by REFEREE §C1.
  Correct.

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE G-b1 = REFEREE-2 G-b3 (O0 for escapes solved before the search) | G-R5-1 |
| REFEREE G-b2 = REFEREE-2 G-b2 ("last escape" pop) | G-R5-1 |
| REFEREE-2 G-b1 (same-search tangles; closed R2 §13.2, signed REFEREE §C5) | G-R5-1 |
| F-b3 (finding, both) | (b) |
| REFEREE-2 G-c1 (first pass, "Z_k closed") | G-R5-2 |
| REFEREE-2 G-c2 / REFEREE §C3 (K5 (i)/(iii) false) | "Finding outside the signed statements" |
| G-e1, G-e2 | G-R5-3 |
| REFEREE-2 G1 for K0 (edges of G') | G-R5-4 |
| G-h1 (both; closed) | G-R5-5 |
| R-i (both) | G-R5-6 |
| REFEREE-2 G-k1, G-k2 | G-R5-7 |
| REFEREE §"Hypotheses" 4 (K4, K5(ii), §3 (b)-(e) in outline) | G-R5-8 |
| REFEREE §"Hypotheses" 2 ((SPP) DATA) / REFEREE-2 "Not checked: (SPP)" | Scope |
| REFEREE-2 §12 "Nothing here is Lean-checked" | G-R5-8 |
| **REFEREE §"Hypotheses" 5: code facts C1-C6 (R-STEP5 §0)** | **not listed** (N-5) |
| **REFEREE §"Hypotheses" 3: "(α) for Theorem A (its premise 'closed'), and Case B (GAP-K'): open"** | (c) is conditional on "closed" and Scope says GAP-K is open; **(α) and Case B are not named** (N-5) |
- G-3 (FAIL, required). The header "Gaps (union; all closed in the reports, to be imported into the author's text)" is false
  for G-R5-8, which reads "Dependencies checked in outline only for this use ... Nothing Lean-checked". Fix (as for R4):
  "Gaps (union): G-R5-1..7 closed in the reports, to be imported into the author's text; G-R5-8 lists dependencies checked in
  outline only."

## 4. Re-runs
- Pinned Oink 8fbf0a7 on docs/referee-2/R2-PROVED2/k5.pg (trunk blob d1081f2 = 581902f's), `--dtl --no-single --no-wcwc
  --no-loops -v`: "found 1 dominions and 0 tangles; solved in 1 iterations; solution verified (4 strategies)", exit 0.
  This matches the draft's "1 iteration, verified".
- REFEREE bthr_probe.py @ 88d8e4c, every .pg under experiments/ (254 files; n ≤ 80 run):
  - oink {'T': 3847, 'b_shape': 0, 'contained': 8059} (65 s);
  - stable {'T': 3768, 'b_shape': 0, 'contained': 7880} (54 s).
  These equal R-PROVED2 (b): 3,847 / 3,768 T pieces, 8,059 / 7,880 tangles, 0 shape-(b) cases.
- REFEREE fdl_random.py @ 88d8e4c, args `4 14 1500`: oink "transitions 293 violations 0"; stable "transitions 293
  violations 0" (8 s each). These equal R-PROVED2 (h): "0 in 293 + 293 transitions".
- REFEREE-2 probe @ 581902f:
  - Build: dtl_probe2.patch on Oink 8fbf0a7. Its only removed lines are rewritten forms carrying the same statement plus
    counters and dumps: the ins loop with R2_REV, `if (already_exists) {`, `tpr.push_back(pr);`, `CurR = R;`, and
    `if (n_candidates == 0) return 1;` with an R2_DUMP print. Release build.
  - Run: corpus, 2 in-orders × relabel seeds 0-1, with R2-STEP5's run.sh, paths changed only. relabel.py fails on 2 files
    for seed 1 ("ValueError"), and the script skips those, as in the original count.
  - Result: runs 1014, no-probe-line 0; dup 6, dup_same 0; all STEP5 counters 0 violations (m1 35,300; P 19,102; tangles
    14,283; dom_str 2 = strfam_S5_n46 stable).
  - probe2_results.txt says "corpus runs 1014 duplicate events 6 same-search duplicates 0". Reproduced.
  - Not re-run: climbdup.py (6 × 1,500 mutants).

## Notes (non-blocking unless noted)
- N-1. (e)'s gloss "a learned tangle meets W_{1-p} ..." is GAP-C §2's map line. The lemma itself is about C_τ, the SCC
  extracted at a closed top, which may also be a dominion or a duplicate. Suggest "the SCC C_τ extracted at a closed top
  meets W_{1-p} only ...".
- N-2. (g): define D ("D = number of dominion-finding searches, ≤ n", GAP-A-M §21c) and cite GAP-A-M §21c next to C5-DTL
  141-142. The C5 lines only show the non-interleaved loops.
- N-3. (j): REFEREE signed with its own reading (an LRN transition at R is one where DV*_R moves; independent of (h)).
  REFEREE-2's reading (first-difference context R and DV*_R changes) defines a subset of those, and REFEREE-2 §13.4 says
  both agree on (j). So "with REFEREE-2's reading" is covered by both signatures. Optionally add "(REFEREE: any DV*_R
  change)".
- N-4. REFEREE (k) writes "Priorities are renumbered to ≤ n at step 0 (L26)". Under L26 / C3e the parser's renumbering
  gives priorities ≤ 2n + 2, which REFEREE-2 states correctly ("consecutive values"). The bit-cost conclusion is unchanged
  (O(log n) bits). This is a slip in the signed text, not in the draft.
- N-5 (recommended). Add to G-R5-8 "code facts C1-C6 (R-STEP5 §0)", and name "(α) and Case B (GAP-K') open" (REFEREE
  hypotheses 3 and 5) next to the Scope line's GAP-K.
- N-6. k5.pg has priorities {2, 3, 4, 5} with n = 4, so it is outside TARGET's {0..n} as written (5 > 4).
  - Oink's parser renumbering leaves these values unchanged: the least is 2, even, so it maps to 2, then 3, 4, 5.
  - TARGET's compression would give {0, 1, 2, 3}.
  - Both maps preserve order and parity, so the finding stands either way. REFEREE §C3 checked it after compression.

## Fix list
1. Required: G-3, the gap header.
2. Recommended: N-2 ((g) definition of D and citation), N-5 (dependencies C1-C6; (α)/Case B open).
3. Optional: N-1, N-3.
After these, CHECKER re-diffs the draft text only. The re-runs stay valid while 88d8e4c, 581902f and Oink 8fbf0a7 are
unchanged.
