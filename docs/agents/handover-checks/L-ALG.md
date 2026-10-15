# Handover check: L-ALG (successor session, 2026-10-15 15:45Z; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given), not recalled from notes/L-ALG.md.
Successor of session_01WN44zjFXZSqaL5SwsoDn7d (handover 1017502).

## 1. Branch, head, distance to trunk
- Branch: `claude/l-alg`, tracking `origin/claude/l-alg`, working tree clean before this file.
- Head: 101750209f18f0641dfef6b84cef16141895be78 (1017502, "L-ALG: handover notebook (DONE / IN FLIGHT / NEEDS / things only
  I know: DTL code facts, scripts)").
- Trunk `origin/claude/vibrant-johnson-nxvvxo` at e86f2085e003a5d5bddb516581dfc15ba3e1a93f (e86f208).
- `git merge-base HEAD origin/claude/vibrant-johnson-nxvvxo` = 1017502 = HEAD: the whole lane branch is already merged into trunk.
- `git rev-list --count origin/claude/vibrant-johnson-nxvvxo..HEAD` = 0 ahead; `git rev-list --count HEAD..origin/claude/vibrant-johnson-nxvvxo` = 107 behind.
- Lane commits touching docs/alg, experiments/alg, notes/L-ALG.md on the branch: 32 (`git log --oneline origin/claude/l-alg -- docs/alg experiments/alg notes/L-ALG.md | wc -l`).
- `scripts/verify.sh` at 1017502 in this container (10 s): VERIFY PASS. doc shape PASS; experiment self-checks PASS (experiments/alg/check.sh
  prints "ALG-CHECK PASS"; attr, harness, m2 checks pass); lean NOT RUN (no lean/lakefile); oink smoke NOT RUN (Oink not built here;
  scripts/setup_oink.sh needed before any DTL run).

## 2. Open work and the next step of each
- DTL gauntlet step 4 (the task after "go", Lead brief 16:00Z): a written proof attempt that DTL (Oink dtl.cpp @ 8fbf0a7; pseudocode
  docs/alg/candidates/C5-DTL.md) is polynomial in tangle count and total work at bit cost (TARGET.md section 3) and correct with positional
  strategies, covering the FIFO attractor order and strategy assignment, the pruning greatest fixpoint (best_vertices), the search_rec −1
  branch and its recursion, dominion removal between iterations, and idtl vs dtl; every step cites dtl.cpp line numbers. Inputs measured
  present: docs/lit/T16-dtl-barriers.md on trunk (step 3 signed with caveats); L-RED R8 docs/red/R8-DTL.md at origin/claude/l-red d6496f3
  (head; the notebook's b72707e is an earlier commit of the same file, both exist). Not started. Next step after go: build Oink
  (scripts/setup_oink.sh), re-read dtl.cpp lines 40-202 (attractors), 643-776 (best_vertices), 834-994 (search_rec), 997-1161
  (search/run), then write docs/alg/DTL-proof.md section by section; if a step breaks, record the exact gap and a candidate instance shape.
- DTL gauntlet step 2, formal part: NOW.md lists "formal 10,000-game run + L-COMP strategy check pending". L-ALG's own data (67,000+ games,
  dtl_check.py, verified strategies) is on the branch; the formal run is L-COMP's bench, not this lane's. Next step: none for L-ALG unless
  the Lead asks for the game list.
- T-ALG1 (docs/alg/T-ALG1.md): (a) "psolC complete iff Strahler 1" proved in prose, UNREFEREED; routing to L-LIT + two referees deferred by
  the Lead 11:20Z. Measured: no mention of T-ALG1 in trunk docs/NOW.md, docs/RESULTS.md, docs/GAPS.md, docs/referee/, docs/lit/
  (`git grep T-ALG1 origin/claude/vibrant-johnson-nxvvxo -- docs/NOW.md docs/RESULTS.md docs/GAPS.md docs/referee docs/lit` is empty), so it
  is still unrouted. (c) conjecture "NE'(k) complete iff Strahler ≤ k+1": data only (84,571 Strahler-2 games, 45 Strahler-3 killers); the k=1
  proof is unwritten. Next step for both: none until the Lead routes (a); (c) is parked behind the DTL task.
