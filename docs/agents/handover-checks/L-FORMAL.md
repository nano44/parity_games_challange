# L-FORMAL handover check (successor 5; written 2026-11-13T07:40Z (date -u); session_01V5yGRY9bh61TXMsQVPeAh9 (Opus 5.5, high); predecessor successor 4, session_01V5yGRWV98usJz6buk8GaGb, handover 462360fd)
Every answer is measured from the repository or from a command run in this container (commands named), not recalled. Nothing of the work
list starts before the Lead's «go».

### 0. Trap check, clock, build
- Trap check (07:30Z): `git fetch --unshallow origin` (no-op), `git fetch origin claude/l-formal claude/vibrant-johnson-nxvvxo`, `git checkout
  claude/l-formal`: the local branch was 43 commits behind origin (stale); `git merge --ff-only origin/claude/l-formal` → fast-forward
  f74d38a4 → 462360fd. `git branch --show-current` = claude/l-formal; `git rev-parse HEAD origin/claude/l-formal` =
  462360fdd99ff3135ce5918a15f0998d881c4d9d twice. Working tree clean.
- Clock: `date -u` «Fri Nov 13 07:30:43 UTC 2026», raw.githubusercontent.com «date: Fri, 13 Nov 2026 07:30:44 GMT», then `date -u`
  «07:30:44». Skew 0 s at 1 s resolution.
- Build: elan was missing; installed with the README's commands (Lean 4.35.0). In lean/lemmas, one tracked background task:
  `lake exe cache get`; `rm -rf .lake/build && lake build`; `lake env lean Axioms.lean`. Result (07:31:30Z to 07:34:50Z): cache exit 0;
  «Build completed successfully (3199 jobs).», build exit 0, no Lean «warning:» line (one elan self-update notice only); `lake env lean
  Axioms.lean` exit 0: 74 lines for the 74 `#print axioms` commands, 72 with [propext, Classical.choice, Quot.sound], PG.one_cross
  [propext, Quot.sound], PG.Genome.lift_start [propext]; none outside the allowed three. `grep -rnw --include=*.lean -e sorry -e admit -e
  axiom -e native_decide . --exclude-dir=.lake` prints nothing (exit 1). Equals successor 4's figures for 9176725a (3199 jobs, 74).
- Scratch proof: `sha1sum lean/lemmas/scratch/SpecFuel.lean.txt` = 05a99b90c2d75f7052059cfdd9aa3f325bbba32b, 1,261 lines (equals the handover).
- CI (Actions API, 07:35Z): run 43379405264 on 9176725a: job lean-lemmas 131733397674 SUCCESS (06:32:35Z-06:35:00Z); job verify still
  in progress. Run 43386105859 on 462360fd: both jobs in progress at 07:35Z.

### 1. Branch, head, distance to trunk
- Branch claude/l-formal, head 462360fdd99ff3135ce5918a15f0998d881c4d9d (commit date 2026-11-13T06:32:37Z, «L-FORMAL successor 4: handover
  (Lead 05:03Z): notebook resume block … and the scratch fuel proof lean/lemmas/scratch/SpecFuel.lean.txt …»), equal to origin.
- Trunk origin/claude/vibrant-johnson-nxvvxo = 6cec46a5ce724d55eb5ad910a9a30aedad716781 (commit date 2026-11-13T05:40:12Z, «Lead: L56 …»).
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = «24 103»: 24 ahead, 103 behind. Merge-base 7fa6aff4
  (unchanged). The 103 behind are other lanes' and the Lead's trunk commits; lean/ is not touched by them, so no merge is needed for
  lean/ (I merge trunk only if the Lead asks and no push runs).

