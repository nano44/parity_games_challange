# Handover check: REFEREE

## successor 28 (2026-11-08T00:12Z by date -u; Opus 5.5, D15; predecessor successor 27, handover d4b39be0)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Trap check: local claude/referee was STALE (1198 commits behind origin). `git fetch --unshallow`, fetch, checkout claude/referee,
  `git merge --ff-only origin/claude/referee`: `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = d4b39be0.
- At d4b39be0: 2 ahead / 124 behind trunk claude/vibrant-johnson-nxvvxo 37a4855e (merge-base af752251).
- Merged trunk 37a4855e with a normal merge 878faaf6: 3 ahead / 0 behind before this file's commit.

### 2. Open work and next step of each
- Inherited queue: none open (successor 27: P-TOWER-FUEL and P-N5-ASC complete; a later P-N5-ASC L-2 would get a byte test).
- P-ACYC (L-SI 43), full independent first review, after «go». Frozen object claude/l-si e3ac4b06 (ancestor of origin/claude/l-si,
  checked). docs/si/P-ACYC.md sha1 0e9edcfda3e3a68dee63ff01427d526b14c67bc4, 16,852 B; L-1 docs/si/P-ACYC-line-L1.txt sha1
  bb12deec6fb0129b4ea9f5af7dd96d6302c5ca50, 2,085 B (both match the brief, measured with git show | sha1sum / wc -c).
  Next: re-derive BETA-ACYC (Γ, Γ3), LAMBDA-CONST, ACYC-LIN, ACYC-XI; FIRST FALLBACK vs SPEC S4/S4c; premise quotes vs trunk
  docs/RESULTS.md by script; §5 scope reading; replay §6 sets A/B/CONTROL with my own simulator in docs/referee/scratch/; DATA rule
  clause by clause on L-1; TARGET.md diff. Report docs/referee/R-P-ACYC.md. docs/referee-2/ not read for this packet before my
  verdict (ls docs/referee-2 | grep -i acyc: 0 files).

### 3. docs/GAPS.md rows relevant to me (trunk 37a4855e)
- REFEREE owns no row. Row the N5 packets feed into: G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D20 (index: active; DECISIONS.md line 423):
   > We have reset the weekly usage, so we can again work faster no?

### 5. One trap that bit this lane, and the check that prevents it
- Trap (again this restart): stale local branch (1198 behind origin). Check: fetch, ff-only, `git branch --show-current` and
  `git rev-parse HEAD origin/claude/referee` equal before any push.sh.
- Trap (s26/s27): the DATA rule applies to my own fix texts, and RESULTS sub-entries are wrapped (single-line quote search gives a
  false NONE). Check: every number in a replacement line comes from my own script first; quote search on joined lines (asc_quotes.py).
