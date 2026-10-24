# N5 on o-cyclic 𝒞^1O, box 28: non-(h) states (NH), and the (w, u*)-run accounting for (CYC')
L-NEW successor 10 (Opus 5.5, D15/D18). Lead GO 2026-10-24 16:18Z (date -u), box to ~19:20Z. This file was started at 16:35Z (date -u).
Labels (L40): PROVED (by whom; unrefereed unless stated), READING (proof sketch, or a combination whose parts are proved but whose
assembly is not refereed), CONJECTURE (with data), OPEN, DATA.
Scope: N5 (docs/new/N5-ssi-global.md SPEC S1-S5) on 𝒞^1O, inside one joint λ-phase with τ fixed. These are lemmas about the
candidate. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
Notation: P-N5-RE §0 and P-N5-XA §0-§1 (R_k, F_k, π_v, θ := Ξ(o), w := W(o), (h), u*, COARSE). "(h) at k" has three clauses
(P-N5-RE §0):
- H1: the honest play from o (σ_k, σ̄_k) does not return to o;
- H2: the W-play from o (σ_k, τ_k) does not return to o;
- H3: Ξ_k(o) and W_k(o) have the same cycle node.
Code: experiments/new/box28/ (nhprof.py, otherstat.py, otherclimb.py, fbre.py, fbclimb.py). They import box25/common.py.

## 0. Results in short
- PROVED (L-NEW): Lemma XW, Ξ_k ⊴ W_k pointwise at every state (§1). So θ ⊴ w always, and under (h) "throttled" is the same as
  θ ≠ w.
- PROVED (L-NEW, by the proof of box 27 Lemma UT): Lemma EQ (§2). A maximal run of states in one joint λ-phase (τ fixed) with
  Ξ = W at each state has ≤ n − 1 value-changing transitions, **whether or not (h) holds**.
  - This removes from (NH) every non-(h) state with Ξ = W. In random runs these are the large majority of non-(h) states (§6).
- PROVED (L-NEW): Lemma FBL-N (§3), with no (h). At an Even fallback with τ fixed, every gate edge from F is flat. If o lies on
  its W-cycle (¬H2), there is no F → R gate edge at all.
