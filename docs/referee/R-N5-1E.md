# R-N5-1E: REFEREE report on packet P-N5-1E (L-SI box 16: Lemma OUT-G on every game, BIT-G, Theorem 1E-POLY, Corollary 1E-TIME)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's GO of 03:41Z (Lead's stamp), item (b).
- Object: docs/si/P-N5-1E-box16.md at trunk 7fef9699, sha1 e613db131d3871c038f53fcb4e009c33f47ca20e (checked with
  `git show 7fef9699:docs/si/P-N5-1E-box16.md | sha1sum`; identical on my tree after merging trunk), 247 lines. Author: L-SI successor 11,
  frozen at l-si adb721b5. (My tree first held an older, unfrozen draft, sha1 630656e5…, from an earlier trunk; I merged trunk and reviewed
  the pinned text only.)
- Written 2026-10-26T03:44Z-04:19Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on P-N5-1E read (none existed on my tree at 03:44Z: `ls docs/referee-2 | grep -i 1e`
  empty). No lane code run or imported (experiments/si/out16/outcheck.py, experiments/new/n5.py not run). D1.
- Sources opened by me for this review: SPEC docs/new/N5-ssi-global.md (S1-S5, Q1-Q4); RESULTS R15 (c), (d), (iii), R18 (d), R21 (a),
  R36 (c), R51 (a)-(e), R54 (a)-(f); docs/si/P-N5-1O-box15.md §2, §3; docs/new/P-N5-DUAL-box43.md §0, Theorem MIRROR and its proof;
  docs/referee/R-N5-DUAL.md §C C.2; TARGET.md §1. VJ00 itself: BRICS RS-00-48, www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, downloaded
  2026-10-26, sha256 485a12de432a2a8c… (the file L-LIT T21 opened), text via pdftotext; read §2 (setting), §4.1-4.3 (play values, order,
  Ωσ), §5.2 (σ̄, Prop. 5.1, Lemma 5.2, (11)), §6 (procedure, Prop. 6.1, Theorem 6.2), and the statements of Lemma 5.8, 5.9, Prop. 5.10.
- Tool: scratch/onee_probe.py (own engine; any game). Logs scratch/onee_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §2 | Lemma OUT-G (every game): Iσ = ∅ ⇒ S5's output at σ is (W_E, W_O) with positional winning strategies σ on W, σ̄ on V ∖ W | SIGNED |
| §2 | premise (VJ) on every game: Ξσ ⊴ V_{σ,τ′} for every positional Odd τ′ (= R18 (d) Lemma S (a), R21 (a)'s parenthetical) | SIGNED (checked against VJ00's text: §1 below) |
| §3 | Lemma BIT-G (every game): R51 (c)'s cost bound with no class step | SIGNED (note 1E-N1: carry R51 (c)'s memoisation sentence into the statement) |
| §4 | Theorem 1E-POLY: on 𝒞^1E, any start pair, ITER ≤ (n(n − 1) + d_e)(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³); uniform form L(n) = T*(n, n², n, n), O(n¹⁷) | SIGNED |
| §5 | Corollary 1E-TIME: on 𝒞^1E, output (W_E, W_O) and positional winning strategies in poly(n + m) time at bit cost | SIGNED |
| §6 | gauntlet / G-N5T-3 (READING) | not signed; READING agreed with the standing premise named (§5 below) |
| §7 | DATA | not signed; not re-run (lane code); my own data in §6 |
No gap. Notes 1E-N1 (BIT-G statement wording), 1E-N2 ((VJ) confirmed from VJ00's text), 1E-N3 (the standing SPEC premise: S1's procedure
realises an optimal σ̄), 1E-N4 (DATA: OUT-G holds at every state with Iσ = ∅, Iτ ≠ ∅ included). TARGET.md diff: not a TARGET.md §2
claim. 𝒞^1E is a subclass that is polynomial by other means (Even has ≤ d_e positional strategies); TARGET.md §4 says that does not count.
OUT-G is a correctness lemma, not a running-time bound. G-N5-TIME stays OPEN for general games.

