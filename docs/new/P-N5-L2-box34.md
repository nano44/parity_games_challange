# Referee packet P-N5-L2: how (h)-runs end and restart, the ¬H1 states, and X-RUN without H1 (box 34)
L-NEW successor 14 (Opus 5.5, D15/D18). Written 2026-10-25 07:45Z onward by date -u, at the Lead's request (07:42Z). Frozen at this
commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/new/N5-REL-box34.md §10-§13. Where they differ, this packet governs.
- Status: L-NEW successor 14's proofs, unrefereed. All statements are about the candidate N5 on 𝒞^1O (exactly one Odd vertex o with
  out-degree > 1), inside a phase. Labels: PROVED (L-NEW succ. 14), CONJECTURE, FALSE, DATA, OPEN. Not a running-time bound, not a
  TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Dependence on P-N5-FRZ (docs/new/P-N5-FRZ-box34.md, sha1 39df373c…, with fixes docs/new/P-N5-FRZ-fixes-box34.md, sha1 168de464…).
  At this writing FRZ has REFEREE's signature (referee 3a520ce, Addendum 3171efc: FRZ-1..3 closed) and is under review by REFEREE-2.
  - §1 H3-CONST, §2 H2-STICK, §5 R-CONST, §6 H1-INT: do NOT rest on P-N5-FRZ.
  - §3 Lemma G′: does not rest on P-N5-FRZ.
  - §4 FREEZE′ and §7 X-RUN′: REST ON P-N5-FRZ (§3 and §6 there, with FRZ-1..3).
- Statements to sign: §1-§7. §8 is NOT TO SIGN (refuted conjectures, open conjectures, open list). §9: data.

## 0. Objects and dependencies (landed RESULTS R15-R30, and P-N5-FRZ where marked)
- As in P-N5-FRZ §0:
  - N5, phase (λ_Ξ and τ constant), Ξ, W, G_τ;
  - R_k, R̄_k := R_k ∪ {o}, F_k;
  - θ, w, c_θ := λ(o), c_w;
  - H1 (o on no honest cycle), H2 (o on no W-cycle ⟺ τ(o) ∈ F), H3 (c_w = c_θ), (h) := H1 ∧ H2 ∧ H3;
  - r := lev(θ, w), COARSE_L, (C1)-(C7), VJ00's order (cycle-node reward, then the signed weight Σ ±2^rank of the path set, which is
    injective with weight(∅) = 0, then length);
  - SN prefix of a fallback-free run (R30 (c) SN-PREFIX); H1-toggle: a transition at which H1 changes; DROP: one from H1 to ¬H1.
- U := λ^{-1}(c_θ), a phase constant.
- On 𝒞^1O the honest graph H_k and the (σ_k, τ)-graph differ only at o. So a vertex's honest play and its (σ_k, τ)-play agree up to its
  first visit of o.
- Signed results used:
  - R15 (a): Ξ non-decreasing at every transition.
  - R19 (a) Lemma G: off R̄, Ξ = W (no (h) needed); under (h), Ξ = π_v ⊕ θ and W = π_v ⊕ w on R̄.
  - R21 (a) XW.
  - R23 (g) WM.
  - R30:
    - (c) R-STICK: at an S4a transition of a phase, every v ∈ R_s whose W-cycle node differs from λ(v) stays in R_{s+1};
    - (c) SN-PREFIX;
    - (d) H3H2: H1 ∧ H3 ⇒ H2, and its proof's step "under H1, c_θ ∈ F";
    - (f) H1-DROP: inside a phase, H1 at k and ¬H1 at k+1 force P(θ_k) = ∅.
- VJ00 (V1) and (P2) as used by R17 / R20.

