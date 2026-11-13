# L-COMP BOX 46 (successor 21; Lead «go» 01:38Z 2026-11-13 with corrections; rulings 02:38Z, 03:30Z): W_key, independent measurement. All DATA.
Nothing here is a TARGET.md claim, an M3 / M4 statement, a bound or a gauntlet step. Box 212's RF-A..RF-D (claude/l-new 5fa64fe6,
docs/new/N5-RFLEVEL-box212.md) stay CANDIDATES / CONDITIONAL; O1, O1′ and G-N5-TIME stay OPEN. Every result is DATA ON THE NAMED SETS
ONLY. Every number below is generated: the three tables are sum46.py's output (out/sum46_1.out, _2.out, _3.out), inserted by mk46.py;
their sha1s and sum46.py's are in out/SHA1SUMS.
**Engine.** Γ3(G) by box34/own34.build; N5 = SPEC's key rule (mode «spec») by box44/n5xi44.run on my n5b SpecSI, from S3, states
0..T_key before the first fallback. win46.py (a copy of box44/lev44.py, my text implementation of box 209's classes / LAG / FRONT / Φ /
stalls, with the window part written from box 212 §4 (RF-B), §5 (tail clause), §6 (RF-D)); rfd212.py was opened only after win46's
first runs. Windows: plateau = maximal [u, v], u < v, of constant Φ with LAG ≠ ∅ and v < b = T_key (Y := {x : class_u(x) ≤ m}); tail
= [b′, T_key] (Y := every vertex) if T_key − b′ > 0. W_key = the longest window (steps).
**Definitions added by the Lead's rulings.** Ξ-cyclic: R104's Ξ-graph («the Ξ-graph has an edge x → xt(x, k) for every option with a
mover as Ξ-target», docs/RESULTS.md l. 9864; «Ξ-graph is ACYCLIC (self-loops count as cycles).», l. 9910; R122 (a) Ξ-ACYCLIC «the
Ξ-graph has no directed cycle», l. 14853; line numbers at trunk f5a237ce) has a cycle. Use of a cycle: offbeta [(gate, state)] σ̄ on
the e-face; cycopt [(mover, state)] σ_t(x) an option whose Ξ-edge lies on a Ξ-cycle; run_used = 1 iff either is > 0 at some state ≤
T_key; a window is USED iff either is > 0 at one of its states; Wused = the longest used window (item 3's objective, 02:38Z). wess (03:30Z)
[step inside a window] = a mover enters or leaves a cycle option, or σ̄ moves onto or off an e-face; W_ess = the longest window with
wess ≥ 2 (win46e.py; win46.py kept unchanged so that item 2's rows are one version).
**Must-0 counters** (unit; scope = every window / every state ≤ T_key): imp3, imp3e ([IMP3]); wcls, wclos, wodd, wout, wimp, hyval (H_Y with
movers on σ_s and every non-mover on s_u, correction (c)); offbacyc [genome: offbeta > 0 on a Ξ-acyclic genome; R122 BETA-ACYC,
docs/RESULTS.md l. 14744 at f5a237ce: «for every genome G whose Ξ-graph is acyclic, on Γ(G) or Γ3(G), and every Even strategy that agrees
with the stated start off the movers (transported through the pads on Γ3), every optimal counterstrategy of Odd takes the β-face at every
gate»]; and box 209's rule-free counters as in lev44. Howard-only facts (nohoward, dom, k5, l4, p3, p6, p7, plat, tail, t1, fbwrong,
n5xig3, t3all) are descriptive. Descriptive: plat_at_b (RF-B's v < b, correction (a); 0 by construction, counted), wout_wclos (overlap).
Controls (out/win46_ctrl.out, win46_usectrl.out): W1 (Y := FRONT_u), W2 (windows ± 1 step), W3 (improvement reversed), W4 (H_Y with the
other Odd successor), W5 (offbeta comparison reversed), lev44's 1 / 5 / 6, and the two genome controls of the use columns (an odd
self-loop tower: Wused 0; a collapsing even variant: run_used 1); each fires (tables below and win46_ctrl.out).

**Correction (recorded, not erased).** My 02:36Z message to the Lead typed «159 of 224», «91 of 91» and «20 of 68» from a partial
tally; the file then had 143 rows, 71 of 71 odd variants unchanged, 20 of 72 even variants keeping the run (corrected 02:38Z). The
complete counts are in the table of item 2. Since 02:39Z every number in a message is pasted from a generated file with its sha1.

## Item 1: win46 (mine) against rfd212 (L-NEW) — no disagreement
@@T1@@
Tuple compared: (T_key, #windows, W_key, stalls, tail, #plateaus, longest plateau, Φ values); rfd212's windows formed as plat + (tail > 0),
W = max(platmax, tail). rfd212.py (sha1 b1eab4b7) run unchanged with python3 -I, RFD_MODE=spec, on the same 86 files (run46b.sh); its
committed rows and the tower genomes are pinned in inst/SHA1SUMS.lnew_5fa64fe6.

## Item 2: Ξ-cyclic sets
@@T2@@
- READING (DATA, these sets only): Ξ-cyclic by R104 does not imply that the key-rule run uses the cycle. An added Ξ self-loop option with
  an ODD β is inert on every tower (the run is the tower's); with an EVEN β it is often taken and the run usually collapses (e.g.
  DBL4_x0_glo_blo_p0: T_key 7 against the tower's 30). Away from the towers, every Ξ-cyclic set has short windows.
- PARTIAL: the final pass with the use columns (run46f.sh named) was stopped at a checkpoint at 05:03Z (the Lead's park order): xmine 19
  of 76, xbest / xbig / xtower not yet re-run; their rows above are the first pass (no use columns). Resume: run46f.sh named.

## Item 3: climbs on Wused / (N + M) over Ξ-cyclic genomes; the W_ess climb
@@T3@@
- Bands changed from the statement's ≈ 70 / 140 / 280 (Lead 03:30Z accepted): long-window Ξ-cycle-using seeds exist only near the
  tower sizes, there is no tower generator, and no such seed near 280. Seeds in inst/seeds46/ (SHA1SUMS), chosen from out/seedcand46.out.
- READING (DATA, these genomes only; numbers in the wess table above, out/wess46.out sha1 aef7edac2d57): on every SEED the used window
  is a tower whose added even self-loop option is taken early and kept: wess_wused 0, W_ess 0 (one random seed: 2). The B3 climb's best
  BEST_B3_WU151_NM163_e934d333.json (sha1 e934d333, N + M 163) is different: its run (T_key 151, ONE window = the whole run, the tail;
  equal on n5b and rfd212, climb46_B3.log) has wess 80 inside that window, so W_ess = 151 at N + M 163 (ratio 0.926): movers enter and
  leave cycle options at 80 of its 151 steps (6 options on Ξ-cycles; cycopt 410 (mover, state) pairs, offbeta 0; cycopt and offbeta
  re-measured by the independent use46.py, out/use46_bests.out sha1 598911aa). The E3 climb (objective W_ess, from the two seeds, both
  W_ess 0) reached only 4: a W_ess climb from W_ess-0 seeds has no gradient. So a Ξ-cyclic genome whose key-rule run keeps ONE
  class-frozen window of 151 steps while its movers keep switching on and off Ξ-cycle options exists; it is the strongest W_ess instance
  here. This is one genome; nothing about growth is claimed.
- Fit: NOT identified (bands B0, B1 not run, B2 / B3 / E3 as listed; three sizes of one construction are not a growth law).

## Files
win46.py (windows, must-0, use columns), win46e.py (+ wess), use46.py (independent use counters), rand46.py, mkx46.py (tower variants),
climb46.py / climb46e.py, sec46.py (n5b spec + rfd212 on every best), cmp46.py, sum46.py, mk46.py; run46a.sh (item 1 mine), run46b.sh
(rfd212), run46c.sh / run46d.sh / run46e.sh / run46f.sh (item 2), run46g.sh (item 3 bands). inst/: seeds46/, xtower/, SHA1SUMS.lnew_5fa64fe6.
Slips: three typed-number slips in messages (23:55Z and 00:46Z of BOX 45, 02:36Z here); message stamps «01:4xZ» / «00:5xZ» not from date -u;
run46f's first Ξ-acyclic draws at P(X) = 0.0 looped for 2 h until the task limit (fixed: 0.3 / 0.6).
