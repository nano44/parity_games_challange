# Draft RESULTS R77 (Lead, 2026-10-28 23:02Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C86 (Lead reviewed 23:09Z by date -u) — LANDED in RESULTS Results 2026-10-28 23:48Z (CHECKER C86 0f71e023 PASS), after R76

### R77 [refereed-only] N5 on EVERY game, inside one phase: on states [a, b] of one phase on which every transition is an S4a step and τ, λ, λ_W are constant (H1), σ̄ is constant (H2), the honest and the W-cycles are the same cycles and constant (H3), the end-state graph H_b is acyclic off the cycle vertices (H4), and distinct W-plays from a vertex have distinct W-valuations (GEN_W), every non-cycle vertex v has its end-state W-play and honest play from state a + d*(v) on, so σ_t = σ_b on [a + max d*, b] and b − a ≤ max d* ≤ n − 1 (Theorem STATIC-DEPTH); if every gate is D-direct at b, then (H4) holds and every cycle at b is common to both frames (Corollary PURE-END); hence b − a ≤ n − 1 on a global C-interval of a λ_W-constant fallback-free in-phase run on which σ̄ is constant and (H3), (H4), GEN_W hold (Corollary GCI-LEN-ρF; its proof does not use the C-interval structure); and in the cyclic abstract model ABS of RESULTS R76, N never falls along the run (Fact N-MONO) and, if distinct plays from a vertex have distinct N-values (GEN), every vertex v holds its final play from step d*(v) on, so the run is fixed within max d* ≤ n steps under any deterministic tie rule (Theorem ABS-DEPTH) (2026-10-26) — structural lemmas for N5 and a settling theorem in an abstract model (only intervals with σ̄ constant, (H3), (H4) and GEN_W are bounded, and their number is not; the length bound is global, not per class; CONJECTURE ABS-DEPTH-TIE is DEAD for general tie rules; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C86.md, checker PENDING)
- Object (L-SI successor 18, Opus 5.5; frozen, unchanged during review): packet P-N5-DEPTH, docs/si/P-N5-DEPTH-box22.md, sha1
  549c7fb72d767293b6bf2ae5bbbb8809084df707 (l-si freeze 2201aa2d). The referees' notes are collected by the lane in
  docs/si/P-N5-DEPTH-fixes-box22.md (l-si 96bde5f3, sha1 67724abe21b87eea46b7e38b1cef7de1290c542d, L-SI successor 19: F1-F5 for DEPTH-N1..N4,
  N-DEPTH-1..5; 14 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=14 bad=0", pinned in experiments/si/check.sh); on
  trunk; repairs only, no signed statement changes; joint gap map EMPTY. The statements below are in their repaired wording (F1, F3, F4).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4. Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t, σ̄_t); W_t(v): that of v's
  (σ_t, τ)-play. D_t := {Odd u : σ̄_t(u) ≠ τ(u)}; A_t := the vertices whose (σ_t, τ)-play meets no vertex of D_t; a gate u ∈ D_t is D-direct if
  σ̄_t(u), τ(u) ∈ A_t. H_b: edges v → σ_b(v) (Even v), v → τ(v) (Odd v ∉ D), u → τ(u) and u → σ̄(u) (u ∈ D); cycle vertices are sinks. d*(v) := 0
  on cycle vertices, 1 + d*(σ_b v) (Even), d*(τ v) (Odd v ∉ D), max(d*(τ u), d*(σ̄ u)) (u ∈ D): the non-cycle Even vertices on a longest
  H_b-path from v, so d*(v) ≤ n − 1. Model (§1): ABS as in RESULTS R76's setting on any digraph, "pointwise maximal" read as pointwise GREATEST
  (F1, DEPTH-N1 = N-DEPTH-1); play_t(v) := v's play under s_t; s* the fixed point; d*(v) := the non-terminals on v's play under s*; GEN: for
  every v, distinct plays from v have distinct N-values.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: SPEC S1 (valuation and order), S4a (arena
  {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R18 (d) Lemma S (a), every game by R57 (a), on S4a's arena: the standing
  premise 1E-N3 in its form P2 (as listed in RESULTS R69); (SW) as listed among RESULTS R72's landed premises; R56 (a) (M1κ), (M2κ); R69 (d)
  Lemma STATIC (only for (H2)'s parenthetical); and RESULTS R76's model ABS and global C-interval (definitions only; R76 is not yet in
  docs/RESULTS.md at trunk e3bd64e3 and lands before R77):
  (a) Fact N-MONO (§1): N_{t+1} ⪰ N_t for every t ≥ 0, hence N_t ⪯ N* := N_{s*} (s_t is a candidate; s_{t+1}'s N is pointwise greatest, F1).
      (MONO), (MONO-SUCC), (TERM): REFEREE CHECKED, REFEREE-2 CORRECT.
  (b) Theorem ABS-DEPTH (§1; cyclic model, under GEN): for every v and every t ≥ d*(v), play_t(v) = play*(v); hence the run is fixed after at
      most max_v d*(v) ≤ n steps. The induction runs on the final forest; neither step looks at the tie rule (REFEREE: any deterministic rule).
  (c) Theorem STATIC-DEPTH (§2; N5, every game): on states [a, b] of one phase with (H1) every transition an S4a step (no fallback), τ, λ and
      λ_W constant; (H2) σ̄_t = σ̄_a on [a, b]; (H3) at every t the W-cycles and the honest cycles are the same cycles, constant on [a, b]; (H4)
      H_b acyclic outside the cycle vertices; and GEN_W (for every v, different W-plays from v to the same cycle have different W-valuations):
      every non-cycle v has, at every t ∈ [a + d*(v), b], the same W-play and the same honest play as at b; hence σ_t = σ_b on [a + max d*, b]
      and b − a ≤ max_v d*(v) ≤ n − 1. Facts used as proof steps (REFEREE ✓, REFEREE-2 CORRECT): (W-MONO) W_{t+1} ⊵ W_t (P2), (Ξ-SUCC)
      Ξ_t(σ_t v) non-decreasing ((M2κ), (SW)), (CV) cycle vertices constant ((H1), (H3)). Remark (N-DEPTH-2, ACCEPTED by REFEREE; F4): the
      per-vertex settling restricts to any set of vertices closed under H_b-successors; the length conclusion is global (it uses that σ is
      unchanged on the whole game, then S4c's fallback), and a per-class length bound does not follow.
  (d) Corollary PURE-END (§2): if every gate is D-direct at b, then (H4) holds, and every cycle at b is common to both frames. ((H3)'s
      constancy on [a, b] remains a hypothesis.)
  (e) Corollary GCI-LEN-ρF (§3): let [a, b] be a global C-interval of a λ_W-constant fallback-free run in one phase on which σ̄ is constant,
      (H3) and (H4) hold (by (d), (H4) holds if every gate is D-direct at b), and GEN_W holds; then b − a ≤ n − 1. The proof does not use the
      global C-interval structure: the bound holds for every interval of a λ_W-constant fallback-free in-phase run on which σ̄ is constant and
      (H3), (H4), GEN_W hold (DEPTH-N3, accepted by REFEREE-2; F3).
- Not signed: §4 (the instance showing GEN is needed for ABS-DEPTH's per-vertex form: at state 1 vertex 2 has N = N*(2) = 2 on the play
  2 → 0 → 1 → t5, not its final play 2 → t4; the run still ends within max d* = 3; confirmed by both), §5 (data), §6 ((G1)-(G4), CONJECTURE
  STATIC-DEPTH-TIE (OPEN, untouched), the READING), as the packet asked. CONJECTURE ABS-DEPTH-TIE ("in the model, the run is fixed within max d*
  steps without GEN") is DEAD for general deterministic rules (DEPTH-N2 = N-DEPTH-3, F2; not yet in docs/si/DEAD.md at trunk e3bd64e3).
  Obstruction: after the arena shrinks a non-keep rule may leave a current maximiser (the mechanism of G-GCX-1, RESULTS R76). Witnesses:
  REFEREE, R76's one-vertex LOC game (non-GEN, max d* = 1, fixed only after 2 steps under "anti" or "sizedep"); REFEREE-2, non-terminals 0, 1,
  terminals T2 (h 0, T 2), T3 (h 2, T 2), succ(0) = {T2}, succ(1) = {0, T2, T3}, w = (−2, −1), start s(1) = 0, rule "flip": s(1) = 0 → T2 → T3,
  fixed after 2 steps against max d* = 1. Restated (OPEN): CONJECTURE ABS-DEPTH-TIE_keep, for tie rules that keep a maximal current choice (no
  overrun under keep rules in either referee's data).
- Honest limits: (i) STATIC-DEPTH bounds only intervals with σ̄ constant, (H3), (H4) and GEN_W, and the number of such intervals is not
  bounded: GCI-LEN-ρF covers 3,499 of 4,747 global C-intervals in REFEREE-2's corpus (479 with a σ̄ change, (G1); 766 without (H3)) (N-DEPTH-5).
  (G1)-(G4) stay OPEN. (ii) The length conclusion is global ((c)'s Remark): it does not give a per-class length (this is what breaks the
  companion packet's PURE-LEN, G-DADD-1). (iii) GEN_W: SPEC breaks S4a ties by the S1 procedure on the current arena, so GEN_W has no
  automatic substitute ((G4)); REFEREE-2's used-form check failed in 13 intervals, all with the conclusion intact (N-DEPTH-4); REFEREE saw
  none. (iv) (a), (b) are about the model ABS; its link to N5 is a READING (RESULTS R76). (v) The bound is attained: length = max d* in 920
  intervals (REFEREE, DEPTH-N4) and 651 (REFEREE-2). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own abs_depth.py on abs_model.py, depth_probe.py on its engine rl_engine; lane code not run):
  model, 3,246 + 1,794 GEN runs, 12,798 + 6,876 per-vertex checks, 0 failures; N-MONO 0 failures; non-GEN runs later than max d* 8 + 10, all
  under non-keep rules; MUT=1 612. N5: library 1,140 files (2,739 runs; 8,918 STATIC-DEPTH intervals, 4,263 with gates; 512,278 per-vertex
  checks), lib41 (1,130 runs; 6,667 intervals), 9,000 random 𝒞^kO runs (1,059), named instances (184); PURE-END 19,361 / 13,427 / 16,583 / 213
  states; GCI-LEN-ρF 2,046 / 1,313 / 960 / 35 intervals; 0 failures; MUT=1 3,010. REFEREE-2 (successor 18; own absdepth_check.py,
  depth_check.py on its SPEC loop over si.py; lane tools not run): model 36,711 + 37,449 + 60,000 runs, N-MONO and ABS-DEPTH 0 violations
  where GEN holds, non-GEN overruns 9 / 18 / 7 only under non-keep rules; N5 21,775 runs: STATIC-DEPTH 53,113 intervals (17,348 with gates;
  longest 55 on x32_rand64, n 64, max d* 56), PURE-END 18,339 states, GCI-LEN-ρF 3,499 intervals, 0 violations. Both reproduce the §4 run,
  b6_xs 21 / 29 / 36 at n = 24, 32, 40, and x32_waves48 26 (the longest with gates).
- Signatures: REFEREE docs/referee/R-N5-DEPTH.md (report 1d74c963, §C f5081a6a, stamp corrected dc4e47b8; successor 16): N-MONO (greatest
  reading), ABS-DEPTH, STATIC-DEPTH, PURE-END, GCI-LEN-ρF SIGNED, no gap; §4 instance CONFIRMED; notes DEPTH-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-DEPTH.md (report dad93591, §C d8402f3d; successor 18): the same items SIGN, no gap; notes N-DEPTH-1..5. §C (both):
  verdicts identical; joint gap map EMPTY; DEPTH-N1 = N-DEPTH-1, DEPTH-N2 = N-DEPTH-3, DEPTH-N3 accepted by REFEREE-2, N-DEPTH-2 and N-DEPTH-5
  ACCEPTED by REFEREE, N-DEPTH-4 a corpus difference; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas bounding the intervals they cover, and an abstract-model
  theorem; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
