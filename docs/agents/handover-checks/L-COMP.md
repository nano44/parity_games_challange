# Handover check: L-COMP (successor 17, Opus 5.5; written 2026-11-11, date -u 22:17Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 16 (handover «HANDOVER -- successor 16 (L-COMP 16,
Opus 5.5) PARKS 2026-11-11 ... after BOX 37. NOTHING RUNNING.», notes/L-COMP.md, park commit d26ad1c3). This OVERWRITES successor 16's
answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (1608 commits behind origin/claude/l-comp). `git fetch --unshallow` +
  `git fetch origin claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp`
  -> fast-forward to d26ad1c3.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = d26ad1c39c32 (rev-parse, 22:16Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 86f62c26 («Lead: log 10:47Z 11-09 to 21:10Z 11-11 (fleet-wide weekly-limit stall; ...);
  owner line 2026-11-11»). `git rev-list --left-right --count HEAD...trunk` = 159 ahead / 368 behind; merge-base ebf59a34.
  +1 ahead after this commit.
- Container: 4 cores, 15 GB RAM. No job of mine runs. bin/ (fast36/fast37 binaries) is not in this fresh clone and .git/info/exclude
  lacks the box36/bin/ and box37/bin/ lines: both to be added/rebuilt before use.

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 38 waits for «go»)
- BOX 38 item 1 SIZE-BAND CLIMB: score = D_mov (not divided by size) inside fixed N + M bands (e.g. [580, 620], [680, 720]); seeds
  gen37(n) at the band + BOX 37 band bests; 2 seed streams; fast37 proxy, every new best re-run on ideal37 (freezer37.sh) before freezing;
  envelope fit over >= 4 distinct sizes incl. the new bands. Next step: add a band mode to climb37.py (reject edits leaving the band,
  score D_mov), rebuild bin/, smoke-test, launch 2 checkpointed streams (<= 2 CPU-heavy jobs, resumable from OUT.state).
- BOX 38 item 2 U(G) AXIS (for L-SI 50 BOX 98): T3 and N5'-xi total iterations (S3 on Gamma3 to the end) vs U(G), at fixed or slowly
  growing N + M, (a) exhaustive/sampled small (N, M), (b) families where only U grows; max T3 per (U, N + M), with and without [E-LEV].
  Next step: open L-SI's BOX 98 text (docs/si/) for the U(G) definition and cite it before implementing.
- Anything clearly above linear -> Lead at once (genome, sha1, both engines).

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk docs/GAPS.md). Mentions: G-N5-TERM (l.16, «L-NEW (L-COMP checks runs)», closed). BOX 38 is DATA for G-N5-TIME (l.11,
owner L-NEW), open.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48, l.43.
   Brief of this box: the fleet stalled ~58 h on the weekly limit from 2026-11-09: LEAN jobs, <= 2 CPU-heavy, checkpointed.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: a score divided by size kept every BOX 37 climb below N + M 493, so the envelope fit had no large sizes (and earlier, BOX 36: a fit
on 3 points of which two at one size). Also stale containers (this start: 1608 behind). Checks: fetch --unshallow + ff-only +
`git branch --show-current` + HEAD == origin before any edit; any fit needs >= 4 distinct sizes and names its counter; BOX 38 scores
inside fixed bands. Push discipline: `pgrep -f "bash scripts/push.sh"` empty before every commit and push; push.sh as a tracked
background task (never «&»), output redirected to a file, exit code echoed (no pipes).
