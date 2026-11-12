# L-COMP BOX 44 (successor 20; Lead «go» 17:37Z 2026-11-12): Lemma WRAP / FREE-REACH on a third engine; box 209 on my own Γ3 builder; a T3 climb. All DATA.
Nothing here is a TARGET.md claim, an M3 / M4 statement or a gauntlet step. Lemma WRAP and Lemma FREE-REACH (L-SI 52, box 104) stay lane lemmas,
unrefereed; box 209 (L-NEW 72: LEVEL3, PLATEAU3, T3-ALL, N5XI-G3) stays a CANDIDATE; N5′-xi stays a CANDIDATE (D1); G-N5-TIME stays OPEN. Every
number names its counter (unit, set, scope). Scope of every run: N5′-xi (RESULTS R118's [N5XI]) or N5 (SPEC) from SPEC's default start S3.
Targets: claude/l-si 26704e01 docs/si/box104-map.md (sha1 in inst/SHA1SUMS.lsi_26704e01_text_out) with experiments/si/box104/inst/ (sha1 list
copied to inst/SHA1SUMS.lsi_26704e01); claude/l-new 311bbf81 docs/new/N5-LEVEL3-box209.md + Addendum A (inst/SHA1SUMS.lnew_311bbf81).
**Independence.** Game builders, valuations of H, Howard runs and every counter are mine and were written from the TEXT; wrap104.py, free104.py,
n5v.py, gamma3.py, level208.py, plat209.py and n5x236.py were not opened before my builds had been compared with the frozen files (L-NEW's
level208.py / plat209.py were then RUN, unmodified, as a cross-check in item 2). The N5′-xi engine (n5xi44.py) is box38/full38.py's loop on my
n5b SpecSI (my port of PGSolver's valuation with SPEC's S1 (iv)-(v) / FIX 2 / FIX 4 choices, written from SPEC's text), so every iteration
count below is independent of L-NEW's n5v and of L-RED's n5x236 **up to SPEC's cycle-node and S4b tie rules** (the wording of L-RED 66's R236,
claude/l-red 7317ed4c), which my engine also implements from SPEC's text. The engine counts where those rules can act (columns «S4b passes /
own-cycle-node vertices / Ξσ-ties»): on every W_n, W(G_n, ι), F_n and frozen-genome row below they act NOWHERE before the first fallback, so
those counts do not depend on them at all; on the random sets the only rule that acts is [N5XI]'s own «SPEC's choice, then the larger index»
among Ξσ-equal options, and every count difference it causes is classified below.

