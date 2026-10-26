# R-N5-NH42: REFEREE report on packet P-N5-NH-box42 (box 42: Lemmas SW, ST, CL, STR-COUNT, NR, Theorem NH)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's messages of 20:12Z and 20:21Z (Lead's stamps): "the bridge lemma for the per-phase bound, so it gets the same care
  as FBPOLY".
- Object: docs/new/P-N5-NH-box42.md at trunk 54ac72e6, sha1 93d19be8018e07a2727bbe1db5920198a0beb1eb (checked with `git show`; identical
  on my tree), 261 lines. Author: L-NEW successor 21. It is a different object from the box-30 P-N5-NH (RESULTS R22).
- Written 2026-10-25T20:25Z-20:32Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-NH42* / R2-N5-NH-box42* file. D1 applied: each statement treated as
  wrong until its proof was checked line by line.
- Premises re-read in their landed text, quoted where used:
  - RESULTS R15 (a), (d), including "at most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged";
  - R19 (a) G (a); R21 (g) Theorem X, (i) X-1;
  - R22 (a) F1° "OTHER states included", (b) TC (i)-(iv), (c) P3′ on (θ, w)-pieces;
  - R24 (d) Theorem U1, (e) Lemma WC with N-U1-3's sharpening "only fallbacks at OTHER states count in f_I";
  - R26 (b) U2 Corollary, (d) U3/U23 Corollary; R38 (a) KEY.
- Tools: own engine (scratch/rl_engine.py) and a new probe scratch/nh42_probe.py; no lane code (nhcheck.py not run).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma SW (a), (b) | PROVED | SIGNED |
| §2 | Lemma ST (a)-(c) | PROVED | SIGNED |
| §2 | Lemma CL (a)-(c) | PROVED | SIGNED |
| §3 | Lemma STR-COUNT (a)-(d) | PROVED | SIGNED |
| §3 | Lemma NR | PROVED | SIGNED (note NH42-N1) |
| §4 | Theorem NH (a), (b), (c) | PROVED | SIGNED |
| §4 Remarks, §5, §6, §7 | readings, input statuses, map, data | not to sign | not signed |
- No (P). Landed premises only. No hypothesis on H1, H2, H3, τ(o), c_w, θ.
- No gaps. Notes NH42-N1..N3.
- Scope: Theorem NH is a REDUCTION. It bounds O and the phase length by polynomials in X, f^O, K_W and E per phase. (E) and (K_W) are
  OPEN, so this is not a running-time bound for N5, not a TARGET.md claim and not a step-4 pass. G-N5-TIME stays OPEN.

## 1. Lemma SW: checked
- (a), honest frame:
  - Off o, every Odd vertex is forced and σ̄ = τ. So the honest play and the W-play from v ∈ R both follow π_v to o.
  - H1: o's honest play never returns to o. It cannot meet π_v either: from such a vertex the honest play (= (σ, τ)-play off o) would
    reach o. So no vertex of π_v is its own cycle node, and (V1) gives Ξ(v) = π_v ⊕ θ.
  - ¬H1: C_Ξ ⊆ R, because its vertices reach o along it with honest = (σ, τ) moves off o. Its top is c_θ.
    - c_θ ∈ π_v: Ξ(v) is read off π_v.
    - c_θ ∉ π_v: the prefix is π_v, then o, then o's path to c_θ along C_Ξ. It is simple: on a simple cycle, the forward arc from o
      reaches c_θ before re-entering the arc through π_v. Its vertices after π_v rank below c_θ, o included. So
      Ξ(v) = (c_θ, A(π_v), |π_v| + ℓ(θ)).
    - Correct.
- (a), W frame: symmetric, with TC (i) for τ(o) ∈ F under H2.
- (b): on a stretch, R, θ and w are constant; routes depend on σ over R's Even vertices only (τ is a phase constant). So no switch on R
  means no change of Ξ or W on R. Correct.

## 2. ST and CL: checked
- ST:
  - The four clause patterns follow TC (ii), TC (iii), the ¬H1 ∧ H2 argument (c_θ ∈ R, c_w ∈ F, hence θ ≠ w and OTHER), and TC (iv).
  - TC (ii)'s "all OTHER or none" agrees with the definitions. Under H2 with (h) failing, either H3 fails (θ ≠ w) or H1 fails, and then
    c_θ ∈ R while c_w ∈ F. Either way no state is EQ.
  - Correct.
- CL:
  - (a) H1, H2 constant on I (TC (i)); c_θ a phase constant; c_w constant on S.
  - (b) The four patterns are all handled. ¬H1 ∧ ¬H2 with both frames in route form forces θ = (o, ∅, 0) = w, i.e. EQ (TC (iv)). The
    piece ⇔ route-form-stretch equivalence holds, because route form is a function of (H1, H2, c_θ, c_w).
  - (c) matches R26's class definitions.
  - Correct.

## 3. STR-COUNT and NR: checked
- STR-COUNT (a): H1 by X-1 (R21 (i)) plus F1°. ¬H1: θ = (c_θ, ∅, d) with d ∈ [0, |R| − 1], monotone by MONO (d = 0 throughout if
  o = c_θ). Correct.
