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