## Item 1: Lemma WRAP (box 104 §3) and Lemma FREE-REACH (§4), third engine
### 1.1 My builder, from the text
Construction lines, quoted from box 104 §3 (wrap44.py's header carries the same quotes):
- «the vertices of H with their owners and indices, and Ω(v) := pr(v) + 6;»
- «for every edge (v, w) with v ∈ V_E: a pad m_(v,w) (Ω 2 if w = s0(v), else 0), an Odd GATE g_(v,w) (Ω 1), pads pe_(v,w) (Ω 1) and pβ_(v,w)
  (Ω 0), with the edges v → m → g, g → pe → c_W and g → pβ → b_(v,w);»
- «for every edge (o, w) with o ∈ V_O: pads x1, x2, x3 (Ω 0), with the edges o → x1 → x2 → x3 → b_(o,w);»
- «for every edge (a, w) of H: a VALVE b_(a,w) (Even, Ω 0) and pads y_(a,w) (Ω 2), pb_(a,w) (Ω 1), with the edges b → y → w and b → pb → K0;»
- «for every o ∈ V_O: a pad pe_o (Ω 1), with the edges o → pe_o → c_W;»
- «c_W (Even, a self-loop, Ω top := the least even number ≥ max Ω(V) + 2), and R117's core with its pads: K0 (Even, top + 2) → {K1, pA},
  pA → K3, K1 (Even, 5) → {q, s}, s → K1, q → K0, K2 (Odd, 3) → {r, K2}, r → K1, K3 (Even, top + 3) → {K1, K2}; pA, s, r have Ω 0, q has Ω 1.»
- «Every pad is an Even vertex with one successor; the new vertices are indexed after V.» «|W| = n + 7·m_E + 6·m_O + n_O + 9.»
Readings (mine): R1 the text fixes no order of the new vertices beyond «after V»; my order is: the Even-edge gadgets (m, g, pe, pβ) edge by
edge, the Odd-edge pads (x1, x2, x3), then (b, y, pb) for every edge, pe_o for every o, then c_W, K0..K3, pA, s, q, r. R2 «max Ω(V)» is over
H's vertices. R3 H's edges are a set.
- Comparison with the frozen instances (wchk44.py fam; wrap44.canon = colour refinement with exact signatures, no hashing, individualisation
  if needed; none was needed). **All 11 frozen wrapper files (W_2 … W_8, WL_1 … WL_4) are isomorphic to my build with H's vertices fixed
  pointwise** (owners, priorities, edges); no mismatch. They are not byte-equal to my build in my vertex order: the only difference is the
  index order of the new vertices. Reading that order off the isomorphism (c_W, K0..K3, pA, s, q, r first; then vertex by vertex, edge by
  edge: pb, y, b, then pβ, pe, g, m or x3, x2, x1; pe_o after an Odd vertex's edges; for G_n the edges in Table 4's order) and building in it
  (ORDER=lsi), **my builder's output is byte-identical to all 11 files** (table, column «bytes equal»).
- Random games: on the 300 frozen games of rand300.json (copied to inst/, sha1 cf421936) my |W| equals the frozen «W» on 300 of 300.
- H for the families: PGSolver's switchallexp_n from trunk experiments/hard-families/pgsolver_port.py with its best-reward start (my n5b's
  initial_strategy_by_best_reward); Friedmann's G_n with ι = my transcription of [F11] Table 4 (wchk44.lmcs, as box 43's, with Figure 4's
  injective priorities as box 104 §5.1 quotes them, or Table 4's as printed), Fact 6.1's node and edge counts asserted.
