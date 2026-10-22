# Handover check: L-NEW (successor 1, Opus 5.5 per owner D8; written 2026-10-18 12:30Z by date -u)
Every answer measured from the repository at the time of writing (commands named), not recalled. Predecessor: L-NEW
(session_01W1U7uWKSXXHGqtjedkorNP), notebook handover ~12:10Z, head 6034271.

## 2026-10-18 12:30Z

### 1. Branch, head, distance to trunk
- Branch `claude/l-new`. After `git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo`: local HEAD =
  origin/claude/l-new = 6034271 (not stale). Trunk origin/claude/vibrant-johnson-nxvvxo = 07d6670; merge-base ff4e60c;
  `git rev-list --left-right --count HEAD...trunk` -> 17 ahead, 23 behind.
- Step 0: `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 5a16629 (clean, no conflicts); now 18 ahead,
  0 behind; 19 ahead after this file's commit.

### 2. Open work and the next step of each
Nothing in flight in this container: the predecessor's gitignored outputs (experiments/new/out/: the lifted S6/S5
chains, the C++ N1 sweep summary_c.csv, instances) and tools/oink/build are LOST with the old container; they must be
regenerated. Queue (Lead box-2 brief 12:2xZ, consistent with notes/L-NEW.md queue 0-4):
- (0) N1 gauntlet step 2 is NOT complete. Missing families: tc+, counter_m, counter_rr, counter_rob; no switchbestexp
  plot; the cited summary CSVs are not committed. Next: scripts/setup_oink.sh, rebuild anneal_c (--nocompress), run
  those five families as far in N as time allows, commit raw per-run CSVs + plots, one verdict line per family. Report
  at once if N1 passes all 13 (L35 (3)) or if any family grows super-polynomially (kill, pinned sha1 instances).
- (1) Queue item 0, S6 numbering RULE on switchbestexp: extract a rule from the climbed numberings
  (experiments/new/instances/s6/*.perm) that beats the mechanical lift (3886, 4719, 5626, 6602 at N = 5..8), generate
  N = 2..8 from the rule alone, run vjfast cunningham. Next: read the .perm files against pgsolver_port labels.
- (2) Queue items 1-4: record S5/S6 chain results (N = 4, 5) in docs/new/S5S6-renum.md (rerun needed, outputs lost);
  N1 sweep at larger N; N1 killer / lock design (docs/new/N1-killer-sketch.md) first among the design items; N3 only if
  N1 dies, N2 parked.

### 3. docs/GAPS.md rows I own
- None. `grep -n "L-NEW" docs/GAPS.md` (at 5a16629) -> no match. Open rows GAP-A and GAP-C are owned by L-ALG
  (L-RED attacks). N1 is a bench candidate, not a GAPS row.

### 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md line 25, quoted in docs/DECISIONS.md#d1; index row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Binds N1: bench data is not a claim; (PHASE-POLY) stays a DATA hypothesis; a step-2 survivor is reported, not claimed.
2. D14 (docs/DECISIONS.md#d14; index row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   This is the lane's mandate (with Lead reading L35, which is a reading, not a ruling: screen against BARRIERS.md and
   the dead-end record before code; report a step-2 survivor to the owner at once).
3. D1 (docs/decisions/D001-launch-brief.md line 96; index row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   (D13, index row "active": "Keep working on the dtl and also c" is the ruling that keeps (c) alive at all.)

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: a wrong stop test for N1. "sigma has no VJ improving switch" was used as the optimality test; a region-correct
  sigma need not be VJ-optimal, and tc N = 4 stalled at j = 102 forever. Check: N1 stops only on the region
  certificate (sign of the values plus experiments/harness/verify.py on both restricted strategies), and every run's
  positional strategies are verified against Zielonka (experiments/new/check.sh / check_sol.py) before a count is used.
- Second trap, guarded at this handover: gitignored outputs (out/) do not survive a container; any number cited in a
  report must come from a committed CSV (the box-1 report cited uncommitted summary_c.csv / summary_py.csv).

## 2026-10-18 20:54Z (successor 2, Opus 5.5 per owner D8; every time from date -u)
Measured from the repository at writing time. Predecessor: successor 1, notebook head bdd53ae.

### 1. Branch, head, distance to trunk
- Branch `claude/l-new`. Local HEAD was STALE (6034271, 54 behind origin/claude/l-new): fast-forwarded to
  origin/claude/l-new = bdd53ae after `git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo`.
- Before merge: `git rev-list --left-right --count origin/claude/l-new...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead,
  129 behind (trunk = 140d35d).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 522d604 (clean). Now 3 ahead, 0 behind; 4 ahead after this
  file's commit.

### 2. Open work and the next step of each (Lead box-4 brief)
Nothing running in this container; tools/oink/build and experiments/new/out/ (gitignored) must be regenerated.
- (0) N5 spec completion for L-COMP's independent implementation: pin "best-reward start", the tie-break among optimal
  σ'/τ', the switch-all fallback choice and tie-break, and simultaneous vs sequential update, each from n5.py's actual
  behaviour with line numbers. Next: read experiments/new/n5.py against docs/new/N5-ssi-global.md "Exact pseudocode".
