# Referee report R-N5-NH: OTHER states inside a joint λ-phase of N5 (box 30)

Referee: REFEREE (successor 4), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-NH: the Lead's message of 2026-10-24 19:4xZ
(read 19:41Z). Pin: trunk claude/vibrant-johnson-nxvvxo c7981ee (an ancestor of my merged HEAD). Object: docs/new/P-N5-NH-box30.md, sha1
382c514300fe056d5d95b836f359b78b1374eabe (verified at the pin). L-NEW successor 10, l-new 4d3b60d.
Context read: SPEC S1-S5; RESULTS R15, R17-R21; my R-N5-RE, R-N5-XA (§5 CR, §C4 N-XA-1), R-N5-X (§3.2 X-1 = Lemma TF). docs/new/N5-NH2-box29.md
was used for background only; the packet governs. docs/referee-2/ was NOT read for this packet.
Written 2026-10-24 19:42Z-19:48Z by date -u. Every verdict is labelled (Opus 5.5, D15).

## Verdict
| item | verdict (Opus 5.5, D15) |
|---|---|
| (1) Lemma P3′ (§3), step 1 (coarse freeze on 𝓡*_w) | SIGNED WITH GAPS: P3-1. When the W frame is in route form by λ_W(o) = o (so H2 fails), 𝓡*_w is NOT a faithful contraction for the vertices of o's W-cycle C_W ⊆ R: switching one of them changes o's own continuation. So "S4a's optimum restricted to R is an optimum of 𝓡*_w's arena" is not justified there. The F1 instances that CR actually uses still hold, because every κ-strict improving edge from a C_W-vertex is vacuous inside J (§1.3). CLOSED by that argument. The other substitutions are checked one by one in §1.2 |
| (1) Lemma P3′ step 2 (monotone-length count) and the bound (n + 1)\|R\| | SIGNED (the count is in fact ≤ \|R\| + (n − 2)(\|R\| − 1)) |
| (1) Corollary: ≤ max(1, \|F\|) pieces per interval under H2 | SIGNED |
| (2) Lemma TC (i)-(iv) and its Consequence | SIGNED |
| (3) Lemma F1° | SIGNED |
| (4) Reduction (§4, READING) | checked as a READING, with one gap: NH-1, the boundary transitions of OTHER blocks are not named in the sum (≤ 2(1 + WC(I)), absorbed). It uses only signed results within their hypotheses, plus F1° and TC from this packet. The Consequence "P3′ bounds ROI on its pieces" needs one more line (NH-2: an R-only W-change needs a switch on R, which changes Ξ there by (SG)) |
No statement is NOT SIGNED. No counterexample. (NH'), (X), U1-U3, W-CYC and G-N5-TIME stay OPEN. DATA for P3′ is nearly vacuous (§5).

## 1. Lemma P3′ (§3)
### 1.1 Facts (R1)-(R4): checked
- (R1). Honest frame under H1: Lemma G (b)'s honest half; o's honest continuation lies in F (TC (i)) and avoids π_v. Honest frame with
  λ_Ξ(o) = o: v's play reaches o along π_v, and o tops its cycle, so v's value is (o, A(π_v), |π_v|). Vertices of π_v may lie on o's cycle,
  but none is the cycle node. The W frame is the same. Correct.
- (R2). P(θ) ⊆ {o} ∪ F under H1, and ∅ if λ_Ξ(o) = o. So A_θ(ρ) ∩ P(θ) = ∅ for routes ρ ⊆ R \ {o}, and the comparison is the top of
  A_θ(ρ) Δ A_θ(ρ′), then length. The same for w (P(w) ⊆ {o} ∪ F under H2, ∅ if λ_W(o) = o). Correct.
- (R3). A_w(ρ) ⊇ A_θ(ρ). The extra vertices lie strictly between c_w and c_θ. c_θ itself is on no route: under H1 it lies in F, and if
  λ_Ξ(o) = o it is o. So the top t of κ Δ κ′ is the top of A_w Δ A_w′, with the same parity. Correct.
- (R4). θ is constant on J and Ξ(v) = π_v ⊕ θ is non-decreasing (R15 (a)), and R is constant on I. So κ(π_v) can change only upward.
  Correct.
### 1.2 Step 1, substitution by substitution (the Lead's item (1))
CR (R20 (d)) is R17's Lemma P / Theorem PH in the coarse order. It uses: (Cmono), (Cstrict), Lemma C (coarse values agree across frames
and are non-decreasing at EVERY transition), (V1c)/(V2c), (F1) for the S4a arena at B-cases, λ_W constant, the vacuous B-fallback case
(N-XA-1), and the squeeze. On 𝓡*_w (R with o a terminal of value w; COARSE := (cycle node, path vertices above c_θ), so on o-routes it is
κ plus the constant P(w) ∩ V*):
- (Cmono)/(Cstrict): generic for any threshold vertex (my R-N5-XA §1). Correct.
- "κ-strict ⇒ gate edge": a κ-strict comparison between routes is strict in the honest order (R3), so a κ-strict improving R → R edge is a
  gate edge, i.e. in the S4a arena. This replaces Lemma C's role in B_c (R20 needed coarse Ξ = coarse W for this). The comparisons in B_c are
  between routes only: R is constant, σ_k(x) ∈ R, and z ∈ R inside 𝓡*_w. Correct.
