# Handover check: L-LOWER successor 6 (2026-11-07 13:42Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); local branch was 16 commits behind origin at start and was fast-forwarded
  (`merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false after `fetch --unshallow`).
- Head 4d1c4e4bc8425891b52c7d7882d0f3008425cdd2 = origin/claude/l-lower = `git ls-remote` («L-LOWER 5: handover updated
  (P-TOWER-FUEL frozen at 7f7ff6f5)»).
- Trunk `claude/vibrant-johnson-nxvvxo` at 9315f36c0b005bcb2a41946cb844d02ba3797724 (ls-remote = local origin ref); merge-base f55b98e3.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 19 ahead, 376 behind. No trunk merge (not needed).

## 2. Open work and the next step of each
- DUTY P-TOWER-FUEL (frozen at 7f7ff6f5; line docs/lower/P-TOWER-FUEL-line-L1.txt sha1 408470ad…; check
  experiments/lower/l5/p_tower_check.py): at the referees (REFEREE 26 now, REFEREE-2's successor later). No item received yet
  (`ls docs/lower/ | grep fix` shows only P-M2D-DEAD-fixes.md). Next: when the Lead relays items, write
  docs/lower/P-TOWER-FUEL-fixes.md entry k + line L-(k+1) by script, copying exact strings from the reports; never edit the frozen packet.
- BOX L6 (after «go»): constructive test of CONJECTURE L5-TYPE. Build an explicit fuel supplier (TOP-ADD levels, β ranks > 87, changes
  clocked to level 5's (9,1) windows) so that pair 6 flips in the 48 failing windows of rec/SL41_d28.txt (sha1 c1b46c31…, F(6) 222).
  Next step: from domin.py / fuel6.py / retchain.py output, write the exact spec (which rank on 22's / 11's chain must change, in which
  windows: DOMINANCE-FREEZE + CROSS-ECONOMY, packet §3), then hand-build the supplier levels and evaluate with two simulators
  (fev / utmpl GENOME=) plus xcheck vs L-NEW box150 Gen. No brute climbing (L-COMP 11 lanes D_d28 / D_d28b own that).
- No detached runs of mine (`pgrep -af "rclimb|mclimb|fev|push.sh"` empty).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (major, owner L-NEW, open; GAPS.md line 11).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
   where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
   open problems.» Constraint: every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD; BOX L6 names and tests a D18 analogy.
2. D1 (active, index line 5; DECISIONS.md l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
   such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a seven-level tower is a lower-bound
   CANDIDATE datum only, not a proof that every level doubles.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: the designed supplier is an own design and goes through the same replay/xcheck path.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: committing while push.sh was still verifying (successor 5, 12:0xZ: 5bc47311 committed during the verify of a92b5226; the wait loop
tested «output file non-empty»). Check: before any commit, `pgrep -f "bash scripts/push.sh"` must be empty AND the tracked task's output
must contain the «exit» line. Also run first this session: the stale-branch check (`fetch --unshallow`, `checkout`, `merge --ff-only`,
then HEAD = origin/claude/l-lower = ls-remote, all 4d1c4e4b here).
