# Referee packet P-N5-NJB: the per-level fallback count for every block, and the exact form of what remains (box 9, part 2)
L-SI successor 4 (Opus 5.5, D18/L40). Written 2026-10-25 07:43Z (date -u). Lead decision 06:56Z: pin at a natural end, with NJB left as the stated CONJECTURE and RDROP,
PL (c′), MINSET proved. Frozen at its commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/si/N5-C-box9.md §8, §10-§12 (lane write-up). Where they differ, this packet governs.
- Status: L-SI successor 4's proofs, unrefereed. Labels: PROVED (L-SI succ. 4), CONJECTURE, OPEN, DATA.
  - Everything here is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1; every script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements:
  - §1 Lemma RDROP and Theorem PL (c′) (PL (c) for every block), with Corollary PL-S′;
  - §2 Lemma MINSET (NJB in an exact equivalent form);
  - §3 Lemma NO-RF-OLD and its Corollary;
  - §4 Lemma ENT-SHAPE.
- §5 is NOT TO SIGN (CONJECTURE NJB and the obstruction). §6: data.

## 0. Objects and dependencies
- Everything in P-N5-FBW §0 (docs/si/P-N5-FBW-box9.md, pinned trunk e69772b, sha1 88337bd6; signed by both referees, with
  docs/si/P-N5-FBW-fixes-box9.md, sha1 91ff4216): N5, S4a / S4c, Ξ, W, H_k, gates, gate levels, M_k, lev, COARSE_L, (C1)-(C7), b_k(y),
  θ, w, R̄ / R / F, H1-H3, (h), r_k, THR / EQ, scope run S.
- From P-N5-FBW (signed, pending CHECKER): Corollary FBW-S, Theorem CLS2, Lemma FLAT-ALL (with FBW-1), Lemma STRETCH (with
  FBW-2 = N-FBW-1), Theorem PL (a)-(b).
  - BLOCK: the fallbacks f_1 < … < f_N of S at level M ≥ 0 (consecutive among S's fallbacks by CLS2). An INTERVAL is (f_i, f_{i+1}).
  - DIRTY: COARSE_M(Ξ) changes at some vertex at a transition inside the interval. D_M := #dirty intervals.
- Landed RESULTS:
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}.
  - R19 (a) Lemma G (off R̄, Ξ = W; under (h), on R, Ξ = π ⊕ θ, W = π ⊕ w with π the route to o, and π ⊆ R).
  - R21 (a) XW (Ξ ⊴ W).
  - R25 (d) FB step (2), (e) OFF and CAP-1 (σ̄(o) is a full Ξ-minimiser over succ(o) when λ(o) ≠ o).
  - R28 (a) U-loc.
  - R29 (a) Fact R (r non-increasing along a scope run), (b) TRANSFER, (c) OFFGATE, (e) NL, (f) CLS1 and its (A)-chain.
  - R30 (a) Lemma OR, (b) TC-SPLIT. ABSORPTION: σ̄(o) changes from x0 with x0 ∈ F_k ∩ R_{k+1}.
- d_o := |succ(o)|. EXITS: the successors of o. N_x(t) := #exits in R_t. REL_M := #exits leaving R at the fallbacks f_1, …, f_{N−1}.
  REL(S) := #exits leaving R at the fallbacks of S.

## 1. Lemma RDROP and Theorem PL (c′) (PROVED)
**Lemma RDROP.** Let j be the first transition of a dirty interval of a level-M block (M ≥ 0) at which COARSE_M(Ξ) changes. Then r_j > M.
Proof.
- By PL (b) (P-N5-FBW §5), j is an S4a step with lev(θ_j, θ_{j+1}) = O_j > M.
- In S, w_{j+1} = w_j, so θ_j ◁ θ_{j+1} ⊴ w_j (R15 (a), XW).
- (C5) gives lev(θ_j, θ_{j+1}) ≤ lev(θ_j, w_j) = r_j. □
**Theorem PL (c′).** For EVERY level-M block of a scope run (M ≥ 0): D_M ≤ (d_o − 1) + REL_M, hence N ≤ n_E·(d_o + REL_M). No
hypothesis on r is needed.
Proof.
- Let P be the maximal initial part of [f_1, f_N] on which r > M (r is non-increasing, Fact R). By RDROP, every dirty interval has its
  first change in P. By PL (b), that change is an absorption, so distinct dirty intervals give distinct absorptions in P.
