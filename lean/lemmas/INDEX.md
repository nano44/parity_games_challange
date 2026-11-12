# lean/lemmas index: lane text ↔ Lean statement ↔ Lean theorem (L-FORMAL, 2026-11-12T13:08Z by date -u)

Status of every row: «Lean-checked (lane)»: lake build passes, no sorry, axioms ⊆ propext, Classical.choice, Quot.sound (Axioms.lean),
and the Lead accepted the statement in his diffs of 2026-11-12 11:49Z, 12:29Z, 13:13Z. A row becomes a RESULT only through CHECKER and
the Lead's CI job. «Premise» = a hypothesis of the Lean statement that is not a definition; rows with premise F1 / (M) are checked
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

STATED, NOT PROVED: box 208 §10 Statement ABS (l-new 8db300fe docs/new/N5-LEVEL-box208.md): `AbsStatement`, with `SPGame`, `SPGame.d`,
`SPGame.HowardAt`, `SPGame.NoZeroCycle` (PGLemmas/AbsStatement.lean). No theorem of that type exists. Proved so far (PGLemmas/Abs.lean):
the Bellman facts (B1) and (K1′) `SPGame.d_le_step`. Proof plan for the rest: notes/L-FORMAL.md.

Not formalized: box 208's Lemma LEVEL on the genome, Addendum A (PLATEAU), WINDOW, SCC-RED, CAP, REACH3 (they need RESULTS R104 / R117's genome and Γ3 in Lean); R15 (b), (c), (d); the
equality of the positional Ω_σ used here with VJ00 §4.3's minimum over plays; anything about running time at bit cost; TARGET.md §6.
