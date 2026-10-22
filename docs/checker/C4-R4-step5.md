# C4: landing gate for RESULTS R4 (GAP-C Step 5 for A_DTL, depth-0 Dom(prevV) pieces keep KT given (ACYC)) — CHECKER, 2026-10-17

Target: docs/agents/R4-draft.md on trunk 20fe2ed (not edited). Branch: claude/checker. Before starting, origin/claude/checker
(4b15364) was confirmed an ancestor of the local branch, and trunk 20fe2ed was merged with a merge commit (99dd846, no rebase).
Clean detached worktrees: referee 8c2d012, referee-2 ce37984 (`git status --porcelain` empty before and after). Code: Oink
8fbf0a7 (tools/oink/src, `git rev-parse` = 8fbf0a7). Statement sources:
- docs/alg/STEP5.md at 8f41be8 (blob 4617f29, unchanged on trunk);
- docs/alg/GAP-C.md §18g-§18k at 8f41be8 (blob ceebb34; trunk has a later blob 45db049, so the draft correctly pins 8f41be8);
- docs/referee/R-STEP5.md (referee 8c2d012, blob 79d462e = trunk);
- docs/referee-2/R2-STEP5.md (ce37984 for the verdicts, a18e9e5 for §9; trunk blob 549c72e = a18e9e5).

## Verdict: FAIL — the re-runs all reproduce; the draft's text needs four edits (one data overstatement, one false header, two wording points) and one missing dependency
| item | verdict |
| --- | --- |
| 1a REFEREE step5_probe.py @ 8c2d012, corpus, both orders | PASS: identical to the claims |
| 1b REFEREE-2 R2-STEP5 (patch + run.sh) @ ce37984 on pinned Oink | PASS: corpus part (2,026 runs) and random part (12,000 runs) identical to probe_results.txt; climb part not re-run |
| 1c pinned Oink on strfam_S5_n46, pk_viol_n20, kfirst_viol_n13 | PASS: complete and verified |
| 2 statement diff (draft vs STEP5 / GAP-C §18g-k / both referees / L26 object) | FAIL (minor): O-1 data overstatement; O-2 "all closed" header; O-3 "alone"; O-4 condition and term not as signed. The four checks the Lead named all PASS |
| 3 gap union and verdict quotes | FAIL (minor): verdicts quoted correctly; one dependency both referees name (Lemma 1.4c / standard parity-game facts) is not in G-S5-1..7 |

## 1. Exact-commit re-runs
### 1a. REFEREE docs/referee/scratch/step5_probe.py (referee 8c2d012)
Corpus: every .pg under experiments/ at 8c2d012 (254 files; the probe silently skips n > 80 and unreadable files, so 243
games are actually run). Command: `DTL_ORDER=oink|stable python3 -I docs/referee/scratch/step5_probe.py <254 files>`.
- oink: {'tangles': 3437, 'tpr_bad': 0, 'top_missing': 0, 'calls': 8323, 'ntf_bad': 0, 'fm_bad': 0, 'f1': 896, 'P': 4476, 'yz_bad': 0, 'strad': 0, 'rounds': 53033} (66 s)
- stable: {'tangles': 3378, 'tpr_bad': 0, 'top_missing': 0, 'calls': 8145, 'ntf_bad': 0, 'fm_bad': 0, 'f1': 890, 'P': 4377, 'yz_bad': 0, 'strad': 1, 'rounds': 51493} (57 s)
- Claimed: NT-f 0/8,323 and 0/8,145; YZ 0/4,476 and 0/4,377; 1 straddle. Reproduced exactly.
- The straddle is strfam_S5_n46 in stable order: that file alone gives strad 1 (stable) and strad 0 (oink), with tangles 30
  in both orders, as R-STEP5 §2 states.
- Tangle total 3,437 + 3,378 = 6,815, as R2-STEP5 §9 quotes for the first referee.
### 1b. REFEREE-2 docs/referee-2/R2-STEP5/ (referee-2 ce37984)
- Build: a copy of tools/oink/src @ 8fbf0a7; `patch -p0 src/solvers/dtl.cpp < dtl_probe.patch`; Release build with
  setup_oink.sh's flags.
- The patch's only removed lines are the ins(v) loop header of attractVertices, rewritten to iterate the same list
  forwards or (R2_REV=1) backwards, and `CurR = R;`, re-added with a counter. Everything else is added counters.
