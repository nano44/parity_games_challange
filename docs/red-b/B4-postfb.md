# B4: POST-FALLBACK, a kill attempt on N5 after its first fallback (L-RED-B successor 3) — STATEMENT (written before any long run)
Written 2026-11-13 (date -u in the commit). Routed by the Lead (02:15Z): «most extra iterations in the bests sit after the first
fallback. That phase is outside every current reduction: box 212 RF-D covers N5 only before its first fallback.» D1 (owner,
verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
own, as wrong until it passes the gauntlet below.» LABEL: a plan and its counters; no result yet; G-N5-TIME stays OPEN.

## 1. Objects
- N5 = SPEC S1-S5 (trunk docs/new/N5-ssi-global.md, sha1 66fde9ef…; the lines quoted in docs/red-b/B3-guide.md §1), engine 1 = L-NEW's
  box190/n5v.py mode spec (claude/l-new 069c888b), engine 2 = L-COMP's experiments/n5-second/n5b.py --mode spec (trunk 7fa6aff4), both
  via git archive. A FALLBACK is an iteration that takes SPEC S4c (l. 56); n5v reports it per iteration (flag fb of n5v.step).
- Games: L-SI's guided wrappers Wg(H, s0, ρ0, γ) (gscan104.wrapg, claude/l-si 2051a0ee) of the B3 families (switchallexp_n, H_n, LMCS
  G_n) and of small random H, with the guides of B3 (data/b3/ state files) and new ones.

## 2. What is measured
(a) PHASES. For a run with iterations 1..I and fallback iterations f_1 < … < f_k (k ≥ 0): PRE = f_1 − 1 (iterations before the first
    fallback; I if k = 0), BETWEEN = Σ_i (f_(i+1) − f_i − 1) (non-fallback iterations between fallbacks), POST = I − f_k (iterations
    after the last fallback, the fallback itself not counted), and k. So I = PRE + BETWEEN + POST + k. Computed by engine 1 per
    iteration; engine 2 reports I and k only.
    Table for every B3 best (22 wrappers of data/b3/gverify_all.out) and for every family member n with its own start and ρ0 = Odd's
    optimal counterstrategy, γ = ∅ (no climb).
(b) CLIMB on the post-first-fallback count P1 := I − f_1 = BETWEEN + POST + (k − 1) (every iteration after f_1; 0 if k = 0), same machinery as
    B3 (gfam.py moves on s0, ρ0, γ; H fixed per family member; and gclimb.py moves on random H), objective P1, ties broken by smaller
    |Wg|; budgets named per row.
