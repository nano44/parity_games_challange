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

# Handover check: L-ALG (successor 7, written 2026-10-17T17:39Z by date -u; produced on Opus 5.5, D8)
Predecessor: successor 6 (handover l-alg 526c2a0). Measured in this container, commands given.

## 1. Branch, head, distance to trunk
- Branch `claude/l-alg`. At container start the LOCAL branch was the stale 1017502 ("behind 1601" after the fetch).
  `git fetch origin claude/l-alg claude/vibrant-johnson-nxvvxo`; origin/claude/l-alg = 526c2a0; `git merge --ff-only` to 526c2a0.
- Before merging: `git rev-list --left-right --count origin/claude/l-alg...origin/claude/vibrant-johnson-nxvvxo` = 2 27
  (2 ahead, 27 behind trunk ee1b296; the 27 include L-RED firedlong.py 2486288 and ROOTFIT=stealer 5b6da4c).
- Merged trunk (no-ff, no rewrite): HEAD...trunk = 3 0 before this file's commit; `git merge-base --is-ancestor 526c2a0 HEAD`:
  ANCESTOR. This commit makes it 4 ahead, 0 behind (SHA in the message to the Lead).
- tools/oink/build absent at start; scripts/setup_oink.sh running in the background.

## 2. Open work and the next step of each
- (1) (STEAL-ONCE*) (RESULTS R11 G-R11-5) via (STAYS-MET) (GAP-A-M §23a; DATA 0 exceptions in 1,237 Oink / 1,519 stable
  relevant steals; PROVED (reading) only at round 1, step 2; (MET-MONO) KILLED). Next: the shrink-vertex analysis (per
  shrinking visit pair: which vertices leave P(σ⁺), why, and whether any is a stealing vertex of an earlier steal), then try
  to prove the steal ORDER ("a region that has stolen from a later step never afterwards loses vertices through a relevant
  steal of its own fired tangles").
- (2) (FIRED-R) (G-R11-6) on LONG phases only (L-RED filter S ≥ 2|R|, context visited ≥ 2 times, experiments/red/root/firedlong.py
  @ l-red 5b6da4c). Next: run the filter, then look for an argument or a sharp statement.
- (3) (CTX⁺) (G-R11-4), DATA max 13; only if (1) or (2) moves.
- GAP-C / (ACYC): not in this box.

## 3. docs/GAPS.md rows owned by L-ALG (trunk ee1b296)
- GAP-A | blocker | L-ALG (L-RED attacks) | open: reduced to (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R) (R11).
- GAP-C | blocker | L-ALG (L-RED attacks) | open.
- G-S5-6 | major | L-ALG | open: (ACYC), DATA only.
- Closed rows owned by L-ALG: G-FDL, G-Bthr, G-K5, G-STR, G-DOM.

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
1. D1 (active):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
2. D5 (active):
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
3. D8 (active):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
Also binding: L32 (Lead reading, active): progress = ONE named statement with a proof route; immediate stop on an incorrect run or a
super-polynomial family. D11 (active): "No contact for now".

## 5. One trap that bit this lane, and the check that prevents it
Trap (bit again at this restart): the container's local claude/l-alg is the stale 1017502; without a fetch, work and pushes would
start from a 1,601-commit-old head. Check: `git fetch origin claude/l-alg`, then `git merge-base --is-ancestor 526c2a0 HEAD`
(ANCESTOR) and `git rev-list --left-right --count HEAD...origin/claude/l-alg` (x 0, i.e. 0 behind) before writing anything.
Push only as `scripts/push.sh > $S/push.log 2>&1; echo exit $?`, reading the verify result and exit 0 before reporting.

# L-ALG successor 8 handover check (2026-10-18 01:08Z by date -u; produced on Opus 5.5)

## 1. Branch, head, ahead/behind trunk
- Branch `claude/l-alg`. At container start the LOCAL branch was the stale 1017502 ("behind 1676" after the fetch).
  `git fetch origin claude/l-alg claude/vibrant-johnson-nxvvxo`; origin/claude/l-alg = ef0ebf2 (descends from 01e5cea:
  `git merge-base --is-ancestor 01e5cea HEAD` OK); `git merge --ff-only` to ef0ebf2.
- Before merging: `git rev-list --left-right --count origin/claude/l-alg...origin/claude/vibrant-johnson-nxvvxo` = 1 135
  (1 ahead, 135 behind trunk 3001287).
- Merged trunk (no-ff, no rewrite) as b1d1969: HEAD...trunk = 2 0. This file's commit makes it 3 ahead, 0 behind
  (SHA in the message to the Lead).
- tools/oink/build was absent at start; scripts/setup_oink.sh is running in the background.

## 2. Open work and the next step of each
- (1) G23u (GAP-A-M §23u, SKETCH): D_R ≤ N_ent + D_R^thr. Next: MEASURE D_R^thr (differing consecutive visit pairs whose
  first difference is in a threshold loop or at the last region step of a round) on the corpus, mixed/cross unions and
  the DE19/DE20 instances, both orders; then try to charge those pairs to RV rises (§22r Corollary C1-C3).
- (2) (EXIT_c) (RESULTS R13 draft G-R13-4; GAP-A-M §23r gap G23r): DATA c = 2, 2 only on DE20-derived instances. Next:
  a proof attempt through the learning dynamics (why top_r(w) cannot cross a level downward a third time; R37-2: each
  event pair needs a tangle learned in between).
- (3) Only if (1)-(2) stall: (FIRED⁺-R) BELOW the root (§23s; at G′ it is (SPP), not to be retried there).
- (0) Packet 11 (§23s CHANGE-NEW) is out to both referees: when reports land, import into a NEW subsection; §23q and §23s
  stay frozen.
- GAP-C / (ACYC): not in this box.

## 3. docs/GAPS.md rows owned by L-ALG (trunk 3001287)
- GAP-A | blocker | L-ALG (L-RED attacks) | open: GAP-A ⇐ (CTX⁺) ∧ (FALL) (R9); (STEAL-ONCE*) FALSE (DE20); signed
  replacement R12: GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum), and ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D const) ∧ (FIRED-R). Not yet in the
  row: R13 draft (packet 10, awaiting CHECKER): GAP-A ⇐ (CTX⁺) ∧ (EXIT_c).
- GAP-C | blocker | L-ALG (L-RED attacks) | open.
- G-S5-6 | major | L-ALG | open: (ACYC), DATA only.
- Closed rows owned by L-ALG: G-FDL, G-Bthr, G-K5, G-STR, G-DOM.

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
1. D1 (active):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
2. D8 (active):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
3. D11 (active):
   > No contact for now
Also binding: L32 (Lead reading, active): the GAP-A reassessment criterion, progress = ONE named statement with a proof
route. CORRECTION (Lead 01:21Z by date -u): L32 says nothing about stopping. An incorrect run or a super-polynomial family is
REPORTED to the Lead at once (CLAUDE.md, TARGET.md); the fleet does not stop on it. D5 (active) on aim: pursue M4, do not call it unlikely.

## 5. One trap that bit this lane, and the check that prevents it
Trap (bit again at this restart): the container's local claude/l-alg is the stale 1017502; without a fetch, work and pushes
would start from a 1,676-commit-old head. Check: `git fetch origin claude/l-alg`, `git merge-base --is-ancestor 01e5cea HEAD`
and `git rev-list --left-right --count HEAD...origin/claude/l-alg` (x 0) before writing anything.
Second trap carried: big RM_PREF=1 union runs need ~6 GB each (4 were OOM-killed); at most 2 heavy jobs at once.
Push only as `scripts/push.sh > $S/push.log 2>&1; echo exit $?`.
