# Draft RESULTS R32 (Lead, 2026-10-25 09:10Z by date -u) (rev. 09:20Z: REFEREE §C C.6 9ad6bfb cited = C41 E-1; rev. 09:31Z: C41 E-2; rev. 09:40Z: C41 N-3) — to CHECKER C41 — LANDED in RESULTS Results 09:48Z (CHECKER C41 22ba41d + Addenda d43a322, 7f5df64, 1670d0d4 PASS), after R31

### R32 [refereed-only] N5 on one-Odd-choice games: a coarse freeze that survives θ-changes, w-changes and fallbacks (Theorem FREEZE, with Fact 0, ARENA, P^c_ℓ, RATCHET, BLOCK), polynomially many crossings per fallback-free run with an H1 SN prefix (Theorem X-RUN), and R20's subrun machinery with θ free (Theorem SUB) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C41.md, checker PENDING)
- Object (packet P-N5-FRZ, added at l-new edbccb6, pinned trunk 25fda0f, unchanged during review): docs/new/P-N5-FRZ-box34.md, sha1
  39df373c17d91f942ad2cb15244cd779ca7abda1 (L-NEW successor 14, Opus 5.5). The referees' repairs are collected by the lanes in
  docs/new/P-N5-FRZ-fixes-box34.md (l-new 1dc42ba, sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd, L-NEW successor 14: FRZ-1..FRZ-3) and
  docs/new/P-N5-FRZ-fixes2-box34.md (l-new 5f02ceb, sha1 ed2ca80df2fcd57bf35160d0e1ad926a29e5bb60, L-NEW successor 15: REFEREE-2's rows
  mapped to FRZ-1..3; N-FRZ-1's two-prefix fact C7′; N-FRZ-4 definitions; NL phase-key line); both on trunk; repairs only.
  Setting as in RESULTS R25 and R27-R31 (COARSE_L, (C1)-(C7), lev with ⊥ < −1 < 0 < …; Ξ, W, λ; on 𝒞^1O inside a PHASE (λ_Ξ and τ
  constant): R, R̄, F, θ, w, c_θ, c_w, H1-H3, (h), r_k := lev(θ_k, w_k), SN prefix (R30 (c))). A WINDOW at ℓ < ∞ is a run of consecutive
  states of a phase, all with (h) and r ≤ ℓ (fallbacks allowed). A (w, r)-SUBRUN is a maximal run of consecutive (h) states of a phase
  with w and r constant (θ may change; fallbacks allowed).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Corollary NL-MF: at an in-phase S4a step j with (h), if r_j > MF_j (the maximal level of a gate into F_j, ⊥ if none), then R_j ⊆
      R̄_{j+1} and MF_{j+1} ≤ MF_j (R29 NL; NL is signed on the key (λ_Ξ, λ_U, τ), and its proof uses no λ_U, so it applies on the
      (λ_Ξ, τ) phase: REFEREE §1, accepted by REFEREE-2 §C).
  (b) Fact 0: at an (h) state of a phase every vertex's W-cycle node is λ(v), and λ(v) = c_θ ∈ F for v ∈ R̄. Lemma ARENA: at an S4a step
      from an (h) state the arena contains every W-improving edge of G_τ except possibly F → R̄ non-gates (WITHHELD), each of level ≤ r_k.
      (The R → R̄ case uses the two-prefix, one-base twin of (C7), not (C7): N-FRZ-1, citation, closed; fixes2 Fact C7′.)
  (c) Lemma P^c_ℓ (R20's Lemma P^c with COARSE_ℓ, statewise Lemma C_ℓ and coarse monotonicity along a window, fallbacks included):
      Ω^c_{k0+j}(x) ⪰ COARSE_ℓ(value(ρ)) for every simple path ρ of G_τ of length ≤ j from x to an honest cycle node. Gaps FRZ-1 = N-FRZ-2
      (case (γ) of B1, the inherited XA-3; wording) and FRZ-2 = N-FRZ-3 (B-fallback B1 at an own cycle node x = λ(x); wording), both
      closed by fixes 168de464.
  (d) Theorem FREEZE: if a window at ℓ has n states ending at F, then for every state t ≥ F of the phase that has some H2 state t2 ≥ t
      in the phase, COARSE_ℓ(Ξ_t) = COARSE_ℓ(Ξ_F) everywhere, and at H2 states t also COARSE_ℓ(W_t) = COARSE_ℓ(Ξ_F); θ, w, R may change
      and fallbacks may occur after F. Corollary RATCHET: at every H2 state t ≥ F, COARSE_ℓ(θ_t) = COARSE_ℓ(w_t) (so H1 there gives (h));
      for ℓ ≥ 0, COARSE_{ℓ−1}(θ) takes ≤ 2d_o values over those states with H1, COARSE_{ℓ−1}(w) changes ≤ once, and they split into
      ≤ 2d_o + 1 runs with constant pair. Lemma BLOCK: on consecutive (h) states t ≥ F with a constant differing pair (r = ℓ), a vertex
      leaving R at an S4a step inside the run does not re-enter R in the run.
  (e) Theorem X-RUN: in a fallback-free run Q of a phase whose SN prefix P has H1 throughout, crossings with both ends in P number
      ≤ 13(d_o + 1)n³; REL_Q ≤ 13 d_o(d_o + 1)n³; ε_H1(Q) ≤ d_o + REL_Q (R30 ABS-COUNT′); Q has ≤ 13(d_o + 1)n³ + n crossings. The
      transition leaving P can release exits and is not covered by R-STICK; REL_Q ≤ d_o(C_P + 1) with C_P + 1 ≤ 13(d_o + 1)n³ (FRZ-3 =
      G-FRZ-1, accounting, closed by fixes 168de464; the stated bounds stand).
  (f) Theorem SUB: on a (w, r)-subrun with r = ρ ≥ 0, R20's Lemma C, Lemma CR and Theorem XA hold with COARSE_ρ (θ free).
- Not signed (packet §8, not to sign): FBF on (w, r)-subruns FALSE (b6_xl2_n32; 1,442 entries after fallbacks); CL1 ("one fallback
  cluster per level per scope run") FALSE (x48_rt48_final, 9 clusters); OPEN (L1), (L2), ¬H1 SN states, f per phase.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) X-RUN bounds crossings per fallback-free run GIVEN H1 on the SN prefix; f per
  phase, (L1) and (L2) are OPEN here, so G-N5-TIME stays open. (iii) DATA is thin: random games never give an n-state (h) window, so
  FREEZE, RATCHET, BLOCK and SUB (iii) rest on library and climb instances; BLOCK is VACUOUS in both referees' data (0 S4a leaves at an
  (h) state after any freeze); no freeze at ℓ = −1 or ⊥ occurs anywhere, so X-RUN's segment −1 and post-F(⊥) parts are proof-only; the
  transition leaving P never carried a leave in any data (FRZ-3 is a proof gap only). (iv) Lane work after the pin (P-N5-L2, P-N5-TOG,
  CN-LAST, PF-THETA) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE frz_probe.py (own trace = n5.run, phase key (λ_Ξ, τ)):
  library 252 files, random 𝒞^1O 4,000 + 3,000 games, 0 failures (NL-MF 1,978; Fact 0 5,320 library + 8,476 random; ARENA withheld
  edges 41,479, every one F → R̄ and not a gate; Step 1 54,191 library + 48,714 random window states; FREEZE 142 windows / 2,958
  later-state checks; BLOCK 30 runs; X-RUN 472 library runs, max 55 crossings in P, max REL_Q 12; SUB 357 subruns); random games give 0
  freeze windows. REFEREE-2 frz_check.py (own N5 accepting any S4a arena optimum; agrees with Oink zlk on 468 / 468 library runs): 16,434
  batch runs + 12 climbs (1,485,828 runs), 0 violations (FREEZE 302 library freezes, 5,502 later states; P^c_ℓ 3,386 windows, 927,530
  sampled path comparisons; BLOCK 60 library blocks + 3,610 in the 12 climbs (three aimed at leaves), 0 S4a leaves); with windows of n/2 states FREEZE
  fails on x32_sc32_final (96 violations), and FREEZE's later-H2 hypothesis is used (x31_rx48). REFEREE re-ran b6_xl2_n32 and
  x48_rt48_final (n5, Oink OK).
- Signatures: REFEREE docs/referee/R-N5-FRZ.md (referee 3a520ce, successor 6; Addendum 3171efc on fixes 168de464; §C 1f13a6f + C.6 9ad6bfb, successor 7):
  NL-MF, Fact 0, ARENA, Steps 1-2, FREEZE, RATCHET, BLOCK, SUB SIGNED; P^c_ℓ SIGNED WITH GAPS FRZ-1, FRZ-2 (closed); X-RUN SIGNED WITH
  GAP FRZ-3 (closed); §C accepts N-FRZ-1 (missed by REFEREE) and N-FRZ-4; C.6: 0 S4a leaves at any (h) state after a freeze at ℓ ≥ 0 (library 261 files, 2,410 (window, ℓ) transition checks). REFEREE-2 docs/referee-2/R2-N5-FRZ.md (referee-2 20a73ca; §C
  f546b43; successor 7): NL-MF, Fact 0, ARENA (N-FRZ-1), P^c_ℓ (N-FRZ-2, N-FRZ-3; label aligned to REFEREE's in §C), FREEZE, RATCHET,
  BLOCK, SUB SIGN; X-RUN SIGN WITH GAPS G-FRZ-1 (closed). §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 6 rows: FRZ-1
  = N-FRZ-2 (wording, closed); FRZ-2 = N-FRZ-3 (wording, closed); FRZ-3 = G-FRZ-1 (accounting, closed); N-FRZ-1 (citation, closed;
  REFEREE-2 only); N-FRZ-4 (wording: d_o, crossing, leave defined in fixes2; REFEREE-2 only); NL phase key (REFEREE only; accepted).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