- On P, CLS1's (A)-chain holds for L = M on each interval: OFFGATE at f_i + 1, then NL (iii). So NL (ii) holds at every S4a step of P:
  no vertex, in particular no exit, leaves R there.
- Count N_x on P:
  - each absorption raises N_x by 1, since no exit leaves R at the same S4a step;
  - N_x falls only at the block's fallbacks inside P, by at most REL_M in total;
  - under H1 (scope), σ̄(o) ∈ F, so 0 ≤ N_x ≤ d_o − 1.
- Hence #absorptions in P ≤ (d_o − 1) + REL_M, and D_M ≤ (d_o − 1) + REL_M. PL (a) then gives N ≤ n_E(1 + D_M). □
**Corollary PL-S′.** For every scope run S: #fallbacks of S at levels ≥ 0 ≤ n_E·(n·d_o + REL(S)). (The blocks are disjoint and there
are ≤ n levels.) This removes P-N5-FBW's hypothesis "every block has r > M" from Corollary PL-S.

## 2. Lemma MINSET (PROVED)
Let (f_i, f_{i+1}) be an interval of a level-M block with r > M on [f_i + 1, f_{i+1}]. For t in it, put
    Mn_t := {exits x ∈ F_t : COARSE_M(o ⊕ Ξ_t x) = COARSE_M(θ_t)}.
- (a) COARSE_M(θ_t) = min over the exits x ∈ F_t of COARSE_M(o ⊕ Ξ_t x). The minimum is attained at σ̄_t(o), so Mn_t ≠ ∅.
- (b) Inside the interval, Mn loses members only by absorption into R, and its members keep their COARSE_M value.
- (c) COARSE_M(θ) changes at t → t+1 exactly when Mn_{t+1} = ∅. Then every member of Mn_t has been absorbed at t.
- (d) At a fallback of the block, Mn can only gain members.
Proof.
- (a) If λ(o) = o, θ is constant and every claim is trivial. Otherwise:
  - σ̄_t(o) ∈ F_t (H1) is a full Ξ-minimiser (CAP-1), and θ_t = o ⊕ Ξ_t(σ̄_t o) ((P2)).
  - For exits x ∈ F_t, o lies on no play from x, so o ⊕ · preserves ⊴ ((C7)). Hence θ_t is the minimum of o ⊕ Ξ_t(x) over the free
    exits, and (C1) passes this to COARSE_M.
- (b) NL (ii): no leave, so F_{t+1} ⊆ F_t, and a member drops out only by entering R. NL (i): a free exit's COARSE_M value is frozen
  ((C7) through o).
- (c) If Mn_{t+1} ≠ ∅, a member has the same COARSE_M value at t and t+1 (b), and it attains the minimum (a). So COARSE_M(θ) is
  unchanged.
  - If Mn_{t+1} = ∅: every free exit at t+1 was free at t, with a frozen value; none was in Mn_t; so all are strictly above
    COARSE_M(θ_t), and COARSE_M(θ_{t+1}) ≠ COARSE_M(θ_t) by (a).
- (d) FLAT-ALL (ii)-(iii) at f_i: no COARSE_M value moves, and F_{f_i} ⊆ F_{f_i+1} (FLAT-ALL (i)). □
Consequence: on the r > M part of a block, NJB (§5) is equivalent to "Mn is never emptied by absorptions strictly inside the block".
By RDROP, the part where r ≤ M has no dirty interval at all.

