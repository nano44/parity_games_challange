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

# Handover check: L-RED (successor 7, Opus 5.5 per owner D8; written 2026-10-18 02:00Z by date -u)
Predecessor: successor 6 (session_01Kf25QZtGKPk1nizXDPFsuJ), parked at l-red 9a4b739 (box 9 END, R38).

## 1. Branch, head, distance to trunk
- Branch claude/l-red. Container start: local HEAD 5a30e98, origin/claude/l-red 9a4b739 (stale-branch trap again).
  Fast-forwarded to 9a4b739; it was 0 ahead / 185 behind trunk origin/claude/vibrant-johnson-nxvvxo (cc59eb8).
  Merged trunk with merge commit e81142d (no conflicts): 1 ahead / 0 behind
  (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`). This check commit makes it 2 ahead;
  the pushed head is reported to the Lead by SHA.

## 2. Open work and the next step of each
Nothing running (ps: no dtl_rootmono; predecessor stopped all climbs 01:48Z; its scratchpad is gone). Oink build started
(scripts/setup_oink.sh, background). Box 10 queue (Lead plan); nothing starts before GO:
- (1) Lag gadget (serialized pieces; R37 addendum, R38): Odd-parity clock delaying closing dominions + gate starting copy
  U two searches late, u^L -> w^U interleave, priorities p -> 40p + (p mod 2). Next: read R37 addendum and L-ALG's
  dtl_stealdepth.py / dtl_prefexits.py / dtl_rootmono.py (unmodified, detached l-alg worktree as LALG_DIR), rebuild
  the predecessor's ctxtrace, then build a 2-copy lag on stealonce_both_n45 / ctx6_n20 and measure depth, exits per
  (step, vertex), first-difference contexts per transition, both orders.
- (2) If infeasible: a precise necessary condition (R37 style) for the lag. Next: only after (1) fails on design.
- (3) Long-phase FIRED-R with multi > 0 (a tangle firing only at a later visit). Next: only if (1)-(2) finish early.

## 3. docs/GAPS.md rows I own
- None. On trunk cc59eb8: GAP-A and GAP-C are owned by L-ALG "(L-RED attacks)", blocker, open; G-STR and G-DOM are
  L-ALG "(L-RED attacks)", closed. L-RED attacks GAP-A via (CTX+) (box 10) and GAP-C.

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25-26, 96-97; index row D1 "active"):
   > - A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   >   claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > - Never publish, post, email, submit or contact anyone outside the fleet. Anything external is
   >   my decision.
2. D7 (docs/DECISIONS.md line 105; index row D7 "active"):
   > a
   (Q9 option (a): continue at the current spend rate; stop at once on overage.) So no climb outlives my box.
3. D8 (docs/DECISIONS.md line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   CORRECTION (Lead 02:09Z): L32 (index "active", a Lead reading) is the GAP-A reassessment criterion ("progress means
   ONE named statement with a proof route"). The rule that an incorrect run or a super-polynomial family goes to the
   Lead at once comes from CLAUDE.md and TARGET.md, not from L32. (Same slip in the successor 6 section above: history.)

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (bit again at this start): stale local branch (local 5a30e98, origin 9a4b739). Check: `git fetch origin
  claude/l-red` then `git rev-parse HEAD origin/claude/l-red` must agree before any edit (fast-forwarded here).
- Also guarded: killed climbs leave dtl_rootmono orphans with ppid 1; after every kill run
  `ps -eo pid,ppid,args | awk '$2==1 && /dtl_rootmono/'` and kill those PIDs in a separate call (never pkill -f).

# Handover check: L-RED (successor 8, Opus 5.5 per owner D8; written 2026-10-18 08:58Z by date -u)
Predecessor: successor 7, parked at l-red 839b76d (box 10 END, R39 lagfam).

## 1. Branch, head, distance to trunk
- Branch claude/l-red. Container start: local HEAD 5a30e98, origin/claude/l-red 839b76d (stale-branch trap again,
  1840 commits behind). Fast-forwarded to 839b76d. It was 0 ahead / 90 behind trunk origin/claude/vibrant-johnson-nxvvxo
  (bb566c3, "LEAD-STATE: 07:03Z sweep"). Merged trunk with merge commit d5c3132 (no conflicts): 1 ahead / 0 behind
  (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`). This check commit makes it 2 ahead.
