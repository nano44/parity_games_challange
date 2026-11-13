# Handover check: L-RED-B successor 4 (second adversary lane; Opus 5.5 per the brief, L53; D1 / D18 / D21 / D22; written 2026-11-13T06:15:12Z by date -u)
Every answer is measured from the repository at the time above (commands named), not recalled. Predecessor: successor 3
(session_01V5yGRXHoHifjbeqR3Lntn5), handover f5761cff (notes/L-RED-B.md «SUCCESSOR 3 HANDOVER»).
Trap check on entry (06:14Z): the local branch was 23 behind origin/claude/l-red-b; `git merge --ff-only origin/claude/l-red-b`
fast-forwarded it; `git branch --show-current` -> claude/l-red-b; HEAD = origin/claude/l-red-b = f5761cff63babe0f95321d6e4c2355c6b74504bb.
The clone is not shallow (fetch --unshallow was a no-op). Clock skew against the Date header of a raw.githubusercontent.com response:
0 s (local Fri Nov 13 06:14:11 UTC 2026, header «Fri, 13 Nov 2026 06:14:11 GMT»).
This container is fresh: experiments/red-b/work/ does NOT exist (`ls experiments/red-b/work` -> nothing), so the B3/B4 archives
(work/b3/: lnew, lred, lsi, llit, lcomp, trunk) and every state file in work/ are gone; they are rebuilt per docs/red-b/B3-guide.md §6.

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b. `git rev-parse HEAD origin/claude/l-red-b` -> both f5761cff63babe0f95321d6e4c2355c6b74504bb.
- Trunk: `git fetch origin claude/vibrant-johnson-nxvvxo` -> 65e02855265ab0df1a8a3392a980c8d5b459d3a1.
  `git rev-list --left-right --count HEAD...65e02855` -> 27 ahead, 126 behind; merge-base 471aba45214c9b4009332ef1d498dd5dbc42f3cb.
  I do not merge trunk; other lanes' files are read with `git show <ref>:<path>` / git archive.
- Read-only refs fetched 06:1xZ: claude/l-new f8a042ab, claude/l-si 047f0725, claude/l-comp 6ff38698, claude/l-red 50fe432a (full SHAs in
  my notebook when used).
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file.

## 2. Open work and the next step of each
- B1 (box 208), B2 (box 209), B3 (GUIDE-RULE): DONE, NO KILL (docs/red-b/B1-box208.md, B2-box209.md, B3-guide.md). Nothing owed.
- B4 (POST-FALLBACK, docs/red-b/B4-postfb.md §5-§7 at f5761cff): DATA (a) and (b) on origin; verdict «so far» NO CANDIDATE KILL; k = 1 on
  all 62 wrappers (23 B3 bests, 14 B4 bests, 25 own guides), 2..37 iterations after the fallback. §7 lists as not done: a second fallback,
  other families, longer P1 climbs, any proof about the post-fallback phase. `pgrep -af "push.sh|python"` -> nothing running;
  `git status --short` -> clean before this file.
- B5 (SECOND FALLBACK, the Lead's brief for this session), after «go», in order:
  1. Rebuild work/b3 (git archive per B3-guide.md §6: n5v spec, L-COMP's n5b --mode spec, harness Zielonka, hard families).
  2. Read SPEC S4c (docs/new/N5-ssi-global.md «## SPEC») and box 104 §8 («on Γ3(G) and on Γ3*(G*), τ never changes and there is one
     fallback»); write in docs/red-b/B5-second-fb.md, BEFORE any search, why a second fallback is or is not possible on W-type wrappers.
     If it is a proof that k ≤ 1 on all W-wrappers: a lemma (L-RED-B reading, not proved / unrefereed), then wrappers outside W.
  3. Constructions that force k ≥ 2 by design; then climbs on k and on iterations after the first fallback (P1), both engines, every
     output against Zielonka; must-0 counters wrong, engdiff, phasesum; a control that fires; growth words only with a fit + residuals
     or «not identified». A super-polynomial family = kill, reported to the Lead before anything else.
  4. If time remains: longer P1 climbs and the families not yet exercised.

## 3. docs/GAPS.md rows
- Owned: none. Trunk 65e02855 docs/GAPS.md open table rows (file lines 6-11): GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME;
  `grep -c L-RED-B` on it -> 0.
- Worked against: G-N5-TIME (line 11; owner «L-NEW (L-LIT T22; referees later)», status open): N5's polynomial iteration bound.

## 4. Owner rulings, verbatim (trunk 65e02855 docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md at the same commit)
- D1 (DECISIONS.md line 7; index line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
- D18 (DECISIONS.md line 333; index line 32, status **active**):
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- D22 (DECISIONS.md lines 487-491; index line 47, status **active**): the Lead's question «... I propose one more lane, L-RED-B, a second
  adversary ... Under D1, a new attack lane needs your «yes».» Owner (verbatim): «yes»
- Also binding: D21 (line 452, index line 46, active), relayed verbatim «Okay, I want maximum effort. I want to use 200% usage in 3 days.
  ...»; Lead readings L51 (to 2026-11-14 10:05Z) and L53 (Opus 5.5 until the Fable reset 2026-11-18 21:00Z).
- L56 named in the brief: `grep -n L56` on trunk 65e02855 docs/DECISIONS.md -> nothing (L55 at line 505 is the latest there). I take the
  brief's wording (self-check skip only for docs/agents/-only changes; my pushes run in full) as the Lead's and do not rely on any skip.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: successor 2's commit 8d5d8388 was never on origin (its session ended before the push), and container restarts killed two pushes
  of successor 3; a lane can report a SHA that does not exist on origin. Also here: work/ (said to survive restarts) is gone in this fresh
  container. Check: after every push, `git ls-remote origin claude/l-red-b` must print the SHA before it is quoted to the Lead; pushes are
  tracked tasks (2-hour timeout, output redirected, exit code echoed, `pgrep -f "bash scripts/push.sh"` first); long runners are
  resumable and their results are moved to data/ and committed in batches, never kept only in work/.
