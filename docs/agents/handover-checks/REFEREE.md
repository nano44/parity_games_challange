# Handover check: REFEREE

## successor 29 (2026-11-08T05:24Z by date -u; Opus 5.5, D15; predecessor successor 28, handover 85947935)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Trap check: local claude/referee checked out, `git merge --ff-only origin/claude/referee` = already up to date;
  `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = 85947935.
- At 85947935: 7 ahead / 43 behind trunk claude/vibrant-johnson-nxvvxo 8f490d7a (merge-base 94062059).
- Merged trunk 8f490d7a with a normal merge 40a22024: 8 ahead / 0 behind before this file's commit.

### 2. Open work and next step of each (all after «go», in the Lead's order)
- A. P-N5-ASC L-4 byte test (gates R121): claude/l-new a744677e (ancestor of origin/claude/l-new, checked),
  docs/new/P-N5-ASC-line-L4.txt sha1 4017305a34eac21615ba8f172a9b899544d25659, 5,198 B (measured: git show | sha1sum / wc -c).
  Next: rebuild L-3 + R5 with scratch/asc_l3.py and the R5 strings in R-P-N5-ASC.md §E, byte-compare, write §F.
- A2. P-ACYC L-4 = L-3 (03453361) + R-G + R-B byte test: waiting for the SHA from the Lead (L-SI 45 writes it; predicted
  sha1 85bb221f…, 3,080 B). Next: check each replacement vs successor 28's LC-1 text and REFEREE-2 G-1 / W-1; write R-P-ACYC.md §E.
- B. P-N5-QUIET L-2 byte test: waiting for the Lead. Next: check every QT-L1..QT-L6 string (Form B accepted, so no fixed sha
  prediction); write R-P-N5-QUIET.md §C.
- C. P-N5-END (L-NEW 63) full independent first review: frozen claude/l-new 131b4c1c (ancestor, checked), docs/new/P-N5-END.md
  sha1 5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 22,967 B (measured). Next: re-derive E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5,
  EXACT-L, END-T3; premise quotes by script; own-engine replay; DATA rule (line requirements, no L-1 yet); TARGET.md diff.
  docs/referee-2/ not read for this packet before my verdict.

### 3. docs/GAPS.md rows relevant to me (trunk 8f490d7a)
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
- Trap (successor 28, three times): wrong time strings written from memory. Check: `D=$(date -u ...)` pasted into the text in the
  same command (this file's time came that way).
- Trap (s27/s28): stale local branch at restart. Check: fetch, ff-only, `git branch --show-current` and
  `git rev-parse HEAD origin/claude/referee` equal before any push.sh (done above; equal at 85947935).
