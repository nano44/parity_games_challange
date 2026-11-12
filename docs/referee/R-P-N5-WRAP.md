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

## 3. Replay with my lane's code (no lane code; s33's wrap_replay.py, own engine rl_engine.py; logs scratch/wrap_logs/s34_*)
- New seeds (driver wrap_logs/s34_run.sh, 4 min 33 s): modes xi (N5′-xi) and spec (N5) × families rand, dup, even, odd, twin, seed 3440,
  2,000 games each, n ≤ 10, plus PERM = 1 (another index order) on xi rand seed 3441: 11 × 2,000 = 22,000 wrapped games. **All 18
  must-be-0 counters (the box's six and twelve of my lane's: size, w1, w4a-d, w5, w6, w8, v5, rem2, rem3) are 0 on every set**; max T 7,
  max |W| 234. (The odd family has T = 0: a trivial set, counted but not informative.)
- G^L_n alone, my lane's transcription (wrap_f11.py), n = 1..10: T = 8, 26, 62, 134, 278, 566, 1,142, 2,294, 4,598, 9,206 (each ≥ 2^n),
  counters fact61, sinkex, w1all, sinkseek, eqval (equal values of two nodes: Claim NT's DATA), tie: 0 (log s34_f11_H_fig4.out; equal to
  s33's f11_H_fig4.out at e44ce56b, `cmp` EQUAL).
- The firing controls and the exhaustive / wrapped-Friedmann rows are my lane's s33 runs (R-WRAP-preread §5, Addendum 1), not re-run.

## 4. DATA rule (L43), clause by clause
1. §9's six must-0 counters: named, with units (games; states; (step, Even vertex of H) pairs; games), sets and output files; controls
   named with their firing counts; the two-implementation agreement is labelled as agreement of one rule. MEETS.
2. §9's iteration and T_n rows: numbers on named instances (11 … 2,297; 8 … 2,294), formula only as «= 9·2^n − 10» beside the numbers;
   checkW.sh re-reads them from out/wrap_lmcs_xi.out and wrap_long.out. MEETS in the packet.
3. §8 / §10: instances by name and sha1 (checked, §1.1); independent replays cited with commits, in the landed «cited, not re-run» form.
   MEETS.
4. **Line L-1's DATA clause: does NOT meet it.** «DATA: T_n = 9·2^n − 10 for n ≤ 8 on the wrappers (…) and n ≤ 10 on G_n» gives a
   formula, not the numbers, and names no unit, column or file; «n ≤ 10 on G_n» names no source. CHECKER C142 E-1 ruled exactly this
   form out for R128 («the numbers are given as formulas …, not as numbers»). REQUIRED: LW-1 (§5).
5. The DEAD row is not a DATA DEAD: it rests on a proof (WRAP, Claim NT) and a published theorem, and is labelled DEAD-CONDITIONAL until
   two signatures (L43: «DEAD» needs a refereed proof or an instance beyond an explicit bound). Correct use.

## 5. Line L-1 against the statements
- Every clause of L-1 matches a statement of «To sign»: WRAP for every H and s0 with the size and the T + 3 / F + 2 counts; the proof
  lemmas named; premises as §1; Claim NT credited to REFEREE successor 33 (L41) with the lane's rendering; NT-RUN; XI-EXP labelled
  CONDITIONAL with Theorem 6.14 cited as published on the READING F-1; «2^Ω(n) … on a game with O(n²) vertices, so 2^Ω(√|V|)»;
  «exactly T_n + 3 ≥ 2^n + 3», |V| = 10.5n² + 152.5n + 48 (my count, §1.3); the obstruction W-FLAT; the frozen instances; «N5 (SPEC)
  is not affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim». Nothing says more than a signed statement.
- REQUIRED (string; old occurs exactly once, checked by scratch/pwrap_l1fix.py; log pwrap_logs/l1fix.out):
  - LW-1 (L43): «DATA: T_n = 9·2^n − 10 for n ≤ 8 on the wrappers (this lane, L-COMP 20 aa863db5, REFEREE 33 e44ce56b / 90703a81: 18
    counters 0 on 523,721 runs) and n ≤ 10 on G_n;» → «DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations
    − 3 on W^L_n; experiments/si/box104/out/wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd,
    nohoward, fbwrong, endwrong, wrong 0 on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n
    − 10 on these eight), and 4,598, 9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b,
    docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); independent replays, every fail counter 0, their counters in their own
    pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), REFEREE 33 (e44ce56b / 90703a81; 18 counters 0 on 523,721 runs);»
  - The numbers in it: n = 1..8 re-read by checkW.sh's patterns from the frozen outputs (PASS, §1.1) and by my replay; n = 9, 10 from
    s33's log at e44ce56b (`git show`), equal to my re-run. Result on L-1: sha1 **be7da8f3a98e4c5a26158eae9aa2766c56531222**, 3,190 B,
    one line, 39 «(» = 39 «)».
- OPTIONAL (the Lead's call): LW-2, the instance clause «(33 … 2,489 iterations = Howard T + 3)» could name its files (out/
  wrap_fried_xi.out, wrap_long.out, free_xi.out) as LW-1 does; LW-3, «an Even valve with an exit to R117's core»: W's core is K0-K3
  with the pads pA, s, q, r (R117's entry names pA; q, s, r with W's edges are not R117's text); «to the core K0-K3 (with pads pA, s,
  q, r)» would avoid the reference. Neither changes a statement.
