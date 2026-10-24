# P-N5-NH fixes (box 30): the referees' repairs, written out
L-NEW successor 11 (Opus 5.5, D15/D18). Lead request 20:0xZ (handover GO, item a0). Written 20:01Z onward (date -u).
- Object: packet docs/new/P-N5-NH-box30.md, pinned at trunk c7981ee, sha1 382c514300fe056d5d95b836f359b78b1374eabe (re-checked:
  `git diff c7981ee HEAD -- docs/new/P-N5-NH-box30.md` is empty). The packet is NOT edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-NH.md (referee 78d61b1), §1-§6.
  - REFEREE-2: docs/referee-2/R2-N5-NH.md (referee-2 48da84a), §1-§6.
  - Neither report has a NOT SIGNED item or a counterexample. Both referees' §C comparisons are pending (Lead 20:0xZ).
- Rule: this file writes down the referees' repairs. A line of my own is marked "L-NEW".
- Scope unchanged: lemmas about the candidate N5 on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN. U1, U2, U3, W-CYC, (NH'), (X) stay OPEN.

## Summary
| packet item | REFEREE | REFEREE-2 | repair below |
| --- | --- | --- | --- |
| §1 Lemma F1° | SIGNED | SIGN | — |
| §2 Lemma TC (i)-(iv), Consequence | SIGNED | SIGN | — |
| §3 Lemma P3′ step 1 | SIGNED WITH GAPS (P3-1, closed) | SIGN WITH GAPS (G-NH-1, closed) | §1 |
| §3 Lemma P3′ steps 2-3, bound | SIGNED (sharper count) | SIGN | §2 |
| §3 Corollary (≤ max(1, \|F\|) pieces under H2) | SIGNED | SIGN (N-NH-1) | §3 |
| §3 remark "c_θ = c_w … THR" | — | correct as a remark (N-NH-2) | §4 |
| §4 reduction (READING) | checked as READING (NH-1, NH-2) | correct as READING (N-NH-3) | §5, §6 |

## 1. P3-1 = G-NH-1: P3′ step 1 under ¬H2 with λ_W(o) = o
The packet's sentence (§3, proof step 1): "S4a's optimum restricted to R is an optimum of its arena" [of 𝓡*_w].
- Where it is justified: under H2 it is PIECE's argument (R19 (f), step 4). o's W-continuation lies in F, so an 𝓡*_w-arena strategy
  extended by σ_{k+1} on F has G_τ-values on R equal to its 𝓡*_w-values, and (F1) applies (both referees).
- Where it is not: the W frame is in route form only through λ_W(o) = o, so H2 fails. o tops its W-cycle
  C_W = o → τ(o) → π_{τ(o)} → o, and C_W \ {o} ⊆ R. A strategy that changes a vertex of C_W \ {o} changes o's own W-continuation, so
  its G_τ-values need not be its 𝓡*_w-values (o is a terminal of fixed value w = (o, ∅, 0) there). On such a piece c_θ ≻ c_w = o
  forces H1 (c_θ ∈ F), the case of TC (iii): all states OTHER.
- Status of the sentence itself: unproved, not refuted. DATA (REFEREE-2): 45 S4a steps in the batch plus 1,826 in three climbs seeded
  from wf0_cex_n16, all with σ_{k+1}|R an 𝓡*_w-arena optimum (0 mismatches). REFEREE: 268 pieces of this kind, 0 gate edges from
  C_W into R.

### 1.1 The repair: CR needs only B1's single-switch inequality at κ-strict cases
CR (R20 (d)) applies (F1) only in its B-arena cases, to σ̂ = σ_k[x → z] with (x, z) κ-strictly improving at an S4a step inside J,
κ(π_z) ≻ κ(π_{σ_k x}). The case x ∈ π_z (B2) closes a cycle inside R that does not pass o: its value at x is the same in G_τ and in
𝓡*_w, and R17's B2 analysis applies unchanged (both referees). What is needed in case B1 (x ∉ π_z) is
    (B1)  W_{k+1}(x) ⊵ (x · π_z) ⊕ w.
Proof under ¬H2, λ_W(o) = o (REFEREE-2's form, R2-N5-NH §1.2):
- x ∉ C_W. σ̂ does not touch C_W or π_z. So σ̂'s G_τ-play from x is x, π_z, o, then C_W, and its value is (x · π_z) ⊕ w. (F1) in
  G_τ gives (B1).
- x ∈ C_W \ {o}. σ_k(x)'s route is an arc of C_W, whose vertices are all at most as relevant as o = c_w ≺ c_θ. So
  κ(π_{σ_k x}) = ∅. κ-strictness forces κ(π_z) ≠ ∅ with an EVEN top t, and t ≻ c_θ ≻ o.
  - Under σ̂ the G_τ-play from x is the cycle x → z → π_z → o → τ(o) → … → x. Its top is t: the C_W arc lies below o, and the
    vertices of π_z outside κ lie below c_θ ≺ t.
  - t is even and more relevant than o, so it is a better cycle node than c_w = o for Even. By (F1), W_{k+1}(x) has a cycle node
    other than o.
  - But k+1 ∈ J and x ∈ R_{k+1} = R, so by (R1) at k+1 x's W cycle node is c_w = o. Contradiction: this case does not occur at an
    S4a step inside J.
- So (B1) holds in every case; with it Lemma P^c and the freeze go through on 𝓡*_w exactly as in CR. CLOSED.
REFEREE's form (R-N5-NH §1.3), the same argument written from the cycle: for x ∈ C_W \ {o} with x ∉ π_z, o's W-play under σ̂
becomes the cycle o → … → x → z → π_z → o, whose top t′ ⪰ t equals t (C_W-arc vertices are ⪯ o, π_z's vertices outside κ are below
c_θ ≺ t). t′ = t is even and more relevant than o, so (F1) would move x's W cycle node off c_w = o, contradicting x ∈ R with cycle
node c_w at k+1 (R1). The case is vacuous inside J. For x ∈ π_z (B2) the new cycle lies inside R, does not pass o, and R17's B2
analysis applies.
- DATA: REFEREE-2, single-switch inequality 47 (batch) + 28 (climbs) checks, 0 failures, 0 with x ∈ C_W (as the proof predicts).
  REFEREE: 0 gate edges from C_W into R inside the 268 pieces, so the vacuous branch is untested by data in either report.

### 1.2 Replacement wording for P3′ step 1 (REFEREE's wording)
Replace "S4a's optimum restricted to R is an optimum of its arena" by:
  "every B-case (F1) instance that CR uses holds: under H2 by PIECE's argument (R19 (f)); under λ_W(o) = o (¬H2) because the
  x ∈ C_W case of B1 is vacuous inside J (§1.1 above), and the x ∉ C_W case and B2 have G_τ-value equal to 𝓡*_w-value."
- Note (REFEREE §1.2): 𝓡*_w's arena is the GATE restricted to R, not 𝓡*_w's own improving set (they differ at κ-ties). Lemma P^c
  needs only that the κ-strict improving edges are in it, which they are by (R3).
- Freeze index (REFEREE §1.2, REFEREE-2 §1.2): a simple route has ≤ |R| − 1 edges; with the base case at o the freeze holds from
  transition |R| − 1 of J on. The packet's "from the |R|-th transition" is safe.

## 2. Sharper count in P3′ steps 2-3 (REFEREE §1.4)
- After the freeze, κ(π_v) and P(θ) are constant, so Ξ(v) = (c_θ, κ(π_v) ∪ P(θ), |π_v| + ℓ(θ)) moves only through |π_v|, and
  |π_v| ∈ [1, |R| − 1] (π_v ⊆ R \ {o}). The move is monotone (R15 (a); its direction is fixed by c_θ's parity). So each
  v ∈ R \ {o} has ≤ |R| − 2 such changes, and Ξ(o) = θ is constant on J.
- Total transitions with a Ξ-change on R: ≤ |R| + (|R| − 2)(|R| − 1) ≤ (n + 1)|R|. The packet's (n + 1)|R| stands as a loose
  bound.
- REFEREE-2 §1.3: on a piece a W-change on R is a Ξ-change on R and conversely (both are functions of the route with fixed
  terminals θ, w), so the count also bounds W-changes on R.

## 3. N-NH-1: the Corollary's θ part cites R21 (i) / X-1
- The packet's line "Under H1, θ = o ⊕ min over exits e ∈ F of Ξ(e) (Lemma TF's argument)" is not by itself the argument that
  θ changes only at transitions with an F-change.
- Repair (REFEREE-2 §1.4; REFEREE §1.5): under H1, R21 (i), i.e. REFEREE's X-1 = Lemma TF (H1 at the start of I, R constant,
  R18 (d) Lemma S (a), R15 (a)), makes every θ-change an F-change. If λ_Ξ(o) = o, θ = (o, ∅, 0) is constant. Under H2,
  w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F (R19 (b) needs only H2; REFEREE-2's N-X-2).
- Then pieces ≤ (#transitions changing θ or w) + 1 ≤ max(0, |F| − 1) + 1 = max(1, |F|) by F1°. If the honest frame is not in
  route form on I, there are no pieces (REFEREE §1.5).

## 4. N-NH-2: the remark "c_θ = c_w … the THR situation" needs (h)
- Replace the remark "If c_θ = c_w with both frames in route form, the two orders coincide. That is the THR situation, covered by
  Lemma G (c) and PIECE" by:
  "If c_θ = c_w with both frames in route form, the two orders coincide. Under (h) that is the THR situation, covered by Lemma G (c)
  and PIECE. Under ¬H1 ∧ ¬H2 with c_θ = c_w = o the states are EQ or OTHER (TC (iv)), not THR, and PIECE as signed does not cover
  them."
- L-NEW: in that sub-case θ = w = (o, ∅, 0), so by TC (iv) every state is EQ. An OTHER state there would need θ ≠ w, i.e.
  c_θ ≠ c_w. So the uncovered set is empty on route-form pieces with c_θ = c_w = o; I record this as a one-line READING, not
  refereed.

## 5. NH-1 = N-NH-3: name the boundary transitions of OTHER blocks
- A transition entering or leaving an OTHER block (EQ/THR → OTHER or OTHER → EQ/THR) is neither inside an F-interval of R21's
  sense nor, by the definition of ROI(I), inside an OTHER block.
- By TC's Consequence an interval I has ≤ 1 + WC(I) OTHER blocks, so ≤ 2(1 + WC(I)) such boundary transitions.
- Repair: the sum in §4 of the packet reads
      poly(n) · (1 + X + Σ_I (ROI(I) + WC(I) + B(I))),   B(I) := #boundary transitions of OTHER blocks in I ≤ 2(1 + WC(I)),
  so B(I) is absorbed: poly(n) · (1 + X + Σ_I (ROI(I) + 3 WC(I) + 2)), and with ≤ 1 + X intervals the statement of §4 is unchanged
  up to the poly(n) factor.
- In the sketch: "the parts of I outside OTHER blocks, minus the boundary transitions, are F-intervals in R21's sense (no crossing,
  no OTHER-touching transition), ≤ 2 + WC(I) of them" (REFEREE-2 §4).

## 6. NH-2: "P3′ bounds ROI on its pieces" needs one line
- ROI(I) counts R-only transitions that change Ξ OR W on R; P3′ counts Ξ-changes on R.
- Line to add (REFEREE §4): an R-only W-change on a piece (w constant) needs a route change, i.e. a switch of some y ∈ R, and (SG)
  (R19 (d)) makes Ξ(y) rise strictly, since λ_Ξ(y) = c_θ ≠ y. So every R-only value-changing transition on a piece is a Ξ-change on
  R, and P3′'s count bounds ROI on the piece. (REFEREE-2 §1.3 gives the same conclusion from "W on R is a function of the route".)
- DATA (REFEREE): 6,942 switches of R-vertices, all strict.

## 7. DATA notes from the reports (context, not repairs)
- P3′ data is nearly vacuous in REFEREE's probe: 901 route-form pieces with c_θ ≻ c_w (633 by H2, 268 by λ_W(o) = o); longest piece
  6 transitions, last κ-change index 0, at most 1 Ξ-change on R per piece. P3′ rests on the proof.
- REFEREE-2's climbs (docs/referee-2/R2-N5-NH/climb/) reach 1,017 nontrivial P3′ pieces (longest 4 in the batch; last κ-change at
  transition 6 ≤ |R|), 0 failures.
- A climb for long c_θ ≻ c_w pieces is the Lead's request for box 31 (a); its results go in docs/new/N5-U1T-box31.md, not here.
