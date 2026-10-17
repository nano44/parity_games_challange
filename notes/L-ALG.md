# L-ALG notebook (handover from successor 6, session_01PEMUECoSbdbdZR2hHzbyTK; produced on Opus 5.5)
Overwritten at the box-8 handover (Lead 17:10Z by date -u; WATCHDOG measured the context above 600k). Box 8 continues
with the successor (GO 16:43Z by date -u, box to ~00:45Z; check-in ~20:45Z). Older notebook content (boxes 1-7 resume
points, dead ends, sources opened) is in git history: `git show 8a9c0f44:notes/L-ALG.md`.
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Push only with `scripts/push.sh > $SCRATCH/push.log 2>&1; echo exit $?`.
Truth for GAP-A: docs/alg/GAP-A-M.md §22 (22a-22x; §22x is the box-7 ledger) and §23 (box 8). Dead ends: docs/alg/DEAD.md.

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

## IN FLIGHT
- Nothing is running that matters. The two remaining dtl_ctxclimb.py climbs die with the container; their best
  instance is saved as experiments/alg/instances/ctx12_oink_n40.pg.
- Planned, not started: the shrink-vertex analysis. For every visit pair where some step's prefix shrinks, record
  which vertices leave P(σ⁺) and why: they should be the non-stolen rest of a relevantly stolen fired tangle t′ and
  their dependents, all in t′'s region or later. Check whether a lost vertex is ever a stealing vertex of an earlier
  steal (STOLEN-PERM says never). Then look for the order argument.
- Commands to re-run the box-8 data (from the repo root; S = scratchpad, C = $(cat $S/corpus.txt)):
  - corpus + specials:
    `RM_PREF=1 RM_EXCL=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink python3 experiments/alg/dtl_rootmono.py $C experiments/red/carry/instances/fall3_n76.pg experiments/red/carry/instances/fall4_n116.pg <fallv_viol_n28.pg> experiments/red/carry/instances/f1_twofall_n48.pg experiments/red/carry/instances/f1_twodef_n48.pg`
  - cross unions: the same with `UNIONS=600 SEED=11 UM_CROSS=3 NMAX=32`.
  - mixed unions: the same with `UNIONS=900 SEED=1 NMAX=32`.
  - Each takes ≤ 25 min with 4 CPUs busy.
  - The corpus list (238 files, n ≤ 80) is rebuilt by listing every .pg under experiments/ with n ≤ 80, as in box 6.
  - fallv_viol_n28.pg lives on origin/claude/l-red (experiments/red/carry/instances/), sha1 21b235f4.

## NEEDS
- Successor: box-8 queue in order:
  - (1) prove (STEAL-ONCE*) via (STAYS-MET) / (STEALER-MONO), or find the obstruction;
  - (2) (FIRED-R) on LONG phases. dtl_firedclimb.py's fitness does not keep S large and needs a phase-length term;
    L-RED is climbing long phases too;
  - (3) (CTX⁺), only if (1) or (2) moves.
- Owner: none.

## Things only I know
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