- Verdict on L-1: **does NOT match yet**: LW-1 required.

## 6. Scope, XI-EXP and the DEAD row (the Lead's checks)
- **XI-EXP stays CONDITIONAL and does not overstate.** Its label names both conditions (WRAP and Claim NT signed by two referees) and
  the cited theorem with READING F-1. The arithmetic is right: |W^L_n| = Θ(n²), so 2^n = 2^Ω(√|V|); «exponential» is said in n only
  (F-3); the count is «exactly T_n + 3 ≥ 2^n + 3». The «More generally» bullet is labelled READING. Note N-1 (wording, no change
  asked): §7's «nothing about RESULTS R118-R125 or boxes 208 / 209, whose scope is R104's genome games Γ3(G)» — R118's IDEAL-CYC, R122,
  R123, R126 and box 208 are on Γ(G), not Γ3(G); the point (W^L_n is not a genome game) holds for both.
- **The DEAD row's scope is N5′-xi as an M4 candidate only**: «claim killed: N5′-xi makes polynomially many iterations on every parity
  game (gauntlet step 4; M4 candidacy)»; «Not killed by this row: N5 (SPEC)»; status DEAD-CONDITIONAL with both conditions. The scope
  line and §12 say the same. Correct. The exact obstruction (W-FLAT) and the killing family with sha1-pinned instances are given, as
  CLAUDE.md asks.
- CLAUDE.md's trap («A "counterexample" from an unfaithful implementation …»): the kill does not rest on an implementation; it rests on
  WRAP (proved on W from SPEC's text), Claim NT and the published theorem; the implementations are DATA.

## 7. TARGET.md diff: CLEAN
- No statement is about an algorithm for parity games or about W_E / W_O; WRAP and XI-EXP are statements about one candidate's
  iteration count on a family of parity games in TARGET.md §1's sense (W(H, s0) has every vertex with a successor; size polynomial in
  |H| at bit cost, §2.1). §12's reading is right: a dead end for N5′-xi; no algorithm or bound claimed; M3 / M4 untouched; G-N5-TIME
  (about N5) OPEN.

## 0. Verdicts (REFEREE successor 34; date -u at writing: see the commit). First of two referee signatures; REFEREE-2 not read.
| § | statement | verdict |
| --- | --- | --- |
| §2 | Definition of W(H, s0), vertex order, size count, rank facts (R_W), standard state | **SIGN** (definition; count and (R_W) re-derived) |
| §2.4 | Fact (H) | **SIGN** |
| §4.1 | PAD-W (W1) | **SIGN** |
| §4.2 | S3-W = WRAP (i) | **SIGN** |
| §4.3 | K3-W (a)-(d) with K2-r-W | **SIGN** |
| §4.4 | ODD-W (a)-(d) | **SIGN** |
| §4.5 | TAU-W = WRAP (ii) = E0-W | **SIGN** |
| §4.6 | ESC-W | **SIGN** |
| §4.7 | REACH-W = WRAP (iii), first half of (v) | **SIGN** |
| §4.8 | E1-W, E2-W, E3-W, E4-W (a), (b); ENDGAME-W = WRAP (iv), second half of (v) | **SIGN** |
| §3 | Lemma WRAP (i)-(v) as a whole | **SIGN** |
| §5 | Remark 3 (under [RULE]) | **SIGN** (PROVED under [RULE]); Remarks 1, 2 READING |
| §6 | Claim NT (this lane's claim, REFEREE 33; the packet's rendering) | **SIGN** (as its originating lane; L41: needs REFEREE-2's independent signature) |
| §6 | Corollary NT-RUN | **SIGN** (CONDITIONAL on WRAP, as labelled) |
| §7 | Statement XI-EXP | **SIGN AS CONDITIONAL**: correct as stated, conditional on WRAP and Claim NT being signed by two referees, with [F11] Theorem 6.14 cited as published on READING F-1 (both confirmed from the PDF, §1.3) |
| §8 | DEAD row (draft) | scope and obstruction CORRECT: N5′-xi as an M4 candidate only; DEAD-CONDITIONAL until two signatures (L43) |
- Gaps: **none.** External premise: [F11] arXiv 1106.0778v2 (sha256 46c96f44…), opened by me: Theorem 6.14 p. 23, I^loc p. 6, 1-sink
  p. 8, Lemma 6.7 p. 17, the restriction p. 17-18; F-1 (Figure-4 priorities) confirmed by my own transcription; F-2 confirmed; Lemmas
  6.2-6.13 not read (not needed for «as published»).
- Scope of the signatures: as the packet states (scope line): N5 (SPEC) not affected; G-N5-TIME OPEN; not M3 / M4; not a TARGET.md claim.
- Note N-1 (§6): «Γ3(G)» for R118-R126 / box 208 should read «Γ(G) / Γ3(G)»; wording only.
- **Line L-1 (sha1 896f9e97…): does NOT match yet.** Required: LW-1 (L43: the DATA clause gives T_n as numbers with unit, column and
  files; C142 E-1's ruling); my result on L-1: sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222. Optional LW-2, LW-3 (the Lead's call). No
  statement, label or proof changes: a fixes entry with L-2 by script needs a byte test, not a re-sign.
