# Draft RESULTS R57 (Lead, 2026-10-26 04:44Z by date -u; both §Cs filled; fixes file FIXES-PENDING) — to CHECKER C66

### R57 [refereed-only] N5's output at its stop is correct on EVERY parity game (Lemma OUT-G), each iteration costs polynomially many bit operations on every game (Lemma BIT-G), and N5 solves one-Even-choice games in polynomial time from any start pair: at most (n(n − 1) + d_e)(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³) ⊆ O(n¹⁷) iterations (Theorem 1E-POLY; Corollary 1E-TIME) (2026-10-26) — the correctness half of gauntlet step 4 for N5 on every game (OUT-G, BIT-G), and a SUBCLASS time result (𝒞^1E, polynomial by other means; TARGET.md §4 first bullet): not a TARGET.md §2 claim, not M4; G-N5-TIME stays open for general games, CHECKER PASS (docs/checker/C66.md, checker PENDING)
- Object (packet P-N5-1E, added at l-si adb721b5, pinned trunk 7fef9699, unchanged during review): docs/si/P-N5-1E-box16.md, sha1
  e613db131d3871c038f53fcb4e009c33f47ca20e (L-SI successor 11, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-1E-fixes-box16.md (FIXES-PENDING); repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with Q1-Q4 and FIX 1-4); any parity game G (TARGET.md §1: V finite, every vertex
  has a successor); n := |V|, m := #edges, Δ := the maximum out-degree. 𝒞^1E := the games in which exactly one Even vertex e has
  out-degree > 1 (any number of Odd choice vertices); d_e := deg(e). Ξσ: Even's honest valuation of σ against S1's optimal Odd
  counterstrategy σ̄; Iσ: SPEC S2's Even improving set. T* is RESULTS R50 (h)'s per-phase bound as used in RESULTS R51 (a). Cost model:
  TARGET.md §3 (word RAM with O(log(n + m))-bit words; longer numbers cost their bit length).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (c), (d), R18 (d)
  Lemma S (a), R21 (a), R36 (c), R51 (a), (c), (d), R54 (a)-(d)); R18 (d) Lemma S (a), R21 (a)'s parenthetical and R36 (c) have
  game-general proofs (one-player G_σ̄ / G_σ on every game; RESULTS R51 (d) N-1O-4, R55, R56), confirmed again by both referees here:
  (a) Premise (VJ), on every game: for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v; read from
      VJ00 (BRICS RS-00-48) §4.3 (Ωσ as the minimum over all plays consistent with σ) and §5.2 (Prop. 5.1, Lemma 5.2, (11)), every finite
      game graph (§2), checked by both referees against the PDF (sha256 485a12de…) (1E-N2 = N-1E-2).
  (b) Lemma OUT-G (every game): if σ is a positional Even strategy with Iσ = ∅, λ(v) is the cycle node of Ξσ(v), W := {v : Ω(λ(v))
      even} and σ̄ is S1's Odd counterstrategy at σ, then W = W_E(G), V ∖ W = W_O(G), σ wins for Even from every v ∈ W against every
      (history-dependent) Odd strategy, σ̄ wins for Odd from every v ∉ W against every (history-dependent) Even strategy, and σ on W and
      σ̄ on V ∖ W are well defined on their regions. Iτ = ∅ is not used; determinacy is derived, not assumed (W_E ∩ W_O = ∅ is proved).
      The "≥ 0" repair of RESULTS R51 (d) (OUT-1) is built in. In particular, on every game N5 stops (R15 (d)) and SPEC S5's output there
      is correct. Standing premise, as in R51 (d): OUT-G concerns SPEC's Ξσ and σ̄; that S1's procedure realises an optimal σ̄ is VJ00 §6
      plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).
  (c) Lemma BIT-G (every game): RESULTS R51 (c) with "on 𝒞^1O" dropped. With valuations stored as (a vertex, an n-bit path-set vector
      indexed by rank, a length ≤ n), compared by cycle-node reward, then the top differing bit, then length (SPEC S1, Q1), one N5
      iteration and the final output step cost O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every
      parity game; no big integers. The longest-path recursion of S1 (iv) is memoised, with the same outputs as SPEC's recursion: R51 (c)'s
      sentence (BIT-N1), which the proof uses and the packet's statement dropped, is read into the statement (1E-N1, REFEREE; accepted by
      REFEREE-2).
  (d) Theorem 1E-POLY: for G ∈ 𝒞^1E and any start pair (the S3 start included), N5 stops after at most ITER ≤ (n(n − 1) +
      d_e)·(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³) iterations; with m ≤ n² and Δ, d_e ≤ n, ITER ≤ (n(n − 1) + d_e)(L(n) + 1) = O(n¹⁷),
      L(n) := T*(n, n², n, n) = O(n¹⁵). Uniform form: RESULTS R54 (c) MIRROR (b) with (H-OF) from (H-N5) by R54 (d) MIRROR (c), and (H-N5)
      from R51 (a) with T*'s monotonicity in m, Δ and d. Parameter form: R54 (c)'s and (d)'s proofs applied to the one game G^d (same n, m,
      Δ; d_o(G^d) = d_e with o = e; F = 2n²), not their uniform statements (N-1E-4); MIRROR (a) (R54 (b)) gives the n(n − 1) + d_e dual
      phases.
  (e) Corollary 1E-TIME: on 𝒞^1E, N5 from any start pair outputs W_E(G), W_O(G) and positional winning strategies for both players (σ on
      W_E, σ̄ on W_O) in O(ITER · n³(n + m)) word operations, with the O(n log n) priority ranking, i.e. in time polynomial in n + m at bit
      cost (TARGET.md §3); the class test costs O(n + m).
