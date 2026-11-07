# P-IDEAL-MOVES fixes (append-only; the packet docs/new/P-IDEAL-MOVES.md is frozen)

## Entry 1 (2026-11-06 from 23:3xZ by date -u; L-NEW successor 57; Lead relay 23:36Z of fix round 1)
- Reports answered: REFEREE 24, claude/referee bc2bdd5a, docs/referee/R-P-IDEAL-MOVES.md (every item SIGN; L-1 MATCHES; optional
  MV-L1); REFEREE-2 29, claude/referee-2 38a2adb6, docs/referee-2/R2-P-IDEAL-MOVES.md (every item SIGN, no gap; L-1 MATCHES after W-1
  and W-2, both required; optional W-3; DATA attribution notes D-1..D-3, not signed, «No fix is required for signing»). No statement,
  proof or DATA of the packet changes. The line changes only (L-2 below). This entry carries no proof.
- W-1 (required; REFEREE-2 l. 106-110). The packet does NOT contain the overclaim. Its text on the relation is §1 Corollary
  MOVES-EQUIV, «μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)·μ(d). In particular MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3, and μ is bounded by a
  polynomial in d iff T^R is» (l. 90-91), and §6 «MOVES-EQUIV is an equivalence of two open bounds, not a bound» (l. 202), where the two
  bounds are «μ polynomial» and «T^R polynomial». Both are correct as written: neither says that MOVES-2D (μ ≤ 2d) is equivalent to a
  polynomial bound on T^R. Wording note, no packet edit: read «two open bounds» at l. 202 as «the two open statements «μ is polynomial»
  and «T^R is polynomial»». The overclaim is in L-1 only, fixed by R1.
- W-2 (required; REFEREE-2 l. 111-113): «the two movers» is ambiguous in L-1 (it can be read as 2j − 2, 2j − 1). The packet's §3 (a)
  says «s_(t−1)(p) ≠ s_(t−1)(q)» with p = 2j, q = 2j + 1, which is what R2 now states.
- W-3 (optional, taken; REFEREE-2 l. 114-115): L-1 left the time of the move implicit; the packet's §4 (e) says «moves at t». R3.
- MV-L1 (optional, taken; REFEREE l. 73-75): the moves bound of AND-GATE, moves(x) ≤ 1 + min(KF_x, PF_x), follows from the counted AGB
  check by arithmetic and is not counted itself. R4 says so in the DATA parenthesis (the C125 G-9 (iii) precedent would also allow leaving
  it; I take the explicit form).
- D-1..D-3 (REFEREE-2 l. 92-101, notes on §6 attribution, not signed): no change. D-3 noted: the tool's docstring labels SWD «SEG-WINDOW
  (d) BURST-2», the packet §6 counts it under WINDOW-DOUBLE (b); it is the BURST-2 case of WINDOW-DOUBLE (b), and SEG-WINDOW (d) follows
  from it with SEG-WINDOW (a). The tool stays frozen.
- Line L-2 (docs/new/P-IDEAL-MOVES-line-L2.txt, sha1 f3692aaa033540ff0494b0aac6b2d524757d5c00, 1 line, 4,495 bytes, 71 «(» = 71 «)»,
  depth never negative, 0 «|»): L-2 = L-1 (819c5815) with exactly these five replacements, applied by script; each old string occurs
  exactly once in L-1; no other byte changes:
  - R1 (W-1, REFEREE-2's text verbatim): «MOVES-2D is not claimed (it is an open conjecture, here shown equivalent up to a factor 2d − 2
    to a polynomial bound on T^R)» → «MOVES-2D is not claimed (it is an open conjecture; here μ(d) is shown equal to T^R(d) up to a factor
    2d − 2 and an additive 3, so MOVES-2D is sufficient, not necessary, for a polynomial bound on T^R)»
  - R2 (W-2): «flips while the two movers are on different options» → «flips while 2j and 2j + 1 are on different options before the
    step»
  - R3 (W-3): «some mover other than x on the chain under s_(t−1) of the option x takes at t + 1 moves;» → «some mover other than x on
    the chain under s_(t−1) of the option x takes at t + 1 moves at t;»
  - R4 (MV-L1): «every pair of consecutive moves and every change of π;» → «every pair of consecutive moves (the min bound by
    arithmetic) and every change of π;»
  - R5 (source note names the fixes file): «(P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md; L-NEW successor 57)» → «(P-IDEAL-MOVES,
    docs/new/P-IDEAL-MOVES.md with its fixes entry 1, docs/new/P-IDEAL-MOVES-fixes.md; L-NEW successor 57)»
- Word diff L-1 → L-2 (difflib on space-separated tokens; [-removed-] {+added+}):
  [-the two movers-]
  {+2j and 2j + 1+}
  [-options,-]
  {+options before the step,+}
  [-moves;-]
  {+moves at t;+}
  [-conjecture,-]
  {+conjecture;+}
  {+μ(d) is+}
  [-equivalent-]
  {+equal to T^R(d)+}
  [-to-]
  {+and an additive 3, so MOVES-2D is sufficient, not necessary, for+}
  {+(the min bound by arithmetic)+}
  [-docs/new/P-IDEAL-MOVES.md;-]
  {+docs/new/P-IDEAL-MOVES.md with its fixes entry 1, docs/new/P-IDEAL-MOVES-fixes.md;+}
