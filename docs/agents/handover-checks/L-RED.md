# Handover check: L-RED (successor 4, Opus 5.5 per owner D8; LANE-RESTART step 3; written 2026-10-17 04:23Z by date -u)
Every answer measured from the repository at the time of writing (commands named), not recalled. Predecessor: successor 3
(notebook resume point 04:20Z, head 2387fd3). The previous version of this file (successor 3's check) is replaced.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container head at start: 5a30e98 (stale local ref, clean tree, "up to date" with a stale
  origin ref). After `git fetch origin`: origin/claude/l-red = 2387fd3, trunk origin/claude/vibrant-johnson-nxvvxo = acd54f1
  ("NOW/LEAD-STATE: K4-B").
- Step 0: `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> e9bf613; 2387fd3 was NOT yet an ancestor
  (`git merge-base --is-ancestor 2387fd3 HEAD` false), so `git merge --no-ff origin/claude/l-red` -> dc9e26a; now true.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 0 behind before this file's
  commit (e8c63bd, 29fcd61, 2387fd3 from l-red plus the two merge commits); 6 ahead after it. `git merge-base` = acd54f1.

## 2. Open work and the next step of each
Nothing in flight in this container: the predecessor's scratchpad (climbs 9031/9032, their bests <scr>/gb/s9011b.pg and
s9022.pg, the lalg6..lalg10 worktrees, oink-det/oink-debug builds) is LOST with the old container. Oink build started
(scripts/setup_oink.sh, background). Queue (Lead brief, matches notebook resume point 04:20Z):
- (1) gapb climbs WITH the K4-B term. Next: rebuild worktrees lalg6 57e2256, lalg7 1335713, lalg8 cf68c58, lalg9 704f8dc,
  lalg10 31fdd98 (detached, from origin/claude/l-alg); export LALG_DIR..LALG5_DIR; relaunch dtl_search.py --fitness gapb
  in both orders from the pinned seeds experiments/red/carry/instances/gapbW_dup_n20.pg (sha1 2ef690f9) and
  gapb_dup_n20.pg (sha1 2f433a31) plus deficit instances (the lost s9011b/s9022 bests cannot be used). Fitness order:
  incomplete/wrong > K-in > K-first > K4-B > LOW-W > dupW > TW > orphW > barren > dup > orphan.
- (2) Constructive GAP-K' breaker (GAP-C.md §13): W_p ≠ ∅, no dominion, first stable piece after −1 pieces with a region
  vertex in W_{1-p} (K4-B), an open lowest region (α), or a stored tangle with all escapes in X (β-1). Next: hand gadget
  where a non-p-won Dom(prevV) −1 piece removes the opponent's escapes into X; check with L-ALG's dtl_k4b.py/dtl_whichpiece.py.
- (3) Spare: (SPP) at n = 40 from experiments/red/carry/instances/spp22_oink_n40.pg (22/38, Oink order).

## 3. docs/GAPS.md rows I own
- None. Trunk docs/GAPS.md (acd54f1): the open table is empty; the closed table holds only G1 (owner L-STRUCT).
  GAP-C / GAP-K' / (K-in) / (K-first) / (K4-B) are L-ALG's (docs/alg/GAP-C.md), which L-RED attacks, not owns.

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25, 96; index row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
2. D7 (docs/DECISIONS.md#d7; index row D7 "active"):
   > a
   (Q9 option (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.")
   With D1 line 62 "On paid overage, stop the fleet and tell me.": no detached climbs outliving my box.
3. D8 (docs/DECISIONS.md#d8; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus work labelled as such; referees wait, so findings stay DATA until refereed.
   Binding Lead reading (not an owner ruling): L22/L26, the frozen DTL statement covers EVERY order datum, so a failure
   under any order refutes A_DTL; every count is labelled with its order.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap: stale local branch at container start (this box: local head 5a30e98 while origin/claude/l-red was 2387fd3; a trunk
  merge alone did not contain 2387fd3). Check: after the fetch, `git merge-base --is-ancestor <reported head> HEAD`, and
  merge origin/claude/l-red with --no-ff if false (done: dc9e26a).
- Older traps still guarded: `| head` in check.sh under pipefail (`grep -c "| head" experiments/red/check.sh` must be 0);
  pushes only as `scripts/push.sh > file 2>&1; echo $?`; kill climbs by PID in a call of their own (pkill -f self-kill).

# Handover check: L-RED (successor 5, Opus 5.5 per owner D8; written 2026-10-17 11:17Z by date -u)
Measured from the repository at the time of writing (commands named). Predecessor: successor 4 (notebook FINAL RESUME
POINT 11:06Z, head 0883016). Successor 4's section above is kept as history.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container head at start: 5a30e98 (STALE; `git status -sb` "behind 1091" after the fetch).
  `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`: origin/claude/l-red = 0883016, trunk = 2b5b14d.
- `git merge --ff-only origin/claude/l-red` -> HEAD 0883016 (= origin). Then
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 214 behind, 0 ahead
  (trunk already holds every l-red commit).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 32b311e: 0 behind, 1 ahead (the merge commit);
  2 ahead after this file's commit.

## 2. Open work and the next step of each
Nothing running in this container (successor 4's climbs were stopped 11:06Z, its scratchpad is gone). Oink build
started 11:16Z (scripts/setup_oink.sh, background). Queue = Lead box-7 plan; nothing starts before GO:
- (1) GAP-C after DE13: attack L-ALG's weakest surviving statement (docs/alg/GAP-C.md §18q/§18r, e.g. "search(p) learns a
  tangle MEETING D, or a later search of the phase learns inside D"). Next: read §18q/§18r at the current l-alg head,
  re-check kin_viol_n29 (sha1 50987098) with L-ALG's current tools, then a fitness for the new statement on top of
  experiments/red/k4b/umix.py (interacting unions, CMAX 12, NMAX 30), the sampler that found kin_viol_n29.
- (2) GAP-A box-7 candidates (docs/alg/GAP-A-M.md §22): (POS-FALL) counterexample = root call with RV and Ψ unchanged,
  no root deficit round, Φ_pos not strictly falling; and #DEF_root per phase vs n. Next: read §22 and L-ALG's tool for
  RV/Ψ/Φ_pos, wrap it unmodified as a carry/ fitness, climb in both orders.
- (3) (beta') T-piece orphan recipe, path (i) (GAP-C §18o): x of priority 0 removed by a level-0 T piece. Next: hand
  gadget from successor 4's constraint list (notes/L-RED.md, 10:20Z message).
- (4) Optional: REFEREE-2's K5' configuration t' = {x,y,u,o}, u old in Z_k (docs/referee-2/R2-P3.md §1).

## 3. docs/GAPS.md rows I own
- None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md`: GAP-A and GAP-C are owned by L-ALG with
  "(L-RED attacks)"; G-S5-6 and G-K5 are L-ALG's; closed rows G1 (L-STRUCT), G-FDL, G-Bthr (L-ALG). L-RED attacks GAP-A
  and GAP-C (both blocker, open).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25-26, 96-97; index row D1 "active"):
   > - A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   >   claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > - Never publish, post, email, submit or contact anyone outside the fleet. Anything external is
   >   my decision.
