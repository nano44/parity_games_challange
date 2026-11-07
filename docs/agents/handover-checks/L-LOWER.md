# Handover check: L-LOWER successor 8 (2026-11-07 20:55Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); local branch was 35 commits behind origin at start and was fast-forwarded
  (`merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head c1e16b59f56787604aa87bafa5f767341b434154 = origin/claude/l-lower («L-LOWER 7: L7 §2 lemma-check counts with L6G_TEST1»).
- Trunk `claude/vibrant-johnson-nxvvxo` at 80c1f1ea3febf5eb6c3d776bc81edb9d8e958676; merge-base 8cc6ebc6.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 4 ahead, 469 behind. No trunk merge (not needed).

## 2. Open work and the next step of each
- Referee byte tests of P-TOWER-FUEL L-3 (7328e673…): DONE per the Lead (REFEREE 27 af752251, REFEREE-2 31 e72661d0, both MATCH);
  the notebook's «pending» is stale. R120 (second fill be8dac23 on trunk) waits only on CHECKER C134 Add. 1; no C134 duty for me unless routed.
- RC-PLATEAU (j = 6 form, L6 §5d): Lead relays L-COMP 11 KILL230 (sha1 29faf25f…, F(6) 230) and KILL238 (sha1 54450906…, F(6) 238),
  caps 6, npaths(q5, pair 6) 0. `git ls-tree -r origin/claude/l-comp | grep KILL2` is EMPTY at this check (fetched now): files not
  on origin yet. Next (after «go»): fetch, sha1-check, freeze copies in experiments/lower/l8/rec/, confirm guard_l6 «noreturn»
  (bca48384) matches L6 §5d, re-run sim6 + fev; if confirmed, RC-PLATEAU DEAD by its stated test.
- BOX L8 item 0: dissect KILL238/230 against SL41 and L6G_TEST1 (6-window profile, MERGE 11:1 → 9:1 (87) → 54 → 22 present or not,
  which failing windows the 10:0 → 17 re-point repairs, what blocks 254; revert each changed part, forced/unforced split).
- Items 1-2: helper pairs in experiments/lower/l7/sched.py (key-fired moves parallel to the lower move, as KILL_M2D_d6); decide h = 2
  exactly at d = 3, then 4, with ranksolve (exh2.py style); then h = 3, helper rule, h = 4 xcheck vs L-NEW box150 Gen; S(h) vs polynomial.
- Item 3: ONE-READ XOR case split (L7 §8; max element over Q_i, Z_i, (b, j), R_j) — close or counterexample wiring.
- Item 4: CANDIDATE G_h with proof sketch, or exact obstruction. Do NOT duplicate L-COMP 11's brute tower climbs.
- No detached runs of mine (`pgrep -f "bash scripts/push.sh"` empty before this push).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (major, owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
   where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
   open problems.» Constraint: every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD with counters (unit, set, scope).
2. D1 (active, index line 5; DECISIONS.md l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
   such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a capped tower or helper schedule
   is a lower-bound CANDIDATE datum only; no asymptotic claim from finite data.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: the helper-schedule family G_h is an own design and goes through the same
   two-simulator + xcheck path as any other genome.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: sessions started with a stale local branch (this one: 35 behind) or shallow clone; a push then fails or pushes old history.
  Check: `git fetch --unshallow`, `checkout claude/l-lower`, `merge --ff-only origin/claude/l-lower`, then assert
  `git branch --show-current` = claude/l-lower and HEAD = origin/claude/l-lower (done above, both true).
- Second (successor 7): a background python started with `&` dies on container restart and escapes tracking. Check: only tracked
  run_in_background tasks; push.sh output redirected to a file, exit code echoed, never piped; `pgrep -f "bash scripts/push.sh"` first.
