# R2-N5-SETTLE-C: §C cross-map with REFEREE's report on P-N5-SETTLE (REFEREE-2 successor 23, Opus 5.5, D15)
Inputs: my R2-N5-SETTLE.md (claude/referee-2 301042bb, pushed before I opened any docs/referee/ SETTLE file); REFEREE's
docs/referee/R-N5-SETTLE.md at claude/referee 1df722e9 (opened 19:07Z on the Lead's word). Object: P-N5-SETTLE-box52.md @ l-si 6a70a520
(aef403c3), line 6aa094e3.

## C.1 Verdicts side by side
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| §1 setting, STEP-SW, MON | CHECKED | CHECKED; N-1 (⊕ reflection needs y ∉ P) | agree; N-1 is mine only (C.3) |
| ARENA-MAX | verbatim at 47000632; used as [R57] | verbatim except one dropped list marker (N-2) | agree on substance; N-2 = a formatting note, REFEREE's SETTLE-N2 adds the missing SHA |
| T54 IDX-MONO / LEX-BFS as used | SIGNED (re-derived from SPEC S1 (iv) with RG′) | SIGNED as used (checked against si.py's recursion and BFS with RG′) | SIGNED by both |
| R143 definitions | definitions only; SETTLE (B), (C) unused | the same | agree |
| Claim RG′ | SIGNED | SIGNED | SIGNED by both |
| PLAY-CAUSE, W-MON, PATH | SIGNED | SIGNED | SIGNED by both |
| RUN-SETTLE, RUN-COUNT | SIGNED | SIGNED | SIGNED by both |
| HEAD-RED | SIGNED | SIGNED | SIGNED by both |
| T-XCH | SIGNED | SIGNED | SIGNED by both |
| line 6aa094e3 | REQUIRED SETTLE-L1 (F), L2 (T), L3 (k in RG′); precision L4 | REQUIRED L-1 (F), L-2 (Iσ_k), L-3 (T); precision L-4..L-6 | C.2 |
Joint gap map for the packet: EMPTY. Nothing FALSE on either side.

## C.2 Line items mapped
- SETTLE-L1 = my L-1 (F unquantified in RUN-SETTLE, RUN-COUNT, HEAD-RED). Same fix.
- SETTLE-L2 = my L-3 (T unbound in T-XCH). Same fix.
- SETTLE-L3 (k free in RG′ and in the H_k / W_(k+1)-tight definitions): AGREE, REQUIRED. I missed it. Fix as REFEREE: «at every S4a step
  k → k + 1 of a W-run».
- My L-2 (Iσ_k unbound) = part of REFEREE's SETTLE-L4 (precision there). I keep it REQUIRED under the strict symbol test (the symbol is used
  in H_k's definition and defined nowhere in the line); it costs five words. The Lead decides; neither of us thinks content is affected.
- SETTLE-L4's other parts (bind «event-free», ⊕, the Σ / max ranges, «for every family of games …»): agree. I missed ⊕ and «event-free»; my
  L-4 (ℓ_(k+1)(v)'s argument), L-5 (status of ARENA-MAX / T54, which REFEREE also calls acceptable as a proof note) and L-6 (the standard
  closing clause) are additional precision items.
- So the joint REQUIRED set for SETTLE line L-1 is: F (L1), T (L2), k (L3), and, in my reading, Iσ_k.

## C.3 Notes
- My N-1 (the ⊕ preserve / reflect sentence of §1 needs y ∉ P of both arguments; instance with x ◁ x′ but y ⊕ x ▷ y ⊕ x′): REFEREE did
  not raise it. It is the same point both referees accepted for WRUN's Fact EXT (WRUN-N1 = my N-1 there). Every use in §5 satisfies the
  condition. Packet erratum only.
- REFEREE's SETTLE-N1 (RG′'s word-diff omits that (B)'s heading changed): I did not compare (B)'s heading against box 51b §10.1; I accept
  it as a note.

## C.4 DATA: the longest event-free block (REFEREE's N3 63 vs my 67), reconciled
- My engine on si/runlin/instances/runfam_K40 (best-reward start): longest event-free block 63 (re-run here: «max_block (63,
  runfam_K40)»). So all three engines (lane rwin «WMAX 63», REFEREE 63, mine 63) agree on runfam_K40.
- My corpus maximum 67 is on red/usplit/instances/gate_K64_n581 + start (n 581). REFEREE's probe skips n > 100 (73 games), so it never runs
  that game. My next largest are 55 (x32_rand64, n 64), which is below 63, and 49 (ladderd0_k48_n156, n 156, also skipped by REFEREE).
- Joint DATA reading: longest event-free block 63 on games with n ≤ 100 (runfam_K40), 67 on the whole corpus (gate_K64_n581). Both ≤ n − 1.
  The packet's «44 at n 48» is the largest RATIO WMAX / n (0.92), as REFEREE's SETTLE-N3 says; my N-3 is answered by that.
- Case split: mine 13,998 / 186 / 13 / 0 / 0 equals the packet's; REFEREE's run set (n ≤ 100) is smaller. No disagreement.

## DONE / FINDINGS / NEEDS
- DONE: this §C; runfam_K40 re-run (63).
- FINDINGS: (1) joint gap map EMPTY; every item SIGNED by both. (2) Line: joint REQUIRED F, T, k (REFEREE's L3, my miss), and Iσ_k in my
  reading. (3) DATA reconciled: 63 (n ≤ 100, runfam_K40, three engines) and 67 (gate_K64_n581, n 581, outside REFEREE's cap).
- NEEDS: Lead: SETTLE line L-1 with F, T, k (and Iσ_k); I word-diff it.
