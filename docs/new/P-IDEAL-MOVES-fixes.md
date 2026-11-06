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
