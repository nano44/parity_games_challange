# L-FORMAL handover check (successor 2; written 2026-11-12T17:19Z (date -u); session_01V5yGRaQYgCY9vD9mnoWrPb; predecessor session_01V5yGRZm5AyrczAEMySsfpN)
Every answer is measured from the repository or from a command run in this container (commands named), not recalled. Nothing of §2 starts
before the Lead's «go».

### 0. Trap check, clock, build (run 17:10Z to 17:16Z by date -u)
- Trap check: `git fetch --unshallow origin` (the clone was not shallow: `git rev-parse --is-shallow-repository` = false), `git fetch origin
  claude/l-formal claude/vibrant-johnson-nxvvxo`, `git checkout claude/l-formal`, `git merge --ff-only origin/claude/l-formal` («Already up
  to date.»). `git branch --show-current` = claude/l-formal. HEAD = origin/claude/l-formal = f74d38a4508963ce5c9ebbf30d4f4054ac984139
  (`git rev-parse`; `git ls-remote origin claude/l-formal` at 17:16Z prints the same SHA). `git status`: working tree clean.
- Clock. A Date header of github.com itself could not be read: `curl` to github.com gets HTTP 403 from the session proxy, and git's
  smart-HTTP answers from github.com carry no Date header (GIT_TRACE_CURL shows X-Github-Request-Id, Content-Type, … only). Measured
  instead: (a) raw.githubusercontent.com (HTTP 200) «date: Thu, 12 Nov 2026 17:11:36 GMT» against `date -u` 17:11:36Z in the same command,
  and the same second from release-assets.githubusercontent.com and objects.githubusercontent.com: skew 0 s at 1 s resolution; (b) the last
  field of github.com's X-Github-Request-Id read as hex epoch seconds (my reading of that field): 6AF5F346 = 17:11:34Z against `date -u`
  17:11:36Z. Skew: at most 2 s.
- Build. elan was missing; installed with the two commands of lean/lemmas/README.md («Lean (version 4.35.0, x86_64-unknown-linux-gnu,
  commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release)», «Lake version 5.0.0-src+eb6cafb»). Then in lean/lemmas, as one tracked
  background task (17:12:52Z to 17:14:40Z, output redirected to a file, exit codes echoed): `lake exe cache get` exit 0; `rm -rf
  .lake/build && lake build` exit 0, «Build completed successfully (3179 jobs).», 0 lines with «warning:» and 0 with «error» in the log;
  `lake env lean Axioms.lean` exit 0: 46 lines for the 46 `#print axioms` commands of Axioms.lean, 45 with [propext, Classical.choice,
  Quot.sound], 1 with [propext, Quot.sound], none outside the allowed three. `grep -rnw --include=*.lean -e sorry -e admit -e axiom -e
  native_decide . --exclude-dir=.lake` prints nothing. Job count and theorem count equal the predecessor's (3179 jobs, 46 theorems).

### 1. Branch, head, distance to trunk
- Branch claude/l-formal, head f74d38a4508963ce5c9ebbf30d4f4054ac984139 (commit date 2026-11-12T15:56:22Z), equal to origin.
- Trunk origin/claude/vibrant-johnson-nxvvxo = 68c8d29339d5945efe6878a7e4cfc9d6a1611d48 (commit date 2026-11-12T15:06:33Z; `git ls-remote`
  at 17:16Z). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = «8 25»: 8 ahead, 25 behind. Merge-base
  071392490dcea36bfa952288aa6170d45fadf874. The 8 commits ahead are the lane's own: 8cee97ea, 9dde1527, 4b376da4, 9fc1a0c4, 91a29b88,
  027b1d65, 3880f474, f74d38a4.
- Consequence: docs/NOW.md, docs/DECISIONS-INDEX.md, docs/DECISIONS.md and docs/GAPS.md in my working tree are the merge-base's copies. I
  read the trunk copies (`git show origin/claude/vibrant-johnson-nxvvxo:<path>`); every line number below is the trunk copy's at 68c8d293.