- STR-COUNT (b): H2 gives w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F, then F1°. ¬H2 is WC as landed (with N-U1-3's sharpening). Correct.
- STR-COUNT (c), (d): a new stretch starts only at a θ- or w-change. The arithmetic (f + 1)(|R|² − 1) + f = (f + 1)|R|² − 1 and
  Σ_I ≤ n²(2X + 2 + f^O) checked. Correct.
- NR: each class bound is the landed one applied to S. Lemma CL makes P3′ / U1 stretches into pieces. Each landed count includes every
  Ξ-change on R: directly (P3′), as "changing Ξ, W or σ on R" (U1, U2C), or, if U3C's "R-changing" means a switch on R, through SW (b).
- NR arithmetic, all re-done:
  - U1: (A + 1)(r − 1); for r ≥ 3, ≤ (f + 1)(n³ − 4n² + 7n − 4) ≤ (f + 1)n³.
  - U2: A(r − 1) − 1.
  - U3: A(2r − 3) − 1.
  - Crude line: n³ ≥ 2n for n ≥ 2.
  - Correct.
- NH42-N1 (precision): K_S and E_S enter only through U2C / U3C as landed, i.e. as the counts R26 defines (non-fallback W-changes on R;
  transitions containing an event). My probe recomputes both from their definitions (§6). They match the lane's per-phase maxima
  exactly, so the definitions are read the same way.

## 4. Theorem NH: checked
- Step 1:
  - The three kinds cover every OTHER-touching transition. A non-crossing with θ and w unchanged keeps R, θ, w, so both ends lie in one
    stretch. That stretch is OTHER by ST (c).
  - The second kind is counted within Σ_I (Θ_I + WC_I) ≤ N.
- Step 2: R15 (d)'s "≤ 4n(n − 1) consecutive iterations with Ωσ and Ωτ unchanged". Ωσ = Ξ (SPEC S1), and Ωτ is fixed because τ is.
  So an OTHER stretch has ≤ D·(N_Ξ(S) + 1) transitions.
- Step 3:
  - F1° per interval sums over its stretches, since they are disjoint runs: ≤ n − 1 per interval, ≤ n(X + 1) per phase.
  - The number of OTHER stretches is ≤ N.
  - Σ N_R by NR, with Σ_S f_S ≤ f^O (a fallback inside an OTHER stretch starts at an OTHER state), Σ K_S = K_W, Σ E_S = E.
- Steps 4-6: (a) as stated.
  - (b): Q·(1 + 2n² + 4n³ + 8n⁴ + 4n⁵ + 8n⁷) + 8n³(K_W + E) with the five low terms < 2.33·n⁷ for n ≥ 2. So O ≤ 11n⁷Q + 8n³(K_W + E).
  - (c): THM-X with (3n² + 1)·D ≤ 13n⁴ and 1 + X + O ≤ 12n⁷Q + 8n³(K_W + E): 156n¹¹Q + 104n⁷(K_W + E). Every inequality checked.
  - Correct.
- NH42-N2 (scope): "So (NH′) follows from (X), NFB-O, (E) and (K_W), each read as polynomial per phase" is exactly the theorem's
  content. I sign it as a conditional statement (an implication), not as a claim that any input is polynomial.
  - §5's statuses ((X) via P-N5-FX, NFB-O via P-N5-FBPOLY) are readings, not signed. Both referees have since signed FBPOLY, and FX
    awaits REFEREE-2.
  - FX's F* needs FBPOLY with the FBP-1 / N-FBP-2 repair (or F* = 1 + 2n(n − 2)). The order is unchanged.
- NH42-N3 (wording): §0.1 defines R with o ∈ R (the R22 convention), while P-N5-FX and R30 use R without o. NH's counts (crossings,
  intervals) are the same under either convention, since o ∈ R̄ always. Worth one line where §5 cites FX.

## 5. Not signed
- §4 Remarks, §5 (input statuses, READING), §6 (map to R22 / R24 / R26: checked, consistent, a reading), §7 data.
- (E) and (K_W) are OPEN. G-N5-TIME stays OPEN.

## 6. Data (DATA, not proof; docs/referee/scratch/nh42_probe.py on rl_engine, logs scratch/nh42_logs/)
For every phase, the probe recomputes intervals, stretches, EQ / THR / OTHER, the class of each OTHER stretch, N_R, N_F, K_S (U2, U3, U23),
E_S (U3, U23; kind A iff c_w ∈ π_v; an event is a kind change at a switched Even R-vertex, or a switch of c_w), Θ_I, WC_I and f^O_I. It
checks ST, CL (b), SW (b), STR-COUNT (a)-(d), F1°, both NR bounds per class, the per-stretch bound D·(N_R + N_F + 1), Theorem NH (a)-(c)
and THM-X.
- (L), 253 𝒞^1O games, SPEC S3's start (nh42_logs/lib.log): 990 phases, 101 with O > 0, ΣO = 833.
  - OTHER stretches by class: P3′ 131, U1 353, U2 66, U3 104, U23 51.
  - Per-phase maxima: O 77, X 100, T 112, f^O 12, K_W 25, E 15. Max N_R per stretch: P3′ 9, U1 12, U2 25, U3 14, U23 8.
  - 705 NR checks, 552 SW checks. 0 failures.
  - Every one of these counts equals the packet's §7 library figures. An independent engine, written from the SPEC, reproduces the lane's
    K_W and E exactly, which supports NH42-N1.
- (L) with 3 random start pairs per game (759 extra runs; nh42_logs/lib_rand3.log): 4,202 phases, 388 with O > 0, ΣO = 1,749.
  - Classes: P3′ 419, U1 1,046, U2 310, U3 440, U23 202.
  - 2,417 NR checks, 1,327 SW checks. The maxima are unchanged.
  - 0 failures.
- As the packet says, the bounds are far from reached (max O = 77 against 11n⁷(1 + X + f^O)). The data test the steps, not tightness.
