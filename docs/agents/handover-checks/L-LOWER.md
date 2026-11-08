# Handover check: L-LOWER successor 10 (2026-11-08 06:44Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); local branch was 59 commits behind origin at start and was fast-forwarded
  (`merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head c99c96f16d985356796ceb4fbe450d7b3542d948 = origin/claude/l-lower («L-LOWER 9: h3d5 Glucose results at park ...; HANDOVER appended»).
- Trunk `claude/vibrant-johnson-nxvvxo` at c9591e35ac3aca556e718468e701ab91c84eba4c; merge-base 8cc6ebc6.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 28 ahead, 531 behind. No trunk merge (not needed).

## 2. Open work and the next step of each (BOX L10, after «go»)
- Item 1 (inductive rule): write, from L8 §1g (HIT7 = trigger + selector + helper, ONE-READ XOR) and the L9 §2 delay maps, a
  CONJECTURE with the exact construction G_h → G_(h+1): new pair, trigger / selector / helper, the ROOM re-timing of pairs 0-5, and
  why each lower cap is kept. Next step: re-read L8 §1g and L9 §0-§4, decode HIT7 per level with fenc / sim6.
- Item 2 (level 8 by hand at d 32): from L-COMP's seed out/seed_HIT7_d32.txt (sha1 ad9a39d4) or a frozen L7 best; measure caps per
  level, F vector, T, room and slack violations (fenc exact from d 32, sim6, replay30.py). Success = F(7) = 510 → genome to the Lead at
  once; failure = exact obstruction (cap, window), frozen. Next step: rebuild fenc, reproduce HIT7 numbers (F, 322 room violations).
- Item 3 (optional): h = 3 at d = 6 or Glucose cubes at d = 5 (h3d5 OPEN: 6 TIMEOUT at 1,800 s, 2 never fully run; resume
  `python3 gwhole.py 3 5 1,1,0 3 1800 $SP/sat`). Only if item 1 needs it.
- No runs of mine in flight (`pgrep -f "bash scripts/push.sh"` and `pgrep -f gwhole` empty before this push).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   Constraint: the inductive rule is a CONJECTURE; every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD with counters.
2. D1 (active, index line 5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: an 8-capped tower is lower-bound
   candidate DATA; no asymptotic claim from finite data.
3. D14 (active, index line 22; DECISIONS.md l. 244): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: the hand-built level 8 is an own design; it goes through the same two-simulator +
   L-COMP end-to-end N5 + Oink check as any other genome.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: stale local branch (this start: 59 behind) or shallow clone; a push then fails («invalid refspec») or pushes old history.
  Check: `git fetch --unshallow`, checkout claude/l-lower, `merge --ff-only origin/claude/l-lower`, then assert branch = claude/l-lower
  and HEAD = origin/claude/l-lower (both true above).
- Second: jobs killed by restarts or the 2-hour task limit (successor 9: h3d5 g3 instances killed with no .res line). Check: only
  tracked background tasks sized under 2 h, resumable per-instance result files; push.sh output redirected to a file, exit code echoed.
