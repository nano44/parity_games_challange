# Box 163 N5-FLIPXI (interim): Ξ-side potentials for FLIP-ADD — MONO survives every flip schedule (MONO-FLIP, PROVED (lane)); level-weighted unhappy counts are DEAD in both level directions; T_∞(2) = 9 exact, with fixed-bit remainders ≤ 2 along the whole optimal run
L-NEW successor 53, 2026-11-05 (date -u: see the commit). Lead brief BOX 163 (FLIP-ADD proof attempt, Ξ side; Lead 11:12Z: keep box 163 on the
Ξ-side potential with L-SI's BIT-CHAIN keys, no footprint-j induction (that is L-SI box 65)). Labels: PROVED (lane), EXACT, DATA, DEAD,
CONJECTURE, READING. Model, c-step, forced run, T_k(m), T^R: packet P-IDEAL-FLIP §0-§1 (docs/new/P-IDEAL-FLIP.md, frozen 9effea1f).
Not a TARGET.md claim. No polynomial bound. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.

## 0. Answer (interim)
- PROVED (lane) MONO-FLIP (§1): in any simultaneous update in which every mover that moves takes an option of its old-state A-set, no
  mover's current Ξ-value falls, and every mover that moves strictly raises its own. Keys play no role. So a forced run under ANY bit
  schedule is a strictly increasing chain of current-value vectors (product order), and T_∞(m) := sup over unlimited flips is finite.
- EXACT: T_∞(2) = 9 (box160/iso.py FREE0 ISO KF = 10 at d = 3: T ≥ 10 UNSAT 1528.5 s, box163/log/kinf_d3_t10.log; T ≥ 9 by
  box162/out/kf8_d3_t9.json). Agrees with L-COMP 9 box 27 (exhaustive; via the Lead 11:12Z: T_k(2) = 9 for k ≥ 6 and unlimited).
  T_∞(m) vs T^R(m): m = 1: 3 vs 2; m = 2: 9 vs 4; m = 3: ≥ 17 vs 8; m = 4: ≥ 21 vs 13 (m ≥ 3 lower bounds: L-SI 39 box 64, via the Lead).
- DEAD (instances, §2): the Ξ-side candidates «number of Ξ-unhappy movers» (U), «U weighted toward high levels (2^lev)» (UWT) and
  «U weighted toward low levels (2^(m+1−lev))» (UW) do NOT decrease at every no-flip step: a move can make a mover of a HIGHER level
  unhappy (U, UWT) and a mover of a LOWER level unhappy (UW). Ξ-edges run both ways in level, so no level weighting of the unhappy set
  is a potential.
- DATA (§3): on the optimal T_∞(2) run the frozen remainders R_0, R_1 (the run under a constant bit) stay ≤ 2 at every state while
  T_∞ = 9; the bit flips at every frame. So the run does not «re-arm a stuck run» a few times (box 160's ISO picture at k = 2): with many
  flips it is a long alternation of 1-step pieces. A useful potential cannot be built from R_0, R_1 alone.
- READING: the only potential found so far that decreases at every step is the definitional one, R_∞(u) := the longest forced run
  from u over all bit schedules (zero jump at a flip; it gives T_k(m) ≤ T_∞(m) and nothing more). FLIP-ADD for every k would follow from
  CONJECTURE INF-ADD: T_∞(m) ≤ T^R(m) + O(m). Data: T_∞ − T^R = 1, 5, ≥ 9, ≥ 8 (m 1-4); nothing kills it, nothing supports it strongly.

## 1. Lemma MONO-FLIP (PROVED (lane); any genome, IDEAL-ACYC)
- Statement. Let s, s′ be states such that for every mover y, s′(y) = s(y) or Ξ_s(y, s′(y)) ▷ Ξ_s(y, s(y)). Then for every mover x,
  Ξ_(s′)(x, s′(x)) ⊵ Ξ_s(x, s(x)), with ▷ if s′(x) ≠ s(x). (⊵ := ▷ or equal; ▷ is a strict total order on sets of β's with distinct
  ranks: compare the largest-rank β of the symmetric difference.)
- Proof. Induction along a reverse topological order of the Ξ-graph (Ξ-targets first). Write V_s(y) := Ξ_s(y, s(y)).
  - Order facts. (O1) For a β b in neither P nor Q: P ⊵ Q iff P ∪ {b} ⊵ Q ∪ {b} (the symmetric difference is unchanged). (O2) ⊵ is
    transitive (it is a total order).
  - x does not move. If xt(x, s(x)) = X, both values are {β(x, s(x))}. Else, with z := xt(x, s(x)), V_(s′)(x) = {β(x, s(x))} ∪ V_(s′)(z)
    and V_s(x) = {β(x, s(x))} ∪ V_s(z); β(x, s(x)) lies on neither chain from z (acyclic); by induction V_(s′)(z) ⊵ V_s(z); apply (O1).
  - x moves to k := s′(x). As above Ξ_(s′)(x, k) ⊵ Ξ_s(x, k) (by induction at z := xt(x, k), or equality if it is X), and
    Ξ_s(x, k) ▷ V_s(x) by hypothesis. By (O2), V_(s′)(x) = Ξ_(s′)(x, k) ▷ V_s(x). ∎
- Use. A real IDEAL step, a c-step and any step with any key rule satisfy the hypothesis (each moving mover takes an option of its
  old-state A-set). This is RESULTS R105's MONO direction re-proved without keys; R105 is not used.
- Does NOT claim: any bound (the product order on value vectors has exponentially long chains in general).

## 2. DEAD candidates (exhaustive screen, experiments/new/box163/pot.py: 300 random ISO R197 ladders, d = 3, 4, every U-state with
level 0 at (0, 0), both bits; 19,234 moving frames)
| candidate Φ (over Ξ-unhappy movers x ∈ U) | frames with Φ(new) ≥ Φ(old) | first kill instance (box163/out/) |
| --- | --- | --- |
| U = #unhappy | 1045 | kill_U.json (d 4), u = 00000100, c 0: mover 5 (level 2) moves, unhappy {4, 5} → {4, 6} (6 is level 3) |
| UWT = Σ 2^lev | 920 | same instance: 8 → 12 |
| UW = Σ 2^(m+1−lev) | 934 | kill_UW.json (d 4), u = 00110110, c 0: mover 6 (level 3) moves, unhappy {3, 6} → {2, 3} (2 is level 1): 10 → 16 |
| R_∞ (definitional) | 0 | — |
- sha1: kill_U.json = kill_UWT.json d77eff3c…, kill_UW.json 4808caf7…. CNT (number of strictly better options) equals U at degree 2.

## 3. DATA: the optimal T_∞(2) run (box163/path.py on box162/out/kf8_d3_t9.json; levels 1: movers 2, 3; level 2: movers 4, 5)
| frame | c | R_0 | R_1 | R_∞ | unhappy | movers |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 1 | 9 | 2, 3, 4, 5 | 4 |
| 2 | 1 | 0 | 1 | 8 | 2, 3, 5 | 2, 3 |
| 3 | 0 | 1 | 0 | 7 | 3, 5 | 3 |
| 4 | 1 | 0 | 2 | 6 | 5 | 5 |
| 5 | 0 | 1 | 1 | 5 | 2, 3, 4 | 2 |
| 6 | 1 | 0 | 1 | 4 | 3, 4 | 3 |
| 7 | 0 | 1 | 0 | 3 | 4 | 4 |
| 8 | 1 | 0 | 1 | 2 | 2 | 2 |
| 9 | 0 | 1 | 0 | 1 | 3 | 3 |
- Moves per mover: 2: 3, 3: 4, 4: 2, 5: 1. After the level-2 move at frame 4, movers 2, 3 and 4 are unhappy again (frame 5): one move
  re-arms both levels. The bit alternates every frame: the key side «releases» exactly one armed mover
  per frame.

## 4. Next (proposal)
- Per-mover form instead of a global Φ: moves(x) ≤ 1 + #(changes of x's better option) (FLIP-1's argument, valid under any keys) gives
  the exponential Ξ-only recursion; the BIT-CHAIN key side must cap how often a changed better option is RELEASED. Candidate (to test
  exactly): «a level-l mover is released at most once per change of its better option AND per change of c_l(·)», counted with L-SI's
  bit chain.
- Exact T_∞(3) (L-SI ≥ 17) only with a cube driver (d 4 monolithic runs take hours); not started.
- Files: experiments/new/box163/mono.py (MONO across random flips: 2,990 frames, 0 falls, 0 non-strict), pot.py, path.py, out/, log/.

## 5. Reading of L-SI box 66 BULGE (Lead 14:07Z; claude/l-si f21640dd, docs/si/N5-FRONT-box66.md, lane-level, not refereed)
- DATA (EXACT per genome; box162/flipcheck.py Vk over every U-start, level 0 at (0, 0), so V_k(G) := the max over starts of V_k(G, s)):
  | genome (𝓛^R_4, ISO) | V_0(G) | V_1(G) | V_2(G) | V_3(G) |
  | --- | --- | --- | --- | --- |
  | box160/out/kf1_d4_t10.json | 5 | 10 | 10 | 10 |
  | box160/out/ISO_1_d4_t12.json | 5 | 8 | 12 | 13 |
  - Both extremal flip genomes have a flip-free maximum of only 5 < T^R(3) = 8. Their flip runs are 2 and 2.6 times that.
- Does BULGE contradict FLIP-ADD? NO. Every number is consistent with T_k(3) ≤ T^R(3) + O(1) (excess ≥ 2 at k = 1, ≥ 4 at k = 2, ≥ 5
  at k = 3). Nothing here grows with m; there is only one m (3) in the data beyond m = 2.
- It SHARPENS the target, in two ways.
  - (S1) DEAD as a proof route (READING, by the two instances): any per-genome additive form «V_k(G) ≤ V_0(G) + c» with c < 5 at m = 3,
    k = 1 (kf1_d4_t10: 10 > 5 + 4). In particular the m = 2 line «pre + post ≤ T_0 + 1», read per genome, does not lift. With SWAP-RUN
    the only per-genome bound left is the trivial V_k(G) ≤ (k + 1) V_0(G) (each piece is a run of H_q or (G^swap)_q, and the
    flip-free maximum over both bits bounds both), and kf1_d4_t10 attains it at k = 1.
  - (S2) So FLIP-ADD, if true, is a GLOBAL trade-off: a genome whose flip-free runs are long (≈ T^R(m)) must chain badly, and a genome
    that chains well must have short flip-free runs. L-SI's f_m3_p4_s1 (V_0 = 8 under each bit, max pre + post 9) and kf1_d4_t10 (V_0 =
    5, sum 10) are the two ends. FLIP-ADD at k = 1 is exactly «V_1(G) ≤ T^R(m) + O(m) for every G»; the data say a proof has to charge
    the excess V_1(G) − V_0(G) to the gap T^R(m) − V_0(G) (kf1_d4_t10: excess 5, gap 3), not to anything that is small per genome.
    (A first draft of this entry stated a «CHAIN-TRADE» inequality V_1 ≤ max(2 V_0, V_0 + c); it is vacuous, since V_1(G) ≤ 2 V_0(G)
    always holds by SWAP-RUN, and is withdrawn.)
