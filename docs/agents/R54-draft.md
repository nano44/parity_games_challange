# Draft RESULTS R54 (Lead, 2026-10-26 ~02:43Z, before commit 8371145b at 02:43:14Z; stamp corrected 03:02Z, the first stamp was not from date -u; both §Cs and the fixes file filled) (rev. 2026-10-26 03:19Z: C63 N-2) — to CHECKER C63 — LANDED in RESULTS Results 2026-10-26 03:19Z (CHECKER C63 04ad4a15 PASS), after R53

### R54 [refereed-only] N5 is mirror-symmetric: on every game, the N5 run on G is the mirror of the "Odd first" run N5^OF on the dual game G^d (Lemma DUAL); on one-Even-choice games σ changes at most d_e − 1 times and a run has at most n(n − 1) + d_e dual phases, and a per-first-phase bound L(n) for N5^OF on one-Odd-choice games ((H-OF), implied by the same bound for N5 by MIRROR (c)) gives at most (n(n − 1) + d_e)(L(n) + 1) iterations on one-Even-choice games (Theorem MIRROR, (b) as an implication); phases ≤ n(n − 1) + ∏ deg(o_i) on every game (Corollary Φ-kO); an empty improving set stays empty (Lemma ENDGAME) (2026-10-26) — structural lemmas for N5 and a conditional transfer (not M3, not a step-4 pass, not a TARGET.md claim; no running-time bound on any class is signed here; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C63.md, checker PENDING)
- Object (packet P-N5-DUAL, added at l-new b15856e8, pinned trunk df073cb5, unchanged during review): docs/new/P-N5-DUAL-box43.md, sha1
  a51f7c30c267a4c02088cf2c849388e28c4121fa (L-NEW successor 22, Opus 5.5). The referees' repair and notes are collected by the lane in
  docs/new/P-N5-DUAL-fixes-box43.md (l-new 478dd6e1, sha1 5d08d0fd421fa85d36408b1caeabf03b75653760, L-NEW successor 23: DUAL-1 = N-DUAL-1 (the one repair), N-DUAL-2,
  N-DUAL-3, a status line); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4); n := |V|. G^d := the dual game (owners swapped, Ω + 1, same ids
  and successor lists; n5.py's dual). N5^OF ("Odd first"): N5 with S4c replaced by "if σ_new = σ and τ_new = τ: if I_τ ≠ ∅ Odd falls
  back (switch-all on I_τ, each Odd v with an improving edge takes the w maximising (Ξ_τ(w), w) on G^d, σ unchanged), else Even falls
  back as in S4c". A TWO-SIDED FALLBACK is an iteration where S4c applies with I_σ ≠ ∅ and I_τ ≠ ∅. The MIRROR of a state (σ, τ) of G is
  the state (τ, σ) of G^d. A choice vertex has out-degree ≥ 2; 𝒞^1O: exactly one Odd choice vertex; 𝒞^1E: exactly one Even choice
  vertex e, d_e := deg(e), any number of Odd choice vertices. Phase: a maximal run with (λ, τ) constant (RESULTS R38 (a) KEY); dual
  phase: a maximal run with (λ^U, σ) constant (λ, λ^U as in RESULTS R47).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R15 (a)-(d), R38 (a), R47 (a):
  (a) Lemma DUAL (every game, every start pair (σ_0, τ_0)): the N5 run on G from (σ_0, τ_0) is the mirror of the N5^OF run on G^d from
      (τ_0, σ_0) (same length, state k ↦ the mirror of state k). Consequently the N5 run on G^d from (τ_0, σ_0) agrees with that mirror on
      states 0, …, j; the first possible difference is at state j + 1, where j → j + 1 is the first two-sided fallback of the run on G;
      with no two-sided fallback the two runs are mirrors. (The second sentence is read with the fixes file's repair: the packet's
      sentence named two different agreement points, its "i.e." clause is the right one and the proof is unchanged; DUAL-1 = N-DUAL-1,
      found independently by both referees.) The proof rests on Ω + 2 invariance of SPEC S1 (rank by (Ω(v), v) and Ω(v) mod 2 only).
  (b) Theorem MIRROR (a): on 𝒞^1E, along any N5 run σ changes at most d_e − 1 times, and the run has at most n(n − 1) + d_e dual phases.
  (c) Theorem MIRROR (b), signed as an IMPLICATION: under hypothesis (H-OF) "there is L(n) such that for every 𝒞^1O game with n vertices
      and every start pair, the first phase of the N5^OF run from that start pair has at most L(n) transitions", N5 on every 𝒞^1E game
      with n vertices, from every start pair, makes at most (n(n − 1) + d_e)(L(n) + 1) iterations. (H-OF) is not proved in the packet.
  (d) Theorem MIRROR (c): (H-OF) follows from (H-N5) "for every 𝒞^1O game with n vertices and every start pair, the first phase of the
      N5 run has at most L(n) transitions" (the first N5^OF phase from a state is a prefix of, or equal to, the first N5 phase from it).
  (e) Corollary Φ-kO (every game): along any N5 run the number of distinct τ's is at most ∏ over the Odd choice vertices o_i of deg(o_i),
      and the run has at most n(n − 1) + ∏_i deg(o_i) phases; mirror: at most n(n − 1) + ∏ over the Even choice vertices of deg dual
      phases. On 𝒞^kO with k fixed, phases ≤ n(n − 1) + n^k. (A bound on phases, not on iterations.)
  (f) Lemma ENDGAME (every game): if I_σ = ∅ at state k of an N5 run, then σ_j = σ_k for every j ≥ k; mirror: if I_τ = ∅ at state k,
      then τ_j = τ_k for every j ≥ k.
- Not signed (packet §1 Scope, §2, §3): the scope READING (𝒞^1E has unboundedly many Odd choice vertices); the §2 start / N5^OF table
  ("to check, not to sign"; its general argument checked by REFEREE, rows spot-checked; the rows used by the 𝒞^1O chain are covered by
  docs/referee/R-N5-START.md with its Addendum 1 and REFEREE-2's R2-N5-1O §3, the other rows unaudited by both, N-DUAL-2); the Φ-kO
  Remark (DATA); docs/new/N5-MULTI-box43.md §2-§4 (CONJECTURES Δ1, Δ2); the cross-field reading of DUAL. READING (N-DUAL-3, both
  referees; not signed here): with RESULTS R51, (H-N5) holds with L(n) = T*(n, n², n, n) (T* is non-decreasing in m, d_o, Δ), so MIRROR
  (b), (c) would give O(n¹⁷) iterations on 𝒞^1E from every start pair; output correctness on 𝒞^1E would also need Lemma OUT stated and
  signed on every game, and Lemma BIT; both are for a separate packet. The 𝒞^1E bound is not a result of this entry.
- Honest limits: (i) No running-time bound is signed here: MIRROR (b) is an implication, and its 𝒞^1E instance is a READING (above).
  (ii) DUAL needs N5^OF on the dual side; the plain N5 run on G^d can part from the mirror at a two-sided fallback (the packet's example
  experiments/red/so/instances/exitr_cex_n48.pg, sha1 7a663df2: first two-sided fallback 2 → 3, first difference at state 3, 22
  iterations on G against 23 on G^d). (iii) Thin data: random games never produce a two-sided fallback (0 in every random set of both
  referees); DUAL's second sentence is exercised by library runs and REFEREE's climbs only.
- Data (DATA, not proof): REFEREE (own dual_probe.py on rl_engine, S4c side rule as a parameter; checks DUAL, PLAIN first difference,
  Ω + 2, ENDGAME, Φ-kO and its mirror, MIRROR (a) on 𝒞^1E, the MIRROR (c) prefix property on 𝒞^1O): lib41 n ≤ 64 (367 files) from S3 and
  2 random start pairs, 1,101 runs, 50 with two-sided fallbacks (128); 3,000 random games with k = 0..4 Odd choice vertices (378 𝒞^1E);
  climbs (dual_climb.py, 3 × 1,200 s) 390,158 runs, 135,671 with two-sided fallbacks (297,779); every plain-mirror first difference exactly
  at j + 1; prefix property on 24,056 sampled states; 0 failures. REFEREE-2 (own dual_check.py on L-SI's si.py engine with an Odd-first
  flag): lib41 824 runs (33 with two-sided fallbacks, 88), 1,006 𝒞^1O library runs (33, 170), 6,000 random runs (2,000 𝒞^kO, 2,000 𝒞^1E,
  2,000 𝒞^1O); every first difference at j + 1; MIRROR (a)'s bound d_e − 1 attained; 0 violations; on lib41 from S3 it reproduces the
  packet's 15 runs / 54 two-sided fallbacks exactly; mutation controls plain (15), phi (36), endg (163) bite.
- Signatures: REFEREE docs/referee/R-N5-DUAL.md (referee cdb187c7, successor 11; §C 78db369b): DUAL first sentence, MIRROR (a), (c),
  Φ-kO, ENDGAME SIGNED; MIRROR (b) SIGNED as an implication; DUAL second sentence SIGNED WITH GAP DUAL-1 (wording), closed by the fixes
  file's repair. REFEREE-2 docs/referee-2/R2-N5-DUAL.md (referee-2 73c2b4a1, successor 13; §C 253fe5c5): all SIGN ((b) as an
  implication), no gap; notes N-DUAL-1..3. §C (both): verdicts identical in substance; joint gap map DUAL-1 = N-DUAL-1, closed by the
  one-line repair; N-DUAL-2 accepted (REFEREE's §6 updated by its R-N5-START audit); N-DUAL-3 agreed as a READING. Nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (no running-time bound is proved; MIRROR (b) is conditional; DUAL, Φ-kO and
  ENDGAME are structural). GAPS G-N5-TIME: open for general games (its 𝒞^1O part closed by RESULTS R51; 𝒞^1E a READING).
