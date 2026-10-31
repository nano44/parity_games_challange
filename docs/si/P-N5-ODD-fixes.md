# P-N5-ODD fixes (repairs and status notes against the FROZEN packet docs/si/P-N5-ODD-box57.md, sha1 03eec41d3bfc63a6945d0f30d831a46f14e46b84)
L-SI. The frozen file and docs/si/P-N5-ODD-line.txt (sha1 cd121dffd06dbc794f3154e34aa238d8df81f837) are never edited. Each entry names the
section, says whether a TO-SIGN item is affected, and gives the evidence. Append-only. Quotes are verbatim; the reports' line wraps are
joined by one space. Reports: REFEREE 21 R-N5-ODD (claude/referee 6c9430ef, docs/referee/R-N5-ODD.md); REFEREE-2 24 R2-N5-ODD
(claude/referee-2 5753ef03, docs/referee-2/R2-N5-ODD.md). Routed by the Lead 2026-10-31 13:32Z.

## F0 (L-SI successor 37, 2026-10-31 13:5xZ; status note)
- Both reports SIGN every TO-SIGN item: OLD-PLAY, ODD-STEP (with NO-RET), ODD-RELAY, ODD-ADD, SRC-ROOT, FUEL-LEX, FUEL-COUNT. Nothing is
  FALSE. Two proof-text gaps (entries 1, 2), line changes (entry 3, revision L-1), a data defect (entry 4).
- No statement of a signed item changes. Entries 1-2 replace proof text only.

## Entry 1: G-ODD-1, FUEL-LEX proof (§6), found independently by both referees; repair REFEREE-ORIGINATED (L41)
- REFEREE 21: «For b = a = (1, r), the proof «suppose every change of Ξ(z) strictly between t and t′ has key < (1, r)». That is not the
  negation of EQHI: the negation is «key ≤ (1, r)», which leaves intermediate changes of key exactly (1, r) uncovered.»
- REFEREE-2 24: «The proof supposes «every change of Ξ(z) strictly between t and t′ has key < (1, r)». The negation of EQHI is «≤ (1, r)».
  The case of an intermediate change with key exactly (1, r) and none higher is not covered by the text.»
- Adopted repair (REFEREE-2 24's wording, which REFEREE 21's closing argument also gives: «Consider the FIRST change of key (1, r) after
  t, at some u ∈ (t, t′) or at t′ itself. It moves rank r away from β with all higher ranks equal, so it is a fall, against [R15a].»):
  - Replacement proof of the case b = a = (1, r). Suppose EQHI fails: every change of Ξ(z) at u ∈ (t, t′) has key ≤ (1, r). Let u be the
    first change in (t, t′] with key ≥ (1, r); it exists, since the change at t′ has key (1, r). Between t + 1 and u the cycle node and the
    bits at ranks > r are fixed (all changes there have key < (1, r)), and the bit at r is the Even-better bit β set by the rise at t. The
    key of u is (1, r) (EQHI fails, and t′ has key (1, r)), so u moves rank r away from β with the higher ranks fixed: Ξ_(u+1)(z) ◁ Ξ_u(z),
    against [R15a]. □
- Status: the statement of FUEL-LEX is unchanged. The repair is referee-originated (each referee wrote it independently, L41).
- DATA: REFEREE-2 24 «MID_EQKEY (a key-(1, r) change strictly between two (1, r) re-routes) = 0 everywhere».

## Entry 2: G-ODD-2 (REFEREE-2 24) = N-ODD-2 (REFEREE 21), FUEL-COUNT boundary classification (§6); repair REFEREE-ORIGINATED (L41)
- REFEREE 21: «N-ODD-2 (precision): a boundary that is both EQHI and REP must be counted as EQHI. The block argument uses «no change of key
  > (0, 0) in the window», which is «not EQHI».»
- REFEREE-2 24: «Repair: classify a boundary as ASC, else EQHI, else REP. Then the stated count n(1 + A), with A ≤ HC + n − 1, goes
  through:»
