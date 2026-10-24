# Draft RESULTS R18 (Lead, 2026-10-24 04:05Z by date -u) (rev. 04:15Z: signed object d78e54f per both referees' §C2; rev. 04:20Z: C27 E-2..E-4, N-1..N-3; rev. 04:29Z: Addendum 1 N-4, N-5) — LANDED in RESULTS Results 04:39Z (CHECKER C27 PASS + Addenda 1-3, checker 7a140bc; lines 3-end verbatim)

### R18 [refereed-only] N5 on o-acyclic one-Odd-choice games: fewer than (C_X + d)(B + 1) iterations from any start, conditional on (P) for one-player games; and Proposition X (2026-10-24) — a bound on the candidate N5 itself on a subclass that is polynomial by other means (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C27.md, checker b688c81 + Addenda 0638755, 46605bb, 7a140bc)
- Objects (packet P-N5-1OA, signed object = trunk d78e54f): (A) docs/red/R58-n5-width.md §9, Proposition X and Corollary X1 (L-RED
  successor 13, Opus 5.5; l-red f93e517); (B) docs/new/N5-1Oacyc-box24.md at l-new 8cc6aaf, the self-contained text (file sha1
  d35502679af112e9fa31eb3af99e64fb4afda1ba; L-NEW successor 8, Opus 5.5), with Lemma R and Lemma S of docs/new/N5-time-box21.md
  §2.1-§2.2. Both referees first reviewed the earlier sketch (trunk 07f298d, l-new 9d7890f), then re-checked d78e54f (REFEREE §0,
  REFEREE-2 §7) and signed it in §C2; verdicts are identical at both pins. N5 as specified in docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15).
  Source for (P): Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…), Lemma 5.8 "1 ⇒ 2".
- Setting: 𝒞^1O = games in which exactly one Odd vertex o has out-degree d > 1. X := the vertices with no path to o (so G[X] has no Odd
  choice), Y := V \ X, m_X := the number of edges inside X. o-acyclic := o lies on no cycle of the game graph. A transition of N5 is
  PURE if σ|X and τ are unchanged; a block is a maximal run of pure transitions; G_τ is the one-player game with Odd fixed to τ.
- Claims signed (both referees, both labelled "(Fable 5.1)"; the packet went to the two Fable referees by a Lead routing error against
  L37 (1), which has Fable sessions succeeded on Opus after their box; the signatures stand as two independent signatures on the more
  capable model, labelled as given):
  (a) Proposition X (any start pair, any 𝒞^1O game, o-acyclic or not): the sequence of distinct σ|X along N5 on G is a prefix of N5's
      run on G[X], and the whole run because N5 terminates (R15 (d)); so σ|X changes fewer than C_X := (|X|² − |X| + 1)(|X| + m_X) times.
      The strategy-level identity holds under SPEC's tie-breaks with G[X] keeping X's index order; the COUNT does not depend on
      tie-breaks (each change of σ|X is a pointwise optimum of G[X]'s arena or its terminal flat fallback, so R17 Corollary 1 bounds it).
  (b) Corollary X1 (signed as a reading, superseded by (c)): on o-acyclic 𝒞^1O, θ = Ξ(o) and w = W(o) change fewer than C_X times
      between changes of τ.
  (c) Theorem (conditional on (P) for the one-player game G[X]): on o-acyclic 𝒞^1O, N5 from ANY start pair makes fewer than
      (C_X + d)·(B + 1) iterations, B := (n² − n + 1)(n + m) (R17). Proof: Lemma 1, at a pure transition σ|X has G[X]'s optimal
      valuation (both cases; the flat case is R17's single-switch case analysis at an arbitrary state, proved in place in the d78e54f text; the pointer to R-N5-1P §4 G4 is the referees'); Lemma 2, θ = w
      at a pure transition (o-acyclicity is used here and only here); Lemma 3, Ξ = W at a pure transition, so the gate is G_τ's
      improving set and every block is a prefix of N5's run on the one-player game G_τ, shorter than B (R17 Corollary 2, which both
      referees confirmed holds from any start); non-pure transitions number at most C_X + d − 1.
  (d) Lemma R (box 21 §2.1): the order of the dual game G^d is the exact reverse of G's. Lemma S (box 21 §2.2) (a)-(b): (a) L_σ is the
      pointwise minimum of V_{σ,τ'} over Odd's strategies τ' and U_τ the pointwise maximum of V_{σ',τ} over Even's σ' (VJ00 (11) on G
      and on G^d); (b) L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run. Lemma S (c)-(d)
      (N5's arena step maximises V_{·,τ_k} over the arena, i.e. is a gated best response; comparison with SSI's step) hold for S4a
      steps only, not at S4c fallbacks (G-1OA-6); the theorem uses (a)-(b) only.
