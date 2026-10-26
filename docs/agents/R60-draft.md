# Draft RESULTS R60 (Lead, 2026-10-26 06:20Z by date -u; both §Cs and the fixes file filled) — to CHECKER C69

### R60 [refereed-only] N5 on EVERY game: inside a phase, every switching transition of a non-cycle-node Even vertex raises its κ-value through the finite set of its simple-path levels, so in-phase fallbacks are at most 1 + N_K (Lemma ACCEL); and inside each epoch of Odd's best response the honest values freeze at the one-player optimum after n − 1 fallbacks, so f ≤ 1 + n·N_ep (Lemma EPOCH) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (neither gives a polynomial bound: N_K can be exponential, N_ep is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C69.md, checker PENDING)
- Object (packet P-N5-ACCEL, added at l-new e9eaaaaf, pinned trunk e7febdc2, unchanged during review): docs/new/P-N5-ACCEL-box44.md, sha1
  301f0be0fa2b2240bba59b347dfbee8426b8dba3 (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-ACCEL-fixes-box44.md (l-new 1c344659, sha1 46ef947403eaea1606837b261c4827aeabd352d3, L-NEW successor 24: N-ACC-2,
  ACCEL-N1 = N-ACC-1, ACCEL-N2, ACCEL-N3 = N-ACC-3, data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; honest frame next_t(v) := σ_t(v) (Even), σ̄_t(v) (Odd); phases as in RESULTS R38 (a); an in-phase
  transition is an S4a step or an Even S4c fallback; f := the in-phase fallbacks of a phase; C, Q, T := C ∪ Q, U_c, wt_c, s_c, κwt_c and κ
  as in RESULTS R56; at a fallback k → k+1, S := S_k ∖ T. K_c(z) := {κwt_c(p ∖ {c}) : p a simple path of G[U_c] from z to c}. An EPOCH: a
  maximal run E of consecutive states of a phase on which σ̄_t|Q is constant; G_E := G with every Odd vertex fixed to σ̄_E; opt_E(z) := the
  best κwt_c-weight of a simple path of G_E[U_c] from z to c; e_1 < e_2 < … the in-phase fallbacks k → k+1 with k ∈ E; N_ep := the epochs
  of the phase.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R17 (a) (V1), R15 (a),
  R15 (d), R19 (d)'s step (SG) ("on all games, not only 𝒞^1O"; its proof uses only R15 (a), the gate, (V1) and strict (V2): ACCEL-N1 =
  N-ACC-1, both referees), R38 (a), R38 (f) CN-LAST (every game), SPEC S1, S2, S4a, S4c; and (VJ), signed on every game in RESULTS R57 (a),
  by which SPEC's Ξσ is VJ00's Ω_σ, so R15 (d) applies to Ξ (ACCEL-N2, REFEREE; accepted by REFEREE-2):
  (a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′), κ-FB-ROUND and CN-ONLY_D, restated with proofs (as in RESULTS R56).
  (b) Lemma ACCEL: in every phase, (a) κ_t(z) ∈ K_c(z) for every state t and z ∈ U_c; (b) the in-phase transitions at which some Even z
      with λ(z) ≠ z switches number at most N_K := Σ_{c ∈ C} Σ_{Even z ∈ U_c ∖ {c}} (|K_c(z)| − 1); (c) f ≤ 1 + N_K.
  (c) Lemma EPOCH: for every phase and epoch E, (a) for t ∈ E with t > e_j and z ∈ U_c, κ_t(z) ≥ the best κwt_c-weight of a simple path of
      G_E[U_c] from z to c with ≤ j edges, and κ_t(z) ≤ opt_E(z) for every t ∈ E; hence κ_t = opt_E on every class for t ∈ E with t >
      e_{n−1}; (b) no transition with both ends in E after e_{n−1} switches an Even z with λ(z) ≠ z, and the part of E after e_{n−1} has at
      most 4n(n − 1) + 1 transitions; (c) f ≤ 1 + n·N_ep.
  Consequence noted by REFEREE-2 and checked by REFEREE (N-ACC-2; it follows from the signed EPOCH (a) and is not a separate statement): for
  every class c and t ∈ E with t > e_{|U_c|−1}, κ_t = opt_E on U_c.
- Not signed (packet §4): what the lemmas do not give (|K_c(z)| can be exponential; no bound on N_ep or on an epoch's S4a steps before its
  freeze); the READING that value-iteration gadgets do not force many N5 switches (consistent with L-RED's built gadget, which collapses:
  docs/red/R76, l-red 2207620f; DATA); the σ̄|Q-repeat instance; the data.
- Honest limits: (i) Neither lemma is a polynomial bound: N_K can be exponential, and N_ep is not bounded here. σ̄|Q REPEATS inside a phase,
  so N_ep is not bounded by the number of σ̄|Q configurations: experiments/new/box25/laps/lap_n6_s1_110421.pg (n 6, Q = {2}, sha1
  4f4fe69c51e1c6f170c9c732feca025da70e7edb), σ̄_t(2) = 0, 4, 0 in one phase, reproduced by REFEREE; repeats in 203 lib41 phases (3 starts)
  and 187 phases of REFEREE-2's 𝒞^1O files; up to 50 epochs in one phase (lev_l_x.pg) and 53 (rise_thin51_n40). (ii) Vacuity (ACCEL-N3 =
  N-ACC-3): EPOCH's global frozen regime (an epoch with ≥ n − 1 in-phase fallbacks) is never reached (REFEREE 0 times; REFEREE-2's best epoch
  1 short in the library, 2 short after four climbs aimed at it, 47,996 runs); EPOCH (a)'s global freeze and (b) rest on their proofs. The
  per-class freeze (N-ACC-2) is reached in data.
- Data (DATA, not proof): REFEREE (successor 12, own engine): lib41 n ≤ 64, the box-43/44 instances, 2,000 random games, 0 failures;
  reproduces the packet's 112 switching transitions and 50 epochs in one phase; 410 switches of Even cycle nodes, none raises κ, so (SG)'s
  hypothesis λ(y) ≠ y cannot be dropped (accepted by REFEREE-2). REFEREE-2 (successor 13, own checker): 51,331 switches, all gaining strictly;
  the per-class freeze checked 18,251 times plus 38,213 in climbs, 0 violations; mutations sg and kk bite (vi, in the same batch, is
  VILB's), ep does not (f stays far below n·N_ep).
- Signatures: REFEREE docs/referee/R-N5-ACCEL.md (referee a19cdff7, successor 12; §C 09b5dbf5): §1, ACCEL (a)-(c), EPOCH (a)-(c) SIGNED; notes
  ACCEL-N1..N3; no gap. REFEREE-2 docs/referee-2/R2-N5-ACCEL.md (referee-2 f0e82d8a, successor 13; §C 5ad79417, successor 14): all SIGN; notes
  N-ACC-1..3; no gap. §C (both): verdicts identical; joint gap map empty; ACCEL-N1 = N-ACC-1; ACCEL-N3 = N-ACC-3; N-ACC-2 accepted by REFEREE
  (missed by it); ACCEL-N2 REFEREE's, accepted; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (no polynomial bound). GAPS G-N5-TIME: open.
