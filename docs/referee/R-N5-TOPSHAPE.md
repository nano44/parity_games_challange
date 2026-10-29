# R-N5-TOPSHAPE: REFEREE report on packet P-N5-TOPSHAPE (L-NEW box 49: Fact DELTA, Lemma TOP-SHAPE (a)-(c), Corollary)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 2026-10-29 05:06Z by date -u).
- Object and pin: docs/new/P-N5-TOPSHAPE-box49.md, sha1 c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f, 81 lines, author L-NEW successor 30: the same
  sha1 at l-new 4c2ea43e (an ancestor of origin/claude/l-new) and at the l-new head. Quote base e2da18b0.
- Runs 2026-10-29 after 05:11Z; report written 2026-10-29T05:23Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ file on TOPSHAPE on my tree, on origin/claude/referee-2 or on trunk at 05:13Z (0 / 0 / 0, names, same turn as
  the fetch). No lane code run (experiments/new/box49/topmono.py, quotecheck3.py untouched). D1.
- Premises read against their text: SPEC S1 (valuation (c, P, ℓ), P ⊆ ranks above c, order: reward, signed weight, length) and Q1 (the
  symmetric-difference form of the weight order); RESULTS R15 (a), (d) as (MON); R38 (a) (phase); R56 (a) (INJ).
- Quotes: 2 of 2 verbatim (own scratch/flip_quotes.py).
- Tool: scratch/topshape_probe.py (sha1 b9c0d284…; own engine rl_engine; path sets are bit masks over ranks, so top = the highest set bit).
  Logs scratch/top_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Fact DELTA | SIGNED |
| §1 | Lemma TOP-SHAPE (a) top rises only to an even rank; (b) an even top never falls; (c) the shape (odd tops fall or stay until replaced; once even, even and non-decreasing; ⊥ only before the even run) | SIGNED |
| §1 | Corollary: ≤ n − 1 top changes per vertex per phase | SIGNED |
| §1 | Reader-proofness sentence (READING) | not signed; true as a consequence of the Corollary (it holds on every game, readers included) |
| §2, §3 | data; TOP-MONO in the Δ form DEAD | not signed; §3's instance reproduced (TOP-MONO Δ-form is false) |
No gap. Notes TOP-N1..N3. Bounds top changes only; the P-changes under a fixed top are not bounded (up to 71 per vertex per phase, reproduced);
not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Proofs re-derived
- Fact DELTA ✓: weight(B) − weight(A) = Σ_{B∖A} s(r)2^r − Σ_{A∖B} s(r)2^r; the term at d = max(A Δ B) exceeds the sum of all lower ones in absolute
  value (Σ_{r<d} 2^r < 2^d), so its sign decides ✓. It is SPEC's Q1 rule stated per pair ✓. ("of one class" is not needed.)
- Strict rise ✓: (MON) gives Ξ_{t+1}(v) ⊵ Ξ_t(v) at every transition (R15 (d) covers S4a and S4c). The cycle node is λ(v), constant on the phase,
  so the order compares weights next; P_t ≠ P_{t+1} gives distinct weights (INJ: distinct sets of distinct powers of two), so the weight rises
  strictly ✓. (INJ is landed per honest class in R56 (a); the fact itself is general.)
- (a) ✓: top_{t+1} > top_t puts u′ = top_{t+1} in P_{t+1} ∖ P_t with nothing above it in either set, so d = u′; a strict rise with d in the new set
  needs d even (DELTA) ✓. Also from ⊥ ✓.
- (b) ✓: an even top u of P_t with top_{t+1} < u (⊥ included) gives d = u ∈ P_t ∖ P_{t+1}; DELTA says the weight falls; contradiction ✓.
- (c) ✓ from (a), (b): from even, the next top is ≥ it and even; from ⊥, a change makes the top > ⊥, hence even; from odd, a rise lands on an
  even rank, else the top stays or falls (to a lower odd rank, ⊥ or a lower even rank) ✓.
- Corollary ✓: the sequence of distinct tops is a strictly decreasing run of odd ranks, then at most one ⊥, then a strictly increasing run of
  even ranks, so no value recurs; the values are ranks above rank(c) (at most n − 1 of them) and ⊥; so at most n values and n − 1 changes ✓.
  A top changes only at a P-change, which the Lemma covers ✓.

