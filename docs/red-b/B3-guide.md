# B3: GUIDE-RULE, a kill attempt on N5 itself (L-RED-B successor 3) — DATA and one claim; NO KILL found
Written 2026-11-13 (date -u in the commit). Brief (Lead): climb N5's iteration count over guided wrappers Wg(H, s0, ρ0) and variants
whose frozen faces disagree with Odd's true reply; score = iterations / |V| and growth over a family; every best on a second engine +
Zielonka, frozen with sha1; a family with clearly super-polynomial growth on two engines goes to the Lead as a CANDIDATE KILL.
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» LABEL: everything below is DATA or an L-RED-B reading; nothing is proved
or signed; G-N5-TIME stays OPEN; no statement about N5's running time follows from a climb that found nothing.

## 1. What is run (SPEC lines quoted)
N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (trunk 7fa6aff4, file sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e), as implemented by
L-NEW's experiments/new/box190/n5v.py mode «spec» (claude/l-new 069c888b, via git archive; n5v's header: «mode "spec": N5 (box21
n5x.step)»). The lines that decide the reading of §3:
- l. 51-53, S4a: «If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps
  only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an
  Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- l. 40-42 and 44, S1 (iv): «Lengths: if Ω(v) even, Odd takes the LONGEST path to v in the restricted graph (recursion over
  successors in list order, first strict maximum wins); if Ω(v) odd, the SHORTEST (BFS from v over predecessors in list order; first
  discovery sets Odd's choice).» … «Successor and predecessor lists are in increasing index order.»
- l. 48, S3 (the start), l. 56, S4c (the fallback).
Wrappers: L-SI's experiments/si/box104/wrap104.py (W, flat) and gscan104.py (Wg, guided, with face targets γ and frozen Odd faces ρ0
that may lead to a non-successor), claude/l-si 2051a0ee via git archive. Correctness of every run: N5's output regions = harness
Zielonka on the wrapper (inside gscan104.run). Second engine: L-COMP's experiments/n5-second/n5b.py --mode spec (trunk 7fa6aff4).
Families: PGSolver switchallexp_n (L-NEW's hard-families/pgsolver_port.py), Friedmann's H_n (L-COMP's experiments/friedmann-hn/hn.py
mode fig, iota; claude/l-comp aa863db5), LMCS G_n (arXiv 1106.0778v2 Figure 4 priorities, L-LIT's transcription claude/l-lit 5c53efbd
docs/lit/T66-depth-check.py). I did not open arXiv 1106.0778 myself; the generators are other lanes' transcriptions.

## 2. Results (DATA). Every number is the best N5 iteration count a hill climb found, i.e. a LOWER bound on the maximum over the
guides searched; budgets are per row («steps» = candidate guides evaluated; one start per row; «restarts» = independent seeds).
### 2.1 H fixed (a family member), guide climbed (gfam.py: s0, ρ0 (half the moves send a face to ANY vertex of H, so it may disagree
with Odd's true reply), γ (the fixed face of an Even edge may lead to any vertex); start = the family's own start, ρ0 = Odd's optimal
counterstrategy to it in H, γ = ∅). Correct output on every candidate (0 wrong). Columns: n, |H|, |Wg|, best iterations (first
fallback), steps × restarts.
| family | n = | best iterations (first fallback) | |Wg| | budget |
| --- | --- | --- | --- | --- |
| switchallexp_n | 2, 3, 4, 5, 6 | 23 (10), 25 (12), 33 (13), 36 (16), 39 (16) | 736, 1063, 1390, 1717, 2044 | 600 steps × 2 restarts each |
| H_n (Friedmann §8.4, L-COMP hn.py) | 1, 2, 3, 4, 5 | 21 (16), 41 (35), 80 (55), 102 (97), 152 (115) | 404, 899, 1457, 2078, 2762 | 400 steps × 1 restart each |
| H_n, longer | 2 | 44 (38) | 899 | 1,500 steps × 1 (another seed) |
| H_n, longer | 3 | running at the commit (72 after 645 steps); reported in an addendum | 1457 | 1,500 steps × 1 (another seed) |
| LMCS G_n (Fig. 4 priorities) | 2, 3, 4, 5, 6 | 18 (10), 21 (13), 23 (9), 22 (14), 31 (17) | 516, 785, 1081, 1404, 1754 | 400 steps × 1 restart each |
Howard on switchallexp_n itself (guide104's own count): T = 30, 70, 150 for n = 2, 3, 4; L-SI's gscan104 on H_n: 14, 36, 64, 98 (n = 1..4).
Growth words (the Lead's rule: a fit, or «not identified»). Least squares on the five counts per family (model, coefficients,
residuals, n range):
- switchallexp, n = 2..6: linear 4.3 n + 14.0, residuals 0.4, −1.9, 1.8, 0.5, −0.8 (RSS 7.9); exponential 17.31 · 1.153^n, RSS 11.4.
- H_n, n = 1..5: quadratic 3.07 n² + 13.87 n + 3.8, residuals 0.3, −2.8, 6.9, −6.4, 2.1 (RSS 101.8); linear RSS 233.9; exponential
  14.83 · 1.627^n, residuals −3.1, 1.7, 16.1, −2.0, −17.3 (RSS 575.3).
- LMCS G_n, n = 2..6: linear 2.7 n + 12.2 (RSS 21.1); quadratic RSS 15.3; exponential 14.38 · 1.120^n (RSS 18.8).
Five climb lower bounds per family do not identify a growth law: GROWTH NOT IDENTIFIED for all three families; among the three models
the exponential fits worst for H_n and the polynomial ones are no worse elsewhere. Nothing here is clearly super-polynomial, so no
CANDIDATE KILL is sent.
### 2.2 H random (gclimb.py: random H with |H| = n, s0, ρ0, γ all mutated; 2,000 steps × 1 restart per row)
best iterations: |H| 6: 10, 11; 8: 13, 14 (faces copied) and 10 (copy = 0), 12 (score iterations/|Wg|); 10: 15, 16; 12: 11, 13 (and
13 with copy = 0, 13 by iterations/|Wg|); 16: 16, 11. GROWTH NOT IDENTIFIED (flat within noise). 0 wrong outputs.
### 2.3 Second engine
gverify.py re-runs every best of 2.1 and two of 2.2 on L-COMP's n5b --mode spec (its own best-reward start = S3) and records the
wrapper's sha1 (data/b3/gverify_all.out): 22 wrappers (all 21 gfam bests incl. both switchallexp seeds, plus gclimb |H| 10 and
16): n5b's iterations and fallbacks EQUAL n5v's on 22 / 22; N5's output correct (Zielonka) on 22 / 22. The .pg files are not committed
(regenerate with gverify.py from the state files in data/b3/; each sha1 is in the output line).

