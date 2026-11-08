# Handover check: REFEREE

## successor 30 (2026-11-08T10:03Z by date -u; Opus 5.5, D15; predecessor successor 29, handover abb93f06)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` + fetch; local claude/referee was 53 behind origin, fast-forwarded with `git merge --ff-only`;
  `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = abb93f06.
- At abb93f06: 17 ahead / 8 behind trunk claude/vibrant-johnson-nxvvxo 3613a1ac (merge-base 8f490d7a).
- Merged trunk 3613a1ac with a normal merge 31f06731: 18 ahead / 0 behind before this file's commit.

### 2. Open work and next step of each (all after «go», in the Lead's order)
- A. P-N5-CHAIN L-2 byte test: L-1 = claude/l-new 71b75424 (ancestor of origin/claude/l-new, checked), sha1 bd152dd9…; apply CL-1
  (Form A, strings in R-P-N5-CHAIN.md §5) with scratch/chain_linefix.py; predicted sha1 e481d260884807424c545bd3f3cdd7fbfb25f05c,
  8,248 B. Next (on the Lead's SHA): cmp with the lane's L-2, check CN-1 in fixes entry 1 (ties has no control), CO-1 optional; write §C.
- B. P-N5-END L-3 byte test: L-2 = claude/l-new 2fcee038 (ancestor, checked), sha1 e8a8ac51…; L-3 = L-2 + REFEREE-2 34's required L-R1
  («changes only» → «leaves κ0 only») + optional N-1 / N-2 (claude/referee-2 9b3cc9b6) + successor 29's optional EL-1 / EL-2.
  Next: check each string and its meaning against L-2; write R-P-N5-END.md §D.
- C. CHECKER items on P-N5-ASC (R121), P-ACYC (R122), P-N5-QUIET, P-N5-END: none routed yet; act when the Lead routes one.

### 3. docs/GAPS.md rows relevant to me (trunk 3613a1ac)
- REFEREE owns no row. Row the N5 packets feed into: G-N5-TIME (line 11; major; owner «L-NEW (L-LIT T22; referees later)»; open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D20 (index: active; DECISIONS.md line 423):
   > We have reset the weekly usage, so we can again work faster no?
   (Read with the brief's seven-day usage warning: keep runs lean.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s30, again this restart: 53 behind): stale local branch. Check: fetch, ff-only, `git branch --show-current` and
  `git rev-parse HEAD origin/claude/referee` equal before any push.sh (done above).
- Trap (s28): wrong times from memory. Check: `D=$(date -u ...)` pasted into the text in the same command (this file's time came that way).