## 1. Lemma H3-CONST (PROVED, L-NEW succ. 14; independent of P-N5-FRZ)
Statement. In a phase, at every state with H2, c_w = λ(τ(o)). Hence:
- H3 holds at all H2 states of the phase or at none;
- if the phase has one (h) state, then at every state of the phase (h) ⟺ H1 ∧ H2.
Proof.
- Under H2, τ(o) ∈ F, and o's W-play is o followed by τ(o)'s W-play, which stays in F (F is closed under the (σ, τ)-plays by its
  definition). On F, W = Ξ (R19 (a)), so τ(o)'s W-cycle node is λ(τ(o)), and c_w = λ(τ(o)).
- τ, λ and c_θ = λ(o) are constant in a phase.
- If some state has (h), then λ(τ(o)) = c_θ, and H3 holds at every H2 state. □

## 2. Lemma H2-STICK (PROVED, L-NEW succ. 14; independent of P-N5-FRZ)
Statement. Let s → s+1 be an S4a transition of a phase with H1 and ¬H2 at s. Then ¬H2 holds at s+1.
Proof.
- ¬H2 at s: τ(o) ∈ R_s, and o lies on its W-cycle, so c_w(s), the top of that cycle, lies in R̄_s.
- τ(o)'s W-cycle node is c_w(s): its (σ_s, τ)-play reaches o and then follows o's.
- λ(τ(o)) = c_θ: its honest play agrees with its (σ_s, τ)-play up to o, then follows o's honest play.
- Under H1, c_θ ∈ F_s (R30 (d), proof of H3H2: o's honest cycle avoids o, and its vertices' plays avoid o).
- So τ(o)'s W-cycle node (in R̄_s) differs from λ(τ(o)) (in F_s). R-STICK (R30 (c)) gives τ(o) ∈ R_{s+1}, i.e. ¬H2 at s+1. □
- Corollary. In a fallback-free run of a phase with H1 at every state, the H2 states form a prefix of the run. If the phase has an
  (h) state, the (h) states of the run form that prefix too (§1).

## 3. Lemma G′ (PROVED, L-NEW succ. 14; independent of P-N5-FRZ): the frames at an H3 state without H1
Statement. Let k be a phase state with H3 and ¬H1, and put c := c_θ = c_w.
- (a) ¬H2 holds, and c ∈ R̄_k.
- (b) Call v ∈ R̄_k c-FIRST if its (σ_k, τ)-play visits c before o (with c ≠ o), and o-FIRST otherwise; o is o-first.
  - A c-first v has Ξ_k(v) = W_k(v).
  - An o-first v has Ξ_k(v) = π_v ⊕ θ_k and W_k(v) = π_v ⊕ w_k. Here π_v is v's route to o, and it is disjoint from P(θ_k), from
    P(w_k) and from c.
