# Draft RESULTS R76 (Lead, 2026-10-28 23:02Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C85 (Lead reviewed 23:09Z by date -u)

### R76 [refereed-only] N5 on EVERY game, inside one phase: at an in-phase S4a step, a vertex z that migrates into the region R_u of a D-direct gate u (u ∈ DD_t ∩ DD_{t+1}, z ∉ R_u(t) ∪ A_t) has its first D_t-vertex u′ leave D (u′ ∉ D_{t+1}), or some Even vertex on z's play before u′ (z included) switches, and then z's play changes (Lemma MIG-SPLIT); so on a run S the transitions carrying such a migration into u number at most the transitions at which a vertex of D ∩ U_c leaves D plus those at which some z ∈ U_c changes its W-play (its Consequence); IF every unforbid-switch (k′, e) of S inside a global C-interval [a, b] has k′ − a < n − 1 (CONJECTURE UL_G, OPEN), THEN on every run S of in-phase S4a steps with λ_W constant |U(S)| ≤ n_E((n − 1)(K(S) + 1) + K(S)) and every vertex's COARSE_{−1}(W) changes at most (n − 1)(1 + n_E((n − 1)(K(S) + 1) + K(S))) times on S, K(S) the number of C-cuts, global C-intervals read transition-locally (Corollary UL-RED, an implication); and in the abstract model ABS (steps to a pointwise greatest valid arena strategy), an acyclic run is fixed after at most its height ≤ n steps under the basic tie rule (Lemma ABS-HEIGHT) and after at most max over paths of Σ deg ≤ m steps under any deterministic tie rule (Lemma ABS-TIE), and in the cyclic model a vertex v with s_{t+2}(v) ≠ s_{t+1}(v) has a successor y with M_t(y) ≠ M_{t+1}(y), N_{t+1}(y) ≠ N_{t+2}(y) or a change of viability for v, or has s_{t+1}(v) ≠ s_t(v) (Lemma LOC′, any deterministic tie rule; without the last alternative only for tie rules that keep a maximal current choice, LOC) (2026-10-26) — structural lemmas and a conditional REDUCTION for N5, and settling lemmas in an abstract model (UL_G is a CONJECTURE and K(S) is not bounded; the model's link to N5 is a READING; LOC as stated, "any deterministic rule", is FALSE (G-GCX-1); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C85.md, checker PENDING)
- Object (L-SI successor 17, Opus 5.5; frozen, unchanged during review): packet P-N5-GCX, docs/si/P-N5-GCX-box21.md, sha1
  5a91bebbc34f14be147da38adc1a6202407c70c2 (l-si freeze 02240121; quote base 7d87f9be). The referees' notes are collected by the lane in
  docs/si/P-N5-GCX-fixes-box21.md (l-si 652a574f, sha1 6a416c0ac0797922f8d45b2a70fe9e7d2d33c595, L-SI successor 19: F1-F8 for G-GCX-1,
  GCX-N1..N5, N-GCX-1..5; 29 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=29 bad=0", pinned in experiments/si/check.sh);
  on trunk; repairs only, no signed statement changes except G-GCX-1's repair of LOC (F1). The statements below are in their repaired
  wording (F1-F6).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; a phase as in RESULTS R38 (a) KEY (λ_Ξ and τ constant); D_k as in RESULTS R55; W_k the
  (σ_k, τ)-play value (RESULTS R62 setting). A RUN S: consecutive states of one phase, all transitions S4a steps (no fallback); (ii) := λ_W
  constant on S; U(S) at level L = −1 as in RESULTS R67's setting (UNFORBID-SWITCHES). For a cycle node c, U_c := λ^{-1}(c); A_t := {z ∈ U_c : z's
  (σ_t, τ)-play meets no vertex of D_t}; R_u(t) := {z ∈ U_c : u is the first D_t-vertex of z's play}; DD_t := {u ∈ D_t ∩ U_c : σ̄_t(u), τ(u) ∈ A_t}
  (D-DIRECT gates); Δ_t(u) := M_t(τ u) − M_t(σ̄ u). An X-MIGRATION into u at t → t+1: z ∈ R_u(t+1) ∖ (R_u(t) ∪ A_t) with u ∈ DD_t ∩ DD_{t+1};
  X_u(S) := the transitions of S carrying one. A transition of S is GOOD if, for every c, A_{t+1} ⊆ A_t, D_{t+1} = D_t, DD_{t+1} = DD_t and
  Δ_{t+1}(u) = Δ_t(u) on DD_t; a GLOBAL C-INTERVAL is a maximal run of good transitions, a C-CUT a transition that is not good, K(S) their
  number (F2, GCX-N1 = N-GCX-2: under the packet's interval-level reading maximal intervals can overlap and UL-RED (a)'s count step fails,
  long121_n40 (experiments/red/n3/instances, sha1 c667c085), S = [31, 37]: two maximal intervals, K = 0). Model ABS (§4): non-terminals V
  (|V| = n), terminals t with h(t) ≤ T(t), weights w, values in a totally ordered abelian group; a valid strategy s reaches a terminal from
  every v; M_s, N_s add h, resp. T; ARENA Al_s(v) := {s(v)} ∪ {y ∈ succ(v) : M_s(y) > M_s(s(v))}; s′ := a valid arena strategy whose N is
  pointwise GREATEST among those (F6, GCX-N4), assumed to exist; ties broken by a deterministic rule R(arena, values, current choice); the
  BASIC rule keeps the current choice when it is a maximiser (a KEEP rule). Acyclic model: the digraph on V is acyclic.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: SPEC (definitions); RESULTS R38 (a) KEY; R55
  setting (D_k); R62 setting and (b) TC-CLASS (for the Consequence's u′ ∈ U_c, F3); R67 setting (run S, (ii), U(S)) and (f) CHARGE-U (for
  UL-RED (b), at L = −1). (c)-(e) are self-contained in the model:
  (a) Lemma MIG-SPLIT (§2): let t → t+1 be an in-phase S4a transition and z an X-migration into u, with first D_t-vertex u′ (u′ ≠ u). Then (L)
      u′ ∉ D_{t+1}, or (S) some Even vertex w on the part π of z's play at t before u′ (z included) has σ_{t+1}(w) ≠ σ_t(w); in case (S) z's play
      changes (proof with the FIRST switching w, F4; on the play every Odd vertex follows τ, constant on the phase, F3). "(z included)" is
      needed (L-RED R93's cxmig_k: the only switcher is z; REFEREE's MUT=2 fails 28 of 28). Consequence: X_u(S) ≤ #{transitions of S at which
      some vertex of D ∩ U_c leaves D} + #{transitions of S at which some z ∈ U_c changes its W-play}; u′ ∈ U_c by RESULTS R62 (b) TC-CLASS, or
      because z's honest play and W-play agree up to the first D-vertex (GCX-N2 = N-GCX-1, F3).
  (b) Corollary UL-RED (§3; an IMPLICATION from CONJECTURE UL_G, under the transition-local reading, F2): premise UL_G: for every run S with
      (ii), every U event (k′, e) ∈ U(S) whose transition k′ → k′+1 lies in a global C-interval [a, b] has k′ − a < n − 1. Under UL_G, for every
      run S with (ii), n_E the number of Even vertices: (a) |U(S)| ≤ n_E·((n − 1)(K(S) + 1) + K(S)); (b) for every vertex x, COARSE_{−1}(W(x))
      changes ≤ (n − 1)(1 + n_E·((n − 1)(K(S) + 1) + K(S))) times on S (CHARGE-U with (a)).
  (c) Lemma ABS-HEIGHT (§4; acyclic model, basic tie rule): the run is fixed (s′ = s) after at most height ≤ n steps (height: longest path to
      a terminal, in vertices). The tie-rule hypothesis is needed (REFEREE: the one-vertex game below is acyclic and, under the rules "anti"
      or "sizedep", is fixed only after 2 steps at height 1).
  (d) Lemma ABS-TIE (§4; acyclic model, any deterministic tie rule): the run is fixed after at most max over paths of Σ deg(v) ≤ m steps. Its
      proof gives "v constant from t + deg(v) − 1" (N-GCX-3, accepted by REFEREE's §C; F5); the stated bound is unchanged.
  (e) Lemma LOC′ (§4 as repaired, G-GCX-1, F1; REFEREE-2's statement, signed by REFEREE in its §C; cyclic model, any deterministic rule): if
      s_{t+2}(v) ≠ s_{t+1}(v), then some successor y of v has M_t(y) ≠ M_{t+1}(y), or N_{t+1}(y) ≠ N_{t+2}(y), or changes VIABILITY for v (its
      play avoids v under s_{t+1} but not under s_{t+2}, or the reverse), OR s_{t+1}(v) ≠ s_t(v). LOC, the same without the last alternative,
      is signed by both for KEEP rules (R returns the current choice whenever it is a maximiser), the basic rule among them.
  Remarks MONO, MONO-SUCC, NO-RETURN (§4; not to-sign items): REFEREE CHECKED, REFEREE-2 SIGN (MONO's N-half with "greatest", F6).
- Not signed: LOC as stated, "(cyclic model; basic or any deterministic rule)": FALSE for "any deterministic rule" (G-GCX-1, found by both
  independently). Witness (REFEREE, scratch/loc_cex.py; REFEREE-2's is the same model under its rule "flip"): one non-terminal v, w(v) = 0,
  terminal successors a (h 0, T 0), b (h 1, T 5), c (h 2, T 5), s_0(v) = a; under the rules "anti" or "sizedep", s_1(v) = b and s_2(v) = c while
  every successor is a terminal (M, N constant, always viable). REFEREE's second repair class (rules current-independent and consistent
  under contraction) is REFEREE's alone; REFEREE-2 calls the repairs compatible. §5 (READING, CONJECTURES, OPEN, DEAD, DATA), as the packet
  asked: the READING that S4a on a pure global C-interval after A's freeze is the model's step (GCX-N3, F7: h_u's constancy follows from
  RESULTS R74 (b) FREEZE-A (b) and the constant Δ(u); the identification stays a READING); the OPEN lift (cycles in G_c, N5's own tie rule,
  impure intervals); CONJECTURES UL_G (OPEN), FINAL-EACH / ABS-CYC; CONJECTURE UL_C is DEAD (L-RED R91, reader_L; it is not UL-RED's premise:
  UL_G holds there with slack, both referees); DEAD box 21 (C-ONCE, UE-ONCE_C) and DEAD box 21b (the naive cyclic settling order, abscyc.py
  DEEP), docs/si/DEAD.md.
- Honest limits: (i) A conditional REDUCTION: UL-RED is an implication from UL_G, whose support where it could bite is thin (index / threshold
  at most 0.45: x32_waves48 21/47, reader_L40 40/95; N-GCX-4); only its arithmetic is new. K(S) (transitions at which some class's A grows,
  D or DD changes, or a D-direct offset changes) is not bounded; L-SI's passive readers raise L-SI's C-cut count without changing the run
  (DATA, fixes F8; RESULTS R75 honest limit (ii)). MIG-SPLIT bounds X_u by D-leaves and play changes, neither bounded here. (ii) (c)-(e) are
  about the model ABS; its link to N5 is the unsigned READING above. Which kind N5's S4a tie rule is stays OPEN, so a use of LOC for N5 must
  check that N5's rule keeps, or use LOC′; LOC is used by no signed item. (iii) Thin: MIG-SPLIT is exercised at 298 migrations in REFEREE-2's
  data, most on constructed families (N-GCX-4). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own gcx_probe.py on its engine rl_engine, abs_model.py; lane code not run): library 1,140
  files (2,739 runs; MIG-SPLIT 223 checks: (L) only 134, (S) only 84, both 5), lib41 (1,130 runs; 30), L-RED's ul instances (48 runs; 40, all
  (S)), 9,000 + 4,500 random 𝒞^kO runs; UL_G held in every run; 0 failures of every signed check; model: 60,000 acyclic runs (6 rules),
  ABS-HEIGHT's bound attained, 15 runs (non-keep rules) fixed after their height (GCX-N5); LOC fails only under non-keep rules, LOC′ 0
  failures in 25,503 change events (§C); controls MUT=1 and MUT=2 fail 28/28, MUT=4 on all 3 reader runs (MUT=3 does not bite). REFEREE-2
  (successor 18; own gcx_check.py on its SPEC loop over si.py, abs_check.py; lane tools not run): 22,592 N5 runs, 5,193 runs S; MIG-SPLIT 298
  migrations ((L) 83, (S) only 215), Consequence 69 (u, S) pairs, C-intervals disjoint in 5,193 runs (5,687 intervals, 4,327 cuts), UL_G 1,187
  U events inside intervals, UL-RED (a) 5,193, (b) 128,361 vertex-runs: 0 violations; model 150,000 acyclic and 97,065 cyclic runs: LOC
  (non-basic) 166 failures, LOC′ and the other model checks 0. Both: nep90 / nep76 migrations all case (L), cxmig_k all case (S).
- Signatures: REFEREE docs/referee/R-N5-GCX.md (report e01bdec6, §C 4aa7cc2f, stamp corrected 159c8f04; successor 16): MIG-SPLIT and its
  Consequence (with TC-CLASS), UL-RED (a), (b) (conditional, transition-local reading), ABS-HEIGHT, ABS-TIE SIGNED; LOC SIGNED for keep rules,
  NOT as stated (G-GCX-1); LOC′ SIGNED in §C; notes GCX-N1..N5. REFEREE-2 docs/referee-2/R2-N5-GCX.md (report fe04ca32, §C fc63f1f1; successor
  18): the same items SIGN, LOC for the basic rule only (G-GCX-1), LOC′ SIGN; notes N-GCX-1..5. §C (both): verdicts identical; joint gap map
  {G-GCX-1}, with two compatible repairs; GCX-N1 = N-GCX-2, GCX-N2 = N-GCX-1, N-GCX-3 ACCEPTED by REFEREE; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas, a conditional reduction and abstract-model lemmas; no
  running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
