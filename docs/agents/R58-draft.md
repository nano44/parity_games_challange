# Draft RESULTS R58 (Lead, 2026-10-26 05:44Z by date -u; both §Cs and the fixes file filled) (rev. 2026-10-26 06:11Z: C67 E-1, N-1, N-2, N-3) — to CHECKER C67 — LANDED in RESULTS Results 2026-10-26 06:23Z (CHECKER C67 9f733791 + Addendum 1 36d6f3e8 PASS), after R57

### R58 [refereed-only] N5 on EVERY game, CONDITIONAL on RESULTS R56: with at most two Odd choice vertices per honest class, the Q-runs holding a late fallback number O(n²) per phase (Theorem FB-2T), so on two-Odd-choice games every phase of every run has at most 1 + (n − 1)(1 + 12n²) = O(n³) in-phase fallbacks (Corollary FB-2O), with Lemmas (YB_q), PFZ-q, ROUTE-2, DIR and SAT-2 (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a fallback count only; not an iteration bound on any class, not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C67.md, checker PENDING)
- Object (packet P-N5-2T, added at l-si f6839fd3, pinned trunk cbb3b738, unchanged during review): docs/si/P-N5-2T-box16.md, sha1
  fcb91130b1f93d041233c9def50614b4d0dc9a05 (L-SI successor 11, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-2T-fixes-box16.md (l-si 35c8eee9, sha1 8aad9f77d27a6231dd012a270882f35b437ab227, L-SI successor 11: 2T-N1 = N-2T-4,
  N-2T-1, 2T-N3 = N-2T-5, N-2T-2, N-2T-3, 2T-N2, 2T-N4 = N-2T-6 data); on trunk; repairs only.
  Setting (every game): as in RESULTS R56 (phase; g_1 < g_2 < … the in-phase fallbacks, g_j also its source state; a fallback belongs to
  the run containing its source, FBRED-N1; f^Θ_j the source of the j-th fallback whose source lies in the run Θ; Q, C, T := C ∪ Q, honest
  classes U_c, κ, κwt_c, G_c, G_c^q, κopt_c, κopt^q, Q-runs; sums of κ values are arithmetic). Q_c := (Q ∩ U_c) ∖ {c}, the terminals of
  class c; a q-run is a maximal run of the phase with Ξ(q) (equivalently κ(q)) constant; q ∈ Q_c is DIRECT at t if q lies on its own
  honest cycle at t or its honest play at t visits c before any other vertex of Q_c; d_q := |succ(q) ∩ U_c|; w_c := |U_c| − 1; Cyc_c :=
  {(0, s_c·ℓ) : 1 ≤ ℓ ≤ |U_c| − 1}. A_q := {κwt_c(q) + κopt_c(y) : y ∈ succ(q) ∩ U_c ∖ Q, κopt_c(y) defined} ∪ {κwt_c(q) : c ∈ succ(q)}
  ∪ Cyc_c; for Q_c = {q, q′}, V_{q′}(α) := {κwt_c(q′) + β_y(α) : y ∈ succ(q′) ∩ U_c, y ≠ q′, β_y(α) defined} ∪ Cyc_c with β_q(α) := α,
  β_c(α) := (0, 0) and, for y ∉ T, β_y(α) := the larger of κopt_c(y) and κopt^q(y) + α over those defined. Hypothesis (2T) for a phase:
  |Q_c| ≤ 2 for every class. 𝒞^2O := the games with exactly two Odd choice vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game and CONDITIONAL on RESULTS R56 (landed); no item uses (P); premises
  LANDED: RESULTS R56 (a), (b), (c), (f), R38 (a); the packet quotes R56 from its landed text (the κ-FB-ROUND parenthetical it quotes is
  FBRED §1.1 l. 52, not R56's own wording: N-2T-1, REFEREE-2; accepted by REFEREE):
  (a) (YB_q): if q ∈ Q_c lies on its own honest cycle at t, then P(Ξ_t q) = ∅ and 1 ≤ ℓ(Ξ_t q) ≤ |U_c| − 1, so κ_t(q) ∈ Cyc_c (proved in
      the packet, not cited: N-2T-2).
  (b) Lemma PFZ-q: R56 (c) κ-PFZ_D with "Q_c-run" weakened to "q-run" and with N-FBRED-1's range: for a q-run Θ with value κ_Θ(q), j ≥ 0,
      t ∈ Θ with t > f^Θ_j (any t ∈ Θ if j = 0), z ∈ (U_c ∖ T) ∪ {q} and every simple path p of G_c^q from z to q with ≤ j edges,
      κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_Θ(q) (the weakening is safe: N-2T-3).
  (c) Lemma ROUTE-2: if Q_c = {q, q′}, at every state of the phase q or q′ is direct.
  (d) Lemma DIR: if t > g_{|U_c|−1} and q ∈ Q_c is direct at t, then κ_t(q) ∈ A_q, |A_q| ≤ d_q + w_c. Its proof never uses |Q_c| ≤ 2, so
      it holds in any class (2T-N2, REFEREE; also REFEREE-2's R2-N5-FBK §0).
  (e) Lemma SAT-2: if Q_c = {q, q′}, Θ is a q-run and t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1}, then κ_t(q′) ∈ V_{q′}(κ_Θ(q)),
      |V_{q′}(α)| ≤ d_{q′} + w_c.
  (f) Theorem FB-2T: in a phase with (2T), R56 (f)'s N_late (the Q-runs holding a fallback g_j, j ≥ n) satisfies N_late ≤ 1 + Σ_c (N_c −
      1) over the classes with Q_c ≠ ∅, where N_c := |A_q| ≤ d_q + w_c if Q_c = {q}, and N_c := |A_q|·(w_c + max_α |V_{q′}(α)|) +
      |A_{q′}|·(w_c + max_α |V_q(α)|) ≤ 2(d + w_c)(d + 2w_c), d := max(d_q, d_{q′}), if Q_c = {q, q′}. Step 3 counts distinct pair
      VALUES (b on I_α) (2T-N3 = N-2T-5, both referees).
  (g) Corollary FB-2O: on 𝒞^2O every phase of every N5 run, from every start pair, has f ≤ 1 + (n − 1)(1 + N_late) ≤ 1 + (n − 1)(1 +
      12n²) = O(n³). Its case list is read with the omitted case "both Odd choice vertices are cycle nodes", where N_late ≤ 1 (2T-N1 =
      N-2T-4, both referees, independently).
- Not signed (packet §6, §7): what else a 𝒞^2O running-time bound needs (crossings, T per phase given f) and the case of more than two
  terminals (READING; that case is RESULTS-pending P-N5-FBK's Theorem FB-kT, in review); the data. The remark after FB-2O's proof (a
  whole-run count via RESULTS R54 (e)) is not part of the signed statements.
- Honest limits: (i) A fallback count per phase, CONDITIONAL on R56; it bounds no iterations, crossings or S4a steps on any class:
  G-N5-TIME stays open, and a 𝒞^2O polynomial bound would still need crossings and transitions per phase. (ii) Vacuity (2T-N4 = N-2T-6):
  natural data never meet SAT-2's or FB-2T's hypothesis in either referee's batches (best closeness −2 on the library, −1 on random
  games); REFEREE-2 met SAT-2's hypothesis on CONSTRUCTED disjoint unions of the box-43/44 instances with small two-terminal gadgets (648 SAT
  checks over all unions, every branch of its proof exercised); the four fb17_g{3,4,5,5c}_P66.pg witnesses (docs/referee-2/R2-N5-2T/
  instances/) carry 108 of them, and REFEREE re-ran those four on its own engine (DIR 93 and SAT 108 checks, equal counts, 0 failures); FB-2T's late regime (an index ≥ n) is never reached (max f 37), so FB-2T rests on
  its proof. (iii) DIR's hypothesis is met 65 times in REFEREE's natural data. (iv) The title's O(n²) for N_late uses d_q ≤ |U_c| (by the
  definition d_q := |succ(q) ∩ U_c|), so N_c = O(w_c²), and Σ_c w_c < n; this arithmetic is in neither report (C67 N-1).
