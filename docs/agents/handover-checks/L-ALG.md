# Handover check: L-ALG (successor 5, written 2026-10-16T23:20Z by date -u; LANE-RESTART step 3; produced on Opus 5.5, D8/L27)
Every answer measured from the repository in this container (commands given), not recalled from notes/L-ALG.md.
Predecessor: session_01KESFSwLyyKvwe3mzqN2Bzr (box 16:01Z-~00:00Z; last lane push b9b3b2b, 23:14Z). Previous check overwritten.

## 1. Branch, head, distance to trunk
- Branch `claude/l-alg`. At container start the LOCAL branch was 1017502 (an old handover commit) and claimed to be "up to
  date" only because origin had not been fetched yet. After `git fetch origin`: origin/claude/l-alg = b9b3b2b ("L-ALG box 4
  end: §18m searches-per-phase table ..."), trunk origin/claude/vibrant-johnson-nxvvxo = 26417b3 ("NOW/LEAD-STATE: L-RED box
  end (R21, spp19 at n=30)").
- Before step 0: `git rev-list --left-right --count origin/claude/l-alg...origin/claude/vibrant-johnson-nxvvxo` = 1 ahead
  (b9b3b2b), 27 behind; merge-base 6652cd7.
- Step 0: `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` = 71b2f4a (made on the stale local 1017502, so it lacked
  b9b3b2b); then `git merge --no-ff origin/claude/l-alg` = 723496d (brings b9b3b2b in; no history rewritten). Now HEAD...trunk
  = 3 ahead, 0 behind, merge-base 26417b3; HEAD...origin/claude/l-alg = 29 ahead, 0 behind. This file's commit makes it 4
  ahead of trunk (SHA in the message to the Lead).
- tools/oink/build absent at start; scripts/setup_oink.sh started in the background (needed for Oink-order measurements).

## 2. Open work and the next step of each
- DTL gauntlet step 4 (docs/alg/DTL-proof.md, §0 frozen for every order datum ω, L26). GAP-C open, not routed. GAP-A OPEN,
  route (H1)-(H4) (GAP-A-M §12); ledger §17. Every per-context (H4) potential is dead (§17 KILLED rows; RESULTS DE10, DE11;
  DEAD.md last section). DATA left: (U-MONO_DTL), (LEX-R), no full-state revisit (§18j). PROVED (unrefereed): §18a, §18h,
  Lemma P on C6 (§20).
- Next-box queue (Lead brief, after "go", 8 h box):
  (1) State (SPP) precisely ("searches in one phase of A_DTL ≤ |G'|", or the sharpest form the data supports; "≤ p-parity
      vertices + c" is already broken by spp_final_n20: 19 > 14), with data for both order data, and send it to the Lead at
      once for L-RED. Next step: run dtl_phasestats.py (and L-RED's replay.py convention) on spp_final_n{20,30,40,60},
      spp19_{oink,stable}_n30 and the R17-R21 instances in Oink order and stable order; tabulate searches per phase vs |G'|,
      p-parity count, and number of distinct priorities.
  (2) A PER-PHASE (global) potential that every search of a phase strictly moves, using DTL's learning order (candidate shape:
      "each search but the last permanently settles a vertex of G'"). Next step: per search of the long phases, record what
      is new and permanent (vertices first entering a stored tangle, first entering the final dominion's attractor, the
      top-level piece structure), test each candidate on the corpus before any proof; mark PROVED/SKETCH/GAP.
  (3) Bound the number of phases (or cite where proved, DTL-proof.md) so that (SPP) closes GAP-A, and write what (SPP) plus
      the phase bound gives in the TARGET.md §3 cost model. Next step: read DTL-proof.md for the phase/dominion count.
  Rule: a phase with more searches than |G'|, or any super-polynomial family, goes to the Lead at once.
- T-ALG1: deferred by the Lead, no step. C1-C4 DEAD. IN FLIGHT: none (the predecessor's climbs stopped 23:14Z; best games
  committed as experiments/alg/instances/spp_final_n*.pg).

## 3. docs/GAPS.md rows owned by L-ALG
None. docs/GAPS.md at 26417b3: the open table is empty; the closed table holds only G1 (owner L-STRUCT). GAP-A and GAP-C are
proof gaps inside the lane file docs/alg/DTL-proof.md §5, not GAPS.md rows.

## 4. Three owner rulings that most constrain this lane (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
1. D1 (active; DECISIONS.md line 7):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: DTL stays "wrong" until TARGET.md §5 passes; (SPP) and every lemma in GAP-A-M.md are unrefereed, not results.
2. D5 (active):
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18: M4 is the primary aim; gauntlet unchanged. Constraint: GAP-A is pursued as a proof target; a negative
   outcome must name the mechanism and the instance.
3. D8 (active):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus 5.5 until the Fable reset 2026-10-21 21:00Z; work labelled "produced on Opus 5.5"; referees wait.
   Constraint: every notebook/doc entry of this session carries that label; no referee request.
Also binding (Lead readings, not owner rulings): L22 (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7), L26
(§0 frozen for every ω), L31 (C6 is the model for the core, not a gauntlet candidate).

## 5. One trap that bit this lane, and the check that now prevents it
Trap (bit me at this restart): the container's local claude/l-alg was the old 1017502, and `git status` said "up to date"
before any fetch. Merging trunk alone (71b2f4a) silently left out the predecessor's last push b9b3b2b (§18m, spp_final_*,
final resume point), which trunk does not contain. Check now: after `git fetch origin`, run
`git rev-list --left-right --count HEAD...origin/claude/l-alg` and require "N 0" (0 behind the lane head) before writing
anything; here it read 0 behind only after the second merge 723496d.
Older trap kept: never pipe verify (b93114a, 08:26Z on 2026-10-16); push only as
`scripts/push.sh > $SCRATCH/push.log 2>&1; echo exit $?` and read "VERIFY PASS" and exit 0 in the log before reporting a SHA.
And: every count names its order datum (spp_n20: 18 searches Oink order vs 11 stable).
