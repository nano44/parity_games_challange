# Box 165 N5-PERMOVER: per-mover move counts on every champion — key flips do NOT follow the Ξ-position, moves do; CONJECTURE PM «moves(x) ≤ (deg(x) − 1)(1 + desc(x))» (0 violations on 255 instance file paths, tight on many movers); without keys PM fails exponentially (2^(desc/2+1) − 1 on the diamond), so a proof must use the key rule
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 165 (18:50Z): per-mover move bound; tools CHAIN-UP (box 164),
the NOW-ONCE ratchet, L-SI Lemma IM (claude/l-si 05644186, docs/si/N5-MECH-box69.md §1), R105 KEYFLIP. Labels: PROVED (lane,
unrefereed) / DATA / CONJECTURE / DEAD (instance) / READING. Model: RESULTS R104 as restated in P-IDEAL-FLIP §0; R105 (ENC, LOCAL,
MONO, KEYFLIP) as landed. Not a TARGET.md claim. No polynomial bound is proved. G-N5-TIME stays OPEN.

## 0. Answer
- Measurement (§2; experiments/new/box165/permover.py, log/all.txt): on 177 IDEAL instance files (all L-RED JSON genomes at
  claude/l-red 002f7cd1 experiments/red/*, including the r197/lag maxima max_d4_L13 (T 13 = T^R(4)), dd_d5_F14, c4x_d5_F12,
  grow_top_N24 (T 64), and every L-NEW box 160-164 genome), for each mover: moves(x), KF_x (R105 KEYFLIP's key flips), desc(x) := the
  number of strict Ξ-descendants (via any option), anc(x). R105 KEYFLIP (moves ≤ 1 + KF at degree ≤ 2) has 0 violations, as it must.
- The Lead's target form «KF_x ≤ g(Ξ-position)» is NOT supported: KF is not governed by the Ξ-position. dd_d5_F14 has a mover with
  desc 1 and KF 14 (= T), c4x_d5_F12 one with desc 0 and KF 9. On 2-wide ladders KF_x depends on the W-level only (R105's excluded
  identity KF_x = F_(lev(x)−1)). KF ≤ T always holds, so no instance can kill a polynomial g. But KF is the wrong quantity: it counts
  key-order flips, most of which do not lead to a move.
- What does follow the Ξ-position is moves(x). CONJECTURE PM (DATA, §3): for every IDEAL-ACYC genome and every start,
  moves(x) ≤ (deg(x) − 1) · (1 + desc(x)) for every mover x.
  - Screen: 0 violations on 255 file paths, some duplicated across L-RED directories (degrees 2, 3, 4; N ≤ 24; T ≤ 64). Equality holds on many movers, e.g. dd_d5_F14 mover 7
    (desc 6, 7 moves) and mover 8 (desc 2, 3 moves).
  - Searches (§3): 0 kills from random all-start screens (d 2-3), hill-climbs on general degree-2 ladders (d 3-6, widths 2-3),
    climbs seeded from the champions, climbs aimed at one tight mover, and diamond Ξ-structures embedded with clock movers driving
    the keys.
  - Consequence if true (PROVED (lane), conditional; §1): T ≤ Σ_x moves(x) ≤ Σ_x (deg(x) − 1)(1 + desc(x)) ≤ (D − 1) · N(N + 1)/2.
    At degree 2: T ≤ N(N + 1)/2.
  - Kill test against the exact data: T^R(d) = 2, 4, 8, 13 against N(N + 1)/2 = 3, 10, 21, 36 at N = 2d. Consistent.
- Without keys PM is FALSE, exponentially (§4, DATA exact on the instances). In the key-free improvement graph of the diamond Ξ-DAG,
  the largest number of moves of a mover on one improving path is 1, 3, 7, 15, 31 = 2^(desc/2 + 1) − 1 for desc = 0, 2, 4, 6, 8 (n = 5,
  N = 10). So PM is a statement about the key rule. Ξ-side tools alone (CHAIN-UP, IM, MONO) cannot prove it beyond desc ≤ 2.
- PROVED (lane), §1: MERGE (a comparison sees only the parts of the two chains before they merge); PM-1 (PM for desc(x) ≤ 1 at
  degree 2, under ANY schedule of improving switches, keys irrelevant); CHARGE-PM (the conditional consequence above).

## 1. Lemmas (PROVED (lane); IDEAL-ACYC; R105 ENC: Ξ_s(x, k) is the integer ε(x, k) + V_s(xt(x, k)), V_s(X) = 0)
- MERGE. For a mover x with options a ≠ b and a state s, let m be the first mover that lies on both chains of (x, a) and (x, b) under s
  (m := X if none). Then Ξ_s(x, a) − Ξ_s(x, b) is the sum of the ε's of the options of the chain of (x, a) strictly before m, minus the
  same sum for (x, b). So x's comparison depends only on the states of the movers on the two chains before they merge.
  Proof: ENC additivity. After m both chains follow the same options (each mover's option is s(·)), so the tails from m are equal and
  cancel. ∎
- PM-1. Let deg(x) = 2 and desc(x) ≤ 1. In any sequence of states in which every mover that switches takes an option of its old-state
  A-set (real runs, forced runs, key-free improving paths), x switches at most 1 + desc(x) times.
  Proof. desc(x) = 0: both Ξ-targets are X, the two option values are constants, and x can only switch toward the strictly better
  one, which then stays better: ≤ 1 switch. desc(x) = 1, y the descendant: if both options target the same place, the difference is
  constant (MERGE): ≤ 1 switch. Else, say xt(x, a) = y and xt(x, b) = X: A_t := Ξ_(s_t)(x, a) is non-decreasing (CHAIN-UP, box 164
  §1) and B := Ξ(x, b) is constant. Switches alternate between a and b. A switch to b needs B > A_t, and a switch to a needs
  A_t > B. After a switch to a, A > B for ever. So the switch pattern is a subword of «b, a»: ≤ 2 switches. ∎
- CHARGE-PM (conditional on PM). Every counted step moves a mover, so T ≤ Σ_x moves(x) ≤ Σ_x (deg(x) − 1)(1 + desc(x)). The pairs
  (x, y) with y a strict Ξ-descendant of x are pairs of an acyclic relation, so Σ_x desc(x) ≤ N(N − 1)/2. ∎
- Does NOT claim: PM itself; any bound at desc ≥ 2 with keys; anything about real N5 (only IDEAL-ACYC).

## 2. Measurement table (selection; full list log/all.txt; format «desc:max moves/max KF» over movers with that desc)
| instance | N | deg | T | per-desc max moves / max KF |
| --- | --- | --- | --- | --- |
| r197/lag/max_d4_L13 (T^R(4) = 13) | 8 | 2 | 13 | 0:1/3 1:1/0 2:3/4 3:3/2 4:4/4 5:3/3 6:3/2 7:1/0 |
| r197/lag/dd_d5_F14 (sha1 06f0e501) | 10 | 2 | 14 | 0:1/2 1:2/14 2:3/14 3:3/3 4:3/2 6:7/6 7:7/6 8:3/3 9:1/0 |
| r197/lag/c4x_d5_F12 | 10 | 2 | 12 | 0:1/9 1:2/9 2:1/0 3:3/12 4:3/2 5:5/6 6:5/6 7:2/12 8:3/2 9:1/0 |
| box160 ISO_1_d4_t12 | 8 | 2 | 12 | 0:1/4 1:1/2 2:3/3 3:3/2 4:4/3 5:3/4 |
| r178 grow_top_N24 | 24 | 3 | 64 | max moves 10, max KF 15; per-desc maxima ≤ 2(1 + desc) |
| r178 u4_d8 | 16 | 4 | 31 | 5:12/8 (bound 3 · 6 = 18) |
- The per-desc maxima grow at most linearly in desc on every file. No instance shows exponential growth in the Ξ-position, so the form
  is NOT DEAD. All runs here are short (T ≤ 64), so the data cannot separate linear from slow super-linear growth.

## 3. Searches for a PM kill (all 0 kills; experiments/new/box165/, logs in log/)
- cand.py / cand2.py: screens. C1 «moves ≤ 1 + desc» fails only at degree ≥ 3 (a degree-3 leaf can move twice), which is why PM has
  the factor (deg − 1). C2 «KF ≤ 1 + desc» fails 202 times. C1D = PM: 0 violations on 255 files (incl. this box's climb outputs).
- randpm.py: every start of random degree-2 genomes (d 2 w 2: 3,000 genomes, 48,000 runs; d 3 w 2: 2 × 400 genomes, 51,200 runs;
  d 3 w 3: 60 genomes, 30,720 runs). Random runs are short (T ≤ 3).
- kill1.py: hill-climbs on (excess, T) over 𝓛^R (d 3-5) and general degree-2 ladders (d 4-6, widths 2-3). Best excess 0.
- seedpm.py: 20,000-step climbs from dd_d5_F14, g5_a, max_d5_L15, rk_D2_k2_d8, ISO_1_d4_t12, grow_top_N15. Best excess 0.
- target.py: climbs on the tight movers 8 (desc 2) and 9 (desc 1) of dd_d5_F14, 40,000 steps × 5 seeds. Best excess 0.
- embed.py: diamond Ξ-structure (n = 3, 4) plus 4-8 clock movers whose moves drive the keys of the diamond movers through random W-levels
  (the clocks are not Ξ-descendants of diamond movers). Best: diamond movers move ≤ 4 times, excess 0.
- READING: the searches are local and the plateau at excess 0 is wide. They are weak evidence. An exact check (SAT, L-RED's xcnf
  driver: «moves(x) ≥ desc(x) + 2 for a named x» on 𝓛^R_d, d ≤ 4) would be the real kill test (NEEDS).

## 4. Control: PM without keys (keylessmv.py; all 2^N states, single improving switches, exact DP)
| diamond n (N = 2n) | desc : max moves of a mover on one improving path | PM excess |
| --- | --- | --- |
| 2 | 0:1 2:3 | 0 |
| 3 | 0:1 2:3 4:7 | 2 |
| 4 | 0:1 2:3 4:7 6:15 | 8 |
| 5 | 0:1 2:3 4:7 6:15 8:31 | 22 |
- Files: box164/out/diamond_n<n>_L<L>.json. Max moves = 2^(desc/2 + 1) − 1 on these. Desc ≤ 2 stays within PM (PM-1, and the
  desc 2 case of the diamond), so the key rule is needed from desc 4 on.
- Mechanism (READING): a mover two layers up switches each time the comparison of its two branches flips, and each flip of a lower
  layer's comparison flips its value twice. Keys stop the cascade in every keyed instance seen: a mover whose comparison flipped
  still waits until its key-preferred option is the better one (R105 KEYFLIP), and the key flips come from the W-levels, not from the
  Ξ-cascade.

## 5. Next (Lead decides)
- Kill side: an exact SAT query for «moves(x) ≥ desc(x) + 2» on 𝓛^R_d (d 3, 4) and on R109's 𝓛_d. That is L-RED's xcnf driver
  (not in my lane).
- Proof side: PM at desc 2 WITH keys is the first case beyond PM-1 that the key-free control does not already settle (key-free desc 2
  also stays ≤ 3, so desc 2 is still Ξ-side). The first key-dependent case is desc 4 (key-free 7 > 5). Lane attempt: combine MERGE
  (a comparison sees only the pre-merge parts) with KEYFLIP and NOW-ONCE (between two moves of x, KP(x) flips). The question is
  whether the comparison flips of x that the keys let through can be charged injectively to the Ξ-descendants.
