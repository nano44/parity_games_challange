# Draft RESULTS R67 (Lead, 2026-10-26 10:59Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C76 (rev. 2026-10-26 11:18Z: C76 E-1..E-4, N-1..N-4) — LANDED in RESULTS Results 2026-10-26 11:33Z (CHECKER C76 Add. 1 9ebda4df PASS), after R66

### R67 [refereed-only] N5 on EVERY game, inside one fallback-free run S of one phase: CR-D's hypothesis (i) can be replaced by a per-edge order transfer (CR-REL); under (h3_D) on S the W/Ξ offset of a vertex is 0 or its gate's offset, a sum of ±2^r over the run's band, so its changes are at most (n − 1) + 2^{B+1} (OFFSET, MERGE-B, TWIN-GAP), and a block of aligned states is a switch-best block of G_τ, so S has at most N_split + (N_split + 1)(n + m − 1) transitions (PIECE_D, SPLIT-RED); and if only λ_W is constant on S (hypothesis (ii)), Lemma P's coarse lower bound holds whenever each Even edge of the path is unforbidden at its one scheduled state (P^c_sch, FRZ-SCH), so every coarse W-change after the first n − 1 states is charged to a forbidden edge (CHARGE), which points into the disagreement region (FZ) and is charged only if later switched into (UNF), giving at most (n − 1)(1 + |U(S)|) coarse W-changes per vertex per run (CHARGE-U) (2026-10-26) — structural lemmas and reductions for N5 beyond one Odd choice vertex (no count: the band B, N_split and the unforbid-switches U(S) are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C76.md, checker PENDING)
- Object (packet P-N5-RUND, added at l-si 762b7243, pinned trunk 94910ed3, unchanged during review): docs/si/P-N5-RUND-box17.md, sha1
  71e198f359cbb321fc0c15e6c28676d4dd046d52 (L-SI successors 12 (§2-§4) and 13 (§5, §6, assembly), Opus 5.5). The referees' notes are
  collected by the lane in docs/si/P-N5-RUND-fixes-box17.md (l-si 74e0375d, sha1 aa4a39201313ba9b34364fb82f76a95589edb828, L-SI successor
  14: the union of RUND-N1..N4 and N-RUND-1..7, a §7 status line; 36 quotes checked by script); on trunk; repairs only, no signed statement
  changes.
  Setting (every game): as in RESULTS R62 (state k; σ̄_k; Ξ_k; G_τ; W_k; λ_Ξ, λ_W; D_k; u(v); R_D, F_D; π_v; (h_D); (h3_D); lev, COARSE_L,
  (C1)-(C4) of RESULTS R25; M_D). A run S: consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no
  fallback); Ω_k := W_k; COARSE := COARSE_L, −1 ≤ L < ∞; (ii) := λ_W constant on S. An Even edge (x, z), a := σ_k(x), is FORBIDDEN at k (level
  L) if COARSE_L(W_k(z)) ≻_L COARSE_L(W_k(a)) but not Ξ_k(z) ▷ Ξ_k(a); SPLIT at k if [Ξ_k(z) ▷ Ξ_k(a)] ≠ [W_k(z) ▷ W_k(a)]; a state is ALIGNED if
  it has no split edge, N_split(S) := the transitions of S with a non-aligned source. Offsets: s^Ξ_k(v), s^W_k(v) := the signed weights
  w(P(·)) of the path sets (R25 (C3)), Δ_k(v) := s^W_k(v) − s^Ξ_k(v), δ_k(u) for u ∈ D_k; L* := max(max_S M_D, −1); U_S, ℓ_S as in the packet
  §3; B := L* − ℓ_S + 1. The SCHEDULE of a simple path r = (r_0, …, r_m) of G_τ to a W-cycle node at state k is CLEAN if k − m ≥ k_0 and no
  Even edge (r_q, r_{q+1}) is forbidden at state k − 1 − q. U(S) := the S4a switch events (k′, (y, z)) of S into an edge forbidden at some
  state of [k′ − n + 1, k′ − 1] ∩ S (UNFORBID-SWITCHES).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R62 (a)-(f) (setting,
  TC-CLASS, C2-H3, WM-G, P^c_L / CR-D, FRZ-U_H3), R55 (a), R25 (C1)-(C4) and (Cstrict), R17 (a) (F1), (c) Theorem PH, (d), R18 (d) Lemma S
  (c), R15 (a), (d) with (VJ) (RESULTS R57), R21 (a) XW; and the standing SPEC premise 1E-N3 (RESULTS R57) in two forms (N-RUND-1,
  REFEREE-2; accepted by REFEREE): P1, S1's σ̄_k is Odd's pointwise optimum in G_{σ_k} (used by FZ, and by OFFSET (a) and so TWIN-GAP); P2, S4a's σ_{k+1}
  is Even's pointwise optimum in its arena H_k (used by §2-§5 and by CHARGE-U, through WM-G and (F1) on H_k; REFEREE-2 §0: OFFSET (b), (c),
  MERGE-B and UNF need neither). The packet's "R19 (d) (SG)" quote is not
  verbatim; the fact OFFSET (a) uses is R15 (a) carried to SPEC's Ξ by (VJ) under P1 (RUND-N1 = N-RUND-2, both referees):
  (a) Lemma CR-REL: CR-D (RESULTS R62 (e)) holds with its hypothesis (i) replaced by EDGE ORDER TRANSFER at L at every state of S (no Even
      edge forbidden at L): under it and (ii), COARSE_L(W) is constant on S from state k_0 + n − 1 on.
  (b) Lemma OFFSET, under (h3_D) on S: (a) λ_Ξ = λ_W, constant on S, and s^Ξ, s^W are non-decreasing along S; (b) Δ_k(v) = 0 if v ∈ F_D or
      λ(v) ∈ π_v, otherwise Δ_k(v) = δ_k(u(v)); (c) every δ_k(u) is a sum of terms ±2^r with ranks r ∈ [ℓ_S, L*], so every offset on S is a
      multiple of 2^{ℓ_S}. Lemma MERGE-B: if λ(y) = λ(z) and Δ(y) = Δ(z), the two frames order the path sets of y and z the same way.
  (c) Theorem TWIN-GAP, under (h3_D) on S, with N_v := the transitions of S at which Δ(v) changes: (i) at such a transition with d :=
      Δ_{k+1}(v) − Δ_k(v), s^W(v) rises by ≥ d if d > 0 and s^Ξ(v) by ≥ −d if d < 0; (ii) at most (2^{L*+2} − 2)/2^{ℓ_S} < 2^{B+1} of them have
      source state ≥ k_0 + n − 1 (N-RUND-4); (iii) N_v ≤ (n − 1) + 2^{B+1}. Corollary: the terminal changes of v at which its offset changes
      are ≤ N_v. In (ii)'s proof each score's rise bound 2^{L*+1} − 1 is the width of the low-part range (RUND-N4, REFEREE).
  (d) Lemma PIECE_D: (a) at an aligned state, Iσ_k is G_τ's improving set and the S4a step is a switch-best step of G_τ (R17's rule, for
      SPEC's pointwise-optimal choice); (b) a block of consecutive transitions of S with aligned sources and λ_W constant has fewer than
      n + m transitions (m = m_τ ≤ m, N-RUND-3; R17 (c) applied to switch-best started mid-run, RUND-N3). Corollary SPLIT-RED, under (h3_D)
      on S: |S| ≤ N_split(S) + (N_split(S) + 1)(n + m − 1), |S| counting transitions (N-RUND-3).
  (e) Lemma P^c_sch, under (ii) only (not (i), not (h3_D)): if the schedule of r at k is clean, Ω^c_k(r_0) ⪰ COARSE(value(r)). Corollary
      FRZ-SCH: if the schedule at s of x's W-play prefix at t is clean, COARSE(W(x)) is constant on [s, t]; it contains CR-D and CR-REL.
      Corollary CHARGE (hypothesis (ii) only): every change of COARSE(W(x)) at s − 1 → s is a WINDOW change (s − 1 − m < k_0, so s ≤ k_0 + n − 1, at most n − 1 per
      x per run) or is CHARGED to an Even edge (r_q, r_{q+1}) of x's W-play prefix at s that is forbidden at state s − 2 − q.
  (f) Fact FZ (premise P1 only, with totality of ⊴, (Cstrict) and the definition of D_k; RUND-N2, REFEREE; no run, phase, S4a or (ii)
      hypothesis): a forbidden (x, z) has Ξ_k(z) ◁ W_k(z), so z's W-play meets D_k. Lemma UNF: a charged change is preceded by an S4a switch
      INTO the charged edge at some k′ with f < k′ ≤ s − 1 ≤ f + n − 1, at which the edge is not forbidden. Corollary CHARGE-U (hypothesis (ii)
      only): for every x the changes of COARSE_L(W(x)) on S number ≤ (n − 1)(1 + |U(S)|); U(S) depends on L, and U_L ⊆ U_{−1} (N-RUND-5).
