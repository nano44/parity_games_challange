# L-RED notebook (independent adversary on A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7)
Box 19 (2026-10-22, successor 11, session_01Vq1xXP1gJphfvYS1UxA4td; GO 05:32Z, to ~08:30Z). Produced on Fable 5.1 (L36) to ~07:25Z, then on
Opus 5.5: the session's model was switched (get_session: user_switched_model claude-opus-5-5, configured_model claude-fable-5-1).
The previous notebook (boxes 1-18) is in git at l-red 4f73e7a6: `git show 4f73e7a6:notes/L-RED.md`; boxes 16-18 handover at a5274bd6.
Owns docs/red/, experiments/red/, this file. Messages only the Lead (session id in docs/NOW.md; first line "From L-RED (<date -u>):").
Push only via `scripts/push.sh > file 2>&1; echo $?`.
Status: PARKED after box 21 (2026-10-23 ~03:10Z): N8a (perfect tree, both frozen rules) DEAD by H_k (Lead re-runs 02:40Z / 02:46Z / 02:58Z). Box 19 merged trunk 18812f7; k-pools NEST* line CLOSED (Lead, D15 / L37). Box 20 = S growth on
two-player games: docs/red/R52-sgrowth.md, experiments/red/sgrow/.

## DONE (box 19; docs/red/R51-piecemap.md; tools experiments/red/nest16/piecemap.py, gatescan.py; evidence in experiments/red/nest16/maps/ and scans/)
- Trap found: fixd_stealentry.run renumbers vertices by priority, so tlog.py / partmask.py print SOLVER indices, not file ids.
  piecemap.py maps back. R50's D-vs-nest5 statements stand (D is the top band); its A/B/C letters from partmask should be re-read.
- Per-search piece map of nest6min_n75 in both orders (identical P): the block #9-#12 is D's (16 O-rise {49}→{50}, 17 G-pair on
  D[61], 16 → stable); the 8- and 7-levels re-close at #14/#15 as D pieces at the same positions after the chain re-indexes at #13
  (D to the head, nest5 to the tail). Roles by variants (R51 §2): the gate builds a descending −1 ladder of A pieces (positions
  10-14, ranks 8..4) that pushes D's block to 16-20 inside the 8-window and lengthens S 20 → 25; the two returns shape D's head ladder
  after #13 so that positions 8 and 7 change first at #14/#15; each alone gives NEST* 5.
- k = 4 by hand on nest6min ⊎ oseg (above), k4u_n101 (37a45ff8…, Oink-verified): the plain union already nests E's piece around D's
  pair (16 ⊃ 18) but loses level 8: NEST* 6, S 25, both orders. 84 gates (D sources into 99/97/76, 4 priority slots: slot never
  matters), 50 returns-on-gate, 126 single returns, 8 pairs/mirrors, 17 ladder-source gates, 120 head-ladder gates, 43 head-gate +
  returns (448 in all): all NEST* ≤ 6. No NEST* 7.
- Lengthening found (R51 §3h-§3i): 72→80 gives S 28 (k4L72_n101, f3097a66…), + 81→49 gives S 31 (k4L72r_n101, e84a57b6…), both
  Oink-verified (even iterations = S), both orders identical, NEST* 5: the extra searches come after the old end or between new rises of
  position 1, which close every deeper window.