## 1. Premise (VJ) on every game (1E-N2)
- VJ00 §2: "We restrict ourselves to finite parity game graphs and for technical convenience we assume that every vertex has at least one
  out-going edge." No other restriction. §4.3: "Ωσ(v) = min⊴ {Θ(P) : P ∈ Playsσ(v)}, where Playsσ(v) is the set of plays starting from
  vertex v and consistent with σ." §5.2: σ̄(v) := a successor minimising Ωσ; Prop. 5.1 (Ωσ is locally progressive for σ, σ̄) and
  Lemma 5.2 (locally progressive for σ, τ ⇔ = Θστ) give "Ωσ = Θσσ̄ (11). Hence by definition of Ωσ we get that Θσσ̄ ⊴ Θστ, for all
  strategies τ for player ⊖." The packet's quotes match this text (up to typesetting).
- Nothing in §2-§5.2 restricts the number of choice vertices. So (VJ) holds on every game: for every positional σ and every positional
  Odd τ′, Ωσ ⊴ Θστ′ pointwise.
- SPEC S1 defines Ξσ as the valuation under "Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once)". The
  packet's argument that every such σ̄′ gives Θσσ̄′ = Ωσ is correct: Θσσ̄′ ⊴ Θσσ̄ = Ωσ by pointwise optimality, and Ωσ ⊴ Θσσ̄′ because
  the (σ, σ̄′)-play from v is in Playsσ(v). SPEC's order is VJ00's §4.2 order with p′ for VJ00's vertex order (Reward ±, MaxDiff
  rule = Q1's top-differing-bit rule, then length by the cycle node's side).
- This is the same point as my lane's R-N5-1O §5 / R-N5-FBRED §1 and REFEREE-2's N-1O-4, N-GD-2, N-FBRED-3, now checked against the
  source text. VERDICT: (VJ) SIGNED on every game.

