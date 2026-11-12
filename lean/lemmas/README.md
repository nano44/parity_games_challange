# lean/lemmas: Lean checks of lane lemmas (L-FORMAL)

A self-contained Lake project. It is NOT built by scripts/verify.sh (there is no lean/lakefile.* at lean/ root, by the Lead's ruling
of 2026-11-12 11:31Z); the Lead rules later how CI runs it.

Pin: Lean v4.35.0 (lean-toolchain), Mathlib v4.35.0 = 56a005855ea17e0b0958f73ec801ae140b0a1679 (lake-manifest.json).
Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no admit, no new axioms.

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
- PGLemmas/Example.lean     `Example.window_example`: a 4-vertex window with b − a = 1 = |Ch| (the hypotheses are satisfiable).
- PGLemmas/VJ00.lean        VJ00 §4.2's order as printed (`vj00Le`) equals `Val.le` on play values (`vj00Le_iff`, `val_proper`).
- PGLemmas.lean             the library root (imports).
- Axioms.lean               `#print axioms` of every theorem above.

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
