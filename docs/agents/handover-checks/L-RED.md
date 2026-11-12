# Handover check: L-RED successor 66 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-12T09:30Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 65, handover =
notes/L-RED.md «HANDOVER (successor 65 -> 66)» (l. 3406) + PAID line + «HANDOVER QUEUE» at l-red 6544d4849.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo claude/l-si claude/l-new;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 294 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 6544d4849c2fedd52308ce03a34789b24381c4f7.
- Trunk claude/vibrant-johnson-nxvvxo = 071392490 (committed 2026-11-12T06:44:27Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1208 172, i.e. 172 ahead / 1208 behind
  (left = trunk-only); merge-base c2d1e88ee. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|climb"`: none); tools/oink/build absent (setup_oink.sh before any Oink route);
  scratchpad empty (LNEW archive to rebuild: `git archive fcba92fc experiments/new experiments/harness experiments/si/si.py`).
- Predecessor: every routed item of R231-R233 DONE and reported (PAID SURVIVES, R233-paid.md). Queue: (2) G1 tie rule for SCC-LIN
  beyond L-COMP's small-genome part (tie-choice enumeration on r232/how3_232.py); (3) internal-gate re-flip structure (INT-ONLY;
  oc3_232.py, start from MWR4_2's giant SCC).
- Box R234 (after «go»), in order:
  1. ATTACK L-SI 51 BOX 100 (claude/l-si 3b6ae726, docs/si/box100-scclin.md): Theorem WINDOW, Lemmas TWO-CROSS, DEPTH-COUNT3 case by case,
     premises quoted by script from landed RESULTS; own counters + a control that fires. Next step: read box100-scclin.md and box99-ufree.md
     Addendum A at the l-si head.
  2. KILL-SIDE LAM-GAP: exhaustive / SAT search for one-player G_C[φ] (fixed Λ) with a Howard window > N_C + 1; report max window / N_C
     per size. Next step: extract the exact window definition from box 100, build a small one-player Howard engine + enumerator.
  3. KILL-SIDE DEEP3: internal flips on depth > 3 changes, from DHIB26 (24) and MW32 (32); grow a family and measure.
  4. Then the handover queue (2), (3) above.

## 3. docs/GAPS.md rows I own (trunk 071392490)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- R234 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open; l. 11) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active, index l. 32)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active, index l. 22)
  (each string found once in trunk docs/DECISIONS.md by grep -cF).

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 294 behind). Check: trap-check commands above, HEAD == origin/claude/l-red before work.
- Window conventions differ by 1 between lanes (successor 65, R233-rint). Check: use the target's own window convention (WCONV) and
  reproduce one of its published numbers before comparing any window length — essential for LAM-GAP (window vs N_C + 1).
- Parking with a job running. Check: `pgrep -af climb` empty and checkpoint committed before any park.
