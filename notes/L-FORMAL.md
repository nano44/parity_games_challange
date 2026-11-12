# L-FORMAL notebook (Lean formalization lane; branch claude/l-formal; files: lean/, this notebook)

## Resume point
- 2026-11-12T10:45Z (date -u): START CHECK written (docs/agents/handover-checks/L-FORMAL.md), waiting for the Lead's «go». No Lean file exists yet.
- After «go», in order: (1) open VJ00 §4.2 and Friedmann arXiv 1106.0778 §3, cite them below; (2) definitions for LAM-GAP (SHARP form,
  b − a ≤ |Ch|) in lean/lemmas/, sent to the Lead for the statement diff BEFORE proving; (3) the proof; (4) Lemma ONE-CROSS, abstract.
- Layout rule: no lean/lakefile.* at lean/ root until the Lead rules on CI (scripts/verify.sh would run `lake build` on every lane's push).
- Toolchain in a fresh container (about 2 minutes, measured in the start check):
  `curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o elan-init.sh`;
  `sh elan-init.sh -y --default-toolchain leanprover/lean4:v4.35.0`; `export PATH="$HOME/.elan/bin:$PATH"`;
  in the project directory `lake update` (clones Mathlib v4.35.0 and fetches its cache), then `lake build`.

## Queue
1. LAM-GAP, SHARP form (inputs: claude/l-si docs/si/box101-lamgap.md §2; claude/l-red docs/red/R234-lamgap.md, not on origin at
   l-red 9cb968e4).
2. ONE-CROSS (input: claude/l-red docs/red/R231-onecross.md §2).

## Sources opened
- None yet (start check only). The lane texts above are inputs, not sources.

## Dead ends
- None yet.

## Things only I know
- Proxy: github.com HTML pages and codeload.github.com return 403; git reads of public repositories, GitHub release assets,
  releases.lean-lang.org, cache.mathlib.org, arxiv.org and www.brics.dk returned 200 (probed 2026-11-12T10:45Z).
