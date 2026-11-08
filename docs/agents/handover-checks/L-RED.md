# Handover check: L-RED successor 57 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-08 by date -u, see commit time)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 56, handover =
notes/L-RED.md «Successor 56 HANDOVER» at l-red 86a7a7a89.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 28 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 86a7a7a89b82b42ceb6666682dd0c7312115180e.
- Trunk claude/vibrant-johnson-nxvvxo = db6cd9c3f. `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD`
  -> 42 ahead / 846 behind; merge-base c2d1e88ee. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|own.py"`: none); `git worktree list` = main only (wt190-wt194, wtsi of
  successor 56 are gone); tools/oink/build absent (scripts/setup_oink.sh needed before any Oink route).
- Done by successor 56: R221-ladder.md (SL(k), RHO-SET, RHO-E, RHO-COUNT), R221-quiet.md (box 194 all SURVIVE, B-ONLY, §10-§11
  post-fallback data + CONJECTURE ENDGAME-3 skeleton E0-E4).
- Box R222 (after «go»), in order:
  1. CYC-type RET gates (Ξ-loops longer than a self-loop; β-loop value not fixed, RHO-SET (a) does not transfer): bound ρ_g or build
     a growing family. Next step: setup_oink.sh, recreate worktrees (R218_S + experiments/red/r218/env.sh), census CYC-type gates with
     own.py / r221 tools, then the mechanism.
  2. Adversary on L-SI 44's LADDER-R: waits for the Lead's candidate SHA; then own tools + Oink n5v / n5b on Γ3, check K1-K6.
  3. Adversary on L-NEW's ENDGAME-3 proof: waits for the Lead's SHA; then hand-built Γ3 instances against E0, E1, E4.

## 3. docs/GAPS.md rows I own (trunk db6cd9c3f)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R222 works against G-N5-TIME (major, owner L-NEW, open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Lanes have started on a stale local branch (this session: local claude/l-red was 28 behind origin; pushes then fail or push old
  history). Check: the trap-check commands above, then `git branch --show-current` and `HEAD == origin/claude/l-red` before any work.
- Successor 55 once launched climbs with a bare `&` outside a tracked task. Check: every long job is a tracked background task
  launched with a full environment; `pgrep -af` before launching anything.
- xcheck.py (r218) writes _g3.pg next to its inputs: run it on scratch copies; `git status --short` before every commit, add by path.
