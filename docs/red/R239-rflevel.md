# R239: adversary against L-NEW 74's box 212 RF-LEVEL (RF-A, RF-B, RF-C, RF-D's [IMP3]) — VERDICT: every statement SURVIVES; no candidate
L-RED successor 68 (Opus 5.5, D21 / L53). Lead brief 2026-11-13 00:20Z: «NEXT, R239: attack L-NEW 74's BOX 212 RF-LEVEL (claude/l-new
5fa64fe6, docs/new/N5-RFLEVEL-box212.md …) … RF-A … RF-B … RF-C … RF-D's hypothesis [IMP3] … on YOUR n5s237 (SPEC-exact), state by
state. Method: your own engine and rules, including adversarial «improving» rules (the worst-key choice, random subsets, one-switch,
a rule that picks the least improving gate); climb for a rule and genome where a class falls, more than P non-stall steps occur, or Y
is not closed; firing controls; every candidate on a second engine before reporting it.»
Object: claude/l-new 5fa64fe6 docs/new/N5-RFLEVEL-box212.md (§0-§9; Addendum A was not on that commit when I read it); definitions from
P-N5-LEVEL (l-new 1e6df499, §2, §4, §5, §7). Labels: DATA (unit, set, scope, counter) / READING / SURVIVES.
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»
**Scope: RF-A..RF-C are statements about IDEAL-CYC(G) on R104 genomes; RF-D is a conditional reduction for N5 on Γ3(G) before its first
fallback. Nothing here bounds N5; G-N5-TIME stays OPEN. My data are not referee signatures.**

## 0. Verdict
| statement | verdict | evidence (all counters 0 on every non-control set; controls fire) |
| --- | --- | --- |
| §2 reading («at every state» = every state of IDEAL-CYC, any rule) | SURVIVES (DATA) | static239: CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, [OPT] at every state visited by 10 rules (§2.3) |
| RF-A (i) (K1)-(K4), (ii) (L1)-(L3), (L5), (iii) ≤ P non-stall steps, (iv) K5-NEW | SURVIVES | rf239 must-0 k1, k2, k3, k4, l1, l2, l3, l5, nsp, k5new, plus f1, imp, cn2 (§2.1, §2.2, §2.4) |
| RF-B (P1), (P2) (no vertex of Y leaves Y), (P4), (P5′) | SURVIVES | p1, p2, p4, p5 on every plateau of every reference state |
| RF-C (tail clause; T ≤ P + (P + 1)·W) | SURVIVES | tail = 0; the inequality follows from nsp = 0 at b = T and the decomposition (§1) |
| RF-D's hypothesis [IMP3] | SURVIVES on n5s237 | imp239: nonstd, nomove, offmover, notimp, tauch 0; towers T = 30 / 67 / 136 / 209 / 299 = box 212's; n5v agrees state by state (§3) |
| Box 212's «not claimed for a general rule» list ((K5) for every gate, (P3), (P6), (P7), QUIET-N on the tail) | CONFIRMED as rule-dependent | k5how, p3, p6idle, p7, tailN are 0 under howard and > 0 under the other rules (§2.1) |
No candidate arose on any non-control run, so no instance needed the second engine; the climbs (§2.4) found none either.

## 1. Reading of the proofs (READING; attacker's notes)
- RF-A's F1 step: each I_t is one switch per mover, each to a strictly better successor; VJ00 §4.4 / R15 (a) Lemma A is stated for ANY
  non-empty unambiguous improving set, so F1 holds for every rule in rf239 (DATA: f1 = 0). (K1) then follows outside the core from F1 and
  (K2) applied to the values of ONE vertex at two states: this is exactly the «(K2) at two different states» weak point named in box 212
  §8. (K2)'s proof uses only E-DOM, the play shape (K0 → K3 → K2 → K1 with LOC-K2) and (VJ-1/2), each a property of one positional pair,
  so it does not care which rule produced the two states. DATA: k2 tested on ALL pairs ((vertex, state), (vertex, state)) of a run when
  (T + 1)·#outside ≤ 700, else on 1,500 sampled pairs per run.
