# N5-SF (box 54): a single-frame N5. Correct, reduces to one open count (Odd's best-reply changes SBC); its W-frame twin cycles
L-NEW successor 32 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 14:24Z, BOX 54: «Define a SINGLE-FRAME variant, N5-SF: the
same as N5, except that the Even step chooses within the arena by Ξ (or the arena is defined by W). Pick the variant that keeps N5's correctness
argument and say why. Then: (1) Termination and correctness ... (2) The per-phase bound ... (3) DATA ... The decisive question is whether the cost
moves from per-phase length into the number of phases, and how fast that grows. Any polynomial claim about N5-SF is wrong until it passes
TARGET.md §5's gauntlet.»
This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. N5-SF has NOT been through the gauntlet. G-N5-TIME
(about N5) is untouched. Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD.
Tools: experiments/new/box54/ (n5sf.py the variant, MODE=w the W-frame twin; sfrun.py N5-SF vs N5 with checks; hf.sh the hard families;
mkdual.py dual mirrors). Logs: box54/sf_*.txt, sfw_*.txt. Engine: N5 via common.rows (n5x).

## 0. Summary
- The variant (§1). N5-SF := SPEC S1-S5 with S4a's opponent τ replaced by Odd's BEST REPLY σ̄ = σ̄(σ), and S4b's opponent σ replaced by τ̄
  (Even's best reply to τ on G^d). So the arena (Ξ-improving edges, S2) and the choice (an optimum in that arena) are taken in the SAME frame,
  the one-player game G_σ̄. The W-frame twin N5-SFW (arena = W-improving edges against τ, choice against τ) does not keep the correctness
  argument, and it CYCLES (DEAD: red/n5inj/instances/theta_thf16, period 10; 49 of 413 library games).
- (1) PROVED (lane). N5-SF terminates and is correct for the same reason as N5 (R15 (c), (d) verbatim; Lemma SF-TERM). The S4c fallback is still
  needed: my Lemma NOFB, claiming it never fires, is FALSE (n5-exhaustive n3all_maxph_0, §2). Lemma DECOUPLE: the sequence of DISTINCT σ values
  of N5-SF depends on σ_0 alone, and that of τ on τ_0 alone. So τ plays no role in Even's run (only in the stall timing).
- (2) PROVED (lane), Theorem SF-RED: a maximal stretch of Even's run on which σ̄ and λ_Ξ are constant is N5's run on the ONE-PLAYER game G_σ̄
  inside one λ-phase, so it has fewer than n + m σ-changes (RESULTS R17 (b), (c), applied as in L-SI's Corollary FW-D0). Hence
  #σ-changes < (n + m)·(1 + LAM + SBC_σ), with LAM ≤ n(n − 1) λ_Ξ-changes and SBC_σ the σ-changes at which σ̄ changes. The same holds for τ.
  So N5-SF is polynomial IFF SBC (Odd's best-reply changes along Even's run, and the mirror) is polynomial. That is the ONE open count.
- (3) DATA (§3). Correct everywhere: 413 + 349 + 276 library games, 20 family runs and 59 hard-family runs; 0 region errors, 0 cycles.
  - SF is shorter than N5 in aggregate: alt_all 5,302 vs 10,224 iterations, lib41 3,735 vs 7,397, sicorpus 3,544 vs 6,737.
  - It erases N5's quadratic families: runquad / s3quad 264 → 2; topfix_N 3N² + 13N − 5 → 7N + 43 (N = 3..10); runfam_K40 172 → 39.
  - It is WORSE than N5 on Friedmann's switchbestexp: 20, 58, 135, 258, 364, 412, 456, 489, 577, 619 at N = 1..10 (n = 25N + 10), against N5's
    20..89, with SBC 1, 4, 11, 26, 49, 56, 60, 75, 92, 97. The growth is steep up to N = 4, then about linear in N.
  - SBC ≤ 1.17n on the library, ≤ 0.37n on switchbestexp at N = 10, and ≤ 16 on every hard family.
- Answer to the decisive question. Yes, the cost moves: inside a (σ̄, λ)-segment the length is R17-bounded (DATA max 0.94n), and the run is
  #segments × that. On the library and on N5's hard families the number of segments stays ≤ 1.2n. On switchbestexp it grows about linearly
  in N after a steep start. CONJECTURE SF-POLY (SBC polynomial) is OPEN. Its natural kill target is Friedmann-type switch-best families,
  where SF's counts (20, 58, 135, 258) track PGSolver's switch-best (23, 61, 137, 289) for N = 1..4 and then fall away. I did not run N > 10.

## 1. The variant, and why this one
- N5's S4a: H = Even v keeps A(v) = {σ(v)} ∪ Iσ(v), Odd v keeps τ(v). σ_new = Even's optimum of H. The arena comes from Ξ = val(σ, σ̄) and the choice
  from W = val(·, τ): the FRAME SPLIT (L-SI N5-CHG §14, N5-FRZ).
- N5-SF's S4a′: the same H, except Odd v keeps σ̄(v), with σ̄ = σ̄(σ_t) Odd's optimal counterstrategy to the current σ (S1). S4b′ is the mirror
  (Even keeps τ̄(v)). S4c, S4d and S5 are unchanged (experiments/new/box54/n5sf.py; step() differs from n5x.step only in those two lines).
- Why this one keeps N5's correctness argument: σ_new still differs from σ only on edges of Iσ (arena edges are σ(v) or improving), and S4c is
  unchanged. So every Even change applies a nonempty subset of Ξ-improving switches, exactly as in N5. That is R15 (c), (d)'s hypothesis, and
  nothing about the opponent used in the optimisation enters it.
- Why the other one does not. N5-SFW's arena is W-improving edges against τ. A W-improving switch need not be Ξ-improving, so σ can go DOWN in
  R15's order ≺, and termination is lost. DEAD (DATA): MODE=w on alt_all, 49 of 413 games revisit a (σ, τ) state (sfw_alt.txt, CYC_V = 49).
  The smallest is red/n5inj/instances/theta_thf16.pg (n 16, sha1 90ed13cf…, SPEC S3 start): state 2 recurs at iteration 12, period 10.
  The largest seen is red/n5/instances/dlm2_4 (n 42, a cycle after 215 iterations). A random search of 4,000 games with n ≤ 7 found no cycle.

## 2. PROVED (lane)
Lemma SF-TERM (termination and correctness). N5-SF stops, and its output (S5) is correct.
Proof. Every iteration has Iσ ∪ Iτ ≠ ∅ (S4). If σ changes, then σ_new is σ with a nonempty subset of Iσ switched (S4a′'s arena, or S4c). So it
goes strictly up in ≺ (RESULTS R15 (c): «every non-empty switch of improvements goes strictly up in ≺»). The same holds for τ on G^d. Every
iteration changes σ or τ: if both optimisations return the old strategies, S4c switches some improving edges. So no state repeats, and the
state space is finite. At the stop Iσ = ∅, and S5's output is N5's (σ optimal by classical SI, the same final argument as N5). □
DEAD: Lemma NOFB («S4c never fires in N5-SF»). Instance n5-exhaustive/instances/n3all_maxph_0.pg with its .start. At state 1, σ = [1, 1]: the
edge (1, 0) is Ξ-improving through the length component of an odd cycle node (Ξ(0) = (1, ∅, 1) beats Ξ(1) = (1, ∅, 0)). But switching it closes
the same cycle at vertex 1, so the value at 1 does not change. The arena optimum is σ itself, and S4c fires, as in N5 on non-sink games. My
one-player argument (an improving switch strictly raises the switched vertex) is false for VJ00's length component on a cycle-closing switch.
DATA: fallbacks fire in 44 / 35 / 16 games of alt_all / lib41 / sicorpus.
Lemma DECOUPLE. In N5-SF, S4a′ reads only σ (Iσ, Ξ and σ̄ are functions of σ). S4c's Even branch fires when σ_new = σ and τ_new = τ, and then
switches by (Iσ, Ξ), which are functions of σ. So whenever σ changes it becomes F(σ), with F(σ) := S4a′'s optimum if that differs from σ, and
S4c's Even switch otherwise. The SEQUENCE of distinct σ values is σ_0, F(σ_0), F(F(σ_0)), … until Iσ = ∅, independent of τ. Only the iterations
at which σ stalls, waiting while τ moves, depend on τ. The same holds for τ. Hence I ≤ (#σ-values − 1) + (#τ-values − 1). □
Theorem SF-RED. Let σ_a, …, σ_b be a maximal stretch of Even's distinct-σ sequence on which σ̄(σ_i) = σ̄_a and λ_Ξ(σ_i) = λ_a. Then it is an
initial segment of N5's run on the one-player game G_{σ̄_a} (G with every Odd vertex cut to its σ̄_a edge) from σ_a, inside one λ-phase of that
run. So b − a < n + m, of which at most n − 1 steps change the valuation. Consequently
  #σ-values − 1 < (n + m)·(1 + LAM + SBC_σ),   LAM ≤ n(n − 1),
with LAM the σ-changes at which λ_Ξ changes and SBC_σ those at which σ̄ changes. The same holds for τ, with τ̄ and the dual.
Proof. On the stretch, Ξ_{σ_i} = val(σ_i, σ̄_a) = the valuation of σ_i in the one-player game G_{σ̄_a}, whose only Odd strategy is σ̄_a, which is
optimal there. So Iσ_i is G_{σ̄_a}'s improving set. S4a′ is N5's S4a on G_{σ̄_a} (τ := σ̄_a). S4c's Even branch is N5's S4c on G_{σ̄_a}: in a
one-player game Iτ = ∅ and the condition is σ_new = σ. So F agrees with one N5 iteration on G_{σ̄_a}. λ_Ξ is that run's λ, constant on the
stretch. RESULTS R17 (b), (c) bound a λ-phase of N5 on a one-player game by n − 1 value-changing steps and fewer than n + m steps (the use
L-SI made in Corollary FW-D0, docs/si/N5-FRZ-box29.md §2). LAM: Ξ never falls along σ-changes (RESULTS R15 (a), (d), as used in R84), its first component compares the cycle
node's reward, and the n rewards are distinct, so each vertex changes its cycle node ≤ n − 1 times. The stretches number ≤ 1 + LAM + SBC_σ. □
- READING. The frame split is gone. What remains is the frame CHANGE, Odd's best reply moving under Even's run. SBC is K9's «changes of σ̄»
  factor (G-N5-TIME row), now for a one-sided algorithm whose Even run ignores τ. N5-SF's Even run is a strategy-improvement algorithm in its
  own right: "the optimal one-player response to the current counterstrategy, within the improving edges". It is to be identified against
  the literature before any claim. Whether it equals a known rule with a known exponential lower bound (Friedmann; PGSolver's
  switch_globally_best; Schewe's optimal SI) is OPEN. switchbestexp's first four counts match PGSolver's switch-best closely.

## 3. DATA (experiments/new/box54/sfrun.py; logs sf_alt.txt, sf_lib41.txt, sf_si.txt, sf_fam.txt, sf_friedmann.txt, sf_sbe_*.txt, sf_hf.txt)
Checks per game: WIN_V (SF's final regions ≠ N5's), OPT_V (SF's final σ has an improving edge), R17_V (a (σ̄, λ)-segment with > n − 1
σ-changes), CYC_V (a repeated state). FB_V counts the games with any S4c fallback.
| corpus | games | N5 iterations | SF iterations | WIN / OPT / R17 / CYC | games with fallbacks | max SF it / n | max SBC / n | max segment / n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (pinned starts) | 413 | 10,224 | 5,302 | PASS ×4 | 44 | 1.36 (block_bk32) | 0.92 (so_sor5_n24) | 0.94 (x32_rand16) |
| lib41 | 349 | 7,397 | 3,735 | PASS ×4 | 35 | 1.50 (pure_22) | 0.92 | 0.94 |
| sicorpus (pinned starts) | 276 | 6,737 | 3,544 | PASS ×4 | 16 | 1.17 (pg_n48_2) | 1.17 (pg_n48_2) | 0.86 |
- The ratio SF / N5 is ≤ 2.1 per game (best_1302: 21 vs 10; bribe_cex_n15: 2 vs 1).
Families (sf_fam.txt). Columns: n, N5 iterations, SF iterations, SBC, LAM, segments, max segment.
| game | n | N5 | SF | SBC | LAM | seg | max seg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| runquad_K3 / K8 (R106) | 54 / 192 | 21 / 264 | 2 / 2 | 1 | 1 | 2 | 1 |
| s3quad_K3 / K8 (R107) | 137 / 479 | 21 / 264 | 2 / 2 | 1 | 1 | 2 | 1 |
| topfix_N, N = 3, 4, 6, 8, 10 (R109) | 63..210 | 61, 95, 181, 291, 425 | 64, 77, 91, 105, 119 (= 7N + 43) | 6, 11, 14, 16, 18 | 4 | 10..21 | 19..60 |
| topfix_8_cmp (box 52 graft) | 171 | 291 | 105 | 47 | 4 | 50 | 48 |
| DLC_d, d = 2, 3, 4 (box 51; one-player) | 27..455 | 7, 15, 31 | 7, 15, 31 | 0 | 0 | 1 | = len |
| runfam_K10 / K40 (L-SI) | 49 / 79 | 100 / 172 | 37 / 39 | 9 | 2 | 10 | 26 / 28 |
| pivot_demo (R110, red/ctl) and its dual | 11 | 2 | 1 | 1 / 0 | 1 | 2 | 1 |
| duals: hntop_n3, runquad_K3, dlc_d3 | 63, 54, 109 | 61, 21, 15 | 64, 2, 15 | 0 | 0 | 1 | 0 |
- In the duals Even's side is trivial (SBC 0) and the count is τ's run. hntop_n3's dual costs SF 64 against N5's 61.
Friedmann's switch-best family (PGSolver port hard-families/pgsolver_port.py switchbestexp N; sf_friedmann.txt, sf_sbe_a/b.txt):
| N | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n | 35 | 60 | 85 | 110 | 135 | 160 | 185 | 210 | 235 | 260 |
| N5 | 20 | 32 | 41 | 47 | 55 | 62 | 68 | 77 | 83 | 89 |
| N5-SF | 20 | 58 | 135 | 258 | 364 | 412 | 456 | 489 | 577 | 619 |
| SBC | 1 | 4 | 11 | 26 | 49 | 56 | 60 | 75 | 92 | 97 |
| max segment | 11 | 19 | 25 | 31 | 35 | 41 | 47 | 53 | 59 | 65 |
| PGSolver switch-best (README) | 23 | 61 | 137 | 289 | 593 | 1201 | 2417 | 4849 | | |
- switchallexp N = 1..6: SF 5, 8, 8, 8, 10, 12; N5 5, 8, 7, 8, 10, 12.
M1 hard families (hf.sh; Oink generators at the pinned 8fbf0a7, PGSolver port; sf_hf.txt). N = 2, 3, 4, 5, 6, 8; SF iterations (N5 in brackets):
counter_symsi 8, 9, 11, 12, 14, 17 (13, 25, 22, 31, 37, 48); tc 4, 8, 9, 13, 13, 17 (4, 7, 16, 19, 18, 30); counter_rob 5, 7, 9, 11, 13, 17
(5, 7, 10, 13, 16, 22); counter_core / ortl / dp / m / rr / qpt and recursiveladder ≤ 16. SBC ≤ 16 everywhere. 0 violations.

## 4. Open count, and what is and is not shown
- SHOWN (PROVED, lane; premises R15, R17): N5-SF is correct, and its length is < 2(n + m)(n² − n + 1 + SBC), with SBC the total best-reply
  changes of both one-sided runs. So the per-phase length is no longer open for N5-SF; only SBC is.
- NOT shown: any bound on SBC. CONJECTURE SF-POLY: SBC is polynomial (DATA: ≤ 1.2n on the library, ≤ 16 on the M1 families, 97 = 0.37n on
  switchbestexp at N = 10, growing roughly linearly after a steep start). OPEN.
- NOT shown: that N5-SF is new, or that it escapes Friedmann's lower bounds. Its first four switchbestexp counts track PGSolver's switch-best,
  so a larger switch-best-type family is the natural kill target. Next steps, if routed: (i) L-LIT identifies N5-SF's one-sided step in the SI
  literature; (ii) switchbestexp N = 12..20 and Friedmann's other switch-best constructions; (iii) the gauntlet (TARGET.md §5).
- Relevance refinement (not done): as in box 52, only σ̄-changes that change Iσ or σ̄ on the arena's plays matter. SBC as measured counts
  them all (topfix_8_cmp: 47 = 16 + the comparator's flips, harmless here).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box54/ (n5sf.py, sfrun.py, hf.sh, mkdual.py; logs; instances out/: switchbestexp N ≤ 12, switchallexp
  N ≤ 6, hf/, duals); check.sh block "Box 54".
- FINDINGS: (1) N5-SF (Ξ frame on both sides) is correct; Lemma SF-TERM, DECOUPLE and Theorem SF-RED are PROVED (lane): length <
  2(n + m)(n² − n + 1 + SBC). (2) DEAD: the W-frame twin N5-SFW cycles (theta_thf16, period 10); and my Lemma NOFB (n3all_maxph_0).
  (3) DATA: SF ≈ ½ of N5 on the library, linear on runquad / s3quad / topfix / runfam, but 7× N5 on switchbestexp N = 10, where SBC grows
  1 → 97. (4) Open count: SBC. CONJECTURE SF-POLY is OPEN, with switch-best families as the kill target.
- NEEDS: none from the owner. (Suggest to the Lead: an L-LIT check of whether N5-SF's step is a known SI rule.)
