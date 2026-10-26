# Draft RESULTS R61 (Lead, 2026-10-26 06:28Z by date -u; both §Cs and both fixes files filled) (rev. 2026-10-26 07:04Z: C70 E-1, N-1, N-2) — to CHECKER C70

### R61 [refereed-only] N5 on EVERY game, CONDITIONAL on RESULTS R56 and R58: the "routes-through" relation among the Odd choice vertices of an honest class is acyclic (ROUTE-k), a routed terminal's value is a shift of its parent's (SAT-k), so the Q-runs holding a late fallback are polynomially many whenever classes have boundedly many Odd choice vertices (Theorem FB-kT): on 𝒞^kO with k fixed, f = O(n^{k+1}) in-phase fallbacks per phase (Corollary FB-kO); and a clean change of Odd's best response at q strictly raises κ(q) unless tied (Lemma ALT), so epochs are bounded by ρ plus ties, non-clean and cycle-node changes (Corollary N_ep) (2026-10-26) — partial step-4 lemmas for N5 (a fallback count; not an iteration bound on any class; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C70.md, checker PENDING)
- Object (packet P-N5-FBK, added at l-new 9dd499d3, pinned trunk 5d723af6, unchanged during review): docs/new/P-N5-FBK-box44.md, sha1
  afd7c65a265053531171b66294811bbd9a801dd2 (L-NEW successor 23, Opus 5.5). Two correction layers, both on trunk, repairs only, no signed
  statement changes: docs/new/P-N5-FBK-fixes-box44.md (l-new 399e8ec6, sha1 79ad8597b2eb54f56b65718baa89d69b90543a68, written before
  review: verbatim quotes of P-N5-2T's PFZ-q, DIR, A_q and DIRECT, checked verbatim by both referees) and docs/new/P-N5-FBK-fixes2-box44.md
  (l-new 2cf61061, sha1 c6c4569120455a9b578570891a251bff90a30dd6, L-NEW successor 24: FBK-1 = G-FBK-1, N-FBK-1, N-FBK-2, FBK-N1 = N-FBK-4,
  FBK-N2 ⊇ N-FBK-3, data).
  Setting (every game): as in RESULTS R56 and R58 (phases, g_j source states, Q, C, T, U_c, κ, κwt_c, G_c, G_c^q, κopt_c, κopt^q, Q-runs;
  Q_c := (Q ∩ U_c) ∖ {c}, m_c := |Q_c|, w_c := |U_c| − 1, d_q, DIRECT, A_q, q-runs, f^Θ_j; N_late := the Q-runs holding a fallback g_j,
  j ≥ n). For q ∈ Q_c not direct at t, par_t(q) := the first vertex of Q_c ∖ {q} on q's honest play at t. D_c := max_{q ∈ Q_c} d_q + w_c
  (≤ 2n). 𝒞^kO := the games with exactly k Odd choice vertices. An EPOCH: a maximal run of a phase with σ̄|Q constant; N_ep := their number.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, CONDITIONAL on RESULTS R56 and on P-N5-2T's PFZ-q and DIR (now
  landed as RESULTS R58 (b), (d)); no item uses (P); premises LANDED: R15 (a), R54 (e), R56 (a), (b), (d), (f), R58 (a), (b), (d). FB-kT
  step 1 also uses (INJ) (R56 (a)), which the packet's §0 omits (N-FBK-2, accepted by REFEREE), and the "(YB as used there)" of §0 is
  P-N5-2T's (YB_q), i.e. R58 (a), not an R56 fact (N-FBK-1, accepted by REFEREE):
  (a) Lemma ROUTE-k: the relation q → par_t(q) has no cycle; every chain ends at a direct terminal, and the depth of q is ≤ m_c − 1.
  (b) Lemma SAT-k: if t > g_{w_c}, q ∈ Q_c is not direct at t, p := par_t(q), Θ_p is the p-run containing t and t > f^{Θ_p}_{w_c}, then
      κ_t(q) ∈ S_{q,p} + κ_t(p), with S_{q,p} := {κwt_c(q) + κopt^p(y) : y ∈ succ(q) ∩ U_c ∖ T, κopt^p(y) defined} ∪ {κwt_c(q) : p ∈ succ(q)},
      |S_{q,p}| ≤ d_q. The hypothesis t > g_{w_c} is unused (FBK-N1 = N-FBK-4).
  (c) Theorem FB-kT: in every phase, N_late ≤ 1 + Σ_c Σ_{q ∈ Q_c} (V_q − 1), with V_q the number of distinct values of κ(q) at the late
      fallbacks and V_q ≤ Σ_{h=0}^{m_c−1} D_c·((m_c − 1)·D_c)^h ≤ m_c·D_c·((m_c − 1)·D_c)^{m_c−1}; with R56 (f), f ≤ 1 + (n − 1)(1 + N_late).
  (d) Corollary FB-kO, per phase: on 𝒞^kO every phase of every N5 run from every start pair has N_late ≤ 1 + k·(2n)·k·(2(k − 1)n)^{k−1} and
      f ≤ 1 + (n − 1)(1 + N_late) = O(k^{k+1}·2^k·n^{k+1}); for fixed k, f = O(n^{k+1}). The packet's last sentence (whole runs) reads, after
      the joint repair FBK-1 = G-FBK-1 (found independently by both referees): "the in-phase fallbacks of a whole run are O(n^{k+1}(n² +
      n^k)): O(n^{2k+1}) for fixed k ≥ 2, O(n⁴) for k = 1". The per-phase bounds are unaffected.
  (e) Lemma ALT: for an in-phase transition t → t+1 and q ∈ Q_c, q ≠ c, with y1 := σ̄_t(q) ≠ y2 := σ̄_{t+1}(q), call the change CLEAN if q
      lies on no honest cycle at t and at t + 1 and y2's honest play at t avoids q; then a clean change has κ_{t+1}(q) ≥ κ_t(q), with
      equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t). Its "≥" is (M2κ); its content is "strict unless a tie";
      the step at t + 1 is (Aκ), which needs only q ≠ c, so "q on no honest cycle at t + 1" is unused (FBK-N2 ⊇ N-FBK-3, both referees).
  (f) Corollary (N_ep): N_ep ≤ 1 + Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q), where ρ_q counts the transitions of the phase changing Ξ(q), tie_q
      the clean ties at q, nc_q the non-clean changes at q, and cyc_q the changes at q while λ(q) = q.
