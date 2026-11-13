# L-FORMAL notebook (Lean formalization lane; branch claude/l-formal; files: lean/, this notebook)

## Resume point
- HANDOVER of SUCCESSOR 3 (session_01V5yGRX3V51LguQp6WMvAgj), written 2026-11-13T00:14Z at about 420k context. A SUCCESSOR STARTS HERE.
  STATE (all Lean-checked (lane); results only through CHECKER (C143 opened by the Lead on MANIFEST c8963698) and the CI job lean-lemmas):
  - On origin before this batch: 91f25983 (handover check), 78c32d90 (RF-A, recovered by transcript replay), c8963698 (MANIFEST +
    check/manifest.lean + check/mkmanifest.py). CI lean-lemmas green on 6ed90b71 (run 43292277834) and 78c32d90 (run 43314716149).
  - This batch (one push of three commits): 99b19401 (Gamma3.lean definitions, accepted 22:22Z; check/gamma3check.py DATA;
    Gamma3Statement.lean), 5ea6cd22 (pad, gamma3_card, gamma3_old), and the commit carrying this block (Gamma3LiftStatement.lean,
    accepted 00:00Z; Gamma3Lift.lean: pad_value = R117 PAD (c), lift_start; README / INDEX / Axioms 74 lines). If its push failed,
    re-run scripts/push.sh as a tracked task (never two pushes).
  - Lean tree at this block: Axioms.lean 74 theorems, all within propext, Classical.choice, Quot.sound; clean build 00:07:44Z-00:13:53Z: 3197 jobs, 0 warnings, 74/74 axiom lines within the allowed three.
  NEXT (Lead 23:53Z, verbatim): «(b) Then SPEC itself, toward N5. Write the Lean DEFINITIONS of N5's step as SPEC S1-S5 states it
  (S4a's improving set A(v), the root-first key, S4b, the S4c fallback) on a general game first, then specialised to Γ3. Ground it in
  a machine comparison against experiments/si n5v (spec mode), state by state, on the frozen sets, with a firing control. Definitions
  only, then my diff, before any theorem. This is the step that would let Lean say anything about N5 itself, which is the target.
  L-NEW 74's box 212/213 has reduced O1′ to «SPEC's key rule on class-frozen one-player windows», so the key rule is the object to
  formalize. (c) C143's rulings, whenever CHECKER sends them, preempt.»
  Pointers for (b) (read, not yet transcribed): SPEC = docs/new/N5-ssi-global.md l. 24-127 (S1-S5 with FIX 1-4 and «Four further SPEC
  points» l. 94-127: FIX 2's explicit-stack DFS and exploration order, FIX 4's «first strict maximum» = smallest index); engine =
  experiments/new/box21/n5x.py `step` (78 lines) via experiments/new/box190/n5v.py mode "spec", valuations experiments/si/si.py
  `Engine` (evaluate, improving, extend, key; the tie rules are in si.py l. 152-195). The key rule is the hard part: Even's S4a choice
  is si.py's Engine on the DUAL game of the arena H (Even restricted to A(v) = {σ(v)} ∪ Iσ(v), Odd fixed to τ). Plan: Defs-level
  `ImprovingSet`, `Arena`, then the choice rule as a DEFINITION over the explicit DFS (FIX 2) with the longest-path rule (FIX 4), then a
  check tool in the genomecheck pattern that evaluates Lean's step on the frozen sets (experiments/new/box*/inst) against n5v.
  Proposals of mine, not routed: S3 in Lean (then S3-START: S3 = std3 start, R117).
  TRAPS met by successor 3: (i) derived `DecidableEq Vertex3` vs the classical instance inside `pset` / `setLt` / `ext` / `plen`:
  never `rw` with a lemma that synthesizes the instance; use `simp only [Finset.mem_symmDiff]` / `[Finset.mem_insert]` (they unify),
  `mem_pset`, and generic-V lemmas (`plen_eq_iff` in Gamma3Lift.lean); (ii) `open scoped symmDiff` for `∆`; (iii) a container restart
  kills push.sh (origin unchanged, files survive): re-check `git ls-remote` and re-run; (iv) RECOVERY of lost Bash-made work: parse
  list_events(kinds=["assistant"]) pages (saved by the harness as files) and replay the tool_use inputs in a scratch worktree (the
  method of successor 3's first block below).
- SUCCESSOR 3 (session_01V5yGRX3V51LguQp6WMvAgj, Opus 5.5, started 2026-11-12T19:59Z; THIS block is the resume point; successor 2's
  blocks below it are history). Successor 2 was stopped by the Fable weekly limit about 19:38Z; its RF-A files were never committed.
  - Handover check 91f25983 (docs/agents/handover-checks/L-FORMAL.md). Lead 20:08Z: «Handover check 91f25983 received, and it matches my
    state … «go» once 91f25983 is on origin with push exit 0.» «Your recovery plan is approved: take the RF-A files' text from successor
    2's transcript … Recovered proofs still have to compile from a clean build before they are committed.» «Your trap note is adopted:
    commit everything that compiles before a push starts. Order: (1) CI run, (2) INDEX rows, (3) RF-A.»
  - (1) CI: workflow verify.yml run 43292277834 on 6ed90b71: job lean-lemmas 131441320129 SUCCESS («Build completed successfully (3189
    jobs).», «LEAN LEMMAS PASS», 19:38:57Z-19:41:18Z); job verify (the gate) was still in progress at 20:07Z.
  - RECOVERY METHOD (reusable): list_events(session_01V5yGRaQYgCY9vD9mnoWrPb, kinds=["assistant"]) pages saved as files by the harness;
    a Python parser took every tool_use input verbatim; successor 2 edited only through Bash heredocs, so its ten commands from 18:59Z
    to 19:09Z were REPLAYED in order (paths rewritten) in a scratch worktree at 6ed90b71. Every build output matched its log: 3161,
    3190, 3171 jobs, the same omega failure at GenomeImp.lean:93:64 and its fix, 3173, then a clean 3191 jobs, 69/69 axiom lines (68
    with the three, 1 with propext + Quot.sound), 9,409 lines in 53 files. Notebook edits re-run with their original NOW times.
  - Recovered: GenomeImpStatement.lean (sha1 f5255b58a05b94716b9acee4a66126133e4a9e8a as recovered; c7a6ecd10b87de4384a6b3b47aed50fcc5c9d4df
    after one comment fix: a literal «\n» in the header became a newline), GenomeImp.lean (503d99d5a2ca8630c89728022e924e110bfd3a5c),
    the GenomeLevel.lean refactor (IdealPreRun), PGLemmas.lean, Axioms.lean, INDEX.md (both 19:00Z wordings, the RF-A rows), README.md.
    Statement text vs what the Lead accepted: the 19:01:59Z file plus `ImpK5NewStatement` (identical to the 19:09Z message text); the
    only other differences are header comments. Lead 20:12Z: «No Statement word changed, so no new diff is needed. The replay method
    goes into the notebook. Go ahead as planned: one commit with a clean build, push, then send me the SHA.»
  - 91f25983 on origin: push.sh exit 0 at 20:58:49Z, VERIFY PASS (git ls-remote = 91f25983).
  - RF-A COMMIT (this commit): the recovered files copied into the lane tree; clean build 20:59:10Z-21:00:11Z: «Build completed
    successfully (3191 jobs).», 0 warnings, Axioms.lean 69/69 (68 with the three, 1 with propext + Quot.sound), no sorry / admit /
    axiom / native_decide, 9,411 lines in 53 files (+2 vs 19:07Z: successor 2's header edit at 19:09Z and my comment fix).
  - NEXT (Lead 20:12Z, verbatim): «After your RF-A commit is on origin and its lean-lemmas CI job is green, send me a one-page MANIFEST
    in lean/lemmas/MANIFEST.md, committed: (a) every theorem to be offered, with Statement name, file, line and commit; (b) the
    definition files those Statements depend on (Defs.lean, Genome.lean, GenomeClass.lean, …), each with its sha1 and the Lead acceptance
    it carries (time, deviations); (c) the exact build and axiom commands and their outputs.» PREPARED (not committed, in the scratch
    worktree; re-create if lost): lean/lemmas/check/manifest.lean, a `#eval` over the compiled environment: for every name in
    Axioms.lean its module, line and the head of its type after the binders (the Statement); and the PG definitions those types
    depend on, transitively through definition bodies (not through theorems), grouped by module (26 modules at RF-A). Run from
    lean/lemmas: `lake env lean check/manifest.lean`. Per-file acceptance times of Statements.lean..Statements7.lean are recorded in
    the lane files only as the set 11:49Z-14:54Z (Statements 11:44Z sent, Statements2 12:26Z sent; 12:29Z / 13:13Z for the next).
  - 78c32d90 (RF-A) on origin: push.sh exit 0 at 21:53:46Z, VERIFY PASS. Lead 21:03Z on per-file acceptance times (verbatim, in
    MANIFEST (b)): «per-file acceptance times not recorded by the Lead; the acceptance set is 11:49Z, 12:29Z, 13:13Z, 13:58Z, 14:54Z
    (2026-11-12)». «Commit MANIFEST after the lean-lemmas CI run on 78c32d90 is green, then send me both SHAs and the CI run id.»
  - CI on 78c32d90: verify.yml run 43314716149, job lean-lemmas 131519592230 SUCCESS (21:53:58Z-21:56:31Z; «Build completed
    successfully (3191 jobs).», «LEAN LEMMAS PASS»).
  - MANIFEST COMMIT (this commit): lean/lemmas/MANIFEST.md (generated 21:54Z), check/manifest.lean (the `#eval` generator),
    check/mkmanifest.py (the formatter; inputs: the generator's output, the build log, the Axioms.lean output). To regenerate: from
    lean/lemmas, `lake env lean check/manifest.lean > m.out`, then `python3 check/mkmanifest.py m.out build.log axioms.out <time> >
    MANIFEST.md` (build.log: a `rm -rf .lake/build && lake build` log with start/end/exit lines; axioms.out: `lake env lean Axioms.lean`).
  - c8963698 (MANIFEST) on origin: push.sh exit 0 at 22:50:31Z, VERIFY PASS. Lead 22:00Z: Weights finding and the eight helper
    modules go into CHECKER item C143 as their own lines; «Next for you: Γ3 in Lean, definitions first … RF-B waits until L-NEW 74
    states it on paper.»
  - Γ3 (this commit): PGLemmas/Gamma3.lean, DEFINITIONS, ACCEPTED by the Lead 22:22Z «with deviations (a)-(e) as you named them»
    (his required sentence on the per-pad priorities is in the header); check/gamma3check.py with outputs check/out/gamma3check*.out
    (r104: 25 genomes, 5,834 vertices, 7 counters 0; free, seeds 1-3: all 0, transcription match 1; controls fire).
    PGLemmas/Gamma3Statement.lean: `PadStatement`, `Gamma3OldStatement`, `Gamma3CardStatement`, STATEMENTS ONLY, PROPOSED (Lead
    22:22Z: «Proposed theorems (i) Γ inside Γ3, (ii) the vertex count, (iii) PAD: approved, Statements first. PAD comes first among
    them»). NEXT: the Lead's diff of those three; then prove PAD (plan: a cycle through any non-core vertex passes a gate's face β or e
    (Ω ≥ 3 by hypothesis) or c_W (top3 ≥ 4); core cycles pass K0, K1 or K3, or are K2's loop (Ω 3); c_X has no in-edge but its loop, so
    lam = c_X only for v = c_X with plen 0; p' orders by Ω first), then (i), (ii).
  - Lead 22:56Z: PadStatement, Gamma3OldStatement, Gamma3CardStatement ACCEPTED (PAD «STRONGER in two ways … Both are fine»; «Record
    (iii) clearly: PAD (c), the value transport, is not stated»). «Prove PAD first, then the other two. Commit when the build is clean
    and push in a batch.» CHECKER item C143 opens on MANIFEST c8963698 (the Lead).
  - Container restart about 23:00-23:40Z killed push.sh of 99b19401 (origin stayed at c8963698); the filesystem survived. PROOF COMMIT
    (this commit, pushed together with 99b19401): PGLemmas/Gamma3Pad.lean (`pad`), PGLemmas/Gamma3Basic.lean (`gamma3_card`,
    `gamma3_old`, `card_vertex`, `card_vertex3`, `idx3_injective`, …); Axioms.lean 72 lines.
  - NEXT (my proposals, not yet routed): PAD (c) / the strategy transport Γ ↔ Γ3 (definitions first: `lift3 σ` on Γ3 from a state of
    Γ, then «val in Γ3 of old v = val in Γ with padded length»); S3-START (needs SPEC's S3 in Lean: a definition diff); then what the
    Lead routes (C143's rulings on the Lean rows; box 212's RF-B when L-NEW 74 states it).
- SUCCESSOR 2 (session_01V5yGRaQYgCY9vD9mnoWrPb, started 2026-11-12T17:10Z; this block is the resume point, the blocks below it are the
  predecessor's and stay as history). Handover check 8fb3dd6c is on origin (push.sh exit 0 at 18:00:32Z). Lead 17:22Z: all five answers
  match, «go». Lead's rulings of 17:22Z, verbatim. Item (0): «(a) Mirror frozen / legal / howard / moves EXACTLY as defined, along
  idealcyc.py + si.py runs on the 11 genomes, with a HowardAt-breaking control that fires. You are right that r187/ideal.traj is the IDEAL
  step and the wrong engine. (b) For opt: at every state, check Odd's reply against si.py's computed optimal counterstrategy, value by
  value. Also check that no single-vertex deviation of σ̄_t improves Odd's valuation at any vertex (unit (state, vertex, deviation)), and
  add a control that makes one gate non-optimal and must fire. Label it: «optimality checked as local optimality of a one-player
  counterstrategy plus agreement with si.py's optimum; full enumeration not done». Lasso enumeration under a cap is optional and only
  where it is cheap. That is DATA about the transcription. It does not replace the Lean proofs.» Item (0′): «if ClassOrder holds for ALL
  pairs under WF, state the stronger form and name the deviation («stronger than box 208 §1's sentence»), as you plan. Send the Statement
  before its proof lands in a commit.» Stale sentences: «fix README l. 117 and INDEX l. 56 in your first commit, as you propose.»
- STATE 2026-11-12T18:59Z (date -u). THE BRIEF'S WORK LIST (0)-(4) IS DONE AND COMMITTED. Nothing of this lane is uncommitted except this notebook
  block. Commits of successor 2 on claude/l-formal:
  - 8fb3dd6c handover check (on origin 18:00Z);
  - a1f02bee engine comparison check/idealcheck.py, `k4` + `OptCounter.le_succ` (GenomeK4.lean), the statement files
    GenomeOrderStatement.lean and GenomeLevelStatement.lean (on origin 18:56Z, VERIFY PASS);
  - e14f5508 the proofs: GenomeOrder.lean `class_order`; GenomeLevel.lean `l2`, `l3`, `l5`; GenomePlateau.lean
    `IdealCycRun.window_le`, `IdealCycRun.gate_const`, `gate_of_cls_eq_some`, `gate_of_cls_eq_none`, `plateau_g`, `quiet`;
    GenomeAllTCyc.lean `all_tcyc_sharp`, `all_tcyc`; GenomeRunStatement.lean + GenomeRun.lean `run_exists`; GenomeExample.lean
    `tiny_wf`, `tiny_run`; GenomeK4.lean `optCounter_of_local`; check/idealcheck.py with wffail; check/levelcheck.py; README, INDEX,
    Axioms.lean (61 theorems);
  - 6ed90b71 merge of trunk 7fa6aff4 with --no-ff (the Lead's instruction: the CI job lean-lemmas is in trunk's
    .github/workflows/verify.yml); no lane file changed by it. push.sh for 6ed90b71 started 18:58Z: CHECK `git ls-remote origin
    claude/l-formal` FIRST; if it does not show 6ed90b71 (or a later commit of this lane), the push did not land: re-run
    scripts/push.sh.
  Build of e14f5508's lean/lemmas: `rm -rf .lake/build && lake build` → «Build completed successfully (3189 jobs).», 0 warnings;
  Axioms.lean 61 theorems (60 with the three allowed axioms, 1 with [propext, Quot.sound]); no sorry / admit / axiom /
  native_decide; 8,957 lines in 51 files.
  WHAT LEAN NOW CHECKS (lane-level; statements accepted by the Lead): for every genome with `G.WF` and every `IdealCycRun σ τ T`:
  T ≤ 2M(N + 2M)(N + 1) + N ≤ P(N + 2M + 6) + N, P = 2M(N + 2M) (box 208 A0); a stopping run from the genome's start exists
  (`run_exists`); the genome `tiny` has a run with T = 1. SCOPE, never to be dropped from a report: a step bound for the MODEL
  IDEAL-CYC on the genome games Γ(G); not N5, not N5′-xi, not Γ3, not TARGET.md; G-N5-TIME stays OPEN; box 208 is a CANDIDATE in its
  lane; a row is a result only through CHECKER and the CI job; no data run comes near the bound.
  DATA: check/idealcheck.py (13 counters 0 on the 11 genomes of experiments/new/box191/inst; controls how / opt / wf fire on all 11);
  check/levelcheck.py (8 counters 0; 1,473 pairs (b, t) with a lag; (α) 747, (β) 726; 309 stall steps; longest interval of stalls 9
  on cyc2_d7 (N = 14) and 8 = N on DEAD_SEG2P_d4_N8; control fires with 1,470 on l2fail, l3fail, l5fail). Outputs in check/out/.
  How the proofs go, for whoever edits them: the file headers of GenomeLevel.lean, GenomePlateau.lean, GenomeAllTCyc.lean,
  GenomeRun.lean, GenomeExample.lean (each lists its lemmas and the argument). The one place where the route leaves box 208's text:
  `gate_of_cls_eq_none` (both faces of a level-0 gate of class (c_W, ∅): Ω(e_g) = (c_W, ∅, 1), plen(β_g) ≥ 2, c_W even, LOC-GATE gives
  σ̄(g) = β_g); the Lead routed it to L-NEW 73.
- LEAD'S VERDICTS (18:20Z, 18:30Z, 18:43Z; quoted in lean/lemmas/README.md): «ACCEPT ALL NINE» (ClassOrderStatement + clsKey, L2, L3, L5,
  PlateauG, Quiet, AllTCyc, AllTCycSharp with deviations (i)-(vii); RunExistsStatement with the deviation «existence is not stated in
  the fleet texts; added so that the theorems about IdealCycRun are not empty; uniqueness not claimed»; `tiny_wf` / `tiny_run` accepted
  as the non-vacuity witness; `optCounter_of_local` logged as the bridge for devfail). «Then I open the CHECKER item for the Lean rows,
  which go through the CI job lean-lemmas».
- LEAD 19:00Z (verbatim): «Witness: your flag is fair. I accept tiny_run as is. Non-vacuity is an existence property: `optCounter_exists`
  plus a derived Howard step is a proof, and «decide or rfl» was my over-specification. No explicit decidable witness is wanted.
  Record in INDEX: «witness by existence (optCounter_exists), not by computation; Lead ruling 19:00Z».» «INDEX's citation of L-RED
  66's SHARP route on my word is fine as written. Say «per the Lead (R235 not opened by L-FORMAL)».» (Both done in INDEX.md.)
  «NEXT, one item, statement-first: RF-A, for L-NEW's BOX 212. - Define IdealImpRun: IdealCycRun with `howard` replaced by «each step
  moves a non-empty set of movers, each to a gate strictly ⊴-better under the current values; every other mover keeps its gate». -
  For each of (K1)-(K5), L2, L3, L5, PlateauG, Quiet, LevelCount's use, list which proofs use `howard`. Then state the rule-free
  versions for IdealImpRun of those that do not need it, plus «at most P = 2M(N + 2M) non-stall steps for every reference state b».
  - Send me the Statements and the list of where `howard` is genuinely needed (K5 surely; PlateauG presumably) before proving
  anything. That is the Lean side of L-NEW 74's RF-A. Γ3 in Lean comes later.» «After 6ed90b71 lands and the lean-lemmas CI job is
  green on it, I open a CHECKER item for the Lean rows. Send me the CI run id when you see it.»
- LEAD 19:05Z (verbatim): «RF-A Statements: ACCEPT, diffed against L-NEW 73's BOX 212 RF-A … - IdealImpRun: improve + moves render
  «each moving mover goes to a strictly better gate; at least one moves; the others keep». frozen / legal / opt are unchanged.
  Correct. - NonStallCount, ImpK1, ImpL2, ImpL3, ImpL5, ImpNonStall: accepted with your readings (a)-(d). … IdealCycRun.toImp is a
  good bridge; add it. - YES to the rule-free remnant of (K5), as one more Statement, ImpK5New: «for the NEW gate y′ = σ_(t+1)(x),
  class_t(y′) ≤ class_(t+1)(x)». Box 212's RF-B («no mover of Y moves to a gate outside Y before the step that ends the interval»)
  will want it. Send me its text with the proofs. - Your «where howard is used» list is logged verbatim as DATA for L-NEW 74's box
  212 … Context: you are near 400k. Prove if room remains; otherwise commit the notebook with the plan and write a handover at about
  450k. A successor continues from it.»
- HANDOVER 2026-11-12T19:08Z (successor 2 parks after the next push; a successor starts here).
  RF-A IS PROVED (uncommitted when this was written; it goes into the commit that follows the push of 6ed90b71):
  - PGLemmas/GenomeImpStatement.lean: `IdealImpRun`, `NonStallCountStatement`, `ImpK1Statement`, `ImpL2Statement`, `ImpL3Statement`,
    `ImpL5Statement`, `ImpNonStallStatement` (accepted 19:05Z) and `ImpK5NewStatement` (the Lead asked for it in those words; its
    accepted 19:13Z).
  - PGLemmas/GenomeImp.lean: `non_stall_count`, `IdealImpRun.toPre`, `IdealCycRun.toImp`, `imp_k1`, `imp_l2`, `imp_l3`, `imp_l5`,
    `imp_non_stall`, `imp_k5_new`.
  - PGLemmas/GenomeLevel.lean was refactored: `IdealPreRun` (frozen, legal, opt, mono = F1) with `isState`, `k2`, `k1`, `bOnly`,
    `ck_step`, `ck_mono`, `cls_const`; `l2_pre`, `l3_pre`, `l5_pre` hold the proofs; `l2`, `l3`, `l5` and the `IdealCycRun.*` lemmas
    are one-line instances through `IdealCycRun.toPre`. No accepted Statement or theorem name changed.
  - Build: `rm -rf .lake/build && lake build` → «Build completed successfully (3191 jobs).», 0 warnings; Axioms.lean 69 theorems (68
    with the three allowed axioms, 1 with [propext, Quot.sound]); no sorry / admit / axiom / native_decide; 9,409 lines in 53 files.
  WHAT IS OPEN, IN THIS ORDER:
  (a) `git ls-remote origin claude/l-formal`: it must show the commit that follows 6ed90b71 (message «RF-A …»). If it shows 6ed90b71
      or older, the last push did not land: check `git status`, commit what is uncommitted by explicit path, run scripts/push.sh as a
      tracked task (2-hour timeout, output to a file, echo the exit code), and report.
  (b) The CI job lean-lemmas on the branch head: read the run with the GitHub tools (ToolSearch «select:mcp__github__actions_list,
      mcp__github__actions_get»; repository nano44/parity_games_challange, branch claude/l-formal) and send the Lead the run id with
      PASS / FAIL. He opens the CHECKER item for the Lean rows after it is green.
  (c) DONE: the Lead 19:13Z (verbatim): «ImpK5NewStatement: ACCEPT. It renders «for the NEW gate y′ = σ_(t+1)(x), class_t(y′) ≤
      class_(t+1)(x)». Stating it for every mover, moved or not, is a harmless generalisation; record it as the named point you
      wrote. RF-A is logged as proved (lane), with your scope sentence verbatim: «bounds the NON-stall steps … under any improvement
      rule (at most 2M(N + 2M) per reference state b); nothing about the number of stalls, so no bound on the run length; genome
      games only, not TARGET.md, G-N5-TIME OPEN». Also logged: no engine DATA under a non-Howard rule. L-NEW 74's box 212 will supply
      that. Commit, push, send the SHA and the CI run id, then park. Your successor's queue: (1) the lean-lemmas CI run on your head;
      (2) anything CHECKER rules on the Lean rows; (3) box 212's RF-B in Lean, when L-NEW 74 states it; (4) Γ3 in Lean,
      definitions-first.»
  (d) Next item, when the Lead routes it: «Γ3 in Lean comes later» (box 209: LEVEL3 / PLATEAU3 / T3-ALL need Γ3(G) of P-N5-REACH §3
      as a new definition, STATEMENT FIRST, with a genomecheck-style DATA comparison against experiments/new/box189/gamma3.py
      build(G, pads) before any proof); box 212's RF-B («no mover of Y moves to a gate outside Y before the step that ends the
      interval») is announced as wanting `imp_k5_new`.
- RULES THAT BIT OR ALMOST BIT (successor 2): never commit while push.sh runs (the gate takes 41 minutes; the stop hook asks for a
  commit anyway: do not); a merge of trunk changes experiments/ under a running gate: merge only when no push runs; the Lead's
  messages can queue for 25 minutes: call ReadNotifications when waiting for a verdict; proofs of a new `…Statement` stay out of
  commits until the Lead's ACCEPT, so they live only in the container: ask for the verdict early and say so.
- TRAPS in Lean met by successor 2: (i) `if_pos` / `if_neg` / `dif_pos` / `push_neg` are deprecated in this Mathlib (warnings): use
  `ite_eq_left` / `ite_eq_right` / `dite_eq_left` / `push Not`. (ii) A module that PGLemmas.lean does not import is built by `lake
  build PGLemmas.<Module>`. (iii) `exact absurd (f … trivial) h` cannot infer an implicit vertex; write `exact (h (f … trivial)).elim`.
  (iv) Numerals in `Fin (tiny.deg x)` need the ascription `(1 : Fin 2)`. (v) Nothing in lean/ is built by the gate (no lean/lakefile.*
  at lean/ root); CI's separate job lean-lemmas builds lean/lemmas.
- 2026-11-12T14:46Z (date -u): STATE. Everything proved so far is «Lean-checked (lane)»: the Lead ACCEPTED every statement (rulings 11:49Z,
  12:29Z, 13:13Z, 13:58Z, 14:54Z, quoted in lean/lemmas/README.md «Status and reading rules») EXCEPT `LevelCountStatement`, which is
  PROPOSED (my addition; verdict open). Rows become RESULTS only through CHECKER + the Lead's CI job «lean-lemmas» (Lead 13:52Z: «elan, lake exe
  cache get, lake build, the sorry / admit grep, and the Axioms.lean allowed-list check»). lean/lemmas/INDEX.md is the table.
- 027b1d655542f8acd8fb751720bfedfd09dd3fbc is on origin (push.sh exit 0 at 15:12Z, VERIFY PASS; git ls-remote).
- The harness compacted my context at 14:31Z (after the handover commit 027b1d65). Lead 14:41Z: «continue». No successor has started.
  Lead 14:54Z: «Park at ~450k by your own count.» A successor reads this section first.
- NEXT TARGET (Lead 14:54Z, verbatim): «the genome and IDEAL-CYC definitions in Lean, aiming at the bridge that box 208's packet needs:
  «an IDEAL-CYC plateau satisfies PlateauStatement's hypotheses (P1)-(P4), (P6)» and «LEVEL's class facts (K1)-(K5) on IDEAL-CYC».
  Statement-first, as before. Start with R104's [DEF] (the genome and Γ(G)) and R118 (a) (IDEAL-CYC), quoted, and send the definitions
  for a diff before any proof. If that turns out to be too large for one session, say so after the definitions, with an estimate.»
- HANDOVER 2026-11-12T15:51Z (my context is near the 450k mark again; a successor starts here). Lead's target (14:54Z, quoted below):
  the genome bridge. STATE: (K1), (K2), (K3), (K5) of box 208 §2 and the landed premises CN2, LOC-K2 (first half), B-ONLY, E-DOM are
  PROVED in Lean with no premise. LEAD'S RULINGS (read 15:54Z): LevelCountStatement «ACCEPT. Keep it in the tree.» (15:16Z, three
  deviation lines, now in README). Genome.lean «ACCEPT with one required change» (15:36Z): «REQUIRED CHANGE (h): WF must require deg x
  ≥ 1 for every mover. … With M = 0 you get bmax = 0, top = 4 < K1's 5, and §3.1's rank facts … fail. Add the field, or state where
  M ≥ 1 is used.» DONE 15:55Z: deg x ≥ 1 already holds by the type of `start`; I added `WF.one_le_N` (so M ≥ 1) and
  `prio_K1_lt_top`, its only use. GenomeClass.lean «ACCEPT» (15:50Z); «One statement is MISSING, and the bridge needs it: … state
  ClassOrder before the assembly: on the classes that occur at IsState maps with OptCounter (cycle nodes β, K1, K2, c_X, c_W by
  B-ONLY), clsLt is irreflexive, transitive and total. Alternatively, give an order-embedding of occurring classes into a lex type.»
  NOT DONE. «IdealCycRun needs one engine comparison before you lean on it: on the 11 pinned genomes, a mirror of frozen / legal /
  howard / moves holds along ideal.traj, and a control that breaks HowardAt fires.» NOT DONE. «Route: PREMISE-FREE APPROVED. … Keep
  statement-first: every new Statement goes to me before its proof lands in a commit.» If a definition changes, re-run genomecheck.py
  and rebuild.
  - Files of the genome layer (all build; last full check 15:55Z, the tree with `WF.one_le_N`: `rm -rf .lake/build && lake build` →
    «Build completed successfully (3179 jobs)», 0 warnings; Axioms.lean 46 theorems within the allowed three; no sorry / admit / axiom;
    7,113 lines in 41 files; genomecheck re-run on 2 genomes after the change: 110 vertices, all counters 0):
    Genome.lean (definitions), GenomeBasic.lean, GenomePlay.lean, GenomeBOnly.lean, GenomeClass.lean (class definitions and
    K1Statement..K5Statement), GenomeK3.lean (`k3`), GenomeK2.lean (`k2`), GenomeK15.lean (`k1`, `k5`, `IdealCycRun.f1`).
  - NEXT, in this order (the first two are the Lead's asks of 15:50Z; the rest is my plan):
    (0) the engine comparison of `IdealCycRun`: a Python mirror of frozen / legal / howard / moves (and of `OptCounter` for σ̄) along
        the fleet engine's IDEAL-CYC run (experiments/new/box191/idealcyc.py with experiments/si/si.py's Engine; check/crosscheck.py
        already mirrors `val`, `Val.lt`, `OptCounter` against si.py) on the 11 genomes of experiments/new/box191/inst, with a control
        that breaks HowardAt; put it in lean/lemmas/check/.
    (0′) the statement ClassOrder (or the order-embedding cls ↦ (rew Λ, wt E) ∈ ℤ ×ₗ ℤ), sent to the Lead for the diff before its proof.
    (1) (K4): `K4Statement` is stated, NOT proved. Plan: LOC-GATE in ⊴ form, for an Odd vertex g and w ∈ E g: Val.le (val s (s g))
        (val s w), s = pair V0 σ τ. Get `UnderProgAt pr s g w` from TwoPlayer.lean `underProgAt_of_opt` with hopt := `OptCounter`.2
        applied to `Function.update τ g w` at the vertex g (pair V0 σ (update τ g w) = update (pair V0 σ τ) g w since g ∉ V0); then the
        converse of Mono.lean `underProgAt_of_le` (valid because lam s g ≠ g: `lam_ne_gate`), with Weights.lean `Val.le_iff_lex`,
        `wt_ext`, `sl_ext`. Then: cls (gate o) = cls (s (gate o)) by `cls_step`; s (gate o) is a face (`IsState.gate`); for the other
        face use `k2` (faces are not core). NO-TIE is not needed for (K4) in this form.
    (2) NO-TIE (R123): Ω(e_g) ≠ Ω(β_g). Plan: if wt g = none, Λ(e_g) = c_W ≠ Λ(β_g) (`b_only` at β_g). Else e_g ∈ Π(e_g)
        (`cls_eface`); if e_g ∉ Π(β_g) the sets differ; if e_g ∈ Π(β_g) the play of β_g passes g then e_g (the only predecessor of e_g
        is g), so len(β_g) > len(e_g).
    (3) LEVEL on the genome: (L2), (L3), (L5) of box 208 §3 from (K1)-(K5) (the stall lemma (L4) is not needed for ALL-TCYC); to use
        `level_count` the classes need a LinearOrder: map a class to the key (rew Λ, wt E) in ℤ ×ₗ ℤ (Weights.lean `setLt_iff_wt_lt`,
        `wt_injective`) and show clsLt ⇔ < on keys.
    (4) PLATEAU's (P1)-(P4), (P6) on a plateau of IDEAL-CYC (box 208 A2), then `plateau` with Ch := the movers of Y; then ALL-TCYC
        by `level_count`; (C4) either by R126 QUIET-N as a premise or by `plateau` with Y := all vertices.
  - Traps met in the genome layer: (i) decidable-equality instances: `ext`, `setLt` and other generic definitions carry the classical
    instance, statements about `Finset G.Vertex` carry the derived `instDecidableEqVertex`; never close such goals by `rfl`, go through
    `Finset.mem_insert` / `Finset.mem_symmDiff` with `simp only`, or `ext u`. (ii) `omega` does not instantiate ∀-hypotheses: give it
    `six_le_bprio o`, `bprio_lt_eprio o o'` for the options at hand. (iii) `rcases v with x | o | o | o | _ | _ | _ | _ | _ | _` is
    the vertex case split (mover, gate, beta, eface, cX, cW, K0, K1, K2, K3); `simp only [prio]` / `[idx]` / `[start0]` unfold one
    constructor. (iv) `(val pr s v).top`, `.set` are `lam pr s v`, `pset pr s v` by rfl; `nxt V0 σ τ t` is `pair V0 (σ t) (τ t)` by
    rfl, `exact` sees through both.
- GENOME TARGET, state 15:36Z (nothing of it committed yet; the push of 3880f474 runs since 15:13Z):
  - PGLemmas/Genome.lean (256 lines, sha1 707974398221…): DEFINITIONS ONLY, sent to the Lead 15:32Z for the diff with deviations (a)-(g)
    (β-id not a field; `none` for «none» and X; WF separate; e_g's edge follows wt; start0 one map with τ_0 on Odd's vertices; in
    `IdealCycRun` τ t is ANY optimal counterstrategy, the first state any mover state, `FromStart` and `Stopped` separate; pmax spells
    out «max Ω so far»). Verdict open.
  - DATA (tool lean/lemmas/check/genomecheck.py; unit: vertex; Lean's `idx`, `prio`, `isOdd`, `E`, `start0`, `pr` evaluated by
    `lake env lean` against stab.py build(G, 0, kgad=True, esc=True) and si.py's p′): experiments/new/box191/inst, 11 genomes, 1,018
    vertices: all 7 counters 0; experiments/new/box202/inst, the 21 genomes with at most 400 vertices, 4,916 vertices: all 0 (14.6 min);
    control GEN_CTRL=1, 2 genomes, 110 vertices: priofail 56, succfail 56, startfail 78, prfail 56. NOT run: the 32 larger corpus genomes.
  - PGLemmas/GenomeBasic.lean (no premise, compiles): `idx_injective`, `pr_injective`, `pr_lt_iff` (under WF), `even_pr`, priority bands
    (`bprio_lt_eprio`, `eprio_lt_top`, `eprio_even`, `top_even`, …), `isE`, `e_dom` (R121 E-DOM from the priorities).
  - PGLemmas/GenomePlay.lean (no premise, compiles, 15:38Z): `IsState` (a successor map of IDEAL-CYC(G)), `IdealCycRun.isState`,
    `cn2` (R123 CN2), `lam_ne_mover`, `lam_ne_gate`, `loc_k2` (R123 LOC-K2: τ(K2) = K1 for every `OptCounter`), `lam_K0..K3`, `lam_cX`,
    `lam_cW`, `IdealCycRun.k2`.
  - ESTIMATE sent to the Lead 15:32Z: full premise-free bridge 3,000-5,000 lines, 3-4 sessions. PROPOSED STAGE A (about 2,500 lines):
    box 208's own logic (§1 classes, (K1)-(K5), LEVEL (L1)-(L3), (L5), PLATEAU (P1)-(P4), (P6), ALL-TCYC via `level_count` and
    `plateau`) CONDITIONAL on the landed statements it quotes (R123 CN2, B-ONLY, NO-TIE; LOC-GATE, LOC-K2, DOM, E-DOM, QUIET-N where
    not proved directly). STAGE B: discharge those premises. The Lead's choice is open.
  - Proof ideas noted for the cheap premises (mine): CN2: a cycle node w of priority < 2 is a mover or a gate, its successor (a gate,
    resp. a face) is on the same cycle with a larger priority. LOC-K2: if τ(K2) = K2 then val(K2) = (K2, ∅, 0), and K2 → K1 gives
    (K1, ∅, 1), strictly smaller since pr K1 > pr K2 and both are odd: against `OptCounter`. B-ONLY: compare with Odd's all-β strategy
    (its cycle nodes are β's, K1 or c_X), then use optimality on rewards. Class order: use the key (rew Λ, wt E) in ℤ ×ₗ ℤ
    (Weights.lean `setLt_iff_wt_lt`, `wt_injective`) to get a LinearOrder for `level_count`.
- BOX 208 TARGET (Lead 13:13Z / 13:52Z: «box 208's abstract core in Lean. claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md: §10 … first,
  then Addendum A's PLATEAU in its one-player form. Send the statements for a diff first.»): BOTH DONE IN LEAN.
  - §10 Statement ABS: `abs_statement : AbsStatement V` (PGLemmas/AbsProof.lean, 14:40Z). Lead's diff of `AbsStatement` (13:58Z): «(i)
    `G.tgt ∉ G.Max`: ACCEPT.» «(ii) ℕ weights, ℕ∞ distances: ACCEPT.» «(iii) Clause (2) for every step t < T: ACCEPT PROVISIONALLY. If
    the proof needs §10's «every step before the last», revert to that wording and tell me. Do not prove a stronger statement than the
    proof supports.» «(iv) Reference b = the last state T: ACCEPT» «(v) NoZeroCycle on all edges: ACCEPT.» The proof gives (iii) as
    stated (every t < T), so nothing was reverted.
    How the proof goes (for whoever edits it): `SPGame.Run` bundles the hypotheses. (K1′) `Run.mono`; (K5′) `Run.k5`; (A)
    `Run.exists_rise` (a step that changes s changes it at a Max z whose old edge was not best, so d(z) rises: every t < T lags
    somewhere); `SPGame.Front` = lagging with the lowest lagging value; (F) `front_zero_edge` (an edge v → u out of the front with
    w + d_t(u) ≤ d_t(v) and u lagging has w = 0 and u in the front; uses that a lagging value is finite); `Run.front_min` (a Min
    vertex of the front has such an edge: a best edge to a non-lagging vertex would pin it by Bellman at T), `Run.front_max_lag`,
    `Run.front_max_stall` (uses (K5′) at y = s_T z); `SPGame.no_closed` (choose! a map along weight-0 edges, pigeonhole on iterates,
    `Relation.TransGen`); (L4) `Run.front_rises`, (L3) `Run.front_level`; `lagMin` (a `Finset.inf`), `frontSet`; (L1) `Run.phi_step`,
    `Run.phi_lt`; (C) t ↦ (lagMin t, |frontSet t| − 1) is injective from range T into `levelVals` × range n.
  - Addendum A2 PLATEAU, abstract one-player form: `PlateauStatement` (PGLemmas/PlateauStatement.lean) and
    `plateau : PlateauStatement V` (PGLemmas/Plateau.lean, 14:44Z). A set Y closed under every state of a window a..b; in Y only Ch
    moves; the successors of Ch lie in Y; Howard at Ch; no cycle node of a vertex of Y changes; every step changes s at a vertex of Ch
    ⇒ b − a ≤ |Ch|. Proof: the run s′ := s on Y, self-loop outside Y, with edges E on Ch and the one successor elsewhere, is a
    one-player Howard run with every cycle node fixed (`val_congr`, `lam_congr`, `lam_of_fixed`), and `lam_gap_oneplayer_noM` bounds
    it. MY READING (not the lane's text): applied to a plateau [u, v] with Ch := the movers of Y this gives v − u ≤ (movers of Y) ≤ N,
    where A2 (P7) has N + 2M + 5 via BR-SEG-G (a). That (P1)-(P4), (P6) hold on a plateau is genome work, NOT formalized.
    Lead 14:54Z: «PlateauStatement diff: ACCEPT, including your deviations» and «Your reading that the bound drops to |movers of Y| ≤ N
    matches L-RED 66's lane remark (R235 «second route») and REFEREE 32's (`brseg` with Mov = movers of Y). Record it as agreement of
    three, still lane-level.»
  - Box 208 §3 (L1) + §4 (C1), (C2), the counting, abstract (my addition while the push ran; PROPOSED, not asked for by the Lead):
    `LevelCountStatement` (PGLemmas/LevelCountStatement.lean: `FrontAt`, `StallAt`) and `level_count` (PGLemmas/LevelCount.lean,
    14:54Z). Classes c t v in any linear order, never falling; M ⊇ the lowest lagging classes; fronts ≤ F; at most L consecutive
    stalls ⇒ every state t with LAG_t ≠ ∅ has t − a < |M|·F·(L + 1). Proof: (L1) in two-state form (`lc_front_le`,
    `lc_front_of_eq`, no induction on the step), the fibers of t ↦ (lowest lagging class, |front|) are runs of stalls (`lc_fiber`),
    `Finset.card_le_mul_card_image`. Tight on one vertex with c t v = t (L = 0, F = 1, |M| = b). (C4) is not stated.
  - DATA for ABS (unit: step of a Howard run on a random shortest-path game; tool lean/lemmas/check/abscheck.py, a Python transcription of
    AbsStatement.lean, NOT the Lean code): seed 1, 20,000 games, n ≤ 7: 7,130 runs with T ≥ 1, 7,914 steps, longest 3; seed 2, 20,000
    games, n ≤ 12: 9,035 runs with T ≥ 1, 10,286 steps, longest 4; dfail, hypfail, boundfail, c2fail, lastfail 0 in both. Control
    ABS_CTRL=1, seed 1, 2,000 games: c2fail 1,140 of 1,140 steps (fires). Reading: the hypotheses are satisfiable with T ≥ 1, and
    clause (2) holds at the last step too.
  - Last full check of the tree with these files (14:55Z): `rm -rf .lake/build && lake build` → «Build completed successfully (3171
    jobs)», 0 warnings; `lake env lean Axioms.lean` exit 0, 35 theorems, 34 with [propext, Classical.choice, Quot.sound], 1 with
    [propext, Quot.sound]; the README's grep for sorry / admit / axiom prints nothing; 5,237 lines in PGLemmas/.
  - NOT DONE, possible next (the Lead routes): (a) the genome and IDEAL-CYC in Lean (Lead 13:13Z: «Defining the genome and IDEAL-CYC in
    Lean comes later and only if §10 goes through»); (b) DONE 14:50Z: PGLemmas/AbsExample.lean `AbsExample.hyps` (3 vertices, T = 1: every
    hypothesis of `AbsStatement` holds; `d_start`, `d_end`: d(0) goes from 1 to 3); (c) §10's last bullet (IDEAL-CYC at class level as a shortest-path game) is not formalized.
  - ℕ∞ hints that worked: split on `G.d s v = ⊤`, else `obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp h` (hk : ↑k = d); `gcongr`
    for `↑w + a ≤ ↑w + b`; `push_cast; rfl` for `↑w + ↑k = ↑(w + k)`; `zero_le` takes no explicit argument; `le_add_self`;
    `exact_mod_cast` from `↑w + ↑k ≤ ↑k` to ℕ; `ite_eq_left h` / `ite_eq_right h` (h : c / h : ¬c) are this Mathlib's names for
    if_pos / if_neg, `dite_eq_left` / `dite_eq_right` for dif_pos / dif_neg.
- Commit 027b1d65 (2026-11-12T14:30Z, after push.sh of 91a29b88 ended with exit 0) held: README.md, INDEX.md
  (Lead's wording rulings applied), PGLemmas/Statements7.lean + NoH0.lean (`BrSegGNoH0Statement`, `brsegG_noH0'`),
  PGLemmas/AbsStatement.lean, PGLemmas/Abs.lean, PGLemmas.lean, Axioms.lean, this notebook.
- Theorems (file: name : statement):
  - PGLemmas/LamGap.lean: `lam_gap_sharp : LamGapSharpStatement V`.
  - PGLemmas/Corollaries.lean: `lam_gap_oneplayer : LamGapOnePlayerStatement V`, `brseg : BrSegStatement V`, `brsegG : BrSegGStatement V`,
    and `brsegG_noH0` (BR-SEG-G (a) with H0 weakened to «every step changes σ at some Even vertex»: the checked proof uses nothing else
    of H0).
  - PGLemmas/OneCross.lean: `one_cross (α) [Preorder α] (F) : OneCrossStatement α F`; `one_cross_vj` (α = node valuations).
  - PGLemmas/Counting.lean (statements in PGLemmas/Statements2.lean, PROPOSED, not yet sent for diff when written): `two_cross`
    (box 100 §2 TWO-CROSS (i), (ii), any preorder), `lam_count` (a ⊴-non-falling sequence of node valuations changes its cycle node
    at most n − 1 times: the Λ part of DEPTH-COUNT3, the per-vertex count behind R118 (i)(b)), `howard_run` (box 101 §3 L1-POLY,
    abstract: T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch| for a Howard run with only Ch moving, given (M)); helper `steps_le_of_breaks`.
  - 2026-11-12T12:36Z: PREMISE (M) IS PROVED IN LEAN FOR ONE-PLAYER GAMES (statements in PGLemmas/Statements3.lean, PROPOSED, need the Lead's diff):
    PGLemmas/Mono.lean `val_mono : ValMonoStatement V` (if every vertex keeps its successor or moves to one of strictly larger value
    under s, then val_s ⊴ val_s′ pointwise: VJ00 Lemma 5.7 / RESULTS R15 (a) when the opponent has no choice); PGLemmas/OnePlayer.lean
    `lam_gap_oneplayer_noM` (LAM-GAP SHARP, one-player, NO premise) and `howard_run_oneplayer` (Howard with VJ valuations on a
    one-player game: T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch|, NO premise). Proof route (Weights.lean + Mono.lean): path sets → integer
    weights wt(M) = Σ ±2^pr (`setLt_iff_wt_lt`; `Nat.geomSum_lt` gives the dominance of the top vertex); keys (wt, signed length)
    compare lexicographically (`Val.le_iff_lex`); `edge_key` (one s′-edge inside a Λ-class) and `telescope` (a walk); `rew_cycle` (a
    cycle of s′ has non-negative weight, so its top beats the old Λ or is it; uses `Function.minimalPeriod` for distinct cycle
    vertices); `prefix_key` (induction on the new prefix length).
  - 2026-11-12T12:44Z: also PROVED (statements PROPOSED, need the Lead's diff): PGLemmas/DepthCount.lean `depth_count : DepthCountStatement V`
    (DEPTH-COUNT3's count of changes of depth in [0, c] with R234's fix D1: ≤ n(S_c(n) − 1) + n(n − 1)S′_c(n) for a non-falling
    sequence of values with lengths < n), `plen_lt_card` (plen < n), `depth_count_val`; PGLemmas/TCyc.lean `tcyc : TCycStatement V`
    (R118 (f) T-CYC and (i)(b), (c) without the genome: T ≤ C + R + (C + R + 1)·|Mov| and C ≤ n(n − 1), given F1).
    Proof notes: `topk pr (c+1) Π` = box 100's P_t; a set change of depth ≤ c raises wt(topk) strictly (`topk_setLt`), deeper ones
    keep topk (`topk_eq`); t ↦ (Λ_t, topk_t) is injective on such steps and misses the heaviest set; length-only steps: t ↦
    (Λ_t, Π_t, len_t or len_t − 1) is injective into n × S′_c × (n − 1).
  - 2026-11-12T12:54Z: TWO-PLAYER F1 = RESULTS R15 (a) LEMMA A IS PROVED IN LEAN (statements in PGLemmas/Statements6.lean, PROPOSED, need the
    Lead's diff): PGLemmas/TwoPlayer.lean `f1 : F1Statement V`: τ an optimal counterstrategy against σ (`OptCounter`: Friedmann §3's
    definition, pointwise ⊴-minimum over Odd's strategies), σ′ arising from σ by improvements ⇒ Ω_σ(v) ⊴ val(σ′, τ′)(v) for EVERY Odd
    strategy τ′, in particular Ω_σ ⊴ Ω_σ′. Also `brseg_opt`, `tcyc_opt` (BR-SEG and T-CYC with «σ̄_t optimal» instead of F1) and
    PGLemmas/OptExists.lean `optCounter_exists` (an optimal counterstrategy exists when every Odd vertex has a successor).
    Route: Mono.lean was refactored around `UnderProgAt pr s u w` (the three under-progress conditions on one edge) and
    `val_le_of_underProg` (VJ00 Lemma 5.5); `underProgAt_of_le` (Ξ(s u) ⊴ Ξ(w) suffices); Dual.lean `val_mono_dual` via the shift
    pr ↦ pr + 1 (`val_shift`: same values; `Val.lt_shift`: reversed order); `underProgAt_of_opt` (if switching u to w does not lower
    the value of u, the edge u → w is under-progressive: else dual (M) makes the value of u unchanged, and (P1) + strict F4′, or the
    empty path set after a cycle node, contradict); `optCounter_exists` by a pointwise-minimal valuation among finitely many strategies.
  - 2026-11-12T13:09Z: DATA (unit: vertex value / pair of values / (Odd strategy, vertex); set: random games n ≤ 8, 3 random Even strategies
    each; tool lean/lemmas/check/crosscheck.py, a Python transcription of Defs.lean, NOT the Lean code): seed 1, 2,000 games: values
    29,823 valdiff 0; pairs 171,723 orddiff 0; optchecks 127,356 optfail 0. Seed 2, 2,000 games: values 30,141 valdiff 0; pairs
    175,539 orddiff 0; optchecks 122,214 optfail 0. Control CTRL=1 (plen read one too long), seed 1, 300 games: valdiff 4,464 of
    4,464 (fires). Reading: the definitions as written denote si.py's valuation and order, and si.py's σ̄ is an `OptCounter`.
  - lean/lemmas/INDEX.md: the table lane text ↔ Lean statement ↔ Lean theorem ↔ remaining premise.
  - 2026-11-12T13:22Z: fresh `git clone --depth 1 --branch claude/l-formal` of origin (HEAD 4b376da457ddb2aed895c56f101c5a86d233f766), then
    in lean/lemmas `lake exe cache get` (exit 0), `lake build` (exit 0, «Build completed successfully (3149 jobs)», 0 warnings),
    `lake env lean Axioms.lean` (exit 0, 13 theorems, axioms ⊆ the allowed three), grep sorry / admit / axiom: nothing. 101 s in all.
  - PGLemmas/Example.lean: `Example.window_example` (4 vertices, Ch = {1}, a window 0..1: the hypotheses hold together and b − a = |Ch|).
  - PGLemmas/VJ00.lean: `vj00Le_iff` (VJ00 §4.2's order as printed = `Val.le` on play values), `val_proper` (every val is a play value).
- How the SHARP proof goes in Lean (LamGap.lean), for whoever edits it:
  - `SPath pr edge Ch ℓ v S x c` (inductive): a simple path v → … → ℓ with vertex set S, value x = value(P), c = choice vertices before ℓ.
    `SPath.count_eq`: c + [ℓ ∈ Ch] = |Ch ∩ S|, so c ≤ |Ch| and c + 1 ≤ |Ch| when ℓ ∈ Ch.
  - `ext_le_val`: inside ONE state σ, x ⊴ val(σ v) with top(x) ≠ v ∉ set(x) gives ext(v, x) ⊴ val(v) (cycle-node case by rewards, other
    case by (P1) + F4′). This one lemma serves both the fixed-vertex and the choice-vertex case of (L).
  - `lower_bound` = (L): induction on k, inside it induction on the SPath derivation; the choice-vertex case uses Howard at a + k − 1,
    then (M), then `ext_le_val` at time a + k (never ext of an old value: box 101's point).
  - `play_spath` = (U): induction on plen; `val_le_of_play` = (L) + (U) with the two count bounds.
  - `lam_gap_sharp`: Ch.card = m + 1 (else nothing moves); x ∈ Ch switches at a + m + 1; u = old successor is strictly below w = new
    one at a + m + 1; x a top → `hback` (values of u, w equal at a + m and a + m + 1) contradicts Howard at a + m; x not a top →
    `hconst` (all values equal at a + m + 1 and a + m + 2) and strict F4′ give val(x) ◁ val(x).
- Next: (1) apply the Lead's diff verdict on all statements (Statements.lean sent 11:44Z; Statements2.lean sent 12:26Z; Statements3-6
  and OptCounterExistsStatement to send); (2) whatever the Lead routes next (L-NEW 72's Lemma LEVEL if it survives). Not formalized
  and needing R104 / R117's genome definitions: WINDOW, SCC-RED, CAP, REACH3. Not formalized, generic: R15 (b), (c) (the φ potential and
  strictness), VJ00's Ω_σ as a minimum over plays (the Lean `OptCounter` is Friedmann's positional form).
- Layout rule: no lean/lakefile.* at lean/ root (Lead 11:31Z: «keep lean/lakefile.* absent at lean/ root»).
- Toolchain in a fresh container: commands in lean/lemmas/README.md (elan, `lake exe cache get`, `lake build`); tested on a fresh copy.

## Queue
000. OPEN: (1) the Lead's diffs: Genome.lean (15:32Z), GenomeClass.lean with K1Statement..K5Statement (15:46Z), LevelCountStatement
     (15:14Z); (2) (K4), NO-TIE, LEVEL (L2), (L3), (L5), PLATEAU (P1)-(P4), (P6), ALL-TCYC on the genome (plan in the Resume point).
0000. DONE 15:51Z: CN2, LOC-K2 (first half), B-ONLY, E-DOM, (K1), (K2), (K3), (K5) for Γ(G) / IDEAL-CYC(G), no premise.
00. DONE 14:44Z: `abs_statement` (box 208 §10) and `plateau` (Addendum A2, abstract one-player form), both Lean-checked (lane).
0. (accepted by the Lead 12:29Z / 13:13Z) TWO-CROSS, Λ-count, Howard run bound, (M) one-player, premise-free one-player LAM-GAP and
   Howard bound, DEPTH-COUNT3 with fix D1, T-CYC without the genome: all PROVED in Lean; every statement needs the Lead's diff.
   Two-player F1 = R15 (a) and the existence of optimal counterstrategies: PROVED in Lean; statements need the Lead's diff.
   Not done: WINDOW, SCC-RED, CAP (they need R104 / R117's genome definitions).
1. LAM-GAP, SHARP form, with BR-SEG and BR-SEG-G as corollaries: PROVED in Lean as sent; waits for the Lead's statement diff.
2. ONE-CROSS: PROVED in Lean as sent (abstract over a preorder, plus the VJ instance); waits for the Lead's statement diff.
3. Possible later (Lead 11:31Z, not yet): L-NEW 72's CANDIDATE Lemma LEVEL, if it survives L-RED.

## Sources opened
- [VJ00] Vöge, Jurdziński, «A Discrete Strategy Improvement Algorithm for Solving Parity Games», BRICS RS-00-48 (Dec 2000),
  https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, pdf sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65 (the
  sha256 RESULTS R15 names). Opened 2026-11-12, read by pdftotext:
  - §2.2 (cycle-domination games): V = {1, …, n} ordered by ≤ (the relevance order), partitions (R+, R−) and (M⊕, M⊖); a play ends at
    its first repeated vertex; λ(P) = the ≤-largest vertex of the play's cycle.
  - §4.1 (play values): Prefix(P) = the vertices before λ(P); π(P) = Prefix(P) ∩ V_{>λ(P)}; #(P) = |Prefix(P)|; Θ(P) = (λ(P), π(P), #(P));
    (1) PlayValues ⊆ {(v, (B, k)) : B ⊆ V_{>v}}.
  - §4.2 (the order): Reward(v) = −v on R−, v on R+; v ⪯ w iff Reward(v) ≤ Reward(w); B ≺ C iff MaxDiff(B, C) ∈ (B∖C) ∩ R− or
    ∈ (C∖B) ∩ R+; ⪯_ℓ compares B ∩ V_{>ℓ}; (B, k) ⊴_ℓ (B′, k′) iff B ≺_ℓ B′, or B =_ℓ B′ and (ℓ ∈ R− and k ≤ k′, or ℓ ∈ R+ and
    k′ ≤ k); (ℓ, (B, k)) ⊴ (ℓ′, (B′, k′)) iff ℓ ≺ ℓ′, or ℓ = ℓ′ and (B, k) ⊴_ℓ (B′, k′). «(1) guarantees that ⊴ is a linear order
    on PlayValues. It is a linear pre-order on V × ℘(V) × N.»
  - §4.4 (improvement, Switch_I, eq. (2)); §5.1 (4)-(10) (path values as shortest paths; (8) Π_σ(ℓ) = (∅, 0)); Lemma 5.7 (σ ⊑ Improve(σ)),
    read only as far as R15 (a) cites it. Not re-derived by me: (M) / F1 enters the Lean statements as a hypothesis.
- [Fr] Friedmann, «An Exponential Lower Bound for the Latest Deterministic Strategy Iteration Algorithms», arXiv 1106.0778 (LMCS 7
  (3:19) 2011), https://arxiv.org/pdf/1106.0778, pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611. Opened
  2026-11-12, read by pdftotext:
  - §2: «W.l.o.g. we assume Ω to be injective».
  - §3: rew(v) := Ω(v) if Ω(v) ≡₂ 0, −Ω(v) otherwise; relevance v < u :⟺ Ω(v) < Ω(u); reward ordering v ≺ u :⟺ rew(v) < rew(u);
    the play π = v₁ … v_k (w₁ … w_l)^ω with v₁ = v, vᵢ ≠ w₁ (1 ≤ i ≤ k), Ω(w₁) > Ω(w_j) (1 < j ≤ l); node valuation
    ϑ := (w₁, {vᵢ > w₁ | 1 ≤ i ≤ k}, k); M ≺ N :⟺ M △ N ≠ ∅ and max_<(M △ N) ∈ ((N ∩ V⊕) ∪ (M ∩ V⊖)); (u, M, e) ≺ (v, N, f) :⟺
    (u ≺ v) or (u = v and M ≺ N) or (u = v and M = N and e < f and u ∈ V⊖) or (u = v and M = N and e > f and u ∈ V⊕). Lemma 3.1,
    Theorem 3.2 ([VJ00]) read as statements only.
  - The Lean definitions (PGLemmas/Defs.lean) encode THIS form, line by line, as RESULTS R118's premise line says («in Friedmann arXiv
    1106.0778 §3's form (si.py)»). On play values (path component ⊆ V_{>cycle node}, VJ00 (1)) it is VJ00 §4.2's order: the filter
    ∩ V_{>ℓ} does nothing there. That equivalence is now a Lean lemma: PGLemmas/VJ00.lean `vj00Le_iff` with `val_proper`.
- Fleet texts read as inputs (not sources): claude/l-si 23d39400 docs/si/box101-lamgap.md §2; claude/l-red 0148d73f
  docs/red/R234-lamgap.md §0, §2, §3; claude/l-red docs/red/R231-onecross.md §2; trunk docs/RESULTS.md R118 (l. 13607 ff.), R17
  (l. 730 ff.), R15 (l. 624 ff.); docs/new/P-N5-XICYC.md §1-§5 and P-N5-XICYC-fixes.md l. 30-60 (F4′, STRICT-G, PATH-G).
  claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md §0-§2 ((K1)-(K5)), §3 (Lemma LEVEL), §4, §10 (Statement ABS), Addendum A (A0-A5, Lemma PLATEAU).
  trunk docs/RESULTS.md R104 (l. 9864) and R118 (l. 13607) header lines; docs/red/P-N5-REALIZE.md §2, §3.1; docs/new/P-N5-XICYC.md §1-§2;
  experiments/red/r187/stab.py build(); experiments/si/si.py l. 7, l. 38-43. NOT opened: R123's and R121's packets (CN2, B-ONLY,
  LOC-K2, E-DOM are proved here from the definitions, by my own arguments), R126's QUIET-N proof, L-RED R235, REFEREE 32.

## Dead ends
- None yet. (One trap met, not a dead end: inside `namespace PG` a theorem named `Val.lt_irrefl` shadows Mathlib's `lt_irrefl` in its
  own body, and `Val.lt_trichotomy` even failed with «fail to show termination»; the root lemmas are written `_root_.lt_irrefl`, …)

## Things only I know
- Proxy: github.com HTML pages and codeload.github.com return 403; git reads of public repositories, GitHub release assets,
  releases.lean-lang.org, cache.mathlib.org, arxiv.org and www.brics.dk returned 200.
- Mathlib v4.35.0 «is designed for use with the module system»: a plain (non-module) file importing it gets one Lake warning per
  import. lean/lemmas/lakefile.toml sets `allowNonModules = true` on the library, which removes the warning (Lake's own opt-out).
- The gate takes about 41 minutes in this container (experiments/si/check.sh about 20 of them): batch commits, one push at a time.
- Design choices in Defs.lean worth knowing: (1) a state is ONE map s : V → V (a positional pair read as one successor map), so the
  one-player lemma and the two-player corollaries share one valuation; (2) `lam` is chosen by Classical.choose among the cycle's
  vertices of largest priority, unique once `pr` is injective (a hypothesis of every statement, not of the definitions); (3) the
  statements are `def … : Prop`, and each theorem will have exactly that type, so the diffed text cannot drift from the proved one.
