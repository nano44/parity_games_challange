# Handover check: L-SI (successor 2, Opus 5.5 per D15/L37; written 2026-10-24 17:35Z by date -u)
Overwrites successor 1's check (96469356). Every answer measured from the repository in this container (commands named), not
recalled. Predecessor: L-SI successor 1, parked 2026-10-24 ~17:35Z at l-si 6e5f64ad ("L-SI successor 1: handover notes").

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-si. The local branch at container start was STALE (0d48da26, 2026-10-15). After
  `git fetch origin claude/l-si claude/vibrant-johnson-nxvvxo`: origin/claude/l-si = 6e5f64ad; `git merge --ff-only origin/claude/l-si`
  brought HEAD to 6e5f64ad (fast-forward, no merge commit).
- `git rev-list --left-right --count origin/claude/l-si...origin/claude/vibrant-johnson-nxvvxo` = 3 0: 3 ahead, 0 behind trunk.
  merge-base c371ffdf. The 3 commits: 8314ce9c (box 3 final), 78b5a9dc (merge trunk), 6e5f64ad (handover notes).
  After this file's commit: 4 ahead, 0 behind (SHA in the message to the Lead).

### 2. Open work and the next step of each
Nothing runs (predecessor parked; no background jobs in this container). tools/oink/build is absent: scripts/setup_oink.sh must run
before any Oink-verified citation (check_sol2.py, verify smoke).
- Box 4 (Lead brief, after "go"): the proof side of (X) = crossing transitions per joint λ-phase (L-NEW box 28 §5c READING: N5 makes
  O(n⁴(1 + X + O)) transitions per phase on o-cyclic one-Odd-choice games). Next step: classify crossings (active/passive,
  entering/leaving R), find what each pays with, then look for an additive potential that rises at every INR/crossing and is not
  restored by o-free progress (box 3 §3), or prove none of a natural kind exists; measure on experiments/si/orlens/instances
  (16 files) and experiments/red/xing/instances.
- OPEN from box 3 (notes/L-SI.md "OPEN"): (ELIM-poly), (LEVEL-poly) (data max m_r 11 at n 32, two nested counter digits in
  lev_l_sc / lev_l_x, no third), (CYC-u*). Next step: none of mine unless box 4 reaches them; the kill design (a carry above 24/21
  in lev_l_sc) is routed to L-RED.
- Old queue (notes "Queue"): fhz_padded rerun for S5/S6 with --engine fast; keep experiments/si/check.sh green. Not in box 4;
  check.sh is run by verify.sh on every push.

### 3. docs/GAPS.md rows I own (`grep -n "L-SI" docs/GAPS.md` at 6e5f64ad: no hits)
- None. The row this lane feeds is G-N5-TIME (owner L-NEW; status open); its 17:24Z update names (X) and (NH') OPEN, which is box 4's
  target. My box 1-3 statements (Lemma U, E1-E6, D, VIS, VIS', LEN, CH, counter bound) are lane readings in docs/si/, PROVED by
  L-SI successor 1, UNREFEREED, not GAPS rows.

### 4. The three owner rulings that most constrain me (verbatim), with index status
1. D18 (docs/DECISIONS.md#d18 l.333; DECISIONS-INDEX row D18 "active"):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Lead reading L40 (active): every statement labelled PROVED (by whom) / CONJECTURE / OPEN; every ASSUMPTION in one line.
2. D1 (docs/DECISIONS.md l.6-7; docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D16 (docs/DECISIONS.md#d16 l.300; DECISIONS-INDEX row D16 "active"):
   > Then keep working as I told you to
   Lead reading L38 (active): no idle fleet; the lane generates its own next direction.
   (Also binding: D15 "Be autonomous, reason about it" (active, L37): no option questions to the owner.)

### 5. One trap, and the check that prevents it
- Trap: citing an unverified climb result. climb.py and sweep.py call elim_g WITHOUT the assert that ortrace.run_states matches
  n5.run's (iterations, fallbacks) (notes "Things only I know"), so a climb "best" can come from a run that is not N5's run.
  Related earlier trap: Odd's final strategy by argmin-over-successors is WRONG (fails verify.py on 3/600 random games and on
  switchallexp); use the recorded restricted-graph counterstrategy.
- Check: re-run any climb best with gaps.py (asserts equality with n5.run) and, per the box-4 rule, re-verify every cited instance
  with experiments/new/n5.py, Oink zlk and check_sol2.py before citing it; pin it in an instances/ directory with its sha1.
- Also carried: stale container (it was stale this time: fetch + ff before anything); push only via scripts/push.sh with output to a
  file, then `$?`, never piped.
