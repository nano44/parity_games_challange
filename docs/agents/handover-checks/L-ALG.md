# Handover check: L-ALG (successor 4, written 2026-10-16T15:57Z; LANE-RESTART step 3; produced on Opus 5.5, D8/L27)
Every answer measured from the repository in this container (commands given), not recalled from notes/L-ALG.md.
Predecessor: session_01BDELabbGbT2QYY2NoRCY8A (parked 15:50Z, last lane push c18eaad). Previous check (5143cc2 era) overwritten.

## 1. Branch, head, distance to trunk
- Branch `claude/l-alg`, tracking origin. At container start local = origin/claude/l-alg = c18eaad ("L-ALG: notebook stamp
  from date -u; produced on Opus 5.5"). Trunk origin/claude/vibrant-johnson-nxvvxo = b16716d ("RESULTS DE10; NOW: L-ALG end
  of box, parked").
- Before step 0: `git merge-base origin/claude/l-alg origin/claude/vibrant-johnson-nxvvxo` = c18eaad (lane head is on trunk);
  `git rev-list --left-right --count origin/claude/l-alg...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead, 278 behind.
- Step 0 merge `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` = 35e7d4f; then HEAD...trunk = 1 ahead, 0 behind,
  merge-base b16716d. This file's commit makes it 2 ahead, 0 behind (SHA in the message to the Lead).
- tools/oink/build is absent in this container; scripts/setup_oink.sh is needed before any Oink-order measurement or Oink
  verification (dtl_pyref --order oink / DTL_ORDER=oink run without it).

## 2. Open work and the next step of each
- DTL gauntlet step 4 (docs/alg/DTL-proof.md, §0 frozen for every order datum ω, L26). GAP-C open, not routed. GAP-A OPEN;
  route (H1)-(H4), GAP-A-M §12; barrier APP(k) §10; ledger §17 (PROVED items with scope C6 / A_DTL / A_DTL under M-cond;
  KILLED items with instances; DE9, DE10 on trunk).
- (H4) on A_DTL, the Lead's next-box queue (after "go", 8 h box):
  (1) a quantity bounding DEF changes at a FIXED (context, M), via the threshold phase (§13e: in 18/19 DEF pairs the region
      vector at r0−1 is identical and some W_t = lfp(U, R, t, T) grows), or the exact reason none exists. Known dead: per-
      context constant (up to 11 at n=28, Oink order, h4_def11_oink_n28), straddler chains, (C-rM), (C-rM-stable)
      (h4_def9_oink_n28: (3,8) and (9,12) repeat), injectivity of the actual return set in time (h4_def10_oink_n28 revisits).
      Next step: per DEF step at fixed (context, M), record (r0, which W_t grew, U at r0) with dtl_regvec.py on the h4_def*
      instances, state a candidate with its data first (to L-RED via the Lead), then prove or kill.
  (2) prove (CM) (child round count M never drops across a parent DEF step into an ideal-stable child context; DATA
      0/123 in GAP-A-M §13h at 14:55Z; the Lead's brief and NOW say 0/129: I take the larger count as including later
      cases and will re-measure with dtl_childM.py and write the number with its order datum) or a weaker form, from
      Lemma R (§13b) and the per-round inclusion V_i ⊆ V̂_i (§13). Next step: identify which step of the C6 Lemma S proof
      fails for the child after a parent DEF step, and whether the child's context change (Dom(prevV) of the parent
      return set) can only remove candidates whose removal cannot shorten the child's run.
  (3) measure K_parent × K_child vs n on existing instances and climbs (h4_compound_n44, h4_compound2x2_n44,
      h4_nested7_oink_n44, h4_deep_oink_n44, h4_def*), Oink order, labelled.
  Rule: any super-polynomial family goes to the Lead at once; each candidate lemma is stated with data before a proof.
- T-ALG1: deferred by the Lead, no step. C1-C4: DEAD (DEAD.md), regressions in experiments/alg/check.sh. IN FLIGHT: none
  (the predecessor's climbs died with its container; best games committed under experiments/alg/instances/).

## 3. docs/GAPS.md rows owned by L-ALG
None. docs/GAPS.md at b16716d: the open table is empty; the closed table holds only G1 (owner L-STRUCT). GAP-A and GAP-C are
proof gaps inside the lane file docs/alg/DTL-proof.md §5, not GAPS.md rows.

## 4. Three owner rulings that most constrain this lane (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
1. D1 (active):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: DTL stays "wrong" until TARGET.md §5 passes; every lemma in GAP-A-M.md is unrefereed and not a result.
2. D5 (active):
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18: M4 is the primary aim; no "M4 unlikely" framing; D1 unchanged. Constraint: GAP-A is pursued as a proof
   target; a negative outcome must name the mechanism and the instance.
3. D8 (active):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus 5.5 until the Fable reset 2026-10-21 21:00Z; work labelled "produced on Opus 5.5"; referees not
   engaged before the reset. Constraint: every notebook/doc entry of this session carries that label; no referee request.
Also binding (Lead readings, not owner rulings): L22 (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7) and
L26 (§0 frozen for every ω; changes only through the Lead and CHECKER).

## 5. One trap that bit this lane, and the check that now prevents it
Trap (08:26Z, 2026-10-16, notebook "SLIP"): the predecessor pushed b93114a with `scripts/verify.sh | tail && git push`; the pipe
replaced verify's exit status with tail's, so the push did not actually depend on the gate. Check now: scripts/push.sh (on
trunk) runs verify with output to a log and pushes only if it exits 0; I call it bare as
`scripts/push.sh > $SCRATCH/push.log 2>&1; echo exit $?` and read "VERIFY PASS" and exit 0 in the log before reporting a SHA.
Second trap kept in mind: counts in stable order ω are valid for the proof (L26) but not pinned-Oink behaviour
(h4_def5_stable_n20 has 5 DEF in stable order, 0 deficit calls in Oink order); every count I report names its order datum.