### 1.2 WRAP's six counters, and mine
Counters as box 104 §3 defines them: s3fail «unit games: S3's pair is not the standard state of s0», nonstd «unit states before the first
fallback», nohoward «unit (step, Even vertex of H) pairs before the first fallback: the new successor is not a ⊴-best successor BY H'S OWN
VALUATION …, or a best current successor was left», fbwrong «unit games: the first fallback is not at T + 1» (T := the first state whose
H-part has no Even vertex with a strictly better successor by H's own valuation), endwrong «unit games: fallbacks ≠ 1 or iterations ≠ T + 3»,
wrong «unit games: regions of W ≠ harness Zielonka on W». Mine in addition: stratbad (unit games: harness verify.check rejects N5′-xi's output
strategies; TARGET.md §5), outsideA (unit (step, Even vertex of H): a move to a successor that is not strictly better by H's valuation),
valdiff (unit (state, vertex of H): n5b's valuation of H ≠ my independent evaluator val44.evaluate, which computes Odd's optimal reply by
one-player improvement on play values and shares no code with PGSolver's evaluation). «Nine must-0 counters» = these nine. Not must-0: tdiff
(T ≠ the length of MY Howard run of H under «keep a best current successor, else the largest index»; needs a tie event).
- **The 300 frozen random games** (inst/rand300.json; out/wrap44_rand300.out; my vertex order; valdiff on): the nine must-0 counters are 0
  on 300 of 300. (T, iterations, |W|) equals the frozen row on **300 of 300** (max T 4, Σ T 348, Σ iterations 1,248 = Σ T + 900, max |W| 268;
  T = 0 / 1 / 2 / 3 / 4 on 82 / 126 / 61 / 24 / 7 games).
- Tie-rule census on these runs (sums over the 300 games, before the first fallback; over all passes in brackets): S4b passes 0 (0);
  own-cycle-node vertices 0 (0); (pass, vertex) pairs with two or more Ξσ-best options 24 (90), on 22 games, decided by SPEC's choice 16 (65)
  and by the index 8 (25). So the only tie rule that acts on a wrapper is [N5XI]'s last clause («SPEC's choice, then the larger index»).
- Its effect, measured by re-running with the new vertices of W in another index order, or with that clause changed (out/wrap44_rand300_rev.out,
  _rand1.out, _tiemin.out; classified by cls44.py as L-RED 66 did in R236, out/cls44_*.out): the nine counters stay 0 in every variant. Rows
  differing from the frozen (T, iterations, |W|): reversed order 9 of 300; shuffled order (seed 1) 12; «smaller index, SPEC's choice ignored»
  3. Runs compared with my order, as start / tie rule / real / fallback: reversed 0 / 12 / 0 / 0 (288 the same run); shuffled 0 / 15 / 0 / 0
  (285); smaller index 0 / 7 / 0 / 0 (293). Against MY Howard run of H with no wrapper («keep a best current successor, else the largest
  index»): 0 / 16 / 0 / 0 (284 the same run; 14 differ in T, the tdiff column). **Every difference is a tie of Howard's rule**: at the first
  differing state both runs chose ⊴-best successors by H's own valuation. No start, fallback or real difference.
- Reading of the 300 of 300: L-SI's vertex order and mine both index the pads of v by increasing w, so the index clause picks the same pad.
  Under another order T changes on 3-4 % of these games; «a Howard run of H, then exactly 3 iterations, one fallback» holds in every variant.
- N5 (SPEC) on the 300 games (out/wrap44_rand300_spec.out, _spec_lsi.out): s3fail, nonstd, endwrong, wrong, stratbad, outsideA 0; 3 / 4 / 5 / 6
  iterations on 142 / 136 / 21 / 1 games, per game the same in my order and in the frozen order (0 of 300 rows differ).
- Controls (first 100 games; out/wrap44_ctrl1..5.out): CTRL=1 (best := worst) nohoward 405; CTRL=2 (T shifted by one) fbwrong 100, endwrong
  100; CTRL=3 (standard state with σ(K0) = K1) s3fail 100, nonstd 218; CTRL=4 (Zielonka on W with c_W odd) wrong 100; CTRL=5 (every strategy
  entry with a choice replaced) stratbad 100. (L-SI's own controls on the same 100 games: nohoward 405, fbwrong 100, endwrong 100; it had
  none for s3fail, nonstd, wrong.)
- Inside the lemma (w4chk44.py; out/w4chk44.out): (ii) «At every state of the N5′-xi run (and of the N5 run) from S3: τ = τ0 and Iτ = ∅»,
  (W1) «no pad, gate or valve is ever a cycle node or in a P-set», (W4) «(a) σ̄(g) = pβ at every gate and σ̄(o) ≠ pe_o at every o ∈ V_O;
  (b) for v ∈ V, Ξσ(v) = (c, P, 6ℓ) where (c, P, ℓ) = Ω^H_s(v); (c) Ξσ(m_(v,w)) = (c, P, 6ℓ + 5)». Counters tauch, itau (unit states, ALL
  states of the run), w4a (unit (Odd vertex, state before the first fallback)), w4b, w4c (unit (vertex, state)), w1:
  | set | tauch | itau | w4a | w4b | w4c | w1 | note |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 300 random games, N5′-xi (1,248 iterations) | 0 | 0 | 0 | 0 | 0 | 0 | Odd's optimal reply is not unique at 290 (Odd vertex, state) pairs (not a failure) |
  | 300 random games, N5 (spec; 1,081 iterations) | 0 | 0 | 0 | 0 | 0 | 0 | |
  | switchallexp_n, n = 2 … 6, and G_n (Figure 4), n = 1 … 6: every row | 0 | 0 | 0 | 0 | 0 | 0 | |
  | CONTROL, factor 5 for 6: 300 random games / G_3 | 0 / 0 | 0 / 0 | 0 / 0 | 3,818 / 2,079 | 4,571 / 3,528 | 0 / 0 | fires |
### 1.3 The families (out/wrap44_fam.out, wrap44_famlsi.out, wrap44_fam_spec*.out; table by tab44.py)
| H | n | \|H\|, edges | T: my Howard on H (tie events) | \|W\| | N5′-xi on my build: iterations, fallbacks | iterations − T | sum of the nine must-0 counters | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback | frozen file vs my build (my order): isomorphic, H's indices fixed | frozen file vs my build in the frozen order: bytes equal; run on it: iterations | N5 (spec): my order / frozen order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switchallexp_n | 2 | 35, 75 | 30 (0) | 567 | 33, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 33 (must-0 sum 0) | 3 / 3 |
| switchallexp_n | 3 | 49, 109 | 70 (0) | 818 | 73, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 73 (must-0 sum 0) | 4 / 4 |
| switchallexp_n | 4 | 63, 143 | 150 (0) | 1069 | 153, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 153 (must-0 sum 0) | 5 / 5 |
| switchallexp_n | 5 | 77, 177 | 310 (0) | 1320 | 313, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 313 (must-0 sum 0) | 6 / 6 |
| switchallexp_n | 6 | 91, 211 | 630 (0) | 1571 | 633, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 633 (must-0 sum 0) | 7 / 7 |
| switchallexp_n | 7 | 105, 245 | 1243 (0) | 1822 | 1246, 1 | 3 | 0 | 0 / 0 / 0 | True | True; not run | not run / not run |
| switchallexp_n | 8 | 119, 279 | 2486 (0) | 2073 | 2489, 1 | 3 | 0 | 0 / 0 / 0 | True | True; not run | not run / not run |
| G_n, ι (Figure 4 priorities) | 1 | 14, 27 | 8 (0) | 211 | 11, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 11 (must-0 sum 0) | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 2 | 24, 52 | 26 (0) | 395 | 29, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 29 (must-0 sum 0) | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 3 | 34, 80 | 62 (0) | 600 | 65, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 65 (must-0 sum 0) | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 4 | 44, 111 | 134 (0) | 826 | 137, 1 | 3 | 0 | 0 / 0 / 0 | True | True; 137 (must-0 sum 0) | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 5 | 54, 145 | 278 (0) | 1073 | 281, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 6 | 64, 182 | 566 (0) | 1341 | 569, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | 4 / 6 |
| G_n, ι (Figure 4 priorities) | 7 | 74, 222 | 1142 (0) | 1630 | 1145, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Figure 4 priorities) | 8 | 84, 265 | 2294 (0) | 1940 | 2297, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 1 | 14, 27 | 8 (0) | 211 | 11, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 2 | 24, 52 | 26 (0) | 395 | 29, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 3 | 34, 80 | 62 (0) | 600 | 65, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 4 | 44, 111 | 134 (0) | 826 | 137, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 5 | 54, 145 | 278 (0) | 1073 | 281, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
| G_n, ι (Table 4 priorities) | 6 | 64, 182 | 566 (0) | 1341 | 569, 1 | 3 | 0 | 0 / 0 / 0 | no frozen file | no frozen file | not run / not run |
- L-SI's lane counts are reproduced on every row: 33, 73, 153, 313, 633 (W_2 … W_6; box 104 §5.2), 11, 29, 65, 137, 281, 569 (W(G_n, ι), n =
  1 … 6), and the Lead's relayed 1,145 and 2,297 with Howard T 1,142 and 2,294 at n = 7, 8. W_7 and W_8 (1,246 and 2,489 iterations) were
  «not run» at the freeze 26704e01; L-SI's box 104 Addendum A (claude/l-si 01900837, out/wrap_long.out, read after my runs) has the same
  four long rows: 1,246, 2,489, 1,145, 2,297. Here all nine counters are 0 on them. T equals 9·2^n − 10 on G_n (n ≤ 8).