- Data (DATA, not proof): REFEREE (successor 12, own probe; path checks for n ≤ 14 by default, some batches at PATHN 16 / 40): 11,999 natural runs (lib41 × 7, lib2o × 7 and × 3,
  3,000 random 𝒞^2O × 3); PFZ-q 169,165 checks, (YB_q) and ROUTE-2 exercised often, DIR 65, 0 failures; mutation (PFZ with j +
  1 edges; DIR / SAT without Cyc_c) bites (125 PFZ failures). REFEREE-2 (successor 14, own tt_check.py, reusing successor 13's SPEC loop; lane code not run): 22,003 natural
  runs (lib41 × 2, 503 𝒞^1O files × 2, lib2o × 3, box-43/44 instances × 5, 20,000 random 𝒞^kO); (YB_q), ROUTE-2, PFZ-q and DIR checked on
  every run, 0 violations; the constructed unions above; mutations sat0 and satalpha bite. L-RED (adversary, docs/red/R76 §8, l-red 7cc9f5ac; not a
  referee check): SAT-2 exercised on climbed natural instances (sat68_n20, 68 checks), DIR 82 checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-2T.md (referee 7055b4a5, successor 12; §C 09b5dbf5 + 906247c6): all seven statements SIGNED,
  conditional on R56; notes 2T-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-2T.md (referee-2 8f43432b + 416334cc and §C
  3d8de145, successor 14): all SIGN, conditional on R56; notes N-2T-1..6; no gap. §C (both): verdicts identical; joint gap map empty; 2T-N1
  = N-2T-4; 2T-N3 = N-2T-5; N-2T-1 accepted by REFEREE (missed by it); 2T-N2 REFEREE's, accepted; SAT-2 exercised on two engines; nothing
  open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase fallback count, conditional on R56; no running-time bound). GAPS
  G-N5-TIME: open.
