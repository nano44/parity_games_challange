# Handover check: L-RED successor 60 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-08 10:5xZ by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 59, handover =
notes/L-RED.md «Successor 59 HANDOVER» at l-red 029e5d8b9.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 49 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 029e5d8b92ebc712a6599289678bbe6f079cf0cf.
- Trunk claude/vibrant-johnson-nxvvxo = 97f6ec5c7 (committed 2026-11-08T09:59:26Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 63 ahead / 903 behind; merge-base c2d1e88ee.
  Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|own.py|climb|comp225"`: none); `git worktree list` = main only;
  tools/oink/build absent (scripts/setup_oink.sh needed before any Oink route).
- Done by successor 59 (all pushed): R225-core.md (Lemma EQUIV, Lemma BIN, HIT7, CONJECTURE ADD(c), CX4_n21), R225-lag.md
  (L-SI box 86 SURVIVE, W-1 LEAPFROG), R225-leap.md (L-SI box 87 LEAPFROG-ASC SURVIVE; events ≤ |E_U| − 1 on data).
- Box R226 (after «go»), in order:
  1. ADVERSARY on routed candidates: L-SI 46's nesting family (box 88), L-NEW 65's BOX 197 lemma, L-LOWER 10's level-8 genome/rule.
     Each waits for its SHA from the Lead; next step = read that SHA's files, re-run on frozen/own instances, attack what is new.
  2. OWN ITEM: DEPTH-2 RACE. Next step: read inst/CX4_n21.json with show225.py, hand-add a second router on the High chain and a
     feedback edge into x17, measure X, D, T vs size exactly (comp225 / show225); decide MULTIPLY (×4 per level) vs ADD; state the
     unified CONJECTURE exactly if ADD. Plus: «events ≤ |E_U| − 1» as a lemma (prove or freeze a counterexample).
- Open from successor 59: CONJECTURE ADD(c) (c ≥ 4); READING «type-II decisions under shared heads» (R225-leap §3); QUIET (P-QUIET
  conditional); PARITY-8 shadow bill for level 8.

## 3. docs/GAPS.md rows I own (trunk 97f6ec5c7)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R226 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 49 behind; successor 59: 43). Check: trap-check commands above, `git branch
  --show-current` and HEAD == origin/claude/l-red before any work.
- A long job launched with a bare `&` (successor 58) escaped tracking. Check: every long job is a tracked background task (never `&`),
  then `ps -eo pid,args | grep <tool>` after each launch.