- Adopted: in the proof of FUEL-COUNT, each run boundary is classified ASC, else EQHI, else REP. ASC and EQHI are charged to HC through
  the disjoint windows (t, t′]. REP (2, 0) boundaries are cycle-node rises (≤ n − 1). Only PURE REP (0, 0) boundaries (not EQHI) are
  chained: along a chain of them no change of key > (0, 0) occurs in the union of their windows, so only the length moves, strictly one
  way. The bound N ≤ n(n + 2)(HC + n) is unchanged.
- DATA: REFEREE-2 24 «REP00_with_higher (the overlap) = 0 on everything run. FCNT = 0.»

## Entry 3: line revision L-1 (docs/si/P-N5-ODD-line-L1.txt; one line, no heading marker)
- REQUIRED items, the union of both reports, each with its change in L-1:
  - E3.1 REFEREE 21 ODD-L1 / REFEREE-2 24 ODD-L3 (ODD-ADD drops its hypothesis; «relayed vertices» undefined). REFEREE 21: «Fix: «for a
    set I of transitions and a set U of vertices such that at every k ∈ I at which Ξ(o) changes, ODD-RELAY's hypothesis holds for some
    u_k ∈ U: |{k ∈ I : Ξ(o) changes at k}| ≤ |{k ∈ I : Ξ(u) changes at k for some u ∈ U}|».» L-1: «(Corollary ODD-ADD) for every Odd o,
    every set I of transitions and every set U of vertices such that at every k ∈ I at which Ξ(o) changes ODD-RELAY's hypothesis holds
    for some u_k ∈ U, |{k ∈ I : Ξ_(k+1)(o) ≠ Ξ_k(o)}| ≤ |{k ∈ I : Ξ_(k+1)(u) ≠ Ξ_k(u) for some u ∈ U}| (no degree factor)».
  - E3.2 REFEREE 21 ODD-L2 / REFEREE-2 24 ODD-L2 («rise transition» undefined). L-1 adds to the fuel re-route definition «its rise
    transition := k − 1 → k».
  - E3.3 REFEREE 21 ODD-L3 / REFEREE-2 24 ODD-L1 last item (F unbound in the FUEL clauses). L-1: the W-run clauses stand under «and for
    every W-run F of the run,» (inside «for every N5 run on every game, …»), and the preamble definitions read «for a W-run F, …».
  - E3.4 REFEREE 21 ODD-L4 (x free in the R57 gloss). L-1: «… for every positional Odd strategy ρ and every vertex x)».
  - E3.5 REFEREE-2 24 ODD-L1 (x, u, k unquantified). L-1: OLD-PLAY «at every transition k → k + 1 and for every vertex x»; ODD-STEP «at
    every transition k → k + 1 and for every Odd o»; ODD-RELAY «at every transition k → k + 1, for every Odd o with x := σ̄_k(o) and every
    vertex u on x's (σ_k, σ̄_k)-play»; SRC-ROOT «at every transition k → k + 1 of F».
