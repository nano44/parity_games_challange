# L-COMP BOX 43 (successor 19; Lead «go» 13:17Z 2026-11-12): box 208 on an independent engine, its lift to G_N; DHIB family; one-gate family. All DATA.
Nothing here is a TARGET.md claim. Box 208 (L-NEW 72: Lemma LEVEL, Lemma PLATEAU, Theorem ALL-TCYC) stays a CANDIDATE on IDEAL-CYC
(lane, unrefereed); CONJECTURE DEEP3 stays OPEN; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Every number names its counter
(unit, set, scope). Target of item 1: claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md (sha1 55e65381), tools experiments/new/box208/.

## Item 1 (a): box 208's counters on MY engine
Engine: box37/ideal37.py (my builder of Γ(G), n5b SpecSI values with Odd's optimal counterstrategy, my Howard step and tie rule).
- hist43.py writes its run in level208.py's --hist format (no L-NEW code). run43a.sh feeds it to L-NEW's counter code: level208.py
  --hist (the 16 must-0 counters: monofail, k3fail, k4fail, k5fail, einF, l3fail, phifail, stallnocyc, nofvs, rstall, boundfail,
  winstall, wbeta, wl3fail, wmid, wbound; window counters for k ≤ 3 only, as in level208) and plat208.plateaus (p1, pclos, p2, p3, p4,
  p5; through plathist43.py, because plat208.py has no --hist mode at 8db300fe).
  | set | genomes | sum of the 16 | sum of the 6 plateau counters | compared with L-NEW's frozen files |
  | --- | --- | --- | --- | --- |
  | records (the 25 k = 1 genomes of box 208 §7) | 25 | 0 | 0 | level43_records.out = level208_records.out = own208_records.out, plat43_records.out = plat208_records.out: every line identical (sorted diff empty) |
  | corpus (box202/inst) | 53 | 0 | 0 | level43_corpus.out = level208_corpus.out = own208_corpus.out, plat43_corpus.out = plat208_corpus.out: every line identical |
  | mine (box39/inst ∪ box40/inst, 57 distinct; k = 1: 31, 2: 10, 3: 2, 4: 1, 5: 2, 8: 1, above the cap: 10) | 57 | 0 | 0 | not in L-NEW's data (CW32_own T 225, MW32_2 T 199, DHIB26_2804, DWT20_2803, C6G8_n54, RWX_n95, FW16_2, …) |
  So three engines (L-NEW's gfc203 / idealcyc, L-RED 54's own.py via L-NEW's adapter, mine) give the same lines on the 78 frozen genomes.
  On «mine»: 27 plateaus, longest 9 steps (K1D4_n48); largest 100·(v − u) / (movers of Y + 1) = 80 (C98_2_2_3: a 4-step plateau with
  4 movers in Y; L-NEW's largest was 57).
- MY OWN counters, lev43.py: 23 must-0 counters written from box 208's TEXT (definitions quoted in the header; no code of level208.py
  or plat208.py): mono (K1), k3c, k3d (K3), k4 (K4), k5 (K5), l1sub, l1phi, phifall (L1), l2 (L2), l3, l3val (L3), l4 (L4), c2 (C2),
  c4 (C4), qfail (L5 / C1), plat (PLATEAU's bound N + 2M + 5), p1, p2, p3, p4, p6, p7 (Addendum A (P1)-(P7)), tcyc (ALL-TCYC's bound).
  Reference b = T. Unit and scope per counter in the header.
  | set (file in out/) | genomes | sum of my 23 | max T | max q | stalls (max per genome) | longest plateau |
  | --- | --- | --- | --- | --- | --- | --- |
  | lev43_records.out | 25 | 0 | 114 | 114 | 9 | 9 |
  | lev43_corpus.out | 53 | 0 | 199 | 199 | 14 | 13 |
  | lev43_mine.out (the 57 + box42 CL0, CL30) | 59 | 0 | 225 | 225 | 9 | 9 |
  | rand43.out, random, this lane's law (rand43.py; seeds 4311-4314; N + M ≤ 60 with P(Ξ-target = X) = 0.6 / 0.3 / 0.0, 1,000 each; N + M ≤ 160, 300) | 3,300 | 0 | 9 | 7 | 4 | 4 |
  | rand43.out, mutants (1-6 moves of box39/mut39.mutate, seed 4320, 150 each of CFI3_n48, K1L10_n48, K1F21_n48, MWR4_2, CW4_n, DSALT6_n108, C6G8_n54, RWX_n95, DHIB26_2804) | 1,350 | 0 | 32 | 32 | 15 | 15 |
  - My descriptive numbers (T, number of Φ values, stalls, plateaus, longest plateau) equal L-NEW's counters' on all 135 runs that have
    both (sum43.py: 0 differences).
  - Controls fire (30 mutants of CFI3_n48, seed 4321): LV43_CTRL=1 (FRONT := the HIGHEST lagging class): l1phi 103, phifall 58, l2 486,
    l3 486, l4 471; LV43_CTRL=2 (plateau set Y := FRONT): p1 14,582, p2 1,654.

## Item 1 (c): measured T_CYC against ALL-TCYC's bound P(N + 2M + 6) + N, P = 2M(N + 2M) (out/sum43.out: one line per genome)
- On every genome run (106 distinct frozen genomes, 3,300 random, 1,350 mutants): T_CYC ≤ the bound (tcyc 0), q ≤ P (qfail 0), every
  plateau ≤ N + 2M + 5 (plat 0), tail T − b′ ≤ N (c4 0).
- The data do not test the constants. Largest T_CYC / bound: 5.55e-04 (C98_2_2_3: 8 against 14,404); random sets ≤ 8.09e-04. Longest
  runs: CW32_own T_CYC 225 against 17,288,282,891 (1.3e-08; q 225 of P 6,391,232; no plateau), MW32_2 199 against 3,435,689,820.
  Largest q / P: 8.3e-03 on frozen genomes (C98_2_2_3), 1.1e-02 random. Largest plateau / (N + 2M + 5): 0.138 (C98_2_2_3: 4 of 29).
  On the long runs (CW, MW, MWR) q = T_CYC: every step raises Φ and there is no plateau.

## Item 1 (b): the lift to (plain parity game, Howard run): where LEVEL / PLATEAU fail on Friedmann's G_N and on switchallexp
Lift (lev43.py game mode; MINE, not L-NEW's): Howard at every Even vertex; «movers» := Even vertices with ≥ 2 successors; «gates» := Odd
vertices with ≥ 2 successors; «e-vertices» W := for each gate its successor of largest even priority (L-LIT T66's «esc»: h_i on G_N,
m_i on switchallexp); class := (reward(Λ), Π ∩ W) with box 208's order; bounds' analogues stated in the header (P := (m_CH + n)·n,
plateau ≤ #Even vertices). Games: G_N = [F11] Table 4 as quoted in L-LIT T66 §3, start ι (my transcription, lev43.lmcs; equal to
L-LIT's function lmcs on priorities, owners, edges, names, start: out/xgame43.out); PGSolver switchallexp, best-reward start.
Second engine: at every state L-SI's experiments/si/si.py re-evaluates my strategy (cycle node, Π, length at every vertex; Odd's choice
at every gate) and runs its own Howard: valdiff 0, taudiff 0, seqdiff 0, same T, on G_N N = 1-8 and switchallexp N = 2-7 (xgame43.py).
T equals T66's (9·2^N − 10; 30 / 70 / 150 / 310 / 630 / 1,243).
| G_N | n | T | q (Φ-intervals) | stalls | plateaus | longest plateau | tail | first failing counters (state) | k5 | l4 | plat (> #Even) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14 | 8 | 3 | 2 | 1 | 2 | 3 | none: all 23 are 0 | 0 | 0 | 0 |
| 2 | 24 | 26 | 8 | 13 | 3 | 7 | 5 | k5, l4, p3, p6, p7 (state 5) | 38 | 7 | 0 |
| 3 | 34 | 62 | 15 | 40 | 6 | 16 | 7 | the same (state 5) | 328 | 30 | 0 |
| 4 | 44 | 134 | 24 | 101 | 10 | 34 | 9 | the same; plat first at the plateau [32, 66] | 1,406 | 87 | 1 |
| 5 | 54 | 278 | 35 | 232 | 15 | 70 | 11 | the same | 4,686 | 214 | 3 |
| 6 | 64 | 566 | 48 | 505 | 21 | 142 | 13 | the same | 13,752 | 483 | 6 |
| 7 | 74 | 1,142 | 63 | 1,064 | 28 | 286 | 15 | the same | 37,428 | 1,038 | 6 |
| 8 | 84 | 2,294 | 80 | 2,197 | 36 | 574 | 17 | the same | 96,962 | 2,167 | 10 |
- Fits on N = 1-8 (DATA, not proved): T = 9·2^N − 10; **q = (N + 1)² − 1**; longest plateau = 9·2^(N−2) − 2 (N ≥ 2); tail = 2N + 1;
  T = q + stalls + tail exactly (c2 0).
- **Smallest N and first step.** N = 2, step 5 → 6: (K5) fails at the mover g2 and its successor f2: class_5(f2) = (x, {h1}) but
  class_6(g2) = (x, ∅) (out/diag43.out). In values: Ω_5(f2) has Π = {f2:33, h1:30, f1:29, k1:27, s:22, e2:10, d2:9, e1:6}; g2's current
  successor k2 has Π = {k2:31}; the most relevant vertex of the difference is z = f2, of ODD priority 33, not an escape, above the escape
  h1 (30). So Ω_5(f2) ◁ Ω_5(k2) although class(f2) > class(k2), and g2 rightly stays at k2.
- **Which step of box 208, which genome property.** (K5)'s proof is DOM + «x has priority 0 … ext(x, ·) adds nothing to Π» + (K2)
  COARSE; (K2)'s proof says «by E-DOM z is an e-vertex, c_W, K0 or K3». DOM holds in values at every one of the failures (k5z43.py:
  domfail 0), and at every one z is an odd, non-escape vertex above the least relevant escape: f_j on G_N (38 / 328 / 1,406 / 4,686 /
  13,752 / 37,428 / 96,962 failures for N = 2-8, all «zodd», all f), k_j on switchallexp (38 / 269 / 1,016 / 3,053 / 8,170 / 20,114 for
  N = 2-7). So the failing step is (K2) inside (K5), and the genome property it needs is **E-DOM** (R121: «Every vertex more relevant
  than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]»), the property L-LIT T66 found G_N to lack (f_j, k_j odd above h_i).
- **What survives on G_N (N ≤ 8) under this lift, and where the exponential sits.** (K1), (K3), (K4), (L1) (Φ never falls; stalls and
  non-stalls as stated), (L2), (L3) with its value clause, (C2), (C4), (P1), (P2), (P4) have 0 failures. Φ takes only (N + 1)² − 1
  values. The run is exponential because the PLATEAUS are: (L4) fails (a stall with no cycle of the stall map inside FRONT; first:
  FRONT = {g2, k1} at state 5 of G_2), (P3) fails (a mover of Y has a successor of higher class: g2 and f2 again), then (P6) (steps of
  a plateau at which no mover of Y switches) and (P7) / the plateau bound (from N = 4). READING: on G_N the lowest-lagging-class
  potential itself is polynomial; what Friedmann's counter defeats is exactly Lemma PLATEAU, through (K5). So for genomes the content
  of ALL-TCYC beyond «Howard in general» is PLATEAU's (P3) → (P5) → (P7) chain, and that is where a referee should look.
- switchallexp (out/lev43_switchall.out): the same first failures at N = 2 (k5 at state 6: mover l1, successor k1, z = k1:41 odd above
  the escape m0:38; l4, p3, p6, p7 at state 7); T 30-1,243, q 12 / 23 / 39 / 59 / 83 / 109, longest plateau 7 / 16 / 36 / 76 / 156 /
  316. From N = 4 also (K1) fails (mono 8 / 46 / 158 / 431: first at state 78, vertex k0 loses the odd k1:65 and the escape m0:62 below
  it), with (K4) (2 / 10 / 32 / 84) and (L1) (phifall 2 / 5 / 9 / 14): there E-MON itself breaks, again at an odd vertex above an escape.
- Second lift (WMODE=up: W := every vertex at least as relevant as the least relevant escape, odd ones with negative sign, so that the
  class order is the VJ order on Π ∩ W and (K2) holds by construction; out/lev43_lmcs_up.out): then (K3 d) fails at state 0 of G_2
  (f2 → e2: class (x, −{f2}) below its successor's: an «e-vertex» of negative weight), with (L2), (L3), (L4), (P2), (P6), (P7) at the
  same state, and (K5) from N = 3 (the movers k_i lie above escapes: [DEF]'s «Even movers of priority 0» fails). Either way the
  shortest-path reading «only e-vertices cost, and they cost for Even» needs E-DOM.
- Side finding for L-LIT (through the Lead): in T66's table as quoted, priorities are NOT pairwise distinct: g_n and a_1 both have
  4n + 4 (T66 §3 cites «the uniqueness of priorities in the game»). Both engines break the tie by index and T = 9·2^N − 10 holds; whether
  the paper's table differs is for L-LIT to check.

## Item 2: fixed-family Deep_3 test on the DHIB line (my engine: box41/deep41.py on own34; second engine: L-SI cross100 on L-RED how3_232)
Counter: Deep_3 = Σ_C Deep_3(C) (flips of INTERNAL gates at steps t ≥ t0(C), charged by TWO-CROSS to a change of depth > 3; L-SI box 100
§4), per-gate max = the largest number of such flips at one gate, dmaxInt = the largest charged depth at internal gates after t0.
- Trace of DHIB26_2804 (N 108, M 292, levels 0-3 with 66 / 38 / 3 / 1 movers; sha1 2c49fd10): trace43.py (out/trace43_DHIB26.out) and
  probe43.py (out/probe43_DHIB26.out). T3 28; one SCC of 102 movers; 24 deep internal flips (depth 4-6) at 13 gates, steps 7-26.
  - A REPEATER: gate (10, 0) (W-target 17, Ξ-target 18) flips 15 times, 7 of them deep (t = 7, 8, 12, 16, 18, 19, 20; depths 5, 4, 4, 5,
    6, 6, 4). Λ = K1 throughout. The top e-vertices of its face values form a nest: e(40, 9) is gained once (t ≈ 10-12); e(38, 5) is
    there before and is re-gained under it (t = 15); e(12, 3) is gained three times (t = 5, 12, 16); the sub-sequence e(75, 1) →
    e(10, 1) → e(76, 1) runs at t = 7-9 and again at t = 18-20, one or two e-vertices deeper. READING: gains 1, 2, 3 per nesting
    level: a staircase, not a doubling.
  - A CASCADE: the gates (76, 1), …, (83, 1) (Ξ-target 18) flip once each at t = 20-26, each charged to its own e-vertex, while mover 17
    walks through its options (17, 2), …, (17, 9) (Ξ-targets 76-83).
  - The HUB 18: Ξ-target of the repeater gate and of every cascade gate.
- Growth rule (no search, equal effort per size; fam43.sh = box42/clone42.py): k clones of ONE mover X of DHIB26_2804, with copies of its
  options and of its in-edge options, gate / β ranks just after the originals'. Three families: D18(k) (the hub; + 22 to N + M per
  clone), D10(k) (the repeater mover; + 6), D80(k) (a cascade mover; + 5). k = 0 is DHIB26_2804 byte for byte. inst/SHA1SUMS.fam43.
  | family | k | N + M | Deep_3 (mine) | per-gate max | dmaxInt | T3 |
  | --- | --- | --- | --- | --- | --- | --- |
  | D18(k) | 0, 4, 8, 16, 32 | 400, 488, 576, 752, 1104 | 24, 92, 160, 296, 568 | 7 | 6 | 28 |
  | D10(k) | 0, 16, 32, 64, 128 | 400, 496, 592, 784, 1168 | 24, 168, 312, 600, 1176 | 7 | 6 | 28 |
  | D80(k) | 0, 16, 32, 64, 128 | 400, 480, 560, 720, 1040 | 24, 40, 56, 88, 152 | 7 | 6 | 28 |
- Fit within each family (fit43.py, out/fit43.out): **exactly linear, exponent 1**: Deep_3 = 24 + 17k = 0.7727 (N + M) − 285.1 (D18);
  24 + 9k = 1.5 (N + M) − 576 (D10); 24 + k = 0.2 (N + M) − 56 (D80); maximum residual < 1e-12 on 5 sizes each. (The log-log slopes
  near 2 that fit43 prints are the affine offset, not curvature.) D10's slope is above 1: Deep_3 exceeds N + M at k = 128 (1,176 at
  1,168). **dmaxInt (6) and the per-gate maximum (7) do not grow with size**; T3 stays 28: every clone is one more gate on the same
  deep changes, at the same steps, as in BOX 42's CL(k). Nothing faster than polynomial; no alert sent.
- Second engine (out/meas43_cross.out): T3, whole-run deep and dmax equal mine on all 13 points (5 of 5 in each family) (on every point my whole-run deep equals my
  Deep_3, so cross100's equal whole-run deep confirms the Deep_3 column; the per-gate maximum is mine only).
- Single clones of the other movers of the nest (my engine only, not frozen): mover 40 (owner of the top e-vertex e(40, 9)): no change
  at k = 1, 2 (Deep_3 24, T3 28); mover 38: T3 24, Deep_3 18, per-gate max 3 (the nest is disturbed); movers 12, 13, 17: Deep_3 26, 24,
  31. No clone adds a round to the repeater: the per-gate maximum stays ≤ 7.

## Item 3: a family whose ONE gate's deep flips grow: the TAIL transformation (tail43.py)
- TAIL_h(G): every option of G whose Ξ-target is the sink X is retargeted to a new mover A_top; the tail A_top, …, A_1, A_0 has one
  mover per level Lmax + h, …, 1, 0 (Lmax = G's largest level), each with ONE option: A_j (j ≥ 1) has W-target A_(j−1) and Ξ-target
  A_j itself with an even β, so its β-face closes an Even-won cycle and Odd must take the escape e(A_j); A_0 has W-target c_W and
  Ξ-target X. Tail gate and β ranks are the lowest. Cost: N + M grows by 2(Lmax + h + 1). Every play that ended at the sink now ends
  through the tail, and its Π gains the same Lmax + h e-vertices, h of them above every e-vertex of G ([E-LEV]).
- DATA, the run is the same run (tailcheck43.py, my engine; out/tailcheck43.out; h = 2; unit (mover of G, state) / (gate of G, state)):
  on MWR4_2, MWR8_2, MWR16_2, C6G8_n54, BEST_C300_r34 (box 36's per-gate record), DHIB26_2804, RWX_n95: T3 equal, seqdiff 0 (every
  σ_t equal on G's movers), taudiff 0 (every Odd choice equal at G's gates), the same internal flips after t0. The charged depth of
  every Λ-quiet flip whose face has Λ = K1 rises by 2 (MWR, C6G8), 3-4 (DHIB26, RWX), 7 (BEST_C300_r34): by h + (Lmax − level of z).
- DATA, Deep_3 after TAIL_2 = all Λ-quiet internal flips before it. QF_K1(G) := the internal-gate flips at t ≥ t0 charged to a change
  with Λ unchanged and = K1. On the seven genomes Deep_3(TAIL_2(G)) = QF_K1(G) exactly:
  | G | N + M → after TAIL_2 | Deep_3(G) | QF_K1(G) = Deep_3(TAIL_2(G)) | per-gate max after TAIL_2 (gate) |
  | --- | --- | --- | --- | --- |
  | MWR4_2 / MWR8_2 / MWR16_2 | 145 → 153 / 261 → 269 / 493 → 501 | 0 / 0 / 0 | 9 / 17 / 33 | 9 / 17 / 33 (the re-arm gate) |
  | C6G8_n54 | 204 → 212 | 3 | 51 | 11 (10, 0) |
  | BEST_C300_r34 | 289 → 307 | 14 | 55 | **34** (82, 0) |
  | DHIB26_2804 | 400 → 412 | 24 | 129 | 15 (10, 0) |
  | RWX_n95 | 328 → 340 | 0 | 56 | 3 (21, 0) |
- **The one-gate family TMWR(n) := TAIL_2(MWR(n))** (fam43b.sh; MWR(n) = L-RED's generator, box37/genmw229_copy.py WTGT=R n 2; n = 4
  reproduces MWR4_2 sha1 856d369b; inst/SHA1SUMS.tail43). Second engine (cross100; out/meas43_tail_cross.out), n = 4, 8, 16, 32, 48
  (N + M 153, 269, 501, 965, 1429 = 29n + 37): T3 30, 54, 102, 198, 294 = 6n + 6, equal to MWR(n)'s; flips of the busiest gate 9, 17,
  33, 65, 97 = **2n + 1**; whole-run deep (every gate) 13, 25, 49, 97, 145 = 3n + 1 = the number of Λ-quiet flips (0 on MWR(n)); dmax
  5 at every n. My engine (out/meas43_tail_mine.out): Deep_3 = per-gate max = 9, 17, 33, 65 for n = 4, 8, 16, 32, dmaxInt 5, T3 and whole-run deep equal
  to cross100's (n = 48 on my engine: see the note at the end of this section).
  So ONE gate's deep flips grow linearly: 2n + 1 = (2/29)(N + M − 37) + 1, dmax constant. TREC = TAIL_2(BEST_C300_r34): one gate with
  34 deep flips at N + M 307 (cross100: T3 48, deep 61 = qflip 61, maxfl 34, dmax 12).
- READING (for L-SI 51 / L-RED 66 through the Lead; an argument sketch, not a refereed lemma). Why the run is unchanged: the tail's
  value is constant; every sink-ending value gains the same set and the same extra length, values with another Λ are untouched, so every
  comparison of two values comes out as before, hence Odd's choices and Howard's steps at G's vertices too. Consequences:
  1. Per-gate deep flips ≥ per-gate Λ-quiet flips of any genome, at a cost of 2(Lmax + 3) in size. The known per-gate flip counts are
     linear (MWR 2n + 1; BOX 36's record 34 at 289; BOX 37's gen37), so the one-gate count is at least linear, and nothing super-linear
     is known for it.
  2. The depth cut-off c does no work on a class closed under TAIL: for every fixed c, Deep_c(TAIL_(c−1)(G)) ≥ QF_K1(G). So CONJECTURE
     DEEP3 (some fixed c) is as strong as «the Λ-quiet internal flips after t0 with a sink-ending face are polynomially many», and
     DEEP3-all as strong as the same for every gate over the whole run. DEPTH-COUNT3 bounds the changes of depth ≤ c, but an adversary
     can push every flip below any fixed depth. What remains open is then the flip count itself (R118's «no bound on R is claimed»),
     not a weaker «deep» part of it.
  3. Depth measured from the top is therefore not intrinsic; a count that TAIL cannot inflate would have to measure depth relative to
     the changing part (for example among the e-vertices that are not common to both faces of the gate).

- Note on n = 48: TMWR48 was still running on my engine (own34, > 25 min) when this record was committed; its line is appended to
  out/meas43_tail_mine.out if it finished before the park (see the notebook). MWR48_2 was not run on my engine (cross100: T3 294, deep 0).

## Files (items 2-3)
trace43.py, probe43.py (trace), fam43.sh, meas43.sh, fit43.py (families, two engines), tail43.py, tailcheck43.py, fam43b.sh (TAIL);
inst/ (families and tail genomes, SHA1SUMS.fam43, SHA1SUMS.tail43); out/meas43_*.out, out/fit43.out, out/tailcheck43.out. Second
engine env: LSI100 (archive of claude/l-si 23d39400), RED (archive of claude/l-red 59daaef2 experiments/), LNEW (archive of claude/l-new
fcba92fc).

## Files (item 1)
hist43.py, plathist43.py, run43a.sh (L-NEW's counters on my history); lev43.py (my counters; genome and game modes; controls LV43_CTRL,
lift WMODE), run43b.sh, rand43.py, run43c.sh, sum43.py; xgame43.py, diag43.py, k5z43.py (game runs); inst/SHA1SUMS.lnew_8db300fe (every
L-NEW input and frozen output used), inst/SHA1SUMS.llit_a19fff23; out/. Needs env LNEW208 = an archive of claude/l-new 8db300fe
(experiments/new, experiments/si/si.py, experiments/harness), LLIT = an archive of claude/l-lit a19fff23 (docs/lit, experiments) for the
table comparison. All runs resumable per genome / per line.