- Coarse monotonicity at every transition (A1 uses Ω^c_k(x) ⪯ Ω^c_{k+1}(x)): on R this is κ-monotonicity (R4), valid at S4a and S4c
  transitions alike. Correct.
- B-fallback vacuous: at an S4c fallback σ_k is the G_τ arena optimum (R18 (d)). A κ-strict gate edge is W-improving in G_τ (R1, R3), hence
  flat (R18 (c)). That needs x = λ_W(x), but λ_W(x) = c_w ∉ R \ {o} for x ∈ R \ {o}. Correct (N-XA-1 transfers).
- λ_W constant on J (used in B1 (α) and B2): on R it is c_w (R1, w constant); on F it is λ_Ξ. Correct.
- Squeeze: every x ∈ R \ {o} routes to o at every state of J. A simple route has ≤ |R| − 1 edges; with the base case at o (REFEREE-2's
  G-RE-3 form) the freeze holds from transition |R| − 1 on, so the packet's "|R|-th" is safe.
- (F1) at B-arena cases: "S4a's optimum restricted to R is an optimum of 𝓡*_w's arena". Under H2, o's W-continuation lies in F. An
  𝓡*_w-arena strategy ρ, extended by σ_{k+1} on F, has G_τ-values on R equal to its 𝓡*_w-values (PIECE's argument, R19 (f)). Correct. Note
  that 𝓡*_w's arena is the GATE restricted to R, not 𝓡*_w's own improving set (the two differ when κ ties). Lemma P^c needs only that κ-strict
  improving edges are in it, which they are.
### 1.3 P3-1: the W frame in route form by λ_W(o) = o
- Here H2 fails, o tops its W-cycle C_W = o → τ(o) → π_{τ(o)} → o, and C_W \ {o} ⊆ R. The piece needs c_θ ≻ c_w = o, so the honest frame is
  in route form by H1 (c_θ ∈ F); this is TC (iii)'s case, all states OTHER.
- For x ∈ C_W \ {o}, the strategy σ̂ = σ_k[x → z] changes o's own W-continuation. The G_τ-value of σ̂ at x then need not be its 𝓡*_w-value
  (o terminal, fixed value w = (o, ∅, 0)). So the packet's sentence is not justified for these x, and the global claim may fail: an 𝓡*_w
  optimum may switch x along a κ-tie edge whose G_τ-value differs.
- Closure (referee's). CR uses (F1) only at B_c cases: (x, z) κ-strictly improving, i.e. κ(π_z) ≻ κ(π_{σ_k x}). For x ∈ C_W \ {o},
  κ(π_{σ_k x}) = ∅: π_{σ_k x} lies on C_W, and every C_W vertex is at most as relevant as o = c_w ≺ c_θ. So κ(π_z) ≠ ∅ with an EVEN top t,
  more relevant than c_θ and hence than o.
  - Under σ̂, if x ∉ π_z (B1), o's W-play becomes the cycle o → … → x → z → π_z → o, whose top is t′ ⪰ t. t′ = t, since every other vertex of that
    cycle is less relevant than t: C_W-arc vertices are at most as relevant as o, and π_z's vertices outside κ are below c_θ ≺ t. So t′ = t is even and more relevant than o: a better cycle node than c_w.
  - By (F1), W_{k+1}(x) has cycle node ≠ c_w. But x ∈ R_{k+1} = R has cycle node c_w (R1 at k+1). This is a contradiction, so the case is
    vacuous inside J.
  - If x ∈ π_z (B2), the new cycle lies inside R and does not pass o. Its value at x is the same in G_τ and in 𝓡*_w, and R17's B2 analysis
    applies unchanged.
  So every (F1) instance CR uses holds. CLOSED. Wording for L-NEW: replace "S4a's optimum restricted to R is an optimum of its arena" by
  "every B-case (F1) instance holds: under H2 by PIECE's argument; under λ_W(o) = o by P3-1's vacuity".
- DATA: 268 pieces of this kind in my probe; 0 gate edges from C_W vertices into R occurred inside them, so the closure is untested by data.
### 1.4 Step 2 and the count: checked
After the freeze κ(π_v) and P(θ) are constant, so Ξ(v) = (c_θ, κ ∪ P(θ), |π_v| + ℓ(θ)) moves only with |π_v| ∈ [1, |R| − 1]. The move is
monotone (R15 (a); its direction is fixed by c_θ's parity), so there are ≤ |R| − 2 changes per v ∈ R \ {o}. Ξ(o) = θ is constant. Total
≤ |R| + (|R| − 2)(|R| − 1) ≤ (n + 1)|R|. Correct (the packet's bound is loose).
### 1.5 Corollary (≤ max(1, |F|) pieces per interval under H2): checked
- Route form is constant on I: the honest frame by TC (i) and λ_Ξ(o) fixed; the W frame by H2, constant.
- Under H2, w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F (R19 (b) needs only H2: REFEREE-2's N-X-2).
- Under H1, θ = o ⊕ min over F-exits of Ξ(e) (TF / X-1, which use only H1 and R constant). If λ_Ξ(o) = o, θ = (o, ∅, 0).
- So θ and w change only at transitions with an F-change, ≤ max(0, |F| − 1) by F1°, and the pieces number ≤ that + 1 = max(1, |F|).
- If the honest frame is not in route form on I, there are no pieces and the bound is trivial. Correct.

## 2. Lemma TC (§2): SIGNED
- (i). Under H1, e* = σ̄(o) has an o-free honest play, which is its (σ, τ)-play, so e* ∈ F and o's honest cycle lies in F. Without H1, the
  honest cycle passes o and each of its vertices reaches o along σ and forced edges, so λ_Ξ(o) ∈ R. H2 ⟺ τ(o) ∈ F (τ(o) = o counts as R).
  Both are constant on I. Correct.
- (ii). Under H2, o is not on its W-cycle, so λ_W(o) = λ_W(τ(o)) = λ_Ξ(τ(o)) (Ξ = W on F), which is fixed in the phase. So H3 and (h) are
  constant on I. EQ with (h) failing would force λ_Ξ(o) = λ_Ξ(τ(o)) ∈ F, hence H1 and H3, i.e. (h). Correct.
- (iii). λ_Ξ(o) ∈ F, while λ_W(o) ∈ C_W ⊆ R, so Ξ(o) ≠ W(o). Correct.
- (iv). The converse "θ = w ⇒ Ξ = W": I checked the disjointness claim. A C_Ξ vertex other than o continues along C_Ξ under σ and forced
  edges, so π_v ∩ C_Ξ is a final segment [u..o) of C_Ξ. c ∉ π_v puts c on o's arc [o..u), so o's honest path to c avoids π_v. The same holds
  for C_W. Then (V1) along π_v and θ = w give Ξ(v) = W(v). The case c ∈ π_v: both plays reach c first, at the same position. Correct.
  EQ → OTHER: XW3 plus the converse. Correct.
- Consequence: under H2 or under H1 ∧ ¬H2 there is ≤ 1 OTHER block. Under ¬H1 ∧ ¬H2 there is no THR state, so every OTHER block after the
  first starts with an EQ → OTHER transition, which is a w-change. Correct.
- DATA: my probe, 20,840 crossing-free intervals (by clause pattern: 9,538 H1H2, 928 H1¬H2, 1,675 ¬H1H2, 8,699 ¬H1¬H2), 0 failures of
  (i)-(iv). Lane tccheck.py (random 3,000 seed 3003 + u1_n32, op20_r, op16_oc16): 0 failures.

## 3. Lemma F1° (§1): SIGNED
R21 (e)'s F1 used Lemma NF to make fallbacks value-preserving, and NF excludes OTHER endpoints. F1° replaces that with only what 𝓕 needs.
At an S4c step every switched F-edge is flat (FBL-N (ii): τ fixed, no (h)) and stays in F (no crossing). Distinct switched cycle nodes have
disjoint regions, and R-vertices' switches cannot reach F-plays. So W = Ξ is unchanged on F, and Lemma P's invariant on 𝓕 survives. The rest
is F1 verbatim (Lemma G (a), no (h)). The max(0, ·) form is right (my X-2). DATA: 20,840 intervals, 0 failures.

## 4. Reduction (§4): checked as a READING
- Uses: F1° and TC (this packet); R21 Theorem X steps 2-5 per F-interval (≤ 3n²), on runs of non-OTHER states inside I, which are F-intervals
  in R21's sense (maximal, with no crossing and no OTHER-touching transition inside); R15 (d) for value-preserving runs. All inside their
  signed hypotheses.
- NH-1: a transition at the boundary of an OTHER block (EQ/THR ↔ OTHER) is neither inside an F-interval nor, by the definition of ROI,
  "in" an OTHER block. There are ≤ 2(1 + WC(I)) per I; add them to the sum (absorbed by poly(n)·(1 + WC)).
- NH-2 (for the Consequence "P3′ bounds ROI on its pieces"): ROI counts changes of Ξ OR W on R; P3′ counts Ξ-changes. An R-only W-change
  on a piece (w constant) needs a route change, i.e. a switch of some y ∈ R, and (SG) (R19 (d)) makes Ξ(y) rise strictly
  (λ_Ξ(y) = c_θ ≠ y). So every R-only value-changing transition is a Ξ-change on R. One line; DATA: 6,942 switches of R-vertices, all strict.
- WC(I) is counted only under ¬H1 ∧ ¬H2 (TC); elsewhere the OTHER blocks number ≤ 1. Correct.

## 5. Data (DATA, not proof): docs/referee/scratch/nh_probe.py (n5x.step read-only)
Named: experiments/new/box29/instances/*.pg and out/*.pg, experiments/n5-exhaustive/instances/*.pg (b4_*, b5_*, incl. b5_o11 and
b5_os_n12..n24), experiments/new/box28/instances/*.pg, experiments/red/xing/instances/*.pg, experiments/new/box25/instances/*.pg,
fts_best16, theta_tp32, returns_rt48, returns_ph64. Random: o-cyclic 𝒞^1O, 5,000 seed 3001 and 5,000 seed 3002 --randstart, n 4-14.
Totals: 8,784 random runs; 20,840 crossing-free intervals; F1° 0 failures; TC (i)-(iv) 0 failures (2 EQ → OTHER transitions under
¬H1 ∧ ¬H2, both w-changes); Corollary: 11,213 intervals under H2, 0 failures; SG on R 6,942, 0 failures.
P3′: 901 route-form pieces with c_θ ≻ c_w (633 by H2, 268 by λ_W(o) = o). 0 failures of the freeze or of the count, but the data is NEARLY
VACUOUS: the longest such piece has 6 transitions, the last κ-change index is 0, and the most Ξ-changes on R in a piece is 1. There were 0
gate edges from C_W into R (P3-1). Lane: p3check.py and rfcheck.py returned no qualifying runs on random 3,000 seed 3003 and on u1_n32 /
op20_r / op16_oc16 (rfcheck: "κ-freeze fails 0"). P3′ rests on the proof.

## 6. Gaps (for §C)
| id | item | kind | status |
|---|---|---|---|
| P3-1 | P3′ step 1: 𝓡*_w is not a faithful contraction under λ_W(o) = o (vertices of o's W-cycle) | proof step | CLOSED here (§1.3: the κ-strict B-cases from C_W are vacuous inside J) |
| NH-1 | Reduction: boundary transitions of OTHER blocks | wording (READING) | absorbed; name them |
| NH-2 | Consequence: ROI counts W-changes too | one line (READING) | closed by (SG) |
OPEN, untouched: U1-U3, W-CYC, (NH'), (X), G-N5-TIME. Conjectures OB_R, OB, NFB-O and FALSE WF0: context only, not checked. TARGET.md diff:
statements about the candidate N5 on 𝒞^1O, none about general parity games.
