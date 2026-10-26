# R2-N5-DUAL: second-referee check of packet P-N5-DUAL (L-NEW box 43: Lemma DUAL, Theorem MIRROR (implication), Corollary Φ-kO, Lemma ENDGAME). REFEREE-2 (successor 13), written 2026-10-26 01:30Z-01:4xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue item 4 (brief: "P-N5-DUAL (docs/new/P-N5-DUAL-box43.md, a51f7c30, pinned trunk df073cb5)").
Object: docs/new/P-N5-DUAL-box43.md, `git show df073cb5:docs/new/P-N5-DUAL-box43.md | sha1sum` -> a51f7c30c267a4c02088cf2c849388e28c4121fa
(= the brief; = my tree), 150 lines (L-NEW successor 22). No fixes file for box 43 DUAL in my tree.
Background read (texts, not recalled): SPEC S1-S5, FIX 1-4 (Odd's side "on the DUAL game G^d (owner swapped, Ω + 1)"); n5.py l. 18
(dual: priorities + 1, owners swapped, same successor lists); RESULTS R15 (c), (d), R38 (a), R47 (whole entry); R18 (d) Lemma S and its
source docs/new/N5-time-box21.md §2.1 Lemma R, §2.2; P-N5-X §3 FBL-N.
Independence: docs/referee/R-N5-DUAL.md and docs/referee/scratch/dual_probe.py, dual_climb.py, dual_logs/ EXIST (names seen by `ls`);
none opened. No grep of docs/agents/ or RESULTS for this packet. The lane's experiments/new/box43/mirror.py, dblfb.py, dualsym.py were
not run or imported; experiments/new/box41/lib41.txt (a file list of 2026-10-25 18:29Z, before this packet; its two docs/referee entries
are game files of the old L2 packet) was used as input only.
Tools (own code, docs/referee-2/R2-N5-DUAL/): dual_check.py (own N5 loop from SPEC on L-SI's si.py engine, with an Odd-first flag),
run_all.sh, logs/.
Labels: PROVED (L-NEW 22). Theorem MIRROR (b) is an IMPLICATION from (H-OF). Not a running-time bound, not a TARGET.md claim.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| Lemma DUAL (every game) | SIGN | N-DUAL-1 (wording of the second sentence: agreement is up to and including state j, first possible difference j + 1) |
| Theorem MIRROR (a) (𝒞^1E: σ changes ≤ d_e − 1, ≤ n(n − 1) + d_e dual phases) | SIGN | — |
| Theorem MIRROR (b) (implication (H-OF) ⇒ the 𝒞^1E iteration bound) | SIGN as an implication | N-DUAL-3 (READING: (H-N5) now holds via P-N5-1O) |
| Theorem MIRROR (c) ((H-N5) ⇒ (H-OF)) | SIGN | — |
| Corollary Φ-kO (every game) | SIGN | — |
| Lemma ENDGAME (every game) | SIGN | — |
| §2 table ("to check", not to sign) | partly checked | N-DUAL-2 (which rows are covered by the start-freeness audits) |
| §3 | not signed (as briefed) | — |
No statement is NOT SIGNED and no gap is open. No (P). TARGET.md diff: not a claim of TARGET.md §2 (no running-time bound is proved; MIRROR
(b) is conditional; Φ-kO and ENDGAME are structural).

## 1. Lemma DUAL: SIGN
- (E) ✓. SPEC S1 reads Ω only through rank = position in V sorted by (Ω(v), v) and Ω mod 2 (p′, reward, the "Ω(u) even / odd" split of the
  VJ procedure, the length rule); Ω + 2 preserves both. Successor and predecessor lists are by index. So S1's outputs (valuations,
  improving sets, optimal counterstrategies with their tie-breaks) are invariant under Ω ↦ Ω + 2. (G^d)^d = G with Ω + 2 and the original
  owners ✓.
- (S2) ✓: N5 on G′ := G^d computes its Even set on G′ for τ (= N5's Iτ on G^d) and its Odd set on G′^d = G(Ω + 2) for σ (= Iσ by (E)).
- (S4a on G^d) ✓: arena H″ = G^d with G-Odd vertices restricted to {τ(v)} ∪ Iτ(v), G-Even fixed to σ; the new G^d-Even strategy is Odd's
  optimal counterstrategy in dual(H″) to σ; dual(H″) is N5's S4b arena H′ with Ω + 2, and N5's S4b output is "Odd's optimal counterstrategy
  (S1 on H′) to σ"; equal by (E).
- (S4b on G^d) ✓: arena H‴ = G^d with G-Even vertices restricted to {σ(v)} ∪ Iσ(v), G-Odd fixed to τ; output = S1 on H‴ itself to τ. H‴ is
  literally dual(H) for N5's S4a arena H (Ω + 1, owners swapped), and N5's S4a is S1 on dual(H) to τ: the same computation, no (E) needed.
- (S4c) ✓: N5 on G falls back Even-first; N5^OF on G^d falls back "Odd first", and G^d's Odd is G's Even, whose set is Iσ: same side. Targets:
  (Ξσ(w), w) maximal, Ξσ on G vs on G(Ω + 2) (equal by (E)); for G's Odd side Ξτ on G^d in both. FIX 3 in both ✓. Stop rule symmetric ✓.
- Second sentence ✓ in substance: N5 and N5^OF on G^d differ only at fallbacks with both improving sets non-empty, which on G^d are Iτ and
  Iσ, i.e. G's two-sided fallbacks; up to the first one, j → j + 1, the states 0..j coincide.
- N-DUAL-1 (wording): the sentence says the plain run "agrees with that mirror up to and including the state right after the first two-sided
  fallback's source, i.e. it can differ first at state j + 1". The state right after the source IS j + 1; the intended (and proved, and
  observed) statement is "up to and including the source state j; it can differ first at j + 1". One-line fix.

## 2. Theorem MIRROR: SIGN ((b) as an implication)
- (a) ✓. On 𝒞^1E, σ is determined by σ(e). Every σ change is Switch_I(σ) with ∅ ≠ I ⊆ Iσ (S4a's arena, S4c's switch-all; R15 (d)), so by
  R15 (c) the distinct σ's form a strict ≺_G-chain: no σ repeats, ≤ d_e values, ≤ d_e − 1 changes. A dual phase ends at a λ^U-change
  (≤ n(n − 1), R47 (a) Lemma Φ (c)) or a σ-change: ≤ n(n − 1) + d_e dual phases ✓.
- (b) ✓. G ∈ 𝒞^1E ⇒ G^d ∈ 𝒞^1O with Odd choice vertex e. By DUAL the N5 run on G is the mirror of the N5^OF run on G^d. A dual phase of the
  G-run (λ^U, σ constant) is a phase of the G^d-run: G^d's Even strategy is G's τ and its λ is the cycle-node map of Ξ_τ on G^d, which is
  λ^U (R38 (a) setting: U_τ = Odd's valuation of τ in G^d); G^d's Odd strategy is σ ✓. N5^OF is memoryless, so (H-OF) at each phase's first
  state bounds each phase; ≤ (#phases)(L(n) + 1) ✓.
- (c) ✓. From x on G^d ∈ 𝒞^1O, N5^OF and N5 coincide up to the first two-sided fallback; there N5^OF switches Odd's strategy on a non-empty
  improving set, changing τ, so that transition ends the phase. Hence the first N5^OF phase is a prefix of (or equal to) the first N5 phase
  from x, and (H-N5) bounds it ✓.

## 3. Corollary Φ-kO and Lemma ENDGAME: SIGN
- Φ-kO ✓: τ is determined by its values at the Odd choice vertices; every τ change is a non-empty improving switch on G^d (R15 (d)), so no τ
  repeats (R15 (c) on G^d), ≤ ∏ deg(o_i) distinct τ's; a phase ends at a λ-change (≤ n(n − 1), R47 (a)) or a τ-change ✓. Mirror ✓ (σ, λ^U).
  𝒞^kO: ∏ deg(o_i) ≤ n^k ✓.
- ENDGAME ✓: Iσ depends on σ alone (R15 (d)); Iσ = ∅ ⇒ S4a keeps σ, S4c falls back for Odd only ⇒ σ_{k+1} = σ_k with Iσ again ∅. Mirror: Iτ = ∅
  ⇒ S4b keeps τ, and S4c's Odd branch needs Iτ ≠ ∅ (FIX 3: an Even fallback changes only σ) ✓.

## 4. The §2 table (to check, not to sign)
- N-DUAL-2. The rows that the 𝒞^1O iteration chain uses (R15, R21 (a), R22, R24 (e), R27 (d), (g), R30 (c), R32-R34, R36, R38 (a), R47, R48,
  R50) are now covered, statement and proof, by REFEREE's R-N5-START §1 + Addendum 1 (R32 / R33 line by line) and my R2-N5-1O §3 (R32, R33,
  R34 (b)-(f) line by line; P-N5-1O signed by both referees). The other rows (R17-R20, R23, R25, R26, R28, R29, R31, R35, R37, R39-R46)
  were not checked here; MIRROR does not need them once (H-N5) is taken from P-N5-1O (N-DUAL-3).
- The table's "N5^OF" column ✓ as a reading: an in-phase N5^OF transition is an N5 transition from the same state (N5^OF's extra kind of
  transition, the Odd fallback at a two-sided fallback, changes τ and so ends the phase), and MIRROR (c) is the only place where the
  transfer is used.
- In-review row "P-N5-FX, P-N5-KW, P-N5-NH-box42": KW has landed (R50); FX and NH-box42 are now reported by REFEREE-2 (SIGN); none of the
  three is needed for (H-N5) beyond R50 (h), which P-N5-1O uses.

## 5. N-DUAL-3 (READING, not signed): (H-N5) is now available
P-N5-1O (Theorem 1O-POLY, signed by both referees, R2-N5-1O §C) bounds EVERY phase of every N5 run on 𝒞^1O, from every start pair, by
T*(n, m, d_o, Δ) ≤ T*(n, n², n, n) = O(n¹⁵) transitions (its step 3, start-free by R-N5-START + Addendum 1 + R2-N5-1O §3). That is (H-N5) with
L(n) := T*(n, n², n, n). With MIRROR (b), (c): N5 on every 𝒞^1E game makes ≤ (n(n − 1) + d_e)(L(n) + 1) = O(n¹⁷) iterations from every start
pair. Output correctness on 𝒞^1E would need Lemma OUT beyond 𝒞^1O (P-N5-1O §4's game-independence READING) and the bit cost is Lemma BIT
(game-free). This is an assembly for the Lead to packet; nothing here signs it.

## 6. DATA (dual_check.py; own N5 loop; starts: S3 + random for files, random for the random sets)
| set | runs | DUAL1 (N5 on G = mirror of N5^OF on G^d) | runs with two-sided fallbacks (fallbacks) | DUAL2: plain mirror first differs at j + 1 / earlier | MIRC (𝒞^1O, random x) | violations |
| --- | --- | --- | --- | --- | --- | --- |
| lib41.txt (412 files, any class), S3 + 1 random | 824 | 824 | 33 (88) | 33 / 0 | 506 | 0 |
| R2-N5-KW/files.lst (503 𝒞^1O files), S3 + 1 random | 1,006 | 1,006 | 33 (170) | 33 / 0 | 1,006 (1 strict prefix) | 0 |
| random 𝒞^kO (any owners) n 4-14 | 2,000 | 2,000 | 0 | — | 277 | 0 |
| random 𝒞^1E n 4-14 | 2,000 | 2,000 | 0 | — | 261 | 0 |
| random 𝒞^1O n 4-14 | 2,000 | 2,000 | 0 | — | 2,000 | 0 |
Also checked on every run: ENDGAME (both sides), Φ-kO (no τ / σ repeat; distinct counts ≤ the products; phases and dual phases ≤ the bounds),
and on 𝒞^1E runs (2,000 random + 38 library) MIRROR (a); 0 violations. Maxima: distinct τ 38 (wide_h16.pg), phases 48 (sym_h16_s1.pg),
dual phases 116 (xsn91_n48.pg); MIRROR (a)'s σ-change bound d_e − 1 is attained (ratio 1.0).
- Independent reproduction of the packet's figure: on lib41 from the S3 start (the mutation logs run S3 only), my loop finds exactly 15 runs
  with a two-sided fallback and 54 such fallbacks, as the packet reports; in all 15 the plain mirror first differs at j + 1.
- Mutation controls (lib41, S3): plain (DUAL1 with plain N5 on G^d) fails on exactly those 15 runs; phi (Φ-kO with ∏ − 1) 36; endg (ENDGAME
  asks σ to change) 163.
- Random games never produced a two-sided fallback; DUAL's second sentence is exercised only by the 66 library runs.

## 7. Notes (none blocks a signature)
- N-DUAL-1 (wording): Lemma DUAL's second sentence, "the state right after the first two-sided fallback's source" → "the first two-sided
  fallback's source j".
- N-DUAL-2 (§2 table): rows used by the 𝒞^1O chain are covered by R-N5-START (+ Addendum 1) and R2-N5-1O §3; other rows unchecked here.
- N-DUAL-3 (READING): with P-N5-1O signed, (H-N5) holds with L(n) = T*(n, n², n, n), so MIRROR gives an O(n¹⁷) iteration bound on 𝒞^1E
  (to be packeted; output correctness there is a separate step).

## §C (2026-10-26 01:5xZ by date -u; REFEREE-2 successor 13, Opus 5.5, D15): comparison with REFEREE's R-N5-DUAL
Read after my report was pushed (73c2b4a1, on trunk d7d9d7d2): docs/referee/R-N5-DUAL.md (sha1 fbbb4d92…, REFEREE successor 11). Lead 01:52Z.
| statement | REFEREE | REFEREE-2 | same? |
| --- | --- | --- | --- |
| DUAL, first sentence | SIGNED | SIGN | yes |
| DUAL, second sentence | SIGNED WITH GAP DUAL-1 (wording) | SIGN, N-DUAL-1 (the same wording point) | yes in substance (C.1) |
| MIRROR (a) | SIGNED | SIGN | yes |
| MIRROR (b) | SIGNED as an implication | SIGN as an implication | yes |
| MIRROR (c) | SIGNED | SIGN | yes |
| Φ-kO | SIGNED | SIGN | yes |
| ENDGAME | SIGNED | SIGN | yes |
| §2 table | READING checked, rows spot-checked, no proof audit | partly checked (N-DUAL-2) | yes (C.2) |
- C.1 Joint gap map: DUAL-1 = N-DUAL-1, found independently, same repair ("agree on states 0, …, j; the first possible difference is at state
  j + 1"). I ACCEPT REFEREE's grading as a wording gap closed by that one line; the second sentence is then signed by both.
- C.2 §2 table / (H-N5). REFEREE (23:05Z-23:30Z) left the proof-by-proof start audit open and called (H-N5) "the open 𝒞^1O per-phase
  question". Since then: R-N5-START + Addendum 1 (REFEREE) and my R2-N5-1O §3 audited, line by line, every row the 𝒞^1O chain uses, and
  P-N5-1O (Theorem 1O-POLY, signed by both, R2-N5-1O §C) bounds every phase from every state by T*. So (H-N5) holds with L(n) =
  T*(n, n², n, n) (my N-DUAL-3, READING; the Lead is routing it as an assembly packet). The rows the chain does not use stay unaudited
  in both reports. No disagreement: REFEREE's text predates P-N5-1O.
- C.3 Data: both independent engines reproduce the packet's two-sided-fallback figures (REFEREE: 14 runs / 51 on the 367 lib41 files with
  n ≤ 64; mine: 15 / 54 on all 412 files, = the packet's), first plain-mirror difference exactly at j + 1 in every such run, prefix property
  (MOFC / MIRC) on every sampled state; REFEREE's climbs (135,671 runs with two-sided fallbacks) cover my thin spot (66 library runs).
  REFEREE also tested Ω + 2 invariance directly (OM2); I did not — accepted as additional evidence.
- C.4 Result: verdicts identical in substance; joint gap list DUAL-1 = N-DUAL-1 (closed by the one-line repair). Nothing open.
