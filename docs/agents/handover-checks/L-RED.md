# Handover check: L-RED successor 23 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-26 18:56Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 22
(session_012UYPozEKit18kRxKv2gKbK), handover = notebook "Successor 22 HANDOVER" at l-red 3eab40ed.
Successor 22's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = 0d0b67a1 (stale; clean tree). `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`
  (18:53Z) moved origin/claude/l-red 0d0b67a1..3eab40ed; `git merge --ff-only origin/claude/l-red`; `git rev-parse HEAD origin/claude/l-red`
  -> both 3eab40ed421170c3dcd219456ae6e8d999e77eea.
- Trunk `claude/vibrant-johnson-nxvvxo` = e92d50c2. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at 3eab40ed
  -> 3 ahead / 114 behind; merge-base 18624c0b (R93 push; R94 + handover commits 768244af, 5be3847c, 3eab40ed not yet on trunk).
- Trunk brought in with `git merge --no-edit origin/claude/vibrant-johnson-nxvvxo` (merge commit 7d8016e1; no rebase, amend or force-push):
  4 ahead / 0 behind before this file's commit.

## 2. Open work and the next step of each
Nothing in flight (`ps -eo pid,ppid,args | grep python3`: no lane job; predecessor's IN FLIGHT: none). tools/oink/build was absent;
scripts/setup_oink.sh run 18:54Z, exit 0: "oink built at 8fbf0a7". Pins re-measured (`sha1sum`): experiments/red/n3/instances/lagx10_n40.pg
7258717c, long121_n40.pg c667c085, experiments/red/ul/instances/cxmig_k4_n54.pg a3893ea4 (= R93 table).
Planned after "go" (D18, N5; Lead brief order; ALTERNATION is the open count, docs/NOW.md line 2; EXIT_x <= phase length, R94):
- (1) Odd-minimum next-top selector (R94 design (a)): an Odd vertex of large out-degree whose sigma-bar-minimum rises one option at a time,
  as an end vertex's only top, to re-arm a Bellman-Ford wave once per fallback over one shared chain (target phase ~n^2 at fixed k).
  Next: read R94 §2 (S4c Xi-greedy blocks static-top re-arming) and N5-EXIT §8-§9, build a generator in experiments/red/, run with vrun.sh
  (n5 = n5b --mode spec, Oink); time box ~2 h; on failure a new R-file with the exact obstruction and instance.
- (2) STATIC-DEPTH gaps (docs/si/P-N5-DEPTH-box22.md): (G1) sigma-bar changes inside a global C-interval (R94's pump is linear), (G3) cyclic
  H_b at an impure end. Next: a long global C-interval at fixed k.
- (3) ALTERNATION directly: many Odd gate changes in one fallback-free run at fixed k, each not paid by a fresh vertex.

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (docs/GAPS.md line 9 after the merge).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11): every target in §2 feeds it. GAP-A, GAP-C (L-ALG, open,
  lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7, D001 key lines), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successors 16, 21): a borrowed checker narrower than its statement (L-SI threv.py stopped at the next fallback; flipck checked only
  both-intact flips), so "0 violations" could not refute the frozen statement. Check: own exact checker written from the frozen text,
  each window/threshold of a borrowed checker listed against the text, and a kill counted only with a faithful N5 run (n5b --mode spec =
  n5.py), sha1 + full start pair, and an Oink check_sol2 cross-check (vrun.sh).
- Also caught at this restart: stale clone (local 0d0b67a1, origin 3eab40ed), by fetch + `merge --ff-only` + `rev-parse HEAD == origin/claude/l-red`.

## Successor 22 section (superseded): L-RED successor 22 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-26 16:16Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 21
(session_01KAhNrh5WEvs2zMwA7VEGx7), handover = notebook "Successor 21 HANDOVER" + addendum at l-red 1dbe6d9f.
Successor 21's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = 0d0b67a1 (stale; clean tree). `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`
  (16:15Z) moved origin/claude/l-red 0d0b67a1..1dbe6d9f; `git merge --ff-only origin/claude/l-red`; `git rev-parse HEAD origin/claude/l-red`
  -> both 1dbe6d9f9aa40a69b1e68b1d7ecb628ca03b3b0b.
- Trunk `claude/vibrant-johnson-nxvvxo` = 5fcabb2a. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at 1dbe6d9f
  -> 0 ahead / 229 behind; merge-base = 1dbe6d9f (the lane head is already on trunk).
- Trunk brought in with `git merge --ff-only origin/claude/vibrant-johnson-nxvvxo` (fast-forward, no merge commit; no rebase, amend or
  force-push): HEAD = 5fcabb2a, 0 ahead / 0 behind before this file's commit (1 ahead after it).

