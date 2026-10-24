# N5 on o-cyclic 𝒞^1O, box 27: crossings in throttled stretches (XING), via a coarse valuation
L-NEW successor 9 (Opus 5.5, D15). Lead GO 2026-10-24 14:22Z (date -u), box to ~17:20Z, stop rule ~16:45Z.
Labels (L40): PROVED (by whom), READING (proof sketch), CONJECTURE (with data), OPEN. ASSUMPTION used throughout: (h) at the states
involved. Nothing here covers states where (h) fails. No running-time claim for N5. G-N5-TIME stays OPEN.
The packet P-N5-RE (docs/new/P-N5-RE-box26.md, pinned at trunk 52c7261) is NOT edited. §0 corrects box 26's notes and adds the
example the Lead asked for.
Notation: box 26 (docs/new/N5-reentry-box26.md) and the packet, §0-§1:
- R, F, routes ρ, o-free values h, Lemma G (a)-(c), Lemma W (box 21 §2.5), R15 (a) (Ξ non-decreasing);
- a (θ, w)-STRETCH is a run inside one joint λ-phase with τ, θ, w constant and (h) at every state;
- THROTTLED means θ ◁ w.
Code: experiments/new/box25/ (coarsecheck.py, fbedges.py, crossings.py, xingclimb.py, xtrace.py).

## 0. Corrections and additions to box 26 (written ~14:31Z by date -u)
- CORRECTION to box 26 §7.3 data and to the 14:12Z (XING) conjecture. The crossing climbs xc16, xc24, xcf20 and tr20_s4 have θ = w at
  every state of their long stretches, so they are UNTHROTTLED. There the band is empty, and the stretch is already bounded:
  - Lemma G with θ = w gives Ξ = W, and the gate is exactly G_τ's improving set;
  - fallbacks are W-flat (box 25 §3, PROVED);
  - box 21 Lemma PT with R17 Theorem PH then gives ≤ n − 1 value-changing transitions per stretch (PROVED by combining those
    results).
  - So those numbers say nothing about (XING). Re-measured on throttled stretches only (crossings.py, now the default):

    | instance | n | crossing transitions per throttled stretch | max crossings of one vertex |
    | --- | --- | --- | --- |
    | theta_tp32 | 32 | 10 | 1 |
    | returns_rt48 | 48 | 9 | 2 |
    | returns_ph64 | 64 | 9 | 2 |
    | fts_best16 | 16 | 3 | 2 |
    | thetare_n | 11 | 1 | 1 |
    | xc16 / xc24 / xcf20 / tr20_s4 | | 0 | 0 |

  - The conjecture of box 26 §7.3 is restated: crossing transitions per THROTTLED (θ, w)-stretch are poly(n). §2-§3 below reduce it
    further.
- EXAMPLE for the packet's Corollary RE: L-COMP's thetaA_canon_n8 (experiments/n5-exhaustive/instances/thetaA_canon_n8.pg, sha1
  10c55131…; Lead re-run Oink OK, strategies verified). It is the smallest canonical-start instance of a non-ROUTE re-entry:
  - class WRISE after an arena leave, with θ = w rising via an Even move at τ(o) = 7;
  - consistent with Lemma RE: the re-entry's interval contains a θ-change.
- L-COMP's thetaA_n6 (n 6, random start) is the same kind (WRISE, θ = w from state 1, unthrottled).
- On T29 Lemma B (Johnson reweighting). A reweighting preserves every comparison N5 makes, so it preserves the band. The band
  comes from the gate and the selection valuing o at different terminals (θ against w), not from a lack of increasingness. What
  removes it is a COARSENING (§1), not a reweighting.

## 1. The coarse valuation: one algebra on the band
Fix a throttled (θ, w)-stretch.
- By (h), θ and w have the same cycle node c.
- Let u* := the most relevant vertex of P(θ) Δ P(w), where w beats θ, if P(θ) ≠ P(w). Otherwise u* := none, and θ, w differ only
  in length.