## 2. Lemma OUT-G, step by step (the Lead's per-step class audit)
| step | claim | checked | class use |
| --- | --- | --- | --- |
| 0 | reward(c) ≥ 0 iff Ω(c) even; odd ⇒ ≤ −1 | SPEC S1: p′(v) = 2·rank(v) + (Ω(v) mod 2); reward = p′ if even, −p′ if odd. Even: 2·rank ≥ 0 (= 0 at rank 0); odd: −(2·rank + 1) ≤ −1. So OUT-1 = N-1O-1's "≥ 0" repair (R51 (d)) is built in ✓ | none |
| 1 | one-player cycle fact | D (vertices seen infinitely often) is strongly connected in H (from some point the play moves inside D). rank sorts by (Ω, v) (SPEC S1), so t := the top-ranked vertex of D with Ω = q is the max-rank vertex of D; a simple cycle C through t inside D exists (a self-loop if D = {t}); t is C's max-p′ vertex. π := a shortest H-path from v to C meets C only at its end. Fixed-player vertices on π ∪ C have one H-edge, the one π / C uses; mover vertices on π ∪ C occur once, so the choice is positional ✓. The play is the lasso π·C^ω, cycle node t ✓ | any finite graph |
| 2 | Even side, any σ | (VJ) (§1) with positional τ′ from step 1 on H = G_σ (Odd moves, Even fixed to σ: the σ-consistent plays of G are exactly the plays of G_σ); S1's order compares cycle-node rewards first, so V ⊵ Ξσ ⇒ reward(cn V) ≥ reward(λ(v)) ≥ 0 ✓ | (VJ): every game |
| 3 | Odd side, Iσ = ∅ | H = G_σ̄ is one-player in R36's sense ✓. R36's V_σ is SPEC S1's play valuation with S1's order (R36 setting line) ✓, and V_σ = Ξσ (S1: Ξσ is the (σ, σ̄)-valuation) ✓. R36's improving edge (x, y) with V_σ(y) ▷ V_σ(σ(x)) = SPEC S2's Iσ (S2 adds w ≠ σ(v), which strictness implies) ✓. R36 (c): V_{σ′} ⊴ V_σ for positional σ′; rewards first ⇒ odd cycle node ✓; step 1 with Even moving ✓ | R36 (c): every one-player game; G_σ̄ one-player on every game |
| 4 | regions, restriction | W_E ∩ W_O = ∅ by the one play consistent with both winning strategies ✓; "a σ-consistent play from W never enters V ∖ W" by steering then following σ̄ (the (σ, σ̄)-play from u ends in λ(u)'s odd cycle) ✓; symmetric ✓. Determinacy is not assumed ✓. S5 (SPEC l.59-60) outputs exactly W, σ on W, σ̄ on V ∖ W ✓ | definitions |
- One-Odd property used anywhere: NONE. I looked for every step that could use "one Odd choice vertex" in P-N5-1O §4's proof (R51 (d)):
  its only class-dependent citation was R21 (a), signed in the 𝒞^1O setting; OUT-G replaces it by (VJ) from VJ00 directly. Step 3's
  one-player game is G_σ̄, one-player for every G because σ̄ is positional. Iτ = ∅ is indeed not used (and my data test it, §6).
- The "In particular" sentence: N5 stops (R15 (d)) exactly when Iσ = Iτ = ∅ (SPEC S5), so OUT-G applies at the stop on every game ✓.
- TARGET.md §1 match: W_E / W_O are defined there with history-dependent strategies and max-parity, as OUT-G proves; priorities in
  {0..n} are ranked by SPEC S1 ✓.
- VERDICT: Lemma OUT-G SIGNED.

## 3. Lemma BIT-G (class audit of R51 (c)'s proof, P-N5-1O §3)
- I re-read P-N5-1O §3 line by line: representation and comparison (Q1); S1 steps (i)-(vi) as DFS / reverse search / restricted-graph
  searches / memoised longest path (Q3's acyclicity argument cites only S1's loop order and VJ00 Prop. 6.1 clause 4) / BFS / copies;
  one iteration = ≤ 4 S1 runs (Ξσ on G, Ξτ on G^d, the S4a dual arena, the S4b arena; G^d and the arenas have ≤ n vertices and ≤ m
  edges) + O(m·n) bits for S2, S4c; S3, S5. No line names o, d_o, 𝒞^1O or a count of choice vertices ✓.
- 1E-N1 (wording): the statement quotes R51 (c) but drops its last sentence, "The longest-path recursion of S1 (iv) is memoised, with the
  same outputs as SPEC's recursion (BIT-N1)". The proof uses it ("with BIT-N1"). Without memoisation SPEC's literal recursion over
  successors is not bounded by the stated cost. Repair: keep that sentence in BIT-G's statement. Not a gap (the proof has it).
- VERDICT: BIT-G SIGNED (with 1E-N1 for the fixes file).

## 4. Theorem 1E-POLY
- Quotes checked against docs/RESULTS.md: R54 (a) first sentence, (b), (c), (d) and the title fragment are verbatim; R51 (a)'s quote is
  verbatim with one ellipsis ("and R50 (h)'s landed chain,"); R15 (c), (d) quotes verbatim up to line wraps. P-N5-DUAL MIRROR (b)'s proof
  (packet l.68-77) applies (H-OF) only to G^d, at the first state of each N5^OF phase ✓; MIRROR (c)'s proof is per game and per state ✓.
- Step 1 ((H-N5) per game): P-N5-1O §2 step 3 bounds EVERY phase of every N5 run on a 𝒞^1O game H by T*(n, m, Δ, d_o), with f ≤ 2n² = F
  (R48 (i)) and R50 (h)'s chain non-decreasing in f; start-free by R51 (b) ✓. The first phase from a state x is a phase of the run from x ✓.
- Step 2 (monotonicity): from the formula (packet §1 = P-N5-1O §2 statement), d enters through X_SN (factor d + 1) and S_o = d(Θ + 1),
  Δ through N_Ξ (factor 3Δn⁴), m only through the factor m − n + 1 ≥ 1 (every vertex has a successor); every other quantity is a sum of
  products of non-negative terms in n and F = 2n². So T* is non-decreasing in m, Δ, d ✓. TARGET.md §1: E ⊆ V × V, so m ≤ n²; Δ, d_o ≤ n
  (self-loops count once) ✓. Hence T*(n, m, Δ, d_o) ≤ L(n) = T*(n, n², n, n) on every 𝒞^1O game with n vertices ✓. The packet's
  pointer to REFEREE's R-N5-DUAL §C C.2 (N-DUAL-3 row: "T* is non-decreasing in m, d_o, Δ") is correct.
- Step 3 (substitution table): G^d = owners swapped, Ω + 1, same ids and successor lists (R54 setting; P-N5-DUAL §0) ✓, so n, m, Δ are
  G's ✓; G^d's Odd choice vertices are G's Even choice vertices, so G^d ∈ 𝒞^1O with o = e and d_o(G^d) = d_e ✓; F = 2n² depends on n
  only ✓. T* has no other game input ✓. R51 (a)'s phase count is correctly NOT used (MIRROR (a)'s n(n − 1) + d_e is). Monotonicity is
  used only in f in the parameter form, and also in m, Δ, d in the uniform form, as the packet states ✓.