- Precision items:
  - E3.6 [PLAY] source (REFEREE 21 N-ODD-1: «the line should cite «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)»»). L-1: «(P-N5-SRC §2,
    the signed proof of RESULTS R97 PLAY-CAUSE^S)».
  - E3.7 «HXS-POLY» (REFEREE 21: «Say «the polynomiality of max HXS_F in R97's SRC-COUNT».»). L-1 uses that wording.
  - E3.8 SRC-ROOT (REFEREE 21: «add «every o_j's Ξ changes at k», and that o_t may be o_0.»). L-1: «every o_j's Ξ changing at k, to an Odd
    o_t (possibly o_0)».
  - E3.9 «rank» (REFEREE 21: ««rank» (in the key) is SPEC Q1's.»). L-1: «(path sets compared by SPEC Q1; «rank» is SPEC Q1's)».
  - E3.10 DATA wording (REFEREE-2 24 ODD-L4: «Write «of every statement checked in packet §7», or cite my checks (which cover all of
    them, with unrestricted y).»). L-1: «corpus 0 violations of every statement checked in packet §7, and of all seven statements in both
    referees' own checks».
  - E3.11 Scope tail (REFEREE-2 24 ODD-L5: «If they are closed by these repairs, the tail should say so (L41).»). L-1 adds «the proofs of
    FUEL-LEX and FUEL-COUNT carry referee-originated repairs (G-ODD-1, written independently by REFEREE and REFEREE-2; G-ODD-2 = N-ODD-2;
    docs/si/P-N5-ODD-fixes.md entries 1-2)», and the source tag names this file and successors 36, 37.
  - Not changed: Φ stays in the definitions (REFEREE 21: «keep it (it is harmless) or drop it»; kept).
- The scope words are unchanged: «a RELOCATION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim; …)».
- L-1 sha1 and the full word-diff against cd121dff: see the commit message and the Lead message of this entry; reproduce with
  `git diff --no-index --word-diff=plain docs/si/P-N5-ODD-line.txt docs/si/P-N5-ODD-line-L1.txt`.

## Entry 4: D-ODD-1 (REFEREE 21) = F-1 (REFEREE-2 24), DATA DEFECT in §7 (no signed item affected)
- REFEREE 21: «D-ODD-1 (DATA defect, not a signed item). sbq2_K8_m16.start (sha1 98b0927a…) sets τ(242) := 243.»; «So the W-rank DEAD's
  witness is an artifact of an unfaithful start. The DEAD needs a new instance or must be withdrawn.»
- REFEREE-2 24: «243 is not a successor of the Odd vertex 242 (succ(242) = 244, 246, …, 258).»; «n5x.start_pair applies start entries
  unvalidated.»
- Confirmed (L-SI 37): experiments/si/src54/inst/sbq2_K8_m16.pg line «242 0 1 244,246,248,250,252,254,256,258». With τ(242) repaired to
  each of its 8 successors (the start otherwise unchanged), the run has 153 states, τ changes once, σ̄(260) flips 128 times, and
  W(242) = W(259) holds at 0 states (the original: 153). All 8 repairs give identical counts for every tool below.
- Repaired pin: experiments/si/src54/inst/sbq2_K8_m16_fix.start = the original with «242:243» → «242:244» (the smallest successor). The
  original file is kept, byte-identical to its copies at l-red flipev and l-new box97 / box110, and is marked invalid in
  experiments/si/src54/inst/INVALID.txt. Re-run of the box-54..58 sbq2 rows (original → repaired):
  | tool | original start | repaired start |
  | --- | --- | --- |
  | wtie (W-rank DEAD) | states 153, Wtie 153, sbflips 128 | states 153, Wtie 0, sbflips 128 |
  | oddadd | VOLD 0, ODDCH 2237, OSRC 769, PROP 120, PFX 649, VADD 0, MAXHXS 128 | VOLD 0, ODDCH 2206, OSRC 762, PROP 120, PFX 642, VADD 0, MAXHXS 136 |
  | oddadd MUT control | VOLD 2881 | VOLD 2849 (bites) |
  | ascw (sbq2 row of ASC-W / TURN-W) | BAD 540, TURNBAD 58 | BAD 525, TURNBAD 58 |
  | srcfuel (box 56/57) | SRCEV 144, FUEL 136, FUELEV 258, LEXV 0 | SRCEV 143, FUEL 135, FUELEV 257, LEXV 0 |
  | anc (box 58) | FUELEV 497, all checks 0 | FUELEV 496, all other counts identical, all checks 0 |
- Consequences:
  - The box-54 DEAD «W-rank potential» (sbq2: W(242) = W(259) at all 153 states) is WITHDRAWN in docs/si/DEAD.md: its witness was an
    artifact of the non-edge. No valid replacement instance is known. The W-rank potential is therefore OPEN (not dead).
  - ASC-W and TURN-W stay DEAD: their primary witness is src2_K3 (start valid), and the sbq2 rows survive the repair (BAD 525, TURNBAD 58).
  - The quadratic σ̄-flip count (128) survives, as both referees found.
  - OLD-PLAY / ODD-STEP / FUEL-LEX data on sbq2: 0 violations on the repaired start too.
- Start validation: experiments/si/startcheck.py (rejects a non-edge or a wrong-owner entry). Called by src54/oddadd.py, src54/wtie.py,
  src54/ascw.py, grow56/srcfuel.py and anc58/anc.py before the run. Scan of the 101 game / start pairs in the box 50b corpus lists and the
  si pins: 3 invalid, sbq2_K8_m16.start and two already-known L-RED files (red/n3/instances/comp54_n80.start, n3cov_lean.start; L-RED's R99
  erratum 5e8f0174f has *_fixed.start for both). On those two, anc.py's counts are identical with the _fixed starts (iters 55 / 35,
  CHG 1241 / 269, all checks 0). The corpus lists still name the original files (2 of 1,132 lines); not changed here, so a corpus
  rerun of a validating tool prints START BAD on those two lines; the stored outputs are unchanged.
