# N5 box 4: the proof side of (X), crossings per joint λ-phase
L-SI successor 2 (Opus 5.5, D15/D18). Lead GO 2026-10-24 17:4xZ; box started 17:43Z (date -u), to ~20:45Z.
Labels (L40): PROVED (by whom; unrefereed unless stated), CONJECTURE (with data), OPEN, DATA, READING (assembly or sketch).
Scope: N5 (docs/new/N5-ssi-global.md, SPEC S1-S5) on 𝒞^1O, inside one joint λ-phase. These are lemmas about the candidate N5.
They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
Notation: as in RESULTS R19/R20 and docs/new/N5-NH-box28.md (θ = Ξ(o), w = W(o), (h) = H1 ∧ H2 ∧ H3, u*, THR = (h) and θ ◁ w).
R_k = vertices ≠ o whose (σ_k, τ)-play reaches o; F_k = V ∖ (R_k ∪ {o}); R̄_k = R_k ∪ {o}. "Crossing transition": R_k ≠ R_{k+1}.
Code: experiments/si/xing/ (each script has a docstring; every script asserts its run equals experiments/new/n5.py's).

ASSUMPTIONS (one line each):
- A1: 𝒞^1O (o is the only Odd vertex with out-degree > 1).
- A2: one joint λ-phase (box 28 convention: (λ_Ξ, λ_U, τ(o)) constant), so τ is fixed.
- A3: (h), or a named clause of it, only where a statement says so.

## 0. Results in short
- PROVED (L-SI succ. 2): **Lemma ACT** (§2). Every crossing transition has an ACTIVE crosser, i.e. a switched vertex whose own
  membership changes:
  - an entry needs a switched edge from F_k into R̄_k;
  - a leave needs a switched edge from R_k into F_k (or a new cycle inside R_k, which **Lemma LOOP** rules out inside a phase
    when H1 holds at k).
  Passive crossers ride on these.
- PROVED (L-SI succ. 2): **what fallbacks can do** (§3).
  - **NOFE**: at a fallback, a switched F_k → R̄_k edge starts on o's W-play or on a (σ_k, τ)-cycle.
    In all 16 random cases (4 seeds) its tail was a cycle node on o's W-play, and (h) failed at k+1 (DATA).
    My first statement, "fallbacks never enter", was FALSE: nofe_cyc_n8.
  - **NOFL-E**: from a state with Ξ_k = W_k and H2, a fallback switches no R_k → F_k edge.
  - **GAP**: at a THR fallback every switched leave edge y → z satisfies Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y): the o-free value lands in
    the trust gap.
- PROVED (L-SI succ. 2): **Lemma LV′** (§4). With Z = the number of direction reversals of R in the phase,
  **X ≤ (n − 1)(Z + 1) + Z**, and Z ≤ X.
  - So (X) ⟺ (Z) up to a factor n. The additive potential box 3 asked for exists for entries: it is |R| itself, the binary-counter
    "number of ones" potential.
  - What remains is the carry count Z.
- READING (with box 28 §5c, itself a READING): per joint λ-phase N5 makes O(n⁵ (1 + Z + O)) transitions.
- DATA (§5): Z ≤ 7 on all 31 named instances.
  - Every climbed instance with X ≥ 27 has a single dip (Z = 2); fbref_cex_n32 has Z = 7.
  - Random runs (2 × 1,650 games, n 16-28) give Z ≤ 1.
  - The reversals pay as follows:
    - 26/28 '+−' reversals are fallbacks at THR states;
    - 30/33 '−+' reversals follow a θ-change, as FBF (R20 (c)) forces after a throttled fallback.
  - Climbs on Z: §6.
- No-go for natural potentials (§7; each refuted by a named, re-verified instance):
  - (NG1) no Φ(R, θ, w) rises at every crossing transition (x31_re24, x31_ru24, under (h));
  - (NG2) no Φ of R-side data alone (R returns to ∅ after 16 crossings and 23 θ-changes on lev_l_sc);
  - (NG3) the trust-gap level rank(u*) does not pay for carries (constant over 19/19 consecutive evicting fallbacks):
    CONJECTURE (U*-DROP) FALSE;
  - (NG4) the tropical / parametric lens (o as a terminal with value θ) is ill-posed for N5: the optimal routes pass through θ's
    own play (247 vertex-states on lev_l_sc).