- C1-C4: DEAD (docs/alg/DEAD.md); no open step. Regressions run in experiments/alg/check.sh at every verify.
- IN FLIGHT: nothing. No background jobs, no timed wakes, no detached processes (fresh container).

## 3. docs/GAPS.md rows owned by L-ALG
None. On trunk e86f208, `grep -n "L-ALG" docs/GAPS.md` returns nothing; the open table is empty and the only closed row (G1, L-STRUCT) is
not mine. T-ALG1 (a)'s own gap list lives in docs/alg/T-ALG1.md, not in GAPS.md (it is unrefereed and unrouted).

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on trunk)
1. D1 (active), docs/decisions/D001-launch-brief.md lines 25-26:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   > claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: DTL is treated as wrong until TARGET.md section 5 steps 1-5 all pass; my step-4 proof attempt is one step, double-refereed
   with every gap listed, and a Lean formalisation is needed for an M4 claim. A broken proof with the exact gap is the deliverable then.
2. D2 (active), docs/DECISIONS.md, changes 2 and 5:
   > 2. Section 6: add a check that the Lean `solve` implements exactly the pseudocode whose running time is analysed.
   >    The referee signs this, and the CHECKER diffs it.
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: the proof must be about the exact pseudocode of C5-DTL.md as it maps to dtl.cpp (no idealised variant), and correctness
   must include positional strategies (the FIFO strategy assignment at dtl.cpp 72-73 and the dominion strategies), not regions alone.
   Also change 1 (priorities {0, ..., n}, compression charged to the algorithm) fixes the input class the bound is stated for.
3. D5 (active), docs/DECISIONS.md:
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18 (verbatim): "M4 (and M4-R) is the fleet's primary aim, and fleet documents and reports drop the "M4 unlikely" framing."
   Constraint: this lane exists under L18; reports state what is proved and what is open without the "unlikely" framing, while D1's
   "treated as wrong" rule stays (L18's last sentence).
Also binding, not counted: D1 "Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision."
(van Dijk's uncommitted counter_dtl is never requested from the author; the fleet proceeds without it, NOW.md Q10).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: an unsound implementation looked like a solver. Twice in this lane: (i) C1/C2's NE(k) first counted a segment's start vertex x as a
"later visit to X" (DTR15-4 Def. 1 says later); with the start counted every p-parity vertex is trivially in W and the solver is UNSOUND
(notebook dfff4c3 lines 90-92); (ii) C4's first implementation omitted the outer fixpoint loop and was WRONG on 7 of 30 library games
(docs/alg/candidates/C4.md lines 26-28). Both were caught only by comparing every decided vertex against Zielonka and running the harness
strategy verifier, never by reading the code. The same trap in the other direction is CLAUDE.md's: a "counterexample" from an unfaithful
implementation is not a counterexample.
Check now in place: experiments/alg/check.sh (run by scripts/verify.sh at every push, "ALG-CHECK PASS" measured above) asserts, on the
whole instance library (experiments/attr/instances, experiments/m2/counterexamples, experiments/harness/bench), that NE(0) equals psolC,
that C1 and C2 at k=1 solve every game with alglib.status == "solved" against zielonka.solve and that verify.check accepts the strategies,
and that the recorded C1 killers and the S_s family still fail at exactly their k. For DTL the same rule is applied through
experiments/alg/dtl_check.py (Oink dtl vs Zielonka/Oink tl, strategies through experiments/harness/verify.py, 67,000+ games), and
C5-DTL.md is a line-mapped transcription of dtl.cpp with trace/NDEBUG code excluded (notebook "DTL facts" item 2) so that the proof,
the attack and the code are the same object. Procedural rule for the step-4 proof: every lemma cites dtl.cpp line numbers and is checked
against a run with `oink --dtl -t -t` on a small instance before it is relied on.
