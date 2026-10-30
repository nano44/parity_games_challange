# R2-N5-FIXD-L3: word-diff of the P-N5-FIXD line, revision L-3 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-FIXD-box91-line-L3.txt @ l-new 59d58d0d, sha1 7d22165a7e0cbd1a556cb546d8d3c53efa640956 (re-hashed: match). Chain
re-hashed at the same commit: L-1 7e99a4a9…, L-2 d553bbba…. Token diffs (difflib over whitespace tokens):
- L-1 → L-2: «revision L-2»; «(λ_Ξ, τ_t)» (my L-3); «then every phase P has» (my L-2). Both as I asked.
- L-2 → L-3: the implication «(Corollary PHASE-RED′, an implication) if every transition … (CONJECTURE FLAT-SW, not proved here), then …»
  becomes «(Theorem FLAT-SW, proof of record Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2
  R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b), from RESULTS R15 (a), (d), the standing SPEC premise of RESULTS R57 and R93 (a)) every
  transition k → k + 1 of every N5 run at which Ξ changes at some vertex, in particular every transition counted in FLATTR_P for any
  phase P, has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x); and (Corollary PHASE-RED′) every phase P has …», and the suffix
  «FLAT-SW is a conjecture» becomes «FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees». Nothing else
  changed.

## Checks
- Scope of the FLAT-SW clause against what is proved. SW-KEEP (R-N5-FIXD §4b, signed in my C.4): for σ′ = Switch_I(σ) with I a non-empty
  set of Ξ_σ-improving edges, at most one per vertex, if every switched vertex keeps its Ξ-value then Ξ_σ′ = Ξ_σ. The clause quantifies
  over every transition of every N5 run at which Ξ changes, in a phase or not. That is SW-KEEP's corollary as REFEREE stated it and as I
  signed it:
  - Ξ = Ξ_σ is a function of σ alone (SPEC S1), so a transition at which Ξ changes changes σ. **No transition has a Ξ-change without an
    Even σ-change.** The kinds where σ does not change (S4b alone; an Odd S4c fallback) leave Ξ unchanged, so the clause says nothing
    about them.
  - Every σ-change is Switch_I with ∅ ≠ I ⊆ Iσ_k and one edge per vertex (R15 (d); S4a's σ_new ∈ H_k, S4c's best improving edge), so
    SW-KEEP applies at S4a steps, at S4a steps together with S4b (σ's part), and at Even S4c fallbacks.
  - SW-KEEP gives some switched x with Ξ_{k+1}(x) ≠ Ξ_k(x), which is exactly the clause's conclusion (MON makes it a strict rise; the
    clause does not claim that).
  - My Lemma OWN corollary (R2-N5-FIXD §5, signed by REFEREE in R-N5-FIXD-C §3, a3aa5b68) proves the in-phase part only, in the stronger
    form «strict rise». The clause's «every transition … of every N5 run» rests on SW-KEEP, the proof of record. Consistent.
- Premises: SW-KEEP uses R15 (a) (MON and the improving edges), R15 (d) (the form of each σ-change), the R57 standing premise (optimality of
  σ̄ against σ′ in its step (4)) and R93 (a) (COMMON PREFIX in its step (2)). The clause lists exactly these. ✓ It does not need R15 (b) or
  any phase hypothesis.
- Strict symbol test of the changed text: k (bound by «every transition k → k + 1»), x (by «an Even vertex x switched at k»), P (by «for
  any phase P» in the FLAT-SW clause, and again by «every phase P» in PHASE-RED′), FLATTR_P, FLATSW_P(x) (both defined earlier in the line;
  definitions unchanged), Ξ, «switched at k» (defined earlier). Every symbol bound. ✓
- Citations: «R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b» is the right file, section and commit; «REFEREE R-N5-FIXD §4b, claude/referee
  2c9d8040» as pushed. ✓
- The suffix is accurate. Optional: it could add that Lemma OWN gives a second, independent proof of the in-phase form (R2-N5-FIXD §5,
  4a960ef9; signed by REFEREE, R-N5-FIXD-C §3, a3aa5b68). Not required.

## Verdict
L-3 (7d22165a): **MATCHES** (Opus 5.5, D15). No required change.

## Correction to my own earlier text (comp54_n80)
REFEREE's §C notes that comp54_n80's vertex 11 is ODD («11 134 1 11;», owner 1), so «11:51» in the start file is τ(11), not σ(11). My
R2-N5-FIXD.md §4 N-1 and R2-N5-FIXD-C.md C.2 wrote σ(11). The substance is unchanged: it is a non-edge at a forced vertex; the repaired run
(vertex 11 → 11) gives 55 / 22 / 32, the lane's numbers; N-1 stays withdrawn.