- PROVED (L-SI succ. 2): **Lemma WM** (§8). The trusted valuation W never decreases at an arena transition. So W-lowerings, the
  "carries", happen only at fallbacks.
  - DATA: on all 31 instances the W-lowering transitions are exactly the evicting fallbacks.
  - CONJECTURE (W-LAY), "≤ n − 1 W-changing transitions between W-lowerings", is FALSE: thclimb_n16_s12 has 16 at n 16. Trusted
    progress is gated by θ, because each θ-rise unblocks one entry.
- OPEN: (Z) reversals of R per joint λ-phase; (NH′) as before. G-N5-TIME stays OPEN.

## 1. Why crossings reduce to reversals (the idea in one paragraph)
- READING. Entries come in monotone runs: R only grows until something evicts. Evictions are almost always fallbacks at throttled
  states, and they evict in bulk.
- After a throttled fallback, nothing enters again until the stretch ends (FBF, signed). So the sign pattern of R is a counter:
  increments (entries, ≤ n − 1 per run) and carries (evictions).
- The two-digit counter of box 3 (lev_l_sc) is one carry: sign string `+…+ − +…+`, Z = 2.
  - The θ-sequence after the carry replays the 23 exits of the first block in the same order: σ̄(o) =
    8, 27, 19, 21, 7, 21, 1, 12, 27, 1, 21, 7, 20, 19, 31, 9, 30, 23, 2 both times.
- A kill must therefore nest carries (Z growing super-polynomially); a proof must bound carries.

## 2. Lemma ACT and Lemma LOOP (PROVED, L-SI succ. 2; pure graph arguments)
Setting: a transition k → k+1 with τ_{k+1} = τ_k; S = Even vertices with σ_{k+1}(v) ≠ σ_k(v). Fact used throughout: a vertex
u ≠ o that keeps its edge has u ∈ R̄_k ⟺ its successor ∈ R̄_k (τ fixed).

**Lemma ACT.**
- (i) If R_{k+1} ⊄ R_k, some s ∈ S has s ∈ F_k, σ_{k+1}(s) ∈ R̄_k and s ∈ R_{k+1} (an active entrant).
- (ii) If R_k ⊄ R_{k+1}, either some s ∈ S has s ∈ R_k, σ_{k+1}(s) ∈ F_k and s ∉ R_{k+1} (an active leaver), or the
  (σ_{k+1}, τ)-graph has a cycle that avoids o, lies inside R_k and contains a switched vertex.

Proof of (i):
- Take x ∈ R_{k+1} ∖ R_k and its new play x = p_0, …, p_m = o (first visit of o).
- It contains switched vertices s_1, …, s_j in order (j ≥ 1, else it is the old play and x ∈ R_k).
- Between σ_{k+1}(s_i) and s_{i+1}, and between σ_{k+1}(s_j) and o, only old edges are used. So membership in R̄_k is constant
  on these segments: M(σ_{k+1}(s_i)) = M(s_{i+1}) and M(σ_{k+1}(s_j)) = R̄. Also M(s_1) = M(x) = F.
- Take the last i with M(s_i) = F and M(σ_{k+1}(s_i)) = R̄. It exists: otherwise M(s_i) = F for every i, so M(σ_{k+1}(s_j)) = F.
- s_i lies on x's new play, which reaches o, so s_i ∈ R_{k+1}.

Proof of (ii):
- Take x ∈ R_k ∖ R_{k+1}. Its new play never visits o and ends in a cycle.
- Define s_1, s_2, … and the segments as in (i); M(s_1) = R̄.
- Suppose no s_i has M(s_i) = R̄ and M(σ_{k+1}(s_i)) = F. Then every vertex of the play lies in R̄_k ∖ {o} = R_k, including its
  final cycle.
- That cycle contains a switched vertex: an all-old cycle inside R_k contradicts "old plays from R_k reach o".
- Otherwise the s_i found lies on x's new play, which avoids o, so s_i ∉ R_{k+1}. □
DATA: every crossing transition on the 31 instances and 2 × 2,600 random runs has an active crosser (xclass.py: Xnoact = 0;
leaves.py: noact = 0).

**Lemma LOOP.** Inside a joint λ-phase, if H1 holds at k, the second case of ACT (ii) does not occur.
Proof:
- Let c be θ_k's cycle node. Then c ∉ R_k: otherwise c's honest play (which agrees with the (σ, τ)-play off o) would reach o and
  return to c, putting o on its own honest cycle, against H1.
