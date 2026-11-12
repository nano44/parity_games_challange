# Handover check: L-COMP (successor 21, session_01V5yGRXVu462BehsZf8icAx; model and effort as the Lead set them under D21 / L53; written 2026-11-12T20:01Z by date -u)
Every answer measured from the repository at the time of writing. Successor of L-COMP 20 (session_01V5yGRYzeDgxCBBXtVUzaJi), which was
stopped by the Fable weekly limit at about 19:38Z (per the Lead's brief) without a park commit; its last pushed state is the «RESUME
POINT -- successor 20» at the top of notes/L-COMP.md (aa863db5). This OVERWRITES successor 20's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (1,621 commits behind origin/claude/l-comp). `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` ->
  fast-forward. Working tree clean.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = `git ls-remote origin claude/l-comp` =
  aa863db51fa9 («BOX 44 part 1»).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 7fa6aff4aa04 (commit date 17:10:52Z, «Lead: CI job lean-lemmas ...»).
  `git rev-list --left-right --count HEAD...trunk` = 200 ahead / 479 behind; merge-base ebf59a34f6c8. +1 ahead after this commit.
- Other lanes at my fetch (~20:01Z): l-si 516b68371860 (box 105 lemma section, successor 52 handover), l-new 069c888b6d0a (successor 73
  handover; BOX 211 frozen at 1e6df499), l-red 2d290a15b672 (R237 (2)). L-SI's replay commit 925577fe is on origin (ancestor of
  origin/claude/l-si) with experiments/si/box104/out/replay209_{level,plat,ctrl}.out and replay209_engine.sha1.
- Clock: `date -u` 20:00:45Z against `date: Thu, 12 Nov 2026 20:00:45 GMT` of a raw.githubusercontent.com response, same command:
  skew below 1 s.
- Container: 4 cores, 15 GB RAM, fresh clone. No job of mine runs; `pgrep -f "bash scripts/push.sh"` empty. NOT in this clone (lost
  with successor 20's container; rebuilt before use): successor 20's scratchpad archives LSI104 (l-si 26704e01) and LNEW209 (l-new
  311bbf81), box37/bin (fast37_w*) and its .git/info/exclude lines, tools/oink/build, and every out/ row successor 20 had not committed
  (item 2's long runs, set «mine», the 925577fe cross-check and run44c's cross; item 3's climb state, its best T3 65 at N + M 285).

## 2. Open work and the next step of each (all DATA; nothing runs; waits for «go»)
- BOX 44 item 1 (WRAP third engine): DONE at aa863db5 (record experiments/comp/box44/README.md).
- BOX 44 item 2 (box 209 on my own Γ3 builder): main part on origin (records 25, corpus 53, dead 3, rand 1,000, mut 600 + controls;
  t3all 0; largest T3 199). PENDING in the README (l. 182-191): (i) set «mine» (box40/inst; 11 of L-SI's 26 genomes) and the long
  runs «big» (out/lev44_big.out, T3 up to 294); (ii) the cross-check against L-SI's replay 925577fe (26 genomes; 15 already equal;
  expect 26/26); (iii) run44c.sh (L-NEW's level208.py --hist / plat209.py --hist on my runs). Next step: rebuild the archives
  (git archive), re-run run44b.sh phases mine + big (resumable, tracked task), cmp against 925577fe, run44c.sh, regenerate the README
  with mkreadme44.py, mark PENDING parts done, one push.
- BOX 44 item 3 (climb T3 / (N + M) at N + M ≈ 300, two seed streams): successor 20's climb state is lost (not committed); restart
  run44d.sh from its seeds (resumable), bests on a second engine (own34 vs fast37 / L-NEW's n5v), freeze bests, fit or «NOT
  identified»; one push.
- Queued behind BOX 44 (Lead 17:37Z): (a) a depth notion TAIL cannot inflate, counted on the frozen sets; (b) the per-gate quiet-flip
  maximum beyond linear; (c) re-run run43a.sh if L-NEW publishes plat208 --hist: at l-new 069c888b `git grep -- --hist` finds box208's
  level208.py / ownhist208.py and box209's plat209.py, not a plat208.py --hist; (c) stays waiting.
- Limits I keep: at most 2 CPU-heavy jobs including verify; every long job resumable and a tracked background task; no long job
  before «go»; one push per completed item.

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk 7fa6aff4 docs/GAPS.md: open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME; no owner is L-COMP). Mention only:
G-N5-TERM (l. 16, owner «L-NEW (L-COMP checks runs)», closed). BOX 44 is DATA for G-N5-TIME (l. 11, owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32; text docs/DECISIONS.md:333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; docs/decisions/D001-launch-brief.md:25, excerpt): «A claimed polynomial algorithm is far more
   likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D21 (active, DECISIONS-INDEX.md:46; docs/DECISIONS.md:451-454): «Okay, I want maximum effort. I want to use 200% usage in 3 days.
   There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200%
   uage under 2 days.» (direct confirmation: «I confrim tge stuff»). Lead readings, not the owner's words: L51 (active, :47) maximum
   effort to 2026-11-14 10:05Z; L52 (active, :48) a limit that has reset is a pause. L53 (this session on Opus 5.5 because the Fable
   5.2 weekly limit is reached) is in my brief but NOT in trunk 7fa6aff4's DECISIONS-INDEX.md (`grep -n L53` empty).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: uncommitted long-run output lost with a container. Successor 20 was stopped by a limit with item 2's long runs, the 925577fe
cross-check, the run44c cross and item 3's climb only in its working tree and scratchpad; all are gone. Check: every completed phase
is committed locally at once (commits are cheap; pushes batched), out/ rows and climb checkpoints (out/*.ck) live in the repo tree,
and the notebook's resume point names the last committed phase. Carried: stale container start (this start: 1,621 behind) caught by
fetch --unshallow + fetch by name + ff-only + `git branch --show-current` + HEAD == ls-remote before any read; `pgrep -f "bash
scripts/push.sh"` empty before every commit and push; push.sh as a tracked background task with a 2-hour timeout, output redirected,
exit code echoed, no pipes, never «&»; no model name in a commit; SHAs quoted only from git output in a later step.
