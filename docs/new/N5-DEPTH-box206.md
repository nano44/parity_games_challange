# Box 206 (D18): CHANGE DEPTH — only deep class changes can make IDEAL-CYC runs long; the MWR leapfrog is depth 0 (L-NEW successor 70, Opus)
Written 2026-11-12 (date -u in the commit). Brief (Lead 01:46Z «go»): «work on research item 2: the MWR basin-leapfrog lemma at k = 1».
Item 2 of the brief: «Aim for a lemma bounding the number of W-target class changes a basin gate can see along a constant exit route
(polynomial or not, on which premises), or an exact obstruction with its instance.»
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting: IDEAL-CYC(G) (RESULTS R118 (a)), every genome, any Ξ-feedback number k
unless stated; class_t(v) = (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), sets of e-vertices compared lexicographically by their
most relevant differing element (RESULTS R121, R123); m := the number of e-vertices (= M); S_c(m) := Σ_(j=0..c+1) C(m, j).
Tools: experiments/new/box206/ (depth206.py, ascdepth206.py, climb206.py); outputs box206/out/.

## 0. Answer
- New statistic, the CHANGE DEPTH. At a step t with Λ_(t−1)(v) = Λ_t(v) and E_(t−1)(v) ≠ E_t(v), let z be the most relevant element of
  E_(t−1)(v) Δ E_t(v); depth := the number of elements of E_(t−1)(v) ∪ E_t(v) more relevant than z (they are common to both sets).
  Depth 0: the most relevant e-vertex of v's play changes. A binary counter on E needs changes of unbounded depth.
  LOUD DEPTH of a loud step t (some vertex changes class): −1 if some vertex changes Λ at t, else the least change depth over the
  vertices whose E changes at t.
- **Lemma DEPTH-COUNT (PROVED, lane; premise R121 E-MON; no hypothesis).** For every c ≥ 0, every vertex v and every interval I of
  states with Λ(v) fixed: at most S_c(m) − 1 of the changes of E(v) on I have depth ≤ c.
- **Theorem LOUD-SPLIT (PROVED, lane; premises R121 E-MON and the per-vertex form of R118 (e) as stated in R121's line, R123 QUIET).**
  For every genome and every c ≥ 0, with Q the number of loud steps and Q_(>c) those of loud depth > c:
    Q ≤ n(2M + 2) + n(2M + 3)(S_c(M) − 1) + Q_(>c)   and   T_CYC ≤ Q + (Q + 1)·L   (L, n as in R123).
  So on any family of genomes, T_CYC is polynomial in N + M iff for some fixed c the number Q_(>c) of loud steps of loud depth > c is.
  In particular: if every loud step has loud depth ≤ c, T_CYC = O((N + M)^(c + 6)) (crude exponent; §2).
- For the brief (MWR basin leapfrog): on MWR(n), n = 4, 8, 16, every class change of the flipping gate's W-target u has depth 0 (u's
  most relevant e-vertex rises: e_qh1 < e_qh2 < …), every change of its Ξ-target R has depth ≤ 1, and every loud step but one has loud
  depth 0 (DATA §3). By DEPTH-COUNT a W-target whose changes have depth ≤ c changes class at most (2M + 2) + (2M + 3)(S_c(M) − 1) times
  over the run, so with GATE-FLIP + FACE-TARGET (box 203 / 204) a gate whose two targets change at depth ≤ c flips O(M^(c + 2)) times
  (c = 1 for MWR). READING: the leapfrog itself is harmless; a basin gate can flip super-polynomially often only if its W-target or
  Ξ-target has super-polynomially many changes of depth > c, for every fixed c. That is the exact obstruction to bound at k = 1.
- DEAD (two conjectures I set up while writing this box, killed by data; §4): «change depth bounded» (WC(n), k = 2: depth n) and
  «loud depth ≤ max ascents» (K1F34_n84, step 52: loud depth 3, ascents 2). Neither kills LOUD-SPLIT's open quantity: on WC(n), T = 4.
