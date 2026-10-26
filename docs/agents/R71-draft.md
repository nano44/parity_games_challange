# Draft RESULTS R71 (Lead, 2026-10-26 15:09Z by date -u; both reports, both §Cs and the fixes file filled (15:24Z by date -u)) — to CHECKER C80 (rev. 2026-10-26 15:49Z by date -u: LEAD-N1 resolved by REFEREE's erratum ae36ce48)

### R71 [refereed-only] N5 on EVERY game: in the honest frame H_C of a configuration C = σ̄|Q (every Odd vertex cut to its σ̄_C edge), an in-phase fallback from a C-state raises the level LEV_C to min(LEV_C + 1, n − 1) (Lemma FB-RISE_C); LEV_C = n − 1 at a C-state gives Ξ = B_C, and later C-states of the phase follow within 4n(n − 1) transitions with Ξ constant (Lemma SAT_C); hence in every phase the in-phase fallbacks number at most |𝒞_f(P)|·(4n² − 3n), 𝒞_f(P) the configurations at fallback sources (Theorem FB-C), so f ≤ (4n² − 3n)·min(N_ep, Π_q deg(q)), f ≤ Δ^k(4n² − 3n) on 𝒞^kO, and f ≤ (1 + m)(4n² − 3n) when |D| ≤ 1 throughout (Corollaries (a)-(d)) (2026-10-26) — a REDUCTION of f to the number of distinct configurations per phase (that number is not bounded here on general games; (a)'s N_ep form and (d) are weaker than RESULTS R60 (c) EPOCH for n ≥ 2; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C80.md, checker PENDING)
- Object (packet P-N5-FBC, added at l-new 1f8d6d7d, pinned trunk de02d37e, unchanged during review): docs/new/P-N5-FBC-box47.md, sha1
  32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (L-NEW successor 26, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-FBC-fixes-box47.md (l-new c2691e46, sha1 1347222ccc39ea380035da050b8af2f7cc8473d6, L-NEW successor 28: R1-R6 for FBC-N1, -N2,
  -N4, N-FBC-1..5 and REFEREE's n = 1 line; §4: FBC-N3 is not a repair but P-N5-EPC §3; 45 quotes checked by script); on trunk; repairs only,
  no signed statement changes.
  Setting (every game): as in RESULTS R70 (N5 = SPEC S1-S5; Ξ_k the value of the honest play; phases; λ; value(r); f). Q := the Odd vertices of
  out-degree ≥ 2; a CONFIGURATION is C = σ̄|Q, k is a C-STATE if σ̄_k|Q = C; H_C := G with every Odd v cut to its one edge σ̄_C(v) (H_{τ|Q} = G_τ);
  LEV_C(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of H_C with ≤ j edges from x to a cycle node of
  λ, defined at every state of the phase, LEV_C ≥ 0 there (N-FBC-1, REFEREE-2; checked by REFEREE) and non-decreasing along it; B_C(x) := the
  maximum of value(r) over the simple H_C-paths r from x to a cycle node of λ; 𝒞_f(P) := the configurations of the sources of P's in-phase S4c
  fallbacks; D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)} as in RESULTS R68 (P-N5-HON §0), and epochs / N_ep as in RESULTS R60, R61 (the packet imports them
  from P-N5-HONFF §0, which does not define them: FBC-N1 = N-FBC-3).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4c with FIX 3; RESULTS R15
  (a), (d) ((MON), and R15 (d)'s window applied to Ξ through RESULTS R57 (a) (VJ) under the standing premise 1E-N3, P1 (FBC-N2, REFEREE; the
  packet's "read as S1's Ξ" names no source)); R17 (a) (V1)/(V2), R17 (b) Lemma P's Case A with Ω := Ξ_t (RESULTS R70's Q-A, YES by both);
  R38 (a); RESULTS R70 (a) FB-RISE's proof, items 2-3 (Even vertices), used verbatim; for (a), (d) only RESULTS R61 (f):
  (a) Lemma FB-RISE_C: if t → t + 1 is an in-phase S4c fallback whose source t is a C-state, then LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1). Its
      Odd case uses no fallback and holds at every C-state (REFEREE); its Even case holds at any source state, the C-state hypothesis being
      needed only for the Odd case (N-FBC-2, REFEREE-2; accepted by REFEREE).
  (b) Lemma SAT_C: if t is a C-state with LEV_C(t) = n − 1, then Ξ_t = B_C; and if t < t′ are C-states of the phase with LEV_C(t) = n − 1, then
      Ξ is constant on t, …, t′ and t′ − t ≤ 4n(n − 1).
  (c) Theorem FB-C: in every phase P, f ≤ |𝒞_f(P)|·(4n² − 3n) (per C: at most n − 1 unsaturated and 4n(n − 1) + 1 saturated fallback sources).
  (d) Corollaries: (a) f ≤ (4n² − 3n)·min(N_ep(P), Π_{q ∈ Q} deg(q)); (b) on 𝒞^kO with maximum out-degree Δ, f ≤ Δ^k(4n² − 3n) per phase;
      (c) if every state of P has |D_k| ≤ 1, f ≤ (1 + m)(4n² − 3n), and the configurations with |D| ≤ d number at most
      Σ_{j ≤ d} C(|Q|, j)(Δ − 1)^j; (d) with RESULTS R61 (f), f ≤ (4n² − 3n)(1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)) (the inequality; the
      comparison sentences after it are READINGS, FBC-N4).
  Header claim CONFIRMED by both for n ≥ 2: (a)'s N_ep form and (d) are implied by RESULTS R60 (c) EPOCH (f ≤ 1 + n·N_ep; with R61 (f) for
  (d)), since 1 + n·N_ep ≤ (4n² − 3n)·N_ep ⇔ 1 ≤ 4n(n − 1)·N_ep; at n = 1, f = 0 (the only vertex has a self-loop only) (REFEREE; N-FBC-4,
  REFEREE-2). What FB-C adds over EPOCH is the per-configuration form: a configuration that recurs in the phase is paid once.
