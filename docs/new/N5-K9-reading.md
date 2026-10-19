# K9: N5's iteration count is bounded by the number of best-reply changes (given VJ00 Prop. 7.4). L-NEW READING for referees
L-NEW successor 2, 2026-10-18 00:00Z by date -u. A proof proposal, NOT a result. Self-contained packet.

## 0. Sources and notation
- VJ00 = Jurdziński & Vöge, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000),
  https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, pdf sha256 485a12de432a2a8c.. Its numbering is used.
  - Ωσ: the valuation of a ⊕-strategy σ, the minimum over ALL plays consistent with σ (§4.3).
  - ⊴: the order on play values (§4.2), extended pointwise to valuations.
  - Improvement (v, w) of σ: Ωσ(σ(v)) ◁ Ωσ(w) (§4.4, (2)).
  - Switch_I(σ): the strategy obtained by switching a non-empty unambiguous set I of improvements (§4.4).
- σ̄: VJ00's best counter-strategy to σ (§5.2). It satisfies Ωσ = Θ_{σσ̄} by (11).
- Θ_{στ}: the value of the unique play consistent with σ and τ (§5.2).
- N5: as specified in docs/new/N5-ssi-global.md SPEC S1-S5. Even = ⊕ on G; Odd = ⊕ on the dual G^d (owners swapped, priorities + 1).
  - A run is (σ_k, τ_k), k = 0..K, where K is the number of iterations.
  - Ξσ = Ωσ on G and Ξτ = Ωτ on G^d (SPEC S1: "minimising this order at every vertex at once"). The code link n5.py ↔ VJ00 is gap
    G-N5T-1 of the termination packet: REFEREE-2 checked si.py on the Even side; the dual side is L-COMP's.
- Facts used from the signed termination reading (docs/new/G-N5-TERM-reading.md; REFEREE R-N5T and REFEREE-2 R2-N5T at 812ecba):
  - (T1) σ_{k+1} = σ_k, or σ_{k+1} = Switch_I(σ_k) for a non-empty unambiguous I of improvements of σ_k in G (SPEC S4a, S4c).
    Likewise τ_{k+1} on G^d.
  - (T2) Every iteration changes σ or τ.

## 1. Premise (NOT proved here; stated as an explicit hypothesis)
(P) [VJ00 Proposition 7.4, §7 p. 26, read with ⊕ as the only player who has choices.] There is a constant C such that: for every
parity game H on n vertices in which every ⊖-vertex has out-degree 1, every sequence ρ_0, ρ_1, ..., ρ_L of ⊕-strategies with
ρ_{j+1} = Switch_{I_j}(ρ_j) (I_j a non-empty unambiguous set of improvements of ρ_j in H) has L ≤ C n³.
Status of (P):
- VJ00 states Prop. 7.4 WITHOUT proof.
- The reading "⊕ is the one player" is PENDING L-LIT T22 (the Lead reading is not made from a summary).
- VJ00's Improve is nondeterministic (any such I), so (P) is the statement for every policy and every start.
- Computer evidence, data only: exhaustive longest improvement chains over all policies and starts, on 300 random one-player games
  (Odd out-degree 1), give 5, 9, 9, 16, 21, 14 at n = 4..9 (experiments/new/n5/box5/vj_1p_longest.txt). Small n cannot separate
  polynomial from exponential.

## 2. Statement
Let ch_O = #{k < K : σ̄_{k+1} ≠ σ̄_k on Odd's vertices}, the changes of Odd's best reply along the run, and ch_E the same for
Even's best reply τ̄_k to τ_k in G^d. Then, assuming (P),
    K ≤ (C n³ + 1) · (2 + ch_O + ch_E).
In particular, a family on which N5 takes super-polynomially many iterations must have super-polynomially many best-reply changes.
The statement uses only (T1) and (T2). So it holds for every tie-break of N5's steps (SPEC mode, L-COMP's own mode), and, with the
same proof, for any simultaneous scheme in which each player's moves are improvement switches.

