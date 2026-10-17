# Handover check: REFEREE-2

## successor (2026-10-17T14:58Z; Opus 5.5 under D12/L33; predecessor session_01SdxPAhFBFXe4ZCwR1WfPL4 parked 13:22Z at ~580k)
Every answer measured from the repository at the time of writing (commands given), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. The container's local branch was STALE (94dde7b, 1562 behind); after
  `git fetch origin claude/referee-2` and `git merge --ff-only origin/claude/referee-2`: HEAD = origin/claude/referee-2 = c7634a7.
- `git rev-list --left-right --count origin/claude/referee-2...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 58 behind
  (trunk d811288); c7634a7 is an ancestor of trunk, so all REFEREE-2 work is on trunk. This file's commit adds one ahead.

### 2. Open work and next step of each
- Nothing in flight (predecessor parked 13:22Z after R2-P6 + comparison §5, c7634a7). Next step: wait for the Lead's next packet.
- Open items held from the predecessor's reports (notebook "Open gaps I hold"; I start none unasked):
  G-F1 (F_R definition must count non-rising e*-at-R transitions, R2-P6 (a)); (CTX⁺) (per-phase count of first-difference
  contexts and Dom inputs); (FALL) (Σ_R F_R polynomial; trunk LEAD-STATE d811288 reports a FALL-V kill, re-run pending);
  G-S5-6 = (ACYC) (R2-STEP5); the P3 K5''/Dep(Str) vs Up(Str) reading (routed by the Lead).
  Next step of each: re-derive against dtl.cpp @ 8fbf0a7 when the Lead routes the L-ALG proof or counterexample.
- Before the first probe: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored) and re-apply
  docs/referee-2/R2-P4/dtl_probe4_full.patch (cumulative instrumented dtl.cpp).

### 3. docs/GAPS.md rows relevant to me (trunk d811288)
- GAP-A blocker, L-ALG, open: referee-signed reduction GAP-A ⇐ (CTX⁺) ∧ (FALL) (RESULTS R5, R7-R9); both DATA only.
- GAP-C blocker, L-ALG, open: KT frame given (ACYC) (RESULTS R4, signed R2-STEP5); single-search progress statements dead (DE13, DE15).
- G-S5-6 major, L-ALG, open: (ACYC). DATA only (32,026 REFEREE-2 runs, 0 failures).
- G-DOM major: closed on trunk (absorbed into (CTX⁺), RESULTS R9 (b)-(c)). Note: GAPS.md on claude/referee-2 (c7634a7)
  still shows it open; trunk is the truth.
- Closed rows I (predecessor) signed: G-FDL, G-Bthr, G-K5 (K5''), G-STR (R2-P5), G-DOM.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D12 (index: active; Lead reading L33 active), docs/DECISIONS.md:220:
   > WE can run referees on opus too temperoraly
   (L33: until the Fable reset 2026-10-21 21:00Z; every signature labelled "(Opus 5.5, D12)".)
2. D1 (index: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
3. D1 (index: active), docs/DECISIONS.md:6:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (R2-P3/R2-P4): set-level arguments about ψ-plays and extraction missed strategy-level effects (old tangle vertices keep
  their str; extraction reads str, dtl.cpp 268, 171, 89), which is how G-STR and the K5' (iii') REJECT arose.
  Check: for every vertex a proof step touches, name the dtl.cpp line that wrote str before signing; re-read every cited line myself.
- Also this session: the local branch was 1562 commits stale; check `git rev-parse HEAD origin/claude/referee-2` equal before any work.
