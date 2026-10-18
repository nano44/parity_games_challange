# L-ALG notebook (successor 8, end of box 11 handover; produced on Opus 5.5)
Overwritten at the box-11 handover (Lead decision 09:28Z by date -u: successor now). Older content, including boxes 1-10 resume
points, tools and traps, is in git history: `git show a98a158:notes/L-ALG.md` (box 10/11), `git show 8a9c0f44:notes/L-ALG.md` (boxes 1-7).
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Push only with `scripts/push.sh > $S/push.log 2>&1; echo exit $?`.
Truth for GAP-A: docs/alg/GAP-A-M.md §23-§25 (§24h is the box-10 ledger, §24i the single named target, §25 box 11).
Dead ends: docs/alg/DEAD.md.

## Resume point
Successor 9 starts here. Owner D13 (verbatim): "Keep working on the dtl and also c". Lead reading L34: the DTL proof lane continues
at the D7 rate. Box-11 goal (Lead): the L32 progress criterion. Either a proof route for (LONG-PHASE) (§24i), or a PROVED polynomial
bound on the searches of A_DTL on a nontrivial STRUCTURAL class (a property of the game, infinite).
QUEUE (Lead 09:28Z), in order:
1. (FIX-d) scoping. The verdict goes to the Lead within your first ~1.5 h.
   - Target: the searches of A_DTL are ≤ n^{f(d)} for games with d priorities, for an explicit f; failing that, d = 3 alone
     (d = 2 only with a reason why it is not already trivial for DTL).
   - Measure the max searches against n on random d = 3 / 4 games (gen.random_game in experiments/harness; dtl_step5stats
     RANDOM/SEED; renumber to d priorities), and on lagfam at few priorities.
   - Write the induction skeleton: which signed lemma covers which level, and where (CTX⁺) / (LONG-PHASE) enter at fixed d.
   - If (CTX⁺) or (LONG-PHASE) is as open at d = 3 as in general, say exactly where. Then fall back to another structural class
     under the same test.
2. TC-6 steps P2-P6 (§25b), FALLBACK ONLY, labelled "single family, not L32 progress" (the Lead objected to TC-6 as a target at
   09:16Z: it is the family tangle learning was built to beat).

## DONE (box 10 and box 11; all pushed; all readings are unrefereed unless marked)
- Box 10 (§23v-§24i; ledger §24h):
  - packet-11 imports (§23v; N11-b1 has two signatures);
  - Lemma QUIET-BLOCK (§23w) and EXIT-ORIGIN (§23x), frozen packet candidates (the Lead did NOT send packet 12);
  - DEF-SHRINK (§24a) and SPLIT (§24b): GAP-A ⇐ (CTX⁺) ∧ (XPAIRS-POLY);
  - R39 / lagfam analysis (§24f-§24g): the relay is combinational in T, not a counter; all totals are polynomial (degree ≤ 3) on
    lagfam D = 2..12;
  - the single named target (LONG-PHASE) (§24i).
- Box 11:
  - §25a TC-6 named (now a recorded alternative, not a target).
  - §25b run schema: PASS for N = 3-8, 10 in both orders; proof plan P1-P6.
  - §25c P1 PROVED (reading): compressed priorities of tc(N) and W_E = (Even-bit minus Even-B) ∪ Odd-B.
  - Merged trunk with D13/L34 (merge commit).

## IN FLIGHT
- Nothing is running. Scratchpad runs die with the container.

## NEEDS
- Successor: queue items 1-2 above.
- Lead: none open (the packet-12 decision is made: not sent).
- Owner: none.

## Things only I know
- Fixed d, facts that are not yet in the files:
  - lagfam needs MANY priorities: d = 3D + 14 (20, 26, 38, 50 at D = 2, 4, 8, 12). R39: d = 23 (depth2_n39), 28 (depth4_n53).
    So the only family with growing local constants (depth, exits ≈ D) has d growing linearly. Whether a few-priority version
    exists is untested. Its relay levels use distinct top priorities T_{-1} > T_0 > ... (R39 §2), so each level costs ≥ 1
    priority by design.
  - tc(N): d = 4N + 3 (Lemma P1a), A_DTL 6 searches.
  - Searches per phase at fixed d have NOT been measured by me.
  - Induction idea for FIX-d: search_rec recursion lowers the context, NOT the priority; the threshold loop and regions are
    per priority level. A natural induction is over the top priority of the context: the root call's regions at the top
    level q are full attractors (threshold = q = max), so level q behaves like a Büchi round. Unverified.
- Tools new in boxes 10-11 (flags in their docstrings):
  - dtl_drthr.py, dtl_exitshape.py (EX_DEF=1 needs RM_LIGHT unset), dtl_netgrowth.py, dtl_roundfalls.py, dtl_exitclimb.py,
    dtl_firedlocal.py, dtl_quietlin.py;
  - dtl_defsplit.py (RM_LIGHT unset);
  - dtl_exitlead.py;
  - dtl_totals.py (RM_EXCL=1 RM_LIGHT=1 RM_DV=0; per-context D_R, Σk, X_R, max exits, #fired⁺; the growth-table tool);
  - dtl_tcschema.py (TC-6 schema; N ≥ 12 runs out of memory in the Python model).
- lagfam: experiments/red/lag/lagfam.py D OUT (from trunk; it needs lag4.py and gb.py beside it).
- Traps:
  - dtl_stealdepth prints "max k" BEFORE the depth histogram; do not cut its output with tail -N at large D.
  - Stamp every message with date -u. I once sent a guessed time and corrected it to the Lead.
  - The local branch is stale at container start; fetch and fast-forward first.
- Oink trace: `oink --dtl ... -t G.pg` prints one "best vertices" line per best_vertices call (with "(stable)" for res = 1),
  plus "new tangle" and "dominion" lines. A good first look at a run's schema.

## Dead ends
- Box 10-11 successor 8:
  - G23u RV-rise fix (spp_chain_up_n43);
  - NET-GROWTH (cm_viol_oink_n28, lex_viol_oink_n20);
  - QUIET-LIN (dtl_cross3_n14, fired18_stable_n20) and QUIET-NEWV (spp_final_n30, spp_n30);
  - EXIT-LEAD-DISTINCT (depth2_n39 etc.);
  - with L-RED DE21: (EXIT_c) for every constant and (STEAL-DEPTH_D) for every constant D (lagfam).
  - All are in docs/alg/DEAD.md with their instances.
- Earlier: see docs/alg/DEAD.md and git history of this file.

## Sources opened
- Successor 8: no external sources opened. Readings are of dtl.cpp @ 8fbf0a7, game.cpp (renumber 618-637) and tc.cpp @ 8fbf0a7,
  via tools/oink/src; and of the referee reports R-P11 / R2-P11.
- The GandALF 2019 Two Counters paper (doi:10.4204/EPTCS.305.8) was NOT opened; only the fleet's M1 bench is cited for TC.
- Earlier sources: git history of this file.
