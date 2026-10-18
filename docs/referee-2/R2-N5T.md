# R2-N5T: second-referee check of G-N5-TERM-reading.md (termination of N5 SSI-GLOBAL). REFEREE-2, 2026-10-18 23:00Z (date -u)
Signature: (Opus 5.5, D12). Packet P-N5T (Lead GO 22:54Z).

Object: docs/new/G-N5-TERM-reading.md at trunk 812ecba (L-NEW reading, unrefereed).
Spec: docs/new/N5-ssi-global.md at 812ecba, "Exact pseudocode" and SPEC S1-S5.
I did not read docs/referee/ before pushing this report.

Source I opened myself: Vöge & Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48.
- URL: https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf.
- pdf sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65 (same file as L-NEW's 485a12de432a2a8c..).
- Read with pdftotext: §3 (postulates P1, P2, I1, I2, Theorem 3.1), §4.1-4.5, §5.1-5.6.
- Cited below by the report's own numbering ("VJ00").

Tools: docs/referee-2/R2-N5T/, my own code written from VJ00's definitions. It imports neither n5.py nor si.py.
- vjbf.py:
  - Ωσ(v) is the min over ALL plays from v consistent with σ (VJ00 §2.2 finite plays, enumerated). It does not use (11) or any
    counter-strategy procedure.
  - Θ, ⊴, MaxDiff and "improvement" are taken from §4.1-4.4.
  - For every σ and every non-empty unambiguous set I of improvements, it checks Lemma A, Lemma B (all four conclusions) and the
    Theorem's step (φ strictly up on a flat switch).
- inst0.py: the reading's §0 instance.
- mutants.py: shows the checker can fail.
- i1check.py: VJ00 postulate I1 (§4 below).
- si_vs_bf.py: cross-check of the object under test (si.py), §5 below.

## Verdict: SIGNED WITH GAPS (Opus 5.5, D12)
Lemma A, Lemma B and the Theorem are correct as stated. Every cited VJ00 item says what the reading uses.
Termination of N5 follows. That is the correctness half of gauntlet step 4 for G-N5-TERM. The running-time half stays open.
The argument does NOT use VJ00 Lemma 5.8's "2 ⇒ 1" or "2 ⇒ 3" (§3). The §0 observation is CONFIRMED and extends to postulate
I1 (§4).
Gaps (none blocks the signature; all are listed for GAPS/RESULTS):
- G-N5T-1 (minor, the code link). The Theorem's N5 paragraph says "Iσ / Iτ in n5.py are VJ00's improvements". This is a claim
  about code, not mathematics.
  - What I signed is the statement for SPEC N5, with Ξ = VJ00's Ω, which is how SPEC S1 defines Ξ: "minimising this order at
    every vertex at once".
  - My cross-check of si.py (Even side, 3,000 random games, 23,943 strategies) agrees exactly (§5).
  - I did not check n5.py's dual construction for Odd's side. That is L-COMP's step-2 check.
- G-N5T-2 (scope). The statement is termination only. The bound h(≺_G) + h(≺_{G^d}) can be exponential, so no polynomial bound
  follows. The reading says so itself.
- G-N5T-3 (not checked, outside the packet). The correctness of N5's output at S5 rests on VJ00 Lemma 5.8's "1 ⇒ 2" proof via
  Lemma 5.9 and Prop. 5.10.
  - VJ00 gives Lemma 5.9 and Prop. 5.10 without proof ("proved similarly to Lemma 5.5").
  - I did not re-derive them. The reading does not claim them, and the solutions are verified by Oink and verify.py in any case.
Notes (wording, no effect on validity): N1-N4 in §2.

## 1. Lemma A (weak monotonicity): CORRECT
VJ00 §4.4 defines Improve(σ) = Switch_I(σ) "for some set I ≠ ∅ of improvements". Lemma 5.7 (σ ⊑ Improve(σ)) is therefore
already stated for every non-empty unambiguous I, so Lemma A is Lemma 5.7 itself (N2). I re-read its proof:
- Prop. 5.3 (Ωσ under-progressive for σ).
- UnderProg along (v, σ(v)), then Prop. 5.4 clause 2 with Ωσ(σ(v)) ⊴ Ωσ(w).
- Lemma 5.5.
None of these steps uses a best edge.
- VJ00 states Prop. 5.4 without proof, so I checked clause 2 myself:
  - Ξ(w) ⊴ Ξ(u) gives Λ(w) ≼ Λ(u). So Λ(v) ≼ Λ(u).
  - If Λ(v) = Λ(u) = ℓ, then Λ(v) ≼ Λ(w) ≼ Λ(u) forces Λ(w) = ℓ, so clauses 2/3 for w apply.
  - ⊕v is monotone for E_ℓ and for Ẽ_ℓ: adding the same element to both multisets leaves MaxDiff of the multiset differences
    unchanged, and both lengths move by +1.
- DATA: 0 Lemma A failures in 936,826 switches (table in §6).

## 2. Lemma B (flat switch): CORRECT, including the requested cancellation step
Setting: Ωσ⁺ = Ωσ and (v, w) ∈ I.
- Prog(Ωσ, (v, w)). Prop. 5.1 for σ⁺ says Ωσ⁺ is locally progressive for σ⁺ and σ̄⁺, and (v, w) = (v, σ⁺(v)) ∈ E_{σ⁺σ̄⁺}.
  Since Ωσ⁺ = Ωσ, Prog(Ωσ, (v, w)) holds. The reading routes this through (11) and Lemma 5.2. That is valid, but Prop. 5.1 alone
  suffices (N1).
- Prog(Ωσ, (v, σ(v))): Prop. 5.1 for σ.
- Case Λ(v) = ℓ ≠ v (cancellation; re-derived from §4.2 and §4.5):
  - Clause 2 gives Π(v) =_ℓ Π(w) ⊕ v and Π(v) =_ℓ Π(σ(v)) ⊕ v. Here =_ℓ is the equivalence of the preorder E_ℓ on M(V) × N.
  - For pairs, (B, k) =_ℓ (B', k') means B =_ℓ B' and k = k' (both length clauses of E_ℓ).
  - ≼ on multisets is antisymmetric: for B ≠ C the element MaxDiff lies in exactly one of B \_M C and C \_M B, and the two
    clauses defining B ≺ C and C ≺ B then exclude each other. So B =_ℓ C iff the restrictions of B and C to V>ℓ are equal as
    multisets.
  - Adding the same element v to both sides cancels in multiset equality, whether v ∈ V>ℓ or not. The +1 on both lengths cancels too.
  - Hence Π(w) =_ℓ Π(σ(v)) with equal lengths, so Ω(w) and Ω(σ(v)) are E-equivalent (clause 1 gives Λ(w) = Λ(σ(v)) = ℓ).
  - That contradicts Ω(σ(v)) ◁ Ω(w), since ◁ is defined as "E and not reverse-E". This needs no antisymmetry of E.
- Case Λ(v) = v:
  - Clause 3 gives Π(v) = (∅, 0) and (∅, 0) ≅~_v Π(w) ⊕ v, i.e. the path part of Π(w) ⊕ v restricted to V>v is ∅. Since v ∉ V>v,
    Π(w) ∩ V>v = ∅. The same holds for σ(v).
  - Ω(w) and Ω(σ(v)) are play values, whose sets lie inside V>v by (1), so both path sets are ∅.
  - E_v then compares lengths only: for v ∈ R−, k ≤ k'; for v ∈ R+, k' ≤ k. Strictness gives the stated inequalities.
- DATA: 0 Lemma B failures in 33,103 flat switches. All four conclusions were checked separately (§6).
- N3: the reading's last bullet is clearer if it says "play values (1)" when it uses Π(w) ⊆ V>v.

## 3. Theorem (Ω, φ) and N5: CORRECT. VJ00 Lemma 5.8's "2 ⇒ 1" / "2 ⇒ 3" is NOT used
- Strict partial order.
  - E on PlayValues is linear (§4.2, after (1)), so pointwise E on Valuations is a partial order (§4.3).
  - (Ω, φ)-lexicographic comparison with φ an integer is therefore irreflexive and transitive.
- Flat case.
  - Cycle nodes and every k_σ(u) are read off the same Ω, so only the switched terms of φ change.
  - By Lemma B each switched v is a cycle node, and ε(v)·k rises by at least 1.
  - Mutant M3 (φ summed over all ⊕ vertices) also never fails, which is consistent with this: only cycle nodes switch in a flat step.
- N5 fits (SPEC S4).
  - S4a: σ_new(v) ∈ A(v) = {σ(v)} ∪ Iσ-targets. So σ_new = Switch_I(σ) with I = {(v, σ_new(v)) : σ_new(v) ≠ σ(v)} ⊆ Iσ.
  - S4b: the same for τ on G^d.
  - S4c (fallback): one edge per vertex, from Iσ (or Iτ), non-empty.
  - The loop runs only while Iσ ∪ Iτ ≠ ∅, and S4c fires exactly when S4a/b changed nothing. So every iteration changes σ or τ.
  - One fact the reading uses without stating it (N4): Iσ and Ξσ are functions of σ alone (Ωσ minimises over all of Odd's
    plays). τ only selects WHICH subset of Iσ is switched, so the σ-sequence is a VJ00 improvement sequence with stutters.
    The same holds for τ.
  - So (σ, τ) never repeats, and #iterations ≤ h(≺_G) + h(≺_{G^d}).
- "Consecutive flat iterations O(n²)" is correct, with an explicit constant:
  - 0 ≤ k ≤ n − 1, so |φ|, |φ^d| ≤ n(n − 1).
  - In a flat iteration neither potential drops and at least one rises.
  - So there are at most 4n(n − 1) consecutive flat iterations.
- Lemma 5.8 is not used. The VJ00 items used are:
  - Lemma A: Prop. 5.3, Prop. 5.4 (2), Lemma 5.5 (with Prop. 5.6).
  - Lemma B: Prop. 5.1, the definitions of Prog, ⊕, E_ℓ, Ẽ_ℓ, (1).
  - Theorem: §4.3.
  The stop rule S5 uses only "no improvement ⇒ maximum" (the proof of 1 ⇒ 2 via (12)); see G-N5T-3.
  This answers the Lead's question: the argument does not need "Improve(σ) ≠ σ ⇒ σ not maximum".

## 4. The §0 observation: CONFIRMED, and postulate I1 fails as well
- inst0.py (my Ω, plays enumerated) on the reading's game, dual side (⊕ = Odd of G, owner 0 in G^d):
  - τ(1) = 1: Ω = [(0,∅,0), (1,∅,0), (0,∅,1), (1,∅,1)]. Improvements: [(1, 3)]. φ = 0.
  - τ(1) = 3: the same Ω. Improvements: none. φ = 1.
  - So 1 ↦ 1 is a maximum and still has an improvement. Lemma 5.8 "2 ⇒ 1" and I2 fail, exactly as the reading says.
  - The faulty sentence is in the proof of 2 ⇒ 3 ("for some v, the predicate Prog does not hold ... along (v, Improve(σ)(v))").
    At a cycle node, Prog clause 3 uses Ẽ, which ignores lengths.
- New (i1check.py, exhaustive n = 3): I1 ("σ not a maximum ⇒ σ ⊑ Improve(σ) and Improve(σ) ⋢ σ") also fails for VJ00's
  Improve, which allows any non-empty I.
  - There are 4,272 (game, σ, single flat improvement) triples with σ not a maximum.
  - Smallest example, a one-player game:
    - Game: prio [0, 2, 4], all vertices Even's, succ 0→{1}, 1→{0, 1}, 2→{0, 1}.
    - σ = (0→1, 1→0, 2→0). Then Ω(1) = (1,∅,0), Ω(0) = (1,∅,1), Ω(2) = (1,{2},2).
    - (1, 1) is an improvement: vertex 1 ∈ R+, and (1,∅,0) beats (1,∅,1) because shorter is better.
    - Switching it leaves Ω unchanged.
    - σ is not a maximum, because (2, 1) gives Ω(2) = (1,{2},1).
  - So VJ00 §5.6's P1 sentence ("Lemmas 5.7 and 5.8 imply that after a finite number of iterations ... Improve(σ) = σ") is
    unsupported as written. P2's first step ("from Lemma 5.8 it follows that Improve(σ) = σ") uses the false I2.
  - The reading's Theorem is exactly the repair for termination: every Improve sequence ends in a σ with no improvement. Then
    1 ⇒ 2 makes that σ a maximum, which gives P1.
  - Correctness at a stop with no improvement only needs (12), so N5's S5 is unaffected.
  - Status as in the reading: an observation on the opened BRICS report, not checked against the CAV 2000 version, not claimed
    new. (Lead reading needed whether to route the I1 instance to L-LIT together with the reading's item (d).)

## 5. Cross-check of the object under test (supports G-N5T-1; DATA)
si_vs_bf.py compares si.py Engine.evaluate and Engine.improving (SPEC S1/S2; si.py unchanged between 812ecba and my HEAD)
against vjbf.omega and vjbf.improvements.
- Setup: 3,000 random games, n = 2..7, out-degree 1-3, priorities in 0..n with ties; every Even strategy (23,943).
- Result: 0 valuation mismatches (cycle node, path mask, length) and 0 improvement-set mismatches.
Output: si_vs_bf.txt.

## 6. Data (docs/referee-2/R2-N5T/*.txt; each run takes 1-8 s)
| run | games | switches (σ, I) | strict | flat | Lemma A fail | Lemma B fail | φ fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ex3: all 3-vertex games up to relabelling (relevance = index, 8 parities × 8 owner maps × 343 successor maps) | 21,952 | 68,776 | 60,428 | 8,348 | 0 | 0 | 0 |
| rnd 4-5 (seed 1; each game and its dual) | 4,000 | 98,857 | 93,564 | 5,293 | 0 | 0 | 0 |
| rnd 6-7 (seed 2; each game and its dual) | 6,000 | 769,193 | 749,731 | 19,462 | 0 | 0 | 0 |
"Switches" covers EVERY non-empty unambiguous subset of the improvements of EVERY strategy. That is a superset of any N5 step,
and of any fallback.
Mutants (mutants.py on ex3; mutants.txt):
- M1 (sign of ε flipped): 8,348 φ failures.
- M2 (length order reversed): 18,920 Lemma A failures and 8,460 Lemma B failures.
- M3 is not a fault (§3).
So the checker detects broken definitions.

## 7. For the Lead
- G-N5-TERM (correctness half) now has one referee signature: REFEREE-2, (Opus 5.5, D12), at 812ecba, with gaps G-N5T-1..3.
  The row closes on a second signature. The running-time half stays open.
- Suggested reading fix (L-NEW's file; not mine to edit):
  - Lemma A = Lemma 5.7 (N2).
  - Prop. 5.1 instead of (11) and Lemma 5.2 in Lemma B (N1).
  - State N4 (Iσ depends on σ only).
  - Add the I1 instance to §0.
