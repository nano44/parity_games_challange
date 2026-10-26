# Draft RESULTS R59 (Lead, 2026-10-26 06:17Z by date -u; both §Cs and the fixes file filled) (rev. 2026-10-26 06:34Z: C68 N-1, N-2) — to CHECKER C68 — LANDED in RESULTS Results 2026-10-26 06:34Z (CHECKER C68 cf48d915 PASS), after R58

### R59 [refereed-only] N5 on EVERY game: after j in-phase fallbacks, the honest κ-values of every honest class are at least the j-step value of that class's min-max reachability game (Lemma VI-LB), i.e. every in-phase fallback is at least one round of value iteration on it (2026-10-26) — a LOWER bound on progress (no count of fallbacks, S4a steps, crossings or phases; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C68.md, checker PENDING)
- Object (packet P-N5-VILB, added at l-new 999e73f4, pinned trunk e7febdc2, unchanged during review): docs/new/P-N5-VILB-box44.md, sha1
  872d4400194ed9d0f6ad9f6a2cc82f2f0821cd9f (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-VILB-fixes-box44.md (l-new 1c344659, sha1 56da789eb295591dada219db9eab41358583211b, L-NEW successor 24: VILB-N1 = N-VILB-1,
  N-VILB-2, VILB-N2 data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; phases as in RESULTS R38 (a); an in-phase transition is an S4a step or an Even S4c fallback; g_1
  < g_2 < … the in-phase fallbacks ("t > g_0" means every state); next_t(v) := σ_t(v) for Even v, σ̄_t(v) for Odd v; for a cycle node c
  of the phase, U_c := λ^{-1}(c); wt_c, s_c, κwt_c and κ_t on U_c as in RESULTS R56. The game Γ_c: vertices U_c; at an Even vertex the
  maximiser and at EVERY Odd vertex the minimiser choose a successor inside U_c; target c with value (0, 0); a play pays the sum of κwt_c
  over its vertices before c, and −∞ if it never reaches c. Val^{≤0}_c(c) := (0, 0), Val^{≤0}_c(z) := −∞ for z ≠ c; for j ≥ 1,
  Val^{≤j}_c(c) := (0, 0) and Val^{≤j}_c(z) := κwt_c(z) + max (Even z ≠ c), respectively min (Odd z ≠ c), over x ∈ succ(z) ∩ U_c of
  Val^{≤j−1}_c(x). For z ∈ U_c ∖ {c} the empty-set conventions of the packet never fire, since by (Aκ) succ(z) ∩ U_c ≠ ∅ (VILB-N1 =
  N-VILB-1, both referees).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R17 (a) (V1), R15 (a),
  R38 (a), SPEC S1, S2, S4c (FIX 3):
  (a) Facts (Aκ), (M1κ), (M2κ) and Lemma κ-FB-ROUND (at an in-phase fallback k → k+1, for every Even v ∈ U_c ∖ {c} and every successor
      x ∈ U_c of v, κ_{k+1}(v) ≥ κwt_c(v) + κ_k(x)), restated with proofs as in RESULTS R48 / R56 (a) with c for c_θ.
  (b) Lemma VI-LB: for every phase, every cycle node c of it, every j ≥ 0, every state t of the phase with t > g_j and every z ∈ U_c,
      κ_t(z) ≥ Val^{≤j}_c(z). The Odd step uses only (Aκ) at t and the induction hypothesis at t, for choice and forced Odd vertices
      alike (N-VILB-2, REFEREE-2; the same step in REFEREE's report).
- Not signed (packet §2 remark, §3, §4): the relation to R48's κ-HAT-FREEZE (a) (an agreed READING: VI-LB is its two-player form); what
  VI-LB does not give (no upper bound κ_t ≤ Val_c, hence no freeze; no count; no claim that N5 does one VI round per fallback; values over
  walks vs N5's simple-path values); the cross-field reading via [BGHM] (T. Brihaye, G. Geeraerts, A. Haddad, B. Monmege, arXiv:1407.5030v4,
  §3 Algorithm 1, Theorem 1 item 4: value iteration on min-cost reachability games is pseudo-polynomial, exponential with 2^rank
  weights; source opened by the lane, sha256 in notes/L-NEW.md) and the obstruction shape (Figure 2(a) mirrored into U_c). The
  obstruction did not materialise: built as N5 games, the gadget collapses to ≤ 1 iteration and 0 fallbacks from every start pair (L-RED
  docs/red/R76, l-red 2207620f, instances bghm_k1_gap6_A, bghm_k3_gap4_A; DATA), a READING consistent with the lane's Lemma ACCEL (RESULTS R60;
  positional simple-path values; R76 §2).
- Honest limits: (i) A LOWER bound only: it bounds no count of anything, and it does not make f polynomial. (ii) The regime where it
  could force a count (many fallbacks in one phase) is not reached in any data (max 33 in-phase fallbacks in lib41, 37 in REFEREE-2's
  𝒞^1O files; never ≥ n).
- Data (DATA, not proof; VILB-N2): REFEREE (successor 12, own vilb_probe.py): 7,151 runs, 20,531 phases, 777,048 VI-LB checks, tight at
  61,861 of 105,188 finite lib41 checks (59 %), 0 failures; mutation oddmax (Odd maximises) fails 46,067 times. REFEREE-2 (successor 13,
  own va_check.py): 70,288 runs (incl. 47,996 climb runs), 161,847 phases, 2,677,247 VI-LB checks, 0 violations; the control "one round
  too many" (Val^{≤j+1}) fails 774 times on lib41, so the bound is attained at round j in data.
- Signatures: REFEREE docs/referee/R-N5-VILB.md (referee dcb1451c, successor 12; §C 09b5dbf5): §1 and VI-LB SIGNED; notes VILB-N1, VILB-N2;
  no gap. REFEREE-2 docs/referee-2/R2-N5-VILB.md (referee-2 f0e82d8a, successor 13; §C 5ad79417, successor 14): all SIGN; notes N-VILB-1,
  N-VILB-2; no gap. §C (both): verdicts identical; joint gap map empty; VILB-N1 = N-VILB-1; the Odd step = N-VILB-2; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a lower bound on progress; no running time). GAPS G-N5-TIME: open.
