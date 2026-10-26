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
6b. **Theorem NO-ENTRY-A (PROVED, §9).** NO-ENTRY holds when τ(o) = o and o is more relevant than c_θ (case A, 288 of the 321
   checked post-fallback states). The proof is an invariant from the fallback state on, with o as the separator:
   - every R̄-value has o in its path set and no F-value has;
   - every R → R gate has level below rank(o) (Step (K) at the fallback, then induction along routes).
   Case B (c_θ odd and more relevant than o) and τ(o) ≠ o stay CONJECTURE. Data: 0 failures in either case.
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
- Climb logs are in experiments/new/out/box37 (gitignored). Final results (11:41Z by date -u; 25 min per run unless stated):
  - sepclimb MODE=sep (breaks without a θ / w change):
    - seed 3711 (b5_os_n40): FINAL (0, 8, 5) after 75,165 mutations: 8 epochs, every break θ-separated;
    - seed 3712 (b5_os_n12): FINAL (0, 3, 2) after 606,389 mutations;
    - seed 3713 (wd16_s2): stopped by me at about 4 min to free a CPU, with no improvement. Not a result.
  - sepclimb MODE=ep, seed 3714: FINAL (2, −1, 0) after 833,219 mutations; no growth.
  - rfclimb all-rises mode: ROUTE-FROZEN refuted by seed 3722 (§5). Seeds 3721 and 3723 were stopped once the refutation was in.
  - rfclimb MODE=ent (NO-ENTRY):
    - seed 3731 (rfroz_cex_n16): FINAL (0, 19) after 217,044 mutations;
    - seed 3732 (b5_os_n40): FINAL (0, 70) after 19,126;
    - seed 3733 (frz24): FINAL (0, 0) after 741,575.
  - rfclimb MODE=ent2 (case-B seeds b5_os_n12, b5_o11, b5_os_n14; seeds 3741-3743): FINAL (0, 0) after 2.0-3.2 M mutations each.
    These climbs never produced a post-fallback R-rise either (§10).
  - So 0 NO-ENTRY violations in every climb. The case-B precondition was never reached.

## 9. Theorem NO-ENTRY-A (PROVED, L-NEW succ. 16; 𝒞^1O, τ(o) = o, rank(o) > rank(c_θ))
Setting.
- A phase with τ(o) = o. So w = (o, ∅, 0), ¬H2 holds at every state, and W(r) = π_r ⊕ w for r ∈ R̄.
- CASE A: o is more relevant than c_θ (rank(o) > rank(c_θ)). Then Ω(o) is even, because reward(o) > reward(c_θ) by XW (R21 (a)).
- Let S be an HN stretch of the phase, and a ∈ S a state at which an Even fallback a → a+1 is taken. Let θ be constant on a run of states
  [a, b] ⊆ S.
- Write x ≡ y when lev(x, y) < rank(o): the same cycle node and the same path-set vertices of rank ≥ rank(o).
- The VJ00 order is lexicographic by the top of the symmetric difference (SPEC S1; the signed weight is dominated by its top term, SPEC
  Q1). Hence:
  - (T1) if x ◁ y with lev(x, y) ≥ rank(o) and x′ ≡ x, then x′ ◁ y;
  - (T2) ≡-classes are intervals of ⊴: x ⊴ y ⊴ x′ with x ≡ x′ gives y ≡ x;
  - (T3) for every vertex z, z ⊕ · respects ≡.