- Every u ∈ R_k has λ_{Ξ,k}(u) = c: its honest play reaches o and continues as o's honest play, which does not return (H1).
- A new cycle inside R_k avoids o. So the honest value of its top vertex t at k+1 has cycle node t ≠ c = λ_{Ξ,k}(t). λ changes, so
  k+1 is not in the phase. □
Consequence (PROVED): inside a joint λ-phase with H1 at k, every leave transition switches an edge R_k → F_k at an active leaver.
- Remark: xclass.py's label "LL" (8 cases) means "the leaver's new target was in R_k but left in the same transition". It is
  not a loop.

## 3. What fallbacks can do (PROVED, L-SI succ. 2)
Inputs (all signed or proved elsewhere):
- RESULTS R19 (a), Lemma G (a): Ξ = W off R, no (h) needed. Lemma G (b): under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w.
- Lemma XW (L-NEW box 28 §1, PROVED, unrefereed): Ξ ⊴ W pointwise.
- SPEC S4: a fallback happens iff N5's arena selection returns σ_k, and it switches only Iσ edges. si.py `improving`:
  (v, z) ∈ Iσ iff Ξ(z) ▷ Ξ(σ(v)).
- The arena optimum is an optimal strategy of a one-player game (VJ00), so it dominates every arena strategy pointwise in W.
- F-pre (box 1 §2): y ⊕ a ◁ y ⊕ b iff a ◁ b, when y lies on neither play.
Key step (K): Suppose an edge y → z is in the arena, y is on no (σ_k, τ)-cycle, z's W-play avoids y, and W_k(z) ▷ W_k(σ_k y).
- Then σ_k[y → z] has W-value y ⊕ W_k(z) ▷ y ⊕ W_k(σ_k y) = W_k(y) at y.
- So σ_k is not arena-optimal, the arena selection differs from σ_k, and k → k+1 is not a fallback.

**NOFE.** At a fallback transition inside the phase, every switched edge y → z with y ∈ F_k and z ∈ R̄_k has y on o's W-play at k
or on a (σ_k, τ)-cycle.
Proof:
- Suppose not. z's W-play is its route (inside R_k, so it avoids y ∈ F_k) followed by o's W-play, which avoids y by assumption.
- (y, z) ∈ Iσ gives Ξ_k(z) ▷ Ξ_k(σ_k y). Also W_k(z) ⊵ Ξ_k(z) (XW), and W_k(σ_k y) = Ξ_k(σ_k y) (G (a); σ_k y ∈ F_k as y ∈ F_k).
- Now apply (K). □
- Instance (pinned): experiments/si/xing/instances/nofe_cyc_n8.pg + .start (sha1 f3868b39; n5.py 2 iterations, 1 fallback;
  Oink zlk OK, strategies verified).
  - At k = 1 (Ξ = W, (h) holds) the fallback switches 2 → 6.
  - Vertex 2 is the cycle node on o's W-play 0 → 7 → 3 → 2, so the switch closes the cycle 2, 6, 5, 0, 7, 3 through o.
  - R grows {1, 5, 6} → {1, …, 7}, and (h) fails at k+1. The value of 2 stays (2, ∅, 0): flat.
- DATA: 16 such fallback entries in 4 × 3,000 random runs (seeds 401-404), all with this shape (tail a cycle node on o's W-play;
  state Ξ = W at k; (h) fails at k+1). None on the 31 named instances (entries at fallbacks: 0).

**NOFL-E.** If Ξ_k = W_k pointwise and H2 holds at k, a fallback at k switches no edge y → z with y ∈ R_k, z ∈ F_k.
Proof:
- z ∈ F_k, so its W-play avoids o and hence avoids y (y's W-play reaches o).
- y is on no cycle: its play reaches o, and o's W-play does not return to o (H2).
- Ξ_k(z) ▷ Ξ_k(σ_k y), and Ξ = W, so W_k(z) ▷ W_k(σ_k y). Now apply (K). □
Consequence (PROVED): from a state with Ξ = W and H1 ∧ H2, a fallback transition has no leave (by ACT (ii) + LOOP). It can enter
only by NOFE's cycle-closing switches.

**GAP.** At a fallback from a THR state k (with (h)), every switched edge y → z with y ∈ R_k, z ∈ F_k satisfies
Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y), i.e. π′ ⊕ θ ◁ Ξ_k(z) ⊴ π′ ⊕ w, where π′ is the route of σ_k(y).
Proof:
- The left inequality is (y, z) ∈ Iσ.
- If Ξ_k(z) ▷ W_k(σ_k y), then W_k(z) = Ξ_k(z) (G (a)), and (K) applies: y is on no cycle (H2); z's W-play avoids y.
  This contradicts the fallback. □