- READING (assembly of proved pieces; §4): (NH) reduces to **(NH')**, the number of transitions with an endpoint in an OTHER state
  (an OTHER state is one where (h) fails and Ξ ≠ W).
- READING (assembly; §5): the (w, u*)-run accounting. Lemmas C, CR, XA and FBL (strong form) are proved state by state. So they
  hold in a whole (w, u*)-run, where θ may change below u*. PIECE needs no θ-constancy (R19 (f)). Hence θ-changes cost nothing
  by themselves. Under (h), and in throttled runs with u* ≠ none, N5's work per joint λ-phase is
      poly(n) · (1 + #w-changes + Σ_runs #non-flat fallbacks in the run + #OTHER-touching transitions).
  - **(CYC') is thereby replaced** by:
    - (W): w-changes per joint λ-phase;
    - (FB-run): non-flat fallbacks per (w, u*)-run;
    - (U0): runs with u* = none.
  - The count of θ-changes (sc32: 43 at n 32) does not enter.
  - Honest limit: on climbed instances non-flat fallbacks per run grow with θ-changes (§6.3). So this is a sharper bookkeeping, not
    yet an easier problem.
- DATA (§6):
  - OTHER-touching transitions per phase: ≤ 5 in random runs; climbs reach 16 at n 16 and 18 at n 24.
  - Non-flat fallbacks per (w, u*)-run: ≤ 2 on the named instances. A climb seeded from L-SI's inr2_n32 reaches 11 at n 32
    (still running).
  - Random samples have almost no throttled runs, so the evidence for (FB-run) is the named instances and the climbs.
- PROVED (L-NEW): Lemma FB-W (§5b). After the coarse freeze, a vertex that a fallback sends to an F-option with w's status at u*
  never re-enters R in that run.
- FALSE (FBRE-F) (§5b): post-freeze fallback evictees DO re-enter. fbref_n48 (n 48, Oink-verified) has 10 such re-entries in one
  (w, u*)-run.
- READING (assembly; §5c, the strongest form): inside a joint λ-phase, N5 makes O(n⁴ (1 + X + O)) transitions, where X = crossing
  transitions (R changes) and O = OTHER-touching transitions. θ-changes, w-changes and u* drop out. So (CYC'), (W), (FB-run) and
  (U0) are all subsumed by **(X)**.
  - Its ingredients are XW, EQ, FBL-N, Lemma G, PIECE (F-part read across w-changes), R17 and R15 (d). It does not use C, CR, XA
    or FBF.
  - DATA: X ≤ n on every named instance; a climb reached X = 33 > n = 32 within 30 s (§5c, §8).
- OPEN: (X) and (NH') per joint λ-phase. G-N5-TIME stays OPEN.

## 1. Lemma XW (PROVED, L-NEW): Ξ_k ⊴ W_k pointwise
Statement. At every state k of any N5 run, and every vertex v, Ξ_k(v) ⊴ W_k(v). In particular θ_k ⊴ w_k.
Proof.
- Ξ_k = Ω_{σ_k, σ̄_k} and W_k = Ω_{σ_k, τ_k} are valuations in the same one-player game G_{σ_k}, where Even is fixed to σ_k and
  Odd chooses.
- σ̄_k is a pointwise-optimal counter-strategy for Odd in G_{σ_k}: VJ00 §5.2, Prop. 5.1 and Lemma 5.2 give Ω_σ = Θ_{σσ̄}
  (eq. (11)); this is fact (F1) on the dual game, signed in RESULTS R17 (a).
- So Ω_{σ_k, σ̄_k}(v) ⊴ Ω_{σ_k, τ}(v) for every Odd strategy τ, in particular τ_k. □
Consequences.
- Under (h), Lemma G gives "Ξ = W iff θ = w". So "throttled" (θ ◁ w) is the same as θ ≠ w.
- With w fixed, once θ = w it stays θ = w: θ is non-decreasing (R15 (a)) and θ ⊴ w.

## 2. Lemma EQ (PROVED, L-NEW, by box 27 Lemma UT's proof): runs with Ξ = W, (h) or not
Statement. Let Q be a maximal run of consecutive states inside one joint λ-phase with τ fixed, such that Ξ_k = W_k pointwise at
every k ∈ Q. Then Q has at most n − 1 value-changing transitions (both endpoints in Q).
Proof. The proof is box 27 Lemma UT's, with Lemma G replaced by the hypothesis Ξ = W.
- At k ∈ Q the gate Iσ_k = {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k(x))} equals G_τ's improving set at σ_k.
  - So an S4a step is a switch-best step of the one-player game G_τ: the pointwise optimum of the arena {σ_k(x)} ∪ I(x)
    (R17 setting).
- At an S4c fallback (Even's, since τ is fixed), S4a returned σ_k, the arena optimum.
  - By the flat-case analysis (R18 (c)), every gate edge is flat.
  - Switching flat edges changes no valuation (box 25 §3, "a fallback at an unthrottled state is W-flat"; that proof uses only
    Ξ = W at k).
  - So W_{k+1} = W_k, and Lemma P's invariant is unchanged across the fallback (P-N5-XA-fixes §5, step 2).
- W's cycle-node map equals Ξ's on Q, and Ξ's is constant in the joint λ-phase.
- R17 Lemma P and Theorem PH, run in G_τ from the first state of Q, give ≤ n − 1 value-changing arena steps. Ξ = W on Q, so
  "value-changing" means the same in both frames. □
- Remark: Q may mix (h)-states (θ = w, box 27 UT) and non-(h) states, e.g. COINCIDENT ones (σ̄(o) = τ(o)), where the two plays are
  the same.

## 3. Lemma FBL-N (PROVED, L-NEW): fallbacks without (h)
Statement. Let k → k+1 be an S4c fallback with τ_{k+1} = τ_k. Then:
- (i) it is Even's, and σ_k is a pointwise optimum of the S4a arena in G_τ;
- (ii) every gate edge (x, z) with x ∈ F_k is flat: x = λ_W(x), and z lies in x's W-region;
- (iii) if o lies on its own (σ_k, τ_k)-cycle (¬H2 at k), then no gate edge goes from F_k to R_k;
- (iv) every edge the fallback switches is a flat F → F or F → R edge, or starts in R_k. Under ¬H2 the flat F → R case is empty.
Proof.
- (i) S4c with τ unchanged means Iσ_k ≠ ∅, so the switch-all is Even's. S4a returned σ_k (R18 (d) Lemma S (c)).
- (ii) x ∈ F_k: x's (σ, τ)-play avoids o, so σ_k(x) ∈ F_k and Ξ_k(σ_k x) = W_k(σ_k x) (Lemma G (a), which needs no (h): R19 (a),
  N-RE-1). The edge is a gate edge, so Ξ_k(z) ▷ Ξ_k(σ_k x), and Lemma XW gives W_k(z) ⊵ Ξ_k(z). So the edge is W-improving. It
  lies in the arena, at the arena optimum, so it is flat (R18 (c)).
- (iii) Take a flat (x, z) with z ∈ R_k. Then λ_W(z) = x. Under ¬H2, z's W-play reaches o and then runs around o's W-cycle C, so
  λ_W(z) ∈ C. Every vertex of C reaches o, so C ⊆ R_k. But x ∈ F_k, a contradiction.
- (iv) follows from (ii) and (iii). □
- What is NOT proved without (h): that R → R gate edges are absent at a fallback. Under (h) that is Lemma G (c). Under H1 alone, an
  R → R gate edge is still route-improving (§4 note), but it need not be W-improving.

## 4. Reduction of (NH) to (NH') (READING: an assembly of proved pieces; L-NEW)
Partition of states inside a joint λ-phase with τ fixed:
- EQ: Ξ = W. This holds at every (h)-state with θ = w (Lemma G), and at every non-(h) state with Ξ = W.
- THR: (h) and θ ≠ w, equivalently (h) and Ξ ≠ W (Lemma G, Lemma XW).
- OTHER: (h) fails and Ξ ≠ W.
This is a partition. Under (h), Ξ ≠ W iff θ ≠ w: by Lemma G, off R Ξ = W, and on R the values are π ⊕ θ and π ⊕ w.
Boundaries:
- EQ ↔ THR: θ = w on one side and θ ≠ w on the other, so θ or w changes. With w fixed, THR → EQ happens once (θ reaches w and
  stays there, §1), and EQ → THR is impossible.
- THR ↔ THR (different (w, u*)-runs): w or u* changes. With w fixed, u* only moves down (box 27 Lemma UD, PROVED), and after
  u* = none it stays none (L-NEW: a θ' with θ ◁ θ' ⊴ w and P(θ) = P(w) must have P(θ') = P(w), by the argument of UD). So at most
  n + 1 runs per w-value between OTHER interruptions.
- Anything ↔ OTHER: the transition touches an OTHER state.
Count per joint λ-phase:
- EQ runs: at most #w-changes + 2 + #OTHER-touching transitions. Each has ≤ n − 1 value-changing transitions (Lemma EQ).
- (w, u*)-runs: at most (n + 1)(#w-changes + 1) + #OTHER-touching transitions. Each is bounded as in §5 (u* ≠ none) or is OPEN
  (u* = none, (U0)).
- OTHER-touching transitions: counted as themselves, (NH').
- Value-preserving transitions come in runs of ≤ 4n(n − 1) (R15 (d)).
So, given (U0) and the §5 bound: iterations per joint λ-phase ≤ poly(n) · (1 + #w-changes + #OTHER-touching transitions +
Σ_runs N_fb(run)).
- Note (H1 alone, used in §3): if H1 holds at k, then Ξ_k(v) = π_v ⊕ θ_k for v ∈ R_k. Lemma G (b)'s honest half uses only "o's
  honest continuation does not return to o" (P-N5-RE §1 (b), proof). L-NEW reading of that proof.

## 5. The (w, u*)-run accounting for (CYC') (READING: an assembly; L-NEW)
A (w, u*)-RUN (L-SI box 2 §0; box 27 §8b) is a maximal run of consecutive states inside one joint λ-phase with:
- τ, w and u* fixed, u* ≠ none;
- θ ◁ w;
- (h) at every state.
θ may change, but only strictly below u* (Lemma UD).
Which lemmas hold in a whole run, with θ varying (L-NEW; each proof was checked for where θ enters):
| lemma | in a (w, u*)-run? | why |
| --- | --- | --- |
| Lemma C (P-N5-XA §2) | yes | per state: P(θ_k) and P(w) agree on V* because u* is the top of their difference at every state of the run; monotone by R15 (a) |
| §1 setting (λ_W constant, u* on no route) | yes | per state (u* ∈ P(θ_k) Δ P(w) lies on o's honest play or W-play at k) |
| Lemma CR (§5) | yes | Lemma P^c's induction uses Lemma C, (Cstrict), (F1) at each step, and a vacuous B-fallback (N-XA-1); never θ's constancy |
| Theorem XA (§6) and its count | yes | step 4 uses only that u* is the top of P(θ_{E+1}) Δ P(w), which holds at every state of the run; step 5 uses Lemma C at L |
| FBL strong form (fixes §1) | yes | a per-state statement at the fallback's state |
| flat fallbacks pass PIECE (fixes §5) | yes | per state; a flat fallback changes no value, so θ is unchanged across it |
| PIECE (R19 (f)) | yes | signed WITHOUT θ-constancy (N-RE-4): τ, w, R constant, (h), no non-flat fallback |
| FBF (fixes §2) | NO | its induction needs Ξ_t(z) = Ξ_L(z) on R, i.e. θ constant. A rising θ re-opens entering edges |
Count for one (w, u*)-run with u* ≠ none. Let N := its number of non-flat fallbacks.
- Entries: first entries ≤ n. Re-entries after an S4a leave (ARE) ≤ n(n − 1) (XA in the run). Re-entries after a fallback leave
  (FBRE) ≤ #fallback leaves ≤ n·N.
- Leaves ≤ entries + n. Crossing transitions X ≤ 2·entries + n = O(n² + nN).
- Every non-flat fallback contains a leave (FBL strong form).
- Value-changing transitions ≤ (n − 1)(X + N + 1) = O(n³ + n²N): PIECE with flat fallbacks passing through, and the separators
  counted once each.
- All transitions ≤ (VC + 1)(4n(n − 1) + 1) (R15 (d)).
So a run costs poly(n)·(1 + N). θ-changes appear nowhere in this count.
- Status: the extension of C / CR / XA from P-N5-XA's θ-constant stretch to the (w, u*)-run is L-NEW's reading of their proofs (the
  table). It was claimed in box 27 §8b, and no referee has checked it. Everything else in the count is signed (R19, P-N5-XA with
  fixes).
- What is left of (CYC'):
  - **(W)**: w-changes per joint λ-phase. Lemma Wo makes w non-decreasing under (h); there is no count. DATA: 0 in the long phases,
    5 in theta_thc24 (box 27 §8).
  - **(FB-run)**: non-flat fallbacks per (w, u*)-run. Within one θ-value FBF shows R only shrinks after a fallback, so there are
    ≤ |R| fallbacks per θ-stretch. A bound independent of θ-changes is OPEN.
  - **(U0)**: u* = none runs (FBL unproved there; XA needs u* ≠ none). There is at most one per w-value (§4).
- Why θ-changes stop mattering (READING): a rising θ only re-opens ENTRY edges (box 26's THETA re-entries, box 27 FBF). Entries
  are paid either by first entries (≤ n), by XA (S4a leaves), or by an earlier fallback leave. Only the last needs the fallback
  count. sc32 (43 θ-changes in one phase, θ changing at every transition) shows the effect: its runs have only first entries, no
  re-entries at all, and ≤ 1 fallback (§6).

## 5b. Fallback re-entries: what is left of (FB-run) (L-NEW, written ~16:42Z by date -u)
Bookkeeping in a (w, u*)-run with u* ≠ none:
- N (non-flat fallbacks) ≤ leaves ≤ entries + n;
- entries ≤ n (first) + n(n − 1) (ARE, by XA) + FBRE;
- FBRE ≤ n · (max FBRE of one vertex).
So **(FB-run) is equivalent, up to poly(n), to bounding FBRE**, the re-entries of vertices that a fallback evicted. The climb
anatomy (§6.3) shows it: 19 non-flat fallbacks in one run at n 32 form one peeling chain inside a single θ-stretch, after a
θ-rising segment of first entries. R only shrinks there (FBF), so the chain is bounded by entries.

Lemma FB-W (PROVED, L-NEW; unrefereed). Let S be a (w, u*)-run with u* ≠ none and first state k_0. Let a fallback at L ≥ k_0 + n − 1
(after the coarse freeze, Lemma CR in the run, §5) evict x from R, switching x to z*. If Ξ_L(z*) has **w's status at u***
(u* ∈ P(Ξ_L(z*)) iff u* ∈ P(w)), then x enters R at no later transition of S.
Proof.
- Status facts. Values with the same cycle node that agree above u* and differ at u* are ordered by their status at u*, and
  w's status is the better one (w ▷ θ is decided at u*). Every R-value ρ ⊕ θ_t (t ∈ S) has θ's status at u*: u* is on no route
  (§1, per state), x ≠ u*, and u* ∈ P(θ_t) Δ P(w) at every state of the run.
- The cycle node is c throughout: λ_Ξ(x) = c is fixed in the joint phase, and x ⊕ Ξ(z*) has the cycle node λ(z*) = λ(x).
- After the freeze, COARSE(Ξ(v)) is constant for every v. So Ξ_{L+1}(z*) ⊵ Ξ_L(z*) (R15 (a)) agrees with it above u*. If its
  status at u* were θ's, it would be strictly smaller. So it also has w's status.
- Ξ_{L+1}(x) = x ⊕ Ξ_{L+1}(z*) (V1; x is not its own cycle node), so it has w's status at u*, and its coarse part is x's frozen
  one.
- For t > L: Ξ_t(x) ⊵ Ξ_{L+1}(x), with the same coarse part. By the same argument it has w's status at u*. But if x ∈ R_t, then
  Ξ_t(x) = ρ_t ⊕ θ_t (Lemma G (b)) has θ's status. So x ∉ R_t. □
- This is box 27 §8c's "one-sided" observation, made exact for fallback leaves.
- Dependency: the coarse freeze in a (w, u*)-run is Lemma CR extended to θ-varying runs (§5 table, L-NEW's reading, unrefereed).
  For a θ-constant throttled stretch, FB-W rests on signed CR alone.
- Same argument, two more post-freeze facts (L-NEW):
  - (i) no arena step k → k+1 moves an R-vertex x to an F-vertex z with Ξ_{k+1}(z) of θ's status at u*.
    - Otherwise W_{k+1}(x) = x ⊕ Ξ_{k+1}(z) would have the same (frozen) coarse part as W_k(x) = ρ ⊕ w, with θ's status at u*
      against w's.
    - So W_{k+1}(x) ◁ W_k(x), against Lemma W (arena steps never lower W);
  - (ii) an arena leave to an F-option with w's status is never followed by a re-entry, by the proof above.
  - DATA: ARE = 0 and arena leaves = 0 in every named run (§6.3).
- DATA before fbref_n48 (fbre.py, the named instances and both climb snapshots):
  - 31 FBRE events in all (inr2_n32 6, rise3_n32 1, thetare_n 1, the FIT=v climb snapshot 23). Every one is a vertex evicted with θ's status at u* ("R-status").
  - 0 re-entries of W-status evictees, even before the freeze.
  - Every one of the 31 had its eviction BEFORE the freeze (eviction index < n − 1 in the run).
- **FALSE (FBRE-F)** (refuted 17:43Z by date -u; it was conjectured at 16:42Z): "in a (w, u*)-run, no vertex evicted by a fallback
  after the coarse freeze re-enters R in that run".
  - Instance: experiments/new/box28/instances/fbref_n48.pg (n 48, sha1 414231a27ba3…, canonical start). Found by fbclimb.py FIT=p
    seeded from returns_rt48.
  - n5.py: 60 iterations, 9 fallbacks; check_sol2.py: Oink zlk OK, strategies verified.
  - One (w, u*)-run, states 3-58 (55 transitions), with w, u* (vertex 28), τ, (h) and θ ◁ w constant at every state.
    - A fallback at run index 48 ≥ n − 1 = 47 (state 51 ≥ k_0 + n − 1 = 50) evicts 10 vertices: 35, 4, 5, 37, 39, 40, 22, 23, 25,
      31.
    - θ changes at index 53, and all 10 re-enter at index 54.
  - Consistency checks on the same run:
    - Lemma C: 0 failures. Coarse values never change in the run, so CR holds trivially.
    - Every one of its 33 FBRE events (23 pre-freeze, 10 post-freeze) is a θ-status ("R-status") evictee, as Lemma FB-W requires.
    - Max FBRE of one vertex = 1, so CONJECTURE (FBRE-1) survives.
  - Obstruction: an eviction decided strictly below u* is undone by a θ-change strictly below u*. That is the recursion one level
    down (box 27 §8c, L-SI box 2-3), and FB-W cannot see it.
- Post-freeze, Lemma FB-W covers the W-status evictions. Post-freeze R-status evictions, where the eviction comparison
  h ▷ ρ ⊕ θ_L is decided strictly below u*, DO re-enter (fbref_n48). That is one level down: the n^depth recursion of box 27 §8c
  and L-SI box 2 §3.

## 5c. One quantity: crossings (READING: an assembly; L-NEW, written ~17:00Z by date -u)
FINAL FORM: docs/new/P-N5-X-box28.md (referee packet, written 17:16Z-17:40Z), Theorem X with Lemmas NF, F1, F2. It
replaces this sketch: step 5 is now Lemma NF, proved with no (h) at k+1, and the constants are explicit (≤ 3n² value-changing
transitions per F-interval).
Claim X. Inside one joint λ-phase with τ fixed, let:
- X := the number of CROSSING transitions (R changes);
- O := the number of transitions with an OTHER endpoint (§4).
Then the phase has O(n⁴ · (1 + X + O)) transitions. θ-changes, w-changes and u* do not appear. So N5 on o-cyclic 𝒞^1O is
polynomial if X and O are poly(n) per joint λ-phase: Lemma Φ (≤ 2n(n − 1) + 1 phases, PROVED box 21) and τ-changes ≤ d − 1.
Ingredients: Lemma XW, Lemma EQ, Lemma FBL-N (§1-§3); Lemma G (a)-(c) (R19 (a)); PIECE (R19 (f)); R17 Lemma P / Theorem PH;
R15 (d). Not needed: C, CR, XA, FBF. Those bound parts of X itself (§5, §5b).
Sketch.
1. F-INTERVALS: maximal intervals of consecutive states in the phase with no OTHER state, no crossing transition and no non-flat
   fallback. F is constant on an F-interval.
2. (F1) In an F-interval the values on F (Ξ = W there, Lemma G (a), no (h) needed) change at ≤ |F| − 1 transitions.
   - At THR states the F → F gate edges are exactly the W-improving ones (Lemma G (a)). At EQ states the gate is G_τ's improving
     set.
   - A transition without crossing maps F into F. So σ_{k+1}|F is an 𝓕-arena strategy whose values dominate the 𝓕-arena optimum,
     hence is one (F1).
   - Fallbacks inside the interval switch only flat F → F edges. At EQ states this is the proof of Lemma EQ. At (h)-states:
     R → R gate edges do not exist (Lemma G (c) at an arena optimum), every F-edge is flat (FBL-N (ii)), and any other switched
     edge would be a crossing. So F-values do not change at fallbacks, and Lemma P's invariant carries over (fixes §5, step 2).
   - λ on F is Ξ's, fixed in the phase. R17 Lemma P / PH on 𝓕 give ≤ |F| − 1 value-changing transitions.
   - This is PIECE's F-part, read across w-changes, θ-changes and EQ states without (h). L-NEW reading; PIECE was signed with w
     constant.
3. (F2) In an F-interval, EQ → THR transitions number ≤ |F| − 1.
   - At such a transition k → k+1, (h) at k+1 gives τ(o) ∈ F_{k+1} = F_k. So o's W-play at k does not return to o (H2 at k), and
     w_k = o ⊕ Ξ_k(τ(o)), which holds at k+1 too.
   - θ_k = w_k (EQ) and θ_{k+1} ⊵ θ_k (R15 (a)). If w_{k+1} = w_k, then θ_{k+1} ⊵ w_{k+1}, so θ_{k+1} = w_{k+1} (XW), against THR.
   - So Ξ(τ(o)) changed: an F-value change, counted by (F1).
   - THR → EQ transitions alternate with them, so an F-interval has ≤ 2|F| + 1 blocks (maximal EQ runs and THR runs).
4. EQ blocks: ≤ n − 1 value-changing transitions each (Lemma EQ).
   THR blocks: w-changes inside them are F-value changes (w = o ⊕ Ξ(τ(o)) under (h)). So they cut the blocks into ≤ (n − 1) +
   #blocks PIECE intervals per F-interval (τ, w, R constant, (h), no non-flat fallback; θ free by R19 (f); flat fallbacks pass,
   step 2). Each has ≤ n − 2 value-changing transitions.
5. #F-intervals ≤ 1 + 2X + 2O.
   - Every non-flat fallback outside an OTHER-touching transition is a crossing transition.
     - At EQ states, fallbacks are flat.
     - At THR states, a non-flat switched edge is a leave, or c's flat F → R edge. That edge puts c into R or makes a vertex of
       π_z leave, and either is a crossing (P-N5-XA-fixes §1, "Why").
6. Value-changing transitions ≤ (1 + 2X + 2O) · O(n²) + X + O. Value-preserving runs are ≤ 4n(n − 1) long (R15 (d)). So there are
   O(n⁴ (1 + X + O)) transitions. □ (sketch)
Status: READING. Every ingredient is PROVED (L-NEW, unrefereed: XW, EQ, FBL-N) or SIGNED (Lemma G, PIECE, R17, R15). Not refereed:
the assembly, and step 2's extension of PIECE's F-part across w-changes and EQ states without (h).
- Consequence for routing: (CYC') and (W) are subsumed. The open quantities for o-cyclic 𝒞^1O are:
  - **(X)**: crossing transitions per joint λ-phase;
  - **(NH')**: OTHER-touching transitions per joint λ-phase.
- What bounds parts of (X) already, inside (w, u*)-runs (§5, §5b): first entries ≤ n per run; re-entries after S4a leaves ≤ n(n − 1)
  per run (XA); non-flat fallbacks ≤ entries + n. FBRE is the open part, and the per-run first entries add up over the runs.
- DATA (xcount.py; longest phases):

  | instance | n | phase length | X (crossing transitions) | entries / leaves | O | θ-changes | w-changes |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | fts_best16 | 16 | 26 | 14 | 14 / 4 | 0 | 8 | 0 |
  | sc32 | 32 | 44 | 30 | 45 / 19 | 0 | 43 | 0 |
  | theta_tp32 | 32 | 41 | 22 | 28 / 4 | 0 | 16 | 0 |
  | returns_rt48 | 48 | 78 | 29 | 55 / 43 | 0 | 3 | 0 |
  | returns_ph64 | 64 | 103 | 30 | 78 / 56 | 0 | 3 | 0 |
  | inr2_n32 | 32 | 27 | 14 | 43 / 23 | 0 | 19 | 0 |
  | wd16_s2 | 16 | 12 | 12 | 0 / 12 | 12 | 0 | 0 |
  | oc16_s2 | 16 | 16 | 3 | 9 / 9 | 16 | 0 | 0 |

  - X ≤ n on every named instance.
  - Anatomy of the X climb best at 513 s (X = 40, n 32, phase of 46 transitions, all THR until the last; 16 θ-changes, 0 w-changes):
    - 21 arena steps, each adding ONE vertex to R;
    - one fallback evicting all 23 vertices at once;
    - 24 more arena steps adding one vertex each;
    - the phase ends at an EQ state.
    So X ≈ n · (number of re-entry WAVES), and each wave sits behind a fallback peel and a θ-change (FBF). It is the same wave
    shape as rt48 / ph64 (§5b).
  - X climb best at 1309 s (experiments/new/box28/instances/x32_sc32_1309s.pg, sha1 3e9ef741d5e9…, canonical start; n5.py 63
    iterations, 3 fallbacks; check_sol2.py: Oink zlk OK, strategies verified) (X = 49, n 32, phase of 54 transitions, 24 θ-changes, 0 w-changes, 0 OTHER): THREE waves (peels of 24
    and 10 vertices). Each wave lies in a DIFFERENT (w, u*)-run (u* = vertices 25, 18, 10, 17 by id), and FBRE = 0 in every run.
    The re-entries of a wave are FIRST entries of the next run.
  - **So per-run statements (XA, FBRE-F, FBRE-1) cannot bound X by themselves.** The waves move across u*-levels. The two
    accountings feed each other:
    - per run: crossings ≤ O(n²) + 2·FBRE;
    - runs per phase ≤ (n + 2)(#w-changes + 1) + O (Lemma UD);
    - w-changes at (h)-transitions ≤ (n − 1)·#F-intervals (Lemma F2 with F1);
    - F-intervals ≤ 1 + X + O.
    Each turn of this loop multiplies by poly(n), and the loop does not close. Bounding X needs a potential that survives the
    change of u*-level.
  - CONJECTURE (FBRE-1): in a (w, u*)-run, a vertex re-enters after a fallback leave at most once.
    - DATA: max 1 on every named run.
    - fbclimb.py FIT=v (fitness: max FBRE of one vertex in a run), seeded from inr2_n32, stayed at 1 for ~210 s while total FBRE
      rose to 25.
    - Alone it does not close (X): first entries reset in every (w, u*)-run, and runs per phase are counted through w-changes,
      which §5c counts through X.
  - xclimb.py (fitness: crossing transitions minus OTHER-touching ones, in one phase), seeded from sc32: 33 > n = 32 after 29 s.
    Running; final numbers in §8.

## 6. Data (DATA, not proof)
### 6.1 Non-(h) transitions (nhprof.py, otherstat.py)
- Named instances (phaseprofile convention: a transition is non-(h) if (h) fails at either endpoint):
  - fts_best16, sc32, thetare_n, i1h_fts_best16: 0 non-(h) transitions in their long phases.
  - wd16_s2 (n 16, box 25): one phase of 12 transitions, all non-(h), H1 holds and H2, H3 fail ("23"), SPLIT (σ̄(o) ≠ τ(o)).
    - 11 consecutive Even fallbacks.
    - Each evicts ONE vertex from R (a chain 10 → 6, 0 → 10, 15 → 0, 13 → 15, …), changing Ξ and W at that vertex.
    - Then an arena step jumps every value to a new cycle node, and the phase ends.
    - The chain length (11) is < n. Box 25 §7's climb for this fitness gave 7 at n 12 and 12 at n 16.
- Random o-cyclic 𝒞^1O (n 6-16; seeds 2801-2804, about 19,000 runs, canonical and random starts):
  - non-(h) transitions per phase ≤ 5;
  - SPLIT non-(h) transitions per phase ≤ 3;
  - Ξ-changing non-(h) transitions per phase ≤ 5.
- Clause patterns (otherstat.py, seeds 2811/2812, 5,263 runs), in state counts:
  - non-(h) EQ states: 4,506 coincident "12" and 692 split "12";
  - OTHER states: "13" 985, "3" 610, "23" 451, "123" 420, "12" 96.
  So OTHER states occur with every clause pattern, including H1 ∧ H2 ∧ ¬H3 ("3"), where Lemma G (a)-(b) still hold but the cycle
  nodes differ.
### 6.2 OTHER-touching transitions per phase (otherclimb.py; canonical start; climb running at the time of writing)
| n | seed | best (OTHER-touching, of them Ξ-changing, total) | at |
| --- | --- | --- | --- |
| 12 | 1 | (7, 6, 8) | 205 s (stopped at ~4 min to free a core) |
| 16 | 2 | (16, 16, 24) | 155 s |
| 20 | 3 | (8, 8, 16) | 171 s (stopped at ~4 min) |
| 24 | 4 | (18, 18, 18) | 189 s |
- The n 16 best (snapshot experiments/new/box28/instances/oc16_s2.pg, sha1 859f564f1276…, canonical start; n5.py 26 iterations,
  3 fallbacks; check_sol2.py: Oink zlk OK, strategies verified; wd16_s2 re-checked the same way: 19 iterations, 14 fallbacks, OK): one phase of 16 transitions, all at "23" SPLIT states (H1, o on
  its W-cycle), θ and w constant, 14 arena steps and 2 fallbacks, each changing 1-9 vertices. So OTHER phases are not only fallback
  chains: arena steps in G_τ also run there, with W's cycle-node map not tied to the joint phase.
### 6.3 (w, u*)-runs (fbre.py)
| instance | run (states) | θ-changes | fallbacks | leaves by fallback / arena | re-entries FBRE / ARE | first entries |
| --- | --- | --- | --- | --- | --- | --- |
| sc32 | 7-25 | 17 | 1 | 19 / 0 | 0 / 0 | 16 |
| sc32 | 28-46 | 18 | 0 | 0 / 0 | 0 / 0 | 21 |
| fts_best16 | 2-16 | 3 | 2 | 4 / 0 | 0 / 0 | 2 |
| inr2_n32 (L-SI) | 5-23 | 17 | 1 | 23 / 0 | 6 / 0 | 18 |
| rise3_n32 (L-SI) | 5-18 | 12 | 1 | 21 / 0 | 1 / 0 | 16 |
| thetare_n | 3-6 | 1 | 1 | 2 / 0 | 1 / 0 | 1 |
- In every named run, all leaves are fallback leaves and ARE = 0. The re-entries are FBRE, bounded by fallback leaves ≤ n·N.
- Random runs (seeds 2821/2822, 6,942 games, n 8-16): 12 (w, u*)-runs with a transition, 0 fallbacks. The samples are vacuous here,
  as both referees found for P-N5-XA.
- fbclimb.py (fitness: non-flat fallbacks in one (w, u*)-run, then FBRE, then θ-changes), seeded runs at n 32:
  - from inr2_n32: (7, 2, 4) after 17 s, then (11, 21, 8) after 129 s;
  - from sc32: (1, 22, 10) after 123 s.
  Running at the time of writing; final numbers in §8.
  - Reading of the (11, 21, 8) point: 11 non-flat fallbacks with 8 θ-changes, so some θ-stretches hold several fallbacks (FBF
    allows ≤ |R| per θ-stretch).
  - **So (FB-run) may be as hard as (CYC') itself.** The §5 accounting moves the open count from θ-changes to fallbacks. It does
    not make it smaller in general. Its gain is on runs like sc32's, where θ changes at every transition but fallbacks are rare.

### 6.4 Mechanical checks of Lemmas XW, EQ and FBL-N (eqcheck.py; DATA)
- Named instances: wd16_s2, oc16_s2, sc32, returns_rt48, returns_ph64, inr2_n32, fts_best16, fts_ph16, theta_tp32.
- Random runs: seeds 2831 (random starts) and 2832 (canonical), 5,284 runs, n 6-14.
| check | count | failures |
| --- | --- | --- |
| XW: Ξ ⊴ W at every vertex of every state | 144,367 random + 16,192 named | 0 |
| EQ: Ξ-changing transitions in a maximal Ξ = W run ≤ n − 1 | 9,026 random runs + 18 named | 0 (max excess over n − 1: −3) |
| FBL-N (ii): gate edges from F at Even fallbacks (τ unchanged) are flat | 211 edges at 245 fallbacks | 0 |
| FBL-N (iii): no F → R gate edge at a fallback when ¬H2 | same | 0 |
- Weak spot: the EQ runs seen are short (excess ≤ −3). A climb on the EQ-run length would test Lemma EQ harder; the proof does not
  depend on data.

## 7. Open items after box 28 (for the Lead's routing)
- **(X) OPEN, the main item** (§5c): crossing transitions per joint λ-phase. Data: X ≤ n named; the climb is above n (§8). The
  (w, u*)-run lemmas (XA, FBF, FB-W) bound parts of it; FBRE and the per-run first entries are what remain.
- (NH') OPEN: OTHER-touching transitions per joint λ-phase. Sub-cases by clause:
  - "23" (H1, o on its W-cycle): FBL-N (iii) holds, and the honest values on R are routes ⊕ θ. The W-values on R run to o's W-cycle,
    not through o, so Lemma G (b)'s W half fails.
  - "3" (H1, H2, different cycle nodes): Lemma G (a)-(b) hold, but the coarse equality of Lemma C fails at the cycle node.
  - "13", "123", "12"-split: o on its honest cycle.
- (W) OPEN: w-changes per joint λ-phase.
- (FB-run) OPEN: non-flat fallbacks per (w, u*)-run. This is equivalent, up to poly(n), to FBRE (§5b).
  - Lemma FB-W (PROVED): post-freeze W-status evictees never re-enter.
  - (FBRE-F) is FALSE (fbref_n48).
- (U0) OPEN: u* = none runs (FBL there, and XA's step 4).
- The table in §5 (C / CR / XA in a (w, u*)-run) needs a referee check before the accounting is promoted.

## 8. Final climb numbers (DATA; canonical starts; every listed best checked with n5.py + check_sol2.py: Oink zlk OK, strategies verified)
| climb | fitness | seed instance | n | final best | instance (sha1) |
| --- | --- | --- | --- | --- | --- |
| otherclimb.py | OTHER-touching transitions in one phase | random | 16 | 16 (all Ξ-changing; 24 in total) | instances/oc16_s2.pg (859f564f1276…) |
| otherclimb.py | same | random | 24 | 19 (stopped ~16:55Z) | instances/oc24_s4_final.pg (11e569928f58…) |
| fbclimb.py | non-flat fallbacks in one (w, u*)-run | inr2_n32 | 32 | 23 (FBRE 0, 12 θ-changes; 25 leaves, 23 first entries) | instances/fb32_inr2_final.pg (9381946b22ed…) |
| fbclimb.py FIT=p | post-freeze FBRE in one run | returns_rt48 | 48 | **10: refutes (FBRE-F)** (§5b) | instances/fbref_n48.pg (414231a27ba3…) |
| fbclimb.py FIT=v | max FBRE of one vertex in one run | inr2_n32 | 32 | 1 (total FBRE 25; stopped at ~4 min) | — (snapshot not kept) |
| wclimb.py | w-changes at THR-touching (h)-transitions in one phase | theta_thc24 | 24 | 15 (θ-changes 16; 17 iterations) | instances/w24b_thc24_final.pg (6a211047db99…) |
| xclimb.py | crossing transitions (minus OTHER-touching) in one phase | sc32 | 32 | 54 (phase of 72 transitions, 17 θ-changes, 0 w-changes) | instances/x32_sc32_final.pg (c871404fbabc…) |
| xclimb.py | same | returns_rt48 | 48 | 70 (phase of 110 transitions, 5 θ-changes, 0 w-changes; 21 fallbacks in the run) | instances/x48_rt48_final.pg (cff46249005e…) |
- Readings:
  - All growth seen is linear in n: X ≈ 1.7n at n 32 and 1.46n at n 48; phase length ≈ 2.25n and 2.3n. No superlinear family is claimed.
  - The w-climb's 15 at n 24 is consistent with Lemma F2: w-changes are F-value changes, ≤ |F| − 1 per F-interval.
  - The non-flat-fallback climb is consistent with "fallbacks ≤ leaves ≤ entries + n".
- An earlier wclimb.py run (out/w24_thc24_unthrottled_fitness.*) counted w-changes at UNTHROTTLED transitions and reached 16. Those
  lie inside one Ξ = W run, so they are harmless by Lemma EQ, and the fitness was corrected.
