# P-N5-X fixes (box 29): the referees' repairs, written out
L-NEW successor 10 (Opus 5.5, D15/D18). Lead request 18:3xZ. Written 18:45Z onward (date -u).
- Object: packet docs/new/P-N5-X-box28.md, pinned at trunk afc88b0, sha1 b21d2d0638d08d750f26ae4dda2faaca7891fa23. The packet is NOT
  edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-X.md (referee 53c0c68), §1-§4 and its gap table.
  - REFEREE-2: report pending. Its repairs will be added in a dated section below when the Lead relays them.
- Rule: this file writes down the referees' repairs. A line of my own is marked "L-NEW".
- Scope unchanged: lemmas about the candidate N5 on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN.

## Summary (REFEREE, R-N5-X verdict table)
| packet item | REFEREE | repair below |
| --- | --- | --- |
| XW (§1), EQ (§2), FBL-N (§3), F2 (§6), FB-W (§9) | SIGNED | — |
| F1 (§5) | SIGNED WITH GAPS (X-2, closed) | §1 |
| NF (§4) | SIGNED WITH GAPS (X-3, closed) | §2 |
| Theorem X (§7) | SIGNED WITH GAPS (X-1, X-2, X-4, all closed) | §3, §4 |
| §8 table | right as a READING | — |
| (FBRE-F) | not used | — |

## 1. X-2: the bound of F1 when F = ∅ (wording)
- Replace "at most |F| − 1" in Lemma F1 (and in its uses in Theorem X steps 2 and 4) by "at most max(0, |F| − 1)".
- If F = ∅, every vertex reaches o. That forces H2 to fail, and such an interval is a single EQ block.
- In Theorem X step 2, the block count reads ≤ max(1, 2|F|). The total ≤ 3n² per F-interval absorbs it.
- DATA (REFEREE): 270 F-intervals with F = ∅, which REFEREE's probe first flagged before the bound was corrected.
- L-NEW: the same reading applies to box 29's Lemma F1° (docs/new/N5-NH2-box29.md §1).

## 2. X-3: Lemma NF, the EQ case (one line)
Replace the packet's first proof line "k is EQ: the fallback is value-preserving (§2)" by:
- If k is EQ, the gate is G_τ's improving set, so by R18 (c) every switched edge is flat, and W_{k+1} = W_k.
- Then Ξ_k ⊴ Ξ_{k+1} ⊴ W_{k+1} = W_k = Ξ_k (R15 (a), Lemma XW). So the fallback is value-preserving, and k+1 is EQ.
- This does not need k+1 to be EQ in advance; §2's proof did. REFEREE also notes that NF uses neither (h) at k+1 nor "k+1 not OTHER".

## 3. X-1: Theorem X step 4, PIECE with θ varying (REFEREE's §3.2 paragraph)
- R19 (f) is signed "θ constant not needed (N-RE-4)". N-RE-4 justifies the GATES (Lemma G (c) at each state). The COUNT of
  Ξ-or-W-changing transitions needs one more step: a θ-change changes Ξ on all of R (Ξ = π ⊕ θ) while no route and no W-value on R
  changes.
- Closure (REFEREE): in a sub-block (THR; τ, w, R constant), a transition that changes θ also changes W at a vertex of F.
  - Under H1 at k, Odd's honest choice e_k := σ̄_k(o) has an o-free honest play, which is also its (σ_k, τ)-play. So e_k ∈ F (R is
    constant on the sub-block), and θ_k = o ⊕ W_k(e_k) ((V1), Lemma G (a)).
  - Suppose W is unchanged on F at k → k+1. Then θ_{k+1} ⊴ Ω_{σ_{k+1}, e_k}(o) = o ⊕ W_{k+1}(e_k) = o ⊕ W_k(e_k) = θ_k. Here Ξ(o) is the
    minimum over o's exits (R18 (d) Lemma S (a)), and e_k's play still avoids o.
  - With θ_{k+1} ⊵ θ_k (R15 (a)), θ_{k+1} = θ_k. □
- Hence every Ξ-or-W-changing transition of a sub-block changes an 𝓡*-value (a route's (A_v, |π_v|)) or an 𝓕-value. PIECE's
  (|R| − 1) + (|F| − 1) bound then holds for the Ξ-or-W count with θ free.
- REFEREE: R19 (f) as landed is true, but its written justification needs this paragraph, and REFEREE recommends a justification note
  on R19 (f). Theorem X step 4 now cites R19 (f) TOGETHER with this paragraph.
- DATA (REFEREE): 176 θ-changes inside sub-blocks, each with a W-change on F; 136 sub-blocks, max 14 value-changing transitions
  (n 24; bound 22); 0 failures.

## 4. X-4: Theorem X step 4, flat fallbacks inside sub-blocks (citation)
- Step 4 must not cite R20 (f) (P-N5-XA-fixes §5). That result is signed only for throttled stretches with u* ≠ none, while step 4
  uses it in sub-blocks with θ varying and any u*.
- Instead, step 4 RE-DERIVES the property from the three facts the argument needs (REFEREE R-N5-XA §C5):
  - (i) the fallback changes no value: NF, since the sub-block has no crossing;
  - (ii) it switches only flat F → F edges and leaves R and (h) intact: NF's classification, which uses (h) at k and R_{k+1} = R_k,
    not FBL. So G-XA-1 for u* = none is not involved. (h) at k+1 holds because k+1 is THR;
  - (iii) Lemma P's induction step uses only the state it starts from.
- New wording of step 4's second bullet: "Its flat fallbacks change no value and switch only flat F → F edges (NF and its proof), and
  R and (h) are intact; Lemma P's induction step uses only its starting state. So both piece runs continue through them
  (re-derivation of the argument of P-N5-XA-fixes §5; R20 (f) is not cited)."

## 5. Gap ledger (REFEREE)
| id | where | kind | status |
| --- | --- | --- | --- |
| X-1 | Theorem X step 4 / R19 (f): θ-free PIECE count of Ξ-or-W changes | proof step (in R19 (f)'s justification) | CLOSED (§3); note on R19 (f) recommended |
| X-2 | F1 and step 2 when F = ∅ | wording | CLOSED (§1) |
| X-3 | NF, EQ case cites §2 | wording | CLOSED (§2) |
| X-4 | step 4 uses R20 (f) outside its hypotheses | citation | CLOSED as a re-derivation (§4) |
| REFEREE-2 | — | — | pending; repairs to be added here when relayed |
