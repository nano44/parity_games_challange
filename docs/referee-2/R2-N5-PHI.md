# R2-N5-PHI: second-referee check of packet P-N5-PHI (L-SI box 14: Lemma Φ, Corollary Φ-1O). REFEREE-2 (successor 11), written 2026-10-25 19:2xZ-19:4xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue addition 19:18Z (Lead's stamp).
Object: docs/si/P-N5-PHI-box14.md, sha1 35e79ec1a91d0213b2b673779b69eb58a3e76b39 on trunk (added at af3a3b5a; `git show <ref>:<file> |
sha1sum`). Author: L-SI successor 9.
Background read: RESULTS R15 (a)-(d) (text checked, quoted below); R18 (d) Lemma R, Lemma S (a)-(b) and their gaps S1, S2, G-1OA-6
(RESULTS R18; docs/referee/R-N5-1OA.md l. 48 for the wording of S1, S2, a signed REFEREE file read for a citation, not for this packet);
R38 (a) KEY; SPEC S1 (order, injective priorities).
Independence: nothing in docs/referee/ was read for this packet (`ls docs/referee | grep -i phi` -> empty). No lane script
(experiments/si/phi14/phicheck.py) was run or imported.
Tools (own code, docs/referee-2/R2-N5-PHI/): phi_check.py (on R2-N5-OUT/out_check.py; λ from Ξ, λ^U from Odd's valuation U_τ, which my
tracer computes as Even's best response read in G's order), files.lst (= R2-N5-FBPOLY/files.lst, 492 𝒞^1O files), run_all.sh, logs/,
totals_logs.txt.
Labels: PROVED (L-SI 9). This is not a running-time bound, not a TARGET.md claim and not a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma Φ (a) | SIGN | — |
| §1 Lemma Φ (b) | SIGN | the packet's question: S1 and S2 do not threaten U's monotonicity (S2 IS its citation, R15 (a) + (d)); see §1 |
| §1 Lemma Φ (c) | SIGN | — |
| §2 Corollary Φ-1O (a), (b) | SIGN | N-PHI-1 (R15 (c) needs the chain to be of distinct strategies only; stated correctly) |
| §2 "Use", §3 | not signed (as briefed) | — |
No statement is NOT SIGNED, and no gap is open. No (P).

## 1. Lemma Φ: SIGN
- (a):
  - R15 (a) (Lemma A, VJ00 Lemma 5.7): a non-empty set I of improvements gives Ωσ ⊴ Ω_{Switch_I(σ)}.
  - R15 (d): every N5 iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to σ, or leaves σ unchanged, and Ωσ depends on σ alone.
  - So Ξ_k ⊴ Ξ_{k+1} pointwise at every transition.
  - S1's order compares reward(cycle node) first, and reward is injective (p′ injective, sign by parity). Strict increase iff the cycle
    node changes. ✓
- (b):
  - Lemma S (b) as signed (RESULTS R18 (d)): "L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run".
  - U_τ is the same object as the packet's U_k = Ξ^d_{τ_k}. By Lemma S (a), U_τ is the pointwise maximum of V_{σ′,τ} over σ′, i.e.
    VJ00 (11) on G^d read through Lemma R. Same play, so same cycle node λ^U.
  - The packet's question about S1, S2, G-1OA-6:
    - S1 (REFEREE R-N5-1OA l. 48): "(a)'s two halves are VJ00 (11) on G and on G^d; R17 (a) carries their derivation". That is a
      citation item on (a), not on monotonicity.
    - S2: "(b)'s monotonicity is R15 (a) = VJ00 Lemma 5.7, which needs the switched edges to be improvements: R15 (d)". So S2 is
      exactly the citation of the packet's fallback argument: R15 (a) on G^d with R15 (d)'s Iτ, and Lemma R reverses the order.
      Both are landed.
    - G-1OA-6 concerns Lemma S (c)-(d) at S4c fallbacks, which are not used here.
    - So (b) holds as stated, by either route. I would cite "R15 (a), (d) on G^d with Lemma R (this is gap S2's resolution)".
  - Equality iff equal cycle nodes, by injectivity. ✓
- (c):
  - Per vertex, the reward of λ_k(v) is non-decreasing and takes values among n, so λ_k(v) changes ≤ n − 1 times.
  - A λ-changing transition changes some λ(v), so there are ≤ n(n − 1) of them. The same holds for λ^U.
  - A joint λ-run starts only at the first state or after a transition that changes λ or λ^U: ≤ 2n(n − 1) + 1. ✓
- Scope: (a)-(c) use only R15 (a), (d), Lemma R and Lemma S (b), which hold on every game. "Every game" is correct. My data are on
  𝒞^1O only (§3).

## 2. Corollary Φ-1O: SIGN
- (a):
  - On 𝒞^1O, Odd's positional strategies are determined by τ(o) ∈ succ(o): d of them.
  - R15 (d): each τ-changing iteration applies Switch_I with ∅ ≠ I ⊆ Iτ on G^d. That includes the Odd S4c fallback (a single switch at o).
  - R15 (c): ≺_{G^d} is a strict partial order, and every such switch goes strictly up. τ is constant between τ-changing iterations, so
    the successive τ's form a strictly increasing chain of distinct strategies: ≤ d of them, so ≤ d − 1 changes. ✓
  - N-PHI-1 (precision): this uses only "no τ repeats" (a chain in a strict partial order), not any height bound; the packet states it so.
- (b):
  - A new phase starts only after a transition that changes λ or τ. There are ≤ n(n − 1) + (d − 1) such transitions, so
    #phases ≤ n(n − 1) + d. ✓
  - The aside "λ^U needs no count" is right: U_τ depends on τ alone (KEY is not even needed for that).
- Remark (reading, not signed): this reduces a polynomial bound for N5 on 𝒞^1O to a polynomial bound on one phase's length, as the
  packet says.

## 3. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 492 𝒞^1O files × own / rand / spec × 3 starts = 4,428 runs; random 𝒞^1O 64,000 runs
  (n 4-14 and 15-30). 1,484 / 1,484 logs "RESULT OK violations=0".
  - PHIA: 3,219,607 (vertex, transition) checks; λ changes 73,135; 0 drops.
  - PHIB: 3,219,607 checks; λ^U changes 21,526; 0 rises. The lane's data did not check λ^U; mine do.
  - PHIC: max changes per vertex 7 (λ) and 5 (λ^U), at most 750‰ of n − 1. Joint λ-runs at most 160‰ of 2n(n − 1) + 1.
  - Φ-1O (a): τ changes 37,223 and no τ repeats. The bound d − 1 is REACHED (1000‰, library and random; max 9 changes).
    Φ-1O (b): phases at most 375‰ of n(n − 1) + d (max 30).
- Mutation control (logs_mut/ub_rnd_own.txt): PHI_MUT=ub flips PHIB's direction and gives 2,385 violations on 2,000 random runs. So
  the λ^U check bites.
- Thin spot: my data are 𝒞^1O only. Lemma Φ is stated for every game, and it rests on its proof there (§1), which uses nothing
  𝒞^1O-specific.

## 4. Notes for the lane (none blocks a signature)
- N-PHI-1 (precision): Φ-1O (a) rests on "no τ repeats" (R15 (c)), which is all it needs.
- N-PHI-2 (citation): cite (b) as "R18 (d) Lemma S (b), whose citation gap S2 is R15 (a), (d) applied on G^d (with Lemma R)". The
  alternative in the packet's Remark is exactly that resolution, so the Remark's "if they do" can be dropped.
