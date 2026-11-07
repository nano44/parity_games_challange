# R2-P-IDEAL-FLIP-L2: P-IDEAL-FLIP fixes entry 1 and line L-2
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-05 12:54Z (date -u). Object: claude/l-new 4c2e5124.

## Hashes (git show 4c2e5124:FILE | sha1sum)
- docs/new/P-IDEAL-FLIP-fixes.md f8d3677e4754fde9922208782483f9d4bff168ac, 57 lines; docs/new/P-IDEAL-FLIP-line-L2.txt
  8099415b58689ea9241f2da9d642ba8a1af74cf9, 1 line, 0 «|». Packet 92803bd5 and L-1 36418d16 unchanged.

## Fixes entry 1: CORRECT
- F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN (Opus 5.5, D12). On 𝓛^R_d, option k of a level-1 mover W-points to mover k,
  so key^c(x, k) = (κ^c_k, g(x, k)) and KP^c(x) does not depend on the state. A change of x at frame t takes an option of
  A_(u_(t−1))(x) other than u_(t−1)(x), so with degree 2 it takes the key^(c_t)-least one, KP^(c_t)(x). With c constant on [a, b], two
  consecutive changes t1 < t2 give u_(t2)(x) = KP = u_(t1)(x) = u_(t2−1)(x), against the change at t2. ✓ No Ξ-value and no ISO is used.
  The c-step keeps 0 and 1 at u_0's options, so the A-sets are G's at those states. ✓ DATA (mine, flip_check.py's c-step, ISO not
  imposed): 1,500 random 𝓛^R_d genomes (d 2-4; 1,300 non-ISO), random bit sequences, 163 consecutive-change pairs, 0 violations.
- F-b, SWAP-RUN with ANY q: SIGN (Opus 5.5, D12). It is my N-1 written out. v := b_0(q) is the same for G and G^swap (shared level-0
  gates); c = v blocks are runs of H_q (W-ONLY (c) on G); c = 1 − v blocks use SWAP Step^(1−v)_G = Step^v_(G^swap), which are runs of
  (G^swap)_q (W-ONLY (c) on G^swap, which is in 𝓦_d and ISO); idle frames follow a stopped run. ✓ The caveat is correctly dropped.
- F-c (my F-1): CORRECT. The R109 SHIFT quote's two pieces are verbatim in the landed R109 entry. The shifted H_q, (G^swap)_q have
  levels 0..d − 2, with the two degree-2 movers of old level 1 and two degree-1 movers at level 0, so they are in 𝓛_(d−1). Each piece
  has ≤ T*(d − 1) moves. It is a remark outside the signed text. ✓

## Line L-1 → L-2: MATCHES
- Token diff: exactly the 3 hunks of entry 1. Byte test: L-1 with «and DEAD: the lane conjecture SC-ISO» → «and CONDITIONAL DEAD (premise
  T^R(3) ≤ 8, machine): the lane conjecture SC-ISO», «whose run is the iterated» → «whose run from any state with q at 0 and 1 is the
  iterated» (my P-3), «every start for d ≤ 4, 40 random starts otherwise);» → «every start);» (my P-1). Each old string occurs once;
  the result equals L-2 (True).
- NOW-ONCE's unconditional c_t-step wording is now proved by F-a. SWAP's unconditional concatenation is proved by F-b.
- «CONDITIONAL DEAD» is exactly my G-FLIP-1 ruling at the time of L-2. My audit R2-T3R-audit.md (same day) closes G-FLIP-1 on my side.
  If the other referee agrees, the label can drop «CONDITIONAL» (an L-3 or an erratum, the Lead's choice), keeping the premise wording
  «two independent CNF encodings, CaDiCaL UNSAT, no DRAT certificate».

## Addendum 1: line L-3 (claude/l-new 47b4e165, branch head a9851eba), 2026-11-05 17:06Z (date -u)
- Stale-clone check: ls-remote claude/referee-2 = local HEAD = b2c0fff8 (no container restart).
- Hashes: docs/new/P-IDEAL-FLIP-line-L3.txt 4089bd73baf65929cf5b6094ef31882df817fd53 (with newline), 4,715 bytes, 1 line, 0 «|»;
  L-2 8099415b unchanged; P-IDEAL-FLIP-fixes.md 4220c44e… (entry 2 appended).
- Byte test: R1-R4 extracted from CHECKER C122 §5 (claude/checker 80ed31a6, line wraps joined). Each old string occurs exactly once in
  L-2 and each new string once in L-3; L-2 with R1, R2, R3, R4 applied equals L-3 exactly (True; 4,715 = 4,715 bytes). Nothing else changed.
- Parentheses: 53 «(» / 53 «)», depth never negative, final depth 0 (G-0 closed by R4's added «)»).
- Content: R1 / R2 measured genome counts (225 + 75 drawn, 65 non-ISO, 36 ISO corpus, 261 ISO); R3 bounds SWAP's DATA to the ISO genomes;
  R4 lists SWAP's concatenation clause under «no signed DATA» and names fixes entry 1 in the source note (F-a, F-b live there). These
  are DATA scope / source-note changes only; no statement changes. The CONDITIONAL DEAD wording is unchanged.
- Verdict: L-3 MATCHES.
