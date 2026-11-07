# Handover check: L-RED successor 55 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-07 18:2xZ by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 54, handover =
notes/L-RED.md «Successor 54 PARK» at l-red f77a0eef.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 9 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both f77a0eeff3e539bcfeefa39943164508a5d59204.
- Trunk claude/vibrant-johnson-nxvvxo = 5f8b399ec. `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD`
  -> 23 ahead / 814 behind; merge-base c2d1e88e. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -f "push.sh|r217|rclimb"`: none); /home/user/r217live absent; tools/oink/build absent;
  no worktrees (`git worktree list` = main only).
- R217 vs CANDIDATE N5′-xi (docs/red/R217-ovt.md §1-§12): LEAP(k) (one gate 2k flips, R linear); lemmas E-DOM-ALL-d, E-DOM-CHOICE,
  TOP-DEC, OVT-DV, LEAK-ARCH, CHAIN-SHIELD, HIDE-BUSY; RS2 works, RS3 per-bit lanes DEAD (110 skipped). Open crux: lane re-arming
  without H1-H2.
- Next step (box R218 after «go»): (1) test (1), NOT RUN by successor 54: a hub that tracks only the HIGHEST set bit, starting from
  RS2 (experiments/red/r217/rs2.py), measure re-arming frequency; (2) a two-level hub design (hub per block of bits, recursive /
  Fenwick-style carries). Verify 4 ways (own impl, box191 idealcyc, subrun191 labels, Γ3 n5v = n5bxi + Oink); freeze instances.
- First practical steps: scripts/setup_oink.sh; recreate worktrees (wt191 f09f67ec, wt192 a2db977d) in scratch via r217/env.sh.

## 3. docs/GAPS.md rows I own (trunk 5f8b399ec)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R217/R218 work against G-N5-TIME (major, owner L-NEW, open) under D1/D18.

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
- Successor 54: xcheck.py writes <genome>_g3.pg next to its inputs (and edomclimb once wrote /nonexistent.json). Check: run xcheck
  on scratch copies, never on inst/; `git status --short` before every commit, add by explicit path only.