- Trunk does NOT yet carry e4cd13f (D13): fetched twice (08:56Z, 08:57Z); `git cat-file -t e4cd13f` fails; no D13 or L34
  row in docs/DECISIONS-INDEX.md or docs/DECISIONS.md. I fetch again and merge it after GO.

## 2. Open work and the next step of each
Nothing running (ps: no dtl_rootmono, no oink). Pinned Oink rebuild started (scripts/setup_oink.sh, background). Box 11
queue (predecessor's SUCCESSOR QUEUE + Lead plan); nothing starts before GO:
- (1) (CTX⁺) serialized contexts. Next: build a game whose -1 branch recursion has a NONEMPTY subgame (search_rec depth
  >= 1) and check it with experiments/red/lag/srtrace.py; then a relay copy with its own clock inside a lower depth-0
  context, root call unchanged; measure first-difference contexts per transition (dtl_rootmono.py + ctxtrace), both orders.
- (2) Long phase at one context with state-dependent NEW tangles (B_j = {T_j} + t_j per relay configuration). Next:
  only after (1) has a nonempty -1 subgame piece to reuse; target #fired⁺(R) per phase above degree 3.
- (3) If (1)/(2) infeasible: a precise necessary condition in R37 / R39 §9 style, for L-ALG.
- REFEREE-2 faithfulness check of dtl_stealdepth / dtl_prefexits on lagfam: with the Lead; I answer questions from
  experiments/red/lag/.

## 3. docs/GAPS.md rows I own
- None. On trunk bb566c3: GAP-A and GAP-C are owned by L-ALG "(L-RED attacks)", blocker, open; G-STR and G-DOM are
  L-ALG "(L-RED attacks)", closed. Box 11 attacks GAP-A via (CTX⁺) and (LONG-PHASE).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25-26 and 96-97; index row D1 "active"):
   > - A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   >   claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > - Never publish, post, email, submit or contact anyone outside the fleet. Anything external is
   >   my decision.
