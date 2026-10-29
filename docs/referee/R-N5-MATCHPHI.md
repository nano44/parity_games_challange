# R-N5-MATCHPHI: REFEREE report on packet P-N5-MATCHPHI (L-LIT: definitions, Fact 1, Lemma MATCH-Φ, Corollary PCH ≤ (K(K+1)/2)(NM + 1) + NM)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 2026-10-29 11:01Z by date -u).
- Object and pin: docs/lit/P-N5-MATCHPHI.md, sha1 544705b74312e49ee31fd93ede1952396ebd12f1, 133 lines, author L-LIT successor: the same sha1 at
  l-lit 12b7d12a (an ancestor of origin/claude/l-lit) and at the l-lit head. Quote base 6abea2e6.
- Runs 2026-10-29T11:03Z-11:27Z; report written 2026-10-29T11:28Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ MATCHPHI file on my tree or on trunk; 17 names on origin/claude/referee-2 at 11:17Z (names only, same turn as
  the fetch, none opened).
- Pinned lane checks, re-run at the Lead's request (read first: local arithmetic and `git show` only), from a clean worktree at 12b7d12a:
  - docs/lit/T33-match-phi-check.py (sha1 6853179bf10bdf1c3d9cae61c939b1054aa4b70c): "A: improving pairs 80640 | matched with phi rise < 1: 0 |
    carries: 32534"; Part B k = 1..8: strict-rise=True, fixed-top=True, NM = 0, 0, 1, 3, 7, 15, 31, 63. EXACTLY as expected (exit 0).
  - docs/lit/P-N5-MATCHPHI-quotecheck.py (sha1 0ac586a48b05ee7484ecfe1bec74a4af4085f741): "quotes=5 bad=0"; my shifted control (the R84 quote
    moved from l. 4967 to 4968) gives "quotes=5 bad=1". As expected.
- Own checks (no lane import): scratch/matchphi_probe.py (sha1 d3f3213d…; own MATCHED search by DFS over the outgoing ranks; N5 data on my
  engine rl_engine), scratch/mp_chain.py; logs scratch/mp_logs/. Quotes 5/5 with my own scratch/flip_quotes.py.
- Premises read: SPEC S1 (ranks, valuation, signed weight; l. 27-31 at 6abea2e6); RESULTS R84 (a) Fact DELTA and R84's setting (l. 4960-4967;
  R84 = P-N5-TOPSHAPE, which I signed as first referee, R-N5-TOPSHAPE.md).

## Verdicts (item by item)
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0-§1 | definitions: K, R_c, pos, w, Φ, MATCHED (M1)-(M3), CARRY, NM, PCH | CHECKED (well defined: c = λ(v) constant on the phase, so R_c and pos are fixed; ranks distinct). The sentence "deciding MATCHED is polynomial per P-change" is TRUE (a bipartite matching that must cover given vertex sets on both sides; e.g. maximum-weight matching) |
| §2 | Fact 1 (w(i) > w(o) iff weight({i}) > weight({o}); even additions / odd removals raise the weight; so MATCHED = a decomposition into individually weight-raising one-for-one exchanges, even additions and odd removals) | SIGNED |
| §2 | Lemma MATCH-Φ (Φ(B) − Φ(A) ≥ 1 at every MATCHED change) | SIGNED |
| §2 | Corollary PCH_𝒫(v) ≤ (K(K+1)/2)(NM + 1) + NM ≤ (n²/2)(NM + 1) + NM, per vertex per phase, every game | SIGNED |
| §2 | the premise claim "the Lemma and the Corollary use none of (MON), R15 or R84's TOP-SHAPE; only distinct ranks and P_t ⊆ R_c" (and the Remark "holds for any sequence of subsets of R_c") | TRUE (checked against the proof, §3 below), with one correction: (MON) is not used by Fact 1 either (MATCH-N1) |
| §3 | pinned check (DATA) | reproduced exactly (above); not signed |
| §3 | L-COMP's N5 data | DATA, not signed; partly reproduced on my engine (§4), one figure differs (MATCH-N3) |
| §4 | ARV reading | READING, not signed |
No gap. Notes MATCH-N1..N4. The Corollary reduces path-set changes to carries and bounds nothing by itself (NM OPEN); not M3, not a step-4 pass,
not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Fact 1 re-derived
- weight({r}) = s(r)2^r; for o ≠ i, Fact DELTA with d = max(o, i): if i > o the exchange raises the weight iff i is even, if o > i iff o is odd ✓.
- The four cases ✓: i > o, i even: w(i) = pos(i) > pos(o) ≥ w(o); i > o, i odd: w(i) = −pos(i) < −pos(o) ≤ w(o); o > i, o odd: w(o) = −pos(o)
  < −pos(i) ≤ w(i); o > i, o even: w(o) = pos(o) > pos(i) ≥ w(i). (pos is increasing in rank, and |w(o)| = pos(o).) ✓
