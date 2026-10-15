# Handover check: L-COMP (successor session, 2026-10-15 ~18:50Z; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given), not recalled from notes/L-COMP.md.
Successor of session_014bbtNwaVKxFymHpXynjURn (handover 25a6e21).

## 1. Branch, head, distance to trunk
- Branch: `claude/l-comp`, tracking `origin/claude/l-comp`, working tree clean before this file.
- Head: 25a6e21 ("L-COMP: notebook resume point after container restart") = `origin/claude/l-comp`.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` at feda157 ("Merge C3c notes applied", 2026-10-15 18:11Z).
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 12 ahead, 452 behind.
- `git merge-base` = 5ba5d8b ("NOW: L-STRUCT correction at (4,6) V"). The 12 commits ahead are all sat-hard work since the last trunk merge
  (48e2744 encoder/CEGAR/LRAT checker ... 2dde459 n=5 diagonal cells, c2e095f and 25a6e21 notebook). Trunk carries the n=5 numbers only as a
  Lead note (docs/agents/LEAD-STATE.md:57), not the files.
- `scripts/verify.sh` at 25a6e21 in this container (3 s): VERIFY PASS. doc shape PASS; experiment self-checks PASS (harness selftest, m2,
  sat-hard SELFCHECK PASS with step 4 NOT RUN: no cadical binary); lean NOT RUN (no lean/lakefile); oink smoke NOT RUN (Oink not built here).
  Consequence: harness selftest steps 3 and 6 (Oink cross-checks) were skipped too; Oink must be built (scripts/setup_oink.sh) before any DTL run.

## 2. Open work and the next step of each
- DTL gauntlet step 2, formal part (NOW.md "In flight": "formal 10,000-game run + L-COMP strategy check pending"; L22 pins
  A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, trace 0). Not started; waits for the Lead's go. Next step after go: build Oink
  (setup_oink.sh pins 8fbf0a7), add registry entries oink-dtl-pin / oink-idtl-pin to experiments/harness/solvers.py with exactly those flags
  (the existing `-raw` entries add `-w 1` but not `--no-loops`), confirm `-w 1` / no-trace is the pinned run, then corpus (gen.py 10,000 seeded),
  rngame corpus, exhaustive tiny games, hard-families (largest finishing sizes), red/dtl generators and alg/instances/dtl_proof_c*.pg, all through
  compare.py + verify.py; growth tables/plots under experiments/dtl-bench/.
- Lead reading L15 (Q4): "When an L-COMP successor is next spawned for other work, it runs the original PGSolver binaries once (d3cd624) to diff
  the hard-family ports; if the platform classifier still refuses, the ported generators plus the REFEREE check stand." This session is that
  successor. Next step: one attempt after the DTL run (re-clone and build per notebook "Things only I know"); M1 does not depend on it.
- sat-hard (L-STRUCT T3 support): parked (NOW roster: "successor only when T3 revives"). Measured state: results.md lines 52-55: w^V(5,5) >= 10,
  s^V(5,5) >= 10, TARGET n=5 weak >= 9 with verified LRAT; s^V(5,5) k=10 and TARGET n=5 strong k=8 UNSAT by CEGAR only, proofs pending; the CNFs
  for those were in experiments/sat-hard/out/ (gitignored) and are GONE in this container (`ls experiments/sat-hard/out`: no such directory);
  regenerate with diag.py per notebook. w^E(4,6) k=8 LRAT also pending. No cadical binary installed here. Next step: none until the Lead routes it.
- counter_qpt growth class (N = 29..40, timeout 600) and counter_dtl (in Oink README, no source upstream): open, low priority, no step scheduled.
- IN FLIGHT: nothing. No background jobs (`pgrep -a python` empty), no timed wakes (fresh container).

## 3. docs/GAPS.md rows owned by L-COMP
None. On trunk feda157 the open table of docs/GAPS.md is empty; the only closed row (G1) is L-STRUCT's. `git grep -i l-comp` on trunk
docs/GAPS.md returns nothing.

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on trunk)
1. D2 (active), change 5 (also TARGET.md §5):
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: every DTL/idtl run on every test game must be strategy-checked by my harness (experiments/harness/verify.py), not by Oink's
   built-in verifier; a run without a checked strategy is not evidence.
2. D1 (active), docs/decisions/D001-launch-brief.md lines 25-26:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   > claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: step 2 is run to find a failure, independently of L-ALG/L-RED; any MISMATCH/BADSTRAT goes to the Lead at once with the shrunk
   instance, and growth fits are reported as data, never as a polynomiality claim.
3. D2 (active), change 1:
   > 1. Section 1: priorities range over {0, ..., n} (d ≤ n + 1); the compression step stays charged to the algorithm.
   Constraint: the input class and the cost model of the runtime measurements follow TARGET.md §1/§3 (bit cost; no preprocessing that Oink does
   for free, hence --no-single --no-wcwc per L22); generated games with sparse priorities are run as given, compression counted in the run.
Also binding, not counted: D1 "Never publish, post, email, submit or contact anyone outside the fleet." (no request to the Oink author for
counter_dtl); Lead readings L22 (pinned command) and L24 (statement frozen; step-2 evidence is input, not a change to §0).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: a solver that never saw the game. In M1, Oink's preprocessing (single-parity and winner-controlled-cycle detection) solved counter_qpt and
the PGSolver families outright, so the first "runtime" numbers measured the preprocessor, not the solver (notebook "Things only I know").
The same trap applies to DTL: run with Oink defaults, the pinned algorithm is bypassed on exactly the families meant to stress it.
Check now in place: experiments/harness/solvers.py:29-30 defines `oink-<s>-raw` = `--<s> -w 1 --no-single --no-wcwc`, and
experiments/hard-families/run_all.sh:30-39 uses only the -raw entries for Oink. For DTL I add `--no-loops` (L22) in a separate pinned entry and
record the exact command line with every result row, so each row is traceable to A_DTL as pinned. Second guard (same family of trap): the harness
never trusts the solver's own verifier; compare.py + verify.py decide MISMATCH/BADSTRAT, and selftest step 4/5 prove they catch a region-wrong
solver and each strategy defect class (run at every verify.sh).