- Assembly: N5 run on G = mirror of the N5^OF run on G^d (DUAL, first sentence; the DUAL-1 repair concerns only the second sentence) ✓;
  ≤ n(n − 1) + d_e dual phases (MIRROR (a)) ✓; each ≤ L transitions (MIRROR (c) prefix + step 1) ✓; ≤ n(n − 1) + d_e − 1 boundary
  transitions ✓; every iteration a transition (R15 (d)) ✓. ITER ≤ (n(n − 1) + d_e)(L + 1) ✓.
- Orders: T* = O(m·Δ·d·n¹¹) (P-N5-1O §2 step 5); ITER = O(n²·m·Δ·d_e·n¹¹) = O(m·Δ·d_e·n¹³); with m ≤ n², Δ, d_e ≤ n: O(n¹⁷);
  L(n) = O(n¹⁵) ✓.
- VERDICT: Theorem 1E-POLY SIGNED (both forms).

## 5. Corollary 1E-TIME, and the §6 READING
- 1E-TIME: correctness by OUT-G at the stop; ≤ ITER iterations (1E-POLY); each O(n³(n + m)) word operations on O(log(n + m))-bit words
  with n-bit vectors counted as O(n) words (BIT-G); ranking O(n log n); S3 O(m); class test O(n + m). Total poly(n + m) at bit cost
  (TARGET.md §3) ✓. VERDICT: SIGNED.
- §6 READING (not signed): OUT-G's proof cites (VJ) = VJ00 (11) (Prop. 5.1, Lemma 5.2) and R36 (c); it does not use VJ00 Lemma 5.8, 5.9 or
  Prop. 5.10 (I checked the steps above and the VJ00 statements). So G-N5T-3 (R15 (iii)) would be answered on every game. I agree as a
  READING, with one standing premise named (1E-N3): OUT-G is about SPEC's Ξσ and σ̄ as SPEC S1 DEFINES them (optimal counterstrategy);
  that S1's procedure realises an optimal σ̄ is VJ00 §6 (Prop. 6.1, Theorem 6.2) plus SPEC's conformance to it, which I did not re-derive
  (the code's match is DATA, R15 G-N5T-1). Every landed N5 result, R51 (d) included, carries the same premise; the packet names it
  (§6 honest limit (iii)). Whether to close the gap row is the Lead's call.

## 6. Data (DATA, not proof; scratch/onee_probe.py, own engine; logs scratch/onee_logs/)
Checks (own definitions, own engine rl_engine via dual_probe.run5 = plain N5 with a start pair; own Zielonka from onecheck.py):
OUTG_W / OUTG_SIG / OUTG_BAR at EVERY state of the run with Iσ = ∅ (OUT-G's only hypothesis), not just at the stop; STOP (the run ends
with Iσ = Iτ = ∅); on 𝒞^1E: ITER1E (ITER ≤ the §4 parameter-form bound, onecheck.bound with d := d_e) and SIGCH (σ changes ≤ d_e − 1,
MIRROR (a)). Mutation control MUT: the three output checks with σ read at the START state.
| set | runs | 𝒞^1E runs | states with Iσ = ∅ (with Iτ ≠ ∅) | max ITER (𝒞^1E) | max σ-changes on 𝒞^1E (runs at d_e − 1) | MUT bites | failures |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games; 45 with n > 64 skipped), S3 + 2 random starts | 1,101 | 24 (8 games) | 1,464 (363) | 115 (2) | 2 (11) | 777 | 0 |
| random 𝒞^1E (dual of a random 𝒞^1O game), n 4-14, seed 21, S3 + 2 random | 9,000 | 9,000 | 16,643 (7,643) | 7 (7) | 3 (1,276) | 1,778 | 0 |
| random 𝒞^1E, n 15-30, seed 22, S3 + 1 random | 2,000 | 2,000 | 5,283 (3,283) | 8 (8) | 3 (320) | 246 | 0 |
| random games with 0-4 Odd choice vertices, n 4-14, seed 23, S3 + 2 random | 9,000 | 822 | 11,418 (2,418) | 7 (4) | 2 (109) | 4,232 | 0 |
- 1E-N4: OUT-G holds at 34,808 states with Iσ = ∅, of which 13,707 have Iτ ≠ ∅ (not stops): the data agree with "Iτ = ∅ is not used".
- Own Zielonka vs Oink 8fbf0a7 --zlk on the 8 lib41 𝒞^1E games: 8 / 8 agree (onee_logs/oink_vs_zielonka_1e.txt; onee_oink.py). On the
  wider library my Zielonka agrees with Oink on 109 files (one_logs/oink_vs_zielonka.txt, R-N5-1O).