Meaning: every eviction at a throttled fallback lands in the TRUST GAP (θ, w], translated by the route. The gap is the same element
w − θ for every vertex of R (integer encoding with c fixed: values are (Σ ±2^rank, ±length) in Z², ⊕ is addition). So all evictions
of one fallback sit in one window of width w − θ.

## 4. Lemma LV′ (PROVED, L-SI succ. 2)
Give each crossing transition a sign:
- '+' if R_k ⊊ R_{k+1};
- '−' if R_{k+1} ⊊ R_k;
- '±' otherwise.
Z := #('±') + #(pure-sign crossing transitions whose sign differs from the previous pure sign).
**Lemma LV′.** In any joint λ-phase, X ≤ (n − 1)(Z + 1) + Z.
Proof:
- A maximal run of equal pure signs changes |R| strictly monotonically inside {0, …, n − 1}, so it has ≤ n − 1 transitions.
- There are ≤ Z + 1 such runs and ≤ Z '±' transitions. □
(zcount.py asserts it on every phase it scans.)
- Amortized-analysis reading (the lens the brief suggested): |R| is the "number of ones" potential of a binary counter. Entries
  are increments; evictions are carries, paid by the entries they undo.
- LV′ is exactly that amortization. It leaves the number of carries, Z, as the only charge.
- In the counter, carries at level i happen 2^{b−i} times. An additive bound therefore needs a reason why carries cannot nest. §7
  shows the natural level-indexed potential (the gap level u*) gives none.

READING (assembly with box 28 §5c, itself a READING):
- per joint λ-phase, N5 makes O(n⁴ (1 + X + O)) = O(n⁵ (1 + Z + O)) transitions;
- o-cyclic 𝒞^1O is polynomial for N5 if (Z) and (NH′) hold per joint λ-phase. Lemma Φ (≤ 2n(n − 1) + 1 phases, box 21) and
  τ-changes ≤ d − 1 are as before.

FBF consequence (PROVED from RESULTS R20 (c), signed):
- In a throttled stretch S (τ, θ, w constant, (h), θ ◁ w), nothing enters after the first fallback of S. So S contains at most one
  '+−' reversal at a fallback.
- A '−+' reversal after a throttled fallback needs the stretch to end first: θ or w changes, or (h) or THR is lost.
- Hence Z ≤ 2·#(throttled stretches with a fallback) + #(reversals at arena steps). This is again multiplicative in θ-changes
  (lev_l_sc: 45 θ-changes, Z = 2), so it does not settle (Z).

## 5. Classification data (DATA; xclass.py, leaves.py, zcount.py, revpay.py; 31 instances, all re-verified §9)
Longest phase per instance (T = transitions, X = crossing transitions; active kinds: EA arena entry, LF fallback leave, LA arena
leave, LL leave through a target that left; Z and its sign string):

| instance | n | T | X | EA | LF | LA | LL | θ-ch | Z | signs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lev_l_sc | 32 | 46 | 33 | 40 | 3 | 0 | 0 | 45 | 2 | `+(15) − +(17)` |
| x31_cu32i | 32 | 39 | 31 | 34 | 4 | 0 | 0 | 38 | 2 | `+(14) − +(16)` |
| x31_cu48 | 48 | 42 | 31 | 50 | 4 | 0 | 0 | 41 | 2 | `+(13) − +(17)` |
| fbref_cex_n32 | 32 | 50 | 28 | 29 | 26 | 0 | 0 | 9 | 7 | `−+(9)−+(3)−+(5)−(5)+(3)` |
| s_tp32_final | 32 | 38 | 27 | 34 | 8 | 0 | 0 | 35 | 4 | `+(10)−+(3)−+(12)` |
| run_x_inr2 | 32 | 49 | 19 | 19 | 12 | 0 | 0 | 43 | 6 | `+(12)−+−+−++` |
| lev_l_x | 32 | 55 | 21 | 20 | 8 | 0 | 0 | 51 | 4 | `+(14)−++−−++` |
| lev_l_n28 | 28 | 22 | 14 | 12 | 0 | 11 | 0 | 22 | 4 | `−−+++±−−+(6)` |
| x31_re24 | 24 | 4 | 4 | 5 | 0 | 3 | 2 | 0 | 2 | `−+±+` |
| s_rt32_final | 32 | 49 | 5 | 0 | 12 | 0 | 0 | 4 | 0 | `−−−−−` |
| oc16_s2 | 16 | 16 | 3 | 3 | 4 | 0 | 0 | 0 | 1 | `+−−` (non-(h)) |

