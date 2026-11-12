# Handover check: L-COMP (successor 18, Opus 5.5; written 2026-11-12, date -u 05:54Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 17 (handover «HANDOVER -- successor 17 (L-COMP 17,
Opus 5.5) PARKS 2026-11-12 ... after BOX 38. NOTHING RUNNING.», notes/L-COMP.md, park commit 0094f41e). This OVERWRITES successor 17's
answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (1601 commits behind origin/claude/l-comp). `git fetch --unshallow` +
  `git fetch origin claude/l-comp claude/vibrant-johnson-nxvvxo claude/l-new claude/l-red` + `git checkout claude/l-comp` +
  `git merge --ff-only origin/claude/l-comp` -> fast-forward to 0094f41e.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = 0094f41e9adb (rev-parse, 05:53Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = b3d7294c3 («Lead: log 02:18Z-04:03Z (C139 closed; C140 FAIL E-1 -> QN L-2 MATCHES both;
  ...)»). `git rev-list --left-right --count HEAD...trunk` = 180 ahead / 410 behind; merge-base ebf59a34. +1 ahead after this commit.
- Container: 4 cores, 15 GB RAM. No job of mine runs. bin/ (fast36/37/38) is not in this fresh clone and .git/info/exclude lacks the
  box36/bin/, box37/bin/, box38/bin/ and out/.lock_* lines: to be re-added/rebuilt before use (allowed before «go»).

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 39 waits for «go»)
- BOX 38: DONE (experiments/comp/box38/README.md). Nothing open from it except «larger U-constrained T3 climbs if L-SI 50 asks».
- BOX 39 item 1 COUNTER: Q_(>c), Q, maxdepth, loud-depth histogram on my IDEAL-CYC engine (ideal37), implemented from box 206's text
  (claude/l-new docs/new/N5-DEPTH-box206.md: Lemma DEPTH-COUNT, Theorem LOUD-SPLIT, Lemma DIV, Addenda A-D; definitions quoted by line in
  the README), not from L-NEW's code; cross-check vs L-NEW's and L-RED's (R231-*) frozen numbers (CW(n), K1L7 bests, BLKX23/26, CWR),
  mismatches reported exactly. Next step: read box 206 and R231, write the counter, run the cross-check list.
- BOX 39 item 2 CLIMB: k = 1, score Q_(>1) raw, bands N + M [280, 320] and [580, 620], 2 seed streams x 1 restart x 200 proposals per band
  (seeds CW(n), gen37, K1L7 best grown); new bests re-run on a second engine and frozen with sha1; Q_(>2) on the 300 band if budget remains.
- BOX 39 item 3 FIT: Q_(>1) of the bests vs N + M with BOX 37/38 points; exponent +- error or «NOT identified» with the reason. Anything
  clearly above linear -> Lead at once (genome, sha1, two engines).

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk docs/GAPS.md). Mentions: G-N5-TERM (l.16, «L-NEW (L-COMP checks runs)», closed). BOX 39 is DATA for G-N5-TIME (l.11,
owner L-NEW), open (via CONJECTURE DEEP-k1 / Theorem LOUD-SPLIT, box 206, lane-proved, unrefereed).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (brief: lean jobs, <= 2
   CPU-heavy at once, checkpointed.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale/detached container starts (this start: 1601 commits behind) -> pushes fail «invalid refspec». Also a commit made while a push
ran (88ac6b07, successor 17). Checks: fetch --unshallow + ff-only + `git branch --show-current` + HEAD == origin before any edit;
`pgrep -f "bash scripts/push.sh"` empty before every commit and push; push.sh as a tracked background task (never «&»), output redirected
to a file, exit code echoed (no pipes). Counters: every number names its counter (unit, set, scope).
