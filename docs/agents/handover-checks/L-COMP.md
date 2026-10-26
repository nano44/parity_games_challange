# Handover check: L-COMP (successor 6, Opus 5.5; written 2026-10-26T19:1xZ, date -u 19:04:08Z at start)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of session_017XFY64b42Hkc6fmeUEzwek (successor 5, handover fb88708d). This OVERWRITES successor 5's answers (1a8a4628 era);
those and older answers are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`. Local head at start was 298d2dc6 (stale container again, though `git status` said "up to date");
  `git fetch origin claude/vibrant-johnson-nxvvxo claude/l-comp` moved origin/claude/l-comp 298d2dc6..fb88708d; tree clean,
  fast-forwarded (`git merge --ff-only`) to fb88708d.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = 1ba37bf3 ("Lead: LAND RESULTS R73 (P-N5-EPC; CHECKER C82 Add. 1 c785690c PASS) ...").
  Before merging: fb88708d was 0 ahead / 51 behind trunk (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`),
  merge-base fb88708d (trunk already contains every lane commit). Merged trunk with a merge commit (no rebase): 866f9094.
  Now 1 ahead (the merge) / 0 behind; +1 ahead after this file's commit.
- Container: Oink built by scripts/setup_oink.sh in this session (exit 0, "oink built at 8fbf0a7", tools/oink/build/oink present); no python jobs
  (`pgrep -a python` empty) before the build.

## 2. Open work and the next step of each
- In flight: nothing (successor 5's notebook: "No background jobs"; box 15 pushed fb88708d).
- BOX 16 (Lead brief, waits for "go"): Friedmann's H_n (LMCS 7(3:19) 2011, arXiv 1106.0778, §8.4) under N5. Next step after GO:
  open the full text of [F], record §/figure numbers in notes/L-COMP.md; check whether M1's ports (experiments/hard-families/
  pgsolver_port.py, pgsolver_si.py; switchallexp/switchbestexp) are faithful to §8.4 (they port PGSolver's switchallexp.ml /
  switchbestexp.ml, which target switch-all / switch-best SI, not necessarily H_n as printed); else build H_n from the paper;
  read docs/new/N5-ALTLIT-box49.md (NOT on trunk 1ba37bf3; on origin/claude/l-new) and docs/si/N5-EXIT-box22.md §9 for ALT_c(S),
  N_ep, NCONF definitions; run n5b SPEC (with n5 = n5b cross-check) from [F]'s start and from S3, n = 3..8.
- Open items left by successor 5 (no step unless routed): L-SI FREEZE-G per-gate reset count (NOT RUN); longer lend doubling at n 32.

## 3. docs/GAPS.md rows owned by L-COMP
None. On 1ba37bf3 the open table (lines 6-11) owners are L-ALG (GAP-A, GAP-C, G-S5-6), L-RED (G-NEST), L-NEW (G-N1-LB, G-N5-TIME).
`grep -n -i l-comp docs/GAPS.md` hits line 16, G-N5-TERM (closed; owner L-NEW, "L-COMP checks runs"), and DATA citations inside
line 11 (G-N5-TIME, L-COMP climbs X 67 / X 75 at n 32). Box 16 feeds G-N5-TIME (ALTERNATION count).

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on 1ba37bf3)
1. D18 (active, DECISIONS-INDEX.md:32), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint: box 16 is N5-focused; every number is DATA, never PROVED by me; assumptions (e.g. the start used for H_n) stated, no owner questions.
2. D2 change 5 (D2 active, DECISIONS-INDEX.md:6), docs/DECISIONS.md:27-28:
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: every H_n run is checked against Oink (zlk or --tl) and verify.py strategies before it is reported; instances pinned by sha1.
3. D1 (active, DECISIONS-INDEX.md:5), docs/DECISIONS.md:6-7:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: H_n is a falsification test for N5's running time; an exponential count goes to the Lead at once with the instance;
   results leave only via scripts/push.sh and send_message to the Lead.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: late-read Lead messages. Successor 5 (notebook "Things only I know") read four Lead messages only at the end of box 14, after
C-ONCE and UL_C were already dead. Check: ReadNotifications between every wait step of a long box (each background job poll, each push),
not only at the end. Carried over and hit again today: stale container (local 298d2dc6 while origin was fb88708d) -> fetch +
ff-only + is-ancestor before any work.
