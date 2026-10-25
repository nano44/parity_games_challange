# N5 on o-cyclic 𝒞^1O, box 37 (b): the out-of-SN fallbacks at H1 ∧ ¬H2 states (SPLIT, EPOCH, F-FLAT, FREEZE-STEP; CONJECTURE NO-ENTRY)
L-NEW successor 16 (Opus 5.5, D15/D18), session_01LLCK4ctQmkMq2huT44SU7d. Box 37 GO by the Lead 10:34Z (Lead's stamp). Written
2026-10-25 11:0xZ onward by date -u.
- Setting:
  - N5 is SPEC S1-S5 (docs/new/N5-ssi-global.md), on 𝒞^1O (exactly one Odd vertex o of out-degree > 1).
  - A PHASE is a run with λ_Ξ and τ constant. It is a joint λ-phase by Remark KEY (P-N5-SCOPE §1).
  - R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}, R̄_k := R_k ∪ {o}, F_k := V ∖ R̄_k. θ := Ξ(o), w := W(o), c_θ := λ(o), c_w := λ_W(o).
  - H1: o lies on no honest cycle. H2: o lies on no W-cycle.
  - A transition is in-phase if both ends are in one phase. A crossing changes R.
  - An HN STATE has H1 ∧ ¬H2. An HN STRETCH is a maximal run of consecutive HN states of one phase.
  - At an HN state, c_w lies in R̄ and c_θ in F. So HN states are outside the SN regime: they are the "H1 ∧ ¬H2" class of P-N5-SCOPE §7.
  - The OTHER class (H1 ∧ H2 ∧ ¬H3) is not treated here.
- Notation and dependencies are as in P-N5-SCOPE §0 (sha1 c3f5ed37…, l-new 8483279d): R15 (a)/(d), R18 (d) Lemma S (a), R19 (a), R21 (c)
  FBL-N, R23 (b) ACT, R30 (c) R-STICK, R30 (d) H3H2, P-N5-TOG §0 (F), FB-INT (P-N5-SCOPE §4).
- Labels (D18/L40): PROVED (L-NEW succ. 16, unrefereed), CONJECTURE, FALSE, OPEN, DATA. Nothing here is a running-time bound for N5, a
  TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Summary
1. **Lemma SPLIT (PROVED).** At an in-phase transition from an HN state:
   - an S4a step never shrinks R;
   - an Even fallback never grows R̄.
   So inside an HN stretch every crossing is an ENTRY (at S4a) or an EVICTION (at a fallback), never both.
2. **Corollary EPOCH (PROVED).** Let a BREAK be an entry that follows an eviction in the same HN stretch with no entry in between. In an
   HN stretch with B breaks, X ≤ 2(n − 1)(B + 1) and f ≤ n_E(2n − 1)(2(n − 1)(B + 1) + 1). So the f ↔ X loop on HN stretches is exactly
   the count of breaks.
3. **Lemma F-FLAT (PROVED).** An in-phase Even fallback from an HN state changes no honest value on F, and does not change θ. So every
   θ-change inside an HN stretch is at an S4a step.
   - DATA: 0 of the 100 library θ-changes in HN stretches are at fallbacks.
4. **Lemma FREEZE-STEP (PROVED).** Inside an HN stretch with θ constant, a state with no gate into R̄ passes this on to the next state.
   From such a state on, until θ changes or the stretch ends:
   - nothing enters R;
   - R̄ only shrinks;
   - Ξ is frozen on R̄.
5. **ROUTE-FROZEN (FALSE, DEAD END).** The claim was: "after a fallback with θ constant, Ξ on R is frozen". It is false.
   - Instance: experiments/new/box37/instances/rfroz_cex_n16.pg (τ(o) = o), with 8 R-value rises after a fallback.
   - So FREEZE-STEP's hypothesis can fail after a fallback.
6. **CONJECTURE NO-ENTRY (DATA).** Inside an HN stretch, after a fallback, no vertex enters R until θ changes.
   - Library: 0 entries in 282 transitions that follow a fallback with θ constant, against 52 entries before the first fallback.
   - Climbs: 0.
   - Every break is separated from its eviction by a θ-change (11 / 11 in the library).
7. **Reduction (READING).** NO-ENTRY gives B ≤ θ_HN, the number of θ-changes of the stretch, all of them at S4a steps by F-FLAT. So on
   an HN stretch, X and f are ≤ poly(n)·(1 + θ_HN).
   - Case τ(o) = o. The phase has no H2 state at all, so its HN stretches are its H1-runs, and there are ≤ ⌈T/2⌉ + 1 of them (P-N5-TOG).
     So the out-of-SN fallbacks of a τ(o) = o phase are ≤ poly(n)·(1 + T)·(1 + θ) given NO-ENTRY.
   - What remains OPEN: NO-ENTRY itself, and θ-changes per HN stretch. They are not bounded by anything proved; with F1° the count is
     again circular in X.

