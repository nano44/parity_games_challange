# Handover check: REFEREE

## successor 27 (2026-11-07T14:09Z by date -u; Opus 5.5, D15; predecessor successor 26, handover e96c8542)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Trap check: local claude/referee was STALE (959 commits behind origin). `git fetch --unshallow`, fetch, checkout claude/referee,
  `git merge --ff-only origin/claude/referee`: `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = e96c8542.
- At e96c8542: 7 ahead / 231 behind trunk claude/vibrant-johnson-nxvvxo 9315f36c (merge-base d7885be4).
- Merged trunk 9315f36c with a normal merge 93320d13: 8 ahead / 0 behind before this file's commit.

### 2. Open work and next step of each
- P-TOWER-FUEL (L-LOWER 5), full independent first review, after «go». Frozen object: claude/l-lower 7f7ff6f5 (ancestor of
  origin/claude/l-lower, checked). L-1 docs/lower/P-TOWER-FUEL-line-L1.txt: sha1 408470adbb1d80f0ed4f29b363867da3d6d430d4 (matches
  the brief); 3,699 characters = 3,834 bytes (the brief's «3,699 B» counts characters; UTF-8 multibyte symbols).
  Next: re-derive MOVE, DOUBLE-EQ (E1)-(E5), PULSE-NEST, GAP-NEST, DOMINANCE-FREEZE (a)-(b), CROSS-ECONOMY (i)-(iii); premise quotes vs
  docs/RESULTS.md on trunk by script (R104, R105 ENC, R110, R113 ALIGN); replay I-ROOM G7_best_d28 and I-FUEL SL41_d28 and the §5
  counters with my own simulator docs/referee/scratch/t3r_sim.py; DATA rule clause by clause on L-1; TARGET.md diff.
  Report docs/referee/R-P-TOWER-FUEL.md. docs/referee-2/ not read on this packet before my verdict is written (ls: 0 files on it).

### 3. docs/GAPS.md rows relevant to me (trunk 9315f36c)
- REFEREE owns no row. Row the lower-bound packets feed into the N5 picture: G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees
  later)», open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D20 (index: active):
   > We have reset the weekly usage, so we can again work faster no?

### 5. One trap that bit this lane, and the check that prevents it
- Trap (again this restart): stale local branch (959 behind origin/claude/referee). Check: fetch, ff-only, `git branch --show-current`
  and `git rev-parse HEAD origin/claude/referee` equal before any push.sh.
- Trap (s26): the DATA rule applies to my own fix texts (an unmeasured «l = 1, …, 4»). Check: every set or count I write into a
  replacement line is produced by my own script first, and the script is cited.
