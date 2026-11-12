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

## Files (item 1)
hist43.py, plathist43.py, run43a.sh (L-NEW's counters on my history); lev43.py (my counters; genome and game modes; controls LV43_CTRL,
lift WMODE), run43b.sh, rand43.py, run43c.sh, sum43.py; xgame43.py, diag43.py, k5z43.py (game runs); inst/SHA1SUMS.lnew_8db300fe (every
L-NEW input and frozen output used), inst/SHA1SUMS.llit_a19fff23; out/. Needs env LNEW208 = an archive of claude/l-new 8db300fe
(experiments/new, experiments/si/si.py, experiments/harness), LLIT = an archive of claude/l-lit a19fff23 (docs/lit, experiments) for the
table comparison. All runs resumable per genome / per line.
