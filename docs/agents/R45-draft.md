# Draft RESULTS R45 (Lead, 2026-10-25 19:35Z by date -u; lands after R44 = P-N5-PFZ, whose FB-ROUND it uses) — to CHECKER C54

### R45 [refereed-only] N5 on one-Odd-choice games: θ's signed path weight is a Bellman-Ford value (Y-FORM), it freezes on F ∩ U after |U| − 2 fallbacks of a phase (HAT-FREEZE) and then changes P(θ) at most deg(o) times (RHO-TAIL); S4a steps between HN states are Bellman-Ford rounds (BF-F, FREEZE-F), so P(θ)-changes over the HN states of a phase are polynomial in n and N_HN (RHO-HN), and so are HN breaks, crossings, fallbacks and θ-changes (HN-POLY) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C54.md, checker PENDING)
- Object (packet P-N5-RHO, added at l-new 3e9fe5c2, pinned trunk c814455, unchanged during review): docs/new/P-N5-RHO-box40.md, sha1
  cd5df65c2f3e6829f85739a57023fc3da6944baa (L-NEW successors 18 (source) and 19 (packet), Opus 5.5). The referees' notes are collected by
  the lane in docs/new/P-N5-RHO-fixes-box40.md (l-new cf02711c, sha1 cc4e8540ee8aeb4a85e68e1493b2bc71b9824997, L-NEW successor 20:
  RHO-N1, RHO-N2, RHO-N3, N-RHO-1, N-RHO-2); on trunk; repairs only.
  Setting as in RESULTS R39, R42 and R44 (𝒞^1O; phase; HN states and stretches; θ, c_θ; R_k, R̄_k, F_k; g_1 < g_2 < … the in-phase Even
  S4c fallback transitions of the phase). U := λ^{-1}(c_θ), Û := U ∖ {o}; wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0;
  M_t(z) := wt(P(Ξ_t z)) for z ∈ U; G_Û the graph on Û with c_θ a sink, and MoptÛ(z) the maximum of wt(p ∖ {c_θ}) over simple paths p
  of G_Û from z to c_θ; Y_t := succ(o) ∩ U ∩ F_t; deg(o) the out-degree of o; N_HN the number of HN stretches of the phase; ρ_HN (ρ_S)
  the number of transitions of the phase (of S) with both ends HN at which P(θ) changes.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma Y-FORM: at an H1 state t, σ̄_t(o) ∈ Y_t and M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y); at a ¬H1 state, P(θ_t) = ∅.
  (b) Lemma HAT-FREEZE: in a phase, (a) for j ≥ 0, every state t > g_j, z ∈ Û and simple path p in G_Û from z to c_θ with ≤ j edges,
      M_t(z) ≥ wt(p ∖ {c_θ}); (b) for z ∈ F_t ∩ U, MoptÛ(z) is defined and M_t(z) ≤ MoptÛ(z); (c) if |U| ≥ 2, M_t(y) = MoptÛ(y) for every
      state t > g_{|U|−2} and y ∈ F_t ∩ U. No assumption on θ, H1, H2, τ(o) or c_w. (The case o = c_θ occurs for every |U|, and the
      statements hold there as well; RHO-N1, wording.)
  (c) Theorem RHO-TAIL: in a phase with |U| ≥ 2, at most deg(o) transitions t → t+1 with t > g_{|U|−2} change P(θ).
  (d) Lemma BF-F: at an in-phase S4a transition k → k+1 with H1 ∧ ¬H2 at k and k+1, M_{k+1}(v) ≥ wt(v) + M_k(x) for every Even
      v ∈ U ∩ F_{k+1}, v ≠ c_θ, and every successor x ∈ U of v.
  (e) Theorem FREEZE-F: on a run [s, e] of consecutive HN states of one phase with no fallback transition, (a) M_t(z) ≥ wt(p ∖ {c_θ}) for
      z ∈ F_t ∩ U and simple paths p in G[F_t ∩ U] with ≤ t − s edges; (b) M is constant on F ∩ U from s + |U| − 2 on; (c) at most
      max(|U| − 2, 0) + deg(o) − 1 transitions of [s, e] change P(θ).
  (f) Theorem RHO-HN: for one phase with |U| ≥ 2, ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o) (its proof gives the sharper
      (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o); N-RHO-1).
  (g) Corollary HN-POLY, conditional on BRK-POLY′ in the weak form (i′) and on (ii)'s window bound B_S ≤ θ_S + (ρ_S + 1)(|U|² − 1)
      (P-N5-PFZ-ext §3, RESULTS R44): HN breaks, crossings, fallbacks at HN states and θ-changes per phase are ≤ poly(n, N_HN)
      (Σ_S B_S = O(n⁴·N_HN), Σ_S X_S = O(n⁵·N_HN), fallbacks at HN states O(n⁷·N_HN)). For τ(o) = o: N_HN ≤ ⌊T*/2⌋ + 1 by RESULTS R34
      (e), with HN = H1 when τ(o) = o, so these are polynomial in n. (The packet cites RESULTS R39 (f) (c), which is signed for case A
      only; RHO-N2, citation, both referees.)
- Not signed (packet §7): N_HN for τ(o) ≠ o (lane result then, now packet P-N5-NHN, in review); the non-HN states; S4a steps that change
  none of the counted quantities (no iteration bound); W-TIE steps and the block lemmas of docs/new/N5-RW-box39.md.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) HN-POLY is polynomial in n and N_HN; for τ(o) ≠ o, N_HN is not bounded here;
  wakes (K) and the other open pieces of G-N5-TIME remain. (iii) Thin data: HAT-FREEZE (c) and RHO-TAIL after the freeze occur in the
  library only at |U| = 2 (trivial) and in climbs only at |U| = 3 (lane 5 phases; REFEREE 685k phases, 1.16 M HAT-FREEZE (c) checks;
  REFEREE-2 133,889 phases), never at |U| ≥ 4; FREEZE-F (b) is vacuous (no fallback-free HN run longer than |U| − 2 transitions; N-RHO-2).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own engine and probe): library 0 failures, the packet's
  §8 (L) counts reproduced exactly; climbs (877k + 5.95 M candidates) 0 failures, 685k post-freeze phases at |U| = 3, RHO-TAIL 0 changes
  past the freeze. REFEREE-2 (own exact-DFS checker): 1,385 batch logs OK, 1.55 M climb runs, 0 violations; mutation control hatall
  bites (701 violations), frzb0 does not (reported as such). Lane rhodata.py: 990 phases, Y-FORM 6,335, BF-F 28,394, FREEZE-F (c) max
  13 changes (epsseg_cex_n48, bound 62), RHO-HN max 13 (bound 2,931), 0 failures.
- Signatures: REFEREE docs/referee/R-N5-RHO.md (referee 5927831, successor 10; §C 06d6e6d): Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F,
  FREEZE-F, RHO-HN SIGNED; HN-POLY SIGNED conditional as labelled; notes RHO-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-RHO.md
  (referee-2 269ae45, successor 10; §C ab7843a, successor 11): all SIGN; notes N-RHO-1, N-RHO-2; no gap. §C (both): verdicts identical;
  joint gap map empty; RHO-N2 accepted by REFEREE-2 (missed by successor 10), RHO-N1 accepted.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