- CONJECTURE DEEP-k1 (open): at k = 1, for some fixed c, Q_(>c) is polynomial in N + M (equivalently T_CYC polynomial at k = 1, by
  LOUD-SPLIT). DATA: Q_(>1) ≤ 2 on every k = 1 record and 0 on 1,000 random k = 1 genomes;
  a climb maximizing it reached 5 at N 48 (§3.3; still running): small, and nothing asymptotic.

## 1. Lemma DEPTH-COUNT (PROVED, lane)
Let I be an interval of consecutive states with Λ_t(v) = w fixed, c ≥ 0, and P_t := the set of the c + 1 most relevant elements of
E_t(v) (all of E_t(v) if it has fewer). Claim: P is non-decreasing on I (lexicographically) and strictly rises at every change of
depth ≤ c; so the changes of depth ≤ c number at most (#subsets of size ≤ c + 1 of the m e-vertices) − 1 = S_c(m) − 1.
Proof. Take consecutive a, b ∈ I with E_a ≠ E_b, and z, d as in §0. By E-MON (R121: Λ fixed implies E_a ≤ E_b) z ∈ E_b \ E_a. The
elements more relevant than z are the same d elements in E_a and E_b (z is the most relevant difference).
- d ≥ c + 1: the c + 1 most relevant elements of E_a and of E_b are among those d common elements: P_a = P_b.
- d ≤ c: z is among the c + 1 most relevant elements of E_b, so z ∈ P_b, and z ∉ E_a ⊇ P_a. The elements of P_a and of P_b more
  relevant than z are the d common ones. So the most relevant element of P_a Δ P_b is z, in P_b: P_a < P_b.
At steps with E_a = E_b, P_a = P_b. So along I, P never falls and rises strictly at each change of depth ≤ c; its values are subsets of
size ≤ c + 1 of the e-vertices. ∎
- Remarks. c = 0: at most m top changes per Λ-interval (the top only rises). If every change on I has depth ≤ c, E takes at most
  S_c(m) distinct values on I. A chain through all 2^m subsets (a binary counter) has changes of every depth up to m − 1.

## 2. Theorem LOUD-SPLIT (PROVED, lane)
Premises: RESULTS R121 E-MON (Lemma E-MON: «if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)»); R121's premise list, R118 (e) in its
per-vertex form «Λ_t(v) takes at most 2M + 3 values, in increasing reward»; R123 Theorem QUIET («every maximal window of quiet steps has
at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps, n = N + 3M + 6»).
Proof. (i) T_CYC ≤ Q + (Q + 1)L: the T_CYC steps are Q loud steps and at most Q + 1 maximal quiet windows (QUIET).
(ii) A loud step of loud depth −1 changes Λ at some vertex. Per vertex Λ takes at most 2M + 3 values in increasing reward, so it changes
at most 2M + 2 times: at most n(2M + 2) such steps.
(iii) A loud step of loud depth d ∈ [0, c] has a vertex v whose E changes at depth d ≤ c with Λ(v) fixed. Per vertex, the states split
into at most 2M + 3 maximal Λ-intervals (Λ only rises), and on each, by DEPTH-COUNT, at most S_c(M) − 1 changes of depth ≤ c. Charging
the step to v: at most n(2M + 3)(S_c(M) − 1) such steps.
(iv) The other loud steps are counted by Q_(>c). Summing (ii)-(iv) gives the bound on Q; with (i), T_CYC is bounded by a polynomial in
N + M times (1 + Q_(>c)). Conversely Q_(>c) ≤ T_CYC. ∎
- Exponent (crude): S_c(M) = O(M^(c + 1)), n = O(N + M), L = O((N + M)^3): with Q_(>c) = 0, Q = O((N + M)^(c + 3)) and T_CYC = O((N + M)^(c + 6)).
- Compare RESULTS R121/R123 (ASC-T): plays with ≤ B ascents give degree 5·2^B − 3 + O(1). LOUD-SPLIT's hypothesis is dynamic (where the
  class changes happen), not structural; on the k = 1 records it is met with c = 1 at all but ≤ 2 steps per run (§3).
