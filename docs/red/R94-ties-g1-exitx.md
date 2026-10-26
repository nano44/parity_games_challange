# R94: STATIC-DEPTH's gaps (G4) ties and (G1) σ̄ changes, and EXIT_x at fixed k: no kill; data, a reduction and the obstructions
L-RED successor 22 (Opus 5.5; D14/D15/D18; Lead 18:03Z (EXIT_x), 18:25Z ((b) ties / (G1) first, then (a))). Written 2026-10-26 ~19:0xZ
(date -u). Labels (D18 / L40): DATA / READING / OPEN. Targets: docs/si/N5-GCILEN-box22.md §5 (l-si 14ba9204) (G1), (G4);
docs/si/N5-EXIT-box22.md §7 (2) (l-si a5d5c0c8).

## 1. EXIT_x at fixed k: a reduction (PROVED, trivial) and where re-arming fails (READING)
- EXIT_x ≤ the phase length: there is at most one exit change of x per transition. So super-linear EXIT_x at fixed k needs a phase of
  length ω(n) at fixed k.
  - None is known. The data maximum is ≈ 3n: long121 (k = 3), nep90 ≈ 2.3n, L-NEW's qpcclimb 127 at n = 48, phclimb 125 at n = 48.
- The other factor is easy. An Odd x of large out-degree (free at fixed k) reading chain positions can move its σ̄-minimum at every wave
  tick, so EXIT_x ≈ phase length is plausible.
- FB-C (RESULTS R71) allows ≤ 4n² in-phase fallbacks per configuration. A phase of ~n/2 fallbacks, each re-arming a ~n/2 Bellman-Ford
  wave over one shared chain in alternating directions, would give ~n²/4.
- Blocked step: at each fallback the NEXT top must become the end vertex's choice.
  - S4c's switch-all takes the Ξ-BEST improving successor, so static increasing tops at one end are all taken at the first fallback.
  - One top per end vertex fails too: a static top's improving-ness is monotone the wrong way (the end vertex's own value only rises).
  - Dynamic tops need triggers. W-triggers fall under R91 §6 (O1)/(O2). Ξ-triggers that read the chain close Ξ-cycles when the wave
    reverses.
- Untried design (the Lead's (a)): an Odd-minimum "next-top selector", i.e. the end vertex's only top is an Odd vertex of large
  out-degree whose σ̄-minimum rises one option at a time.

## 2. (G4) W-ties (DATA, abstract model)
experiments/red/ties/abstie.py is the cyclic abstract model of N5-ABSCYC §1 WITHOUT GEN.
- It uses N5's kind of tie rule: among N-optimal arena strategies, the lexicographically smallest successor-index vector (S4a picks the
  first maximum in successor-list order).
- Values carry length, so a tie needs equal weight AND equal length, as in N5.
- Random runs: 3,000 games each at n = 4 and 5, with small values (ties frequent). No run is longer than n (max 4).
- Climbs: four at n = 5 (6,000 steps) reach exactly 5; two at n = 6 (3,000 steps) reach exactly 6.
- READING (each step elementary): after W settles (ABS-DEPTH's (B) holds without GEN), every further switch keeps W and raises M. So the
  switching vertex moves to a region with a strictly smaller W − Ξ gap, and the gap depends only on the first gate of its W-play.
  - Hence ≤ (number of distinct gaps) tie-switches per vertex; with an index rule, also ≤ deg(v).
  - A sequential tie cascade needs W-tied options of equal length at every step of a chain, i.e. extra vertices per step.
  - I found no structure that beats n.

## 3. (G1) σ̄ changes inside a global C-interval (READING; DATA)
- Mechanism (READING). A σ̄ change at a non-direct gate u moves Ξ (honest frame) and leaves W alone, so it is a free Ξ-trigger: arena edges
  into u's region appear.
- The pump: Even vertices on gate u's minimum option enter another gate u′'s region. That disables or raises the option, so σ̄(u) moves
  to the next minimum and Ξ(u) rises. Then the vertices on u′'s minimum option can enter u, and so on.
  - This is an ALTERNATING CASCADE between two gates of large out-degree, at k = 2.
  - Each step consumes one option and its Even vertex. An option whose path re-enters through the other gate's σ̄ is disabled (it would
    close a Ξ-cycle), so the cascade ends after ≤ (sum of out-degrees) steps. That is linear, with ≥ 2 vertices per step.
  - Re-use would need option values to leapfrog, which needs triggers again: the same wall as §1 and R91 §6.
- DATA:
  - ulx.py (G_LEN_SLACK_SB) on lib41 (S3 + 2 random starts, n ≤ 64): 448 of 4,122 global C-intervals contain a σ̄ change. The longest is
    [0, 18] at n = 24 (experiments/new/box28/instances/oc24_s4_final.pg, S3 start, 2 σ̄ changes), slack −5.
  - Climbs (experiments/red/ties/gclimb.py: box43 mutate with the Odd choice set fixed; objective = longest σ̄-changing global C-interval
    of a λ_W-constant fallback-free run, minus (n − 1); 3,000 steps each, n ≤ 40):
    - from oc24, seeds 1 and 2: no improvement (−5);
    - from b6_xs_n24 (k = 1, gate-free), seeds 3 and 4: no σ̄-changing interval found.
    The climb is weak (S3 starts, few accepted moves). This is not evidence for GCI-LEN.

## 4. Tools added
- ulx.py: PURE_SW_SLACK / PURE_SW_2N (the last Even switch in a pure C-interval against ABS-DEPTH's (|A_a| − 1) + |U_c| and against 2n)
  and G_LEN_SLACK_SB.
  - On the pins every pure interval is quiet well before the bound: slack −42 on run49, −66 on long121.
- experiments/red/ties/abstie.py, gclimb.py.

## 5. OPEN (for successor 23)
- The Odd-minimum next-top selector (Lead's (a), time-boxed ~2 h).
- (G3) a cyclic H_b at an impure end (reader_L already fails (H3)/(H4) but stays below n − 1).
- A k = 2 or 3 alternating-gate structure whose options are RE-ENABLED (a gate's σ̄ path stops leading back), to test whether the §3
  cascade can re-use options.