## 2. Open work and the next step of each
Nothing in flight (`ps -eo pid,args | grep python3`: no lane job; predecessor's IN FLIGHT: none). tools/oink/build was absent;
scripts/setup_oink.sh run 16:15Z, exit 0: "oink built at 8fbf0a7". Pins re-measured (`sha1sum`): experiments/red/n3/instances/
lagx10_n40.pg 7258717c, long121_n40.pg c667c085, matching the HANDOVER.
Planned after "go" (D18, N5; Lead brief), in order:
- (1) C-ONCE (L-SI 17, docs/si/N5-GCX-box21.md). Measured at l-si f984baa0 (§4): L-SI has ALREADY recorded C-ONCE DEAD on its own
  instances cone_n65 (3e95fca9) and cone_n69 (dd03ba78), Bellman-Ford staggering between NON-direct gates (DD empty). Survivor:
  C-ONCE_X (migrations INTO a D-direct gate at most once per vertex per C-interval), DATA only; L-SI itself expects it to die.
  Next: ask the Lead which form is the live target (C-ONCE_X and the "index >= |U| - 1" clause); own exact checker from the frozen §4 text
  (not gcx.py alone); then a CONSTRUCTION: transfer cone_n65's staggering onto two D-direct gates (equal and different offsets) so a vertex
  enters a D-direct gate region twice inside one C-interval; Oink cross-check; no overlap with L-COMP 5's climbs.
- (2) QP_c long-phase side (docs/new/N5-NCONF-box48.md §11, l-new b9a6568f): a long-phase family with QP_c growing in n (not disjoint
  copies). Next: compute QP_c on long121 / long90_k2 / lagx10, then build/climb on QP_c at fixed class.
- (3) Returns without fresh content inside one fallback-free run (R89 §3, R90 §2/§5): hand-built ruler-content mkgate variant (ii).

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk 5fcabb2a docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11): N5 makes polynomially many iterations; every target in §2
  feeds it. GAP-A, GAP-C (L-ALG, open, lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (trunk docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 16 and again successor 21, box 54): a borrowed checker narrower than its statement (L-SI threv.py stopped at the next
  fallback; flipck checked only both-intact flips), so its "0 violations" could not refute the frozen statement.
  Check now: write my own exact checker from the frozen text (for C-ONCE: from N5-GCX §4's C-interval definition, every transition of
  every fallback-free run), list each window/threshold of any borrowed checker (gcx.py) against the text, and count a kill only with a
  faithful N5 run (n5b --mode spec), sha1 + full start pair, and an Oink check_sol2 cross-check.
- Also caught at this restart: stale clone (0d0b67a1, 1dbe6d9f on origin), by fetch + `merge --ff-only` + `rev-parse HEAD == origin/claude/l-red`.

## Successor 21 section (superseded): L-RED successor 21 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-26 11:45Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 20
(session_01UNywtigtQoPeTPobY4H8bC), handover = notebook "Successor 20 HANDOVER" at l-red 80ccc8fd.
Successor 20's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = 0d0b67a1 (stale; clean tree). `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo`
  (11:44Z) moved origin/claude/l-red 0d0b67a1..80ccc8fd; `git merge --ff-only origin/claude/l-red`; `git rev-parse HEAD origin/claude/l-red`
  -> both 80ccc8fde446ee61cb1bdd01010f049b64d38170.
- Trunk `claude/vibrant-johnson-nxvvxo` = fb3302f5. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at 80ccc8fd
  -> 2 ahead / 232 behind; merge-base 843d88b2 (R85). The 2 ahead: b08c8bae (R86) and 80ccc8fd (HANDOVER), not yet on trunk.
- Trunk merged into the lane with `git merge --no-ff` (cd1b17c4; no rebase, amend or force-push): 3 ahead / 0 behind before this commit.

## 2. Open work and the next step of each
Nothing in flight (`ps -eo pid,args | grep python3`: no lane job; predecessor reported none). tools/oink/build was absent;
scripts/setup_oink.sh run 11:44Z, exit 0: "oink built at 8fbf0a7" (needed for every Oink cross-check). Pins re-measured: pp_K12_n161_dual.pg f967a43d,
gate_K16_n197.pg 3eeddc86 (experiments/red/usplit/instances/), matching R84/R86.
Planned after "go" (D18, N5; Lead brief), in order:
- (1) Open core of R83-R86: release of Ξ-blocked, W-tempted edges WITHOUT fresh content (trapping both players at once). Either a family
  where unforbid-switches per run, or runs per phase, grow super-polynomially (faithful N5, SPEC S1-S5), or the precise obstruction as a
  lane lemma. Known: R86 (τ-counters need k = ω(1) Odd choice vertices), R85 (Friedmann's counter fails under S4a), R84 (re-arming without
  release). Next: read R83 §2/§4, R84, R86; try to prove "a Ξ-block re-armed without new content is never released" from S4a's Ξ optimum
  (monotone over the frozen τ), and build the counter-candidate on 𝒞^2O with mkgate + a second reader if the proof stalls.
- (2) CONJECTURE HON-FF (docs/new/P-N5-HON-box46.md §5, trunk 67a7b54d): exact checker from the frozen §5 text (Ξ-level across every
  gap between W-honest states, inside fallbacks included); seeds experiments/n5-epoch/instances/ffin12_n32, ffin5_n32, ffin4_n24 and
  lib41's j10_n24, j7_n32, j8_n32; then climb on (level drop).
- (3) CONJECTURE FRZ-RHO (docs/si/N5-RUND-box17.md §23.3, DATA, 0 violations, tightest ratio 0.87) and §24's N3 level lemma if stated:
  own exact checker, climb on the ratio.

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner "L-NEW (L-LIT T22; referees later)", **open**, line 11): targets (1)-(3) feed it.
  GAP-A, GAP-C (owner "L-ALG (L-RED attacks)", open, lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 20, R80 §0a): a near mis-claimed kill. The first U-SPLIT family changed R_D (z left R_D), so it killed L-SI §17 only as
  written, not under the stretch_D reading (stretch_D = D, R_D and gate values constant).
  Check now: list every clause of the target's definitions (not only the clause the conjecture spells out) and test each on the kill
  instance before claiming; pin with sha1 + start pair and cross-check with Oink and a second implementation (n5.py / n5b).
- Also caught at this restart: stale local branch (0d0b67a1, behind origin/claude/l-red), by fetch + `merge --ff-only` + rev-parse.

## Successor 20 section (superseded): L-RED successor 20 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-26 08:06Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 19
(session_017GDW2Qywsw52DKHPD8kAM6), handover = notebook "Successor 19 HANDOVER" + RESUME POINT at l-red 6c06792c.
Successor 19's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo` (08:03Z) moved origin/claude/l-red
  0d0b67a1..6c06792c (stale clone); `git merge --ff-only origin/claude/l-red`; `git rev-parse HEAD` -> 6c06792cbd9d25783a336ad62c4307064b5ee304.