- No tie rule acts on any family row: before the first fallback S4b never runs, no Even vertex with a choice is its own arena cycle node,
  and no two Ξσ-best options tie; my Howard run of H has 0 tie events. So these counts are the same under every tie rule.
- **N5 itself (SPEC) on W(G_n, ι): 4 iterations on my build, 6 on L-SI's (its out/wrap_lmcs_spec.out: «F 4 iterations 6»).** Classified:
  TIE RULE (vertex index). On the byte-equal builds (ORDER=lsi) my engine also makes 6 (first fallback at 4); the two builds differ only
  in the index order of the new vertices, and SPEC's pick inside TIE(v) = A(v) goes by index (WRAP (v), Remark (3)). The must-0 counters
  of WRAP (v) (s3fail, nonstd, endwrong = «fallbacks ≠ 1 or iterations ≠ F + 2», wrong, stratbad, outsideA) are 0 in both orders. On W_n
  both orders give 3, 4, 5, 6, 7 (n = 2 … 6), L-SI's numbers. So N5's count on a wrapper is not a property of (H, s0) alone.
### 1.4 F_n (box 104 §4-§5: the free Γ3-shaped form of L-RED 54's compiled switchallexp_n) (out/free44.out; table by tab44.py)
Text used: «G* = (G, π): G has the data of an R104 genome without its β-ranks and parities … and π is an injective map from the 2M CARRIERS
β_q, e_q into the integers ≥ 6, of either parity. Γ3*(G*) is R117's Γ3 (same vertices, indices, owners, edges and pads) with Ω(β_q) :=
π(β_q), Ω(e_q) := π(e_q), top := the least even number ≥ max π + 2, Ω(c_W) := top, Ω(K0) := top + 2, Ω(K3) := top + 3; movers 0, gates 1,
c_X 2, K2 3, K1 5 and the pad priorities are R117's.» I did not rebuild comp(G_n) (L-RED's compiler) or π_n: free44.decode reads a free
genome (G, π) back from each frozen F_n.pg by its SHAPE alone (gates = Odd vertices of priority 1; m-pads = the vertices whose one
successor is a gate; movers = Even vertices all of whose successors are m-pads; levels from the W-targets, checked for consistency), and
free44.g3free (my builder: box34/own34.build's vertex order with the definition's priorities) rebuilds the game from it.
| F_n | N, M | \|V\|, edges | T(G_n): my Howard on switchallexp_n (tie events) | N5′-xi on F_n: T3*, iterations, fallbacks | iterations − T | sum of the eleven counters | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback | rebuilt from its decoded free genome by my builder: bytes equal | e-vertices below some β; odd β above some e; carriers; c_W | N5 (spec): iterations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F_2 | 54, 92 | 708, 929 | 30 (0) | 30, 33, 1 | 3 | 0 | 0 / 0 / 0 | True | 92 of 92; 16; 6..348; 350 | 5 |
| F_3 | 76, 133 | 1017, 1338 | 70 (0) | 70, 73, 1 | 3 | 0 | 0 / 0 / 0 | True | 133 of 133; 23; 6..500; 502 | 5 |
| F_4 | 98, 174 | 1326, 1747 | 150 (0) | 150, 153, 1 | 3 | 0 | 0 / 0 / 0 | True | 174 of 174; 30; 6..652; 654 | 5 |
| F_5 | 120, 215 | 1635, 2156 | 310 (0) | 310, 313, 1 | 3 | 0 | 0 / 0 / 0 | True | 215 of 215; 37; 6..804; 806 | 5 |
| F_6 | 142, 256 | 1944, 2565 | 630 (0) | 630, 633, 1 | 3 | 0 | 0 / 0 / 0 | True | 256 of 256; 44; 6..956; 958 | 6 |
| F_7 | 164, 297 | 2253, 2974 | 1243 (0) | 1243, 1246, 1 | 3 | 0 | 0 / 0 / 0 | True | 297 of 297; 51; 6..1108; 1110 | not run |
| F_8 | 186, 338 | 2562, 3383 | 2486 (0) | 2486, 2489, 1 | 3 | 0 | 0 / 0 / 0 | True | 338 of 338; 58; 6..1260; 1262 | not run |
- **Every frozen F_n (n = 2 … 8) is byte-identical to Γ3*(decode(F_n)) built by my builder**, so each is a Γ3*-shaped game of a free genome
  with N = 22n + 10, M = 41n + 10, |V| = 309n + 90 (box 104 §5.1's formulas) and two levels. The census column reproduces L-SI's out/prio.out
  (every e-vertex below some β; no odd e; 16, 23, 30, 37, 44, 51, 58 odd β above some e: not R104 genomes).
- FREE-REACH's counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong, as §4 defines them, T3* := the first state at which no mover has
  a strictly better successor) + stratbad, outsideA, valdiff (my evaluator on the whole game at every 10th state), tdiff (T3* ≠ T(G_n)),
  profdiff (unit steps: #movers that switch at step t ≠ #Even vertices of G_n that switch at step t of MY Howard run of switchallexp_n): all
  0 on every row. Iterations 33, 73, 153, 313, 633, 1,246, 2,489 = T(G_n) + 3, one fallback: L-SI's counts. Controls on F_2
  (out/free44_ctrl.out): CTRL=1 nohoward 660; CTRL=2 fbwrong 1, endwrong 1; CTRL=3 s3fail 1, nonstd 31; CTRL=4 wrong 1.
- What this does NOT check: that F_n is the image of switchallexp_n under L-RED's comp.py with box 104's π_n (I did not run comp.py); the
  evidence here for «F_n carries Howard's run of G_n» is T3* = T(G_n) and the equal switch-count profile at every step, not L-SI's
  vertex-by-vertex xtraj.

## Item 2: box 209 on my own Γ3 builder (lev44.py; my engine)
Game: box34/own34.build (my text builder of Γ3(G), BOX 34). Run: n5xi44 from S3 to the END. States 0 … T3 = the states before the first
fallback. σ̄_t is read off the values (the successor w of an Odd vertex with Ω_t(v) = ext(v, Ω_t(w))). 47 must-0 counters, written from box
209's text (units in lev44.py's header):
- premises as landed, re-measured (13): s3fail, nonstd, nohoward, fbwrong (R125 REACH3-ALL / HOW3), f1, dom, cn23 (CN2-3), notie3, locgate3,
  k2r (LOC-K2-3), bonly3, odd2 (σ̄ unique), edom3;
