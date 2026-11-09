# Handover check: L-COMP (successor 16, Opus 5.5; written 2026-11-09, date -u 07:57Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 15 (handover «HANDOVER -- successor 15 (L-COMP 15,
Opus 5.5) PARKS 2026-11-09 ... after BOX 36», notes/L-COMP.md, park commit fa97fa0a). This OVERWRITES successor 15's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (local claude/l-comp 1594 commits behind origin, at 3ae78ea8). `git fetch --unshallow` +
  `git fetch origin claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp`
  -> fast-forward to fa97fa0a.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = fa97fa0a91f0 (rev-parse, 07:57Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 547985a1 («Lead: log 05:17Z-06:23Z (both referees MATCH P-N5-END L-4; ...; k = 1 climbs)
  + resume delta»). `git rev-list --left-right --count HEAD...trunk` = 145 ahead / 337 behind; merge-base ebf59a34. +1 ahead after this commit.
- Container: 4 cores, 15 GB RAM. No job of mine runs. fast36 binaries (bin/, not committed) and Oink to be rebuilt before use.

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 37 waits for «go»)
- BOX 37 item 1: extract a parametric family gen37(n) from BEST_C300_r34_C17 (30d4ea76) and BEST_B400_r34_C17 (1694d52f): diff the
  accepted genomes of C300 restart 0 (17 -> 20 -> 24 -> 28 -> 32 -> 34), reproduce both bests byte for byte (or state where not), measure
  per-gate flips (per-gate maximum), C, T3, N + M up to caps ~500 / ~700 on fast36 + own36, fit on >= 4 distinct sizes. Next step: locate
  the climb logs / accepted-genome checkpoints of C300 restart 0 in experiments/comp/box36/out/climb and diff consecutive accepts.
- BOX 37 item 2 (only if item 1 fails): k = 1 climb at caps 500 and 700 with a stated size penalty, 2 seed streams each, freezer.sh per
  new best, fit on bests at >= 4 distinct sizes.
- BOX 37 item 3: any point clearly above linear (per-gate flips or C against N + M) to the Lead at once (genome, sha1, two engines).
- Open from BOX 36: whether gate (82, 0) of the r32/r34 bests descends from MWR8_2's qz (62) (not checked).

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk docs/GAPS.md). Mentions: G-N5-TERM (l.16, «L-NEW (L-COMP checks runs)», closed). BOX 37 is DATA for G-N5-TIME (l.11, owner
L-NEW), open.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48, l.43. Brief
   of this box: seven-day usage warning (resets 2026-11-11 21:00Z), <= 2 CPU-heavy jobs.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container (this start: 1594 commits behind; successor 15: 1587) and a fit read as a growth law when the points are not
distinct sizes (BOX 36: 3-point fit, two at the same size; reported NOT identified). Checks: fetch --unshallow + ff-only +
`git branch --show-current` + HEAD == origin before any edit; any fit needs >= 4 distinct sizes and names its counter (per-gate maximum vs
total). Push discipline: `pgrep -f "bash scripts/push.sh"` empty before every commit and push; push.sh as a tracked background task (never
«&»), output redirected to a file, exit code echoed (no pipes).
