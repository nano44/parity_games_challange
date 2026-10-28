# Draft RESULTS R74 (Lead, 2026-10-28 21:09Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C83 (rev. 2026-10-28 22:03Z by date -u: C83 E-1 (a)-(d), N-1) — LANDED in RESULTS Results 2026-10-28 22:22Z (CHECKER C83 Add. 1 4f494319 PASS), after R73

### R74 [refereed-only] N5 on EVERY game, inside one phase: an S4a step is a Bellman-Ford round at the Even vertices of A_t := F_D(t) ∩ U_c that stay disagreement-free (v ∈ F_D(t) ∩ F_D(t+1)) (Lemma BF-F_D); while A does not grow and no fallback occurs, path weights on A freeze after |A_s| − 1 transitions and an Odd vertex q whose choice lies in A then changes its path weight at most deg(q) − 1 times (Theorem FREEZE-A, (R-LEN)); hence a per-phase bound on those changes in terms of f + G_c (Corollary ROOT-PIECE, a REDUCTION: G_c, the A-gains, is not bounded); every A-gain is a D-leave or an Even switch of an unsplit vertex, and a clean D-leave carries a ROUTE / CYC / TOG event, a route change or a tie (Lemma DL-SPLIT); behind a D-direct gate u the honest path weight M lags the W-path weight MW by exactly the gate's offset Δ_t(u) ≥ 0 and the W-frame step is exact (Lemma GATE-SHIFT), so on a G-interval (S4a steps only, u a D-direct gate, A and R_u not growing, Δ constant) W-path weights on A ∪ R_u freeze after |E_s| − 1 transitions (Theorem FREEZE-G), and a relay of the gate then changes its path weight at most deg(u)(|U_c| − 1 + deg(q)) times after A's freeze (Corollary RELAY-PIECE) (2026-10-26) — structural lemmas and two REDUCTIONS for N5 (G_c, f and the number of G-intervals are not bounded here; FREEZE-G (b)'s freeze sentence, FREEZE-G (c) and RELAY-PIECE's multi-value content rest on proof alone; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C83.md, checker PENDING)
- Objects (L-SI successor 16, Opus 5.5; frozen, unchanged during review): packet P-N5-ROOT, docs/si/P-N5-ROOT-box20.md, sha1
  d3788bc0ce0e3da2d54298c58e227e437242419a (l-si freeze ced5cf27), and its addendum P-N5-ROOT-add, docs/si/P-N5-ROOT-add-box20.md, sha1
  af1c7ad4581cce4a9830b4ed01e2370d26ef850b (l-si freeze 829003b2), reviewed together; both on trunk 539b4192 at REFEREE's review. The
  referees' notes are collected by the lane in docs/si/P-N5-ROOT-fixes-box20.md (l-si 15795d31, sha1
  c8d01a25c61d6ae2eefd3f42a470fa2a467e0c3a, L-SI successor 19: F1-F10 for ROOT-N1..N5, ADD-N1..N2, N-ROOT-1..7; 36 quotes checked by
  script); on trunk; repairs only, no signed statement changes. The statements below are in their repaired wording (F1, F4, F5, F6, F9).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; phases as in RESULTS R38 (a) KEY (λ_Ξ and τ constant); every in-phase transition is an
  S4a step or an Even S4c fallback; D_k, u(v), R_D, F_D as in RESULTS R55's setting; W_t(v) the value of the (σ_t, τ)-play; classes U_c, κ,
  κwt_c, wt_c as in RESULTS R56's setting. Fix a phase, a cycle node c, U := U_c, wt := wt_c, M_t(z) := wt(P(Ξ_t z)), MW_t(z) := wt(P(W_t z))
  when W_t(z) has cycle node c. A_t := F_D(t) ∩ U. G[A]: the graph on A in which every Even v ∈ A ∖ {c} keeps its edges into A, every Odd
  v ∈ A ∖ {c} keeps its τ-edge if τ(v) ∈ A, and c is a sink; MoptA(z) := the best wt-weight of a simple G[A]-path from z to c. An A-GAIN: an
  in-phase S4a transition with A_{t+1} ⊄ A_t; G_c := their number in the phase; f := the in-phase fallbacks. An Odd u ∈ U is a D-DIRECT
  GATE at t (u ∈ DD_t) if u ∈ D_t, σ̄_t(u) ∈ A_t and τ(u) ∈ A_t; its OFFSET Δ_t(u) := M_t(τ u) − M_t(σ̄_t u); R_u(t) := {z ∈ U : the first
  D_t-vertex of z's (σ_t, τ)-play is u}; E_t := A_t ∪ R_u(t); off_t := 0 on A_t and Δ_t(u) on R_u(t); N_t := MW_t on E_t. G′[E] and
  MoptG′[E] as G[A] and MoptA, with R_u-vertices keeping their edges into E (Even) or their τ-edge if it lies in E (Odd, u included). A
  G-INTERVAL for u: states [s, e] of the phase, all transitions S4a, u ∈ DD_t throughout, A_{t+1} ⊆ A_t, R_u(t+1) ⊆ R_u(t), Δ_t(u) constant.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase; no item uses (P); premises LANDED: SPEC S1
  (injective rewards), S4c with FIX 3; RESULTS R38 (a); R55 setting and (a) G_D (a); R17 (a) (F1) and (V1), R21 (a) XW (game-general by
  RESULTS R54 / R55); R56 (a) (Aκ), (A0κ), (M1κ), (M2κ), (INJ) and (d) κ-Y-FORM_D; R61 (e) ALT (CLEAN); R62 (d) WM-G; R63 (a) R-STICK_D;
  P-N5-FLIP §1 additivity (signed as a proof step); RESULTS R72 (b) RELAY-CHAIN for DL-SPLIT (i) (the packet's condition, MET by R72's
  landing: REFEREE-2, and REFEREE's §C). Standing premise 1E-N3 in its two forms (N-ROOT-5, accepted by REFEREE in place of ROOT-N2; F2):
  P2 (S4a's σ_{t+1} is Even's pointwise optimum in the arena H_t) for (F1) on S4a's arena and WM-G (BF-F_D, FREEZE-A, GATE-SHIFT (b),
  FREEZE-G, and through them ROOT-PIECE, RELAY-PIECE); P1 (σ̄ is Odd's pointwise optimum in G_σ) for κ-Y-FORM_D (FREEZE-A (c), DL-SPLIT,
  GATE-SHIFT (a); through them also (R-LEN) and ROOT-PIECE (fixes F2's table), and FREEZE-G and RELAY-PIECE, whose Even step uses GATE-SHIFT
  (a)'s Δ ≥ 0):
  (a) Lemma BF-F_D: at an in-phase S4a transition t → t + 1, for Even v ∈ U ∖ {c} with v ∈ F_D(t) ∩ F_D(t+1) and every successor x ∈ U of v,
      M_{t+1}(v) ≥ wt(v) + M_t(x).
  (b) Theorem FREEZE-A: let every transition of [s, e] be an S4a step with A_{t+1} ⊆ A_t, and L := max(|A_s| − 1, 0). (a) For t ∈ [s, e],
      z ∈ A_t and every simple G[A_t]-path p from z to c with ≤ t − s edges, M_t(z) ≥ wt(p ∖ {c}). (b) M_t(z) ≤ MoptA_t(z) on A_t; hence for
      s + L ≤ t ≤ t′ ≤ e and z ∈ A_{t′}, M_{t′}(z) = M_t(z) = MoptA_t(z). (c) For Odd q ∈ U and V_q := {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩
      A_{s+L}}: at every t ∈ [s + L, e] with σ̄_t(q) ∈ A_t, M_t(q) ∈ V_q; so at most deg(q) − 1 transitions in [s + L, e) with σ̄(q) ∈ A at both
      ends change M(q). For q = c, (Aκ) is not used: M(c) = 0 and τ(c) is c's successor on its cycle, with M = 0 (ROOT-N1 = N-ROOT-1, F1).
      (R-LEN): at the states counted in (c), Ξ(q) runs through ≤ deg(q)·(|U| − 1) distinct values, so it changes at most
      deg(q)·(|U| − 1) − 1 times at the counted transitions (ROOT-N4 = N-ROOT-2, F6: the count follows from the chain of distinct
      (M, length) pairs; the packet's sentence about Ξ on A_t is true but is not the step, as q may lie in D_t).
  (c) Corollary ROOT-PIECE (a REDUCTION in G_c): for Odd q ∈ U, the transitions of the phase with σ̄(q) ∈ A at both ends that change M(q)
      number ≤ (f + G_c + 1)·(|U| + deg(q) − 2) + f + G_c, and the Ξ-changes of q at them ≤ (f + G_c + 1)·(|U| − 1)(deg(q) + 1) + f + G_c.
  (d) Lemma DL-SPLIT: at an in-phase S4a A-gain of class c, every entering z ∈ A_{t+1} ∖ A_t satisfies (A) its first D_t-vertex u is not in
      D_{t+1} (a D-LEAVE at u: σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u)), or (B) z is unsplit at t (λ_{W,t}(z) = λ_t(z) = c) and leaves R_D by an Even switch
      (N-ROOT-4, F4: the packet's statement lacks the binder; the proof shows this form). In case (A) with a CLEAN change (RESULTS R61 (e)),
      y1 := σ̄_t(u), y2 := σ̄_{t+1}(u) and e1 := y1's exit: (i) e1 ≠ c and Ξ(e1) changes, so the transition carries a ROUTE, CYC or TOG event of
      class c (RESULTS R72 (b) RELAY-CHAIN (a)); or (ii) u has a ROUTE CHANGE (some class exit path or exit of u's options differs at t and
      t + 1) (N-ROOT-3, F5); or (iii) a TOG step at e1 or a TIE κ_t(y2) = κ_t(y1). Consequence (a decomposition, not a bound): G_c ≤
      #(B-gains) + #(S4a transitions carrying a ROUTE / CYC / TOG event of class c, or a route change, a tie or a non-clean change at a
      D-leaving vertex). REFEREE's §C: in the clean case (A) without a tie, u also has a ρ event, so a route change there is a ROUTE event in
      P-N5-FLIP's sense; the list is unchanged in content.
  (e) Lemma GATE-SHIFT: (a) at a state t, for z ∈ U with u(z) ∈ DD_t: W_t(z) has cycle node c, Δ_t(u) ≥ 0 and M_t(z) = MW_t(z) − Δ_t(u);
      (b) at an in-phase S4a transition, for Even z ∈ U ∖ {c} whose first D_{t+1}-vertex u lies in DD_{t+1} and every successor x ∈ U of z whose
      (σ_t, τ)-play avoids z: MW_{t+1}(z) ≥ wt(z) + M_t(x), hence M_{t+1}(z) ≥ wt(z) + M_t(x) − Δ_{t+1}(u).
  (f) Theorem FREEZE-G: on a G-interval [s, e] for u, L := |E_s| − 1: (a) for t ∈ [s, e], z ∈ E_t and every simple G′[E_t]-path p from z to c
      with ≤ t − s edges, N_t(z) ≥ wt(p ∖ {c}) (the base N_t(c) = 0 uses c ∉ R_u(t): ADD-N1, F8); (b) N_t(z) ≤ MoptG′[E_t](z); hence for
      s + L ≤ t ≤ t′ ≤ e and z ∈ E_{t′}, N_{t′}(z) = N_t(z) and M_{t′}(z) = M_t(z); (c) for Odd q ∈ U ∖ {u, c}, over t ∈ [s + L, e] with
      σ̄_t(q) ∈ E_t, M_t(q) lies in {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩ E_{s+L}}, non-decreasingly, so ≤ deg(q) − 1 such transitions with
      σ̄(q) ∈ E at both ends change M(q).
  (g) Corollary RELAY-PIECE (a REDUCTION in the number of G-intervals): let [s, e] satisfy FREEZE-A's hypothesis, L_A := |A_s| − 1, u ∈ DD_t
      for every t ∈ [s, e] and R_u(t+1) ⊆ R_u(t). (i) Over [s + L_A, e], Δ_t(u) takes ≤ deg(u) values (non-increasing), so [s + L_A, e] is the
      union of ≤ deg(u) disjoint G-intervals for u (blocks of consecutive states; each transition at which Δ changes lies between two
      consecutive blocks, in neither) (ADD-N2, F9). (ii) For Odd q ∈ U ∖ {u, c}, the transitions in [s + L_A, e) with σ̄(q) ∈ E at both ends
      that change M(q) number ≤ deg(u)·(|U| − 1 + deg(q)).
- Not signed: ROOT §6 and the addendum's §5-§6 (the map of FRZ-U's single-gate steps, GATE-LAG and the other READINGs; the DATA; the OPEN
  items: G_c, which is self-referential with ROOT-PIECE (ρ ≤ (f + G_c + 1)·B and G_c ≤ B-gains + ROUTE / CYC / TOG transitions); the relays'
  own ROUTE events; f on general games; the number of G-intervals). The packet's DATA sentence "case (iii) never occurred" holds only as
  "never ALONE": (iii) occurs (REFEREE 237 ties and 221 TOG steps in its library; REFEREE-2 579 clean D-leaves), always with (i) or (ii)
  (ROOT-N5 = N-ROOT-6, F7).
- Honest limits: (i) Structural lemmas and REDUCTIONS: ROOT-PIECE bounds an Odd vertex's path-weight changes by (f + G_c + 1)·poly(n) and
  RELAY-PIECE bounds a relay's per G-interval; G_c, f and the number of G-intervals (resets of a gate's offset or region) are not bounded
  here; DL-SPLIT decomposes G_c but does not bound it. Nothing here bounds ρ, N_ep, f or N5's running time. (ii) PROOF ALONE (N-ROOT-7,
  REFEREE §4, both §Cs, F10): FREEZE-G (b)'s freeze sentence, FREEZE-G (c), and RELAY-PIECE's multi-value / multi-interval content are never
  reached on natural games (no G-interval outlives its freeze window in the lane's, REFEREE's or REFEREE-2's data, nor in REFEREE's hill
  climbs (best excess −1); Δ(u) never changes after FREEZE-A's freeze index in any run). They are reached only in REFEREE-2's constructed
  disjoint unions (docs/referee-2/R2-N5-ROOT/union/: 25,497 G-intervals past the freeze index, 5 with N moving inside the interval, all pass;
  REFEREE successor 16 re-ran u7101_1900, u7201_1948, u7202_374 with its own engine: 3 G-intervals past the freeze window, max excess 45, 0
  failures); the control that tightens (b)'s freeze index never bites. Both referees checked these proofs line by line. (iii) Over-budget
  pieces: path enumeration skipped REFEREE 165 FREEZE-A pieces / 111 G-intervals in its library row (UNK) and REFEREE-2 the large classes of
  the n = 40-64 library games (e.g. lib41: 7,350 pieces, 5,024 G-intervals UNK).
- Data (DATA, not proof): REFEREE (successor 15, own root_probe.py on its own engine; lane code not run): library n ≤ 24 (2,960 runs; BF-F_D
  316,395 checks; FREEZE-A 142,861 checks, 378 pieces past s + L; FREEZE-G (a) = (b) 47,498 checks on 1,899 G-intervals), 3,000 random games
  (21,000 runs), nep90_n40 and nep76_n40 at the lane's starts, FREEZE-G hill climbs (n 5-10, 2 × 100,000 candidates); 0 failures;
  mutations bite (MUT=1 one more edge: FREEZE-A (a) 136, FREEZE-G (a) 1; MUT=2 GATE-SHIFT (b) with Δ := 0: 181; MUT=3 BF-F_D without
  v ∈ F_D(t+1): 48). REFEREE-2 (successor 17, own root_check.py; lane code not run): the lane's starts, lib2o, lib41, its 503 𝒞^1O files,
  random games with 2, 4 and all Odd choice vertices (19,500 runs), and 12,000 constructed unions; BF-F_D 922,585 checks on lib41 alone;
  0 violations of every check in every set; controls gs0 (Δ := 0) 9,469, fa1 81, fg1 20 (and 8 on unions), early 0 (N-ROOT-7). Both
  reproduce the lane's BF-F_D 7,827 / 8,701 and GATE-SHIFT (a) 684 / 404, (b) 943 / 661 on nep90 / nep76.
- Signatures: REFEREE docs/referee/R-N5-ROOT.md (referee 619fccf2, successor 15; §C da0c1902, stamp corrected 65f55427, successor 16):
  BF-F_D, FREEZE-A (a)-(c), (R-LEN), ROOT-PIECE (as a REDUCTION), DL-SPLIT (split, clean case (A), Consequence as a decomposition), GATE-SHIFT
  (a), (b), FREEZE-G (a)-(c) (FREEZE-G (b)'s freeze sentence and (c) on PROOF ALONE), RELAY-PIECE (i), (ii) SIGNED, no gap; notes ROOT-N1..N5,
  ADD-N1..N2. REFEREE-2 docs/referee-2/R2-N5-ROOT.md (referee-2 3febbfaf, §C f5381a5c, successor 17): the same items SIGN, no gap; DL-SPLIT's
  condition MET (RESULTS R72); notes N-ROOT-1..7. §C (both): verdicts identical; joint gap map EMPTY; ROOT-N1 = N-ROOT-1, ROOT-N4 = N-ROOT-2,
  ROOT-N5 = N-ROOT-6; N-ROOT-5 replaces ROOT-N2 (accepted by REFEREE); N-ROOT-3 and N-ROOT-4 accepted by REFEREE; ROOT-N3, ADD-N1, ADD-N2
  accepted by REFEREE-2; nothing open. Both under the standing premise 1E-N3 (P1 and P2).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and per-phase reductions; no running-time bound). GAPS
  G-N5-TIME: open.