- Obstruction (R51 §4): all 126 single returns keep S 25 and the identical prefix P[0..13]; after the block there is one free
  index (#14) before 7 closes at #15; a seventh level needs two recurring positions between 9 and 16, i.e. a longer post-block tail,
  which only a gate-type change (not a return) can add; gates from the innermost pieces replace D's block by E's instead of nesting.

## DONE box 21 (R53; produced on Opus 5.5; target N8a = L-NEW's kl.py @ l-new 4fd179c8, run unmodified)
- Super-polynomial pivot families for N8a on the perfect universal tree, BOTH frozen rules (docs/red/R53-n8a-counter.md):
  - H_k = klmin_n13 (13 vertices, 18 edges) + 2k isolated self-loops with new top priorities: dual pivots 4·n^{k+1} under global AND
    switch-all (k = 0..3: 52, 900, 19,652, 521,284; all Oink-zlk-checked). Generator experiments/red/kl/famgen.py H k.
  - F_k (klcount_n16, switch-all 4·n^{3+k}+3) and G_k (klglobal_n16, global 8·n^{1+k}+6, switch-all 5·n^{1+k}+1).
- Mechanism: an open lapping cycle (the rule never closes it; the forced-increase least fixed point ratchets) raises one label component
  by one per period; Tighten's base-n successor carries through every counted tree level; each extra priority value adds a level.
- Tools: kclimb.py (graded pivot climb, kl.py imported unmodified), ktrace.py (trace from kl.py's own functions, asserts kl.solve's count),
  kshrink.py (greedy gadget shrink), famgen.py.

## DONE box 20 (R52; produced on Opus 5.5)
- Structured families: tc S ≤ 3, tc+ S = N+1 ≈ log n, Oink counters S ≤ 3, lagfam S = D+7 ≈ n/7.
- Climbs (oclimb.py, Oink proxy F = max(even, odd) − dominions; neutral padding to grow n): best S per n = 21/29/34/36/35 (oink order),
  20/29/30/34/33 (stable) at n = 20/30/40/60/80; log-log slope 0.36 / 0.34. All Oink-verified, Oink count = S. No super-polynomial or
  super-linear signal. s21_oink_n20 (da164511…): S 21 > |G'| 20 in oink order (R24's (SPP) DATA bound broken by 1; stable 11).

## IN FLIGHT
None. No process runs at box end.

## NEXT (for the Lead to route; items 1-2 belong to the CLOSED k-pools line and stay only as history)
1. Lengthening without shallow rises: start from k4L72r_n101 (S 31) and look for edges that stop the mixed piece at position 1
   (ABCDE[14,37,40,47,60,62,86,88,…]) from absorbing vertices between the block and the closes; score = NEST* of P restricted to
   the stretch after the block, plus S.
2. A different fourth part: E = nest5_n49 (a part with its own 5-level structure) above nest6min, then the recipe; n 124, ~40 s/eval.
3. Re-read R50 §4 / §7 cross-part attributions with piecemap.py (file ids).
## Resume point
PARKED after box 21 (2026-10-23 ~03:10Z, date -u). Nothing in flight; no process runs. Wake only on a new named target from the Lead.
Box 21 state: R53 §1-§6 final (freeze §1-§6; corrections in new sections). Open follow-ups only if routed: (a) tree-SI on the succinct
(JL17) tree or with single-switch rules is a NEW candidate (needs its own code from L-NEW; then re-run H_k / climb); (b) a proof of
the H_k law for all k (period read off traces). Earlier resume points: box 20 text below in git (`git show 595ca267:notes/L-RED.md`),
`git show a5274bd6:notes/L-RED.md`, `git show 4f73e7a6:notes/L-RED.md`.
Climb lessons (box 20, oclimb.py; box 21, kclimb.py): fitness from the solver's own counter, confirm with the reference tool; pad
NEUTRALLY (S growth) or with NEW TOP PRIORITIES (tree-level growth); budget by wall clock; pause a climb with kill -STOP / -CONT for
short checks; count jobs with `ps -eo args | grep -c '^python3 .*<tool>'`; never pkill -f a pattern from your own command line.

## Sources opened
- arXiv 2108.13338 (Z. K. Koh, G. Loho, "Beyond value iteration for parity games: strategy iteration with universal trees", LMCS 21(2)
  2025, 24:1-24:35), PDF sha256 21ee0e4336252f7e6e1fcba7cb305b03f0950799610f324235eed5ecba15c9a9, opened 2026-10-23 (box 21): §2.1
  perfect (ℓ, h)-universal tree and p-truncation, §2.2 feasibility / violated / tight / Tighten / lift, Proposition 2.5, Algorithm 1 and
  Theorem 3.1 (iterations ≤ n·|L(T)|; pivot rules left open, intro p. 3).