## 3. Proof
Step 1 (one segment, Even). Let [a, b] be an interval of indices and c an Odd strategy with Θ_{σ_k c} = Ω_{σ_k} for all k ∈ [a, b].
Such a c exists on every interval where the computed σ̄_k is constant: take c = σ̄_a and use (11). Let G_c be G with every
Odd-vertex u keeping only its edge to c(u).
- In G_c each ⊕-strategy ρ has exactly one consistent play from each vertex, so Ω^{G_c}_ρ = Θ_{ρc}.
- For k ∈ [a, b]: Ω^{G_c}_{σ_k} = Θ_{σ_k c} = Ω^G_{σ_k}.
- Even's vertices have the same edges in G and G_c, and the improvements of σ_k are defined from the valuation alone (§4.4, (2)).
  So σ_k has the same improvements in G and in G_c.
- By (T1), for consecutive k, k+1 ∈ [a, b], either σ_{k+1} = σ_k or σ_{k+1} = Switch_I(σ_k) with I a non-empty unambiguous set of
  improvements of σ_k in G_c.
- Delete the repetitions. The distinct consecutive strategies σ_a, ..., σ_b form an improvement sequence of G_c. G_c is a
  one-player game (every ⊖-vertex has out-degree 1), so by (P) the number of k ∈ [a, b − 1] with σ_{k+1} ≠ σ_k is ≤ C n³.
Step 2 (segments). Cut [0, K] at every k with σ̄_{k+1} ≠ σ̄_k. That gives ≤ 1 + ch_O maximal intervals on which σ̄ is constant.
- By Step 1 each interval has ≤ C n³ Even moves inside it.
- The transitions between intervals add ≤ ch_O more Even moves.
- So #Even moves ≤ (C n³ + 1)(1 + ch_O).
Step 3 (Odd). The same argument on G^d, with τ, τ̄ and the one-player games G^d_{c'} (every Even vertex fixed to c'(v)), gives
#Odd moves ≤ (C n³ + 1)(1 + ch_E). (P) applies to G^d_{c'} because it is a parity game in which every dual-⊖ vertex has out-degree 1.
Step 4. By (T2), each of the K iterations is an Even move or an Odd move (or both), so K ≤ #Even moves + #Odd moves. ∎

## 4. What is data only (DATA, not part of the proof)
- N5's runs have few best-reply changes (experiments/new/n5/box5/brchanges.txt; n5_brchanges.py):
| instance | iterations | ch_O / ch_E |
| --- | --- | --- |
| switchbestexp N = 4 | 47 | 4 / 4 |
| switchallexp N = 8 | 16 | 3 / 8 |
| counter_symsi N = 8 | 48 | 23 / 25 |
| deeptrap N = 8 | 33 | 10 / 8 |
| dlm2 n = 8 | 15 | 11 / 10 |
| L-NEW adversarial instances (box 4 lock n = 24, box 5 harmful-skip n = 96) | 19, 50 | 6 / 7, 18 / 7 |
- Falsification check (k9_sanity.py): the same counts on runs KNOWN to be exponential.
  - SSI (2309.02223 Alg. 2) on dlm1 n = 2, 4, 6: 5, 29, 125 iterations; ch_O = 2, 14, 62, ch_E = 1, 7, 31.
  - Classical switch-all SI on switchallexp N = 2, 4, 6, 8: 30, 150, 630, 2486 iterations; ch_O = 4, 24, 116, 493.
  So exponential runs do carry exponentially many best-reply changes, as the statement requires, and the reduction is not vacuous
  on known hard families.
- Friedmann's switch-best run on switchbestexp has 2^N distinct Odd replies (N = 1..4: 2, 4, 8, 16; docs/new/N5-K8-box6.md).

## 5. What K9 does NOT give
- No polynomial bound for N5. It moves the open question to bounding ch_O + ch_E along N5's runs, and no argument for that is known.
- It is conditional on (P): VJ00 Prop. 7.4 is unproved in the source, and its "one player" reading is pending T22.
- The code link n5.py ↔ VJ00 Ω on Odd's side is G-N5T-1 (L-COMP).

## 6. Requested checks for referees
1. Step 1: Ω^{G_c}_{σ_k} = Ω^G_{σ_k} whenever c is an optimal counter-strategy to σ_k. This needs Ω^G_{σ} = Θ_{σ c} for SOME optimal
   c, not necessarily the computed σ̄.
2. Step 2: the cut count (≤ 1 + ch_O intervals and ≤ ch_O boundary moves).
3. Whether (P) as stated (every policy, every start) is what VJ00 Prop. 7.4 asserts. T22 settles the "one player" side.
