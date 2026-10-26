# P-N5-FX fixes (box 14 packet; repairs only)
L-SI successor 11 (Opus 5.5; D15, D18, L37, L40). Prepared and frozen at the Lead's GO of 02:21Z (Lead's stamp), after both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-FX-box14.md, sha1 aa227b0b310b60c630a89afa248cd60ea04b66c3 (l-si fe58fbab, L-SI successor 9). FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 10, docs/referee/R-N5-FX.md: report at referee 843ba1f8 (file sha1 d270ed61…); REFEREE successor 11's §C at
    9f736349 (0fdf64ad…).
  - REFEREE-2 successor 13, docs/referee-2/R2-N5-FX.md: report at referee-2 83a3e8c7 (file sha1 eaa31d01…); §C at 253fe5c5 (20686bf9…).
- Both §Cs: identical verdicts, joint gap map empty, nothing open.
- Verdicts. Corollary FX (a) and (b) are SIGNED by both, with no gaps.
  - (b) is now UNCONDITIONAL. Its premise FB-POLY has landed as RESULTS R48, with FBP-1 / FBP-2 repaired. REFEREE's §C C.1 says: "So I
    now agree that (b) holds unconditionally, citing R48 (i) in its repaired form."
  - §2 (READINGs) and §3 (DATA) are not signed.

## Lines (one per note)
- FX-N1 = N-FX-1 (citation; (a)). REFEREE's §C fixes line, verbatim: "(a) is implied by R30 (c); the proof here is a second
  derivation".
  - R30 (c) Corollary SN-PREFIX already lands the sharper per-phase bound "crossings ≤ (f + 1)(n − 1) + f + X_SN". It is smaller than
    FX (a)'s n·(f + X_SN) + n − 1 by (n − 1)·X_SN.
  - FX (a)'s proof uses R-STICK alone. It needs no SN-PREFIX ordering, so it is an independent derivation of the weaker form.
  - Substituting into R30 (c)'s form instead gives X = O(d_o n⁵). P-N5-1O (RESULTS R51) already does this. The order O(d_o n⁶) ⊆ O(n⁷)
    stated in (b) remains a correct upper bound.
- FX-N2 = N-FX-2 (citation and the case o = c_θ; (b)). REFEREE's §C fixes line, verbatim: "f ≤ F* by R48 (i) (a) (repaired) if
  o ≠ c_θ; by R48 (i) (b), (c) if o = c_θ".
  - Replace the §0 dependency row "FB-POLY … IN REVIEW" by RESULTS R48 (i) (LANDED). Its end bound is the repaired one:
    f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1) = F*.
    - The packet's chain through deg_U(o) ≤ n − 1 is the step FBP-1 repaired. It is false when o has a self-loop and succ(o) ⊇ U = V.
      The conclusion f ≤ F* is the landed one and is unchanged.
  - Case o = c_θ, which the packet did not treat. Both referees checked this:
    - n ≥ 3: R48 (i) (c) gives f ≤ |U| ≤ n ≤ F*, since F* − n = 2n² − 6n + 3 ≥ 0.
    - n = 2: R48 (i) (b) (|U| = 2) or (c) (|U| = 1) gives f ≤ 1 = F*.
  - So f ≤ F* holds in every phase, and (b)'s substitution into (a) and R34 (f) X-SN-PHASE is valid. Both are non-decreasing in f.
  - Drop "CONDITIONAL on FB-POLY" from (b).
- FX-N3 (scope; REFEREE only, stands per both §Cs). The remark "it covers TYPE H, TYPE Q and TYPE N phases alike" is about (a), which
  has no phase-type hypothesis. §2's READINGs are not signed: T-K, and "N5 on 𝒞^1O is polynomial given K".
  - Since then, the 𝒞^1O assembly has landed as RESULTS R51 (P-N5-1O) on its own premises. It does not rest on §2.
  - 𝒞^1O is a subclass. TARGET.md asks about general games. G-N5-TIME stays OPEN beyond 𝒞^1O.

## Data
- Neither referee asks for any. REFEREE-2: 1,509 library runs (S3 + 2 random starts) and 6,000 random, 0 violations, max X / FX (a)
  bound 0.660.
- REFEREE (phifx_probe.py): 0 failures.
