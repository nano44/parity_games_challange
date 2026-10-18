# QUIET-BLOCK: the threshold-loop changes of a context are polynomial between grid changes (referee brief)

L-ALG successor 8, box 10, 2026-10-18 (produced on Opus 5.5). Source: docs/alg/GAP-A-M.md §23w (Lemma and data) and §23x
(Lemma EXIT-ORIGIN). Status: READING, UNREFEREED. Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7,
every order datum (frozen §0, L26). "N" = dtl.cpp line N (tools/oink/src/src/solvers/dtl.cpp).

## Setting (as signed in RESULTS R13 draft G-R13-1 / GAP-A-M §23t)
- One phase (G′ and p fixed) and one best_vertices context R. Visits i = 1, 2, ... of R in the phase; T_i = the alive tangles
  at visit i. T_i ⊆ T_{i+1} (packet 11, §23v).
- Grid: rounds r = 1..|R|+1 and grid tops τ = every p-vertex of R. After a res = 1 stop (716 or 765) the last round repeats;
  after a V = ∅ stop (768-771) later rounds are empty.
- top_r^i(w): the top whose round-r region holds w at visit i (⊥ = −1 if none). U_r^i := ∪ of round r's regions (Z after 703).
  W_{r,t}^i := Cl_t(U_r^i; T_i) for every grid round and level t = 0..max_prio (722).
- ENTRY / EXIT of w at (r, τ) between visits x and y = x + 1: top_r^x(w) ≤ τ < top_r^y(w), resp. the reverse.
- A pair x → y is QUIET if it has no entry and no exit. D_R = number of pairs whose set-level computations differ.
  M_R = number of non-quiet pairs. X_R, N_ent = total exits, entries (RESULTS R13 draft).

## Lemma QUIET-BLOCK
If x → y is quiet, then for every grid round r and level t: (i) every round-r region other than that of the lowest grid
top low is equal in x and y, and low's region can only grow; (ii) U_r^x ⊆ U_r^y and W_{r,t}^x ⊆ W_{r,t}^y; (iii) if the
computations of x and y differ, Φ := Σ_r |U_r| + Σ_{r,t} |W_{r,t}| is strictly larger at y.

Proof. By induction on r, with (I_r): V_r^x ⊆ V_r^y. (I_1): V_1 = the p-vertices of R in both (662-667).
1. Regions (690-705). Quiet means top_r^x(w) = top_r^y(w) except ⊥ ↔ low (only those moves are invisible on the grid). So
   every region of a top τ > low is equal, and the prefix before low is equal. If low is processed in x, then low ∈ V_r^x ⊆
   V_r^y and low is not in the common prefix, so low is processed in y. By EXACT (RESULTS R10 (a)) the region is
   Cl_{pr low}(prefix ∪ {low}; T \ E_low), with E_low fixed by the prefix, so T_x ⊆ T_y gives A_x(low) ⊆ A_y(low). If low is
   processed only in y, A_x(low) = ∅. So no vertex moves low → ⊥, which gives (i) and U_r^x ⊆ U_r^y.
2. Threshold loop (722-739). Each level re-pushes all of Z (724), uses Gx = R and consumes nothing, so its output is
   Cl_t(Z_in; T) (DTL-proof Lemma 1.2; packet-11 G11-a1). The level chain gives Cl_t(Cl_{t′}(U_r)) = Cl_t(U_r) for t′ ≤ t. So the
   level-t output is W_{r,t}, and Cl is monotone in its base and in T: W_{r,t}^x ⊆ W_{r,t}^y. A round that returns at 716 has
   no loop; W is then defined by the convention (the G-Ψ convention of R-P4 / R2-P4).
3. Candidates (713-716, 734-739, 745-752). Candidates are scanned in descending index (= priority) order, and the scan at
   level t stops at the first live candidate with priority ≤ t (737). So a top v ∈ V_r is removed iff it is not attracted to
   U_r (714) and not attracted to W_{r,t} for every level t < pr v (738). attracts is monotone in the target set. So a top
   removed in y that is in V_r^x is removed in x, and V_{r+1}^x = V_r^x \ cand_x ⊆ V_r^y \ cand_y = V_{r+1}^y: (I_{r+1}).