- For a value v = (c', P, ℓ), put COARSE(v) := (c', P ∩ {vertices more relevant than u*}). It ignores the length, and keeps all of
  P when u* = none. Order: cycle node first, then path set, as in VJ00.
Lemma C (PROVED, L-NEW). At every state of the stretch, COARSE(Ξ(v)) = COARSE(W(v)) for every v, and COARSE(Ξ(v)) is non-decreasing
along the stretch, fallbacks included. So COARSE(W) is non-decreasing too, even where W drops (box 25 §3).
Proof.
- If v ∈ F, then Ξ(v) = W(v) (Lemma G (a)).
- If v ∈ R, then Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w (Lemma G (b)). π_v is disjoint from both continuations, and
  P(θ), P(w) agree above u*. So the coarse parts agree.
- Monotonicity is R15 (a), since COARSE is order-preserving (⊵ implies coarse ⊵). □
Lemma FBL (PROVED, L-NEW). Let a fallback happen at a throttled (h)-state. Then every edge it switches is either a LEAVE (x ∈ R,
z ∈ F, type d2) or a flat switch at a cycle node of F. In particular, F's plays are unchanged except for flat switches, and every
non-flat fallback contains a leave.
Proof.
- The fallback fires only when the S4a arena optimum is σ itself. By (F1) σ is then pointwise optimal in the arena, so no gate edge is
  strictly W-improving. Flat switches at a vertex's own cycle node are the only W-ties allowed by R15 (b) / the P-N5-1OA flat case.
- By Lemma G (d), a gate edge that is not W-improving is of type (d2), x ∈ R and z ∉ R.
  - Gate edges R → R and F → F are honest-improving iff W-improving (Lemma G (c), (a)).
  - Gate edges F → R are honest-improving, hence W-improving, since w ⊵ θ.
- S4c switches every vertex that has a gate edge. □
DATA (fbedges.py): every switched edge at the 36 throttled (h)-fallbacks of fts_best16, theta_tp32, returns_rt48, returns_ph64,
i1h_fts_best16, fbh_drop9 and fbh_thr is a leave (D2 77, other 0). No such fallback in 15,000 random runs.
Lemma CR (coarse R17; L-NEW; written out in full in §7, PROVED-in-writing, referee check pending). It transcribes R17 Lemma P / Theorem PH into the coarse order. The fallback-step part of
Case B is new and is proved below; the transcription of R17's Case B sub-cases (B1/B2, cycle creation) into the coarse order is
argued, not written out. In a throttled (θ, w)-stretch (fallbacks allowed), coarse values change only at the first n − 1 transitions of the
stretch.
Proof.
- Work in the one-player game G_τ with the coarse order. By Lemma C, COARSE(Ξ) = COARSE(W) =: Ω^c.
- R17 Lemma P (docs/new/N5-phase-bound-box10.md §2) uses four things: (V1), (V2), (F1) for the step taken, and (F2) monotonicity.
  - (V1) and (V2) hold for the coarse order: the prefix x ⊕ adds x to the coarse set iff x is more relevant than u* (and than the
    cycle node), on both sides at once.
  - (F2): Lemma C.
- Case B. The edge (x, z) is coarse-improving. Then it is fine Ξ-improving, so it is in the gate.
  - At an ARENA step, (F1) for the arena (fine W) gives W_{k+1}(x) ⊵ val_{σ̂}(x). Hence Ω^c_{k+1}(x) ⪰ coarse(val_{σ̂}(x)).
  - At a FALLBACK step (throttled, (h)), by Lemma FBL x is in R, z ∈ F, and x switches to its honest-best gate edge z* ∈ F. The F side
    is unchanged, so z*'s path avoids x, and
        Ξ_{k+1}(x) = x ⊕ Ξ_k(z*) ⊵ x ⊕ Ξ_k(z)    ((V1), honest-best, (V2)).
    Take coarse.
