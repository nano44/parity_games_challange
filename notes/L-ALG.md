# L-ALG notebook (successor 7, session_01FBjx3fNL2aVsbUmNkN2fC3, end of box 8; produced on Opus 5.5)
Successor 8: START at GAP-A-M §23o (the GAP-A position in one place), then §23p, then §23n (the ledger).
Overwritten at the box-8 handover (Lead 17:10Z by date -u; WATCHDOG measured the context above 600k). Box 8 continues
with the successor (GO 16:43Z by date -u, box to ~00:45Z; check-in ~20:45Z). Older notebook content (boxes 1-7 resume
points, dead ends, sources opened) is in git history: `git show 8a9c0f44:notes/L-ALG.md`.
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Push only with `scripts/push.sh > $SCRATCH/push.log 2>&1; echo exit $?`.
Truth for GAP-A: docs/alg/GAP-A-M.md §22 (22a-22x; §22x is the box-7 ledger) and §23 (box 8). Dead ends: docs/alg/DEAD.md.

## Successor 7 (session started 17:38Z by date -u; GO 17:46Z; box to ~00:45Z; check-in ~20:45Z; produced on Opus 5.5)
Handover check 5/5 (ca909c3). Box-8 results so far, all in GAP-A-M §23b-§23e:
- §23b: (STEALER-MONO) KILLED by stealer_viol_n76 (L-RED, stable order; RESULTS DE19, Lead-verified). Obstruction: upward
  migration, i.e. a higher region captures the region's fired tangle whole. (STAYS-MET), (STEAL-ONCE*) and (STOLEN-PERM)
  survive there. Chain STOLEN-PERM ⇒ STAYS-MET ⇒ NO-REFIRE ⇒ STEAL-ONCE* (each arrow PROVED, reading).
- §23c: shrink-vertex analysis (dtl_shrinkdep.py). Lost prefix vertices fall into three classes: A, under a relevantly
  stolen path tangle; B, region top gone; C, escape cascades (an escape left the prefix; checked on 2 cases). (DEP-SAFE)
  holds 1,169/1,169, but the single-parent forest misses the C class.
- §23d: (FIRED-R) on long phases (L-RED filter): at most 3 fired, ratio ≤ 0.375; long-phase contexts are small (|R| ≤ 9).
- §23e: on all 32,024 contexts, (FIRED-STEP) with a constant, (FIRED-LAMINAR) and (FIRED-TOP-INJ) are KILLED
  (fired18_stable_n20, c6_replay3_n32). (FIRED ≤ |R|) is tight DATA (18/18). That tight case is mostly singleton tangles
  (14 of 18), so it looks fragile.
Tools: dtl_stealtrace.py, dtl_shrinkdep.py, dtl_firedlong2.py (flags in their docstrings).
- §23f: (STEAL-ONCE*) KILLED (RESULTS DE20, L-RED stealonce_viol_n76, stable order). It takes down STOLEN-PERM, STAYS-MET,
  NO-REFIRE and DEP-SAFE. R11 count with the factor k: F_R ≤ 3·Σ_q k_q ≤ 3k_R(|R|+1)|R|·#fired(R).
- §23g: Lemma CHARGE plus the depth count: (STEAL-DEPTH_D) ⇒ Σ_q k_q ≤ 2Q^{D+1} (reading). PACKET 9 went to both referees,
  pinned at trunk c5e2b4d (Lead 20:11Z). DO NOT EDIT §23f-§23g while it is out; corrections go to a new subsection, and tell
  the Lead. A self-contained copy with dtl.cpp lines is docs/alg/STEAL-DEPTH.md.
- §23h: NO-RETURN KILLED (same instance). §23i: CTX-LAMINAR KILLED (ctx12_oink_n40, dtl_searches15_n24). §23j: (CTX⁺) context
  structure data; no statement yet.
- Running (dies with the container): experiments/alg/dtl_depthclimb.py, 4 climbs from stealonce_viol_n76 (seeds 1-4, 600
  steps). Output goes to the scratchpad dc/ folder; best_s*.pg holds the best instance. Any depth ≥ 2 or k ≥ 3 goes to the
  Lead at once.
- Flags added to dtl_rootmono.py (default output unchanged): RM_LAM=1 (CTX-LAMINAR), RM_BIRTH=1 (CTX-BIRTH).
- Trap: in-process order switches must set os.environ["DTL_ORDER"], because dtl_deficit.build reads it.
- Packet 9 is SIGNED by both referees (R-P9, R2-P9, trunk 25111fa); the imports are in §23k (l-alg 67b9e05). Working
  conclusion: GAP-A ⇐ (CTX⁺) ∧ (FIRED-R) ∧ (STEAL-DEPTH_D for a constant D), given STR-DET; all three premises are DATA. The
  Lead drafts RESULTS R12.
