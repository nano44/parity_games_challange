# lean/lemmas: Lean checks of lane lemmas (L-FORMAL)

A self-contained Lake project. It is NOT built by scripts/verify.sh (there is no lean/lakefile.* at lean/ root, by the Lead's ruling
of 2026-11-12 11:31Z); the Lead rules later how CI runs it.

Pin: Lean v4.35.0 (lean-toolchain), Mathlib v4.35.0 = 56a005855ea17e0b0958f73ec801ae140b0a1679 (lake-manifest.json).
Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no admit, no new axioms.

## Status and reading rules (Lead rulings 2026-11-12 11:49Z, 12:29Z, 13:13Z; statements accepted as diffed)
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
- PGLemmas/AbsStatement.lean  box 208 §10 Statement ABS (shortest-path games): DEFINITIONS AND STATEMENT ONLY, NOT PROVED.
- PGLemmas/Abs.lean         first lemmas towards ABS: Bellman facts of d (`SPGame.d_tgt`, `d_le_edge`, `exists_edge_eq`, `d_max`) and
                            «a Howard step lowers no d» (`SPGame.d_le_step`). `AbsStatement` itself is NOT proved.
- PGLemmas/Example.lean     `Example.window_example`: a 4-vertex window with b − a = 1 = |Ch| (the hypotheses are satisfiable).
- PGLemmas/VJ00.lean        VJ00 §4.2's order as printed (`vj00Le`) equals `Val.le` on play values (`vj00Le_iff`, `val_proper`).
- PGLemmas.lean             the library root (imports).
- Axioms.lean               `#print axioms` of every theorem above.
- INDEX.md                  lane text ↔ Lean statement ↔ Lean theorem, with the premise each statement keeps.
- check/crosscheck.py       DATA, not Lean: a line-by-line Python transcription of Defs.lean (and of `OptCounter`) compared with the
                            fleet's engine experiments/si/si.py on random games. Counters valdiff / orddiff / optfail must be 0.
                            `python3 -I lean/lemmas/check/crosscheck.py 1 2000 8` (from the repository root; about 3 s).

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