## 1. Lemma SPLIT (PROVED, L-NEW succ. 16; 𝒞^1O)
Statement. Let k → k+1 be an in-phase transition with H1 ∧ ¬H2 at k.
- (a) If it is not a fallback (so it is an S4a step: τ is constant in a phase, and every iteration changes σ or τ, R15 (d)), then
  R_k ⊆ R_{k+1}.
- (b) If it is an Even S4c fallback, then R̄_{k+1} ⊆ R̄_k. (An Odd fallback changes τ and leaves the phase.)
Proof.
- (a) Let v ∈ R_k.
  - v's (σ_k, τ)-play reaches o and then follows o's W-play.
  - Under ¬H2, o lies on its W-cycle C_W. Every vertex of C_W reaches o, so C_W ⊆ R̄_k, and v's W-cycle node is the top c_w of C_W, a
    vertex of R̄_k.
  - v's honest play agrees with its (σ_k, τ)-play up to o (on 𝒞^1O the two graphs differ only at o), and then follows o's honest play.
    So λ(v) = λ(o) = c_θ.
  - Under H1, c_θ ∈ F_k (R30 (d), proof of H3H2: o's honest cycle avoids o, and its vertices' plays avoid o).
  - So v's W-cycle node differs from λ(v), and R-STICK (R30 (c)) keeps v in R_{k+1}. This is H2-STICK's argument (P-N5-L2 §2), applied to
    every v.
- (b) Suppose R̄ gains a vertex.
  - By ACT (i) (R23 (b)), some switched Even s ∈ F_k has σ_{k+1}(s) ∈ R̄_k.
  - S4c switches only gate edges, so (s, σ_{k+1}(s)) is a gate edge from F_k into R̄_k.
  - By FBL-N (iii) (R21 (c); P-N5-X convention, o ∈ R), if H2 fails at k there is no gate edge from F_k to R_k ∪ {o}. Contradiction. □
- Consequence. Inside an HN stretch, an entry is an S4a transition with R_k ⊊ R_{k+1}, and an eviction is a fallback with R̄_{k+1} ⊊ R̄_k.
  Every crossing is exactly one of the two.
- DATA (epoch.py, 113 library HN stretches; 1,331 random HN stretches, seed 3702): 0 failures of (a) or (b).

## 2. Corollary EPOCH (PROVED, L-NEW succ. 16; 𝒞^1O)
Statement. Let S be an HN stretch. A BREAK is an entry transition of S that is preceded in S by an eviction, with no entry between the
two. Let B be the number of breaks of S, X_S the number of crossings of S, and f_S its number of fallbacks; both count transitions with
both ends in S. Then:
- X_S ≤ 2(n − 1)(B + 1);
- f_S ≤ n_E(2n − 1)(X_S + 1) ≤ n_E(2n − 1)(2(n − 1)(B + 1) + 1).
Proof.
- Cut S just before each break. This gives B + 1 segments.
- Inside a segment no entry follows an eviction: such an entry would be a break, and breaks only start segments. So in a segment every
  entry precedes every eviction.
- Count the crossings of one segment.
  - By SPLIT, before the segment's first eviction R never shrinks, and every entry makes it strictly larger. |R| ∈ [0, n − 1], so there
    are ≤ n − 1 entries.
  - After the first eviction there are no entries, and every eviction makes R̄ strictly smaller, so there are ≤ n − 1 evictions.
  - So a segment has ≤ 2(n − 1) crossings.
- Fallbacks. The crossings of S cut it into ≤ X_S + 1 maximal crossing-free runs. Each lies in one maximal crossing-free run of the phase,
  so FB-INT (P-N5-SCOPE §4) gives ≤ n_E(2n − 1) fallbacks in each. □