- Pins: experiments/new/check.sh block «P-IDEAL-MOVES» now also pins this file and L-2; the packet, L-1, tool, output and instances are
  unchanged.

## Entry 2 (2026-11-07 from 00:1xZ by date -u; L-NEW successor 57; Lead relay 00:16Z of fix round 2)
- Reports answered: REFEREE 25, claude/referee 72f4b2f3, docs/referee/R-P-IDEAL-MOVES.md §C (fixes entry 1 CORRECT, L-2 byte test MATCHES,
  MV-C1 REQUIRED); REFEREE-2 29, claude/referee-2 f71fdbdb (fixes entry 1 CORRECT, L-2 MATCHES, W-3 read as intended). Relayed by the Lead
  at 00:16Z with the replacement text. No statement, proof or DATA of the packet changes; the packet and entry 1 stay as they are. This
  entry carries no proof.
- MV-C1 (REFEREE 25, required). L-2's «so MOVES-2D is sufficient, not necessary, for a polynomial bound on T^R» overclaims: the packet
  proves sufficiency (§1 MOVES-EQUIV: MOVES-2D ⇒ T^R(d) ≤ 4d² − 4d + 3) and never proves non-necessity; MOVES-2D is open, and if it is
  true it is trivially necessary. The phrase came in with W-1's wording (entry 1, R1). The packet does not contain it (entry 1, W-1
  note). R6 below states only what is proved: sufficiency, and that a polynomial bound on T^R gives only μ polynomial (§1: μ(d) ≤ T^R(d)).
- Line L-3 (docs/new/P-IDEAL-MOVES-line-L3.txt, sha1 d3983c68cdda03e81fdaedec770af587f758d84e, 1 line, 4,567 bytes, 71 «(» = 71 «)»,
  depth never negative, 0 «|»): L-3 = L-2 (f3692aaa) with exactly these two replacements, applied by script; each old string occurs
  exactly once in L-2; no other byte changes:
  - R6 (MV-C1, the Lead's text verbatim): «so MOVES-2D is sufficient, not necessary, for a polynomial bound on T^R)» → «so MOVES-2D is
    sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial)»
  - R7 (source note names entry 2): «(P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md with its fixes entry 1, docs/new/P-IDEAL-MOVES-fixes.md;
    L-NEW successor 57)» → «(P-IDEAL-MOVES, docs/new/P-IDEAL-MOVES.md with its fixes entries 1-2, docs/new/P-IDEAL-MOVES-fixes.md; L-NEW
    successor 57)»
  - Byte test: L-2 with R6 alone gives 4,563 bytes, sha1 747dfa48c3a6a1d75f4d92aea5aa086128b87588 = REFEREE 25's prediction; R7 then adds
    4 bytes («entry 1,» → «entries 1-2,»).
- Word diff L-2 → L-3 (git diff --no-index --word-diff=plain; [-removed-] {+added+}):
  [-sufficient, not necessary,-]
  {+sufficient+}
  [-T^R);-]
  {+T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial);+}
  [-entry 1,-]
  {+entries 1-2,+}
- Pins: experiments/new/check.sh block «P-IDEAL-MOVES» pins this file (new sha1) and L-3; packet, L-1, L-2, tool, output and instances
  unchanged.

## Entry 3 (2026-11-07 from 01:2xZ by date -u; L-NEW successor 57; Lead relay 01:16Z of fix round 3, Lead reading)
- Decision answered (Lead reading, 01:16Z): P-IDEAL-MOVES lands with a line that makes NO status claim about MOVES-2D; the DEAD record of
  MOVES-2D goes in a separate entry. Reasons given: a DEAD claim in the line would need both referees' replay and would pull the d 5 data
  into this landing; the packet's signed items do not depend on MOVES-2D (REFEREE 25). No statement, proof or DATA of the packet
  changes; the packet and entries 1-2 stay as they are. This entry carries no proof.
- Wording note (no line change, no packet edit): the packet's status labels «OPEN» for MOVES-2D, l. 9 («CONJECTURE MOVES-2D and G-N5-TIME
  stay OPEN») and l. 77-78 («CONJECTURE MOVES-2D (lane, box 181, OPEN)»), are superseded. MOVES-2D's status is recorded separately:
  L-LOWER successor 3's instances experiments/lower/l3/kill/KILL_M2D_d6_mu13.json (sha1 5301c716f68f219bda2806f29b317c94e0ed5df0) and
  KILL_M2D_d8_mu21.json (sha1 d96c2b3657e79c410b180580d829366cbecc9ea4) on claude/l-lower 4d747490, replayed by L-NEW box 188
  (docs/new/N5-KILLREPLAY-box188.md, commits 6d043927 and 42427d9e: REPRODUCED, d 6 13 > 12, d 8 21 > 16), referee review pending. The
  instances are NOT added to the packet or to movescheck's corpus. G-N5-TIME stays OPEN.
