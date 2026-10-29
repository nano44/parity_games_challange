# R2-N5-MPGS-C: REFEREE-2 §C (joint gap map) for packet P-N5-MPGS (l-lit a23179b0, sha1 24913a7f…)
Written by REFEREE-2 successor 20, Opus 5.5 (D15, L37), 2026-10-29 from 12:06Z (date -u). Lead ruling 11:54Z: the §C goes in this NEW file, and is
based on both REFEREE-2 reports with their differences listed.

**Inputs.**
- REFEREE: docs/referee/R-N5-MPGS.md (origin/claude/referee; REFEREE successor 17). First opened 12:05Z, after both REFEREE-2 reports were
  pushed.
- REFEREE-2, report of record: docs/referee-2/R2-N5-MPGS.md (successor 19, 0c4524f0).
- REFEREE-2, concurring: docs/referee-2/R2-N5-MPGS-s20.md (successor 20, c1c4676a; written without reading 19's).

## C.1 Verdict map
| item | REFEREE | REFEREE-2 (19, record) | REFEREE-2 (20, concurring) | joint |
| --- | --- | --- | --- | --- |
| A0 definitions | CHECKED | SIGNED | SIGNED | agreed |
| Fact A1 | SIGNED | SIGNED | SIGNED | SIGNED by both referees |
| Lemma MATCH-Φ | SIGNED | SIGNED | SIGNED | SIGNED by both |
| Added statement (A) | SIGNED (proof condensed: MPGS-N1) | SIGNED | SIGNED | SIGNED by both; wording note MPGS-N1 |
| B0 definitions | CHECKED | SIGNED | SIGNED | agreed |
| Fact B1 | SIGNED | SIGNED | SIGNED | SIGNED by both |
| Fact B2 | SIGNED | SIGNED | SIGNED | SIGNED by both |
| Lemma GATE-SHUT (steps 1-6) | SIGNED | SIGNED | SIGNED | SIGNED by both |
| Added statement (B) | SIGNED | SIGNED | SIGNED | SIGNED by both |
| pinned checks T33, T34, quotecheck | reproduced exactly | reproduced exactly | reproduced exactly | identical figures in all three |
| A3/A4/B3/B4 | not signed | not signed | not signed | DATA / READING |

**Joint gap map: EMPTY.** No referee lists a gap. No item is FALSE. Part (A) and Part (B) are SIGNED by both referees, with the notes in C.3.

## C.2 Agreements reached independently (three reports, no exchange)
- (H2)'s necessity is NOT exhibited: REFEREE MPGS-N3 (MUT 2: 8,975 relaxed hits, all still shut), REFEREE-2 19 N-MPGS-1 (0 of 15,528), REFEREE-2
  20 N-GS-3 (0 of 1,648, 426 of them under every τ). (H1) and (H3) are each needed: all three report controls that bite. (H2) is used by the proof
  (steps 2-3) and stays a hypothesis. Whether (H1) + (H3) suffice is OPEN. REFEREE-2 20 notes that (H1) alone already gives e ∉ ρ.
- T34 tests (H1) only via rank(d1) > rank(c_h): REFEREE MPGS-N4 (checked on H_4's four gates), REFEREE-2 19 N-MPGS-2, REFEREE-2 20 N-GS-5
  (hn.py l. 46-49: d1 < d2 < d3 < e for every gate i in mode fig). Exact on Friedmann's H_n. Say so in B3.
- Part (A) has the same mathematics as MATCHPHI with reworded text. All three carry the MATCHPHI verdicts over. MATCH-N1 (REFEREE) = N-MP-1
  (REFEREE-2) is repaired by MPGS's "Uses" line.

## C.3 Differences between the reports (each is a note; none changes a verdict)
| # | point | raised by | REFEREE-2 20's assessment |
| --- | --- | --- | --- |
| D1 | MPGS-N1: (A)'s Corollary proof skips the rise/fall summation (R − F = Φ(end) − Φ(start) ≤ W, F ≤ W·NM, #MATCHED ≤ R); also "W ≤ K(K+1)/2" is an equality | REFEREE; 19 noted the "≤ / =" point in §1 | Correct. I marked "compressed" in my diff table without flagging it. Restore MATCHPHI's three lines |
| D2 | MPGS-N2: step 3 uses h ∉ Q (from (H2), ρ starts at h) and d Even (π_1 = d) | REFEREE | Correct. My §2.4 uses both implicitly. One clause |
| D3 | T34 imports L-COMP code from a hard-coded ROOT (the working tree at run time, not the freeze commit) | REFEREE (MPGS-N4) | Correct, and the same as REFEREE-2's standing trap (pinned scripts read the working tree). Pin the imports or state the dependency |
| D4 | B4 READING: "(H1) is automatic" holds only where c_h is the sink; the noH1 control bites on 28 H_n gate-states | REFEREE-2 19 (N-MPGS-4) | Agreed (my H3-H6 run: X1 = 32 of 32 there) |
| D5 | Enumeration caps (π ≤ 6 vertices / ≤ 40 per (e, d); ≤ 64 paths; DFS budget 4,000) | 19 (N-MPGS-5); caps differ per referee | Covered jointly: three different enumerations, 0 failures in all |
| D6 | Scope wording: the Lemma holds at any state, in-phase or not; (B) is per transition | 19 (N-MPGS-6) | Agreed; matches my N-GS-4 |
| D7 | G^d's order is the exact reverse of G's on ALL valuations (B1 is a special case) | 20 (N-GS-2) | Not raised by the others; checked on 200,000 pairs |
| D8 | ENGXI: Ξτ = the (τ̄, τ)-play value at every vertex, as the R57 (b) standing premise | 20 (N-GS-1); 19 (DENG); REFEREE ("realised by τ̄ at every vertex") | All three rely on it, and two check it in data |
| D9 | The Lemma checked at EVERY τ of 80,000 small random games (not only at run states) | 20 | Adds coverage only |
| D10 | Part (A) text: REFEREE calls it "NOT identical, content the same" (similarity 0.12); 19: "mathematics IDENTICAL"; 20: "not byte-identical, same content" | all | Same finding in different words. Every verdict was carried over by content, not by text |

Data scale (Part B), for the landing entry:
- REFEREE: 22,487 hits, plus 3.7M B1 pairs.
- REFEREE-2 19: 72,985 gates.
- REFEREE-2 20: about 28,700 (state, e, d) triples with (H1)-(H3), proof steps GS2-GS5 on actual plays, and 76M B1 pairs.
- 0 failures in all three.

## C.4 Joint list for L-LIT (fixes file docs/lit/P-N5-MPGS-fixes.md)
1. (A) Corollary proof: restore the rise/fall summation; write "W = K(K+1)/2" (D1).
2. Step 3: state h ∉ Q (from (H2)) and that d = π_1 is Even (D2).
3. B3: T34's (H1) test via d1 is exact on H_n because d1_i is Q's lowest vertex (hn.py l. 46-49); pin or state T34's imports from the working
   tree (D3, C.2).
4. B3's "the hypotheses are needed": true for (H1) and (H3) separately; (H2)'s necessity is not exhibited (C.2). Optional OPEN question:
   do (H1) + (H3) suffice?
5. B4: "(H1) automatic" only where c_h is the sink (D4).
6. Optional one-liners: the full order reversal (D7); the Corollary uses only the hypotheses at the source state, and π may vary (D6).
Carried from MATCHPHI: N-MP-2 / MATCH-N4 (first term sharp at NM = 0), N-MP-3 (additivity line), N-MP-5 / MATCH-N2.

## C.5 DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: the joint gap map is EMPTY. Parts (A) and (B) are SIGNED by both referees. Ten differences, all notes. (H2)'s necessity is not
  exhibited in any of the three independent data sets.
- NEEDS: Lead: land P-N5-MPGS (A) and (B) per C.1, citing REFEREE-2 20 as "concurring"; route C.4 to L-LIT.
