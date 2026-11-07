# Handover check: L-RED successor 56 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-07 by date -u, see commit time)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 55, handover =
notes/L-RED.md «Successor 55 HANDOVER» at l-red 68a1f609.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 19 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 68a1f609b25f8cd75688650114e3f596e8ae3dac.
- Trunk claude/vibrant-johnson-nxvvxo = 16d582d2a. `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD`
  -> 33 ahead / 841 behind; merge-base c2d1e88e. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|own.py"`: none); `git worktree list` = main only (wt191/192/190/190b/193
  of successor 55 are gone); tools/oink/build absent (scripts/setup_oink.sh needed before any Oink route).
- R218 (hubs: T1-T4 DEAD), R219 (FLIP-E, GATE-REARM, GATE-POLY «U(G) = O(1) ⇒ polynomial before the first fallback IF Σρ_g and
  ΣH_g are polynomial», «F_g ≤ f(d)» DEAD by LEAP), R220 (P-N5-ASC @ l-new 95dc76d7: all statements SURVIVE, [E-LEV] NEEDED): done.
- Next (box R221 after «go»), in order: (1) adversary vs L-NEW 62's [LOC]-at-gates lemma once the Lead sends its SHA: run own.py
  (experiments/red/r220/own.py, EORD=lev|rev) on LEAP_k64, rd3_d4 and the R217-R219 instances first, then look for a gate where [LOC]
  fails or a premise gap; (2) LADDER: smallest Ξ-cyclic genome whose hub plays climb k upward Ξ-edges, k growing; measure U(G),
  max ascents per play, e-set height, R, N; compare the climb's recursion with Gray-code / Hanoi; result = R superlinear in N
  (two implementations + Oink n5v / n5b on Γ3) or the blocking lemma with its instance; (3) Σρ_g at SET gates: bound or growing family.
- First practical steps: scripts/setup_oink.sh; recreate worktrees in the scratchpad via experiments/red/r218/env.sh (R218_S=<scratch>).

## 3. docs/GAPS.md rows I own (trunk 16d582d2a)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R221 works against G-N5-TIME (major, owner L-NEW, open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Successor 55 once launched climbs with a bare `&` outside a tracked task (killed at once). Check: every long job is a tracked
  background task launched with a full environment; `pgrep -af` before launching anything.
- Successor 53 typed a SHA into a Lead message before reading git's output. Check: SHAs are copied from git output of an earlier step.
- xcheck.py (r218) writes _g3.pg next to its inputs: run it on scratch copies; `git status --short` before every commit, add by path.
