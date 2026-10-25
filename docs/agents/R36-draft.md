# Draft RESULTS R36 (Lead, 2026-10-25 13:10Z by date -u) (rev. 13:31Z: addendum 5c29d93d §3 cited; reading aligned) — to CHECKER C45 — LANDED in RESULTS Results 13:52Z (CHECKER C45 3667fb1c PASS), after R35

### R36 [refereed-only] The one-player premise (P) holds: in a one-player game a positional Even strategy with no improving edge is optimal (Lemma P1, via a set/multiset bridge, Lemma B), which discharges R18's G-1OA-4 (2026-10-25) — a lemma used by N5's analysis (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C45.md, checker PENDING)
- Object (packet P-N5-P1, added at l-si 6ba9a69, pinned trunk 48a8a4c, unchanged during review): docs/si/P-N5-P1-box10.md, sha1
  b98ca7941264affe4bfe79cb72b744d2ab158e07 (L-SI successor 5, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-P1-fixes-box10.md (l-si d2701d8, sha1 83ef83b0e3a9c2df7c76d8d6f8096564db0618bf, L-SI successor 6: N-P1-1; REFEREE's §5
  correction) and docs/si/P-N5-RL-P1-addendum-box10.md §3 (l-si f5b39de, sha1 5c29d93d54f133edd4a8fb9e43c331067b8c6b2e: P1's joint
  state); on trunk; repairs only.
  Setting: SPEC S1 (VJ00 play values (c, P, ℓ) and Even's order ⊴, with lengths at cycle nodes), S2 (improving edge). A ONE-PLAYER game
  is a game in which every non-Even vertex has one successor. V_σ is the play valuation of a positional Even strategy σ.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma B: the extended order on path MULTISETS (lexicographic on signed multiplicity vectors, then length by the parity of the
      cycle node) is a total order; on sets it coincides with SPEC S1's order; real play values are sets (the play is simple before its
      first visit of the cycle node). Multisets occur only inside chains whose two ends are real values.
  (b) Lemma M: prefixing x ⊕ · is strictly monotone in the extended order.
  (c) Lemma P1 (Steps 1-6): if σ is a positional Even strategy of a one-player game H with no improving edge (no Even edge (x, y) with
      V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v. Corollary P1′: V_σ is then
      the pointwise maximum over positional Even strategies (R17 F1's W*). The trivial cases m = 0 in Step 4 and b = 0 in Step 6 are
      named in the fixes file (N-P1-1, wording, closed).
  (d) Hypothesis match: R18's premise (P) ("CONDITIONAL on (P) for one-player games (G-1OA-4, open by design): VJ00 Lemma 5.8 '1 ⇒ 2',
      used only in Lemma 1 on G[X]") and P-N5-RL §0's (P) are exactly the statement of Lemma P1 on the one-player games G[X], G_τ and
      G_τ[F_k]. So R18's condition G-1OA-4 is discharged.
- Reading (both referees, not signed as such): P1 discharges (P) for one-player games only. It does NOT discharge the two-player VJ00
  Lemma 5.8 (R15's G-N5T-3). For P-N5-RL (in review) it removes the (P) condition from BL (b), (c), (e), FREE-FREEZE, EV, EV+ and
  TEV-RED′; the packet's original TEV-RED stays NOT SIGNED as stated (RL-1 is independent of (P)); EQ-END keeps
  its CN-LAST condition (REFEREE §5 correction).
- Honest limits: (i) one-player games only. (ii) This entry discharges a premise of R18; it adds no bound on N5's running time.
- Data (DATA, not proof): REFEREE p1_probe.py (own engine): 8,000 random one-player games (n ≤ 13), every positional strategy
  enumerated, 9,083 improvement-free strategies, 0 violations of P1; control: 266,806 strategies with an improving edge are non-optimal;
  ~2.35 M order / Lemma B / M pairs, 0 failures. REFEREE-2 (own code): 28,973 one-player games, 1,030,157 strategies, 0 violations;
  Lemma B against SPEC S1 on 46,356,800 real-value pairs, 0 mismatches; mutation tests (a flipped odd rule; a coarse "improving" without
  lengths) fail as expected. Lane: p1check.py, 136,286 strategies, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-P1.md (referee 58a5b73, successor 8; §C 5f52510): Lemma B (a)-(c), Lemma M, Lemma P1 (Steps 1-6)
  and Corollary P1′, §4 hypothesis match SIGNED; no gaps. REFEREE-2 docs/referee-2/R2-N5-P1.md (referee-2 e036e4c, successor 8; §C
  88571b0): Lemma B, Lemma M, Lemma P1, §4 SIGN; note N-P1-1. §C: no verdict differs.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