- Not signed (packet §7-§9): the CONJECTURES FS and LC2 (OPEN) and the OPEN items (R1)-(R4); the
  dead CONJECTURES UF-ONCE (packet §7; REFEREE-2's side finding: so_th_n32, sha1 ae9126ad, reproduced by REFEREE; phase2_pk48, sha1 83dead9b;
  both reproduced by the lane) and PAIR-OC (packet §7; L-RED R81, pairoc_n58, sha1 4824c73c), and, outside the packet, U-SPLIT (lane note
  §17; L-RED R80, usplit_rd_s3_n27, sha1 1e9ca56d), all three recorded as DEAD in the fixes file's §7 status line, none of them a signed
  item; the §3 READING (polynomial only for a narrow band); the data.
- Honest limits: (i) Structural lemmas and reductions; no count. TWIN-GAP is exponential in the band B (B reaches 39 at n ≤ 48 in the
  lane's data (44 on lib41 in REFEREE's data, 155 at n = 192 in REFEREE-2's)); SPLIT-RED leaves N_split unbounded; CHARGE-U leaves |U(S)| unbounded, and |U(S)| = Θ(n) for one vertex in one run is
  realized (L-RED R82, mkgrow, DATA), so CHARGE-U's route gives at best order n² coarse W-changes per vertex per run. (ii) The lane's
  reduction of stretch boundaries to ρ, epochs and gate W-changes (docs/si/N5-RUND-box17.md §20) and the relay-cycle obstruction (§22) are
  lane work after the packet, not part of this entry. (iii) Thin data (N-RUND-6 and REFEREE's thin-data bullets): CR-REL's own hypothesis
  held only 3-5 times in REFEREE's samples and 12 CR-REL freezes are non-vacuous in REFEREE-2's; the TWIN-GAP (ii) and PIECE_D (b) bounds
  are slack in all data (max tail rise 38 % of its cap; longest aligned block 55 against n + m_τ = 300) and the mutations tg4, tgr and piece
  do not bite; the exhaustive P^c_sch check ran only on small games, where nothing is charged; REFEREE's probe skips runs where λ_W changes,
  so CHARGE-U on so_th_n32's sub-run is REFEREE-2's check only, and there it holds through the window term alone (the run has 21 < n − 1
  transitions); the U-term is exercised elsewhere (REFEREE-2: 15,314 charged changes).
- Data (DATA, not proof): REFEREE (successor 13, own rund_probe.py, every L in {−1, …, n − 1}, suffix runs on the long instances; lane code
  not run): 0 failures; long runs (frz1-3_n24 with their starts, pftheta34_n32): 9.9M FRZ-SCH pairs, 47,413 charged changes, 57,867 UNF
  checks, max |U| 7; lib41: 67M FRZ-SCH pairs, 65,201 charged changes, 70,546 UNF checks; 6,000 random games with exhaustive P^c_sch for
  n ≤ 7; controls MUT=1 and MUT=2 fail (78,800 / 405,240). REFEREE-2 (successor 16, own rund_check.py with Ξ and W as play values; lane
  code not run): 20,254 N5 runs (90,290 states), 0 violations, including about 5.4M P^c_sch clean checks (random paths seeded by a salted hash; not exactly reproducible), 15.4M FRZ-SCH checks, 17,088 UNF and
  566,623 FZ checks; brute force on small arenas: P1 at 31,001 states, P2 at 24,910 transitions; mutations shift, noforb, fz, unf, chu0 and
  crrel1 bite; CHARGE-U on so_th_n32 states 1-22: 29,696 checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-RUND.md (referee 29846bca, §C 62a1a01d, successor 13): §2-§6 SIGNED, no gap; notes RUND-N1..N4.
  REFEREE-2 docs/referee-2/R2-N5-RUND.md (referee-2 7a02a1f2, §C 2c8c17c6, addendum ac7e80e9 (merged at e8d31c47) correcting its §C header to REFEREE's §C
  62a1a01d and adding the so_th_n32 CHARGE-U check, successor 16): all 14 items SIGN, no gap; notes N-RUND-1..7. §C (both): verdicts
  identical, all 14 items signed by both; joint gap map empty; RUND-N1 = N-RUND-2; RUND-N2, N3, N4 accepted by REFEREE-2; N-RUND-1, 3, 4, 5
  accepted by REFEREE; N-RUND-6, 7 agree with REFEREE's thin-data bullets and §4 checks; nothing open on the signed items (REFEREE §C: outside them, §7's route to |U(S)| ≤ n_E via UF-ONCE is closed and needs another argument).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and reductions; no running-time bound). GAPS G-N5-TIME: open.
