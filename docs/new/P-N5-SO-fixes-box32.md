# P-N5-SO fixes (box 32): the referees' repairs, written out
L-NEW successor 12 (Opus 5.5, D15/D18). Lead relays 01:16Z and 01:25Z (read 01:30Z). Written 2026-10-25 by date -u.
- Object: packet docs/new/P-N5-SO-box32.md, pinned at trunk 1ef02bb, sha1 deb5ee4422da3ab7389ce35e4542977927b53886 (re-checked at this commit:
  unchanged). The packet is NOT edited; this file is its correction layer.
- Sources: REFEREE docs/referee/R-N5-LP.md Part 2 (claude/referee dcb4119); REFEREE-2 docs/referee-2/R2-N5-LP.md §8 (claude/referee-2 ba67f41,
  trunk ec7e9b6). §C items, if any, follow in a later file.
- Rule: one line per item, then the repair written out. A line of my own is marked "L-NEW".

## 0. Verdicts and items
| statement | REFEREE | REFEREE-2 | items |
| --- | --- | --- | --- |
| Lemma TH | SIGNED WITH GAP SO-1 | SIGN (N-SO-1) | SO-1 (dependency, §1); N-SO-1 (transfer of F1°, §2) |
| Lemma SO | SIGNED (dependency SO-1) | SIGN WITH GAPS G-SO-1 (closed), N-SO-3 | §3, §4 |
| Corollary XJ | SIGNED WITH GAP XJ-1 | SIGN WITH GAPS N-SO-2 (= XJ-1) | §5 |

## 1. SO-1: the full-minimiser property used in TH (H1 case) and in SO ("σ̄(o) ∈ T_k")
- Replace the citation "R25 CAP-1, REFEREE's case split" by: σ̄_k(o) is a FULL Ξ_k-minimiser over succ(o) when λ(o) ≠ o — REFEREE's case proof
  in docs/referee/R-N5-FB.md §4.2, re-checked and adopted by REFEREE-2 in docs/referee-2/R2-N5-FB.md §C.3 (claude/referee-2 eb10cf7). (REFEREE-2's
  own G-FB-4 closure proved only COARSE_{−1} minimality, which does not suffice here.)
- DATA (REFEREE): 0 exceptions to full minimality (61,968 earlier states plus every state of this review).
- L-NEW: P-N5-OE (docs/new/P-N5-OE-box32.md, §0 and Lemma OE step 1) uses the same "CAP-1 closure"; read it with this citation too.

## 2. N-SO-1: F1° on the LP phase notion (TH)
- R22 (a) F1° is signed for R22's phase key (λ_Ξ, λ_U, τ); TH uses it on crossing-free intervals of the coarser phase of P-N5-LP (λ_Ξ, τ). Its
  proof uses only λ_Ξ on F, τ, Lemma G (a), (F1) in G_τ and FBL-N (ii); none needs λ_U, so it transfers (REFEREE-2). DATA (REFEREE-2): 7,241 +
  38,680 intervals of this phase notion, 0 failures.

## 3. G-SO-1 (closed): the two strict increases in SO's frozen-key step
Replace "Ξ_{k+1}(p) ▷ Ξ_k(p) (P2, R15 (a), ⊕ keeps strictness), and then Ξ_{k+1}(x) = (the unchanged prefix) ⊕ Ξ_{k+1}(p) ▷ Ξ_k(x)" by:
- p's strict gain is RESULTS R19 (d) (SG): a switched Even vertex y with λ(y) ≠ y gains strictly in Ξ (the general phrase "⊕ keeps strictness"
  is false for set-valued ⊕, R24 TB-1 (b)).
- Along x's unchanged prefix x → … → p, ⊕ is strictly monotone: the prefix vertices lie in neither path set (Ξ_k(p), Ξ_{k+1}(p)), because a path
  before the first visit of c is simple and a repeat would close a cycle without c, against λ = c in the phase. So adding them (and +1 to the
  length per step) preserves the strict order: Ξ_{k+1}(x) ▷ Ξ_k(x), and x ∉ T_{k+1}. (REFEREE-2.)

## 4. N-SO-3: "⊕ is injective for a fixed cycle node"
- False in general (two values whose path sets differ only at o have the same o ⊕). Replace by: μ is determined by θ on the exits' values — for
  x ∈ T the value is the unique μ with o ⊕ μ = θ among values whose paths avoid o; an exit whose path passes o has value path ⊕ θ, strictly
  longer than μ, so it is never in T. (REFEREE-2.) The rest of SO is unchanged.

## 5. XJ-1 = N-SO-2 (arithmetic)
- Replace "f ≤ n_E(2n − 1)(J + 1) + J = O(n³(1 + X))" by O(d_o·n³(1 + X)) ⊆ O(n⁴(1 + X)), since J ≤ S_o ≤ d_o(2n + (n + 1)X) = O(n²(1 + X)).
- The stated T = O(m·n⁷(1 + X) + m·n⁵·K) is correct (it already used n⁴ for f); the K term is even O(m·n³·K) (REFEREE). The reading "(J-poly),
  NFB-O and the fallback count follow from (X) per phase" stands, given SO-1.
- L-NEW: P-N5-OE's Corollary OX sharpens this to J ≤ X and f ≤ n_E(2n − 1)(X + 1) + X (unrefereed).

## 6. Labels after two signatures (D18/L40)
- PROVED (L-NEW; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER: Lemma TH, Lemma SO, Corollary XJ on 𝒞^1O, with §1-§5.
- DATA (both referees): 0 violations in all SO data (REFEREE-2: 3,915 θ-fixed relevant σ̄(o) changes, the old choice leaving T every time; J = S_o
  attained; S_o − d_o(Θ + 1) ≥ −1 at the closest).
