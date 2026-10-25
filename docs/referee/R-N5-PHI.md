# R-N5-PHI: REFEREE report on packet P-N5-PHI (L-SI box 14: Lemma Φ, Corollary Φ-1O)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 19:19Z (Lead's stamp).
- Object: docs/si/P-N5-PHI-box14.md at trunk 02ad3f88, sha1 35e79ec1a91d0213b2b673779b69eb58a3e76b39 (checked with `git show`; identical on
  my tree), 85 lines. Author: L-SI successor 9.
- Written 2026-10-25T19:52Z-20:13Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-PHI* file. D1 applied.
- Premises re-read: RESULTS R15 (a)-(d) (VJ00 Lemma A for any set of improvements; Theorem (c) with ≺; N5 switch form (d)); R18 (d)
  Lemma R and Lemma S (a)-(b), with the R-N5-1OA verdict row (l. 48) on gaps S1, S2; R38 (a) KEY; SPEC S1 (injective priorities, the order).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma Φ (a)-(c) (every game) | PROVED | SIGNED |
| §2 | Corollary Φ-1O (a), (b) (𝒞^1O) | PROVED | SIGNED |
| §2 "Use", §3 | reading, data | not to sign | not signed |
- No (P), and no packet in review is used. Landed premises only.
- No gaps. Notes PHI-N1 (the lane's question), PHI-N2 (data: λ^U, which the lane's tracer did not expose).

## The lane's question: do R18's gaps S1, S2 touch the U-monotonicity? (PHI-N1)
- The gaps as recorded by my lane (docs/referee/R-N5-1OA.md l. 48):
  - S1: "(a)'s two halves are VJ00 (11) on G and on G^d; R17 (a) carries their derivation".
  - S2: "(b)'s monotonicity is R15 (a) = VJ00 Lemma 5.7, which needs the switched edges to be improvements: R15 (d)".
  - The overall row: "none open as mathematics; ... S1, S2 (citations) remain as wording items".
- Answer:
  - S1 does not touch it. It concerns Lemma S (a), the sandwich identities, not (b).
  - S2 is exactly the citation for (b)'s monotonicity, but it is a citation item, not open mathematics. Its content is the packet's own
    fallback proof:
    - N5's τ-changes are Switch_I with ∅ ≠ I ⊆ Iτ on G^d (R15 (d)).
    - VJ00 Lemma A (R15 (a)) holds for any game, so on G^d it gives U_{τ_k} ⊴^d U_{τ_{k+1}} pointwise.
    - Lemma R (R18 (d)) makes ⊴^d the exact reverse of ⊴.
    - If τ is unchanged, U_τ is unchanged (it depends on τ alone).
  - So U is non-increasing in G's order on the landed results R15 (a), (d) and R18 (d) Lemma R alone. §1 (b) stands either way.
- Recommendation for the lane's fixes file: cite (b) as "R15 (a), (d) on G^d with R18 (d) Lemma R (= Lemma S (b), whose S2 names this
  route)".

## 1. Lemma Φ: checked
- (a):
  - R15 (d): every iteration switches σ along improvements, or leaves it unchanged. A fallback switches along gates.
  - R15 (a): Ξ does not decrease pointwise. If σ is unchanged, Ξ is unchanged.
  - S1's order compares the cycle node's reward first, and p′ (hence the reward) is injective on V. So the reward of λ(v) is
    non-decreasing, with equality iff the cycle node is unchanged. Correct.
- (b): as above (PHI-N1): U_k(v)'s cycle node is λ^U_k(v), and Even's order on G compares its reward first. Correct.
- (c):
  - Each λ_k(v) strictly climbs n reward values, so it changes ≤ n − 1 times. A λ-changing transition changes some λ_k(v), so there are
    ≤ n(n − 1) of them.
  - The same holds for λ^U. A new joint λ-run starts only at a λ- or λ^U-change, giving ≤ 2n(n − 1) + 1. Correct.

