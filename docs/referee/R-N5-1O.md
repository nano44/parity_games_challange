# R-N5-1O: REFEREE report on packet P-N5-1O (L-SI box 15: Theorem 1O-POLY, Lemma BIT, Lemma OUT, Corollary 1O-TIME) — a subclass result, NOT a TARGET.md claim
Referee: REFEREE (successor 11, session_01VH2ckvgGP9CGkb8Suno5f1), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 00:51Z (Lead's stamp), "TOP PRIORITY".
- Object: docs/si/P-N5-1O-box15.md at trunk 291c110d, sha1 2cf5e67262d31712976fb882175f5080cc3dc4ec (checked with
  `git show 291c110d:docs/si/P-N5-1O-box15.md | sha1sum`; identical on my tree), 184 lines. Author: L-SI successor 10.
- Written 2026-10-26T00:55Z-01:00Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/R2-N5-1O* file read. No lane code run or imported. D1: wrong until checked.
- Read for this report (texts, not recalled): TARGET.md §1, §3, §4; SPEC docs/new/N5-ssi-global.md S1-S5, Q1-Q4, FIX 1-4; RESULTS R15 (c),
  (d), R17 (a), R18 (d), R21 (a) with its source P-N5-X-box28 §1, R36 (c), R47 (b), R48 (i), R50 (h); P-N5-FRZ-box34 §0-§7 and
  P-N5-L2-box34 §1-§7 (the R32 / R33 chain, line by line, for start-freeness); experiments/si/si.py l. 140-180 (memoisation; DATA).
- Tools: own engine scratch/rl_engine.py + rl_probe.py; new probe scratch/onecheck.py (own Zielonka, one-player winning checks, the
  packet's bound). Logs scratch/one_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | the citation table (exact quotes) | CHECKED: every quote matches docs/RESULTS.md; ellipses drop only parentheticals (§1 below) |
| §2 | Theorem 1O-POLY (any start pair; ITER ≤ (n(n − 1) + d_o)(T* + 1), O(m·Δ·d_o·n¹³)) | SIGNED (notes 1O-N1, 1O-N2) |
| §2.1 | start-freeness | CLOSED: the line-by-line R32 / R33 pass asked for is done here (§3) and recorded as R-N5-START Addendum 1 |
| §3 | Lemma BIT | SIGNED (note BIT-N1: memoisation) |
| §4 | Lemma OUT | SIGNED WITH GAP OUT-1 (one inequality: "reward(λ(v)) > 0" is ≥ 0; one-word repair, conclusion unchanged) |
| §5 | Corollary 1O-TIME | SIGNED |
| §6, §7 | gauntlet status, MIRROR, frontier | READING, not signed; checked as readings (§7 below) |
Summary: N5 solves 𝒞^1O games (exactly one Odd vertex of out-degree > 1) from any start pair in polynomially many iterations, each of
polynomial bit cost, with correct regions and positional winning strategies. This is a SUBCLASS result, polynomial by other means (TARGET.md
§4, first bullet): NOT a TARGET.md §2 claim and not M4. One gap (OUT-1, a corner of an inequality), closed by its repair.

## 1. The citations (Lead's item "each cited statement is quoted exactly")
- R15 (c): "≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺" — verbatim
  (RESULTS R15 (c), across a line break).
- R15 (d): verbatim up to two ellipses, which drop "(S4a/S4b, or the S4c fallback, a switch-all); Iσ depends on σ alone (…)" and the
  iteration count; nothing used is dropped.
- R47 (b): verbatim; the ellipsis drops "(the τ's form a strict ≺_{G^d}-chain by R15 (c), (d) on G^d, so no τ repeats; N-PHI-1)".
- R48 (i): verbatim; the ellipsis drops the intermediate form "f ≤ 1 + (|U| − 2)·(deg_U(o) + |U|), and"; the quoted form is the repaired
  one (FBP-1 = N-FBP-2).
- R50 (h): verbatim (RESULTS R50 (h)).
- R36 (c): verbatim (the first sentence of R36 (c)); "one-player: every non-Even vertex has one successor" is the packet's gloss of R36's
  setting, correct.
- R21 (a): verbatim.

## 2. Theorem 1O-POLY: SIGNED
- Step 1: R15 (d) "changes at least one of them": every iteration is a transition; termination. Correct.
- Step 2: R47 (b): ≤ n(n − 1) + d_o phases; boundary transitions ≤ #phases − 1. Correct.
- Step 3, f ≤ F := 2n². R48 (i) (a) 1 + (n − 2)(2n − 1) = 2n² − 5n + 3 ≤ 2n²; (b) 1; (c) |U| ≤ n. The cases are exhaustive (o ≠ c_θ, with
  (b) its sub-case, or o = c_θ). Correct.
  - 1O-N1 (units): R48's f counts "in-phase Even S4c fallbacks"; R50 (h)'s f counts the phase's "fallback transitions". They are the same
    number: an Odd fallback changes τ and so is a phase boundary (SPEC S4c, FIX 3; P-N5-KW §1), never an in-phase transition.
- The f-monotonicity step (Lead's item). R50 (h)'s chain bounds the phase's actual counts X, Θ, S_o, W_ch, N_st, N_Ξ, T_rel, T by
  expressions each of which is a sum of products of non-negative terms, non-decreasing in f and in the counts it takes as arguments:
  - X_SN ≤ 13(d_o + 1)n³(f + 1 + t) + t with the actual toggle count t ≤ T_H = n² + 2n − 1 (R34 (e)), non-decreasing in f and t;
  - X ≤ (f + 1)(n − 1) + f + X_SN; Θ ≤ (n − 1) + n(X + 1) + X (or Θ = 0 when c_θ = o); S_o ≤ d_o(Θ + 1); W_ch ≤ (f + X + 1)n²;
    N_st ≤ 1 + X + Θ + W_ch; N_Ξ ≤ f + (N_st − 1) + (X + 1)(n − 1) + (N_st + f)·3Δn⁴; T ≤ (m − n + 1)(S_o + N_Ξ + 1).
  - Substituting f ≤ F and each count by its bound, in this order, is valid because every expression is non-decreasing in each argument
    (all coefficients are non-negative; n ≥ 1, m ≥ n since every vertex has a successor). Correct.
  - 1O-N2 (looser, harmless): the packet's N_Ξ uses F + N_st where R50 (h) has f + (N_st − 1).
- Step 4: ITER ≤ #phases·T* + (#phases − 1) ≤ (n(n − 1) + d_o)(T* + 1). Correct (phase-count arithmetic, Lead's item).
- Step 5, the orders: X_SN, X = O(d_o n³(F + n²)) = O(d_o n⁵); Θ = O(n X) = O(d_o n⁶); S_o = d_o(Θ + 1) = O(d_o² n⁶) ⊆ O(d_o n⁷);
  W_ch = (F + X + 1)n² = O(d_o n⁷); N_st = O(d_o n⁷); N_Ξ = (N_st + F)·3Δn⁴ + lower = O(Δ d_o n¹¹); T* = O(m Δ d_o n¹¹); × O(n²) phases:
  ITER = O(m Δ d_o n¹³); with d_o, Δ ≤ n and m ≤ n² (successor lists are sets), O(n¹⁸). Checked.
- "From any start pair": each cited result is start-free (R-N5-START), and the R32 / R33 caveat is closed (§3). N5 is memoryless, so a
  run from any start pair is covered. Correct.

## 3. Start-freeness of the R32 / R33 chain, line by line (the packet's §2.1 "REFEREES' CHECK")
Read in full: P-N5-FRZ-box34 §0-§7 (R32) and P-N5-L2-box34 §1-§7 (R33). Every statement and every step, by kind ((S) statewise, (T) one
N5 transition, (W) a window / run / phase with its base at the window's first state; R-N5-START §0):
| item | kind | the step that could depend on history, and why it does not |
| --- | --- | --- |
| R32 NL-MF | (T) | one (h) S4a transition, R29 NL's (A_j) at j. |
| R32 Fact 0 | (S) | at one (h) state. |
| R32 ARENA | (T) | one S4a step from an (h) state. |
| R32 Step 1 (Lemma C_ℓ) | (S) | at each window state separately ("this holds at each state separately"). |
| R32 Step 2 | (T) | WM at S4a steps; R15 (a) + Step 1 at fallbacks. |
| R32 Lemma P^c_ℓ | (W) | induction on j from the window's first state k0; base j = 0 by Fact 0 at k0 (statewise); cases A, B1, B2 and B-fallback use (V1), (V2c), (F1), Fact 0 at k+1, FBL step 1 (any in-phase fallback). |
| R32 Theorem FREEZE | (W) | Step 3 at any H2 state t ≥ F of the same phase (paths in G_τ, statewise); Step 4: R15 (a), XW, Step 1 at F. "No hypothesis on the states after F". Nothing before k0. |
| R32 RATCHET | (W) | FREEZE at x = o; monotone θ, w after F. |
| R32 BLOCK | (W) | inside a set I of consecutive states after F. |
| R32 X-RUN | (W) | inside one fallback-free run Q and its SN prefix P; F(ℓ) defined inside P; the level-by-level segments live in P. |
| R32 SUB | (W) | inside a (w, r)-subrun; (ii) uses its first n states as a window. |
| R33 H3-CONST | (S) + phase constants | τ, λ, c_θ constant in the phase; "if the phase has one (h) state" is a property of the phase, not of the run's start. |
| R33 H2-STICK | (T) | one S4a transition (R-STICK). Corollary: a prefix of a fallback-free run. |
| R33 G′ | (S) | one H3 ∧ ¬H1 state. |
| R33 FREEZE′ | (W) | FREEZE's proof re-checked at H3 windows; same anchors. |
| R33 R-CONST | (S) | one ¬H1 state. |
| R33 H1-INT | (W) | monotone θ (R15 (a)) inside the phase; H1-DROP at one transition. |
| R33 X-RUN′, X-RUN° | (W) | split of one fallback-free run's SN prefix into H1 / ¬H1 runs; X-RUN applied inside each H1 run. |
Result: the R32 / R33 chain under R34 (f) X-SN-PHASE is START-FREE, statement and proof. With R-N5-START's other rows, every result the
packet's chain uses is start-free. Recorded as R-N5-START Addendum 1 (same commit).

## 4. Lemma BIT: SIGNED, note BIT-N1
- Representation: SPEC S1 values (c, P, ℓ); Q1 gives the order by the top differing rank of P Δ P′ and its parity, so a comparison costs
  O(n) bit operations; rewards |±p′| ≤ 2n + 1 and lengths ≤ n are one word. No number exceeds n bits (si.py's Python ints for P are
  n-bit masks: DATA). This meets TARGET.md §3 ("Arithmetic on numbers longer than one word costs its bit complexity"). Correct.
- S1's procedure, step by step against SPEC S1 (i)-(vi): (i) one DFS, (ii) one reverse search, (iii) per u ∈ R above v one reachability
  search, ≤ n bit-sets, O(m) edge deletions; (iv) longest path (Ω(v) even) or BFS (odd); (v) one DFS (FIX 2, Q2); (vi) ≤ n copies.
  O(n(n + m)) word operations plus O(n²) vector updates per v, n values of v. Correct.
- BIT-N1 (precision): S1 (iv) says "recursion over successors in list order, first strict maximum wins"; the O(n + m) bound needs the
  recursion MEMOISED. Memoisation computes the same lengths and choices (each vertex's value is a function of its successors' values in
  the restricted graph, which Q3 shows has no cycle avoiding v; I checked Q3's three cases: lower-ranked or odd top ⇒ an earlier dead
  cycle; even top above v ⇒ cut by step (iii) for u = that top), so a memoised implementation IS SPEC's step. si.py memoises (state
  dict with a cycle guard, l. 152-170). Without memoisation the plain recursion could take exponential time on a DAG; the lemma is
  about the memoised computation, which the fixes file should say in one line.
- Per iteration: Ξσ on G, Ξτ on G^d, S4a's run on the dual arena, S4b's run on H′: ≤ 4 runs of S1; Iσ, Iτ, S4c: ≤ m comparisons each.
  S3 (FIX 1) O(m); S5 one run plus O(n). Correct. (The packet's O(n³(n + m)) word operations per iteration is a loose upper bound of
  O(n²(n + m)) + O(n³) bit operations; correct as stated.)

## 5. Lemma OUT: SIGNED WITH GAP OUT-1
- Step 1 (one-player cycle fact): D = the vertices seen infinitely often, strongly connected through the play's edges; its top-ranked
  vertex t has the top priority p (rank orders by (Ω, v)); a simple cycle C in D through t has t as top and cycle node (p′ order = rank
  order); a shortest path from v to C meets C only at its end, so path + C is a positional choice for the mover. Correct.
- Step 2 (Even's side). Uses: for every positional Odd τ′, val(σ, τ′)(v) ⊵ Ξσ(v).
  - The Lead's question, whether R21 (a)'s parenthetical is general and whether it uses 𝒞^1O: its proof (P-N5-X-box28 §1) is "σ̄_k is a
    pointwise-optimal counter-strategy for Odd there: VJ00 §5.2, Prop. 5.1 and Lemma 5.2, eq. (11); this is R17 (F1) on the dual game.
    So Ω_{σ_k, σ̄_k} ⊴ Ω_{σ_k, τ} for every Odd strategy τ". So the GENERAL form, every Odd strategy τ′, is exactly what is proved, and
    the proof uses no 𝒞^1O fact: R17 (a) (F1) is "the optimum of a one-player game dominates every strategy of that game pointwise", for
    every one-player game, and VJ00 (11) is game-general. RESULTS R18 (d) Lemma S (a) states the same pointwise minimum ("L_σ is the
    pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ … VJ00 (11) on G"). So Lemma OUT's use is correct, and the packet's §4 READING
    (the same proof on every game) is consistent; as a READING it is not signed here.
  - OUT-1 (gap, closed by a one-word repair): the proof says "v ∈ W, so reward(λ(v)) > 0 (λ(v) even)" and then "the cycle node … has reward
    ≥ reward(λ(v)) > 0: it is even". If λ(v) is the vertex of rank 0 and its priority is even, p′(λ(v)) = 0 and reward(λ(v)) = 0, so
    "> 0" is false there. The conclusion survives: every odd cycle node has reward −p′ ≤ −1 < 0, so reward ≥ 0 already forces an even
    cycle node. Repair: "reward(λ(v)) ≥ 0" (and "every odd vertex has reward ≤ −1"). Odd's side ("< 0", "≤ … < 0") is correct as written.
  - Then step 1 in H := G_σ: an odd-outcome σ-play would give a positional τ′ with an odd cycle node, reward ≤ −1 < 0 ≤ reward(λ(v)):
    contradiction. Correct with OUT-1.
- Step 3 (Odd's side): H := G_σ̄ one-player for Even; σ's play valuation there is Ξσ by S1's definition; its improving edges are S2's Iσ,
  empty at the stop; R36 (c) gives V_{σ′} ⊴ Ξσ; even cycle nodes have reward ≥ 0 > reward(λ(v)); step 1. Correct. (OUT uses only
  Iσ = ∅ of the stop condition; that is enough.)
- Step 4: W ⊆ W_E and V \ W ⊆ W_O, so equality; closure of σ-plays in W and σ̄-plays in V \ W by the steering argument. Correct.
  Positional: σ and σ̄ are positional.
- "This removes, ON 𝒞^1O, R15's outside gap G-N5T-3": correct as stated (Lemma 5.8's needed half is R36 (c) plus the pointwise-minimum
  fact).

## 6. Corollary 1O-TIME: SIGNED
- ITER (§2) × per-iteration cost (§4) + the ranking + S3 + S5 + the class test (O(n + m)): polynomial in n + m at bit cost, from any
  start pair, with W_E, W_O and positional strategies (§5). TARGET.md §1's encoding: priorities in binary, compressed by sorting
  (TARGET.md §1). Correct.

## 7. READINGs (§6, §7; not signed)
- §6 gauntlet table: correctly says this is for the subclass; Lean NOT done; second implementation "in progress per R15"; step 5 after
  the referees. As a reading it is accurate; it is not a gauntlet pass for TARGET.md (the class is restricted, TARGET.md §4).
- §6 "What this does NOT do" and §7 (MIRROR / 𝒞^1E in review; the frontier): accurate.

## 8. Data (DATA, not proof; scratch/onecheck.py on rl_engine; logs scratch/one_logs/)
Checks at N5's stop: OUT_W (W = own Zielonka's W_E), OUT_SIG (σ wins W: no vertex of W reaches an odd-topped cycle in G_σ), OUT_BAR (σ̄
wins V \ W in G_σ̄), ITER ≤ the packet's bound, FMAX (in-phase fallbacks ≤ 2n² per phase).
| corpus | runs | phases | failures |
| --- | --- | --- | --- |
| P-N5-RHO's library (253 𝒞^1O games), S3 + 2 random start pairs | 759 | 3,116 (max f 33, max ITER 115) | 0 |
| 500 random 𝒞^1O games, n 4-14 | 500 | 874 | 0 |
- My Zielonka vs Oink 8fbf0a7 `--zlk -v` on 120 library files: 109 parsed, 0 mismatches (one_logs/oink_vs_zielonka.txt).
- Mutation controls (one_logs/mutation_start_state.txt): at the START state (Iσ ≠ ∅ in general) OUT_BAR fires in 136 of 239 games and W
  differs from W_E in 133, so Lemma OUT's need for Iσ = ∅ shows; OUT_SIG never fires at the start state, as the proof predicts (Even's
  side uses only σ̄'s optimality, true at every state); OUT_SIG on the odd set fires in 56 of 56 games that have one (the check has teeth).
- The iteration bound is far above every observed count (max 115 iterations); no growth law is claimed or tested.

## 9. Notes and gap for the fixes file
- OUT-1 (Lemma OUT step 2): "reward(λ(v)) ≥ 0" in place of "> 0"; add "every odd vertex has reward ≤ −1".
- BIT-N1 (Lemma BIT (iv)): the longest-path recursion is memoised (same outputs as SPEC's recursion; Q3 makes the restricted graph minus v
  acyclic).
- 1O-N1 (Theorem step 3): R48's f (in-phase Even fallbacks) = R50 (h)'s f (in-phase fallback transitions); an Odd fallback ends a phase.
- 1O-N2 (T*): N_Ξ's "F + N_st" is looser than R50 (h)'s "f + (N_st − 1)"; harmless.
- §2.1's REFEREES' CHECK: done (§3 here; R-N5-START Addendum 1).

## §C. Comparison with REFEREE-2 (R2-N5-1O.md, referee-2 04c2d708, REFEREE-2 successor 13) (Opus 5.5, D15)
Written 2026-10-26T01:22Z by date -u, REFEREE successor 11. Routing: the Lead's message of 01:18Z (Lead's stamp). My report (4298dae9) was pushed
before I opened R2-N5-1O.md. Same object: P-N5-1O-box15.md sha1 2cf5e672 at 291c110d.

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 |
| --- | --- | --- |
| §1 quotes | checked, verbatim (table) | checked, 11 of 13 verbatim; 2 cosmetic attributions (N-1O-6) |
| Theorem 1O-POLY | SIGNED (1O-N1, 1O-N2) | SIGN (N-1O-2) |
| §2.1 start-freeness, R32 / R33 line by line | done (§3; R-N5-START Addendum 1): START-FREE | done (N-1O-5): START-FREE |
| Lemma BIT | SIGNED (BIT-N1) | SIGN (N-1O-3) |
| Lemma OUT | SIGNED WITH GAP OUT-1 | SIGN (N-1O-1 precision; N-1O-4) |
| Corollary 1O-TIME | SIGNED | SIGN |
| §6, §7 READINGs | not signed | not signed |
Both referees sign every statement. The only difference is the label of one shared finding (C.2, first row). The R32 / R33 start-freeness
item was checked line by line by both, independently, with the same result.

### C.2 Joint gap / note map (one fixes-file line per row)
| REFEREE | REFEREE-2 | ruling |
| --- | --- | --- |
| OUT-1 ("reward(λ(v)) > 0" false when λ(v) is the rank-0 vertex with even priority; "≥ 0" repairs it; odd rewards ≤ −1) | N-1O-1 (the same; REFEREE-2's data REACHES the case: 1,969 of 26,000 random stops, 81 of 1,509 library stops; the conclusion holds there) | SAME finding, found independently. As with KW-1, I keep "gap, CLOSED by the repair" (a sentence false as written, one vertex), and do not object to the Lead recording it as one precision item. ONE fixes line: "Step 2: reward(λ(v)) ≥ 0 (twice); odd cycle nodes have reward ≤ −1". REFEREE-2's data shows the corner is not hypothetical. |
| — (my §2 marked "O(n¹⁸)" as checked) | N-1O-2 (ITER = O(mΔd_o n¹³) ⊆ O(n¹⁷) with m ≤ n², Δ, d_o ≤ n; "O(n¹⁸)" is true but loose) | ACCEPTED: n² · n · n · n¹³ = n¹⁷. I checked the inclusion, not its tightness. Fixes line: "⊆ O(n¹⁷)". |
| — (my §4 accepted O(n²(n + m)) per S1 run as a loose bound) | N-1O-3 (each R_v becomes dead at (vi), so Σ_v |R_v| ≤ n and one S1 run costs O(n(n + m)) words + O(n²) vector bits) | ACCEPTED: the regions R_v are disjoint, so step (iii)'s loop over u ∈ R_v totals ≤ n reachability searches over all v. Optional fixes line. |
| BIT-N1 (memoisation of S1 (iv)'s recursion; Q3) | — | REFEREE only; stands. Fixes line as in §9. |
| §5 step 2: R21 (a)'s parenthetical is the general form (P-N5-X §1: VJ00 (11), R17 (F1) on the dual, no 𝒞^1O); R18 (d) Lemma S (a) states it | N-1O-4 (the same: YES; cite R18 (d) Lemma S (a) beside R21 (a)) | SAME. Fixes line: "cite R18 (d) Lemma S (a) (statement) with R21 (a) (parenthetical)". |
| §3 / Addendum 1 to R-N5-START (R32 / R33 line by line) | N-1O-5 (the same check, step by step) | SAME result, two independent readings. The packet's §2.1 REFEREES' CHECK is closed by both. |
| §1 (quotes in the citation table verbatim) | N-1O-6 (two further quotes in §4: VJ00 (11) via P-N5-LP §0 l. 29, and R15's G-N5T-3 with inner quote marks; cosmetic) | ACCEPTED (my §1 checked the citation table only). Cosmetic. |
| 1O-N1 (R48's f = R50 (h)'s f; an Odd fallback ends a phase) | — | REFEREE only; stands (a units line). |
| 1O-N2 (N_Ξ's "F + N_st" looser than R50 (h)) | — | REFEREE only; harmless. |

### C.3 Data, compared
- Lemma OUT at the stop: my onecheck (759 library runs with random starts, 500 random games; W = own Zielonka, σ and σ̄ winning) and
  REFEREE-2's (26,000 random 𝒞^1O stops, 1,509 library stops, 7,000 general-game stops): no failure on either engine. REFEREE-2 also
  records the OUT-1 corner; my probe did not count it.
- No disagreement in data.

### C.4 Result
- P-N5-1O: Theorem 1O-POLY, Lemma BIT, Lemma OUT and Corollary 1O-TIME are signed by both referees. One shared item OUT-1 = N-1O-1 (closed by
  its one-word repair); notes N-1O-2 (O(n¹⁷)), N-1O-3, N-1O-4, N-1O-5, N-1O-6, BIT-N1, 1O-N1, 1O-N2 for the fixes file. The R32 / R33
  start-freeness check is done by both.
- What it is: N5 solves 𝒞^1O games in polynomial time from any start pair, with correct regions and positional strategies (refereed-only;
  no Lean). What it is NOT: a TARGET.md §2 claim (TARGET.md §4: "Polynomial only on a restricted class"); 𝒞^1O is polynomial by other
  means; nothing transfers to games with two or more Odd choice vertices.
