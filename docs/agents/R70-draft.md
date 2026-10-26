# Draft RESULTS R70 (Lead, 2026-10-26 13:50Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C79 (rev. 2026-10-26 14:14Z: C79 E-1, N-1..N-3)

### R70 [refereed-only] N5 on EVERY game: an in-phase fallback is a Bellman-Ford step of the honest valuation, so across it the level LEV reaches min(LEV + 1, LEV_odd, n − 1), a rise unless an Odd vertex's own level binds or LEV is saturated (Lemma FB-RISE (a)), and after a W-honest state h it reaches min(LEV(h) + 1, n − 1) (FB-RISE (b)); hence in every phase the W-honest states number at most 4n² − 3n (Theorem HON-FF), with no fallback term, and so do the D = ∅ states, the D = ∅ epochs and the in-phase transitions whose source lies in a D = ∅ epoch (HON-0-FF), and the {u}-intervals of a phase number at most 1 + (4n² − 3n) + X_dir + X_big (REC-1-FF (a)); as IMPLICATIONS from premise (Στ), the |D| = 1 part of a phase is bounded by REC-1-FF (c), (d) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (the D = ∅ part of every phase is free of f; f itself, X_dir, X_big and |D| ≥ 2 epochs are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C79.md, checker PENDING)
- Object (packet P-N5-HONFF, added at l-new 2fca63b8, pinned trunk 4a0a8aba, unchanged during review): docs/new/P-N5-HONFF-box47.md, sha1
  98101d1fe723a570f3c79085b929a456ebb7dff5 (L-NEW successor 26, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-HONFF-fixes-box47.md (l-new b2dcf365, sha1 ccc520dd83c9086b57a2417c1cdcede44e7b7865, L-NEW successor 27: HONFF-N1..N3,
  N-HONFF-1..4, the independence addendum; 45 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R68 (N5 = SPEC S1-S5; Ξ_k the value of the honest play (σ_k, σ̄_k); W_k := V_{σ_k,τ_k}; phases; W-HONEST
  states; LEV(k) the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of G_τ with ≤ j edges to a cycle node of λ;
  f_in, X_dir, X_big, T*_Q). LEV_odd(k): the same with x ranging over the Odd vertices only, so LEV(k) ≤ LEV_odd(k).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4c with FIX 3; RESULTS R15
  (a), (d) ((MON)); R17 (a) (V1)/(V2), R17 (b) Lemma P's Case A; RESULTS R68 (HON, its step 1 for fallback-free gaps, and the Odd-case argument
  of SAT0's proof (b), with the wording of R68 (b)); the standing SPEC premise 1E-N3, FB-RISE using P1 only (through (MON)) and HON-FF P1 and
  P2 (P2 only through HON's step 1) (N-HONFF-2, REFEREE-2; accepted by REFEREE). The packet's premise list names XW, which HON-FF does not use
  (N-HONFF-1, REFEREE-2; checked by REFEREE); and it cites "SAT0's Odd case" where the Odd-case argument of SAT0's proof is meant, SAT0's
  hypothesis need not hold at h (HONFF-N1, REFEREE = REFEREE-2 §1 (b)):
  (a) Lemma FB-RISE: let t → t + 1 be an in-phase S4c fallback and j := min(LEV(t) + 1, LEV_odd(t), n − 1). (a) (general form) LEV(t + 1) ≥ j.
      (b) (honest form) If h ≤ t is a W-honest state of the phase, then LEV(t + 1) ≥ min(LEV(h) + 1, n − 1).
  (b) Theorem HON-FF: in every phase P of N5, the W-honest states number at most 4n² − 3n.
  (c) Corollary HON-0-FF: in every phase, (a) the D = ∅ states, (b) N_0, the epochs with D_E = ∅, and (c) the in-phase transitions whose
      source lies in a D = ∅ epoch each number at most 4n² − 3n. Against RESULTS R66 (REC-0): (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) =
      f(n + 1) + 2 > 0 for every f ≥ 0, n ≥ 1 (checked by both referees).
  (d) Corollary REC-1-FF (a): the {u}-intervals of a phase, over all u ∈ Q, number at most 1 + (4n² − 3n) + X_dir + X_big.
  (e) IMPLICATIONS from (Στ) (signed as implications; both referees note that they hold at RESULTS R65's audit strength): REC-1-FF (c) the
      |D_k| = 1 states, and the epochs with |D_E| = 1, number at most (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2); (d) if every state of the
      phase has |D_k| ≤ 1, the phase has at most (4n² − 3n) + (1 + 4n² − 3n + X_dir)·(T*_Q + 2) states.
  Q-A (the packet's question to the referees), answered YES by both, with the same list: Lemma P's Case A (A1, A2) with Ω := Ξ_t reads only
  facts about the value of a single play of a positional strategy pair (the Case-A non-improvement inequality from S2, the bound at the
  suffix from LEV(t), (V1) with the path to the cycle node avoiding x, (V2), and the own-cycle-node facts), so it holds for the honest
  valuation and needs no optimality premise; A1's last link via (F2) is replaced by (MON).
- Not signed (packet §3, §4): the data; §4's READING (f on general games is not bounded here: a fallback with LEV_odd(t) ≤ LEV(t) need not
  raise LEV; fallbacks with no W-honest state before them are not touched by (b)).
- Honest limits: (i) The D = ∅ part of each phase is free of f; f itself, X_dir, X_big and the |D| ≥ 2 epochs are not bounded here (lane work
  after the packet, P-N5-FBC, under review, bounds f by distinct configurations; not part of this entry). (ii) (e) needs T*(G^u), polynomial
  but very large (RESULTS R51 (a)). (iii) Thin decisive data (N-HONFF-3, both referees): exact LEV was reached on 5 of the 6 known gaps
  with a fallback inside (j7_n32 stays over budget on both engines, REFEREE-2 even at 1.5·10⁸ paths per phase); REFEREE verified 10 inside
  fallbacks exactly, with 7 phases over budget. The "no Odd term" control fails, always where LEV_odd binds (both referees; "always where LEV_odd binds" is REFEREE's observation), so the Odd term
  in (a) is needed.
- Data (DATA, not proof): REFEREE (successor 14, own ff_probe; lane code not run): 0 failures in 23,129 phases (the packet's six
  inside-gap instances with their starts, lib41 n ≤ 20, random games n 5-12, 9,000 runs); max 18 W-honest states in a phase; the "+2"
  mutation bites (5). REFEREE-2 (successor 16, own honff_check.py; lane code not run): 0 violations; FB-RISE (a) exercised at 1,642
  in-phase fallbacks (1,084 at non-honest states) in its sets (overlapping sets; its report §4); Case A checked pointwise 661M+ times, 0 failures; mutations
  ctrl and b2 bite (b2 once).
- Signatures: REFEREE docs/referee/R-N5-HONFF.md (referee cce5ea5e, §C e7db1ab4, successor 14): all SIGNED, (e) as implications, no gap;
  Q-A YES; notes HONFF-N1..N3. REFEREE-2 docs/referee-2/R2-N5-HONFF.md (referee-2 05e7663c, independence addendum 1306c31e, §C 11e3cfb1,
  successor 16): all SIGN, (e) as implications, no gap; Q-A YES; notes N-HONFF-1..4. §C (both): verdicts identical; joint gap map empty;
  N-HONFF-1, N-HONFF-2 accepted by REFEREE; HONFF-N1 = REFEREE-2 §1 (b); N-HONFF-3, N-HONFF-4 match REFEREE's data; REFEREE-2's independence
  addendum (it saw REFEREE's file name and commit subject, never the file, after its report was final) accepted by REFEREE, no effect;
  nothing open on the signed items. Both under the standing premise 1E-N3.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase bounds and reductions; no running-time bound). GAPS G-N5-TIME: open.