- (iii) counts the non-stall steps as distinct values of Φ: Φ never falls while LAG ≠ ∅ ((L1), from (K1) only) and rises at every
  non-stall step that leaves LAG non-empty; (L5) bounds the values. No step uses the rule. The bound P is very loose on the data: at most
  13 non-stall steps per reference state on random genomes, 35 on R235's frozen ones, against P in the thousands.
- RF-B: (P1), (P2), (P4) are P-N5-LEVEL §7's proofs, which use (K1), (K3), (K4), (D1), LOC-K2 and the freeze. (P5′) is new: its step
  clause needs that a moved mover x ∈ Y lands in Y. That is (P2) at s + 1, legitimate because s + 1 ≤ v. My counter p2 checks
  s_s(x) ∈ Y for every vertex of Y at every state of the plateau, so «no mover of Y leaves Y before the end» is tested directly.
- RF-C: with q ≤ P intervals of constant Φ, at most q plateaus, each ≤ W, and the tail ≤ W: T = q + Σ (v_i − u_i) + (T − b′) ≤ P + P·W
  + W. The arithmetic is right. The tail clause's case (3) (equal face classes ⇒ σ̄ = e_g) rests on B-ONLY and (K3 (d)); NO-TIE excludes
  an exact tie of the face values, so Odd's optimal reply at a gate is unique and the face cannot flip inside the tail. DATA: tail = 0.
- RF-D's READING «Ξσ's order on Γ3 is Ω_t's»: imp239 measures improvement by Ξσ = SPEC S1's valuation (n5s237.vjproc), which under the
  standing premise 1E-N3 is the VJ value against Odd's pointwise-optimal reply, i.e. Ω_t. So [IMP3] is tested in SPEC's own order.
- Nothing in RF-A..RF-C looked wrong on this reading; I found no sentence to aim an instance at beyond box 212 §8's named weak points,
  which the counters cover.

## 2. DATA: RF-A / RF-B / RF-C on L-RED's own IDEAL-CYC engine (experiments/red/r239/rf239.py)
Engine: experiments/red/r221q/own.py (L-RED 54: Γ(G) from R104's description, own VJ values, Odd's optimal reply by own one-player SI;
no code from rf212, rv208, level208 or si.py). Rules: howard; allleast, allworst (the strictly better gate of the LARGEST gate number:
the worst key), allrand (every improvable mover); subrand (a random non-empty subset); onebest, onerand, oneleast (one random improvable
mover); onefirst (the lowest-numbered improvable mover to its least better gate); oneworst (one random mover, worst key). Reference
states: every b when T + 1 ≤ 12, else b = T and 11 random b. Must-0 and descriptive counters: rf239.py's docstring.
### 2.1 Random genomes (out/rf239.out; own generator rf239.rand_genome: levels, W-targets one level down, Ξ-targets any mover or X (15 %),
gates and β-ranks permutations, random parities and start)
| seed | genomes | N ≤ | depth ≤ | degree ≤ | rules | every must-0 counter | Howard-only facts (k5how / p3 / p6idle / p7 / tailN) | max T | max plateau |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2391 | 300 | 6 | 3 | 3 | all 10 | 0 | 0 under howard; > 0 under every other rule (e.g. oneworst 150 / 308 / 112 / 14 / 0) | 13 | 4 |
| 2392 | 150 | 10 | 4 | 3 | all 10 | 0 | 0 under howard; onefirst 260 / 612 / 333 / 59 / 0 | 17 | 8 |
| 2393 | 60 | 16 | 5 | 3 | all 10 | 0 | 0 under howard; onefirst 277 / 702 / 385 / 50 / 0 | 23 | 9 |
| 2394 | 40 | 24 | 8 | 2 | all 10 | 0 | 0 under howard (and the all-mover rules); onebest 235 / 462 / 264 / 13 / 0 | 22 | 6 |
- 40 rows (4 sets × 10 rules), every must-0 counter 0. tailN fired once (oneleast, seed 2391): a tail longer than N, as box 212 §5
  says can happen without Howard.
