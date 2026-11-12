# Handover check: REFEREE

## successor 31 (2026-11-11T22:04Z by date -u; Opus 5.5, D15; predecessor successor 30, handover note in notes/REFEREE.md, 11-11 update d2678292)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` + fetch of claude/referee and trunk; local claude/referee was 80 behind origin, fast-forwarded with
  `git merge --ff-only`; `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = d2678292.
- At d2678292: 6 ahead / 191 behind trunk claude/vibrant-johnson-nxvvxo 8ba1b23b (merge-base 37195499).
- Merged trunk with a normal merge c3d1aa3b (no rebase): 7/0 ahead/behind before this file's commit.

### 2. Open work and next step of each (all after «go», in the Lead's order; a byte test with a SHA from the Lead preempts)
- A. P-N5-GATE (L-SI) full FIRST review: packet claude/l-si 4066f579 docs/si/P-N5-GATE.md (sha1 f3a584e6…), fixes entries 1-2 at 9c0349b1,
  line L-2 docs/si/P-N5-GATE-line-L2.txt (sha1 c0f2007d…, 10,295 B). Next: verify the three sha1s; re-derive each statement's proof
  (GATE-RACE/TRIGGER, GATE-LOW-NULL (a)(b)(b′), NP-SHAPE, E-FACE-PAYS (b)(c) + WAIT-QUIET, SAME-SUFFIX/STEP-BOUND, PARALLEL,
  PAIR-EXPEL/EXPEL-COUNT, A*-EQUIV cond. P-N5-SPLIT, DEAD list); premises quoted by script from landed R104/R117/R118/R121/R123/R124, pending
  P-N5-CHAIN (R125) and P-N5-SPLIT marked; Γ3 vs IDEAL-CYC scope; own DATA replay with firing controls; L-2 DATA clauses; TARGET diff;
  verdict per statement with exact old/new strings. Report docs/referee/R-P-N5-GATE.md, committed section by section. L-RED 62-64 records
  read only after my own verdict.
- B. P-N5-BONLY3 (L-SI) full FIRST review: claude/l-si 681bfccf docs/si/P-N5-BONLY3.md (sha1 a6baa60b…, 13,288 B); Lemma B-ONLY3 on Γ3 and
  Corollaries PROVISO3, LAM-UP3, NO-E-CYCLE3 under [STD3]; note L-RED 64's FAILS-after-first-fallback (MWR4_2 856d369b, states 32-33) is
  context, checked against the hypothesis scope. Report docs/referee/R-P-N5-BONLY3.md.
- C. Byte tests the Lead routes: P-N5-SPLIT fixes + L-1 (L-NEW 69) against LS-1..LS-8 and SP-1/SP-2 (R-P-N5-SPLIT.md §C); CHECKER items.

### 3. docs/GAPS.md rows relevant to me (trunk 8ba1b23b)
- REFEREE owns no row. Row the N5 packets feed into: G-N5-TIME (line 11; owner «L-NEW (L-LIT T22; referees later)»; open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D20 (index: active; DECISIONS.md line 423):
   > We have reset the weekly usage, so we can again work faster no?

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s31; this restart 80 behind): stale local branch. Check: fetch, ff-only, `git branch --show-current` and
  `git rev-parse HEAD origin/claude/referee` equal before any push.sh (done above).
- Trap (s28): wrong times from memory. Check: `D=$(date -u ...)` pasted into the text in the same command (this file's time came that way).
