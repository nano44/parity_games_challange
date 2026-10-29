# R116: N5-SF makes EXPONENTIALLY many iterations on dwN = fcN plus one repeater per escape-chain edge: 19·2^N − 18 iterations at n = 26N + 9, SBC_σ = 2^(N+1) − N − 2 (N = 3..8, two engines). DATA against CONJECTURE SF-POLY; plain N5 stays linear on the same games
L-RED successor 29 (Opus 5.5; D1/D18; Lead 18:10Z STEP 1, "push N5-SF's iteration degree above 3, or find the obstruction"). Written
2026-10-29 from 18:30Z (date -u). Labels: DATA / READING / OPEN / DEAD. Not a TARGET.md claim. N5-SF is L-NEW's single-frame variant
(claude/l-new docs/new/N5-SF-box54.md; CONJECTURE SF-POLY in P-N5-SF-box55.md §5). This note does NOT concern N5 SSI-GLOBAL itself (§3).
Engines: sf2.py (L-RED, from the N5-SF text, L-COMP PGSolver-port valuations; R114 §0) and L-NEW's n5sf.py (claude/l-new 9faf17be,
default MODE). Correctness: experiments/red/sf/okcheck.sh (Oink zlk regions = sf2's regions; verify.py on sf2's strategies).
Start: SPEC S3 default (best-reward start for both players) everywhere.

## 1. The family dwN (DATA)
- Generator: experiments/red/sf/dlchain.py N 1. Take fcN (R115: sbev.py N --drop fc, PGSolver switchbestexp N minus the N edges
  f_i → c). Then:
  - For i = 0..N−2, put one Even "repeater" u_i on the escape-chain edge v_i → r_(i+1): v_i → u_i → r_(i+1).
  - u_i has edges {r_(i+1), v_(i+1)}. For i = N−2 there is no v_(N−1), so the fallback is p.
  - u_i has a low ODD priority 2i + 3. These sit above q's 1 and below everything else.
  - Every other priority ≥ 2 is shifted up by 2(N−1) + 2, parity kept.
  - n = 26N + 9. Pins: experiments/red/sf/instances/dw_N.pg, N = 3..8.

  | N | n | N5-SF iterations (sf2) | n5sf.py | 19·2^N − 18 | SBC_σ | 2^(N+1) − N − 2 | SBC_τ | LAM | fallbacks | Oink + verify.py | sha1 (12) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 87 | 134 | 134 | 134 | 11 | 11 | 3 | 0 | 0 | OK | e5f94c800324 |
  | 4 | 113 | 286 | 286 | 286 | 26 | 26 | 4 | 0 | 0 | OK | eba759c1e811 |
  | 5 | 139 | 590 | 590 | 590 | 57 | 57 | 5 | 0 | 0 | OK | c03e3e00578a |
  | 6 | 165 | 1198 | 1198 | 1198 | 120 | 120 | 6 | 0 | 0 | | 34ad93bc62d0 |
  | 7 | 191 | 2414 | 2414 | 2414 | 247 | 247 | 7 | 0 | 0 | | 6b40922a7950 |
  | 8 | 217 | 4846 | 4846 | 4846 | 502 | 502 | 8 | 0 | 0 | | 5a7fe1cc2d78 |
  | 9 | 243 | S9 | | 9710 | | 1013 | | | | | |
  | 10 | 269 | S10 | | 19438 | | 2036 | | | | | |
  Both formulas hold exactly wherever measured. For comparison, fcN (no repeaters) gives 121 / 215 / 520 / 1021 at N = 3 / 4 / 6 / 8
  (R115).
- The σ̄-flip word (sftrace.py; h_i+ = Odd escapes cycle i, i.e. bit i set; h_i− = Odd returns). N = 5, 57 flips:
  `h0+ h1+ h0- h0+ h2+ h1- h0- h0+ h1+ h0- h0+ h3+ h2- h1- h0- h0+ h1+ h0- h0+ h2+ h1- h0- h0+ h1+ h0- h0+ h4+ h3- …`.
  READING: a binary counter. EVERY set of bit j, record or not, is followed by a top-down cascade that resets bits j−1..0. The cascade is
  followed by a re-climb that is itself the same counter on bits 0..j−1. Let F(j) be the number of flips from "bits < j clear" to "bit j
  set and bits < j re-set". Then F(j) = 2F(j − 1) + j + 1, which gives Σ = 2^(N+1) − N − 2. Each set costs one lane walk. The walks
  repeat at every level, so the iterations double with N as well.
- I^glo (evseq.py --rule glo, the switch-best rule in the Ξ frame) gives the same σ-sequence lengths: 134 / 286 / 590 at N = 3 / 4 / 5
  (σ̄-changes 10 / 24 / 54).

## 2. Why one repeater suffices (READING; the mechanism is L-NEW's LATENCY, box59 §1.3)
- In fcN a set of bit j below the current top reaches two places along the same shared chain:
  - the lane, because d enters at the lowest set bit (y → l_0) and climbs the escape chains;
  - every closed lower cycle's escape.
  So both hear it at the same F-step and nothing opens (L-NEW box59 §1.3, "a re-set never triggers a cascade").
- A record reaches the lane one F-step before the top lower escape chain (w → l_k is one switch; v_(k−1) → r_k then z_(k−1) → v_(k−1) is
  two). Every escaping lower cycle opens in that one-step gap, and the cascade follows.