- Not signed (packet §5): the model obstruction (the lemmas used admit abstract tuple sequences with D^{depth} values per terminal, so no
  SUM bound over terminals follows from them alone; a statement about the lemmas, not about N5); the data; what N5 on 𝒞^kO still needs
  (crossings per phase, transitions per phase given f; READING); the ALT reading that epochs and ρ count the same quantity up to residuals.
- Honest limits: (i) A fallback count per phase, conditional on R56 and R58; no iterations, crossings or S4a steps are bounded, and for k
  not fixed the bound is exponential in k. (ii) Vacuity: FB-kT's late regime (an index ≥ n) is never reached in data; SAT-k's hypothesis is
  met only on constructed unions (REFEREE-2's fb17_k3_P66.pg, a 3-terminal chain class, at depths 1 and 2), re-run on both engines.
  (iii) ALT's residuals are not always small: 33 % non-clean changes on one climbed instance (L-RED rho3_253_n32, R76 §8; DATA).
- Data (DATA, not proof): REFEREE (successor 12, own engine): 14,874 runs (lib41 with 6 random starts, the lib2o list, random 𝒞^3O,
  𝒞^4O, and the four 2T witnesses), 0 failures; ROUTE-k holds with depth up to 15 in its batches (118 in its §C run); ALT 7,354 σ̄(q) changes, no violation; SAT-k 37 checks on REFEREE-2's 2T witnesses
  and 26 on fb17_k3_P66 (equal to REFEREE-2's count), 0 failures, the mutation fails all 37. REFEREE-2 (successor 14, own fbk_check.py; lane
  code not run): ROUTE-k 246,592 checks, depth up to 118 (tcL_N12, 233 terminals in one class), no cycle; ALT reproduces the lane's lib41
  counts exactly (1,910 clean strict, 75 ties, 65 non-clean, 1 at a cycle node), every clean equality a tie; SAT-k 76 checks on the k3
  gadget at depths 1 and 2, 0 violations; mutations satk0 (4) and shift (76 / 76) bite.
- Signatures: REFEREE docs/referee/R-N5-FBK.md (referee c7fa8d5e, successor 12; §C 0e4ba6ee): ROUTE-k, SAT-k, FB-kT, FB-kO per phase, ALT and
  its corollary SIGNED, conditional; GAP FBK-1 (FB-kO's whole-run sentence); notes FBK-N1..N3. REFEREE-2 docs/referee-2/R2-N5-FBK.md
  (referee-2 d4cc40d9, Addendum A 5ad79417 on the pre-review fixes file and §C 9a482c93, all successor 14): all SIGN, conditional;
  minor gap G-FBK-1 (the same sentence); no inherited gap from P-N5-2T; notes N-FBK-1..4. §C (both): verdicts identical; the one gap is
  joint, FBK-1 = G-FBK-1, the two repairs giving the same bound, closed by fixes2 §1; N-FBK-1, N-FBK-2 accepted by REFEREE (missed by it);
  FBK-N1 = N-FBK-4; FBK-N2 ⊇ N-FBK-3; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase fallback count, conditional; no running-time bound). GAPS G-N5-TIME:
  open.
