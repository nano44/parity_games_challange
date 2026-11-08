# Handover check: L-RED successor 61 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-08 15:3xZ by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 60, handover =
notes/L-RED.md «Successor 60 HANDOVER» at l-red 94823af62.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 61 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 94823af62a16b3f7b4154ec8f6c2164ce333e31c.
- Trunk claude/vibrant-johnson-nxvvxo = 59dacf223 (committed 2026-11-08T14:06:41Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 75 ahead / 984 behind; merge-base c2d1e88ee.
  Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|own.py|climb|asc"`: none); `git worktree list` = main only;
  tools/oink/build absent (scripts/setup_oink.sh needed before any Oink route).
- Done by successor 60 (pushed): R226-race.md (depth-2 race ADDS, DATA; «events ≤ |E_U| − 1» DEAD; Lemma SHARP PROVED (lane);
  CONJECTURE NEST-POLY), R226-core197.md §0-§10 (BOX 197 lemmas + ALT-EQUIV SURVIVE; DS-TOPS s ≤ 7 DEAD, DSALT9 A 9 at N 416;
  climbs A ≈ 0.9·log2(N + M); tower High under GROW7's race gives A 4-5, not ~2K; READING: race needs a HELD High).
- Box R227 (after «go»):
  1. ADVERSARY on routed candidates (L-NEW 65 BOX 198 lemma, L-SI 46 BOX 89 build, L-LOWER 11 OSC-ROOM). Each waits for its SHA from
     the Lead; next step = read that SHA's files, re-run on frozen / own instances, attack what is new.
  2. OWN ITEM: HOLD GADGET between a designed tower (HP_mup / HP-b) and GROW7's replaying low race, holding each tower value ≥ 2 steps;
     aim A ~ 2K. Next step: read GROW7 / CX4 (R226-core197 §10, inst/), find how CX4's x17 is held 2 steps (R226-race §1: x17 is a
     2-digit counter held 2 steps) and copy that hold onto each tower level; measure A, T3, N + M at 2-3 heights on own.py and on
     L-NEW asc197 (f98e93ee, detached scratchpad worktree); freeze; decide linear-in-K vs obstruction; then the nested version.
- Open from successor 60: CONJECTURE NEST-POLY; CONJECTURE ALT-POLY (L-NEW; = G-N5-TIME on Γ3); hold gadget unbuilt.

## 3. docs/GAPS.md rows I own (trunk 59dacf223)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R227 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 61 behind; successor 60: 49). Check: trap-check commands above, `git branch
  --show-current` and HEAD == origin/claude/l-red before any work.
- A long job launched with a bare `&` (successor 58) escaped tracking. Check: every long job is a tracked background task (never `&`),
  then `ps -eo pid,args | grep <tool>` after each launch.
