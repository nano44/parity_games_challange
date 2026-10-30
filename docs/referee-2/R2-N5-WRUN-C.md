# R2-N5-WRUN-C: §C cross-map with REFEREE's report on P-N5-WRUN (REFEREE-2 successor 23, Opus 5.5, D15)
Inputs: my report docs/referee-2/R2-N5-WRUN.md (claude/referee-2 a281189a, pushed before I opened any docs/referee/ file for this packet);
REFEREE's docs/referee/R-N5-WRUN.md at claude/referee 8c0b2e69 plus Addendum 1 at a3aa5b68 (opened 17:24Z on the Lead's word); REFEREE's
instance docs/referee/scratch/wrun_logs/wc_line_cex.pg @ 8c0b2e69 (sha1 a8a5013bbb4860a2d700b0f554b065b08487d65a, re-hashed). Object
unchanged: P-N5-WRUN-box92.md @ 7668bc9b (fae68aa0); lines 0faa5b80 and L-1 d92521f7.
Owner rulings: D1 «Never downgrade the referee to save money.»; D18 «Clearly distinguish proven results from conjectures and open problems.»

## C.1 Verdicts side by side
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| §1 setting, STEP-SW | CHECKED | CHECKED | agree |
| Fact EXT | true only if y ∉ P of both arguments (WRUN-N1); every use satisfies it | FALSE as worded, instance x = (c, {y}, ℓ), x′ = (c, ∅, ℓ); true with y ∉ P(x) ∪ P(x′); every use satisfies it (N-1) | the SAME point. Joint: wording fix, no signed item affected (C.3) |
| §2.1-2.3 other lanes | verbatim; not signed; FL-INT's counting step signed inside E7 | the same | agree |
| [SUB] | SIGNED independently (§9.1) | my own check (a11c2868); quoted verbatim | two signatures: [SUB] double-refereed, so BIP-RED and E8 are unconditional |
| XI-RUN | SIGNED | SIGNED | SIGNED by both |
| WRUN-EQ E1-E13 | SIGNED (both directions where marked) | SIGNED | SIGNED by both; E10 vacuous (both: BIP-REL-1 DEAD; REFEREE recorded the Lead's report, I re-ran the kill) |
| WAIT-CYCLE′, DEAD-CYCLE, CHARGE | SIGNED for §4.1's definition | SIGNED | SIGNED by both |
| E0-BOUND, TRIPLE-RED | SIGNED | SIGNED | SIGNED by both |
| RET-ΞRISE, FREE-RED | SIGNED | SIGNED | SIGNED by both |
| GAP-DEV, ΞCH-PCH, RSTAR-PCH | SIGNED | SIGNED | SIGNED by both |
| LEX-SIGN, PREFIX-MON, LEVEL-RED | SIGNED | SIGNED | SIGNED by both |
| BIP, BIP-MON, NO-DEV (corrected) | SIGNED | SIGNED | SIGNED by both |
| BIP-RED | SIGNED, unconditional with [SUB] | SIGNED (implication; unconditional once [SUB] double-signed) | SIGNED by both, unconditional |
| REL2-WRISE | SIGNED; conclusion already landed as R91 LATE-W (WRUN-N2) | SIGNED; the line's LATE-W parenthesis is correct | agree |
| INT-XCH⁰ | SIGNED | SIGNED | SIGNED by both |
| line | 0faa5b80 does NOT match: G-WRUN-1, WRUN-L1, WRUN-L2, N4 | candidate L-1 d92521f7: MATCHES in content; L-1 REQUIRED («strict release» unbound), L-2..L-5 precision | C.2 |

Joint gap map for the packet: EMPTY. Nothing FALSE in the packet on either side. The only FALSE statement either of us found is in line
0faa5b80 (G-WRUN-1), and line L-1 already repairs it.

## C.2 Line: G-WRUN-1, WRUN-L1, WRUN-L2 against my L-1 verdict
- **G-WRUN-1 (REFEREE, on 0faa5b80): CONFIRMED independently.** Re-run with my own N5 loop (R2-N5-WRUN/line0_cex.py; no REFEREE code) on
  wc_line_cex.pg from the best-reward start: 2 states, σ(3) = 0 at both. Under 0faa5b80's block wording (not improving; play from g reaches
  X; E0 iff X is its own cycle node and the route is below X), the REG «block» (X, g) = (3, 0) at state 0 with route [0] recurs at state 1.
  That is exactly REFEREE's (t1, X, g, π, t) = (0, 3, 0, [0], 1). So WAIT-CYCLE′ as worded in 0faa5b80 is FALSE. Under the packet's §4.1
  definition (g ≠ σ_t(X); route pairwise distinct; route avoids X's cycle when X lies on it): 0 recurrences.
- **Revision L-1 already contains the fix.** Its block definition reads «(X, g) not improving, g ≠ σ_t(X), and the (σ_t, σ̄_t)-play from g
  reaching X, its vertices before X (the route) pairwise distinct and, when X lies on the cycle of its own (σ_t, σ̄_t)-play, avoiding that
  cycle». That is §4.1's definition. I reviewed L-1 as the candidate and found no block problem; on 0faa5b80 I would have hit the same gap.
  Joint: G-WRUN-1 CLOSED in L-1.
- WRUN-L1 (k free in LEVEL-RED): L-1 has «for every k ≥ 1» in both the DEEP definition and the clause. CLOSED in L-1.
- WRUN-L2 (term order unbound): L-1 writes the order out. CLOSED in L-1. I checked L-1's wording of the order against §7.2: identical.
- WRUN-N2 (REL2-WRISE = R91 LATE-W): L-1 adds «(a special case of RESULTS R91 Lemma LATE-W, which needs neither (A2) nor the frozen
  stretch)». My report §2.10 checks that this is correct (q2 ≥ s + 2 automatically, so q2 is a «later state»).
- WRUN-N3 ([P-INT] «of a W-run»): AGREE. The packet's l. 108 (L-SI's wording «of every run») would let an interval span a W-run boundary.
  The line (0faa5b80 and L-1) reads it on W-runs. I missed this point in the packet text, but the line is right.
