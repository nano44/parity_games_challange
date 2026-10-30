# N5-SBAR (box 75): ρ per phase is breadth (1198 = 15n on the corpus), and Odd's reply σ̄ is NOT a chain in any order inside a phase (thetaA_n7: σ̄(6) = 5 → 1 → 5). So no potential of σ̄ alone works
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 06:38Z (read 07:03Z, after box 74 was pushed): «BOX 74: ρ-POLY, per phase, the R56 ρ
… try a D18 angle on the Odd side's σ̄-changes inside a phase: τ is fixed and Ξ is monotone. Is σ̄'s sequence a monotone path in a
polytope, a matroid basis exchange, or a lattice chain? Proof or exact obstruction.» Box 74 had already done ρ per W-run. This box does
the per-PHASE version and the σ̄ question. Written 07:04Z-07:10Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME
OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Definitions:
  - Phase: (λ_Ξ, τ) constant (R38 (a)).
  - ρ_P: R56's ρ, the pairs (transition of P, q ∈ Q) with Ξ(q) changing; Q is the set of Odd vertices of out-degree ≥ 2.
  - SBQ_P: the pairs with σ̄(q) changing.
  - REVISIT: a change of σ̄(q) to a successor that q already held earlier in the phase.
  - VECTOR RETURN: σ̄|Q equals an earlier vector of the same phase, after having changed.
- Tool box75/sbq.py; run.sh gives sbq_*.txt (1132 runs × N5 and N5-LZC).

## 1. DATA (N5; N5-LZC is the same up to ±1 %)
- ρ per phase:
  - corpus max 1198 at n 80 (new/box48/out/qpcclimb/scale/snap_n80_s62, alt start): 15.0n;
  - box 74's cr_n80: 910 in one phase.
  - The figure "0.79n" from earlier data is far exceeded. ρ per phase is breadth, as per W-run (box 74).
- SBQ per phase: max 282 (snap_n80_s62); max ratio 4.3n (best_qpc_nep76_n40_s63, n 64).
- SBQ_P / Σ_{q∈Q}(deg q − 1): up to 13.2, on red/usplit gate_K64_n581 (|Q| 5, all degree 2). There a degree-2 Odd vertex flips Θ(K) times
  in one phase, so SBQ per q is not bounded by its degree.
- REVISITS: 3951 in 229 of 1132 runs.
- VECTOR RETURNS: 1706.
- Smallest instance: n5-exhaustive/instances/thetaA_n7.pg (sha1 cd2a3bc8d7b06ef21e588ac9a33e7505ff8fb1b9) with its alt_all start
  thetaA_n7.start (SIGMA0 0:4 1:6 2:2 3:2 4:2 5:4, TAU0 6:5).
  - n 7, one Odd choice vertex 6 with successors {1, 5}, 3 iterations, ONE phase (λ_Ξ ≡ 2, τ(6) = 5 throughout).
  - σ̄(6) goes 5 → 1 → 5. Even's switch 5: 4 → 0 at 1 → 2 makes 1 the better reply. Even's switch 1: 3 → 6 at 2 → 3 makes 1 → 6 → 1 a
    cycle and sends Odd back to 5.

## 2. DEAD: every potential that is a function of σ̄ alone
- Statement. There is no function Φ of Odd's strategy σ̄ (or of σ̄|Q) that is strictly monotone along the σ̄-changes of a phase of N5.
  The same holds for N5-LZC.
- Instance: thetaA_n7 + start, where σ̄|Q = (5), then (1), then (5) in one phase. A strictly monotone Φ would need Φ(5) < Φ(1) < Φ(5).
- So the three D18 templates fail in their plain form, on σ̄'s own sequence:
  - a monotone path in a polytope whose vertices are Odd strategies;
  - a basis-exchange walk (each step a strict improvement of some fixed weight);
  - a chain in a lattice of Odd strategies.
  Each needs a strictly monotone σ̄-potential.
- Per vertex too: "σ̄(q) never revisits a successor inside a phase" (which would give SBQ_P ≤ Σ(deg q − 1)) is DEAD at the same instance.
  gate_K64_n581 shows a ratio of 13.2 against Σ(deg − 1).
