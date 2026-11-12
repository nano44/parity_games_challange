# lean/lemmas: Lean checks of lane lemmas (L-FORMAL)

A self-contained Lake project. It is NOT built by scripts/verify.sh (there is no lean/lakefile.* at lean/ root, by the Lead's ruling
of 2026-11-12 11:31Z); the Lead rules later how CI runs it.

Pin: Lean v4.35.0 (lean-toolchain), Mathlib v4.35.0 = 56a005855ea17e0b0958f73ec801ae140b0a1679 (lake-manifest.json).
Allowed axioms: propext, Classical.choice, Quot.sound. No sorry, no admit, no new axioms.

## Files
- PGLemmas/Defs.lean        definitions only: node valuations and their order (Friedmann arXiv 1106.0778 §3 = VJ00 §4.1-§4.2), the
                            valuation of a positional play, Howard's step, the window.
- PGLemmas/Statements.lean  the statements as Lean propositions (`…Statement`); each is the exact type of the theorem proving it.
- PGLemmas.lean             the library root (imports).

## Build and check (from the repository root; about 2 minutes and 10G of disk on a fresh machine)
```
curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o elan-init.sh
sh elan-init.sh -y --default-toolchain leanprover/lean4:v4.35.0
export PATH="$HOME/.elan/bin:$PATH"
cd lean/lemmas
lake exe cache get        # prebuilt Mathlib (first run clones Mathlib at the pinned commit)
lake build                # must end with "Build completed successfully"
grep -rnw --include=*.lean -e sorry -e admit . --exclude-dir=.lake    # must print nothing
```