- lib41 holds 8 𝒞^1E games (onee_logs/lib41_1e_files.txt); the packet's §7 "16" counts runs (8 games × S3 + 1 random): consistent.
- Thin: random 𝒞^1E runs are short (ITER ≤ 8); the bound is far above every count. The ITER1E check is therefore weak; the theorem
  rests on its proof (§4). Mutation controls bite on every set.
- Reproduce (from docs/referee/scratch): `sh onee_logs/run_all.sh` (fixed seeds; file starts seeded by the RELATIVE path, so runs
  reproduce from any worktree); `python3 -I onee_oink.py <tmpdir> $(cat onee_logs/lib41_1e_files.txt)`.

## 7. Notes for the fixes file
- 1E-N1: BIT-G's statement should keep R51 (c)'s sentence on the memoised longest-path recursion (BIT-N1).
- 1E-N2: (VJ) on every game is checked against VJ00's text (§2, §4.3, §5.2 (11)); a landing note may record it against R18 (d) S (a)
  and R21 (a).
- 1E-N3: standing premise (S1's procedure realises SPEC's optimal σ̄; VJ00 §6 + SPEC conformance, code DATA); name it in the landing entry.
- 1E-N4: DATA: OUT-G checked at every state with Iσ = ∅, including states with Iτ ≠ ∅.

## §C. Comparison with REFEREE-2 (REFEREE successor 12; written 2026-10-26T04:31Z-04:31Z by date -u; (Opus 5.5, D15))
- Routing: the Lead's message of 04:30Z (Lead's stamp), item (1). Objects: this report (c82c4ecf, §1-§7 above unchanged) and
  docs/referee-2/R2-N5-1E.md (referee-2 ceed1f63, successor 13), read after c82c4ecf was pushed. Both reviewed the same pinned text
  (sha1 e613db13…, trunk 7fef9699). Both opened VJ00 independently (same sha256 485a12de…).

### C.1 Verdicts side by side
| § | statement | REFEREE (c82c4ecf) | REFEREE-2 (ceed1f63) | joint |
| --- | --- | --- | --- | --- |
| §2 | premise (VJ) on every game | SIGNED (1E-N2) | SIGN (N-1E-1, N-1E-2) | signed |
| §2 | Lemma OUT-G (every game); class audit table | SIGNED; audit checked | SIGN; audit CHECKED | signed |
| §3 | Lemma BIT-G (every game) | SIGNED (1E-N1 wording) | SIGN | signed; wording 1E-N1 |
| §4 | Theorem 1E-POLY (parameter and uniform forms); G^d table | SIGNED; table checked | SIGN (N-1E-3, N-1E-4); table CHECKED | signed |
| §5 | Corollary 1E-TIME | SIGNED | SIGN | signed |
| §6, §7 | READING, DATA | not signed; §6 agreed with premise 1E-N3 | not signed; §6 concur (N-1E-5) | not signed; READING agreed by both |
No disagreement. Neither report has a gap or a NOT SIGNED statement. Both: not a TARGET.md §2 claim (𝒞^1E is a restricted class,
TARGET.md §4); G-N5-TIME OPEN for general games.

