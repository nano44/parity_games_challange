# N5-ELIM (box 93): CONJECTURE ELIM-WIN (L-LIT T58) is EQUIVALENT to polynomial W-runs (Lemma ELIM-EQ, lane), so it is another face of XI-CH-POLY, not a smaller target. The contraction-free route (BETA-MON + ELIM-ORD-β + "Ξ rises every step" + XI-RUN) is DEAD as a proof route: VJ switch-all on switchallexp_N keeps all four and has HW = 5·2^(N−1) − 5. Any proof must use S4a's arena optimum (R140), and through GP* that leads back to R*_F and FL_F
L-NEW successor 39 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 17:50Z: «BOX 93 = CONJECTURE ELIM-WIN on the proof side … prove
HW_F ≤ p(n), or give the exact obstruction with an instance … ask whether S4a's arena optimum (ARENA-MAX, R140) plus XI-RUN / SEG-XCH give a
contraction-free argument: some non-final edge's β-gap must close within poly(n) steps because Ξ rises somewhere every step (XI-RUN);
ELIM-ORD-β then makes the elimination permanent.» Written 2026-10-30 17:52Z-17:54Z (date -u). Working note, unrefereed. Labels: PROVED (lane) /
CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources and definitions
- L-LIT T58 (l-lit d78e1815, docs/lit/T58-action-elimination.md §3-§4; read in full): β_t(v) := Ξ_t(σ_t(v)); Lemma BETA-MON (β never falls in a
  W-run); Lemma ELIM-ORD-β («If β_t(v) ⊵ Ξ_end(w) for some t in F, then (v, w) is not adopted at any s ≥ t in F»); «HW_F(t) := min over the
  edges e ∈ σ_t with e ∉ σ_q of (the last state at which e ∈ σ) + 1 − t. HW_F := max_t HW_F(t)» (F = [p, q]; states with σ_t = σ_q are
  skipped); «Counting (PROVED, as HMZ Thm 6.5). |F| ≤ (m_E + 1)·HW_F»; «CONJECTURE ELIM-WIN: HW_F ≤ p(n) for every W-run F of N5». HMZ =
  Hansen-Miltersen-Zwick arXiv 1008.0530 (opened by L-LIT, not by me; nothing from it is used here beyond T58's quotes).
- P-N5-WRUN (l-new 7668bc9b; signed by both referees, lines L-1/L-2 in docs/new/P-N5-WRUN-fixes-box92.md): Theorem XI-RUN, Lemma RET-ΞRISE,
  Corollary WRUN-EQ (WRUN-POLY ⇔ XI-CH-POLY ⇔ … ⇔ R*-POLY ∧ FL-POLY). L-RED R140 (l-red 47000632): ARENA-MAX, hybrid V0 / V1 / V2 table.
- Notation: a W-run F = [a, b] of N5 (RESULTS R89); m_E, n_E as in P-N5-WRUN §1. An Even edge e = (v, w) is HELD at t if σ_t(v) = w;
  NON-FINAL at t if held at t and σ_b(v) ≠ w; RETIRED at last(e) + 1 where last(e) is the last state of F at which e is held (if that is < b).

## 1. Lemma ELIM-EQ (PROVED, lane): ELIM-WIN ⇔ WRUN-POLY (⇔ XI-CH-POLY by P-N5-WRUN row E1)
- Statement. For every W-run F = [a, b] with b > a: (i) HW_F ≤ |F|; (ii) |F| ≤ (m_E − n_E)·HW_F ≤ (m_E + 1)·HW_F. Hence CONJECTURE ELIM-WIN
  ⇔ WRUN-POLY ⇔ XI-CH-POLY.
- Proof. (o) σ does not repeat in F: every transition of F applies Switch_I with ∅ ≠ I ⊆ Iσ (P-N5-WRUN Fact STEP-SW, RESULTS R15 (d)), and
  RESULTS R15 (c) says no strategy repeats under non-empty improving switches. So σ_t ≠ σ_b for every t < b, and every t < b has a non-final
  edge.
  (i) For t < b and a non-final edge e of σ_t, last(e) ≤ b − 1 (e is not held at b), so HW_F(t) ≤ last(e) + 1 − t ≤ b − t ≤ |F|.
  (ii) Put t_0 := a. Given t_j < b, some non-final edge e_j of σ_{t_j} has last(e_j) + 1 ≤ t_j + HW_F; put t_{j+1} := last(e_j) + 1. The
  retired edges e_0, e_1, … are distinct (an edge is never held after last(e)) and each is non-final, so at most m_E − n_E of them exist
  (every Even v keeps one final edge). The t_j strictly increase by at most HW_F, and the process stops only at t_j = b. So
  |F| ≤ (m_E − n_E)·HW_F. (This is T58's counting with the constant tightened.) □
- Consequence (READING). ELIM-WIN is not a new, smaller target: proving it is proving polynomial W-runs. HW is a useful MEASURE (it was
  linear, m + 1, on fx_K_m where per-edge returns are quadratic), but a proof of HW ≤ p(n) is exactly as hard as XI-CH-POLY.

## 2. Lemma REVISIT (PROVED, lane): in a window without retirement, every digit returns
- Statement. Let t < b and T := HW_F(t) − 1. Every Even v holds σ_t(v) at some state ≥ t + T. So every Even v that switches in [t, t + T)
  returns to σ_t(v) after its first leave in the window, and for each such leave s → s + 1 and the next return k → k + 1 (k ≥ s + 1),
  Ξ_k(σ_t v) ▷ Ξ_s(σ_t v).
- Proof. If σ_t(v) = σ_b(v), it is held at b ≥ t + T. Otherwise (v, σ_t v) is non-final at t, so last + 1 − t ≥ HW_F(t), i.e. last ≥ t + T.
  The Ξ-rise is P-N5-WRUN Lemma RET-ΞRISE (§5.1) for the return to σ_t(v). □
- So a long elimination window is literally «a counter where every digit returns» (T58 §4, L-RED's R144 aim), each return paid by a strict
  Ξ-rise of the digit's σ_t-target. The rises are per vertex: this is XI-CH-POLY again.
- DATA (box93/elimwin.py, REVISIT = switching vertices of the maximising window that hold σ_t(v) again later): every switching vertex of
  every maximising window returns (by the lemma); max REVISIT 46 (runfam_K40, n 79, HW 45, |F| 159).

## 3. DEAD (as a proof route): the contraction-free argument. Instance: VJ switch-all on switchallexp_N
- The route proposed: (a) BETA-MON, (b) ELIM-ORD-β, (c) Ξ rises somewhere at every step, (d) XI-RUN / SEG-XCH (each return pays a Ξ-rise
  of its target) ⇒ some non-final edge's β-gap closes within p(n) steps ⇒ HW ≤ p(n).
- Why (a)-(d) cannot suffice. Their proofs use only: every step applies a non-empty set of Ξ-improving switches (Iσ), Ξ is pointwise
  non-decreasing (R15 (a)), and SUCC-MON (same reason). These hold in EVERY Vöge-Jurdziński strategy-improvement run against Odd's optimal
  counterstrategy, whatever the selection rule. With Ξ_end := the final valuation of the run and F := the whole run, T58's definitions
  read verbatim.
- Instance (box93/swall_hw.py: L-RED R140 hybrid.py V0 = PGSolver's switch-all rule on L-SI's engine; games by
  experiments/hard-families/pgsolver_port.py switchallexp N, L-COMP's byte-identical port; best-reward start):

  | N | n | m_E | iterations | BETA-MON viol. | ELIM-ORD-β viol. | steps with Ξ unchanged | HW | |run| ≤ (m_E + 1)·HW |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 49 | 89 | 70 | 0 | 0 | 0 | 15 | yes |
  | 4 | 63 | 117 | 150 | 0 | 0 | 0 | 35 | yes |
  | 5 | 77 | 145 | 310 | 0 | 0 | 0 | 75 | yes |
  | 6 | 91 | 173 | 630 | 0 | 0 | 0 | 155 | yes |
  | 7 | 105 | 201 | 1243 | 0 | 0 | 0 | 315 | yes |

  HW = 5·2^(N−1) − 5 for N = 3..7 (n = 14N + 7): exponential in n. (a), (b), (c) hold with 0 exceptions; (d) holds by its proof (R86
  SW-RETURN uses only (F-MON), (F-SW) and S2, all true for switch-all). The iteration counts equal R140's V0 column (70, 150, 310, 630).
- Exact obstruction. (a)-(d) say that Ξ moves and that each return is paid by SOME Ξ-rise of the returned-to target. Nothing in them
  limits how many Ξ-rises one target can have: on switchallexp the bit vertices' targets rise exponentially often (lexicographic counter,
  P-N5-WRUN §13 / [FFSS]). A "β-gap closes in p(n) steps" statement is a contraction, and (a)-(d) contain none (T58 §2: (C) missing).
- What survives. R140's V1 column (S4a's arena optimum against σ̄, otherwise the same loop) is linear on the same games (8, 8, 10, 12, 14).
  So the property that switch-all lacks and N5 has is ARENA-MAX (and inside a W-run, τ fixed). A proof of ELIM-WIN must use it.

## 4. What ARENA-MAX gives inside a W-run, and where it stops (READING with one exact pointer)
- ARENA-MAX + τ fixed is RESULTS R88 GP* on W-runs (R89 GP*-RUN): W is a Bellman-Ford climb in G_τ, n − 1 W-changing transitions per
  "epoch" between late adoptions of blocked edges (FW-R*). In HMZ terms this IS a contraction, in W: within n − 1 steps W reaches the arena
  optimum. It does not transfer to Ξ (the valuation offers and retirements are judged by) because Ξ ⊴ W with a gap carried by Odd deviations
  (P-N5-WRUN GAP-DEV).
- So ARENA-MAX bounds the W-changing part of every window by (n − 1)(R*_window + 1) ([SUB], two referee signatures in P-N5-WRUN) and leaves
  R* and FL: exactly P-N5-WRUN row E4. The elimination window adds no handle beyond E4. The open quantity is unchanged.
- CONJECTURE ELIM-WIN stays OPEN (equivalent to WRUN-POLY). No instance with super-linear HW in N5 is known.

## 5. DATA (box93/elimwin.py; corpus = box 83's lists, 1132 runs, 1692 W-runs; elimwin_sbcg.txt, elimwin_alt.txt)
- Counting |F| ≤ (m_E + 1)·HW_F: 0 violations. ELIM-EQ (i) HW_F ≤ |F| + 1: 0 violations.
- Max HW 45 (si/runlin/instances/runfam_K40.pg, n 79, |F| 159; RUN-LIN's killer family): HW / n ≈ 0.57. Pins: fx_K8_m32 HW 33 (|F| 280),
  latew_K16_m32 HW 33 (|F| 560), pftheta34_n32 HW 7 (|F| 34).
- Retired edges certified by ELIM-ORD-β at the end of their W-run (β_b(v) ⊵ Ξ_b(w)): 27,035; NOT certified: 494 (e.g.
  n5-epoch/instances/nconf61_n48.pg: 12 of 145). So ELIM-ORD-β is a sufficient, not a necessary, sign of retirement: some retired edges are
  still Ξ-improving at the last state of their W-run (the W-run ends by a τ- or λ_W-change before they would be re-offered). An
  ELIM-ORD-β-certified window would be a strictly stronger CONJECTURE than ELIM-WIN; not pursued.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box93/elimwin.py (HW, counting, REVISIT, certification), swall_hw.py (switch-all control), run.sh,
  elimwin_sbcg.txt, elimwin_alt.txt; check.sh section "box 93"; this note.
- FINDINGS:
  1. PROVED (lane) Lemma ELIM-EQ: HW_F ≤ |F| and |F| ≤ (m_E − n_E)·HW_F, so CONJECTURE ELIM-WIN ⇔ WRUN-POLY ⇔ XI-CH-POLY. Not a smaller target.
  2. PROVED (lane) Lemma REVISIT: in a window shorter than HW_F(t) every switching Even vertex returns to σ_t(v), each return paid by a
     strict Ξ-rise of σ_t(v) (RET-ΞRISE).
  3. DEAD (proof route): BETA-MON + ELIM-ORD-β + "Ξ rises every step" + XI-RUN cannot prove ELIM-WIN. VJ switch-all on switchallexp_N
     satisfies all four (0 exceptions) with HW = 5·2^(N−1) − 5 (N 3..7, n = 14N + 7). A proof must use ARENA-MAX (R140 V1 linear there).
  4. READING: ARENA-MAX inside a W-run is GP*'s W-contraction. It bounds the W-changing part of a window and leaves R* and FL (WRUN row E4).
     ELIM-WIN adds no handle. CONJECTURE ELIM-WIN OPEN; max HW 45 (runfam_K40, 0.57n).
  5. DATA: 494 retired edges are not ELIM-ORD-β-certified at the end of their W-run (nconf61_n48 and others).
- NEEDS: none from the owner. Lead: L-RED's R144 target (every digit returns) is exactly Lemma REVISIT's window. The instance to beat is
  runfam_K40 (HW 45 at n 79).