- WRUN-N4 («one-way» → «proved in one direction only»): applied in L-1.
- **My L-1 («strict release» unbound in REL2-WRISE).** REFEREE reads the term as defined implicitly by R°_Φ and finds that acceptable. I keep
  it REQUIRED under the strict symbol test, because the line never names the term, and the clause uses it as a hypothesis. It costs one
  definition, or nothing if the clause drops the hypothesis (REFEREE's own note: «It is not needed (WRUN-N2)»). The Lead decides. Both of
  us agree it does not affect any signed content.
- My L-2..L-5 (τ unbound in GAP-DEV / BIP-MON; «there is a polynomial p»; «over Even edges»; REG = not E0): precision only. REFEREE did not
  raise them.
- Status after L-1: of the line items, only my L-1 (and the optional L-2..L-5) remain. The Lead reports they are routed to L-NEW 39 for line
  L-2.

## C.3 Fact EXT: my N-1 against REFEREE's WRUN-N1
The same point, stated two ways: REFEREE gives the condition («needs y ∉ P(x) for both arguments»), and I give an instance showing that the
unconditional wording is false. Both of us checked that every use satisfies the condition: REFEREE lists REL2-WRISE (i) and the
v-not-own-cycle-node uses (TRIPLE-RED, RSTAR-PCH, RETURN-CHARGE); I list §10 (i) and RETURN-CHARGE and note that the «Ω(v) =
ext(v, Ω(succ))» sentence satisfies it automatically. Joint fix: add «for values x, x′ with y ∉ P(x) ∪ P(x′)» to Fact EXT. I label it
FALSE as worded (with the instance) rather than «wording only», so that nobody later cites Fact EXT without the clause. No signed item
changes either way.

## C.4 Notes only one of us raised
- Mine: N-2 (R3-POLY used in the packet, defined only in the line). REFEREE's token pass lists R3-POLY as bound in the line, which is
  consistent: a packet-text note only.
- REFEREE's: MUT 1 shows that the clause «π avoids Z*» was never needed in the corpus (0 recurrences without it over 283,077 blocks), while
  the proof needs it (Case 2). G-WRUN-1's instance needs the other dropped clause, g ≠ σ_t(X), together with π meeting Z*. Both clauses
  stay in.

## C.5 DATA
- Run sets: REFEREE n ≤ 100 (813 runs; 73 skipped for size); mine all 1132 runs (no size cap; comp54_n80 with its forced Odd vertex 11
  repaired, τ(11) = 11). Both 0 violations of every check.
- Agreements: XI-RUN max ratio 0.272 (thetaA_n6; both), packet 0.273 (rounding). WAIT-CYCLE′: REFEREE 269,250 REG blocks (all), mine 286,472
  (sampled, larger corpus): 0 each. NO-DEV max |F| 55 (x32_rand64) on both sides for n ≤ 100; mine also 58 (topfix_n10, n 210), above
  REFEREE's cap.
- Pins: pftheta34 34 / bound 1010 (both); latew_K16_m32 560 transitions (both), SB_F 513 (REFEREE) and bound 4389 (mine); gate_K64_n581
  R*_F 64 (both), plus |F| 71, ΞCH 63 (mine); fx_K8_m32 280 transitions (both), max ΞCH 137 and bound 2005 (mine), max R* 16 (REFEREE).
- BIP-REL-1: REFEREE recorded the kill from the Lead's report without re-running it; I re-ran it on rel2_R2_n82 (l-red 717f407a): 2 strict
  releases of one edge in one frozen stretch, all other checks 0. So the kill now has an independent reproduction.

## DONE / FINDINGS / NEEDS
- DONE: this §C; line0_cex.py (independent reproduction of G-WRUN-1's instance).
- FINDINGS: (1) joint gap map for the packet EMPTY, every item SIGNED by both; [SUB] double-signed, so BIP-RED and E8 are unconditional.
  (2) G-WRUN-1 CONFIRMED on 0faa5b80 (instance reproduced with my own engine) and CLOSED in L-1, as are WRUN-L1, WRUN-L2, N2, N4. (3) Fact
  EXT: my N-1 = REFEREE's WRUN-N1. (4) Open line item: my L-1 («strict release»), REQUIRED in my reading and acceptable in REFEREE's; the
  Lead decides. (5) BIP-REL-1 kill independently reproduced.
- NEEDS: Lead: decide my L-1 against REFEREE's reading; send WRUN line L-2 for a word-diff.
