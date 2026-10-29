# N5-RANK (box 53): ranking-function synthesis for N5. Certified obstructions for four natural feature families, and no uniform form found
L-NEW successor 32 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 13:47Z, BOX 53: «RANKING-FUNCTION SYNTHESIS, from program
termination analysis (Podelski–Rybalchenko-style linear ranking functions; lexicographic and polyranking functions). Treat one N5 transition as a
program step. ... (a) A uniform form found on the corpus ...: then state it as a CONJECTURE with its range ... (b) The LP is infeasible on a named
instance for a natural feature family: that is a certified obstruction ("no linear ranking function over features F"), recorded with the instance.»
Literature: L-LIT T42 (claude/l-lit docs/lit/T42-ranking-functions.md, read 2026-10-29 ~14:10Z). It reports no prior application to strategy
iteration, and its §3 OPEN question is whether a ranking template over (rank, owner, edge) with polynomial coefficients exists.
This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Tools: experiments/new/box53/ (feat.py features, rlp.py LP search,
mkcert.py + cert.py exact certificates, revpair.py). LP: scipy 1.18.1 HiGHS (installed in this container; NOT needed by check.sh, which re-checks
the certificates in pure Python with integers).

## 0. Summary
- Setting. For a feature map f (integers of polynomial range) a LINEAR RANKING FUNCTION of a run is a c with c·(f(s_{t+1}) − f(s_t)) ≥ 1 at
  every transition. Read as a potential, −c·f decreases. If the coefficients are polynomial and the features have polynomial range, the run
  is polynomially long (T42 §3 (a), (b): a lexicographic function of depth d gives the product of d such ranges).
- Lemma CIRCUIT (PROVED, elementary; §1). If positive integers y_t on some transitions satisfy Σ_t y_t Δ_t = 0, then the run has NO linear and NO
  lexicographic-linear ranking function over f, of any depth and any coefficient size. The checker is exact (cert.py).
