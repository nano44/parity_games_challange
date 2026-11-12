# Handover check: L-RED successor 67 (Fable 5.2, xhigh, D1/D18/D21; LANE-RESTART step 3; written 2026-11-12T18:05Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 66, handover =
notes/L-RED.md «HANDOVER (successor 66 -> 67)» (l. 3477) at l-red 5eca1c328.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo; git checkout
  claude/l-red; git merge --ff-only origin/claude/l-red`. The local branch was 308 behind (at 429351d5, successor 49's park);
  fast-forwarded.
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 5eca1c32837b9330e8fd52f1b31d51b0f6d04ca8.
- Trunk claude/vibrant-johnson-nxvvxo = 68c8d2933 (committed 2026-11-12T15:06:33Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1233 186, i.e. 186 ahead / 1233 behind
  (left = trunk-only); merge-base c2d1e88ee. Trunk is not merged in; the truth docs (NOW, DECISIONS-INDEX, GAPS, DECISIONS,
  LANE-RESTART) were read from trunk by `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.
- Clock: `date -u` 18:03:32Z against the Date header of a raw.githubusercontent.com response 18:03:32 GMT: skew 0 s.

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "plc235|dclimb|push.sh|climb"`: none); tools/oink/build absent; scratchpad empty, so
  the four read-only archives must be rebuilt before any run:
  BOX104 = `git archive 26704e01 experiments/si/box104`, LNEW = `git archive fcba92fc experiments/new experiments/si/si.py
  experiments/harness experiments/hard-families experiments/n5-second`, LRED = `git archive 8c01d40e experiments/red/r217`,
  LLIT = `git archive 5c53efbd docs/lit/T66-depth-check.py`.
- Done by the predecessor and reported: R236 (F_n CONFIRMED on own engine n5x236), R237 (1) (WRAP's six counters 0 on 300 random,
  W(G_n, ι), switchallexp, F_n; 14 random rows ±1 = Howard ties in H; control fires).
- Box after «go», in order:
  1. R237 (2): adversarial climb on WRAP's step (W4). Base experiments/red/r236/wr237.py `check(H, s0)`; score = nohoward + nonstd +
     fbwrong, then T; mutate H (owners, priorities, edges) and s0; CTRL=1 must fire. Two seed streams, small H (n ≤ 12) then medium
     (n ≤ 30). Every candidate is re-run on a second engine (n5v xi via the LNEW archive) and against the spec line before a report.
     Next step: rebuild the archives, re-run `wr237.py json` on rand300 to reproduce R237 (1)'s line, then write the climb (resumable
     checkpoint in experiments/red/r237/).
  2. Read WRAP's written proof of (W4) (claude/l-si docs/si/box104-map.md §3, l. 148-164 at a9ea60b96) as an adversary: weakest
     sentence, an instance aimed at it. First candidates seen on the pre-read (not yet tested): the sentence «a pe-free strategy
     gives u a value with a node in H, strictly ◁-smaller» when the H-cycle is even with a large reward (the comparison c_W against
     an even node of H is by reward, top > every Ω of H: to be checked for odd/even cases); (b)'s «pointwise minimum is unique as a
     value» with equal priorities in H (ranks by (priority, index)); self-loops and vertices with one successor in H.
  3. If budget remains: L-SI 52's box 105 (KEY-MODEL) once its first commit lands (not on claude/l-si at a9ea60b96: `git ls-tree -r`
     shows no docs/si/box105* and no experiments/si/box105; the 7 «box105» paths in that tree are L-NEW's older box 105 under
     docs/new and experiments/new): replay key105.py's equivalence on n5x236 in spec mode on random free genomes; report keyfail.
- ON HOLD (Lead): DEEP3 climbs. Their scratchpad checkpoints died with the old container; the bests are frozen in r234/inst.

## 3. docs/GAPS.md rows I own (trunk 68c8d2933)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- This box works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open; l. 11) under D1/D18: WRAP bears on the
  variant N5′-xi only; the row's claim is about N5 and stays OPEN.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5; full string found once in trunk docs/DECISIONS.md by grep -cF; its first sentence once in trunk
  docs/decisions/D001-launch-brief.md)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active, index l. 32;
  string found once in trunk docs/DECISIONS.md)
- D21 «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere
  where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.» (active, index l. 46; relayed text in trunk
  docs/DECISIONS.md l. 452). Lead reading L51 (not the owner's words): maximum effort until 2026-11-14 10:05Z; a «rejected» limit
  still pauses, so on a limit failure I resume from the notebook when woken.

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 308 behind, at successor 49's park). Check: the trap-check commands above; HEAD ==
  origin/claude/l-red before any work.
- Typed stamps and SHAs (successor 66: a verdict header «10:35Z» typed, not measured; a SHA typed before git printed it, 13:50Z).
  Check: every stamp from `date -u` in the same command; every SHA copied from git output in a step after the commit.
- A «counterexample» from my own engine's tie readings (R236: 16 of 300 counts differ from n5v, all tie rule). Check for this box:
  no (W4) candidate is reported before it survives the second engine (n5v xi) and I have quoted the SPEC line my engine implements at
  the state where the run leaves Howard's.
- Parking or committing with a job or a push running. Check: `pgrep -af "bash scripts/push.sh"` before every commit and push; at
  most 2 CPU-heavy jobs including verify; long jobs resumable from a committed checkpoint.