None new in boxes 16-18. The work cites only fleet-internal signed results (RESULTS R5, R8, R9, R11; P-C1P items; R16 draft) and
dtl.cpp @ 8fbf0a7. Earlier opened sources are listed in `git show 4f73e7a6:notes/L-RED.md`.

## Dead ends (box 19; each with the exact obstruction and the instance that killed it; earlier ones: `git show a5274bd6:notes/L-RED.md`)
- Gate from the innermost-window pieces (D's 49, 50, 51, 52, 58, 59, 68) into the fourth part: E's block replaces D's (masking), NEST* 5
  at best; k4g50_n101 (62cbc3e8…), scans/scan1_gate_oink.txt. Priority slot of the gate target never matters (4 slots, same P).
- Gate into a copy vertex with an even self-loop (97, 76): phase collapse S 7-10; scan1.
- Return edges on the plain union: only re-index the tail after #13; S 25 and prefix P[0..13] identical in all 126; never a new
  recurring position; scans/scan3_returns_on_union_oink.txt. Pairs and triples the same (scan4).
- Literal mirror of the k = 3 step onto nest6min ⊎ oseg: NEST* 4 (scan4; agrees with R50 §5 on nest6 ⊎ oseg).
- Head-ladder gates (72→80 etc., + returns): lengthen S to 28 / 31 but NEST* 5; added searches are cut by new rises of position 1
  (k4L72r_n101, three 1-rises at P indices 13, 19, 21); scans/scan6_*, scan7_*.
- (SPP) "S ≤ |G'|" (longest phase at most the unsolved game at its start; R24's target, DATA only, never signed) is FALSE in oink
  order: s21_oink_n20 (experiments/red/sgrow/instances/, sha1 da164511784449b906663c190757fd78c057f97c), an Even phase of S 21 at
  |G'| 20 (pinned Oink even 21, odd 1, verified; Lead re-ran 10:24Z, CONFIRMED). Stable order on the same game: S 11. Excess +1, linear.
- Rule-free transfer of the N8a lapping counter ("whatever the pivot rule picks among improving arcs"): FALSE on H_k. Single-switch
  rules (lowest / highest index, random seeds 1, 2) solve H_0..H_2 in 9 / 5 / 5 / 17 iterations for every k (ksubset.py; R53 §6b item 4).
  The counter needs simultaneous switching (class SA). Any-universal-tree transfer: READING, gap G1 = local second-child offsets below
  the counted level (unary vertices of succinct trees), untested.
- k-pools NEST* line (boxes 16-19) CLOSED by the Lead (D15 / L37, 07:34Z): NEST* plateaus at 6 (448 hand-built configurations and
  climbs), S linear (≤ 31 at n 101). Obstruction R51 §4: a seventh level needs a longer post-block stretch with no shallow first
  change; no edge class gives both. Killing instance k4u_n101 (37a45ff8a932bcc6e4a79d4848a0a57dbb82367a), scans 1-7.
- Plain union nest6min ⊎ oseg above: E's piece nests around D's pair (16 ⊃ 18) but level 8 is lost: NEST* 6, not 7 (k4u_n101).

## NEEDS
- Lead: route NEXT 1-3 or close the k-pools line; referee routing of R51 only if a claim needs signing (it is DATA plus readings).

## Things only I know
- Box 21 (N8a): kl.py is fast (~0.4 ms per pivot at n ≤ 20; 0.05-0.2 s per solve on the hard bench), so climbs run ~500 steps/s at n 10.
  The first climb hit at n 16 found the 4·n^3 counter within 2 minutes; the law was found by PADDING with isolated new-top-priority
  self-loops (adds a tree level) vs same-priority pads (adds only base). Run L-NEW's files from a read-only `git archive` extract in
  scratch with a `tools` symlink to the repo's tools/ (check_sol2.py looks for ../../tools/oink/build/oink and ../out/).
- Box 20: oclimb.py with Oink fitness is ~8 ms/step at n 20 but 0.2-1.5 s at n 40-80 on long-phase games; use --secs. Random padding
  kills long phases (early dominions); pad neutrally (priority 0, one successor into the game). Pause a climb with kill -STOP / -CONT
  to run a short measurement without a third job. smeasure.py at n 80 takes ~4 min per game (Python DTL).
- SOLVER INDICES: fixd_stealentry.run renumbers vertices by priority (stable: sorted by (prio, v); oink: stdsort.oink_order). Chains,
  tangles and escapes from the harness are in those indices. piecemap.py and gatescan.py map back (idx[i]); tlog.py, partmask.py,
  learnpos.py do not. Part labels by vertex range are only safe after mapping (or for a part that is a priority band).
- Box 19 tools (experiments/red/nest16/): piecemap.py G.pg cut... (per-search map, file ids; ~8 s at n 75, ~15 s at n 101);
  gatescan.py BASE.pg E.pg OUTDIR CONFIGS.txt cut... (config lines 'move:v:prio;edge:u:v'; E placed above; ~25 s per config at n 101,
  oink order). Scans and configs are committed in experiments/red/nest16/scans/, maps in maps/.
- The shared shell's working directory races between parallel tool calls: use absolute paths everywhere; never `cd` and rely on it.
- `pgrep -f` and `ps | grep` count the calling shell's own command line when it contains the pattern: count with
  `ps -eo args | grep -c '^python3 .*gatescan.py'`. The 2-job limit was briefly exceeded once this box (3 jobs, no restart).
- date -u said 05:53Z when I had estimated 06:12Z: always stamp with date -u, never estimate.
- Tool entry points (all in experiments/red/nest16/; L-ALG modules through ../xctx/xscore.py, unmodified):
  - starclimb.py: graded climb. `[FIT=seg|wrap|pool] DTL_ORDER=.. GROW=.. NMAX=.. starclimb.py climb 1 START.pg STEPS SEED OUT`,
    or `starclimb.py G.pg` to score. FIT=pool runs DTL twice per evaluation (slow at n ≈ 100).
  - crossclimb.py: cross-part-only climb. `CUTS=49,75 DTL_ORDER=oink crossclimb.py START.pg STEPS SEED OUT`. About 10 s/step at n 75-90.
  - kcheck.sh G.pg: sha1 + P in both orders + pinned Oink -v (needs tools/oink/build/oink; run scripts/setup_oink.sh first in a
    fresh container).
  - table.py G.pg: n, S, |P|, I, NEST*, pools, and G-NEXT / G-ADJ violations with transition indices, both orders.
  - pairunion.py B.pg OUT A.pg ...: B ⊎ A in placements above / below / inter. mergesearch.py: random interleavings.
  - witness.py P...: NEST* witness chain. learnpos.py: learning positions per search. partmask.py G.pg cut...: part labels per
    transition. gdiff.py / shrinkdiff.py / subsets.py: what a climb changed, and its minimal subset. lawscan.py, gnext1p.py,
    segstat.py, segscan.py: law scans over the library.
- Container limit: at most 2 Python jobs at n ≈ 75-100. With 3, the container was killed (exit 137). There were two restarts this
  session (~01:2xZ and ~04:0xZ on 2026-10-22); climbs were resumed from saved bests, so step counts are lower bounds. Scratch
  (/tmp/claude-0/.../scratchpad) survived both restarts, but do not rely on it in a new session.
- Committed vs scratch: every instance in the table is committed in experiments/red/nest16/instances/. All climb logs (c*, k3*,
  k4*, x*, y*), union seeds k3_*.pg / k4_*.pg / k4s_* / k4m_*, and the library-scan logs were scratch only and are NOT in the
  repo. Their numbers are quoted in R49 / R50.
- Pipes buffer output: a monitored `... | sort | head` shows nothing until it ends, and a timeout kills it with nothing printed
  (this lost the 94-union scan). Write results to files.
- date -u in the container can lag behind work done; always run date -u right before writing a timestamp.
- Frozen text: R46 §1-§3 (pin 01d63d7), R47 §1-§5 (pin da63c40), R49 §1-§8, R50 §1-§7. Add new sections only.
