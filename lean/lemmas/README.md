# lean/lemmas: Lean checks of lane lemmas (L-FORMAL)

A self-contained Lake project. It is NOT built by scripts/verify.sh (there is no lean/lakefile.* at lean/ root, by the Lead's ruling
of 2026-11-12 11:31Z); the Lead rules later how CI runs it.

Pin: Lean v4.35.0 (lean-toolchain), Mathlib v4.35.0 = 56a005855ea17e0b0958f73ec801ae140b0a1679 (lake-manifest.json).
Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no admit, no new axioms.

## Status and reading rules (Lead rulings 2026-11-12 11:49Z, 12:29Z, 13:13Z, 13:58Z, 14:54Z, 15:16Z, 15:36Z, 15:50Z, 17:22Z, 18:20Z, 18:30Z, 18:43Z; statements accepted as diffed)
- Every theorem here is «Lean-checked (lane)». It becomes a RESULT only through CHECKER (statement diff against the landed text,
  exact-commit re-run) and the Lead's CI job for lean/lemmas. INDEX.md lists each statement with the premise it keeps.
- Statements with a premise are checked in Lean CONDITIONAL on F1 (premise (M)); F1 is landed RESULTS R15 (a), refereed on paper.
  `f1` proves F1 in Lean in Friedmann's positional form. One paper step remains named: that the value against a positional optimal
  counterstrategy (`OptCounter`) equals VJ00 §4.3's Ω_σ, the minimum over the plays consistent with σ (VJ00 §4.3 / Friedmann Lemma 3.1).
- `pr` is injective in every statement. In the fleet `pr` is the relevance rank (priority, index), injective by construction (n5b's
  tie-break; si.py's p′ = 2·rank + parity), so this is not a restriction.
- `Window.moves` (every step of the window changes the state) is the encoding of «a..b are states of a Howard run that has not stopped».
- BR-SEG (`brseg`) has no genome: that IDEAL-CYC(G) meets its hypotheses is RESULTS R118 (a)'s definitions and stays a paper step.
- BR-SEG-G (a): `BrSegGStatement` is the landed text (with H0); `BrSegGNoH0Statement` (`brsegG_noH0'`) is the separate statement
  without H0. H0 is used at one proof step only: to give `Window.moves`.
- `HowardRunStatement` is an ABSTRACT form: its constant is n(n − 1) + (n(n − 1) + 1)·|Ch|, not box 101's L1-POLY constant
  (n3(n3 − 1) + 1)(N_C + 1).
- Howard with VJ valuations on a one-player game stops within n(n − 1) + (n(n − 1) + 1)·|Ch| steps, Lean-checked with no premise
  beyond the definitions (`howard_run_oneplayer`).
- DEPTH-COUNT3: the proved bound is R234's corrected one, n·(S_c(n) − 1) + n·(n − 1)·S′_c(n); box 100's uncorrected bound
  n·(S_c(n) − 1) is NOT proved (R234 gap D1).
- `tcyc` is the generic T-CYC (RESULTS R118 (f)) and the C ≤ n(n − 1) clause, without genome and without H0. It IMPLIES R118 (i)(b),
  (c): instantiate Mov := V0 (then |Mov| = n_E; «every step changes σ» follows from H0). It is not those clauses word for word.
- Statement ABS (l-new 8db300fe docs/new/N5-LEVEL-box208.md §10; a CANDIDATE in its lane, about shortest-path games, NOT about parity
  games): `abs_statement : AbsStatement V` is Lean-checked (lane), no premise. Reading rules, as the Lead accepted them (13:58Z):
  - the constant of clause (1) is (Σ_{z ∈ Max} |E z|)·|V| = §10's «(number of edges of Max vertices)·(number of vertices)»;
  - caveat relayed by the Lead from L-LIT T69 (not opened by L-FORMAL): «Howard's all-switch step; Max improves (Björklund–Vorobyov's
    LSP orientation)». The Lean statement is about exactly that step (`SPGame.HowardAt` at every Max vertex), nothing else;
  - (i) the target is not a Max vertex (`G.tgt ∉ G.Max`); (ii) weights in ℕ, d in ℕ∞; (iv) the reference state is the last state T;
    (v) «no cycle of total weight 0» is `NoZeroCycle` over all edges;
  - (iii) clause (2) is proved for EVERY step t < T, the last one included (§10 says «every step before the last one»): a run here is
    s 0, …, s T with every step changing the state, and a step that changes the state raises d somewhere (`SPGame.Run.exists_rise`).
  - ABS says nothing about IDEAL-CYC or a genome: §10's last bullet («IDEAL-CYC at class level is such a game») is NOT formalized.