(The other 20 instances: Z ≤ 2. Full output: `python3 experiments/si/xing/zcount.py <instances>`.)
- Entries at fallbacks: 0 on all named instances.
- Leave transitions: almost all at fallbacks from THR states (kind 'T'). Arena leaves occur on lev_l_n28 (at θ-changes), x31_re24 and
  x31_ru24.
- Reversals (revpay.py, all 31 instances):

  | count | reversal | at | state | since the previous crossing |
  | --- | --- | --- | --- | --- |
  | 27 | −+ | arena | T | θ changed |
  | 21 | +− | fallback | T | nothing |
  | 5 | +− | fallback | T | θ changed |
  | 2 | −+ | arena | T | θ and w changed |
  | 2 | −+ | arena | T | nothing (x31_re24 / ru24, after ARENA leaves; FBF covers only fallbacks) |
  | 2 | ± | arena | T | nothing |
  | 1 | ± | arena | T | θ changed |
  | 1 | +− | arena | T | θ changed |
  | 1 | +− | fallback | N | (h) lost (oc16_s2) |

- Random runs (zcount.py --rand, n 16-28, o-cyclic 𝒞^1O): seed 501 with random starts: 1,650 games, 5,111 phases, Z ≤ 1;
  seed 502, canonical start: 1,650 games, Z ≤ 1. Random runs are nearly vacuous for (Z), as for every crossing statement so far.

## 6. Climbs on Z (DATA; lclimb.py, fitness (Z, X, T) of the best phase)
Filled in at the end of the box (§9 has the final numbers and the re-verification).

## 7. Natural potentials tested, and why each fails (PROVED-by-instance or DATA as labelled)
Box 3 asked for a potential that rises at every INR/crossing and is not restored by o-free progress. Each candidate below is a
function of data a proof could plausibly control.
- (NG1) Φ(R, θ, w), any function. PROVED-by-instance: x31_re24 (and x31_ru24) has the same (R, θ, w) at states 1 and 5
  (|R| 21), with 4 crossing transitions between, (h) at every state, one phase. So no such Φ rises at every crossing.
  - (R, θ, w, σ|R) does not repeat on any instance under (h). By Lemma RE (R19 (d)) with RM, a vertex of R_k that leaves and
    re-enters with θ constant comes back with a strictly better route. So such a repeat would need all crossers to lie outside R_k.
- (NG2) Φ of R-side data alone (R, σ|R). PROVED-by-instance: lev_l_sc has R = ∅ at states 8 and 32 of one phase, with 16 crossing
  transitions and 23 θ-changes between, (h) throughout.
  - fbref_cex_n32 (states 26, 49): 14 crossings between. Any potential must see θ or F-values.
- (NG3) The trust-gap level rank(u*), u* = top of P(θ) Δ P(w). It is non-increasing while w is constant (Lemma U, box 1), so it would
  pay for carries if carries forced it down.
  - CONJECTURE (U*-DROP) "between consecutive leave transitions with w unchanged, rank(u*) drops" is FALSE: 19 of 19 checks fail on
    fbref_cex_n32, lev_l_x, run_x_inr2, x31_lem_t32 and s_rt32_final (ustar.py).
  - u* is the top-ranked differing vertex (rank 28-31 at n 24-32) and stays fixed through every evicting fallback. The carries
    happen under one unchanged top-level gap.
