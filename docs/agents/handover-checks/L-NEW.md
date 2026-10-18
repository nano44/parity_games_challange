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
