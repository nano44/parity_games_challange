# lean/lemmas MANIFEST (L-FORMAL, 2026-11-12T21:54Z by date -u; for the Lead's RESULTS draft and CHECKER)

Generated, not hand-copied: (a) and (b) come from `lake env lean check/manifest.lean` (a `#eval` over the compiled environment:
each theorem named in Axioms.lean, its module and line, the head of its type after the binders, and every PG definition the type
depends on, transitively through definition bodies, grouped by module); the «commit» column is the first commit whose diff adds the
declaration line (`git log -G`); sha1 = sha1sum of the file at this commit. Status of every row: «Lean-checked (lane)»; a result only
through CHECKER and the CI job lean-lemmas. Scope: see README «Status and reading rules»; nothing here is a TARGET.md §2 statement.

## (a) Theorems offered (69 = every `#print axioms` line of Axioms.lean)

| # | theorem | Statement (type head) | file:line | first commit |
| --- | --- | --- | --- | --- |
| 1 | `lam_gap_sharp` | LamGapSharpStatement | LamGap.lean:247 | 4b376da4 |
| 2 | `lam_gap_oneplayer` | LamGapOnePlayerStatement | Corollaries.lean:19 | 4b376da4 |
| 3 | `brseg` | BrSegStatement | Corollaries.lean:52 | 4b376da4 |
| 4 | `brsegG` | BrSegGStatement | Corollaries.lean:108 | 4b376da4 |
| 5 | `brsegG_noH0` | (no Statement; type: LE.le) | Corollaries.lean:82 | 4b376da4 |
| 6 | `one_cross` | OneCrossStatement | OneCross.lean:12 | 4b376da4 |
| 7 | `one_cross_vj` | OneCrossStatement | OneCross.lean:80 | 4b376da4 |
| 8 | `Example.window_example` | (no Statement; type: Exists) | Example.lean:196 | 4b376da4 |
| 9 | `vj00Le_iff` | (no Statement; type: Iff) | VJ00.lean:44 | 4b376da4 |
| 10 | `val_proper` | (no Statement; type: Proper) | VJ00.lean:91 | 4b376da4 |
| 11 | `two_cross` | TwoCrossStatement | Counting.lean:20 | 4b376da4 |
| 12 | `lam_count` | LamCountStatement | Counting.lean:143 | 4b376da4 |
| 13 | `howard_run` | HowardRunStatement | Counting.lean:262 | 4b376da4 |
| 14 | `val_mono` | ValMonoStatement | Mono.lean:449 | 9fc1a0c4 |
| 15 | `lam_gap_oneplayer_noM` | LamGapOnePlayerNoMStatement | OnePlayer.lean:47 | 9fc1a0c4 |
| 16 | `howard_run_oneplayer` | HowardRunOnePlayerStatement | OnePlayer.lean:56 | 9fc1a0c4 |
| 17 | `depth_count` | DepthCountStatement | DepthCount.lean:275 | 9fc1a0c4 |
| 18 | `plen_lt_card` | PlenLtStatement | DepthCount.lean:431 | 9fc1a0c4 |
| 19 | `depth_count_val` | (no Statement; type: LE.le) | DepthCount.lean:443 | 9fc1a0c4 |
| 20 | `tcyc` | TCycStatement | TCyc.lean:41 | 9fc1a0c4 |
| 21 | `val_le_of_underProg` | (no Statement; type: Val.le) | Mono.lean:422 | 9fc1a0c4 |
| 22 | `val_mono_dual` | (no Statement; type: Val.le) | Dual.lean:126 | 9fc1a0c4 |
| 23 | `f1` | F1Statement | TwoPlayer.lean:118 | 9fc1a0c4 |
| 24 | `brseg_opt` | BrSegOptStatement | TwoPlayer.lean:185 | 9fc1a0c4 |
| 25 | `tcyc_opt` | TCycOptStatement | TwoPlayer.lean:211 | 9fc1a0c4 |
| 26 | `optCounter_exists` | OptCounterExistsStatement | OptExists.lean:49 | 9fc1a0c4 |
| 27 | `brsegG_noH0'` | BrSegGNoH0Statement | NoH0.lean:16 | 027b1d65 |
| 28 | `SPGame.d_max` | (no Statement; type: Eq) | Abs.lean:62 | 027b1d65 |
| 29 | `SPGame.d_le_step` | (no Statement; type: LE.le) | Abs.lean:74 | 027b1d65 |
| 30 | `abs_statement` | AbsStatement | AbsProof.lean:323 | 3880f474 |
| 31 | `plateau` | PlateauStatement | Plateau.lean:90 | 3880f474 |
| 32 | `AbsExample.hyps` | (no Statement; type: And) | AbsExample.lean:65 | 3880f474 |
| 33 | `AbsExample.d_start` | (no Statement; type: Eq) | AbsExample.lean:46 | 3880f474 |
| 34 | `AbsExample.d_end` | (no Statement; type: Eq) | AbsExample.lean:55 | 3880f474 |
| 35 | `level_count` | LevelCountStatement | LevelCount.lean:136 | 3880f474 |
| 36 | `Genome.pr_injective` | (no Statement; type: Function.Injective) | GenomeBasic.lean:156 | f74d38a4 |
| 37 | `Genome.pr_lt_iff` | (no Statement; type: Iff) | GenomeBasic.lean:159 | f74d38a4 |
| 38 | `Genome.e_dom` | (no Statement; type: Or) | GenomeBasic.lean:242 | f74d38a4 |
| 39 | `Genome.cn2` | (no Statement; type: LE.le) | GenomePlay.lean:149 | f74d38a4 |
| 40 | `Genome.loc_k2` | (no Statement; type: Eq) | GenomePlay.lean:213 | f74d38a4 |
| 41 | `Genome.b_only` | (no Statement; type: LT.lt) | GenomeBOnly.lean:214 | f74d38a4 |
| 42 | `Genome.k3` | Genome.K3Statement | GenomeK3.lean:218 | f74d38a4 |
| 43 | `Genome.k2` | Genome.K2Statement | GenomeK2.lean:201 | f74d38a4 |
| 44 | `Genome.k1` | Genome.K1Statement | GenomeK15.lean:50 | f74d38a4 |
| 45 | `Genome.k5` | Genome.K5Statement | GenomeK15.lean:68 | f74d38a4 |
| 46 | `Genome.prio_K1_lt_top` | (no Statement; type: LT.lt) | GenomeBasic.lean:228 | f74d38a4 |
| 47 | `OptCounter.le_succ` | (no Statement; type: Val.le) | GenomeK4.lean:58 | a1f02bee |
| 48 | `Genome.k4` | Genome.K4Statement | GenomeK4.lean:99 | a1f02bee |
| 49 | `Genome.class_order` | Genome.ClassOrderStatement | GenomeOrder.lean:161 | e14f5508 |
| 50 | `Genome.l2` | Genome.L2Statement | GenomeLevel.lean:259 | e14f5508 |
| 51 | `Genome.l3` | Genome.L3Statement | GenomeLevel.lean:366 | e14f5508 |
| 52 | `Genome.l5` | Genome.L5Statement | GenomeLevel.lean:421 | e14f5508 |
| 53 | `Genome.IdealCycRun.window_le` | (no Statement; type: LE.le) | GenomePlateau.lean:272 | e14f5508 |
| 54 | `Genome.plateau_g` | Genome.PlateauGStatement | GenomePlateau.lean:355 | e14f5508 |
| 55 | `Genome.quiet` | Genome.QuietStatement | GenomePlateau.lean:339 | e14f5508 |
| 56 | `Genome.all_tcyc_sharp` | Genome.AllTCycSharpStatement | GenomeAllTCyc.lean:29 | e14f5508 |
| 57 | `Genome.all_tcyc` | Genome.AllTCycStatement | GenomeAllTCyc.lean:90 | e14f5508 |
| 58 | `optCounter_of_local` | (no Statement; type: OptCounter) | GenomeK4.lean:85 | e14f5508 |
| 59 | `Genome.run_exists` | Genome.RunExistsStatement | GenomeRun.lean:152 | e14f5508 |
| 60 | `Genome.tiny_wf` | (no Statement; type: Genome.WF) | GenomeExample.lean:129 | e14f5508 |
| 61 | `Genome.tiny_run` | (no Statement; type: Exists) | GenomeExample.lean:211 | e14f5508 |
| 62 | `non_stall_count` | NonStallCountStatement | GenomeImp.lean:26 | 78c32d90 |
| 63 | `Genome.IdealCycRun.toImp` | (no Statement; type: Genome.IdealImpRun) | GenomeImp.lean:126 | 78c32d90 |
| 64 | `Genome.imp_k1` | Genome.ImpK1Statement | GenomeImp.lean:150 | 78c32d90 |
| 65 | `Genome.imp_l2` | Genome.ImpL2Statement | GenomeImp.lean:153 | 78c32d90 |
| 66 | `Genome.imp_l3` | Genome.ImpL3Statement | GenomeImp.lean:156 | 78c32d90 |
| 67 | `Genome.imp_l5` | Genome.ImpL5Statement | GenomeImp.lean:159 | 78c32d90 |
| 68 | `Genome.imp_non_stall` | Genome.ImpNonStallStatement | GenomeImp.lean:163 | 78c32d90 |
| 69 | `Genome.imp_k5_new` | Genome.ImpK5NewStatement | GenomeImp.lean:197 | 78c32d90 |

