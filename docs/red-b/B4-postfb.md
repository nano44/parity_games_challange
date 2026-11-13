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
H_1); the climbed guides lengthen it to at most 37. PRE for the own guides: H_n 11, 33, 61, 95, 135 = 3n² + 13n − 5 exactly (n = 1..5).
