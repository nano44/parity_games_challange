# Draft RESULTS R56 (Lead, 2026-10-26 03:54Z by date -u; both §Cs filled; fixes file filled 04:00Z) (rev. 2026-10-26 04:15Z: C65 N-1, N-2) — to CHECKER C65 — LANDED in RESULTS Results 2026-10-26 04:15Z (CHECKER C65 b911ecce PASS), after R55

### R56 [refereed-only] N5 on EVERY game: in-phase fallbacks per phase are at most 1 + (n − 1)(2 + ρ), ρ := the Ξ-changes at Odd choice vertices in the phase, and at most 1 + (n − 1) + (n − 1)·N_late counting only Q-runs that hold a late fallback (Theorem FB-RED, both forms, signed as a REDUCTION in ρ), with the set-form κ lemmas of RESULTS R48 and the terminal-value freeze (Lemma TV) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (not M3, not a step-4 pass, not a TARGET.md claim; ρ is not bounded, CONJECTURE ρ-POLY OPEN; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C65.md, checker PENDING)
- Object (packet P-N5-FBRED, added at l-new 3732ab55, pinned trunk c3f6f2bf, unchanged during review): docs/new/P-N5-FBRED-box44.md, sha1
  11b15455f70d439c93a48d7e82fcdc14ef73854d (L-NEW successor 23, Opus 5.5); a port of RESULTS R48 (P-N5-FBPOLY, "FBP") to every game. The
  referees' notes are collected by the lane in docs/new/P-N5-FBRED-fixes-box44.md (l-new 2742f3e9, sha1 05c249433431f7e147272ad689c0a7815b7a5b71, L-NEW successor 23:
  N-FBRED-1, N-FBRED-2, FBRED-N1, N-FBRED-3, N-FBRED-4 = FBRED-N2, the signed scope); on trunk; repairs only, no signed statement changes.
  Setting (every game; no hypothesis on the class, (h_D), (h3_D), H1, τ or c_w): N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md; phases as
  in RESULTS R38 (a) KEY; g_1 < g_2 < … the in-phase (Even S4c) fallbacks of a phase. Q := the Odd vertices of out-degree ≥ 2; C := the
  honest cycle nodes of the phase; T := C ∪ Q (terminals); for c ∈ C the honest class U_c := λ^{-1}(c). κ_t(z) := (signed weight of
  P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if
  rank(v) > rank(c), else 0. At a fallback k → k+1, S_k := the switched Even vertices, S := S_k ∖ T, S_c := S ∩ U_c, x*_v := σ_{k+1}(v).
  G_c := U_c ∖ (Q ∖ {c}) with c a sink; for q ∈ Q ∩ U_c, q ≠ c, G_c^q := U_c ∖ (T ∖ {q}) with q a sink (Even vertices keep their edges
  inside, Odd vertices, all forced there, their edge if inside); κopt_c(z), κopt^q(z) := the best κwt_c-weight of a simple path of G_c
  to c, respectively of G_c^q to q. A Q_c-run (Q-run): a maximal run of the phase with Ξ(q) constant for every q ∈ Q ∩ U_c (every q ∈ Q).
  ρ := the number of pairs (transition t → t+1 of the phase, q ∈ Q) with Ξ_{t+1}(q) ≠ Ξ_t(q). "The i-th fallback of its run" counts the
  fallback k → k+1 in the run that contains its source state k (FBRED-N1, both referees).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R15 (a), R17 (a) (V1),
  R18 (d) Lemma S (a), R38 (a) KEY and R38 (f) CN-LAST, and the FBP steps of RESULTS R48 that the packet ports. R18 (d) Lemma S (a) is
  signed under a 𝒞^1O setting line; both referees read its proof (VJ00 (11) and R17 (F1) on the one-player game G_σ) and CONFIRM it holds
  on every game (N-FBRED-3 = REFEREE §1):
  (a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class, and κ-FB-ROUND_D (FBP §0.3, §1 with c for c_θ).
  (b) κ-HAT-FREEZE_D (a)-(c) on G_c: (a) for t > g_j, z ∈ U_c ∖ (Q ∖ {c}) and every simple path p of G_c from z to c with ≤ j edges,
      κ_t(z) ≥ κwt_c(p ∖ {c}); (b) if z's honest play at t avoids Q ∖ {c}, κ_t(z) ≤ κopt_c(z); (c) for t > g_{|U_c|−1}, κ_t(y) =
      κopt_c(y) for every y ∈ U_c whose honest play at t avoids Q ∖ {c}.
  (c) κ-PFZ_D (per q ∈ Q ∩ U_c, q ≠ c, Θ a Q_c-run): for t ∈ Θ after the j-th fallback of Θ and every simple path p of G_c^q from z to q
      with ≤ j edges, κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_t(q); stated for z ∈ (U_c ∖ T) ∪ {q}, since the induction passes through z = q, where the
      claim is trivial (N-FBRED-1, both referees).
  (d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle): κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y),
      with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}, a definition the packet gives only in its not-to-sign §4 table and
      which is read into the signed text (N-FBRED-2, REFEREE-2; accepted by REFEREE). The "≤" half uses R18 (d) Lemma S (a) on every game.
  (e) EXIT-SWITCH_D (at an in-phase fallback k → k+1 with S_c ≠ ∅, some u ∈ S_c has: the honest play at k from x*_u visits T ∩ U_c
      before it visits u; for the first such vertex e, p_u := u · (that play up to e) is a simple path of G_c (e = c) or G_c^e (e ∈ Q),
      and κ_k(x*_u) = κwt_c(p_u ∖ {u, e}) + κ_k(e)), FREEZE-EXIT_D (conservative indices: if k = g_j with j ≥ |U_c| and k is the i-th
      fallback of its Q_c-run with i ≥ |U_c|, then S_c = ∅) and CN-ONLY_D (a fallback with S = ∅ is the last transition of its phase; at most one per phase).
  (f) Theorem FB-RED: for every phase of N5 on any game, f ≤ 1 + (n − 1) + (n − 1)(1 + ρ) = 1 + (n − 1)(2 + ρ). Late form: f ≤ 1 + (n − 1)
      + (n − 1)·N_late, with N_late := the Q-runs of the phase holding a fallback g_j, j ≥ n, and N_late ≤ 1 + ρ_late (ρ_late := the
      Ξ-changes at Odd choice vertices at transitions after g_{n−1}). Both SIGNED AS A REDUCTION in ρ: polynomial in n only given ρ.
  (g) Lemma TV: for a Q-run Θ, c ∈ C, and t ∈ Θ after |U_c| − 1 fallbacks of the phase and of Θ, every z ∈ U_c ∖ T has κ_t(z) =
      max(κopt_c(z), max over q ∈ Q ∩ U_c, q ≠ c, of κopt^q(z) + κ_Θ(q)).