Separation fact (SEP-o). At an H1 state t of S:
- every z ∈ R̄_t has o ∈ P(Ξ_t z), because Ξ_t(z) = π_z ⊕ θ_t and o ∈ P(θ_t) in case A;
- every f ∈ F_t has o ∉ P(Ξ_t f), because its play avoids o.
So lev(Ξ_t z, Ξ_t f) ≥ rank(o) for such z and f. In particular Ξ_t(z) ≠ Ξ_t(f), and Ξ_t(z) ≢ Ξ_t(f).
Invariant INV(t), for a state t of the run:
- (i) no gate (y, z) ∈ Iσ_t with y ∈ F_t and z ∈ R̄_t;
- (ii) every gate (v, z) ∈ Iσ_t with v ∈ R_t, z ∈ R̄_t has lev(Ξ_t(σ_t v), Ξ_t(z)) < rank(o).
Statement. INV(t) holds for every t ∈ [a, b]. No transition of [a, b] is an entry, R̄ only shrinks, and Ξ_t(z) ≡ Ξ_a(z) for
z ∈ R̄_t.
Proof.
- BASE: INV(a).
  - (i) is FBL-N (iii) (R21 (c)).
  - (ii). Let (v, z) be an R → R gate at a, and suppose ℓ := lev(Ξ_a(σ_a v), Ξ_a(z)) ≥ rank(o).
    - Both values are π ⊕ θ_a with cycle node c_θ. Routes lie in R and θ's path in {o} ∪ F, so the symmetric difference of the two path
      sets is (π_z Δ π_{σ_a v}) ∩ V_{>c_θ}.
    - Its top u has rank ℓ > rank(o): u ≠ o, since o lies in both. Ω(u) is even, since the gate is Even-improving and u lies on z's side.
    - Since σ_a is a pointwise arena optimum in G_τ (FBL-N (i)), it dominates σ_a[v ↦ z] at v (R17 (a) (F1) in the one-player arena).
      Two cases show the switch would raise W at v:
      - z's route avoids v. Then W after the switch is v ⊕ W_a(z). W_a(z) and W_a(σ_a v) have cycle node o, and path sets
        π ∩ V_{>o}. Their top difference is the same u (Even). So v ⊕ W_a(z) ▷ v ⊕ W_a(σ_a v) = W_a(v): the switch raises W at v.
      - z's route passes v, i.e. π_z = q · v · π_{σ_a v}. Then the switched play closes the cycle q · v, whose top is u (the top of
        q ∪ {v} above c_θ). Its cycle node u is even, and reward(u) = p′(u) > p′(o) ≥ reward(o): again W at v rises.
    - Either way, a contradiction.
- STEP: INV(t) ⇒ INV(t+1), for t, t+1 ∈ [a, b].
  - Switched edges are gate edges (R15 (d); S4c). By (i) none goes F_t → R̄_t. So ACT (i) gives no entry, and R̄_{t+1} ⊆ R̄_t.
  - Values on R̄_{t+1} (claim: Ξ_{t+1}(z) ≡ Ξ_t(z)). Induction on z's route distance d to o at t+1.
    - d = 0: Ξ_{t+1}(o) = θ = Ξ_t(o).
    - d ≥ 1: z′ := next_{t+1}(z) ∈ R̄_{t+1}, and Ξ_{t+1}(z) = z ⊕ Ξ_{t+1}(z′) by (V1). z is not a cycle node: its play runs on through o
      into F. Three cases:
      - z is forced or not switched: next_t(z) = z′.
      - z is switched: (z, z′) was an R → R gate at t, so Ξ_t(z′) ≡ Ξ_t(σ_t z) by (ii).
      In each case (T3) and the induction hypothesis give Ξ_{t+1}(z) ≡ z ⊕ Ξ_t(next_t z) = Ξ_t(z).
  - (i) at t+1. Let y ∈ F_{t+1} be Even, z ∈ R̄_{t+1}, and suppose Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y).
    - Their lev is ≥ rank(o) by SEP-o at t+1, so (T1) with Ξ_t(z) ≡ Ξ_{t+1}(z) gives Ξ_t(z) ▷ Ξ_{t+1}(σ_{t+1} y).
    - Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y), by R15 (a) and (d). So Ξ_t(z) ▷ Ξ_t(σ_t y).
    - z = σ_t(y) is impossible, since it gives x ▷ x. So (y, z) ∈ Iσ_t with z ∈ R̄_t.
    - If y ∈ F_t, this contradicts (i) at t.
    - If y ∈ R_t (evicted at the fallback t), it is an R → R gate, so Ξ_t(z) ≡ Ξ_t(σ_t y) by (ii). Then
      Ξ_t(σ_t y) ⊴ Ξ_{t+1}(σ_{t+1} y) ◁ Ξ_t(z), and (T2) gives Ξ_{t+1}(σ_{t+1} y) ≡ Ξ_t(z). But σ_{t+1}(y) ∈ F_{t+1}, so
      o ∉ P(Ξ_{t+1}(σ_{t+1} y)), while o ∈ P(Ξ_t z): a contradiction.
  - (ii) at t+1. Let (v, z) be an R → R gate at t+1 with lev ≥ rank(o).
    - Ξ_{t+1}(σ_{t+1} v) ≡ Ξ_t(σ_{t+1} v) ≡ Ξ_t(σ_t v), by the value claim and (ii) at t if v switched. Also Ξ_{t+1}(z) ≡ Ξ_t(z).
    - So the comparison is decided at the same level ≥ rank(o) at t. That makes (v, z) an R → R gate at t with lev ≥ rank(o),
      contradicting (ii). □