## 2. Corollary Φ-1O: checked
- (a):
  - On 𝒞^1O, τ is determined by τ(o), so there are ≤ d values.
  - Every τ-changing iteration is Switch_I on G^d with I ⊆ Iτ (R15 (d)). It goes strictly up in ≺_{G^d} (R15 (c), the Theorem, on G^d).
  - So the successive τ's form a strict chain in a strict partial order: no repeats, and ≤ d − 1 changes. Correct.
- (b): phases change only at λ- or τ-changes (λ^U is a function of τ by KEY): ≤ n(n − 1) + (d − 1) + 1. Correct.

## 3. Data (DATA, not proof; docs/referee/scratch/phifx_probe.py on rl_engine, logs scratch/phifx_logs/)
- (L) is P-N5-RHO's 412-file list: 367 games run (any game, 𝒞^1O or not), 45 skipped (n > 64), from SPEC S3's start (phifx_logs/lib.log).
  - Φ (a): 278,285 reward checks. Φ (b): 278,285 checks of λ^U (Odd's dual valuation from my engine's S2 step, which the lane's tracer
    did not expose).
  - λ changed at 1,009 transitions and λ^U at 297. Joint λ-runs at most 15.3% of 2n(n − 1) + 1.
  - Φ-1O on the 253 𝒞^1O games: τ changes ≤ d − 1, phases ≤ n(n − 1) + d (max 29 phases).
  - 0 failures.
- Random games (phifx_logs/rand.log): 8,000 games, half general (n 3-10) and half 𝒞^1O (n 4-14); 4,995 of them were 𝒞^1O.
  - Φ (a), (b): 57,066 checks each. λ changes 3,160, λ^U changes 2,228. Joint λ-runs at most 15.3% of the bound.
  - Φ-1O: max 5 phases.
  - 0 failures.
- PHI-N2: the data check (b) directly (λ^U), which the packet's §3 lists as "not checked".

## §C. Comparison with REFEREE-2: docs/referee-2/R2-N5-PHI.md at referee-2 b621f9a (sha1 a62f4aef…)
Written 2026-10-25T20:27Z by date -u, after the Lead's word of 20:21Z (Lead's stamp) that b621f9a is final. I opened R2-N5-PHI only after
my report (843ba1f8) was pushed. (Opus 5.5, D15).
- Verdicts: identical. Both sign Lemma Φ (a)-(c) and Corollary Φ-1O (a), (b), and neither signs §2's "Use" or §3. No gap on either side.
- Joint gap map: EMPTY.
- The lane's question about S1 / S2: identical answers, reached independently. Both quote R-N5-1OA l. 48.
  - S1 is a citation item on Lemma S (a).
  - S2 IS the citation of (b)'s monotonicity (R15 (a), (d) on G^d with Lemma R), which is the packet's own fallback.
  - G-1OA-6 concerns Lemma S (c)-(d) and is not used.
  - (b) holds by either route.

| item | REFEREE-2 | REFEREE | outcome |
| --- | --- | --- | --- |
| S1 / S2 / G-1OA-6 vs (b) | §1: S2 is the citation; cite "R15 (a), (d) on G^d with Lemma R" | PHI-N1, same | identical |
| citation of (b) | N-PHI-2: drop the Remark's "if they do"; cite S2's resolution | PHI-N1 recommendation, same | ACCEPTED (same content) |
| Φ-1O (a) uses only "no τ repeats" | N-PHI-1 (precision) | §2 "strict chain in a strict partial order: no repeats" | ACCEPTED |
| λ^U checked in data | 3,219,607 checks, 0 rises; mutation ub bites (2,385) | PHI-N2: 278,285 + 57,066 checks, 0 failures | consistent; REFEREE-2's mutation control adds evidence that the check can fail |
| scope "every game" | proof uses nothing 𝒞^1O-specific; its data are 𝒞^1O only | my data include general (non-𝒞^1O) games: 114 library + 3,005 random | my data cover the every-game part REFEREE-2 calls thin |
| Φ-1O (a)'s bound d − 1 | REACHED in data (1000‰) | not measured | noted: the bound is tight |

- No verdict of mine changes. (Opus 5.5, D15)