- Not signed (packet §4-§6): the step table against FBP (a READING; both referees' own diffs agree with it); THETA-AFTER (fails as proved
  with several terminals; its per-terminal bound held in every check, unproved); CONJECTURE ρ-POLY and the nested-freeze route (OPEN;
  §5.1: short late Q-runs and terminal path-sum values); the data. On 𝒞^1O, RESULTS R48 (FB-POLY) stays the unconditional form.
- Honest limits: (i) A REDUCTION: ρ per phase is not bounded (max ρ 218 in one phase, tcL_N10, n 350, REFEREE). (ii) Vacuity
  (FBRED-N2 = N-FBRED-4, both referees): no phase in any sample or climb of either referee or the lane reaches n in-phase fallbacks (max
  37 at n 48 on 𝒞^1O, dirty_a_best in REFEREE-2's 503 files, 33 in lib41; 17 at n 32 on the frontier, fb17_n32; REFEREE-2's climbs on f − n reach −4), so FREEZE-EXIT_D's hypothesis, the
  third bullet of FB-RED, the late form's N_late and Lemma TV's hypothesis are never met in data: they rest on their proofs. (iii)
  REFEREE successor 12 re-derived every port against FBP §0.3-§4 except κ-HAT-FREEZE (b), (c) in detail, where it accepts successor 11's
  reading (R-N5-FBRED §C C.1). (iv) The constant n − 1 (not FBP's |U| − 2) comes from FREEZE-EXIT_D's conservative indices.
- Data (DATA, not proof): REFEREE (successor 11, own fbred_probe.py on rl_engine; logs scratch/fbred_logs/): lib41 n ≤ 64 (367 games)
  from S3 and 2 random start pairs, 1,101 runs, 5,393 phases, max f 33, max ρ 51; the box-43/44 instances × 5 starts, 50 runs, max f 17
  (fb17_n32); 1,200 random runs with 1-4 Odd choice vertices; 0 failures; successor 12 added the 45 games with n > 64 (135 runs, 1,834
  phases, max ρ 218), 0 failures, and reproduced REFEREE-2's ρ 194 on tcL_N8 at its start pair. REFEREE-2 (own fbred_check.py): 22,292
  runs, 61,151 phases (lib41 × 3, 503 𝒞^1O files × 2, the 10 instances × 5, 20,000 random 𝒞^kO), κ-Y-FORM_D 309k and κ-PFZ_D 290k checks
  (exhaustive simple-path enumeration for n ≤ 11), HAT (c) and TV 97 qualifying states each; 0 violations; mutations yf, cno bite, fex,
  red do not (the data never come within 4 of FREEZE-EXIT_D's indices).
- Signatures: REFEREE docs/referee/R-N5-FBRED.md (referee 1feff548, successor 11; §C 1ea0d317, successor 12): every to-sign statement
  SIGNED, FB-RED and its late form AS A REDUCTION; notes FBRED-N1, FBRED-N2; no gap. REFEREE-2 docs/referee-2/R2-N5-FBRED.md (referee-2
  814ac456, successor 13; §C a4a642b6): all SIGN, FB-RED as a reduction in ρ; notes N-FBRED-1..4; no gap. §C (both): verdicts
  identical; joint gap map empty; N-FBRED-1, N-FBRED-2 accepted (N-FBRED-2 missed by REFEREE successor 11); N-FBRED-3 = REFEREE §1;
  N-FBRED-4 = FBRED-N2; FBRED-N1 REFEREE's, the convention REFEREE-2 uses; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; no running-time bound). GAPS G-N5-TIME: open for general games.
