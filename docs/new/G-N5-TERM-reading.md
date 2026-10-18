# G-N5-TERM: termination of N5. L-NEW READING (successor 2, 2026-10-18 22:13Z by date -u). A proof proposal for the referees, NOT a result.
GAPS row G-N5-TERM (major, owner L-NEW). SPEC's sentence "each iteration strictly improves σ or τ (in Ξ)" is false as written
(instance below). This file proposes the repair and a proof from VJ00's lemmas. Status: unrefereed. Under CLAUDE.md the row stays
open until two referees sign or Lean checks it.

Source: Jurdziński & Vöge, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000),
pdf sha256 485a12de432a2a8c.. (opened 21:17Z). Section/lemma numbers below are from that report. Notation as there: Ωσ = (Λσ, Πσ);
⊴ is the order on play values (§4.2), pointwise on valuations (§4.3); R+ / R− are ⊕'s / ⊖'s priorities; (B, k) ⊕ v = (B ∪_M {v}, k+1).

## 0. The instance (also an apparent gap in VJ00 Lemma 5.8)
Original game:
- prio [2, 6, 0, 1], owner [0, 1, 0, 0], succ [[0, 2], [1, 3], [0], [0, 1, 2]].
- In the dual (⊕ = Odd), Odd's vertex 1 has the self-loop and the edge to 3.
- With τ(1) = 1: Ω(1) = (1, ∅, 0) and Ω(3) = (1, ∅, 1). Vertex 1 is an R− cycle node for ⊕, so longer is better there, and (1, 3)
  is an improvement by VJ00 (2).
- After the switch, Ω is identical at every vertex.
- Checked twice: by L-SI's engine, and by experiments/new/vj_bruteforce.py, which is written from VJ00 §4 only (n5/box4/vj_bruteforce.txt).
- Both of ⊕'s strategies have the same Ω, so 1 ↦ 1 is a maximum element AND has an improvement.
So VJ00 Lemma 5.8's "2 ⇒ 1" (Improve(σ) ≠ σ ⇒ σ is not a maximum), and postulate I2, fail on this game. The gap is in the proof of
2 ⇒ 3: "for some v, the predicate Prog does not hold for Ωσ along (v, Improve(σ)(v))". At a cycle node v (Λ(v) = v), Prog's
clause 3 compares only path sets (≅~_v), not lengths, so a length-only improvement at v keeps Prog true.
What is NOT affected: "1 ⇒ 2" (no improvement ⇒ maximum, proved via over-progressive valuations and Lemma 5.9) still holds. That
is the direction N5's stopping rule (S5) uses. So correctness of N5's output stands; only termination needs the argument below.
(Status: an observation on the opened report, with an instance. It is not checked against the CAV 2000 version and is not claimed
to be new.)

## 1. Lemma A (weak monotonicity for ANY subset of improvements; VJ00 Lemma 5.7's own proof)
Let I be an unambiguous set of improvements for σ (VJ00 §4.4), and σ⁺ = Switch_I(σ). Then Ωσ ⊴ Ωσ⁺.
Proof (verbatim structure of Lemma 5.7):
- Ωσ is locally under-progressive for σ (Prop. 5.3).
- For (v, w) ∈ I: Ωσ(w) ⊳ Ωσ(σ(v)), and UnderProg holds along (v, σ(v)). By Prop. 5.4 clause 2 it holds along (v, w).
- So Ωσ is locally under-progressive for σ⁺, and Lemma 5.5 gives Ωσ ⊴ Ωσ⁺. ∎
Lemma 5.7 never uses that I contains a best edge per vertex, so it holds for every subset.