- Not signed (packet §6, §7): the READING on G-N5T-3 (RESULTS R15 (iii): output correctness rested on VJ00 Lemma 5.8 '1 ⇒ 2', which uses
  VJ00's unproved Lemma 5.9 and Prop. 5.10): with OUT-G signed, its premises are VJ00 (11) and R36 (c), not Lemma 5.8, 5.9 or Prop. 5.10;
  both referees concur that the output half of G-N5T-3 is thereby removed on every game (N-1E-5, REFEREE §C). This is recorded as a Lead
  reading in GAPS, not as a signed statement. Also not signed: the gauntlet table for 𝒞^1E, the scope reading, the frontier remark, the
  data.
- Honest limits: (i) The time bound is for a SUBCLASS that is polynomial by other means (Even has ≤ d_e positional strategies, each leaving
  a one-player game); its value is the method. (ii) It rests on RESULTS R51 and everything R51 cites (R15, R18 (d), R21, R36, R47, R48,
  R50) and on R54. (iii) OUT-G and BIT-G are about SPEC's N5 and S1 (pseudocode); the code's match is DATA (G-N5T-1). (iv) OUT-G gives
  correctness at the stop on every game; it gives no running-time bound: G-N5-TIME stays OPEN for general games. (v) Thin data for long
  runs: random 𝒞^1E runs are short (max ITER 6 in REFEREE-2's data, 8 in REFEREE's).
- Data (DATA, not proof): REFEREE (successor 12, own engine; seeds fixed or by relative path): 21,101 runs (lib41 n ≤ 64, random 𝒞^1E n
  4-30, random any-class); OUT-G checked at all 34,808 states with Iσ = ∅ (13,707 of them with Iτ ≠ ∅); ITER and σ-changes within the
  bounds on 11,846 𝒞^1E runs; 0 failures; mutation controls bite; its Zielonka agrees with Oink --zlk on the 8 lib41 𝒞^1E games.
  REFEREE-2 (successor 13, own onee_check.py: own SPEC loop, outputs checked from definitions with own Zielonka, enumerated strategies
  and a strategy verifier): 12,324 stops (7,500 random 𝒞^1E n 4-30, 4,000 any-class, 824 lib41), 0 violations; with R2-N5-1O's 7,000
  general-game stops, 19,324; mutations flip, sbar, early bite.
- Signatures: REFEREE docs/referee/R-N5-1E.md (referee c82c4ecf, successor 12; §C 6170561a): (VJ), OUT-G, BIT-G, 1E-POLY (both forms),
  1E-TIME SIGNED; notes 1E-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-1E.md (referee-2 ceed1f63, successor 13; §C bd68d39d, successor
  14): all SIGN; notes N-1E-1..5; no gap. §C (both): verdicts identical; joint gap map empty; 1E-N1 REFEREE's, accepted by REFEREE-2 (its
  predecessor's tick on that quote withdrawn); 1E-N2 = N-1E-2; 1E-N3 = N-1E-1; N-1E-4 = REFEREE's §4 per-game assembly; N-1E-3 closed
  (the quoted R-N5-DUAL C.2 lines exist, l. 138); nothing open.
- TARGET.md diff: OUT-G and BIT-G are statements about N5 on every game (correctness at the stop; cost per iteration); they are not a
  TARGET.md §2 claim, which needs a polynomial bound on iterations for every game. 1E-POLY / 1E-TIME are for a restricted class (TARGET.md
  §4, first bullet). Objects match TARGET.md §1 (winning regions against history-dependent strategies; positional strategies output) and §3
  (bit cost). GAPS G-N5-TIME: open for general games; 𝒞^1O (R51) and 𝒞^1E (this entry) parts closed.