(c) MUST-0 COUNTERS (each per run): wrong (N5's output regions ≠ harness Zielonka on Wg), engdiff (n5v's (I, k) ≠ n5b's (I, k)),
    phasesum (I ≠ PRE + BETWEEN + POST + k: a bookkeeping check). CONTROL for engdiff: n5v in mode xi (N5′-xi) against n5b spec must
    differ on some wrapper (B2/B3 DATA: they differ, e.g. K1F21_n48 on Γ3: 34 vs 6).
(d) Growth words only with a stated fit (model, coefficients, residuals, n range); otherwise «growth not identified».
## 3. Kill criterion (the Lead's, verbatim in substance)
A family whose POST-first-fallback count P1 grows super-polynomially in |Wg|, checked on both engines (I and k equal), every output
correct, each best frozen with its sha1: it goes to the Lead at once as a CANDIDATE KILL, before anything else, nothing more.
## 4. Not claimed
Nothing about N5 before its first fallback (B3, box 212 RF-D), M4 or general games; a climb that finds nothing proves nothing.

## 5. DATA (a): phases (data/b4/b4phase_*.out; b4phase.py; engine 1 n5v, engine 2 n5b; 2026-11-13)
| set | wrappers | k (fallbacks) | BETWEEN | POST = P1 | wrong | engdiff | phasesum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B3 bests (21 gfam + 2 gclimb; b4phase_bests_spec.out) | 23 | 1 on all 23 | 0 | 5..37 (H_5 best: 37; switchallexp n = 2..6 bests: 13/14, 10/13, 14/20, 20/14, 17/23; LMCS 8, 8, 14, 8, 14) | 0 | 0 | 0 |
| own guides, switchallexp n = 2..6 | 5 | 1 | 0 | 3, 3, 3, 3, 3 | 0 | 0 | 0 |
| own guides, LMCS G_n n = 2..6 | 5 | 1 | 0 | 3, 3, 3, 3, 3 | 0 | 0 | 0 |
| own guides, H_n n = 1..5 | 5 | 1 | 0 | 2, 3, 3, 3, 3 | 0 | 0 | 0 |
| CONTROL n5v mode xi vs n5b spec (fried and LMCS bests; b4phase_ctrl_xi.out) | 15 | 1 | 0 | — | 0 | 2 (fires) | 0 |
Reading: on every wrapper so far N5 has exactly ONE fallback; with the families' own guides the run after it is 3 iterations (2 for
H_1); the climbed guides lengthen it to at most 37. PRE for the own guides: H_n 11, 33, 61, 95, 135, equal to 3n² + 13n − 5 at n = 1..5 (DATA; not a formula
for H_n's run until n ≥ 6 agrees or it is proved). The table counts 38 wrappers (23 bests + 15 own guides).

## 6. DATA (b): the climb on P1, and the own guides at larger n (2026-11-13)
Climb (b4climb.py, run_b4.sh): objective P1 = I − f_1 (ties by I), moves on s0 / ρ0 (any vertex) / γ as in B3, H fixed, start = the
family's own guide; budget 400 steps × 1 restart per row. Bests re-run on both engines (data/b4/b4phase_climbs_spec.out, sha1 of each
wrapper there):
| family | n = | best P1 (I, PRE) | |Wg| |
| --- | --- | --- | --- |
| switchallexp_n | 2, 3, 4, 5, 6 | 19 (23, 3), 14 (18, 3), 15 (28, 12), 20 (33, 12), 24 (31, 6) | 736 … 2044 |
| LMCS G_n | 2, 3, 4, 5, 6 | 10 (17, 6), 14 (22, 7), 16 (26, 9), 18 (21, 2), 19 (25, 5) | 516 … 1754 |
| H_n | 1, 2, 3, 4 | 12 (21, 8), 18 (29, 10), 30 (37, 6), 33 (74, 40) | 404 … 2078 |
On all 14 bests: k = 1 (one fallback, BETWEEN = 0), wrong 0, engdiff 0, phasesum 0. Climb candidates: 0 wrong outputs.
Growth words: GROWTH NOT IDENTIFIED (P1 per family from 400-step climbs: switchallexp 19, 14, 15, 20, 24; LMCS 10, 14, 16, 18, 19;
H_n 12, 18, 30, 33; none of these is a fit). Nothing clearly super-polynomial: NO CANDIDATE KILL.
Own guides at larger n (run_b4own.sh; both engines, all correct, k = 1, POST = 3 on every one):
- H_n, n = 6, 7: I = 185, 237; PRE = 181, 233. The DATA «PRE equals 3n² + 13n − 5 at n = 1..5» now also agrees at n = 6, 7 (181, 233):
  DATA on n = 1..7, still not a formula (not proved).
- switchallexp n = 7..10: I = 18, 20, 22, 24 (equal 2n + 4 at n = 3..10, DATA); LMCS n = 7..10: I = 17, 19, 21, 23 (equal 2n + 3 at
  n = 3..10, DATA).
Reading (L-RED-B, not proved): on these wrappers the phase after N5's only fallback is short and does not grow with n under the own
guides (3 iterations at every n tried); the guide climbs lengthen it to a few dozen at most. The kill criterion of §3 is not met.
## 7. Verdict on B4 (so far), not done
- NO CANDIDATE KILL; on 62 wrappers (23 B3 bests, 14 B4 bests, 25 own guides) N5 has exactly one fallback; the phase after it is
  2..37 iterations; both engines agree on every one and every output is correct.
- Not done: guides that force a SECOND fallback (none found: k = 1 everywhere, so BETWEEN and the run after a later fallback were never
  exercised); other families; climbs longer than 400 steps on P1; any proof about the post-fallback phase.
