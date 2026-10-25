# Draft RESULTS R38 (Lead, 2026-10-25 13:45Z by date -u) (rev. 14:07Z: C47 E-1 (CN-LAST wording from packet §6), N-2, N-3) — to CHECKER C47 — LANDED in RESULTS Results 14:16Z (CHECKER C47 d0900448 + Addendum 1 e666fb56 PASS), after R37

### R38 [refereed-only] N5: (λ_Ξ, τ)-phases are the joint λ-phases (KEY), w-changes between H2 states and scope runs per phase are polynomial in (T, f, X) (WCH, SCOPE-COUNT), fallbacks per crossing-free stretch and at ¬H1 states are polynomial (FB-INT, NH1-FB), and a fallback whose gates are all own-cycle-node length switches ends its phase (CN-LAST) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C47.md, checker PENDING)
- Object (packet P-N5-SCOPE, added at l-new 8483279, pinned trunk 8998ee6, unchanged during review): docs/new/P-N5-SCOPE-box36.md, sha1
  c3f5ed3788f0853939d247dbcfb970334c9dcf7d (L-NEW successor 16, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-SCOPE-fixes-box36.md (l-new eb5477a, sha1 e25507556562d8d84f2c0038ba3d3f85b2b851a1, L-NEW successor 17: N-SC-1..4, O-1
  as a §7.2 note, REFEREE's §C lines); on trunk; repairs only.
  Setting as in RESULTS R28-R34 (phase; R, F; H1-H3, (h); crossings X; fallbacks f; H1-toggles; T := TOGGLE-COUNT's count, at most
  T* = |U|(n+1) + n − 1 (R34 (e)); scope runs; n_E := number of Even vertices). U_k = Ξ^d_{τ_k} is Odd's valuation and λ_U its cycle-node
  map.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Remark KEY (every game): λ_U is a function of τ alone, so on every run of states with τ constant it is constant; a (λ_Ξ, τ)-phase is
      exactly a joint λ-phase (λ_Ξ, λ_U, τ), and every result signed on joint λ-phases with τ constant holds verbatim on (λ_Ξ, τ)-phases.
  (b) Lemma WCH (𝒞^1O): at a transition k → k+1 of a phase with H2 at k and k+1 and w_k ≠ w_{k+1}, either it is a crossing or
      Ξ_k(t0) ≠ Ξ_{k+1}(t0) for t0 := τ(o); off crossings t0 ∈ F_k = F_{k+1} (N-SC-2, wording). Hence such transitions number at most
      (n − 2)(X + 1) + X per phase.
  (c) Corollary SCOPE-COUNT (𝒞^1O; premise RESULTS R34 (g) RESTARTS): the scope runs of a phase number at most
      #(h)-runs + #WCH ≤ (1 + T + f) + (n − 2)(X + 1) + X.
  (d) Lemma FB-INT (𝒞^1O): a maximal run of consecutive transitions of a phase, none of them a crossing, contains at most n_E(2n − 1)
      S4c fallback transitions (every non-tame transition of a phase is a crossing: the proof of RESULTS R28 (c) (ii); N-SC-3).
  (e) Corollary NH1-FB (𝒞^1O; premises RESULTS R33 (e) R-CONST and R34 (e) TOGGLE-COUNT): the S4c fallback transitions k → k+1 of a phase
      with ¬H1 at k number at most n_E(2n − 1)(⌈T/2⌉ + 1) + T ≤ poly(n), with no X term and no f term.
  (f) Lemma CN-LAST (every game): if k → k+1 is an S4c fallback at which Even switches (Iσ_k ≠ ∅), and every gate (y, z) ∈ Iσ_k has λ_k(y) = y and
      lev(Ξ_k(σ_k y), Ξ_k(z)) = −1, then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is the last state of its phase (the next iteration changes
      τ, or N5 stops).
- Not signed (packet §7): the out-of-SN fallbacks (fallbacks at H1 ∧ ¬H2 states and at H1 ∧ H2 ∧ ¬H3 states; OPEN), CONJECTURE OUT-POLY,
  the level −1 residue (oc12_s1), and the dead end "PF-THETA, linear form" FALSE (experiments/red/so/instances/pftheta_cex_n32.pg, sha1
  9f526135; 33 θ-changes > n = 32 after one fallback in one scope run; L-RED successor 15; Lead re-run: one Odd choice vertex, n5 38/1,
  Oink zlk OK strategies verified). Note O-1 (both referees): §7.2's out-of-SN count needs f_out ≤ n_E(2n − 1)(X_out + 1) + X_out, since
  evicting fallbacks are crossings and lie in no FB-INT stretch (experiments/new/box25/instances/wd16_s2.pg: every in-phase fallback a
  crossing; Lead re-run n5 19/14, Oink OK).
- Honest limits: (i) KEY and CN-LAST hold on every game; the rest is on 𝒞^1O. (ii) The bounds are polynomial GIVEN T, f, X; f per phase
  outside these classes (the out-of-SN fallbacks) is OPEN, so G-N5-TIME stays open. (iii) The bounds are far from reached in all data
  (at most 4 fallbacks per crossing-free stretch, 4 ¬H1 fallbacks per phase in REFEREE-2's climbs on its own N5; REFEREE's climbs: at
  most 1 per crossing-free run, no ¬H1 fallback). (iv) The packet's dependency status "IN LANDING"
  for P-N5-L2 was stale: RESULTS R33 landed before the packet (N-SC-1). (v) Lane work after the pin (P-N5-OUT, P-N5-NEB) is not part of
  this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every 𝒞^1O game): REFEREE scope_probe.py, scope_climb.py (own trace = n5.run):
  library 276 files (KEY 7,455; WCH 135; scope runs 225; non-tame 339; ¬H1 fallbacks 9; CN-LAST 23), random 𝒞^1O 30,000 games, general
  games 20,000 (KEY, CN-LAST), 2 climbs (766,585 candidates), 0 failures; CN-LAST 1,422 cases, in 1,420 N5 stops at k+1 and in 2 the next
  transition changes τ. REFEREE-2 (own N5, which takes another S4a optimum; own general N5 for CN-LAST): 849 logs / 86,517 runs and 8
  climbs (5,443,544 runs), 0 violations; Oink zlk agrees on 552 / 552 + 574 / 574 + 16 / 16 games.
- Signatures: REFEREE docs/referee/R-N5-SCOPE.md (referee fb6089b + 560ff4c, successor 7; §C 257c3d8, successor 8): KEY, WCH,
  SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST SIGNED; no gaps. REFEREE-2 docs/referee-2/R2-N5-SCOPE.md (referee-2 6d6e4bc, successor 8, draft 1f8a9109, stamp 8655f692; §C
  fb6fa69): KEY, WCH (N-SC-2), SCOPE-COUNT, FB-INT (N-SC-3), NH1-FB (N-SC-4), CN-LAST SIGN; notes N-SC-1..4, observation O-1. §C: no
  verdict differs; the joint gap map is empty; REFEREE accepts N-SC-1..4 and O-1.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