- run.sh was used with only its two scratch paths changed (SP, O).
- Corpus part, `run.sh corpus 3` (254 files × 2 in-orders × 4 labellings), agg.py output: runs 2026, no-probe-line 0;
  {'m1': 70276, 'ntf_viol': 0, 'fm_viol': 0, 'P': 37968, 'P0': 27904, 'yz_viol': 0, 'dom_acc': 4, 'dom_nonstr': 0,
  'dom_str': 4, 'acyc_viol': 0, 'tangles': 28384, 'tpr_bad': 0, 'notop': 0}; 4 runs with a straddle, all
  strfam_S5_n46 rev=1 s=0..3.
- This is identical line for line to the first block of probe_results.txt.
- Random part (gen.py seeds 1-3000, `run.sh list 1`, 12,000 runs): runs 12000, no-probe-line 0; {'m1': 103229, 'ntf_viol': 0, 'fm_viol': 0, 'P': 67160, 'P0': 65742, 'yz_viol': 0, 'dom_acc': 0, 'dom_nonstr': 0, 'dom_str': 0, 'acyc_viol': 0, 'tangles': 19901, 'tpr_bad': 0, 'notop': 0}; 0 runs with a straddle or a violation — identical to probe_results.txt's second block (3 min 22 s).
- Not re-run: the climb part (climb.py, 18,000 mutants).
### 1c. Pinned Oink (tools/oink/build/oink @ 8fbf0a7), `--dtl --no-single --no-wcwc --no-loops -v`
| instance (trunk blob) | output |
| --- | --- |
| experiments/alg/instances/strfam_S5_n46.pg (7e0642d) | found 1 dominions and 30 tangles; solved in 6 iterations; solution verified (0 strategies) |
| experiments/red/carry/instances/pk_viol_n20.pg (e96c162) | found 1 dominions and 4 tangles; solved in 2 iterations; solution verified (11 strategies) |
| experiments/red/carry/instances/kfirst_viol_n13.pg (79e53f3) | found 2 dominions and 6 tangles; solved in 5 iterations; solution verified (4 strategies) |
All three are complete (Oink's verifier accepts the full solution; exit 0).

## 2. Statement diff
### The Lead's four named checks: PASS
- Scope stops at depth-0 P pieces: "Scope: depth-0 P pieces of one search only." Both referees say the same (R-STEP5 §6.7;
  R2-STEP5 header: "Outside these five claims and not refereed: FM+ as a separate row, KT-STEP-first, the S and T steps
  (18i, 18j), (K-in)").
- (ACYC) listed as open: the title says "given (ACYC)", and G-S5-6 is "OPEN hypothesis (ACYC) ... DATA only". Both referees
  say so (R-STEP5 §6.1; R2-STEP5 §8).
- G-S5-5 (edges of G') appears, with REFEREE-2's consequence ("whole-game edges make P-KT (4) false"). R2-STEP5 §2 G1:
  "P-KT step (4) ... fails at such a vertex".
- No "step 4 passed" / "completeness" claim: the title says "(not M3, not a step-4 pass)"; Scope says "(K-in) and GAP-C
  as a whole, are NOT established ... Gauntlet step 4 stays open."
- Object: "A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26)". This
  matches L26 (DTL-proof §0 at l-alg e144992, every ω) and both referees' object lines. REFEREE adds that every signed
  statement "uses no order-specific choice ... it holds for every ω".
### Claim by claim (draft vs STEP5 §3 / GAP-C 18g-18k vs signatures)
| draft | source / signed | |
| --- | --- | --- |
| (1) KT(R) definitions; KT(G') holds when D ≠ ∅; KT(R_end) fails | STEP5 KT0; GAP-C 18g; REFEREE (1) SIGN; REFEREE-2 (1) SIGN WITH GAPS (G1) | matches |
| (2) Lemma NT-f: the final pruning round of a −1 call accepts no stored tangle | STEP5 NT-f row, verbatim in substance (the draft omits "in its region loop"; the rescue loop is a different loop) | matches; suggest "in its region loop" |
| (3) FM (Z_f ⊆ Z^r for every round r of a −1 call) and WM, as consequences of NT-f | STEP5 "FM, WM": Z_f ⊆ Z^r ⊆ A^r_t | matches; WM is named but not defined in the draft (suggest "WM: Z^r ⊆ A^r_t") |
| (4) the (YZ) reading of dtl.cpp 961-976, and (YZ) ⇐ (ACYC) | STEP5 YZ-read (961-976) and §6.1; REFEREE (4) SIGN + SIGN WITH GAPS; REFEREE-2 (4) SIGN WITH GAPS | matches |
| (5) Lemma P-KT: a depth-0 Dom(prevV) piece never breaks KT, given (YZ) | STEP5 P-KT: "at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds ..., witnessed at level c1"; REFEREE-2 §8: "P-KT at every depth-0 P piece with D ∩ R ≠ ∅" | O-4 |
| "Hence: ... given (ACYC) alone." | REFEREE-2: "(ACYC) ... is the only hypothesis between the signed chain and ..."; both also list cited dependencies | O-3 |
### Overstatements and wording (exact diffs)
- O-1 (data; must fix). The Data bullet says "the only straddling Dom firing is strfam_S5_n46 stable order". REFEREE-2's
  climb runs produce many straddling firings: R2-STEP5 §7 says "The climbs produce many straddling firings, and never a
  cyclic new part or a YZ failure"; the table row says "firings kept: last accepted states score 20, 6, 4, 24, 1, 6". Only
  the corpus has the single firing.
  Fix: "... the only straddling Dom firing in the 254-file corpus is strfam_S5_n46 stable order (both referees ...); REFEREE-2's
  climbs from it produce many straddling firings, all with an acyclic new part and Y_0 = Z_f."
- O-2 (gap header; must fix). "Gaps (union, all closed in the reports; to be imported into the author's text):" is followed
  by G-S5-6 "OPEN hypothesis (ACYC)" and G-S5-7 (dependencies checked "only for this use"). That is not "all closed".
  Fix: "Gaps (union): G-S5-1..5 closed in the reports, to be imported into the author's text; G-S5-6 open; G-S5-7
  dependencies."
- O-3 (wording). "given (ACYC) alone": the chain also rests on the cited dependencies of G-S5-7 (and of the missing item
  of §3). Suggest "with (ACYC) as the only open hypothesis", which is REFEREE-2's wording.
- O-4 (wording; signed form). Draft (5) and the title say "a depth-0 Dom(prevV) piece never breaks KT". The signed form is
  "at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds".
  - The two agree in substance: KT(R) needs D ∩ R ≠ ∅, so "KT(R) ⇒ KT(R \ Y_0)" is implied.
  - But "P piece" is the defined term (STEP5 §2: best_vertices returned −1 with V = prevV and the threshold scan 898-912
    found nothing). "Dom(prevV) piece" is defined nowhere in the draft.
  - Suggest: "(5) Lemma P-KT: at every depth-0 P piece (−1 return, empty threshold scan; Dom(prevV) removal, dtl.cpp
    961-991) with D ∩ R ≠ ∅, KT(R \ Y_0) holds, given (YZ)". Use the same wording in the "Hence" line.
- N-1 (note). "all labelled '(Opus 5.5, D12)'": REFEREE labels each verdict cell; REFEREE-2 labels its verdict table
  heading ("## Verdicts (Opus 5.5, D12)"). That is true in substance.
- N-2 (note). "254 corpus files" for REFEREE's probe: the probe runs 243 of them (n ≤ 80 and readable). REFEREE-2's C++ run
  uses all 254.

## 3. Gap union and verdict quotes
Verdicts: the draft's lines match both tables exactly.
- REFEREE: (1)-(3) SIGN; (4) "(YZ) reading: SIGN ... (YZ) ⇐ (ACYC): SIGN WITH GAPS"; (5) SIGN WITH GAPS.
- REFEREE-2: (1), (2), (4), (5) SIGN WITH GAPS; (3) SIGN; comparison §9 at a18e9e5.
- Independence: REFEREE "docs/referee-2/ was not read"; REFEREE-2 header "Not read before this report was pushed:
  docs/referee/". No REJECT in either.
| referee item | in draft |
| --- | --- |
| REFEREE F2.1 / REFEREE-2 G2 (Lemma 1.5a for NT-f (D)) | G-S5-1 |
| REFEREE G4.1 (both inclusions of (iii), least fixed points, tangle retrial) | G-S5-2 |
| REFEREE G4.2 / REFEREE-2 G3 (trigger case) | G-S5-3 |
| REFEREE G5.1 / REFEREE-2 G4 (c1 = 0) | G-S5-4 |
| REFEREE wording note (claim 1) / REFEREE-2 G1 (edges of G') | G-S5-5 |
| (ACYC) open (both) | G-S5-6 |
| REFEREE §6.3-6.5 (Lemma 1.5a, Lemma 1.2 checked only for this use; code facts C1-C6, C1 = sorted indices); REFEREE-2 §8 (O1; nothing Lean-checked) | G-S5-7 (names 1.5a, 1.2, sorted indices, O1, Lean). C2-C6 not named; acceptable, since they are the readings signed |
| **REFEREE §6.6: "Positional determinacy and D = W_p(G') for the parity game G' (DTL-proof.md Lemma 1.4c) — standard"; REFEREE-2 header: "the standard parity-game facts named in (1)"** | **missing** |
Fix for §3: add to G-S5-7 "DTL-proof Lemma 1.4c (G' is a parity game, D = W_p(G')) and positional determinacy, standard
(REFEREE §6.6; REFEREE-2 header)".

## Fix list (all in docs/agents/R4-draft.md; no referee work needed)
1. O-1: restrict "the only straddling Dom firing" to the corpus and mention the climbs' firings.
2. O-2: correct the gap header (G-S5-6 open, G-S5-7 dependencies).
3. §3: add Lemma 1.4c / positional determinacy to G-S5-7.
4. O-3, O-4 (recommended): "(ACYC) as the only open hypothesis"; the signed P-KT form with "P piece" and "D ∩ R ≠ ∅".
5. Optional: "in its region loop" in (2); define WM in (3).
After these, CHECKER re-diffs the draft text only. The re-runs above stay valid while 8c2d012, ce37984 and Oink 8fbf0a7 are
unchanged.

## C4 re-diff (CHECKER, 2026-10-17 ~09:55Z): docs/agents/R4-draft.md at trunk 6d5962d, text only
Method: word-level diff 20fe2ed → 6d5962d of the draft. Branch synced by merge commit after confirming that
origin/claude/checker is an ancestor of the local branch. No re-runs; §1 above stays valid (8c2d012, ce37984 and Oink 8fbf0a7
are unchanged).

### Verdict: PASS (one non-blocking citation note)
| item | at 6d5962d | |
| --- | --- | --- |
| O-1 straddle data | "In the corpus the only straddling Dom firing is strfam_S5_n46 stable order ...; REFEREE-2's climbs from it (18,000 runs) produce many straddling firings, none with a cyclic new part or a YZ failure (no total count kept)". Matches R2-STEP5 §7 | FIXED |
| O-2 gap header | "G-S5-1..5 are closed in the reports and are to be imported into the author's text; G-S5-6 is OPEN; G-S5-7 lists dependencies checked only for this use" | FIXED |
| O-3 | title and "Hence": "with (ACYC) as the only open hypothesis" (REFEREE-2 §8's wording) | FIXED |
| O-4 | (5) "at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds (witnessed at level c1)", the signed form (STEP5 §0 / §3; REFEREE-2 §8). P piece defined by quoting STEP5.md line 9 at 8f41be8; I checked the quote: "(the −1 branch with Q empty, dtl.cpp 961-991)" | FIXED |
| §3 missing dependency | G-S5-7 adds "positional determinacy and D = W_p(G') (DTL-proof.md Lemma 1.4c; REFEREE §6.6, REFEREE-2 'standard parity-game facts named in (1)'), standard" | FIXED |
| optional | (2) "in its region loop"; (3) "WM (Z^r ⊆ A^r_t, ...)" | DONE (note N-3) |
| Lead's exactness edits | REFEREE probe "243 of the 254 corpus files: n > 80 and one unreadable file skipped" matches my count. REFEREE-2 "254 corpus + 3,000 random/unions + 9,000 climb mutants (each in 2 in-orders), 32,026 runs" matches 2,026 + 12,000 + 18,000. The corpus and random sets are also run in 4 and 2 labellings respectively, which "each in 2 in-orders" does not mention; the total is exact | CORRECT |
| CHECKER sentence | "CHECKER C4 (checker 7d7c6fb) reproduced REFEREE's probe and REFEREE-2's corpus and random parts exactly"; "Lead and CHECKER re-ran pinned Oink: 6 iterations, verified" | CORRECT (§1 above) |
| nothing else moved | the diff touches only the lines listed; object, signature lines, G-S5-1..6 texts and Scope are unchanged from the version checked above | CONFIRMED |

- N-3 (note, non-blocking). (3) cites "WM (Z^r ⊆ A^r_t, GAP-C §18h)". §18h defines only the special case (WM_c1) and uses it.
  The general (WM), "Z_f ⊆ Z^r ⊆ A^r_t for all r, t", is stated and proved in GAP-C §18k (line 37 of that section at 8f41be8),
  and STEP5 §3's "FM, WM" row agrees. Suggest "GAP-C §18k". This does not change the claim.

The draft at 6d5962d may land as RESULTS R4. If the N-3 citation is changed, no further check is needed.
