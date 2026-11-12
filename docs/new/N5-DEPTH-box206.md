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