- Certified obstructions (DATA with exact certificates; §2). Each is a single game's own run, so per-game coefficients do not help:
  | family F | size | smallest certified instance (n, transitions) | circuit | corpus count (alt_all, 410 games) |
  | --- | --- | --- | --- | --- |
  | F24: aggregate valuation encodings (Ξ, W, Ξ_τ: cycle reward, signed rank-sum, signed count, signed top, ± rank-sums, oriented length) + |Iσ|, |Iτ|, |D| | 24 | red/xing/instances/u23sw64_n32 (32, 16) | 5 | 39 games |
  | F24m: rank moments Σ_r (r+1)^j N_r, j ≤ 4, per frame, + cycle / length sums + the 3 counts | 24 | n5-exhaustive/instances/b5_os_n16 (16, 26) | 8 | 36 games |
  | F45 = F24 ∪ F24m | 45 | red/n5inj/instances/returns_ph64 (64, 105) | 12 | 1 game |
  | EB: the (σ, τ) edge indicators [σ(v) = w], [τ(v) = w], i.e. the state itself (T42 §3's encoding) | m | n5-epoch/instances/lend9_n8 (8, 10) | **2** | 89 games (80 by a reverse pair) |
- EB is the strongest kill and the most elementary (Corollary REVERSE-PAIR, §1). If a vertex makes a switch a → b at one transition and the exact
  reverse b → a at a later one, with the same switch sets, then no linear function of the state encoding ranks the run. lend9_n8: vertex 3
  switches 6 → 7 at t = 2 and 7 → 6 at t = 5. So T42 §3's OPEN template class (λ over (rank, owner, edge), any coefficient size) is EMPTY on
  lend9_n8 and on 88 more library games. Edge templates are DEAD.
- Valuation aggregates cannot see the order. Every circuit of F24 / F24m / F45 consists of Ξ path-set changes (the W and Ξ_τ frames are mostly
  constant) where each polynomial-weight statistic moves both ways while Ξ rises in S1's top-rank-first order (§2.2). The order itself is
  linear in the per-rank counts N_r only with weights ±2^r (READING).
- Shared functions. No single linear ranking over F45 serves several games: the four n = 32 games si/xing/instances/zcl_{fb1, fb2, rx, tp}_n32
  give an exact 18-transition circuit. Joint lexicographic search over all of lib41 / alt_all gets STUCK at depth 3 / 4 with 3,666 / 4,518
  transitions left.
- Where ranking functions DO exist (DATA, §3). Per game, F45 is feasible on 409 of 410 alt_all games, 333 of 333 lib41 and 274 of 274 sicorpus
  games, and on every long scaling family: topfix_N to N = 12 (583 transitions ≫ 45 features), runquad_K8 (264), runfam_K100 (292), DLC_5,
  and the comparator graft topfix_12_cmp. F45 ∪ EB is feasible on all 410. But most corpus runs are no longer than the feature count, so
  feasibility there is OVERFITTING, not evidence. Only the long families are informative, and they are families already known to be
  quadratic or linear.
- Outcome against the brief. (b) obstructions: four, named and exactly certified. (a) uniform form: none. I state no CONJECTURE, since the
  only feasible uniform family (F45 ∪ EB, per game) has no test that is not overfit. READING (§4): with a fixed polynomial-weight feature
  family the true order (2^r weights) is out of reach on small instances already. With enough features to escape the circuits, the LP has
  more unknowns than the runs have transitions. The method cannot be decisive at the fleet's run lengths.

## 1. Lemma CIRCUIT and Corollary REVERSE-PAIR (PROVED, lane; elementary)
Let s_0, …, s_I be a run, f a map from states to Z^k, and Δ_t := f(s_{t+1}) − f(s_t).
Lemma CIRCUIT. Suppose there are a nonempty set U of transitions and integers y_t ≥ 1 (t ∈ U) with Σ_{t∈U} y_t Δ_t = 0. Then (i) there is no
c ∈ R^k with c·Δ_t ≥ 1 for all t (no linear ranking function over f), and (ii) there is no lexicographic-linear ranking function
⟨c_1, …, c_d⟩ over f of any depth d (each transition: c_1·Δ_t, …, c_{j−1}·Δ_t ≥ 0 and c_j·Δ_t ≥ 1 for some j, and every component
≥ 0 on the transitions not yet ranked; the ADFG / BG form of T42 entry 2, written for increase).
Proof. (i) Σ y_t (c·Δ_t) = c·Σ y_t Δ_t = 0, but every term is ≥ y_t > 0. (ii) Induction on the components. Every t ∈ U has c_1·Δ_t ≥ 0
(either = 0 or ≥ 1), and Σ y_t (c_1·Δ_t) = 0 with y_t > 0, so c_1·Δ_t = 0 on U. Then no t ∈ U is ranked by c_1, and the same argument
applies to c_2, and so on. So no t ∈ U is ever ranked. □ (This is Gordan's / Farkas' alternative, specialised.)
Corollary REVERSE-PAIR. With f = EB (the edge indicators [σ(v) = w] for Even v and [τ(v) = w] for Odd v, at vertices of out-degree ≥ 2), if
transitions t < t′ change exactly opposite sets of choices (the set of (v, old, new) at t′ is {(v, new, old) : (v, old, new) at t}), then
Δ_t + Δ_t′ = 0 and U = {t, t′}, y = (1, 1) is a circuit. So the run has no linear and no lexicographic-linear ranking function in the state
encoding. □
Exactness. Every certificate below has integer y and was re-checked by cert.py, which recomputes the run (n5x via common.rows), the features
(feat.py) and Σ y_t Δ_t in integers. A shifted control fails (check.sh "Box 53").

## 2. Certified obstructions (DATA; certificates experiments/new/box53/cert/*.json, 30 files)
### 2.1 How they were found
rlp.py mode uni1 solves, per game, min Σ|c| subject to c·Δ_t ≥ 1 (HiGHS, columns scaled). If it is infeasible, it solves max Σ y subject to
Σ y_t Δ_t = 0 with 0 ≤ y ≤ 1. It then shrinks the support to a minimal infeasible set (a circuit, kernel dimension 1) and solves that exactly
in rationals (rlp.cert_y). mkcert.py writes the compact certificate.
| run (log) | family | games | infeasible | smallest (n, transitions; circuit) |
| --- | --- | --- | --- | --- |
| uni1_altall.txt / uni1_lib41.txt | F24 | 410 / 333 | 39 / 26 | x31_cu24 (24, 22; 10); u23sw64_n32 (32, 16; 5) |
| mom_alt.txt / mom_lib41.txt | F24m | 410 / 333 | 36 / 18 | b5_os_n16 (16, 26; 8), b5_os_n20 (20, 34; 9) |
| both_alt.txt / both_lib41.txt / both_si.txt | F45 | 410 / 333 / 274 | 1 / 0 / 0 | returns_ph64 (64, 105; 12) |
| eb6_alt.txt | EB | 410 | 89 | lend9_n8 (8, 10; 2), b5_o11 (10, 12), b5_os_n12 (12, 18), s4c8_n13 (13, 12) |
| revpair_alt.txt (revpair.py) | EB, reverse pairs only | 413 | 80 | lend9_n8: vertex 3, 6 → 7 at t = 2, 7 → 6 at t = 5 |
| eb7_alt.txt | F45 ∪ EB | 410 | 0 | (overfit, §0) |
| zcl32 (joint, four games) | F45 shared | 4 (n 32) | circuit 18 | zcl_fb1, fb2, rx, tp _n32 |
| blex_lib41.txt / blex_alt.txt (joint lexicographic) | F45 shared | 7,397 / 10,224 transitions | STUCK at depth 3 / 4 | 3,666 / 4,518 left |
- Lexicographic per game: F24 on u23sw64_n32 and x31_cu24 is STUCK at depth 2. F45 on returns_ph64 is STUCK at depth 2 (80 of 105 left), as
  Lemma CIRCUIT (ii) predicts.
### 2.2 What the circuits look like (READING)
- returns_ph64's 12-circuit (transitions 8, 12, 18, 45, 49, 51, 61, 62, 64, 70, 74, 84): on every one the W-frame change equals the Ξ-frame change,
  or nearly (D is mostly empty), and Ξ_τ does not change. ps, pc, pp, pn and the moments m0-m4 move in both directions across the circuit (for
  example X_ps −33 at t = 8 and +1000 at t = 51; X_m4 +86,126,853 at t = 8 and −542,632,730 at t = 18). Ξ rises at each of them in S1's order,
  in which the top differing rank decides. A polynomial reweighting of ranks cannot reproduce that order on these runs.
- u23sw64_n32's 5-circuit (t = 3, 4, 5, 7, 8) involves only Ξ path sets and |Iσ|: X_ps +36, −556, −109, +59, +12 with weights
  33,875 : 13,895 : 37,988 : 86,120 : 463,811.

## 3. DATA where ranking functions exist (rlp.py uni1, FAM = 5; logs both_long.txt, uni1_famL.txt, famL / fam)
| run | transitions | F45 linear ranking | note |
| --- | --- | --- | --- |
| topfix_8, _10, _12 (R109 family; box52/out) | 291, 425, 583 | FEASIBLE | largest coefficients on the cycle rewards X_cr, W_cr and on W_tp (LP values 0.001-0.07) |
| topfix_12_cmp (comparator graft, box 52) | 583 | FEASIBLE | |
| runquad_K8_m30_n192 (R106) | 264 | FEASIBLE | X_ps, W_ps, W_tp only |
| runfam_K100 (L-SI RUN-LIN killer) | 292 | FEASIBLE | X_cr, X_tp, W_ps, W_ln, nIs |
| dlc_d5 (box 51) | 63 | FEASIBLE | integer c: X_ln −1, nIs −2 |
| F24 alone: runquad_K3, hntop_n3, dlc_d3 / d4, topfix_3_cmp, duals of dlc_d3 and hntop_n3, runfam_K10 (fam) | 15-100 | FEASIBLE | e.g. runquad_K3: W_cr alone (every transition changes λ_W, L-SI box 29) |
- The long families are ranked by one or two cycle-reward / top features. That is the CN-W / TOP-SHAPE mechanism (L-SI box 29; RESULTS R84),
  and those quantities are already polynomially bounded. The runs that defeat the aggregates are short library runs whose Ξ path sets change
  under a fixed top, the part TOP-SHAPE leaves open (R84: «NOT the P-changes under a fixed top»).

## 4. READING: what this says about the method
- Necessary content. A polynomial bound for N5 needs, per game, SOME ranking function with polynomial range (T42 §3). Lemma CIRCUIT shows that
  for each fixed polynomial-size feature family tried here there are library games with none. The EB kill is unconditional on coefficients:
  the state encoding with any weights is not a ranking function on lend9_n8, because N5 makes a switch and later its exact reverse.
- Overfitting. With per-vertex, per-rank or EB ∪ valuation features the number of unknowns (21n, 3n, m + 45) is at least the run lengths seen
  in the library (≤ 3n, and ≤ 3N² on n = 21N for topfix). So every such LP is feasible for a trivial reason, and its feasibility says nothing.
  A family of runs longer than its feature count by a growing factor would be needed. The only such families known are ranked by the already
  bounded cycle / top features (§3).
- So ranking-function synthesis, as a method, reduces here to the same open quantity as boxes 51 and 52: Ξ path-set changes under a fixed
  top. Its useful product is the certificate format (Lemma CIRCUIT). Any future candidate potential written as a linear form in polynomially
  bounded features can be refuted or confirmed per game by an exact LP, and cert.py checks the refutations without an LP library.

## 5. Dead ends (also in notes/L-NEW.md)
- Linear / lexicographic ranking over F24: DEAD on u23sw64_n32 (circuit 5; cert/f0_u23sw64_n32.json). Over F24m: DEAD on b5_os_n16 (circuit 8;
  cert/f4_b5_os_n16.json). Over F45: DEAD on returns_ph64 (circuit 12; cert/f5_returns_ph64.json). Over the edge indicators (any template over
  (rank, owner, edge)): DEAD on lend9_n8 (reverse pair, circuit 2; cert/f6_lend9_n8.json). A shared F45 function across games: DEAD on four
  zcl n32 games (circuit 18). Obstruction: S1's top-rank-first order is not a polynomial-weight linear form on path-set statistics, and N5
  makes exact reverse switches.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box53/ (feat.py, rlp.py, mkcert.py, cert.py, revpair.py; logs *.txt; 30 certificates cert/*.json);
  check.sh block "Box 53" (four pinned certificates re-checked exactly + a corrupted-certificate control).
- FINDINGS: (1) PROVED (lane) Lemma CIRCUIT and Corollary REVERSE-PAIR. (2) DATA, exact certificates: no linear / lexicographic ranking
  function over F24 (u23sw64_n32), F24m (b5_os_n16), F45 (returns_ph64) or the edge indicators (lend9_n8, n 8; 89 of 410 library games), and
  no shared F45 function across zcl n32. (3) F45 ranks every long scaling family, through the already bounded cycle / top features.
  (4) READING: no uniform form, so no CONJECTURE. Richer families are overfit at library run lengths. The open core is again Ξ path-set
  changes under a fixed top.
- NEEDS: none from the owner.
