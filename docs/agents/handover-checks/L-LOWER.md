# Handover check: L-LOWER (successor session, 2026-10-15 08:35Z; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given), not recalled.

## 1. Branch, head, distance to trunk
- Branch: `claude/l-lower`, tracking `origin/claude/l-lower`, working tree clean.
- Head: f0e5e8f6fa87be48988e53e3aeb6da90462c3bbd (f0e5e8f, "L-LOWER handover: notebook ...; 100-game minimal UNSAT core").
- Trunk `origin/claude/vibrant-johnson-nxvvxo` at 9958cf1db1ba345864b1321f09c72285e0795657; merge-base fe676d9.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 29 ahead, 18 behind.
- `scripts/verify.sh` at f0e5e8f: VERIFY PASS (doc shape PASS; experiment self-checks PASS incl. experiments/lower/check.sh
  "L-LOWER CHECK PASS"; lean NOT RUN, no lakefile; oink smoke NOT RUN, Oink not built in this container).

## 2. Open work and the next step of each
- T-L2 theory box (the task after "go"): not started. Next step: notebook T-L2 plan step 1, minimise the 100-game core
  experiments/lower/b2_n4_k6_core_min.json (measured: 100 games, list of (prio, owner, succ); by #Odd vertices {0: 2, 1: 20,
  2: 43, 3: 28, 4: 7}; by #P_2 {1: 21, 2: 56, 3: 22, 4: 1}; the 400-game core b2_n4_k6.json: by #P_2 {1: 105, 2: 210, 3: 81,
  4: 4}), then the human proof for "no 6-gate program at n = 4, two-player" (step 2), then the growing family (step 3).
  Kill criterion as written in notes/L-LOWER.md.
- T-L1 (one-player, B_1(n) = ω(n)): PARKED by the Lead 07:50Z; data against (B_1(1..5) = 2n − 2). No next step unless unparked.
- Structural n = 5 runs (window-3 chains k = 8, window-2 k = 9): STOPPED, not concluded, no bound; nothing running now
  (no detached processes, no timed wakes; notebook "IN FLIGHT: (none)").
- Refereeing: L1-statement v2 OK (R-L1b); Lemma 2.1' OK; Theorem B OK with one change (Claim 3 case t < t' < a), which is
  present in docs/lower/L1-report.md §2 Claim 3 at f0e5e8f. B_1(5) = 8, B_2(4) = 7 are data points, unrefereed; nothing is
  due to REFEREE until a claim is to be recorded. L-LIT novelty check of T-L1/T-L2: parked.

## 3. docs/GAPS.md rows owned by L-LOWER
None. `grep -n "L-LOWER" docs/GAPS.md` returns nothing; the only row (G1, L-STRUCT, closed) is not mine.

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md)
1. D1 (active), M3 definition, docs/decisions/D001-launch-brief.md lines 39-41:
   > - M3 Partial results: for example a new polynomial class or structural parameter, a lower bound
   >   for a broader algorithm model, or a tighter analysis of a known algorithm. Each must be new
   >   against the literature map.
   Constraint: a T-L2 bound is M3 only if L-LIT finds it new; the SLP model (Def. 1.3) must be compared against CDHL's and ANP's.
2. D2 (active), change 1, docs/DECISIONS.md:
   > 1. Section 1: priorities range over {0, ..., n} (d ≤ n + 1); the compression step stays charged to the algorithm.
   Constraint: the Büchi alphabet {1, 2} and the one-vertex priority-2 game need the translation of L1-statement §1.0; every
   lower bound must hold a fortiori on the TARGET class.
3. D1 (active), docs/decisions/D001-launch-brief.md:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   Constraint: sources are opened and quoted, never contacted; novelty questions go to L-LIT through the Lead.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: ANP's bound n^{lg(d/lg n)+O(1)} (LIPIcs.CSL.2021.9 Cor. 3.7) was taken, via the landscape doc and L-LIT's T7, as the
non-adaptive (SLP) upper bound. It is not: Lemma 3.6's proof is a worklist that re-evaluates only changed equations, i.e.
adaptive; only the symmetric two-tree bound n^{2·lg(d/lg n)+O(1)} (Lemma 3.2, p.9:9) is straight-line.
Check now in place: docs/lower/L1-statement.md Transfer 2.4 carries the CAUTION paragraph naming Lemma 3.6 and the worklist;
REFEREE R-L1 (docs/referee/2026-10-14-L1-statement-check.md lines 114-120) and L-LIT T9 (docs/lit/T9-L1.md line 66,
"L-LOWER's non-adaptive reading is confirmed: the best known oblivious exponent is 2·lg(d/lg n)+O(1)") both confirm it; T7 was
amended. Procedural rule: every cited bound goes into the notebook's "Sources opened" table with theorem number and the
adaptive/non-adaptive reading before it is used (CLAUDE.md: the landscape doc is never a source by itself).
Second, tooling trap: SAT instances above ~20·10^6 clauses reach 8 GB and are OOM-killed by the 16 GB cgroup (window-2 k = 9
run died at 2483 games). Check: at most two SAT runs at once, detached with `setsid nohup`, resumed from the .subset.json
checkpoints (notebook "Things only I know").
