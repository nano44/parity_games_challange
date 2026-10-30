# N5-R2 (box 82): CONJECTURE R2-POLY is DEAD. Odd gates with τ-honest routing give 2^k W-values with Ξ a genuine pair valuation (ogl_8: 256 at n 48). What is left is Odd OPTIMALITY: under σ̄ the gates collapse, and each gate would need its own interleaving clock (L-RED design spec)
L-NEW successor 37 (Opus 5.5), D14 / D18, Lead reading L40. Lead 10:32Z: «THEN BOX 82: R2-POLY, GO … If you find an instance, write it up
as an L-RED design spec.» Written 2026-10-30 10:20Z-10:45Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
- Definitions: docs/new/N5-WCHT-box80.md (R0, ladder_k, LADDER), docs/new/N5-R1-box81.md (R1, GATED-LADDER). R2 := R1 with CONSISTENCY:
  X_t := the [S1-val] valuation of the (σ_t, ρ_t)-plays for SOME positional Odd strategy ρ_t; X_t ⊴ W_t (W_t := the valuation of the
  (σ_t, τ)-plays, τ fixed); X non-decreasing in t; offers Of_t := {(v, w) : X_t(w) ▷ X_t(σ_t v)}; σ_{t+1} := the one-player W-optimum of
  σ_t ∪ Of_t. N5 inside a W-run is R2 with ρ_t := σ̄_t (Odd's OPTIMAL counterstrategy, [S1-Xi]) and the further S4a / S4c mechanics.
- Tools in experiments/new/box82: r2search.py (exhaustive R2 search, abstract model, k ≤ 3), ogladder.py (construction + engine
  verification); instances inst/ogl_{2,3,4,6,8}.pg.

## 1. The Odd-gated ladder ogl_k
- ladder_k (box 80) with every choice edge v → u(j, c) replaced by v → o(v, c), where o(v, c) is an ODD gate with successors
  {u(j, c) = τ(o), u(j, 1 − c)}. Gates are less relevant than the sink (priority 2, self-loop, the only cycle node), so they never enter
  a path set, and all plays from one vertex have equal length. n = 2k + 2 + 2(2k − 1) = 6k; 4k − 2 Odd choice vertices.
- So W (Odd fixed to τ) is ladder_k's valuation, and X under ρ reads, at each gate, either its own child (HONEST, ρ(o) = τ(o)) or the other
  child (ROUTED).

## 2. Proposition ODD-GATED-LADDER (PROVED, lane; DATA: exhaustive k ≤ 3, engine replay k ≤ 8)
- Statement. For every k there is an R2 run on ogl_k in which W(T) takes 2^k values.
- Construction. Box 80's lead-follow schedule, with ρ_t(o(v, c)) := u(j, 1 − c) (ROUTED) iff v holds o(v, 1 − c) at t, the scheduled switch
  at t is not v → o(v, c), and W_t(u(j, c)) ▷ W_t(u(j, 1 − c)); otherwise HONEST.
- Proof.
  - Every CURRENT gate is honest (a gate is routed only while its owner holds the OTHER gate), so every ladder vertex and reader has
    X = W; only non-current gates can differ.
  - A routed gate o(v, c) has X = (gate) ⊕ W(u(j, 1 − c)) = X of v's current gate: equal, so it is not offered. An honest non-current gate
    o(v, c) has X = W(u(j, c)) ⊴ W(u(j, 1 − c)) = X(current) unless it is the scheduled target: not offered. The scheduled target is honest
    with W(u(j, c)) ▷ W(current): offered and W-improving. So Of_t is exactly the scheduled edge, and the one-player optimum takes it.
  - X ⊴ W: a routed gate reads the W-smaller child.
  - X non-decreasing: an honest gate tracks W(u(j, c)) and a routed one tracks W(u(j, 1 − c)), both non-decreasing (box 80). A switch
    honest → routed happens when u(j, c) overtakes u(j, 1 − c), so the new value W_{t+1}(u(j, 1 − c)) ⊵ W_t(u(j, 1 − c)) ⊵ W_t(u(j, c)), the
    old one. A switch routed → honest goes from the smaller child to the larger. □
- DATA. r2search.py (exhaustive over all (σ, ρ) runs, abstract values): max W(T)-rises 3 (k = 2), 7 (k = 3) = 2^k − 1 = the R0 maximum.
  ogladder.py (fleet Engine, X computed as the valuation of the actual (σ, ρ) pair on the .pg): k = 2, 3, 4, 6, 8: T-values 4, 8, 16, 64,
  256 at n = 12, 18, 24, 36, 48; X > W 0, X decreases 0, offer mismatches 0, non-improving 0, W decreases 0, cycle nodes {0}. Pinned:
  inst/ogl_8.pg.
- So R2-POLY is DEAD: consistency alone does not bound per-vertex W-changes. Ξ's freedom at Odd choice vertices with ρ ≠ τ suffices for
  2^k values at one vertex.

## 3. What N5 adds: Odd OPTIMALITY, and why ogl_k collapses under it (PROVED, lane)
- Lemma GATE-COLLAPSE. In ogl_k, if ρ_t = σ̄_t (Odd's pointwise optimum against σ_t), then for every reader v the two gates have equal X,
  so no reader is ever offered a switch (no S4a step at a reader).
  - Proof. A gate is less relevant than the sink and adds one step to every play, so X(o(v, c)) = o ⊕ X(ρ(o)) with ρ(o) ∈ {u(j, 0),
    u(j, 1)}, and the two values differ only by the ladder part. The pointwise optimum minimises at o ([S1-Xi]), so ρ(o) is the X-smaller
    of u(j, 0), u(j, 1) for BOTH gates of v. Their values are equal triples. [S2] needs a strict rise. □
- So the obstruction left between R2 and N5 is exactly OPTIMALITY of σ̄. Under σ̄ a gate is honest only if its own child is the X-SMALLER
  option, but the counter needs it honest exactly when its child is the BETTER one (to offer it).
- L-RED DESIGN SPEC (READING; what a gate must do in N5): give each gate o(v, c) a private ESCAPE e(o) in place of u(j, 1 − c), with Ξ(e)
  monotone and alternating relative to the ladder:
  - while o must be BLOCKED: Ξ(e) ⊴ Ξ(v's current option) (so σ̄ routes to e and the gate is not offered);
  - while o must be OPEN: Ξ(e) ⊵ Ξ(u(j, c)) (so σ̄ stays honest and the gate is offered at the ladder value).
  Both bounds rise with the counter, so e needs its own clock whose values INTERLEAVE with the ladder's, once per counter step, with
  W(e) ⊵ Ξ(e) and λ_W fixed. That is R132's / R108's reused waiting gate, now as an exact requirement on one Odd vertex: an escape whose Ξ
  climbs in lock-step between two consecutive ladder values, 2^k times, inside one W-run. If such a clock costs poly(n) vertices per gate,
  ogl_k with clocked escapes would be an exponential N5 W-run (a G-N5-TIME kill); if every clock that interleaves with a counter must itself
  be a counter of the same length on private vertices, the size doubles per level and the construction stays polynomial.
- CONJECTURE R3-POLY (OPEN, the precise next target): with ρ_t = σ̄_t (R2 + Odd optimality), per-vertex W-changes per W-run are polynomial.
  N5 on W-runs is an R3 run, so R3-POLY ⇒ [P-WCHτ] on W-runs.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box82/r2search.py, ogladder.py, inst/ogl_{2,3,4,6,8}.pg; this note; check.sh "box 82" (ogl_6 replay).
- FINDINGS:
  1. DEAD: CONJECTURE R2-POLY. Proposition ODD-GATED-LADDER (lane-PROVED; exhaustive k ≤ 3, engine k ≤ 8): Odd gates with τ-honest or
     routed choices, Ξ a genuine pair valuation, X monotone and ⊴ W: 2^k W-values at one vertex (ogl_8: 256 at n 48).
  2. PROVED (lane) Lemma GATE-COLLAPSE: with Odd's optimal reply the ogl gates of a reader are X-equal, so nothing is offered. The gap
     R2 → N5 is exactly σ̄'s optimality.
  3. READING / L-RED design spec: each gate needs a private escape whose Ξ interleaves with the ladder values once per counter step
     (R132's reused gate, exact form). CONJECTURE R3-POLY is the next target.
- NEEDS: none from the owner. Lead: route the design spec (§3) to L-RED if wanted; go / no-go on R3-POLY. Context ~440k; I park at ~550k.