## 2. Lemma B (what a flat switch looks like)
In the setting of Lemma A, suppose moreover Ωσ⁺ = Ωσ. Then for every (v, w) ∈ I:
- Λσ(v) = v (v is a cycle node);
- Λσ(w) = Λσ(σ(v)) = v;
- Πσ(w) ∩ V>v = Πσ(σ(v)) ∩ V>v = ∅;
- the lengths k(w), k(σ(v)) (second components of Πσ) satisfy: k(w) > k(σ(v)) if v ∈ R−, and k(w) < k(σ(v)) if v ∈ R+.
Proof.
- (11) gives Ωσ⁺ = Θσ⁺σ̄⁺, so Ωσ = Ωσ⁺ is locally progressive for (σ⁺, σ̄⁺) (Lemma 5.2), and Prog(Ωσ, (v, w)) holds.
- Prop. 5.1 gives Prog(Ωσ, (v, σ(v))).
- Suppose Λ(v) = ℓ ≠ v. Clause 1 gives Λ(w) = Λ(σ(v)) = ℓ. Clause 2 gives Π(v) =_ℓ Π(w) ⊕ v and Π(v) =_ℓ Π(σ(v)) ⊕ v.
  - Multiset union with {v} and +1 cancel in =_ℓ (MaxDiff over multiset differences is unchanged when the same element is added
    to both; the lengths differ by the same 1).
  - So Π(w) =_ℓ Π(σ(v)), hence Ω(w) and Ω(σ(v)) are ⊴-equivalent. That contradicts Ω(σ(v)) ◁ Ω(w).
- Hence Λ(v) = v. Clause 1 gives Λ(w) = v. Clause 3 gives Π(v) = (∅, 0) and (∅, 0) ≅~_v Π(w) ⊕ v, i.e. Π(w) ∩ V>v = ∅
  (v ∉ V>v). The same holds for σ(v).
- Two play values with the same Λ = v and empty path sets above v compare by length alone (§4.2): for v ∈ R−, k ≤ k'; for
  v ∈ R+, k' ≤ k. The improvement is strict, which gives the claim. ∎

## 3. Theorem (termination of any switch sequence, hence of N5)
For a ⊕-strategy σ, let φ(σ) = Σ_{v ∈ M⊕, Λσ(v) = v} ε(v) · k_σ(σ(v)), with ε(v) = +1 if v ∈ R−, −1 if v ∈ R+, and k_σ(u) the
length component of Πσ(u). Write σ ≺ σ⁺ iff either Ωσ ◁ Ωσ⁺ (pointwise ⊴, not equal), or Ωσ = Ωσ⁺ and φ(σ) < φ(σ⁺).
Then ≺ is a strict partial order on the finite set of strategies, and every non-empty switch of improvements σ ↦ Switch_I(σ)
goes up in ≺.
Proof.
- By Lemma A, Ωσ ⊴ Ωσ⁺. If they differ, we are done.
- If they are equal, the cycle nodes {v : Λ(v) = v} and every k_σ(u) are the same for σ and σ⁺ (they are read off the same Ω).
  The terms of φ change only at switched vertices.
- By Lemma B, each switched v is a cycle node whose term ε(v) · k strictly increases. So φ(σ⁺) > φ(σ).
- ≺ is irreflexive and transitive: the pointwise order on valuations is a partial order (§4.3), and on a fixed Ω the integer φ
  is compared. ∎
N5. In every iteration:
- Even's new σ is σ, or Switch_I(σ) with ∅ ≠ I ⊆ Iσ: step S4a changes σ only on edges of A_σ(v) \ {σ(v)} ⊆ Iσ; S4c is a switch-all
  on Iσ.
- The same holds for τ on G^d.
- Iσ / Iτ in n5.py are VJ00's improvements: SPEC S1/S2, si.py key = VJ00's ⊴ (Q1: path sets by MaxDiff; lengths as in §4.2).
- Every iteration changes σ or τ: S4 changes one of them, or the fallback does.
So (σ_k) and (τ_k) never go down in ≺ (resp. ≺ on G^d) and at least one goes strictly up. No (σ, τ) state can repeat, and the
number of iterations is at most h(≺_G) + h(≺_{G^d}), where h is the height of the order. Hence N5 terminates. ∎
What this does NOT give: a polynomial bound. h can be exponential, so the iteration count stays open (that is the gauntlet's
step 4 question). Consecutive flat iterations (neither Ωσ nor Ωτ changes) number O(n²): in each one the side that changes raises its φ, and φ, φ^d
are integers in [−n², n²] while the valuations are fixed.

## 4. Data matching the reading
- No repeated state in any run of box 4: n5_lock.py over all start pairs (n ≤ 8; 1,600 games), and the climbs.
- The Ξ-flat climb (n5_adv3.py, Lead 21:35Z) is running, with its own repeated-state detector. Results:
  docs/new/N5-killer-box4.md §8.
Requested check for the referees: re-derive Lemma B's cancellation step from VJ00 §4.5's definitions (multiset ⊕, MaxDiff over
\_M), and confirm on the §0 instance.
