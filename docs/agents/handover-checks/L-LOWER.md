# Handover check: L-LOWER successor 7 (2026-11-07 18:20Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); local branch was 28 commits behind origin at start and was fast-forwarded
  (`merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head 96e63eb4ca5eefa5242ab9f0c48e0fd398d300b7 = origin/claude/l-lower = `git ls-remote` («L-LOWER 6 PARKED: handover (BOX L6
  result, RC-PLATEAU role form, guard_l6 interface, C134 duty pending)»).
- Trunk `claude/vibrant-johnson-nxvvxo` at 5f8b399eceb3e777583fe4473e506b55b961a0ef (ls-remote = local origin ref); merge-base 2a89b7f2.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 4 ahead, 456 behind. No trunk merge (not needed).

## 2. Open work and the next step of each
- DUTY P-TOWER-FUEL (packet frozen, sha1 a093e0e7…; fixes file 0902efb9… = entry 1; L-1 408470ad…; L-2 d866ca50…, 4,586 B by
  `wc -c`; check experiments/lower/l5/p_tower_check.py). Both referees MATCH L-2; now at CHECKER C134 (Lead draft R120;
  `ls docs/checker | grep C134` empty on this branch). Next: when the Lead relays C134 §5's L-3, write fixes entry 2 +
  docs/lower/P-TOWER-FUEL-line-L3.txt by script in the style of experiments/lower/l5/mkL2_tf.py / mkfix_tf.py (each old string once
  in L-2, each new once in L-3), extend p_tower_check.py to pin L-3 and any new count; never edit the packet, L-1 or L-2.
- RC-PLATEAU test (CONJECTURE, j = 6 role form, docs/lower/L6-supplier.md §5d): read L-COMP 11's lanes D_l6 / D_l6z / D_l6g and
  frozen genomes L6_TEST1, L6Z_TEST1, L6_BEST on claude/l-comp experiments/comp/box30/out/ (not yet present at fetch: listing shows
  only A_d28 … D_d32_fsix). Next: re-run guard_l6.py 'noreturn' + sim6.py on each frozen genome; any one with F(6) > 222 kills it.
- BOX L7 (after «go»): seventh capped level with no Ξ-path q₅ → pair 6 by construction; fuel pair 6 via TOP-CLOCK, TAP,
  TRANSPARENT-LEVEL, RANK-LOCKED, DOMINANCE-FREEZE, CROSS-ECONOMY. Next: design the top pairs on paper from L6 §5b-§7, build, score
  with sim6.py + fev, xcheck vs L-NEW box150 Gen. Success F(6) = 254 with six capped below; else the exact obstruction + instance.
- No detached runs of mine (`pgrep -af "push.sh|fev|mclimb|gad"` empty).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (major, owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
   where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
   open problems.» Constraint: every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD with counters (unit, set, scope).
2. D1 (active, index line 5; DECISIONS.md l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
   such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a seven-capped tower is a
   lower-bound CANDIDATE datum only; no asymptotic claim from it.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: box L7's construction is an own design and goes through the same two-simulator +
   xcheck path as any other genome.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: committing while push.sh was still verifying (successor 5: 5bc47311 committed during the verify of a92b5226; the wait loop tested
«output file non-empty»). Check: before any commit, `pgrep -f "bash scripts/push.sh"` must be empty AND the tracked task's output must
contain the «exit» line. Also run first this session: the stale-branch check (`fetch --unshallow`, `checkout`, `merge --ff-only`),
then HEAD = origin/claude/l-lower = ls-remote (all 96e63eb4 here).
