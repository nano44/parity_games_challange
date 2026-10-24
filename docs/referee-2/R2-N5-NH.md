# R2-N5-NH: second-referee check of packet P-N5-NH (L-NEW box 30: OTHER states inside a joint λ-phase). REFEREE-2 (successor 4), 2026-10-24 19:49Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-NH (Lead 19:4xZ), pinned at trunk claude/vibrant-johnson-nxvvxo c7981ee (an ancestor of my merged tree).
Object: docs/new/P-N5-NH-box30.md, sha1 382c514300fe056d5d95b836f359b78b1374eabe (170 lines; checked at the pin; L-NEW successor 10, l-new 4d3b60d).
Background read: RESULTS R19, R20, R21 (with R21 (i), the R19 (f) clarification); P-N5-XA §5 (CR); P-N5-X §5 (F1), §4 (NF); the SPEC.
Independence: I have not read docs/referee/R-N5-NH.md. I did not run the lane's box 29 scripts; its two instances are inputs only.
Tools (docs/referee-2/R2-N5-NH/, own code on my R2-N5-RE/re_check.py definitions and own N5 with random tie-breaks; "spec" = n5.py's
state sequence): nh_check.py, nh_climb.py, run_all.sh, logs/, climb/.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| (1) §3 Lemma P3′, step 1 (coarse freeze on 𝓡*_w) | SIGN WITH GAPS | G-NH-1: one substitution is not justified as written. "S4a's optimum restricted to R is an optimum of 𝓡*_w's arena" is PIECE's step 4, and that step needs o's real W-continuation to leave R (H2). Under ¬H2 with λ_W(o) = o, an arena strategy's real values need not be its 𝓡*_w-values. CR uses the claim only through the single-switch inequality of case B1, which I prove directly (§1.2). CLOSED |
| (1) P3′ step 2 (monotone length count) and step 3 | SIGN | — |
| (1) Corollary (≤ max(1, \|F\|) pieces under H2) | SIGN | N-NH-1: under H1 the θ part needs "θ-change ⇒ F-change", i.e. R21 (i) / REFEREE's X-1 argument (H1 at the start, R constant), not only "θ = o ⊕ min over F-exits" |
| (1) remarks after the Corollary | correct as remarks | N-NH-2: "c_θ = c_w with both frames in route form … is the THR situation" holds only under (h). With ¬H1 ∧ ¬H2 and c_θ = c_w = o the states are EQ or OTHER (TC (iv)), not THR |
| (2) §2 Lemma TC (i)-(iv) and Consequence | SIGN | — |
| (3) §1 Lemma F1° | SIGN | — |
| (4) §4 reduction (READING) | correct as a READING | N-NH-3: the transitions entering and leaving OTHER blocks (≤ 2(1 + WC(I)) per interval) are not named in the sketch; they are absorbed by the poly(n) factor. Uses only F1°, TC (signed here), R21 Theorem X steps 2-5 on R21-style F-intervals (within its hypotheses) and R15 (d) |
Context: (NH'), (X), U1-U3, W-CYC and G-N5-TIME stay OPEN. FALSE (WF0) is context; its instance seeded my climb (§5).

## 1. Lemma P3′
### 1.1 Facts (R1)-(R4): checked
- (R1). Honest frame under H1: Lemma G (b)'s honest half, which needs only that o's honest continuation (in F) does not return to o. ✓
  - Honest frame with λ_Ξ(o) = o: v's honest play first meets o at the end of π_v, and o is the top of its cycle. So the value is
    (o, π_v ∩ above o, |π_v|) = π_v ⊕ (o, ∅, 0), and θ = (o, ∅, 0). ✓ (This holds even if π_v enters the honest cycle before o.)
  - The W frame is the same. ✓
- (R2). P(θ) ⊆ {o} ∪ F under H1, and P(θ) = ∅ if λ_Ξ(o) = o, so A_θ(ρ) ∩ P(θ) = ∅ for ρ ⊆ R \ {o}. The order is decided by the top of
  A_θ(ρ) Δ A_θ(ρ'), and then by length. ✓ The same holds for w.
- (R3). c_θ ∉ R \ {o}: under H1, c_θ ∈ F; otherwise c_θ = o. So every vertex of A_w(ρ) Δ A_w(ρ') outside κ(ρ) Δ κ(ρ') lies strictly
  between c_w and c_θ, below the top t of κ Δ κ'. ✓
- (R4). On R, the full path-set difference of π ⊕ θ and π' ⊕ θ is κ(π) Δ κ(π') (P(θ) is shared). So a κ-change is decided by κ, and R15 (a)
  makes it go up. ✓
- DATA: (R1) 151,926 vertex checks and (R3) 3,044 route pairs in the batch (plus 7,494 route pairs during the climbs); 0 failures (§5).
### 1.2 Step 1: the coarse freeze on 𝓡*_w, ingredient by ingredient
CR (R20 (d)) needs four things: (Cmono)/(Cstrict), Lemma C, coarse monotonicity at every transition, and in case B-arena (F1) applied to
σ̂ = σ_k[x → z] with the value formula of R17 B1/B2. I checked each substitution.
- (Cmono)/(Cstrict) → (R3). If κ(ρ) ≠ κ(ρ'), both frames decide as κ does. So a full W-order ⊵ implies κ ⪰ (Cmono), and a κ-strict
  comparison is strict in both frames (Cstrict). So a κ-strict edge inside R is a gate edge and W-improving. ✓
- Lemma C → (R1)-(R3): both frames induce the same κ-order on R. ✓
- Coarse monotonicity → (R4), at every transition, S4c included. ✓ At a fallback, σ_k is an arena optimum in G_τ, and a κ-strict gate edge
  is W-improving, hence flat (R18 (c)). That needs x = λ_W(x), but λ_W(x) = c_w ≠ x for x ∈ R \ {o}, and o is Odd. So B-fallback is
  vacuous (N-XA-1). ✓
- λ_W constant on J (needed in B1 (α) and B2): it is c_w on R by (R1), and λ_Ξ on F. ✓
- The squeeze: a route has ≤ |R| − 1 edges. "From the |R|-th transition" is a safe statement. ✓
- G-NH-1 (the substitution "S4a's optimum restricted to R is an optimum of 𝓡*_w's arena").
  - Under H2 this is PIECE's step 4: o's real continuation lies in F, so any 𝓡*-arena strategy extended by σ_{k+1} on F has real values
    equal to its 𝓡*_w-values, and (F1) applies.
  - Under ¬H2 the W frame is in route form only through λ_W(o) = o, and o's real W-continuation runs through R: o → τ(o) → π_{τ(o)} → o,
    the W-cycle C_W, whose top is o. An 𝓡*_w-arena strategy that changes a vertex of C_W changes o's real continuation, so its real values
    are not its 𝓡*_w-values. The packet's sentence does not cover this.
  - What CR actually uses is B1's inequality W_{k+1}(x) ⊵ (x · π_z) ⊕ w for a single κ-strict switch σ̂ = σ_k[x → z], x ∉ π_z, at an S4a
    step inside J. (B2, x ∈ π_z, closes a cycle inside R before o and is unaffected.) Proof of B1 under ¬H2:
    - x ∉ C_W. σ̂ does not touch C_W or π_z, so σ̂'s real play from x is x, π_z, o, then C_W. Its real value is (x · π_z) ⊕ w, and (F1)
      in G_τ gives the inequality.
    - x ∈ C_W. Then σ_k(x)'s route is an arc of C_W, whose vertices are all below o = c_w. So A_w(π_{σ_k x}) = ∅ and κ(π_{σ_k x}) = ∅
      (c_θ is above c_w). κ-strictness then forces κ(π_z) ≠ ∅ with an even top t, and t is above c_θ.
      - Under σ̂ the real play from x is the cycle x, π_z, o, τ(o), …, x. The C_W part is below o and t is the top of π_z, so its top is t.
      - t is even and above o, so it is a better cycle node than o for Even. By (F1), W_{k+1}(x) then has a cycle node other than o.
      - But x ∈ R_{k+1} (R is constant), and in route form at k+1 (k+1 ∈ J, ¬H2) x's W cycle node is λ_W(o) = o. Contradiction. So
        this case does not occur at an S4a step inside J.
    - So B1 holds in every case. With it, Lemma P^c and the freeze go through on 𝓡*_w exactly as in CR. CLOSED.
  - DATA: 1,826 S4a steps inside nontrivial P3′ pieces under ¬H2 during three climbs seeded from wf0_cex_n16, plus 45 in the batch. At
    every one, σ_{k+1}|R IS an optimum of 𝓡*_w's arena (0 mismatches). So the packet's sentence held on every case I could produce: it is
    unproved, not refuted. The single-switch inequality: 28 checks during the climbs and 47 in the batch, 0 failures, and 0 with x ∈ C_W
    (as the proof says).
### 1.3 Steps 2-3: SIGN
- After the freeze, κ(π_v) and P(θ) are fixed, so Ξ(v) = (c_θ, κ ∪ P(θ), |π_v| + ℓ(θ)) moves only through |π_v| ≤ |R| − 1, monotonically
  (R15 (a); the direction is fixed by c_θ's parity). So each v has ≤ n − 2 such changes, and the total is ≤ |R| + (n − 2)|R| + |R|. ✓
- In a piece, a W-change on R is a Ξ-change on R and conversely, since both are functions of the route with fixed terminals. So the count
  also bounds W-changes on R. ✓
- DATA: 23 nontrivial P3′ pieces in the batch (longest 4 transitions; climbs: 1,017 more), max count 4, max last κ-change at transition 6
  (≤ |R| every time), 0 failures.
### 1.4 Corollary and remarks
- Under H2, W's route form holds throughout I, and the honest one holds throughout I or never (TC (i); λ_Ξ(o) fixed in the phase).
  - w = o ⊕ Ξ(τ(o)) changes only with an F-value (F1° budget).
  - θ: if λ_Ξ(o) = o it is constant. Under H1, R21 (i) (REFEREE X-1: H1 at the start, R constant, Lemma S (a), R15 (a)) makes every
    θ-change an F-change. (N-NH-1: "θ = o ⊕ min over F-exits" alone is not the full argument; X-1 or my TF is.)
  - So pieces ≤ (#θ- or w-change transitions) + 1 ≤ max(0, |F| − 1) + 1 = max(1, |F|). ✓ DATA: max 17 pieces in an H2 interval, always ≤
    max(1, |F|); 0 failures.
- N-NH-2: "c_θ = c_w with both frames in route form … that is the THR situation, covered by Lemma G (c) and PIECE" needs (h). The case
  ¬H1 ∧ ¬H2 with c_θ = c_w = o is not THR (TC (iv): EQ or OTHER) and is not covered by PIECE as signed. It is a remark, not a claim, but it
  should say so.

## 2. Lemma TC: SIGN
- (i) ✓. Under H1, e* = σ̄(o) ∈ F (its play reaching o would return the honest play), and the honest cycle lies in the closed set F.
  Under ¬H1, every vertex of the honest cycle reaches o along it, so λ_Ξ(o) ∈ R. H2 ⟺ τ(o) ∈ F. Both are constant on I: λ_Ξ(o) is fixed
  in the phase, and τ and F are fixed on I.
- (ii) ✓. λ_W(o) = λ_W(τ(o)) = λ_Ξ(τ(o)) (τ(o) ∈ F, Ξ = W on F), fixed. So H3 and (h) are constant on I. If (h) fails, EQ would need
  λ_Ξ(o) = λ_W(o) ∈ F, which gives H1 and H3, i.e. (h).
- (iii) ✓. λ_Ξ(o) ∈ F and λ_W(o) ∈ R.
- (iv) ✓. I checked the three cases of the converse.
  - c on π_v: both plays reach c before o, and c is on the frame's cycle, so the values coincide.
  - c ∉ π_v: π_v meets C_Ξ only in a final arc [u..o) that avoids c. So o's honest path to c is disjoint from π_v, and Ξ(v) = π_v ⊕ θ;
    likewise for W.
  - c = o is included.
  EQ → OTHER ⇒ w changes, by XW and R15 (a).
- Consequence ✓. Under ¬H1 ∧ ¬H2, states are EQ or OTHER, and each new OTHER block after the first is entered from EQ, which costs a
  w-change.
- DATA: TC (i) at 39,250 states. (ii)-(iv) on every interval, by case: H1∧H2 18,177, ¬H1∧H2 2,549, H1∧¬H2 2,025, ¬H1∧¬H2 12,091.
  21 EQ → OTHER transitions, all with a w-change. The OTHER-block bound holds on every interval. 0 failures.

## 3. Lemma F1°: SIGN
- Steps 1-3 and 5-6 are R21 (e)'s, and none of them uses (h) or the state type. Lemma G (a) holds at every state (N-X-1), the S4a step's
  restriction to F is an 𝓕-arena optimum by (F1), and λ on F is λ_Ξ.
- Step 4: FBL-N (ii) needs no (h) and gives "every gate edge from F is flat". Flat switches at distinct cycle nodes have disjoint regions, so
  F-values are unchanged. R-vertices' switches do not affect F. Lemma P's invariant carries over. ✓
- DATA: 34,842 crossing-free intervals (2,982 with ≥ 2 states, 184 of these containing OTHER states): 0 failures of
  max(0, |F| − 1).

## 4. The reduction (READING): correct
- At most 1 + X crossing-free intervals. On each: F-changes ≤ max(0, |F| − 1) (F1°); OTHER blocks ≤ 1 + WC(I) (TC); the parts outside
  OTHER blocks, minus the boundary transitions, are F-intervals in R21's sense (no crossing, no OTHER-touching transition), ≤ 2 + WC(I) of
  them, each with ≤ 3n² value-changing transitions (R21 Theorem X steps 2-5, within its hypotheses).
- Inside OTHER blocks, a value-changing transition changes an F-value (counted by F1°) or is R-only (ROI). N-NH-3: the ≤ 2(1 + WC(I))
  boundary transitions should be named.
- Value-preserving runs ≤ 4n(n − 1) (R15 (d)). So poly(n)·(1 + X + Σ_I (ROI + WC)). ✓ Only signed results (R15, R17, R18, R19, R21) and
  the three lemmas signed here are used.

## 5. Mechanical checks (DATA; logs/totals.txt)
| quantity | count | violations |
| --- | --- | --- |
| runs / transitions (batch) | 12,064 / 27,186 | — |
| crossing-free intervals (≥ 2 states / with OTHER) | 34,842 (2,982 / 184) | 0 (F1°) |
| TC states / interval cases (H1H2, ¬H1H2, H1¬H2, ¬H1¬H2) | 39,250 / 18,177, 2,549, 2,025, 12,091 | 0 |
| pieces (c_θ above c_w / equal / U1) | 29,046 (2,366 / 24,341 / 2,339) | — |
| (R1) / (R3) | 151,926 / 3,044 | 0 |
| nontrivial P3′ pieces (batch / climbs) | 23 / 1,017 | 0 (freeze, count) |
| G-NH-1: S4a steps under ¬H2, 𝓡*_w-optimum test (batch / climbs) | 45 / 1,826 | 0 mismatches |
| G-NH-1: single-switch inequality (batch / climbs) | 47 / 28 (0 with x ∈ C_W) | 0 |
| Corollary (H2 intervals) | all, max 17 pieces | 0 |
Sources:
- Random o-cyclic 𝒞^1O, n 6-14: own seeds 111 and 112 (8,000 runs), SPEC seed 113 (3,000).
- Named instances, SPEC + 20 own runs each: box29's u1_n32 and wf0_cex_n16, box28's 8 instances, fbref_cex_n32, fts_best16, theta_tp32,
  returns_rt48, rtt24, wdrop_cyc, fbh_thr.
- Climb outputs (100 own + SPEC each).
- Climbs (nh_climb.py): n 9-14 from random games (4 climbs, no nontrivial P3′ piece reached), and three from wf0_cex_n16, which reach
  P3′ pieces under ¬H2. Every scored run was checked: 0 violations.

## 6. Gap list
| id | where | status |
| --- | --- | --- |
| G-NH-1 | P3′ step 1: "S4a's optimum restricted to R is an optimum of 𝓡*_w's arena" under ¬H2 (λ_W(o) = o) | CLOSED: CR needs only B1's single-switch inequality, proved in §1.2 (x ∉ C_W: real = contracted; x ∈ C_W: vacuous inside J). The sentence itself is unproved (0 counterexamples in 476 cases) |
| N-NH-1 | Corollary, θ part | cite R21 (i) / X-1 |
| N-NH-2 | remark "c_θ = c_w … THR situation" | needs (h) |
| N-NH-3 | reduction: boundary transitions of OTHER blocks | name them |

## C. Comparison with REFEREE's R-N5-NH (referee 78d61b1, trunk f42ccad; read after my push 48da84a1; written 20:03Z by date -u)
### C.1 Agreement per item
| item | REFEREE | REFEREE-2 | agreement |
| --- | --- | --- | --- |
| P3′ step 1 | SIGNED WITH GAPS (P3-1, closed) | SIGN WITH GAPS (G-NH-1, closed) | full: same gap, same closure (C.2) |
| P3′ step 2 and count | SIGNED; sharper bound ≤ \|R\| + (\|R\| − 2)(\|R\| − 1) | SIGN | full. I accept the sharper bound: \|π_v\| ≤ \|R\| − 1 gives ≤ \|R\| − 2 moves per v ≠ o, and Ξ(o) = θ is fixed |
| Corollary | SIGNED | SIGN (N-NH-1) | full. REFEREE's §1.5 cites TF / X-1 for θ, which is my N-NH-1 |
| TC, F1° | SIGNED | SIGN | full |
| Reduction (READING) | checked (NH-1, NH-2) | correct (N-NH-3) | full. NH-1 = N-NH-3. I accept NH-2 and correct my §1.3 (C.3) |
| remark "c_θ = c_w … THR" | — | N-NH-2 | mine only (wording) |
No disagreement on any verdict.
### C.2 P3-1's closure against my single-switch proof: the same argument
- Both reduce CR's use of 𝓡*_w to the (F1) instances in the κ-strict B-cases:
  - x ∉ C_W: σ̂ leaves o's W-continuation alone, so the real value is the contracted value;
  - x ∈ C_W: κ(π_{σ_k x}) = ∅, so a κ-strict target has an even top t above c_θ, the real cycle's top is t, and (F1) would move λ_W(x)
    off c_w = o inside J. So the case is vacuous;
  - B2 (x ∈ π_z): the cycle stays inside R, so contracted = real.
- REFEREE spells out why the cycle's top is exactly t (C_W arcs are ≤ o, and π_z's vertices outside κ are below c_θ). My §1.2 has this as
  "the C_W part is below o and t is the top of π_z". These are not substitutes but the same proof. REFEREE adds that the global sentence
  "may fail" (an 𝓡*_w optimum may take a κ-tie edge from C_W). That is consistent with my "unproved, not refuted".
- Its proposed wording for L-NEW ("every B-case (F1) instance holds: under H2 by PIECE's argument; under λ_W(o) = o by P3-1's vacuity") is
  right. I endorse it.
- Data on the vacuous case: neither probe saw a κ-strict gate edge from C_W into R inside a piece (REFEREE: 268 such pieces; mine: 0 of
  75 single-switch checks). My climbs give the stronger P3′ data: 1,017 nontrivial pieces and 1,871 S4a steps under ¬H2, every one an
  𝓡*_w-arena optimum. REFEREE's probe has 901 pieces, longest 6.
### C.3 NH-2, and a correction to my §1.3
- My §1.3 said: "In a piece, a W-change on R is a Ξ-change on R and conversely, since both are functions of the route with fixed terminals."
  - "Ξ-change ⇒ W-change" at a vertex is right: κ ⊆ A_w, and the length is shared.
  - "W-change ⇒ Ξ-change" at the same vertex is WRONG when c_θ is above c_w. A route change that alters only the vertices between c_w and
    c_θ, at equal length, changes W(v) but not Ξ(v). I WITHDRAW that half.
- REFEREE's NH-2 gives the right statement at the level of transitions. An R-only W-change needs a route change (w is constant), hence a
  switch of some y ∈ R. (SG) (R19 (d); λ_Ξ(y) = c_θ ≠ y) makes Ξ(y) rise strictly. So every R-only value-changing transition is a
  Ξ-change on R, and P3′'s count bounds ROI on its pieces. ✓ I accept NH-2 as the replacement.
### C.4 Joint gap map
| REFEREE | REFEREE-2 | status |
| --- | --- | --- |
| P3-1 | G-NH-1 | CLOSED (same proof); wording for L-NEW as in REFEREE §1.3 |
| (sharper count, §1.4) | — | accepted (remark) |
| NH-1 | N-NH-3 | wording (READING) |
| NH-2 | (my withdrawn §1.3 converse) | closed by (SG); REFEREE's line replaces mine |
| §1.5 θ via TF / X-1 | N-NH-1 | the same citation note |
| — | N-NH-2 | wording (remark needs (h)) |
Final verdicts (Opus 5.5, D15), unchanged:
- P3′: step 1 SIGN WITH GAPS (closed); steps 2-3 SIGN.
- Corollary, TC, F1°: SIGN.
- Reduction: correct as a READING, with NH-1 and NH-2.
(NH'), (X), U1-U3, W-CYC and G-N5-TIME stay OPEN.