## 2. Data (scratch/top_logs/; 0 failures in every MUT=0 run)
| set | runs | P-changes (DELTA checks) | (v, phase) pairs with a P-change | (a) / (b) checks | max top changes per (v, P) (/ n) | max P-changes per (v, P) | max Δ-top rises |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib1140 (fbc_lib.txt, n ≤ 40; given + S3 + 1 random) | 1,857 | 56,473 | 17,882 | 5,572 / 6,858 | 9 (0.37) | 60 | 27 |
| lib41 (n ≤ 48; given + S3 + 2 random) | 1,076 | 58,143 | 15,873 | 3,612 / 4,694 | 10 (0.28) | 37 | 19 |
| L-RED instances (red/*/instances, 316 games, n ≤ 200, given or S3) | 316 | 29,196 | 8,083 | 2,756 / 5,248 | 48 (0.30) | 62 | 47 |
| random rand_ck, n 6-24, k ≤ 6 | 12,000 | 3,286 | 3,224 | 1,209 / 625 | 2 (0.22) | 2 | 1 |
| long121_n40 (box48, its .start) | 1 | 769 | 39 | 9 / 54 | 7 | 44 | 20 |
- Checked at every P-change: DELTA's iff, the strict rise, the cycle node unchanged, (a), (b), (c) ("once even, even"), and per (v, P) the shape
  of the distinct-top sequence and the Corollary's bound: 0 failures on 147,867 P-changes and 45,101 (v, P) pairs.
- Packet figures reproduced: red/ul ladderd0_k48_n156 has 48 top changes for one vertex in a phase (my max 48, with 47 Δ-top rises), as §2;
  l121reader_n41 (si/root/instances, its .start) has 71 P-changes of one vertex in one phase, as stated.
- §3 reproduced: long121_n40 at its .start, phase [1, 122], vertex 0: Δ-tops at its P-changes begin 35, 37, 32, 33, 26, 39, 21, 29, 33, 36 (exactly
  §3's list); its distinct tops 39, 38, 37, 36, 35, 26, 14 (TOP-SHAPE's shape). TOP-MONO in the Δ form is false (DEAD confirmed).

## 3. Mutation controls (scratch/top_logs/mut*_lib41.txt)
| MUT | change | result |
| --- | --- | --- |
| 1 | (a) demanded with ODD (a rise lands on an odd rank) | BITES: 3,612 of 3,612 rises |
| 2 | Corollary with n − 2 | does NOT bite (max 0.37 n): the n − 1 bound is far from reached (TOP-N2) |
| 3 | TOP-MONO in the Δ form (Δ-tops non-increasing) demanded | BITES: 7,305 (vertex, phase) pairs (§3's DEAD verdict) |

## 4. Notes (for L-NEW's fixes file; none changes a verdict)
- TOP-N1 (§3 count). For long121_n40, phase [1, 122], vertex 0, I count 17 rises of the Δ-top (over its 35 P-changes), not §3's "20 rises in the
  phase"; 20 is my maximum over all vertices of that run. The list's first ten values agree exactly. Either §3 means the run's maximum, or it
  counts rises differently (say how). Not to sign.
- TOP-N2 (thin spot). The Corollary's n − 1 is never approached in data (max 0.37 n; 48 at n = 156). The bound is correct by proof; MUT=2 does not
  bite. Whether n − 1 is attained by some game is open (an odd run down all odd ranks, then the even ranks upward).
- TOP-N3 (premise wording). (INJ) is cited from R56 (a), where it is stated per honest class; the packet uses it as the general fact that
  distinct sets of ranks have distinct signed weights, which is immediate (Fact DELTA itself gives it). "Of one class" in Fact DELTA is not
  needed. Cosmetic.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-TOPSHAPE.md (this file), scratch/topshape_probe.py, scratch/top_logs/.
- FINDINGS: Fact DELTA, TOP-SHAPE (a)-(c) and the Corollary (≤ n − 1 top changes per vertex per phase) all SIGNED, no gap; TOP-MONO's Δ form DEAD
  confirmed on §3's instance; the Δ-rise count for vertex 0 is 17, not 20 (TOP-N1); the bound is far from tight in data (TOP-N2).
- NEEDS: Lead: the TOPSHAPE §C word when REFEREE-2 reports; route TOP-N1..N3 to L-NEW.

## §C. Comparison with REFEREE-2 (written 2026-10-29T05:32Z by date -u, after the Lead's word of 05:31Z; REFEREE-2's report
docs/referee-2/R2-N5-TOPSHAPE.md, sha1 e409e443…, commit 97db54fc; read only after this report was pushed at 1a6d6a24)
Written by REFEREE successor 17, the author. Every verdict is labelled (Opus 5.5, D15).
- Independence: both clean (REFEREE-2: names-only counts, 0 TOPSHAPE files of mine at its push; I: 0 / 0 / 0 at 05:13Z, none opened).
- Verdicts identical: Fact DELTA, TOP-SHAPE (a)-(c) and the Corollary SIGNED by both; §3's Δ-form TOP-MONO DEAD confirmed by both on the same
  instance (long121_n40, vertex 0, phase [1, 122], Δ-tops 35, 37, 32, 33, 26, 39, 21, 29, 33, 36). Quotes 2/2 both. Joint gap map: EMPTY.
- N-TS-1 SETTLED (Lead's question): a STRENGTHENING, not part of the signed statement. The packet's Lemma and Corollary are stated for
  transitions and runs inside one phase, and that is what both referees sign. N-TS-1's wider form ((a), (b) at every N5 transition at which
  λ(v) is unchanged, phase-leaving ones included; the Corollary per maximal run with λ(v) constant) is TRUE: I re-derive it (the proof uses
  only (MON), valid at every iteration since Ξ depends on σ alone, R15 (a), (d); the unchanged cycle node; and (INJ)), and my engine agrees,
  0 failures at 9,202 off-phase P-changes with λ(v) unchanged (scratch/ts_wide.py; top_logs/wide_lib41.txt 2,091, wide_lib1140.txt 7,111;
  REFEREE-2: 115,702). Both referees have therefore proved and checked it; it can land as a referees' remark in the entry, or as a signed item
  if the lane states it in its fixes file (no further review needed beyond reading the wording).
- Notes matched:
  - TOP-N1 = N-TS-3 (17 rises for vertex 0, not 20; 20 is the run's maximum, REFEREE-2: vertex 6). The DEAD verdict does not depend on the count.
  - TOP-N3 = N-TS-5 ((INJ) is the general fact; R38 (a) only as the phase definition).
  - TOP-N2 (n − 1 far from reached: mine max 0.37 n, its 0.43 (n − 1) on lend9_n8; 62 at n = 581 in its corpus) and N-TS-2 (the sharper count
    n − 1 − rank(λ(v))): ACCEPTED, consistent.
  - N-TS-4 (even / odd rank = parity of Ω of the vertex of that rank, worth a reminder in §2): ACCEPTED as wording.
- Nothing open on TOPSHAPE. G-N5-TIME stays OPEN.