- §23l: PIECES-LAMINAR killed; the piece count tracks S. §23m: FIRED ≤ |R| climbs stop at 1.0; FIRED-HALL killed.
- Climbs running: depthclimb s1 and s4 (from stealonce_viol_n76), s5 (stealer_viol_n76) and s6 (fall3_n76). A watcher fires on
  depth ≥ 2, k ≥ 3 or INCOMPLETE.
- Trap: attribute-name clashes between subclasses of dtl_rootmono.RM (the _spR bug). Use distinct names.

## DONE
Signed by both referees (all readings of dtl.cpp @ 8fbf0a7, every order datum):
- (S0), PREFIX-MONO, POS-FALL, ROOT-BOUND (packet 4).
- STR-DET (packet 5).
- The Dom budget per input, and F_R = every non-rise (packet 6).
- EXACT, PREFIX-MONO-X (packet 7); EXACT*, PREFIX-MONO-X* (packet 8).
Reduction (signed conditional):
- GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R), given STR-DET.
- Per phase: S − 1 ≤ Σ_R 2(F_R + 1)(H + 1) + 2n(|C_T| + |C_Dom|) + 1, with F_R ≤ 3(|R| + 1)|R|·#fired(R) under (STEAL-ONCE*).
Box 8 so far (GAP-A-M §23a). The invariant behind (STEAL-ONCE*), DATA only, 0 exceptions:
- (STAYS-MET): once a fired tangle t is relevantly stolen at a step σ, every later prefix at σ still meets t, and t
  never fires at σ again. (STAYS-MET) ⇒ (STEAL-ONCE*).
- Sharper:
  - (STOLEN-PERM): the stealing vertices t ∩ P(σ⁺) stay in every later prefix at σ.
  - (STEALER-MONO): the region that holds them never loses any vertex afterwards.
- Counts: corpus plus fall3/fall4/fallv/f1_two* 216 / 214; cross unions 377 / 456; mixed unions 644 / 849
  (Oink / stable).
- FALSE: (MET-MONO), "every met tangle stays met" (117 of 119 shrink pairs lose one).
- Prefixes DO shrink between visits (119 of 8,252 pairs), always at relevant steals.
- PROVED (reading): (STAYS-MET) at round 1, step 2. The first region Cl({τ₁}; T) has no exclusions, so the step-2
  prefix is monotone.
- THE EXACT MISSING STEP: from step 3 on, region j can lose vertices when one of its own fired tangles is relevantly
  stolen by a region above it. Prove that this never happens AFTER region j has stolen from a later step. STEALER-MONO
  says it doesn't, which would be an ORDER on steals: a region steals only after the regions above it have stopped
  changing. Attack shape for L-RED: region 2 steals from region 3, and later region 1 (monotone) grows into a tangle
  that fired in region 2.

## IN FLIGHT (box-8 end, 00:08Z by date -u)
- Nothing that matters. One dtl_depthclimb run (s9) may still be going and dies with the container.
- Climb outcome (dtl_depthclimb, 7 runs, ~4 h): NO depth ≥ 2, NO k ≥ 3, NO incomplete run.
  - Best: 34 re-steals, all depth 1, on a two-copy union of stealonce_both_n45. Saved as
    experiments/alg/instances/resteal34_union_n90.pg (sha1 e59314d0; pinned Oink 6 iterations verified; stable: 34
    re-steals at depth 1, k = 2; Oink: none).
  - Other climbs: 18 re-steals from stealonce_both_n45 (s8); 10 from stealonce_viol_n76 (s4).
  - s6 (from fall3_n76) died silently, cause unknown (not OOM). The climb now logs exceptions.
- Older successor-6 IN-FLIGHT notes are superseded; see git history.

## NEEDS
- Successor 8 queue:
  - (1) (EXIT_c) or (STEAL-POLY_sum): proof attempt, or the sharpest failure;
  - (2) if L-RED finds depth ≥ 2 or k ≥ 3: re-run with dtl_stealdepth.py and dtl_prefexits.py, both orders, and record it;
  - (3) (CTX⁺) only with a genuinely new idea.
- Owner: none.

## Things only I know
- Successor-7 tools (flags in their docstrings):
  - dtl_stealtrace.py: STEALER-MONO traces.
  - dtl_shrinkdep.py: attraction forest, A/B/C shrink classes, DEP-SAFE.
  - dtl_firedlong2.py: FL_ALL, FL_SHOW; LAMINAR / TOP-INJ / BIRTHTOP / HALL / ≤ |R| checks.
  - dtl_stealdepth.py: analyze() and run_game(); re-steal causes and depth.
  - dtl_depthclimb.py: climbs on depth, then k.
  - dtl_prefexits.py: vertex exits.
  - dtl_ctxpieces.py: depth-0 pieces.
  - dtl_firedclimb.py FC_RATIO=1: ratio-first fitness.
  - dtl_rootmono.py RM_LAM=1, RM_BIRTH=1: default output unchanged.
- dtl_rootmono's pref[(round, top)] is P(τ⁺), the prefix BEFORE the top (Z before tattr). regset is the region.
- Memory: dtl_rootmono with RM_PREF=1 on big unions (NMAX=60) needs about 6 GB per process. Run at most 2 at a time; 4 were
  OOM-killed.