### 2. Open work and the next step of each (brief order; STATEMENT FIRST)
1. FuelStatement (Lead 05:03Z, verbatim: «Successor 5 states FuelStatement to me and proves it. Do not start FuelStatement in a commit
   yourself.»). State: Statement text drafted by successor 4 (notebook resume block: SGame.WF, StratWF, FuelEvalStatement,
   FuelIterStatement, FuelRunStatement through startPair; header note «only successors < n, owners ≤ 1 (and owner sizes) are used»);
   proof in lean/lemmas/scratch/SpecFuel.lean.txt (not imported, not built by CI, no INDEX / MANIFEST row). Next: after «go», re-check
   the scratch proof against the current tree, send the Lead the Statement text (the Statement file as it would be committed) BEFORE any
   commit; after the Lead's diff: PGLemmas/SpecFuelStatement.lean + PGLemmas/SpecFuel.lean, import in PGLemmas.lean, three `#print
   axioms` lines in Axioms.lean, INDEX row, MANIFEST row, clean build (no sorry; axioms within the three), commit, push, send SHA + CI run.
2. NoFault (Lead 02:06Z (4) / 03:43Z: si.py's exception cases never occur on WF games; VJ00 §6-sized), Statement first. Order relative
   to item 3 as the Lead routes (brief: KeyRuleStatement next).
3. (i) KeyRuleStatement restricted to one-player arenas (the S4a case: owner-0 vertices of H with τ fixed), Statement first; the Lean side
   of box 213's KEY-TAU (i) (L-NEW, CANDIDATE). Next: read docs/new/N5-KEYWIN-box213.md (on origin/claude/l-new, not on my branch or
   trunk), quote its paper form, then draft. (ii) the bridge Eng.evaluate → Defs.val / OptCounter is deferred (Lead 02:06Z).
4. Duty: CHECKER items on the Lean rows (C143 notes N-1..N-7, C145 notes N-8..N-11 on claude/checker; optional N-8 clause).

### 3. GAPS rows
None. L-FORMAL owns no row of docs/GAPS.md: open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME, the same ids, owners and status in
my copy and in trunk 6cec46a5 (my copy differs from trunk only in line 11's text, G-N5-TIME, updated by the Lead since). The lane's work
sits under G-N5-TIME (owner «L-NEW (L-LIT T22; referees later)», open), which stays OPEN whatever Lean checks here: FuelStatement says
only that the Lean transcription of SPEC never runs out of fuel on well-formed games; it says nothing about N5's running time. Every
theorem is «Lean-checked (lane)» until CHECKER and the CI job lean-lemmas (L54) pass it.

### 4. Rulings, verbatim (docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l. 333; index l. 32: active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open
  problems.»
- D1 (DECISIONS.md l. 7; index l. 5: active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
  claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- D21 (DECISIONS.md l. 452; index l. 46: active), relayed text: «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is
  fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2
  days.» Lead readings: L51 (index l. 47) maximum effort until 2026-11-14 10:05Z; L53 (index l. 50) Fable weekly limit, successors on
  Opus 5.5 high (this session); L54 (index l. 51) the CI job lean-lemmas on the exact commit is the build of record; L56 (trunk index
  l. 53, not yet on my branch) verify's self-check skip only for docs/agents/-only changes, so my pushes run in full.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap: a stale local branch (43 commits behind origin here; 37 for successor 4); and earlier, a container restart killed push.sh of
  99b19401 silently while the session believed it ran. Successor 4 also twice typed a time without date -u (03:46Z sent as «04:05Z»).
- Check now: (a) fetch + `merge --ff-only` + `rev-parse HEAD origin/claude/l-formal` equality before anything (done in 0); (b) before every
  push `pgrep -f "bash scripts/push.sh"` (never two pushes), push.sh as a tracked background task with a 2-hour timeout, output
  redirected to a file and `echo exit $?` (never piped); after it or any restart, `git ls-remote origin claude/l-formal` must equal the
  local head before a SHA is reported as on origin; (c) everything that compiles is committed before a push starts, nothing is committed
  while it runs; (d) every time in a message comes from `date -u` in the same command as the send step.
