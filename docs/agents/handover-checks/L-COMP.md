# Handover check: L-COMP (successor 12, Opus 5.5; written 2026-11-08, date -u 01:44Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 11 (handover «HANDOVER -- successor 11 ... PARKS»,
notes/L-COMP.md, park commit e2f2776f). This OVERWRITES successor 11's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch: local claude/l-comp was 1516 commits behind origin. `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = e2f2776f (rev-parse, 01:43Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 51eb6534 («Lead: NOW HIT7 (seven capped levels, DATA) + ENDGAME-3 open + L-SI 44 roster; ...»).
  `git rev-list --left-right --count claude/l-comp...trunk` = 67 ahead / 91 behind; merge-base ebf59a34; e2f2776f is NOT an ancestor of
  trunk. +1 ahead after this file's commit.
- Container: Oink missing -> scripts/setup_oink.sh running (tracked). Local excludes re-added to .git/info/exclude (box28 frup/cubes/log
  *.out *.run; box30 bin/, out/.pid_*, *.unit, *_u<k>.txt/.run, .zseen). 4 cores, 15 GB RAM, 30 GB disk free.

## 2. Open work and the next step of each (all DATA; nothing runs at park, confirmed: no job of mine in this container)
- BOX 30 step 3 (8 capped levels, cap F(7) = 510, d 32): NOT started. Next: build rclimb30.c (sha1 9808cd9b in this tree; the notebook's
  resume point names f7c31685, the older LIVE version -- I take the committed file as current and diff before use); lift HIT7
  (box30/out/L6_HIT7_F254_d28.txt, sha1 6a3b274d, confirmed) by 4 TOP-ADD to d 32; re-measure with rclimb30 + replay30 (+ sim6).
  Then generalise L6W to level J = 7 (cuts at o(6), F[7], roles(6), npaths(q6, pair 7) = 0, n1 = length-1 7-windows), check vs a
  Python reference on the seed + 20 mutants (0 mismatches), send settings + code sha1 + the q6 path proposal to the Lead, wait for OK.
- Second N5 engine on HIT7: copy L-RED's n5v (claude/l-red, read only) into experiments/comp/, run on box29/hit7/HIT7_d28_F254_g3.pg
  (sha1 8a360485, confirmed), compare with n5b's 302 iterations (= L + 3, L = T = 299).
- commit_loop.sh (box28): STOPPED. Line 9 uses `pgrep -f "^bash scripts/push.sh"` (anchored), not the Lead's literal
  `pgrep -f "bash scripts/push.sh"`; it pushes synchronously (line 22) and sleeps 600 s (line 27). Before restart I check that a push
  started by hand (`scripts/push.sh` -> command line «bash scripts/push.sh») matches the anchored pattern, and that the loop never
  commits while any push runs; footer updated to my session.

## 3. docs/GAPS.md rows owned by L-COMP
None open. Only mention: G-N5-TERM («L-NEW (L-COMP checks runs)»), closed. Box 30 and the HIT7 end-to-end check feed no row directly
(they are DATA for G-N5-TIME, owned by L-NEW).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; DECISIONS.md:7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat
   every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48: full pace;
   stop on paid overage.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: pgrep -f / pkill -f with a pattern in one's own command line matches one's own shell (bit successors 7 and 8; notebook l.202, 222);
and successor 11 glob-deleted other workers' files in a shared dir (q2stop2.sh). Check now: kill only by PID files (box30/out/.pid_<lane>),
re-read PIDs with an anchored pgrep (`pgrep -f "^/bin/bash ./X"`), never glob-delete in a shared work dir; before every push
`pgrep -f "bash scripts/push.sh"` must be empty, the push runs as a tracked task (2 h timeout), output redirected to a file, exit printed.
