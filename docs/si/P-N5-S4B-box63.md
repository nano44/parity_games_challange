# P-N5-S4B (packet, L-SI box 63): S4b's new τ is Odd's pointwise optimum against σ in S4b's arena, under R57's standing premise 1E-N3 alone. So a τ kept at a τ-stretch transition is that optimum. A premise result: it bounds no count
L-SI successor 38 (Opus 5.5; D18). Lead 2026-11-01 02:24Z: «freeze a SMALL referee packet P-N5-S4B … If both referees sign it, I will
record a Lead reading lifting L42's S4b restriction.» FROZEN 2026-11-01 (this commit); the sha1 of this file and of the line file go to
the Lead. Repairs go to docs/si/P-N5-S4B-fixes.md, never into this file. Working note: docs/si/N5-S4B-box63.md (this packet governs).
- Status: lane-authored (L-SI), not referee-originated (L41 does not apply). No count is bounded. G-N5-TIME stays OPEN. Not M3, not a
  step-4 pass, not a TARGET.md claim.
- Object: N5 only (SPEC S1-S5, docs/new/N5-ssi-global.md, with Q1-Q4 and FIX 1-4).

## 0. What to sign
| § | item | label |
| --- | --- | --- |
| 2 | Lemma S4B-OPT | PROVED (to sign) |
| 3 | Corollary S4B-KEEP | PROVED (to sign) |
| 4 | brute-force check, mutation control, pins | DATA, NOT to sign |

## 1. Setting and premises (landed labels only)
- [1E-N3] RESULTS R57's standing SPEC premise: S1's procedure realises the pointwise optimum. Its scope, as read and signed by REFEREE-2
  (docs/referee-2/R2-N5-1E.md §2, note N-1E-1), quoted: «VJ00's setting (§2) is every finite game graph with a successor at each vertex =
  TARGET §1's games; no class hypothesis. What remains SPEC's requirement, as in every landed N5 result: that S1's PROCEDURE outputs an
  optimal σ̄ (VJ00 §6)». Used here in the form: for every finite game graph G* (the priorities of G, a successor at every vertex) and
  every Even strategy σ* of G*, the Odd strategy ρ* that S1's procedure outputs for σ* on G* satisfies val(σ*, ρ*)(x) ⊴ val(σ*, ρ)(x) for
  every positional Odd strategy ρ of G* and every vertex x.
- [S4b] SPEC S4b: «If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H′: Odd v keeps only edges to A(v); Even v only the edge
  to σ(v). τ_new = Odd's optimal counterstrategy (S1 procedure on H′, not dual) to σ. Else τ_new = τ.»
- [S4c / S4d / FIX 3] SPEC S4c: FALLBACK if σ_new = σ and τ_new = τ (Even's improving edges if Iσ ≠ ∅, otherwise Odd's on Iτ); S4d:
  σ, τ := σ_new, τ_new. FIX 3: «In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ) … Odd falls back only if Iσ = ∅.»
- Notation. A run is the sequence of states (σ_k, τ_k). Iσ_k and I_τ_k are N5's Even and Odd improving edges at state k (SPEC S2, the
  latter on G^d). For a state k with I_τ_k ≠ ∅: H′_k := S4b's arena at k, and τ_new,k := S4b's output at k. val(σ, ρ)(x) := the SPEC S1
  value of the (σ, ρ)-play from x. ⊴ is SPEC S1's order (better for Even). An Odd fallback is an S4c iteration with Iσ_k = ∅. A
  τ-stretch transition is a transition k → k + 1 with τ_(k+1) = τ_k.

## 2. Lemma S4B-OPT (PROVED)
- Statement. For every state k of every N5 run with I_τ_k ≠ ∅, every positional Odd strategy ρ of H′_k and every vertex x:
  val(σ_k, τ_new,k)(x) ⊴ val(σ_k, ρ)(x). Moreover τ_(k+1) = τ_new,k unless k → k + 1 is an Odd fallback.
