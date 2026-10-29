# R123: CONJECTURE RESET-LIN-S is false. A switcher that leaves and re-enters R120's wave observer once per pivot cycle puts all of the observer's MATCHED P-changes inside one span: #MAT^span = (K − 2)(m − 1) + K, 482 > n = 346 at K = 12 (fallback-free, τ constant). PCH-QUAD-S is not touched (PCH^span ≈ n²/196). READING: PCH-QUAD-S can only fail on a λ-run longer than n² + n
L-RED successor 31 (Opus 5.5; D1/D18; Lead 2026-10-29 22:19Z STEP 1: "attack the fleet's cleanest single target for G-N5-TIME ...
CONJECTURE PCH-QUAD-S ... Also RESET-LIN-S, CARRY-SEG-S and MIN-QUAD ... What a kill needs: one pair (v, c) where v leaves c and
re-enters it later ... Report at the first super-quadratic sign, or at a clear obstruction."). Written 2026-10-29 from 22:49Z (date -u).
Targets: L-SI docs/si/N5-SPAN-box38.md §3 and N5-SPANW-box39.md §3 (l-si dab44572, read only). Labels: DATA / DEAD / READING / OPEN.
Not a TARGET.md claim. G-N5-TIME stays OPEN: everything here is quadratic.

## 1. The device (DATA; experiments/red/span/spanobs.py)
- Base: R120's game, mkr.py K m (m = 4K) + obs2.py (Odd observer o -> y_j -> r_j, Xi(o) = min_j q_j + Xi(r_j)).
- Added (3 vertices, no in-edges into them except e -> o, so mkr's σ-run is unchanged):
  - e: Even, priority 0, edges {o, d}; start σ(e) = o.
  - d: Odd, priority 0, single successor h′ (hp). So Xi(d) = Xi(h′), W(d) = W(h′).
  - yh: Odd, priority q_h = Z − 1 + 2(m + 1) (even, above every q_j, below the shifted range), single successor h; o gets the extra edge
    o -> yh and τ(o) = yh. Xi(o) is still the reactor minimum (q_h + Xi(h) is above it); W(o) = q_h + W(h).
- Why the W-route is needed (first version without yh: e never moved: (e, d) was in I_σ at every h′-step but the W step kept o; scratch check). N5's Even step takes, among {σ(e)} ∪ I_σ(e), the
  W-best option against τ, and W ≥ Xi pointwise. With τ(o) = y_1, W(o) beats W(d) at every state. With yh, e's W comparison is h against
  h′, the same comparison the reactors make, and it leapfrogs.
- Trace (K = 4): e leaves o at the h′-step (Xi(d) = V_i beats the reactors' H_i; W(h′) beats W(h)) and re-enters right after
  (t 18 -> 19 leave, 20 -> 21 re-entry; again at 37/39, 56/58, 75). The out-windows are short; the waves (o's P-changes) fall in the
  in-windows. The span (first leave to last re-entry) holds every wave except the first and the last.

## 2. Counts (DATA; two counters, Even side, one λ-run of Xi carries the whole run)
| K | m | n | iterations | win.py span(e, o) MAT / PCH | spanc.py span(e, o) MAT / PCH | RESET-LIN-S (MAT^span ≤ n) | spanw.py WCH^span(e, o) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 122 | 76 | 33 / 38 | 34 / 39 | holds | not run |
| 8 | 32 | 234 | not recorded | 193 / 206 | 194 / 207 | holds | not run |
| 12 | 48 | 346 | 612 | 481 / 502 | 482 / 503 | FAILS (win.py: RESETLINS FAIL) | 11 |
- win.py = L-SI odd/win.py (SIDE=E; engine L-NEW n5x / L-SI si.py; MATCHED from L-SI compose.matched), run from a worktree of
  origin/claude/l-si. spanc.py = mine: n5b SPEC trace, MATCHED test from mix/matc.py (written from RESULTS R85, not from L-SI's code).
  spanc counts the re-entry transition itself, win.py's span is half-open: the difference is exactly 1 in every row.
- Fit (spanc, 3 rows): MAT^span = (K − 2)(m − 1) + K; n = 28K + 10. RESET-LIN-S fails from K = 10 (322 > 290).
- CARRY-SEG-S: SEG 1 on every row (holds). MIN-QUAD: max min(PCH, WCH) = 22 at K = 12 (holds). spanw.py at K = 12: pair (e, o)
  PCH 502, WCH 11, τ constant on all of them (TQ = PCH), 0 fallbacks.
- Pin experiments/red/span/instances/spanobs_K12_m48.pg (sha1 5384eab66ea4fb7d10683d63f995404fe7264abd), .start
  (af48ece498911e9b9b5af05c2b7bf0cce8a3d099). vrun_spanobs_K12_m48.txt: n5b SPEC 612 iterations, 0 fallbacks; L-NEW n5.py (si.py
  engine) 612, 0; state sequences identical (xeng.py); both final solutions: Oink zlk OK, strategies verified (check_sol2.py).
- check.sh gate: regenerates the pin; spanc on K = 4: pair (119, 102) MAT 34 PCH 39.

## 3. Reading
- DEAD: CONJECTURE RESET-LIN-S (#MAT^span ≤ n). The span form is as reader-inflatable as the λ-run form (R120) once the switcher
  oscillates: Lemma SPAN's span is [first leave, last re-entry], and one vertex that leaves and re-enters once per cycle makes it the
  whole run. Cost: 3 vertices.
- DEAD as a fallback-free statement too: box 39's "PCH^span ≤ WCH^span + O(n)" was killed with fallbacks (rise_thin51_n40); here
  PCH^span − WCH^span = 491 > n at K = 12 with 0 fallbacks and τ constant. Obstruction: Xi(o) follows Odd's honest minimum (the wave's
  argmin), W(o) follows τ(o) = yh -> h, which changes only at pivot steps.
- Not killed: PCH-QUAD-S. Here PCH^span ≈ 4K² ≈ n²/196.
- Why PCH-QUAD-S is out of reach of this whole design class (READING, elementary):
  1. PCH^span_R(v, c) ≤ |span| ≤ |R|: at most one P-change of c per transition. So a kill needs a λ-run of more than n² + n
     transitions.
  2. Longest λ-runs known in the fleet: mkr 4K² + 3K − 1 at n = 24K + 6 (≈ n²/144, R106); hntop 3N² + 13N − 5 at n = 21N (≈ n²/147,
     R109); this family ≈ n²/196 inside the span.
  3. Every such family is a product of two factors: a clock (K pivot levels at a ≥ 1 vertices each) times a chain (m reactors at
     b ≥ 1 vertices each), L ≈ K·m with aK + bm ≤ n, so L ≤ n²/(4ab) ≤ n²/4 < n² + n. A kill needs a third multiplicative factor
     (nesting, R106 OPEN (4); R108: backpressure, first attempt mk3 failed).
  4. So PCH-QUAD-S ⇐ "every λ-run has ≤ n² + n transitions" (RUN-QUAD). With R47 Lemma Φ (≤ 2n(n − 1) + 1 joint λ-runs), RUN-QUAD
     alone gives T ≤ (2n(n − 1) + 1)(n² + n), with no use of Lemma SPAN.
  5. Conversely, if N5 is polynomial, every λ-run is, and so is PCH^span. With Lemma SPAN + span COMPOSE, "PCH^span ≤ poly(n)" is
     therefore EQUIVALENT to G-N5-TIME (given R47). The reduction re-expresses the target; it does not weaken it. The only content of
     PCH-QUAD-S beyond G-N5-TIME is the exponent.
- OPEN, next: a super-quadratic λ-run (a third factor). Nothing in this box approaches it.

## DONE / FINDINGS / NEEDS
- DONE: span/spanobs.py (device), span/spanc.py (second span counter), pin spanobs_K12_m48 + vrun output, check.sh gate, this note.
- FINDINGS:
  1. DATA: span(e, o) MAT = (K − 2)(m − 1) + K; 482 (spanc) / 481 (win.py) > n = 346 at K = 12; two engines state by state, Oink OK.
  2. DEAD: CONJECTURE RESET-LIN-S. Also the fallback-free form of "PCH^span ≤ WCH^span + O(n)" (491 > n).
  3. DATA: CARRY-SEG-S, MIN-QUAD, PCH-QUAD-S hold on the family (SEG 1, MIN 22, PCH^span ≈ n²/196).
  4. READING: a PCH-QUAD-S kill needs a λ-run > n² + n; two-factor designs give ≤ n²/4; PCH-poly-S ⇔ G-N5-TIME given Lemma SPAN + R47.
- NEEDS: none from the owner.