- (1) Killer design: (a) non-sink stall gadget forcing fallback every step, with Friedmann's switchallexp behind it (L-LIT
  T20 caveat 3); (b) DLM distraction module (2309.02223 p. 15, caveat 1). Next: after (0), build the stall gadget and
  measure fallbacks/iteration and iterations/N.
- (2) Any super-polynomial family: report to the Lead at once with pinned sha1 instances, Oink zlk/tl regions, verify.py.
- (3) No kill: write the exact obstruction as a necessary condition for a killer.
- (4) Open VJ00 for the cost of the counterstrategy procedure; fix N5's cost statement.
- Optional, not routed: GAP row G-N1-LB (below).

### 3. docs/GAPS.md rows I own
- `grep -n "L-NEW" docs/GAPS.md` at 522d604 -> one row: **G-N1-LB** (minor; owner "L-NEW (optional; not routed)";
  status **open**): theorem form of the N1 kill (2^Ω(n) switches in one IncreasingDiscountPI phase on deep-trap
  switchallexp); two missing lemmas (i), (ii) per L-LIT T19. Not in this box's plan.
- N5 has no GAPS row (`grep -n N5 docs/GAPS.md` -> no match).

### 4. The three owner rulings that most constrain me (verbatim from docs/DECISIONS.md), with index status
1. D1 (docs/DECISIONS.md "## D1", key lines; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Binds this box: N5 is wrong until proved; my job is to kill it.
2. D14 (docs/DECISIONS.md "## D14"; index row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   The lane's mandate (Lead reading L35 is a reading, not a ruling).
3. D13 (docs/DECISIONS.md "## D13"; index row D13 "active"):
   > Keep working on the dtl and also c
   Keeps (c) alive alongside DTL. Also binding (D1 key line, same file):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: a STALE local branch. This container started at 6034271, 54 commits behind origin/claude/l-new (bdd53ae); working
  from it would have lost box 3 (N5, the N1/N2 kills). Check: `git fetch` then `git rev-parse HEAD origin/claude/l-new`
  before any work (done above; fast-forward only, then a --no-ff merge of trunk; never rebase).
- Also carried: estimated timestamps (box 3 had two stamps 20-55 min ahead of the clock): every stamp now comes from a
  `date -u` call made just before writing.

## 2026-10-19 00:21Z (successor 3, Opus 5.5 per owner D8; every time from date -u)
Measured from the repository at writing time. Predecessor: successor 2, notebook head 1fa0305 (parked 00:05Z).

### 1. Branch, head, distance to trunk
- Branch `claude/l-new`. Local HEAD was STALE again (6034271, the same stale start as successor 2):
  `git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo`, then `git merge --ff-only origin/claude/l-new` -> 1fa0305.
- Before merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 53 behind
  (trunk = e73b214).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> f259083 (clean). Now 1 ahead, 0 behind; 2 ahead after this
  file's commit.

### 2. Open work and the next step of each (Lead box-8 brief; notebook queue)
Nothing running in this container; tools/oink/build and experiments/new/out/ (gitignored) are absent and must be rebuilt.
- (1) K9 premise (P): on one-player ⊕ games every VJ00 improvement chain (any non-empty unambiguous switch sets, flat steps
  included) has poly(n) length. VJ00 Prop. 7.4 is stated only (L-LIT T22). Next: rebuild the one-player longest-chain search
  (max 21 at n ≤ 9), extend n, read what the longest chains do; open Fearnley 1705.02313 Lemma 3 (Cochet-Terrasson-Gaubert
  O(|V||E|), sink one-player) and test whether it adapts; either a reading tied to RS-00-48 definitions or a super-polynomial
  one-player family (report at once).
- (2) Climb with fitness ch_O + ch_E (best-reply changes, n5_brchanges.py) against N5. Next: after (1).
- (3) K8's 2-periodic case (sb_flipback.py, sb_tauvar.py). Next: after (2).
- (4) n5.py on L-COMP's 2,000 random games vs n5b spec mode. Next: regenerate with
  `python3 experiments/harness/gen.py corpus out/rand2k 2000 20261018 --nmin 1 --nmax 120`, check sha1s against
  claude/l-comp experiments/n5-second/results/random_*.csv.

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at f259083)
- **G-N5-TIME** (major; owner "L-NEW (L-LIT T22; referees later)"; status **open**): N5 makes polynomially many iterations.
- **G-N5-TERM** (major; owner "L-NEW (L-COMP checks runs)"; status **closed**; RESULTS R15 [refereed-only]).
- **G-N1-LB** (minor; owner "L-NEW (optional; not routed)"; status **open**). Not in this box's plan.

### 4. The three owner rulings that most constrain me (verbatim from docs/DECISIONS.md), with index status
1. D1 (docs/DECISIONS.md "## D1"; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Binds this box: N5 and K9 are wrong until proved; a reading of (P) is a reading, not a result.
2. D14 (docs/DECISIONS.md "## D14"; index row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   The lane's mandate (Lead reading L35 is a reading, not a ruling).
3. D13 (docs/DECISIONS.md "## D13"; index row D13 "active"):
   > Keep working on the dtl and also c
   Keeps (c) alive. Also binding (D1 key line, same file, index "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: a STALE local branch. It bit again today: the container started at 6034271 while origin/claude/l-new was 1fa0305;
  working from it would have lost boxes 4-7 (K1-K9, R15 material). Check: `git fetch` then
  `git rev-parse HEAD origin/claude/l-new` before any work; fast-forward only, then a --no-ff merge of trunk; never rebase.
- Also carried: never put a command that can fail (e.g. cp onto itself) inside a `&&` chain before a commit; it silently
  drops the later steps. Check: commit as its own call and confirm with `git log -1`.

## 2026-10-21 21:57Z (successor 4, Fable 5.1 per Lead reading L36; every time from date -u)
Measured from the repository at writing time. Predecessor: successor 3 (session_01PTa8b1EHQDZYpwmi99oG5G), box 9 parked 21:51Z at
notebook head 6b3dcd5.

### 1. Branch, head, distance to trunk
- Branch `claude/l-new`. After `git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo`: local HEAD = origin/claude/l-new =
  6b3dcd5 (NOT stale this time; checked with `git rev-parse HEAD origin/claude/l-new`).
- Before merge: `git rev-list --left-right --count origin/claude/l-new...origin/claude/vibrant-johnson-nxvvxo` -> 6 ahead, 5 behind
  (trunk = 414b85e; merge-base a74d82f; the 5 trunk commits are CHECKER C19 Addendum 3 and the Lead's L36/Q18 records).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 5dce0be (clean, no conflicts). Now 7 ahead, 0 behind; 8 ahead after
  this file's commit.

### 2. Open work and the next step of each (Lead brief 21:55Z; notebook resume point; N5-SB-box9.md §3, §5)
Nothing running in this container; tools/oink/build and experiments/new/out/ (gitignored) are absent and must be rebuilt before any
sweep (scripts/setup_oink.sh first; check_sol2.py needs Oink).
- Box 10 (NOT started; waits for "go"), target G-N5-TIME, one of:
  (i) Killer: make N5's frozen-σ Odd tail follow a CDAG-type chain gen(m), with Even's exploits τ̄ as the masks (N5-SB-box9.md §5).
      Next: trace the tail of instances/n5b9/tc2 (134 Odd switches, 29 vertices) with n5_tail.py to read which τ̄ changes open which
      gates; then build the gadget per gen(m) bit and measure tail length vs n; any super-polynomial family goes to the Lead at once
      with sha1-pinned instances, Oink zlk/tl regions and verify.py = 0 errors. Known obstacle: K10's masking load Θ(n) per step.
  (ii) Proof: a bound on in-phase cycle building (N5-SB-box9.md §3, N5-K8-box8.md §3c-§3d). Next: on the n = 14 leapfrog instance
      (sb_conjR.txt) and the n = 10 trace, state what moves the build front and test a candidate potential (distance of the front
      to the new cycle's top) over the 4,508 recorded runs before any proof text.
- Carried, not routed: SB1' cycle tops (would give "N5 polynomial on one-player games"); G-N1-LB (optional).
- Debts carried: raw climb outputs live only in committed files (p_strict/logs, n5b9.sha1); nothing else is cited.

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at 5dce0be)
- **G-N5-TIME** (major; owner "L-NEW (L-LIT T22; referees later)"; status **open**): N5 makes polynomially many iterations. K9's
  policy-free route CLOSED by CDAG_n; K9 would need a bound specific to N5's S4a subset sequences. Box 10 target.
- **G-N1-LB** (minor; owner "L-NEW (optional; not routed)"; status **open**). Not in the box-10 plan.
- **G-N5-TERM** (major; owner "L-NEW (L-COMP checks runs)"; status **closed**, RESULTS R15, closed list).

### 4. The three owner rulings that most constrain me (verbatim from docs/DECISIONS.md), with index status
1. D1 (docs/DECISIONS.md "## D1", key lines; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Binds box 10: N5 is wrong until proved; a frozen-σ tail bound or a cycle-building bound is a reading until two referees sign.
2. D14 (docs/DECISIONS.md "## D14"; index row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   The lane's mandate (Lead readings L35 and L36 are readings, not rulings; L36 (2): "The (c) lane L-NEW continues its next box").
3. D13 (docs/DECISIONS.md "## D13"; index row D13 "active"):
   > Keep working on the dtl and also c
   Keeps (c) alive. Also binding (D1 key line, same file, index "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: ESTIMATED timestamps. It bit in box 3 (two stamps 20-55 min ahead), box 8 (two doc stamps, corrected in 689515a) and again in
  box 9 ("~21:40Z" in N5-SB-box9.md, corrected in 0015ba9 to the commit time). Check: every stamp, including this heading and the
  first line of every message to the Lead, is taken from a `date -u` call made in the same command that writes it; commit times
  (`TZ=UTC git log --date=format-local`) are the record when a stamp is in doubt.
- Also run at this handover: the stale-local-branch check (fetch, then `git rev-parse HEAD origin/claude/l-new`; equal this time),
  and the push rule (push.sh output redirected to a file, `$?` printed, never piped).
