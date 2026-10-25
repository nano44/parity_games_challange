# Referee packet P-N5-PHI: cycle nodes only rise along N5, so a run has at most 2n(n − 1) + 1 joint λ-runs, and on 𝒞^1O at most n(n − 1) + d phases (Lemma Φ, Corollary Φ-1O) (box 14)
L-SI successor 9 (Opus 5.5; D18, L40), session_018jN1MJkw56F58G3qcfcuZA. Written 2026-10-25 18:56Z (date -u), at the Lead's request of
18:41Z (Lead's stamp): "Φ micro-packet: YES. Write docs/si/P-N5-PHI-box14.md (frozen, self-contained) containing Lemma Φ ... plus the
corollary #phases ≤ n(n−1)+d via R38 KEY." Frozen at this commit: corrections go in a fixes file, never here.
- Source: docs/new/N5-time-box21.md §2.3 (L-NEW box 21, l-new a5f282d), Lemma Φ. That text was never refereed: RESULTS R21, R23, R25, R27
  and R28 call it "unrefereed", and REFEREE R-N5-Z l.16 / l.45 and REFEREE-2 R2-N5-Z l.22 left it unsigned. This packet re-states and
  re-proves it from landed results. Where the packet and the source differ, the packet governs.
  - Difference from the source: the dual half is proved from R18 (d) Lemma S (b) (U non-increasing). The source said "the same argument
    applies on G^d".
- Labels (D18/L40): PROVED (L-SI 9, unrefereed; from LANDED results only). No (P). No packet in review is used.
- Scope: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md.
  - §1 holds on every game.
  - §2 is on 𝒞^1O.
  - Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## To sign
| § | statement | label | uses |
| --- | --- | --- | --- |
| §1 | Lemma Φ (a)-(c) | PROVED | R15 (a), (d); R18 (d) Lemma S (b); SPEC S1 (injective ranks, the order) |
| §2 | Corollary Φ-1O | PROVED | §1, RESULTS R38 (a) KEY, R15 (c), (d) on G^d |

## 0. Objects
- N5 run: states (σ_k, τ_k), k = 0, 1, …. Every iteration changes σ or τ or both (R15 (d)).
- Ξ_k := Ξ_{σ_k}: Even's valuation against Odd's optimal counterstrategy σ̄_k (SPEC S1; R15's Ω_σ). It depends on σ_k alone.
  λ_k(v) := the cycle node of Ξ_k(v).
- U_k := Ξ^d_{τ_k}: Odd's valuation of τ_k in the dual game G^d (SPEC S2 "the same on G^d"; RESULTS R38 (a)'s U_k). It depends on τ_k
  alone. λ^U_k(v) := its cycle node.
- The order (SPEC S1): reward of the cycle node first (p′(c) if Ω(c) is even, −p′(c) if odd), then the path set, then the length.
  - p′(v) = 2·rank(v) + (Ω(v) mod 2), with rank injective (SPEC S1 "injective priorities").
  - So c ↦ reward(c) is injective on V.
- A JOINT λ-RUN is a maximal run of consecutive states with (λ_k, λ^U_k) constant.
- On 𝒞^1O, a PHASE is a maximal run of consecutive states with (λ_k, τ_k) constant. By RESULTS R38 (a) KEY it is a joint λ-phase
  (λ, λ^U, τ).

## 1. Lemma Φ (PROVED, L-SI 9; every game)
Statement.
- (a) For every vertex v and every k: reward(λ_{k+1}(v)) ≥ reward(λ_k(v)), with equality iff λ_{k+1}(v) = λ_k(v).
- (b) For every vertex v and every k: reward(λ^U_{k+1}(v)) ≤ reward(λ^U_k(v)), with equality iff λ^U_{k+1}(v) = λ^U_k(v).
- (c) Along a run, at most n(n − 1) transitions change λ, and at most n(n − 1) change λ^U. So a run has at most 2n(n − 1) + 1 joint
  λ-runs.
Proof.
- (a) By RESULTS R15 (a) and (d), Ξ_k ⊴ Ξ_{k+1} pointwise at every transition.
  - R15 (d): every N5 iteration applies Switch_I with ∅ ≠ I ⊆ Iσ_k to σ, or leaves σ unchanged.
  - R15 (a): such a switch does not decrease Ξ pointwise.
  - If σ is unchanged, Ξ is unchanged: Ξ_σ depends on σ alone.
  So Ξ_k(v) ⊴ Ξ_{k+1}(v). The order compares reward(λ(v)) first, so reward(λ_k(v)) ≤ reward(λ_{k+1}(v)). If the two rewards are equal,
  the two cycle nodes are equal, because reward is injective.
- (b) By RESULTS R18 (d) Lemma S (b), U_{τ_k} is non-increasing along the run, in Even's order on G.
  - Lemma S (b), as signed in R18: "L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run".
  - U_{τ_k}(v) has cycle node λ^U_k(v), and Even's order compares the reward of the cycle node first.
  So reward(λ^U_{k+1}(v)) ≤ reward(λ^U_k(v)), with equality iff the cycle nodes are equal (injectivity).
- (c) By (a), for each v the sequence reward(λ_k(v)) is non-decreasing, and it changes exactly when λ_k(v) changes.
  - Each change moves to a strictly larger value among the n values {reward(c) : c ∈ V}. So λ_k(v) changes at most n − 1 times.
  - A transition that changes λ changes λ_k(v) for at least one v, so there are at most n(n − 1) such transitions. The same holds for
    λ^U by (b).
  - A new joint λ-run starts only at a transition that changes λ or λ^U. So there are at most 2n(n − 1) + 1 joint λ-runs. □
- Remark. R18 (d) Lemma S was signed "WITH GAPS S1, S2, G-1OA-6". G-1OA-6 concerns Lemma S (c)-(d) at S4c fallbacks. The theorem there
  "uses (a)-(b) only", and (b) is what is used here. Referees: please confirm that S1 and S2 do not touch the monotonicity of U.
  - If they do, (b) also follows by the proof of (a) applied to G^d: R15 (a) on G^d with R15 (d)'s Iτ. Since R18 (d) Lemma R makes G^d's
    order the exact reverse of G's, the cycle-node reward in Even's order then falls.

## 2. Corollary Φ-1O (PROVED, L-SI 9; 𝒞^1O)
Statement. On 𝒞^1O with d := deg(o):
- (a) along any N5 run, τ changes at most d − 1 times;
- (b) a run has at most n(n − 1) + d phases.
Proof.
- (a) On 𝒞^1O, Odd's positional strategies are fixed by τ(o) ∈ succ(o): at most d of them.
  - By RESULTS R15 (d), every iteration that changes τ applies Switch_I with ∅ ≠ I ⊆ Iτ on G^d.
  - By R15 (c) on G^d, every such switch goes strictly up in the strict partial order ≺_{G^d}. Between such iterations τ is constant.
  - So the τ's along the run form a strictly ≺_{G^d}-increasing chain, and no τ repeats. Hence at most d − 1 changes.
- (b) A new phase starts only at a transition that changes λ or τ.
  - λ changes at most n(n − 1) times (§1 (c)) and τ at most d − 1 times ((a)).
  - So #phases ≤ n(n − 1) + (d − 1) + 1.
  - (λ^U needs no count: by R38 (a) KEY it is a function of τ.) □
- Use (READING, not to sign): with this corollary, a polynomial bound on N5 on 𝒞^1O needs only a polynomial bound on the length of one
  phase. See docs/si/N5-LEDGER-box14.md §1-§2 and docs/si/N5-FBPHASE-box14.md §6.

## 3. Data (DATA; not to sign)
experiments/si/phi14/phicheck.py (REFEREE-2's tracer, SPEC mode, read only). Corpus: docs/referee-2/R2-N5-OUT/files.lst, all 295 files,
S3 start + 1 random start each, 590 traces. Log: experiments/si/phi14/phicheck_lib.txt.
- 427,644 reward checks with 0 drops of reward(λ_k(v)).
- λ changes per vertex: max 0.5·(n − 1).
- τ changes ≤ d − 1 in every trace (max 9).
- Phases: max 0.375·(n(n − 1) + d).
- RESULT OK. Not checked: λ^U, which the tracer does not expose.
