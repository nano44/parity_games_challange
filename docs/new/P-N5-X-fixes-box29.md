# P-N5-X fixes (box 29): the referees' repairs, written out
L-NEW successor 10 (Opus 5.5, D15/D18). Lead request 18:3xZ. Written 18:45Z onward (date -u).
- Object: packet docs/new/P-N5-X-box28.md, pinned at trunk afc88b0, sha1 b21d2d0638d08d750f26ae4dda2faaca7891fa23. The packet is NOT
  edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-X.md (referee 53c0c68), §1-§4 and its gap table.
  - REFEREE-2: docs/referee-2/R2-N5-X.md (referee-2 059f492), §1-§3 (added in §6 below).
  - Both §C comparisons: REFEREE 865eadd, REFEREE-2 3a581a5. They show no disagreement and confirm the clarified R19 (f) wording
    (docs/agents/R19-note-X1.md).
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
| G-X-1 (REFEREE-2) = X-1 | Theorem X step 4: θ-free PIECE count | proof step | CLOSED by Lemma TF (§6) |
| N-X-1 (REFEREE-2) | F1 step 2 | remark | §6 |
| N-X-2 (REFEREE-2) | F2's use of R19 (b) | citation | §6 |
| N-X-3 (REFEREE-2) = X-4 | step 4's use of fixes §5 | citation | §4 and §6 |

## 6. REFEREE-2's repairs (R2-N5-X, referee-2 059f492; added 19:05Z by date -u)
Verdicts:
- F1 and NF: SIGN.
- Theorem X: SIGN WITH GAPS (G-X-1, closed).
- XW, EQ, FBL-N, F2, FB-W: SIGN. FB-W's data is vacuous: 0 qualifying evictions in REFEREE-2's runs.
- §8 table: agree.

### 6.1 G-X-1 (= REFEREE's X-1, stated sharper): Lemma TF
- With θ varying, Ξ changes on R at a θ-change without any route change. Read with Ξ on R, the per-part count "R-values change
  ≤ |R| − 1 times" of R19 (f) is FALSE.
  - Instance: experiments/new/box28/instances/fbref_n48.pg (sha1 414231a2…), transition 56 → 57.
  - It is one phase, with (h) at both ends, no fallback, w = (27, ∅, 2) constant, and R = {o} = {14}.
  - θ goes from (27, {28}, 9) to (27, {15, 28, 29}, 18). Ξ changes at 14 ∈ R, whose budget is 0, and at the F-vertices 3, 16, 19.
  - The Lead re-ran this with docs/referee-2/R2-N5-X/dump_tf.py.
  - Only the total ≤ |R| − 1 + |F| − 1 survives.
- Lemma TF (REFEREE-2, R2-N5-X §3.2). Let k → k+1 have τ constant, R_{k+1} = R_k, and (h) at k and k+1. If θ_{k+1} ≠ θ_k, then Ξ changes
  at some vertex of F_k.
  - θ_j = min over the exits e of Ω_{σ_j, e}(o) (𝒞^1O; σ̄ is pointwise optimal).
  - By H1 at j, the minimiser σ̄_j(o) lies in F_j. For e ∈ F_j, Ω_{σ_j, e}(o) = o ⊕ Ξ_j(e).
  - An exit e ∈ R gives a cycle through o, with its cycle node in R ∪ {o}, while F-exit values have their cycle node in F. So the
    minimum is attained only in F, and θ_j = min_{e ∈ F} o ⊕ Ξ_j(e).
  - With F the same at k and k+1, an unchanged Ξ on F gives θ_{k+1} = θ_k. □
  - Precision (REFEREE §C): X-1 and TF use R_{k+1} = R_k (which PIECE assumes) and need (h) at k only.
- New wording of Theorem X step 4: "PIECE's R-part counts ROUTE changes on R (W on R; the route game against the frozen terminal w).
  A θ-change is an F-value change (Lemma TF = REFEREE X-1) and is charged to the F-part. So every Ξ-or-W-changing transition of a
  sub-block is counted, and the total ≤ |R| − 1 + |F| − 1 holds."
- R19 (f), clarified wording (Lead, docs/agents/R19-note-X1.md; confirmed by both referees in §C; carried as R21 (i)): θ constant is not
  needed, provided the R-part counts route (W) changes on R; under (h) at both ends, a θ-change is an F-change (Lemma TF =
  REFEREE X-1).
- DATA (REFEREE-2, x_check.py):
  - 317 θ-changes inside F-intervals, all with an F-change;
  - 253 transitions with Ξ changing on R without a route change, all with an F-change;
  - 753 sub-blocks (211 of them θ-varying): the corrected split and the total both hold, 0 failures.

### 6.2 N-X-1: F1 step 2 needs only Lemma G (a)
At every state (EQ, THR and OTHER alike), for x, z ∈ F, (x, z) ∈ Iσ_k iff it is 𝓕-improving. This uses only Lemma G (a), which needs no
(h).
- L-NEW: this is also exactly what box 29's Lemma F1° uses (N5-NH2-box29.md §1).

### 6.3 N-X-2: F2 uses R19 (b) at a single state
R19 (b) (w = o ⊕ Ξ(τ(o))) is signed under (h) at two consecutive states. F2 uses it at k+1 alone. The identity needs only H2 at that state:
o's W-play does not return to o, so (V1) and Lemma G (a) give it.
- L-NEW: Lemma TC (ii) in box 29 uses it the same way.

### 6.4 N-X-3 (= REFEREE's X-4)
Step 4 uses P-N5-XA-fixes §5 / R20 (f) outside u* ≠ none. NF's proof supplies exactly the three facts the argument needs. Same repair as
§4 above.
