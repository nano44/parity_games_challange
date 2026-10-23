# Handover check: L-COMP (successor 2, 2026-10-23 05:35Z by date -u)
Every answer measured from the repository at the time of writing (commands given), not recalled from notes/L-COMP.md.
Successor of session_01Nd4XCMfDaYHsh1P6XTtRGz (parked; handover 7ac0d432 "L-COMP: park (N5 second implementation complete; notebook
resume point)"). The previous answers (2026-10-15) are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`, tracking `origin/claude/l-comp` (was at 7ac0d432, working tree clean).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` fetched: 269edc63 ("Lead: C22 closed; roster", 2026-10-23 05:27Z).
- `git merge origin/claude/vibrant-johnson-nxvvxo` was a fast-forward (trunk already contained 7ac0d432): head = 269edc63.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead, 0 behind (before this file's commit;
  after it: 1 ahead, 0 behind).
- Container: Oink not built (`tools/oink/build` absent), no background jobs (`pgrep -a python` empty), no timed wakes.

## 2. Open work and the next step of each
- In flight: nothing. The N5 second implementation is DONE and merged (NOW.md roster line 26: b49c9fc).
- N5 leftover: tc N = 26 was not compared in SPEC mode (notebook resume point; orig mode N = 26 verified, no reference). Next step: none
  unless the Lead routes it (N5 step 2 declared complete by the Lead 2026-10-18 23:58Z).
- STEP 2 of this box (Lead brief 05:36Z): second independent implementation of N8d-R2 (Koh-Loho, arXiv 2108.13338, Alg. 1, over the
  perfect (n, d/2)-universal tree; pivot R2) plus deterministic R1 cross-check. Waits for GO. Next step after GO: build Oink
  (scripts/setup_oink.sh, pinned 8fbf0a7), open the paper from arXiv (record version, sections), read docs/new/N8d-single.md §0 only,
  write experiments/n8d-second/ from those two sources, freeze and commit before reading experiments/new/kl/*.py or the code-to-paper tables.
- sat-hard (L-STRUCT T3 support): parked (notebook queue 0-3; CNFs gone with the container; regenerate with diag.py). No step until routed.
- counter_qpt growth class (N = 29..40, timeout 600): open, low priority, not scheduled.

## 3. docs/GAPS.md rows owned by L-COMP
None. `grep -n -i l-comp docs/GAPS.md` on 269edc63 returns one row, G-N5-TERM (closed list; owner L-NEW, "L-COMP checks runs"),
closed 2026-10-19 by RESULTS R15. No open row names L-COMP.

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on 269edc63)
1. D2 change 5 (D2: active):
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: my N8d-R2/R1 implementations output positional strategies for both players, and every output is checked by
   experiments/harness/verify.py, not by the implementation's own claims.
2. D2 change 4 (D2: active):
   > 4. 7b changed: a randomized (Las Vegas, expected polynomial) algorithm is labelled M4-R, not M3, and reported to me
   >    at once like an M4 claim.
   Constraint: N8d-R2 is randomized; its pivot counts are random variables, so I report distributions (mean, spread per family and size)
   and any super-polynomial growth of the expectation at once, never a single-seed number as a growth class.
3. D1 (active), docs/decisions/D001-launch-brief.md:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   > claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: step 2 is run to find a failure, independently of L-NEW: written from the paper and §0 only, any wrong region/strategy
   from either implementation reported at once with the instance.
Also binding: D14 (active; L-NEW is the (c) lane whose candidate I test) and D15/L37 (active; Opus 5.5; no option questions to the owner).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: unspecified orders make "equal counts" meaningless. In the DTL step 2 (2026-10-15, notebook dead ends) a reimplementation from the
written pseudocode could not reproduce Oink's tangle counts: four unpinned orders (sort, in-edge order, stored tangle order, SCC order)
changed counts up to 8 per game while regions never changed; a count mismatch looked like a bug and was not.
Check now: counts are compared exactly only where the spec pins every order; otherwise distributions are compared and the unpinned choice
is named. For this box that is written into the brief: R1 (lowest index, deterministic) must match results/*.r1.csv per instance, and a
mismatch is a finding traced to the spec line; R2 (uniform draw, candidate-list order unpinned by §0) is compared by mean and spread
per family and size. Regions/strategies are always decided by verify.py and Oink zlk (labelled --tl where zlk aborts, counter_m N = 41, 42).
