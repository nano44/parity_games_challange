# Draft RESULTS R34 (Lead, 2026-10-25 10:48Z by date -u) (rev. 11:04Z: C43 E-1) — to CHECKER C43 — LANDED in RESULTS Results 11:18Z (CHECKER C43 70b0e9c + Addendum 36905e57 PASS), after R33

### R34 [refereed-only] N5 on one-Odd-choice games: H1-toggles per phase are polynomial (L-MONO, Z-COUNT, Theorem TOGGLE, TOGGLE-COUNT), so crossings in SN prefixes per phase are polynomial in f (X-SN-PHASE) and (h)-runs per phase are at most 1 + T + f (RESTARTS) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C43.md, checker PENDING)
- Object (packet P-N5-TOG, added at l-new 3e45aed, pinned trunk d3daae1, unchanged during review): docs/new/P-N5-TOG-box35.md, sha1
  7dfda8c88a0e9b752156f4faec726d8dccc20ccb (L-NEW successor 15, Opus 5.5). The referees' repairs are collected by the lanes in
  docs/new/P-N5-TOG-fixes-box35.md (l-new b5b8e66, sha1 f15b58dddf232d810fab277010e29ae5187d382d, L-NEW successor 15: G-TOG-1, N-TOG-1)
  and docs/new/P-N5-TOG-fixes2-box35.md (l-new e570bc6, sha1 698539a9e525c467a46ebd59b1785dc0be98c113, L-NEW successor 16: TOG-1 =
  G-TOG-1 and TOG-2 = N-TOG-1 with REFEREE's tighter record line; the DATA attribution of G-TOG-1; §7's DROP-LEN line out of date);
  both on trunk; repairs only.
  Setting as in RESULTS R30-R33 (𝒞^1O; phase with λ_Ξ and τ constant; c := λ(o), U := λ^{-1}(c); H1; next_k(v) := σ_k(v) for Even v,
  σ̄_k(v) for Odd v; (M) := RESULTS R15 (a)). An H1-TOGGLE is a transition inside a phase at which H1 changes; a DROP is one from H1 to ¬H1.
  Z_k := {(v, length of Ξ_k(v)) : v ∈ U, P(Ξ_k v) = ∅}.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Fact (F): if x lies on the cycle of c's H_k-play and λ_k(c) = c, then Ξ_k(x) = (c, ∅, dist_k(x → c)); if x ≠ c and λ_k(x) = c,
      then Ξ_k(x) = x ⊕ Ξ_k(next_k x). (Separately signed by REFEREE-2; used by REFEREE in its setting.)
  (b) Lemma L-MONO: for c = λ(o) ≠ o in a phase, the length L_k of the cycle of c's H_k-play is non-increasing if Ω(c) is even and
      non-decreasing if Ω(c) is odd, strictly whenever σ(c) changes; so σ(c) changes at most n − 1 times per phase.
  (c) Lemma Z-COUNT: Z_k ≠ Z_{k+1} at no more than |U|(n + 1) transitions of a phase.
  (d) Theorem TOGGLE: at an H1-toggle k → k+1 inside a phase with c ≠ o, if Z_{k+1} = Z_k then next_{k+1}(c) ≠ next_k(c), so c ∈ V_E
      and σ(c) changes.
  (e) Corollary TOGGLE-COUNT: H1-toggles per phase ≤ T := |U|(n + 1) + n − 1 ≤ n² + 2n − 1, and drops ≤ ⌈T/2⌉; no toggles when c = o.
  (f) Corollary X-SN-PHASE (premise RESULTS R33 X-RUN′, hence R32): X_SN per phase ≤ 13(d_o + 1)n³(f + 1 + T) + T, with no hypothesis
      on H1. X_SN also counts the S4a crossing from each run's last SN-prefix state out of the prefix, which X-RUN′ (a) does not; X-RUN°
      gives ≤ 13(d_o + 1)n³ − 1 crossings per H1 run, and the slack covers it, so the stated bound stands (TOG-1 = G-TOG-1, accounting,
      closed). The packet cites X-RUN′ as "P-N5-L2 §11"; it is §7 (TOG-2 = N-TOG-1, citation, closed).
  (g) Corollary RESTARTS (premises RESULTS R33 H2-STICK, H3-CONST and RESULTS R30 H3H2): a phase has at most 1 + T + f maximal (h)-runs;
      a restart is an H1-toggle or an Even S4c fallback.
- Not signed (packet §7): CONJECTURE DROP-LEN is listed there as open; it is FALSE (RESULTS R33, droplen_cex_n12), and so is its
  per-run form (onerun_cex_n32, RESULTS R33). OPEN: (L1), the f ↔ X loop, K.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) X-SN-PHASE and RESTARTS are polynomial GIVEN f; f per phase, (L1) and the
  out-of-SN fallbacks are OPEN, so G-N5-TIME stays open. (iii) DATA is thin against the bounds: at most 6 toggles per phase in the
  library and 5 in climbs against T ≈ n²; max X_SN 91 per phase (library). (iv) TOG-1's boundary crossing occurs on the SPEC trace
  (REFEREE: 26 library files, one per file, e.g. experiments/n5-exhaustive/instances/b4_cyc6_0.pg 0→1, and 88 random; REFEREE-2 19 of
  its 239 files (the report text says 238); L-RED 26 files, e.g. experiments/red/so/instances/so_sor5_n24.pg 21→22); REFEREE-2's counts 310 batch / 246,038 climb
  come from its own N5 (another S4a optimum) only. (v) Lane work after the pin (box 36, P-N5-SCOPE) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE tog_probe.py, tog_climb.py (own trace = n5.run):
  library 272 files, random 30,000 + 15,000 games, 2 climbs (714 improvements re-checked), 0 failures; library toggles 29, random 329 +
  132, each with Z changed or σ(c) switched; c = o phases have no toggle. REFEREE-2 (own code): 31,434 batch runs (239 files and
  random) and 4 climbs (1.75 M runs), 0 violations; every toggle with Z unchanged changed next(c) at an Even c. Re-runs of
  onerun_cex_n32 (8/0), fbrestart_cex_n12 (5/2), fbrestart_cex_n24 (23/3) agree (REFEREE, REFEREE-2, Lead); Lead re-ran b4_cyc6_0 (2/0)
  and so_sor5_n24 (23/0), Oink zlk OK strategies verified, one Odd choice vertex.
- Signatures: REFEREE docs/referee/R-N5-TOG.md (referee fff6e62, successor 7; §C 49dc13b): L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT,
  RESTARTS SIGNED; X-SN-PHASE SIGNED WITH GAPS TOG-1, TOG-2 (closed). REFEREE-2 docs/referee-2/R2-N5-TOG.md (referee-2 faabe71, successor
  7; Addendum A 16d27d1; §C 8681e3f): (F), L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS SIGN; X-SN-PHASE SIGN WITH GAPS G-TOG-1;
  note N-TOG-1. §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 2 rows: TOG-1 = G-TOG-1 (accounting, closed); TOG-2 =
  N-TOG-1 (citation, closed).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
