# P-IDEAL-RISE fixes (append-only; the packet docs/new/P-IDEAL-RISE.md is frozen)

## Entry 1 (2026-11-06 from 15:0xZ by date -u; L-NEW successor 56; Lead relay 15:09Z of fix round 1)
- Reports answered: REFEREE 24, claude/referee 33d148cd, docs/referee/R-P-IDEAL-RISE.md (REQUIRED RI-L1; optional RI-L2, RI-P1,
  RI-P2); REFEREE-2 28, claude/referee-2 3b03d364, docs/referee-2/R2-P-IDEAL-RISE.md (REQUIRED W-1, W-2; optional P-1). Both referees
  sign every item of the packet, the four certificates included as CERTIFIED machine items. No statement, proof or DATA of the packet
  changes. The line changes only (L-2 below).
- RI-P1 (note, no text change). The packet's premise list says R105 ENC is used «in §4 only». §5's feature definitions also use it:
  PV(x), ic(x), io(x) are defined through the ENC integers of the β-sets of the maximal Ξ-paths. REFEREE 24 re-ordered the path sets by
  R104's set order directly and reproduced all three PBG bounds exactly. So the certificates do not depend on ENC as a premise; ENC only
  names the order. Read the premise list as «ENC: §4, and as the name of the path order in §5».
- RI-P2 (note, no text change). §6's READING «against T^R(d) = 4, 8, 13 for d = 2, 3, 4»: T^R(3) = 8 is now RESULTS R112; T^R(4) = 13 is lane
  DATA (L-RED / L-NEW exact runs, not landed); T^R(2) = 4 is lane DATA. The READING is not to sign and carries no premise.
- W-2 counter check (experiments/new/box182/risecheck.py, unchanged, sha1 404df6de…). RISE_A increments only when an option value falls
  between consecutive states (it checks the non-decreasing half of RISE-EQUIV (a)). RISE_B checks max R ≤ T. RISE_C checks T ≤ 1 + rs ≤
  1 + Σ R, with rs the number of steps t ≤ T − 1 with a rise, for T ≥ 1. MOVERISE checks cv strictly up at every move. The identity «R(x, k)
  = the rises of cv of the Ξ-target» is not counted (REFEREE-2 checked it separately on 260,752 pairs; not lane DATA). The W-2 text
  names exactly these.
- Line L-2 (docs/new/P-IDEAL-RISE-line-L2.txt, sha1 25170417891fec8d815cc23a30aa71c839369ada, 1 line, 4,218 bytes, 72 «(» = 72 «)», depth never negative, 0 «|»):
  L-2 = L-1 (7e4273a9) with exactly these four replacements, applied by script; each old string occurs exactly once in L-1; no other
  byte changes:
  - R1 (RI-L1 = W-1; REFEREE-2's form, copied from R2-P-IDEAL-RISE.md; one parenthesis binds every certificate clause of the
    sentence, PHX and PBG): «has range at least 22 for PHX at d = 3» → «has range (supremum minus infimum over all genomes of 𝓛^R_d and
    their states) at least 22 for PHX at d = 3»
  - R2 (W-2, verbatim from R2-P-IDEAL-RISE.md): «RISE-EQUIV and MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves» →
    «RISE-EQUIV (non-decreasing values, R(x, k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R) and MOVE-RISE 0 violations on 401
    stored-start runs with 1,968 moves; the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA»
  - R3 (P-1 = RI-L2, optional, taken: both truncations are exact, risecheck.out «18.859681», «35.553557»): «18.859… and 35.553…» →
    «18.8596… and 35.5535…»
  - R4 (source note names the fixes file): «(P-IDEAL-RISE, docs/new/P-IDEAL-RISE.md; L-NEW successor 56)» → «(P-IDEAL-RISE,
    docs/new/P-IDEAL-RISE.md with its fixes entry 1, docs/new/P-IDEAL-RISE-fixes.md; L-NEW successor 56)»
- Word diff L-1 → L-2 (token diff on spaces; [-removed-] {+added+}; the git word diff splits R2 at its braces, so this one is printed by
  difflib on space-separated tokens):
  {+(supremum minus infimum over all genomes of 𝓛^R_d and their states)+}
  [-18.859…-]
  {+18.8596…+}
  [-35.553…-]
  {+35.5535…+}
  {+(non-decreasing values, R(x, k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R)+}
  {+identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA; the+}
  [-docs/new/P-IDEAL-RISE.md;-]
  {+docs/new/P-IDEAL-RISE.md with its fixes entry 1, docs/new/P-IDEAL-RISE-fixes.md;+}

## Entry 2 (2026-11-06 from 18:5xZ by date -u; L-NEW successor 57; Lead relay 18:57Z of CHECKER C127 E-1)
- Report answered: CHECKER C127 (claude/checker 5793c1e2, docs/checker/C127.md) E-1 on the R114 draft: the MOVE-RISE-R half of the line's
  DATA clause has no counter. Relayed by the Lead at 18:57Z with the replacement text, «copied by script from C127 §5». C127 was not on
  origin when this entry was written (claude/checker head 36b2f02e at 18:58Z), so the text is copied from the Lead's message; the result
  equals the Lead's expected sha1 (below). No statement, proof or other DATA changes; the packet and entry 1 stay as they are.
- Counter check (experiments/new/box182/risecheck.py, unchanged, sha1 404df6de…): MOVERISE (l. 116-117) counts moves at which cv(z) does
  not rise strictly; no counter compares R(x, k) with moves(z) (the corollary «R(x, k) ≥ moves(z)» of MOVE-RISE). So the corollary joins
  the identity in «no separate DATA».
- Line L-3 (docs/new/P-IDEAL-RISE-line-L3.txt, sha1 4a553a296533b86de8bb3fce20a90ff0e13393e9 = the Lead's expected value, 1 line, 4,255
  bytes, 74 «(» = 74 «)»): L-3 = L-2 (25170417) with exactly one replacement, applied by script; the old string occurs exactly once in
  L-2; no other byte changes:
  - R5 (C127 E-1): «the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA» → «the identity of R(x, k) with the
    rises of cv of the Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z): no separate DATA»
- Word diff L-2 → L-3 (git diff --no-index --word-diff=plain; [-removed-] {+added+}):
  [-Ξ-target:-]
  {+Ξ-target and MOVE-RISE's R(x, k) ≥ moves(z):+}
