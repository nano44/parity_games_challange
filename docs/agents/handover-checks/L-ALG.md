# Handover check: L-ALG (second successor session, 2026-10-15 23:35Z; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given), not recalled from notes/L-ALG.md.
Successor of session_012cQPWcEm23KMdMQSvWrULr (handover ed9b87e). Previous check (session_012cQPW..., 15:45Z, 5/5) overwritten.

## 1. Branch, head, distance to trunk
- Branch: `claude/l-alg`, tracking `origin/claude/l-alg`; local was at 1017502 at container start and was fast-forwarded to origin
  (`git fetch origin claude/l-alg && git merge --ff-only origin/claude/l-alg`). Working tree clean before this file.
- Head: ed9b87e65c3fda1a057faddcf4cd26d8ef63288b (ed9b87e, "L-ALG: DTL proof: CHECKER C3c notes N-1..N-4 folded in ...").
- Trunk `origin/claude/vibrant-johnson-nxvvxo` at 31efe342a2b516f4f1cde39edcc6b811732e0f91 (31efe34, "L15 done; all lanes parked").
- `git merge-base claude/l-alg origin/claude/vibrant-johnson-nxvvxo` = ed9b87e = HEAD: the whole lane branch is merged into trunk.
- `git rev-list --left-right --count claude/l-alg...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead, 343 behind.
- Lane commits touching docs/alg, experiments/alg, notes/L-ALG.md on the branch: 55.
- `scripts/verify.sh` at ed9b87e in this container (10 s): VERIFY PASS. doc shape PASS; experiment self-checks PASS (alg, attr,
  harness, m2; the harness self-test's MISMATCH lines are its planted-defect check); lean NOT RUN (no lean/lakefile); oink smoke
  NOT RUN (tools/oink/build absent: scripts/setup_oink.sh must run before any DTL measurement in this session).

## 2. Open work and the next step of each
- DTL gauntlet step 4, docs/alg/DTL-proof.md (statement §0 frozen at ccff864 by L24; §6 status table measured at ed9b87e):
  §1 PROVED; §2.1 soundness + strategies PROVED; §2.2 halting PROVED (exponential bound); §2.3 completeness SKETCH with GAP-C;
  §3 (b)(c)(d) PROVED, (e) conditional on (a); §3(a) tangle count = GAP-A; §4 idtl PROVED; §7 correspondence table unsigned.
  The two open rows of §5: GAP-C (Lemma K; shapes (α) straddling tangle, (β') duplicate with escapes in removed pieces; never
  observed: dtl_dupclimb.py best fitness 0, tc+ N=6 0 duplicate extractions) and GAP-A (D2(a); Lemma S proves strategy determinacy
  for first pieces given R-mono, Lemma D bounds first-piece region sets per top by 2n+1; the ~1.24N² tangles of tc+ are learned in
  LATER pieces, which are re-cut between searches: dtl_pieces_monotone.py; piece refinement and the removal-order invariant FALSE).
  Next step (Lead brief 23:40Z, task B): a fresh invariant that survives re-cutting, or a potential bounding distinct later-piece
  (top, set) pairs, or the counter shape; start from the notebook's "Two most promising untried ideas" (Idea 1 DFS-parent flips
  per top, Idea 2 escape potential), every step marked PROVED/SKETCH/GAP, a GAP or counter shape messaged to the Lead at once.
- C5-DTL.md uniqueness (Lead brief task A; L-COMP divergences #1-#3 recorded in trunk docs/NOW.md and experiments/dtl-bench/README.md):
  C5 fixes regions and strategies but not tangle/iteration counts because of four unstated orders (equal-priority sort, ins(v)
  lists, stored tangle vertex order, dominion-SCC queue order) and the undefined idtl iteration counter; the dominion-extension
  attractor in search() is queue-order dependent (tangles deleted on solve). Next step: draft both options with their cost to the
  proof, (i) pin Oink's orders in C5 and §0, (ii) claim D1/D2 for every order; recommend one; any §0 change goes through the Lead
  and CHECKER (L24). Measured: C5-DTL.md header already claims every equal-priority order (L22); the other three orders and the
  idtl counter are not in C5 (`grep -n -i "ins(v)\|tangle vertex order\|queue order\|iterations" docs/alg/candidates/C5-DTL.md`
  shows ins(v) only as "the edge lists" in §0 and no order statement).
- T-ALG1 (docs/alg/T-ALG1.md): (a) "psolC complete iff Strahler 1" prose proof, UNREFEREED; still unrouted (measured:
  `git grep -l T-ALG1 origin/claude/vibrant-johnson-nxvvxo -- docs/NOW.md docs/RESULTS.md docs/GAPS.md docs/referee docs/lit
  docs/LEAD-STATE.md` is empty; the previous check recorded this as "deferred by Lead 11:20Z", confirmed by the Lead's re-measure).
  (c) NE'(k) conjecture: data only. Next step: none until the Lead routes (a); (c) stays behind DTL.
- C1-C4: DEAD (docs/alg/DEAD.md); regressions run in experiments/alg/check.sh at every verify. No open step.
- IN FLIGHT: nothing. Fresh container: no background jobs, no detached processes, no timed wakes, Oink not built, no debug build.
  The notebook's "per-top run on tc N = 4..16 may still be in a background shell" is gone with the old container; §3(a) has what arrived.

## 3. docs/GAPS.md rows owned by L-ALG
None. On trunk 31efe34, `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -c L-ALG` = 0; the open table is empty and
the only closed row (G1, L-STRUCT) is not mine. GAP-C and GAP-A live in docs/alg/DTL-proof.md §5 (lane file), not in GAPS.md, because
DTL is a step-4 attempt and not a claim; the notebook's NEEDS asks the Lead to route them to L-RED.

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on trunk 31efe34)
1. D1 (active), docs/decisions/D001-launch-brief.md lines 25-26:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   > claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: DTL stays "wrong" until TARGET.md §5 steps 1-5 pass; step 4 needs two referees with every gap listed and, for M4,
   Lean. A proof with GAP-A and GAP-C open is not a result; the deliverable is the exact gap or the counter shape.
2. D2 (active), docs/DECISIONS.md, changes 2 and 5:
   > 2. Section 6: add a check that the Lean `solve` implements exactly the pseudocode whose running time is analysed.
   >    The referee signs this, and the CHECKER diffs it.
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: the analysed object is the pseudocode C5-DTL.md as it maps to dtl.cpp @ 8fbf0a7 (§7 correspondence, signed separately),
   which is exactly why task A (unstated orders) matters: a proof about an under-specified pseudocode is a proof about several
   algorithms; and correctness includes the positional strategies (str[] under the LIFO attractor, dtl.cpp 72-73, 171).
3. D5 (active), docs/DECISIONS.md:
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18 (verbatim): "M4 (and M4-R) is the fleet's primary aim, and fleet documents and reports drop the "M4 unlikely" framing."
   Constraint: this lane exists under L18/L19; GAP-A is pursued as a proof target, not framed as hopeless, while D1's "treated as
   wrong" rule stays (L18's last sentence).
Also binding, Lead readings (not owner rulings, not counted): L22 (pinned command `oink --dtl --no-single --no-wcwc --no-loops` @
8fbf0a7, trace 0, every equal-priority order) and L24 (§0 frozen at ccff864; changes go through the Lead and CHECKER). And D1
"Never publish, post, email, submit or contact anyone outside the fleet": van Dijk's uncommitted counter_dtl is never requested.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: a transcription of the code that is not the code. C5-DTL.md was written with `Q` as a FIFO queue and with "a fresh copy of R
per top, regions overlap" in best_vertices (dtl.cpp 690-699); both were wrong (Q is a stack, uintqueue.hpp `pop()` = `queue[--pointer]`;
one CurR per round, consumed across tops). L-RED's R8 built a FIFO-layer argument on the first error and had to withdraw it (R8 §9),
and the proof's strategy-determinacy question (Lemma S) only makes sense under DFS order. Both errors were found by running a debug
build with `-t -t -t` on a hand-built 5-vertex game (experiments/alg/instances/dtl_proof_c1.pg) and comparing the printed attraction
events with the pseudocode, never by re-reading. The same family of trap is now reported by L-COMP's second implementation: C5
leaves four orders and the idtl counter unstated, so a faithful implementation of C5 differs from Oink in tangle counts (up to 8 per
game) while agreeing on regions and strategies.
Check now in place: (i) C5-DTL.md is a line-mapped transcription (every primitive cites dtl.cpp line numbers) and DTL-proof.md §7 is
an itemised correspondence table to be signed separately (TARGET §6 / D2 change 2); (ii) every proof lemma is checked against a
`-t -t` trace on a small instance before it is relied on (notebook rule, §6 worked example c3); (iii) the second independent
implementation from C5 alone (L-COMP dtl_py.py, 238,071 games) is the mechanical test that the text and the code are one object,
and it is what found the remaining under-specification; (iv) experiments/alg/check.sh (verify.sh at every push) keeps C1-C4's
regressions and dtl_check.py keeps dtl/idtl against Zielonka with harness-verified strategies on the pinned command.
Procedural rule carried forward: no measurement in this session before scripts/setup_oink.sh (release) and the notebook's item-6
debug build; a proof step about an order is tested against both an Oink run and the C5 reading, since they may now differ.
