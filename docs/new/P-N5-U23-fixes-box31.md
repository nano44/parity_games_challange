# P-N5-U23 fixes (box 31 packet, answered in box 32): the referees' repairs, written out
L-NEW successor 12 (Opus 5.5, D15/D18). Lead requests 23:53Z, 23:57Z, 00:12Z, 00:24Z (read 00:28Z). Written 2026-10-25 by date -u.
- Object: packet docs/new/P-N5-U23-box31.md, pinned at trunk 7666336, sha1 ee3e5d1ef95623d3f5e08a34af416fa6b2d09186 (re-checked at
  this commit: the file is unchanged). The packet is NOT edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-U23.md (claude/referee 7ffbd9f; §C cde420b), §C.3 "Joint gap map".
  - REFEREE-2: docs/referee-2/R2-N5-U23.md (claude/referee-2 07b22b0; §C 5e24010), §C.6 "Joint gap map".
  - Both §C on trunk 8e25d39. No disagreement; no NOT SIGNED; no counterexample.
- Rule: this file writes down the referees' repairs, one line per row of REFEREE §C.3 (its "repair" column). A line of my own is marked
  "L-NEW".
- Scope unchanged: lemmas about the candidate N5 (SPEC tie-breaks) on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4
  pass. (E), (K_W) and G-N5-TIME stay OPEN.

## 1. One line per row of REFEREE §C.3
| statement | joint status | repair (REFEREE §C.3 column, = REFEREE-2 §C.6) | where below |
| --- | --- | --- | --- |
| CASC-U2 + Corollary | SIGNED by both | — (DATA: u2flat_n32) | §5 |
| CASC-U3 step 1, (i), (iii) | SIGNED by both | U3-2: state the induction along the new routes; U3-3: the c_θ = c_w case | §2, §3 |
| CASC-U3 (ii) | SIGNED by both; U3-1 = G-U23-1, closed | "≤ max(L_B − 1, 0) + λ − 2" (= max(L_B, 1) + λ − 3) | §4 |
| CASC-U3 Corollary | SIGNED by both | optional: factor \|R\| − 2 (REFEREE §2.4; REFEREE-2 accepted) | §4 |
| §3 (E), (K_W) | OPEN, not signed | — | — |
| §3 READING | READING; R-1 = N-U23-2, closed | add: "under ¬H1, θ = (c_θ, ∅, d), so ≤ \|R\| − 1 θ-changes per phase (R15 (a))" | §6 |

## 2. U3-2: kinds are constant on an event-free sub-run (packet §2 proof, step 1)
Replace the packet's sentence "A vertex changes kind only if it, or a vertex on its route, switches across kinds" by the induction below
(REFEREE §2 step 1; REFEREE-2 signs step 1 and takes this argument for granted, REFEREE §C downgrades U3-2 to wording).
- Let k → k+1 be a transition of an event-free sub-run. The stretch has no crossing, so at k+1 every R-vertex's σ_{k+1}-route reaches o.
- Induct along the k+1 routes, from o outward (on the length of the σ_{k+1}-route to o).
  - x = c_w: kind A by definition, at k and at k+1.
  - x ≠ c_w does not switch: σ_{k+1}(x) = σ_k(x) =: x′, and kind_{k+1}(x) = kind_{k+1}(x′) = kind_k(x′) (induction: x′ is one step closer to
    o on the k+1 route) = kind_k(x).
  - x switches: the switch is not an event, so x keeps its kind by the definition of an event.
- So kind_{k+1} = kind_k on R \ {o}, at every transition of the sub-run. □

## 3. U3-3: under U23, c_θ = c_w is possible (packet §2 proof, step 4)
- Under U23 both cycles pass o, so c_θ = c_w can happen. Then c_w is its own honest cycle node: Ξ(c_w) = (c_w, ∅, 0), and the packet's
  formula "Ξ(c_w) = c_w ⊕ Ξ(σ(c_w))" is false there.
- The proof uses only that Ξ(c_w), the honest terminal of every kind-A vertex, is constant on the sub-run from some step on. With
  Ξ(c_w) = (c_w, ∅, 0) it is constant from step 0, which is stronger. Nothing else changes. (Wording; both referees.)

## 4. U3-1 = G-U23-1: the statement of (ii), and the sharper Corollary
Repaired (ii) (replaces the packet's "≤ L_B + λ(v) − 3"):
- (ii) a kind-A vertex v whose σ-path reaches c_w after λ(v) steps switches only at sub-run steps ≤ max(L_B − 1, 0) + λ(v) − 2.
- The two referees' forms agree: max(L_B − 1, 0) + λ − 2 = max(L_B, 1) + λ − 3 for every L_B ≥ 0 (L_B ≥ 1: both are L_B + λ − 3;
  L_B = 0: both are λ − 2).
- Proof change: in the packet's step 4 start the kind-A induction at T := max(L_B − 1, 0) instead of T := L_B − 1. When kind B is empty
  (A2 = ∅, every R-vertex routes through c_w; L_B := 0), T = −1 is not a step; the kind-A terminals are constant from step 0 (c_w does not
  switch on an event-free sub-run), and the induction S^A_λ ≤ T + λ − 1 gives switches only at steps ≤ T + λ − 2. With T = max(L_B − 1, 0)
  this is the repaired (ii). For L_B ≥ 1 nothing changes.