- Read-only inputs opened: claude/l-new 311bbf81faa525eda9c09ad15d0b0d170a2c25e9, docs/new/N5-LEVEL-box208.md (566 lines; §0-§4, Addenda
  A and B read); docs/red/P-N5-REALIZE.md §2-§3.1 (sha1 067f06b6c679…) and docs/new/P-N5-XICYC.md §1-§3 (sha1 149e2414be65…), each
  byte-identical on my branch, on trunk and on claude/l-new. Located, not yet read: claude/referee 890daf41
  docs/referee/R-box208-preread.md (REFEREE 32; G-P6 and its repair in §5.2, required change PR-1).
- Read in the lane's tree: notes/L-FORMAL.md (HANDOVER 15:51Z and «Resume point»), lean/lemmas/README.md, INDEX.md, PGLemmas/Defs.lean,
  Statements6.lean, Genome.lean, GenomeClass.lean, LevelCountStatement.lean, PlateauStatement.lean, `IsState` in GenomePlay.lean. The
  proof files are not yet read line by line.

### 2. Open work and the next step of each (the brief's order; STATEMENT FIRST for every new `…Statement`)
- (0) ENGINE COMPARISON of `IdealCycRun` (asked by the Lead 15:50Z; not started; nothing in lean/lemmas/check/ mirrors a run). Next step:
  a new tool lean/lemmas/check/idealcheck.py that evaluates exactly the five fields of `Genome.IdealCycRun` (Genome.lean l. 235-247:
  frozen, legal, opt, howard, moves), with `Stopped` at T and `FromStart` at 0, on the states (σ_t, σ̄_t) of the fleet's IDEAL-CYC run
  (experiments/new/box191/idealcyc.py `build` / `run`, valuation engine experiments/si/si.py), on the 11 JSON genomes of
  experiments/new/box191/inst (cyc_d3 … cyc_d8, cyc2_d7, cyc2_d8, DEAD_SEG2P_d4_N8, _d7_N14, _d9_N18). Values and order by
  check/crosscheck.py's transcription of Defs.lean, not by si.py's keys. Control: break `HowardAt` (for example «a mover moves to a
  ⊴-smallest gate») and require the howard counter to fire. One limit to settle with the Lead at «go»: `opt` quantifies over all Odd
  strategies (2^(M+1) of them), so on a genome it cannot be enumerated; planned as every play (simple lasso) from every vertex where that
  enumeration ends under a stated cap, and every single-vertex deviation of σ̄_t (the instance (K4)'s proof uses) on every genome, with
  the unit and the scope printed. Until the tool exists, `k1` / `k5` are about `IdealCycRun` as defined (the brief's sentence).
- (0′) STATEMENT ClassOrder (asked by the Lead 15:50Z; not written). Next step: a statement-only file with `ClassOrderStatement`, sent to
  the Lead before any proof is committed. Form I will propose (my reading, to be diffed against box 208 §1 «It is a strict total order on
  the classes that occur»): under `G.WF`, `clsLt` is irreflexive, transitive and total (clsLt c c′ ∨ c = c′ ∨ clsLt c′ c), together
  with an order-embedding key of classes into a lex type (first rew of Λ, then a weight of E) with clsLt c c′ ↔ key c < key c′: the
  LinearOrder that `level_count` needs. Expected to hold for ALL pairs (Λ, E), not only the occurring ones, because `pr` is injective
  under WF (`pr_injective`); if so the statement is stronger than the lane's sentence and I say so in the message.
- (1) (K4) (`K4Statement` accepted 15:50Z, NOT proved). Next step: the predecessor's plan, notebook «NEXT (1)»: LOC-GATE in ⊴ form from
  `OptCounter` at `Function.update τ g w` (`underProgAt_of_opt`, then the converse of `underProgAt_of_le`, valid by `lam_ne_gate`), then
  `cls_step`, `IsState.gate` and `k2`. Theorem `k4 : G.K4Statement`, with its Axioms.lean line and INDEX row.
- (2) NO-TIE (R123). Not needed for (K4) in ⊴ form (predecessor's note). Next step: decide when (L3) and (P4) are stated whether any
  step needs Ω(e_g) ≠ Ω(β_g); prove it (notebook «NEXT (2)») only then.
- (3) LEVEL (L2), (L3), (L5) on the genome (box 208 §3). Next step: `L2Statement`, `L3Statement`, `L5Statement` over an `IdealCycRun` with
  a reference state b, phrased with `FrontAt` on the key of (0′), sent to the Lead first. (L4) is not needed for ALL-TCYC.
- (4) PLATEAU's (P1)-(P4), (P6) on the genome (Addendum A2, with REFEREE 32's G-P6 repair = Addendum B1 (1)(a): answer with σ̄_s), then
  the assembly. Next step: read R-box208-preread.md §5.2; state (P1)-(P4), (P6) as Statements for the Lead; then `plateau` with Ch := the
  movers of Y (bound ≤ N), `level_count` with |M| ≤ 2M, F = N + 2M, and the quiet tail by `plateau` with Y := all vertices (Addendum B1
  (5)), no QUIET-N premise. The final `…Statement` (T ≤ P(N + 2M + 6) + N, P = 2M(N + 2M), for every `G.WF` and every `IdealCycRun`) goes
  to the Lead for the diff against box 208 A0 and TARGET.md BEFORE its proof. It is not a TARGET.md statement: genome games only, a step
  count of a model (TARGET.md §4; box 208's scope line).
- Housekeeping found while reading (lane files, first commit after «go»): README.md l. 117 («No theorem about the genome is in the tree»)
  and INDEX.md l. 56 («Not formalized: … the class facts (K1)-(K5)») are stale: `k1`, `k2`, `k3`, `k5` are in the rows above them.

### 3. GAPS rows
None. L-FORMAL owns no row of docs/GAPS.md. Open rows at trunk 68c8d293 (l. 6-11): GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME. The
lane's work sits under G-N5-TIME (owner «L-NEW (L-LIT T22; referees later)», status open), which stays OPEN whatever Lean checks here: box
208 is a CANDIDATE about IDEAL-CYC on Γ(G) only («not Γ3, not N5′-xi, not M4; G-N5-TIME stays OPEN»), and a Lean theorem of this lane is
«Lean-checked (lane)» until CHECKER and the CI job lean-lemmas have passed it.

### 4. Rulings, verbatim (trunk docs/DECISIONS.md; status from trunk docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l. 333; index l. 32: active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
  needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open
  problems.»
- D1 (DECISIONS.md l. 7; index l. 5: active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
  claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- D21 (DECISIONS.md l. 452; index l. 46: active), relayed text: «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is
  fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2
  days.» Lead reading L51 (index l. 47: active), items (1) and (2) in part: «maximum effort until 2026-11-14 10:05Z, drawing on the owner's
  usage resets (general and Fable 5.2)» and «Both are verification / literature roles, not attack lanes (D1).»
- How they bind this lane (my reading): D1: every Lean theorem here is lane-level, box 208 stays a CANDIDATE, a result only through
  CHECKER and CI. D18: proved / conjecture / open kept apart in README and INDEX. D21 / L51: full effort inside the window; L-FORMAL
  verifies, it does not attack; if a turn fails on a usage limit I resume from the notebook.

### 5. One trap that bit this lane, and the check that now prevents it
- The trap: Genome.lean's `WF` as first sent (15:32Z) allowed a genome with no option. Lead 15:36Z, required change (h), as the notebook quotes it (notes/L-FORMAL.md l. 18-20): «WF must require
  deg x ≥ 1 for every mover. … With M = 0 you get bmax = 0, top = 4 < K1's 5, and §3.1's rank facts … fail.» Neither the build (a
  definition type-checks either way) nor the lane's data check (check/genomecheck.py runs on real genomes, all with M ≥ 1) could see it;
  the Lead's diff did. Fixed by `WF.one_le_N` (used by `prio_K1_lt_top` only).
- The check: STATEMENT FIRST. Every new definition or `…Statement` goes to the Lead for a diff against the lane text before its proof
  lands in a commit; a statement is a `def … : Prop` and its theorem has exactly that type; after any change to Genome.lean,
  check/genomecheck.py is re-run (GEN_CTRL=1 must fire) and the tree is rebuilt from `rm -rf .lake/build`. My addition: each Statement
  message lists the degenerate instances I tried against it (N = 1, one option, every wt = none, T = 0, a = b).
- Process trap named in the brief, checked at start (§0): a detached, shallow or stale checkout makes the push fail. And: the gate takes
  40 to 60 minutes, so `pgrep -f "bash scripts/push.sh"` before every push, one push at a time, no commit while it runs.
