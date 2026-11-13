# Handover check: L-COMP (successor 22, session_01V5yGRWfgPQ815hzDFM7SSJ; model and effort as the Lead set them under D21 / L53; written 2026-11-13T05:47Z by date -u)
Every answer measured from the repository at the time of writing. Successor of L-COMP 21 (session_01V5yGRXVu462BehsZf8icAx), which parked
with a handover at 367158c9 («HANDOVER -- successor 21» at the top of notes/L-COMP.md; NOTHING RUNNING at the park). This OVERWRITES
successor 21's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (1,666 commits behind origin/claude/l-comp). `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = 367158c9d3ab («L-COMP 21: handover»), working tree clean.
- Trunk origin/claude/vibrant-johnson-nxvvxo = 65e02855265a (commit date 2026-11-13T05:37:20Z, «Lead: R129 third fill ...»).
  `git rev-list --left-right --count HEAD...trunk` = 245 ahead / 581 behind; merge-base ebf59a34f6c8. +1 ahead after this commit.
- Other lanes at my fetch: l-new cd4f7f4ded1b (box 214 Step A, box 215 KEYSIDE-ALL; has experiments/new/box213/keymu213.py and
  experiments/new/box215/keyside215.py, the tools for WORK item 2), l-si 047f07254620, l-red 50fe432a9d19.
- Clock: `date -u` 05:46:27Z against `date: Fri, 13 Nov 2026 05:46:27 GMT` of a raw.githubusercontent.com response, same command: skew below 1 s.
- Container: 4 cores, 15 GB RAM, fresh clone. No job of mine runs; `pgrep -f "bash scripts/push.sh"` empty. NOT in this clone (rebuilt
  before use, per successor 21's «Things only I know»): scratchpad archives LNEW212 (l-new 5fa64fe6), LNEW209, eng/red, eng/lnew, LSI925;
  box37/bin (fast37_w*) and the .git/info/exclude line experiments/comp/box3*/bin/; tools/oink/build.

## 2. Open work and the next step of each (all DATA; nothing runs; waits for «go»)
Order from the Lead's brief:
1. W_ess climb SEEDED at BEST_B3_WU151_NM163 (W_ess 151 at N + M 163, wess 80; experiments/comp/box46), objective W_ess / (N + M),
   must-0 counters as in BOX 46, both second engines (n5b spec, rfd212) on every new best; growth only with fit + residuals or «not
   identified»; a super-polynomial W_ess family goes to the Lead first. Next step: rebuild LNEW212 (git archive l-new 5fa64fe6 ...), build a
   seeded variant of climb46e (win46e.py, run46h) from box46's tools, resumable, tracked task.
2. BEST_B3_WU151_NM163 through L-NEW's keymu213.py (box 213, KEY-TAU) and keyside215.py (box 215, KEYSIDE-ALL), read-only from l-new
   cd4f7f4d (git archive into the scratchpad, run with python3 -I from their own directory); report every must-0 counter.
3. Handover items: BOX 46 item 2 final pass with the use columns (`LNEW212=<archive> bash run46f.sh named`; checkpoint at xmine 19 of 76;
   xbest, xtower, xbig to re-run), then bands B0 [60, 80] and B1 [105, 135] (`bash run46g.sh 0`, `bash run46g.sh 1`, then run46h.sh,
   python3 -B mk46.py).
4. BOX 45 (c): re-run box43/run43a.sh when L-NEW publishes plat208 --hist: at l-new cd4f7f4d `git show ...:experiments/new/box208/plat208.py
   | grep -- --hist` is empty: still waiting.
Limits: at most 2 CPU-heavy jobs including verify; every long job resumable and a tracked background task; no long job before «go».

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk 65e02855 docs/GAPS.md: open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME; no owner is L-COMP). Mention only:
G-N5-TERM (l. 16, owner «L-NEW (L-COMP checks runs)», closed). BOX 46 and the WORK items are DATA for G-N5-TIME (l. 11, owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32; text docs/DECISIONS.md:333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; docs/decisions/D001-launch-brief.md:25, excerpt): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D21 (active, DECISIONS-INDEX.md:46; docs/DECISIONS.md:452): «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is
   fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2
   days.» Lead readings (not the owner's words): L51 (active, :48) maximum effort to 2026-11-14 10:05Z; L53 (active, :50) successors on
   the successor model the Lead names until the Fable reset 2026-11-18 21:00Z. The verify self-check skip is L55 at trunk 65e02855 (DECISIONS-INDEX.md:52;
   DECISIONS.md:504-512); `grep L56` in trunk docs/DECISIONS.md is empty, so the brief's «L56» is not on trunk yet. My branch's
   scripts/verify.sh does not carry the skip (it differs from trunk's), so every push of mine runs in full.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: a job that cannot end. Successor 21's run46f.sh looped at P(X) = 0.0 (rand46.py --acyclic: acyclic draws too rare) until the
2-hour task limit, and a runner script was edited while it ran (run45a.sh). Check: before launching, every runner's sampling loop has a
draw cap (or the rand46 --acyclic P(X) 0.0 cell is skipped), and `tail` of its log is read at each wake-up; a runner or a tool it imports
per genome is never edited while a job uses it (copy to a new name instead). Carried: stale container start (this start: 1,666 behind)
caught by fetch --unshallow + fetch by name + ff-only + `git branch --show-current` + HEAD == origin before any read; `pgrep -f "bash
scripts/push.sh"` empty before every commit and push; push.sh as a tracked background task with a 2-hour timeout, output redirected,
exit code echoed, no pipes, never «&»; no model name in a commit; SHAs quoted only from git output in a later step; every number in a
message pasted from a generated file with path + sha1.