- The tools count exits and steals only at steps present in both visits. Visits with fewer rounds (G9-b2) are not modelled
  as virtual rounds.
- dtl_rootmono.py flags:
  - RM_DV=0 skips DV*;
  - RM_LIGHT=1 skips the ideal and step-deficit checks, so "clean/dirty" labels are meaningless in light mode;
  - RM_EXCL=1 records excluded tangles, fired tangles and tangle counts per region step (PREFIX-MONO-X, X*,
    STEAL-ONCE, FIRED-R, NO-REFIRE);
  - RM_PREF=1 records prefixes and region sets per step (STOLEN-PERM, STEALER-MONO, MET-MONO, prefix shrinks);
  - RM_KSEQ=1 prints first-difference positions; RM_FALLDET=1 prints fall details; RM_WIT prints witnesses;
  - games and unions come from dtl_step5stats.games (UNIONS, SEED, UM_CROSS, NMAX).
- The tool implements the G-Ψ convention (W_{r,t} := Cl_t(U_r) for rounds returning at 716) since e9acfb86. Without
  it, union411 of the cross unions gives a false "Ψ not monotone".
- dtl_fdlcheck.py log entries carry R and Gx at indices 7 and 8. The caller name must be read in the outermost tattr
  override (the old one was vacuous).
- Other tools: dtl_union_dump.py IDX OUT G.pg... writes union IDX as a file. dtl_ctxclimb.py and dtl_firedclimb.py are
  climbs. dtl_meetd.py tests the GAP-C (MEET)/(PHASE-IN) statements.
- Keep blocking waits under 5 min and read notifications between waits. I slipped twice (22 and 19 min).
- Unquoted heredocs eat backticks (this ate "-t -t" once).
- When the Lead names a § letter that is already taken, use the next free letter and say so.
- Stamps: always $(date -u +%H:%MZ) inside the heredoc. The Lead's stamps are date -u now.
- Pinned Oink: tools/oink/build/oink --dtl --no-single --no-wcwc --no-loops -v G.pg OUT.sol, then grep "solution
  verified". Re-run every instance before reporting it.

## Resume point
Successor 8:
- Read GAP-A-M §23o (the position: signed conditionals, the three DATA premises with best data and killed routes, and the best
  guess), then §23p (EXIT-CHARGE), §23k (the packet-9 imports), and docs/alg/STEAL-DEPTH.md.
- Best next target, in my judgement: the STEAL premise via the local statement (EXIT_c). Each vertex leaves each step's
  prefix P(τ⁺) at most c times per phase. Data: c = 2, reached only on the DE20 instances.
  - Question: how can w re-enter P(τ⁺) after an exit? In R35 the re-entry comes from a NEW tangle fired by region 66.
  - Route idea: an exit needs a relevant steal at an earlier step (local PREFIX-MONO-X*), and a re-entry needs prefix growth
    above.
- (CTX⁺) and (FIRED-R): every set-structure route is dead (see §23o). Do not retry CHAIN, CTX-ROOT, CTX-LAMINAR,
  PIECES-LAMINAR, FIRED-STEP, FIRED-LAMINAR, FIRED-TOP-INJ, FIRED-HALL or NO-RETURN.
- RESULTS R12 (packet 9) is being drafted by the Lead.

## Dead ends
- Box 8 successor 7: STEALER-MONO (stealer_viol_n76), FIRED-STEP const and FIRED-TOP-INJ (fired18_stable_n20), FIRED-LAMINAR
  (c6_replay3_n32); all in docs/alg/DEAD.md.
Box 7-8 dead ends, each with its instance, are in docs/alg/DEAD.md (latest sections):
- root-call RMONO = (M) (dtl_mviol_n20);
- CHAIN (dtl_searches15_n24);
- CTX-ROOT (dtl_cnew14_n20);
- F_R ≤ const (fall3_n76, fall4_n116);
- FALL-V (fallv_viol_n28);
- per-tangle steal counting (fallv_viol_n28);
- MET-MONO (§23a; corpus, 117 shrink pairs);
- the raw input bound (vacuous);
- distraction mass as a potential.
Boxes 1-6: see `git show 8a9c0f44:notes/L-ALG.md`.

## Sources opened
- Successor 7: no external sources opened. Readings are of dtl.cpp @ 8fbf0a7 through experiments/alg/dtl_pyref.py (attractVertices
  67-76, attractTangle 78-101, tattr 196-203, best_vertices 220-) and of the fleet's docs.
- No external sources were opened in boxes 7-8. All arguments are readings of dtl.cpp @ 8fbf0a7 (tools/oink/src/src/solvers/dtl.cpp,
  dtl.hpp) and of the fleet's referee reports (docs/referee/R-P4..R-P8.md, docs/referee-2/R2-P4..R2-P8.md).
- Earlier sources: `git show 8a9c0f44:notes/L-ALG.md`.