- (NG4) Tropical / parametric lens.
  - PROVED (elementary, L-SI succ. 2), Lemma TROP: in a one-player game with a terminal t of value ω and no other dependence on ω,
    V_y(ω) = max(Π*_y ⊕ ω, f*_y), where Π*_y is the best route to t and f*_y the best t-free value. ω ↦ Π ⊕ ω is order-preserving,
    so R*(ω) = {y : Π*_y ⊕ ω ▷ f*_y} is an up-set chain in ω, with at most one breakpoint per vertex.
  - So the OPTIMAL crossing structure, as o's value rises, is monotone with ≤ n events.
  - N5's game is not of this form: θ is the value of o's own play, and R must avoid that play (H1).
  - Measured exactly (hterm.py: o made a terminal of value θ_k, plays valued by Engine.extend): the abstract optimum routes through
    θ's own play at 247 vertex-states on lev_l_sc. On fbref_cex_n32 switch-all on the abstract game does not converge.
  - A frozen-copy gadget instead (rstar.py) suffers a rank artefact: copies get ranks different from their originals. Its
    "R* constant per phase" output is not evidence.
  - Obstruction (READING): entering supp(θ's play), which is what an INR does, changes the parameter itself. The parametric curve
    and N5's R are coupled exactly where the monotone structure would help.
- (NG5) CORR = #vertices at their optimum in the abstract game (correct2.py). Not monotone: it drops by 18 at one arena transition
  on lev_l_sc. Since NG4 makes the model ill-posed, this is weak evidence only (DATA).
- What does work: |R| as an amortized potential (LV′). It reduces (X) to the carry count Z and pays for every entry, INR included.
  So box 3's "potential that rises at each INR" is not needed. What is needed is a bound on carries.

## 8. The trusted world: Lemma WM (PROVED, L-SI succ. 2) and the refuted (W-LAY)
**Lemma WM.** Inside a joint λ-phase, at every non-fallback transition, W_{k+1} ⊵ W_k pointwise.
Proof:
- τ is constant in the phase: 𝒞^1O, and τ(o) is part of the phase key.
- σ_{k+1} is N5's Even selection: an optimal strategy of the one-player arena (Even restricted to {σ_k(v)} ∪ Iσ(v), Odd fixed to τ)
  under VJ valuations (SPEC S3; computed as the optimal counterstrategy on the dual, VJ00).
- An optimal one-player strategy's valuation dominates every arena strategy's valuation pointwise. σ_k is an arena strategy.
- Its arena valuation equals W_k: same plays. □
Consequences:
- W-lowerings, i.e. transitions where some W(v) decreases, are fallback transitions (PROVED).
- At a THR fallback, GAP puts every evicted target value inside the gap of σ_k(y), Ξ_k(z) ⊴ W_k(σ_k y). So an eviction trades a
  trusted value for an honest one at most as large.
- DATA (wlay.py): WM has 0 violations on the 31 instances and on 2 × ~1,700 random runs (seeds 601, 602; n 8-20). On every
  instance, #W-lowering transitions = #evicting fallbacks (fbref_cex_n32: 8, s_rt32_final: 6, x31_lem_t32: 5, lev_l_sc: 1).
- Reading: the carries of §1 are exactly the W-lowerings. Between carries, N5 is a switch-best run in the one-player game G_τ, but
  restricted to honest-improving edges.
- CONJECTURE (W-LAY): "between consecutive W-lowerings, at most n − 1 transitions change W" (R17's bound for unrestricted
  switch-best). FALSE (DATA, wlay.py): thclimb_n16_s12 (sha1 6e0704b7) has a phase of 16 transitions, all W-changing, with no
  fallback and no W-lowering, at n 16.
  - There θ changes at every transition, and R grows 0 → 11 one vertex at a time (an INR chain).
  - The arena lacks the W-improving entries that are not honest-improving (θ ◁ w). They are released one per θ-rise.
  - So R17's layering does not transfer to N5's trusted world: θ gates it.

## 9. Re-verification and files
Re-verified in this box (reverify.sh: sha1, n5.py n5 iterations/fallbacks, check_sol2.py = Oink zlk (pinned 8fbf0a7) + verify.py
strategies): all 16 files in experiments/si/orlens/instances, all 14 in experiments/red/xing/instances, box 28's oc16_s2, and
nofe_cyc_n8. Every one: "zielonka(oink zlk) OK strategies verified". The sha1 prefixes and iteration counts are in the reverify
output (§10 of notes/L-SI.md lists them).
Files (experiments/si/xing/):
- xclass.py (active/passive classification, asserts n5.run equality);
- leaves.py (L, LV check, random mode);
- zcount.py (Z, LV′ assert, random mode);
- revpay.py (reversal payers);
- repeats.py (NG1/NG2);
- ustar.py (NG3);
- hterm.py, correct2.py, rstar.py, correct.py (NG4/NG5; rstar/correct carry the rank artefact, kept for the record);
- lclimb.py (climb on Z);
- reverify.sh;
- instances/nofe_cyc_n8.pg + .start.
