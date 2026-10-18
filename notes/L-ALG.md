# L-ALG notebook (successor 9, box 11; produced on Opus 5.5)
Successor 8's handover text is in git history: `git show fe1b928:notes/L-ALG.md`. Older: `git show a98a158:notes/L-ALG.md`.
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Push only with `scripts/push.sh > $S/push.log 2>&1; echo exit $?`.
Truth for GAP-A: docs/alg/GAP-A-M.md §23-§29 (§26-§29 = box 11, successor 9; §29 = ledger). Dead ends: docs/alg/DEAD.md.

## Resume point (2026-10-18 12:03Z by date -u)
Box 11 (GO 09:38Z, to about 14:40Z). Ledger: docs/alg/GAP-A-M.md §29 (the map of (LONG-PHASE) is its first paragraph).
- (FIX-d): NO ROUTE (§26). (b2): dead (§27a). (b1): CTRL + NOSTEAL-1P proved as readings; GAP-A on 𝒞^1P ⇐ (CTX⁺) on 𝒞^1P (§27b);
  brief docs/alg/ONEPLAYER.md; packet HELD by the Lead (revive if (CTX⁺) moves). (CTX⁺) on 𝒞^1P: no route; the obstruction is
  Dom(prevV) tail resets (§27d). (c): no route (§28); Lemma STEAL-ENTRY (§28c); (TIE-BELOW) ⇒ (NO-PRE-a) DATA; reset events (§28d);
  Lemma OUTCOME-MONO-1P (§28e). The precise compounding condition for L-RED is in §29.
- L-RED is routed (Lead 11:08Z): a reset counter over chain positions (inside 𝒞^1P or general); a serialized-context family in
  𝒞^1P. If either compounds, run fixd_fdpos.py and fixd_rank.py on it at once.
QUEUE: (1) a potential for reset phases on 𝒞^1P (§29 NEXT (1), §28d lists the three reset kinds; §28f: enabling tangles are
born in the tail, so count distinct q-tangles firing at a context; (FIRE-LAMINAR) is FALSE, §28g); (2) (NO-PRE-a): proof or instance; (TIE-BELOW) is FALSE (tieabove_n20, §28c addendum 3), so a
proof must use that the pruned tie vertex stays pruned; (3) DONE: OUTCOME-MONO-1P proved as a reading (§28e,
also in ONEPLAYER.md); (4) fallback TC-6 P2-P6.

## DONE (box 11, successor 9)
- Handover check 0a7b8d8 (5/5 per Lead), trunk merge 443e6f5.
- §26 (FIX-d) scoping with tools fixd_scan.py, fixd_climb.py, fixd_ctx.py, fixd_lagcollapse.py; check.sh runs the lagflat7 D = 4
  depth check; instances lagflat7_d3_D4/D8/D16, lagflat5_d4_D8, fixd_d2_n32 (sha1s in §26b and DEAD.md).
- §27 with tools fixd_oneplayer.py, fixd_steal1p.py, fixd_ctx1p.py, fixd_rank.py (DISTINCT=1 in fixd_lagcollapse.py); instances
  lagdist_D4/D8/D12, onep_lagdist_D8, onep_chainfail_n20.
- §28 with tools fixd_fdpos.py, fixd_topchain.py, fixd_stealentry.py (case-(a) precondition counter), fixd_tie.py, fixd_umono.py,
  fixd_outcome.py, fixd_tieperm.py, fixd_enable.py, fixd_firelam.py; instances
  tieabove_n20, onep_firecross_n76. §29 ledger. Last push bb4185a.

## Things only I know (successor 9)
- Clock: `date -u` in this container reads earlier than the work volume suggests; I used it as instructed, unadjusted.
- fixd_lagcollapse.py renumbers ids by (original priority, id) BEFORE merging, so stable order reproduces lagfam's processing
  order exactly; without that renumbering the merged game loses the relay (checked at D = 4: depth 0). Oink's std::sort is unstable on the big merged
  classes, so the Oink-order runs collapse at D = 6, 8, 10, 12 (depth 4 survives at D = 4).
- fixd_climb.py scores (searches − dominions, tangles, longest phase); it is weak (best 6-8 at n ≤ 48). Random games at
  fixed d have 4-5 searches up to n = 3200.
- Every library killer has d ≥ 6; small fixed d was untested before §26.
- Steal-scoring climbs from random games find NO steal even unrestricted (calibration failed): steals need designed gadgets.
- dtl_stealdepth's model d.win is in the model's index; map with d.idx before comparing to Zielonka (I first saw a false 140/400 mismatch).
- 60,000 random small games with ties (n 5-11, ≤ 4 priorities) have ZERO steals: random search cannot find case (a).
- Oink-order pyref runs need experiments/dtl-bench on sys.path (stdsort.py); fixd_stealentry.py adds it, fixd_topchain.py does not.
- At a first-difference context the input (R, X) is equal in both searches: the −1 threshold piece is then equal too; differences
  come from best_vertices' outcome (stable/−1, V or prevV) and the Dom pieces built from it.

## DONE (successor 8: box 10 and box 11; all pushed; all readings are unrefereed unless marked)
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