- (c) For every vertex v, lev(Ξ_k(v), W_k(v)) ≤ r_k.
Proof.
- (a) ¬H1: o lies on its honest cycle, whose top is λ(o) = c. Every vertex of that cycle reaches o along it (Odd vertices other than o
  are forced), so c ∈ R̄_k. If H2 held, c_w would lie in F_k (o's W-play leaves R̄ through τ(o) ∈ F), against c_w = c ∈ R̄_k.
- (b), c-first: the honest play and the (σ, τ)-play of v agree up to o, so both reach c along the same path before o.
  - In both frames the cycle node is c: λ(v) = c, because the honest play reaches o; and the W-cycle node is c_w = c.
  - So both values are (c, the path's vertices more relevant than c, its length), and they are equal.
- (b), o-first: by (V1) along the route, Ξ_k(v) = π_v ⊕ Ξ_k(o) and W_k(v) = π_v ⊕ W_k(o). The route avoids o's later vertices (it
  stops at its first o), so both prefix sums are VJ00 values.
  - Disjointness: P(θ_k) lies on o's honest path o → σ̄(o) ⇝ c. That path avoids o after its start and passes only forced Odd vertices,
    so it is also the (σ_k, τ)-path of each of its vertices. P(w_k) lies on o → τ(o) ⇝ c, likewise.
  - If π_v met a vertex y ≠ o of either path, then v's (σ_k, τ)-play would continue along y's path and reach c before o, so v would
    be c-first. π_v also avoids c, for the same reason.
- (c) On F_k, Ξ = W (R19 (a)). On c-first vertices, (b). On o-first vertices, (C7) with (b)'s disjointness gives
  lev = lev(θ_k, w_k) = r_k. □
- Remark: if c = o, every v ∈ R̄_k is o-first, θ_k = w_k = (o, ∅, 0), and r_k = ⊥.

## 4. Theorem FREEZE′ (PROVED, L-NEW succ. 14; RESTS ON P-N5-FRZ §3 and fixes FRZ-1, FRZ-2)
Statement. Theorem FREEZE (P-N5-FRZ §3) holds with these two changes:
- (1) in the window, "(h)" is replaced by "H3";
- (2) in the conclusion (b) and in the range of t, "H2" is replaced by "H2 or H3".
Explicitly: suppose the states k0, …, k0 + n − 1 of a phase all have H3 and r ≤ ℓ, and put F := k0 + n − 1. Let t ≥ F be a state of
the phase such that some state t2 ≥ t has H2 or H3. Then COARSE_ℓ(Ξ_t) = COARSE_ℓ(Ξ_F) pointwise. If t itself has H2 or H3, then also
COARSE_ℓ(W_t) = COARSE_ℓ(W_F) = COARSE_ℓ(Ξ_F).
Proof. Go through P-N5-FRZ §3 and check each use of (h) and of H2.
- Step 1 (Lemma C_ℓ) at a window state k. With H1, H3 ⇒ (h) (R30 (d)) and FRZ Step 1 applies. Without H1, Lemma G′ (c) gives
  lev(Ξ_k v, W_k v) ≤ r_k ≤ ℓ for all v, and (C2) gives the equality.
- Fact 0 at H3 states. FRZ Fact 0's two uses are (i) the W-cycle node of every v is λ(v), and (ii) every honest cycle node u has
  W(u) = (u, ∅, 0).
  - (i): on F, W = Ξ. On R̄, the W-cycle node is c_w, and c_w = c_θ = λ(v) by H3 (and λ(v) = c_θ as in G′ (b)).
  - (ii): an honest cycle node u is in F, where W = Ξ; or u ∈ R̄, in which case u = λ(u) = c_θ = c_w, a W-cycle node, so W(u) = (u, ∅, 0).
  This covers FRZ's base case and the cases A2, B1 (α), B2 of P^c_ℓ that use "Fact 0 at k+1".
- Step 2 (monotonicity): WM at S4a steps; at a fallback, Step 1 at both ends and R15 (a). Neither uses (h).
- Lemma P^c_ℓ: the rest of FRZ's proof uses only Steps 1-2, Fact 0, (F1), arena-optimality at a fallback (R20 FBL step 1, a statement
  about any in-phase fallback), and the coarse facts. So it holds on H3 windows.
- Step 3 at t: FRZ uses H2 only to know that x's W-play ends at an honest cycle node. If t has H3, the W-plays that pass o end at
  c_w = c_θ, which is honest (λ(c_θ) = c_θ). Those staying in F end at λ(x). So W_t(x) is again the value of a simple G_τ path to an
  honest cycle node.
- Step 4 (sandwich) uses only R15 (a), XW and Step 1 at F. □
- DATA: none specific. No window of n consecutive H3 states that contains a ¬H1 state occurs in the library (freeze.py MODE=H3 gives the
  same 183 freezes as MODE=(h); data/freezeH3_lib.txt), or in 20,000 random 𝒞^1O games at n 4-9 (no freeze at all).

