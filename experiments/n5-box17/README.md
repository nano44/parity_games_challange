# Box 17: exhaustive small-n tables of SEG-COUNT excess, SEG(S), L-WAVE′ gap and f per phase (L-COMP successor 7)
Lead brief 2026-10-29 09:59Z (D18). Every number here is DATA. "Exhaustive at n ≤ N" means only: every game of the stated model, every
stated start pair. Nothing here proves any conjecture; none of the four is touched for n > N except by the random tables, which are
samples. Labels: CONJECTURE (L-SI's statements), OPEN, DATA.

## Definitions (L-SI's, verbatim sources)
- REL cutting: experiments/si/lwp/seglast.py `segs()`; text docs/si/N5-GRUN-box25.md §4 (Q, X_b, RO_b, CW_b, CH_b, REL-admissible, maximal
  segments from the run's end). Run key (λ_Ξ, τ) of RESULTS R38 (a); a run = maximal fallback-free stretch of a phase (L-SI's trace.runs).
- (a) SEG-COUNT excess: experiments/si/lay/segsw.py, EXC = (b − a) − #(Even vertices switching in [a, b]), over segments with b > a.
  CONJECTURE SEG-COUNT (L-SI, docs/si/N5-LAY-box27.md §6): EXC ≤ 0.
- (b) SEG(S): number of maximal REL segments of a fallback-free run S (runs with ≥ 1 transition). CONJECTURE SEG-RUN (N5-GRUN-box25 §5): SEG = O(n).
- (c) L-WAVE′ gap: experiments/si/grun/lwave.py PMODE=1 (events: non-L REL cuts, and every transition at which the path set of Ξ changes
  at an Odd choice vertex of RO_b); gap = distance between consecutive points of {run start} ∪ events ∪ {run end}.
  CONJECTURE L-WAVE′ (N5-GRUN-box25 §5, N5-LWP-box26 §0): every gap ≤ n − 1.
- (d) f(P): in-phase fallbacks of a phase P (transitions t → t + 1 with t, t + 1 ∈ P that take S4c). CONJECTURE FB-LIN (N5-ALT-box23 §13): f ≤ n.

## Implementation and cross-check (done BEFORE enumerating)
- box17.py: my own implementation of the four quantities from the text above, on L-COMP's engine n5b (experiments/n5-second, SPEC mode;
  shares no valuation code with L-SI's engine). Eng.step is n5b.N5.run's loop body unchanged; Eng.info adds Ξ, σ̄ (SPEC S1 choice), the
  honest and W successor maps and their cycle sets.
- xcheck.py + lsi_side.py: runs L-SI's own tools (seglast.segs, segsw's EXC formula, relseg.segcount, lwave.maxgap PMODE=1, common.phases +
  fb; L-SI's engine via experiments/new/box21/n5x.py) in a separate process and compares, field by field: the state sequence (σ_t, τ_t),
  fallback flags, σ̄_t, the runs, every REL segment (a, b), the excess of every segment, max SEG, max L-WAVE′ gap − (n − 1), f of every phase.
- Result: identical on every instance tried (0 mismatches):
  | set | instances | notes |
  | --- | --- | --- |
  | L-SI pins (start pinned where a .start exists) | seglast_kill_n110, seglast_kill_n29, hgrow_kill_n89, wgrow_kill_n90, psidrop_kill_n70 (l-si 668efcc1), lwkill_n31, lwp_gap_n26 (gap = n − 1 exactly, as L-SI reports), cycset_kill_n60, karena_kill_n71, setstep_kill_n71 | seglast_kill_n110 max EXC 0 ([11, 16]; [2, 8] has −1, as box 27 §6) |
  | fallback / SEG records | rise_fb38_n48 (f 37), ccl_w48_n48 (f 33), farrise25_n32 (f 25), lend107_n32 + start (f 10), run49_n32, pftheta34_n32 (SEG 24), grun/out/sg_2 (SEG 29 at n 29) | the f and SEG values equal L-SI's published maxima |
  | random (randx.py seed 1: 3,000 games n 2-8; seed 2: 1,000 games n 9-16; random start pair each) | 4,000 | |
- privar.py (model check): 6,000 runs (3,000 random games with repeated, unordered priorities in 0..n, n ≤ 8, a random start and S3): the
  trajectory (σ, τ, fb, σ̄, key) and all four quantities equal those of the game with canonical distinct priorities of the same
  (Ω, id)-rank and parity: 0 differences. So priorities matter only through rank and parity (the reduction used below).

## Enumeration model (stated assumptions)
- C(n): vertex ids 0..n−1; owners free; priorities distinct and increasing in the id (minimal values for the parity pattern of the ranks);
  every vertex any nonempty successor set (self-loops allowed, no multi-edges). 2^n · 2^n · (2^n − 1)^n games. No further dedup: with ids
  in rank order, the only relabelling preserving the rank order is the identity, and N5 is not invariant under relabelling (id tie-breaks),
  so C(n) has no symmetry to quotient. Every game with arbitrary priorities equals (privar.py) a game with distinct priorities; C(n) is the
  subset whose id order is the rank order.
- L(n) (--labelled): every rank permutation of the ids too (n! · |C(n)|): ALL games on n vertices up to priority values.
- Start pairs: ALL (σ0, τ0) = ∏_v |succ(v)| per game (every positional pair N5 admits); each state's N5 step is computed once per game.