- §2 (12): k0a, k0b, k0c (K0′), k2 (COARSE, on class-adjacent pairs of a mover's successors and of a gate's faces), mono (K1′), k3a, k3b, k3c,
  k3d, k3e (K3′), k4 (K4′), k5 (K5′);
- §3 LEVEL3 (8): l1sub, l1phi, phifall (L1′), l2 (L2′), l3, l3val (L3′), l4 (L4′, with the kinds mover → m-pad → gate → pβ → β along the stall
  cycle), qfail (L5′: more than P3 = 2M(N + 4M) values of Φ, or a value on two intervals);
- §4 PLATEAU3 (10): plat ((i): v − u > n_E3 = N + 6M + 9), p1, p2, p3, p4, p6, p7 ((P1)-(P7)), c2 (b′ = q + Σ(v − u)), t1, tail ((ii));
- §5 and output (4): t3all (T3 > P3·(n_E3 + 1) + n_E3), n5xig3 (fallbacks ≠ 1 or iterations ≠ T3 + 3), wrong (regions ≠ Zielonka), stratbad.
Reference states: L-NEW's data use b = T3 only; LEVEL3 and PLATEAU3 are stated for EVERY reference state b, so lev44 also runs them for every
b = 1 … T3 on the small sets (BREF=all) and for 3 further evenly spaced b on the long runs (BREF=k:3).
| set (file in out/) | genomes | sum of my 47 must-0 counters | max T3 | max T3 / bound | sum of T3 | stalls | plateaus (longest) | longest tail | reference states per genome | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback (sums) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lev44_records.out | 25 | 0 | 114 | 8.10e-06 | 1011 | 31 | 14 (9) | 2 | 1-4 | 0 / 0 / 0 |
| lev44_corpus.out | 53 | 0 | 199 | 7.20e-06 | 1646 | 48 | 15 (13) | 0 | 3-4 | 0 / 0 / 2 |
| lev44_dead.out | 3 | 0 | 21 | 3.81e-05 | 50 | 16 | 5 (8) | 4 | every b | 0 / 0 / 0 |
| lev44_rand.out | 1000 | 0 | 8 | 1.77e-04 | 1731 | 105 | 83 (3) | 5 | every b | 0 / 0 / 48 |
| lev44_mut.out | 600 | 0 | 32 | 5.91e-07 | 13167 | 1521 | 483 (15) | 25 | every b | 0 / 0 / 0 |
- Sets. records / corpus / dead: L-NEW's frozen 25 + 53 + 3 (box 209 §6's list; sha1 of each in inst/SHA1SUMS.lnew_311bbf81). mine: box39/inst
  ∪ box40/inst (which holds the 26 genomes of L-RED r232's SHA1SUMS that L-SI's replay uses) ∪ box42 CL0, CL30. rand: this lane's law
  (box43/rand43.rgen), seed 4411, 300 each at P(Ξ-target = X) = 0.6 / 0.3 / 0.0 with N + M ≤ 60, and seed 4412, 100 with N + M ≤ 160: 1,000
  genomes. mut: 100 mutants (1-6 moves of box39/mut39.mutate, seed 4420) of each of CFI3_n48, K1L10_n48, K1F21_n48, MWR4_2, CW4_n, K1D4_n48.
  big: the long runs of BOX 42 / 43 (next table).