## 3. Lemma F-FLAT (PROVED, L-NEW succ. 16; 𝒞^1O)
Statement. Let k → k+1 be an in-phase Even S4c fallback with H1 ∧ ¬H2 at k. Then Ξ_{k+1}(v) = Ξ_k(v) for every v ∈ F_k, and
θ_{k+1} = θ_k.
Proof.
- Step 1: the switched vertices in F_k. Let x ∈ F_k be switched to z.
  - By FBL-N (ii), x = λ_W(x) and λ_W(z) = x. By FBL-N (iii), z ∉ R̄_k, so z ∈ F_k.
  - On F_k, plays avoid o, so honest and (σ_k, τ)-plays coincide and W = Ξ (R19 (a)). Hence λ_k(x) = x and λ_k(z) = x.
  - By (F), Ξ_k(σ_k x) = (x, ∅, L_x − 1).
  - Let q be z's path to its first visit of x. No switched vertex lies on q before x: a switched x′ ∈ F_k is its own cycle node, so a play
    through x′ ends on x′'s cycle, and λ_k(z) = x would force x′ = x. Odd vertices on q are forced (q avoids o).
  - So at k+1, x's honest play is the cycle x → z → q → x, the same for every Odd strategy.
  - If some vertex of q were more relevant than x, the top of that cycle would be that vertex, and λ_{k+1}(x) ≠ x. The transition would
    then leave the phase. So P(Ξ_k z) = ∅: the gate has level −1.
- Step 2: v ∈ F_k.
  - Let c := λ_k(v), and let p be v's honest path to its first visit of c. p lies in F_k.
  - A switched vertex on p before c is its own cycle node, so it would be v's cycle node c. So p contains no switched vertex before c.
  - At c: if c is not switched, its old cycle is intact. (A switched x on it, x ≠ c, would have λ_k(x) = c ≠ x.)
  - If c is switched, the continuation is the cycle c → z_c → q → c of Step 1, topped by c.
  - Either way, under (σ_{k+1}, σ̄_k) the play from v has prefix p and cycle node c, so V_{σ_{k+1}, σ̄_k}(v) = Ξ_k(v).
  - Lemma S (a) (R18 (d)) gives Ξ_{k+1}(v) ⊴ V_{σ_{k+1}, σ̄_k}(v) = Ξ_k(v). R15 (a) gives ⊵. So the two are equal.
- Step 3: θ.
  - Under H1, x0 := σ̄_k(o) has an honest play that never visits o, so x0 ∈ F_k.
  - Under (σ_{k+1}, σ̄_k), o's play is o → x0 followed by x0's play from Step 2, which never returns to o. So o is not a cycle node of it,
    and by (V1), V_{σ_{k+1}, σ̄_k}(o) = o ⊕ Ξ_k(x0) = θ_k.
  - Lemma S (a) and R15 (a) give θ_{k+1} = θ_k. □
- Corollary. Inside an HN stretch, θ changes only at S4a steps.
- DATA (hnstat, library): 113 HN stretches, 100 θ-changes (34 with τ(o) = o, 66 with τ(o) ≠ o), 0 at fallbacks.

## 4. Lemma FREEZE-STEP (PROVED, L-NEW succ. 16; 𝒞^1O) and its tail corollary
Statement. Let t → t+1 be an in-phase transition with H1 ∧ ¬H2 at t, H1 at t+1 and θ_{t+1} = θ_t. Suppose no gate (y, z) ∈ Iσ_t has
z ∈ R̄_t. Then:
- (i) R̄_{t+1} ⊆ R̄_t, and the route (the (σ, τ)-path to o) of every z ∈ R̄_{t+1} is the same at t and t+1;
- (ii) Ξ_{t+1}(z) = Ξ_t(z) for every z ∈ R̄_{t+1};
- (iii) no gate (y, z) ∈ Iσ_{t+1} has z ∈ R̄_{t+1}.
Proof.
- Route form under H1. For z ∈ R̄_k at an H1 state, z's honest play is its route π_z to o followed by o's honest play, which never
  returns to o. No vertex of π_z is the cycle node of its own play. So by (V1) along π_z, Ξ_k(z) = π_z ⊕ θ_k, with ⊕ iterated along π_z.
- (i), S4a case.
  - The arena of v is {σ_t(v)} ∪ Iσ_t(v), and every gate target lies in F_t.
  - An entry needs a switched s ∈ F_t with σ_{t+1}(s) ∈ R̄_t (ACT (i)). That target is not σ_t(s) ∈ F_t, so it is a gate target in R̄_t,
    and there is none. So R̄_{t+1} ⊆ R̄_t. With SPLIT (a), R_{t+1} = R_t.
  - A switched v ∈ R_t would have σ_{t+1}(v) ∈ F_t. Since R̄_{t+1} = R̄_t, that successor is outside R̄_{t+1}, so v ∉ R_{t+1}, a
    contradiction. So no vertex of R_t switches, and routes are unchanged.
