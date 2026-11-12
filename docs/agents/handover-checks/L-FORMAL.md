# L-FORMAL start check (new lane, no predecessor; written 2026-11-12T10:44Z (date -u); session_01V5yGRZm5AyrczAEMySsfpN)
Every answer is measured from the repository or from a command run in this container (commands named), not recalled.

### 1. Branch and head
- Trap check run first: `git fetch --unshallow origin` (repository was not shallow), `git fetch origin claude/vibrant-johnson-nxvvxo
  claude/l-si claude/l-red`. `git branch --show-current` = claude/l-formal. HEAD = 071392490dcea36bfa952288aa6170d45fadf874 =
  origin/claude/vibrant-johnson-nxvvxo (trunk commit 2026-11-12T06:44:27Z); `git rev-list --left-right --count HEAD...trunk` = 0 0.
- `git ls-remote origin claude/l-formal` was empty before this push: the branch is new, this commit is its first.
- Read-only inputs at fetch time: claude/l-si 4fda7245bd59ae34d7b0614065a775f6ca10e387 (docs/si/box101-lamgap.md, §2 LAM-GAP with the
  bound |Ch| + 1), claude/l-red 9cb968e421db703bb626b2be673c1d1ef1c5f524 (docs/red/R231-onecross.md, Lemma ONE-CROSS).
  docs/red/R234-lamgap.md (Lemma SHARP, b − a ≤ |Ch|) is NOT on origin/claude/l-red at that head (`git show`: path does not exist).

### 2. Plan (5 lines; nothing below starts before «go»)
1. Sources first: open VJ00 (BRICS RS-00-48, §4.2) and Friedmann arXiv 1106.0778 §3; record section numbers in notes/L-FORMAL.md; fix
   the value type (Λ, Π, length) and the order ⊴ exactly as RESULTS R118's [VJ] premise names it (R118 premise line, R15 l. 628).
2. Definitions only, in a self-contained project lean/lemmas/ (its own lakefile there, none at lean/ root): one-player game on a finite
   graph with priorities, positional strategy, lasso play, VJ value, ⊴, Howard switch-all step, Λ-constant window. Send them to the
   Lead for the statement diff against box 101 §2 (and R234 once on origin) BEFORE any proof.
3. Prove LAM-GAP in the SHARP form (b − a ≤ |Ch|) along box 101 §2's steps (U), (L), (O), (E). Premise (M) (R15 (a), pointwise
   monotonicity) enters as a named hypothesis of the theorem, as in the lane text, unless the Lead asks for it to be proved in Lean too.
4. Then Lemma ONE-CROSS, abstract, from its three premises (F1 monotone, NO-TIE, LOC-GATE) over a linear order on values.
5. Each delivery: `lake build` log, a grep for sorry / admit, `#print axioms` of every theorem (allowed: propext, Classical.choice,
   Quot.sound), the exact build commands for the Lead, notebook updated; park with a handover at ~450k context.

### 3. GAPS rows this lane will touch
None. L-FORMAL owns no row of docs/GAPS.md (open rows at trunk 07139249: GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME). The two
lemmas sit under G-N5-TIME (owner L-NEW), which stays OPEN whatever Lean checks here: they are steps of a chain that ends in CONJECTURE
DEEP3 (box 101 Addendum A). TARGET.md §6's Lean form of the TARGET statement is not this task.

### 4. Rulings, verbatim (trunk docs/DECISIONS.md; both «active» in docs/DECISIONS-INDEX.md, rows l. 32 and l. 5)
- D18 (DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas
  of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
  briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
- D1 (DECISIONS.md l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including
  the fleet's own, as wrong until it passes the gauntlet below.»
- D21: named in my brief as «being recorded»; it has no row in docs/DECISIONS-INDEX.md at trunk 07139249, so I do not quote it.

### 5. TOOLCHAIN check (run 10:40Z to 10:44Z by date -u, inside the 20-minute box): Lean 4 and Mathlib both install and build here
What worked, in order (all through the session's HTTPS proxy, nothing bypassed):
- elan: `curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o elan-init.sh` (9,823 bytes, sha256
  a620ff16…), then `sh elan-init.sh -y --default-toolchain leanprover/lean4:v4.35.0`: exit 0, under 1 minute. The elan binary came from
  github.com/leanprover/elan/releases (release asset, HTTP 200); the toolchain from
  https://releases.lean-lang.org/lean4/v4.35.0/lean-4.35.0-linux.tar.zst. Installed under $HOME/.elan (3.0G, outside the repository).
  `lean --version`: «Lean (version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release)»;
  `lake --version`: «Lake version 5.0.0-src+eb6cafb (Lean version 4.35.0)»; elan 4.2.4. v4.35.0 is the newest «stable» entry of
  https://release.lean-lang.org/ (created 2026-10-12).
- Mathlib: a scratch project outside the repository (lakefile.toml with `require mathlib`, git
  https://github.com/leanprover-community/mathlib4, rev v4.35.0; lean-toolchain leanprover/lean4:v4.35.0). `lake update`: exit 0 in
  65 s; it cloned mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679 and 8 dependencies (batteries, aesop, Qq, proofwidgets, importGraph,
  plausible, LeanSearchClient, Cli) by git over HTTPS and fetched the prebuilt cache (9,031 files from https://cache.mathlib.org). Then
  `lake build` of a file importing Mathlib.Data.Finset.Card and Mathlib.Order.Basic: exit 0 in 2 s, «Build completed successfully (640
  jobs)», `#print axioms` printed «[propext, Quot.sound]». The project's .lake directory is 7.3G (must stay out of git).
What was blocked or odd:
- HTTP 403 from the proxy for github.com HTML pages (github.com/leanprover/lean4/releases/latest, github.com/leanprover-community/mathlib4)
  and for codeload.github.com (source tarballs). Not needed: git reads of the public repositories and release assets returned 200.
- elan warning «could not check for elan self-update: failed to parse latest release tag» (same 403; harmless).
- Lake warning on the test file: Mathlib «is designed for use with the module system; consider adding `module`» (a warning, build passes).
Not tested: the CI runner (GitHub Actions ubuntu-24.04) and other lanes' containers. Neither has Lean today; scripts/verify.sh's lean()
step fails with «lake not installed» as soon as a file lean/lakefile.* exists, so I create none at lean/ root (brief's layout rule).
Proposed pin for lean/lemmas/, to be confirmed by the Lead at «go»: Lean v4.35.0 with Mathlib v4.35.0 (56a00585…), lake-manifest.json
committed, lean/lemmas/.gitignore with .lake/. If the Lead prefers no Mathlib (a smaller install for CI: toolchain only, no 7.3G
cache), I say so in the definitions message and build the finite-set and order facts by hand; that costs proof time.

### Trap and the check that prevents it
A file lean/lakefile.* at lean/ root makes every lane's push fail (verify.sh lean(): «lake not installed», exit 1). Check before every
commit: `ls lean/lakefile.*` must fail. Also: .gitignore covers lean/.lake/ only, so lean/lemmas/.gitignore must exist before the
first `lake` run there; `git status --short` before every commit, commit by explicit path only.
