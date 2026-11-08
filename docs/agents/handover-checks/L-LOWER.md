# Handover check: L-LOWER successor 9 (2026-11-08 01:4xZ, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); local branch was 48 commits behind origin at start and was fast-forwarded
  (`merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head 09e6c8d24bd498577dd4c657d5b35e75449e539d = origin/claude/l-lower («L-LOWER 8 PARKED: handover; L8 §1g HIT7 dissected ...»).
- Trunk `claude/vibrant-johnson-nxvvxo` at db6cd9c3f9fa05dae9931b1949e12d15044f2f39; merge-base 8cc6ebc6.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 17 ahead, 481 behind. No trunk merge (not needed).

## 2. Open work and the next step of each
- BOX L9 item 1 (main): build level 8 by hand at d 32 from docs/lower/L8-design.md §4 (j = 6): τ level 9 (movers 18/19) on q6's chain,
  key-fired by o(8) at u1 + 1; σ selector level 12 (24/25); ρ key-fired helper level 10 (20/21). Next step: lift HIT7 (L-COMP 709e57a0,
  experiments/comp/box30/out/L6_HIT7_F254_d28.txt, sha1 6a3b274d…; freeze a copy in experiments/lower/l9/rec/ with sha1 check) to d 32,
  set the target with PULSE_6 = 2 in all 127 6-windows, decide with ranksolve; check with sim6 + fev; xcheck vs L-NEW box150 Gen.
  Outcome: 8-capped tower (F(7) = 510) frozen + sent to the Lead at once, or the exact obstruction with the instance.
- Item 2: if level 8 works, state the G_h → G_{h+1} recipe as CONJECTURE with DATA (d per level 20/24/28/32?), with the
  trigger / selector / helper existence sketch (ONE-READ XOR, WINDOW-CAP, PULSE-TRIGGER).
- Item 3 (lower priority): SAT h3d5 (16 instances × 16 cubes, 0 decided at park; experiments/lower/l8/out/sat/STATUS_at_park.txt);
  resume `./sat_all.sh K 3` as tracked tasks; DRUP re-check h3d4 α100 / α110 with IGNDEL=1 (default mode NOT VERIFIED).
- No runs of mine in flight (`pgrep -f "bash scripts/push.sh"` empty before this push). Do not duplicate L-COMP's d 32 brute climbing.

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 332): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
   where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
   open problems.» Constraint: every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD with counters (unit, set, scope).
2. D1 (active, index line 5; DECISIONS.md l. 3): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
   such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: an 8-capped tower and any inductive
   recipe are lower-bound CANDIDATE data/conjecture only; no asymptotic claim from finite data.
3. D14 (active, index line 22; DECISIONS.md l. 244): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: the hand-built level 8 is an own design and goes through the same two-simulator +
   xcheck path as any other genome.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: sessions started with a stale local branch (this one: 48 behind) or shallow clone; a push then fails or pushes old history.
  Check: `git fetch --unshallow`, `checkout claude/l-lower`, `merge --ff-only origin/claude/l-lower`, then assert
  `git branch --show-current` = claude/l-lower and HEAD = origin/claude/l-lower (done above, both true).
- Second: background jobs started with `&` die on restart and escape tracking; SAT cubes lost at restarts (successor 8). Check: only
  tracked run_in_background tasks with resumable .res files; push.sh output redirected to a file, exit code echoed, never piped.
