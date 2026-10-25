# N5 box 9: every in-scope fallback obeys CLS1, and the per-level count reduces to absorptions above the level
L-SI successor 4 (Opus 5.5, D18/L40). Lead GO 2026-10-25 04:52Z. Started 04:53Z (date -u).
Labels (L40): PROVED (L-SI succ. 4, unrefereed unless stated), CONJECTURE, OPEN, DATA, READING, FALSE.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- §2 (Lemma FBW) holds on EVERY game. §3-§4 are on 𝒞^1O (exactly one Odd vertex o with out-degree > 1; every script asserts it),
  inside one PHASE.
- Notation as in RESULTS R25 (P-N5-FB §0-§1) and R29 (P-N5-CLS §0): lev, COARSE_L, (C1)-(C7), gates Iσ_k, gate level, M_k, TAME,
  R̄_k / R_k / F_k, (h) = H1 ∧ H2 ∧ H3, θ_k = Ξ_k(o), w_k = W_k(o), r_k = lev(θ_k, w_k), SCOPE RUN, THR / EQ, OFF, FB step (2).
- W_k := V_{σ_k, τ_k}, the play valuation of the (σ_k, τ_k)-play. It uses the engine's convention (experiments/si/si.py l.72-75 and
  l.150ff.): a cycle node c has value (c, ∅, 0), and for a non-cycle-node v, V(v) = v ⊕ V(next v), where
  v ⊕ (c, P, d) = (c, P ∪ {v if rank v > rank c}, d + 1). Ξ_k satisfies the same (P2) on H_k (VJ00 Lemma 5.2, ENG-1 of R25).
- b_k(y) := Ξ_k(σ_k y) for Even y. It is ⊴-non-decreasing in k (R15 (a), (d); R29 box 8 §12).
- BLOCK (§3): for a scope run S and a level M ≥ 0, the fallbacks of S at level M. By Theorem CLS2 below they are consecutive among
  the fallbacks of S. Write them f_1 < … < f_N. An INTERVAL is (f_i, f_{i+1}).

## 1. Tool fix (item 1 of the GO): the level ∞
- experiments/si/coarse/mono.py lev() returned 99 for "cycle nodes differ" (∞), and coarse(v, L) treated L ≥ 99 as ∞. A genuine top
  rank ≥ 99, possible at n ≥ 100, was therefore read as ∞.
- Fix (l-si bf8be06f): mono.INF = 10**6. The same sentinel was replaced in fbcount.py (check (iii)) and xing/carries.py.
  experiments/si/coarse/levcheck.py pins the behaviour (rank-99 level < INF; coarse at 99 ≠ ()); experiments/si/check.sh runs it.
  The old code fails it ("module 'mono' has no attribute 'INF'").
- Re-run: run_all.sh and run_cls.sh now take LOGDIR. All 15 logs in experiments/si/coarse/logs/box9/ are byte-identical to the pinned
  logs in experiments/si/coarse/logs/ (n ≤ 64). The pinned logs, packets and fixes files are untouched.
- No one-Odd-choice game with n ≥ 100 in the repository has an in-scope fallback. On kchain10 / kchain32 (n 123 / 365, L-NEW box 33),
  old and new cls2 / rfinv / clscope outputs are identical. The fix changes no recorded number.

## 2. Lemma FBW (PROVED, every game): fallback gates are bounded by the Ξ/W gap at their ends
Let k be an S4c fallback of N5 at which Even switches (Iσ_k ≠ ∅). For a gate (y, z) at k put u := σ_k(y),
ℓ := lev(Ξ_k u, Ξ_k z) and δ := max(lev(Ξ_k u, W_k u), lev(Ξ_k z, W_k z)). Then:
- (a) ℓ ≤ max(δ, −1);
- (b) if ℓ = −1 > δ, then y is its own W_k-cycle node (and its own Ξ_k-cycle node).