- Additions of an even rank / removals of an odd rank raise the weight (DELTA with d the changed rank) ✓.
- The reading "MATCHED ⇔ decomposition into individually raising exchanges, even additions, odd removals" ✓ (by the equivalence just shown).
  Consequence worth stating (my data, and immediate from additivity of the weight): every MATCHED change raises the weight; in my exhaustive
  K = 6, 7 runs no MATCHED pair is non-improving.
- Data: Fact 1 on every ordered rank pair of every parity pattern, K = 6, 7 (1,920 + 5,376 checks): 0 failures.

## 2. Lemma MATCH-Φ re-derived
- Φ(B) − Φ(A) = Σ_{B∖A} w − Σ_{A∖B} w; the matching pairs, the uncovered incoming ranks and the uncovered outgoing ranks partition A Δ B (each
  rank in at most one pair) ✓. Each pair contributes the integer w(i) − w(o) ≥ 1 by (M1); each uncovered i contributes pos(i) ≥ 1 by (M2);
  each uncovered o contributes pos(o) ≥ 1 by (M3) ✓. A ≠ B gives at least one term ✓.
- (M1)'s strictness is automatic: distinct ranks have distinct |w|, so w(i) = w(o) never holds (the non-strict mutation does not change a single
  MATCHED verdict, MUT=2).
- Data: on ALL ordered pairs A ≠ B (improving or not) of subsets of K ranks, for EVERY parity pattern: K = 6, 258,048 pairs (the same count as
  L-COMP's cross-check), 78,268 MATCHED, 0 with Φ rise < 1; K = 7, 2,080,768 pairs, 571,298 MATCHED, 0 failures. Improving pairs: 129,024 (K = 6;
  78,268 MATCHED + 50,756 carries) and 1,040,384 (K = 7).

## 3. The Corollary re-derived, and the premise claim
- Φ(A) ∈ [−Σ_{odd} pos, Σ_{even} pos] for every A ⊆ R_c, width Σ_{k ≤ K} k = K(K+1)/2 = W ✓. Φ(P_t) changes only at P-changes ✓.
- Total rise R and total fall F over the phase: R − F = Φ(end) − Φ(start) ≤ W, so R ≤ W + F ✓. Falls occur only at carries (MATCHED changes rise),
  each ≤ W in absolute value: F ≤ W·NM ✓. Each MATCHED change contributes ≥ 1 to R: #MATCHED ≤ R ≤ W(1 + NM) ✓. PCH = #MATCHED + NM ✓.
  K ≤ n − 1 gives W ≤ n(n − 1)/2 ≤ n²/2 ✓.
- The premise claim is TRUE: the proof uses only that R_c (hence pos and w) is fixed on the phase (c = λ(v) constant) and that P_t ⊆ R_c with
  distinct ranks. (MON), R15 and TOP-SHAPE are not used, and the Corollary holds for ANY sequence of subsets of R_c. Data: 3,000 + 2,000 random
  arbitrary sequences (K = 8, length 40; K = 10, length 300) and as many weight-increasing ones: 0 failures.
- Tightness (new, not in the packet): for all-even ranks and K = 1..8 the longest chain of MATCHED changes (NM = 0) has exactly W = K(K+1)/2
  changes (Φ rising by 1 per step; scratch/mp_chain.py, mp_logs/chain.txt). So W cannot be lowered for abstract sequences, and the mutation
  W := K is false from K = 2 (MUT=3). Whether N5 realizes such chains is not examined.