### C.2 Joint note map
| REFEREE | REFEREE-2 | relation | joint status |
| --- | --- | --- | --- |
| 1E-N1 (BIT-G statement drops R51 (c)'s memoisation sentence, BIT-N1; the proof uses it) | — (R2 §1: "R51 (c) as restated in §3: the landed text with 'on every parity game' added ✓") | ADDITIONAL from us. Re-checked now: R51 (c) (RESULTS l.2587-2590) ends "The longest-path recursion of S1 (iv) is memoised, with the same outputs as SPEC's recursion (BIT-N1)."; the packet's §3 statement has no such sentence (its proof does: "with BIT-N1"). R2 compared the restatement against the landed text and did not flag the dropped sentence. | fixes file: keep the sentence in BIT-G's statement (wording; not a gap) |
| 1E-N2 ((VJ) checked against VJ00 §2, §4.3, §5.2 (11)) | N-1E-2 (same quotes, same PDF) | SAME; two independent reads of the source agree | landing note |
| 1E-N3 (standing premise: S1's PROCEDURE realises SPEC's optimal σ̄; VJ00 §6 + SPEC conformance; code DATA) | N-1E-1 (same: "S1's procedure computing an optimal σ̄ stays SPEC's requirement (VJ00 §6), as in R51, with the code DATA") | SAME | name it in the landing entry |
| §4 assembly per game (MIRROR (b)'s proof applies (H-OF) only to G^d; (c) per state) | N-1E-4 (parameter form uses R54 (c), (d)'s PROOFS per game; written out by the packet) | SAME substance | proved, not a reading |
| §4 step 2: the pointer to R-N5-DUAL §C C.2 checked (N-DUAL-3 row: "T* is non-decreasing in m, d_o, Δ"); the §2 quote of C.2 checked verbatim ("Lemma OUT's proof uses R36 (c) ... I see no 𝒞^1O step in it.") | N-1E-3 (not verified by R2, independence; not needed) | CLOSED by us: both REFEREE lines exist as quoted (docs/referee/R-N5-DUAL.md l.138); both referees also checked monotonicity directly | closed |
| §5 READING on G-N5T-3, with premise 1E-N3 | N-1E-5 (concur) | SAME | READING agreed; closing the gap row is the Lead's call |
| 1E-N4 (DATA: OUT-G at every Iσ = ∅ state, Iτ ≠ ∅ included) | — (R2 checks at stops, with enumerated counter-strategies and O2: play value = S1's Ξσ) | complementary data | DATA |

### C.3 Data
| item | REFEREE | REFEREE-2 | agree? |
| --- | --- | --- | --- |
| random 𝒞^1E | 11,000 runs (n 4-30); max ITER 8 | 7,500 runs (n 4-30); max ITER 6 | YES (shape; different seeds and generators) |
| random any class | 9,000 runs (0-4 Odd choice vertices) | 4,000 runs | YES |
| lib41 | 1,101 runs (n ≤ 64), 24 𝒞^1E runs (8 games) | 824 runs (412 files × 2), 16 𝒞^1E runs | YES (8 𝒞^1E games; 16 = 8 × 2 starts) |
| what is checked | OUT-G at all 34,808 Iσ = ∅ states (13,707 with Iτ ≠ ∅); ITER, σ-changes on 𝒞^1E; MUT control | at stops: play = Ξσ, W = Zielonka, both strategies win against enumerated positional counter-strategies; ITER, MON, MIRROR (a); REW0 corner 1,061 stops; three mutation controls | complementary; 0 failures in both |
| Zielonka cross-check | own Zielonka = Oink --zlk on the 8 lib41 𝒞^1E games | own Zielonka (R2-N5-1O) | — |
Both: runs are short; the bound is far above every count; the theorem rests on its proof.

### C.4 Joint state (for the Lead and CHECKER)
- All five to-sign items are signed by both referees; no gap.
- Fixes file: 1E-N1 (BIT-G statement keeps the memoisation sentence).
- Landing notes: (VJ) on every game checked against VJ00's text by both (1E-N2 = N-1E-2); standing premise 1E-N3 = N-1E-1.
- READING (both, not signed): with OUT-G, G-N5T-3's output half holds on every game under the standing premise.
