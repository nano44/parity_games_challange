# P-N5-FRZ fixes file 2 (box 34): REFEREE-2's items
L-NEW successor 15 (Opus 5.5, D15/D18). Written 2026-10-25 08:4xZ by date -u, at the Lead's request (08:38Z, 08:41Z).
- Object: packet docs/new/P-N5-FRZ-box34.md (pinned trunk 25fda0f, sha1 39df373c17d91f942ad2cb15244cd779ca7abda1). It is never edited.
- The first fixes file, docs/new/P-N5-FRZ-fixes-box34.md (sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd), is cited and FROZEN, and is not
  edited either. This file adds to it.
- Reports answered:
  - REFEREE-2: docs/referee-2/R2-N5-FRZ.md, report at referee-2 20a73ca, §C at f546b43;
  - REFEREE: docs/referee/R-N5-FRZ.md, report 3a520ce, Addendum 3171efc (row 6 only).

## 1. Map of REFEREE-2's items (the six rows of the §C joint gap map)
| row | REFEREE-2 item | kind | where it is answered |
| --- | --- | --- | --- |
| 1 | N-FRZ-2 (P^c_ℓ, B1: case (γ), P(π) = ∅, c′ even, shorter) | wording | = REFEREE FRZ-1. Repair already in fixes 168de464 §1, FRZ-1. REFEREE-2 §9 / C.2 judges the repair text correct, and adds that x = c′ cannot occur in (γ) (it would put x ∈ π, case B2). No new text. |
| 2 | N-FRZ-3 (P^c_ℓ, B-fallback B1, "x ⊕ Ω_k(s x) = Ω_k(x)" needs x ≠ λ(x)) | wording | = REFEREE FRZ-2. Repair already in fixes 168de464 §1, FRZ-2 (two sub-cases λ(x) ≠ x and λ(x) = x). Judged correct. No new text. |
| 3 | G-FRZ-1 (X-RUN: the transition leaving P can release exits, and R-STICK does not cover it) | proof gap, closed | = REFEREE FRZ-3. Repair already in fixes 168de464 §1, FRZ-3 (REL_Q ≤ d_o (C_P + 1), C_P + 1 ≤ 13(d_o + 1)n³). Judged correct. The bounds stand as stated. No new text. |
| 4 | N-FRZ-1 (ARENA §2, R → R̄ case: (C7) cited for a two-prefix comparison) | citation | NEW text, §2 below (Fact C7′, with proof, and the replacement line for ARENA). |
| 5 | N-FRZ-4 (d_o, "crossing transition", "leaves R" are not defined in the packet) | wording | NEW text, §3 below (definitions with their RESULTS sources). |
| 6 | REFEREE's NL phase-key note, accepted by REFEREE-2 (C.2 row 6) | citation | NEW text, §4 below (one line added to the packet's §0 dependencies). |

## 2. N-FRZ-1: the two-prefix twin of (C7) (row 4)
**Fact C7′ (PROVED, L-NEW succ. 15; elementary).** Let b = (c, P, ℓ) be a valuation, and let a, a′ be vertex sequences (paths) disjoint from
P and from c. Put A := a ∩ V_{>c} and A′ := a′ ∩ V_{>c}, where V_{>c} is the set of vertices more relevant than c. Then:
- a ⊕ b = (c, P ⊔ A, ℓ + |a|) and a′ ⊕ b = (c, P ⊔ A′, ℓ + |a′|) (the ⊕ rule of RESULTS R25 / P-N5-FBW §0, applied vertex by vertex);
- the order between a ⊕ b and a′ ⊕ b, and lev(a ⊕ b, a′ ⊕ b), depend only on (A, A′), |a| − |a′| and the parity of c. They do not depend
  on P or on ℓ.
Proof.
- Same cycle node c, so the comparison goes to the path sets.
- (P ⊔ A) Δ (P ⊔ A′) = A Δ A′, because P is disjoint from A and from A′. The top rank of A Δ A′ decides the order: it is good for Even if
  that vertex is even and lies on the side being compared as better, and so on. That top rank is also the level.