## 4. N5 data on my engine (DATA, not signed; scratch/mp_logs/n5_*.txt; 0 Corollary failures)
| set | runs | (vertex, phase) pairs with a P-change | P-changes | carries | max PCH / max NM per (v, phase) | max NM / n |
| --- | --- | --- | --- | --- | --- | --- |
| pl130_n40 (red/sel, its .start) | 1 | 38 | 962 | 688 | 62 / 47 | 1.175 (vertex 1, phase [1, 131]: 62 P-changes, 47 carries) |
| alt_all, n ≤ 100 (379 of 413 games; given start else S3) | 379 | 7,596 | 45,234 | 25,585 | 67 / 41 | 0.90 (red/n3 ret22_n40, vertex 1, phase [7, 90]) |
| L-RED instances (red/*/instances, n ≤ 200, given or S3) | 319 | 8,148 | 29,501 | 15,978 | 62 / 47 | 1.175 (pl130_n40) |
| lib41 (n ≤ 48, given or S3) | 349 | 5,785 | 30,700 | 15,751 | 37 / 18 | 0.47 |
- Reproduced: max NM 47 = 1.18 n on pl130_n40 (L-COMP: "47 = 1.18n on pl130_n40"); max NM / n 0.90 (L-COMP: "max NM/n 0.90 on pinned starts").
- Not reproduced (MATCH-N3): L-COMP's "max NM per (vertex, phase): 31 on alt_all (0.775n)": my alt_all (n ≤ 100) maximum is 41 carries, and 36 at
  n = 40 (0.90 n). And "pl130: 157 = 41 matched + 116 carries": the unit is not stated; my per-vertex maximum on pl130 is 62 = 15 + 47.
- The alt_all games with n > 100 (34) were not run: my exhaustive MATCHED search is too slow there (a 20-minute run killed, recorded).

## 5. Mutation controls
| MUT | change | result |
| --- | --- | --- |
| 1 | (M2) dropped (odd additions may stay uncovered) | BITES: 43,975 MATCHED pairs with Φ rise < 1 (K = 6) |
| 2 | (M1) non-strict | does not change any verdict: equality is impossible (§2) |
| 3 | Corollary with W := K | BITES on the all-matched chains (§3; K ≥ 2); does not bite on random sequences (loose there) |

## 6. Notes (for L-LIT's fixes file; none changes a verdict)
- MATCH-N1 (premise sentence). "(MON) and Fact DELTA are used only by Fact 1": Fact 1 uses Fact DELTA only, not (MON). (MON) enters only the
  READING that under N5 a P-change raises the weight, so that "carry" means a non-decomposable improvement.
- MATCH-N2 (Fact 1, a consequence to state). By additivity of the weight, every MATCHED change raises weight(P); so in a phase (where every
  P-change raises the weight, R84) the carries are exactly the improving changes that do not decompose. My exhaustive data confirm it.
- MATCH-N3 (§3 DATA, not signed). L-COMP's "31 on alt_all (0.775n)" is not what my engine finds on alt_all (41; 0.90 n at n = 40); "157 = 41 +
  116" needs its unit. The pl130 maximum (47 = 1.18 n) and the 0.90 ratio agree.
- MATCH-N4 (tightness). The Corollary's W = K(K+1)/2 is attained by abstract all-matched chains (§3); the bound is sharp as a statement about
  subset sequences. Its N5 tightness is open.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-MATCHPHI.md (this file), scratch/matchphi_probe.py, scratch/mp_chain.py, scratch/mp_logs/; the pinned checks re-run (exact).
- FINDINGS: definitions CHECKED; Fact 1, Lemma MATCH-Φ and the Corollary SIGNED, no gap; the premise claim (no (MON), no TOP-SHAPE) TRUE, with
  (MON) not used by Fact 1 either (MATCH-N1); W is tight for abstract sequences (MATCH-N4); L-COMP's alt_all NM figure differs from mine (MATCH-N3).
- NEEDS: Lead: the MATCHPHI §C word when REFEREE-2's report is in (or to successor 18, per the handover); route MATCH-N1..N4 to L-LIT.