- Line L-4 (docs/new/P-IDEAL-MOVES-line-L4.txt, sha1 73c16d1e2b009ff2e3d774a904e4462be0874db1, 1 line, 4,598 bytes, 71 «(» = 71 «)»,
  depth never negative, 0 «|»): L-4 = L-3 (d3983c68) with exactly these three replacements, applied by script; each old string occurs
  exactly once in L-3; no other byte changes:
  - R8 (Lead): «(the open conjecture MOVES-2D)» → «(the lane conjecture MOVES-2D, not claimed here)»
  - R9 (Lead): «MOVES-2D is not claimed (it is an open conjecture; here» → «MOVES-2D is not claimed (its status is not part of this result;
    here»
  - R10 (source note): «fixes entries 1-2» → «fixes entries 1-3»
- Word diff L-3 → L-4 (git diff --no-index --word-diff=plain; [-removed-] {+added+}):
  [-open-]
  {+lane+}
  [-MOVES-2D)-]
  {+MOVES-2D, not claimed here)+}
  [-(it-]
  {+(its status+}
  [-an open conjecture;-]
  {+not part of this result;+}
  [-1-2,-]
  {+1-3,+}
- Pins: experiments/new/check.sh block «P-IDEAL-MOVES» pins this file (new sha1) and L-4; packet, L-1..L-3, tool, output and instances
  unchanged.

## Entry 4 (2026-11-07 from 03:3xZ by date -u; L-NEW successor 58; Lead relay 03:06Z of CHECKER C129, FAIL E-1, E-2)
- Source: CHECKER C129, docs/checker/C129.md at claude/checker a1963575 (§2 verdict FAIL E-1, E-2; §3 the findings; §5 the exact L-5
  wording). Both items concern the LINE's DATA wording only. No statement, proof, tool, output or instance of the packet changes; the
  packet (5ce2947d) and entries 1-3 stay as they are. This entry carries no proof.
- E-1 (unit, ACCEPTED). The line's «equality on 59,502» is movescheck's counter RXEQ (movescheck.py l. 41): T = 1 + #{t ≤ T − 1 :
  Mv_t ∩ Z ≠ ∅}, the equality case of REDUCE-XI's first form. It is not equality in the line's displayed bound T ≤ 1 + Σ_(z ∈ Z) moves(z),
  which C129 measured to hold with equality on 8,399 of the 63,223 runs (C129 §3, §5 «R1's 8,399 is from my instrumented run; it
  matches the drafter's measurement»). R1 names both.
- E-2 (instance, ACCEPTED). movescheck's dense() runs pass_d3_D3.json and pass_d4_D4.json from the starts 110100 and 01010111
  (movescheck.py l. 108-109), not from their stored starts (000000, 00000000). The line named no start for them. R2 names them, so that a
  reader can reproduce the DEAD instances from the line (CLAUDE.md: a dead end gives the instance that killed it).
- N-1 (ACCEPTED, folded in as R3 on the Lead's relay). m4_z4_r7.json is run from its stored start 10111010; R3 names it, so that every
  DEAD instance in the line names its start.
- Line L-5 (docs/new/P-IDEAL-MOVES-line-L5.txt, sha1 a42257cb159b2e51128c2334062d44edb97661f6, 1 line with its newline, 4,750 bytes,
  74 «(» = 74 «)», depth never negative, 0 «|»): L-5 = L-4 (73c16d1e) with exactly these three replacements, copied from C129 §5 and
  applied by script; each old string occurs exactly once in L-4; no other byte changes (the source note keeps «fixes entries 1-3», as
  in C129's computed sha1, on the Lead's instruction):
  - R1 (E-1): «REDUCE-XI 0 violations on 63,223 runs, equality on 59,502;» → «REDUCE-XI 0 violations on 63,223 runs, equality T = 1 +
    #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} on 59,502 (T = 1 + Σ_(z ∈ Z) moves(z) on 8,399);»
  - R2 (E-2): «also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4 with LM 0» → «also pass_d3_D3.json from start 110100 and
    pass_d4_D4.json from start 01010111, D 3 and 4 with LM 0»
  - R3 (N-1): «experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4: a Ξ-target» → «experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4, its stored
    start 10111010: a Ξ-target»
- The result equals C129 §5's «L-5 with R1-R3 (my script): sha1 a42257cb159b2e51128c2334062d44edb97661f6 with its newline (4,750
  bytes)» byte for byte.
- Word diff L-4 → L-5 (git diff --no-index --word-diff=porcelain; - removed, + added):
  + from start 110100
  - pass_d4_D4.json,
  + pass_d4_D4.json from start 01010111,
  - 𝓛^R_4:
  + 𝓛^R_4, its stored start 10111010:
  + T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} on 59,502 (T = 1 + Σ_(z ∈ Z) moves(z)
  - 59,502;
  + 8,399);
- Pins: experiments/new/check.sh block «P-IDEAL-MOVES» pins this file (new sha1) and L-5; packet, L-1..L-4, tool, output and instances
  unchanged.
