# R212 FLIP-ADD under attack: co-designed lower bounds for T_1, T_2 at m 4-7; Lemma FROZEN-EMBED (L-RED successor 51)
Started 2026-11-06 07:4xZ (date -u). Lead BOX R212 (brief to successor 51). Model: the external-flip model of RESULTS R110 (T_k(m) over
the ISO genomes of 𝓛^R_(m+1), level 0 frozen, a c-step sequence with ≤ k changes of c); T^R(m) over 𝓛^R_m (RESULTS R110).
Labels: PROVED (lane, unrefereed), MACHINE (exhaustive check by a stated tool, no Lean), DATA (replayed witnesses; lower bounds
only), READING. Not a TARGET.md claim. FLIP-ADD and G-N5-TIME stay OPEN. No SAT is used in this file.

## 0. Answers
- **No kill of FLIP-ADD, and none is possible from data at fixed m.** Lemma FROZEN-EMBED (§1, PROVED lane) gives
  T_k(m) ≤ (k + 1)·T^R(m), so the excess E_k(m) = T_k(m) − T^R(m) is at most k·T^R(m). FLIP-ADD can fail only if T^R itself is
  superlinear. The adversarial measures are the ratio T_2 / T^R and the growth of T^R; both are reported below.
- **Best values, every number a certified witness (§2):**

  | m | T^R(m) ≥ | T^R_ISO(m) ≥ | T_0(m) ≥ | T_1(m) ≥ | T_2(m) ≥ | T_2 − T^R-best | T_2 − T^R_ISO-best | T_2 / T^R-best |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 2 | 4 (exact) | — | 4 (exact) | 5 (exact) | 7 (exact) | 3 | — | 1.75 |
  | 3 | 8 (exact) | — | 8 (exact) | 10 (exact-SAT) | 12 (exact-SAT) | 4 | — | 1.50 |
  | 4 | 13 (exact) | 12 (L-NEW) | **13 (exact)** | **15** | **17** | 4 | 5 | 1.31 |
  | 5 | **16** | **15** | **16** | **17** | **22** | 6 | 7 | 1.38 |
  | 6 | **22** | **18** | **22** | **26** | **34** | 12 | 16 | 1.55 |
  | 7 | **26** | **22** | **26** | **27** | **37** | 11 | 15 | 1.42 |

  - Bold = new in R212. m 2-3 rows: L-COMP box 27, L-SI boxes 70-71 (exact-SAT: one solver, proof unchecked).
  - Previous bests: T^R(5) ≥ 15 (R202), T^R(6) ≥ 18, T^R(7) ≥ 20 (R207); T_1(4) ≥ 14, T_2(4) ≥ 15 (L-SI box 68).
  - T_0(4) = 13 EXACT: ≥ by LIFT of max_d4_L13, ≤ by FROZEN-EMBED (C1) and T^R(4) = 13 (R197).
  - T^R_ISO(d) ≥ T_0(d − 1) for free (an E-genome is an ISO ladder of 𝓛^R_d whose level 0 does not move from the witness start).
  - T^R(5) ≥ 16 settles the question of the MAIN cube run (d 5 T ≥ 16, conditional on SEG-CAP) as SAT: the witness has segments 6 / 0
    / 8 ≤ 13, and r212/modelck.py shows its run is a model of the xcnf encoding (SEGMAX 13 SAT; controls SEGMAX 7 UNSAT, 8 SAT). The
    cube-only solve of its canonical cube 0:7;1:8;2:7;3:2;4:1;5:5 was UNKNOWN at 50 min. MAIN re-aimed at T ≥ 17 (Lead ruling).
