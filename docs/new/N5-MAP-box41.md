# N5 on 𝒞^1O, box 41 (c): the G-N5-TIME map after FB-POLY (READING; what is left is (E), (K_W), the (NH′) assembly and Lemma Φ)
L-NEW successor 20 (Opus 5.5, D15/D18), session_018pjn8Y8JRES3YuFDUCAJgM. Working note (not a packet), written 2026-10-25 19:0xZ (date -u).
- Label: READING throughout (how statements combine; every premise is named with its status). Not a running-time claim. G-N5-TIME
  stays OPEN. The Lead's map governs; this note says what the lane sees.

## 1. Per-phase counts on 𝒞^1O
| count | bound | premises (status) |
| --- | --- | --- |
| f (in-phase Even fallbacks) | ≤ 1 + (n − 2)(2n − 1) | FB-POLY, packet P-N5-FBPOLY (l-new 4a17f8e1, sha1 de244dcd…; lane PROVED, in review) |
| T (H1-toggles) | ≤ n² + 2n − 1 | TOGGLE-COUNT, RESULTS R34 (e) (LANDED) |
| X_SN (S4a crossings at states with c_w = c_θ) | ≤ 13(d_o + 1)n³(f + 1 + T) + T | X-SN-PHASE, RESULTS R34 (f) (LANDED) |
| X (all crossings) | ≤ (f + 1)(n − 1) + f + X_SN | SN-PREFIX, RESULTS R30 (c) (LANDED) |
| fallbacks at OTHER states (NFB-O) | ≤ f | FB-POLY |
| X_OUT (crossings inside OUT stretches) | ≤ (|U| − 2)(f + N_OUT) + f | X-OUT, docs/new/N5-XOUT-box41.md (lane; not needed given the row above, but sharper) |
So (X) of RESULTS R21's consequence ("X poly(n) per phase") follows from FB-POLY and landed results: X = O(d_o·n³·(f + T)) = O(n⁶).

## 2. What is left for N5 on o-cyclic 𝒞^1O
- R21 (g) Theorem X (LANDED): per phase ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) transitions; O := OTHER-touching transitions.
- (NH′) := "O is poly(n) per phase". READINGs checked by both referees, not signed: R22 → R24 (RESULTS R24 "Reduction"): (NH′) reduces to
  (X), NFB-O and the U2/U3 re-routings; R26 ("Reading"): (NH′) reduces to (X), NFB-O, (E) and (K_W), with the ¬H1 θ-count closed by R-1.
  With §1, (X) and NFB-O are in hand. Left: (E) (events per W-flat run: kind crossings and c_w's switches) and (K_W) (non-fallback
  W-changes on R outside route form), both OPEN (R26 honest limits (ii)); and the reductions themselves are READINGs, not signed.
- Lemma Φ (≤ 2n(n − 1) + 1 joint λ-phases; box 21, lane PROVED, UNREFEREED), and τ-changes ≤ d − 1 (R15 (c) on G^d).
- o-acyclic 𝒞^1O: RESULTS R18 (conditional on (P) for one-player games; (P) discharged for one-player games by R36).
- Beyond 𝒞^1O (games with ≥ 2 Odd choice vertices): nothing of this map applies. TARGET.md's question is untouched by 𝒞^1O results.

## 3. Suggested next targets (lane view; for the Lead to route)
- (E) and (K_W) on 𝒞^1O with f now bounded: the κ-freeze lens (Bellman-Ford rounds at fallbacks; BF-F at S4a steps on F) is the natural
  tool; note the S4a length-case gap below.
- A referee check of the (NH′) reductions (R24, R26 READINGs) as signed statements, now that their (X) / NFB-O premises are lane-proved.
- Lemma Φ to the referees.
- Recorded obstruction (box 41, for the κ form of FREEZE-F): BF-F's M-form proof does not lift to κ at S4a steps. In case 2 with x's
  play passing v, the cycle C = v → x → … → v created by v ↦ x can have wt(C) = 0 and top u ∉ {c_θ} of rank < rank(c_θ); the gate is then
  a pure length gain (s_θ = +1), (F1) gives nothing (reward(u) < reward(c_θ)), and κ_{k+1}(v) ≥ κwt(v) + κ_k(x) is not implied. So
  κ-FREEZE-F is OPEN; θ-changes are still ≤ (ρ + 1)(|U| − 1) by κ(o)-monotonicity at fixed P(θ) (θ-LEN, P-N5-PFZ-ext). θ_ph is no longer
  needed for f (FB-POLY) or X (§1).