- Case A is R17's case A with coarse values. Case A2 (x its own cycle node) is unchanged.
- Hence after j transitions, Ω^c_j(x) ⪰ coarse(value(r)) for every simple path r of ≤ j edges from x to a cycle node of the phase
  (paths through o continue along τ(o) in G_τ).
- After n − 1 transitions every Ω^c(x) is maximal among such coarse path values. Later values are values of actual plays, i.e. of
  such paths, so they cannot increase, and by monotonicity they cannot decrease. □
DATA (coarsecheck.py): C1 (coarse Ξ = coarse W) and C2 ("last coarse change ≤ n − 1") hold with 0 failures, fallbacks included:
- on fts_best16, theta_tp32, returns_rt48, returns_ph64, theta_thf16, thetare_n, i1h_fts_best16;
- on 8,000 random runs.
- Max index of the last coarse change: 10 (theta_tp32, n 32). On returns_rt48 / ph64, throttled stretches of 40 / 56 transitions have
  no coarse change at all.

## 2. Re-entries after arena leaves are paid by coarse progress
Theorem XA (L-NEW). The strict coarse increase per re-entry is PROVED (Lemma W, R15 (a), Lemma C). The count ≤ n(n − 1) is READING,
because it uses Lemma CR.
- Setting: a throttled (θ, w)-stretch with u* ≠ none. Let x leave R at L by an arena step, its own or downstream of one, i.e. no
  fallback at L. Let x next re-enter at E inside the stretch.
- Claim: COARSE(Ξ_{E+1}(x)) ▷ COARSE(Ξ_L(x)).
- So inside one stretch, such re-entries number at most Σ_x #(coarse increases of x) ≤ n(n − 1), and all of them lie in the first
  n − 1 transitions.
Proof.
- At an arena step, Lemma W gives W_{L+1}(x) ⊵ W_L(x) = π^L ⊕ w. Since x ∈ F_{L+1}, W_{L+1}(x) = Ξ_{L+1}(x).
- By R15 (a), Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x). By Lemma G (b), Ξ_{E+1}(x) = π^{E+1} ⊕ θ. So π^{E+1} ⊕ θ ⊵ π^L ⊕ w.
- Suppose the coarse parts were equal, i.e. the route vertices above u* coincide. The two sides then first differ at u*, which lies on
  a continuation and not on either route. There w is better, so π^{E+1} ⊕ θ ◁ π^L ⊕ w, a contradiction.
- Hence the coarse parts differ, and the fine order forces the coarse one strictly up. Count: Lemma CR. Each of at most n − 1
  transitions raises at most n vertices. □
When u* = none (P(θ) = P(w), only lengths differ): the same argument gives, at equal coarse value, a strictly shorter or strictly
longer route (by the parity of c). That allows at most n re-entries per coarse value, so ≤ n²(n − 1) per stretch. (READING: the same
proof with the length added.)

## 3. The per-stretch reduction
Corollary (READING, since it uses Lemma CR; L-NEW). In a throttled (θ, w)-stretch S with u* ≠ none:
- entries(x) ≤ 1 + re-entries(x), and leaves(x) ≤ 1 + entries(x);
- the non-flat fallbacks of S are at most the leaves at fallbacks (Lemma FBL). Flat fallbacks change no value, and R15 (d) bounds them
  by 4n(n − 1) between value changes;
- re-entries = (after arena leaves: ≤ n(n − 1), Theorem XA) + (after fallback leaves: (FB-RE)).
- Hence:
      crossing transitions(S) + non-flat fallbacks(S) ≤ 4n + 4n(n − 1) + 4·FB-RE(S),
  and by PIECE (packet §5):
      value-changing transitions(S) ≤ (n − 1)·(5n + 4n(n − 1) + 4·FB-RE(S) + 1).
- So inside a throttled (θ, w)-stretch everything is polynomial except (FB-RE).
- (FB-RE) = 0 by Lemma FBF (§5, PROVED). The bound is therefore O(n²) crossings and fallbacks per throttled stretch (READING, via
  Lemma CR).