- DATA (REFEREE): the corner L_B = 0 occurred in 2 named and 27 random event-free sub-runs, all switch-free; no counterexample to the
  packet's literal form either. It is the proof that does not reach it.
Sharper (iii) and Corollary (REFEREE §2.4, accepted by REFEREE-2; optional):
- The kinds partition R \ {o}. A kind-A vertex at W-level λ has λ + 1 kind-A vertices on its σ-path to c_w (c_w included); a kind-B vertex
  with |π| = L_B has L_B kind-B vertices on its route. So L_B + λ ≤ |R| − 2.
- With the repaired (ii): kind B switches at steps ≤ L_B − 2 ≤ |R| − 3 (by (i)); kind A at steps ≤ max(L_B − 1, 0) + λ − 2 ≤ |R| − 4 (for
  L_B ≥ 1: L_B + λ − 3 ≤ |R| − 5; for L_B = 0: λ − 2 ≤ |R| − 4). So every switch of an event-free sub-run is at a step ≤ |R| − 3: (iii)
  holds with |R| − 3 in place of 2|R| − 4.
- So an event-free sub-run has ≤ |R| − 2 R-changing transitions, and the Corollary reads: the R-changing transitions of a U3 or U23 stretch
  number ≤ f + K_W + E + (K_W + f + E + 1)(|R| − 2). The packet's factor 2|R| − 4 also stands. E counts transitions containing an event
  (REFEREE's reading, §2 Corollary row).

## 5. DATA notes
- u2flat_n32 (L-RED box 35, l-red bee6487; experiments/red/xing/instances/u2flat_n32.pg, sha1 1a016c446d8c48b0e856d88b4527f61dfb1983e0;
  Lead re-run n5.py 13 iterations / 3 fallbacks, Oink OK, strategies verified, one Odd choice vertex): the first live U2 W-flat switches.
  - REFEREE: 2 U2 W-flat switches, at step 0. My box31/u23check.py: U2_sw 2, no violation (Lead run).
  - REFEREE-2: over 20 starts, 7 switches; the CASC-U2 bound is attained (step = ℓ − 2); 0 violations.
  - The kind-B half of CASC-U3, (i), is still vacuous in all data (REFEREE-2: 0 kind-B switches; 34,230 kind-A switches, max 1 below the
    bound).
- Gaps of my checker experiments/new/box31/u23check.py against the frozen packet (L-RED box 35; the checker tests less than the packet
  states; no lemma bug):
  - (a) U23 stretches are never classified or checked (9 on the pinned instances, nr_u23_n32 among them with 32 switches);
  - (b) (iii) is tested at 2|R|, not at the packet's 2|R| − 4;
  - (c) (ii) for kind A, and both Corollaries, are untested.
  L-RED's experiments/red/xing/u23x.py checks every statement exactly as stated: 0 violations on ~90 pinned 𝒞^1O instances. The packet's §4
  data line rests on u23check.py as written; read it with (a)-(c). Both referees' own checkers (REFEREE docs/referee/scratch/u23_probe.py,
  REFEREE-2 u23_check.py) cover U23 and (ii).

## 6. R-1 = N-U23-2: the θ-change count under ¬H1 (packet §3 READING)
Add to the READING: "Under ¬H1 (U2, U23), θ = (c_θ, ∅, d), so there are ≤ |R| − 1 θ-changes per phase (R15 (a))."
- Why (REFEREE §3): under ¬H1, o lies on C_Ξ, whose top is c_θ. So θ = Ξ(o) = (c_θ, ∅, d), with d ∈ [0, |R| − 1] the honest distance from o to
  c_θ. c_θ is fixed in the phase (λ_Ξ constant), and Ξ is monotone (R15 (a)), so d moves in one direction (fixed by c_θ's parity). Hence
  ≤ |R| − 1 θ-changes.
- Why it is needed: summing the stretch bounds over a phase needs the number of stretches, i.e. of θ- and w-changes. w-changes are F-changes
  under H2 (F1°) and are bounded by WC (R24) under ¬H2; θ-changes are F-changes under H1 (TF) and constant if λ_Ξ(o) = o; under ¬H1 a stretch
  can end at a θ-change with no F-change (REFEREE-2 saw 5 in 1,203 intervals, seed 811), which R-1 now counts. REFEREE-2 re-checked R-1 on
  1,364 ¬H1 states: closed.
- With R-1 the READING "(NH') reduces to (X), NFB-O, (E) and (K_W)" is complete as stated (REFEREE §3; REFEREE-2 §C.4).
- L-NEW (box 32, unrefereed, docs/new/N5-L-box32.md): the gate-level freeze proposed for (E), (K_W) is vacuous where it is needed, and
  the stronger merge via NO-WAKE is FALSE (instances/nowake_cex_n32.pg, a U3 state). (E) and (K_W) stay the open cores.