- Honest limits: (i) SUBCLASS that is already polynomial: 𝒞^1O games are solvable in polynomial time by other means; the value is a
  bound on N5 itself. (ii) CONDITIONAL on (P) for one-player games (G-1OA-4, open by design): VJ00 Lemma 5.8 "1 ⇒ 2", used only in
  Lemma 1 on G[X]. A derivation of the one-player form exists (R-N5-1P §3 route (a)), read as sound by REFEREE-2 but not refereed as a
  signature; DATA: 2,283 improvement-free strategies of G[X] all optimal (REFEREE-2). (iii) o-CYCLIC 𝒞^1O is NOT covered: Lemma 1 holds on (REFEREE-2 N-3, accepted by REFEREE; the signed text §6 says instead that Lemma 1 "has no analogue" there)
  all of 𝒞^1O, but Lemma 2 fails when an exit of o routes back through o (fts_best16: Lemma 2 fails at 24 of 28 pure states). fts_best16 is an
  o-cyclic 𝒞^1O game with 27 iterations in one λ-phase (box 21); box 21's longer one-phase runs fts_best39 (78) and fts_g43
  (121) have 4 and 8 Odd choice vertices and lie outside 𝒞^1O. (iv) Code link (G-N1 = G-N5T-1, inherited): n5.py agrees
  with the referees' definitions on all tested runs, DATA not proof. (v) L-NEW's DATA remark "every block ≤ |Y|" is FALSE (L-RED R58 §10:
  block_bk20 n 24, |Y| 21, one block of 27; block_bk32 n 36, |Y| 33, one block of 49); the theorem bounds blocks by B, not |Y|.
- Data (DATA, not proof): REFEREE (own probe, n5.py unmodified): 7,200 random o-acyclic runs, 2,707 pure transitions, Lemmas 1-3 0
  failures, 2,380 blocks all prefixes of n5.py on G_τ (max 7), Prop X 7,168 runs / 4,841 changes of σ|X 0 mismatches, engine Ξ = own Ξ at
  15,985 states. REFEREE-2 (own code): 1,147 random o-acyclic games (canonical and random starts), 20 composed games with long X runs,
  statY_12, i4_hand: Prop X exact in every case (also on 735 𝒞^1O games with X ≠ ∅, o-cyclic or not), 1,531 changes of σ|X all pointwise optima, 83 pure
  transitions 0 violations. Both: block_bk20 / block_bk32 (blocks of 27 and 49), Lemmas 1-3 and the block identity at all 76 pure states,
  0 violations. Lead: statcheck.py fresh seeds 41/42 and bk20/bk32, 0 failures. Negative control fts_best16 fails as expected (all three).
- Signatures: REFEREE docs/referee/R-N5-1OA.md (referee 9060b51; §0 re-pin bb96f45; §C 061052c; §C2 73b46eb): (A) SIGNED WITH GAPS
  A1-A2, Cor. X1 SIGNED as a reading, (B) SIGNED CONDITIONAL ON (P) WITH GAPS B7 (= N-4) and N-5 (B1-B6 closed or confirmed), Lemma R
  SIGNED, Lemma S SIGNED WITH GAPS S1, S2, G-1OA-6 (first half). REFEREE-2 docs/referee-2/R2-N5-1OA.md (referee-2 603cb3a; §7 re-pin
  3188622; logs d5d941a; §C 0ea3441; §C2 77f9cf7): (A) SIGN WITH GAPS (G-1OA-1, -2 closed; N-1), Cor. X1 SIGN, (B) SIGN WITH GAPS
  conditional on (P) for one-player games (N-2, N-4 = B7, N-5; G-1OA-3, -5 closed by the d78e54f text), Lemma R SIGN, Lemma S SIGN WITH
  GAPS (G-1OA-6; S1, S2). Both §C and §C2: identical verdicts at both pins, no disagreement; joint gap map A1 = G-1OA-2 + N-1,
  A2 = G-1OA-1, B2 = G-1OA-3, B3 = N-3, B4 = G-1OA-5, B7 = N-4, S2 = G-1OA-6 (second half), (P) = G-1OA-4; REFEREE accepted two items it
  had missed (G-1OA-6 first half and N-5). Joint open list: G-1OA-4 ((P), conditional by design) and inherited DATA gap G-N1;
  wording items G-1OA-1, G-1OA-2/N-1, G-1OA-6, N-2, N-4, N-5, S1.
- TARGET.md diff: not a claim of TARGET.md section 1 (a subclass with one Odd choice vertex; no statement about general parity games).
  Gauntlet: partial step-4 lemma for N5 on a subclass. GAPS G-N5-TIME: o-acyclic 𝒞^1O closed conditional on (P) on landing; o-cyclic
  𝒞^1O and the general case open.