- Trunk `claude/vibrant-johnson-nxvvxo` = 0f5ff835. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 2 ahead / 521 behind at 6c06792c; merge-base 743e4281. The 2 ahead: 6769a735 (R78 LEVEL-COUNT kill + HANDOVER) and 6c06792c
  (lcount2_n23 pin + notebook); not yet on trunk.
- Trunk merged into the lane with `git merge --no-ff` (8665e57c; no rebase, amend or force-push): 3 ahead / 0 behind before this commit.

## 2. Open work and the next step of each
Nothing in flight: the predecessor's jobs ended with its container (`ps -eo pid,args | grep python3`: no lane job). tools/oink/build
absent; scripts/setup_oink.sh started 08:04Z (needed before any kill is Oink-checked). Kill pins re-measured: lcount_n23.pg f86125a0,
lcount2_n23.pg dd9847c6 (experiments/red/h3/instances/, with .start / .start.json), matching the notebook and R78.
Planned work after "go" (D18, N5; Lead brief), in order:
- (a) Long epochs / many epochs (unbounded parts after RESULTS R63 X-EP and R64 EP-0 / EP-k / EP-1 under (Στ)). Next: add N_ep per phase
  and len(E) for epochs with |D_E| ≥ 2 as objectives in climbfr19 (ANALYSER fbr19 already reports EPOCH / N_ep 80 record), seed from
  R76 pins (lev74_n40, fr39_q4_n48) and lcount_n23; climb for extremes and kills, not distributions (L-COMP 5 box 12 does the census).
  Attack L-NEW's REC-0 (docs/new/N5-NEP-box45.md §5, l-new 40659d50): #(D = ∅ epochs per phase) ≤ (f + 1)(n + 1) + 4n(n − 1) + 1.
  Next: read §5 at that SHA, write an exact counter from its definitions, check every run, climb on count − bound.
- (b) √n growth target (R78 §3, mkalt family): offset changes per vertex per stretch_D beyond √n; trigger from the other score
  (W versus Ξ timing as in lcount_n23).
- (c) Old resume list: R74 §2.5 construction; FB-CAP |U| ≥ 3 (fcap3 never > 0); beta2 cascade (maxbeta 2, never 3).

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11): N5 makes polynomially many iterations; items (a)-(c) feed it.
  GAP-A, GAP-C (owner "L-ALG (L-RED attacks)", open, lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (trunk docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 19, twice): killing climbers with `ps | grep [c]limb... | kill` (or `pkill -f`) killed the lane's own shell (exit 144:
  the pattern is in its own command line), and a heredoc inside the killed shell was never written. Check now: print
  `ps -eo pid,args` first, kill only an explicit pid list, then confirm with `ls` that every file the step should have written exists.
- Also caught at this restart: stale clone (origin moved 0d0b67a1..6c06792c on fetch), by fetch + ff-merge + `rev-parse HEAD`.
  Related (successor 19): climbfr19 writes a _FAIL_ json per failing candidate; demote dead checks (LEVEL-COUNT now) to counters first.

## Successor 19 section (superseded): L-RED successor 19 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-26 01:00Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 18
(session_01D6HqejxBahRiMjurWjAtzT), handover = R74 + notebook RESUME POINT at l-red d3e8b47e.
Successor 18's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. `git fetch origin claude/l-red` (00:58Z) moved origin/claude/l-red 0d0b67a1..d3e8b47e (stale clone);
  `git checkout -B claude/l-red origin/claude/l-red`; `git rev-parse HEAD origin/claude/l-red` -> both
  d3e8b47ec178b55c8462c291256bb3f2d0e736c3. Clean tree.
- Trunk `claude/vibrant-johnson-nxvvxo` = 1c23106b. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 1 ahead / 54 behind; merge-base c45b888b. The 1 ahead is d3e8b47e (R74 + RESUME POINT), not yet on trunk.
- Trunk merged into the lane with `git merge --no-ff` (no rebase, amend or force-push) before this file's commit.

## 2. Open work and the next step of each
Nothing in flight: no lane job in this container (`ps -eo args | grep python`: none). tools/oink/build absent;
scripts/setup_oink.sh started 00:59Z (needed before any kill is Oink-checked). Pinned instances, sha1 re-measured, all match R72-R74:
exsw_loop_n15.pg e38329f8 (+ start 03f43926), kt6_n58.pg 41d4f7cb, cw11_n24.pg 5c6dcf2d, frzu_tight_n14.pg 46503678, kc18_n24.pg b0d34a31.
Planned work (Lead 01:0xZ brief), in order:
- (1) Adversary on P-N5-1O (docs/si/P-N5-1O-box15.md, trunk sha1 2cf5e672; pinned trunk 291c110d, an ancestor of trunk). Next: read the
  frozen text; extend fbx18 / kw18 (both take --start) into an exact checker of its per-phase bounds and iteration count on 𝒞^1O; hunt
  non-S3 start pairs (random, exhaustive at small n, climbs on iterations / phase transitions vs landed bounds R44-R48); check
  Lemma OUT's output against Oink on every run.
- (2) P-N5-DUAL (docs/new/P-N5-DUAL-box43.md, trunk sha1 a51f7c30). Next: check Lemma DUAL on our engine (N5 on G from (σ0, τ0) equals
  the mirror of N5^OF on G^d from (τ0, σ0)); hunt a phase from a non-S3 start or under Odd-first ties exceeding landed per-phase bounds.
