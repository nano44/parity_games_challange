# Draft RESULTS R51 (Lead, 2026-10-26 01:25Z by date -u; both §Cs and the fixes file filled 01:33Z) (rev. 2026-10-26 01:48Z: C60 E-1, E-2, N-1..N-4) — to CHECKER C60 — LANDED in RESULTS Results 2026-10-26 02:18Z (CHECKER C60 17c5ff9b + Addendum 1 231c8fe6 PASS), after R50

### R51 [refereed-only] N5 solves one-Odd-choice parity games in polynomial time: from any start pair it stops after at most (n(n − 1) + d_o)(T* + 1) = O(m·Δ·d_o·n¹³) iterations (Theorem 1O-POLY), each iteration and the output step cost polynomially many bit operations (Lemma BIT), and the output is the pair of winning regions with positional winning strategies (Lemma OUT; Corollary 1O-TIME) (2026-10-26) — a SUBCLASS result (𝒞^1O, polynomial by other means; TARGET.md §4 first bullet): not a TARGET.md §2 claim, not M4, and not M3 as a class result (the method's novelty is not checked by L-LIT); G-N5-TIME stays open for general games, CHECKER PASS (docs/checker/C60.md, checker PENDING)
- Object (packet P-N5-1O, added at l-si 058e5aee, pinned trunk 291c110d, unchanged during review): docs/si/P-N5-1O-box15.md, sha1
  2cf5e67262d31712976fb882175f5080cc3dc4ec (L-SI successor 10, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-1O-fixes-box15.md (l-si 90f93566, sha1 647deab5f9aeff2c113230bd18df88a6c58b6d68, L-SI successor 10: OUT-1 = N-1O-1, 1O-N1,
  1O-N2, BIT-N1, N-1O-2..6, R-N5-START Addendum 1); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with Q1-Q4 and FIX 1-4); 𝒞^1O := the games in which exactly one Odd vertex o
  has out-degree > 1; n := |V|, m := #edges, d_o := deg(o), Δ := the maximum out-degree. Cost model: TARGET.md §3 (word RAM with words
  of O(log(n + m)) bits; longer numbers cost their bit length).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (c), (d), R18 (d)
  Lemma S (a), R21 (a), R36 (c), R47 (b), R48 (i), R50 (h)):
  (a) Theorem 1O-POLY: for G ∈ 𝒞^1O and any start pair (the S3 start included), N5 stops after at most ITER ≤ (n(n − 1) + d_o)·(T* + 1)
      iterations, where T* is R50 (h)'s bound with f := F := 2n² (R48 (i) gives f ≤ 2n² in every phase; every term of R50 (h)'s chain is
      non-decreasing in f) and R50 (h)'s landed chain, and n(n − 1) + d_o is R47 (b)'s phase count. So ITER = O(m·Δ·d_o·n¹³) ⊆ O(n¹⁸)
      (REFEREE-2 N-1O-2: in fact O(n¹⁷)). R48's f (in-phase Even fallbacks) equals R50 (h)'s f (in-phase fallback transitions), since an
      Odd fallback ends a phase (1O-N1).
  (b) Start-freeness: every result the chain cites is start-free in statement and proof (statewise facts, per-transition facts, and
      inductions whose base is the first state of the window they bound): docs/referee/R-N5-START.md (referee 4e440bd5), with the R32 /
      R33 chain under X-SN-PHASE read line by line in its Addendum 1 (REFEREE, with this review) and by REFEREE-2 (N-1O-5), and
      R34 (b)-(f) line by line in REFEREE-2's report (R2-N5-1O §3; its §C.4 notes that R-N5-START Addendum 1 covers R32 / R33 and R34
      (f), not R34 (b)-(e)).
  (c) Lemma BIT: with valuations stored as (a vertex, an n-bit path-set vector indexed by rank, a length ≤ n), compared by cycle-node
      reward, then the top differing bit, then length (SPEC S1, Q1), one N5 iteration and the final output step cost O(n³(n + m)) word
      operations on O(log(n + m))-bit words and O(n)-bit vectors; no big integers. The longest-path recursion of S1 (iv) is memoised, with the
      same outputs as SPEC's recursion (BIT-N1).
  (d) Lemma OUT: if N5 stops at (σ, τ) on G ∈ 𝒞^1O (Iσ = Iτ = ∅), λ(v) is the cycle node of Ξσ(v), W := {v : Ω(λ(v)) even} and σ̄ is
      S1's best reply, then W = W_E(G), V ∖ W = W_O(G), σ wins for Even from every v ∈ W against every (history-dependent) Odd strategy, and
      σ̄ wins for Odd from every v ∉ W against every Even strategy. The proof's "reward(λ(v)) > 0" fails at the rank-0 even cycle node and
      is repaired to "≥ 0", with every odd vertex of reward ≤ −1; the conclusion is unchanged (OUT-1 = N-1O-1, both referees,
      independently; fixes). It uses R21 (a)'s parenthetical (σ̄ pointwise optimal in G_σ), which holds on every game (N-1O-4; R18 (d)
      Lemma S (a)).
  (e) Corollary 1O-TIME: on 𝒞^1O, N5 from any start pair outputs W_E(G), W_O(G) and positional winning strategies for both players in
      O(ITER·n³(n + m)) word operations, with the O(n log n) priority ranking, i.e. in time polynomial in n + m at bit cost (TARGET.md §3); the class test costs O(n + m).