- If A = A′, the path sets are equal, and the lengths ℓ + |a| and ℓ + |a′| decide (shorter is better for Even iff c is even). Their order
  depends only on |a| − |a′|. The level is −1 if |a| ≠ |a′|, and ⊥ if the values are equal. □
**Corollary (the R → R̄ case of ARENA).** Let two bases b, b′ have the same cycle node c, and let a, a′ be disjoint from P(b) ∪ P(b′) ∪ {c}.
Then a ⊕ b and a′ ⊕ b compare exactly as a ⊕ b′ and a′ ⊕ b′ do, at the same level.
**Replacement line for the packet §2, Lemma ARENA, case R → R̄.** Replace the packet's line 76, "R → R̄: both frames are π ⊕ (θ or w) with the same π, so they order these edges alike (C7).", with:
- "R → R̄: z, σ_k(y) ∈ R̄_k, so Ξ_k(z) = π_z ⊕ θ_k, Ξ_k(σ_k y) = π_{σy} ⊕ θ_k, W_k(z) = π_z ⊕ w_k and W_k(σ_k y) = π_{σy} ⊕ w_k (R19 (a),
  under (h)). Here π_z, π_{σy} ⊆ R_k are the routes to o (empty for o itself).
- Under H1 and H2 the paths of θ_k and w_k after o lie in F_k ∪ {o}, so the routes avoid P(θ_k), P(w_k) and the common cycle node
  c_θ = c_w (H3).
- By Fact C7′'s Corollary, (y, z) is Ξ-improving iff it is W-improving, at the same level. So no R → R̄ edge is withheld."
- The conclusion of ARENA is unchanged: both referees signed it, and REFEREE-2's data (105,757 withheld edges, all F → R̄) agrees.

## 3. N-FRZ-4: definitions used by the packet (row 5)
Add to the packet's §0 (setting and notation):
- d_o := |succ(o)|, the out-degree of o (RESULTS R27 setting; R30).
- A CROSSING TRANSITION is a transition k → k+1 with R_k ≠ R_{k+1} (RESULTS R19-R22, R21's setting: "the crossing transitions (R changes)";
  P-N5-SN §0).
- A vertex v LEAVES R at s → s+1 if v ∈ R_s and v ∉ R̄_{s+1}, i.e. v ∈ F_{s+1} (P-N5-SN §5 Lemma LEAVE, RESULTS R30 (e)). An EXIT RELEASE is a
  leave by a successor of o; REL counts them (RESULTS R30).
- With these, every use in the packet (§5 X-RUN, §6, FRZ-3's replacement) reads as both referees read it (REFEREE-2 §6: "I used R30's and
  R21's").

## 4. REFEREE's NL phase-key note (row 6)
Add to the packet's §0, in the list of signed results used:
- "R29 (e) Lemma NL is signed under the phase key (λ_Ξ, λ_U, τ). Its proof uses Lemma G and (C7) (statewise), WM (τ only; transfer in
  R30 (c)), R25's (T) (iii) step (λ_Ξ constant) and TRANSFER (R15 only). Nothing uses λ_U, so NL holds on this packet's (λ_Ξ, τ) phases.
  (REFEREE R-N5-FRZ §1; accepted by REFEREE-2, R2-N5-FRZ §C.2 row 6.)"
- The same applies to NL-MF (§1), which uses NL (ii)-(iii) only.

## 5. Labels after both referees (from REFEREE-2 §C.1; record, not refereed text)
- Signed by both: NL-MF, Fact 0, ARENA (with row 4's line), Steps 1-2, FREEZE, RATCHET, BLOCK, SUB.
- P^c_ℓ: SIGNED WITH GAPS FRZ-1, FRZ-2 (wording, closed). REFEREE-2 adopted REFEREE's label.
- X-RUN: SIGNED WITH GAP FRZ-3 = G-FRZ-1 (closed by fixes 168de464).
- §8: not signed. G-N5-TIME stays OPEN.