## (b) Definition modules the offered types depend on (26)

Statements.lean … Statements7.lean, Defs.lean, OptExists.lean (Lead 21:03Z, verbatim): «per-file acceptance times not recorded by the
Lead; the acceptance set is 11:49Z, 12:29Z, 13:13Z, 13:58Z, 14:54Z (2026-11-12)». CHECKER diffs each Statement against its lane text;
the times are context, not the check. «Helper definitions» rows: no separate acceptance is recorded; CHECKER diffs them as definitions.

| module | sha1 | definitions | Lead acceptance | theorems reaching it |
| --- | --- | --- | --- | --- |
| AbsExample.lean | eb8d4f68dde8 | `AbsExample.G`, `AbsExample.s` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 3: #32, #33, #34 |
| AbsStatement.lean | 4b2571cd9ec6 | `AbsStatement`, `SPGame`, `SPGame.E`, `SPGame.HowardAt`, `SPGame.Max`, `SPGame.NoZeroCycle`, `SPGame.PathW`, `SPGame.d`, `SPGame.edge`, `SPGame.tgt`, `SPGame.w` | 13:58Z, reading rules (i)-(v) (README «Statement ABS») | 6: #28, #29, #30, #32, #33, #34 |
| Defs.lean | b41c937cc862 | `HowardAt`, `OnCycle`, `Val`, `Val.le`, `Val.len`, `Val.lt`, `Val.set`, `Val.top`, `Window`, `lam`, `pair`, `plen`, `pset`, `rew`, `setLt`, `val` | definitions of Statements.lean; the Lead's diffs 11:49Z-14:54Z (INDEX l. 3-4); per-file time not recorded (see note) | 54: #1-69 (54 rows) |
| Genome.lean | 09b1bbf046c5 | `Genome`, `Genome.E`, `Genome.FromStart`, `Genome.IdealCycRun`, `Genome.M`, `Genome.N`, `Genome.Opt`, `Genome.Stopped`, `Genome.V0`, `Genome.Vertex`, `Genome.Vertex.K0`, `Genome.Vertex.K1`, `Genome.Vertex.K2`, `Genome.Vertex.K3`, `Genome.Vertex.beta`, `Genome.Vertex.cW`, `Genome.Vertex.cX`, `Genome.Vertex.casesOn`, `Genome.Vertex.ctorElim`, `Genome.Vertex.ctorElimType`, `Genome.Vertex.ctorIdx`, `Genome.Vertex.eface`, `Genome.Vertex.gate`, `Genome.Vertex.match_on_same_ctor._@.PGLemmas.Genome.3783567388._hygCtx._hyg.39`, `Genome.Vertex.match_on_same_ctor.het._@.PGLemmas.Genome.3783567388._hygCtx._hyg.39`, `Genome.Vertex.mover`, `Genome.Vertex.proxyTypeEquiv`, `Genome.Vertex.rec`, `Genome.WF`, `Genome.bmax`, `Genome.bpar`, `Genome.bprio`, `Genome.brank`, `Genome.deg`, `Genome.eb`, `Genome.epos`, `Genome.eprio`, `Genome.gate`, `Genome.idx`, `Genome.instDecidableEqVertex`, `Genome.instDecidableEqVertex.decEq`, `Genome.instFintypeVertex`, `Genome.isOdd`, `Genome.lev`, `Genome.pmax`, `Genome.pos`, `Genome.pr`, `Genome.prio`, `Genome.rk`, `Genome.start`, `Genome.start0`, `Genome.top`, `Genome.wt`, `Genome.xt` | 15:36Z, 15:50Z, deviations (a)-(h); (h) `WF.one_le_N` REQUIRED by the Lead (README «THE GENOME LAYER») | 31: #36-69 (31 rows) |
| GenomeBasic.lean | e7b3d8196455 | `Genome.isE`, `Genome.lexLt` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 19: #37-69 (19 rows) |
| GenomeClass.lean | ee81431726b4 | `Genome.K1Statement`, `Genome.K2Statement`, `Genome.K3Statement`, `Genome.K4Statement`, `Genome.K5Statement`, `Genome.cls`, `Genome.clsLe`, `Genome.clsLt`, `Genome.eset`, `Genome.isCore` | 15:50Z, deviations (K2), (K3) (e), (K4) (README «THE GENOME LAYER») | 18: #42-69 (18 rows) |
| GenomeExample.lean | 5b48854052c2 | `Genome.tiny` | the witness genome `tiny`; tiny_wf / tiny_run accepted 18:43Z («Accepted as an example theorem»); 19:00Z «witness by existence (optCounter_exists), not by computation» | 2: #60, #61 |
| GenomeImpStatement.lean | c7a6ecd10b87 | `Genome.IdealImpRun`, `Genome.ImpK1Statement`, `Genome.ImpK5NewStatement`, `Genome.ImpL2Statement`, `Genome.ImpL3Statement`, `Genome.ImpL5Statement`, `Genome.ImpNonStallStatement`, `NonStallCountStatement` | 19:05Z (readings (a)-(d)); ImpK5NewStatement 19:13Z, named point «stated for every mover, moved or not» | 8: #62, #63, #64, #65, #66, #67, #68, #69 |
| GenomeLevelStatement.lean | 478d0a714603 | `Genome.AllTCycSharpStatement`, `Genome.AllTCycStatement`, `Genome.L2Statement`, `Genome.L3Statement`, `Genome.L5Statement`, `Genome.PlateauGStatement`, `Genome.QuietStatement`, `Genome.ck` | 18:20Z (repeated 18:30Z, 18:43Z), deviations (i)-(vii) quoted in README | 11: #50, #51, #52, #54, #55, #56, #57, #65, #66, #67, #68 |
| GenomeOrderStatement.lean | 6ea42f8f6eb6 | `Genome.ClassOrderStatement`, `Genome.clsKey` | 18:20Z (repeated 18:30Z, 18:43Z): «stronger than box 208 §1: all pairs (Λ, E), B-ONLY not used» | 9: #49, #50, #51, #52, #54, #65, #66, #67, #68 |
| GenomePlay.lean | 7c5cd11657b8 | `Genome.IsState` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 6: #39, #40, #41, #42, #43, #48 |
| GenomeRunStatement.lean | 3c061e100308 | `Genome.RunExistsStatement` | 18:43Z, named deviation «existence is not stated in the fleet texts …; uniqueness not claimed» | 1: #59 |
| LevelCountStatement.lean | 777e6d61c5af | `FrontAt`, `LevelCountStatement`, `StallAt` | 15:16Z, deviation lines (a)-(c) (README «LEVEL, the counting») | 10: #35, #50, #51, #52, #54, #62, #65, #66, #67, #68 |
| Mono.lean | 75ebe80c9c86 | `UnderProg`, `UnderProgAt` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 1: #21 |
| OneCross.lean | 866c2ef3a285 | `valPreorder` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 1: #7 |
| OptExists.lean | 35cb62cc74ce | `OptCounterExistsStatement` | OptCounterExistsStatement: accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4) | 1: #26 |
| PlateauStatement.lean | 48aed4a9a6c4 | `PlateauStatement` | 14:54Z, deviations (a)-(c) (README «PLATEAU, abstract») | 1: #31 |
| Statements.lean | aaa3c0c2900d | `BrSegGStatement`, `BrSegStatement`, `LamGapOnePlayerStatement`, `LamGapSharpStatement`, `OneCrossStatement`, `nxt` | sent 11:44Z (notebook); accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4) | 30: #1-69 (30 rows) |
| Statements2.lean | 1b4e7c0474cb | `HowardRunStatement`, `LamCountStatement`, `TwoCrossStatement` | sent 12:26Z; accepted 12:29Z / 13:13Z (notebook Queue item 0) | 3: #11, #12, #13 |
| Statements3.lean | 457d1f43a9a6 | `HowardRunOnePlayerStatement`, `LamGapOnePlayerNoMStatement`, `ValMonoStatement` | accepted 12:29Z / 13:13Z (notebook Queue item 0) | 3: #14, #15, #16 |
| Statements4.lean | bac135d3c546 | `DepthCountStatement`, `PlenLtStatement`, `Sc`, `Sc'`, `depth` | accepted 12:29Z / 13:13Z (notebook Queue item 0); proved bound is R234's corrected one (README) | 3: #17, #18, #19 |
| Statements5.lean | f0ec83155a5d | `TCycStatement` | accepted 12:29Z / 13:13Z (notebook Queue item 0); IMPLIES R118 (i)(b), (c), not word for word (README) | 1: #20 |
| Statements6.lean | 68345b5a7d90 | `BrSegOptStatement`, `F1Statement`, `OptCounter`, `TCycOptStatement` | accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4); per-file time not recorded (see note) | 29: #23-69 (29 rows) |
| Statements7.lean | 76503546d4a1 | `BrSegGNoH0Statement` | accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4); kept apart from the landed BR-SEG-G text (README) | 1: #27 |
| VJ00.lean | 2a67315117fc | `Proper`, `above`, `vj00Le` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 2: #9, #10 |
| Weights.lean | 2b57e8b9f8ae | `LexLe`, `ds`, `dw`, `pw`, `sgw`, `sl`, `wt` | helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed | 10: #21, #49, #50, #51, #52, #54, #65, #66, #67, #68 |

## (c) Commands and outputs (run from lean/lemmas on the tree of 78c32d90, 2026-11-12; the MANIFEST commit adds no file under PGLemmas/)

```
lake exe cache get
rm -rf .lake/build && lake build
  start 2026-11-12T20:59:10Z
  Build completed successfully (3191 jobs).
  build exit 0
  axioms exit 0
  grep exit 1 (1 = nothing found)
  end 2026-11-12T21:00:11Z
  lines with «warning:»: 0
lake env lean Axioms.lean
   68  depends on axioms: [propext, Classical.choice, Quot.sound]
    1  depends on axioms: [propext, Quot.sound]
grep -rnw --include=*.lean -e sorry -e admit -e axiom -e native_decide . --exclude-dir=.lake   (prints nothing, exit 1)
lake env lean check/manifest.lean   (the generator of (a) and (b))
```
