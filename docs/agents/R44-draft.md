# Draft RESULTS R44 (Lead, 2026-10-25 19:35Z by date -u) (rev. 20:26Z: C53 E-1 by route (a), E-2, N-1, N-2) — to CHECKER C53 — LANDED in RESULTS Results 20:36Z (CHECKER C53 7f4570b0 + Addendum 1 053a74f0 PASS), after R43

### R44 [refereed-only] N5 on one-Odd-choice games: every in-phase Even fallback is a Bellman-Ford round on U = λ⁻¹(c_θ) (FB-ROUND), so on a θ-run (and on a P-epoch) P(Ξ) freezes on U after |U| − 1 fallbacks (P-FREEZE, P-FREEZE′), later U-rises are length rises and, in case A, not crossings (LEN-TAIL, NO-CROSS-A), θ changes at most |U| − 2 times inside a P-epoch (θ-LEN), and breaks per HN stretch are polynomial in θ-changes (BRK-POLY, via RISE′) and in P(θ)-changes (BRK-POLY′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C53.md, checker PENDING)
- Objects (one review unit; both unchanged during review): packet P-N5-PFZ, docs/new/P-N5-PFZ-box39.md, sha1
  3c617e06f7b9c67d5d9cd865acd134f3a8aed071 (added at l-new c9f9caa1, pinned trunk 283bcb6), and its companion P-N5-PFZ-ext,
  docs/new/P-N5-PFZ-ext-box39.md, sha1 b3702b1ba1849c6aa19cebd2c8fa57e02a318d2a (added at l-new 1b6239fb, pinned trunk c61ecc4) (L-NEW
  successor 18, Opus 5.5). The referees' notes and the repair of gap PFZ-1 are collected by the lane in docs/new/P-N5-PFZ-fixes-box39.md
  (l-new cf20cdc2, sha1 3f55bc882b08d97508d98eda1c3a9f6aeaa0c99c, L-NEW successor 20); on trunk; repairs only.
  Setting as in RESULTS R39 and R42 (𝒞^1O; phase; HN states and stretches; θ, c_θ; R_k, R̄_k, F_k; crossings, entries, evictions;
  breaks B_S; θ_S the θ-changes of S). U := λ⁻¹(c_θ) (constant on a phase); wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0
  (sgn = +1 for even, −1 for odd priority); M_t(z) := wt(P(Ξ_t z)) for z ∈ U. A θ-RUN is a maximal run of states of a phase with θ
  constant, and f_1 < f_2 < … are its in-run Even S4c fallback transitions. A P-EPOCH is a maximal run of states of a phase with P(θ)
  constant; ρ_S is the number of transitions of S at which P(θ) changes. A U-RISE is a strict rise of Ξ at some z ∈ U. The
  TERMINALS are o and c_θ. G_U is the graph on U in which every Even v ∈ U ∖ {c_θ} keeps all its edges into U, every Odd
  v ∈ U ∖ {o, c_θ} keeps its forced edge, and o and c_θ are sinks. For a θ-run Θ, M_Θ(o) := wt(P(θ)) and M_Θ(c_θ) := 0, and
  Mopt_Θ(z) := max{wt(p ∖ {end}) + M_Θ(end) : p a simple path in G_U from z to a terminal}; M_Π and Mopt_Π are the same on a P-epoch Π.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma FB-ROUND: at an in-phase Even S4c fallback k → k+1, M_{k+1}(v) ≥ wt(v) + M_k(x) for every Even v ∈ U ∖ {c_θ} and every
      successor x ∈ U of v (with the facts (A) additivity, (M1′), (M2′) of packet §1).
  (b) Theorem P-FREEZE: on a θ-run Θ, (a) after f_j, M_t(z) is at least the weight of every simple path in G_U from z to a terminal
      with ≤ j edges (plus the terminal's value); (b) M_t(z) ≤ Mopt_Θ(z); (c) for t > f_{|U|−1}, M_t = Mopt_Θ on U and P(Ξ_t z) is
      constant on U.
  (c) Corollary LEN-TAIL: in a θ-run, at most |U|(|U| − 1) transitions after f_{|U|−1} carry a U-rise, each a length rise. Corollary
      NO-CROSS-A (case A): a transition of a θ-run after f_{|U|−1} with H1 at both ends is not a crossing.
  (d) Lemma RISE′ (a re-proof of P-N5-NEB's RISE from landed results): if an in-phase Even fallback is taken at a ∈ S (S an HN stretch),
      k > a, k → k+1 is an entry in S and no transition of [a, k) is an entry, then θ changes at some t → t+1 with a + 1 ≤ t ≤ k, or some
      t → t+1 with a ≤ t < k, θ constant on [a, t+1] and t+1 ∈ S, carries an R̄-rise.
  (e) Theorem BRK-POLY: for every HN stretch S, any τ(o) and any c_w, B_S ≤ θ_S + (θ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ θ_S +
      (θ_S + 1)(n² − 1); in case A, B_S ≤ θ_S + (θ_S + 1)(|U| − 1).
  (f) Theorem P-FREEZE′ (ext §1): P-FREEZE (a)-(c), LEN-TAIL and NO-CROSS-A hold verbatim on P-epochs, with Θ, M_Θ, Mopt_Θ replaced by
      Π, M_Π, Mopt_Π (only M(o) = wt(P(θ)) is used). Lemma θ-LEN (ext §2): a P-epoch has
      at most max(|U| − 2, 0) θ-changes.
  (g) Theorem BRK-POLY′ (ext §3), for every HN stretch S, any τ(o) and any c_w: (i) θ_S ≤ (ρ_S + 1)·max(|U| − 2, 0); (ii) B_S ≤ θ_S +
      (ρ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ (ρ_S + 1)(|U|² + |U| − 3) ≤ (ρ_S + 1)(2n² − 1); (iii) in case A, B_S ≤ θ_S + (ρ_S + 1)(|U| − 1) ≤
      (ρ_S + 1)(2n − 3). The ext's proof of (i) ("apply θ-LEN to each of the ≤ ρ_S + 1 P-epochs") omits the ρ_S transitions at which
      P(θ) itself changes, which are θ-changes too (gap PFZ-1 = G-PFX-1, found independently by both referees); as written it gives
      only (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). (i)-(iii) are signed as stated with REFEREE's repair as the proof of (i)
      (fixes §1): a refined θ-LEN, ≤ |A_low| − [o ∈ A_low] = |U| − 2 − |A_high ∖ {o}| θ-changes per P-epoch, and ρ_S ≥ 1 forces some
      u ∈ A_high ∖ {o} (o's membership in P(θ) is fixed on the phase), so θ_S ≤ (ρ_S + 1)(|U| − 2) − 1 for ρ_S ≥ 1 (for ρ_S = 0, θ-LEN gives θ_S ≤ max(|U| − 2, 0)).
      REFEREE-2 diffed the fixes §1 text against its C.2 (§C addendum C.5, referee-2 ea5cc217): equal in substance in every step
      that carries the argument; two omissions, not mismatches (the case o = c_θ, where θ is constant; U constant on the phase).
- Not signed (packets' "Not to sign"): W-TIE steps (OPEN); the block lemmas of docs/new/N5-RW-box39.md (BF-RW, FREEZE-M, FREEZE-X,
  ROUTE-LEN, W-POT, CW-COUNT; lane, not routed); OPEN: θ_S / θ_ph, ρ per phase (lane packet P-N5-RHO, in review), HN stretches per phase
  for τ(o) ≠ o (lane packet P-N5-NHN, in review), OTHER states, S4a steps between fallbacks (P-FREEZE is not an iteration bound).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) BRK-POLY and BRK-POLY′ bound breaks GIVEN θ_S, resp. ρ_S; the counts of θ- and
  P(θ)-changes per phase and the other open pieces of G-N5-TIME remain. (iii) Thin data: the post-freeze regime (t > f_{|U|−1}) occurs
  in data only for |U| ≤ 2, even under targeted climbs (REFEREE-2: 955,321 θ-runs at |U| = 2, none at |U| ≥ 3; REFEREE: one fallback short
  of the freeze at |U| ≥ 3, never past it); so P-FREEZE (c), LEN-TAIL, NO-CROSS-A and BRK-POLY's j ≥ |U| branch rest on their proofs. The
  repaired (i) never came within 6 of its bound in REFEREE-2's data.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own probe on 278 𝒞^1O games, θ-runs and P-epochs):
  FB-ROUND 80,955 checks, the upper bound and P-FREEZE (a) exact for |U| ≤ 13, BRK-POLY / BRK-POLY′ all checked, 0 failures; a 6.48 M
  mutant climb; the refined θ-LEN count 0 failures over 599 in-epoch θ-changes. REFEREE-2 (own checker): batch 66,655 runs, climbs
  4,653,840 runs, FB-ROUND 6.77 M checks, 0 violations; ext: 1,367 logs and 408k climb runs, 0 violations, (i) as written never exceeded;
  in its PFZ §C, the refined count was reached exactly 6,398 times in 849,280 climb runs and never exceeded. Lane: 714 θ-runs, 857
  P-epochs, 0 failures.
- Signatures: REFEREE docs/referee/R-N5-PFZ.md (referee 8595343, successor 9; main §C 4859e63; ext §C ed8bc20, successor 10):
  FB-ROUND, P-FREEZE (a)-(c), LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY (i), (ii), P-FREEZE′, θ-LEN SIGNED; BRK-POLY′ (ii), (iii) SIGNED given
  (i); (i) SIGNED WITH GAP PFZ-1, repaired in the ext §C; notes PFZ-N1..N3. REFEREE-2 docs/referee-2/R2-N5-PFZ.md (referee-2 37e55fd,
  successor 9, main packet; §X 78896bf, successor 10, ext; §C 212f88e, successor 11): FB-ROUND, P-FREEZE, LEN-TAIL, NO-CROSS-A, RISE′,
  BRK-POLY, P-FREEZE′, θ-LEN SIGN; BRK-POLY′ (i) NOT SIGNED as stated in §X (G-PFX-1), (i′) signed; in §C (C.2) BRK-POLY′ (i)-(iii)
  SIGNED as stated with REFEREE's repair as the proof of (i), subject to its diff of the fixes text; in C.5 (ea5cc217, successor 11)
  the diff is recorded and (i)-(iii) are SIGNED UNCONDITIONALLY as stated, with the fixes §1 repair as the proof of (i); notes N-PFZ-1..3. §C (both): verdicts identical after the repair; joint
  gap map: PFZ-1 = G-PFX-1, closed by the repair (fixes §1; REFEREE-2's condition discharged in C.5).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