- The repeater u_j−1 adds one more Even switch to the escape chain's route into bit j. It is re-armed: while bit j is clear, r_j → z_j
  → … carries z_j's high odd priority, so u_(j−1) prefers its fallback v_j. Odd q-adjacent priorities make the shortcut u → v strictly
  better than u → r while r is worse.
  - So at EVERY set of bit j, the lane, through x → w → l_j or through y → l_0 and the already re-pointed chains, can carry m_j
    one F-step before the escapes of the closed cycles below j do.
  - In that gap they open, exactly as at a record.
- Two near misses, both DEAD and recorded:
  - (i) Fallback p (env FB=p): the chain is never re-armed. r_(i+1) never drops below the sink while any higher bit is set. Counts are
    identical to fcN at N = 3, 4 for chain lengths L = 1..5.
  - (ii) Repeater priorities BELOW q's: the valuation (Vöge–Jurdziński: only priorities above the cycle's count, then path length)
    ignores them, and a longer path is better for Even in an Odd-won play, so the chain stays pointed forward. Counts again equal
    fcN's.
- Chain length L ≥ 1 does not matter: L = 1, 2, 4 give the same counts at N = 3 (134) and N = 4 (286). The lag only needs to be positive.

## 3. Scope
- Plain N5 SSI-GLOBAL (n5b.py --mode spec, L-COMP's second engine) on dwN: 41 / 47 / 55 / 62 iterations at N = 3..6. These are the same
  as on fcN (41 / 47 / 55 / 62). N5's S4a arena keeps Odd FREE, and its look-ahead closes the hop-count race. Nothing here bears on
  G-N5-TIME.
- N5-SF: the iteration count is exponential on this family, on N ≤ 8 (both engines agree at every N = 3..8), with an
  exact closed form. SF-RED's bound (n + m)(1 + LAM + SBC) is not violated: SBC is exponential.
- CONJECTURE PV (DEAD since R115 §2c) and any relevance-restricted version PV_rel: the vertices h_i are on Even's run's own
  cycles (they decide every bit). h_0 flips 2^N − 1 times (15 / 31 at N = 4 / 5; at N = 5 the word has h0..h4 flipping 31, 15, 7, 3, 1 times). READING: any PV_rel that counts h_i's
  flips is false on dwN. I will check PV_rel's exact statement when L-NEW lands it.

## 3b. The Lead's composition question (DATA; superseded by §1)
- Two fc blocks of 3 bits (compose.py, n 170), plus an Odd vertex o on the N-COND edge (scratch comp2.py, not kept):
  - 'oh': o has odd priority P(X) + 1, just above d_A.
  - 'ob': o has priority 0 and edges {s_B, p_A}, an Odd break.
  - 'ohb': both.
- Results:
  - 'sink,athru' + any gadget: 12 iterations, LAM 1. A's root has lost its lane role, so the gadget cannot help.
  - 'sinkE,athru': 58 (LAM 4 or 19).
  - 'sink,aroot' (o on d_A → s_B) and 'sink,root' (o on d_B → s_A): 121. That is one block's count: o is never used, and the blocks
    run in parallel.
  - None of them beats the single block (121).
- READING: with disjoint priority ranges, a vertex of one block that reads the other is decided either by the upper block's part, or
  by the sign of the lower block's top (p_B, top odd, or even under sinkE). Either way the choice is constant: the read is never used,
  or it is used permanently. Nesting by composition needs a reader whose top lies in the lower block's bit range. I did not pursue
  this, because §1 needs no nesting at all.

## 4. What is and is not shown
- DATA: two independent engines agree on the counts for N = 3..8, see the table. Oink regions and verify.py are OK at N = 3, 4, 5. The
  closed forms are fits that hold exactly at every measured N.
- NOT shown: a proof that the word is the binary counter for every N. That would need an induction over the run, like the one L-NEW
  left open for fcN (box59 §1.3). The doubling F(j) = 2F(j − 1) + j + 1 is read from the words for N ≤ 5 only.
- What would make this wrong: an engine bug shared by both engines (they share no code: sf2 uses L-COMP's PGSolver port, n5sf.py uses L-SI's
  si.py), or a mismatch between N5-SF as both engines implement it and L-NEW's frozen text. CHECKER: re-run from the pushed generator.

## DONE / FINDINGS / NEEDS
- DONE: dlchain.py (dwN), pins dw_3..dw_8, check.sh gate (dw_3 134/11, dw_4 286/26), two-engine counts, Oink checks, the word, the I^glo
  and plain-N5 comparisons.
- FINDINGS: (1) DATA: N5-SF iterations 19·2^N − 18 and SBC_σ 2^(N+1) − N − 2 on dwN (n = 26N + 9), N = 3..8. This is evidence that
  CONJECTURE SF-POLY is false, on an exact exponential pattern. (2) READING: one positive hop lag on each escape-chain edge turns fcN's
  unary counter into a binary one, so N5-SF's frame (Odd fixed to σ̄) loses the race that plain N5 wins. (3) Plain N5 is unaffected
  (linear, = fcN). (4) DEAD: repeaters with fallback p, and repeaters with priorities below q.
- NEEDS: none from the owner. To the Lead: an independent re-run (CHECKER or L-NEW) before SF-POLY is labelled DEAD.