## 3. Claim FLAT-IDX (L-RED-B reading, NOT PROVED; a candidate for L-NEW, with a proof sketch and a direct test)
**AMENDED WORDING (after R240, §3a; this replaces the claim below, which is kept as history):** On W(H, s0), before N5's first fallback
and while τ is standard at the gates, σ_(j+1)(v) = the element of {σ_j(v)} ∪ Iσ_j(v) with the least ROOT-FIRST KEY (index of its pe,
then of its gate, then of its pad); with wrap104.py's numbering (the pads of v's edges created in H.succ[v] order) this is the least
position in H.succ[v]. Keys (in wrap104's numbering: positions) never increase, so at most Σ_v (deg(v) − 1) ≤ |E(H)| iterations move
H before the first fallback; this |E(H)| bound is the part that holds under EVERY numbering of the new vertices. The key form is not
new: it is WRAP Remark (3) / R104 [RULE] (per R240 §3; I had not read WRAP's remarks when writing the sketch).
History (the wording of 9bce72fa):
Setting: W = W(H, s0) of wrap104.py for any parity game H and Even strategy s0; N5 (SPEC) from S3 on W.
Claim. At every iteration j before the first fallback at which τ_j is standard at every gate (τ_j(g) = pe_g), and for every Even vertex
v of H: σ_(j+1)(v) = the option of least position in H.succ[v] among {σ_j(v)} ∪ Iσ_j(v). Hence the position of σ(v) never increases
before the first fallback (while τ is standard at the gates), and the number of such iterations that change σ at some Even vertex of H
is at most Σ_v (deg_H(v) − 1) ≤ |E(H)|.
Proof sketch (from the SPEC lines of §1 and wrap104.py's construction; not checked by a referee):
(1) In S4a's arena, an Even vertex v of H keeps only its options in A(v); each option is v → m_(v,w) → g_(v,w) → pe_(v,w) → c_W
    (the gate is Odd and keeps only τ(g) = pe_g; pe is a pad). So every play from v in the arena is v → m → g → pe → c_W → c_W …:
    the same cycle node c_W, the same set P (nothing on the path is above c_W, the top even priority below the core), length 4.
    Every option of v has the same arena value: S4a's choice is decided by the tie rule of S1 alone.
(2) σ_new is computed on the DUAL of the arena, where c_W has priority top + 1, odd. v reaches no other cycle in the arena, so v is
    valued when c_W is processed, and S1 (iv)'s odd branch applies: BFS from c_W over predecessors in increasing index order; the
    first discovery sets v's choice.
(3) BFS layers: c_W's predecessors are the pads pe (gates' and Odd vertices') in index order; then each gate g (its only arena edge
    is to pe_g); then each m-pad; then v, discovered first through the m-pad whose pe_(v,w) came first, i.e. the option in A(v)
    with the least pe index. wrap104.py creates the pads of v's edges in the order of H.succ[v] (sorted), so pe index order = position
    order in H.succ[v]. Hence σ_new(v) = the least-position option of A(v) = {σ_j(v)} ∪ Iσ_j(v).
(4) σ_new(v) ≠ σ_j(v) only if a strictly smaller position exists in A(v); positions never increase; each v changes at most
    deg(v) − 1 times. An iteration that moves some Even vertex of H uses up at least one of these changes.
What it does NOT say: anything after the first fallback; anything when τ leaves the standard faces before the fallback (not seen in
DATA: counter taunstd); anything about the guided Wg (there the arena values differ: a gate's τ-face leads back into H); the total
iteration count (iterations that move only valves, core or τ are not counted by (4); in DATA they do not occur before the fallback).
### 3a. R240 (L-RED successor 68, claude/l-red 50fe432a docs/red/R240-flatidx.md; read 2026-11-13 after its verdict)
R240 attacked the claim as the Lead stated it (it could not read this sketch: 9bce72fa was not yet on origin). Verdict: DEPENDS ON
NUMBERING. With wrap104's numbering «least position / never increases» SURVIVES (notmin 0, idxinc 0 on 2,211 games); with the pe's
renumbered, which W's definition («the new vertices are indexed after V») allows, it FAILS (PERM pe: notmin 1,947, idxinc 1,072; 42
frozen instances, n5v agrees); the numbering-free form «least root-first key» SURVIVES under all six numberings (keymin 0 on 13,266
games); hbound and taunstd are 0 under every numbering. My reading of R240: it agrees with step (3) of my sketch, which already derives
«position» from wrap104's creation order; the claim's first sentence should have said so. The wording is amended above. My own DATA
below uses wrap104's numbering only and is unchanged.
Direct test (wflat.py): counters idxinc, notmin (unit (iteration, Even vertex of H) before the first fallback),
hbound (game), taunstd (iteration); CONTROL: N5′-xi (ALG=xi, Howard's best-value tie rule) must fire idxinc / notmin.
DATA of the direct test (data/b3/wflat_*.out; N5 = n5v spec, N5′-xi = n5v xi; unit of idxinc / notmin: (iteration, Even vertex
of H) before the first fallback):
| set | games | idxinc | notmin | hbound | taunstd | notes |
| --- | --- | --- | --- | --- | --- | --- |
| N5, random H (harness gen.random_game, |H| 2..10, seed 11) | 3,000 | 0 | 0 | 0 | 0 | 1,337 games with an H-move; max 3 H-move iterations; 122 games meet the bound exactly |
| N5, random H (|H| 2..30, seed 12) | 1,000 | 0 | 0 | 0 | 0 | 738 games with an H-move; max 3 |
| N5, switchallexp n = 2..8 | 7 | 0 | 0 | 0 | 0 | H-move iterations 0..6 (bound 38..152) |
| N5, LMCS G_n n = 2..8 | 7 | 0 | 0 | 0 | 0 | 3 each |
| N5, H_n n = 1..6 | 6 | 0 | 0 | 0 | 0 | 1 each |
| CONTROL N5′-xi, random (seed 11) | 3,000 | 2,266 (1,410 games) | 2,435 | 0 | 0 | fires |
| CONTROL N5′-xi, switchallexp n = 2..6 | 5 | 5,550 | 5,952 | 4 games | 0 | Howard: 30, 70, 150, 310, 630 H-move iterations > the bound 57..114 for n ≥ 3 |
So on the flat wrapper N5 takes at most Σ(deg − 1) H-moves before its first fallback (as the claim says) where N5′-xi takes Howard's
exponentially many; the claim explains why: SPEC's S1 (iv) BFS tie rule, not the values, chooses N5's step there.

## 4. Verdict on B3 so far, scope, next
- NO CANDIDATE KILL. No family with clearly super-polynomial growth was found; growth NOT IDENTIFIED from five lower bounds per family.
- FLAT-IDX (§3) is an L-RED-B reading with a proof sketch and a direct test (0 on 4,020 N5 runs; the control fires); not proved; the
  Lead routes it (L41).
- Scope: N5 (SPEC, n5v spec mode; n5b agrees on the bests) from S3 on L-SI's wrappers of three families and of small random games.
  Not M4, not a statement about N5's running time; G-N5-TIME stays OPEN.
- Not done: guides on families other than these three; climbs longer than 1,500 steps; targeted constructions (the climbs mutate
  blindly); the phase after the first fallback is where most extra iterations of the bests sit (e.g. H_3: 80 iterations, first fallback
  55) and is not analysed.

## 5. Sources opened
trunk 7fa6aff4 docs/new/N5-ssi-global.md (SPEC, l. 23-62, read in full); claude/l-si 2051a0ee experiments/si/box104/wrap104.py (header,
wrap, check, howard), guide104.py, gscan104.py (read in full) and out/gscan104.out; claude/l-new 069c888b experiments/new/box190/n5v.py
(header, step, run). Not opened: arXiv 1106.0778 (the families are other lanes' transcriptions), L-SI's box 104 map and reports.

## 6. Reproduction
experiments/red-b: build B3ROOT = work/b3 by git archive as in gclimb.py's header (plus claude/l-lit 5c53efbd docs/lit/T66-depth-check.py
-> work/b3/llit, claude/l-comp aa863db5 experiments/friedmann-hn -> work/b3/lcomp, trunk 7fa6aff4 experiments/n5-second/n5b.py,
hard-families, harness -> work/b3/trunk); then run_b3.sh work/b3 climbs | fam | fam2, run_b3b.sh work/b3, run_wflat.sh work/b3,
gverify.py work/b3 OUTDIR STATEFILES. Outputs and the climbs' final state files (the guides) are in data/b3/, pinned in data/SHA1SUMS.

## Addendum A (2026-11-13, L-RED-B successor 3): longer H_n climbs (budget check)
- H_2, 1,500 steps × 1 (seed 5002): best 44 (first fallback 38), vs 41 at 400 steps (seed 2021).
- H_3, 1,500 steps × 1 (seed 5003): best 73 (first fallback 47), vs 80 at 400 steps (seed 2031): the longer climb from another seed did
  NOT beat the shorter one; the counts are seed-limited as much as budget-limited.
- H_4, 1,500 steps × 1 (seed 5004): PARTIAL at this commit: best 101 (first fallback 97) after 481 steps (vs 102 at 400 steps, seed
  2041); the final value goes into the B4 report.
- The family members' OWN guides (start iota, ρ0 = Odd's optimal counterstrategy, γ = ∅; docs/red-b/B4-postfb.md DATA, b4phase.py,
  both engines): H_n, n = 1..5: N5 iterations 14, 37, 65, 99, 139 with one fallback each at iteration 12, 34, 62, 96, 136. The
  iterations before the first fallback (11, 33, 61, 95, 135) equal 3n² + 13n − 5 at n = 1..5 (DATA; a 3-parameter fit to 5 points
  with zero residuals, not a formula for H_n's run until n ≥ 6 agrees or it is proved). This matches the proxy count 3n² + 13n − 5 that successor 2 reported for H_n (Lead's relay; not DATA of
  mine before this). switchallexp n = 2..6: 10, 10, 12, 14, 16 (equal 2n + 4 at n = 3..6, DATA only); LMCS n = 2..6: 8, 9, 11, 13, 15 (equal 2n + 3 at n = 3..6,
  DATA only). (Corrected in the commit after d889e559, which printed «both: 2n + 4».)
