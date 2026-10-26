# R-N5-FX: REFEREE report on packet P-N5-FX (L-SI box 14: Corollary FX, crossings per phase)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 19:19Z (Lead's stamp).
- Object: docs/si/P-N5-FX-box14.md at trunk 02ad3f88, sha1 aa227b0b310b60c630a89afa248cd60ea04b66c3 (checked with `git show`; identical on
  my tree), 62 lines. Author: L-SI successor 9.
- Written 2026-10-25T19:52Z-20:13Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-FX* file. D1 applied.
- Premises re-read in their landed text: RESULTS R30 (c) (R-STICK and Corollary SN-PREFIX), R34 (e) TOGGLE-COUNT, R34 (f) X-SN-PHASE;
  P-N5-FBPOLY (my report R-N5-FBPOLY, 3de7cab7).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Corollary FX (a) (no hypothesis on f) | PROVED | SIGNED (note FX-N1: weaker than the landed R30 (c) SN-PREFIX bound) |
| §1 | Corollary FX (b) (CONDITIONAL on FB-POLY) | PROVED | SIGNED, conditional as labelled; its constant F* = 1 + (n − 2)(2n − 1) needs FB-POLY with the FBP-1 repair (note FX-N2) |
| §2, §3 | readings (T-K, …), data | not to sign | not signed |
- No (P). Landed premises: R30 (c), R34 (e), (f). The only premise in review is P-N5-FBPOLY, in (b).
- No gaps. Notes FX-N1, FX-N2, FX-N3.

## 1. Corollary FX: checked
- (a):
  - Every in-phase transition is S4a or an Even fallback (τ constant). So every crossing is (i) a fallback, (ii) S4a with c_w = c_θ, or
    (iii) S4a with c_w ≠ c_θ.
  - (ii) is X_SN's definition, which matches R30 (c) and R34 (f): "S4a crossings at states with c_w = c_θ".
  - (iii): R-STICK (R30 (c): "if c_w(s) ≠ c_θ, R_s ⊆ R_{s+1}") gives R_k ⊊ R_{k+1}.
  - Between cuts, R changes only at (iii) crossings, because non-crossings keep R. These grow R ⊆ V ∖ {o} strictly, so there are
    ≤ n − 1 per segment, with ≤ f + X_SN + 1 segments.
  - Correct.
- FX-N1 (citation): (a) is already LANDED in a sharper form.
  - R30 (c) Corollary SN-PREFIX: "per phase, crossings ≤ (f + 1)(n − 1) + f + X_SN" = n·f + n − 1 + X_SN. Inside a fallback-free run,
    the c_w = c_θ states form a prefix, so cuts at (ii) are not needed.
  - FX (a)'s n·(f + X_SN) + n − 1 is weaker by (n − 1)·X_SN. Both are correct. The lane may cite R30 (c) instead, and (b)'s constant then
    improves to n·F* + n − 1 + X_SN-bound.
- (b):
  - X-SN-PHASE (R34 (f)) is X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T, with T the per-phase toggle bound |U|(n + 1) + n − 1 ≤ n² + 2n − 1.
  - Both (a) and X-SN-PHASE are monotone in f and T, so substituting f ≤ F* and T ≤ n² + 2n − 1 is valid.
  - Orders: F* = O(n²), X_SN = O(d_o n⁵), X = O(d_o n⁶) = O(n⁷). Correct.
- FX-N2 (condition): F* = 1 + (n − 2)(2n − 1) is FB-POLY (a)'s final bound. My R-N5-FBPOLY signs it WITH GAP FBP-1: it needs
  |succ(o) ∩ Û| in place of deg_U(o) when o has a self-loop. Without the repair, use F* = 1 + 2n(n − 2). The order is unchanged.
- FX-N3 (scope): "So it covers TYPE H, TYPE Q and TYPE N phases alike" is right for (a), which has no phase-type hypothesis. The §2
  readings (T-K, and polynomiality of N5 on 𝒞^1O given K) are not signed. K stays OPEN, so G-N5-TIME stays OPEN.

## 2. Data (DATA, not proof; docs/referee/scratch/phifx_probe.py on rl_engine, logs scratch/phifx_logs/)
Per phase of every 𝒞^1O run, the probe:
- counts crossings X, in-phase fallbacks f and X_SN (S4a crossings at states with c_w = c_θ);
- checks R-STICK at each S4a crossing with c_w ≠ c_θ (R_k ⊊ R_{k+1});
- checks FX (a), the sharper R30 (c) bound, and (b)'s numeric bound.
Results:
- (L), 253 𝒞^1O games, 990 phases (phifx_logs/lib.log): X 3,661 in total (X_SN 2,867), max 100 in one phase. 0 failures.
- Random 𝒞^1O, 4,995 runs, 8,255 phases (phifx_logs/rand.log): X 142 (X_SN 124), max 2. 0 failures.
- The bounds are far from reached.

## §C. Comparison with REFEREE-2 (R2-N5-FX.md, referee-2 83a3e8c7, REFEREE-2 successor 13) (Opus 5.5, D15)
Written 2026-10-26T01:54Z by date -u, REFEREE successor 11. Routing: the Lead's message of 01:52Z (Lead's stamp). My report (843ba1f8,
successor 10) was pushed long before R2-N5-FX.md existed.
### C.1 Verdicts
| statement | REFEREE | REFEREE-2 |
| --- | --- | --- |
| FX (a) | SIGNED (FX-N1) | SIGN (N-FX-1) |
| FX (b) | SIGNED, conditional on FB-POLY (+ FBP-1 repair for F*) (FX-N2) | SIGN, now UNCONDITIONAL since R48 landed (N-FX-2) |
| §2, §3 | not signed (FX-N3) | not signed |
Agreement. The one difference is time: my condition on (b) was FB-POLY, which has since LANDED as RESULTS R48 with FBP-1 / FBP-2 repaired.
So I now agree that (b) holds unconditionally, citing R48 (i) in its repaired form.
### C.2 Joint note map
| REFEREE | REFEREE-2 | ruling |
| --- | --- | --- |
| FX-N1 ((a) is weaker than landed R30 (c) by (n − 1)·X_SN) | N-FX-1 (the same; a second derivation from R-STICK alone) | SAME. Fixes line: "(a) is implied by R30 (c); the proof here is a second derivation". |
| FX-N2 (F* needs FB-POLY with the FBP-1 repair) | N-FX-2 (cite R48 (i) (a) repaired, and (b), (c) for o = c_θ) | SAME core; REFEREE-2 adds the o = c_θ branch, which I did not treat: f ≤ |U| ≤ n ≤ F* for n ≥ 3 (2n² − 6n + 3 ≥ 0), and for n = 2, R48 (i) (b) (|U| = 2, repaired by FBP-2) gives f ≤ 1 = F*. I checked both steps: correct. ACCEPTED. Fixes line: "f ≤ F* by R48 (i) (a) (repaired) if o ≠ c_θ; by R48 (i) (b), (c) if o = c_θ". |
| FX-N3 (scope: (a) has no phase-type hypothesis; readings not signed) | — | REFEREE only; stands. |
### C.3 Data
REFEREE-2: 1,509 library runs (S3 + 2 random starts), 6,000 random; 0 violations; max X / FX (a) bound 0.660. Mine (R-N5-FX §2, phifx_probe.py): 0
failures. No disagreement.
### C.4 Result
P-N5-FX (a), (b) signed by both; (b) unconditional now (R48). Crossings per phase: X = O(d_o n⁶) (R30 (c)'s form gives the same order).
