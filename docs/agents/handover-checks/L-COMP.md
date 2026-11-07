# Handover check: L-COMP (successor 11, Opus 5.5; written 2026-11-07, date -u 10:47Z at start)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of L-COMP 10 (handover «HANDOVER -- successor 10 ... PARKED», notes/L-COMP.md, pushed at d4d9588e). This OVERWRITES
successor 7's answers (the last ones in this file; successors 8-10 wrote theirs into the notebook); older answers are in git history.

## 1. Branch, head, distance to trunk
- Container started on a stale local branch: local claude/l-comp was 3ae78ea8, 66 commits behind origin. `git fetch --unshallow` +
  `git fetch origin claude/l-comp claude/vibrant-johnson-nxvvxo` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = d4d9588e (rev-parse, 10:46:59Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 8abffb34 («Lead: restart rows (L-NEW 60, L-LOWER 5: 4.5 each); log»).
  `git rev-list --left-right --count origin/claude/l-comp...trunk` = 38 ahead / 1365 behind; merge-base cf2e0e4f;
  d4d9588e is NOT an ancestor of trunk (the box 28-30 commits of successor 10 are not merged yet). +1 ahead after this file's commit.
- Container: Oink not present (tools/oink/build/oink missing): scripts/setup_oink.sh running (verify.sh needs it).
  /home/user/pf (query 2 / xval proof dir, outside git) does not exist: q2pieces.sh re-unzips the DIMACS and checks sha1 f3d4b6ad.
  4 cores, 15 GB RAM, ~30 GB disk free.

## 2. Open work and the next step of each (all DATA; relaunch script experiments/comp/box28/relaunch_all.sh, read)
- BOX 30 lane D_d32 (priority): SLACKH=7 score from out/seed_D_d32.txt, next seed 340000 (unit 0). Next step: re-measure the seed with
  my own rclimb30 build (level-5 violations v and F vector; expect 30 / F(6) 222), then run.
- BOX 30 lane B_d32: units 0-5 done (out/B_d32.log, last line 10:06:08Z unit 5 seed 310005, best score 48895, F(6) 190); next seed 310006.
  TRAP FOUND: out/<lane>.unit files are not committed (local exclude), so in this container lane30.sh would restart B_d32 at unit 0
  (seed 310000). Before relaunch I write out/B_d32.unit = 6 and out/D_d32.unit = 0.
- Query 2 (box 28): q2_c0s0p0 CERTIFIED (log/q2/q2_c0s0p0.chk: «s VERIFIED (8849652 lemmas RUP-checked)»; summary.txt). Next: q2pieces.sh
  piece c0s0p1q0, then c0s0 p1-p7 x 4 (vars 50, 56), then c0s1, c4s0, c4s2, c0s2, c0s3, c4s3 x 8 (vars 32, 38, 44).
  Machine split (4 cores): 2 climb lanes + 1 query-2 Glucose/drup + 1 xval (niced) — to be stated to the Lead with «go».
- xval_d3: log/xval_d3.txt has 11 cube lines (0, 1, 2, 3, 5, 6, 9, 10, 13, 14, 15), each frup VERIFIED = drup VERIFIED with lemma counts
  and proof bytes = the P-TR3 table (cube 3: DIMACS sha1 df5ecf8c, 1,419,744,096 bytes, 803,571 lemmas = P-TR3.md l.87). FINDING: cube 3
  is already done (committed in b317e04a), but log/xval_d3/c3.* was never committed, so xval_d3.sh would redo it; remaining: 4, 7, 8, 11, 12
  (c7.frup/.gen exist, no .done). Next step: run those five (I pass the cube list explicitly).
- commit_loop.sh (box28): uses `pgrep -f "^bash scripts/push.sh"` (anchored; push.sh's shebang is `#!/usr/bin/env bash`, so a push's
  command line is «bash scripts/push.sh» and matches) and pushes synchronously, so its own pushes never overlap. Gap: it does not stop
  while MY hand commit is being made; rule: I commit by hand only with the loop stopped (PID file cubes/.pid_commit) or between its
  rounds after checking. Its commit footer names successor 10's session: I update it to mine before relaunch.

## 3. docs/GAPS.md rows owned by L-COMP
None. Open table (trunk 8abffb34 = branch): GAP-A, GAP-C, G-S5-6 (L-ALG), G-NEST (L-RED), G-N1-LB, G-N5-TIME (L-NEW).
`grep -n L-COMP docs/GAPS.md`: line 16, G-N5-TERM («L-NEW (L-COMP checks runs)»), closed. Box 30 / query 2 / xval feed no row directly.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32; DECISIONS.md:333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint: climb outputs are DATA, query 2 is CERTIFIED only when every piece has «s VERIFIED»; nothing is called PROVED.
2. D20 (active, DECISIONS-INDEX.md:42; DECISIONS.md:423):
   > We have reset the weekly usage, so we can again work faster no?
   Constraint (with Lead reading L48, active, line 43): full pace — use all 4 cores; stop on paid overage.
3. D1 (active, DECISIONS-INDEX.md:5; DECISIONS.md:7):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: a HIT is reported with an independent replay (replay30.py), never on rclimb30's word alone.

## 5. One trap that bit this lane, and the check that now prevents it
Trap (successor 10): `pgrep -f` / `pkill -f` match any command line containing the pattern (lost a queued chain 04:3xZ, deadlocked
queued commit jobs 07:2xZ). Check: kill by PID files; anchored pattern «^bash scripts/push.sh» before every push/commit; never edit a
running bash script. Also (this container): state that lives only in gitignored/excluded files (.unit, /home/user/pf, per-cube xval
files) is lost at a new container — re-derive it from committed logs before relaunch (B_d32 unit 6 from out/B_d32.log).
