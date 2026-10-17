# Handover check: REFEREE

## successor (2026-10-17T12:45Z; Opus 5.5 under D12/L33; predecessor session_01W3Z4peJy1bngBmMVdJ1f6K parked at ~550k)
Every answer measured from the repository at the time of writing (commands given), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. The container's local branch was STALE (5ed56c5, 1517 behind); after `git fetch origin claude/referee`
  and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = ca03021.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...origin/claude/referee` -> 13 behind, 0 ahead
  (trunk 44af920); ca03021 is an ancestor of trunk, so all REFEREE work is on trunk. This file's commit adds one ahead.

### 2. Open work and next step of each
- Nothing in flight (predecessor parked 12:38Z after R-P5). Next step: wait for the Lead's next packet.
- Open items I hold from the predecessor's reports (each waits on a packet; I do not start them unasked):
  (ACYC) (R-STEP5); G-e1/G-DOM (R-P4 §22e: first difference in a Dom tattr); (CTX), (DIRTY)/(FALL) (R-P4/R-P5 §22e);
  (SPP) (R-PROVED2, (SPP) => bound only); the (α) shape (R-P3, SKETCH); GAP-A beyond round r (R-P3).
  Next step of each: re-derive against dtl.cpp @ 8fbf0a7 when the Lead routes the L-ALG proof or a REFEREE-2 comparison.
- Before the first packet: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored).

### 3. docs/GAPS.md rows relevant to me (trunk 44af920)
- GAP-A blocker, L-ALG, open: (SPP) DATA only; phases <= D+2 and (SPP) => O(n^10(m+n^2)) signed (R-PROVED2).
- GAP-C blocker, L-ALG, open: KT frame given (ACYC) (RESULTS R4, signed R-STEP5); single-search progress statements dead (DE13, DE15).
- G-S5-6 major, L-ALG, open: (ACYC). DATA only.
- G-DOM major, L-ALG, open: (e* ∉ Dom) = my R-P4 G-e1. DATA only.
- G-STR major, closed (trunk d8a4e19): STR-DET signed by both referees (my R-P5). Note: GAPS.md on claude/referee (ca03021)
  still shows G-STR open; trunk is the truth.
- Closed rows I signed: G-FDL, G-Bthr, G-K5 (K5'' with Dep(Str)).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D12 (index: active; Lead reading L33 active):
   > WE can run referees on opus too temperoraly
   (L33: until the Fable reset 2026-10-21 21:00Z; two independent referees; every signature labelled "(Opus 5.5, D12)".)
2. D1 (index: active):
   > Never downgrade the referee to save money.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D1 (index: active):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (notebook Lessons; R-P3 (a) and G-STR): set-level arguments about what a ψ-play or an extraction does missed strategy-level
  effects; R-P3's G-a1/G-a2 step was wrong (old tangle vertices keep their region strategy, dtl.cpp 169) and was REJECTED after
  REFEREE-2's configuration. Check: for every vertex a proof step touches, name the line that wrote str (89 / 171 / 73) before
  signing; and no signature before re-reading the cited code lines myself.
- Also this session: the local branch was 1517 commits stale; check `git rev-parse HEAD origin/claude/referee` equal before any work.