2. D7 (docs/DECISIONS.md line 105; index row D7 "active"):
   > a
   (Q9 option (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.")
   With D1 line 62 "On paid overage, stop the fleet and tell me.": no detached climb outlives my box.
3. D8 (docs/DECISIONS.md line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus work labelled as such. Binding Lead reading L32 (index "active", not an owner ruling): an
   incorrect run or a super-polynomial family is reported to the Lead at once.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (bit again this box): stale local branch at container start (local 5a30e98, origin 0883016, 1091 commits behind).
  Check: `git fetch origin claude/l-red` then `git rev-parse HEAD origin/claude/l-red` must agree (fast-forwarded here)
  before any edit; `git merge-base --is-ancestor <reported head> HEAD` before reporting a head.
- Also guarded: pushes only as `scripts/push.sh > file 2>&1; echo $?` (never piped); climbs killed by PID in a separate
  call after listing them with `ps` (pkill -f matched its own shell before).

# Handover check: L-RED (successor 6, Opus 5.5 per owner D8; written 2026-10-17 18:56Z by date -u)
Session successor 6. Predecessor: successor 5 (session_01DT8bvW9MGLgZURmnwB2JAc), handover at l-red 5a5f49e.

## 1. Branch, head, distance to trunk
- Branch claude/l-red. Container start: local HEAD 5a30e98, origin/claude/l-red 5a5f49e (local was 1339 behind; the stale
  branch trap again). Fast-forwarded to 5a5f49e, then merged trunk origin/claude/vibrant-johnson-nxvvxo (d2f7415) with a
  merge commit 994029e (no conflicts). Before this check: 5a5f49e was 5 ahead / 281 behind trunk; after the merge
  994029e is 6 ahead / 0 behind (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`).
  The head after this commit is reported to the Lead by SHA.

## 2. Open work and the next step of each
Nothing running (predecessor's climbs stopped 18:51Z; its scratchpad is gone, so its unpinned bests are lost). Oink build
started (scripts/setup_oink.sh, background). Box 8 queue (Lead plan); nothing starts before GO:
- (1) Break (STOLEN-PERM) (root DATA statement of GAP-A-M §23b: STOLEN-PERM => STAYS-MET => NO-REFIRE => STEAL-ONCE*).
  Next: detached l-alg worktree as LALG_DIR; re-check stealer_viol_n76 (sha1 714ecc0f) with unmodified
  experiments/alg/dtl_rootmono.py RM_EXCL=1 RM_PREF=1 RM_DV=0, both orders; then relaunch ROOTFIT=stay climbs (stable
  seed 23001, oink seed 23002) and build L-ALG's case C by hand: a path tangle whose escape leaves the PREFIX, so the
  prefix itself loses a stealing vertex (not DE19's upward migration of one region).
- (2) Hand-built LONG-phase (FIRED-R): SPP chain + re-visited gadget firing a new stored tangle per search; judge with
  root/firedlong.py (S >= 2|R|, >= 2 visits); best 0.455. Next: relaunch firedlong 21001/21002 from spp25_oink_n40 while
  designing the gadget; report the ratio trend against phase length.
- (3) (CTX+) n-trend (13 at n 40 and 48) and a FALL delay gadget. Next: grow ctx13_n40 with root/grow.sh at n 56/64.

## 3. docs/GAPS.md rows I own
- None. On trunk d2f7415 GAP-A and GAP-C are owned by L-ALG "(L-RED attacks)", both blocker, open; G-S5-6 is L-ALG's
  (major, open). L-RED attacks GAP-A (box 8: STOLEN-PERM, FIRED-R, CTX+) and GAP-C.

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25-26, 96-97; index row D1 "active"):
   > - A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   >   claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > - Never publish, post, email, submit or contact anyone outside the fleet. Anything external is
   >   my decision.
2. D7 (docs/DECISIONS.md line 105; index row D7 "active"):
   > a
   (Q9 option (a): continue at the current rate; stop at once on overage, D1.) So no detached climb outlives my box.
3. D8 (docs/DECISIONS.md line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L32 (index "active"; a Lead reading, not an owner ruling): an incorrect run or a super-polynomial family
   goes to the Lead at once.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap: killing a rootfit/ucompose climb leaves its dtl_rootmono subprocess alive with ppid 1, still burning CPU and
  writing (box 7). Check: after every kill, `ps -eo pid,ppid,args | awk '$2==1 && /dtl_rootmono/'` and kill those PIDs
  in a separate call (never pkill -f: it matched its own shell four times).
- Also (bit at this start): stale local branch; check `git rev-parse HEAD origin/claude/l-red` after a fetch.