## 3. Lemma NO-RF-OLD and Corollary (PROVED)
**Lemma NO-RF-OLD.** Let k0 be a fallback of S with L := M_{k0}, and t* ≤ the next fallback of S, with r_s > L for s ∈ [k0+1, t*]. Let
j ∈ (k0, t*) be an S4a step with COARSE_L(θ_{j+1}) ≠ COARSE_L(θ_j). Then for every t ∈ [j+1, t*], no gate (y, z) at t has
y ∈ R_j ∩ R_t and z ∈ F_t.
Proof.
- (A_s) for L holds on [k0+1, t*] (OFFGATE, NL (iii)), with NL (i)-(ii) at its S4a steps.
- Suppose (y, z) is such a gate. By (A_t) its level is ≤ L, so COARSE_L(Ξ_t z) = COARSE_L(b_t y) =: ζ.
- z ∈ F_s for s ∈ [k0+1, t] (no leave), so COARSE_L(Ξ_s z) = ζ there (NL (i)).
- b_j(y) ⊴ b_t(y). If COARSE_L(b_j y) ◁_L ζ, then (y, z) is a gate of level > L into F_j at j, against (A_j). So COARSE_L(b_j y) = ζ.
- For s ∈ {j, t}: b_s(y) = ρ_s ⊕ θ_s with ρ_s ⊆ R_s (Lemma G (b)), so P(b_s y) = (ρ_s ∩ V_{>c}) ⊔ P(θ_s) (c := c_θ).
  - P(Ξ_s z) ⊆ F_s, because z's H_s-play avoids o and stays in F_s.
  - COARSE_L = (cycle node, P ∩ V_{>L}), so ρ_s has no vertex above max(L, rank c), and P(θ_s) ∩ V_{>L} = P(Ξ_s z) ∩ V_{>L}.
- The right side is the same at s = j and s = t. So COARSE_L(θ_j) = COARSE_L(θ_t). With θ_j ⊴ θ_{j+1} ⊴ θ_t (R15 (a)) this gives
  COARSE_L(θ_{j+1}) = COARSE_L(θ_j), against the choice of j. □
**Corollary.** If t* = k is the next fallback and M_k ≥ 0, then by FBW-S the state k is THR with u* ≠ none. By FBL, every non-flat
switched edge at k is R → F, and by NO-RF-OLD its tail y lies in R_k ∖ R_j: an ENTRANT. If M_k = L, a level-L tail exists
(FB step (2)), and it is an entrant.

## 4. Lemma ENT-SHAPE (PROVED)
Setting as in §3, with M_k = L ≥ 0. Let (y, z) be a level-L gate at k with y ∈ R_k and z ∈ F_k. Let v_L be the vertex of rank L and β
the rank-L bit (good / bad for Even) of P-N5-FBW §4 (2). Then:
- (1) y ∈ R_k ∖ R_j, and COARSE_L(b_t y) = ζ := COARSE_L(Ξ_k z) for all t ∈ [k0, k].
  - Proof: y ∈ R_k ∖ R_j is §3's Corollary.
  - For s ∈ [k0+1, k], z ∈ F_s (no leave) with COARSE_L(Ξ_s z) = ζ (NL (i)), and b_s(y) ⊴ b_k(y). If COARSE_L(b_s y) ◁_L ζ, then
    (y, z) would be a gate of level > L into F_s, against (A_s). So COARSE_L(b_s y) = ζ.
  - At k0: y is not a level-L tail there (see (3), whose proof uses only s ≥ k0 + 1). If y switches at k0, it does so along a gate of
    level < L, whose target keeps its COARSE_L value (FLAT-ALL (iii)). So COARSE_L(b_{k0} y) = COARSE_L(b_{k0+1} y) = ζ.
  - y's route at k has no vertex above max(L, rank c) (the computation of §3 at s = k).
- (2) β(b_t y) is bad for every t ∈ [k0, k].
  - Proof: b is non-decreasing with constant COARSE_L on [k0, k], and b_k(y) is bad because (y, z) has level exactly L. A bad value
    can only follow bad values.
- (3) y is not a level-L tail at k0.
  - Proof: otherwise b_{k0+1}(y) would be good (STRETCH step (3)), against (2).
- (4) β(Ξ_{k0} z) is bad and β(Ξ_k z) is good, while COARSE_L(Ξ z) is constant on [k0, k] (OFF at k0, NL (i) after).
  - Proof: if z were good at k0, then (y, z) would be a level-L gate at k0 (ζ equal, β ordered). y would then be a level-L tail at k0,
    against (3).
- (5) So z's honest value rises at level exactly L at some S4a step in (k0, k) while z stays in F.
  - At that step, U-loc and (A) leave only Even switches of level ≤ L on z's F-play. The rise therefore needs a switch of level
    exactly L on that play. □