- Mover form: box 204 Theorem EQ (lane) says T_CYC is polynomial iff D_mov is; by DEPTH-COUNT, D_mov is polynomial when the movers'
  changes of depth > c are polynomially many, for a fixed c (same proof as (ii)-(iii) per mover).

## 3. DATA
Tool depth206.py (IDEAL-CYC; box203 gfc203.hist_ideal). Must-0 counters (TOTALS): elfall (unit (vertex, step): E falls at fixed Λ;
R121 E-MON), topfall (same unit: the most relevant element of E falls at fixed Λ), pfail (unit change: P_t with c := the largest depth on
the vertex's Λ-interval does not strictly rise), ufail (unit (change, c0), c0 = 0, 1, 2: DEPTH-COUNT's unconditional form fails: P^(c0)
does not strictly rise at a change of depth ≤ c0, or changes at a change of depth > c0), cfail (unit (vertex, Λ-interval): more changes
than S_c(m) − 1, c the largest depth there). Descriptive: maxdepth (largest change depth), L-1 / L0 / L1 / … (unit: loud steps, by loud
depth), maxloud (largest loud depth). Scope «all» = every vertex of Γ(G) (LOUD-SPLIT's quantity); «movers» = the movers only.
### 3.1 k = 1 (scope all; out/depth206_k1records_all.out, out/depth206_all_k1_s63.out)
| genome (k = 1) | T | maxdepth | loud steps by loud depth | Q_(>0) | Q_(>1) |
| --- | --- | --- | --- | --- | --- |
| MWR4_2 / MWR8_2 / MWR16_2 | 30 / 54 / 102 | 1 | L0 29 / 53 / 101, L1 1 | 1 | 0 |
| K1F21_n48 | 31 | 3 | L0 27, L1 1, L2 1, L3 1 | 3 | 2 |
| K1F34_n84 | 52 | 3 | L0 50, L2 1, L3 1 | 2 | 2 |
| K1C16_n400 | 51 | 3 | L0 43, L1 4, L2 1 | 5 | 1 |
| B400_r32 (L-COMP 15) | 49 | 2 | L0 46, L1 2, L2 1 | 3 | 1 |
| k1fail_202 | 4 | 1 | L0 3 | 0 | 0 |
| naive_k1_s71 (box 205) | 3 | 0 | L-1 1 | 0 | 0 |
| K1D4_n48 (this box, §3.3) | 23 | 5 | L-1 2, L0 10 | 0 | 0 |
- 1,000 k = 1 genomes (box202 k1srch202.mk, seed 63; T ≤ 7): 1,318 loud steps, L-1 1,045, L0 273: every loud step has loud depth ≤ 0;
  maxdepth 4 (one genome; 822 genomes 0, 162 genomes 1).
- All must-0 counters 0 on every row of 3.1-3.2 (23 output rows, both scopes).
### 3.2 other sets
- 1,000 rand191 genomes (d 1-6, w 1-3, degree 2-3, seed 64; scope all): 1,690 loud steps, L-1 1,283, L0 402, L1 5; maxdepth 3.
- 300 k = 2 genomes (K1_MODE=2, seed 65; scope all): 573 loud steps, L-1 475, L0 97, L1 1; maxdepth 3.
- 58 genomes: box 202's 53 corpus genomes, k1fail_202, MWR16_2, K1C16_n400, B400_r32, K1F34_n84 (scope movers; out/depth206_corpus.out, run with the
  first version of depth206.py, which had no ufail / loud columns): elfall, topfall, pfail, cfail 0 on all 58 rows; maxdepth 0 (1
  genome), 1 (9), 2 (34), 3 (8), 4 (2: CT12_cap200, WC4_2), 5 (DSALT9_n416), 6 (DHIB26_2804), 8 (WC8_2), 16 (WC16_2).
- Controls (check206.out): DEP_CTRL=1 (relevance reversed) on MWR4_2: elfall 96, topfall 20, pfail 96, ufail 212 (all fire).
### 3.3 kill-side climbs at k = 1 (climb206.py, box203 aclimb203 mutations with AC_FREE=1, k kept = 1; logs in the scratchpad, not kept)
- Objective maxdepth (seed 1, from K1F21_n48, stopped at 2,275 iterations): best maxdepth 4 at N 48 (movers; 5 in scope all), frozen as
  inst/K1D4_n48.json (sha1 in inst/SHA1SUMS). Its loud steps all have loud depth ≤ 0: deep changes there ride on shallow ones.
