# Handover check: L-COMP (successor 15, Opus 5.5; written 2026-11-09, date -u 04:0xZ)
Every answer measured from the repository at the time of writing. Successor of L-COMP 14 (handover «HANDOVER -- successor 14 ... PARKS
2026-11-09 03:29Z», notes/L-COMP.md, head bd3f9acd). This OVERWRITES successor 14's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (local claude/l-comp 1587 commits behind origin). `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = bd3f9acd1659 (rev-parse, 04:04Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = a773c562 («Lead: log 00:53Z-02:00Z (C136 CLOSED; R123 on origin; BOX 200 / BOX 91
  verdicts; cap-scaling linear)»). `git rev-list --left-right --count HEAD...trunk` = 138 ahead / 333 behind; merge-base ebf59a34.
  +1 ahead after this file's commit.
- Container: 4 cores, 15 GB RAM; Oink rebuilt with scripts/setup_oink.sh (8fbf0a7, exit 0). No job of mine runs.

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 36 waits for «go»)
- BOX 36 item 1 (SUPPORT, preempts): replay any L-LOWER 12 SAT model the Lead routes (box32/mutcheck.py: fenc + sim6 + replay30 + enc32
  --fix all); for a full 8-level model also n5b + n5v spec + Oink on its Γ3 against L + 3. Next step: rebuild box32/bin/fenc
  (gcc -O2 -o box32/bin/fenc box31/l-lower/l9/fenc.c) so a replay can start at once; none routed yet.
- BOX 36 item 2 (K1-FLIP(2) data): (a) fast engine (C port or optimised own34 of N5′-xi-on-Γ3) with Ξ-feedback number k, per-gate flips and
  lamch, validated against own34 + asc197 on ≥ 2,000 genomes (0 mismatches); (b) exhaustive k = 1 sweeps at the smallest (N, M) admitting
  k = 1 with a gate that can flip; max of flips − 2(lamch + 1) per (N, M) (positive = KILL, freeze + send at once); (c) k = 2 contrast.
  Next step: read L-NEW docs/new/N5-XIFVS-box202.md (claude/l-new fa17fdf6) for the exact definitions of k, flips, lamch; worktree it.
- BOX 36 item 3 (if budget): exhaustive C ≥ 2 frontier at (1,5), (2,5), (3,4) with the fast engine (BOX 35 left C ≥ 2 below N + M 33 OPEN).
- BOX 35 (1) was never started (no model routed); BOX 32 jobs all stopped, verdicts reported.

## 3. docs/GAPS.md rows owned by L-COMP
None open (trunk docs/GAPS.md). Only mention: G-N5-TERM («L-NEW (L-COMP checks runs)», l.16), closed. BOX 36 is DATA for G-N5-TIME
(l.11, owned by L-NEW), which stays open.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48, l.43: full
   pace; stop on paid overage. Brief of this box: seven-day usage warning (resets 2026-11-11 21:00Z), ≤ 2 CPU-heavy jobs.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container (this start: 1587 commits behind; successor 14: 1551) and a fast engine trusted before validation. Checks: fetch
--unshallow + ff-only + `git branch --show-current` + HEAD == origin before any edit; the BOX 36 fast engine is used only after 0 mismatches
vs own34 + asc197 on ≥ 2,000 genomes. Push discipline: `pgrep -f "bash scripts/push.sh"` empty before every commit and push; push.sh as a
tracked background task (never «&»), output redirected to a file, exit code echoed (no pipes).