4. Strictness. If Φ is equal, then every U_r is equal (by (ii)). With (i) this makes the round maps equal, and every W_{r,t}
   is equal. Then by induction on r, V_r is equal (step 3 with equal sets), every region and threshold output is equal, and so
   are the stop decisions at 716, 765 and 768-771. So the computations are identical. □

## Corollary (closes gap G23u of GAP-A-M §23u)
- Φ ≤ (|R| + 1)(L + 1)|R|, where L = max_prio + 1 ≤ n + 1 is the number of levels.
- Along a maximal run of consecutive quiet pairs, Φ never decreases (steps 1-3 hold at every quiet pair, identical or not)
  and it rises at every differing pair.
- So D_R ≤ M_R + (M_R + 1)(|R| + 1)(L + 1)|R|.
- Every non-quiet pair has an entry or an exit, so M_R ≤ N_ent + X_R ≤ 2X_R + (|R| + 1)|R|² (RESULTS R13 draft (a), step 3).
- With (EXIT_c): X_R ≤ c(|R| + 1)|R|² (REFEREE R-P10 (c)), so D_R is polynomial at every context, the root G′ included.
- Conversely, X_R ≤ D_R·(|R| + 1)|R|². So per context (D-POLY) ⇔ (EXITS-POLY) up to polynomial factors. This is a
  REFORMULATION that makes the (EXIT_c) route and the CHANGE-NEW route (RESULTS R14 draft) meet. It is not a bound on GAP-A.

## Lemma EXIT-ORIGIN (§23x; optional second item)
Step order: rounds ascending; within a round, grid tops descending, then a virtual end-of-round step with prefix U_r.
If x → y has an exit, let (r₁, τ₁) be its first exit step. Then (a) V_{r₁}^x ⊆ V_{r₁}^y, and (b) the pair has a relevant steal
at some step (r₁, τ′) with τ′ > τ₁.
Proof. (a) No exit before (r₁, τ₁) gives U_r^x ⊆ U_r^y for r < r₁ (the virtual step is included). Steps 2-3 above use only
that and T ⊆, so V_{r+1}^x ⊆ V_{r+1}^y. (b) Otherwise the local PREFIX-MONO-X* (GAP-A-M §23g G23g-1, checked by both
referees in packet 9) gives P_x ⊆ P_y at every step of round r₁ up to (r₁, τ₁), so there is no exit there. □
So a "V-loss" exit (a top of V_r^x missing from V_r^y) is always secondary to an earlier exit of the same pair.

## Data (DATA, not part of the claims; tools: experiments/alg/dtl_drthr.py, dtl_exitshape.py)
- Six runs: corpus (141 files) + DE19/DE20 and fall3/fall4 instances; mixed unions UNIONS=900 SEED=1 NMAX=32; cross unions
  UNIONS=600 SEED=11 UM_CROSS=3 NMAX=32 (DR_VIRT=1). Both orders.
- 8,318 quiet differing pairs: W grows strictly at all 8,318, and RV is unchanged at all 8,318.
- 0 invisible-only pairs. Every pair whose first difference is a region step has an entry.
- Max D_R = 41 = the length of one quiet block (spp_chain_up_n43 root; pinned Oink 43 iterations, verified).
- Exits: round 1: 5 (stable), 0 (Oink). Rounds ≥ 2: V-loss 1,406 and steal 982 (stable); V-loss 663 and steal 239 (Oink).

## What is open
- (EXIT_c) (DATA, c = 2) and (CTX⁺). The obstruction is in GAP-A-M §23x: the grid vector rises lexicographically, and
  EXIT-ORIGIN shows that resets are re-triggered by earlier growth, i.e. a counter. (EXIT_c) says DTL is not a counter.
