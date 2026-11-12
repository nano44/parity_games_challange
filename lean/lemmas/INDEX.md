# lean/lemmas index: lane text ↔ Lean statement ↔ Lean theorem (L-FORMAL, 2026-11-12T18:46Z by date -u)

Status of every row: «Lean-checked (lane)»: lake build passes, no sorry, axioms ⊆ propext, Classical.choice, Quot.sound (Axioms.lean),
and the Lead accepted the statement in his diffs of 2026-11-12 11:49Z, 12:29Z, 13:13Z, 13:58Z, 14:54Z (15:16Z: the level count; 15:36Z, 15:50Z: Genome.lean with the required `WF.one_le_N`, and GenomeClass.lean; 18:20Z, 18:30Z, 18:43Z: ClassOrder, the seven statements of GenomeLevelStatement.lean with deviations (i)-(vii), which README.md quotes verbatim, and RunExistsStatement). A row becomes a RESULT only through CHECKER and the Lead's CI job. «Premise» = a hypothesis of the Lean statement that is not a definition; rows with premise F1 / (M) are checked
CONDITIONAL on F1 = landed RESULTS R15 (a).

| Lane / landed text | Lean statement (file) | Lean theorem (file) | Premise |
| --- | --- | --- | --- |
| LAM-GAP SHARP: l-si box 101 §2 + l-red R234 §3 | LamGapSharpStatement (Statements) | lam_gap_sharp (LamGap) | (M) on the window |
| the same, one-player wording of box 101 §2 | LamGapOnePlayerStatement (Statements) | lam_gap_oneplayer (Corollaries) | (M) on the window |
| the same, one-player, no premise | LamGapOnePlayerNoMStatement (Statements3) | lam_gap_oneplayer_noM (OnePlayer) | none |
| BR-SEG: RESULTS R118 (d), without the genome | BrSegStatement (Statements) | brseg (Corollaries) | F1 on the window |
| BR-SEG with «σ̄_t optimal» | BrSegOptStatement (Statements6) | brseg_opt (TwoPlayer) | none |
| BR-SEG-G (a): RESULTS R118 (i)(a), under H0 | BrSegGStatement (Statements) | brsegG (Corollaries) | F1 |
| BR-SEG-G (a) without H0 (every step changes σ) | BrSegGNoH0Statement (Statements7) | brsegG_noH0' (NoH0) | F1 |
| generic T-CYC (RESULTS R118 (f)) and C ≤ n(n−1), without genome and without H0; implies R118 (i)(b), (c) with Mov := V0 | TCycStatement (Statements5) | tcyc (TCyc) | F1 |
| T-CYC with «σ̄_t optimal» | TCycOptStatement (Statements6) | tcyc_opt (TwoPlayer) | none |
| ONE-CROSS: l-red R231 §2 | OneCrossStatement (Statements) | one_cross, one_cross_vj (OneCross) | F1 at one face, NO-TIE, LOC-GATE |
| TWO-CROSS: l-si box 100 §2 | TwoCrossStatement (Statements2) | two_cross (Counting) | F1 at both faces, NO-TIE, LOC-GATE |
| DEPTH-COUNT3, Λ clause: l-si box 100 §3 | LamCountStatement (Statements2) | lam_count (Counting) | the sequence never falls |
| DEPTH-COUNT3, depth ≤ c, with fix D1: box 100 §3 + R234 §0, §4 | DepthCountStatement, PlenLtStatement (Statements4) | depth_count, plen_lt_card, depth_count_val (DepthCount) | the sequence never falls |
| L1-POLY: l-si box 101 §3, abstract | HowardRunStatement (Statements2) | howard_run (Counting) | (M) |
| L1-POLY, one-player, no premise | HowardRunOnePlayerStatement (Statements3) | howard_run_oneplayer (OnePlayer) | none |
| (M), one-player: R15 (a) / VJ00 Lemma 5.7 with no choice for the opponent | ValMonoStatement (Statements3) | val_mono (Mono); val_le_of_underProg = VJ00 Lemma 5.5; val_mono_dual (Dual) | none |
| F1: RESULTS R15 (a) Lemma A, Friedmann's positional form | OptCounter, F1Statement (Statements6) | f1 (TwoPlayer) | none («τ optimal» is a hypothesis, see next row) |
| optimal counterstrategies exist: Friedmann Lemma 3.1 | OptCounterExistsStatement (OptExists) | optCounter_exists (OptExists) | none |
| VJ00 §4.2's order as printed = the order of Defs.lean on play values | (theorem only) | vj00Le_iff, val_proper (VJ00) | none |
| the window hypotheses are satisfiable, bound attained at \|Ch\| = 1 | (theorem only) | Example.window_example (Example) | none |
| Statement ABS (shortest-path games, Howard's all-switch step, Max improves): l-new 8db300fe box 208 §10, a CANDIDATE there; clause (2) for every step t < T | AbsStatement (AbsStatement) | abs_statement (AbsProof) | none (target not a Max vertex; no weight-0 cycle) |
| the hypotheses of AbsStatement are satisfiable with T = 1 (3 vertices, one Howard step, d rises from 1 to 3) | (theorem only) | AbsExample.hyps, d_start, d_end (AbsExample) | none |
| PLATEAU, abstract one-player form: box 208 Addendum A2 (P5) + (P7), on the original vertex set with Y ⊆ V; bound \|Ch\| = movers of Y | PlateauStatement (PlateauStatement) | plateau (Plateau) | (P1)-(P4), (P6) of A2 are HYPOTHESES; for IDEAL-CYC they are discharged in `plateau_g` |

| LEVEL, the counting: box 208 §3 (L1) + §4 (C1), (C2), abstract (classes in ANY linear order; that box 208's class order is linear is `class_order`): b′ − a ≤ \|M\|·F·(L + 1) | FrontAt, StallAt, LevelCountStatement (LevelCountStatement) | level_count (LevelCount) | (K1); the lowest lagging classes lie in M; fronts ≤ F; at most L consecutive stalls (for IDEAL-CYC: `k1`, `l5`, `plateau_g`) |
| GENOME LAYER (definitions: Genome.lean, GenomeClass.lean). RESULTS R123 CN2: every cycle node has priority ≥ 2 | (theorem only) | Genome.cn2, lam_ne_mover, lam_ne_gate (GenomePlay) | none |
| RESULTS R123 LOC-K2, first half: σ̄(K2) = K1 | (theorem only) | Genome.loc_k2 (GenomePlay) | none |
| RESULTS R123 B-ONLY | (theorem only) | Genome.b_only (GenomeBOnly) | none |
| RESULTS R121 E-DOM | (theorem only) | Genome.e_dom (GenomeBasic) | none |
| pr is injective and orders the vertices by (priority, index) (si.py's p′) | (theorem only) | Genome.pr_injective, pr_lt_iff, even_pr (GenomeBasic) | none (WF) |
| box 208 §2 (K1) MONOTONE | K1Statement (GenomeClass) | Genome.k1 (GenomeK15) | none |
| box 208 §2 (K2) COARSE | K2Statement (GenomeClass) | Genome.k2 (GenomeK2) | none |
| box 208 §2 (K3) ALONG THE PLAY (a)-(e) | K3Statement (GenomeClass) | Genome.k3 (GenomeK3) | none |
| box 208 §2 (K4) GATES | K4Statement (GenomeClass) | Genome.k4 (GenomeK4) | none |
| RESULTS R123 LOC-GATE, in ⊴ form, for any game (an optimal counterstrategy sends an Odd vertex that is not its own cycle node to a successor of ⊴-least value) | (theorem only) | OptCounter.le_succ (GenomeK4) | none |
| box 208 §2 (K5) HOWARD DOMINATES | K5Statement (GenomeClass) | Genome.k5 (GenomeK15) | none |
| ClassOrder: box 208 §1 «It is a strict total order on the classes that occur»; stated STRONGER, for all pairs (Λ, E), with the order-embedding clsKey into ℤ ×ₗ ℤ | clsKey, ClassOrderStatement (GenomeOrderStatement) | Genome.class_order (GenomeOrder) | none |
| box 208 §3 (L2): a front vertex is a mover, a gate or a β-vertex with a mover successor | ck, L2Statement (GenomeLevelStatement) | Genome.l2 (GenomeLevel) | none |
| box 208 §3 (L3): case (α) or case (β) | L3Statement (GenomeLevelStatement) | Genome.l3 (GenomeLevel) | none |
| box 208 §3 (L5), as its two factors (the front's class is the class at b of a gate or (β, ∅); a front has at most N + 2M vertices) | L5Statement (GenomeLevelStatement) | Genome.l5 (GenomeLevel) | none |
| box 208 Addendum A, Lemma PLATEAU on the genome, with the bound N for any interval of consecutive stalls: a STRONGER claim than A0's N + 2M + 5, matching L-RED 66's SHARP route and REFEREE 32's PR-5 (Lead 18:20Z; L-FORMAL has opened only REFEREE 32's text); (P6) with REFEREE 32's repair | PlateauGStatement (GenomeLevelStatement) | Genome.plateau_g, IdealCycRun.window_le, IdealCycRun.gate_const (GenomePlateau) | none |
| the quiet window (the content of RESULTS R126 QUIET-N; box 208 §4 (C4)): a window of constant classes has at most N steps; a «premise-free replacement of a landed citation» (Lead 18:20Z). Its proof contains the level-0 sub-case that box 208's text lacks (`gate_of_cls_eq_none`: equal classes (c_W, ∅) at both faces of a gate) | QuietStatement (GenomeLevelStatement) | Genome.quiet, gate_of_cls_eq_none (GenomePlateau) | none |
| box 208 Addendum A, Theorem ALL-TCYC: T ≤ P(N + 2M + 6) + N, P = 2M(N + 2M), for EVERY run of IDEAL-CYC(G) (any first mover state, any optimal counterstrategy, any choice among best gates); and with the bound P(N + 1) + N of the Lean route, «credited to L-RED 66's SHARP route (L41)» (Lead 18:20Z). A bound for the model IDEAL-CYC on the genome games only: not TARGET.md, G-N5-TIME stays OPEN | AllTCycStatement, AllTCycSharpStatement (GenomeLevelStatement) | Genome.all_tcyc, Genome.all_tcyc_sharp (GenomeAllTCyc) | none |
| runs exist and stop: a run of IDEAL-CYC(G) from the genome's start whose last state has stopped; named deviation (Lead 18:43Z): «existence is not stated in the fleet texts; added so that the theorems about IdealCycRun are not empty; uniqueness not claimed» | RunExistsStatement (GenomeRunStatement) | Genome.run_exists (GenomeRun) | none |
| the hypotheses are satisfiable with a step: the 13-vertex genome `tiny` satisfies WF and has a run of length 1 from its start | (theorem only) | Genome.tiny_wf, Genome.tiny_run (GenomeExample) | none |
| local optimality suffices for `OptCounter` (a counterstrategy that no single-vertex deviation improves at the deviating vertex is optimal) | (theorem only) | optCounter_of_local (GenomeK4) | none |

DATA beside the genome rows (check/genomecheck.py: Lean's `idx`, `prio`, `isOdd`, `E`, `start0`, `pr` evaluated on a genome file against
experiments/red/r187/stab.py build(G, 0, kgad=True, esc=True) and si.py's p′; unit: vertex): experiments/new/box191/inst, 11 genomes, 1,018
vertices, and the 21 genomes of experiments/new/box202/inst with at most 400 vertices, 4,916 vertices: nfail, miss, priofail, ownfail,
succfail, startfail, prfail all 0. Control GEN_CTRL=1, 2 genomes, 110 vertices: priofail 56, succfail 56, startfail 78, prfail 56. Not run:
the 32 larger genomes of box202/inst.

DATA beside the genome rows, the run (check/idealcheck.py: a Python evaluation of the five fields of `IdealCycRun`, of `FromStart` and of
`Stopped` as Genome.lean states them, NOT the Lean code; engine: experiments/new/box191/idealcyc.py run(G) with experiments/si/si.py,
σ̄_t = the counterstrategy that si.py returns; set: the 11 JSON genomes of experiments/new/box191/inst; 1,018 vertices, 191 states, 180
steps; outputs check/out/idealcheck*.out): wffail (the fields of `Genome.WF` on the genome file; unit: failed condition), builddiff,
prdiff (unit: vertex), fastdiff (18,814 (state, vertex)), frozenfail, legalfail,
taufail, valdiff (18,814 (state, vertex)), devfail (546,942 (state, vertex, single-vertex deviation of σ̄_t)), howardfail (2,388 (step,
mover)), movesfail (180 steps), startfail, stopfail (272 (mover, gate) at T): all 0. Controls: IDEAL_CTRL=how (one mover per step sent to
a ⊴-smallest gate): howardfail 180, on all 11 genomes; IDEAL_CTRL=opt (one gate per state switched to its other face): devfail 7,361,
valdiff 3,541, on all 11 genomes; IDEAL_CTRL=wf (every level raised by one): wffail 44, on all 11 genomes. Label of `opt` (Lead 17:22Z): «optimality checked as local optimality of a one-player counterstrategy
plus agreement with si.py's optimum; full enumeration not done» (by the Lean theorem `optCounter_of_local`, the single-vertex
deviations at the deviating vertex suffice for `OptCounter`). The runs are short (T ≤ 22): this checks the transcription, not growth,
and it replaces no Lean proof.

DATA beside the rows (L2), (L3), (L5), PLATEAU, QUIET, ALL-TCYC (check/levelcheck.py: a Python evaluation of the conclusions of those
statements as GenomeLevelStatement.lean states them, NOT the Lean code; the same engine runs as idealcheck.py; set: the 11 JSON genomes
of experiments/new/box191/inst, 191 states; every reference state b; outputs check/out/levelcheck*.out): keyfail (the key order against
`clsLt`; unit: ordered pair of occurring classes), k1fail (unit: (step, vertex)), l2fail (unit: (b, t, front vertex)), l3fail, l5fail
(unit: (b, t) with a lagging vertex; 1,473 such pairs), platfail (unit: (b, maximal interval of stalls)), quietfail (unit: maximal
window of constant classes), boundfail (unit: genome): all 0. Descriptive: clause (α) of (L3) holds at 747 of the 1,473 pairs, clause (β)
at 726; 309 stall steps over all b; the longest interval of stalls has 9 steps (cyc2_d7, N = 14), and on DEAD_SEG2P_d4_N8 it has 8
steps with N = 8, so the bound N of `plateau_g` is attained there; the longest window of constant classes has 9 steps; the largest front
has 76 vertices. Control LEVEL_CTRL=1 (the front at the highest lagging key): l2fail 1,470, l3fail 1,470, l5fail 1,470. These runs are
short (T ≤ 22): the data show that the statements are not empty on real runs; they do not test the bound of ALL-TCYC.

DATA beside the ABS row (check/abscheck.py, a Python transcription, not Lean; unit: step of a Howard run on a random shortest-path game):
seed 1, 20,000 games with at most 7 vertices: 7,130 runs with T ≥ 1, 7,914 steps, longest run 3 steps; seed 2, 20,000 games with at most
12 vertices: 9,035 runs with T ≥ 1, 10,286 steps, longest run 4 steps; dfail, hypfail, boundfail, c2fail, lastfail all 0 in both. Control
ABS_CTRL=1 (seed 1, 2,000 games): c2fail 1,140 of 1,140 steps. The runs are short: this checks the reading of the statement, not growth.

Not formalized: box 208 §3 (L4) and §5-§6 (WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC); RESULTS R123 NO-TIE (not needed on the route to
ALL-TCYC); §10's reading of IDEAL-CYC at class level as a shortest-path game; anything on Γ3, N5′-xi or N5; WINDOW, SCC-RED, CAP, REACH3
(they need RESULTS R104 / R117's genome and Γ3 in Lean); R15 (b), (c), (d); the equality of the positional Ω_σ used here with VJ00 §4.3's
minimum over plays; anything about running time at bit cost; TARGET.md §6.
