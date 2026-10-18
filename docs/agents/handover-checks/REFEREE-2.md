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

## successor 2 (2026-10-18T22:48Z by date -u; Opus 5.5 under D12/L33)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch was STALE again (94dde7b, 2227 behind origin). After
  `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = 6be9dd7.
- `git rev-list --left-right --count origin/claude/referee-2...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 128 behind
  (trunk c2b1848). I then merged trunk with a merge commit (e3ccfe7): now 1 ahead, 0 behind; this file's commit adds one more.

### 2. Open work and next step of each
- Nothing in flight. Last done: R2-N5-ESC (CONFIRMED, docs/referee-2/R2-N5-ESC.md, 8197777).
- Routed next (Lead brief, after GO): packet P-N5T, docs/new/G-N5-TERM-reading.md at trunk 812ecba (Lemma A, Lemma B,
  Theorem with potential (Ω, φ)). Next step: read N5-ssi-global.md "Exact pseudocode" + S1-S5, open VJ00 myself, check every
  cited lemma, test whether the argument needs VJ00 Lemma 5.8's direction "Improve(σ) ≠ σ ⇒ σ not maximum", brute-force
  Lemma B on small games from the reading's text. Output docs/referee-2/R2-N5T.md.
- Held from predecessors (start none unasked): G-F1, (NSTEAL), (CTX⁺), (FALL), G-S5-6 = (ACYC), K5''/Up(Str) dispute.

### 3. docs/GAPS.md rows relevant to my packet (trunk c2b1848)
- G-N5-TERM | major | L-NEW (L-COMP checks runs) | open | N5 SSI-GLOBAL terminates (gauntlet step 4, correctness). SPEC sentence
  "each iteration strictly improves σ or τ in Ξ" FALSE as written (Odd switch closing a cycle changes τ with Ξτ unchanged);
  lexicographic repair proposed, not proved; DATA: no repeated (σ, τ) state in any run. Running-time bound also open.
- G-N1-LB | minor | L-NEW | open (not routed; N1 kill theorem form). Not my packet; listed because it is the other L-NEW row.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D12 (index: active; Lead reading L33 active):
   > WE can run referees on opus too temperoraly
   (L33: until the Fable reset 2026-10-21 21:00Z; every signature labelled "(Opus 5.5, D12)".)
2. D1 (index: active):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (index: active; Lead reading L35 active):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   (It created L-NEW, whose N5 I referee; L35 (3) keeps the gauntlet and D1's "wrong until it passes" for it.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap: the container's local branch is stale at every handover (1562 behind last time, 2227 this time); working from it would
  read old GAPS/NOW and stale packets. Check: `git rev-parse HEAD origin/claude/referee-2` equal before any work (done above).
- Second trap (R2-N5-ESC): a one-player optimum "τ̄" can have ties; an escape claim must hold for every admissible tie-break,
  so I treat τ̄(v) as the SET of optimal choices and report #optimal at each step.
