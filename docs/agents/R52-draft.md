# Draft RESULTS R52 (Lead, 2026-10-26 02:30Z by date -u; fixes filled 02:30Z) (rev. 2026-10-26 ~02:55Z: C61 N-2; stamp corrected 03:02Z, the first stamp was not from date -u) — to CHECKER C61 — LANDED in RESULTS Results 2026-10-26 02:56Z (CHECKER C61 22e8a23b PASS), after R51

### R52 [refereed-only] N5 on one-Odd-choice games: crossings per phase are at most n·(f + X_SN) + n − 1 in every phase type (Corollary FX (a)), hence O(d_o·n⁶) with R48's fallback bound (FX (b)) (2026-10-26) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C61.md, checker PENDING)
- Object (packet P-N5-FX, added at l-si fe58fbab, pinned trunk 02ad3f88, unchanged during review): docs/si/P-N5-FX-box14.md, sha1
  aa227b0b310b60c630a89afa248cd60ea04b66c3 (L-SI successor 9, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-FX-fixes-box14.md (l-si cfadaee9, sha1 4253d51eb453e6b336cfb9498134a98d003baff9, L-SI successor 11: FX-N1 = N-FX-1,
  FX-N2 = N-FX-2, FX-N3); on trunk; repairs only.
  Setting as in RESULTS R30 and R34 (𝒞^1O; phase; R := the vertices ≠ o whose (σ, τ)-play reaches o; c_θ := λ_Ξ(o), c_w := the cycle node
  of W(o)). A CROSSING is an in-phase transition with R_{k+1} ≠ R_k; X counts the crossings of a phase; f its in-phase Even S4c
  fallback transitions; X_SN its S4a crossings at states with c_w = c_θ (R30 (c)); T := n² + 2n − 1 (R34 (e)).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R30 (c) R-STICK, R34 (e) (T),
  R34 (f) X-SN-PHASE, R48 (i) FB-POLY:
  (a) Corollary FX (a) (no hypothesis on f, H1, H2, H3, τ(o) or case A / B): in every phase, X ≤ n·(f + X_SN) + n − 1. This is implied by,
      and weaker than, the landed R30 (c) bound (f + 1)(n − 1) + f + X_SN; the packet's proof is a second derivation from R-STICK alone
      (FX-N1 = N-FX-1, both referees).
  (b) Corollary FX (b): hence X ≤ n·(F* + 13(d_o + 1)n³(F* + 1 + T) + T) + n − 1 = O(d_o·n⁶), with F* := 1 + (n − 2)(2n − 1). Signed
      by REFEREE conditional on FB-POLY, by REFEREE-2 unconditionally after FB-POLY landed as RESULTS R48; both §Cs: unconditional now. The
      packet's chain through deg_U(o) is FBP-1's false end inequality: read f ≤ F* by R48 (i) (a) (repaired) if o ≠ c_θ, and by R48 (i) (b)
      / (c) if o = c_θ (f ≤ |U| ≤ n ≤ F* for n ≥ 3, f ≤ 1 = F* for n = 2) (FX-N2 ≈ N-FX-2, both referees; the o = c_θ branch from REFEREE-2).
- Not signed (packet §2, §3): the READINGs that FX covers every phase type ("TYPE H, TYPE Q and TYPE N phases alike" is right for (a);
  FX-N3) and its use in the 𝒞^1O assembly (now RESULTS R51, which uses R30 (c)'s sharper form); FB-PHASE (a lane cross-check).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FX (a) is subsumed by R30 (c); its value is the independent derivation. (iii) The
  bound's tightness is untested: no phase comes above 0.66 of the FX (a) bound in REFEREE-2's data, and its tighter-count mutations do not
  bite.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own phifx_probe.py on rl_engine): 253 𝒞^1O library games,
  990 phases, X 3,661 in total (X_SN 2,867), max 100 in one phase; 4,995 random 𝒞^1O runs, 8,255 phases, max X 2; 0 failures. REFEREE-2 (own
  fx_check.py): 1,509 library runs (503 files, S3 + 2 random starts), 6,282 phases, crossings by kind (i) / (ii) / (iii) 2,513 / 8,444 /
  456, max X 100 (xsn91_n48); 6,000 random 𝒞^1O runs; 0 violations; mutations stick and noiii bite.
- Signatures: REFEREE docs/referee/R-N5-FX.md (referee 843ba1f8, successor 10; §C 9f736349, successor 11): FX (a) SIGNED, FX (b) SIGNED
  conditional on FB-POLY (unconditional in §C); notes FX-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-FX.md (referee-2 83a3e8c7,
  successor 13; §C 253fe5c5): (a), (b) SIGN, (b) unconditional; notes N-FX-1, N-FX-2; no gap. §C (both): verdicts identical; joint gap map
  empty; FX-N1 = N-FX-1, FX-N2 ≈ N-FX-2 with the o = c_θ branch accepted by REFEREE; FX-N3 REFEREE only.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open for general games (its 𝒞^1O part closed by RESULTS R51).
