# P-N5-TOPSHAPE fixes (box 49 packet; repairs only)
L-NEW successor 30 (Opus 5.5; D14, D18, L40). Written 2026-10-29 from 05:43Z (date -u), on the Lead's wake-up of 05:41Z (message to L-NEW):
"Write docs/new/P-N5-TOPSHAPE-fixes-box49.md (repairs only, quotes pinned)." FROZEN at push; its sha1 is reported to the Lead.
- Object, FROZEN and not edited: docs/new/P-N5-TOPSHAPE-box49.md, sha1 c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f (l-new freeze 4c2ea43e), author
  L-NEW successor 30.
- Repairs only; no signed statement changes. Every changed sentence is quoted from a referee.
- Sources:
  - REFEREE: docs/referee/R-N5-TOPSHAPE.md, report 1a6d6a24 and §C e0499401 (successor 17), quoted at e0499401.
  - REFEREE-2: docs/referee-2/R2-N5-TOPSHAPE.md, report 97db54fc and §C 0e2063bf, quoted at 0e2063bf.
  - The packet at its freeze 4c2ea43e.
- Quotes. Every «…» is verbatim at its tagged lines. They are checked by experiments/new/box49/quotecheck3.py, pinned in
  experiments/new/check.sh with their count, a shifted-line control and this file's sha1.

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:82-83] «Verdicts identical: Fact DELTA, TOP-SHAPE (a)-(c) and the Corollary SIGNED by both; §3's Δ-form TOP-MONO DEAD confirmed by both on the same instance»
  and [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:83] «Quotes 2/2 both. Joint gap map: EMPTY.»
- REFEREE-2's joint list: [Q docs/referee-2/R2-N5-TOPSHAPE.md@0e2063bf:137] «TOP-N1 = N-TS-3, TOP-N2 (+ N-TS-2's sharper count), TOP-N3 = N-TS-5, N-TS-1, N-TS-4. No verdict changes.»

## F1. TOP-N1 = N-TS-3: §3's rise count (DATA in a DEAD item; the verdict is unaffected)
- Packet text: [Q docs/new/P-N5-TOPSHAPE-box49.md@4c2ea43e:74] «35, 37, 32, 33, 26, 39, 21, 29, 33, 36, …, with 20 rises in the phase.»
- REFEREE: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:63-64] «I count 17 rises of the Δ-top (over its 35 P-changes), not §3's "20 rises in the phase"; 20 is my maximum over all vertices of that run.»
- REFEREE's §C: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:92] «TOP-N1 = N-TS-3 (17 rises for vertex 0, not 20; 20 is the run's maximum, REFEREE-2: vertex 6). The DEAD verdict does not depend on the count.»
- Re-counted with topmono.py's definition: vertex 0 has 35 P-changes and 17 rises; vertex 6 has 44 P-changes and 20 rises (the maximum of the
  run). Corrected §3 sentence: "…, with 17 rises in the phase (vertex 6 of the same run has 20, the run's maximum)."

## F2. N-TS-1: (a), (b) hold at every N5 transition with λ(v) unchanged (a REMARK; a strengthening outside the signed statement)
- REFEREE-2: [Q docs/referee-2/R2-N5-TOPSHAPE.md@0e2063bf:20] «It also holds at every N5 transition at which v's own cycle node is unchanged, phase or not (N-TS-1)»
- REFEREE's §C: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:84] «N-TS-1 SETTLED (Lead's question): a STRENGTHENING, not part of the signed statement.»
  and [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:86-87] «the proof uses only (MON), valid at every iteration since Ξ depends on σ alone, R15 (a), (d); the unchanged cycle node; and (INJ)»
- Added after the Corollary, as a REMARK (not part of the signed Lemma): "The proof uses only (MON), the unchanged cycle node λ(v) and (INJ). So
  (a) and (b) hold at every N5 transition at which λ(v) is unchanged, phase-leaving transitions included, and the Corollary holds per maximal
  run of states with λ(v) constant. Both referees re-derived this, and checked it with 0 failures: REFEREE at 9,202 off-phase P-changes,
  REFEREE-2 at 115,702 checks."

## F3. TOP-N2 with N-TS-2: the count is far from tight; the sharper count (remark)
- REFEREE: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:66] «The Corollary's n − 1 is never approached in data (max 0.37 n; 48 at n = 156).»
  and [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:67] «Whether n − 1 is attained by some game is open (an odd run down all odd ranks, then the even ranks upward).»
- REFEREE-2: [Q docs/referee-2/R2-N5-TOPSHAPE.md@0e2063bf:79] «N-TS-2 (sharper count). The number of values is (ranks above rank(c)) + 1, so top changes ≤ n − 1 − rank(λ(v)).»
  and its data: [Q docs/referee-2/R2-N5-TOPSHAPE.md@0e2063bf:51] «The ratio is at most 0.43·(n − 1) (lend9_n8).»
- Added after the Corollary (remark): "The proof gives the sharper count: top changes ≤ n − 1 − rank(λ(v)), with ranks counted from 0, since the
  values are the ranks above rank(λ(v)) and ⊥. In data the count stays at most 0.43·(n − 1) (REFEREE-2, lend9_n8), and 0.37 n in
  REFEREE's data. Whether n − 1 is attained is OPEN."

## F4. TOP-N3 = N-TS-5: (INJ) is the general fact; "of one class" in Fact DELTA is unnecessary (premise wording)
- Packet text: [Q docs/new/P-N5-TOPSHAPE-box49.md@4c2ea43e:35] «Fact DELTA. For path sets A ≠ B of one class,»
- REFEREE: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:68-70] «the packet uses it as the general fact that distinct sets of ranks have distinct signed weights, which is immediate (Fact DELTA itself gives it). "Of one class" in Fact DELTA is not needed. Cosmetic.»
- Repaired: Fact DELTA reads "For sets A ≠ B of ranks, weight(B) > weight(A) iff …". The premise line "(INJ) (RESULTS R56 (a))" reads "(INJ):
  distinct sets of ranks have distinct signed weights (immediate from Fact DELTA; stated per honest class in RESULTS R56 (a))". The phase
  premise is the phase definition only: [Q docs/referee/R-N5-TOPSHAPE.md@e0499401:93] «TOP-N3 = N-TS-5 ((INJ) is the general fact; R38 (a) only as the phase definition).»

## F5. N-TS-4: "even / odd rank" means the parity of Ω (wording)
- REFEREE-2: [Q docs/referee-2/R2-N5-TOPSHAPE.md@0e2063bf:85] «"Even / odd rank" means the parity of Ω of the vertex of that rank (§0 says so), not the parity of the rank»
- Added to §2 (DATA): "Here, as in §0, an even or odd rank is the parity of Ω of the vertex of that rank, not of the rank number. For example,
  sc32's tops 31, 30, 29, 27, 26, 21, 20 are all odd in this sense."

## What this file does not do
- It bounds nothing new. The P-changes under a fixed top stay unbounded (up to 71 per vertex per phase); FB-LIN stays OPEN; G-N5-TIME stays
  OPEN. Not a TARGET.md claim.
