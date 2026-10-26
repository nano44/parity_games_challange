# Draft RESULTS R50 (Lead, 2026-10-25 23:35Z by date -u; both §Cs and the fixes file filled 2026-10-26 00:12Z) (rev. 2026-10-26 00:28Z: C59 E-1..E-3, N-1..N-4) — to CHECKER C59 — LANDED in RESULTS Results 2026-10-26 00:38Z (CHECKER C59 dc29ee23 + Addendum 1 a58dcd3a PASS), after R49

### R50 [refereed-only] N5 on one-Odd-choice games: above the more relevant cycle node m*, routes freeze after |R| − 1 transitions of every fallback-free run of every stretch (FRZ-U), kinds change at most once and only B → A after the freeze (KIND-MONO, with PAR: c_w ≻ c_θ forces c_w even), so the Ξ-changes on R of a run are ≤ 3Δ·r⁴ (Theorem RUN), (K_W), (E) and wakes K are polynomial per stretch given its fallbacks (Corollary KW-S), and the transitions of a phase are ≤ an explicit polynomial in n, m and its fallbacks f (Corollary PHASE) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C59.md, checker PENDING)
- Objects (one review unit; both unchanged during review): packet P-N5-KW, docs/si/P-N5-KW-box15.md, sha1
  c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (added at l-si bf1ed0f7), and its addendum docs/si/P-N5-KW-addendum-box15.md, sha1
  8d6bfb3c32d80ed7040df4ae2dee56bb9bb9b5bd (added at l-si 47c4e7a2: every count is a TRANSITION count; switches ≤ n · transitions),
  both pinned trunk d9291be0 (L-SI successor 10, Opus 5.5; Lemma PAR and four additions from L-NEW successor 21's cross-read). The
  referees' notes are collected by the lane in docs/si/P-N5-KW-fixes-box15.md (l-si 1d33a337, sha1
  c65f4c1e31b437f66e19cef2ff29cec66b212bdc, L-SI successor 10: KW-1 = N-KW-3, KW-N1..N5, N-KW-1..6, REFEREE's Addendum 1); on trunk;
  repairs only.
  Setting as in RESULTS R24, R26, R27 and R38 (𝒞^1O; phase = joint λ-phase; S4a / S4c; Ξ, W; θ, w, c_θ, c_w; H1, H2; R = R_k (o ∈ R),
  r := |R|, F := V ∖ R, routes π_v; crossings; route form; R26's classes U1, U2, U3, U23 and kinds A / B (under ¬H2 with c_w ≠ o, v is of
  kind A iff c_w ∈ π_v); W-flat runs). A STRETCH is a maximal run of states of a phase with R, θ, w constant; a RUN of a stretch is a
  maximal run of its consecutive non-fallback transitions. m* := the more relevant of c_θ and c_w (c_θ if equal); κ(ρ) := ρ ∩ V_{>m*},
  κ_k(v) := κ(π_v^k). Δ := the maximum out-degree, d_o := |succ(o)|, m := #edges.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every premise is LANDED (R15, R17, R18 (d), R19, R21 (a) XW, R22, R23
  (g), R24, R26, R27, R30 (c), R34 (e), (f), R38 (a)):
  (a) Lemma W-ONCE (every game): if k → k+1 → k+2 are two consecutive S4a transitions of one phase with Ξ_{k+1} = Ξ_k, then
      W_{k+2} = W_{k+1}; and Corollary W-ONCE′.
  (b) Facts A0, A, B (on a stretch): values on R are route values with constant terminals (A0); P(Ξ(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_Ξ and
      P(W(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_W with C_Ξ, C_W constant and disjoint from π_v (A); for y, z ∈ R with κ(π_y) ≠ κ(π_z),
      Ξ(y) ◁ Ξ(z) ⟺ W(y) ◁ W(z) ⟺ κ(π_y) ≺ κ(π_z) (B).
  (c) Lemma FRZ-U: on a run S of a stretch (states k0, …), κ_t(v) = κ_{k0+r−1}(v) for every state t ≥ k0 + r − 1 of S and every v ∈ R.
      Its proof is self-contained (Claim P^c, cases A, B1, B2, B3); it does not rest on a transfer of R20 CR (REFEREE §3).
  (d) Corollary LEN: after k0 + r − 1, the frame whose cycle node is m* changes on R only by lengths, monotonically.
  (e) Lemma PAR (L-NEW successor 21): at every state of a phase on 𝒞^1O, if c_w ≻ c_θ then Ω(c_w) is even (R21 (a) XW).
      Lemma H-PATH: on a stretch with ¬H2, c_w ≠ o and c_w ≻ c_θ, for v ∈ R ∖ {o}, c_w ∈ P(Ξ(v)) iff v is of kind A.
      Lemma KIND-MONO: in a run of such a stretch, after k0 + r − 1 every v ∈ R ∖ {o} changes kind at most once, and only from B to A.
      Lemma CASC-B: in a W-flat segment of a U3 / U23 stretch with no kind change (c_w and kind-A vertices may switch), a kind-B vertex v
      switches only at steps ≤ |π_v| − 2.
      Lemma CW-INT: in a run of a stretch with ¬H2 and c_w ≠ o, between two states with no kind change and no kind-B switch in
      between, c_w switches at ≤ deg(c_w) − 1 transitions.
      Proposition E-SEG (ii)-(v) on a post-freeze W-flat segment Q of a U3 / U23 stretch with c_w ≻ c_θ, with N_cut(Q) := the transitions
      of Q with a kind change or a kind-B switch ≤ (e(Q) + 1)(r − 1). E-SEG (i) as written (N_B(Q) ≤ (e(Q) + 1)(r − 2) over all
      kind-B-switch transitions) is not proved: a kind-change transition can also carry a kind-B switch; the proof gives
      N_B(Q) ≤ e(Q) + (e(Q) + 1)(r − 2); with N_B(Q) redefined as the kind-B-switch transitions WITHOUT a kind change, (i) holds,
      N_cut (counted once) ≤ (e(Q) + 1)(r − 1) − 1, and (ii)-(iv) and Theorem RUN use only N_cut (KW-1 = N-KW-3, both referees,
      independently; fixes).
  (f) Theorem RUN: on a run of a stretch, the transitions with a Ξ-change at some vertex of R number ≤ 3Δ·r⁴: ≤ (r − 1)² if
      c_θ ⪰ c_w; ≤ r³ if c_w ≻ c_θ and the W frame is in route form; ≤ (r − 1)² + (Δr + 1)(2r − 3)·r² ≤ 3Δ·r⁴ on U3 / U23 with
      c_w ≻ c_θ (for r ≥ 2; KW-N3 = N-KW-4).
  (g) Corollary KW-S: a stretch with f_st fallback transitions has ≤ (f_st + 1)·n² non-fallback transitions with a W-change on R ((K_W)),
      polynomially many event transitions per W-flat run ((E); explicit per run: ≤ (r − 1) + (Δr + 1)(r − 1)², KW-N4 = N-KW-6), and
      K ≤ T_rel (wakes counted as transitions).
  (h) Corollary PHASE (CONDITIONAL on f only): a phase on 𝒞^1O with f fallback transitions has T ≤ (m − n + 1)(T_rel + 1) transitions,
      with T_rel ≤ S_o + N_Ξ, N_Ξ ≤ f + (N_st − 1) + (X + 1)(n − 1) + (N_st + f)·3Δn⁴, N_st ≤ 1 + X + Θ + W_ch and the landed bounds on X
      (R30 (c), R34 (e), (f)), Θ and S_o (R27 (g)) and W_ch (R24 (e), F1°); so T = O(m·Δ·d_o·n⁹·(f + n²)).
- Not signed (packet §8 READINGs, §9-§11): with FB-POLY (RESULTS R48), T = O(m·Δ·d_o·n¹¹) per phase; with Corollary Φ-1O (RESULTS R47)
  and a polynomial bit cost per iteration, N5 on 𝒞^1O would make polynomially many iterations (a READING here, to be packeted and
  refereed as an assembly); the lane notes docs/si/N5-KW-box15.md (5ebbb3b6) and docs/new/N5-KW-box42.md v3.2 (349d553c), two independent
  lane proofs. No polynomial bound for N5 on 𝒞^1O is proved by this entry; the assembly (P-N5-1O) is not yet refereed.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase; Corollary PHASE is conditional on f. (ii) Thin data: no post-freeze kind change and no post-freeze c_w switch occurs in
  any data (REFEREE: 0 in 2.46 M post-freeze U3 / U23 transitions with c_w ≻ c_θ; REFEREE-2; L-RED R73; both lanes), so KIND-MONO,
  CW-INT after the freeze and E-SEG's post-freeze counts rest on their proofs; W-ONCE's hypothesis: 2 checks on REFEREE's engine, 571 in
  REFEREE-2's climbs; CASC-B's hypothesis is exercised on REFEREE's engine (Addendum 1, cascb_witness.pg, one step below its bound), in
  REFEREE-2's climbs (10 cases, the latest at step |π_v| − 2, the bound) and twice in L-RED's runs (R73 §7 random, at step |π_v| − 4, two
  below the bound, not pinned; §8 on REFEREE's witness); the c_w-odd branches are empty by PAR. (iii) FRZ-U's index |R| − 1 and CW-INT's deg(c_w) − 1 are attained in
  data (L-RED R73: frzu_tight_n14, cw11_n24).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own kw_probe.py, kw_climb.py on rl_engine): library 253
  games × 4 starts and climbs (2.24 M evaluations): Corollary PHASE inequalities 2.77 M phases, H-PATH 21.9 M vertex-states, PAR 5.1 M
  states, CW-INT 413k c_w switches, CASC-B 687k kind-B switches; 0 failures. REFEREE-2 (own kw_check.py, kw_climb.py): batch 503 files × 3 starts × 3
  traces (4,527 runs) and 3,000 random runs, climbs 160,163 evaluations (640,652 runs); 0 violations; 1.15 M kind changes and 157,577
  c_w switches with c_w ≻ c_θ, ¬H2, all BEFORE the freeze index; CASC-B exercised 10 times, the latest at step exactly |π_v| − 2
  (not saved; two later climbs saved witnesses witness_cascb_13011.pg, witness_cascb_13012.pg, one step below the bound); FRZ-U's κ changes as late as run step 39 on kw_n48.pg
  (N-KW-5; index r − 1 = 47 never exceeded); mutations frz0 and par fire, casc does not on saved data. L-RED successor 18
  (docs/red/R73-*.md, l-red 896aea76; own kw18 tools): lib41 and 4,267,132 random runs, 0 FAIL; PAR 0 odd cases in 1.24 M qualifying
  states. Lane (kwcheck.py, kwclimb.py): ~13 M states, 0 failures.
- Signatures: REFEREE docs/referee/R-N5-KW.md (referee 56ac6538, successor 11; Addendum 1 1d6cbf32; §C a6e50742 + stamp fix 776281ac): W-ONCE, Facts A0 / A /
  B, FRZ-U, LEN, PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, RUN, KW-S, PHASE SIGNED; E-SEG SIGNED WITH GAP KW-1 (one-line repair); notes
  KW-N1..N5. REFEREE-2 docs/referee-2/R2-N5-KW.md (referee-2 8a47fd92, successor 12; §C 20fea7d7): all SIGN, no gap; notes N-KW-1..6.
  §C (both): verdicts identical; joint gap map one row, KW-1 = N-KW-3, found independently and closed by the definitional repair;
  KW-N3 = N-KW-4, KW-N4 = N-KW-6, KW-N5 = N-KW-5; N-KW-1, N-KW-2 (CW-INT step 1 reads "kind B or o") accepted by REFEREE; KW-N1, KW-N2
  accepted by REFEREE-2; REFEREE's CASC-B witness reproduced on REFEREE-2's SPEC trace. No disagreement remains.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
