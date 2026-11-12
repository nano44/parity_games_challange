# R-P-N5-WRAP: first referee report on packet P-N5-WRAP (L-SI successor 53; a DEAD-END packet for N5′-xi)
REFEREE successor 34 (D1; the Lead's item D, 22:02Z). Date -u at writing: 2026-11-12T22:11Z. Written section by section; §0
(verdicts) last. A SIGNATURE review of the frozen packet.
- Prior work of this lane, disclosed: R-WRAP-preread.md (successor 33, claude/referee e44ce56b, Addendum 1 90703a81; «no gap found»,
  notes W-1..W-4, F-1..F-3). **Claim NT and its proof originate in this lane** (successor 33, R-WRAP-preread §3.2, (T-2)); the packet
  renders it and labels it so (L41). I sign the packet's rendering below as this lane's claim; under L41 it counts as two-referee
  signed only when REFEREE-2 signs it independently. I re-derived every step from the frozen text, not from the pre-read.
- Not read before my verdict: docs/referee-2/ on P-N5-WRAP; L-RED 66 R236 / R237, L-COMP 20 BOX 44 (cited DATA, not opened).

## 1. Objects and premises
### 1.1 Objects (git, measured)
- Freeze: claude/l-si e01447e77d57e2cdd26b7e537546c35c49b26fc8 (an ancestor of origin/claude/l-si, checked).
  docs/si/P-N5-WRAP.md sha1 1670432a8a07490ff80ceed45c861515ff070b9b, 56,745 B, 462 lines; line docs/si/P-N5-WRAP-line-L1.txt sha1
  896f9e97394695f903131f832a67f31bcfc23c28, 2,648 B, one line, 35 «(» = 35 «)», 6 «|» (in |V|, |V_E|; 35 landed RESULTS headings
  carry «|», e.g. R96-R101 «n := |V|», so no shape issue). experiments/si/pwrap/out/P-N5-WRAP.sha1 lists both sha1s.
- Instances: experiments/si/box104/inst unchanged from 26704e01 to e01447e7 (`git diff --quiet`); `sha1sum -c SHA1SUMS` 19 / 19 OK on
  `git archive e01447e7`; the 18 sha1 prefixes of §8 equal SHA1SUMS's (my script). WL_1..WL_4 headers «parity 210 / 394 / 599 / 825»:
  211, 395, 600, 826 vertices.
- `bash experiments/si/pwrap/checkW.sh` on that archive (no git; lane's check of quotes, sha1s and the §9 DATA lines): «PWRAP checks:
  PASS», exit 0.

### 1.2 Fleet premises, quoted by my own script
- scratch/pwrap_quotes.py (mine; not the lane's qwrap.py): every outermost «…» after a [Q] mark looked up in SPEC (docs/new/N5-ssi-global.md)
  and P-N5-XICYC.md at trunk 7fa6aff4, in every RESULTS entry there, and in R-WRAP-preread.md at e44ce56b / 90703a81. Log
  pwrap_logs/quotes.out: **30 quotes, 0 missing**: 13 in SPEC (S1 rank, value, order, Ξσ, dual; S2; S4, S4a-c; S5; FIX 1; FIX 3), [N5XI]
  in P-N5-XICYC, [1E-N3], [DUAL] and [RULE] in R104, R15 (a), (c), (d) in R15, ten in my lane's pre-read (one only at 90703a81, the
  Addendum).
- Status of each premise: SPEC is the definition of N5 that R15 / R57 / R104 / R118 run; [N5XI] is R118's definition of N5′-xi; [1E-N3]
  (R57 (b) as landed in R104), [DUAL] (R104 (a)), R15 (a), (c), (d), [RULE] (R104's premise clause; Remark 3 only) are landed. The
  only external premise is [F11], §1.3.

### 1.3 The external premise [F11], from the PDF I opened
- Fetched arxiv.org/pdf/1106.0778v2 into a fresh scratch directory: 618,145 B, sha256
  46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611 (= the packet's pin). `pdftotext` (43 pages); `-layout` for Table 4.
  Read in the extracted text, page numbers by form feed:
  - p. 3: «W.l.o.g. we assume Ω to be injective, i.e. there are no two different nodes with the same priority.»
  - p. 6: «The locally optimizing policy I^loc_G selects a most profitable strategy decision in every point with respect to the
    current valuation. More formally, it holds for every strategy σ, every player 0 node v and every w ∈ vE that w ⪯σ I^loc_G(σ)(v).»
    (glyphs garbled by pdftotext; matches the packet's quote).
  - p. 8: Sink Existence («there is a node v∗ … with v∗Ev∗ and Ω(v∗) = 1 reachable from all nodes; also, there is no other node w
    with Ω(w) ≤ Ω(v∗)»), Sink Seeking («for each player 0 strategy σ with Ξ_ιG ⊴ Ξσ and each node w … the cycle component of Ξσ(w)
    equals v∗»), the remark «the path-length component equals the cardinality of the path component, because all nodes except the
    sink node are more relevant than the cycle node itself», and Lemma 5.1 with its proof (graph and order only).
  - p. 15: Table 4 and «Fact 6.1. The game Gn has 10 · n + 4 nodes, 1.5 · n2 + 20.5 · n + 5 edges and 12 · n + 8 as highest priority.»
  - p. 16: Figure 4 (G_3) labels: d 3, 7, 11; e 4, 8, 12; g 6, 10, 14; k 33, 37, 41; f 35, 39, 43; h 36, 40, 44; c 28; t1 … t6 15 …
    25; a1 … a6 16 … 26; r 32; s 30; x 1.
  - p. 17: Lemma 6.7 with its proof; p. 17-18: «we will assume that b is different from 0n and that the two highest bits in b are zero
    and remain zero, i.e. we will only use the first n − 2 bits for counting. Note however, that every bit works as intended in the
    counter.»
  - p. 23: «Theorem 6.14. Let n > 0. The Strategy Improvement Algorithm with the I loc -policy requires at least 2n improvement steps
    on Gn starting with ιGn .» (2n = 2^n, superscript flattened; the bound is the published theorem's.)
- **F-1 (misprint reading): CONFIRMED independently.** scratch/pwrap_f11.py (mine) builds G_n from Table 4 as I read it, with Table
  4's priorities and with Figure 4's (the six formulas d, e, g, k, f, h minus 2), n = 1..10 (log pwrap_logs/f11_counts.out): Table 4's
  version is NOT injective for any n (g_n = a_1 = 4n + 4) and its maximum is 12n + 10; Figure 4's version is injective for all ten n
  with maximum 12n + 8 = Fact 6.1's, and it reproduces Figure 4's labels at n = 3. Both have 10n + 4 nodes and 1.5n² + 20.5n + 5 edges
  (Fact 6.1). So the game of Theorem 6.14 is read as the Figure-4 game, as the packet says («on the READING that Table 4's six priority
  formulas carry a misprint and Figure 4's priorities are meant»).
- **F-2 («as published»): CONFIRMED** at p. 17-18 (quote above). XI-EXP cites Theorem 6.14 as published, and its «2^Ω(n)» does not
  need more than that. I did NOT read Lemmas 6.2-6.13, so the pre-read's line-by-line «order 4·2^(n−2) minus a constant» is cited,
  not checked by me; it only restates the same 2^Ω(n).
- The facts NT-RUN takes from [F11] (Sink Existence / Seeking, Lemma 5.1, Lemma 6.7, the I^loc property) read as quoted. Lemma 6.7's
  proof uses the edges, the owners and that x has the least priority 1 (true in both versions); my script also checks its graph claim
  (under τ(e_i) = h_i the only cycle of G_n|τ is x's loop): true for n = 1..10. So (T-3) holds: the six differing formulas are not used.

## 2. Proofs, re-derived on W
### 2.1 Definition, count, (R_W), Fact (H), PAD-W, S3-W: CORRECT, no gap
- Count n + 7·m_E + 6·m_O + n_O + 9 re-counted from §2.1's list (7 per Even edge, 6 per Odd edge, pe_o per Odd vertex, 9 core / c_W);
  each H-edge becomes a 6-edge path with inner Ω ≤ 2. Priorities ≤ top + 3, polynomial at bit cost.
- (R_W): Ω ≤ 2 < K2 (3) < K1 (5) < H (≥ 6) < c_W (top) < K0 (top + 2) < K3 (top + 3); K0 even, K3 odd. Correct.
- Fact (H): P2 makes the arena values under σ_new equal W*; v not its own cycle node gives W*(v) = v ⊕ W*(σ_new(v)), so σ_new(v) ∈
  TIE(v) = {w0}; N5′-xi picks inside TIE(v). Correct.
- PAD-W: outside the core and c_W the vertex types strictly advance along every edge (m < g < pβ < x1 < x2 < x3 < b < y; pe, pe_o, pb
  exit); the core's simple cycles each contain K0, K1, K3 or are K2's loop. Correct.
- S3-W: FIX 1 at every vertex with a choice (I re-did all eight cases: V_E → the Ω-2 pad; valve → y; K0 → pA; K1 → s; K3 → K2 (lowest
  odd); gate → pe; o → pe_o; K2 → K2). Correct.

### 2.2 K3-W with K2-r-W, ODD-W, TAU-W, ESC-W, REACH-W: CORRECT, no gap
- K2-r-W and K3-W (a)-(d): all eight core values recomputed; (b) the three comparisons (K3 odd in pA's set; K3 odd in q's set; node K1
  odd so longer is better); (c) τ̄ maximises, r reaches K0's cycle; (d) arena values via K1 (node K1) and via pA (node K2), K0 on no
  arena cycle (q ∉ A(K1)). Correct; every argument uses the core only, as E1-W later needs.
- ODD-W: (a) a pe-free Odd strategy exists and keeps every play from V, gates, valves and inner pads on the 6-edge paths, so its node is
  a vertex of H, below c_W; P1 then excludes pe / pe_o. (b) pe-free strategies ↔ positional Odd strategies of H; values (c, P, 6ℓ),
  the map strictly order-preserving and injective; P1 over all Odd strategies gives the pointwise H-optimum. (c) five more steps, no
  new P-element. (d) follows. Correct.
- TAU-W: Iτ depends on τ alone; under τ0 gates and V_O reach c_W; each alternative (pβ → b, x1 → … → b) lets Even reach K0's even cycle
  via pb, which τ̄ (maximising, [DUAL]) takes or beats; so no alternative is better for Odd; K2 by K3-W (c); induction over S4b, S4c,
  FIX 3. Correct.
- ESC-W: every pad's arena play is m → g → pe → c_W, so TIE(v) = A(v) at V_E; at a valve pb may be improving (when w's H-node is odd,
  K1's reward is higher) but the arena prefers y (node c_W, even) over pb's odd core cycles, and (H) gives y; the core by K3-W (d).
  Correct.
- REACH-W: A(v) = {current pad} ∪ {pads of strictly H-better successors} (ODD-W (d)); the Ξσ-best pick is the pad of a ⊴_H-best
  successor; if the current one is best then A(v) = {σ(v)} (keep-if-best is automatic); the run of H-parts is a Howard run with §2.3's
  tie rule, finite by [R15c]; at T no improving pad, fallback at T + 1 with (K0, K1) ∈ Iσ. For N5: P2 and TIE(v) = A(v). Correct.

### 2.3 E1-W..E4-W and ENDGAME-W: CORRECT, no gap
- E1-W: K3-W's proofs use the core only, so they hold for every σ with K-config κ0; the K-config changes only at a fallback.
- E2-W: Iσ ≠ ∅ at F, an Even fallback (FIX 3); in the core only (K0, K1) is improving: κ1.
- E3-W: values under κ1 recomputed (K0 (K1, {K0}, 1), q (K1, {K0}, 2), …); (K1, q) improving ({K0} even in q's set); arena W*(K1) = (K0,
  ∅, 2) via q, K1 ⊕ W*(s) = (K0, ∅, 4) ≠: (H) gives q; κ2.
- E4-W (a): under κ2 Odd keeps K2's loop (r reaches K0); (K3, K1) improving by reward; at a valve, P1 bounds Ξσ(w) by the play under
  «pe, pe_o, K2-loop», node c_W, so pb (node K0) is improving where σ(b) = y and y is not where σ(b) = pb (this covers valves switched
  at the fallback F); arena: TIE(b) = {pb}, σ_new(K3) = K1 (K3 on no arena cycle): κ3, σ*(b) = pb, not a fallback.
- E4-W (b): at σ* Odd plays pe, pe_o and K2's loop (all alternatives reach K0); every pad of v ∈ V_E has (c_W, ∅, 3): no improving
  edge; valves keep pb; the three core comparisons recomputed: Iσ* = ∅, Iτ = ∅: stop.
- ENDGAME-W: F exists for N5′-xi (T + 1) and for N5 ([R15d] termination; κ0 forbids stopping); then κ1, κ2, κ3 and stop: F + 2
  iterations, one fallback. WRAP (iv) = T + 3. Correct.

### 2.4 Remarks
- Remark 3 (PROVED under [RULE]): the root-first key of each pad (pe, g, m) is fixed, SPEC picks the key-least option of TIE(v) = A(v),
  so each v ∈ V_E moves at most deg(v) − 1 times: F ≤ m_E − |V_E| + 1. Correct given [RULE] (landed in R104's premise clause).
- Remarks 1, 2: READING; not signed.

### 2.5 Claim NT (this lane's claim) and Corollary NT-RUN: CORRECT, no gap
- Claim NT, the packet's rendering: with τ := τσ the play from u is v_1 … v_k then a cycle; Sink Seeking (hypothesis Ξ_ι ⊴ Ξσ) makes
  the cycle component x, and Sink Existence (every other node more relevant than x) forces the cycle to be x's loop and the path
  component to be all of v_1 … v_k; equal values for u ≠ u′ (both ≠ x) put u′ = v_j (j ≥ 2) on u's play, and positionality makes u′'s
  play a suffix that misses u, yet u's path component contains u: contradiction. ⪯ is total, so a node's successors (distinct nodes,
  distinct values) have one maximum. Correct; the rendering matches (T-2) step for step.
- NT-RUN: (G^L_n, ι) is 1-sink (Lemma 6.7 with Lemma 5.1; injective Ω on the Figure-4 reading, §1.3); each Howard step is a non-empty
  unambiguous switch of improvements, so [R15a] gives Ξ_ι ⊴ Ξ_(s_t) by transitivity; SPEC S1's values and order on an injective-Ω game are
  [F11] §3's (rank by (Ω, index) = Ω's order; path set includes the start; length = steps to the cycle node; reward, then the most
  relevant vertex of the symmetric difference by parity, then length by the node's parity); by Claim NT each Even node has one best
  successor, which a Howard step and every policy with the I^loc property must take; the stop rule is the algorithm's. So T is the
  number of improvement steps of Theorem 6.14. Correct.