- (i), fallback case. SPLIT (b) gives R̄_{t+1} ⊆ R̄_t. Take a switched vertex on the route at t+1 of some z ∈ R̄_{t+1}. Its new successor
  is a gate target in F_t, so it is not in R̄_{t+1}; but the next vertex of the route is in R̄_{t+1}. Contradiction. So routes are unchanged.
- (ii). The route form at t and at t+1 (H1 at both), with the same route and θ_{t+1} = θ_t.
- (iii). Suppose (y, z) ∈ Iσ_{t+1} with z ∈ R̄_{t+1}.
  - Then Ξ_t(z) = Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y). The last two steps use R15 (a) and
    σ_{t+1}(y) ∈ {σ_t(y)} ∪ Iσ_t(y) (R15 (d)).
  - If z = σ_t(y), this reads Ξ_t(z) ▷ Ξ_t(z), which is impossible.
  - Otherwise (y, z) ∈ Iσ_t with z ∈ R̄_t, against the hypothesis. □
- Corollary (TAIL). If some state t of an HN stretch has no gate into R̄_t, then on the rest of the stretch, up to the first θ-change:
  - nothing enters R and R̄ only shrinks, so there are ≤ n − 1 crossings;
  - Ξ is frozen on R̄.
  Proof: induction with FREEZE-STEP. An H1-toggle ends the stretch, and so does an H2-restart. □
- Where the hypothesis holds: at a fallback state there is no gate from F into R̄ (FBL-N (iii)). Gates from R into R̄ can exist there,
  though. When they do, the fallback switches them, R-values rise, and new gates can follow. §5 shows that this happens.

## 5. DEAD END: ROUTE-FROZEN ("after a fallback with θ constant, Ξ on R stays frozen inside an HN stretch") is FALSE (DATA, verified)
- First DATA (rfrozen.py, library): 0 R-value rises in 282 transitions after a fallback with θ constant, against 106 before the first
  fallback. So the conjecture was natural.
- Climb (rfclimb.py, seed 3722, from wd16_s2, 2.5 min) found experiments/new/box37/instances/rfroz_cex_n16.pg.
  - sha1 a9b40395ba9a351037f8dff612d50848540ddbc1; n 16, o = 11, succ(o) = {11, 12, 15}, τ(o) = o, so w = (11, ∅, 0).
  - n5.py n5: 15 iterations / 5 fallbacks. check_sol2.py: "zielonka(oink zlk) OK strategies verified". One Odd choice vertex asserted.
  - Phase ph394, states 4-13: H1 ∧ ¬H2 throughout, θ = (6, 36880, 3) constant.
  - The fallback at 4 → 5 evicts 10. After it, R-values rise at the S4a steps 5 → 6 (σ(9): 13 → 7), 6 → 7 (σ(2): 1 → 9) and 7 → 8
    (σ(13): 0 → 2), and at later fallbacks.
  - In all: 8 transitions with an R-rise after a fallback (5 S4a, 3 fallbacks), and 0 entries.
- Exact obstruction: S4a takes R → R gates that are W-improving, and fallbacks take any R → R gate. So routes inside R keep improving
  after a fallback, and FREEZE-STEP's hypothesis (no gate into R̄) fails at the next state.
- What survives: NO-ENTRY (§6). Entries never followed a fallback on this instance either.

## 6. CONJECTURE NO-ENTRY (DATA) and the reduction (READING)
- Statement: inside an HN stretch, if a fallback occurs at k0, then no S4a transition k ≥ k0 + 1 of the stretch has an entry while θ is
  constant on [k0, k + 1].
- DATA:
  - rfrozen.py, library 429 paths (270 in 𝒞^1O):
    - after a fallback with θ constant: 216 S4a steps and 66 fallbacks, 0 entries;
    - before the first fallback: 205 S4a steps with 52 entries.
  - epoch.py: 11 breaks in the library, all with a θ-change between the eviction and the entry (sep_theta 11; sep_NONE 0; w never changes
    inside an HN stretch). Random (30,000 games, n 4-14, seed 3702): 1,331 HN stretches and no break at all.
  - Climbs: sepclimb.py (fitness = breaks without a θ / w change) seeds 3711-3714, and rfclimb.py MODE=ent seeds 3731-3733. Results: §8.
- Reduction (READING, from §1-§4). Given NO-ENTRY, every break is preceded by a θ-change at an S4a step (F-FLAT), so B ≤ θ_S. EPOCH then
  gives, per HN stretch:
  - X_S ≤ 2(n − 1)(θ_S + 1);
  - f_S ≤ n_E(2n − 1)(2(n − 1)(θ_S + 1) + 1).