- LEVEL, the counting (box 208 §3 (L1), §4 (C1), (C2)): `level_count : LevelCountStatement V α` is Lean-checked (lane); the Lead accepted
  `LevelCountStatement` (15:16Z), with three deviation lines: (a) the class order is an arbitrary LinearOrder α; for box 208's classes
  the bridge must show that the class order is linear (now `class_order`; `clsKey` maps the classes into ℤ ×ₗ ℤ) and that (K1)
  holds (now `k1`);
  (b) hypotheses 2-4 (the set M, the bound F, the bound L) are HYPOTHESES of `level_count`; for IDEAL-CYC they are now discharged by
  `l5` (the set M and the bound F) and `plateau_g` (L := N); (c) lane-level only: a result only through CHECKER and the CI job
  lean-lemmas. (C4) (the quiet steps after b′) is `quiet`.
- THE GENOME LAYER (Genome*.lean). The Lead ACCEPTED the definitions: Genome.lean (15:36Z, 15:50Z; diffed by him against P-N5-REALIZE §2,
  §3.1 l. 51-100) and GenomeClass.lean with K1Statement..K5Statement (15:50Z; against box 208 §1-§2). Deviations of Genome.lean from the
  texts: (a) the β-id is not a field, only br(b(x, k)) and bp(b(x, k)) are (`brank`, `bpar`); (b) «none» and the exit X are both `none`;
  (c) GRADED, the bijections and the parities are the separate predicate `WF`; (d) e_g's edge follows wt (none ↦ c_W); (e) `start0` is
  one map, σ_0 on Even's vertices and τ_0 on Odd's; (f) in `IdealCycRun` τ t is ANY optimal counterstrategy, the first state is any mover
  state, `FromStart` and `Stopped` are separate; (g) `pmax` spells out «max Ω so far»; (h) REQUIRED BY THE LEAD: `WF.one_le_N` (there is
  a mover; every mover has an option by the type of `start`, so M ≥ 1: the text's implicit assumption; without it top = 4 < Ω(K1) = 5).
  `one_le_N` is used by `prio_K1_lt_top` only. Deviations of GenomeClass.lean: (K2) for ANY two `IsState` maps with K2 → K1; (K3) (e)
  names the constant classes; (K4) spells «min» as «equal to one face's class and ≤ both».
  Asked for by the Lead (15:50Z), state 2026-11-12 18:12Z: (i) ClassOrder («It is a strict total order on the classes that occur», box
  208 §1): `class_order : G.ClassOrderStatement` (PGLemmas/GenomeOrder.lean), with the named deviation that the statement is STRONGER
  than the lane's sentence (all pairs (Λ, E), not only the classes that occur; B-ONLY is not used) and with the order-embedding `clsKey`
  into ℤ ×ₗ ℤ. (ii) The engine comparison of `IdealCycRun` is DONE, as
  DATA: check/idealcheck.py (below; numbers in INDEX.md), with the Lead's label for `opt` (17:22Z): «optimality checked as local
  optimality of a one-player counterstrategy plus agreement with si.py's optimum; full enumeration not done». It is DATA about the
  transcription and replaces no Lean proof.
  Proof origins: `b_only`, `cn2`, `loc_k2`, `e_dom` are proved from the definitions by L-FORMAL's own arguments (R123's and
  R121's packets were not opened); `k1`-`k5` follow box 208 §2, except `k5`, which goes through F1 and (K2) instead of DOM and CN2.
  Every theorem about Γ(G) is Lean-checked (lane) and has no premise: `cn2` (R123 CN2), `loc_k2` (R123 LOC-K2, first half), `b_only` (R123
  B-ONLY), `e_dom` (R121 E-DOM), `k1`, `k2`, `k3`, `k4`, `k5` (box 208 §2; box 208 is a CANDIDATE in its lane), and
  `OptCounter.le_succ` (RESULTS R123 LOC-GATE in ⊴ form, for any game: an optimal counterstrategy sends an Odd vertex that is not its
  own cycle node to a successor of ⊴-least value; `k4` uses it, NO-TIE is not used). DATA for the definitions: check/genomecheck.py; for the run: check/idealcheck.py (both below).
- BOX 208 ON THE GENOME, THE CHAIN TO ALL-TCYC (statements in PGLemmas/GenomeLevelStatement.lean and GenomeRunStatement.lean; the Lead's
  diff verdict: see INDEX.md). Lean-checked (lane), no premise, for every genome with `G.WF`:
  - `l2`, `l3`, `l5` (box 208 §3 (L2), (L3), (L5)); `plateau_g` (Addendum A, Lemma PLATEAU, with the bound N for any interval of
    consecutive stalls); `quiet` (a window of a run on which no class changes has at most N steps: the content of RESULTS R126 QUIET-N,
    proved here from the definitions, R126's packet not opened);
  - `all_tcyc_sharp`: every `IdealCycRun σ τ T` has T ≤ 2M(N + 2M)(N + 1) + N; `all_tcyc`: T ≤ P(N + 2M + 6) + N with P = 2M(N + 2M),
    box 208 Addendum A0's bound word for word. The run is ANY run in the sense of `IdealCycRun`: any first mover state, any optimal
    counterstrategy at each state, any choice among ⊴-best gates that are not the current one;
  The Lead's diff verdicts (2026-11-12 18:20Z, repeated 18:30Z, 18:43Z): «A. ClassOrderStatement: ACCEPT, with the named deviation
  «stronger than box 208 §1: all pairs (Λ, E), B-ONLY not used».» «B. All seven: ACCEPT, with your deviations (i)-(vii) recorded
  verbatim in README/INDEX.» «PlateauG with bound N, sharper than A0's N + 2M + 5: accepted as a STRONGER claim. In INDEX, cite it as
  matching L-RED 66's SHARP route and REFEREE 32's PR-5.» «Quiet replacing R126 QUIET-N: accepted. Name it in INDEX as «premise-free
  replacement of a landed citation».» «AllTCycStatement is A0 word for word. AllTCycSharpStatement is your route's bound, credited to
  L-RED 66's SHARP route (L41).» «(vii) TARGET.md diff: correct. Restricted model class, not §2, G-N5-TIME OPEN.» 18:43Z:
  «RunExistsStatement: ACCEPT. … Record the named deviation «existence is not stated in the fleet texts; added so that the theorems
  about IdealCycRun are not empty; uniqueness not claimed».» «tiny_wf / tiny_run (a run with T = 1, no premise) is the non-vacuity
  witness I asked for. Accepted as an example theorem.» «optCounter_of_local is logged as the Lean bridge for idealcheck's devfail.»
  The deviations (i)-(vii) of GenomeLevelStatement.lean, as sent to the Lead 18:17Z and accepted, verbatim: «(i) LAG / FRONT / STALL
  are on the keys `ck`; by ClassOrder (key injective and order-preserving) that is the lane's definition on classes. So B depends on
  A. (ii) (L3) (β) states the kinds of the cycle's vertices (mover, gate or β, all in the front), not the alternation mover → chosen
  gate → β-face → mover, which is what the successor map does on such a cycle. (iii) (L5) is stated as its two factors, the form
  `level_count` consumes; «at most M·(N + 2M) if case (β) never occurs» is not stated. (iv) PLATEAU: bound N (movers; `plateau`), where
  A0 has N + 2M + 5; any interval of consecutive stalls, maximality not used. (v) QUIET: every window of constant classes, no premise;
  it replaces the citation of R126 QUIET-N in (C4). (vi) ALL-TCYC: every `IdealCycRun` of length T (any first mover state, not only the
  genome's start, and not only the run to its stop), so in particular T_CYC. `AllTCycStatement` is A0's bound word for word (P·(N + 2M
  + 6) + N, P = 2M(N + 2M)); `AllTCycSharpStatement` is the bound my route gives, P·(N + 1) + N. (vii) TARGET.md: none of these is a
  TARGET.md §2 statement. They bound Howard steps of a model (IDEAL-CYC, R118 (a)) on a restricted family (the genome games of R104);
  TARGET.md §4 excludes restricted classes. G-N5-TIME stays OPEN.»
  - `run_exists`: for every genome there is a run from the genome's start whose last state has stopped (so T_CYC exists for that run and
    obeys the bound); `tiny_run`: the 13-vertex genome `Genome.tiny` has a run of length 1 from its start, so the hypotheses are
    satisfiable with a real Howard step.
  Reading rules. (a) This is a bound on the number of Howard steps of a MODEL (IDEAL-CYC, RESULTS R118 (a)) on a RESTRICTED family of
  games (the genome games Γ(G) of R104). It is not a TARGET.md statement (TARGET.md §4: restricted class), says nothing about N5,
  N5′-xi or Γ3, and docs/GAPS.md G-N5-TIME stays OPEN. (b) Box 208 is a CANDIDATE in its lane; these rows are «Lean-checked (lane)»
  and become results only through CHECKER and the CI job. (c) The theorems are about the Lean definitions (Genome.lean, GenomeClass.lean,
  `OptCounter`, `HowardAt`); that these are the fleet's objects rests on the Lead's diffs and on the DATA of check/genomecheck.py and
  check/idealcheck.py. (d) The route differs from box 208's text at three places, each named in GenomeLevelStatement.lean: the plateau
  bound is N (LAM-GAP SHARP through `plateau`) instead of N + 2M + 5; (C4) uses `quiet` instead of citing QUIET-N; and the equal-class
  case of (P4) at a gate whose W-face leads to c_W (both faces of class (c_W, ∅)) is proved by a length argument
  (`gate_of_cls_eq_none`: the level-0 sub-case that box 208's text lacks; reported to the Lead 18:00Z, routed by him to L-NEW 73) that
  Addendum B1 (5) does not give; it is needed only for `quiet` (Y := all vertices). (P6) follows REFEREE
  32's repair (claude/referee R-box208-preread §5.2 = Addendum B1 (1)(a)). (e) No run in the data comes near the bound (T ≤ 22 on the
  11 pinned genomes): the data test the transcription, the Lean proof is what bounds T.
  Not formalized: RESULTS R123 NO-TIE (not needed on this route); box 208 (L4), §5-§6 (WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC), §10's
  reading of IDEAL-CYC as a shortest-path game; anything on Γ3, N5′-xi, N5.
- PLATEAU, abstract one-player form (box 208 Addendum A2, steps (P5) + (P7)): `plateau : PlateauStatement V` is Lean-checked (lane),
  no premise (M). The Lead accepted `PlateauStatement` (14:54Z) with its three deviations from A2's wording: (a) one statement on the
  original vertex set with Y ⊆ V, instead of a separate game H; (b) the bound |Ch|; (c) (P6) only for t < b.
  - (P1)-(P4) and (P6) are HYPOTHESES of the Lean statement `PlateauStatement`. That a plateau of IDEAL-CYC satisfies them is now
    `plateau_g` (PGLemmas/GenomePlateau.lean, through `IdealCycRun.window_le`).
  - The bound is |Ch| (the movers of Y, so ≤ N), from LAM-GAP SHARP; A2 (P7) has n_E(H) ≤ N + 2M + 5 from BR-SEG-G (a). Lead 14:54Z:
    «Your reading that the bound drops to |movers of Y| ≤ N matches L-RED 66's lane remark (R235 «second route») and REFEREE 32's
    (`brseg` with Mov = movers of Y). Record it as agreement of three, still lane-level.» (L-FORMAL has not opened those two texts.)

## Files
- PGLemmas/Defs.lean        definitions only: node valuations and their order (Friedmann arXiv 1106.0778 §3 = VJ00 §4.1-§4.2), the
                            valuation of a positional play, Howard's step, the window.
- PGLemmas/Statements.lean  the statements as Lean propositions (`…Statement`); each is the exact type of the theorem proving it.
- PGLemmas/Order.lean       the order is a strict total order on all triples (injective priorities); `ext` and F4′.
- PGLemmas/Play.lean        Λ(s v) = Λ(v); (P3) val = (v, ∅, 0) at a cycle node; (P1) val v = ext(v, val(s v)) elsewhere.
- PGLemmas/LamGap.lean      `lam_gap_sharp : LamGapSharpStatement V` (claims (L), (U) of box 101 §2; R234 §3's sharpening).
- PGLemmas/Corollaries.lean `lam_gap_oneplayer`, `brseg`, `brsegG`, and `brsegG_noH0` (clause (a) without H0).
- PGLemmas/OneCross.lean    `one_cross` (any preorder) and `one_cross_vj` (node valuations).
- PGLemmas/Statements2.lean three further statements, PROPOSED to the Lead (TWO-CROSS, the Λ-change count, the Howard run bound).
- PGLemmas/Counting.lean    `two_cross`, `lam_count`, `howard_run` (proofs of Statements2).
- PGLemmas/Statements3.lean premise (M) for one-player games and the two premise-free one-player statements, PROPOSED to the Lead.
- PGLemmas/Weights.lean     additive path weights: `setLt_iff_wt_lt` (the order on path sets = the order of Σ ±2^pr), `Val.le_iff_lex`.
- PGLemmas/Mono.lean        `val_mono : ValMonoStatement V`: premise (M) = VJ00 Lemma 5.7 when the opponent has no choice.
- PGLemmas/OnePlayer.lean   `lam_gap_oneplayer_noM`, `howard_run_oneplayer`: one-player LAM-GAP SHARP and Howard's run bound, no premise.
- PGLemmas/Statements4.lean DEPTH-COUNT3's shallow-change count with R234's fix D1 (`depth`, `Sc`, `Sc'`), PROPOSED to the Lead.
- PGLemmas/DepthCount.lean  `depth_count : DepthCountStatement V`, `plen_lt_card`, `depth_count_val`.
- PGLemmas/Statements5.lean R118 (f) T-CYC and (i)(b), (c) as one statement without the genome, PROPOSED to the Lead.
- PGLemmas/TCyc.lean        `tcyc : TCycStatement V`, `lam_steps_le`.
- PGLemmas/Statements6.lean two-player F1 (`OptCounter`, `F1Statement`) and BR-SEG / T-CYC with «σ̄_t optimal» in place of F1, PROPOSED.
- PGLemmas/Dual.lean        `val_mono_dual`: (M) for the minimising player (priorities shifted by one reverse the order, keep the values).
- PGLemmas/TwoPlayer.lean   `f1 : F1Statement V` (RESULTS R15 (a) Lemma A = VJ00 Lemma 5.7), `brseg_opt`, `tcyc_opt`.
- PGLemmas/OptExists.lean   `optCounter_exists`: an optimal counterstrategy exists (Friedmann Lemma 3.1, existence).
- PGLemmas/Statements7.lean, NoH0.lean  `BrSegGNoH0Statement` and `brsegG_noH0'` (BR-SEG-G (a) without H0, kept apart from the landed text).
- PGLemmas/AbsStatement.lean  box 208 §10 Statement ABS (shortest-path games): definitions (`SPGame`, `SPGame.d`, `SPGame.HowardAt`,
                            `SPGame.NoZeroCycle`) and the statement `AbsStatement`.
- PGLemmas/Abs.lean         Bellman facts of d (`SPGame.d_tgt`, `d_le_edge`, `exists_edge_eq`, `d_max`) and (K1′) «a Howard step lowers
                            no d» (`SPGame.d_le_step`).
- PGLemmas/AbsProof.lean    `abs_statement : AbsStatement V`. (K5′) `Run.k5`, (L3) `Run.front_level`, (L4) `Run.front_rises` (no stall),
                            (L1) `Run.phi_step`, the count; the weight-0 cycle argument is `SPGame.no_closed`.
- PGLemmas/AbsExample.lean  `AbsExample.hyps`: a 3-vertex shortest-path game and a Howard run of one step for which every hypothesis of
                            `AbsStatement` holds (T = 1); `d_start`, `d_end`: the step raises d at Max's vertex from 1 to 3.
- PGLemmas/PlateauStatement.lean  box 208 Addendum A2 (P5) + (P7) as one statement `PlateauStatement` (accepted by the Lead 14:54Z).
- PGLemmas/Plateau.lean     `plateau : PlateauStatement V`; `val_congr` (the valuation of a vertex of a closed set depends only on the
                            successor map on the set), `lam_of_fixed`.
- PGLemmas/Example.lean     `Example.window_example`: a 4-vertex window with b − a = 1 = |Ch| (the hypotheses are satisfiable).
- PGLemmas/VJ00.lean        VJ00 §4.2's order as printed (`vj00Le`) equals `Val.le` on play values (`vj00Le_iff`, `val_proper`).
- PGLemmas/LevelCountStatement.lean  box 208 §3 (L1) + §4 (C1), (C2) without the genome: `FrontAt`, `StallAt`, `LevelCountStatement`
                            (accepted by the Lead 15:16Z).
- PGLemmas/LevelCount.lean  `level_count : LevelCountStatement V α`: classes in any linear order that never fall, at most |M| lowest
                            lagging classes, fronts of at most F vertices, at most L consecutive stalls ⇒ every state at which
                            something lags is among the first |M|·F·(L + 1).
- PGLemmas/Genome.lean      DEFINITIONS ONLY (accepted by the Lead 15:36Z, 15:50Z): the IDEAL genome (`Genome`, `Genome.WF`), the game Γ(G)
                            (`Genome.Vertex`, `idx`, `prio`, `pr`, `E`, `isOdd`, `V0`, `start0`: RESULTS R104 [DEF] = P-N5-REALIZE §2,
                            §3.1) and IDEAL-CYC(G) (`Genome.IdealCycRun`, `FromStart`, `Stopped`: RESULTS R118 (a) = P-N5-XICYC §2).
                            No theorem is in this file; the theorems about Γ(G) and IDEAL-CYC(G) are in the Genome*.lean files below.
- PGLemmas/GenomeBasic.lean first facts about Γ(G), read off the definitions (no premise): `Genome.idx_injective`, `pr_injective`,
                            `pr_lt_iff` (under `WF` the injective priority orders the vertices by (priority, index)), `even_pr`, the
                            priority bands of P-N5-REALIZE §3.1's «Rank facts», and `e_dom` (RESULTS R121 E-DOM).
- PGLemmas/GenomePlay.lean  plays of IDEAL-CYC(G), no premise: `Genome.IsState`, `IdealCycRun.isState`; `Genome.cn2` (RESULTS R123
                            CN2: every cycle node has priority ≥ 2), `lam_ne_mover`, `lam_ne_gate`; `Genome.loc_k2` (R123 LOC-K2, first
                            half: an optimal counterstrategy sends K2 to K1); the cycle nodes of the core and of c_X, c_W.
- PGLemmas/GenomeBOnly.lean `Genome.b_only` (RESULTS R123 B-ONLY), no premise: against the all-β answer (`tauBeta`, `lam_allBeta`).
- PGLemmas/GenomeClass.lean box 208 §1-§2 as DEFINITIONS AND STATEMENTS (accepted by the Lead 15:50Z): `isCore`, `eset`, `cls`, `clsLt`, `clsLe`;
                            `K1Statement` … `K5Statement`.
- PGLemmas/GenomeK3.lean    `Genome.k3 : G.K3Statement` ((K3) (a)-(e)); `BOnly`, `no_e_cycle`, `cls_step`, `cls_eface`, `cls_fixed`.
- PGLemmas/GenomeK2.lean    `Genome.k2 : G.K2Statement` ((K2) COARSE); `core_path` (a play from outside the core with cycle node K1 runs
                            K0 → K3 → K2 → K1), `cW_notMem_pset`.
- PGLemmas/GenomeK15.lean   `Genome.k1 : G.K1Statement`, `Genome.k5 : G.K5Statement`; `IdealCycRun.f1` (F1 along a run).
- PGLemmas/GenomeK4.lean    `Genome.k4 : G.K4Statement` ((K4) GATES); `OptCounter.le_succ` (RESULTS R123 LOC-GATE in ⊴ form, any game);
                            `le_of_underProgAt` (the converse of `underProgAt_of_le` at a vertex that is not its own cycle node);
                            `optCounter_of_local` (a counterstrategy that no single-vertex deviation improves at the deviating vertex
                            is optimal: the Lean bridge for check/idealcheck.py's counter `devfail`).
- PGLemmas/GenomeOrderStatement.lean  ClassOrder as a DEFINITION AND A STATEMENT: `Genome.clsKey` (the key (rew Λ, Σ_{x ∈ E} 2^(pr x))
                            in ℤ ×ₗ ℤ) and `ClassOrderStatement`.
- PGLemmas/GenomeOrder.lean `Genome.class_order : G.ClassOrderStatement`; `clsLt_iff`, `clsKey_lt_iff`, `clsKey_le_iff`,
                            `clsKey_injective`, `clsLt_total`, `clsLt_trans`; `pw_lt_of_max`.
- PGLemmas/GenomeLevelStatement.lean  STATEMENTS ONLY: box 208 §3 (L2), (L3), (L5) on the genome (`Genome.ck`, `L2Statement`,
                            `L3Statement`, `L5Statement`), Addendum A's Lemma PLATEAU with the bound N (`PlateauGStatement`), the quiet
                            window (`QuietStatement`: the content of RESULTS R126 QUIET-N, with no premise), Theorem ALL-TCYC with the
                            lane's bound (`AllTCycStatement`) and with the bound of the Lean route (`AllTCycSharpStatement`). The
                            deviations from the lane text are listed in the file's header.
- PGLemmas/GenomeLevel.lean `Genome.IdealPreRun` (what the class facts use of a run: states, optimal counterstrategies, F1) with
                            `IdealPreRun.k1`, `l2_pre`, `l3_pre`, `l5_pre`; their Howard instances `Genome.l2`, `l3`, `l5`; `ck_eq_iff`, `ck_le_iff`, `ck_lt_iff` (keys against classes),
                            `IdealCycRun.ck_mono` ((K1) on keys), `cls_succ_le` (the class does not rise along the play),
                            `IdealCycRun.cls_const` (the classes that never change).
- PGLemmas/GenomePlateau.lean  `Genome.plateau_g : G.PlateauGStatement`, `Genome.quiet : G.QuietStatement`; the window lemma
                            `IdealCycRun.window_le`; (P4) `IdealCycRun.gate_const` with `gate_of_cls_eq_some`,
                            `gate_of_cls_eq_none`; `succ_eq_eface` (the only predecessor of e_g is g), `cW_dom`, `pset_of_lam_cW`.
- PGLemmas/GenomeAllTCyc.lean  `Genome.all_tcyc_sharp : G.AllTCycSharpStatement`, `Genome.all_tcyc : G.AllTCycStatement`: the assembly
                            by `level_count`, `l5`, `plateau_g` and `quiet`.
- PGLemmas/GenomeImpStatement.lean  RF-A (Lead 19:00Z; accepted 19:05Z), DEFINITION AND STATEMENTS ONLY: `Genome.IdealImpRun` (a run
                            under an arbitrary improvement rule), `NonStallCountStatement`, `ImpK1Statement`, `ImpL2Statement`,
                            `ImpL3Statement`, `ImpL5Statement`, `ImpNonStallStatement`, `ImpK5NewStatement`; its header lists where
                            the proofs of e14f5508 use `howard` ((K5), `plateau_g`, `quiet`, `all_tcyc`, `run_exists`) and where they
                            do not.
- PGLemmas/GenomeImp.lean   RF-A proved, no premise: `non_stall_count`, `Genome.IdealImpRun.toPre`, `IdealCycRun.toImp`, `imp_k1`,
                            `imp_l2`, `imp_l3`, `imp_l5`, `imp_non_stall`, `imp_k5_new`. Reading rule: these bound the NON-stall
                            steps of IDEAL-CYC under any improvement rule; they say nothing about the number of stalls, so they give
                            no bound on the length of such a run. Same scope as ALL-TCYC: the genome games only, not TARGET.md.
- PGLemmas/GenomeRunStatement.lean  STATEMENT ONLY: `RunExistsStatement` (a run of IDEAL-CYC(G) from the genome's start exists and
                            stops).
- PGLemmas/GenomeRun.lean   `Genome.run_exists : G.RunExistsStatement`; `exists_best`, `howardNext`, `howardNext_spec` (Howard's
                            choice is a `HowardAt` step), `runSeq`, `run_prefix`.
- PGLemmas/GenomeExample.lean  `Genome.tiny` (one mover, two options, 13 vertices), `tiny_wf`, `tiny_better`, `tiny_run` (a run of
                            length 1 from the start); `setLt_insert_of_lt`, `ext_ext_lt`, `core_closed`.
- PGLemmas/Gamma3.lean      DEFINITIONS ONLY (accepted by the Lead 22:22Z, deviations (a)-(e) in its header): the S3-padded game Γ3(G)
                            of RESULTS R117 (= P-N5-REACH §3) and its free-priority form Γ3*(G*) of L-SI box 104 §4 as ONE definition
                            with the carrier priorities as a parameter (`Carrier`, `r104`, `Carrier.WF`); `Vertex3`, `idx3`, `prio3`,
                            `top3`, `pr3`, `isOdd3`, `V0_3`, `E3`, the standard state `std3 s`, `start3`. Per-pad priorities fixed by
                            experiments/new/box189/gamma3.py (R117's text: ≤ 2), DATA-checked (check/gamma3check.py).
- PGLemmas/Gamma3Statement.lean  STATEMENTS ONLY, accepted by the Lead 22:56Z: `PadStatement` (R117's Lemma PAD (a), (b), STRONGER:
                            every legal successor map, carriers Ω ≥ 3; PAD (c), the value transport, NOT stated), `Gamma3OldStatement`
                            (Γ inside Γ3), `Gamma3CardStatement` (n = N + 7M + 10); deviations in its header.
- PGLemmas/Gamma3Pad.lean   `Genome.pad : G.PadStatement`, no premise beyond the statement's: `reach_high` (every vertex but c_X
                            reaches Ω ≥ 3 within four steps), `eq_cX_of_iterate` (only c_X reaches c_X), `pr3_lt_of_prio_lt`,
                            `prio3_pad_le`, `top3_ge`.
- PGLemmas/Gamma3Basic.lean `Genome.gamma3_card`, `Genome.gamma3_old`; `card_vertex` (N + 3M + 6), `card_vertex3`, `idx_lt`,
                            `idx3_lt`, `idx3_injective`, `prio3_r104_old` (Γ3(G)'s priorities on Γ's vertices are Γ's).
- PGLemmas/Gamma3LiftStatement.lean  DEFINITIONS AND STATEMENTS, accepted by the Lead 00:00Z: the transport Γ → Γ3 (`padAt`,
                            `padSucc`, `lift3`, `npad`), `PadValueStatement` (R117 Lemma PAD (c)), `LiftStartStatement`.
- PGLemmas/Gamma3Lift.lean  `Genome.pad_value`, `Genome.lift_start`; `pr3_lt_iff`, `pr3_injective`, `pr3_old_lt_iff` (p′ of Γ3 orders
                            Γ's vertices as p′ of Γ), `lift3_legal`, `iterate_f` (lift3^[n + npad n] (old v) = old (s^[n] v)),
                            `cover`, `onCycle_old_iff`, `lam_old`, `plen_old`, `pset_old`, `pad_step`, `setLt_image_iff`.
- PGLemmas.lean             the library root (imports).
- Axioms.lean               `#print axioms` of every theorem above.
- INDEX.md                  lane text ↔ Lean statement ↔ Lean theorem, with the premise each statement keeps.
- check/crosscheck.py       DATA, not Lean: a line-by-line Python transcription of Defs.lean (and of `OptCounter`) compared with the
                            fleet's engine experiments/si/si.py on random games. Counters valdiff / orddiff / optfail must be 0.
                            `python3 -I lean/lemmas/check/crosscheck.py 1 2000 8` (from the repository root; about 3 s).
- check/genomecheck.py      DATA, not Lean: evaluates `Genome.idx`, `prio`, `isOdd`, `E`, `start0`, `pr` of Genome.lean on a genome file
                            and compares them, vertex by vertex, with experiments/red/r187/stab.py build(G, 0, kgad=True, esc=True) and
                            si.py's p′ = 2·rank + parity. Counters nfail / miss / priofail / ownfail / succfail / startfail / prfail
                            must be 0; GEN_CTRL=1 (the indices of e_g and β_g swapped in the reference) must fire. Needs lean/lemmas built.
                            `python3 -I lean/lemmas/check/genomecheck.py experiments/new/box191/inst/*.json` (about 40 s).
- check/gamma3check.py      DATA, not Lean: evaluates `idx3`, `prio3`, `isOdd3`, `E3`, `start3`, `pr3` of Gamma3.lean on a genome file
                            and compares them, vertex by vertex, with experiments/new/box189/gamma3.py build(G, {"K","pe","pb","m"})
                            (mode r104, π = r104) or with L-SI's free104.py build_free, transcribed in the tool (GAMMA3_MODE=free,
                            random carriers ≥ 6 by GAMMA3_SEED; FREE104_SRC=<free104.py> checks the transcription line for line).
                            Counters nfail (also n = N + 7M + 10) / miss / priofail / ownfail / succfail / startfail / prfail must be 0;
                            GAMMA3_CTRL=1 (pe_g and pβ_g swapped in the reference) must fire. Frozen outputs: check/out/gamma3check*.out.
                            `python3 -I lean/lemmas/check/gamma3check.py experiments/new/box189/corpus/*.json
                            experiments/new/box191/inst/*.json` (about 3 min per mode).
- check/idealcheck.py       DATA, not Lean: evaluates the five fields of `Genome.IdealCycRun` (frozen, legal, opt, howard, moves) and
                            `FromStart`, `Stopped`, as Genome.lean states them, on the run of the fleet's engine
                            (experiments/new/box191/idealcyc.py with experiments/si/si.py; σ̄_t = si.py's counterstrategy). `opt` is
                            checked as agreement with si.py's optimum, value by value, plus every single-vertex deviation of σ̄_t; full
                            enumeration is not done (by `optCounter_of_local` the single-vertex deviations suffice). It also checks
                            the fields of `Genome.WF` on the genome file. Thirteen counters, all must be 0; the controls
                            IDEAL_CTRL=how (HowardAt broken), IDEAL_CTRL=opt (one gate made non-optimal) and IDEAL_CTRL=wf (GRADED
                            broken) must fire. Frozen outputs: check/out/idealcheck*.out.
                            `python3 -I lean/lemmas/check/idealcheck.py experiments/new/box191/inst/*.json` (about 75 s).
- check/levelcheck.py       DATA, not Lean: evaluates the conclusions of `L2Statement`, `L3Statement`, `L5Statement`,
                            `PlateauGStatement`, `QuietStatement`, `AllTCycSharpStatement` and (K1) on keys, as the Lean file states
                            them, along the same engine runs as idealcheck.py, for every reference state b. Eight counters, all must
                            be 0; descriptive counts of fronts, stalls and plateaus; LEVEL_CTRL=1 (the front taken at the highest
                            lagging key) must fire. Frozen outputs: check/out/levelcheck*.out.
                            `python3 -I lean/lemmas/check/levelcheck.py experiments/new/box191/inst/*.json` (about 10 s).
- check/abscheck.py         DATA, not Lean: a Python transcription of AbsStatement.lean (d by Bellman-Ford and, for n ≤ 7, by enumerating
                            the paths of the definition), run on random shortest-path games: the hypotheses are satisfiable with T ≥ 1 and
                            both conclusions hold at every step. Counters dfail / hypfail / boundfail / c2fail / lastfail must be 0;
                            ABS_CTRL=1 (move to a smallest edge) must fire c2fail.
                            `python3 -I lean/lemmas/check/abscheck.py 1 20000 7` (from the repository root; about 1 s).

## Build and check (from the repository root; about 2 minutes and 10G of disk on a fresh machine)
```
curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o elan-init.sh
sh elan-init.sh -y --default-toolchain leanprover/lean4:v4.35.0
export PATH="$HOME/.elan/bin:$PATH"
cd lean/lemmas
lake exe cache get        # prebuilt Mathlib (first run clones Mathlib at the pinned commit)
lake build                # must end with "Build completed successfully"
grep -rnw --include=*.lean -e sorry -e admit -e axiom . --exclude-dir=.lake    # must print nothing
lake env lean Axioms.lean # every line: a subset of [propext, Classical.choice, Quot.sound]
```
