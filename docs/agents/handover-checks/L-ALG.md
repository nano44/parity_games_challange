# Handover check: L-ALG (successor 6, written 2026-10-17T05:03Z by date -u; LANE-RESTART step 3; produced on Opus 5.5, D8/L27)
Every answer measured from the repository in this container (commands given), not recalled from notes/L-ALG.md.
Predecessor: session_01XTdnsK1p5KyoCaDSAc2evA (successor 5; last lane push 39f6111, "merge trunk into l-alg", box 5 end).
Previous check overwritten.

## 1. Branch, head, distance to trunk
- Branch `claude/l-alg`. At container start the LOCAL branch was again the old 1017502 ("L-ALG: handover notebook ...";
  `git log -1 HEAD^1` after the merge) and `git status` said "up to date with origin/claude/l-alg" before any fetch.
- After `git fetch origin`: origin/claude/l-alg = 39f6111, trunk origin/claude/vibrant-johnson-nxvvxo = 6ad923d ("RESULTS
  DE12; NOW/LEAD-STATE: L-ALG succ. 5 box end"). `git rev-list --left-right --count origin/claude/l-alg...trunk` = 0 2
  (trunk already contains 39f6111 via 9583190 "Merge l-alg 39f6111").
- Step 0: `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` = a872695. `git merge-base --is-ancestor 39f6111 HEAD`:
  ANCESTOR, so no second merge was needed. HEAD...trunk = 1 0 (merge-base 6ad923d); HEAD...origin/claude/l-alg = 3 0
  (0 behind the lane head). This file's commit makes it 2 ahead of trunk (SHA in the message to the Lead).
- tools/oink/build absent at start; scripts/setup_oink.sh started in the background (needed for Oink-order runs).

## 2. Open work and the next step of each
- DTL gauntlet step 4 (docs/alg/DTL-proof.md; statement frozen for every order datum, L26). Two open gaps:
  - GAP-C (my box). Reduced to (K-low) (GAP-C.md §12, §14, §16) plus (TW); both DATA, 0 violations (corpus, 1,500 random,
    235 disjoint unions, 1,200 interacting unions, both orders). Every rule naming the productive piece in advance is dead
    (RESULTS DE12: K-first, K4-B, FIRST-W, PEEL, S2, Cb1). Sketch GAP-C.md §17: Steps 1-3 PROVED, Step 4 SKETCH, Step 5 GAP
    (the −1 piece with Q empty removes Dom(prevV, R_i), dtl.cpp 962-991, neither p-won nor opponent-won; must be "repaid"
    by a later productive candidate inside W_p), Step 6 GAP ((α) at the candidate), secondary.
    Next step after "go": (1) write exactly what Dom(prevV, R) removes and leaves (dtl.cpp 878-991, C5 §2) with line numbers;
    (2) attempt Step 5 (repayment proof, or a counting/contradiction argument over all candidates of a search, or the precise
    failure with the smallest shape), sending each candidate lemma with its data to the Lead before proving it (L-RED succ. 4
    attacks); (3) if Step 5 closes, (TW) and Step 6.
  - GAP-A (polynomial searches): not in this box. State: (SPP) DATA, tight (spp_chain_up_n43); phases ≤ D + 2 PROVED;
    no per-phase potential survives (GAP-A-M §21, DEAD.md box 5).
- T-ALG1: deferred by the Lead. C1-C4 DEAD. IN FLIGHT: none (predecessor's climbs stopped; nothing running).

## 3. docs/GAPS.md rows owned by L-ALG
None. docs/GAPS.md at 6ad923d: the open table is empty; the closed table holds only G1 (owner L-STRUCT). GAP-A and GAP-C are
proof gaps inside lane files (docs/alg/DTL-proof.md §5, docs/alg/GAP-C.md), not GAPS.md rows.

## 4. Three owner rulings that most constrain this lane (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
1. D1 (active; DECISIONS.md line 7):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: A_DTL stays "wrong" until TARGET.md §5 passes; SCC1, B-thr, O0/O1, OPP-EXIT, Theorem A are unrefereed readings.
2. D5 (active; line 91):
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18: M4 is the primary aim; gauntlet unchanged. Constraint: Step 5 is pursued as a proof target; a negative
   outcome must name the obstruction and the smallest instance.
3. D8 (active; line 161):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus 5.5 until the Fable reset 2026-10-21 21:00Z; work labelled "produced on Opus 5.5"; referees wait.
Also binding (Lead readings): L22 (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7), L26 (frozen for every ω).

## 5. One trap that bit this lane, and the check that now prevents it
Trap (present again at this restart): the container's local claude/l-alg is the stale 1017502 and claims "up to date"
before the fetch; a merge of trunk alone would have lost the lane head whenever trunk lacks it (it bit successor 5:
71b2f4a lacked b9b3b2b). Check: after `git fetch origin`, `git merge-base --is-ancestor 39f6111 HEAD` (ANCESTOR here) and
`git rev-list --left-right --count HEAD...origin/claude/l-alg` = "3 0" (0 behind) before writing anything.
Second trap (successor 5): Lead messages read 1.5 h late. Check: ReadNotifications before every push and when idle.
Push only as `scripts/push.sh > $SCRATCH/push.log 2>&1; echo exit $?`, reading "VERIFY PASS" and exit 0 before reporting.