- Proof.
  - (i) H′_k is a finite game graph. It carries G's priorities, and every vertex has a successor in it: σ_k(v) for Even v, and τ_k(v) ∈
    A(v) for Odd v. Its only Even strategy is σ_k.
  - (ii) By [S4b], τ_new,k is the Odd strategy that S1's procedure outputs for σ_k on H′_k. [1E-N3] with G* := H′_k and σ* := σ_k gives
    val_(H′_k)(σ_k, τ_new,k)(x) ⊴ val_(H′_k)(σ_k, ρ)(x) for every positional Odd strategy ρ of H′_k and every x.
  - (iii) A value depends only on the play and the priorities (SPEC S1). Every (σ_k, ρ)-play of H′_k is the (σ_k, ρ)-play of G from the
    same vertex, with the same priorities. So val_(H′_k) = val on these plays, and (ii) is the claim.
  - (iv) By S4d, τ_(k+1) = τ_new,k unless S4c applies. S4c applies only when σ_new = σ_k and τ_new,k = τ_k. If Iσ_k ≠ ∅, FIX 3 keeps
    τ_(k+1) = τ_new,k (= τ_k). If Iσ_k = ∅ it is an Odd fallback. □
- Remark (no dual). S4a's optimality (RESULTS R95's premise text: «for S4a, σ_new is the pointwise optimum of the one-player arena H_t»)
  applies [1E-N3] to the DUAL of S4a's arena and reads the result back on G. S4b applies [1E-N3] to H′_k itself («not dual»), so no
  dual reading is needed.

## 3. Corollary S4B-KEEP (PROVED)
- Statement. At every τ-stretch transition k → k + 1 with I_τ_k ≠ ∅: τ_k = τ_new,k. Hence τ_k is a pointwise-optimal Odd strategy of
  H′_k against σ_k.
- Proof. An Odd fallback sets τ_(k+1)(v) to an improving w ≠ τ_k(v) for some v (S4c), so it is not a τ-stretch transition. By §2,
  τ_k = τ_(k+1) = τ_new,k, and §2's inequality applies. □
- (If I_τ_k = ∅, S4b does not run and H′_k is not defined; the statement is about I_τ_k ≠ ∅ only.)

## 4. DATA (NOT to sign)
- Tool experiments/si/anc58/s4bopt.py (l-si 9521f2e72bf049e71de7eadec7853d99227b9dc7). At every state with I_τ ≠ ∅ it recomputes
  τ_new as experiments/new/box21/n5x.py step() does. When H′ has at most CAP Odd strategies, it enumerates all of them and counts
  (state, ρ, vertex) triples with val(σ, ρ)(x) strictly better for Odd than val(σ, τ_new)(x) (OPTV). Control S4AV: the same brute force
  for S4a's σ_new on S4a's arena against τ.
- Corpus experiments/si/anc58/corpus_fixed.lst (1,132 games; output anc58/s4bopt_corpus.txt; CAP 1,024):
  - 7,772 states with I_τ ≠ ∅; 6,719 enumerated, comparing 290,345 strategies; OPTV 0. 1,053 states had more than 1,024 arena
    strategies and were NOT enumerated.
  - τ_(k+1) = τ_new at 7,736 states. The other 36 are the Odd fallbacks.
  - S4a control: 16,430 states enumerated, S4AV 0.
- Mutation control (MUT=1: τ_k in place of τ_new,k): OPTV 215 on experiments/red/h3/instances/lcount2_n23 (+ .start) and 677 on
  experiments/red/n5/instances/sym_h8_s1 (default start, experiments/si/anc58/inst/sym_h8_s1_default.start). So the check can detect a
  non-optimal τ.
- Pins: experiments/si/check.sh «box 63» (lcount2_n23: STATES 6, CHECKED 6, RHOS 46, OPTV 0; the mutation control OPTV 215; corpus totals).
  Faithfulness of lcount2_n23 and sym_h8_s1 (box 62): startcheck OK, n5b (red/seg/xeng.py) state sequences identical, n5.py's solutions =
  Oink zlk, strategies verified.
- The data checks the code (n5x / si.py), so the code's conformance to SPEC stays DATA (R15 G-N5T-1), as for every landed N5 result.

## 5. RESULTS line draft
- File: docs/si/P-N5-S4B-line.txt (one line, no heading marker; sha1 sent to the Lead with this packet's).
- Pre-check against CHECKER's recurring E-items:
  - (a) Free symbols: σ_k, τ_k, I_τ_k, Iσ_k, H′_k, τ_new,k, val, ⊴, ρ, x, Odd fallback and τ-stretch transition are all bound in the line.
  - (b) DATA overclaim (C108 E-1, C109 E-3): the DATA clause states the exact enumerated scope (6,719 states, CAP 1,024, 1,053 not
    enumerated). It is marked «not part of the claim».
  - (c) L43: the line contains no DEAD.
  - (d) L41: lane-authored, said so.
  - (e) Landed labels only: R57 (1E-N3), R15 (G-N5T-1), SPEC S1, S2, S4b, S4c, S4d, FIX 3. REFEREE-2's N-1E-1 is cited by file and section.