- **READING (DATA).**
  - The T_2 excess against T^R-best is 3, 4, 4, 6, 12, 11 for m 2-7; the ratio T_2 / T^R-best stays in [1.31, 1.75]. Against
    T^R_ISO-best (the bound FLIP-ADD actually feeds through W-ONLY) the excess is 5, 7, 16, 15 for m 4-7.
  - Both columns are lower bounds. T^R(6) rose 18 → 22 and T^R(7) 20 → 26 under the same climbing effort that raised T_2; at m 6 a
    second round (400k ladder iterations, 300k E-iterations) moved neither T^R(6) nor T_2(6). So the m 6 / m 7 numbers are stable
    under this search, not exact.
  - The excess grows faster than the constant of the m ≤ 4 data, roughly tracking T^R (ratio ~1.4-1.55). That is what (C2) allows and
    what FLIP-ADD forbids only if T^R is superlinear. No superlinear T^R is visible: T^R-best 4, 8, 13, 16, 22, 26 (increments 4, 5, 3,
    6, 4). So the data neither kill nor support FLIP-ADD beyond «excess ≤ 0.55 T^R».
  - T_1 − T^R-best: 1, 2, 2, 1, 4, 1 (m 2-7): one flip adds little; two flips buy nearly a third run (best T_2 witnesses are three
    long segments: 6+5+6, 8+5+9, 13+13+8, 14+13+10, each segment ≤ the genome's own T_0).

## 1. Lemma FROZEN-EMBED (PROVED, lane; unrefereed)
Statement. Let G be an ISO genome of 𝓛^R_(m+1) (m ≥ 1) and c ∈ {0, 1}. Let Lad_c(G) be the genome obtained as follows:
- drop movers 0 and 1; rename mover x ≥ 2 as x − 2, so level l becomes level l − 1;
- every option keeps its Ξ-target (renamed; ISO: never 0 or 1) and its β (rank and parity);
- options of levels ≥ 2 keep their W-target (renamed) and gate;
- the four options of the old level-1 movers lose their W-target (they are now level-0 options) and receive the four old level-1
  gates re-assigned in the lexicographic order of the pairs (κ^c_w, g), where w is the option's old W-target (mover 0 or 1),
  κ^c_0 = 1 − c, κ^c_1 = c (RESULTS R110's c-step keys) and g its old gate.

Then (a) Lad_c(G) ∈ 𝓛^R_m, and (b) for every state u of the levels ≥ 1 of G, the IDEAL step of Lad_c(G) from u equals the c-step of G
from u (states identified through the renaming).

Proof.
- (a) Two movers per level, all of degree 2, option k of a mover of level l ≥ 1 W-points to mover 2(l − 1) + k (renaming by −2 keeps
  the convention), no other movers. The Ξ-graph is a subgraph of G's, so it is acyclic. Ranks are a subset of G's, so distinct.
  Gates: the four level-1 values are permuted among themselves, so they stay distinct.
- (b) A-sets. The face of an option is the β-sum along its Ξ-chain under the old state. By ISO no chain of an option of level ≥ 1
  visits 0 or 1, so the chains, the β's and hence the faces are the same in G and in Lad_c(G) under the same state u. So the A-sets
  agree. (This is RESULTS R110 W-ONLY (b): the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1.)
- (b) Keys. Write key_G for the c-step keys of G (level-1 option (x, k): (κ^c_w, g(x, k)); higher option: key_G of its W-target's new
  option followed by its gate), and key_L for the keys of Lad_c(G) (level-0 option: (h(x, k)); higher: as in G). Claim: for two
  options of the same level, key_G(o) < key_G(o′) iff key_L(o) < key_L(o′), under the same new state of the levels below.
  - Old level 1: h is the rank of (κ^c_w, g) among the four, read in the four old gate values, so the orders agree by construction.
  - Higher level: both keys are lexicographic tuples «key of the W-target's new option, then gate». The first components compare as
    at the level below (induction; equal iff the two W-targets are the same mover); the gates are the same in both genomes.
- (b) Moves. Each mover takes the key-least option of its A-set, lowest level first, keys under the new state, in both genomes. The
  A-sets agree and the key orders agree level by level (induction from the bottom), so the chosen options agree. ∎

Corollaries (PROVED, lane).
- (C1) T_0(m) ≤ T^R(m). Each maximal interval of a c-step sequence on which c is constant is, on its counted steps, a prefix of a run
  of Lad_c(G) (a state where the c-step does not move stays fixed under the c-step).
- (C2) T_k(m) ≤ (k + 1)·T^R(m) for every k. Hence the excess E_k(m) := T_k(m) − T^R(m) is at most k·T^R(m).
- (C3) FLIP-ADD can only fail through a superlinear T^R: if T^R(m) = O(m) then E_2(m) ≤ 2T^R(m) = O(m) and FLIP-ADD holds. So no
  amount of data at fixed small m can refute FLIP-ADD; the adversarial measure is the ratio T_2(m) / T^R(m) together with the growth of
  T^R. (With W-ONLY: FLIP-ADD ⇒ T^R_ISO(d) ≤ T^R(d − 1) + O(d), and C2 gives back only T^R_ISO(d) ≤ 3T^R(d − 1) + 2.)
- (C4) Lad_0(G) and Lad_1(G) differ only in the order of their four level-0 gates: the two «classes» (options W-pointing to old mover 0,
  resp. 1) swap places, each class keeping its inner order. So T_k(m) is the longest alternation, with ≤ k switches, between the runs
  of a «class-separated» ladder of 𝓛^R_m and its class swap. (Compare RESULTS R110 SWAP, which leaves 𝓛^R; this form stays in 𝓛^R_m.)

Converse (LIFT, r212/lift.py). A ladder L of 𝓛^R_m whose two smallest level-0 gates belong to different movers is Lad_1(G) of an ISO
genome G of 𝓛^R_(m+1) (after relabelling the options of a level-0 mover of L). So T_0(G) ≥ T(L) for such L.

Machine check (r212/embed.py; runs of Lad_c(G) under r187/ideal.py compared state by state with the c-step runs of L-SI's flipdp.py
Ext.step, every state, both c): 0 mismatches on 100 random ISO genomes at m 2 (3,200 runs), 100 at m 3 (12,800), 30 at m 4 (15,360), and
L-SI's inf18_m3 (128). Negative control NEG=1 (old level-1 gates kept, no re-ranking): 6,677 mismatches of 12,800 at m 3.

Scope (READING, D1): RESULTS R110 signs «T ≤ T_2(d − 1) + 2» for the runs of ISO genomes of 𝓛^R_d only. The brief's «T^R(d) ≤
T_2(d − 1) + 2» therefore covers T^R_ISO(d), not T^R(d): ladders with Ξ-targets at level 0 are outside W-ONLY (b)-(d). FLIP-ADD would
make T^R_ISO polynomial; the non-ISO part of T^R needs another reduction.

## 2. Witnesses and checks
- Engines: r212/fk.c (E-model T_0..T_8, T_inf; climb), r212/fl.c (full-ladder T over all starts, ISO switch; climb). Search tools only.
  - fk vs L-SI flipdp.py: r212/xval.py, 0 mismatches on 460 random ISO genomes (m 2-4).
  - fl vs r187/ideal.py: r212/xvalfl.py, 0 mismatches on 260 random ladders (d 3-4, ISO and not).
- cert.sh (E-model witness): fk; r212/verify.py (DP over r187/ideal.py steps on the level-0-restricted genome + L-NEW box 150 Gen
  replay of the optimal schedule, segment by segment); L-SI flipdp.py (self-checks + XSIM vs Gen); embed.py on the genome; r189/lemck.py
  on the full genome at the witness start.
- certL.py (ladder witness): R197 convention; ISO flag; r187/ideal.py max over all 2^N starts; box 150 checker (VIOL 0, XSIM 0); lemck.
- Files (r212/keep/, sha1 in pins.sha1):

  | quantity | file | values | check |
  | --- | --- | --- | --- |
  | T_0(4) = 13, T_2 15 | T0_m4_13.txt | T_0..T_2 13, 13, 15 | cert OK |
  | T_1(4) ≥ 15 | T1_m4_15.txt | 8, 15, 15 | cert OK |
  | T_2(4) ≥ 17 | T2_m4_17.txt | 6, 11, 17 (segments 6, 5, 6) | cert OK |
  | T_0(5) ≥ 16 | T0_m5_16.txt | 16, 17, 18 | cert OK |
  | T_1(5) ≥ 17 | T1_m5_17.txt | 9, 17, 17 | cert OK |
  | T_2(5) ≥ 22 | T2_m5_22.txt | 10, 14, 22 (8, 5, 9) | cert OK |
  | T_0(6) ≥ 22 | T0_m6_22.txt | 22, 23, 24 | cert OK |
  | T_1(6) ≥ 26, T_2(6) ≥ 34 | T2_m6_34.txt | 13, 26, 34 (13, 13, 8) | cert OK |
  | T_0(7) ≥ 26 | T0_m7_26.txt | 26, 27, 28 | cert OK |
  | T_1(7) ≥ 27, T_2(7) ≥ 37 | T2_m7_37.txt | 14, 27, 37 (14, 13, 10) | cert OK |
  | T^R(5) ≥ 16 | TR_d5_T16.json (+ _canon) | T 16, segments 6 / 0 / 8 | certL OK; modelck SAT |
  | T^R(6) ≥ 22 | TR_d6_T22.json, TRL_d6_T22.json | T 22 (two independent witnesses) | certL OK |
  | T^R(7) ≥ 26 | TRL_d7_T26.json (TR_d7_T22.json: 22) | T 26 | certL OK |
  | T^R_ISO(5) ≥ 15, (6) ≥ 18, (7) ≥ 22 | ISO_d5_T15.json, ISO_d6_T18.json, ISO_d7_T22.json | ISO 1 | certL OK |
- experiments/red/check.sh runs: builds, pins, xval / xvalfl, embed + NEG control, cert of T2_m4_17 and T2_m5_22, certL of TR_d5_T16.

## 3. Method (co-designed construction + simulation; no SAT for any lower bound)
- LIFT (r212/lift.py) turns a T^R(m) champion into an E_m genome with T_0 = its T; climbing T_2 from there gave the m 4-5 records.
- extend.py adds a top or bottom level to a champion (old ranks / gates keep their order); seeds for m + 1.
- fk / fl climbs: random mutations of Ξ-targets (acyclic; ISO for fk), ranks, parities, gates; plateau moves accepted; ANNEAL=t adds
  simulated annealing. Effort per m on both sides: ~0.3-1M evaluations at m 4-5, ~0.5M at m 6, ~0.2M at m 7 (m 7 least explored).
- Dead end recorded (no instance needed: a weak search): unseeded random climbs reach only T_0(4) 11 < 13 and T_1(4) 12-14; every
  record came from a lifted or extended champion.

## 4. Traps (this box)
- verify.py's MATCH test: «MISMATCH» ends with «MATCH»; grep « MATCH$».
- lemck needs gates / betas 0..M−1: embed.py and certL.py renumber order-preservingly.
- A queued push waiter must not `pgrep -f scripts/push.sh` when its own command line contains that string (it waits forever).
- cert.sh changes into r212/: pass witness paths relative to r212.