- τ(o) = o (the Lead's first case). o is on its W-cycle (the self-loop) at every state of the phase, so H2 never holds, there are no (h)
  or SN states, and the phase's states are H1 (HN) or ¬H1.
  - So its HN stretches are its maximal H1-runs: ≤ ⌈T/2⌉ + 1 of them, with T ≤ n² + 2n − 1 (P-N5-TOG TOGGLE-COUNT).
  - Given NO-ENTRY, the out-of-SN fallbacks of a τ(o) = o phase are ≤ (⌈T/2⌉ + 1)·n_E(2n − 1)(2(n − 1)(θ + 1) + 1), where θ is the
    number of θ-changes of the phase.
  - DATA: 37 library HN stretches with τ(o) = o: at most 11 θ-changes in one (post31_n48, n 48, X 31, f 0), and at most 12 fallbacks
    (wd16_s2, θ 0, X 12).
- What stays OPEN:
  - (1) NO-ENTRY itself. The base case is the open part: after the fallback, R → R gates switched at k0 can raise R-values (§5).
  - (2) θ-changes per HN stretch. θ only changes at S4a steps (F-FLAT), but F1° bounds them by (n − 2) per crossing-free interval, which
    is circular in X. A bound independent of X is the PF-THETA question (poly form, CONJECTURE) moved to HN stretches.
  - (3) OTHER states (H1 ∧ H2 ∧ ¬H3): 2 fallbacks in the library. Not treated.
  - (4) For τ(o) ≠ o, the number of HN stretches per phase. They start after toggles or after (h)-ends, and (h)-runs ≤ 1 + T + f is
    circular in f.

## 7. Angles tried for NO-ENTRY's base case (READING; no proof)
- W-frame potential. For τ(o) = o, w = (o, ∅, 0) is constant, and every R-vertex has W-cycle node o while F ∩ U has cycle node c_θ,
  with reward(o) > reward(c_θ) (XW: θ ⊴ w and c_θ ≠ o). So S4a takes EVERY honest gate from F ∩ U into R̄, and entries come only from
  U = λ^{-1}(c_θ).
  - So NO-ENTRY says: after a fallback, the honest values Ξ(σ y) of F ∩ U never fall below the R̄-values they can reach.
  - R → R gates raise R-values. In the counterexample to ROUTE-FROZEN they did, and no gate from F ∩ U into R̄ appeared. Why it cannot
    appear is the open point.
- Exchange view (matroid-style). At a fallback, the route set of R is W-optimal (FBL-N (i)), and every honest gate from F into R̄ is
  absent (FBL-N (iii)).
  - The R → R gates that remain are honest-better, W-worse exchanges: they swap a route for one with more Even-favourable vertices
    between rank(c_θ) and rank(o), or with the other length parity.
  - A proof would show that such an exchange never raises a vertex of R̄ above an F-neighbour's current Ξ(σ y). No exchange inequality
    of this kind has been found.

## 8. Data and scripts (DATA; experiments/new/box37)
- Every script asserts exactly one Odd vertex of out-degree > 1. File lists skip non-𝒞^1O games and count them (skipped_not_C1O).
- Library: lib37.txt (429 paths: box34/lib.txt + box34/box35/box25 instances + experiments/red/*/instances + experiments/si/coarse/instances
  + docs/referee/R-N5-L2; 270 in 𝒞^1O).
- Scripts:
  - outsn.py: out-of-SN stretches; entries / exits / re-entries; EXIT-UP check;
  - epoch.py: SPLIT check, breaks and their separation by θ / w;
  - rfrozen.py: ROUTE-FROZEN / NO-ENTRY classes;
  - sepclimb.py and rfclimb.py: climbs.
- Logs (committed, data/):
  - outsn_lib.txt: 40 OUT stretches, 107 fallbacks, 47 re-entries (all with Ξ strictly up), max 14 re-entries in one stretch (b5_os_n40,
    9 fallbacks);
  - outsn_rand.txt: seed 3701, 20,000 games; no OUT stretch;
  - epoch_lib.txt, epoch_rand.txt;
  - rfrozen_lib.txt.
- Climb logs are in experiments/new/out/box37 (gitignored). Results so far (11:0xZ):
  - sepclimb (breaks without a θ / w change): 0 found in every run. Epochs reached 5 (seed 3711, b5_os_n40) and 3 (seed 3712).
  - rfclimb (all modes): ROUTE-FROZEN refuted (§5).
  - rfclimb MODE=ent (NO-ENTRY): runs in progress, 0 so far.