## 5. NOT TO SIGN: the conjecture and the obstruction
- CONJECTURE NJB: no COARSE_M change happens strictly inside a level-M block of a scope run. Equivalently, by §2, Mn is never emptied
  by absorptions there.
  - NJB gives D_M = 0, ≤ n_E fallbacks per level, ≤ n·n_E fallbacks of level ≥ 0 per scope run: the second half of R29's (CL-S).
- CONJECTURE ENT (implies NJB, via §3): at a fallback that follows a rise of θ above the previous fallback level L, with r > L in
  between, no R → F gate has an entrant tail.
- The obstruction (where a proof stops). Nothing proved excludes an F → F switch of level exactly L inside an interval. (A) allows
  it, and NL (i) freezes only above L. DATA: such switches are common (1,451 F → F switches at level = L after fallbacks).
- So a violation needs, in one scope run with (h) throughout and w constant:
  - (i) a level-L fallback k0;
  - (ii) the absorption of every member of Mn, which raises θ above L while r > L;
  - (iii) an F-vertex z gaining or losing v_L through an F → F level-L switch;
  - (iv) an entrant y with an edge to z, COARSE_L(b(y)) = COARSE_L(Ξ z), and a bad rank-L bit;
  - (v) a second fallback at level L, with (y, z) a level-L gate.
- Item (ii) followed by ANY later fallback has never been observed.
- OPEN, inherited: level −1 fallbacks per scope run; REL(S).
- Not offered here: the lane's Proposition PL-I (docs/si/N5-C-box9.md §7), which is CONDITIONAL on L-NEW's FREEZE (P-N5-FRZ). PL-I is
  this packet's §1-§4 inside frozen r = ℓ blocks, with "w constant" replaced by "r = ℓ constant".

## 6. Data (DATA, not proof; scripts experiments/si/coarse/, logs experiments/si/coarse/logs/box9/, in this packet's commit)
- Sets:
  - NAMED = experiments/si/coarse/named.txt (53) + instances/*.pg (12) + instances/box9/*.pg (5 climb bests);
  - LIB = experiments/new/box33/lib.txt (234; first column).
  - Runs are asserted equal to n5.py run().
- reltrace.py (blocks; NAMED / LIB): 75 / 169 blocks, 252 / 526 block fallbacks; r-drop blocks 6 / 13; dirty intervals 0; tail repeats
  0; NJ-INT intervals 185 / 377 with 0 θ-changes above L.
- minset.py (§2; NAMED / LIB):
  - 244 / 357 block intervals; |Mn| at the interval start summing to 560 / 1,051; intervals where |Mn| reaches 1: 126 / 149;
  - members absorbed inside intervals: 5 / 5, each while another member remained;
  - Mn emptied (NJB violations) 0; MINSET (c) mismatches 0.
- norf.py (§3; NAMED / LIB / NORF climb bests): rises above L after a fallback 12 / 33 / 2; post-rise states with r > L 3 / 6 / 44;
  0 violations, 0 fallbacks after a rise.
- ffprobe.py (§5): switch kinds and levels after in-scope fallbacks.
- L-NEW's drain/refill instances x48_rt48_final and b6_xw_n56: 8 blocks, up to 12 fallbacks in one; dirty 0, repeats 0.
- Climbs (jclimb.py; each best re-verified with xing/reverify.sh: n5.py, Oink zlk OK, strategies verified):
  - NORF, 2 × 20 min: cl9_norf_a (n 32, sha1 33580f22), cl9_norf_b (n 32, a90ad304). 44 post-rise states, 0 violations, 0 fallbacks
    after a rise.
  - MINSET, 2 × 25 min (seeds 9301-9302, from zcl_fb2_n32 and cl9_rep_a):
    - cl9_mn_a (n 32, sha1 f60b411a, 39 iterations / 15 fallbacks): 56 Mn-member absorptions inside block intervals and 33 intervals
      with |Mn| = 1, yet Mn is never emptied.
    - cl9_mn_b (n 40, dcec4e14, 41 / 35): one block of 34 fallbacks.
    - Both: dirty intervals 0, tail repeats 0 (logs/box9/minset_climb.txt).