- (3) Successor-19 resume list: R74 §2.5 construction (post-freeze kind change via a late BAND trigger of a kind-A length cascade);
  FB-CAP |U| ≥ 3 beyond the simplest chain; beta2 cascade (≥ 3 r = −1 fallbacks in one scope run; never started).

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11): N5 makes polynomially many iterations; P-N5-1O and P-N5-DUAL
  feed it. GAP-A, GAP-C (L-ALG, open, lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (trunk docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 18, notebook): Lead messages queue silently. Two (20:15Z, 21:00Z) sat unread until a 21:39Z report, so work followed a
  superseded order. Check now: ReadNotifications at every wait, before each report and before starting each planned item.
- Also caught at this restart: stale clone (origin moved 0d0b67a1..d3e8b47e on fetch), by fetch + checkout -B + `rev-parse HEAD ==
  origin/claude/l-red`. Related checker trap (successor 18): on an o = c_θ phase use G_U, not G_Û / G_U^o; run every new checker on one.

## Successor 18 section (superseded): L-RED successor 18 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-25 19:42Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 17
(session_01DJB52MMkzsddv3hXsMpos5), handover = R71 §7 addendum + notebook RESUME POINT at l-red e63003bf.
Successor 17's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Fresh container: local branch 1963 commits behind origin/claude/l-red (stale clone, clean tree).
- `git fetch origin claude/l-red` (19:41Z) -> origin/claude/l-red = e63003bf; `git checkout -B claude/l-red origin/claude/l-red`;
  `git rev-parse HEAD origin/claude/l-red` -> both e63003bf53ce7d05cab0a37604a7c8e3ea92d72a.
- Trunk `claude/vibrant-johnson-nxvvxo` = db711979. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 7 ahead / 41 behind at e63003bf; merge-base 24f3af85. R71 §0-§6 (8e429a89) is on trunk; the §7 addendum (e63003bf) is not yet.
- Trunk merged into the lane with `git merge --no-ff` (no rebase, amend or force-push) before this file's commit: 8 ahead / 0 behind.

## 2. Open work and the next step of each
Nothing in flight here: the predecessor's 8 background jobs (fbcap17 fb5r2 / fb4x2, fbpclimb17 × 4, shrink17 × 2) died with its
container (`ps -eo pid,args | grep python`: none; experiments/red/frz/out/ absent). Their logs are lost; only the pinned instances survive,
sha1 re-measured: fbcap_eq_u4_n11.pg 39beb8b8, fx2_n11.pg 9bb47bb3, fx2_n11.start.json 1a86a8e2 (all match R71 §7).
tools/oink/build is absent: scripts/setup_oink.sh must run before any kill can be Oink-verified.
Frozen targets unchanged on trunk (sha1 of `git show <trunk>:<path>`): P-N5-PFZ 3c617e06, P-N5-RHO cd5df65c, N5-NHN 81302f57,
N5-FBPOLY 7a7087f7, N5-FBPHASE f7aaa624, N5-RISE 3b8fea13. New on trunk since the predecessor's base: P-N5-PFZ-fixes, P-N5-RHO-fixes,
N5-MAP-box41, docs/si/P-N5-FX-box14, P-N5-PHI-box14, N5-LEDGER-v2-box14 (not yet read; candidates for the next route).
Open targets (RESUME POINT, R71 §6-§7):
- (a) FB-CAP kill: a phase with ≥ |U| − 1 in-phase Even fallbacks at |U| ≥ 3. Best: equality at |U| = 4 (fbcap_eq_u4_n11).
  Next: relaunch the n 5 start-pair search (fbcap17 random, new seed) and the n 4 exhaustive to completion; shrink with GMIN ≥ 2, UMIN ≥ 4.
- (b) beta2 cascade (Lead 18:16Z): ≥ 3 r = −1 fallbacks in one scope run. Not started. Next: climber objective on that count, seeded
  from beta2_n11.
- (c) FX slack 0 (best −2, fx2_n11) and THETA-AFTER slack 0 (best −1). Next: re-run fbpclimb17 OBJ=fx START=1 and check against the
  new docs/si/P-N5-FX-box14.md text before climbing (its statement may differ from N5-FBPHASE's Corollary FX).
- (d) FREEZE-EXIT: hypothesis never reached; needs (a) first.
- Also open from R71: (4) LV-NONE / SCOPE-FB (P-N5-LV2), not started; INTO wording at gate-free last states (R71 §4).

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11): N5 makes polynomially many iterations; every target in §2
  feeds it. GAP-A, GAP-C (L-ALG, open, lines 6-7; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (trunk docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 17, R71 §7 / RESUME POINT): long searches launched as background jobs live only in the container; when it ends,
  the logs (experiments/red/frz/out/, gitignored) and any unpinned best are lost. Successor 17's 8 jobs are gone in this container.
  Check now: pin every best instance into experiments/red/<box>/instances/ with sha1 and start pair as soon as it is found, commit
  summary counts (not logs) at each report, and before claiming a run's numbers confirm the log exists (`ls`, `tail`) in this container.
- Also caught at this restart: stale clone (1963 behind), by fetch + checkout -B + `rev-parse HEAD == origin/claude/l-red`.

## Successor 17 section (superseded): L-RED successor 17 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-25 16:41Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 16
(session_014kwWmBLu9B31iceFsng38k), handover = R70 + notebook RESUME POINT at l-red 9589ffa3. Successor 16 wrote its own check
into notes/L-RED.md ("Handover check (successor 16)"); successor 15's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Fresh container: local branch 1703 commits behind origin/claude/l-red (stale clone, clean tree).
- `git fetch origin claude/l-red` (16:39Z) -> origin/claude/l-red = 9589ffa3; `git reset --hard origin/claude/l-red`;
  `git rev-parse HEAD origin/claude/l-red` -> both 9589ffa3b36d20485bffd7f5b647087e6ae986d5.
- Trunk `claude/vibrant-johnson-nxvvxo` = f7b6e688 (16:34Z). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 4 ahead / 106 behind; merge-base d7df76f9. The 4: 859c137a (trunk merge), 2d9cd5f7 (lv16), 63ff3fe8 (R70 draft), 9589ffa3 (R70 final).
  Trunk merged into the lane with `git merge --no-ff` (no rebase, amend or force-push) before this file's commit.

## 2. Open work and the next step of each
Nothing in flight (`ps aux`: no lane job; the predecessor's scratch logs died with its container; verified bests are in
experiments/red/so/instances/, sha1 re-measured: nleq_cex_n48 e72e4034, tevlast_cex_n40 ff1e9cb4, tev_cex_n40 17078f78).
Oink not present in the new container: scripts/setup_oink.sh started 16:40Z (vrun.sh needs it). Open targets (RESUME POINT, none started):
- (a) A (Σ) pair with a COARSE_L(θ) rise (must end at a fallback with M_k < L by TEV-FB, RESULTS R40); it would hit RISE-LAST and
  test P-N5-ENT. Next: climb16.py new objective on rise events, seeded from the tx/conf bests, n ≥ 11 (all n ≤ 5 tables vacuous, R70 §3).
- (b) XSN-RUN aimed at n − 1 (best n − 2 at n 10, xrun8_n10). Next: random/biased search at n ≤ 12 with rnd16.py (exhaustive infeasible past n 5).
- (c) TEV-RED (5) configuration (TEVCONF): none seen. Next: conf climb with tevred16.py as the exact checker.
- (d) NJB's straddle after NL= fell (R70 §4, OPEN in GAPS G-N5-TIME); (β)-fallback count per scope run (2 seen, beta2_n11);
  "no fallback after a rise" (REFEREE-2; 1.5 M far-climb evaluations, no hit). Next: whichever the Lead routes; P-N5-LV2 is in review,
  so its LV-NONE / SCOPE-FB bounds (≤ 4·n·n_E + 3) are the nearest named lemma to attack.

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11; trunk text: "NL= FALSE (L-RED nleq_cex_n48, Lead re-run);
  NJB's straddle OPEN"). GAP-A, GAP-C (L-ALG, open; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 16, R69 notebook trap 2): a borrowed checker narrower than its statement. L-SI's threv.py stops at the next
  fallback, so its "0 hits" could not refute TEV-LAST over the full window.
  Check now: write the exact checker from the frozen statement (rx16.py / tevred16.py), list each window/threshold of any borrowed
  checker against the packet text, and count a kill only with one Odd choice vertex, an Oink-verified run, and the exact obstruction.
- Also caught at this restart: stale clone (1703 behind), by fetch + reset + `rev-parse HEAD == origin/claude/l-red`.

## Successor 15 section (superseded): L-RED successor 15 (Opus 5.5, D15/D18; LANE-RESTART step 3; written 2026-10-25 ~01:05Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 14
(session_01DYUCLfp4LkaCnY7moyVLAa), handover notebook notes/L-RED.md @ 97654ed9. Previous answers (successor 14) are in
history: `git show 97654ed9:docs/agents/handover-checks/L-RED.md`.

### 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = 0d0b67a1, 706 commits behind origin/claude/l-red (stale; clean tree).
- `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo` (01:01Z): origin/claude/l-red = 97654ed9; trunk = 1ef02bb2.
- `git merge --ff-only origin/claude/l-red` -> 97654ed9 (local = origin/claude/l-red).
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 66 behind; merge-base 97654ed9
  (lane head is an ancestor of trunk). `git merge --no-edit origin/claude/vibrant-johnson-nxvvxo` fast-forwarded to 1ef02bb2:
  0 ahead / 0 behind before this file's commit (1 ahead after it). No rebase, amend or force-push.
- Packets pinned on trunk 1ef02bb2, sha1 re-measured (`git show <trunk>:<file> | sha1sum`): docs/new/P-N5-SO-box32.md deb5ee44…,
  docs/new/P-N5-LP-box32.md d2c8121a… (match the brief).

### 2. Open work and the next step of each
Nothing running in this container (`ps aux | grep -c python3` = 3: grep and harness only). Predecessor parked after box 35
with nothing in flight (notebook RESUME POINT).
- (A) Expected box (after GO, orientation only): adversary on P-N5-SO (Lemmas TH, SO, Corollary XJ) and P-N5-LP (used-level
  freeze, Theorem LP, Lemmas DF/BAND/WAKE, Corollary LP′). Next step: read both packets as frozen; check the statement of Lemma SO
  (S_o ≤ d_o(Θ+1); "minimiser set only shrinks with θ fixed, key of a surviving exit frozen") and P-N5-LP §4's J ≤ S_o against
  traces from n5.py; build a checker that tests the frozen statement exactly (trap 3), then climb for violations (o-cyclic 𝒞^1O,
  exactly one Odd vertex with out-degree > 1); then K (wakes per phase) growth. Seeds: j10_n24 (R64), u2flat73_n32 (R65).
- (B) Open kill targets from R62/R64/R65, not started: hand-built k-digit counter (R62 §1); J super-linear (R64 §2); K_W / E
  growth (R65). Next: fold J and K growth into (A).
- (C) (FBRE-F′) with the window at run index ≥ n, or excluding post-θ-change re-entries (R61): edit fbref.py's boundary and climb.
  Only if routed.
- (D) G-NEST (R48 §4): paused with the DTL line by L40 (1). Next only on a Lead route.

### 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (docs/GAPS.md line 9).
- Attacked, not owned: GAP-A, GAP-C (L-ALG, open; DTL paused by L40); G-N5-TIME (L-NEW, open) is the target the N5 work attacks.

### 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active**:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   (Lead reading L40, active: L-RED is the N5 adversary; labels PROVED / CONJECTURE / OPEN; DTL paused.)
2. D15 (docs/DECISIONS.md line 278), status **active**:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   (Lead reading L37, active.)
3. D1 launch brief (docs/decisions/D001-launch-brief.md lines 92-93 and 99), status **active**:
   > Failing any step makes it a dead end, recorded with the exact obstruction or counterexample.
   > - Dead ends are kept, with the obstruction and the instance that killed them.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap (R65, notebook trap 3): a reference checker (u23check.py) tested a weaker statement than the frozen packet P-N5-U23
  (U23 unchecked, (iii) at 2|R|), so "0 violations" from it would not have meant the frozen statement holds.
  Check now: read the frozen statement first, write my own checker against it (u23x.py), and list each threshold of any
  borrowed checker against the packet text before reporting. Applies directly to Lemma SO / J ≤ S_o.
- Also caught again at this restart: stale local branch (706 behind), by fetch + `merge --ff-only` + rev-parse before work.

## Successor 24 (Opus 5.5, D15; created 2026-10-29 ~00:25Z, date -u) handover check
Measured 2026-10-29 00:29Z (date -u).
### 1. Branch, head, distance to trunk
- claude/l-red, head before work b2c3d07c (`git rev-parse`); trunk origin/claude/vibrant-johnson-nxvvxo 5f2dc2e8.
- Before merge: 2 ahead / 175 behind (`git rev-list --left-right --count HEAD...trunk` = "2 175"). Merged trunk (merge commit 9d99f7ef,
  no conflicts): 3 ahead / 0 behind; `merge-base --is-ancestor trunk HEAD` true.
### 2. Open work and the next step of each
- Nothing in flight (predecessor HANDOVER "IN FLIGHT: nothing"; this container has no climb running). Oink not built here
  (`ls tools/oink/build`: missing); scripts/setup_oink.sh started.
- Lead 00:28Z target: kill CONJECTURE FB-LIN (at most n in-phase fallbacks in one phase). Next: a per-phase fallback counter (f per phase,
  max over phases) on the trace engine, re-measure rise_fb38_n48 (lib record f 37 = 0.78n), then climbs with fitness f and hand
  constructions from the long121 carry cell (R98 §3).
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), **open** (docs/GAPS.md line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open, DTL paused by L40);
  G-N5-TIME (L-NEW, open, line 11) is what the FB-LIN attack targets.
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D18 (index line 32, **active**): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems." (Lead reading L40, active: L-RED = N5 adversary.)
2. D15 (index line 26, **active**): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
3. D1 (index line 5, **active**; D001 launch brief): "Failing any step makes it a dead end, recorded with the exact obstruction or counterexample."
### 5. One trap and its check
- Trap (R99): n5.py does not validate start entries, so comp54_n80 / n3cov_lean starts with missing edges gave counts on a different
  start. Check: write every pinned start with experiments/red/sel/fullstart2.py (drops invalid entries, full S3 base) and confirm with
  n5b.py --mode spec, which rejects invalid starts, before any count is reported.

## Successor 25 (Opus 5.5, D15/D18; created 2026-10-29 ~09:59Z, date -u) handover check
Measured 2026-10-29 10:00:55Z (date -u; fetch at 10:00:09Z).
### 1. Branch, head, distance to trunk
- claude/l-red, head before work 92754453 (= origin/claude/l-red, the predecessor's HANDOVER push; local was fast-forwarded from b2c3d07c).
  Trunk origin/claude/vibrant-johnson-nxvvxo e3b435ab. Before merge: 0 ahead / 244 behind (`git rev-list --left-right --count`).
  Merged trunk (merge commit 8e7e02ad, no conflicts): 1 ahead / 0 behind; `merge-base --is-ancestor trunk HEAD` true.
### 2. Open work and the next step of each
- Nothing in flight (predecessor HANDOVER "IN FLIGHT: nothing"; FB-LIN parked as CONJECTURE, data max 0.79n). Oink not built here
  (tools/oink/build missing); scripts/setup_oink.sh started.
- Lead 09:59Z box: (1) attack CONJECTURE SEG-COUNT (L-SI LAY §6) by construction: two deadlock steps in one REL segment charged to one
  H-sink; seed seglast_kill_n29 (experiments/si/lay/instances/). Next: own REL/segment/sink checker on seglast_kill_n29, reproduce L-SI's
  table, then build the two-deadlock gadget. (2) if (1) stalls: L-WAVE′ (gaps ≤ n − 1) by a vertex switching twice in one gap.
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), **open** (docs/GAPS.md line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open); G-N5-TIME (L-NEW, open, line 11)
  is what the SEG-COUNT attack targets.
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D18 (index line 32, **active**): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
2. D15 (index line 26, **active**): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
3. D1 (index line 5, **active**; D001 launch brief): "Failing any step makes it a dead end, recorded with the exact obstruction or counterexample."
### 5. One trap and its check
- Trap (R100-R104): every count-based climb fitness except the target itself got gamed (switch-all fallbacks, parallel waves, several gates
  per stall). Check: keep the target quantity (here EXC = (b − a) − switching Even vertices, recomputed by my own checker) primary, and
  inspect the trace of the best game before reporting a number.

## Successor 26 (Opus 5.5, D15/D18; created 2026-10-29 ~11:07Z, date -u) handover check
Measured 2026-10-29 11:08:19Z (date -u; fetch of claude/l-red, claude/l-lit, trunk just before).
### 1. Branch, head, distance to trunk
- claude/l-red. Local was stale at b2c3d07c (successor 23); fast-forwarded to origin 7002ff99 (predecessor's handover stamp;
  `merge-base --is-ancestor 7002ff99 HEAD` true). Before merge: 3 ahead / 45 behind trunk origin/claude/vibrant-johnson-nxvvxo
  (merge-base 22d7c6ab). Merged trunk (merge commit 09d020c7, no conflicts): 4 ahead / 0 behind.
### 2. Open work and the next step of each
- Nothing in flight (HANDOVER "IN FLIGHT: nothing"). Oink not built in this container; setup_oink.sh started.
- Lead 11:07Z box: STEP 1 = R107 (DATA) on mkr K = 2..14, m = 4K, both engines: (a3) S3 default start run length / phases / longest
  fallback-free run; (b) per-vertex switch counts in the long run (max over v vs K, n); (c) total iterations, phases, runs, explicit and S3
  starts. Next: run n5b SPEC + n5.py on mkr instances with no start file. STEP 2 = (a2) a counter clock across phases (odd-top sequencing).
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (docs/GAPS.md line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open); G-N5-TIME (L-NEW, open, line 11).
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D18 (index line 32, active): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
2. D15 (index line 26, active): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
3. D1 (index line 5, active; D001 launch brief): "Failing any step makes it a dead end, recorded with the exact obstruction or counterexample."
### 5. One trap and its check
- Trap (R106 caveat): every R105/R106 run used an explicit start pair; a result from an explicit start bounds a run, not N5's iteration
  count from its S3 default start. Check: every count reported in R107 names its start (file sha1 or "S3 default"), and stale local branch
  (b2c3d07c, 2 handovers behind) caught by fetch + ff + is-ancestor.

## Successor 27 (Opus 5.5, D1/D15/D18; created 2026-10-29 ~13:47Z, date -u) handover check
Measured 2026-10-29 13:49:47Z (date -u; fetch of claude/l-red, claude/l-lit, trunk at 13:48Z).
### 1. Branch, head, distance to trunk
- claude/l-red. Local clone was stale at b2c3d07c (successor 23); fetched and fast-forwarded to origin 1811cae2 (predecessor's last push,
  R111 §4 + notebook). Before merge: 2 ahead / 134 behind trunk origin/claude/vibrant-johnson-nxvvxo (merge-base 61881154). Merged trunk
  (merge commit 2c8e7d04, no conflicts): 3 ahead / 0 behind (`git rev-list --left-right --count HEAD...trunk` = 3 0).
### 2. Open work and the next step of each
- Nothing in flight (HANDOVER "IN FLIGHT: nothing"). Oink not built in this container; setup_oink.sh started 13:49Z.
- Lead 13:47Z STEP 1: the COUPLED family (R111 §4 (C4)/(C5) target): a game where σ-changes and τ-changes per joint λ-run both grow,
  each caused by the other. Next: design a gadget where an Odd τ-run (dual hntop-like) and an Even σ-run interleave; measure NM* (nm.py),
  NM*^U (nm.py on G^d via ctl/dualize.py + mirror), τ/σ-changes per joint λ-run, totals; two engines, Oink, S3 start via s3embed.
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (docs/GAPS.md line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open; lines 6-7); G-N5-TIME (L-NEW,
  open, line 11).
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D18 (index line 32, active): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
2. D1 (index line 5, active; D001 launch brief): "Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet"
3. D15 (index line 26, active): "Be autonomous, reason about it"
### 5. One trap and its check
- Trap (R99 erratum, R106 caveat): reported counts came from starts that were invalid or explicit, not the SPEC S3 default. Check: every
  count names its start (file sha1 or "S3 default"); explicit-start pins are re-run from S3 via s3embed.py with the "same as image" check;
  and today's stale clone (b2c3d07c, 3 handovers behind) was caught by fetch + ff before any work.

## Successor 28 (session_01V5yGRXarwpixU1C9hcL21Z, Opus 5.5, D1/D18; created 2026-10-29 ~15:28Z, date -u) handover check
Measured 2026-10-29 15:34Z (date -u; fetch of all origin branches at 15:33Z).
### 1. Branch, head, distance to trunk
- claude/l-red. Local clone was stale: 650 behind origin/claude/l-red; fast-forwarded to 2ca02039 (predecessor's last push; 23d4956b is its
  ancestor). Before merge: 1 ahead / 89 behind trunk origin/claude/vibrant-johnson-nxvvxo (merge-base 23d4956b). Merged trunk (merge commit
  665ee8f9, no conflicts): 2 ahead / 0 behind (`git rev-list --left-right --count HEAD...trunk` = 2 0).
### 2. Open work and the next step of each
- Nothing in flight (HANDOVER "IN FLIGHT: nothing"). Oink not built in this container; setup_oink.sh started 15:33Z.
- Lead 15:28Z STEP 1: attack CONJECTURE SF-POLY (N5-SF, claude/l-new docs/new/N5-SF-box54.md): find a family with super-polynomial SBC, or the
  largest polynomial degree. Next: an independent N5-SF implementation from the definition, cross-checked with n5sf.py; switchbestexp N > 16
  and a switch-best-type construction aimed at moving σ̄ (DECOUPLE: Even's σ sequence is fixed by σ_0).
- Queue after SF-POLY: handover items (a)/(b) = mkr + dewin coupling (needs a menu-gated mkr variant first), R113 §3 routes (A)/(B).
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (docs/GAPS.md line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open; lines 6-7); G-N5-TIME (L-NEW, open, line 11).
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D1 (index line 5, active): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet"
2. D18 (index line 32, active): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
3. D15 (index line 26, active): "Be autonomous, reason about it"
### 5. One trap and its check
- Trap: counts from an explicit or invalid start reported as if from the SPEC S3 default (R99 erratum, R106 caveat); and the stale clone (650
  behind today). Check: fetch + ff-only + rev-list counts before any work; every count names its start (file sha1 or "S3 default").

## Successor 29 (session_01V5yGRa1utvwvH65mnBBssK; Opus 5.5, D1/D18; created 2026-10-29 ~18:10Z, date -u) handover check
Measured 2026-10-29 18:11Z (date -u; fetch of claude/l-red, claude/l-new, trunk at 18:10Z).
### 1. Branch, head, distance to trunk
- claude/l-red. Local clone was stale at b2c3d07c (successor 23): 748 behind origin/claude/l-red; fast-forwarded to 745f3b07 (predecessor's
  HANDOVER push). Before merge: 1 ahead / 126 behind trunk origin/claude/vibrant-johnson-nxvvxo (merge-base c5f3bed1). Merged trunk f388b165
  (merge commit fdf01a3f, no conflicts): `git rev-list --left-right --count HEAD...trunk` = 2 0.
### 2. Open work and the next step of each
- Nothing in flight from successor 28 (its /tmp randomedgesubexp runs are lost with the container; optional).
- Lead 18:10Z STEP 1: push N5-SF iteration degree above 3 (fcN cubic) or find the obstruction. Next: a two-block 3+3 composition with an Odd
  break / odd top priority on the N-COND loop d_A → s_B → … → d_A (R115 §2c), measured against one block (121 iterations at N = 3).
- Second: attack PV_rel when L-NEW lands it (PV as stated DEAD, R115 §2c).
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open; lines 6-7); G-N5-TIME (L-NEW, open, line 11).
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D1 (index line 5, active): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet"
2. D18 (index line 32, active): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
3. D15 (index line 26, active): "Be autonomous, reason about it"
### 5. One trap and its check
- Trap: stale clone (748 behind today, "up to date" by git status because origin refs were stale too). Check: fetch the branch first, then
  rev-parse HEAD vs origin + is-ancestor + ff-only, before reading any notebook. Second trap (successor 28): `pkill -f` on a pattern in
  your own command line kills the shell; kill by PID.

## Successor 30 (Opus 5.5, D1/D18; created 2026-10-29 ~19:51Z, date -u) handover check
Measured 2026-10-29 19:52Z (date -u).
### 1. Branch, head, distance to trunk
- claude/l-red. Local clone stale at b2c3d07c (successor 23). `git ls-remote origin` first (refs l-red a134e6be, l-new 0989b72c, l-si 33f04452,
  trunk acf60fdc all exist), then `git fetch origin claude/l-red claude/l-new claude/l-si claude/vibrant-johnson-nxvvxo`; ff-only to a134e6be
  (predecessor's HANDOVER push). Before merge: 1 ahead / 37 behind trunk (merge-base 747da675). Merged trunk acf60fdc (merge commit ecddfaf7,
  no conflicts): `git rev-list --left-right --count HEAD...trunk` = 2 0.
### 2. Open work and the next step of each
- Nothing in flight (HANDOVER "IN FLIGHT: nothing"; `ps` shows no lane python3). Oink not built here; setup_oink.sh started 19:52Z.
- Lead 19:51Z STEP 1: break G-N5-TIME's reduction halves: (a) coupled counters with UNPROTECTED (class-X) Odd options re-entered; (b) a
  super-polynomial fixed-tau stretch under the mixed frame (FO*). Next: read R116-R118, R111-R113 §3, N5-FREEZE-box63, N5-ODD-box33; then
  build (a) on mkr + dual through class-X options, measured with sf/tstretch.py, cpl/cpl.py, seg/xeng.py, Oink.
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (`grep -n G-NEST docs/GAPS.md` line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open, lines 6-7);
  G-N5-TIME (L-NEW, open, line 11) = this box's target.
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D1 (index line 5, active; DECISIONS.md line 7): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
2. D18 (index line 32, active; DECISIONS.md line 333): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
3. D15 (index line 26, active): "Be autonomous, reason about it"
### 5. One trap and its check
- Trap (Lead, three times today): a nonexistent ref in `git fetch` aborts the whole fetch, leaving every origin ref stale with no visible
  error in a tail. Check: `git ls-remote origin` first, fetch only names it lists, then rev-parse HEAD vs origin + ff-only + is-ancestor.

## Successor 31 (Opus 5.5, D1/D18; created 2026-10-29 ~22:19Z, date -u) handover check
Measured 2026-10-29 22:26Z (date -u).
### 1. Branch, head, distance to trunk
- claude/l-red. Local clone stale at b2c3d07c. `git ls-remote origin` first (l-red 1e07ddfc, l-si dab44572, trunk a60e5704 exist), then
  `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo claude/l-si`; ff-only to 1e07ddfc (predecessor's last push; 033dcab8 is
  an ancestor). Then 0 ahead / 90 behind trunk (merge-base 1e07ddfc = HEAD), so ff-only to trunk a60e5704: 0 / 0.
### 2. Open work and the next step of each
- Nothing in flight (HANDOVER "IN FLIGHT: nothing"; `ps` shows no lane python3). Oink not built here; setup_oink.sh started 22:26Z.
- Lead 22:19Z STEP 1: attack CONJECTURE PCH-QUAD-S (and RESET-LIN-S, CARRY-SEG-S, MIN-QUAD) of L-SI box 38/39 Lemma SPAN: one pair (v, c)
  whose span holds > n^2+n path-set changes of c. Next: read N5-SPAN-box38 / N5-SPANW-box39 and odd/win.py, odd/spanw.py, then build mkr +
  leave/re-enter switcher families. Predecessor's open items (FG climb, RESET-LIN-T window, CARRY-SEG) are superseded by this STEP 1.
### 3. docs/GAPS.md rows I own
- G-NEST (major; L-RED), open (GAPS line 9). Attacked, not owned: GAP-A, GAP-C (L-ALG, open, lines 6-7); G-N5-TIME (L-NEW, open, line 11).
### 4. Owner rulings (verbatim), DECISIONS-INDEX status
1. D1 (index line 5, active; DECISIONS.md line 7): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
2. D18 (index line 32, active; DECISIONS.md line 333): "Focus on N5 and work toward proving it. Explore novel approaches ... Clearly distinguish proven results from conjectures and open problems."
3. D15 (index line 26, active; DECISIONS.md line 278): "Be autonomous, reason about it"
### 5. One trap and its check
- Trap: stale clone (b2c3d07c, git status said "up to date" against stale origin refs). Check: `git ls-remote origin` first, fetch only
  listed names, rev-parse HEAD vs origin, is-ancestor 033dcab8, ff-only. Second (predecessor): a push.sh moved to background by a tool
  timeout still holds the tree; wait for it before committing.
