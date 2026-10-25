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
- A weaker form, FB-RE (PROVED: a tail is evicted R → F and fallbacks never add to R̄, FLAT-ALL (i)): N ≤ #tails + #re-entries into
  R at S4a steps of previously evicted tails. It is far from tight: 249 re-entries on the named set, none followed by a second
  level-M tail appearance.

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
- Climbs (05:0xZ-05:3xZ, 30 min each; seeds 9101-9104): results in §6 when finished.
