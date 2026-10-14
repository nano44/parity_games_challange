# Referee report: code review of L-COMP's gauntlet bench (experiments/) for landing on trunk

Referee: REFEREE. Date: 2026-10-14. Routed by the Lead 2026-10-14 19:11Z (pipeline review step).

## Range and scope
- Range: claude/l-comp, merge-base a3777f1 .. de7ea19, everything under experiments/ (146 files, +6004 lines).
- Reviewed by reading: experiments/harness/zielonka.py, verify.py, compare.py, gen.py, exhaustive.py, solvers.py,
  selftest.py, xverify.py, check.sh, README.md, validation.md, pg.py (read earlier), experiments/hard-families/sweep.py,
  experiments/m2/check.sh. Skipped as already refereed: pgsolver_port.py, pgsolver_si.py
  (docs/referee/2026-10-14-pgsolver-ports.md). Not reviewed (out of the Lead's focus list): avh.py, shrink.py,
  families.py, verdicts.py, run_*.sh, make_hkp.py, result tables and plots.
- Executed: a detached worktree of de7ea19 with the built Oink 8fbf0a7 linked in; scripts/verify.sh clean; six planted
  faults (four solver faults through compare.py, three checker faults through the self-test); scripts/verify.sh with a
  planted fault in zielonka.py. Fault scripts: docs/referee/scratch/harness_faults.py.

## Verdict: CHANGES (2 findings on the self-test's coverage; the solver, verifier and comparison code are correct)

Findings 1 and 2 are small additions to selftest.py; nothing in zielonka.py, verify.py, compare.py, sweep.py, gen.py
or exhaustive.py needs to change. With 1 and 2 done I would sign OK for landing.

## What was checked and holds

### zielonka.py (reference solver and brute-force oracle): OK
- `attractor`: standard; the opponent's counter counts distinct successors in `alive` and `pred` lists each pair
  once (pg.py builds `pred` from `set(s)`), so the decrement matches. ✓
- `solve_sub`: textbook Zielonka. Strategies: in the "opponent wins nothing" branch, attractor strategy on A \ top,
  any `alive` successor on top, the sub-call's strategies elsewhere; this wins because either top (the maximum of
  `alive`, of p's parity) is seen infinitely often or the play settles in alive \ A, a p-trap complement where the
  sub-strategy wins. In the other branch W[1−p] is closed in the full subgame because V \ A is a p-trap, so the
  sub-call's strategies for 1−p stay valid; B's attractor strategies and the second call's strategies compose. Stale
  entries for vertices re-solved with a different winner are masked by `owner == win` in `solve_with_strategy`. ✓
- `brute_force`: enumerates Even's positional strategies; `_odd_wins_one_player` marks Odd-winning vertices as those
  reaching a cycle whose maximum is odd (per odd priority p: vertices of priority p on a cycle inside priorities ≤ p,
  then backward reachability). Correct by positional determinacy, and independent of any attractor code. ✓

### verify.py (positional-strategy verifier, D2 change 5): OK as a complete certificate checker
- Closure: every winner-owned vertex has a strategy edge inside its region; every opponent vertex in a region has all
  successors inside it. ✓
- Winning: in the region's one-player graph (winner's vertices keep only the strategy edge), recursive SCC
  decomposition with the test "top priority of each non-trivial SCC has the winner's parity, then remove the top
  vertices and recurse". Sound and complete for "no cycle with opponent-parity maximum", and together with closure
  this certifies the solution: a play consistent with the strategy stays in the region, its infinitely-often set is
  strongly connected and its maximum lies on a simple cycle inside, whose parity the test checked. ✓
- Consequence worth stating: a solution with wrong regions can never pass verify.py (both regions would be dominions
  with winning strategies). So BADSTRAT alone already catches wrong regions; MISMATCH is the second, independent net.
  My run confirms it: on 14 random games where a min-parity solver's regions were wrong, verify.py rejected all 14.

### compare.py, sweep.py: OK
- Reference run first and its own strategies verified; MISMATCH before BADSTRAT; exit 1 on MISMATCH/BADSTRAT/error;
  `--stop-first`; CSV. sweep.py: every finishing solver verified, pairwise region agreement, py-zlk below --ref-max-n,
  exit 1 on any disagreement. ✓