## 5. Lemma R-CONST (PROVED, L-NEW succ. 14; independent of P-N5-FRZ)
Statement. At every ¬H1 state k of a phase, R̄_k = U (= λ^{-1}(c_θ), a phase constant). Hence no transition between two ¬H1 states of a
phase is a crossing.
Proof.
- (⊆) For v ∈ R̄_k, v's honest play agrees with its (σ_k, τ)-play up to o and then follows o's honest play, so λ(v) = λ(o) = c_θ.
- (⊇) Let λ(v) = c_θ.
  - In the functional graph H_k, each vertex lies on at most one cycle, so the cycle through c_θ is unique. Under ¬H1 it is o's honest
    cycle, since o lies on its own honest cycle and the top of that cycle is λ(o) = c_θ.
  - v's honest play ends on the cycle through its cycle node c_θ, i.e. on o's cycle, so it visits o.
  - Up to that first visit it equals the (σ_k, τ)-play, so v ∈ R̄_k. □

## 6. Lemma H1-INT (PROVED, L-NEW succ. 14; independent of P-N5-FRZ)
Statement. In a phase:
- (a) the states k with P(θ_k) = ∅ form one interval I_∅ of consecutive states;
- (b) every ¬H1 state lies in I_∅, and so does every state k with H1 at k and ¬H1 at k+1;
- (c) on I_∅, θ_k = (c_θ, ∅, ℓ_k) changes only in its length ℓ_k ∈ [0, n − 1], monotonically, at most n − 1 times.
Proof.
- (a) θ is non-decreasing (R15 (a)), and its cycle node c_θ is constant. With equal cycle nodes, VJ00's order compares the signed
  weights of the path sets first. So a < k < b and P(θ_a) = P(θ_b) = ∅ give 0 = weight(∅) ≤ weight P(θ_k) ≤ weight(∅) = 0, and
  weight is injective, so P(θ_k) = ∅.
- (b) At a ¬H1 state, θ is o's value on its own honest cycle: the path from o to the top c_θ along the cycle (or the trivial path, if
  c_θ = o). Every vertex of the cycle other than c_θ is less relevant than c_θ, so P(θ) = ∅. For the state before a drop, use R30 (f)
  H1-DROP.
- (c) On I_∅ the cycle node and the path set are fixed, so the order is the length order (by the parity of c_θ), and θ moves
  monotonically within n values. □

## 7. Theorem X-RUN′ (PROVED, L-NEW succ. 14; RESTS ON P-N5-FRZ §6 with fix FRZ-3)
Statement. Let Q be a fallback-free run of a phase, P its SN prefix, and t_Q the number of H1-toggles at transitions with both ends in P.
- (a) P has at most 13 (d_o + 1) n³ (t_Q + 1) + t_Q crossing transitions with both ends in P.
- (b) REL_Q ≤ d_o (C + 1), where C is the number in (a).
- No hypothesis on H1 is made.
Proof.
- (a) Split P into maximal runs of consecutive H1 states and of ¬H1 states. Both kinds number ≤ t_Q + 1, and the transitions between
  runs are exactly the t_Q toggles.
  - Inside a ¬H1 run there is no crossing (§5).
  - An H1 run P_i consists of consecutive (h) states of a fallback-free run: H1 ∧ H3 ⇒ (h) by R30 (d), and every state of P has H3.
    The proof of X-RUN (P-N5-FRZ §6) uses only that its set is such a run: its windows, RATCHET (c), BLOCK and the level count all live
    inside it. So it gives ≤ 13 (d_o + 1) n³ crossing transitions with both ends in P_i.
- (b) As in FRZ-3. R-STICK (R30 (c)) forbids leaves at S4a transitions from states with c_w ≠ c_θ, so every exit release in Q is at a
  transition with both ends in P, or at the single transition from P's last state, which releases ≤ d_o exits. □