- Exact obstruction. σ̄_t is Odd's optimal reply to σ_t (one-player optimum on G_{σ_t}). In a phase σ_t moves by S4a and S4c, and each
  Even move changes the costs of Odd's options in a different direction:
  - a switch can make an option better for Odd (5: 4 → 0 lowers Ξ through 1, for Odd);
  - it can also close a cycle that makes the option bad for Odd (1: 3 → 6 creates the cycle 1 → 6 → 1).
  Odd's argmin therefore LEAPFROGS between options. The monotone quantity is Ξ (R15), a function of the PAIR (σ, σ̄), not of σ̄. Any chain
  argument must carry σ, i.e. go back to the Ξ-route.

## 3. What does hold (PROVED, lane; trivial but the right normalisation)
- ρ_P(q) ≤ |P| and SBQ_P(q) ≤ |P| (|P| = the transitions of the phase), so ρ_P ≤ |Q|·|P| and SBQ_P ≤ |Q|·|P|.
- SBQ_P(q) ≤ ρ_P(q) is FALSE as a general claim. σ̄(q) can change while Ξ(q) stays equal (a tie between options, broken by the S1
  procedure). DATA: 352 such changes in the 2264 runs (both engines), e.g. ffin12_n32 and nep13_n24. So SBQ and ρ are incomparable per
  (phase, q).
- So phase length polynomial ⇒ ρ-POLY per phase (factor |Q| ≤ n). The converse is NOT shown: R56 bounds fallbacks by ρ, but nothing here
  bounds a phase's S4a steps by ρ. READING: ρ is breadth inside the phase; the depth quantity is the phase length, as the W-run length was
  for box 74.

## 4. READING, a D18 pointer (not a citation)
- Odd's reply σ̄_t, as σ_t moves, is a PARAMETRIC one-player optimum: the same graph with costs that change over time. In parametric
  shortest-path problems, the number of optimal-path changes along a one-parameter family of linear costs is known to be able to be
  superpolynomial. I have NOT opened a source for this, so it is not cited and must not be used.
- The difference: here the "parameter" is Even's whole strategy, and the costs move monotonically in Ξ's order (R15).
- Request for L-LIT, through the Lead: the exact parametric-shortest-path breakpoint bounds (upper and lower, with sources), and whether
  a MONOTONE (non-linear) cost path admits a better bound. That is the precise form of the Lead's "monotone path in a polytope" question
  once σ is carried along.

## DONE / FINDINGS / NEEDS
- DONE: box75/sbq.py, run.sh, sbq_*.txt (1132 × 2); this note; check.sh "box 75" (pins thetaA_n7 + start).
- FINDINGS:
  1. DATA: R56's ρ per phase reaches 1198 = 15n (snap_n80_s62, corpus); it is breadth. SBQ per phase ≤ 4.3n; per q up to 13.2 × (deg − 1).
  2. DEAD: every strictly monotone potential of σ̄ alone, and with it the plain polytope-path, basis-exchange and lattice-chain templates
     on σ̄'s sequence. Instance n5-exhaustive/instances/thetaA_n7.pg + .start (sha1 cd2a3bc8…), σ̄(6) = 5 → 1 → 5 in one phase, n 7,
     one Odd choice vertex. Also "no revisit per q" is DEAD there (3951 revisits, 1706 vector returns in the corpus).
  3. Obstruction: Odd's best reply leapfrogs. Even's moves lower one option's cost and close cycles on another. The monotone object is Ξ
     of the pair (σ, σ̄).
  4. PROVED (trivial): ρ_P ≤ |Q|·|P|, so phase length poly ⇒ ρ-POLY. The converse is not shown. "SBQ ≤ ρ per (phase, q)" is FALSE
     (352 tie changes in the data).
  5. OPEN request: L-LIT on parametric shortest-path breakpoint bounds (no source opened by me; not cited).
- NEEDS: none from the owner. From the Lead: (a) route the L-LIT request if useful; (b) choose the next box (TIE for plain N5, LZ-NOC, or
  phase length via a (σ, σ̄) pair potential).