### gen.py, exhaustive.py: OK
- splitmix64 keyed by sha256 of the parameter string; rejection sampling; partial Fisher–Yates. Deterministic across
  Python versions, pinned by the self-test's corpus hash. ✓ exhaustive.py counts (8 / 324 / 74088) re-derived. ✓

### check.sh inside scripts/verify.sh: confirmed
- Clean de7ea19: `PASS experiment self-checks (experiments/*/check.sh)`, all five self-test steps and the m2 CE1
  regression, `VERIFY PASS`.
- With `p = (d + 1) % 2` planted in zielonka.py: self-test steps 2 and 3 fail, `SELFTEST FAIL`,
  `FAILED experiment self-checks`, `VERIFY FAILED`. ✓

## Planted solver faults (through compare.py, `--ref py-zlk`, seeded corpus of 60 games, n ≤ 12)
| fault | how | result |
| --- | --- | --- |
| winner of one vertex swapped (strategies untouched) | flip win[1] | MISMATCH on 60/60, exit 1 |
| strategy leaves its region (regions right) | redirect one winner-owned vertex to an out-of-region successor | applied on 11/60 games, BADSTRAT "strategy leaves the region" on 11/11, exit 1 |
| strategy stays in region, opponent closes a losing cycle | redirect inside the region to a successor that creates an opponent-parity top cycle | applied on 30/60, BADSTRAT "opponent cycle with top priority q through v" on 30/30, exit 1 |
| parity convention flipped (solver reads the game as min-parity) | solve the ρ ↦ M − ρ game | wrong regions on 14/60, MISMATCH on 14/14, exit 1; on the other 46 the two conventions give the same regions and a valid strategy, i.e. a correct output |
Direct unit checks: missing strategy and non-edge strategy are rejected with the expected messages.

## Planted checker faults (through the self-test)
| fault | self-test result |
| --- | --- |
| compare.py: region comparison disabled (`if diff:` → `if False:`) | **SELFTEST PASS** (with Oink). Step 4's wrong solver writes no strategies, so it is flagged BADSTRAT and the exit code is still 1. |
| verify.py: cycle test removed (closure only) | SELFTEST FAIL, but only through step 5 (`DIFF game 1: mine=True oink=False`); steps 1–4 pass. |
| both of the above, Oink hidden | **SELFTEST PASS** (steps 3 and 5 print NOT RUN). |

## Findings
1. **selftest.py step 4 does not test what it says.** It asserts only `rc == 1`; a compare.py that ignores region
   mismatches passes because the wrong solver is caught as BADSTRAT. Fix: call `compare.judge` on a wrong-region
   solution (or read the status rows) and assert the status is exactly `MISMATCH`; and give the wrong solver the
   reference's strategies so that only the region path can flag it.
2. **No Oink-independent negative test of verify.py.** Steps 1–4 accept a verifier that skips the cycle test; only
   step 5 (Oink's `verify`) rejects it, and step 5 is NOT RUN without Oink, so on a machine without Oink the gate
   passes with a vacuous verifier. Fix: add deterministic hand-built cases that `verify.check` must reject (strategy
   leaving the region, in-region losing cycle, missing strategy, non-edge; the four games in
   docs/referee/scratch/harness_faults.py or smaller) and one it must accept; independent of Oink.
3. Cosmetic: selftest.py prints "2. brute force == py Zielonka on 300 tiny games" after FAIL lines of step 2 (the
   final SELFTEST line is right). sweep.py's docstring advertises `--budget`, which is not implemented. compare.py
   with `--csv` on an empty corpus raises on `rows[0]`.
4. Note for the gauntlet design, not a defect: a parity-convention flip is caught only on games where min- and
   max-parity regions differ (14 of 60 here); the 10,000-game corpus has plenty, but any family-only bench should
   include such games.

## Gaps
- Not machine-checked beyond the runs above; the correctness arguments for zielonka.py and verify.py are my reading.
- avh.py, shrink.py and the hard-families drivers were not reviewed (not in the routed focus).
