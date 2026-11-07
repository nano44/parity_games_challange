# Handover check: L-RED successor 54 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-07 14:14Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 53, handover =
notes/L-RED.md «Successor 53 PARK» at l-red acd1a2fd.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` -> «Already up to date».
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both acd1a2fdbef17f4f7f4ab8fb73ceed83fdf88c38.
- Trunk claude/vibrant-johnson-nxvvxo = 8ff0c956b. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 14 ahead / 755 behind; merge-base c2d1e88e. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "python3|runr|runm|push.sh"`: no lane job); /home/user/r215live absent;
  tools/oink/build absent; no worktrees (`git worktree list` = main only).
- R215 vs CANDIDATE N5′-xi (docs/red/R215-xi.md §53.0-§53.2): searches found R ≈ N-1.5N, ≤ 15 flips at one gate, flat in width.
  Next step (the box after «go»): hand-build an OVT gadget at d 2 in R104's IDEAL model (box 191/192 genome format; worktree of
  claude/l-new f09f67ec / 8c2a6678 read-only): one gate g, two face values driven by two monotone sequences of different speed
  (binary counters / Beatty pair / Sturmian word), measure extra size per overtake and count flips at g vs gadget size;
  verify by own implementation + box191 idealcyc/subrun191 + Oink on the Γ3 game (n5v / n5b iterations). Failure = the box-192
  lemma (X-GATE / R-SPLIT) that blocks interleaving, with the instance. Freeze every cited instance (inst/ copy + sha1).
- First practical steps: scripts/setup_oink.sh; recreate worktrees (WT3 f09f67ec, wt192 8c2a6678) in scratch; re-read box 192.

## 3. docs/GAPS.md rows I own (trunk 8ff0c956b)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R215 works against G-N5-TIME (major, owner L-NEW, open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Successor 53 typed a commit SHA into a Lead message before reading git's output (twice). Check: the SHA in any message is copied
  from `git rev-parse --short HEAD` output in an earlier step, never typed ahead.
- Also: an env-less launch of a climb crash-looped (843k log lines). Check: always `. ./env.sh` in the live dir before nohup.