- Controls fire (out/lev44_ctrl1..6.out, on CFI3_n48, MWR4_2, DEAD_SEG2P_d4_N8): 1 (FRONT := the highest lagging class) l1phi 30, phifall 21,
  l2 60, l3 60, l4 55, p1 2,265, p3 20, p4 7; 2 (Y := FRONT_u) p1 2,733, p2 82; 3 (bounds := 1, 0) qfail 3, plat 3, t3all 3; 4 (T3 shifted)
  fbwrong 3, n5xig3 3; 5 (σ̄ at a gate := the other face) k3a 5,141, k3c 5,555, k4 5,555, l4 15, p2 1,012, p4 1,012; 6 (class order reversed
  on E) k2 1,732, mono 2,132, k4 414, k5 1,714 and LEVEL3 / PLATEAU3 counters. No control: tail, t1 (every tail is short), cn23, bonly3,
  k0a-k0c, k3b, k3e, odd2, edom3, f1, dom, notie3, k2r, c2, wrong, stratbad.
- Against L-NEW's frozen rows (cmp44.py; claude/l-new 311bbf81 box209/out): (T3, number of Φ values, stalls, plateaus, longest plateau,
  tail) per genome: records 25 of 25, corpus 53 of 53, dead 3 of 3 equal, against BOTH of its engines (its n5v rows and its rows on L-RED
  65's HOW3 engine): 0 differing rows. Its nine LEVEL3 counters and my 47 are 0 on all 81.
- Against L-SI's replay (claude/l-si 925577fe experiments/si/box104/out/replay209_level.out, replay209_plat.out: L-NEW's counter code on L-RED
  65's HOW3 engine, L-SI's 26 frozen genomes; out/cmp44_lsi925577fe.out, one line per genome, all 26 listed): 26 of 26 EQUAL in (T3, number
  of Φ values, stalls, plateaus, longest plateau, tail); my must-0 sum 0 and L-SI's 9 + 9 counters sum 0 on all 26; largest T3 199
  (MW32_2). My rows come from my sets records (5), corpus (11) and mine (10: C98_* 7, Ku_4/8/16, Kprev_8 — box40/inst; 59 distinct genomes
  in «mine», must-0 sum 0; MWR4/8/16_2 occur in both box39/inst and box40/inst with equal sha1 and run once).