- Corollary (case A, τ(o) = o; given F-FLAT and EPOCH). Every break of an HN stretch is preceded by a θ-change at an S4a step. So
  B ≤ θ_S, X_S ≤ 2(n − 1)(θ_S + 1), and f_S ≤ n_E(2n − 1)(2(n − 1)(θ_S + 1) + 1).
  - Over a τ(o) = o phase of case A, the out-of-SN fallbacks are ≤ (⌈T/2⌉ + 1)·n_E(2n − 1)(2(n − 1)(θ + 1) + 1). θ, the number of
    θ-changes of the phase, stays OPEN.
- What the proof does not cover:
  - case B (c_θ odd and more relevant than o): SEP-o fails, R → R gates at a fallback are honest length-only, and an F-vertex can match
    an R̄-value above level −1;
  - τ(o) ≠ o: the W threshold is c_w, which need not lie on θ's path.
- DATA (inva.py, data/inva_lib.txt; library + rfroz_cex_n16):
  - case A: 288 checked states, case B: 33; 57 later fallbacks;
  - 0 failures of (i), (ii) and (iii) in either case. (ii) holds in case B too, though the proof covers only case A.
  - rfroz_cex_n16 is case A (rank(o) = 12 > rank(c_θ) = 2). Its post-fallback R-rises are at levels 8-11 < 12, as the proof requires.

## 10. Case B (c_θ more relevant than o, τ(o) = o): what is proved, and the exact shape of a violation (OPEN)
- c_θ is odd. reward(o) > reward(c_θ) (XW), and an even c_θ more relevant than o would have the larger reward.
- PROVED (L-NEW succ. 16): at an HN fallback state a in case B, every R → R gate (v, z) is honest length-only (lev = −1), with z's route
  longer than σ_a(v)'s. Proof.
  - Suppose the honest top difference u lies above c_θ.
    - Then rank(u) > rank(c_θ) > rank(o), so the W frame (threshold o) sees the same top u with the same verdict.
    - The switch would raise W at v, by the same two cases as §9 BASE (the cycle case gives cycle node u, which is even since the gate
      is Even-improving, with reward(u) > reward(o)). That contradicts FBL-N (i).
  - So the routes agree above c_θ, and the honest gate is decided by length. c_θ is odd, so the longer route is better for Even.
  - Non-improvement for W then needs one of two things:
    - a W-unfavourable top difference with rank between rank(o) and rank(c_θ);
    - no such difference, and Ω(o) even (W prefers the shorter route).
    Both parities of o are possible in case B: with c_θ odd, −p′(o) > −p′(c_θ), so an odd o also satisfies reward(o) > reward(c_θ).
- So R-rises at a case-B fallback are length-only. A post-fallback entry would therefore need:
  - an F-vertex y with an edge to some z ∈ R̄, and P(Ξ_a(σ_a y)) = P(Ξ_a(z)) = (π_z ∩ V_{>c_θ}) ∪ P(θ);
  - a honest length of σ_a(y) strictly between z's lengths before and after the fallback.
  SEP-o is not available: o is below c_θ and not in P(θ).
- DATA:
  - inva.py: 33 case-B post-fallback states, 0 failures of (i), (ii) or of the frozen-values check;
  - gadget.py (one added Even vertex, every (v, f, priority)) on b5_o11, b5_os_n12, b5_os_n14, wdrop_canon: 0 violations;
  - NO-ENTRY climbs from case-B seeds (MODE=ent2, seeds 3741-3743): no post-fallback R-rise found at all within the first 8 min. The
    precondition (a length-only R → R gate at a case-B fallback) is itself rare.
- CONJECTURE NO-ENTRY-B: the case-B statement of §9. Not proved.