Premise P-OPT (signed). S4a's Even step at k returns a pointwise maximiser of V_{·,τ_k} over the arena A(σ_k). A(σ_k) is the set of
Even strategies that use σ_k(v) or a gate target at each Even v. This is RESULTS R18 (d) Lemma S (c) (from R17 (F1)). The gap
G-1OA-6 says only that the strategy S4c then installs is not that maximiser. At an S4c fallback, S4a returned σ_k: SPEC S4c fires
exactly when S4a and S4b return σ_k and τ_k (n5.py; mono.states). Hence V_{σ',τ_k} ⊴ W_k pointwise for every σ' ∈ A(σ_k).

Proof.
- Step 1 (the gate is W-improving at the same level). Suppose ℓ > δ; then δ < ∞.
  - By (C2), COARSE_δ(Ξ x) = COARSE_δ(W x) for x ∈ {u, z} (for δ = ⊥ the values are equal).
  - Ξ z ▷ Ξ u at level ℓ > δ, so COARSE_δ(Ξ z) ▷_δ COARSE_δ(Ξ u) strictly ((C1), (C2)). Then COARSE_δ(W z) ▷_δ COARSE_δ(W u), so
    W z ▷ W u ((C1), (C3)).
  - For every L′ ≥ δ the COARSE_{L′} values of Ξ and W agree at u and z, so lev(W u, W z) = ℓ.
- Step 2 (one switch strictly improves y). Put σ′ := σ_k[y ↦ z] ∈ A(σ_k), V := W_k, V′ := V_{σ′,τ_k}. Since τ_k is fixed, every play is
  a lasso. Let c be the cycle node of V(y).
  - (a) z's σ_k-play avoids y. It is also z's σ′-play, so V′(z) = V(z), and V′(y) = y ⊕ V(z).
    - If y is a cycle node, V(y) = (y, ∅, 0) and V(u) has cycle node y. V(z) has another cycle node (its play avoids y), so
      rew(c_z) > rew(y) and V′(y) ▷ V(y).
    - Otherwise V(y) = y ⊕ V(u). y lies in neither path set: z's play avoids y; if u's play visits y, then y is on its cycle below c.
      So y ⊕ · preserves the strict order: V′(y) ▷ V(y).
  - (b1) z's play visits y, and y is not on its own cycle. Let q_1 … q_m be z's play before y; none is on y's cycle.
    - V(z) = q_1 ⊕ … ⊕ q_m ⊕ y ⊕ V(u), and V(u) has cycle node c.
    - The new play from y is the cycle C = (y, q_1, …, q_m), so V′(y) = (t, ∅, ·) with t := the top of C.
    - Let D′ := the vertices of C of rank > rank c. Then P(V z) = P(V u) ⊔ D′.
    - If D′ ≠ ∅, W-improvement means D′'s top is even. That top is t, of rank > rank c, so rew(t) = pp(t) > |rew(c)|.
    - If D′ = ∅, the improvement is length-only and c is odd. Then rank t < rank c gives rew(t) > −pp(c) = rew(c).
    - In both cases V′(y) ▷ V(y).
  - (b2) y lies on its own cycle C_y (top c, possibly y = c). Then u ∈ C_y and P(V u) = ∅. z's play p_0 = z, …, p_a = e enters C_y
    at e and reaches y along C_y. P(V z) = {p_i : i < a, rank p_i > rank c}.
    - If P(V z) ≠ ∅, its top is even, and it is the top t of the new cycle C = (y, p_0 … e … along C_y … to y). As in (b1),
      V′(y) ▷ V(y).
    - If P(V z) = ∅ (length-only) and c ∉ C, then c is odd and rank t < rank c. As in (b1), V′(y) ▷ V(y).
    - If P(V z) = ∅, c ∈ C and y ≠ c: V′(y) = (c, ∅, d′) with d′ = 1 + a + dist_{C_y}(e, c), against V(y) = (c, ∅, 1 + dist(u, c)).
      The length comparison that made (y, z) W-improving (V(z) has length a + dist(e, c)) gives V′(y) ▷ V(y), for either parity of c.
    - If P(V z) = ∅ and y = c: V′(y) = (c, ∅, 0) = V(y). This is the only case without a strict improvement. Here y is its own
      cycle node and lev(V u, V z) = −1.
- Step 3. Outside the exception, V′(y) ▷ W_k(y), against P-OPT. So ℓ > δ forces the exception, where ℓ = lev(W u, W z) = −1
  (Step 1) and y is its own W-cycle node. Ξ u = W u there, so y is also its own Ξ-cycle node. □

**Corollary FBW-S (PROVED, 𝒞^1O).** At an in-phase Even S4c fallback k with (h) at k, every gate has level ≤ max(r_k, −1). In
particular M_k ≤ −1 at EQ states (r = ⊥) and at THR states with u* = none (r = −1). At EQ, every gate is a length-only switch at a
cycle node.
- Proof: δ ≤ max_v lev(Ξ_k v, W_k v). Off R̄_k, Ξ = W (R19 (a) Lemma G (a)). On R_k, Ξ = π_v ⊕ θ and W = π_v ⊕ w (Lemma G (b)), and
  (C7) applies as in CLU's proof (P-N5-CLS §1), so the level is r_k. At o the level is r_k. □
- An in-scope fallback is an Even fallback: an Odd fallback changes τ, which leaves the phase.

**Theorem CLS2 (PROVED): the first half of (CL-S) for every in-scope fallback.** Along a scope run S, the fallback levels M_k form a
non-increasing sequence. Moreover M_k ≤ max(r_k, −1) at every fallback of S.
- Proof: the bound is FBW-S. By Fact R (R29) the THR fallbacks with u* ≠ none (r ≥ 0) come first, and CLS1 (R29) orders them.
  Later fallbacks have r ≤ −1, so M = −1 (gate levels are ≥ −1, since gates are strict). −1 is ≤ every earlier level. □
- This closes (H-EQ) and makes (H-KIND) unnecessary (R29 §7 OPEN items 1-2). (H-EQ)'s non-flat R → R̄ and F → F switched edges at
  EQ / u* = none fallbacks have level ≤ −1 because every gate there does.
- DATA (fbw.py; logs/box9/fbw_*.txt).
  - Named set + 12 pinned bests: 272 Even fallbacks, 837 gates; L-NEW's library (box33/lib.txt, 234 files): 694 fallbacks,
    2,384 gates; 1,500 + 4,000 random general games (seeds 901, 902, n 4-20): 141 fallbacks.
  - 0 violations of (a), (b), Step 1 and P-OPT (re-computed arena optimum = σ_k at every fallback).
  - In-scope fallbacks: named 252 THR with u* ≠ none + 4 EQ; library 526 + 8 (the sets overlap); random 5 EQ; 0 THR with
    u* = none anywhere.
  - Each EQ fallback of the named set and the library has exactly one gate, a level −1 cycle-node switch. Probe:
    scratch eqprobe, same scope as rfinv.py.
- Item 2 of the GO (climb for a THR u* = none fallback or an EQ non-flat edge above −1): FBW-S makes the second impossible, and the
  first harmless (its M is ≤ −1). Two 30-min climbs (jclimb.py JMODE=HEQ) test the proof itself; §5.

## 3. The per-level count (PROVED reduction to absorptions above the level)
**Lemma FLAT-ALL (PROVED).** Let k be a fallback of a scope run S with level M := M_k ≥ 0 and (h) at k and k+1. Then:
- (i) F_k ⊆ F_{k+1}, and every v ∈ R̄_{k+1} lies in R̄_k with the same route to o;
- (ii) COARSE_M(θ_{k+1}) = COARSE_M(θ_k);
- (iii) COARSE_M(Ξ_{k+1} v) = COARSE_M(Ξ_k v) for every v;
- (iv) M_{k+1} ≤ M.
Proof.
- r_k ≥ M ≥ 0 by FBW-S, so k is THR with u* ≠ none. FBL (R20 (b)) leaves two kinds of switched edge: R → F, and flat cycle-node
  switches.
- (i) A switched cycle node y′ keeps λ(y′) = y′, so its new play is a cycle through y′. That cycle avoids o: otherwise it would be
  o's W-cycle, against H2 at k+1.
  - So the plays of F_k vertices stay in F (an R-tail now points into F_k).
  - A play reaching o at k+1 meets no switched vertex: an R-tail continues in F; a cycle node continues on its cycle. So it is the
    play at k.
- (ii) If λ(o) = o, θ is constant. Otherwise put x0 := σ̄_k(o) ∈ F_k (H1). θ_k = o ⊕ Ξ_k(x0) by (P2).
  - x0 ∈ F_{k+1} by (i). Its H_{k+1}-play avoids o, so Lemma S (a) (Odd may answer x0 at o) gives θ_{k+1} ⊴ o ⊕ Ξ_{k+1}(x0).
  - R15 (a) gives θ_k ⊴ θ_{k+1}. By OFF (R25), COARSE_M(Ξ_{k+1} x0) = COARSE_M(Ξ_k x0), and (C7) carries this through o ⊕.
  - So COARSE_M(θ_k) = COARSE_M(θ_{k+1}) by (C1) and (C3).
- (iii) Off R̄_{k+1}, use OFF. On R̄_{k+1}, Lemma G (b) at k and k+1 with the same route, (C7) and (ii).
- (iv) TRANSFER (R29 §2) with (iii): a gate at k+1 of level > M would be a gate at k of level > M_k. □

**Lemma STRETCH (PROVED).** Let [s, e] be states of a scope run with COARSE_M(Ξ_t v) independent of t ∈ [s, e] for every v (M ≥ 0).
Then every Even y is a level-M tail (a tail whose max gate level is M = M_k) at most once among the fallbacks k with s ≤ k < k+1 ≤ e.
Proof.
- (1) COARSE_M(b_t(y)) is constant on [s, e].
  - A switch of y at t along a gate of level > M would change COARSE_M(Ξ(y)) at t → t+1 ((P2), (C7)), unless y is a cycle node.
    In-phase cycle-node switches have level −1 (CN, R29).
  - A switch of level ≤ M keeps COARSE_M(b), because its target's COARSE_M is constant.
- (2) Fix y and M. Let v_M be the rank-M vertex. For values with the same COARSE_M, say β = good when v_M's membership in the path
  set favours Even (v_M ∈ P if v_M is even, v_M ∉ P if v_M is odd), else bad. With COARSE_M fixed, ⊴ orders by β first ((C1) at
  M − 1).
- (3) Let y be a level-M tail at k. Then b_k(y) is bad and the best target z (FB step (2)) is good: the gate has level exactly M.
  - b_{k+1}(y) = Ξ_{k+1}(z) ⊵ Ξ_k(z) has the same COARSE_M, so it is good.
  - b is non-decreasing and COARSE_M(b) is constant, so b stays good on [k+1, e].
  - A level-M gate at y needs b bad. So y is not a level-M tail at any later fallback k′ ≤ e − 1. □

**Theorem PL (PROVED).** Let f_1 < … < f_N be the level-M block (M ≥ 0) of a scope run S. Call an interval (f_i, f_{i+1}) DIRTY if
COARSE_M(Ξ) changes at some vertex at a transition inside it.
- (a) N ≤ n_E·(1 + D_M), where D_M := #dirty intervals.
- (b) The first change in a dirty interval is at an S4a step j with O_j > M = max(M, E_j) (an ε-transition), and lev(θ_j, θ_{j+1})
  = O_j > M. Under H1 at j (scope), j is an ABSORPTION: σ̄(o) leaves an exit x0 ∈ F_j that lies in R_{j+1}.
- (c) If r_t > M on [f_1, f_N], then D_M ≤ (d_o − 1) + REL_M, where d_o = |succ(o)| and REL_M := #exits of o that leave R at
  f_1, …, f_{N−1}. Hence N ≤ n_E·(d_o + REL_M).
Proof.
- (a) By FLAT-ALL (iii), fallback transitions of the block (k = f_i with i < N; (h) holds at f_i + 1 because S continues) change
  no COARSE_M. So the block [f_1, f_N] splits into at most 1 + D_M stretches with constant COARSE_M(Ξ), cut only inside dirty
  intervals. Every fallback of the block has a level-M tail (FB step (2)). By STRETCH each Even vertex is such a tail at most once
  per stretch.
- (b) In an interval, M_t ≤ M holds at f_i + 1 (FLAT-ALL (iv)). It persists while COARSE_M(Ξ) is unchanged (TRANSFER). So at the
  first change j, M_j ≤ M, and every relevant Even change has level ≤ M (E_j ≤ M).
  - U-loc (R28 (a)) freezes COARSE_M at every vertex whose H_{j+1}-path to its cycle node meets no relevant change above M. So the
    change needs the σ̄(o) change, with O_j > M ≥ E_j.
  - Lemma OR (c) / TC-SPLIT (P-N5-SN §1-§2, R30 in landing; signed by both referees) give lev(θ_j, θ_{j+1}) = O_j. Lemma OR (a)-(b)
    give the absorption.
- (c) Under r > M, CLS1's proof gives (A) for L = M on each interval (R29), and NL (ii) gives no leave at the S4a steps of an
  interval.
  - By ABS-L (P-N5-SN §8, PROVED; signed), the absorbed exits of an interval are distinct and stay in R until its end.
  - Count N_x := #exits in R. Each absorption raises N_x by 1. N_x falls only at the block's fallbacks (REL_M). Under H1,
    N_x ≤ d_o − 1. Each dirty interval has its own first absorption (b), so D_M ≤ (d_o − 1) + REL_M. □

**Corollary PL-S (PROVED).** In a scope run S whose level blocks all have r > M:
    #fallbacks of S at levels ≥ 0 ≤ n_E·Σ_{M} (d_o + REL_M) ≤ n_E·(n·d_o + REL(S)),
where REL(S) := #exit releases at fallbacks of S. The blocks are disjoint, and there are ≤ n levels.
- Compare R25 Theorem FB: per phase ≤ n_E(2n − 1)(J + 1) + J, multiplicative in J, because levels reset at every jump.
  - Here the levels never reset across a scope run (CLS2). The count is additive, and the only remaining term is releases of exits
    at fallbacks.
  - This is the Lead's REL "from the fallback-level side". Releases at a level-M fallback cost only when the released exit is
    re-absorbed ABOVE M inside the same block.

**Sharper OPEN statement (CONJECTURE NJB).** No COARSE_M change, equivalently no absorption above M, happens strictly inside a level-M
block of a scope run. NJB gives D_M = 0, hence ≤ n_E fallbacks per level: the second half of (CL-S). With CLS2, a scope run then has
at most n·n_E fallbacks of level ≥ 0.
- DATA (reltrace.py; logs/box9/rel_*.txt). Named set + pinned bests: 75 blocks, 252 fallbacks; library: 169 blocks, 526 fallbacks.
  - Changes inside blocks B = 0, gates above M inside blocks 0, θ-changes above M inside blocks 0.
  - Exits released at block fallbacks: 371 / 499. So releases happen, but no released exit is re-absorbed above M within a block.
- Also PROVED and checked (DATA 0 failures):
  - FB-FLAT, the b-form of FLAT-ALL (iii): 252 / 526.
  - ONE-RISE: a level-M tail at f_{i+1} has COARSE_M(b) unchanged since f_i + 1, when r > M on the interval. Proof: by (A) on the
    interval, its target z stays in F and frozen. A rise of COARSE_M(b(y)) would make (y, z) a gate above M into F at f_i + 1.
    Checks: 224 / 495.
  - CONSEC: consecutive fallbacks of a block have disjoint level-M tail sets (STRETCH on a clean interval; ONE-RISE + FB-FLAT
    otherwise). Checks: 177 / 357.
  - In the data no vertex is ever a level-M tail twice in one block (max_rep 1).
- Stronger CONJECTURE NJ-INT: between any two consecutive fallbacks k0 < k of a scope run with r > L := M_{k0} on (k0, k], θ does
  not change above L. NJ-INT implies NJB.
  - DATA: 185 (named) + 377 (library) such intervals, 0 θ-changes above L. This matches REFEREE-2's 583 / 0 for ABS-L
    (P-N5-SN fixes §4): ABS-L is vacuous in all data.
- A weaker form, FB-RE (PROVED: a tail is evicted R → F and fallbacks never add to R̄, FLAT-ALL (i)): N ≤ #tails + #re-entries into
  R at S4a steps of previously evicted tails. It is far from tight: 249 re-entries on the named set, none followed by a second
  level-M tail appearance.

## 3b. Lemma ABS-O (PROVED; an attempt on NJB that turned out vacuous)
Statement. Let j → j+1 be an in-phase transition with H1 at j at which σ̄(o) changes from x0, and x0 ∈ F_j ∩ R_{j+1} (an
absorption). Put c := λ(o), and let g be the max gate level of the Even switches on x0's H_{j+1}-path s_0 = x0, …, s_{m−1}, o.
- (a) Every vertex of A := {s_0, …, s_{m−1}, o} of rank > max(g, rank c) lies in P(Ξ_j x0).
- (b) In particular, rank o ≤ max(g, rank c).
Proof.
- No s_t is an H_j-cycle node. If one were, it would be one at j+1 too (phase), and x0's path would end on its cycle before o,
  whereas Lemma OR (a) puts o on the path before c.
- For an unswitched s_t, (P2) gives Ξ_j(s_t) = s_t ⊕ Ξ_j(s_{t+1}) exactly (Odd vertices other than o are forced).
- For a switched s_t, (P2) gives Ξ_j(s_t) = s_t ⊕ Ξ_j(σ_j s_t), and lev(Ξ_j σ_j s_t, Ξ_j s_{t+1}) ≤ g.
- COARSE_g(s ⊕ a) is a function of COARSE_g(a) (formal ⊕: union, length + 1). At o, Ξ_j(o) = o ⊕ Ξ_j(x0) (P2).
- Composing around the closed walk x0 → … → o → x0 gives COARSE_g(Ξ_j x0) = COARSE_g(A ⊕ Ξ_j x0), with ⊕ as formal union. That is (a).
- Under H1, x0's H_j-play is the tail of o's honest play, so o ∉ P(Ξ_j x0). That is (b). □
- DATA (abso.py; logs/box9/abso_*.txt): 462 + 715 absorptions; for the 172 + 298 with rank o > rank c, g ≥ rank o every time.
- Why it does not help NJB. When rank o > rank c, every gate R → F has level ≥ rank o: Ξ(σ y) = π ⊕ θ contains o, and an F-value
  does not. So every evicting fallback, and hence every block, has M ≥ rank o.
  - ABS-O would exclude absorptions inside a block only when rank o > M; that case never arises (abso.py: 0 of 778 in-scope
    fallbacks have rank o > max(M, rank c)).
  - So ABS-O is a true but vacuous route to NJB. I record it as a dead end for that purpose.
  - Obstruction: the cycle closed by an absorption contains o, but o sits below every evicting level.

## 4. What remains (labels)
- PROVED this box (L-SI succ. 4, unrefereed):
  - Lemma FBW (every game), Corollary FBW-S, Theorem CLS2 (all in-scope fallbacks; (H-EQ) closed).
  - Lemma FLAT-ALL, Lemma STRETCH, Theorem PL (a)-(c), Corollary PL-S, ONE-RISE, CONSEC, FB-RE.
- CONJECTURE NJB (above). The open quantity is the absorptions above M inside a level-M block. Each needs an exit released at an
  earlier fallback of the block (PL (c)). It is the fallback-side form of L-NEW's REL.
- OPEN: blocks where r drops to M (6 of 75 / 13 of 169 blocks). There NL and ABS-L do not apply; PL (a)-(b) still hold. DATA:
  B = 0 there too.
- OPEN, inherited: level −1 fallbacks per scope run (STRETCH's β-argument becomes a length argument, ≤ n per value). REL(S) itself.
  Θ per scope run.

## 5. Data, scripts, climbs
- Scripts (all assert one Odd choice vertex where 𝒞^1O is needed; runs asserted equal to n5.py run()):
  - experiments/si/coarse/fbw.py (§2);
  - reltrace.py (§3: FB-FLAT, ONE-RISE, CONSEC, PL, FB-RE, EV-FRZ, block statistics);
  - levcheck.py (§1);
  - jclimb.py modes HEQ (FBW violations, then in-scope u* = none / EQ fallbacks, then fallbacks) and REP (reltrace violations, then
    tail repeats + θ-changes above M inside blocks, then block fallbacks).
- Logs: experiments/si/coarse/logs/box9/ (fbw_named, fbw_lib, fbw_rand902, rel_named, rel_lib, and the 15 re-run logs of §1).
- Climbs (05:11Z-05:41Z, 30 min each; seeds 9101-9104): 0 violations; HEQ reached 1 in-scope EQ fallback, 0 with u* = none; REP 0
  repeats and 0 θ-changes above M in blocks.
  - Bests: instances/box9/cl9_heq_b (n 32, 7535a99c), cl9_rep_a (n 40, 9d31fb39), cl9_rep_b (n 48, 8efbbc9e; a 37-fallback block).
  - All re-verified (Oink zlk OK).
- Packet: docs/si/P-N5-FBW-box9.md (Lead 05:28Z).

## 7. Bridge to L-NEW box 34 (L1): the per-level count inside a frozen r = ℓ block (Lead relay 05:40Z)
Setting: docs/new/N5-REL-box34.md §3-§6 (L-NEW succ. 14; lane PROVED, unrefereed; read, not edited). Let I be a maximal run of
consecutive (h) states of a phase with r = ℓ ≥ 0, after a FREEZE window at ℓ. So COARSE_ℓ(Ξ) is constant on I (FREEZE (a)). w may
change inside I. Fallbacks are allowed.

**Proposition PL-I (PROVED, L-SI succ. 4; CONDITIONAL on L-NEW's Theorem FREEZE, packet P-N5-FRZ pinned 25fda0f, under review).**
- (i) The fallback levels inside I are non-increasing and ≤ ℓ.
- (ii) I has at most n_E fallbacks at level ℓ.
- (iii) For M < ℓ, the level-M fallbacks of I satisfy N_M ≤ n_E(1 + D_M), with D_M ≤ (d_o − 1) + REL_M (Theorem PL, with I in place
  of the scope run).
- Hence I has at most n_E(1 + ℓ·d_o + REL(I)) fallbacks, and so at most n times that many fallback evictions and (L1) re-entries.
Proof: the scope-run hypothesis "w constant" is used in §2-§3 only through Fact R (r non-increasing). On I, r = ℓ is constant, so
Fact R is trivial there. Each remaining ingredient uses only (h) at both ends of each transition, inside a phase:
- CLS1's induction: FBL + CLU in the case r ≤ L; the OFFGATE / NL (iii) chain in the case r > L.
- FBW-S, FLAT-ALL, STRETCH, PL (b).
- ABS-L's proof (P-N5-SN §8): it uses (A_j), NL (i)-(ii), CAP-1 and (h).
All hold on I.
- (i) follows from CLS1's induction and FBW-S (M ≤ r = ℓ).
- (ii) FREEZE makes COARSE_ℓ(Ξ) constant on all of I, so STRETCH applies to I as one stretch.
- (iii) is PL (a)-(c) with r = ℓ > M. □
- Consequence: NJB (on I) gives D_M = 0. Then I has ≤ n_E(ℓ + 1) fallbacks and ≤ n·n_E(ℓ + 1) evictions, so (L1) is polynomial per
  frozen block.
  - So L-NEW's (L1) and my NJB are the same open piece, seen from the run side and from the fallback-level side.
  - The residue is: absorptions at levels in (M, ℓ] inside a level-M sub-block of I.
- DATA (frzblk.py; logs/box9/frz_*.txt; own engine path, n5.run asserted). Frozen r = ℓ blocks containing fallbacks:
  - NAMED + pinned bests + box 9 climbs: 9 blocks, 38 fallbacks, 71 evictions, 20 (L1) re-entries (max 15 in one block).
  - box34/lib.txt: 20 blocks, 112 fallbacks, 203 evictions, 42 (L1) re-entries.
  - D_M = 0 in all 10 + 25 level sub-blocks. 0 failures of (i), (ii), (iii).
- So in the data, (L1) re-entries occur (42), but the fallbacks that produce them are already bounded by n_E per level. NJB holds in
  every frozen block seen.

## 8. NJB attempt (Lead GO 05:53Z): after a rise above L, old R-vertices have no gate into F
Data first (scratch probes, then norf.py).
- After an in-scope fallback, 54 θ-changes above L := the last fallback level occur in NAMED + LIB. All are absorptions.
- All 54 lie after the LAST fallback of their scope run: no fallback follows any of them.
- In the 110 later in-scope states there is no R → F gate at all, although every one of those states has gates. r drops to ≤ L at
  101 of them.
So the mechanism that would violate NJ-INT / NJB (a rise above L, then another evicting fallback) never starts.

**Lemma NO-RF-OLD (PROVED, L-SI succ. 4).** Let S be a scope run, k0 a fallback of S with L := M_{k0}, and t* ≤ the next fallback of
S, with r_s > L for s ∈ [k0+1, t*]. Let j ∈ (k0, t*) be an S4a step with COARSE_L(θ_{j+1}) ≠ COARSE_L(θ_j). Then for every
t ∈ [j+1, t*], no gate (y, z) at t has y ∈ R_j ∩ R_t and z ∈ F_t.
Proof.
- (A_s) for L holds on [k0+1, t*] (OFFGATE at k0 + 1, then NL (iii); R29 (c), (e)), and NL (i)-(ii) hold at its S4a steps.
- Suppose (y, z) is such a gate. By (A_t) its level is ≤ L, so COARSE_L(Ξ_t z) = COARSE_L(b_t y) =: ζ.
- z ∈ F_s for all s ∈ [k0+1, t]: a vertex of R_s would have to leave R before t, and there is no leave (NL (ii)). So COARSE_L(Ξ_s z) =
  ζ on [k0+1, t] (NL (i)).
- b_j(y) ⊴ b_t(y). If COARSE_L(b_j y) ◁_L ζ = COARSE_L(Ξ_j z), then (y, z) is a gate at j of level > L into F_j, against (A_j). So
  COARSE_L(b_j y) = ζ ((C1), (C3)).
- For s ∈ {j, t}, y ∈ R_s, so b_s(y) = ρ_s ⊕ θ_s with ρ_s ⊆ R_s, the route of σ_s(y) (Lemma G (b)). Hence P(b_s y) = (ρ_s ∩ V_{>c}) ⊔
  P(θ_s), with c = c_θ.
- z's H_s-play avoids o and stays in F_s, so P(Ξ_s z) ⊆ F_s.
- COARSE_L = (cycle node, P ∩ V_{>L}), and COARSE_L(b_s y) = ζ = COARSE_L(Ξ_s z). So ρ_s has no vertex above max(L, rank c), and
  P(θ_s) ∩ V_{>L} = P(Ξ_s z) ∩ V_{>L}, for s = j and s = t.
- The right side is the same at j and t, so COARSE_L(θ_j) = COARSE_L(θ_t). With θ_j ⊴ θ_{j+1} ⊴ θ_t (R15 (a)) this gives
  COARSE_L(θ_{j+1}) = COARSE_L(θ_j), against the choice of j. □
**Corollary (PROVED).** In that setting, let the next fallback k = t* of S have level M_k ≥ 0. Then every non-flat switched edge at
k is an R → F edge (FBL; FBW-S gives r_k ≥ M_k ≥ 0). Its tail entered R after j: y ∈ R_k ∖ R_j.
- So NJ-INT, and hence NJB, reduce to one statement. CONJECTURE ENT: at such a fallback, no R → F gate has a tail that entered R
  after a θ-change above L in (k0, k).
- What an entrant tail must satisfy (PROVED by the same computation, with Z := P(Ξ_t z) ∩ V_{>L}): COARSE_L(b(y)) is constant from
  j to t, across y's entry into R. From its entry step e onward, COARSE_L(θ) already equals (c, Z). So the entrant arrives only after
  θ has finished rising above L, and its route carries no vertex above L.
- DATA (norf.py; logs/box9/norf_*.txt): NAMED + pinned + climbs 12 rises, LIB 33 rises. States checked after a rise with r > L:
  3 + 6. 0 violations of NO-RF-OLD or ENT, and 0 fallbacks after a rise. This data is THIN; r usually drops to ≤ L right after the rise.
- Climbs: jclimb.py JMODE=NORF, 2 × 20 min (seeds 9201-9202, from x31_rx32 and jcl_lev_l_sc). Results in §9.

## 9. NORF climbs (DATA; 06:01Z-06:21Z, 20 min each, seeds 9201-9202)
- Fitness: (NO-RF-OLD / ENT violations + fallbacks after a rise, post-rise states checked with r > L, rises).
- Final: (0, 21, 1) from x31_rx32 and (0, 23, 1) from jcl_lev_l_sc. Every climb step kept 0 violations and 0 fallbacks after a rise.
- Bests pinned in experiments/si/coarse/instances/box9/. Both re-verified with xing/reverify.sh (Oink zlk OK, strategies verified):
  - cl9_norf_a (n 32, sha1 33580f22, 35 iterations / 2 fallbacks);
  - cl9_norf_b (n 32, a90ad304, 32 / 2).
- Together: 44 post-rise states with r > L, 0 R → F gates (logs/box9/norf_climb.txt).
- Reading: the climbs keep r > L for many states after a rise, but they do not produce a second fallback. Every R → F gate stays
  absent, including entrant tails. ENT remains a CONJECTURE: 53 states checked in total, 0 failures.

## 10. NJB on L-NEW's drain/refill instances, and the exact reformulation (Lead relays 05:58Z, 06:04Z)
- DATA: x48_rt48_final (experiments/new/box28/instances) and b6_xw_n56 (experiments/n5-exhaustive/instances):
  - 8 level blocks, 30 fallbacks, up to 12 in one block;
  - B = 0 (no COARSE_M change inside a block), 0 tail repeats, FBW 30 fallbacks / 93 gates with 0 failures, 2 rises above L after a
    fallback and no fallback after either.
  - L-NEW's repeated same-level clusters (its §8, up to 9 at one level) lie inside one of my blocks. Its "θ rises at exactly level M"
    between drains is a COARSE_{M−1} change, which STRETCH allows. NJB survives there.
**Lemma MINSET (PROVED, L-SI succ. 4).** Let S be a scope run, (f_i, f_{i+1}) an interval of a level-M block with r > M on it, and
Mn_t := {exits x ∈ F_t : COARSE_M(o ⊕ Ξ_t x) = COARSE_M(θ_t)}.
- (a) COARSE_M(θ_t) = min over the exits x ∈ F_t of COARSE_M(o ⊕ Ξ_t x), and Mn_t ≠ ∅.
- (b) Inside the interval, Mn only loses members, and only by absorption into R. Its members keep their COARSE_M value (NL (i)).
- (c) COARSE_M(θ) changes inside the interval exactly when Mn becomes empty. At that step the last members are absorbed, which is
  the absorption of PL (b).
- (d) At a fallback f_i of the block, Mn can only gain members: by FLAT-ALL (ii)-(iii), no COARSE_M value moves, and F only grows.
Proof.
- (a): CAP-1 (σ̄(o) is a full Ξ-minimiser over succ(o)), H1 (σ̄(o) ∈ F) and (P2) at o. An exit in R has o on its play, and its value
  is ⊵ θ anyway.
- (b): NL (ii) (no leave, so F only shrinks, by entries) and NL (i) (values off R̄ frozen above M).
- (c): an exit of Mn left in F keeps the minimum at COARSE_M(θ). Conversely, if Mn empties, the minimum over F-exits is strictly
  above.
- (d): as stated. □
- So NJB ⇔ "inside a level-M block, Mn is never emptied by absorptions". |Mn| ≤ d_o, and Mn regains members only from releases at
  the block's fallbacks.
  - This is the fallback-level form of L-NEW's REL: an emptying needs every COARSE_M-minimal free exit to be absorbed between two
    level-M drains.
  - With ABS-O (a), each such absorption closes a cycle through o whose vertices above max(M, rank c) lie in P(Ξ x0).
- Status: NJB stays a CONJECTURE.
  - PROVED reductions: PL (to absorptions), MINSET (to emptying Mn), NO-RF-OLD (after an emptying, only entrant tails can be evicted).
  - Nothing here rests on FREEZE. §7's PL-I does rest on it, and is CONDITIONAL on P-N5-FRZ (pinned 25fda0f).

## 11. The r-drop blocks (Lead item 2): PL (c) holds for every block
**Lemma RDROP (PROVED, L-SI succ. 4).** In a level-M block (M ≥ 0) of a scope run S, let j be the first transition of a dirty
interval at which COARSE_M(Ξ) changes. Then r_j > M. So every interval whose states all have r ≤ M is clean.
Proof. By PL (b), lev(θ_j, θ_{j+1}) = O_j > M. In S, w_{j+1} = w_j, so θ_j ◁ θ_{j+1} ⊴ w_j (R15 (a), XW). (C5) then gives
lev(θ_j, θ_{j+1}) ≤ lev(θ_j, w_j) = r_j. □
**Theorem PL (c′) (PROVED).** For EVERY level-M block of a scope run (M ≥ 0), D_M ≤ (d_o − 1) + REL_M, hence N_M ≤ n_E·(d_o + REL_M).
The hypothesis "r > M on the block" is not needed.
Proof.
- Fact R makes r non-increasing on S. Let P be the maximal prefix of [f_1, f_N] on which r > M.
- By RDROP, every dirty interval has its first break inside P. Each such break is an absorption (PL (b)), and distinct dirty
  intervals give distinct absorptions.
- On P, CLS1's (A)-chain and NL (ii) hold, so no exit leaves R at an S4a step of P.
- N_x (the number of exits in R) rises by 1 at each absorption. It falls only at the block's fallbacks inside P, by at most REL_M in
  total. Under H1 (scope), N_x ≤ d_o − 1.
- Hence the absorptions in P number ≤ (d_o − 1) + REL_M. This needs neither ABS-L nor r > M after P. □
- Consequence: Corollary PL-S holds for every scope run: #fallbacks at levels ≥ 0 ≤ n_E·(n·d_o + REL(S)). The OPEN item
  "r-drop blocks" (§4, P-N5-FBW §6) is CLOSED. Not in the frozen packet; for a fixes file if the referees want it.
- DATA consistency: 6 / 13 / 1 r-drop blocks (NAMED / LIB / climbs), all with B = 0 (§3, §5).

## 12. ENT, time-boxed attempt (Lead 06:34Z): outcome (b), the exact obstruction and the shape of a violation
Setting. S is a scope run, k0 a fallback of S with L := M_{k0} ≥ 0, and j ∈ (k0, k) the S4a step where θ first changes above L
(Mn empties, §10). k is the next fallback of S, and r > L on [k0+1, k]. v_L is the vertex of rank L, and β is the rank-L bit of §4
(good / bad for Even).
- By CLS1 (R29 (f)), M_k ≤ L always. The Lead's suggested angle (switched levels at k are ≤ L = M_{k0}) therefore holds, but it does
  not by itself help the per-level count. A violation of NJB needs the next fallback k to have level EXACTLY L.
- If M_k < L, the block of level L ends at k0 and the rise is not inside it. Per-level count PL then charges the interval to no block
  of level L.
**Lemma ENT-SHAPE (PROVED, L-SI succ. 4).** Suppose M_k = L. Let (y, z) be a level-L gate at k with y ∈ R_k and z ∈ F_k (it exists by
FBL and R25 FB step (2)). Then:
- (1) y entered R after j (NO-RF-OLD), with COARSE_L(b(y)) = (c, Z) constant on [k0+1, k] and no vertex above L on its route (§8).
- (2) β(b_t y) is bad for all t ∈ [k0, k]. Reason: b is non-decreasing with constant COARSE_L (FLAT-ALL (iii) across k0), and b_k(y)
  is bad because (y, z) has level exactly L.
- (3) y is not a level-L tail at k0. Otherwise b_{k0+1}(y) would be good (STRETCH step (3)), against (2).
- (4) β(Ξ_{k0} z) is bad, and β(Ξ_k z) is good. Reason: COARSE_L(Ξ z) is frozen on [k0, k] (OFF at k0, NL (i) after). If z had been
  good at k0, (y, z) would have been a level-L gate at k0, making y a level-L tail at k0, against (3). So z's honest value rises at
  level EXACTLY L at some S4a step in (k0, k), while z stays in F.
- (5) That rise of an F-vertex at level L needs a switch of level exactly L on z's F-play at that step. The gate is into F, of
  level ≤ L by (A), and U-loc bounds every other change by L.
Proof: each item is shown inline above from the cited lemmas. □
- The step that fails. Nothing proved so far forbids an F → F switch of level exactly L inside the interval. (A) allows level L into
  F, and NL (i) freezes only above L. So the chain "Mn empties (rise above L) → an entrant y with a frozen-bad rank-L bit → its F-target
  z gains rank L → next fallback at level L" is not excluded.
- What a counterexample must contain (for L-RED; all inside one scope run, in-phase, (h) throughout, w constant):
  - (i) a level-L fallback k0;
  - (ii) the full absorption of Mn (every COARSE_L-minimal free exit absorbed at S4a steps), raising θ above L while r stays > L;
  - (iii) after that, an F-vertex z whose play gains (or loses) v_L at an S4a step through an F → F switch of level L;
  - (iv) a vertex y that enters R after (ii) with an edge to z, whose successor value has the same COARSE_L as z's and the bad rank-L
    bit;
  - (v) a second fallback at level L, with (y, z) a level-L gate.
  - DATA: no instance has even (ii) followed by any fallback (§8-§9: 54 + 44 post-rise states, 0 R → F gates).
- Next (per the Lead's instruction): the r-drop blocks, already CLOSED in §11. So the per-level count has exactly one open piece, the
  chain above.
- DATA for step (iii) (ffprobe.py; logs/box9/ffprobe.txt; NAMED + pinned + climbs + LIB): Even switches at S4a steps after an in-scope
  fallback, by kind and by level relative to L.
  - F → F: 1,451 at level = L, 1,968 below.
  - F → R̄: 337 at = L, 2,026 below, 73 above.
  - R → R̄: 1 at = L, 273 below, 14 above.
  - R → F: 2 at = L, 15 below.
  - So (iii) is common, and the obstruction is not (iii). The only ingredient never observed is (ii) followed by any later fallback
    in the same scope run. L-RED's target is a scope run that empties Mn and still reaches another level-L drain.

## 13. MINSET data and climbs; packet P-N5-NJB (Lead 06:56Z)
- minset.py (NAMED / LIB):
  - 244 / 357 block intervals; |Mn| reaches 1 in 126 / 149 of them;
  - members absorbed inside intervals: 5 / 5, always with another member left;
  - Mn emptied 0 times.
- MINSET climbs (cl9_mn_a, cl9_mn_b; P-N5-NJB §6): up to 56 member absorptions inside block intervals, and Mn still never emptied.
  The sole minimiser σ̄(o) is never absorbed inside a block.
- Packet: docs/si/P-N5-NJB-box9.md. Contents: RDROP, PL (c′), PL-S′, MINSET, NO-RF-OLD, ENT-SHAPE; NJB and ENT as CONJECTURES with the
  obstruction.
