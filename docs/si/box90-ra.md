# Box 90: hand design for P / C on N5′-xi runs from S3 on Γ3 (L-SI successor 47; Lead «go» 18:35Z 2026-11-08)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No counterexample candidate: T3 is linear on
every family below.
Setting: L-NEW 65's BOX 198 (claude/l-new fcba92fc, docs/new/N5-PAIR-box198.md): tops(v, I), c_y, RA(y), P(y) (Lemma RA-PATHS
c_y ≤ P(y)), Corollary C-EQUIV (T3 polynomial iff C = max c_y is). L-RED 61 R227 (claude/l-red 1c802d82, docs/red/R227-box198.md §5:
depth alone is cheap).
Tools: experiments/si/box90/ (gen90.py = the FW family; fibseq.py = the abstract sequence; mult90.py = census with the per-pair
multiplicity m(y, z), engines own / g3; run90.sh extracts the pinned engines of pins.txt with git archive; check90.sh, wired).
Engines (two on every number, pins.txt): own = L-RED R221 own.py (IDEAL-CYC Howard, [E-LEV], the genome's start) with L-RED's ra227.py
(claude/l-red ea985380); g3 = L-NEW's Γ3 N5′-xi run from S3 (n5v / n5x / gamma3 / eg195, claude/l-new fcba92fc) with L-NEW's
pair198.py, and my mult90.py on each of the two engines.

## 0. Answer
- P is the WRONG target. PROVED (lane, abstract): a lex-legal top sequence of length 3d − 3 has C = 3 and P = F_(d+2) − 1 (Fibonacci),
  RA depth d, fan-in 2 (§1). So P is not polynomially bounded by C or by the run length, and «(S3) P ≤ poly» is STRICTLY stronger than
  the open core, not equivalent to it (box 198 §3 calls it equivalent).
- DATA (two engines, both counts identical): the same staircase is REALIZED on real N5′-xi runs from S3 on Γ3 by a hand-designed family
  FW(d, 2) (§2): maxP = F_(d+2) − 1 (7, 54, 376, 2583 at d = 4, 8, 12, 16), RA depth d, fan-in 2, C = 3, A = 4, and T3 = 3d + 5,
  N + M = 52d − 45. So P grows EXPONENTIALLY in N + M while T3 grows linearly.
- DEAD (game properties, refuted on FW): any polynomial bound on P(y); (S2) of box 198 (fan-in ≤ k and RA depth O(log(N + M))):
  depth = d is linear in N + M with fan-in 2; CONJECTURE RA-LOG (depth O(log(N + M))) is FALSE (L-RED 61 §5 predicted it from the
  abstract staircase; FW realizes it). A game lemma for L-NEW 66 must therefore bound C (or m below), not the RA paths.
- Window FW(d, k) (§3, DATA, two engines): C = k + 1, A = 2k, fan-in k, T3 linear: constant bounds on C, A or fan-in are false (previous
  maxima C 5, A 9). A = 2k is L-RED 61's «A ~ 2K» stepping stone (R227-hold §0), reached by a K-valued window, and ALT-H's linear
  ceiling is met.
- The right per-pair quantity (PROVED, lane, trivial): m(y, z) := #gaps between consecutive y-tops whose most relevant top is z. Then
  c_y − 1 = Σ_z m(y, z) and m(y, z) ≤ c_z, so «m polynomial» ⟺ «C polynomial» ⟺ (C-EQUIV) «T3 polynomial»; with m ≤ K constant,
  C ≤ 1 + K·M. BIN needs m(y, z) = c_z; FW has m ≡ 1. CONJECTURE RA-MULT(K) and its DATA: §4.
- Milestone 2 (§6, Lead 19:58Z approval): maxm GROWS. Family MW(n): m(y, z) = n, C = 2n + 1, A = 2n + 2, fan-in n + 1, T3 = 6n + 7,
  N + M = 29n + 29 (n = 4, 8, 16, 32; two engines, all fails 0). CONJECTURE RA-MULT(K) for constant K is DEAD; C reaches ≈ T3 / 3 with
  T3 linear. This does NOT touch G-N5-TIME (m ≤ c_z ≤ T3, C ≤ T3).
- Net READING of box 90: P, m and C can each be driven to their trivial ceilings on real N5′-xi runs (P exponential, m and C linear in T3)
  while T3 stays linear in N + M. So none of the box 198 counters separates; a bound must charge C to TIME, i.e. the open core is T3 itself.
- Obstruction to making C grow in this design (READING, §5): every u_j runs its window once; y re-enters under z a second time only if
  z's own W-continuation u_z changes again with a top above y, i.e. a counter at u_z: the PAIR-HIGH recursion itself. No new lemma.

## 1. The abstract Fibonacci staircase (PROVED, lane)
Letters 1 < 2 < … < d. S_d := for j = 1, …, d the stage «j, j − 2, j − 1» (entries < 1 dropped): 1 | 2 1 | 3 1 2 | 4 2 3 | … | d (d−2) (d−1).
- Legal: between two occurrences of a letter y there is a letter above y (y occurs at stages y, y + 1 (last), y + 2 (second); between the
  first two lies y + 1, between the last two lies y + 2). With the states E := (E ∩ {above the top}) ∪ {top}, every top enters and
  E is lex-increasing (E-MON3's form).
- RA(y) = {y + 1, y + 2} for y ≤ d − 2, RA(d − 1) = {d}; so P(y) = 1 + P(y + 1) + P(y + 2), P(d) = 1, P(d − 1) = 2: P(1) = F_(d+2) − 1.
  c_y = 3 for y ≤ d − 2. Length 3d − 3. ∎ Tool: fibseq.py; table out/fibseq.out (d ≤ 16: P(1) = 2583 at length 45, C = 3).
- Reading: P counts paths, but each re-arming letter re-arms y only ONCE here; c_y − 1 = |RA(y)|. Paths overcount when re-armings are
  not nested (BIN nests them: m(y, z) = c_z).

## 2. The game family FW(d, 2) (design; DATA)
Genome (gen90.py d 2; all movers are IDEAL genome movers of R104's form, Ξ-cyclic only through the Even-winning loop W):
- Letters: q_1 … q_d, level-1 one-option movers (W-target u_j, Ξ-target a clock node), gate ranks increasing in j, so e(q_1) ≺ … ≺ e(q_d).
- Clock: an Even lane a_1 … a_m (each a_i → a_(i+1) or → X; X-edges have even β-ranks decreasing along the lane) ending in an Even-
  winning loop W (one option, even β, Ξ → W). a_i becomes Even-winning at state ≈ m − i + 1; q_j's β-face points to the a_i that does so
  at state 3j + 2, from where Odd's e-exit at q_j is forced (the β-face reaches an Even-winning cycle): letter c_j «arrives».
- v (level 0) has a β-option to every q_j: it moves to the newest arrived letter (most relevant).
- u_j (level 0, the W-target of c_j) has an X-option (highest even β) and two delay lanes, to q_(j−2) (length 7) and q_(j−1) (length 5),
  so c_(j−2) and then c_(j−1) arrive at u_j one and two steps after v moved to q_j.
- Run (trace, own and g3 identical): v's e-set at stage j: {c_j}, {c_j} ∪ E(q_(j−2)), {c_j} ∪ E(q_(j−1)); the tops are exactly S_d of §1.
| instance (sha1: inst/SHA1SUMS) | d | N + M | T3 | C | maxP | RA depth | fan-in | A | maxm | fails (own; g3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FW4_2 | 4 | 163 | 17 | 3 | 7 | 4 | 2 | 4 | 1 | 0; 0 |
| FW8_2 | 8 | 371 | 29 | 3 | 54 | 8 | 2 | 4 | 1 | 0; 0 |
| FW12_2 | 12 | 579 | 41 | 3 | 376 | 12 | 2 | 4 | 1 | 0; 0 |
| FW16_2 | 16 | 787 | 53 | 3 | 2583 | 16 | 2 | 4 | 1 | 0; 0 |
- Counters: mult90.py (unit (v, I, y): idfail = c_y − 1 ≠ Σ_z m(y, z), rafail; unit change: lexdec), ra227.py (ph1, ph2, phc, raup, rp,
  lexdec) and pair198.py (ph1fail, ph2fail, rafail, rpfail); all 0 on every row, on both engines. T3 = T of own.py on every row.
- Fit (exact on the 4 rows): T3 = 3d + 5, N + M = 52d − 45, maxP = F_(d+2) − 1 ≈ φ^d = φ^((N + M + 45)/52), i.e. maxP ≥ 1.009^(N+M) on the rows, while T3 ≈ (N + M)/17.

## 3. Window FW(d, k): C = k + 1, A = 2k (DATA)
gen90.py d k: u_j has delay lanes to q_(j−k), …, q_(j−1) (lane to q_(j−i) of length (k + 1)·i + k − i + 1), stage length k + 1.
| instance | d | k | N + M | T3 | C | maxP | RA depth | fan-in | A | maxm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FW6_3 | 6 | 3 | 471 | 30 | 4 | 28 | 6 | 3 | 6 | 1 |
| FW6_4 | 6 | 4 | 719 | 37 | 5 | 31 | 6 | 4 | 8 | 1 |
| FW8_4 | 8 | 4 | 1127 | 47 | 5 | 116 | 8 | 4 | 8 | 1 |
- Same counters, all fails 0, both engines (out/fw90.out). C = k + 1 while the lanes cost N + M of order d·k³ and T3 = (k + 1)·d + O(k):
  C stays far below T3, as it must (C ≤ T3).

## 4. CONJECTURE RA-MULT(K) and its DATA
- CONJECTURE RA-MULT(K): on every genome with [E-LEV], every (v, I) of the Γ3 run and all letters y ≺ z: m(y, z) ≤ K (K an absolute
  constant). By §0, RA-MULT(K) gives C ≤ 1 + K·M and so (C-EQUIV) T3 polynomial. RA-MULT with K := poly(N + M) is EQUIVALENT to the
  open core; only a constant (or slowly growing) K is a real game restriction. I give it the weight of the data below and no more.
- DATA (mult90.py own; unit (v, I, y, z); set: the frozen genomes of L-RED r224-r227/inst, L-NEW box196/inst_si85, box197/hfam, box198/inst,
  L-SI box84-89/inst; scope own.py, cap 3000): out/corpus90.out. maxm ≤ 2 on all of them (2 on CX4, CC2, D2R, DG3, GROW7/8, C2CX4,
  HOLD3K), fails 0. The census was taken before the MW design (§6), which refutes RA-MULT(K) for every constant K.
- What RA-MULT forbids is exactly BIN's nesting: y replaying under each re-entry of the same higher z. A proof would have to show that a
  letter z that re-enters v's set cannot bring back the same lower letter y twice, i.e. a «no replay under one letter» lemma.

## 5. Why FW does not make C grow (READING)
- c_y counts the stages whose window contains y (k + 1 of them), because each u_j runs X → q_(j−k) → … → q_(j−1) once (u_j's own e-set is
  lex-increasing: E-MON3 at u_j).
- A second re-arming by the same z (m(y, z) = 2) needs z to re-enter v's set with y returning after it, i.e. z's W-continuation u_z to
  change again with a top above y, i.e. u_z itself to run a counter. That is PAIR-HIGH's recursion one level down; the FW design gives
  no handle on it. No new obstruction lemma; the open design step is the same as box 89's (a High that waits for the low race), now at u_z.

## 6. MW(n): the per-pair multiplicity grows (milestone 2; DATA, two engines)
Design (genm90.py n L; L = 2): high letters h_1 ≺ … ≺ h_n arrive by the clock of §2 every L + 4 states (W-target a dead sink D). A low
letter z ≺ h_1 (level-1 qz, Ξ-target the Even-winning loop W, so Odd always exits by e_z) has W-target u, with an X-option and a delay
lane of length L to each qh_k. v and R choose among the qh_k and qz; R also has the race option to Q (the least relevant letter y, W-target
hv → v, Ξ-target R: CX4's x18 / x10 / x17 race). Run (trace, own and g3 identical), stage k: R → qh_k (top h_k, y and z leave), R → Q
(top y), v and R → qz once u's lane reaches h_k (top z, y leaves), R → Q (top y). So y re-enters under each of z's n entries.
| instance (sha1: inst/SHA1SUMS) | n | N + M | T3 | C | maxP | RA depth | fan-in | A | maxm | fails (own; g3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MW4_2 | 4 | 145 | 31 | 9 | 10 | 3 | 5 | 10 | 4 | 0; 0 |
| MW8_2 | 8 | 261 | 55 | 17 | 18 | 3 | 9 | 18 | 8 | 0; 0 |
| MW16_2 | 16 | 493 | 103 | 33 | 34 | 3 | 17 | 34 | 16 | 0; 0 |
| MW32_2 | 32 | 957 | 199 | 65 | 66 | 3 | 33 | 66 | 32 | 0; 0 |
- Counters as in §2 (mult90 on own and g3; ra227; pair198), out/mw90.out. Fit (exact on 4 rows): maxm = n, C = 2n + 1, A = 2n + 2,
  T3 = 6n + 7, N + M = 29n + 29.
- DEAD: CONJECTURE RA-MULT(K) for every constant K (§4). Also «A ≤ constant», «fan-in ≤ constant» (A 66, fan-in 33 at N + M 957).
- Not a candidate: T3 linear. m ≤ c_z ≤ T3, so maxm growth cannot touch G-N5-TIME (Lead 19:58Z). The target that matters is C growing
  super-polynomially in N + M, which forces T3 to. A race multiplies changes at ONE vertex, not steps: stacking races needs the spacing to
  double per level (R must see each change two steps apart), so C ∝ T3 on every race stack (READING; same as box 89 §3's feed-forward
  doubling).