2. D7 (docs/DECISIONS.md line 105; index row D7 "active"):
   > a
   (Q9 option (a), as recorded on line 106: "Continue at the current rate. We pause automatically if the cap is hit and
   stop at once on overage.") So at most 2 heavy jobs, and no climb outlives my box.
3. D8 (docs/DECISIONS.md line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   (Work in this box is labelled Opus 5.5 in notes/L-RED.md.) Not owner rulings, but binding Lead readings: L22/L26
   (a failure under either order datum refutes a statement about A_DTL) and L32 (GAP-A reassessment criterion).

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (bit again at this start): stale local branch (local 5a30e98, origin 839b76d). Check: `git fetch origin
  claude/l-red` then `git rev-parse HEAD origin/claude/l-red` must agree before any edit (fast-forwarded here).
- Also guarded: killed climbs leave dtl_rootmono orphans with ppid 1; after every kill run
  `ps -eo pid,ppid,args | awk '$2==1 && /dtl_rootmono/'` and kill those PIDs in a separate call (never pkill -f).

# L-RED successor 9 handover check, 2026-10-18 20:52Z (date -u) (produced on Opus 5.5, owner D8)

## 1. Branch, head, ahead/behind trunk
- Branch claude/l-red. On arrival the local branch was STALE (local 5a30e98, origin 4b12770b); fast-forwarded to
  origin/claude/l-red 4b12770b. At 4b12770b: 6 ahead, 88 behind trunk origin/claude/vibrant-johnson-nxvvxo 1b6f6924
  (`git rev-list --left-right --count origin/claude/l-red...origin/claude/vibrant-johnson-nxvvxo`).
- Merged trunk 1b6f6924 with a merge commit (no rebase): head 6a7076c2, 7 ahead, 0 behind. This check commit makes it 8 ahead.
- First push (20:58Z) was REJECTED: the predecessor pushed 8451b455 (marginclimb.py MC_RE mode, committed 20:45Z) to
  origin/claude/l-red after my first fetch. Fetched and merged it with a merge commit (no rebase). After that merge and this
  edit the branch is 11 ahead, 0 behind trunk 1b6f6924.

## 2. Open work and the next step of each
Nothing running (ps: no oink, no dtl_*, no climbs). Pinned Oink rebuild started (scripts/setup_oink.sh, background).
Box 14 plan (Lead); nothing starts before GO:
- (1) FIRST: attack (XCTX@p0) and (CHAIN-CHANGE) on 𝒞^1P (one-player games, opponent out-degree 1, distinct priorities).
  Next: fetch claude/l-alg, quote the exact statements of GAP-A-M §33 (and §34 (TREE-PIECE⁺)) with the l-alg SHA, find
  L-ALG's checker and class checker; then search inside 𝒞^1P (exhaustive small n, then structured one-player conversions of
  ctx13_n40 / nest4_n80 / lagfam), checking every candidate with the UNMODIFIED checker in both orders.
- (2) THEN: compounding counter with cross-copy carry tangles (R41 §5) against (TREE-PIECE⁺), checked with l-alg
  b12_ident.py TREE=1 PLUS=1, unmodified. Next: design two copies whose carry tangle spans both copies, so the interval-product
  obstruction of R41 §5 does not apply.
- (3) If (1) or (2) is infeasible: a precise necessary condition (R37 / R39 §9 / R41 §8 style).

## 3. docs/GAPS.md rows I own
- None. On trunk 1b6f6924: GAP-A and GAP-C are owned by L-ALG "(L-RED attacks)", blocker, open; G-STR and G-DOM are
  L-ALG "(L-RED attacks)", closed. Box 14 attacks GAP-A on 𝒞^1P.

## 4. The three owner rulings that most constrain me (verbatim, from docs/DECISIONS.md), with their DECISIONS-INDEX status
1. D1 (docs/DECISIONS.md lines 6-7; index row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
2. D13 (docs/DECISIONS.md line 229; index row D13 "active"):
   > Keep working on the dtl and also c
   (Lead reading L34, not an owner ruling: L-RED continues as the DTL adversary at the D7 rate.)
3. D8 (docs/DECISIONS.md line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   (Work in this box is labelled Opus 5.5.) Binding Lead readings, not owner rulings: L22/L26 (a failure under either order
   datum refutes a statement about A_DTL), L34.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (bit again at this start): stale local branch (local 5a30e98, origin 4b12770b). Check: `git fetch origin claude/l-red`,
  then `git rev-parse HEAD origin/claude/l-red` must agree before any edit (fast-forwarded here).
- Second trap (box 11): Lead messages arrived up to 3.5 h late. Check: ReadNotifications at every check-in, after every long
  wait and after every push.

# L-RED successor 10 handover check, 2026-10-19 03:07Z (date -u) (produced on Opus 5.5, owner D8)

## 1. Branch, head, ahead/behind trunk
- Branch claude/l-red. On arrival the local branch was STALE (local 5a30e98, origin/claude/l-red 878fd1a2, 2352 behind).
  Fast-forwarded to 878fd1a2 (0 local commits to keep). At 878fd1a2: 0 ahead, 58 behind trunk
  origin/claude/vibrant-johnson-nxvvxo 7710c0e1 (`git rev-list --left-right --count`).
- Merged trunk 7710c0e1: git fast-forwarded (l-red had no commits trunk lacked), so no merge commit was needed; no rebase.
  Head 7710c0e1, 0 ahead, 0 behind. This check commit makes it 1 ahead, 0 behind.

## 2. Open work and next step of each item
- (1) R48 §4 (box 16 target): does a −1 piece's own outcome rise ever feed a SHALLOWER −1 piece (carries chaining through
  intermediate levels)? Next step: on nest3_n20 / nest3_n24 (experiments/red/xctx/instances/), log per search which piece's rise
  feeds which (tlog.py), then either climb for NEST* ≥ 4 with a chain-through fitness (nestclass.py STAR=1 pattern) or
  read dtl.cpp for the mechanism that forbids it. Waits for GO.
- (2) CHECKER C19 / referee questions on R46/R47 via the Lead. Next step: answer when routed. R46 §1-§3 and R47 §1-§5 are FROZEN
  (pinned 01d63d7 / da63c40); corrections go in new sections only.
- (3) Adversarial check of any proof route for (NEST*-BOUNDED) that appears (dommono.py / lexrand.py pattern). Nothing to do yet.
- Nothing running (no climbs started this session).

## 3. docs/GAPS.md rows relevant to me
- GAP-A (blocker, L-ALG; L-RED attacks): open. On 𝒞^1P the refereed reduction R16 draft (awaits CHECKER C19):
  GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED); class best NEST* 3 (R48).
- GAP-C (blocker, L-ALG; L-RED attacks): open (completeness; needs a cross-search progress measure).
- G-FDL, G-STR, G-DOM: closed (used as signed inputs).

## 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md)
1. D13 (line 228; index row D13 "active"):
   > Keep working on the dtl and also c
   (Lead reading L34, active: L-RED works on a long phase at one context and serialized contexts.)
2. D7 (line 105; index row D7 "active"):
   > a
   (Q9 (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.")
   So at most 2 heavy jobs, and no climb outlives my box.
3. D8 (line 161; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   (Work in this box is labelled Opus 5.5 in notes/L-RED.md.)

## 5. One trap that bit this lane, and the check that now prevents it
- Trap: editing referee-signed text after its pin (successor 9 changed the K constant in R46 §1/§3 after pin 01d63d7; a referee
  caught it). Check: before any edit to docs/red/R46-R48, `git diff 01d63d7 -- docs/red/R46-nest-bound.md` and
  `git diff da63c40 -- docs/red/R47-chainkeep.md` limited to §1-§3 / §1-§5 must stay empty; new material goes in new sections
  and is flagged to the Lead.
- Also (bit again at this start): stale local branch; `git rev-parse HEAD origin/claude/l-red` must agree before any edit.

# L-RED successor 11 handover check, 2026-10-22 05:24Z (date -u) (produced on Fable 5.1, Lead reading L36)

## 1. Branch, head, ahead/behind trunk
- Branch claude/l-red. On arrival the local branch was NOT stale: after `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`,
  `git rev-parse HEAD origin/claude/l-red` both gave a5274bd6 (0/0 by `git rev-list --left-right --count HEAD...origin/claude/l-red`).
- At a5274bd6: 3 ahead, 2 behind trunk origin/claude/vibrant-johnson-nxvvxo b41d57b4 (merge-base 4f73e7a6; the 2 trunk commits are
  the Lead's ae3ddce4 merge of box 18 and b41d57b4 NOW/LEAD-STATE bookkeeping; the 3 l-red commits are the predecessor's merge
  f4cc51d7 and the notebook handover 95a9b445, a5274bd6).
- Merged trunk b41d57b4 with a merge commit (no rebase): head 25985b22, 4 ahead, 0 behind. This check commit makes it 5 ahead.

## 2. Open work and the next step of each
- Nothing running on arrival (ps: no oink, no dtl_*, no climbs, no python). Pinned Oink is not built in this fresh container;
  `scripts/setup_oink.sh` started in the background (log in scratch), needed by experiments/red/nest16/kcheck.sh.
- Box 19 target = notes/L-RED.md NEXT option (a); nothing starts before GO:
  - (1) Per-search piece map of nest6min_n75 (e2c0d57f…, oink order). Next step: for each of the 25 searches, dump the depth-0 chain
    with each piece's vertices, rank and part label (parts 0-25 near4, 26-45 chainfail, 46-48 climb-added, 49-74 oseg) with
    ../xctx/tlog.py + partmask.py (L-ALG code unmodified); then name the piece holding the innermost open window of the witness
    0 ⊃ 1 ⊃ 7 ⊃ 8 ⊃ 16 ⊃ 17 (positions 16/17 at P indices 9-12) and the enclosing 8- and 7-windows; then the tangles learned and
    their escape vertices against the edges 23→73, 55→27, 64→15 (R50 §8b).
  - (2) Then hand-build a GATE + RETURN pair (R50 §8d) for a fourth part on k4seed_c1_n82 (37c93f21…) or nest6min_n75 ⊎ a part with
    n ≈ 10-12, aiming at NEST* 7 without a climb. Next step after (1): pick the gate vertex from the map, move its priority into the
    band, add return edges into the parts carrying the enclosing levels; score with table.py in BOTH orders, verify every candidate
    with pinned Oink (kcheck.sh), pin sha1s. At most 2 parallel jobs.
  - (3) Standing: CHECKER / referee questions on R49 / R50 if the Lead routes them (R49, R50 are DATA, unrefereed). Frozen: R46 §1-§3,
    R47 §1-§5, R49 §1-§8, R50 §1-§8d; new sections only.

## 3. docs/GAPS.md rows I own
- G-NEST (major, owner "L-RED (attacks + proof attempts); L-ALG successor if any"): OPEN. (NEST*-BOUNDED): NEST* ≤ c on 𝒞^1P.
  GAPS text says class best NEST* 3 → 5 (box 16); the notebook / R50 §6 have NEST* 6 at k = 3 (nest6_n75, nest6min_n75, nest6x_n75,
  Lead re-ran nest6_n75) and 6 with no 7 at k = 4; the row's update to 6 is the Lead's (docs/*.md). No family, no growth law,
  not refuted, no proof route.
- Relevant but owned by L-ALG "(L-RED attacks)": GAP-A (blocker, open; on 𝒞^1P reduced to (NEST*-BOUNDED) by RESULTS R16),
  GAP-C (blocker, open). G-STR, G-DOM, G-FDL: closed (signed inputs).

## 4. The three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with their DECISIONS-INDEX status
1. D1 (docs/DECISIONS.md lines 6-7; index row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   (Any NEST* 7 candidate stays DATA until re-run by the Lead / referees; a "counterexample" from unmodified tools and pinned Oink only.)
2. D13 (docs/DECISIONS.md line 229; index row D13 "active"):
   > Keep working on the dtl and also c
   (Lead readings L34 and L36, not owner rulings: L-RED continues as the DTL adversary; new sessions start on Fable 5.1 until the
   owner answers Q18; no Opus referee signatures after the reset.)
3. D7 (docs/DECISIONS.md line 105; index row D7 "active"):
   > a
   (Q9 option (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.") So at most
   2 heavy jobs, and no climb outlives my box. D8 (Opus until the reset, "active" in the index) no longer applies to a session created
   after the 2026-10-21 21:00Z reset (L36 (3)); this box is labelled Fable 5.1.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (box 18, twice): three parallel Python jobs at n ≈ 75-100 killed the container (exit 137, restarts ~01:2xZ and ~04:0xZ on
  2026-10-22); scratch climbs lost steps, so the k = 4 step counts are lower bounds. Check: before launching any job,
  `ps -eo pid,etime,args | grep -c "[p]ython.*nest16"` must be ≤ 1 (so the new job makes at most 2), and results go to files,
  never to a pipe (a timeout on `| sort | head` lost the 94-union scan).
- Standing check (bit successors 8-10, not this one): `git fetch origin claude/l-red` then `git rev-parse HEAD origin/claude/l-red`
  must agree before any edit.

# L-RED successor 12 handover check, 2026-10-23 10:10Z (date -u) (Opus 5.5, D15)

## 1. Branch, head, ahead/behind trunk
- Branch claude/l-red. On arrival the local checkout was STALE: local HEAD a5274bd6, origin/claude/l-red 8acfa086 (box 23 END).
  Fast-forwarded to 8acfa086 (`git merge --ff-only origin/claude/l-red`), then merged trunk origin/claude/vibrant-johnson-nxvvxo
  1075e90c with a merge commit (no rebase): head 1d753f84.
- At 1d753f84: 6 ahead, 0 behind trunk 1075e90c (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  = 6 0; merge-base = 1075e90c). This check commit makes it 7 ahead.

## 2. Open work and the next step of each
- Nothing in flight on arrival (0 python processes). Pinned Oink not built in this container; scripts/setup_oink.sh started in the
  background (scratch log) for result verification.
- Target N8d-R2 (docs/new/N8d-single.md §0; survives boxes 22-23, R54, R55). Box 24, nothing starts before GO:
  - (1) Per-step comparison: run R2 (experiments/n8d-second/kl2fast.py) and VJ Random-Edge (experiments/red/gzeta/vj_re.py,
    experiments/si/si.py Engine, read-only) on gz2 / gz3 from the same strategy; at each state compare R2's admissible-arc set
    with VJ's improving-switch set; locate the first state where they differ and give the mechanism (Lemma 4.75 gap,
    docs/lit/T26-N8d-step3.md). Next step: read R55 §3-§4, gzeta.py, vj_re.py, kl2fast.py; write a shared strategy encoding.
  - (2) From that mechanism, a counter R2 cannot escape: a gate comparing a lower label component, or delay lanes that reset each
    lap (R55 §4). Kill criteria: mean pivots over ≥ 5 seeds super-polynomial with every output verified, or any incorrect output.
  - Closed / parked lines: k-pools NEST* (CLOSED, D15 / L37); N8a DEAD (R53, box 21).

## 3. docs/GAPS.md rows I own
- G-NEST (major, owner "L-RED (attacks + proof attempts); L-ALG successor if any"): OPEN. Class best NEST* 6 on 𝒞^1P (DATA);
  the k-pools line is CLOSED by the Lead (L37); (NEST*-BOUNDED) neither refuted nor proved.
- Attacker role (owner L-ALG, "L-RED attacks"): GAP-A (blocker, open), GAP-C (blocker, open). G-STR, G-DOM: closed.
- No GAPS row names N8d / N8a (grep: none); N8d-R2 survivals are recorded in docs/red/R54, R55 and docs/NOW.md.

## 4. The three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   (N8d-R2 surviving my boxes is not evidence of polynomiality; any kill must come from faithful, unmodified code with verified outputs.)
2. D15 (index row D15 "active"; Lead reading L37 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   (L37: L-RED is the cheap adversary; Opus 5.5; reports are information, no option questions to the owner.)
3. D14 (index row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   (The (c) lane L-NEW produces the candidates I attack, N8d-R2 included; I read its files and never edit them.)
- Also binding: D7 (index "active") "a" = continue at the current rate, stop on overage: at most 2 heavy jobs, no job outlives the box.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (box 19): fixd_stealentry.run renumbers vertices by priority, so tlog.py / partmask.py printed SOLVER indices that were read
  as file ids; R50's A/B/C attributions had to be re-read. Check: every tool that reports vertices maps back through idx[i]
  (piecemap.py, gatescan.py), and any cross-tool comparison asserts both tools see the same vertex ids on a known instance first.
  For box 24 this applies directly: before comparing R2's admissible set with VJ's improving set, assert that kl2fast and si.py
  number vertices and arcs identically on gz2 (round-trip a strategy through both encodings).
- Also bit at this start (as for successors 8-10): stale local branch; `git rev-parse HEAD origin/claude/l-red` must agree after
  fetch before any edit.

# L-RED successor 13 handover check, 2026-10-23 22:50Z (date -u) (Opus 5.5, D15)

## 1. Branch, head, ahead/behind trunk
- Branch claude/l-red. On arrival local HEAD = origin/claude/l-red = 0d0b67a1 (box 25 handover); not stale this time.
- At 0d0b67a1: 4 ahead, 12 behind trunk a4fb9957. Merged trunk origin/claude/vibrant-johnson-nxvvxo a4fb9957 with a merge commit
  (no rebase): head 6995fd92, 5 ahead, 0 behind (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  = 5 0). This check commit makes it 6 ahead.

## 2. Open work and the next step of each
- Nothing in flight on arrival (0 python processes). Pinned Oink not built in this container: scripts/setup_oink.sh started in the
  background (scratch log), needed to verify any N5 output.
- Box 26 target (after GO): N5 SSI-GLOBAL against R57 §6's kill requirement, a game meeting (R-a) two coupled honest counters and
  (R-b) no jump-ahead switch in N5's joint optimum.
  - Next step: read R57 §3-§6b, docs/new/N5-ssi-global.md (S1-S5), N5-dlm-box5.md §4 (K6), and the n = 32 seed
    experiments/red/n5/instances/sym_h16_s1.pg; with perswitch.py / n5tr.py, list at each iteration of the 55-iteration run which
    switches N5 takes that a one-step counter would withhold (the jump-aheads), and on which edge classes (counter edge, threat,
    other). That says whether R-b fails there on edges a lane could guard (C1-C3).
  - Then either a family with super-polynomial N5 iterations (Oink zlk + verify.py on every output, n5b agreeing) or a sharpened
    O4 (conjecture or partial incompatibility argument, labelled READING / PROVED).
  - L-NEW successor 8 works the opposite direction (incompatibility proof); I read its files only.
- G-NEST, N8d-R2 (DEAD, DE30 draft), k-pools (CLOSED, L37): no open work from me; CHECKER C23 may ask about R56 §4.

## 3. docs/GAPS.md rows I own
- G-NEST (major, owner "L-RED (attacks + proof attempts); L-ALG successor if any"): OPEN. Class best NEST* 6; k-pools line CLOSED
  by the Lead (L37); (NEST*-BOUNDED) neither refuted nor proved.
- Attacker role (owner L-ALG, "L-RED attacks"): GAP-A (blocker, open), GAP-C (blocker, open).
- G-N5-TIME (major, owner L-NEW; OPEN): not mine, but box 26 attacks it (R57 is L-RED's input to it).

## 4. The three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   (N5 surviving my boxes is not evidence of polynomiality; a kill needs faithful, unmodified n5.py with verified outputs.)
2. D15 (index "active"; Lead reading L37 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   (L37: L-RED is the cheap adversary, Opus 5.5; reports are information, no option questions to the owner.)
3. D14 (index "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   (The (c) lane L-NEW produces N5, the candidate I attack; I read its files and never edit them.)
- Also binding: D7 (index "active"): continue at the current rate, stop on overage; at most 2 heavy jobs, no job outlives the box.

## 5. One trap and the check that prevents it
- Trap: a game built for R-a/R-b can easily make n5.py and n5b.py disagree on "iterations" (§6b: n5b "orig" mode gave 28 vs 34 at
  n = 24), and a climb fitness read from one implementation can be an artefact of tie-breaking, not of N5. Check: every reported
  iteration count is re-run with n5b in SPEC mode and must match exactly; the region/strategy output is checked against Oink zlk
  + verify.py (and, on counter_m N = 41/42, against `--tl`, since zlk aborts there, CLAUDE.md Traps).
- Standing check: `git fetch origin claude/l-red` then `git rev-parse HEAD origin/claude/l-red` must agree before any edit;
  kill processes only by exact argv fields (`pkill -f` on a pattern in my own command line kills my shell).