- The cross (L-NEW's own counter code, claude/l-new 311bbf81 box208/level208.py --hist (16 counters) and box209/plat209.py --hist (9
  counters), run unchanged with python3 -I on the history of MY builder + engine; run44c.sh; compared by cross44.py, whole line character for
  character after «plat3 hist » := «plat3 »; out/cross44.out): records 25, corpus 53, dead 3 — 0 differing lines against BOTH of L-NEW's
  engines (its n5v rows level3_* / plat3_* and its rows on L-RED 65's HOW3 engine own3_*), level and plat; mine 59 runs, of which the 26 of
  L-SI's replay (925577fe) compare: 0 differing lines, level and plat. L-NEW's 16 + 9 counters sum 0 on all 140 of my runs.
### T3 against the T3-ALL bound; the largest T3 seen (out/lev44_big.out; table by tab44.py)
| genome | N + M | n | T3 | iterations | bound P3·(n_E3 + 1) + n_E3 | T3 / bound | sum of my 47 | stalls, plateaus (longest), tail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TMWR4 | 153 | 769 | 30 | 33 | 61531483 | 4.876e-07 | 0 | 0, 0 (0), 0 |
| TMWR8 | 269 | 1365 | 54 | 57 | 348030879 | 1.552e-07 | 0 | 0, 0 (0), 0 |
| TMWR16 | 501 | 2557 | 102 | 105 | 2303241703 | 4.429e-08 | 0 | 0, 0 (0), 0 |
| TMWR32 | 965 | 4941 | 198 | 201 | 16680259959 | 1.187e-08 | 0 | 0, 0 (0), 0 |
| MWR32_2 | 957 | 4909 | 198 | 201 | 16359115035 | 1.210e-08 | 0 | 0, 0 (0), 0 |
| TREC | 307 | 1523 | 48 | 51 | 483615361 | 9.925e-08 | 0 | 0, 0 (0), 0 |
| TC6G8 | 212 | 1146 | 17 | 20 | 205932255 | 8.255e-08 | 0 | 0, 0 (0), 0 |
| TDHIB26 | 412 | 2210 | 28 | 31 | 1488256823 | 1.881e-08 | 0 | 1, 1 (1), 0 |
| D10_k128 | 1168 | 6770 | 28 | 31 | 43136380685 | 6.491e-10 | 0 | 1, 1 (1), 0 |
| D18_k32 | 1104 | 6898 | 28 | 31 | 45717250925 | 6.125e-10 | 0 | 1, 1 (1), 0 |
| D80_k128 | 1040 | 5874 | 28 | 31 | 28142642189 | 9.949e-10 | 0 | 1, 1 (1), 0 |
| CL131 | 1202 | 7122 | 14 | 17 | 50257678866 | 2.786e-10 | 0 | 0, 0 (0), 0 |
| MWR48_2 | 1421 | 7293 | 294 | 297 | 53710057643 | 5.474e-09 | 0 | 0, 0 (0), 0 |
| TMWR48 | 1429 | 7325 | 294 | 297 | 54417975559 | 5.403e-09 | 0 | 0, 0 (0), 0 |
- All sets (records, corpus, dead, rand, mut, mine, big; 1,754 genome runs = 1,681 + 59 + 14; counter t3all and every other must-0 counter
  0 on every row; run by successors 20 and 21): the largest T3 is 294 (MWR48_2, N + M 1,421, bound 53,710,057,643, ratio 5.5e-09; TMWR48,
  N + M 1,429, the same T3); the largest T3 / bound is 1.77e-04 (rand_s4411_nm60_px0.3_115: T3 1, bound 5,660). The data do not test the
  constants of T3-ALL: no run is within a factor 5,000 of its bound. The long runs (14 genomes, N + M 153-1,429) were re-run by successor 21
  (successor 20's rows were lost with its container, never committed).

## Item 3: a climb on T3 / (N + M) at N + M ≈ 300
RUNNING at this commit (item 3 is pushed separately when both streams end). climb44.py / run44d.sh; band 280 ≤ N + M ≤ 320; seeds gen37(9): T3
61 at N + M 290, ratio 0.2103; gen37(10): 67 at 319, 0.2100; MWR(9): 60 at 290; MWR(10): 66 at 319, 0.2069. Successor 20's climb state was
lost with its container; successor 21 restarted stream 1 from its seed (RNG seeded by (4431, restart, step), so the run repeats): restart 0
again reaches T3 65 at N + M 285 (ratio 0.2281; text engine agrees, box 209 counters 0), as successor 20 reported. No result is claimed here yet.

## Files
wrap44.py (builder, canonical relabelling, isomorphism), n5xi44.py (engine + tie-rule census), val44.py (independent evaluator, Howard),
wchk44.py, w4chk44.py, cls44.py, free44.py (item 1); lev44.py, rand44.py, cmp44.py (item 2); climb44.py (item 3); sum44.py, tab44.py; run44a.sh
(item 1), run44b.sh (item 2), run44c.sh (L-NEW's counter code on my runs), run44d.sh (item 3). inst/: rand300.json (copy of L-SI's),
SHA1SUMS.* (every other-lane input and frozen output used), seed_*.json and the frozen climb bests. out/: every output, with out/SHA1SUMS.
Environment: LSI104 = an archive of claude/l-si 26704e01 (experiments/si/box104/inst); LNEW209 = an archive of claude/l-new 311bbf81
(experiments/new, experiments/si/si.py, experiments/harness, experiments/n5-second, experiments/hard-families); box37/bin/fast37_w<w> (built
from box37/fast37.c) for the climb. Every phase is resumable.
