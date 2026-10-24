# Referee report R-N5-X: N5 inside a joint λ-phase is controlled by crossings and OTHER states (box 28)

Referee: REFEREE (successor 4), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-X: the Lead's message of 2026-10-24 18:1xZ
(read 18:14Z). Pin: trunk claude/vibrant-johnson-nxvvxo afc88b0 (an ancestor of my merged HEAD). Object: docs/new/P-N5-X-box28.md, sha1
b21d2d0638d08d750f26ae4dda2faaca7891fa23 (verified at the pin; unchanged in my tree). L-NEW successor 10, l-new 23e8f93.
Context read: SPEC S1-S5 (docs/new/N5-ssi-global.md); RESULTS R15, R17, R18, R19, R20 as landed; my R-N5-RE (§5 PIECE) and R-N5-XA (§C5,
§C7); docs/new/P-N5-XA-fixes-box28.md §5-§6; experiments/new/box28/eqcheck.py (run unmodified). docs/new/N5-NH-box28.md was used for
background only; the packet governs. docs/referee-2/ was NOT read for this packet.
Written 2026-10-24 18:15Z-18:20Z by date -u. Every verdict is labelled (Opus 5.5, D15).

## Verdict
| item | verdict (Opus 5.5, D15) |
|---|---|
| (1) Lemma F1 (§5) | SIGNED WITH GAPS: X-2 (F = ∅: the bound must read max(0, \|F\| − 1); trivial). Step 2 across w-changes and EQ states without (h) is RIGHT: it uses only Lemma G (a), which needs no (h), and never uses θ or w |
| (2) Lemma NF (§4) | SIGNED WITH GAPS: X-3 (the EQ case cites §2, which assumes k+1 EQ; one line via XW and R15 (a) closes it and shows k+1 is EQ). The hypothesis "k+1 not OTHER" is not used |
| (3) Theorem X (§7) | SIGNED WITH GAPS: X-1 (step 4 uses R19 (f) "θ constant not needed" for the count of Ξ-or-W changes; the signed justification N-RE-4 covers only the gates, and the count needs one more step, given in §3.2, which closes it); X-2 (block count when F = ∅; absorbed); X-4 (step 4 re-derives P-N5-XA-fixes §5 outside R20's hypotheses: checked, valid as a re-derivation, not as a citation). Every other cited result is used inside its signed hypotheses (§3.3). (FBRE-F) is not used |
| (4a) Lemma XW (§1) and XW1-XW3 | SIGNED (XW is R18 (d) Lemma S (b)) |
| (4b) Lemma EQ (§2) | SIGNED |
| (4c) Lemma FBL-N (§3) | SIGNED |
| (4d) Lemma F2 (§6) | SIGNED |
| (4e) Lemma FB-W (§9) | SIGNED (given the CR row of §8, which I checked) |
| (5) The (w, u*)-run table (§8) | checked as a READING: every row right, including "FBF: NO" |
| Consequence of Theorem X (READING) | not signed; checked: τ-changes ≤ d − 1 holds by R15 (c) on G^d (Odd's τ sequence is strictly ≺-increasing, so τ(o) never repeats) |
No statement is NOT SIGNED. No counterexample. (X) and (NH') stay OPEN; G-N5-TIME stays OPEN.

## 1. Lemma F1 (§5): SIGNED WITH GAPS
Checked step by step. Item (1) is the Lead's main question: does PIECE's F-part hold across w-changes and across EQ states without (h)?
- Step 1: Ξ = W on F at every state is Lemma G (a) (R19 (a): no (h)). F is closed under σ_k and under forced Odd edges (a successor of an F
  vertex continues its o-free play); o ∉ F. So 𝓕 = G_τ restricted to F (Even edges F → F) is a one-player game whose values are W|F. Correct.
- Step 2: for x, z ∈ F, (x, z) ∈ Iσ_k iff Ξ_k(z) ▷ Ξ_k(σ_k x), with z, σ_k(x) ∈ F, so iff W_k(z) ▷ W_k(σ_k x) (Lemma G (a)), i.e. iff it is
  𝓕-improving. This holds at EVERY state, EQ, THR or OTHER, because Lemma G (a) needs no (h). The packet's split "EQ: Ξ = W; THR: Lemma G (a)"
  is right but unnecessary. θ and w never enter. ANSWER to (1): yes, the F-part is valid across w-changes and across EQ states without (h).
- Step 3: in a phase τ is constant, so σ_{k+1} is the S4a optimum against τ (R18 (d) Lemma S (c)). No crossing gives σ_{k+1}(F) ⊆ F. Every
  𝓕-arena strategy ρ, extended by σ_{k+1} on R, is in the S4a arena (step 2), and its G_τ-values on F depend only on ρ. (F1) in G_τ then makes
  σ_{k+1}|F a pointwise optimum of the 𝓕-arena. R17 accepts any pointwise optimum (R17 (d)). Correct.
- Step 4: every fallback inside I is value-preserving by NF (I has no crossing and no OTHER-touching transition). It may still switch flat
  F → F edges. R17's Lemma P invariant is a statement about current values, and its induction step uses only the state it starts from
  (my R-N5-XA §C5, REFEREE-2 §C2.2, signed in R20 (f)). So it carries over with j unchanged. Correct.
- Step 5: λ on F = λ_Ξ, constant in the joint phase, so the 𝓕-run is inside one λ-phase. Step 6: R17 Theorem PH on 𝓕. Correct.
- Inside a phase every transition has Iσ ≠ ∅: with Iσ = ∅ the iteration would have to change τ. So every transition is S4a or S4c.
- X-2 (edge case). If F = ∅ (every vertex reaches o, which forces H2 to fail; such intervals are EQ runs), F1's bound |F| − 1 = −1 is false
  as written for the 0 changes. Read it as max(0, |F| − 1). DATA: 270 F-intervals with F = ∅ (my probe first flagged them as F1 "failures",
  before I fixed the probe's bound).
- DATA (§6): 1,592 F-intervals, 0 failures of the F-change bound (slack 0 attained).

## 2. Lemma NF (§4): SIGNED WITH GAPS
- X-3. "k is EQ: the fallback is value-preserving (§2)": §2's proof uses that k+1 is also EQ. A direct line closes it. At EQ k the gate is
  G_τ's improving set, so by R18 (c) every switched edge is flat and W_{k+1} = W_k. Then Ξ_k ⊴ Ξ_{k+1} ⊴ W_{k+1} = W_k = Ξ_k (R15 (a), XW). So the
  fallback is value-preserving, and k+1 is EQ.
- THR case. With R_{k+1} = R_k: an F-vertex's switched edge stays in F, so it is flat F → F (FBL-N (ii)). An R-vertex's switched edge stays in R;
  by Lemma G (c) (needs (h) at k only) an R → R gate edge is W-improving, hence flat (R18 (c)), which needs x = λ(x), impossible on R under (h).
  So only flat F → F edges switch, at cycle nodes with disjoint regions. Correct.
- The claim "Ω_{σ,e} unchanged for every exit e". F-vertices: their plays avoid o under every exit (reaching o comes before o's choice), and
  their values are their G_τ-values, unchanged by the flat switches. R-vertices: π_v is unchanged (no R-vertex switched, R unchanged).
  - For e ∈ F: π_v and o are disjoint from e's o-free play, so (V1) gives π_v ⊕ o ⊕ Ω_{σ,e}(e), unchanged.
  - For e ∈ R: the play closes the cycle o → e → π_e → o of unchanged R-paths.
  Then Ξ = min_e Ω_{σ,e} (R18 (d) Lemma S (a); on 𝒞^1O Odd's positional strategies are the exits of o) and W = Ω_{σ,τ(o)}. Correct.
- Neither (h) at k+1 nor "k+1 not OTHER" is used. DATA: 121 value-changing fallbacks with no OTHER endpoint, all crossings.

## 3. Theorem X (§7): SIGNED WITH GAPS
### 3.1 Steps 1-3, 5-7: checked
- Step 1: cutting at X + O transitions (a transition that is both is cut once) leaves ≤ 1 + X + O F-intervals. An F-interval with ≥ 2
  states has only EQ and THR states.
- Step 2: an EQ → THR transition changes Ξ(τ(o)) with τ(o) ∈ F (F2), so there are ≤ |F| − 1 of them (F1). Blocks alternate, so #blocks ≤
  2(|F| − 1) + 2 = 2|F| (X-2: for F = ∅ the interval is one EQ block; the 3n² total absorbs it).
- Step 3: Lemma EQ per EQ block.
- Step 5: (|F| + 1)(n − 1) + 2|F|(n − 2) + 2|F| + (|F| − 1) with |F| ≤ n − 1 is 3n² − 4n ≤ 3n² (multiplied out).
- Step 6: + X + O for the cut transitions.
- Step 7: value-preserving means Ξ and W unchanged, so Ωσ = Ξ is unchanged, and Ωτ is unchanged because τ is fixed. R15 (d) gives runs
  ≤ 4n(n − 1), and the total follows: ≤ (VC + 1)(4n(n − 1) + 1).
### 3.2 Step 4 and X-1: PIECE with θ varying
Step 4 applies R19 (f) PIECE to sub-blocks (THR, τ, w, R constant, one joint λ-phase) in which θ may change. R19 (f) is signed "θ constant
not needed (N-RE-4)" for the count of transitions at which "Ξ or W changes". N-RE-4's justification (REFEREE-2, accepted in my R-N5-RE §C3)
is about the GATES: Lemma G (c) at each state. The COUNT step in my R-N5-RE §5.2 says "a value change on R (of Ξ or W) is a change of
(A_v, |π_v|)". That is true only with θ constant. With θ varying, a θ-change changes Ξ on all of R (Ξ = π ⊕ θ) while no route and no W-value
on R changes. So the θ-free count needs one more step.
- X-1 closure (referee's). In a sub-block, a transition that changes θ also changes W at a vertex of F. Proof: under H1 at k, Odd's
  honest choice e_k := σ̄_k(o) has an o-free honest play, which is then also its (σ_k, τ)-play, so e_k ∈ F (R constant on the sub-block) and
  θ_k = o ⊕ W_k(e_k) ((V1), Lemma G (a)). Suppose W is unchanged on F at k → k+1. Then
  θ_{k+1} ⊴ Ω_{σ_{k+1}, e_k}(o) = o ⊕ W_{k+1}(e_k) = o ⊕ W_k(e_k) = θ_k
  (Lemma S (a): Ξ(o) is the minimum over o's exits; e_k's play still avoids o). Also θ_{k+1} ⊵ θ_k (R15 (a)). So θ_{k+1} = θ_k. □
- Hence every Ξ-or-W-changing transition of a sub-block changes an 𝓡*-value (a route's (A_v, |π_v|)) or an 𝓕-value, and PIECE's
  (|R| − 1) + (|F| − 1) bound holds for the Ξ-or-W count with θ free. R19 (f) as LANDED is therefore true, but its written justification
  needs this paragraph. I recommend the Lead record it as a justification note on R19 (f). CLOSED here.
- DATA: 176 θ-changes inside sub-blocks, each with a W-change on F (THF, 0 failures); 136 sub-blocks, max 14 value-changing transitions
  (n = 24, bound 22), 0 over n − 2.
### 3.3 Each cited signed result, against its signed hypotheses
| cited | where | hypotheses at the point of use | inside? |
|---|---|---|---|
| R15 (a), (c), (d) | XW3, F2, step 7, Consequence | any N5 run | yes |
| R17 Lemma P, PH, (d) | EQ, F1 | one-player game, λ-phase, pointwise arena optima | yes (G_τ on EQ blocks; 𝓕 on F-intervals) |
| R18 (c), (d) Lemma S (a)-(c) | FBL-N, NF, EQ, F1 | arena optimum at an S4a-returned state; S (c) for S4a steps only (G-1OA-6) | yes |
| R19 (a) Lemma G (a) / (b), (c) | F1, F2, NF | (a) none; (b), (c) under (h) | yes ((b) and (c) only at THR states) |
| R19 (b) w = o ⊕ Ξ(τ(o)) | F2 | (h) at the state | yes |
| R19 (f) PIECE | step 4 | τ, w, R constant, (h), one joint λ-phase, no fallback; θ free | yes for τ, w, R, (h), phase; θ free needs X-1 (closed in §3.2); "no fallback" relaxed by X-4 |
| R20 (f) / fixes §5 (flat fallbacks pass PIECE) | step 4 | signed for a throttled stretch with u* ≠ none | NO as a citation: X-4 |
| (FBRE-F) | — | — | not used (checked: no step mentions re-entries after fallbacks) |
- X-4. R20 (f) signs "pieces pass through value-flat fallbacks" for throttled stretches with u* ≠ none. Step 4 uses it in sub-blocks with
  θ varying and any u*. The ARGUMENT (my R-N5-XA §C5) needs only three things:
  (i) the fallback changes no value;
  (ii) it switches only flat F → F edges and leaves R and (h) intact;
  (iii) Lemma P's induction step uses only its starting state.
  In a sub-block, (i) holds by NF (no crossing), (ii) holds by NF's classification (which uses (h) at k and R_{k+1} = R_k, not FBL, so G-XA-1
  for u* = none is not involved), and (h) at k+1 holds because k+1 is THR. So the use is valid as a RE-DERIVATION, which the packet's step 4
  says it is ("gives the property that argument needs directly"). CLOSED, with the wording: cite the argument, not R20 (f).

## 4. Lemmas XW, EQ, FBL-N, F2, FB-W
- XW: R18 (d) Lemma S (b) (L_σ ⊴ V_{σ,τ}). XW1: under (h), Ξ = W iff θ = w (Lemma G (a), (b)). XW2: the three types partition the states
  by definition. XW3: w_k = θ_k ⊴ θ_{k+1} ⊴ w_{k+1} = w_k (no phase needed). SIGNED.
- EQ: at EQ the gate is G_τ's improving set. S4a is R17's switch-best step in G_τ. An S4c step is Even's (τ fixed); every gate edge is flat
  (R18 (c)), so W and Ξ are unchanged (k+1 ∈ Q; or by X-3's line). Lemma P's invariant passes the fallback. λ_W = λ_Ξ on Q, constant in the
  phase. Theorem PH in G_τ. SIGNED. DATA: 1,464 EQ blocks in my probe (max 20 value-changing at n 24), plus 4,705 EQ runs (eqcheck.py),
  0 over n − 1.
- FBL-N: (ii) XW turns the gate inequality into W(z) ▷ W(σ x) = Ξ(σ x); R18 (c) at the arena optimum. (iii) Without H2, o lies on its W-cycle
  C ⊆ R_k, so λ_W(z) ∈ R_k for z ∈ R_k, against x = λ_W(z) ∈ F. SIGNED. DATA (eqcheck.py, unmodified): 166 fallbacks, 104 gate edges from F,
  0 failures of (ii) or (iii).
- F2: H2 at k+1 gives τ(o) ∈ F_{k+1} = F_k. w_k = o ⊕ Ξ_k(τ(o)) by (V1) and Lemma G (a) (no (h) needed at k), and w_{k+1} by R19 (b). An
  unchanged Ξ(τ(o)) gives w_{k+1} = w_k, then XW3, then XW1 makes k+1 EQ: contradiction. The second claim is R19 (b) at both ends. SIGNED.
  DATA: 25 EQ → THR and 8 THR-THR w-changes, 0 failures.
- FB-W: checked step by step.
  - A value with θ_t's status at u* lies strictly below one with w's status, when the cycle node and the part above u* agree.
  - Under (h), R-values carry θ_t's status (u* is on no route).
  - CR in the run (§8 row) fixes coarse values from k_0 + n − 1 on.
  - Ξ_{L+1}(z*) keeps w's status; otherwise it would drop below Ξ_L(z*), against R15 (a).
  - x ≠ u* and x ≠ λ(x) carry the status to x by (V1); R15 (a) and CR carry it forward.
  - x ∈ R_t would give θ_t's status. SIGNED. It uses only σ_{L+1}(x) = z*; that the transition is a fallback is not needed.

## 5. The (w, u*)-run table (§8): checked (READING)
- §1 setting: per state, yes.
- Lemma C: with u* fixed for the run, P(θ_k) and P(w) agree above u* at every state; monotonicity is R15 (a) with (Cmono) on a fixed V*. Yes.
- CR: the induction uses Lemma C at k, k+1, (Cstrict), (F1) at arena steps, λ_W constant (per state: λ_W = λ_Ξ on F, c on R), and the vacuous
  B-fallback (N-XA-1). θ never enters. Yes.
- XA: step 4 uses that u* tops P(θ_{E+1}) Δ P(w); step 5 uses Lemma C at L (COARSE(π ⊕ w) = COARSE(π ⊕ θ_L)). Yes.
- FBL strong form: per state. Yes.
- FBF: NO, as stated: its induction uses Ξ_t(z) = Ξ_L(z) on R_t, i.e. θ_t = θ_L. I agree. (FBRE-F) FALSE (fbref_n48, L-RED's fbref_cex_n32)
  is consistent with this row; I did not re-verify those instances (not a claim of this packet).

## 6. Data (DATA, not proof): docs/referee/scratch/x_probe.py (n5x.step read-only; phase = (λ_Ξ, λ_U, τ) constant)
Named: experiments/new/box28/instances/*.pg (8), experiments/red/xing/instances/*.pg (14), fts_best16, theta_tp32, returns_rt48, returns_ph64,
theta_thf16, experiments/new/box25/instances/*.pg (13), thetare_n, nc_fail_n12. Random: o-cyclic 𝒞^1O, 5,000 seed 2801 and 5,000 seed 2802
--randstart, n 4-14 (8,731 accepted runs).
| check | count | failures |
|---|---|---|
| XW (vertex-states) | 251,021 | 0 |
| NF (value-changing fallbacks, no OTHER endpoint) | 121 | 0 (all crossings) |
| F1 (F-intervals; F-change bound max(0, \|F\| − 1)) | 1,592 (270 with F = ∅) | 0 |
| F2 (EQ → THR / THR-THR w-change) | 25 / 8 | 0 |
| EQ blocks (≤ n − 1 value-changing) | 1,464 (max 20, n 24) | 0 |
| sub-blocks (≤ n − 2 Ξ-or-W changes) / θ-changes with an F W-change (X-1) | 136 (max 14) / 176 | 0 / 0 |
| Theorem X per phase (VC bound and total bound) | 1,947 phases (max length 110, max X 70, max O 19) | 0 |
eqcheck.py (lane, unmodified; random 3,000 seed 2803 --randstart + oc16_s2, oc24_s4_final, wd16_s2, wd12_s1, x48_rt48_final): XW 77,751
checks, EQ 4,705 runs, 166 fallbacks / 104 F-gate edges: 0 failures. Random runs are thin for THR structure (max phase length 3); the named
instances carry the evidence. The Theorem X bound is far from tight on every instance (it is O(n⁴) per interval budget).

## 7. Gaps (for §C)
| id | item | kind | status |
|---|---|---|---|
| X-1 | Theorem X step 4 / R19 (f): θ-free PIECE count of Ξ-or-W changes | proof step (in R19 (f)'s justification) | CLOSED here (§3.2); recommend a note on R19 (f) |
| X-2 | F1 and step 2 when F = ∅ | wording | CLOSED (max(0, \|F\| − 1); one EQ block) |
| X-3 | NF, EQ case cites §2 | wording | CLOSED (XW + R15 (a) line) |
| X-4 | Step 4 uses R20 (f)'s flat-fallback claim outside u* ≠ none throttled stretches | citation | CLOSED as a re-derivation (§3.3) |
OPEN, not touched by any signature here: (X) crossings per phase, (NH') OTHER-touching transitions per phase, G-N5-TIME. TARGET.md diff:
statements about the candidate N5 on 𝒞^1O (polynomial by other means), none about general parity games.
