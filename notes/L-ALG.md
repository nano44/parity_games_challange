# L-ALG notebook (successor 10, box 12; produced on Opus 5.5)
Successor 9's handover text is in git history: `git show a97f451:notes/L-ALG.md`. Older: `git show fe1b928:notes/L-ALG.md`.
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Push only with `scripts/push.sh > $S/push.log 2>&1; echo exit $?`.
Truth for GAP-A: docs/alg/GAP-A-M.md §23-§30 (§30 = box 12, successor 10; §29 = box-11 ledger). Dead ends: docs/alg/DEAD.md.

## Resume point (2026-10-18 19:42Z by date -u; box 13, GO 17:17Z by the Lead's clock, to ~21:30Z; same session)
Ledger: GAP-A-M §33 (𝒞^1P reduction), §34 (two-player, (TREE-PIECE)); box 12 = §30-§32 (see below). L32: NOT met.
- PROVED (readings, unrefereed): Lemma W (§33a); Lemma SAME-CTX (§33b; mechanical check 26,155 class pairs, 0 failures);
  Corollary: on 𝒞^1P, (VR-NEW_all) at a transition ⇐ (XCTX@p0). So GAP-A on 𝒞^1P ⇐ (XCTX@p0) ∧ (CHAIN-CHANGE), both DATA.
  Referee packet: HOLD (Lead 19:03Z). Triggers: (a) a proof route for (XCTX@p0), or (b) (TREE-PIECE⁺) survives L-RED's box-13
  attack AND a proof sketch exists.
- (TREE-PIECE⁺) (§34b-c): key (v, depth, position in parent, ρ, |R|, |V|) over every call's PIECE; every transition whose call
  sequence changes gives some vertex a never-held key. DATA: 0 violations, library both orders, L-RED's instances, tc+ N ≤ 5, climbs.
  Literal (TREE-PIECE) FALSE on identical call trees (tp_ident_n20). Consistency with known results: §34d. L-RED's split: §34e (fails).
- KILLED this box: literal CORE, (SIG-DISJ) (onep_vrj_n40), (TREE-PIECE) literal (tp_ident_n20), membership tree keys, L-RED split.
IN FLIGHT 19:42Z (scratchpad, nothing depends on them): two-player climbs vs (TREE-PIECE⁺): tp2_b (from vrV_viol_n40, Oink),
tp2_c (from tc+ N = 2, stable).
QUEUE for the successor:
(1) (XCTX@p0) on 𝒞^1P: compare two DIFFERENT equal-size contexts at the first changed position; no monotone link known.
(2) A proof sketch for (TREE-PIECE⁺), recursive SAME-CTX: per call, X = parent piece \ R; in two-player games outcomes are not
    monotone (SAME-CTX fails 6 times, fall3_n76), so the class argument does not transfer; identical-tree runs need (FALL)-type bounds.
(3) Run b12_ident.py TREE=1 / tp_score on every new L-RED instance at once.

## DONE (box 12, successor 10)
- Handover check 50e66d3 (5/5 per Lead), trunk merges 781790d and the box-start merge.
- Oink built (scripts/setup_oink.sh exit 0), so verify's smoke step runs.
- §30 with tools b12_topchain.py (class set + TOP-CHAIN@R scan), b12_topclimb.py (climb, --check), b12_pertop.py (tangles
  learned per (phase, top)), b12_mono.py (re-cut-proof potentials, per_position); instance onep_topuniq_n20 (check.sh).
- §31 with tool b12_nopre.py (scan / climb); instance nopre_near_n20 (near miss, pinned Oink 5 iterations verified).
- Box 13: §33 (b12_core.py), §34 (b12_ident.py incl. climb, b12_split.py); instance tp_ident_n20. Pushes 4f2b321, 1fac015,
  d2784b1, 4101eb2 and the box-end commit.
- §32 with tools b12_pot.py (climb: KEY=..., MARGIN=1), b12_fdkey.py, b12_noret.py, b12_margin.py, b12_fdwit.py; instances
  onep_fdkey_n20, onep_vr_n12, onep_vrj_n40 (all 𝒞^1P, pinned Oink verified). Pushes: 50e66d3, c81bb8f, 6f6a246, 41abf76,
  e2132ae, 011e663, 1618e76, and the box-end commit.

## Things only I know (successor 10)
- TRAP that bit me: four Lead messages (14:42Z-17:10Z) sat unread until 17:15Z because I never called ReadNotifications
  between tool runs. Call it after every long wait or push, not only when a system notice says so.
- `date -u` advances much more slowly than the work done (as successor 9 noted); timestamps are as printed, unadjusted.
- `pkill -f <name>` / `pgrep -f` / `ps | grep <name>` from the Bash tool match the tool's OWN shell when <name> is anywhere in
  the command (exit 144, the rest of the command is lost). List PIDs with `ps -eo pid,args | awk '$2=="python3"'` in one call,
  kill by number in another.
- b12_nopre.py used to set ONEP_ANY=1 at import, which makes fixd_oneplayer.inclass() always true for every importer
  (fixed 41abf765). Any tool that imports a climb module: check `'ONEP_ANY' in os.environ` after import.
- Running two RM-model (dtl_rootmono) library scans at once got both silently killed (empty output, likely OOM). Run them one at
  a time; SE-model (fixd_stealentry) scans are light.
- With all priorities distinct, the stable and Oink index orders coincide; the two order data then differ only in ins_desc,
  TV_SORTED and PEARCE (fixd_stealentry.run). Map model index i to the input vertex with sorted(range(n), key=(prio, id)).
- Random-forced class games rarely fire tangles at all (221 firing contexts in 891 games); Zielonka-forced trial 0 is richer.
- leanT_N files parse; a few library files (with "% start" lines) do not, and classgames() skips them silently.
- classgames() uses in-class games AS GIVEN (ties possible) unless DIST=1; for 𝒞^1P statements always run with DIST=1.
- b12_pot / b12_fdkey numbers depend on the corpus seed: TRIALS=3 SEED=2 NMAX=200 is the set used in §32 (1,086-1,094 transitions).
- Climbs at n = 40 take ~1 s per step (RM-free SE model); the RM-model climbs (b12_fdkey) are slower and memory-heavier.

## DONE (box 11, successor 9)
- Handover check 0a7b8d8 (5/5 per Lead), trunk merge 443e6f5.
- §26 (FIX-d) scoping with tools fixd_scan.py, fixd_climb.py, fixd_ctx.py, fixd_lagcollapse.py; check.sh runs the lagflat7 D = 4
  depth check; instances lagflat7_d3_D4/D8/D16, lagflat5_d4_D8, fixd_d2_n32 (sha1s in §26b and DEAD.md).
- §27 with tools fixd_oneplayer.py, fixd_steal1p.py, fixd_ctx1p.py, fixd_rank.py (DISTINCT=1 in fixd_lagcollapse.py); instances
  lagdist_D4/D8/D12, onep_lagdist_D8, onep_chainfail_n20.
- §28 with tools fixd_fdpos.py, fixd_topchain.py, fixd_stealentry.py (case-(a) precondition counter), fixd_tie.py, fixd_umono.py,
  fixd_outcome.py, fixd_tieperm.py, fixd_enable.py, fixd_firelam.py; instances
  tieabove_n20, onep_firecross_n76. §29 ledger. Last push: see git log (box-end commit after 485d0d9).

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
