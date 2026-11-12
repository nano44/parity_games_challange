# L-FORMAL handover check (successor 3; written 2026-11-12T20:05Z (date -u); session_01V5yGRX3V51LguQp6WMvAgj; predecessor session_01V5yGRaQYgCY9vD9mnoWrPb (successor 2, stopped by the Fable weekly limit about 19:38Z))
Every answer is measured from the repository or from a command run in this container (commands named), not recalled. Nothing of the work
list starts before the Lead's «go».

### 0. Trap check, clock, build (run from 19:59Z by date -u)
- Trap check: `git fetch --unshallow origin` (no-op), `git fetch origin claude/l-formal claude/vibrant-johnson-nxvvxo`, `git checkout
  claude/l-formal` (the local branch was 31 commits behind: stale), `git merge --ff-only origin/claude/l-formal` → fast-forward f74d38a4 →
  6ed90b71. `git branch --show-current` = claude/l-formal. `git rev-parse HEAD origin/claude/l-formal` = 6ed90b713f5815789852acb7a183c8fa5d6b3ecd
  twice. Working tree clean.
- Clock: `date -u` «Thu Nov 12 19:59:53 UTC 2026» and, in the same command, raw.githubusercontent.com «date: Thu, 12 Nov 2026 19:59:53 GMT».
  Skew 0 s at 1 s resolution.
- Build: elan was missing; installed with the README's two commands (Lean 4.35.0, commit eb6cafb7…, Lake 5.0.0-src+eb6cafb). Then in
  lean/lemmas as one tracked background task: `lake exe cache get`; `rm -rf .lake/build && lake build`; `lake env lean Axioms.lean`.
  Result (20:01:19Z to 20:03:34Z): cache exit 0; «Build completed successfully (3189 jobs).», build exit 0, 0 lines with «warning:»;
  `lake env lean Axioms.lean` exit 0: 61 lines for the 61 `#print axioms` commands, 60 with [propext, Classical.choice, Quot.sound], 1 with
  [propext, Quot.sound], none outside the allowed three. `grep -rnw --include=*.lean -e sorry -e admit -e axiom -e native_decide .
  --exclude-dir=.lake` prints nothing (exit 1). Job count and theorem count equal successor 2's figures for e14f5508 (3189 jobs, 61 theorems).

### 1. Branch, head, distance to trunk
- Branch claude/l-formal, head 6ed90b713f5815789852acb7a183c8fa5d6b3ecd (commit date 2026-11-12T18:57:50Z; the no-ff merge of trunk),
  equal to origin.
- Trunk origin/claude/vibrant-johnson-nxvvxo = 7fa6aff4aa04054fe063abaa57889591883db014 (commit date 2026-11-12T17:10:52Z, the Lead's CI
  job lean-lemmas). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = «12 0»: 12 ahead, 0 behind.
  Merge-base = 7fa6aff4 (trunk head). The 12 ahead: 8cee97ea, 9dde1527, 4b376da4, 9fc1a0c4, 91a29b88, 027b1d65, 3880f474, f74d38a4,
  8fb3dd6c, a1f02bee, e14f5508, 6ed90b71 (the lane's own commits and the merge).
- NOT on origin (successor 2's last 30 minutes, lost with its container): PGLemmas/GenomeImpStatement.lean, PGLemmas/GenomeImp.lean (RF-A,
  built 19:08Z: 3191 jobs, 69 theorems), a refactor of GenomeLevel.lean, the INDEX / README rows of the Lead's 19:00Z rulings and the
  notebook rewrite of 18:59Z-19:08Z. Seen in successor 2's transcript (list_events on session_01V5yGRaQYgCY9vD9mnoWrPb, tool results
  «?? lean/lemmas/PGLemmas/GenomeImp.lean», «Build completed successfully (3191 jobs)», «axiom lines: 69 of 69»). The origin notebook's
  resume block is the 18:43Z one.

### 2. Open work and the next step of each (the brief's order; STATEMENT FIRST for every new `…Statement`)
1. CI run of lean-lemmas (workflow verify.yml) on 6ed90b71: not yet read. Next: GitHub Actions list for branch claude/l-formal, report run
   id and result; if red, fix the cause in lean/ only.
2. INDEX rows of the Lead's 19:00Z rulings (verbatim, from the brief and the Lead's message in successor 2's transcript): on `tiny_run`
   «witness by existence (optCounter_exists), not by computation; Lead ruling 19:00Z»; on the SHARP-route citations «per the Lead (R235
   not opened by L-FORMAL)». Next: edit lean/lemmas/INDEX.md (and README where the same citation stands), in the first commit.
3. RF-A (redo; Statements ACCEPTED by the Lead 19:05Z and 19:13Z): IdealImpRun (IdealCycRun with `howard` replaced by improve + moves),
   NonStallCountStatement, ImpK1, ImpL2, ImpL3, ImpL5, ImpNonStallStatement (≤ 2·M·(N + 2·M) lagging non-stall steps per b ≤ T),
   ImpK5NewStatement (every mover, moved or not), IdealCycRun.toImp, IdealImpRun.toPre. Next: first try to recover the exact Statement
   text from successor 2's transcript (its Write / Edit tool calls on GenomeImpStatement.lean, via list_events); if not recoverable,
   re-enter from the Lead's quoted renderings, and send the text to the Lead (no re-diff unless a word changes). Then the route:
   IdealPreRun (frozen, legal, opt, F1 pointwise) carrying k1 / l2 / l3 / l5 once, both runs projecting to it.
4. Then what the Lead routes: box 212's RF-B in Lean (when L-NEW 74 states it), Γ3 in Lean (definitions first).

### 3. GAPS rows
None. L-FORMAL owns no row of docs/GAPS.md (trunk 7fa6aff4 = my merge-base; open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME).
The lane's work sits under G-N5-TIME (owner «L-NEW (L-LIT T22; referees later)», open), which stays OPEN whatever Lean checks here: the
theorems are about IDEAL-CYC (and RF-A: any improvement rule) on Γ(G) only, «Lean-checked (lane)» until CHECKER and the CI job pass them.

### 4. Rulings, verbatim (docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md, both at 6ed90b71 = trunk's copies)
- D18 (DECISIONS.md l. 333; index l. 32: active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open
  problems.»
- D1 (DECISIONS.md l. 7; index l. 5: active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
  claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- D21 (DECISIONS.md l. 452; index l. 46: active), relayed text: «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is
  fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2
  days.» Lead reading L51 (index l. 47): maximum effort until 2026-11-14 10:05Z. This session runs on Opus 5.5 (Fable weekly limit, L53).

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: proofs that exist only on disk die with the session. Successor 2 finished RF-A at 19:08Z but could not commit while push.sh of
  6ed90b71 ran (rule: never commit while a push runs); the Fable weekly limit stopped it about 19:38Z and the container went with it:
  GenomeImp*.lean are lost.
- Check now: (a) before starting a push, commit everything that compiles (batch commits so no proof waits for a push); (b) while a push
  runs, keep each finished proof file's full text in this session's transcript (cat it after the build), so
  a successor can recover it with list_events; (c) at every pause `git status --short` must show nothing under lean/ that is not either
  committed or echoed. Plus the earlier trap (stale local branch, 31 behind here): fetch + `--ff-only` + `rev-parse` equality, done above.