- Not signed (packet §3-§5): the τ-frame split and its DEAD charge (s4c8_n13, j5_n16); the data; the OPEN items (the number of distinct
  configurations per phase on general games; a better saturated term); the READINGs, including "incomparable with RESULTS R56", which is
  witnessed in one direction only (FBC-N4 = N-FBC-5: FB-C's number never beat R56's or EPOCH's in any phase either referee ran; max
  N_ep/|𝒞_f| = 45 at n = 32 against 4n − 3 = 125, REFEREE-2).
- Referee strengthening (NOT part of this entry): FBC-N3 (REFEREE's proof, checked line by line and accepted by REFEREE-2 in its §C): at most
  one saturated fallback per configuration and phase, via SAT_C (b), RESULTS R15 (b) through R57 (a), and RESULTS R38 (f) CN-LAST, so
  f ≤ n·|𝒞_f(P)|. The same statement is a lane statement in packet P-N5-EPC §3 (Lemma SAT-FB, Corollary SAT-FB1, Theorem FB-C′; l-new
  81ab0b72, sha1 9f48ded7, pinned), proved by the lane on its own route and in review; it lands, if at all, with that packet.
- Honest limits: (i) A REDUCTION: f is bounded by distinct configurations at fallback sources, which is not bounded here on general games
  (Π_q deg(q) in the worst case); for fixed k and bounded degree (b) is O(n²) per phase. (ii) The saturated term 4n(n − 1) + 1 is untested:
  at most 1 saturated source per (phase, configuration) in every set of both referees, longest saturated window 2 transitions (tog6b_n32);
  REFEREE-2's "≤ 1 saturated per C" control cannot bite (N-FBC-6; FBC-N3 proves why). (iii) Over-budget pairs: REFEREE-2 left 173 (phase,
  configuration) pairs undecided at budget 3·10⁶ (1,519 fallback sources skipped for the LEV_C checks); at 3·10⁷ its six worst named
  instances are decided except one configuration in each of ffin12_n32, rise_thin51_n40, zcl_rx_n32; REFEREE's n ≤ 34 row has 115 UNK
  phases. (iv) No running-time bound.
- Data (DATA, not proof): REFEREE (successor 15, own fbc_probe.py on its own engine; exact LEV_C by simple-path enumeration in H_C; lane code
  not run): 35,720 runs in its §4 table over the library at n ≤ 20 and n ≤ 34 (1,140 files), two random 𝒞^kO batches (k ≤ 4, k ≤ 8) and
  fr39_q4_n48, with 2,794 in-phase fallbacks checked exactly by FB-RISE_C out of 3,384 (the other 590 in the n ≤ 34 row's 115 over-budget
  phases); its §C's "36,720 runs, 3,394 FB-RISE_C checks" is an arithmetic slip, corrected by its erratum below the §C (referee ae36ce48;
  LEAD-N1); 0 failures of REAL, MONO, FBC, ODDC, SATB, SATW, THM, CORA, CORC; FLATLAST (FBC-N3) 951 Ξ-flat fallbacks, all end their
  phase; reproduces fr39_q4_n48 (39 fallbacks, 7 configurations, 24 unsaturated) and farrise25_n32 (25); mutations MUT=1 (G_τ frame) 79,
  MUT=2 (+2) 144, MUT=3 (S4c minimum) 15 and FLATLAST 8 failures. REFEREE-2 (successor 17, own fbc_check.py; lane code not run): 21,753
  runs (named instances, lib41, its 503 𝒞^1O files, random games with 2, 4 and all Odd choice vertices); 2,294 fallback sources checked
  exactly (1,637 unsaturated); 0 violations of every signed check, Case A in H_C 32,431,842 times; max f 37 in one phase (rise_fb38_n48,
  |𝒞_f| 1); controls plus2 298 and tau 14,399 failures (the honest frame is what makes the Odd case free).
- Signatures: REFEREE docs/referee/R-N5-FBC.md (referee 0addfc5f, §C d08011be, successor 15): FB-RISE_C, SAT_C, Theorem FB-C, Corollaries
  (a)-(d) SIGNED, no gap; header claim CONFIRMED for n ≥ 2; notes FBC-N1..N4. REFEREE-2 docs/referee-2/R2-N5-FBC.md (referee-2 aab45be6,
  §C bde1ea77, successor 17): the same items SIGN, no gap; header claim CONFIRMED for n ≥ 2; notes N-FBC-1..6. §C (both): verdicts identical;
  joint gap map empty; FBC-N1 = N-FBC-3, FBC-N4 = N-FBC-5, REFEREE's n = 1 remark = N-FBC-4; N-FBC-1, N-FBC-2 accepted by REFEREE; FBC-N3
  accepted by REFEREE-2 and explains N-FBC-6; nothing open. Both under the standing premise 1E-N3 (P1) and RESULTS R70's Q-A.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase reduction of f; no running-time bound). GAPS G-N5-TIME: open.