- The Ξ-side reading (box 163): MONO-FLIP makes the value vector rise along the whole flip run; a short flip-free run with a long flip
  run means the value vector has a long chain that no single bit can follow. A potential that sees this has to measure «distance to a
  bit-c dead end» for both c together: R_∞ (definitional) does, R_0, R_1 (frozen) do not (§3: R_0, R_1 ≤ 2 along a 9-step T_∞ run).
- On the SAT query «max post subject to pre ≥ p at m = 3, p = 0..8»: the side condition is two lines in box160/iso.py (bits equal on
  frames 1..p, flipped from frame p + 1 on, KF = 1). The d 4 one-flip runs are slow (T_1(3) ≥ 10 SAT took 8261 s; ≥ 11 died
  UNKNOWN after hours twice, the second time in today's 14:07Z container restart), and monolithic runs do not survive restarts. The
  mid-range UNSAT points (pre 3..6, sum ≥ 11) are the expensive ones.

## 6. Global trade-off candidate SUM (Lead 14:13Z: a non-vacuous charge of V_1(G) − V_0(G) to T^R(m) − V_0(G))
- V_k(G) := max over U-starts of the exact per-genome k-flip maximum (box162 Vk). Trivial facts: V_0(G) ≤ T_0(m); V_k(G) ≤ (k + 1) V_0(G)
  (SWAP-RUN, both bits).
- CONJECTURE SUM_k (lane; DATA m ≤ 3 only): for every ISO genome of 𝓛^R_(m+1), V_0(G) + V_k(G) ≤ 2 T^R(m) + 1, for k = 1 and k = 2.
  - Charge form: V_k(G) − V_0(G) ≤ 2 (T^R(m) − V_0(G)) + 1. Each step a genome's flip-free runs fall short of T^R(m) buys at most two
    extra flip steps.
  - Not vacuous: at m = 3 the trivial facts allow V_0 + V_1 up to 8 + 10 = 18 and V_0 + V_2 up to 8 + 12 = 20. At m ≤ 2 it IS vacuous
    (V_0 ≤ T^R, V_1 ≤ T^R + 1 already give it), so m = 3 is the first test.
  - Tight at both ends: f_m3_p4_s1 (L-SI pin; V_0, V_1, V_2 = 8, 9, 9): 17 for k = 1, 2; ISO_1_d4_t12 (V_0 5, V_2 12): 17 for k = 2.
  - k = 3 is DEAD: ISO_1_d4_t12 has V_0 + V_3 = 5 + 13 = 18 > 17 (EXACT per genome; box160/out/ISO_1_d4_t12.json).
  - It does NOT imply FLIP-ADD. With V_k ≤ (k + 1) V_0 it gives T_1(m) ≤ (4 T^R(m) + 2) / 3 and T_2(m) ≤ (6 T^R(m) + 3) / 4.
    Those are multiplicative, so with W-ONLY (d) the recursion is still exponential. SUM is a first true-looking global trade-off,
    not the bound.
- DATA (box163/sumclimb.py; hill-climb over ISO 𝓛^R_(m+1) genomes, objective V_0 + V_k; lower bounds only; logs box163/log/climb_*):
  | m | objective | starts | best (V_0, V_1, V_2) | max found | 2 T^R(m) + 1 |
  | --- | --- | --- | --- | --- | --- |
  | 2 | V_0 + V_1 | 4 seeds × 10 random restarts × 2000 steps | (4, 5) | 9 | 9 |
  | 3 | V_0 + V_1 | from f_m3_p4_s1 (2 seeds), kf1_d4_t10 (2 seeds), random, ISO_1 | (8, 9) | 17 | 17 |
  | 3 | V_0 + V_2 | from ISO_1_d4_t12 and from f_m3_p4_s1 | (5, 8, 12) and (8, 9, 9) | 17 | 17 |
  - The climb from kf1_d4_t10 (5, 10) moved to (8, 9): it trades flip gain for flip-free length along SUM = 17, never above it.
- R_∞ on the ISO channel (Lead's question): R_∞ is defined ON the ISO forced model, decreases by ≥ 1 at every moving frame and does not
  move at a flip (PROVED (lane), immediate from the definition + MONO-FLIP termination). So it is a usable potential, but what it proves
  is only T_k(m) ≤ T_∞(m) for every k. It gives FLIP-ADD iff INF-ADD (T_∞(m) ≤ T^R(m) + O(m)) holds. Data T_∞ − T^R = 1, 5, ≥ 9, ≥ 8
  (m 1-4). The real ISO runs need only k ≤ 2, so R_∞ throws away the k ≤ 2 restriction that SUM_2 uses.

## 7. Why SUM breaks at k = 3, and whether it can be iterated (Lead 15:02Z)
- DATA (box163/pieces.py: an optimal ≤ k-flip run over all starts, exact, cut into its constant-bit pieces; lengths in order):
  | genome | V_0 | k = 1 | k = 2 | k = 3 |
  | --- | --- | --- | --- | --- |
  | ISO_1_d4_t12 | 5 | 3, 5 (= 8) | 4, 3, 5 (= 12) | 1, 4, 3, 5 (= 13) |
  | kf1_d4_t10 | 5 | 5, 5 (= 10) | 10 (k 2 adds nothing) | |
  | f_m3_p4_s1 (L-SI) | 8 | 4, 5 (= 9) | 3, 1, 5 (= 9) | |
  - Every piece after the first runs until its bit is stuck (its length equals the frozen remainder R_c at its start). In ISO_1 the
    optimal (k + 1)-schedule is the optimal k-schedule with ONE MORE PIECE IN FRONT: the run grows backwards, one stuck run at a time.
- Answer (READING). On this data, k = 3 does not break SUM through a structural parity effect. k = 2 starts and ends on the same bit
  (c, 1 − c, c) and k = 3 does not, but the break is simply one more short piece (length 1) in front of the k = 2 run, which was already
  tight (5 + 12 = 17). Nothing in the data says that an even number of flips (back to the original genome) is special.
- Can SUM be iterated? The natural iterable form is per bit, and it is DEAD:
  - W_c(G) := the largest number of moving frames that use bit c, over all schedules with ANY number of flips (box163/perbit.py, exact).
    «W_c(G) ≤ T^R(m) + 1 for both c» would give T_∞(m) ≤ 2 T^R(m) + 2 for every k at once.
  - DEAD at m = 2: box163/out/perbit_m2_s32.json (ISO 𝓛^R_3; sha1 a530b076…): W_0, W_1, T_∞, V_0 = 2, 6, 8, 4. W_1 = 6 > T^R(2) + 1 = 5.
  - DEAD at m = 3: box163/out/perbit_m3_s42.json (sha1 cb3838c9…): W_0 = 10 > 9; also perbit_m3_s44.json: W_1 = 10.
  - Found by hill-climb (perbit.py --climb); each instance re-evaluated by the exact search and checked R197-convention, ISO, acyclic.
  - SUM_k with k = 3 is DEAD (§6). So no per-genome form iterates over k on the data. The iterable statement left is global:
    CONJECTURE INF-2 (lane; DATA): T_∞(m) ≤ 2 T^R(m) + 1. m = 1: 3 ≤ 5; m = 2: T_∞(2) = 9 = 2·4 + 1 (EXACT here and in L-COMP 27);
    m = 3: ≥ 17 = 2·8 + 1 (L-SI lower bound; my climbs reach 13). Like SUM it is multiplicative (factor 2) and does not give a
    polynomial bound through W-ONLY.
- No lane proof of SUM_1 yet. What a proof must use, from the piece data: a one-flip run whose two pieces are both near-full runs exists
  only when each bit's runs are short (kf1: 5 + 5 with V_0 = 5), and a genome with a full T^R run under one bit has only one long piece
  (f_m3_p4_s1: 4 + 5 after an 8-run is possible). SUM_1 says this exchange rate is at most 2 : 1.