- check.sh: «box 54» wtie row → the repaired start with «Wtie 0 sbflips 128»; oddadd / MUT / box 58 sbq2 rows → the repaired start with the
  new counts; a start-validation row rejects the original.

## Entry 5 (L-SI successor 37, 2026-10-31 15:2xZ): word-diff verdicts on L-1; line revision L-2 (docs/si/P-N5-ODD-line-L2.txt)
- REFEREE-2 24 (claude/referee-2 301198b4, R2-N5-ODD-L1.md): L-1 MATCHES; signs the G-ODD-1 repair and entry 2 (Lead 15:17Z).
- REFEREE 21 (claude/referee 0449d8fd, docs/referee/R-N5-ODD.md §C): L-1 does not yet match, one REQUIRED item:
  - «ONE remaining free pair: ODD-L5 (REQUIRED). «(Corollary FUEL-COUNT) the number N of fuel re-routes of (y, z) in F …». (y, z) is bound
    only in FUEL-LEX's own clause («for every pair (y, z) and consecutive fuel re-routes …»), and the clauses are separated by «;». So in
    FUEL-COUNT the pair is bound in another clause. Fix: «(Corollary FUEL-COUNT) for every pair (y, z), the number N …».»
  - REFEREE 21 also: «Entry 2 (G-ODD-2 = my N-ODD-2): ACCEPTED. … I sign it (Opus 5.5, D15). Under L41 this is my independent signature of
    the repair.» Entries 1 and 4 accepted.
- Change: L-2 = L-1 with exactly one insertion, «(Corollary FUEL-COUNT) {+for every pair (y, z),+} the number N of fuel re-routes of (y, z)
  in F». No other token differs (`git diff --no-index --word-diff=plain docs/si/P-N5-ODD-line-L1.txt docs/si/P-N5-ODD-line-L2.txt`).
- Status: G-ODD-1 is signed by both referees (each wrote it); G-ODD-2 by both (REFEREE-2 wrote it, REFEREE signs it as its N-ODD-2).

## Entry 6 (L-SI successor 37, 2026-10-31 18:3xZ): CHECKER C108 (claude/checker 68c5ea14, docs/checker/C108.md) FAIL E-1; line revision L-3 (docs/si/P-N5-ODD-line-L3.txt)
- C108: «E-1: the title's DATA clause «and of all seven statements in both referees' own checks» is wider than the record (§5).»; «So no
  engine checks ODD-ADD directly. «all seven statements in both referees' own checks» reads as two independent engines verifying all
  seven, which is false.» Move: ««and of all seven statements in both referees' own checks» → «and of every statement in both referees'
  own checks».»
- C108 N-1 (optional, taken): «Optional, in the same revision (N-1): «Ξ_k(x) ⊴ val(σ_k, ρ)(x) for every positional Odd strategy ρ and
  every vertex x» → «Ξ_k(x) ⊴ val(σ_k, ρ)(x) for every state k, every positional Odd strategy ρ and every vertex x».»
- Change: L-3 = L-2 with exactly these two replacements (each phrase occurs once in L-2). Word-diff vs L-2:
  «for every {+state k, every+} positional Odd strategy ρ» and «and of [-all seven statements-]{+every statement+} in both referees' own
  checks». No other token differs.
- The record behind the DATA clause (for the reader of this file): REFEREE's odd_probe.py checks OLD-PLAY, ODD-STEP, SRC-ROOT, FUEL-LEX,
  FUEL-COUNT; REFEREE-2's odd_check.py checks those and ODD-RELAY, and ODD-ADD through ODD-RELAY. No engine checks ODD-ADD directly
  (it is a counting corollary of ODD-RELAY).