### 2.2 Frozen genomes
- R235's three climbed genomes (experiments/red/r235/inst/plc_*.json) under all 10 rules: 0 (out/rf239.out, 10 rows); max T 121
  (onebest), longest plateau 37 (onebest), at most 35 non-stall steps for one reference state (oneleast).
- Box 212's 81 frozen genomes (git archive 5fa64fe6, the list ALL of its run212.sh), one process per (genome, rule) (frz239.sh):
  - N ≤ 100 (57 genomes) × 10 rules: 570 pairs, 0 timeouts, every must-0 counter 0 (out/rf239_frz_small.out).
  - N > 100 (24 genomes, N up to 416) × howard, oneworst, oneleast, subrand: 96 pairs, 0 timeouts, all 0 (out/rf239_frz_big.out).
  - N > 100 × the other six rules (allleast, allworst, allrand, onebest, onerand, onefirst): 144 pairs, 0 timeouts, all 0
    (out/rf239_frz_big2.out). So all 81 × 10 = 810 (genome, rule) pairs are checked, with 0 timeouts (box 212 §7 had 9 timeouts and 1
    out-of-memory pair under its single-switch rules, unchecked there).
### 2.3 §2's reading: the five static lemmas of R123 at every visited state (static239.py; out/static239.out)
- CN2, B-ONLY, NO-TIE, LOC-GATE (the chosen face strictly lower), LOC-K2 and [OPT] (no Odd improving switch) at every state of every
  rule's run: 30 rows (seeds 2395 / 2396 / 2397: 300 genomes N ≤ 6, 100 N ≤ 12, 40 N ≤ 20; 10 rules each), every counter 0.