- Not signed (packet §6, §7): the gauntlet table (a READING: steps 1-3 done for N5 per RESULTS R15 (step 3 with caveats, L-LIT T20; a second
  implementation by L-COMP in progress), step 4 for the subclass by this entry
  and R47-R50; Lean not done and not needed, since this is not an M4 claim); MIRROR / 𝒞^1E (P-N5-DUAL, in review); the frontier
  𝒞^(≥2E,≥2O), where every known exponential strategy-improvement family lies (L-NEW 22, DATA) and nothing here transfers as proved.
- Honest limits: (i) SUBCLASS 𝒞^1O, which is polynomial by other means (Odd has at most d_o positional strategies); the value is the
  method. (ii) The bound is loose and unoptimised; it is not a growth law (R47's data: at most 30 phases in any run). (iii) It rests on
  RESULTS R15, R18 (d), R21, R36, R47, R48 and R50 and on everything those cite. (iv) The objects are SPEC's N5 (pseudocode); BIT is checked
  against SPEC's text, and the code's match to SPEC is DATA (R15 G-N5T-1). (v) Thin data: random 𝒞^1O runs are short (max 8 phases, phase
  length 4, f 1); the long runs are the library's (f 37, length 112, 29 phases); REFEREE-2's Even-strategy enumeration is capped at 4,096
  per stop (skipped at 3,645 random and 1,080 library stops).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own onecheck.py on rl_engine; checks at the stop: W =
  own Zielonka's W_E, σ wins W, σ̄ wins V ∖ W, ITER ≤ the bound, f ≤ 2n² per phase): P-N5-RHO's library (253 𝒞^1O games) from S3 and 2
  random start pairs, 759 runs, 3,116 phases (max f 33, max ITER 115), and 500 random 𝒞^1O games; 0 failures; its Zielonka agrees with
  Oink 8fbf0a7 --zlk on 109 library files; mutation controls bite (the output read at the start state is wrong in 133 of 239 games).
  REFEREE-2 (own onecheck.py): 26,000 random 𝒞^1O stops (n 4-30) and 503 library files × 3 starts, every check from definitions (play =
  Ξσ, W = W_E, both strategies win against every enumerated positional counter-strategy), 0 violations; ITER, f, phases and phase
  lengths within the bounds on 1,509 library runs (max f 37, max phase length 112, max 29 phases); all mutation controls bite. The
  bound is far above every observed count.
- Signatures: REFEREE docs/referee/R-N5-1O.md (referee 4298dae9, successor 11; §C e785b8e1): 1O-POLY, BIT, 1O-TIME SIGNED; OUT SIGNED
  WITH GAP OUT-1 (one-word repair); notes 1O-N1, 1O-N2, BIT-N1; R-N5-START Addendum 1 (R32 / R33 line by line). REFEREE-2
  docs/referee-2/R2-N5-1O.md (referee-2 04c2d708, successor 13; §C 3312144c): all SIGN, no gap; notes N-1O-1..6. §C (both): verdicts identical in substance; joint gap map one row, OUT-1 =
  N-1O-1, closed by the repair; 1O-N1, 1O-N2, BIT-N1 and N-1O-2, N-1O-3, N-1O-4, N-1O-6 accepted across; REFEREE-2's §3 reads R34 (b)-(f) line by
  line (§C.4), so the R32 / R33 / R34 chain is read in full jointly. No disagreement remains.
- TARGET.md diff: not a claim of TARGET.md §2 (restricted class; TARGET.md §4, first bullet). Its objects match TARGET.md §1 (winning
  regions against history-dependent strategies; positional strategies output) and §3 (word RAM, bit cost). GAPS G-N5-TIME: open for general
  games; its 𝒞^1O part is closed by this entry.