- Objective (#loud steps of loud depth ≥ 2, max loud depth, T) (seed 2, from K1F21_n48): 2 at start, 4 after 875 iterations, 5 after 1,192
  (N 48), still running at this commit; seed 3 from K1F34_n84 stopped at 125 iterations (3). Small numbers at N 48-84; nothing asymptotic.

## 4. DEAD (with instances)
- «Change depth is bounded by a constant» (any k): WC(n) (box 202 corpus, k = 2): one change of depth n at n = 4, 8, 16
  (experiments/new/box202/inst/WC4_2, WC8_2, WC16_2; maxdepth 4 / 8 / 16, T = 4). This is why LOUD-SPLIT counts STEPS of loud depth
  > c rather than bounding depth: WC's deep change is one step.
- «Loud depth bounded» (any k): the same WC(n), loud depth n at one step (out/ascdepth206.out; WC16_2: maxld 16).
- «Loud depth ≤ the largest number of ascents of any play at t − 1 or t» (CONJECTURE LD-ASC, set up and killed here): K1F34_n84 (k = 1,
  experiments/new/box204/inst/K1F34_n84.json), step 52: loud depth 3, ascents 2. Also DHIB26_2804 step 28 (6 vs 4) and CT12_cap200
  step 46 (4 vs 3) (ascdepth206.py, out/ascdepth206.out); WC(n): equality (n vs n). A link to R121's ascents would have improved
  ASC-T's exponent 5·2^B to about B; it fails by at least 2.

## 5. Status and next step
- PROVED (lane, unrefereed): DEPTH-COUNT (premise R121 E-MON), LOUD-SPLIT (premises R121 E-MON, R121's per-vertex form of R118 (e),
  R123 QUIET); the mover form via box 204 Theorem EQ (lane).
- READING for the brief: the MWR basin leapfrog is a depth-0 mechanism (u's top e-vertex rises, R's changes have depth ≤ 1, all loud
  steps but one have loud depth 0), hence polynomially bounded by DEPTH-COUNT alone. What a super-polynomial k = 1 run would need is
  super-polynomially many loud steps at which NO vertex changes Λ or changes E at depth ≤ c, for every fixed c. At k = 1 the records have at most
  2 such steps (c = 1) per run; a climb reached 5 at N 48.
- CONJECTURE DEEP-k1 (open): for some fixed c (data: c = 1 or 2), Q_(>c) is polynomially bounded at k = 1. Equivalent to T_CYC
  polynomial at k = 1 (LOUD-SPLIT + Theorem EQ). Next: (i) a structural reason why a loud step has a shallow change somewhere (the
  divergence vertex of a changed play carries the same top difference z with depth no larger: start of a proof; a reconvergent high
  e-vertex is what keeps its depth positive); (ii) climbs on Q_(>1) at larger N; (iii) a WC-like k = 1 construction that repeats
  WC's deep step.

## Addendum A (L-NEW successor 70; Lead 02:59Z: «Proceed as you proposed: first Addendum A with the frozen climb genome …, then the divergence-vertex lemma at k = 1»; written 2026-11-12 by date -u)
### A1. The climb genome K1L7_n48 (frozen)
- inst/K1L7_n48.json (sha1 in inst/SHA1SUMS; k = 1 by box202 fvs202.kfvs): the end state of climb206.py seed 2 (CL_OBJ=loud, AC_FREE=1,
  from K1F21_n48) at 3,000 iterations, score (7, 4, 37) = (movers' loud steps of loud depth ≥ 2, max loud depth, T); log
  out/climb206_loud_s2_part1.log.
- Scope all (out/depth206_K1L7.out): T 37, loud 34; by loud depth L-1 1, L0 24, L1 2, L2 2, L3 1, L4 4: Q_(>1) = 7 with scope all
  too (L2 + L3 + L4); maxdepth 4; all must-0 counters 0.
### A2. Lemma DIV (PROVED, lane): the divergence vertex carries the change
Premises: R118 (a) (IDEAL-CYC: every non-mover Even vertex frozen, Odd unrestricted), R123 LOC-K2 (σ̄(K2) = K1 at every state), the
value (Λ, Π, k) of R118's order (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3: Π = the vertices of the path from v to its cycle node Λ,
before Λ, more relevant than Λ).
Statement. Let t ≥ 1 and v a vertex with Λ_(t−1)(v) = Λ_t(v) = w and E_(t−1)(v) ≠ E_t(v); z and d as in §0. Let p be the first vertex of
v's play under (σ_(t−1), σ̄_(t−1)) whose successor under (σ_t, σ̄_t) is different. Then p exists, p comes before the first occurrence of
w on both plays from v (which agree up to p), Λ_(t−1)(p) = Λ_t(p) = w, E_(t−1)(p) Δ E_t(p) = E_(t−1)(v) Δ E_t(v), and p's change has the
same z and depth ≤ d. p is a mover with σ_t(p) ≠ σ_(t−1)(p) or a gate with σ̄_t(p) ≠ σ̄_(t−1)(p).
Proof. Positional plays agree as long as successors agree. If no vertex of the old play up to its first occurrence of w had a new
successor, the new play would follow the same path to w; since Λ_t(v) = w, Π_t(v) would be the same set (Π depends on the path to Λ
only), so E_t(v) = E_(t−1)(v): contradiction. So p exists and precedes the first w on the old play; the new play shares the prefix
v … p, which does not contain w. Both plays are simple up to w, so for s ∈ {t − 1, t}: Π_s(v) = A ⊔ Π_s(p) with A := the prefix
vertices before p more relevant than w (the same set at both states), and Λ_s(p) = w (p's play is the suffix of v's). Hence
E_(t−1)(v) Δ E_t(v) = E_(t−1)(p) Δ E_t(p), the same z, and the elements of E_s(p) more relevant than z are among those of E_s(v): depth
≤ d. Vertices with a fixed successor in IDEAL-CYC are the e-vertices, the β's, c_W, c_X and the frozen core and non-mover Even
vertices; K2's successor is K1 at every state (LOC-K2). So p is a mover (σ changed) or a gate (σ̄ changed). ∎
- Corollary DIV-LOUD (PROVED, lane). The loud depth of a loud step with no Λ change is attained at a mover that switches or a gate that
  flips at that step. So in LOUD-SPLIT (iii) only movers and gates need to be charged:
  Q ≤ n(2M + 2) + (N + M)(2M + 3)(S_c(M) − 1) + Q_(>c).
- DATA for DIV (div206.py, out/div206.out; must-0 counters, unit (v, t) with Λ_t(v) fixed and E changed: nop (no p before the first
  w), lamp (Λ(p) ≠ w), symp (E(p)'s symmetric difference ≠ E(v)'s), dep (p's depth > v's), kind (p not a switching mover or flipping
  gate)): all 0 on K1L7_n48 (1,940 cases), MWR8_2 (2,225), WC8_2 (146), K1F21_n48 (1,930), K1F34_n84 (4,307), 300 k = 1 genomes (seed 67;
  1,635) and 300 rand191 genomes (seed 68; 3,410). Control DIV_CTRL=1 (p replaced by its old successor) on K1L7_n48: symp 1,277,
  kind 1,268 (fires).
- DATA for DIV-LOUD (deepdiag206.py, out/deepdiag206.out; K1L7_n48, K1F21_n48, K1F34_n84, K1C16_n400, B400_r32, MWR8_2): every deep loud
  step (loud depth ≥ 2) is attained at a switching mover.
### A3. Where the deep loud steps are at k = 1 (DATA, READING)
- Unit: loud steps of loud depth ≥ 2 (scope all), listed by step number t of T; «CC» = the cycle set of Ξ_σ changes at t.
  | genome (k = 1) | T | deep loud steps (t: loud depth) |
  | --- | --- | --- |
  | K1L7_n48 | 37 | 30: 2 CC, 31: 2 CC, 33: 3 CC, 34: 4 CC, 35: 4, 36: 4, 37: 4 |
  | K1F21_n48 | 31 | 30: 2 CC, 31: 3 CC |
  | K1F34_n84 | 52 | 51: 2 CC, 52: 3 CC |
  | K1C16_n400 | 51 | 51: 2 CC |
  | B400_r32 | 49 | 49: 2 CC |
  | MWR8_2 | 54 | none |
- READING: at k = 1 the deep loud steps sit in the last steps of the run. On K1L7 (steps 28-37, Λ ≡ K1 at every switching mover) the
  switching movers' e-sets are subsets of the six most relevant e-vertices: e.g. step 35, mover 39: E from positions {96, 94, 93, 92} to
  {96, 94, 93, 92, 91} (positions in the relevance order of the 97 e-vertices, 96 = most relevant): the deep changes add or swap
  elements inside one block of top e-vertices, reached repeatedly through ascents. They are not a counter in this run: the block has
  6 elements and the run ends. Whether such end phases can be made long (a counter on a top block) is the k = 1 question in LOUD-SPLIT form.
### A4. Climbs on Q_(>1) at k = 1 (in progress at this commit; logs in the scratchpad)
- N 48 (seed 2, resumed from K1L7_n48's state): 7 deep loud steps (movers) unchanged from iteration 3,000 to 3,900 (T 37 → 38).
- N 84 (seed 4, from K1F34_n84, start 2): 150 iterations so far (≈ 5 s per evaluation at N 84), no gain yet.
- So far: 7 at N 48 against 2 at N 84; one local climb per size, nothing about growth in N (the Lead's trend request: next report).

## Addendum B (L-NEW successor 70; Lead 03:30Z: «Ruling: theory first. Freeze the N 48 best (Q_(>1) = 10) as Addendum B … Theory target: the top-block lemma»; written 2026-11-12 by date -u)
### B1. K1L10_n48 (frozen)
- inst/K1L10_n48.json (sha1 in inst/SHA1SUMS; k = 1): climb206.py seed 2 (CL_OBJ=loud) at 9,000 iterations, score (10, 4, 31); full log
  out/climb206_loud_s2.log (7 at iteration 3,000, 9 at 8,440, 10 at 8,829; still rising: search effort, not a trend in N).
- Scope all (out/depth206_K1L10.out): T 31, loud 28; by loud depth L-1 1, L0 16, L1 1, L2 3, L3 1, L4 6: Q_(>1) = 10; must-0 counters 0;
  DIV counters 0 (1,694 cases). Deep loud steps (out/deepdiag206_K1L10.out): steps 22-31 of 31, all at switching movers; steps 27-31 are
  p-steps (one mover switches, no gate flips), the propagation phase that BR-SEG (R118) bounds by N per p-run.
- Ascents: max over plays 4, loud depth max 4 (ascdepth206.py: ldfail 0 on this genome).
### B2. What the top block does (DATA; block206.py, out/block206.out; READING)
- Every k = 1 record except B400_r32 (levels 0-2) has two levels, 0 and 1 (MWR, K1F21, K1F34, K1C16, K1L7, K1L10). Level-0 gates take the β-face at every
  state (R118 LEVEL0), so E_t(x) is a set of level-1 e-vertices: the TOP BLOCK (b := the number of level-1 options). The whole class
  dynamics at fixed Λ is a lexicographically rising sequence of subsets of the top block.
- On K1L10 the top block has b = 6 elements (e-positions 96 … 91, gates of the level-1 movers 33, 32, 30, 31, 34, 46). Mover 47's block
  set over the run (bits = positions 96 … 91): ...... → ..1... → ..1.1. → .1..11 → .1.1.1 → .1.11. → .1.111 → 1....1 → 1.1... → 1.1.1.
  → 1.1.11 → 1.11.1 → 1.111. → 1.1111: 14 values, with counter-like resets (.1.111 → 1....1). It is a PARTIAL binary counter on the
  block: 14 of the 64 subsets at one mover, 19 over all movers.
- READING: this is the abstract chain system CS(b) of RESULTS R121 realised by a game: items = the b top-block e-vertices, next(g) = the
  first top-block e-vertex on the play of g's W-target (a level-0 mover), a mover's set = the chain from its first top-block e-vertex,
  ascents = steps of a chain to a more relevant item (here ≤ 4). R121's HUB-ASC bounds the values by F′_B(M) for B ascents; its tight
  B = 0 value is F_0(b) = 1 + b(b + 1)/2, and CS(4) with B = 1 already reaches 16 = 2^4 abstractly (R121 DATA: «B 1 max 16 at M 4»).
  So the abstract system allows full counters on the block; the question is whether IDEAL-CYC at k = 1 can drive one.
- CONJECTURE BLOCK-DESC (new, open; tested): at every mover x, the number Dtop(x) of distinct top-block sets over the run is at most
  F_0(b) = 1 + b(b + 1)/2, as if the chains had no ascents. With b ≤ M it bounds D_mov on two-level k = 1 genomes by (2M + 3)·F_0(M)
  (Λ-values per R121), hence T_CYC polynomial there (Theorem EQ, box 204). DATA (unit: max over movers of Dtop − F_0(b), «excess»;
  must be ≤ 0): K1F21 **0** (22 = F_0(6): on the bound), K1L7 −4 (18 vs 22), K1L10 −8 (14 vs 22), K1F34 −21, MWR8 −38, K1C16 −1,449,
  B400_r32 −10 (three levels; its top block is level 2, b 4, Dtop 1), MW8_2 (k = 2) −21, CT12 −22, WC8 −43; 1,000 random k = 1
  genomes (seed 70) and 1,000 rand191 genomes (seed 71): max excess −1 (at b = 2); pfall (block part falls at fixed Λ) 0 everywhere.
- **DEAD BLOCK-DESC** (killed by a climb): inst/BLKX23_n48.json (sha1 in inst/SHA1SUMS; k = 1 by
  fvs202; two levels; b = 6): Dtop = 23 > F_0(6) = 22 (out/block206_BLKX23.out; pfall 0). It is climb206.py CL_OBJ=block seed 8 from
  K1F21_n48 (excess 0) at iteration 41 (state at 75). IDEAL-CYC run: T 28; scope all: must-0 counters 0, maxdepth 3, loud depth ≤ 3
  (L0 21, L1 2, L2 2, L3 1).
- The witness is close to a pure BINARY COUNTER. Mover 47's top-block set (bits = e-positions 96 … 91), as integers: 0, 1, 2, 3, 4, 5,
  6, 7, 8, 9, 10, 11, 16, 17, 18, 19, 33, 34, 36, 40, 41, 42, 43 (23 values; movers 46 and 29 identical). The three low bits run a
  full count 0 → 7 and on to 11. So IDEAL-CYC at k = 1 does drive R121's chain system through a genuine counter on a top block of 6.
- READING (kill side, the sharpest lead this lane has at k = 1): if a family of two-level k = 1 genomes with b top-block options and
  N + M = poly(b) makes one mover count through 2^Ω(b) block sets, then D_mov − 1 ≤ T_CYC (box 204 Theorem EQ, left inequality) makes
  T_CYC exponential at k = 1. One instance at b = 6 says nothing asymptotic; it shows the mechanism exists. Next: read the counter's
  wiring off BLKX23 (which level-0 chains realise next(g) and the resets), and try to build the b-bit family by hand.
- Status of the Lead's target («inside one top-level block … counted by HUB-ASC (R121) or bounded by DEPTH-COUNT»): the block dynamics
  IS R121's chain system with ascents (B ≤ 4 on these runs), so HUB-ASC counts it with F′_B, polynomial for fixed B (no new lemma
  needed for that). Why the end phase stays short is NOT explained: the abstract system reaches 2^b; BLOCK-DESC states the observed
  sharper bound F_0(b), and a proof would need the game's Howard rule, not just E-MON.

## Addendum C (L-NEW successor 70; CORRECTION of Addendum B's READING, and the hand-built carry family; Lead 04:03Z: «GO with your default: a HAND-BUILT b-bit two-level k = 1 family … Measure Dtop, D_mov, T and N + M against b»; written 2026-11-12 by date -u)
### C1. Correction (governs Addendum B where they differ)
- Addendum B called BLKX23's sequence «close to a pure BINARY COUNTER». That is WRONG beyond 2 bits. Step trace (trace206.py,
  out/trace206_BLKX23.out; bits = the level-1 movers 33, 32, 31, 30, 34, 46, high to low): the two LOW bits (34, 46) count 00 → 11 by the
  race (R = mover 47 alternates R → Q = 46 and R → 34; v = 44 follows); the HIGH bits 30, 31, 32, 33 arrive ONE AT A TIME from the clock
  lane (lane movers switch X → next from the lane's end, one per step; each bit's Ξ-target is a lane node), each arrival resetting the
  low part. So 0 … 11 is {no high bit, 30, 31} × the 2-bit low counter: 12 = {30, 31} never occurs (11 → 16). The high part is one-hot,
  as in MW(n) (L-SI box 90's «R's tops are h_k, y, z, y»). The only multi-high-bit sets (steps 21-28) come from one nesting edge: bit 31's
  W-target chain 41 → 42 reaches bit 33.
- What stands: DEAD BLOCK-DESC (Dtop 23 > F_0(6) = 22; exact counts). The kill-side «binary counter» reading is withdrawn; with one-hot
  high bits Dtop is linear in b, and BLOCK-DESC fails only at small b (4b-type counts against 1 + b(b + 1)/2).
### C2. Hand-built carry family CW(n) (DATA; exact)
- Construction (carry206.py MWR.json OUT.json [PAR]; PAR = 0 used): from MWR(n) (box203/inst, L-RED 63's family), every high-bit mover
  qh_k (k < n) gets a new level-0 W-target c_k instead of the dead sink D; c_k's options have Ξ-targets qh_j (j > k) and X, new β ranks
  above all existing ones (even), new gate indices after all existing ones, start = the X option. No Ξ-edge enters c_k: k stays 1.
  Frozen: inst/CW4_n.json, CW8_n.json, CW16_n.json (sha1 in inst/SHA1SUMS).
- Measures (cwmeas206.py, out/cwmeas206.out; IDEAL-CYC from the start; Dtop = max over movers of distinct top-block sets; D_mov = max over
  movers of distinct classes (Λ, E); T = T_CYC):
  | genome | k | N + M | b | Dtop | D_mov | T |
  | --- | --- | --- | --- | --- | --- | --- |
  | MWR4_2 / MWR8_2 / MWR16_2 | 1 | 145 / 261 / 493 | 6 / 10 / 18 | 10 / 18 / 34 | 10 / 18 / 34 | 30 / 54 / 102 |
  | CW4_n / CW8_n / CW16_n | 1 | 157 / 303 / 643 | 6 / 10 / 18 | 12 / 38 / 92 | 12 / 38 / 92 | 30 / 59 / 114 |
  | BLKX23_n48 | 1 | 145 | 6 | 23 | 23 | 28 |
- Odd parity (PAR = 1) is weaker: CW4 Dtop 7, CW8 Dtop 11 (scratch runs, not frozen).
- Ascents (ascdepth206.py, out/ascdepth206_CW.out): max ascents per play 5 / 9 / 17 = b − 1; max loud depth 3 / 8 / 16; ldfail 0.
  [E-LEV] holds (gamma3's e-priorities by (level, gate)). So CW lies OUTSIDE HUB-ASC's fixed-B regime (B grows with b).
- READING: carries work locally (CW8's mover 46 reaches sets such as ..11111111 and .11....111), and D_mov grows faster than MWR's
  2n + 2 (about 3n, 4.75n, 5.75n at n = 4, 8, 16), but T stays linear and D_mov − 1 ≤ T_CYC (box 204 Theorem EQ): each step jumps many
  counter values. No 2^Ω(b) here. Growing ascents alone do not make runs long; a long k = 1 run would need carries that must be
  RE-ARMED step by step (a nested race), which CW does not have. Consistent with CONJECTURE DEEP-k1 (open).