- Control CTRL=1 (B-ONLY's comparison reversed): bonly 3,541 (howard) and 4,645 (oneworst) on 50 genomes.
### 2.4 Climbs (climb239.py; mutations experiments/red/r230/mut230; N ≤ 24, degree ≤ 3; the rule's random choices seeded per evaluation)
Score plat = (must-0 sum, longest plateau, stalls, T); T = (must-0 sum, T, longest plateau). Out: out/climb239.log; checkpoints and
best genomes out/climb/ (ck_c*.json, best_c*.json with rule and rule seed).
| climb | rule | score | evals | best score | max T | longest plateau | max non-stall (one b) | max |V| | must-0 sum | candidates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c1 | oneworst | plat | 9,671 | [0, 8, 18, 11] | 13 | 8 | 9 | 117 | 0 | 0 |
| c2 | onerand | plat | 12,456 | [0, 20, 59, 23] | 29 | 20 | 13 | 130 | 0 | 0 |
| c3 | oneleast | T | 9,822 | [0, 25, 7] | 25 | 9 | 15 | 100 | 0 | 0 |
| c4 | subrand | plat | 12,129 | [0, 4, 4, 6] | 7 | 4 | 7 | 90 | 0 | 0 |
| c5 | allworst | T | 4,518 | [0, 21, 4] | 21 | 4 | 15 | 168 | 0 | 0 |
| c6 | howard | plat | 5,738 | [0, 4, 30, 14] | 15 | 4 | 14 | 156 | 0 | 0 |
| c7 | onefirst | plat | 2,150 | [0, 75, 645, 87] | 87 | 75 | 23 | 165 | 0 | 0 |
| c8 | allleast | T | 5,845 | [0, 20, 2] | 20 | 3 | 17 | 162 | 0 | 0 |
| total | 8 rules | | 62,329 | | 87 | 75 | 23 | 168 | 0 | 0 |
- Sum of T over all climbed runs: 613,638 steps. The longest plateau, 75 steps under onefirst (one mover per step, the lowest-numbered
  improvable one, to its least better gate), is a closed class-frozen window on which (P1), (P2), (P4), (P5′) hold at every state; the
  Howard-only facts fail there massively (p6idle 500,004, p7 20,526 over the climb), as box 212 §4 says they may.
- No climb got near P: the most non-stall steps for one reference state is 23 (c7), against P = 2M(N + 2M) ≥ several hundred there.
## 3. DATA: RF-D's [IMP3] on n5s237 (experiments/red/r239/imp239.py; out/imp239.out)
N5 = n5s237 mode spec (SPEC-exact; R237) from S3 on Γ3(G) = box 189's gamma3.build with box 195's PADS (objects only), up to the first
fallback. Counters (must 0): nonstd (a state off the standard form: σ off the movers or τ differs from S3's), nomove, offmover, notimp
(a mover to a pad not strictly Ξσ-better), tauch. Second engine: box 190's n5v spec from S3, σ state by state up to F1.
| set | genomes | every counter | non-fallback steps checked | max F1 | second engine sampled / xdiff |
| --- | --- | --- | --- | --- | --- |
| towers DBL4, RECF4, H5, H6, HIT7 (box 212 inst, sha1 = its SHA1SUMS) | 5 | 0 | 741 | 300 | 5 / 0 |
| random 2391 (N ≤ 6) | 1,000 | 0 | 652 | 4 | 50 / 0 |
| random 2392 (N ≤ 10) | 500 | 0 | 437 | 5 | 25 / 0 |
| random 2393 (N ≤ 16) | 300 | 0 | 300 | 4 | 15 / 0 |
| random 2394 (N ≤ 24, depth ≤ 8) | 200 | 0 | 202 | 5 | 10 / 0 |
| climb i1 (impclimb239, from random, N ≤ 24; score (counters, F1)) | 14,108 | 0 | 136,417 | 19 | 564 / 0 |
| climb i2 (from tower DBL4, N ≤ 40) | 916 | 0 | 17,792 | 35 | 36 / 0 |
- Climbs: out/impclimb239.log, out/climb/ick_i*.json, ibest_i*.json. In total [IMP3] is checked on 17,029 genomes and 156,541
  non-fallback transitions (741 of them on the towers), every counter 0; n5v agrees state by state on 705 sampled genomes.
- The towers' run lengths from my engine: T = F1 − 1 = 30 (DBL4), 67 (RECF4), 136 (H5), 209 (H6), 299 (HIT7), equal to box 212 §6's
  T = 30, 67, 136, 209, 299 (from n5v / n5b), each with exactly one fallback and F1 + 2 iterations.
- Control CTRL=1 (notimp's comparison inverted): notimp 180 on 200 genomes (fires).

## 4. Controls (each must fire)
| control | change | fires |
| --- | --- | --- |
| rf239 CTRL=1 | the e-set order reversed in the class order | k1 115-201, k2 35,060-70,958, k4, l1, l2, l3, l5, p2, p5 (howard, onerand, oneworst; 60 genomes) |
| rf239 CTRL=2 | one step to a strictly WORSE gate | imp 16-25, f1 208-278, k1, k5new, l1, l3, tail |
| rf239 CTRL=3 | Φ's second coordinate +|FRONT| | l1 10 / 51 / 82 |
| static239 CTRL=1 | B-ONLY reversed | bonly 3,541 / 4,645 |
| imp239 CTRL=1 | notimp inverted | notimp 180 |
| climb239 CTRL=1 (onerand, 150 s) | as rf239 CTRL=1, in climb mode | 1,837 of 1,993 evaluations are candidates (k1 11,282, k2, k4, l1, l2, l3, l5, p2, p5) |
- No control for nsp (P is far above every count), p4, tail beyond CTRL=2, cn2, notie, locgate, lock2, opt, nonstd, offmover, tauch.

## 5. What this does and does not touch
- RF-A, RF-B, RF-C and [IMP3] survive an independent engine, ten improving rules (four of them adversarial: worst key, least improving
  gate, lowest-numbered mover, random subsets), 81 frozen genomes, the five towers and the climbs. Box 212's list of Howard-only facts
  is right: they do fail under other rules.
- This is DATA plus a reading, not a proof or a signature. RF-D stays a CONDITIONAL reduction: it moves O1′ to a bound on the key rule
  inside class-frozen windows, which no one has; on the towers the whole run is one window (box 212 §6), so the reduction gives nothing
  there. G-N5-TIME stays OPEN.
