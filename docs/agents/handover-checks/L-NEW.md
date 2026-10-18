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