(FB-RE), as first stated (superseded by §5): re-entries, inside one throttled (θ, w)-stretch, of vertices whose last leave was forced
by a fallback.
- By Lemma RE each such re-entry strictly improves x's route (θ constant). It may do so below u*, with no coarse gain.
- DATA (coarsecheck.py, reentry.py): 0 inside a stretch on every pinned instance.
  - returns_rt48: one throttled stretch of 40 transitions with 42 fallback leaves, 0 re-entries inside it.
  - All THETA re-entries of box 26 come after fallback leaves, but in a LATER (θ, w)-stretch (θ changed), so they are not FB-RE.

## 4. Where this leaves N5 on o-cyclic 𝒞^1O (READING; assumes (h))
N5 on o-cyclic 𝒞^1O is polynomial if the following are poly(n) per joint λ-phase:
- (a) (θ, w)-stretches, i.e. θ-changes plus w-changes. (CYC) and Lemma Wo: w is monotone, but its changes are not otherwise
  bounded.
- (b') (FB-RE) per throttled stretch. CLOSED by Lemma FBF (§5): it is 0.
- (d) Transitions at states where (h) fails.
Unthrottled stretches are bounded by Lemma PT + R17 (§0). Throttled stretches are bounded by §3 given (b').
Fallbacks are no longer a separate item inside throttled (h)-stretches: §3 bounds the non-flat ones and R15 (d) the flat ones.

## 5. Lemma FBF: after a throttled fallback, R is frozen for the rest of the stretch (PROVED, L-NEW, 14:42Z)
Statement. Let an Even S4c fallback happen at transition L at a throttled (h)-state. Then for every later state t of the same
(τ, joint-λ, θ, w)-stretch (with (h) at every state):
- R_t ⊆ R_{L+1};
- every v ∈ R_t has the same route as at L;
- no vertex enters R at any transition in [L+1, t).
Proof.
1. At L the S4a arena optimum is σ_L (a stall). By (F1) no gate edge at L is W-improving. In particular, at L:
   - (i) no R → R edge is in the gate: R → R edges are honest-improving iff route-improving iff W-improving (Lemma G (c));
   - (ii) no F → R edge is in the gate: an honest-improving entering edge is W-improving, since w ⊵ θ.
2. The fallback switches only leaves (Lemma FBL). A vertex of R_{L+1} has an unchanged path: had its path met an evicted vertex, it
   would follow that vertex's new o-free path and be outside R. So the routes of R_{L+1} are the L-routes, with the same values
   (θ and w are unchanged).
3. Induction on t. Assume R_t ⊆ R_{L+1}, the routes are as at L, and no entry has happened.
   - R → R edges (x, z) at t: route values are as at L, so (x, z) is route-improving at t iff at L. By (i) none is.
   - F → R edges (y, z) at t, with z ∈ R_t: Ξ_t(z) = π_z ⊕ θ = Ξ_L(z).
     - If y ∈ F_L, then along y's switches since L each new successor had strictly higher honest value at its switch, and R15 (a)
       keeps those values from falling. So Ξ_t(σ_t(y)) ⊵ Ξ_L(σ_L(y)) ⊵ Ξ_L(z) by (ii).
     - If y was evicted at L (y ∈ R_L), its new successor z* satisfies Ξ_L(z*) ▷ Ξ_L(σ_L(y)) (a gate edge). Also
       Ξ_L(σ_L(y)) ⊵ Ξ_L(z) for every z ∈ R_L, by (i) applied to y. Then R15 (a) along y's later switches gives the same conclusion.
     So no F → R edge is honest-improving at t, and none is in the gate.
   - Every step switches only gate edges, arena or fallback alike. So no vertex of R switches to another R-vertex, and no vertex
     enters R; R can only lose vertices. The routes of the remaining R-vertices are unchanged, and the hypothesis holds at t+1. □
DATA (box25/fbfcheck.py): 0 entries and 0 route changes in 141 post-fallback transitions after 39 throttled fallbacks:
- fts_best16, theta_tp32, returns_rt48, returns_ph64, i1h_fts_best16, theta_thf16, fbh_drop9;
- the fbreclimb.py n 48 best.
The FB-RE climbs (fbreclimb.py: n 16 seeded from fts_best16, n 48 seeded from returns_rt48) push throttled fallback leaves to 16 and
74 per run, and the FB-RE count stays 0.

Consequence (READING via Lemma CR; PROVED apart from CR). Take a throttled (θ, w)-stretch S under (h).
- All entries and re-entries of S happen before S's first fallback. The re-entries there follow arena leaves, so each needs a strict
  coarse increase (Theorem XA): at most n(n − 1) of them, by CR.
- After the first fallback, R only shrinks: at most n leaves. Every later non-flat fallback contains a leave (FBL), so there are at
  most n of them.
- Value changes are bounded by PIECE between crossings. After the first fallback the F side runs R17 pieces separated by leaves:
  ≤ n(n − 1).
- Total: crossings(S) + fallbacks(S) + value-changing transitions(S) = O(n³).

## 6. The reduction after box 27 (READING; assumes (h); L-NEW)
N5 on o-cyclic 𝒞^1O makes poly(n) iterations if, per joint λ-phase, both of these are poly(n):
- (a) the number of (θ, w)-stretches, i.e. θ-changes + w-changes;
- (d) the number of transitions at states where (h) fails.
Ingredients:
- PROVED: Lemma Φ (≤ 2n(n − 1) + 1 phases); τ-changes ≤ d − 1; RM, RE, Wo, G (packet P-N5-RE); C, FBL, FBF, XA (this file).
- PIECE (packet §5, a proof sketch there) and CR (written out in §7; referee check pending).
- Unthrottled stretches: Lemma PT + R17.
- Flat steps: R15 (d).
Not covered: states where (h) fails, and the counts in (a), (d). Next targets:
- (CYC') θ-changes and w-changes per phase. L-RED's data plateau at 16 θ-changes.
- (NH) Non-(h) transitions. These include τ(o) closing a cycle at o, the setting of all box-25 W-drop instances.

## 7. Lemma CR written out in full (L-NEW, written ~14:46Z by date -u; this upgrades CR from READING to PROVED-in-writing; a referee should check it)
Setting.
- S is a throttled (θ, w)-stretch with states k_0, k_0 + 1, …. τ, θ, w and the joint λ-map are constant, and (h) holds.
- Ω := W = the valuation of the one-player game G_τ. Ω^c := COARSE(Ω), which equals COARSE(Ξ) by Lemma C.
- Ω's cycle-node map is constant on S. For F-vertices it is Ξ's (Lemma G (a)); for R-vertices it is c, the cycle node of w and of θ.
- For a simple path r = (x = r_0, …, r_L = u) of G_τ to a cycle node u of σ_{k_0}: value(r) := (u, P(r), L), as in R17 §2. Paths may
  pass o; then they continue along τ(o).
Claim (coarse Lemma P). For every j ≥ 0 with k_0 + j in S, every x and every such r with L ≤ j: Ω^c_{k_0+j}(x) ⪰ COARSE(value(r)).
The coarse order compares cycle nodes first, then path sets above u*, ignoring length. (V1) and (V2) hold for it verbatim, with "more
relevant than u*" added to the membership test of ⊕.
Proof, by induction on j. The base j = 0 is R17's. Step: r = x → z → r', and the IH gives Ω^c(z) ⪰ COARSE(value(r')).
- Case A_c: Ω^c(z) ⪯ Ω^c(σ(x)).
  - A1 (x not its own cycle node): COARSE(value(r)) = COARSE(x ⊕ value(r')) ⪯ COARSE(x ⊕ Ω(σ(x))) = Ω^c(x), by coarse (V1)/(V2).
    Then Ω^c is monotone (Lemma C) at every step, arena or fallback.
  - A2 (x its own cycle node): as in R17, using cycle nodes only.
- Case B_c: Ω^c(z) ≻ Ω^c(σ(x)). Coarse-strict implies fine-strict for Ξ and for W alike, so (x, z) is in the gate AND W-improving.
  - At an ARENA step: σ̂ := σ[x → z] is an arena strategy, so (F1) gives Ω_{k+1}(x) ⊵ val_σ̂(x). Run R17's B1/B2 analysis for the fine
    W-improving edge (x, z) in G_τ:
    - every branch where "the phase ends" contradicts the constancy of Ω's cycle nodes on S;
    - the remaining branches give val_σ̂(x) = x ⊕ Ω(z) (B1), or the flat case x = λ(x) (B2, D = ∅, handled as in R17 with cycle
      nodes only).
    Taking COARSE and using the IH with coarse (V2) gives Ω^c_{k+1}(x) ⪰ COARSE(value(r)).
  - At a FALLBACK step (throttled, (h)): by Lemma FBL, (x, z) is a d2 edge with x ∈ R and z ∈ F, and x switches to its honest-best
    gate edge z* ∈ F. The F side is unchanged up to flat cycle-node switches, which keep plays inside their regions, away from x ∈ R.
    So z*'s path avoids x, and Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(z*) = x ⊕ Ξ_k(z*) ⊵ x ⊕ Ξ_k(z). Taking COARSE (Lemma C) and the IH gives the
    claim. □
Lemma CR follows as in R17 Theorem PH.
- At j = n − 1 the claim covers every simple path.
- Ω_t(x) is the value of x's actual play, a simple path to a phase cycle node. So Ω^c_t(x) ⪯ Ω^c_{k_0+n−1}(x) ⪯ Ω^c_t(x) for
  t ≥ k_0 + n − 1, and coarse values are constant from k_0 + n − 1 on. □
With §7, Theorem XA's count (≤ n(n − 1) arena-type re-entries per throttled stretch) and §5's O(n³) per stretch are PROVED-in-writing,
like CR. They depend on: the packet's Lemma G and PIECE (PIECE itself is a sketch in the packet), Lemma W (box 21 §2.5, signed in
R18 (d) context), R15 (a), and R17 §1-§3.

## 8. Whole-phase decomposition (L-NEW, written ~14:49Z by date -u)
Lemma UT (PROVED, combining box 21 Lemma PT, R17 Lemma P / Theorem PH, Lemma G and box 25 §3). Take a maximal run of consecutive
UNTHROTTLED (h)-states (θ = w at each) inside one joint λ-phase with τ fixed. θ = w may change along the run. Then the run has at most
n − 1 value-changing transitions.
Proof.
- At every such state Ξ = W and the gate equals G_τ's improving set (Lemma G with θ = w). So box 21 Lemma PT's hypothesis
  "A(ρ_j) ⊇ H_j" holds at every arena step, and PT does not require θ to be constant.
- Fallbacks at these states are W-flat (box 25 §3, PROVED), so they change no W-value. Count only arena steps in Lemma P's induction.
- W's cycle-node map equals Ξ's, which is constant in the joint phase.
- So R17 Theorem PH gives ≤ n − 1 value-changing transitions. □
Phase decomposition (READING; assumes (h) except where counted; uses §5 for throttled stretches). A joint λ-phase with τ fixed splits
into:
- maximal unthrottled runs: ≤ n − 1 value-changing transitions each (UT);
- throttled (θ, w)-stretches: O(n³) value-changing transitions, crossings and non-flat fallbacks each (§5; PIECE; CR);
- transitions at states where (h) fails;
- flat transitions, at most 4n(n − 1) between value changes (R15 (d)).
There are at most 2·(#θ-changes + #w-changes + #non-(h) transitions) + 1 runs and stretches. Hence
    iterations per phase ≤ poly(n) · (1 + #θ-changes + #w-changes + #non-(h) transitions),
and with Lemma Φ (phases) and τ-changes ≤ d − 1, N5 on o-cyclic 𝒞^1O is polynomial if:
- (CYC') #θ-changes + #w-changes per joint λ-phase is poly(n), and
- (NH) #non-(h) transitions per joint λ-phase is poly(n).
DATA (phaseprofile.py, longest phases):

| instance | n | longest phase | θ-changes | w-changes | (θ, w)-stretches | non-(h) transitions | throttled transitions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 26 | 8 | 0 | 9 | 0 | 24 |
| theta_tp32 | 32 | 41 | 16 | 0 | 17 | 0 | 39 |
| theta_thc24 | 24 | 12 | 11 | 5 | 12 | 0 | 7 |
| returns_rt48 | 48 | 78 | 3 | 0 | 4 | 0 | 67 |
| returns_ph64 | 64 | 103 | 3 | 0 | 4 | 0 | 92 |

- The long phases are a few long throttled stretches with no non-(h) transitions. L-RED's θ-change climbs plateau at 16
  (R58 §11a).
- stretchclimb.py (fitness = (θ, w)-stretches per phase): see §9.

### 8b. θ-changes against a fixed w: the u*-levels (L-NEW, written 14:50Z by date -u)
Lemma UD (PROVED, L-NEW). Inside a joint λ-phase, take consecutive throttled values θ_1 ◁ θ_2 ⊴ w with w fixed and the same cycle node
(h). Let u*_i := the most relevant vertex of P(θ_i) Δ P(w), and v := the most relevant vertex of P(θ_1) Δ P(θ_2), if any. Then:
- v is not more relevant than u*_1;
- if v = u*_1, then u*_2 is strictly less relevant than u*_1 (or θ_2 = w);
- if v is less relevant than u*_1, or P(θ_1) = P(θ_2), then u*_2 = u*_1.
Proof.
- Above u*_1, θ_1 and w agree.
- If v were more relevant than u*_1, then θ_1, θ_2 and w would agree above v. θ_2 beats θ_1 at v, where θ_1 has w's status, so
  θ_2 ▷ w, a contradiction.
- If v = u*_1, θ_2 takes the better status at u*_1, which is w's, and agrees with w at and above u*_1.
- Otherwise θ_2 agrees with θ_1 at and above u*_1. □
Consequences.
- Per value of w there are at most n "u*-levels", and at most n² over the w-values of a phase whose w changes ≤ n times.
- Inside one (w, u*)-RUN (w and u* fixed, θ free to change below u*), Lemmas C, CR and XA hold verbatim. Their proofs use only
  "θ and w agree above u*, and w is better at u*", never θ's constancy. So in a (w, u*)-run:
  - coarse values freeze after n − 1 transitions;
  - arena-type re-entries are at most n(n − 1).
- Lemma FBF does NOT extend across θ-changes. A rising θ re-opens entering edges, which is exactly box 26's THETA re-entries, at most
  n per θ-change.
So (CYC') reduces to:
- OPEN (CYC-u*): the number of θ-changes inside one (w, u*)-run, i.e. changes of θ strictly below u* while w and u* are fixed, plus
  the number of w-changes per phase.
DATA: θ-changes per phase plateau at 16 (L-RED), and returns_rt48 / ph64 have 3.

### 8c. Next idea for (CYC-u*) (READING; not a result)
After the coarse freeze in a (w, u*)-run, let x have its best R-option ρ and its o-free value h with coarse(ρ ⊕ θ) = coarse(h).
Then one of the two frames decides at u* itself:
- If h has w's status at u*: the honest frame prefers F at u*, so x can never ENTER R by the gate. It can only leave (arena or
  fallback).
- If h has θ's status at u*: the W frame prefers R at u*, so x never LEAVES by an arena step. It can enter (honest comparison below
  u*) and can be evicted only by a fallback.
- So below u* every vertex is one-sided, and its type changes only when h's status at u* changes.
A recursion on the next differing level below u* is the natural continuation. Done naively, it gives n^depth, not a polynomial. A
proof needs to show that the type changes, or the recursion depth, are bounded.

## 9. Referee corrections to P-N5-RE, applied here (the pinned packet is not edited; written 15:08Z by date -u)
From REFEREE (docs/referee/R-N5-RE.md) and REFEREE-2 (docs/referee-2/R2-N5-RE.md):
- RE §4 step 2: RE-1. The caveat sentence is false: vertices on z's path between z and y may switch too. Replace step 2 by REFEREE's
  argument (R-N5-RE §4.2):
  - (V1) at L and L+1 (y is its own cycle node at neither state);
  - the gate gives Ξ_L(z) ▷ Ξ_L(σ_L y), and R15 (a) gives Ξ_{L+1}(z) ⊵ Ξ_L(z);
  - one strict (V2) on (Ξ_L(σ_L y), Ξ_{L+1}(z)), whose paths both avoid y by (V1).
  This covers every case. Hypothesis (NC) is NOT needed: G26-1 is CLOSED.
  - General form (SG; both referees): at any N5 transition, a switched Even vertex that is its own cycle node neither before nor after
    gains strictly.
  - REFEREE-2: the (NC) configurations occur (nc_fail_n12.pg, plus 31 more cases) and always with a strict gain. The packet §6's "flat
    leave" cannot occur.
- RE §4 step 3: RE-2. The justifying sentence is false (a play can pass a vertex twice). The conclusion holds by the same argument
  applied along the prefix: (V1) at both states, then strict (V2) (R-N5-RE §4.3).
- Corollary RE: (NC) is dropped. N-RE-3 (REFEREE-2): τ must be constant on each interval (L, E+1].
- PIECE:
  - P-1: the count |R| − 1 needs REFEREE's contraction 𝓡*, with o a self-loop carrying c's priority (R-N5-RE §5.3). R17 verbatim on
    𝓡 gives 2n − 3. REFEREE-2's G-RE-3 closes it differently: re-run Lemma P with the base case at o.
  - P-2 / N-RE-4: the Consequence needs "inside one joint λ-phase". REFEREE-2 also notes that PIECE does not need θ constant.
  §7 above and packet P-N5-XA §7 use PIECE in this corrected form.
- Data note (REFEREE): my random reentry.py samples have 0 re-entries (737 leaves). RE's class data rest on the pinned instances.

## 10. Box-27 climbs (DATA; every best checked: Oink zlk OK, strategies verified)
- Throttled crossings (xingclimb.py, throttled stretches only; 40 min each), FINAL:
  - max crossings of one vertex per throttled stretch: 3 (n 16), 4 (n 24), 3 (n 32);
  - crossing transitions per throttled stretch: 10, 18, 23, and 25 (n 32 seeded from theta_tp32).
  All are below n − 1.
- FB-RE (fbreclimb.py; seeded from fts_best16 / returns_rt48; 30 min), FINAL: 0 re-entries after fallback leaves, with up to 23 / 84
  throttled fallback leaves per run. Lemma FBF predicts the 0.
- (θ, w)-stretches per phase (stretchclimb.py), interim:
  - box25/instances/sc32.pg (n 32, seeded from theta_tp32, sha1 in the commit): 32 θ-changes in one 35-iteration phase, 0 w-changes,
    0 non-(h) transitions. That is twice L-RED's plateau of 16, and linear in n so far. Oink zlk OK, strategies verified.
  - n 24 from random: 17.
  (CYC') is the open count; this is the sharpest instance for L-RED.
- L-SI's elim24_p52 (experiments/si/orlens/instances/elim24_p52.pg, n 24, one Odd choice vertex 18): its 52-iteration phase (2.2n) is 5
  throttled (θ, w)-stretches with 4 θ-changes and 0 non-(h) transitions. The excess lives inside stretches, which §5 / packet §7 bound
  polynomially (O(n³) each).