## 8. NOT TO SIGN: refuted conjectures, open conjectures, open list
- FALSE: CONJECTURE ONE-H, "the (h) states of a phase are consecutive".
  - experiments/new/box34/instances/oneh_cex_n32.pg (sha1 51dab08664031c9d34b38de04ba99f255926e14b; n 32, o = 27).
  - n5.py n5 gives 3 iterations, 1 fallback; check_sol2.py gives "zielonka(oink zlk) OK strategies verified"; one Odd choice vertex.
  - The phase is states 1-3: (h) at 1; at 2, ¬H1 ∧ ¬H2 ∧ H3 with c_θ = c_w = 13 and R̄ = everything; the fallback 2 → 3 returns to (h).
  - Also random game 2863 of seed 3461 (n 12): states 0-2, the same pattern through S4a steps.
- FALSE: CONJECTURE ONE-DROP, "at most one transition from H1 to ¬H1 per phase".
  - experiments/new/box34/instances/onedrop_cex_n32.pg (sha1 5793d5a3303fd8c180dd7d0b8105e2d6961af1cd; n 32, o = 27).
  - n5 gives 6 iterations, 1 fallback; check_sol2 OK; one Odd choice vertex. Lead re-run 07:42Z agrees.
  - The phase is states 2-6 with c_θ = 13. The drops are 2 → 3 (S4a) and 5 → 6 (fallback). θ = (13, ∅, 10) at 2-3 and (13, ∅, 8)
    at 4-6.
- CONJECTURE DROP-LEN (OPEN): between two drops of a phase, θ changes.
  - With §6 (c) this would give ≤ n drops and ≤ 2n + 1 H1-toggles per phase.
  - With §7, X_SN per phase would then be ≤ (f + 1)(2n + 2)·13 (d_o + 1) n³ + 2n + 1.
  - Weaker, also OPEN: at most one drop per fallback-free run.
- OPEN list for (L2) (from N5-REL-box34.md §12-§13):
  - (1) DROP-LEN, or its weaker per-run form.
  - (2) A restart of (h) by a fallback at an H1 ∧ ¬H2 state that moves τ(o) out of R. Never seen; impossible at S4a steps (§2).
  - (3) Restarts through ¬H1 ∧ ¬H2 ∧ H3 states. They cost no crossing inside the ¬H1 part (§5), and at most one per drop.
  - (4) (h)-runs shorter than n states never contain a FREEZE window; they cost ≤ n transitions each.
- OPEN, outside (L2): (L1), the re-entries after fallback evictions below r inside frozen r = ℓ blocks. Inside scope runs these equal
  the θ-changes after fallbacks (N5-REL-box34.md §9). Also the fallback count f per phase, and G-N5-TIME.

## 9. Data (DATA, not proof; experiments/new/box34; logs committed in experiments/new/box34/data/)
- LIB = experiments/new/box34/lib.txt (234 files). The "library" below adds experiments/red/*/instances and
  experiments/si/coarse/instances. Every script asserts exactly one Odd vertex with out-degree > 1.
- hruns.py (H3-CONST consequences, (h)-runs per phase): data/hruns_lib.txt.
  - 1,272 phases, at most 1 (h)-run each; 36 interruptions, all ¬H2 (with ¬H3 or ¬H1).
  - --rand 30,000 games at n 5-14 (seed 3461): one phase with 2 (h)-runs (§8).
- h1tog.py (R-CONST, H1-INT (a), (b), H1-DROP, drops and toggles per phase): data/h1tog_lib.txt.
  - Library: 1,274 phases, 1,043 ¬H1 states, 0 failures.
  - --rand 20,000 games at n 4-14 (seed 3481): 40,037 phases, 23,308 ¬H1 states, 0 failures.
- freeze.py MODE=H3 (FREEZE′): data/freezeH3_lib.txt (no ¬H1 windows, §4).
- Climbs:
  - hrclimb.py (ONE-H): found oneh_cex_n32 from u1flat_best_n32.
  - dropclimb.py (ONE-DROP), 40 min each: seed 3502 from oneh_cex_n32 found onedrop_cex_n32. Seeds b4_n5_other_0 (10.9M steps) and
    so_th_n32: at most 1 drop per phase.
