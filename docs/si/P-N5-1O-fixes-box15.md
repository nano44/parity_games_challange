# P-N5-1O fixes (box 15 packet; repairs only)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). DRAFT prepared at the Lead's request of 01:18Z (Lead's stamp). Frozen only when its sha1
is reported, on the Lead's go after both §Cs land. Stamp: the reporting commit (date -u).
- Object: docs/si/P-N5-1O-box15.md, sha1 2cf5e67262d31712976fb882175f5080cc3dc4ec (l-si 058e5aee; pinned trunk 291c110d). FROZEN, not
  edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 11, docs/referee/R-N5-1O.md at referee 4298dae9 (40598100…). The same commit adds docs/referee/R-N5-START.md
    Addendum 1 (f3530690…).
  - REFEREE-2 successor 12, docs/referee-2/R2-N5-1O.md at referee-2 04c2d708 (8d48103f…).
  - §Cs: pending.
- Verdicts. Every statement to sign is signed by both: 1O-POLY, BIT, OUT, 1O-TIME. REFEREE signs OUT WITH GAP OUT-1 (one-word repair);
  REFEREE-2 signs everything with no gap and files the same point as N-1O-1.

## Lines (one per note)
- OUT-1 = N-1O-1 (Lemma OUT step 2). Read "reward(λ(v)) ≥ 0" in place of "> 0", and add "every odd vertex has reward ≤ −1".
  - Why: reward(c) = p′(c) = 2·rank(c) for even c, so the rank-0 even vertex has reward 0. REFEREE-2 reaches this case in data.
  - The step's conclusion is unchanged: a cycle node with reward ≥ reward(λ(v)) ≥ 0 cannot be odd, since odd rewards are ≤ −1.
- 1O-N1 (Theorem 1O-POLY step 3; units). R48 (i)'s f counts in-phase Even S4c fallbacks; R50 (h)'s f counts the phase's fallback
  transitions. They are the same count: inside a phase every fallback is Even's, because an Odd fallback changes τ and so ends the phase.
- 1O-N2 (T*; harmless). The packet's N_Ξ uses "F + N_st" where R50 (h) has "f + (N_st − 1)": looser, still valid.
- N-1O-2 (Theorem 1O-POLY step 5; arithmetic). With m ≤ n² and Δ, d_o ≤ n, O(m·Δ·d_o·n¹³) is O(n¹⁷). The stated "⊆ O(n¹⁸)" is true but
  loose.
- BIT-N1 (Lemma BIT (iv); precision). S1 (iv)'s "recursion over successors in list order, first strict maximum wins" is read as memoised.
  Memoisation gives the same outputs as SPEC's recursion, and Q3 makes the restricted graph minus v acyclic, so each vertex is computed
  once.
- N-1O-3 (Lemma BIT; optional, loose bound). One S1 run is O(n(n + m)) word operations, because the sets R of distinct cycle nodes are
  disjoint. The stated O(n²(n + m)) is true but loose.
- N-1O-4 (Lemma OUT step 2; the referees' check). YES, the parenthetical is general. Cite RESULTS R18 (d) Lemma S (a) (the statement)
  beside R21 (a) (the parenthetical) and P-N5-X §1 (the proof).
  - REFEREE-2 records that R21 (a) holds on every game via R18 (d) S (a). So the packet's §4 READING "S5 correct on every game" now has its
    premise checked. It stays a READING here; Lemma OUT is signed for 𝒞^1O.
- N-1O-5 = REFEREE R-N5-START Addendum 1 (§2.1; the referees' item). The R32 / R33 chain under R34 (f) is START-FREE, checked line by line
  by both referees. R-N5-START's depth caveat ("A line-by-line re-read of every R32 / R33 step was NOT done here") is CLOSED by that
  Addendum. The packet's §6 honest-limits line on it is superseded.
- N-1O-6 (§1 / §4 quotes; cosmetic). All quotes are verbatim except two attributions: VJ00 (11) is quoted via P-N5-LP §0, and G-N5T-3's
  inner quotes. Quote marks only.
- (Placeholder) §C items of either referee: pending.
