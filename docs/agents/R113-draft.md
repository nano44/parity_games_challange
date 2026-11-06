# Draft RESULTS R113 (Lead; first fill 2026-11-06T11:20:49Z by date -u (subagent) on P-IDEAL-ALIGN line L-2, docs/new/P-IDEAL-ALIGN-line-L2.txt, l-new c787aab1, sha1 cb5f0398431cc1a5122e13327e7bbae9f9985e51) — to CHECKER C125 — NOT LANDED; goes after R112, before Erratum E-1
FIRST FILL (this text). Read at the origin heads fetched at its start (git fetch, 2026-11-06T11:0xZ): l-new b38726b4 (its ancestor
c787aab1 holds L-2 and fixes entry 1; b38726b4 changes no P-IDEAL-ALIGN file: the packet, L-1, L-2, the fixes, box178/aligncheck.py,
box178/aligncheck.out, box150/check.py, box172/inst/dd_d5_F14.json and experiments/new/check.sh are byte-equal at c787aab1 and
b38726b4, git diff empty), referee 1140096d (its ancestor 0e2c354f holds §C of R-P-IDEAL-ALIGN.md, byte-equal at 1140096d), referee-2
ee1d6e18 (its ancestor ddca4cc7 holds Addendum 1 of R2-P-IDEAL-ALIGN.md, byte-equal at ee1d6e18), checker 89764538; origin trunk
1393ebbc («Lead: RESULTS R112 TR3 landed (P-TR3 line L-3: T^R(3) = 8, machine-certified; CHECKER C123 Add. 1 89764538 PASS; CI 6403
green); GAPS line-11 UPDATE; log»), pushed. referee, referee-2 and checker were already ancestors of 1393ebbc; l-new was not. Local
trunk 7302bc7c = one merge (--no-ff) of l-new b38726b4 into 1393ebbc; then the commit holding this file (and the commit holding
docs/agents/R110-note-E3-draft.md). Not pushed. c787aab1 and b38726b4 are NOT ancestors of origin trunk 1393ebbc (git merge-base
--is-ancestor); cb8e0dca, 6f0daf60, 0e2c354f, ea08029d and ddca4cc7 are. The Lead pushes trunk before landing. The body makes NO
statement about trunk (C113 E-2). R111 and R112 ARE LANDED: RESULTS R111 (l. 11598, e751969c) and R112 (l. 11909, 1393ebbc), and GAPS
l. 11 ends with R112's UPDATE. RESULTS (sha1 70407ce74b93fb77fae28452e9ccd6b3ea2b01e8, 12,730 lines), GAPS (sha1
f204d0a12bd3d5eb1160c64a96260e88f073dbbd, 23 lines; l. 11 76 "|", 47 «UPDATE 2026-»), TARGET.md, DECISIONS, NOW and CLAUDE.md are
byte-equal at 1393ebbc and 7302bc7c (git diff --quiet). Last commit on RESULTS and GAPS: 1393ebbc (2026-11-06T10:37:50Z).
Sources read: the packet docs/new/P-IDEAL-ALIGN.md (frozen cb8e0dca, sha1 d8acdececb507bfad476341411bddd579fcc5b00, 180 lines,
18,683 bytes; unchanged at c787aab1 and b38726b4), line L-1 (cb8e0dca, e46b0417295bfbde7f4cb2d434deed5d0f2e209c), fixes entry 1 and
line L-2 (c787aab1); experiments/new/box178/aligncheck.py (sha1 9335dee71554491004b5f7567bb1a6784c5292dd, 93 lines) and aligncheck.out
(sha1 b653b01bbdca19c8e0c7d406b1bd2470c35c55fc, 4 lines), box150/check.py (Gen: keys, optkey, face, run), experiments/new/check.sh
block «P-IDEAL-ALIGN» (l. 919-927 at c787aab1); REFEREE successor 24's docs/referee/R-P-IDEAL-ALIGN.md (report 6f0daf60, §C 0e2c354f;
l. 1-127 at 0e2c354f = the report, by cmp) with scratch/align_probe.py and align_logs/ (corpus.txt, random.txt); REFEREE-2 successor
28's docs/referee-2/R2-P-IDEAL-ALIGN.md (report ea08029d, Addendum 1 ddca4cc7; l. 1-89 at ddca4cc7 = the report, by cmp) with
R2-P-IDEAL-ALIGN/r2align.py and r2align_seed178.out; RESULTS R104 (title l. 9864), R105 (l. 10155), R108 (l. 10812), R110 (l.
11323-11597), R111 (l. 11598-11908), R112 (l. 11909-12151), Erratum E-1 (l. 12152), E-2 (l. 12165) and the Dead-ends section (l.
12193-); GAPS l. 11; DECISIONS L41, L42, L43, L45; docs/agents/LEAD-STATE.md (2026-11-06 entries to 10:37Z); docs/checker/C120.md-C124.md
and notes/CHECKER.md (89764538); docs/agents/R111-draft.md and R112-draft.md as landed (the models of this draft).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r113, from a git
archive of c787aab1's experiments/new and docs/new, nothing written into the repository): (a) check.sh block «P-IDEAL-ALIGN» (l. 1-6,
the «cd» and «tmp» lines, l. 919-927), 2026-11-06T11:07:03Z, rc 0, PASS line «P-IDEAL-ALIGN: aligncheck 0 violations (output = frozen
aligncheck.out); pins packet d8acdece, line L-1 e46b0417, tool 9335dee7, output b653b01b, instance 06f0e501, fixes 25b050ee, line L-2
cb5f0398: PASS» (runw178.sh, w178.out); aligncheck.py's raw output byte-equal to aligncheck.out (cmp; w178raw.out); (b) my split of
aligncheck.py's counter sets (acstats.py = aligncheck.py plus recording lines that draw no random number, built by acstats_make.py; its
first 4 output lines equal aligncheck.out): LAND checks 11,824 (t ≥ 1), KFF checks 21,296 (level ≥ 1), MOV checks 11,324 at level 0 and
21,296 at level ≥ 1, F0 checks 5,662 (F(0) ≤ 2 only), 0 files skipped by RuntimeError, runs 184 corpus + 5,478 random, runs by d 1: 2,
2: 1,098, 3: 4,286, 4: 143, 5: 120, 6: 11, 8: 2; corpus 184 files with 156 distinct contents (20 groups of byte-identical copies;
dd_d5_F14 three times: box152, box160/ext, box172/inst); the 44 equalities F(l) = 2F(l − 1) + 2: 30 corpus, 14 random, dd_d5_F14's
level 3 three times (its three copies); measured with the same runs, not lane DATA: F(l) ≤ 2^(l+2) − 2 0 violations, 2d + 2 Σ F(l) ≤
2^(d+2) − 2d − 4 0 violations (acstats.out); (c) my own simulator (mysim113.py: mysim111.py's definitions, written from the packet §0
text, β-SET comparison, no ENC; no lane or referee code imported) on the same 184 corpus files from their stored starts: every part of
ALIGN, F0 (both halves), PAIR-DOUBLE, MOVES (both parts), T-BOUND (all three inequalities) and PATH-RISE (rises of the current β-set by
the R104 order against P(z) counted by recursion), 0 violations, 30 equalities; dd_d5_F14 (sha1 06f0e501…) in 𝓛^R_5, acyclic, T 14,
F(0..4) = 2, 3, 6, 14, 7, F(3) = 2F(2) + 2 (mysim113.out); (d) the L-1 → L-2 byte test and token diff (wdiff113.py); (e) the premise
quote test (prem113.py, hits.py); (f) the UPDATE build with 16 controls (upd113.py); (g) the quote sweep, the line-precise check, the
stale-status grep and the landing simulation (chk113.py, sim113.py).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1:
the premise route is checked against what RESULTS records (G-4; prem113.py, hits per quote). C116 G-1, C118-C124 §4: the UPDATE rule of
R111 (sentinel_build111 with its default drops and the «(DATA, » opening), unchanged; no adaptation (G-U). C116 G-2: name clashes
settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed; the instance inlined. C118 E-1: no stale status
sentence; the entry calls nothing «pending» (the only «PENDING» is the title fill) and states no other item's status as current except
landed RESULTS entries (G-11). C118 §3 / Erratum E-2: every DEFINITION of L-2 diffed against the packet (G-2). C120 §5 / C121 §5 / C122
E-2 / C124 E-1, and REFEREE fadbb9a0 R-P-IDEAL-KEYS l. 241-242 «Lesson: test each DATA clause against the tool's counter code (unit and
set), not only against the packet's §8 wording.»: EVERY DATA clause of L-2 tested against aligncheck.py's counter code, unit and set
(G-9; three clauses flagged). C122 G-0: parentheses balanced (G-1). C122 E-3: the source note names every proof-carrying file (G-1).
C123 E-1: no lane label and no packet name in the title before the claims (G-1). C123 E-2: no stale referee state (G-13). C119 E-1:
every «referee X did Y» is checked against that referee's file (line-precise check, Addendum (5)).
to check: FLAGS FIRST (G-0 to G-14; four of them are for the Lead or CHECKER: G-0 (number), G-9 (i)-(iii) (three DATA clauses whose
counter differs from the named clause; C124 E-1 class), G-9 (iv) (ALIGN's packet labels (a)-(c) in the DATA only), G-8 (the scope
tail's description and the R108 comparison)), then the CLEAN items and (0)-(14). A NOTE FOR THE LEAD that is NOT part of this entry:
G-C (P-IDEAL-KEYS is now R111; T^R(3) = 8 is now R112; neither is used).
- G-0, THE CHECKER NUMBER. «C125» and «C126» occur 0 times in the repository at 7302bc7c and on origin claude/checker, referee,
  referee-2 and l-new (git grep); docs/checker/ ends at C124.md; notes/CHECKER.md (89764538) l. 5-6 names only «C123 Add. 2 (landed
  check + CI)» as NEXT. This draft uses C125 (title fill, UPDATE head, GAPS preamble); the Note E-3 draft uses C126.
- G-9, DATA (the C120 §5 / C121 §5 / C124 E-1 check item: unit and set of every count, against aligncheck.py's counter code). Every
  figure of L-2's DATA parenthesis equals aligncheck.out and my re-run: «184» = «SCOPE corpus files 184»; «300 random» = «random 300»;
  «5,662 runs» = «runs 5662»; «22,472 (state, level ≥ 1) pairs» = «statelevels 22472»; «11,824 of them with t ≥ 1» = statelevels −
  runlevels and = my LAND check count; «10,648 (run, level ≥ 1) pairs» = «runlevels 10648»; «equality on 44» = «dbltight 44»; «32,620
  (run, mover) pairs» = «runmovers 32620»; «21,296 with level ≥ 1» = my KFF check count; the TIGHT line «TIGHT dd_d5_F14 LR True T 14 F
  [2, 3, 6, 14, 7] F(3) = 2F(2) + 2 True». Counter by counter (aligncheck.py l. 43-71, read by me):
  - ALIGN: KPEQ (l. 50-51) and ORD (l. 53-54) on every (state, level ≥ 1) pair; LAND (l. 52) under «if t and any(», i.e. on the
    (s_t, l) pairs with t ≥ 1, each testing the movers of the pair that moved at step t against c computed from the keys of s_t. The
    line's «ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥ 1) pairs and (b) on the 11,824 of them with t ≥ 1»: unit and set
    MATCH (fixes F-a; REFEREE AL-L1 (i)).
  - PAIR-DOUBLE: DBL per (run, l ≥ 1) (l. 57-60), «dbltight» the equalities. MATCH.
  - PATH-RISE: PATH per (run, mover) (l. 69-70), rises of cv (face, the ENC integer of the current chain) against P(z) by recursion
    over the options (l. 36-42). MATCH.
  - (i) F0 (FLAG, C124 E-1 class: unit). «F0 0 on 5,662 runs»: the counter F0 (l. 56, «if F[0] > 2: C["F0"] += 1») tests only F(0) ≤
    2. The line's F0 clause is «each level-0 mover moves at most once and F(0) ≤ 2»; its first half is tested by MOV at level 0 (l. 68,
    bound 1), 11,324 = 2 × 5,662 (run, level-0 mover) pairs, which the line counts under MOVES (item (ii)). Packet §7 l. 162 names the
    unit exactly: «Lemma F0 (F(0) ≤ 2): 5,662 runs, 0 violations.»; the line drops «(F(0) ≤ 2)».
  - (ii) MOVES (FLAG, C124 E-1 class: set). «MOVES 0 on 32,620 (run, mover) pairs for the moves bound»: MOV (l. 68) runs on every
    (run, mover) pair, 21,296 at level ≥ 1 (moves(x) ≤ 1 + F(l − 1)) and 11,324 at level 0 (moves(x) ≤ 1). The line's MOVES clause is
    «KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1) for every mover x of level l ≥ 1»: its moves bound has 21,296 pairs; the other 11,324
    test F0's first half. The count is the packet's (§5 Corollary MOVES includes «For x of level 0: moves(x) ≤ 1.», l. 131; §7 l. 164
    «the moves bound at every level»), but the line moved level 0 into its F0 clause. REFEREE's own fix text (R2, §5 l. 110) carries
    the 32,620; fixes F-a l. 12 «MOV (the moves bound) on every (run, mover) pair».
  - (iii) T-BOUND (FLAG, C124 E-1 class: unit). «T-BOUND 0 on 5,662 runs»: TB (l. 71) tests T ≤ 2d + 2 Σ_(l ≤ d−2) F(l) and T ≤
    2^(d+2) − 2d − 4 per run; the clause's first inequality «F(l) ≤ 2^(l+2) − 2» is not counted (it follows from the F0 and DBL counts
    on the same runs by the corollary's induction, but no counter tests it); packet §7 l. 165 says «Corollary T-BOUND (both
    inequalities): 5,662 runs, 0 violations.». Measured for this draft on the same runs (acstats.py; my DATA, not lane DATA, not wired
    into check.sh): 0 violations of F(l) ≤ 2^(l+2) − 2 and of the middle inequality; my own simulator (c) the same on the corpus.
  - Both referees' own tools cover these statements (DATA, not the line's): REFEREE align_probe.py l. 57 tests both halves of F0
    («F[0] > 2 or any(» … «> 1 for y in (0, 1))»); REFEREE-2 r2align.py l. 59 tests «any(F[l] > 2 ** (l + 2) - 2 for l in range(d))»
    in TBOUND1. Neither referee raised (i)-(iii) on the line: REFEREE §5 l. 99 «F0 0 on 5,662 runs» and «T-BOUND 0 on 5,662 runs»: «one
    check per run. MATCH.»; REFEREE-2 l. 80 «DATA: each count names its statement». Per the brief the line is not changed here; CHECKER
    rules E-item or note. If E: one possible L-3 wording, not mine to choose and not a quotation: "F0 0 on 5,662 runs for F(0) ≤ 2";
    "MOVES 0 on the 21,296 (run, mover) pairs with level ≥ 1 for both parts, and F0's moves bound 0 on the other 11,324"; "T-BOUND's two
    bounds on T 0 on 5,662 runs (F(l) ≤ 2^(l+2) − 2: no separate DATA)". All three figures are lane counts already printed by
    aligncheck.out or derived from it (11,324 = 2 × 5,662, as fixes F-a l. 13 derives 21,296).
  - (iv) ALIGN's LABELS (NOTE for CHECKER). The DATA says «ALIGN (a) and (c)» and «(b)», but the line's ALIGN clause carries no item
    labels: its three parts, in order, are packet §2's (a) «both movers 2l and 2l + 1 have KP_s = c_l(s)», (b) «each of them that moves
    at step t moves to option c_l(s_t)» and (c) «the order of their keys under s is …». The labels came in with R1 (REFEREE's §5 fix
    text). The body states the mapping (Claims (a), Data). Note or E-item: CHECKER.
  - (v) PRECISION, «184 in-tree 𝓛^R_d genome files»: 184 files with 156 distinct contents; «files» is exact (C124 G-9 (vi) precedent).
    The 44 equalities count dd_d5_F14's level 3 three times (three byte-identical copies); «equality on 44, among them L-RED's
    dd_d5_F14 at level 3» is true as worded. Note.
  - (vi) PRECISION, KP-MOVE: «KP-MOVE outside 𝓛^R_d: no separate DATA» is exact (aligncheck.py has no KP-MOVE counter; on 𝓛^R_d the
    MOV and KFF counters test its consequence). Note.
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-2 is one line, 3,191 characters, 3,330 bytes with the newline, 641 whitespace
  tokens, 76 «(» / 76 «)», depth never negative, final depth 0 (C122 G-0: met); 0 "|"; 0 guillemets; one « — », with its own date
  parenthesis «(2026-11-06)», «2026» once. It begins «In the IDEAL model of RESULTS R104»: no packet name and no lane label before the
  claims (C123 E-1: met); the packet name occurs only in the source note, as in R109-R112. Source note «(P-IDEAL-ALIGN,
  docs/new/P-IDEAL-ALIGN.md with its fixes entry 1, docs/new/P-IDEAL-ALIGN-fixes.md; L-NEW successor 55)»: the packet carries every
  proof (packet l. 4-5 «this packet carries every proof in full and is checked against this text only; no other file carries a proof of
  a statement below.»); fixes entry 1 l. 6 «This entry carries no proof.». Every proof-carrying file is named (C122 E-3: met). REFEREE
  §C l. 149 «AL-L1 MET; AL-L2 MET; the source note names the fixes file.»; REFEREE-2 Add. 1 l. 107 «The source note now names the fixes
  file, which carries no proof.». The title is "### R113 [refereed-only] " + L-2 + the fill ", CHECKER PASS (docs/checker/C125.md,
  checker PENDING)", nothing inserted.
- G-2, DEFINITIONS DIFFED AGAINST THE PACKET (the C118 §3 / Erratum E-2 lesson; my own diff). (i) Premise parenthesis = packet l.
  19-32 (G-4). (ii) «T the number of steps of a run» = §0 l. 49 («T := the number of steps.»). (iii) «Mv_t the movers of step t» = l.
  49 (Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}). (iv) «moves(x) the number of steps t with x ∈ Mv_t» = l. 55, the E-2 (E2c) binder. (v)
  «KP_s(x) the option of x with the least key under s» = l. 56 (unique by (F1)); «KF_x the number of steps t with KP_(s_t)(x) ≠
  KP_(s_(t−1))(x)» = l. 56. (vi) flip: «for two distinct movers u, w of one level a flip of (u, w) at step t a change between s_(t−1)
  and s_t of the order of the keys of their current options» = l. 57-58 (ord_s(u, w) := [key_s(u, s(u)) < key_s(w, s(w))]). (vii) «on
  𝓛^R_d F(l) the number of steps at which the pair (2l, 2l + 1) flips» = l. 59 (0 ≤ l ≤ d − 1 implicit). (viii) «for 1 ≤ l ≤ d − 1
  c_l(s) the option index k for which mover 2(l − 1) + k has the smaller current key under s» = l. 60-61 (c_l(s) := 0 iff b_l(s) =
  ord_s(2l − 2, 2l − 1), i.e. iff mover 2l − 2 has the smaller current key; REFEREE l. 36-37 checked the orientation). (ix) «γ_l(j) :=
  [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)» = l. 61 with §0 l. 38 («a gate index g(x, k)»). (x) «cv_s(z)
  the integer value of z's current option (R105 ENC)» = l. 62 (v_s, cv_s). (xi) «P(z) the number of maximal Ξ-paths from z (one option
  chosen at every mover on the way, ending at the exit X)» = l. 64-65. Claims: ALIGN = §2 (a)-(c) l. 70-72 in that order; KP-MOVE = §3
  l. 87-89 (frame «on acyclic Ξ-graphs» = IDEAL-ACYC; «at any degree elsewhere» = «any degree elsewhere»); F0 = l. 96; PAIR-DOUBLE = l.
  103; MOVES = l. 131 at level ≥ 1 (its level-0 sentence is the line's F0 first half: narrower or equal); T-BOUND = l. 134 (0 ≤ l ≤ d −
  1 implicit); PATH-RISE = l. 142-143 («any width» implicit in «at any degree»). ALL EQUAL. Both referees diffed every definition of
  L-1 (REFEREE §5 l. 95 «Definitions diffed against §0: T, Mv_t, moves(x) (E2c binder), KP_s, KF_x, flip, F(l), c_l(s), γ_l(j), cv_s and
  P(z) all MATCH.»; REFEREE-2 l. 73-75); L-2 changes one definition (R3: g defined) and no claim.
- G-3, STRICT SYMBOL TEST (notes). u, w, s, t, l, j, k, x, z are bound in their clauses; «d» is free in 𝓛^R_d (each clause «on
  𝓛^R_d»); «g» is defined by R3; «X» is R104's exit (§0 l. 37); «𝓛^R_d» is R110's (premise); «KP_s» in ALIGN is KP_s(x) for x = 2l, 2l
  + 1; «cv(z)» in PATH-RISE is cv_s(z) along the run; «2·6 + 2» in the DATA is F(3) = 2F(2) + 2 with F(2) = 6. «L-RED's dd_d5_F14» is an
  attribution (packet l. 168-169: a byte copy of claude/l-red experiments/red/r197/lag/dd_d5_F14.json).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem113.py, hits.py on RESULTS at 7302bc7c). L-2's premise parenthesis: «premise:
  R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC and MONO only; and RESULTS R110's definition of 𝓛^R_d
  only». Packet l. 19-32: ENC (265 characters) and MONO (69 characters), each 1 hit in RESULTS, R105's title l. 10155; R110's 𝓛^R_d
  wording (191 characters) 2 hits: R110's title l. 11323 (the source) and R112's body l. 12020-12021, which quotes R110's definitions
  verbatim (R112 landed after the packet and after both referees' tests: REFEREE §1 l. 7 «Premises checked against trunk 4b35e2b0
  (RESULTS).», l. 23 «R110's 𝓛^R_d wording: verbatim (1 hit).»); with its R110 context («R109's SEG-ONCE at l = −1 only), on acyclic
  Ξ-graphs, with 𝓦_d …») the wording has 1 hit, l. 11323. R104: the packet restates the definition in §0 (l. 35-66, «RESULTS R104's
  definition, as restated in P-IDEAL-FLIP §0 and P-IDEAL-KEYS §0»); R104's own wording, «an IDEAL genome G has N movers x with levels
  lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the
  exit X, a distinct β-rank with a parity, a distinct gate index, and a start; …» (861 characters, as packet P-TR3 §1 l. 7-14 quotes it), 1 hit, R104's
  title l. 9864. REFEREE-2 l. 23-24 diffed §0 against R104 («R104: §0 is the same restatement as P-IDEAL-KEYS §0, which I diffed
  against RESULTS R104 l. 9864»). Use: ENC and MONO in PATH-RISE only (packet l. 21-24); R110's wiring in ALIGN (a) (l. 73) and
  through it in every 𝓛^R_d item; R104's definition everywhere. Not used: packet l. 30-32 (R105 KEYFLIP, LOCAL and every other R105
  item, R106-R109, P-IDEAL-KEYS, docs/lit, docs/sources, any other lane file; «No machine premise is used by any signed item.»);
  REFEREE §1 l. 25-29; REFEREE-2 l. 27-28 («I read every proof step: no other premise is used.»). Erratum E-2: does not bear (packet l.
  24-26; REFEREE l. 24; REFEREE-2 l. 25-26). R108 appears in the line only in the scope tail as a landed comparison («improving RESULTS
  R108's bound T ≤ 3^d − 1 …»), not as a premise: «T ≤ 3^d − 1 on a d-level ladder with two movers of degree 2 per level» is 1 hit,
  R108's title l. 10812, inside R108's frame «on acyclic Ξ-graphs, any number of movers per level»; 𝓛^R_d is such a ladder (REFEREE-2
  l. 77-79). No unlanded result, no lit note, no lane file and no machine premise is a premise of a signed statement.
- G-5, ERRATA (note). Erratum E-1 concerns R97-R100 counts; Erratum E-2 concerns R105's CHAIN-BACK, TOP-MONO and KEYFLIP; L-2 uses
  R105's ENC and MONO only, which E-2 leaves unaffected («Unaffected: R105's other definitions»). moves(x) carries the (E2c) binder
  anyway (packet l. 25-26). Not bearing.
- G-6, NAMES (by script on RESULTS 70407ce7 / GAPS f204d0a1; note; C116 G-2's remedy). 0 times in RESULTS and GAPS: «R113», «C125»,
  «P-IDEAL-ALIGN», «KP-MOVE», «PAIR-DOUBLE», «PATH-RISE», «aligncheck», «c_l(s)», «γ_l», «DBL-O(1)», «2^(d+2) − 2d − 4». Same names,
  other meanings: «ALIGN» once (R67); «(F0)» once (R96); «T-BOUND» 4 times (R7, R9); «MOVES» inside «PAIR-MOVES» (R111, and GAPS l. 11);
  «P(z)» once (R99); «AL-L1» and «AL-P1» are REFEREE gap labels of R104's packet (12 and 3 times there). Consistent: «PAIR-LIN» is R111's
  conjecture of that name (not claimed in either); dd_d5_F14 is the genome of R109 / R111 (sha1 06f0e501…). One body sentence (Honest
  limits (viii)).
- G-7, L41 (the C109 E-1 class): not triggered (my reading). The proofs are L-NEW successor 55's (packet l. 2, 6); the fixes entry
  carries no proof; R1 and R2 are REFEREE's DATA fix texts and R3, R4 REFEREE-2's word changes (line wording, not proof steps). Neither
  referee mentions L41.
- G-8, THE SCOPE TAIL (NOTE for CHECKER). (a) «a STRUCTURE / EXPONENTIAL-BOUND statement inside the IDEAL model on the key side of
  2-wide ladders» describes ALIGN, F0, PAIR-DOUBLE, MOVES and T-BOUND; KP-MOVE is stated for every acyclic genome and PATH-RISE is a
  Ξ-side lemma at any degree and width (their own clauses say so: «at any degree elsewhere», «at any degree»). A description, not a
  claim, and no clause is narrowed by it; the tail's «genomes outside 𝓛^R_d (outside PATH-RISE and KP-MOVE) are not covered» keeps
  the two apart. Both referees MATCHED the tail. Note. (b) «improving RESULTS R108's bound … (strictly for d ≥ 3; equal at d = 1, 2)»:
  checked: 3^d − 1 = 2, 8, 26, 80 and 2^(d+2) − 2d − 4 = 2, 8, 22, 52 for d = 1-4; for d ≥ 3, 3^d − 1 > 2^(d+2) − 2d − 4 (both
  referees: REFEREE §C l. 145, REFEREE-2 l. 78-79). It is a comparison of two landed-or-landing bounds, not a READING inside a claim
  clause (C124 G-8 (b): «Later lines should keep readings in the scope tail (the R110 form) rather than inside a claim clause.»: met).
  (c) No DEAD, no CONDITIONAL, no L43 item. «polynomially» once («bounds nothing polynomially»); «O(» 0.
- G-10, LEAD READINGS AND RULINGS (the C111 E-1 class): CLEAN. L-2 cites no Lead reading and no ruling (by script: «Lead reading» 0,
  «L4» 0, «D1» 0). The lane works under D14 / D18 / D20 (packet l. 2). The freeze brief (packet l. 2-3 «Lead brief BOX 178 (2026-11-06
  03:23Z)»; the freeze cb8e0dca is 03:24:15Z) and the fix-round relay (fixes l. 3 «Lead relay 05:32Z of fix round 1»; LEAD-STATE
  05:53Z; the lane commit c787aab1 is 05:31:56Z) are messages; their exact minutes are not verifiable from the repository (D-2).
- G-11, STALE LANE TEXT (notes; nothing here lands as current). (i) Packet l. 31 «the signed but not yet landed packet P-IDEAL-KEYS
  (R111; its PAIR-KF and LADDER are not used: §2 and §3 re-prove what is needed)»: P-IDEAL-KEYS is RESULTS R111 since e751969c; the
  packet does not use it (REFEREE l. 27; REFEREE-2 l. 27-28); the body says so in the present tense (Premise: RESULTS R111 among the items not used). (ii)
  Fixes F-b l. 20-21 «T^R(3) = 8 = packet P-TR3 (signed, not yet landed)»: T^R(3) = 8 is RESULTS R112 since 1393ebbc; F-b's values are
  lane DATA «not used by any statement» (l. 20); the body cites F-b only as what it does and states R112's landing correctly. (iii)
  REFEREE l. 68 and §C l. 140, REFEREE-2 Add. 1 l. 102 call P-TR3 «not landed»: true then; history. (iv) notes/L-NEW.md 8bf32e2e
  («P-IDEAL-ALIGN pending») is a log. The entry says only what L-2 says and what RESULTS now holds.
- G-12, SHA1 PINS IN check.sh (the C110 F-1 / C116 G-3 class): present. experiments/new/check.sh block «P-IDEAL-ALIGN» (cb8e0dca, l.
  919-927; at c787aab1 the same lines with pin178 extended by the fixes 25b050ee and L-2 cb5f0398; check.sh 927 lines, sha1
  3ea24d7e3dff5d50042c5c4298331ce6094d229a at c787aab1 and b38726b4) compares aligncheck.py's output with the frozen aligncheck.out and
  pins the packet, L-1, the tool, its output, dd_d5_F14, the fixes and L-2. Re-run: PASS (Re-runs (a)).
- G-13, THE REFEREES' ROUNDS (note; state on file at this fill). L-1 (e46b0417): REFEREE (6f0daf60) all seven statements SIGN, L-1
  «NOT YET: REQUIRED AL-L1 (two DATA clauses wider than the tool's counters); optional AL-L2» (l. 18), optional AL-P1 (l. 67-71);
  REFEREE-2 (ea08029d) all seven SIGN, «No gap. No REFUSE.» (l. 20), L-1 «**MATCHES** (optional word changes P-1, P-2)» (l. 19). Fix
  round (fixes entry 1, c787aab1): F-a (AL-L1), F-b (AL-P1), F-c (P-1, P-2 = AL-L2), L-2 = L-1 with R1-R5. Second round: REFEREE §C
  (0e2c354f) «L-2 MATCHES.», «Fixes entry 1 is CORRECT.», «All seven statements stay SIGNED. Open items of mine: none.» (l. 151-153);
  REFEREE-2 Add. 1 (ddca4cc7) «**Fixes entry 1: CORRECT.**» (l. 95), «**Line L-2: MATCHES.**» (l. 105), «My seven SIGNs stand.» (l.
  107). No addendum after these is on origin (R-P-IDEAL-ALIGN.md byte-equal at 0e2c354f and 1140096d; R2-P-IDEAL-ALIGN.md at ddca4cc7
  and ee1d6e18). No gap is open at either referee.
- G-14, THE FIXES FILE (note). Fixes entry 1 carries no proof (l. 6) and changes no statement, proof or hypothesis (l. 5-6); F-a and
  F-b re-read packet §7 and §5 text, F-c is line-only. The source note names it (G-1).
- G-C, NOTE FOR THE LEAD (not part of R113; nothing about it is in the entry beyond G-11's present-tense sentences): R111 and R112 are
  now landed; R113 uses neither (packet l. 30-32; T-BOUND's «Does NOT claim» T^R values are lane DATA, F-b). The Lead may later
  compare T^R(3) = 8 (R112) with T-BOUND's 22 at d = 3; the line does not.
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on cb5f0398):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (docs/new/P-IDEAL-ALIGN-line-L3.txt absent at b38726b4); L-1
  appears only in the line history.
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (Addendum (2)).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4.
  C110 F-1 / C116 G-3 (pins): G-12.
  C111 E-1 (stale Lead-reading statements): G-10.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 / E-2 (scope; instance under-specified): the tightness instance is inlined in Claims (d) (every option field, the start, the
  fifteen states).
  C118 E-1 (stale status sentence): no «pending» in the entry; R111 and R112 named as landed; no other item's status (G-11).
  C118 §3 / Erratum E-2 lesson (definitions diffed): G-2.
  C120 §5 / C121 E-1 / C122 E-2 / C124 E-1 (DATA unit and set against the counter code): G-9; three clauses flagged ((i)-(iii)).
  C122 G-0 (parentheses): 76 / 76, depth never negative (G-1).
  C122 E-3 (source note): CLEAN (G-1).
  C123 E-1 (lane label or packet name before the claims): none (G-1).
  C123 E-2 (stale referee state): G-13.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R113 goes DIRECTLY AFTER R112's block. docs/RESULTS.md at local trunk 7302bc7c (= origin trunk 1393ebbc for this file)
has sha1 70407ce74b93fb77fae28452e9ccd6b3ea2b01e8, 12,730 lines (wc -l), last changed by 1393ebbc (R112's landing). «### R112» is l.
11909 (entry l. 11909-12150, l. 12151 blank); «**Erratum E-1**» is l. 12152; «**Erratum E-2**» is l. 12165; «## Dead ends (kept;» is
l. 12193. PROPOSED (R102's to R112's layout): insert R113's entry after l. 12151 (R112's blank line), with one blank line after it, so
the R-entries stay contiguous and both errata follow them. "### R113" occurs 0 times in RESULTS and GAPS; «R113» 0 times. GAPS has sha1
f204d0a12bd3d5eb1160c64a96260e88f073dbbd, 23 lines, last changed by 1393ebbc. If the Note E-3 draft (docs/agents/R110-note-E3-draft.md)
lands first, it sits after Erratum E-2 and before the Dead ends, below R113's place: R113's insertion point and block are unchanged.
(1) TITLE. The title is the line file docs/new/P-IDEAL-ALIGN-line-L2.txt (l-new c787aab1e33ce464e59281df29d2f4037f5ffa38,
2026-11-06T05:31:56Z, the file's only commit, sha1 cb5f0398431cc1a5122e13327e7bbae9f9985e51, 3,330 bytes with the newline; unchanged
at the l-new head b38726b4), verbatim: one line, no heading marker (it begins «In the IDEAL model of RESULTS R104»), no outer quotes,
no final period. NOTHING is stripped and NOTHING is inserted: the heading is the level-3 marker, then "R113 [refereed-only] ", then the
file without its newline, then the fill ", CHECKER PASS (docs/checker/C125.md, checker PENDING)" (as R90-R112). Built by script
(fill113.py: assert the sha1 cb5f0398…, equality with the blob at c787aab1 and at the l-new head, one line, no marker, one «
(2026-11-06) — », no "|"; prepend, append) and re-checked after writing this file (chk113.py): equal, byte for byte. Heading:
3,270 characters, 3,408 bytes; sha1 of the heading line without its newline ae1d939fcc61007ee80d855ea417d5bd63b88d71; it is l. 347 and the only «### R» line of this file.
(2) LINE HISTORY: two lines. L-1 e46b0417295bfbde7f4cb2d434deed5d0f2e209c (cb8e0dca, frozen with the packet, the file's only commit;
3,055 bytes, 582 tokens, 69 «(» / 69 «)»): REFEREE NOT YET (AL-L1), REFEREE-2 MATCHES with optional P-1, P-2 (G-13). L-2 cb5f0398
(c787aab1; 3,330 bytes, 641 tokens, 76 / 76): fixes entry 1 lists five replacements R1-R5 (fixes l. 31-37) and their word diff (l.
38-49); my byte test (wdiff113.py: R1-R5 parsed from fixes l. 33-37, outermost guillemets; each old string once in the current text
when applied in order, each new string once in L-2) gives L-1 with R1-R5 = L-2 byte for byte (True); my token diff (difflib on
whitespace tokens) finds 6 non-equal hunks (5 tokens out, 64 in), all inside R1-R5. Both referees byte-tested L-2 the same way (REFEREE
§C l. 146-147 «L-1 + R1..R5, each old string once, gives sha1 cb5f0398…, 3,330 bytes: EQUAL to L-2.»; REFEREE-2 Add. 1 l. 105-106
«applying them gives a string byte-identical to L-2 (3,330 B)»). R1, R2 narrow two DATA ranges (AL-L1); R3 defines g (P-1); R4 bounds
«improving» (P-2 = AL-L2); R5 names the fixes file. No hunk changes a claim. So the title is L-2, and L-1 is history.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 24, docs/referee/R-P-IDEAL-ALIGN.md: report 6f0daf60 (2026-11-06T04:32:55Z, new file,
127 lines, sha1 ddecaab349361fa74c99bddb96ac51466b7694aa), §C 0e2c354f (2026-11-06T05:51:24Z, 153 lines, sha1
9e4df3674e2936086759280107792dbd0a3c6119): «L-2 MATCHES.» (l. 151). REFEREE-2 successor 28, docs/referee-2/R2-P-IDEAL-ALIGN.md: report
ea08029d (2026-11-06T04:16:35Z, new file, 89 lines, sha1 b6fcce64bf2cfdf2b2d735b652f4fb6ee29ec4b6): L-1 «**MATCHES** (optional word
changes P-1, P-2)»; Addendum 1 ddca4cc7 (2026-11-06T05:51:29Z, 107 lines, sha1 4177f480861d27fe24ee78e643c5a7580c86dca9): «**Line L-2:
MATCHES.**» (l. 105). Both MATCH L-2.
(4) CLAIMS SIGNED = the items below, each SIGN in BOTH referees' verdict tables (REFEREE "## 0. Verdicts" l. 10-18; REFEREE-2 "##
Verdicts" l. 11-20), unchanged in their second rounds (REFEREE §C l. 153; REFEREE-2 Add. 1 l. 107); the cells are the reports' words:
| item (source) | REFEREE (successor 24) | REFEREE-2 (successor 28) |
| --- | --- | --- |
| (a) Lemma ALIGN (a), (b), (c) (packet §2 l. 68-84) | l. 12 «SIGN» | l. 13 «**SIGN** (Opus 5.5, D12)» |
| (b) Lemma KP-MOVE (a), (b) (§3 l. 87-95) | l. 13 «SIGN» | l. 14 «**SIGN** (Opus 5.5, D12)» |
| (c) Lemma F0 (§3 l. 96-100) | l. 13 (the same row) | l. 15 «**SIGN** (Opus 5.5, D12)» |
| (d) Theorem PAIR-DOUBLE (§4 l. 102-127) | l. 14 «SIGN» | l. 16 «**SIGN** (Opus 5.5, D12); tight (dd_d5_F14, level 3; recomputed)» |
| (e) Corollary MOVES (§5 l. 129-133) | l. 15 «SIGN» | l. 17 «**SIGN** (Opus 5.5, D12)» |
| (f) Corollary T-BOUND (§5 l. 134-139) | l. 15 (the same row) | l. 17 (the same row) |
| (g) Lemma PATH-RISE (§6 l. 141-152) | l. 16 «SIGN» | l. 18 «**SIGN** (Opus 5.5, D12)» |
Both, verbatim: REFEREE l. 123-124 «All seven statements SIGNED: ALIGN, KP-MOVE, F0, PAIR-DOUBLE, MOVES, T-BOUND and PATH-RISE, with
ALIGN (a)-(c) and KP-MOVE (a), (b) each signed.», §C l. 153; REFEREE-2 l. 20 «No gap. No REFUSE.», Add. 1 l. 107. No gap is open at
either referee.
Clause checks (L-2 against the packet; G-2): ALIGN = l. 70-72; KP-MOVE = l. 88-89; F0 = l. 96; PAIR-DOUBLE = l. 103; MOVES = l. 131
(level ≥ 1); T-BOUND = l. 134; PATH-RISE = l. 142-143. Nothing in L-2 is wider than signed.
Signed by both, NOT stated by L-2 as separate items: MOVES' level-0 sentence (in L-2 it is F0's first half); the intermediate
quantities of PAIR-DOUBLE's proof (Φ, Φ′, the D-states, M, B₁). Not signed, so NOT landed: packet §7 (DATA, machine checks, EXCLUDED,
TARGET diff, READING; «DATA / READING (not to sign)», l. 17), in particular the bound F(l) ≤ F(l − 1) + 1 when γ_l(0) ≠ γ_l(1)
(machine-checked by box177/automaton.py only, l. 171-172), CONJECTURE DBL-O(1), CONJECTURE PAIR-LIN, the READING l. 178-180, and §5's
T^R values (lane DATA, fixes F-b).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R105's ENC
and MONO (title l. 10155); RESULTS R110's definition of 𝓛^R_d (title l. 11323). Nothing else for a signed statement. RESULTS R108 (l.
10812) is cited in the scope tail as a comparison only. The source docs/new/N5-PAIRDOUBLE-box177.md (packet l. 4) is history; the
tightness instance is a data file ((10)).
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at 1393ebbc's version). RESULTS labels in L-2 (by script): «R104» 3 («RESULTS
R104», «R104's definition», «theorem of R104»); «R105» 2 («RESULTS R105's ENC and MONO only», «(R105 ENC)»); «R110» 1; «R108» 1 (scope
tail). Each exists: R104 l. 9864, R105 l. 10155, R108 l. 10812, R110 l. 11323. Erratum E-2 governs R105's KEYFLIP, CHAIN-BACK and
TOP-MONO, none used. No Lead reading and no other RESULTS label is cited. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST: G-3. Every symbol of L-2 is R104's (IDEAL model, Ξ-graph, acyclic, mover, level, option, key, gate index, state, step,
run, exit X), R105's (ENC, MONO, the integer value), R110's (𝓛^R_d), bound in the line (T, Mv_t, moves(x), KP_s(x), KF_x, flip, F(l),
c_l(s), γ_l(j), g(x, k), cv_s(z), P(z), and the clause variables), a file with its path (aligncheck.py, the packet, the fixes), or a
landed RESULTS entry (R108's bound). Agreeing tests: REFEREE §5 l. 95-96; REFEREE-2 l. 73-76.
(8) FIXES AND STATUS NOTES (docs/new/P-IDEAL-ALIGN-fixes.md, L-NEW successor 55, append-only, one entry, one commit c787aab1): sha1
25b050ee187559f757c02eca97ed4f32d0c28b8f, 49 lines, 4,686 bytes. Header l. 1 («(append-only; the packet docs/new/P-IDEAL-ALIGN.md, sha1
d8acdece…, stays frozen)»). Entry 1 (l. 3-49): reports answered (l. 4-6); F-a AL-L1 (l. 8-16); F-b AL-P1 (l. 18-23); F-c P-1, P-2 =
AL-L2 (l. 25-27); line L-2 with R1-R5 and the word diff (l. 29-49). Verdicts: REFEREE §C l. 135-149; REFEREE-2 Add. 1 l. 95-107.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills nothing («DBL-O(1)», «PAIR-DOUBLE»,
«PATH-RISE» occur 0 times in GAPS; «PAIR-LIN» once, in R111's UPDATE, not claimed in either). A line-11 UPDATE is proposed at the end,
to go AFTER R112's UPDATE (GAPS at 1393ebbc: the last UPDATE on l. 11 is R112's «UPDATE 2026-11-06 10:37Z: RESULTS R112 (P-TR3; CHECKER
C123 89764538) [refereed-only] LANDED: …», ending «G-N5-TIME stays open.» before the row's closing « |»; l. 11 holds 76 "|" and 47
«UPDATE 2026-»), as a pure insertion with one separating space. BUILT FROM L-2 (scratch upd113.py = upd112b.py l. 1-284 unchanged
(controls R97-R111; its l. 284, the state assertion that R111's UPDATE is the last on l. 11, is commented out because R112's now follows
it), plus R112's control, plus R113). CONTROLS (same script, same run, rc 0): R97's to R112's LANDED UPDATEs (GAPS l. 11 at 1393ebbc)
rebuilt from their lines byte for byte (True ×16; R112's from P-TR3 L-3 at 9c70c980 through upd112b.py's R112 call with head «UPDATE
2026-11-06 10:37Z: RESULTS R112 (P-TR3; CHECKER C123 89764538) [refereed-only] », 1,736 bytes filled, also equal to R112-draft l. 570
and to r112/fill2/upd112L3.txt with <DATE> 2026-11-06, <HH:MM> 10:37, <checker> 89764538). R113: the R111 procedure (sentinel_build111
of upd111.py, unchanged, default drops) on L-2: 7 labels, each found once after the start «ending at the exit X): », in order, moved
behind their clauses; « (2026-11-06) — » → «: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …» (R111's
«(DATA, » opening); «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a TARGET.md claim» dropped; the source parenthesis
kept; «. G-N5-TIME stays open.» appended. L-2 has no DEAD clause, so no clause is put back. NO ADAPTATION: L-2's scope sentences are
R111's default pair. Labels with inner «; »: none of the seven clauses has one, so build()'s cut at the last «; » before the next label
is exact. Cross-check: a direct build written in upd113.py (claims split before each "; (LABEL) ", each label moved behind its clause, the tail
opened and the two sentences dropped by string replacement): equal (True). L-2 holds no "|", so no replacement list. Checked by script:
one line, 0 "|", one «<DATE>», one «<HH:MM>», one «<checker>», 3,364 bytes, 3,228 characters, 640 tokens, 75 «(» / 75 «)», balanced;
«2026-11-06» 0 times; token multiset diff against L-2 = the head, the seven moved labels, «(DATA,» opened, the two dropped scope
sentences, « — » and the final sentence (upd113.out). Head «UPDATE <DATE> <HH:MM>Z: RESULTS R113 (P-IDEAL-ALIGN; CHECKER C125
<checker>) [refereed-only] » («P-IDEAL-ALIGN» 0 times in GAPS); <DATE> = the landing date.
(10) DATA of record = packet §7 (l. 154-180), NOT signed; L-2's DATA parenthesis states its counts per statement, with the three
flags of G-9. Re-run at this fill: Re-runs (a)-(c) in the header (PASS; my split; my own simulator).
- PASS line: «P-IDEAL-ALIGN: aligncheck 0 violations (output = frozen aligncheck.out); pins packet d8acdece, line L-1 e46b0417, tool
  9335dee7, output b653b01b, instance 06f0e501, fixes 25b050ee, line L-2 cb5f0398: PASS».
- aligncheck raw (byte-equal to aligncheck.out, cmp): «SCOPE corpus files 184 random 300»; «COUNTS runs 5662 steps 5602 statelevels
  22472 runlevels 10648 runmovers 32620 dbltight 44»; «KPEQ 0 LAND 0 ORD 0 DBL 0 F0 0 KFF 0 MOV 0 TB 0 PATH 0»; «TIGHT dd_d5_F14 LR
  True T 14 F [2, 3, 6, 14, 7] F(3) = 2F(2) + 2 True». Equal to both referees' runs of the block at cb8e0dca (REFEREE §3 l. 86-87;
  REFEREE-2 l. 65-66).
- My split and my simulator: header Re-runs (b), (c).
NOT re-run: the referees' tools (docs/referee/scratch/align_probe.py; docs/referee-2/R2-P-IDEAL-ALIGN/r2align.py); I read their
committed logs (align_logs/corpus.txt, random.txt; r2align_seed178.out), whose counts equal the reports (REFEREE §3 l. 78-84; REFEREE-2
l. 55-63). check.sh's other blocks and scripts/verify.sh: not run.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the three DATA clauses of G-9 (i)-(iii). D-2 packet l. 2-3 «Lead
brief BOX 178 (2026-11-06 03:23Z)» and fixes l. 3 «Lead relay 05:32Z of fix round 1» against the lane commits cb8e0dca (03:24:15Z)
and c787aab1 (05:31:56Z), the relay one minute after the commit; stamps of messages, not verifiable from the repository. D-3 REFEREE
§3 l. 80 calls its corpus «L-NEW corpus box150-179 at cb8e0dca»; at cb8e0dca no box179 exists and box178 has no JSON, and its log
align_logs/corpus.txt has the glob «box1[5-7][0-9]» with «L^R genomes 184»: the set is aligncheck.py's 184. D-4 REFEREE-2's loader
reads 103 of the 184 𝓛^R files (l. 56); its own set, not the lane's. D-5 independence timing: REFEREE-2's report (04:16:35Z) precedes
REFEREE's (04:32:55Z) by 16 min 20 s; each states it did not read the other's directory (REFEREE l. 2-3; REFEREE-2 l. 2-3); in the second
round REFEREE knew REFEREE-2's items through the fixes entry only (§C l. 134); the two second rounds were pushed 5 s apart (05:51:24Z,
05:51:29Z). D-6 REFEREE-2 l. 62-63 and Add. 1 l. 102-103 compare its maxima with T^R(1..3) = 2, 4, 8 and «13 at d = 4»: DATA, not used.
(12) Excluded: packet §7 (DATA counts, machine checks, pins, EXCLUDED, TARGET diff, READING); the γ_l(0) ≠ γ_l(1) bound (machine only);
CONJECTURES DBL-O(1) and PAIR-LIN; box177's DATA and READINGS; T-BOUND's «Does NOT claim» T^R values (F-b); boxes 179- (later lane
work). Not part of this entry.
(13) Commits: lane (claude/l-new): cb8e0dca (2026-11-06T03:24:15Z; freeze: packet d8acdece (180 lines), L-1 e46b0417, aligncheck.py,
aligncheck.out, check.sh block P-IDEAL-ALIGN) → c787aab1 (2026-11-06T05:31:56Z; fixes entry 1, 49 lines; L-2; pin178 extended); later
lane commits change no P-IDEAL-ALIGN file (8bf32e2e handover, ee58acfb, box 179). The instance: experiments/new/box172/inst/dd_d5_F14.json
(l-new b302bbf5, sha1 06f0e5015d09c0f1e03f1b9293ab3cd8483e435b). REFEREE (claude/referee): 6f0daf60 (report; align_probe.py 133 lines,
align_logs/corpus.txt, random.txt) → 0e2c354f (§C, +26 lines). REFEREE-2 (claude/referee-2): ea08029d (report; r2align.py 77 lines,
r2align_seed178.out) → ddca4cc7 (Addendum 1, +18 lines). CHECKER: 89764538 (C123 Add. 1). Trunk: see the header.
(14) Placement: see (0). DEAD-ENDS ROWS: NONE (not drafted). R113 kills nothing.

### R113 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC and MONO only; and RESULTS R110's definition of 𝓛^R_d only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), for two distinct movers u, w of one level a flip of (u, w) at step t a change between s_(t−1) and s_t of the order of the keys of their current options, on 𝓛^R_d F(l) the number of steps at which the pair (2l, 2l + 1) flips, for 1 ≤ l ≤ d − 1 c_l(s) the option index k for which mover 2(l − 1) + k has the smaller current key under s, γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k), cv_s(z) the integer value of z's current option (R105 ENC) and P(z) the number of maximal Ξ-paths from z (one option chosen at every mover on the way, ending at the exit X): (ALIGN) on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j; (KP-MOVE) at any degree elsewhere, a mover x of degree 2 that moves at step t moves to KP_(s_t)(x), so moves(x) ≤ 1 + KF_x; (F0) on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤ 2; (PAIR-DOUBLE) on 𝓛^R_d, F(l) ≤ 2F(l − 1) + 2 for 1 ≤ l ≤ d − 1; (MOVES) on 𝓛^R_d, KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1) for every mover x of level l ≥ 1; (T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2 and T ≤ 2d + 2(F(0) + … + F(d − 2)) ≤ 2^(d+2) − 2d − 4; (PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run (2026-11-06) — a STRUCTURE / EXPONENTIAL-BOUND statement inside the IDEAL model on the key side of 2-wide ladders, improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d (strictly for d ≥ 3; equal at d = 1, 2); bounds nothing polynomially; the bound F(l) ≤ F(l − 1) + 1 for γ_l(0) ≠ γ_l(1) (machine-checked only) and the conjectures PAIR-LIN and DBL-O(1) are not claimed; Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside PATH-RISE and KP-MOVE) are not covered; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/new/box178/aligncheck.py on the 184 in-tree 𝓛^R_d genome files of experiments/new/box150 to box177 from their stored starts and 300 random 𝓛^R_d genomes, 5,662 runs: ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥ 1) pairs and (b) on the 11,824 of them with t ≥ 1; F0 0 on 5,662 runs; PAIR-DOUBLE 0 on 10,648 (run, level ≥ 1) pairs, equality on 44, among them L-RED's dd_d5_F14 at level 3 (F(3) = 14 = 2·6 + 2); MOVES 0 on 32,620 (run, mover) pairs for the moves bound and on the 21,296 with level ≥ 1 for KF_x = F(l − 1); T-BOUND 0 on 5,662 runs; PATH-RISE 0 on 32,620 (run, mover) pairs; KP-MOVE outside 𝓛^R_d: no separate DATA) (P-IDEAL-ALIGN, docs/new/P-IDEAL-ALIGN.md with its fixes entry 1, docs/new/P-IDEAL-ALIGN-fixes.md; L-NEW successor 55), CHECKER PASS (docs/checker/C125.md, checker PENDING)
- Object (L-NEW successor 55, Opus 5.5, D14 / D18 / D20, box 178; frozen, unchanged during review): packet P-IDEAL-ALIGN,
  docs/new/P-IDEAL-ALIGN.md, sha1 d8acdececb507bfad476341411bddd579fcc5b00, 180 lines (l-new freeze cb8e0dca, 2026-11-06T03:24:15Z;
  identical at c787aab1 and b38726b4). Both referees measured the sha1 (REFEREE l. 5 «docs/new/P-IDEAL-ALIGN.md: sha1
  d8acdececb507bfad476341411bddd579fcc5b00, 180 lines;»; REFEREE-2 l. 6 «docs/new/P-IDEAL-ALIGN.md sha1
  d8acdececb507bfad476341411bddd579fcc5b00, 180 lines;»). Labels (l. 6-7): «Labels: PROVED (L-NEW 55, unrefereed) / DATA / READING (not
  to sign). Not a TARGET.md claim. Every statement is about the IDEAL model of RESULTS R104 only. The bounds proved are exponential.» To
  sign (table l. 9-17): §2 ALIGN, §3 KP-MOVE and F0, §4 PAIR-DOUBLE, §5 MOVES and T-BOUND, §6 PATH-RISE; §7 «DATA / READING (not to
  sign)». Sections: premises (l. 19-33), §0 the model and notation (l. 35-66), §2 (l. 68-84), §3 (l. 86-100), §4 (l. 102-127), §5 (l.
  129-139), §6 (l. 141-152), §7 (l. 154-180). Source (l. 4): docs/new/N5-PAIRDOUBLE-box177.md §0; «this packet carries every proof in
  full and is checked against this text only; no other file carries a proof of a statement below.» (l. 5).
  Fixes: docs/new/P-IDEAL-ALIGN-fixes.md, append-only, entry 1 (c787aab1; 49 lines, sha1 25b050ee187559f757c02eca97ed4f32d0c28b8f): F-a
  checks the two DATA ranges of the line against aligncheck.py's counter code; F-b labels the T^R values of §5's «Does NOT claim» as
  lane DATA used by no statement; F-c defines g in the line and qualifies «improving»; line L-2. Entry 1: «Both sign all seven
  statements; no statement, proof or hypothesis changes here. This entry carries no proof.» (l. 5-6).
  The RESULTS line is L-2, cb5f0398431cc1a5122e13327e7bbae9f9985e51 (docs/new/P-IDEAL-ALIGN-line-L2.txt, l-new c787aab1,
  2026-11-06T05:31:56Z, the file's only commit; 3,330 bytes). The title is L-2 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-06)» and its source note are the line's own; the source note names the packet, which carries every proof, and the fixes
  file, which carries none). L-2's parentheses balance (76 «(» / 76 «)»). Line history: L-1 (e46b0417, cb8e0dca, frozen with the
  packet); L-2 (cb5f0398, c787aab1, fixes entry 1: L-1 with exactly five replacements R1-R5, fixes l. 33-37: the ALIGN and MOVES DATA
  ranges narrowed to the counter code (AL-L1), g defined in γ_l (P-1), «improving» qualified «(strictly for d ≥ 3; equal at d = 1, 2)»
  (P-2 = AL-L2), the fixes file named in the source note; L-1 with R1-R5 equals L-2 byte for byte, by my script). L-2 MATCHES at both
  referees, each after its own byte test: REFEREE (0e2c354f) §C l. 147 «L-1 + R1..R5, each old string once, gives sha1 cb5f0398…, 3,330
  bytes: EQUAL to L-2.», l. 151 «L-2 MATCHES.»; REFEREE-2 (ddca4cc7) Addendum 1 l. 105 «**Line L-2: MATCHES.**», l. 106 «applying them
  gives a string byte-identical to L-2 (3,330 B)». Both diffed every definition of L-1 against packet §0 (REFEREE §5 l. 95; REFEREE-2 l.
  73-75); L-2 adds the definition of g and changes no other definition.
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report 6f0daf60, §C 0e2c354f; REFEREE-2 successor 28 «(Opus 5.5, D12/D20)»,
  report ea08029d, Addendum 1 ddca4cc7). Items (a)-(g) are SIGN in both verdict tables (REFEREE "## 0. Verdicts" l. 10-18 of
  R-P-IDEAL-ALIGN.md; REFEREE-2 "## Verdicts" l. 11-20 of R2-P-IDEAL-ALIGN.md) and stand in both second rounds (REFEREE §C l. 153 «All
  seven statements stay SIGNED. Open items of mine: none.»; REFEREE-2 Add. 1 l. 107 «My seven SIGNs stand.»). REFEREE-2 l. 20 «No gap.
  No REFUSE.». Every item is about R104's IDEAL model on acyclic Ξ-graphs; (a), (c), (d), (e) and (f) on 𝓛^R_d (RESULTS R110's 2-wide
  degree-2 ladders: movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to
  mover 2(l − 1) + k); (b) for a mover of degree 2 of any acyclic genome; (g) at any degree and width. Notation (packet §0 l. 49-65):
  T the number of steps, Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}; moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c));
  KP_s(x) the option k of x with the least key_s(x, k) (unique by (F1)), KF_x := #{t ∈ [1, T] : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}; for u ≠
  w of one level ord_s(u, w) := [key_s(u, s(u)) < key_s(w, s(w))], a flip of (u, w) at t a change of ord between s_(t−1) and s_t,
  flips(u, w) their number; on 𝓛^R_d, F(l) := flips(2l, 2l + 1), and for 1 ≤ l ≤ d − 1, p := 2l, q := 2l + 1, b_l(s) := ord_s(2l − 2,
  2l − 1), c_l(s) := 0 if b_l(s) is true, else 1, γ_l(j) := [g(p, j) < g(q, j)] with g the gate index; v_s(x, k) := Σ over the β's of
  Ξ_s(x, k) of ±2^rank (+ for even parity), cv_s(x) := v_s(x, s(x)); P(z) the number of maximal Ξ-paths from z, a maximal Ξ-path being
  a sequence of options (y_0, k_0), …, (y_r, k_r) with y_0 = z, y_(i+1) = xt(y_i, k_i) and xt(y_r, k_r) = X. (F1) the keys of two
  distinct options of one level differ; (F2) if x ∈ Mv_t, then s_t(x) is available and strictly better under s_(t−1), and at degree 2
  s_(t−1)(x) is x's other option (l. 50-53).
  (a) Lemma ALIGN (§2 l. 68-82) [G ∈ 𝓛^R_d; 1 ≤ l ≤ d − 1; any run; s any state, t any step]: «(a) KP_s(p) = KP_s(q) = c_l(s).»; «(b)
      If x ∈ {p, q} and x ∈ Mv_t, then s_t(x) = c_l(s_t).»; «(c) ord_s(p, q) = [s(p) = c_l(s)] if s(p) ≠ s(q), and ord_s(p, q) = γ_l(j)
      if s(p) = s(q) = j.». In the line these are, in order, the ALIGN clause's three parts (its DATA calls them (a), (c) and (b)).
      Proof: wt(x, k) = 2(l − 1) + k for both x ∈ {p, q} (R110's wiring), so key_s(x, k) is the key of the current option of mover 2l −
      2 + k followed by g(x, k); the two prefixes are keys of options of two distinct movers of level l − 1, unequal by (F1), and decide;
      (b) by (F2) both options are available and the step takes the one with the least key under s_t; (c) distinct options of p, q give
      the two lower movers' prefixes, equal options give equal prefixes and the gates decide. Cells: REFEREE l. 12 «SIGN»; REFEREE-2 l.
      13 «**SIGN** (Opus 5.5, D12)».
  (b) Lemma KP-MOVE (§3 l. 87-95) [IDEAL-ACYC, x of degree 2, any run]: «(a) If x ∈ Mv_t, then s_t(x) = KP_(s_t)(x).»; «(b) moves(x) ≤
      1 + KF_x.». Proof: as ALIGN (b); consecutive moves go to different options, so KP(x) changes in each window [t_i + 1, t_(i+1)],
      and the windows are disjoint. It re-proves R105 KEYFLIP's degree-2 argument for one mover (l. 94-95), so KEYFLIP is not a premise.
      Cells: REFEREE l. 13 «SIGN»; REFEREE-2 l. 14 «**SIGN** (Opus 5.5, D12)».
  (c) Lemma F0 (§3 l. 96-100) [G ∈ 𝓛^R_d, d ≥ 1; any run]: «Then moves(0) ≤ 1, moves(1) ≤ 1, and F(0) ≤ 2.». Proof: level-0 keys are
      the constant gates, so KF = 0 and KP-MOVE (b) gives moves ≤ 1; a flip of (0, 1) needs a step moving 0 or 1. Cells: REFEREE l. 13
      (the KP-MOVE row); REFEREE-2 l. 15 «**SIGN** (Opus 5.5, D12)».
  (d) Theorem PAIR-DOUBLE (§4 l. 102-127) [G ∈ 𝓛^R_d; 1 ≤ l ≤ d − 1; any run]: «Then F(l) ≤ 2 F(l − 1) + 2.» (l. 103). Proof: with c_t
      := c_l(s_t), the b-steps (b_l changes) are exactly the F(l − 1) flip steps of the pair below; Φ(t) the number of movers of {p, q}
      not on option c_t; a non-mover's alignment toggles at a b-step, a mover lands aligned (ALIGN (b)); by ALIGN (c) the order of (p,
      q) is a function of the alignments and c_t, and a flip without a move of p or q needs a b-step from a state with Φ = 1; summing
      the changes of Φ gives F(l) ≤ Φ(0) + Σ over the b-steps of h(Φ(t − 1)) with h ≤ 2, so F(l) ≤ 2 + 2F(l − 1). Tight: the genome
      experiments/new/box172/inst/dd_d5_F14.json (sha1 06f0e5015d09c0f1e03f1b9293ab3cd8483e435b; a byte copy of L-RED's claude/l-red
      experiments/red/r197/lag/dd_d5_F14.json), in 𝓛^R_5, with option fields (W-target, Ξ-target, gate, β rank, β parity; X the exit, −
      no W-target) mover 0 (lev 0): (−, 4, 4, 7, even), (−, 3, 17, 12, odd); 1 (lev 0): (−, 9, 3, 6, odd), (−, X, 9, 10, even); 2 (lev
      1): (0, 8, 18, 1, odd), (1, 1, 15, 4, odd); 3 (lev 1): (0, X, 11, 19, even), (1, X, 16, 9, odd); 4 (lev 2): (2, 6, 6, 16, odd),
      (3, 9, 2, 15, odd); 5 (lev 2): (2, 8, 19, 13, odd), (3, 3, 8, 8, odd); 6 (lev 3): (4, 7, 0, 14, even), (5, 5, 5, 11, odd); 7 (lev
      3): (4, 5, 7, 3, even), (5, 2, 10, 2, odd); 8 (lev 4): (6, 9, 12, 17, even), (7, 3, 14, 18, odd); 9 (lev 4): (6, 3, 13, 5, odd),
      (7, X, 1, 0, even); start 1101111110 (movers 0..9); run 1101111110, 1111111011, 1111110001, 1111100101, 1111101101, 1111001001,
      0100000001, 0100010111, 0100011110, 0000111010, 0010110000, 0010100100, 0010101100, 0010001000, 0010000000: T = 14, F(0..4) = 2,
      3, 6, 14, 7, and F(3) = 14 = 2F(2) + 2 (packet §7 l. 168-169; aligncheck.out «TIGHT dd_d5_F14 LR True T 14 F [2, 3, 6, 14, 7]
      F(3) = 2F(2) + 2 True»; REFEREE-2 l. 64 «my run: T 14, F(0..4) = 2, 3, 6, 14, 7; F(3) = 14 = 2 · 6 + 2. ✓»; REFEREE §3 l. 82-83;
      my own simulator for this draft: the same 15 states and F values). The option fields are those of movers 0-9 printed in RESULTS R111
      Claims (j). Cells: REFEREE l. 14 «SIGN»; REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12); tight (dd_d5_F14, level 3; recomputed)».
  (e) Corollary MOVES (§5 l. 129-133) [G ∈ 𝓛^R_d; any run]: «For every mover x of level l ≥ 1: KF_x = F(l − 1) and moves(x) ≤ 1 + F(l
      − 1). For x of level 0: moves(x) ≤ 1.». Proof: by ALIGN (a), KP_s(x) = c_l(s), which changes iff b_l changes, i.e. iff (2l − 2, 2l
      − 1) flips; KP-MOVE (b); level 0 is F0. The line states the level-≥-1 part under MOVES and the level-0 part under F0. Cells:
      REFEREE l. 15 «SIGN»; REFEREE-2 l. 17 «**SIGN** (Opus 5.5, D12)».
  (f) Corollary T-BOUND (§5 l. 134-139) [G ∈ 𝓛^R_d; any run]: «F(l) ≤ 2^(l+2) − 2 for 0 ≤ l ≤ d − 1, and T ≤ 2d + 2 Σ_(l=0..d−2) F(l)
      ≤ 2^(d+2) − 2d − 4.». Proof: F(0) + 2 ≤ 4 and F(l) + 2 ≤ 2(F(l − 1) + 2); every step moves a mover, so T ≤ Σ_x moves(x) ≤ 2 +
      Σ_(l=1..d−1) 2(1 + F(l − 1)); the sum of 2^(l+2) − 2 over l = 0, …, d − 2 is 2^(d+1) − 4 − 2(d − 1). Values 2, 8, 22, 52 at d =
      1-4 (both referees recomputed them: REFEREE l. 61, REFEREE-2 l. 48-49). Cells: REFEREE l. 15 (the MOVES row); REFEREE-2 l. 17 (the
      same row).
  (g) Lemma PATH-RISE (§6 l. 141-152; premises R105 ENC, MONO) [IDEAL-ACYC, any degree, any width; z any mover; any run]: «Then the
      number of steps at which cv(z) rises is at most P(z) − 1.» (l. 142-143). Proof: the current chain of z is a maximal Ξ-path; two
      distinct maximal Ξ-paths first differ at a mover y both visit, with different options there, and each visits y once (acyclic), so
      their β-sets differ, hence (ENC) their integers differ; so cv(z) takes at most P(z) values, and by MONO it never decreases. Cells:
      REFEREE l. 16 «SIGN»; REFEREE-2 l. 18 «**SIGN** (Opus 5.5, D12)».
  The RESULTS line (L-2) states (a)-(g) with their exact hypotheses, and nothing wider.
- Premise: RESULTS R104's definition of the IDEAL model and of the Ξ-graph (no R104 theorem), restated in packet §0 (REFEREE-2 l. 23-24
  diffed the restatement against RESULTS R104 l. 9864); RESULTS R105's ENC and MONO, each quoted verbatim by the packet (l. 21-24:
  «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even
  parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»
  and «(MONO) the current Ξ-value of every mover never decreases along a run»), each 1 hit in RESULTS (R105's title, l. 10155),
  whitespace normalised; and RESULTS R110's definition of 𝓛^R_d, quoted verbatim by the packet (l. 27-29: «the 2-wide degree-2 ladders
  in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1
  W-pointing to mover 2(l − 1) + k)»), found in R110's title (l. 11323) and quoted from there in R112's body. L-2: «premise: R104's
  definition of the model only, no theorem of R104 used; RESULTS R105's ENC and MONO only; and RESULTS R110's definition of 𝓛^R_d only».
  Use: ENC and MONO in PATH-RISE only; R110's wiring in ALIGN (a) and through it in F0, PAIR-DOUBLE, MOVES and T-BOUND. Not used: R105
  KEYFLIP (KP-MOVE re-proves its degree-2 argument), R105 LOCAL and every other R105 item, R106-R109, RESULTS R111 (P-IDEAL-KEYS; its
  PAIR-KF and LADDER are not used, ALIGN (a) and PAIR-DOUBLE re-prove what is needed), RESULTS R112, docs/lit, docs/sources, any other
  lane file (packet l. 30-32; REFEREE l. 25-28; REFEREE-2 l. 27-28). «No machine premise is used by any signed item.» (packet l. 32);
  REFEREE l. 29 «No machine premise. The γ(0) ≠ γ(1) bound is machine-only and is EXCLUDED, correctly.». Both referees byte-tested the
  three quotes against RESULTS (REFEREE l. 22-23; REFEREE-2 l. 25, 27). Erratum E-2 does not bear (packet l. 24-26; REFEREE l. 24;
  REFEREE-2 l. 25-26). RESULTS R108's bound, named in the line's scope tail, is a comparison, not a premise.
- L41 and L43. The proofs are L-NEW successor 55's (packet l. 2, 6); the fixes entry carries none; the referees' align_probe.py and
  r2align.py are checking tools. Nothing referee-written is a proof step of the entry (my reading; neither referee mentions L41). No
  DEAD item; L43 does not bear.
- Fixes (docs/new/P-IDEAL-ALIGN-fixes.md, L-NEW successor 55, append-only; entry 1 at c787aab1, 49 lines, sha1
  25b050ee187559f757c02eca97ed4f32d0c28b8f), after REFEREE 6f0daf60 and REFEREE-2 ea08029d:
  - F-a (l. 8-16, AL-L1): LAND (ALIGN (b)) is counted under «if t and …» (aligncheck.py l. 52), so (b) covers 22,472 − 10,648 = 11,824
    pairs; KFF (KF_x = F(l − 1)) under «if l >= 1 and …» (l. 67), so it covers 32,620 − 2·5,662 = 21,296 pairs; packet §7's MOVES count
    is to be read with that split. REFEREE §C l. 135-137 «F-a (AL-L1): CORRECT.»; REFEREE-2 Add. 1 l. 96-101 («These are finer than my
    reading; I accept them.»).
  - F-b (l. 18-23, AL-P1): §5's «Does NOT claim» values T^R(1..4) = 2, 4, 8, 13 are labelled lane DATA, «not landed and not used by any
    statement», with their sources. REFEREE §C l. 138-142; REFEREE-2 Add. 1 l. 102-103. (Since then T^R(3) = 8 is RESULTS R112; no
    statement here uses it.)
  - F-c (l. 25-27, P-1, P-2 = AL-L2): line only; g is §0's gate index; at d = 1, 2 both bounds are 2 and 8, from d = 3 the new one is
    strictly smaller (22 < 26). REFEREE §C l. 143-145; REFEREE-2 Add. 1 l. 104.
  - Line L-2 (l. 29-49): L-1 «with exactly these five replacements, applied by script» (l. 31), R1-R5 (l. 33-37) and the word diff (l.
    38-49).
  No fix changes a statement, a proof or a hypothesis; F-a and F-b re-read packet text; F-c and R1-R5 change the line's wording only.
- Not signed: packet §7 (DATA, machine checks, EXCLUDED, TARGET diff, READING; «DATA / READING (not to sign)», l. 17), in particular
  the bound F(l) ≤ F(l − 1) + 1 when γ_l(0) ≠ γ_l(1), «machine-checked only, by exhaustive DP over the 8-state automaton (a_p, a_q, b)
  for F(l − 1) ≤ 30» (l. 171-172), and the READING l. 178-180; §5's T^R values (lane DATA, F-b). OPEN, not claimed: CONJECTURE DBL-O(1)
  and CONJECTURE PAIR-LIN (l. 173); any polynomial bound on F(l) or T; PAIR-DOUBLE, MOVES and T-BOUND outside 𝓛^R_d (in R109's 𝓛_d two
  movers of a level may W-point to different lower movers, l. 83-84); KP-MOVE at degree ≥ 3; whether T-BOUND is attained for d ≥ 2;
  any bound on P(z) (exponential in desc(z) on diamond-shaped Ξ-graphs, l. 151); G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee remarks and own checks):
  (i) REFEREE §3 (align_probe.py on its simulator t3r_sim.py, «set order, no ENC», logs align_logs/): the 184 𝓛^R corpus genomes from
      every start if at most 64 (4,246 runs) and 400 random 𝓛^R_d genomes (d 2-6, a third hill-climbed; 10,288 runs), every statement
      0 violations, KP-MOVE (a), (b) also on 264 other corpus genomes; controls fire («F(l) ≤ F(l − 1) + 1» fails 198 / 103 times,
      «rises ≤ P(z) − 2» fails 2,152 / 3,863 times; l. 84-85 «The bounds are not vacuous.»).
  (ii) REFEREE-2 (r2align.py on its r2sim.py, «R104 text, β-sets»): 600 random 𝓛^R_d genomes (d 1-6) and 103 corpus files, 28,039
       runs, 0 violations of every check, 262 PAIR-DOUBLE equalities (l. 55-63).
- Honest limits: (i) A STRUCTURE / EXPONENTIAL-BOUND statement inside the IDEAL model: on 𝓛^R_d the key side of every level is
  governed by the pair below (ALIGN, MOVES), each level at most doubles its pair's flips plus 2 (PAIR-DOUBLE), so T ≤ 2^(d+2) − 2d − 4
  (T-BOUND), strictly below RESULTS R108's 3^d − 1 for d ≥ 3 and equal to it at d = 1, 2; KP-MOVE and PATH-RISE hold on every acyclic
  genome. It bounds nothing polynomially (T-BOUND is exponential; PATH-RISE's P(z) can be exponential); G-N5-TIME stays open; not M3,
  not a step-4 pass, not a TARGET.md claim. (ii) ALIGN, F0, PAIR-DOUBLE, MOVES and T-BOUND are stated on 𝓛^R_d only, KP-MOVE at degree
  2 only; Ξ-cyclic genomes are not covered. (iii) PAIR-DOUBLE is tight at one level of one genome (dd_d5_F14, level 3); whether
  T-BOUND is attained for d ≥ 2 is not claimed, and the sharper F(l) ≤ F(l − 1) + 1 for γ_l(0) ≠ γ_l(1) is machine-checked only and
  not claimed. (iv) The DATA is per statement, as the line's DATA parenthesis says, with these exact sets and units (aligncheck.py,
  read by me): 184 in-tree 𝓛^R_d genome files of box150-box177 (156 distinct contents; well-formed, with a start, acyclic) from their
  stored starts and 300 random 𝓛^R_d genomes (d 2-5; every start for d ≤ 3, the genome start otherwise): 5,662 runs; ALIGN's (a) and
  (c) (the line's first and third ALIGN parts) on every (state, level ≥ 1) pair, (b) (the second part) on the 11,824 pairs with t ≥ 1;
  the F0 count tests F(0) ≤ 2 per run; the moves-bound count runs on every (run, mover) pair, 21,296 at level ≥ 1 and 11,324 at level 0
  (bound 1, F0's first half); the T-BOUND count tests the two bounds on T per run; F(l) ≤ 2^(l+2) − 2 has no lane count of its own; the
  44 equalities include dd_d5_F14's level 3 three times (three copies in the corpus). (v) Every statement is about R104's IDEAL model;
  nothing is said about a real N5 run or a parity game beyond what R104 already says. (vi) Premises: RESULTS R104's definition, R105's
  ENC and MONO, and R110's definition of 𝓛^R_d; R106-R109, R111 and R112 are not used. No lit note, no lane file, no outside source, no
  machine premise. No Lean. (vii) Every proof is in docs/new/P-IDEAL-ALIGN.md, which the line's source note names with the fixes file
  (which carries no proof). (viii) Names: «R113» here is this RESULTS entry; «ALIGN» is this lemma, not the ALIGN of R67; «F0» is this
  lemma, not R96's (F0); «T-BOUND» is this corollary, not the T-BOUND items of R7 and R9; «MOVES» is this corollary, not R111's
  PAIR-MOVES; «P(z)» counts maximal Ξ-paths, not R99's P(z); «AL-L1», «AL-L2», «AL-P1» (REFEREE) and «P-1», «P-2» (REFEREE-2) are this
  packet's referee labels, not R104's AL-items; dd_d5_F14 is the genome of R109's LIFT champion and of R111 (sha1 06f0e501…). (ix) The
  tightness instance is L-RED's genome (dd_d5_F14), used here only to show PAIR-DOUBLE tight; T is R104's number of steps.
- Data (DATA, not proof): experiments/new/box178/aligncheck.py (l-new cb8e0dca, sha1 9335dee71554491004b5f7567bb1a6784c5292dd, 93
  lines; deterministic, seed 178; simulator: experiments/new/box150/check.py's Gen), output frozen in experiments/new/box178/aligncheck.out
  (sha1 b653b01bbdca19c8e0c7d406b1bd2470c35c55fc, 4 lines) and wired into experiments/new/check.sh block «P-IDEAL-ALIGN» (l. 919-927 at
  c787aab1, with sha1 pins of the packet, L-1, aligncheck.py, aligncheck.out, dd_d5_F14, the fixes and L-2; unchanged at b38726b4).
  L-2's DATA parenthesis: «(DATA, experiments/new/box178/aligncheck.py on the 184 in-tree 𝓛^R_d genome files of experiments/new/box150
  to box177 from their stored starts and 300 random 𝓛^R_d genomes, 5,662 runs: ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥
  1) pairs and (b) on the 11,824 of them with t ≥ 1; F0 0 on 5,662 runs; PAIR-DOUBLE 0 on 10,648 (run, level ≥ 1) pairs, equality on
  44, among them L-RED's dd_d5_F14 at level 3 (F(3) = 14 = 2·6 + 2); MOVES 0 on 32,620 (run, mover) pairs for the moves bound and on
  the 21,296 with level ≥ 1 for KF_x = F(l − 1); T-BOUND 0 on 5,662 runs; PATH-RISE 0 on 32,620 (run, mover) pairs; KP-MOVE outside
  𝓛^R_d: no separate DATA)». What each count covers (aligncheck.py, read by me): KPEQ and ORD every (state, level ≥ 1) pair of every
  run (22,472); LAND the (s_t, level ≥ 1) pairs with t ≥ 1 (11,824), testing each mover of the pair that moved at step t; F0 F(0) ≤ 2
  per run (5,662); DBL F(l) ≤ 2F(l − 1) + 2 per (run, level ≥ 1) (10,648), «dbltight» its equalities (44); KFF KF_x = F(l − 1) per
  (run, mover of level ≥ 1) (21,296); MOV moves(x) ≤ 1 + F(l − 1) at level ≥ 1 and moves(x) ≤ 1 at level 0, per (run, mover) (32,620 =
  21,296 + 11,324); TB T ≤ 2d + 2 Σ_(l ≤ d−2) F(l) and T ≤ 2^(d+2) − 2d − 4 per run (5,662); PATH the rises of cv(z) against P(z) per
  (run, mover) (32,620). The block's outputs, reproduced by both referees at cb8e0dca (REFEREE §3 l. 86-87 «aligncheck.py regenerates
  aligncheck.out identically»; REFEREE-2 l. 65-66, «exit 0») and re-run for this draft (2026-11-06T11:07:03Z from a `git archive` of
  c787aab1's experiments/new and docs/new, rc 0, PASS line ending «fixes 25b050ee, line L-2 cb5f0398: PASS»; aligncheck.py's output
  byte-equal to aligncheck.out): «SCOPE corpus files 184 random 300»; «COUNTS runs 5662 steps 5602 statelevels 22472 runlevels 10648
  runmovers 32620 dbltight 44»; «KPEQ 0 LAND 0 ORD 0 DBL 0 F0 0 KFF 0 MOV 0 TB 0 PATH 0»; «TIGHT dd_d5_F14 LR True T 14 F [2, 3, 6,
  14, 7] F(3) = 2F(2) + 2 True».
  REFEREE (successor 24; own docs/referee/scratch/align_probe.py on its simulator t3r_sim.py, logs align_logs/corpus.txt and
  random.txt): l. 78-81 (14,534 runs, 0 violations of every check). REFEREE-2 (successor 28; own docs/referee-2/R2-P-IDEAL-ALIGN/r2align.py
  on r2sim.py, output r2align_seed178.out): l. 55-63 (28,039 runs, 0 violations). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-P-IDEAL-ALIGN.md: successor 24's report 6f0daf603ec39a1024ac31bd85db87aa58375fd3
  (2026-11-06T04:32:55Z, new file, 127 lines, sha1 ddecaab349361fa74c99bddb96ac51466b7694aa, with scratch/align_probe.py and
  align_logs/): every statement SIGN, L-1 NOT YET (AL-L1), optional AL-L2 and AL-P1 (l. 10-18, 67-71, 101-117); §C
  0e2c354f1340fc2f06fd946c1f0dc6df4ebc052b (2026-11-06T05:51:24Z, 153 lines, sha1 9e4df3674e2936086759280107792dbd0a3c6119; l. 1-127 =
  6f0daf60's, by cmp): F-a, F-b, F-c CORRECT, the byte test of L-2 (l. 146-149), «L-2 MATCHES.» (l. 151), «Fixes entry 1 is CORRECT.»
  (l. 152), «All seven statements stay SIGNED. Open items of mine: none.» (l. 153). REFEREE-2 docs/referee-2/R2-P-IDEAL-ALIGN.md:
  successor 28's report ea08029d31661ec9ea399e61055d33d5d42e6781 (2026-11-06T04:16:35Z, new file, 89 lines, sha1
  b6fcce64bf2cfdf2b2d735b652f4fb6ee29ec4b6, with R2-P-IDEAL-ALIGN/r2align.py and r2align_seed178.out): every statement SIGN, «No gap. No
  REFUSE.», L-1 MATCHES with optional P-1, P-2 (l. 10-20, 85-89); Addendum 1 ddca4cc7ee74887c22f533e94286313ba594484a
  (2026-11-06T05:51:29Z, 107 lines, sha1 4177f480861d27fe24ee78e643c5a7580c86dca9; l. 1-89 = ea08029d's, by cmp): «**Fixes entry 1:
  CORRECT.**» (l. 95), «**Line L-2: MATCHES.**» after its byte test (l. 105-106), «My seven SIGNs stand.» (l. 107). Lane: freeze and
  L-1 cb8e0dca169be4ee1f06508b7105334746cac4f2, fixes entry 1 and L-2 c787aab1e33ce464e59281df29d2f4037f5ffa38.
  INDEPENDENCE: REFEREE l. 2-3 «Independent: I did not open or list docs/referee-2/ on this packet before this report was pushed.»;
  REFEREE-2 l. 2-3 «Independent: docs/referee/ not read for this packet before this push.». REFEREE-2's report (04:16:35Z) precedes
  REFEREE's (04:32:55Z); neither cites the other's first report; each checked the statements with its own simulator written from R104's
  text and compared β-sets, not ENC integers. In the second round REFEREE knew REFEREE-2's items only through the fixes entry (§C l. 134
  «I know REFEREE-2's items (P-1, P-2) only through the entry.»). Differences, resolved: REFEREE required AL-L1 on L-1, REFEREE-2 matched
  L-1 and read ALIGN (b) inside the 22,472 (l. 81-82); REFEREE-2 accepted the finer ranges (Add. 1 l. 100-101); both raised the
  «improving» point (AL-L2 = P-2); REFEREE alone raised AL-P1, REFEREE-2 alone P-1. Both SIGN the same seven statements and both MATCH
  L-2 (each byte-tested it with its own script). No disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a cost model
  (packet §7 l. 175-177 «Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a
  complexity class.» «None is an M4 or M3 claim, none bounds anything polynomially (T-BOUND is exponential), none is a gauntlet step.
  G-N5-TIME stays OPEN.»; REFEREE §4 l. 90-91 «Every statement is inside R104's IDEAL model. The bounds are exponential. Not M3, not M4,
  not a gauntlet step. G-N5-TIME OPEN.»; REFEREE-2 l. 69 «IDEAL model only; exponential bounds; no game, no algorithm, no complexity
  class; not M3 / M4 / step 4; G-N5-TIME OPEN.»). The line (L-2) makes no M4 claim and no TARGET claim; its tail reads «a STRUCTURE /
  EXPONENTIAL-BOUND statement inside the IDEAL model on the key side of 2-wide ladders» and «G-N5-TIME stays OPEN; not M3, not a step-4
  pass, not a TARGET.md claim» (L-2, by script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R112's UPDATE of G-N5-TIME (GAPS at 1393ebbc: the last UPDATE on l. 11 is
R112's, «UPDATE 2026-11-06 10:37Z: RESULTS R112 (P-TR3; CHECKER C123 89764538) …», before the row's closing « |»), built by script
(upd113.py: upd112b.py's controls and procedures unchanged, R112's control added (16 controls, R97-R112, all landed, byte for byte,
True); sentinel_build111 of upd111.py unchanged, default drops, the «(DATA, » opening; no DEAD clause; no adaptation; cross-checked
against a direct build: True) only from the clauses of the title line L-2: the seven labels behind their clauses; « (2026-11-06) — » →
«: »; the DATA parenthesis before the source parenthesis opened as «; DATA, …»; «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass,
not a TARGET.md claim» dropped; the source parenthesis kept; «. G-N5-TIME stays open.» at the end. L-2 holds no "|"; the UPDATE holds
none (3,364 bytes, 75 «(» / 75 «)»; sha1 of the line without newline, placeholders unfilled:
d4f2d7c1d7cc4076f0a19d87cd7daaa8a91b5d86). <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit; C114 Add. 1 E-1),
<HH:MM> the landing time and <checker> the CHECKER C125 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R113 (P-IDEAL-ALIGN; CHECKER C125 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC and MONO only; and RESULTS R110's definition of 𝓛^R_d only), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, KP_s(x) the option of x with the least key under s, KF_x the number of steps t with KP_(s_t)(x) ≠ KP_(s_(t−1))(x), for two distinct movers u, w of one level a flip of (u, w) at step t a change between s_(t−1) and s_t of the order of the keys of their current options, on 𝓛^R_d F(l) the number of steps at which the pair (2l, 2l + 1) flips, for 1 ≤ l ≤ d − 1 c_l(s) the option index k for which mover 2(l − 1) + k has the smaller current key under s, γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k), cv_s(z) the integer value of z's current option (R105 ENC) and P(z) the number of maximal Ξ-paths from z (one option chosen at every mover on the way, ending at the exit X): on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j (ALIGN); at any degree elsewhere, a mover x of degree 2 that moves at step t moves to KP_(s_t)(x), so moves(x) ≤ 1 + KF_x (KP-MOVE); on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤ 2 (F0); on 𝓛^R_d, F(l) ≤ 2F(l − 1) + 2 for 1 ≤ l ≤ d − 1 (PAIR-DOUBLE); on 𝓛^R_d, KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1) for every mover x of level l ≥ 1 (MOVES); on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2 and T ≤ 2d + 2(F(0) + … + F(d − 2)) ≤ 2^(d+2) − 2d − 4 (T-BOUND); at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run (PATH-RISE): a STRUCTURE / EXPONENTIAL-BOUND statement inside the IDEAL model on the key side of 2-wide ladders, improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d (strictly for d ≥ 3; equal at d = 1, 2); bounds nothing polynomially; the bound F(l) ≤ F(l − 1) + 1 for γ_l(0) ≠ γ_l(1) (machine-checked only) and the conjectures PAIR-LIN and DBL-O(1) are not claimed; Ξ-cyclic genomes and genomes outside 𝓛^R_d (outside PATH-RISE and KP-MOVE) are not covered; DATA, experiments/new/box178/aligncheck.py on the 184 in-tree 𝓛^R_d genome files of experiments/new/box150 to box177 from their stored starts and 300 random 𝓛^R_d genomes, 5,662 runs: ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥ 1) pairs and (b) on the 11,824 of them with t ≥ 1; F0 0 on 5,662 runs; PAIR-DOUBLE 0 on 10,648 (run, level ≥ 1) pairs, equality on 44, among them L-RED's dd_d5_F14 at level 3 (F(3) = 14 = 2·6 + 2); MOVES 0 on 32,620 (run, mover) pairs for the moves bound and on the 21,296 with level ≥ 1 for KF_x = F(l − 1); T-BOUND 0 on 5,662 runs; PATH-RISE 0 on 32,620 (run, mover) pairs; KP-MOVE outside 𝓛^R_d: no separate DATA (P-IDEAL-ALIGN, docs/new/P-IDEAL-ALIGN.md with its fixes entry 1, docs/new/P-IDEAL-ALIGN-fixes.md; L-NEW successor 55). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-06T11:20:49Z by date -u). (1) FIRST FILL on line L-2 (l-new c787aab1,
sha1 cb5f0398…), to CHECKER C125. NOT pushed; my commits: the merge (--no-ff) 7302bc7c (l-new b38726b4) and one commit holding this file
(the Note E-3 draft is a separate commit). Push trunk before landing. (2) TITLE l. 347 = "### R113 [refereed-only] " + L-2 without its
newline + ", CHECKER PASS (docs/checker/C125.md, checker PENDING)", checked by script (chk113.py): equal, byte for byte (True); the only
«### R» heading of this file; 76 + 1 «(» and 76 + 1 «)», balanced; no «[lane», no packet name before the claims. (3) BODY l. 347-556
(python slice d[346:556]; 0 "|" in the range, by script); GAPS preamble l. 558-567 (two "|", both inside quotation marks: the row's
closing « |» and holds no "|"); UPDATE l. 568 (d[567]; one line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 3,364 bytes; sha1
d4f2d7c1d7cc4076f0a19d87cd7daaa8a91b5d86 of the unfilled line without newline; controls True ×16: R97's-R112's landed UPDATEs). No
Dead-ends row is drafted ((14)). A landing script in the shape of R112's slices d[346:556] for the entry and reads d[567] for the UPDATE
(with «R113», «R112» as PREV, «C125», and the GAPS l. 11 assertion on «RESULTS R112 (P-TR3» as the last UPDATE). (4) RE-RUNS: listed in
the header paragraph "Re-runs", (a)-(g). NOT RUN: the referees' tools (their committed logs read); scripts/verify.sh; the full check.sh.
(5) QUOTE SWEEP (chk113.py: the rule of chk111b.py and chk112b.py: outermost guillemet quotes, whitespace joined, split at the ellipsis,
parts of 6+ characters; sources: the packet, L-1, L-2, the fixes, aligncheck.py and aligncheck.out, check.sh and box150/check.py at
c787aab1, both referee files at 0e2c354f / ddca4cc7 with align_probe.py, align_logs, r2align.py and r2align_seed178.out,
R-P-IDEAL-KEYS.md at fadbb9a0, P-TR3.md at d3e3cde8 (for the R104 quote), RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, NOW, LEAD-STATE,
TARGET.md, CLAUDE.md, notes/CHECKER.md, C120-C124, R111-draft, R112-draft, R105-erratum-E2-draft at the local trunk, the commit subjects
of the cited commits, my re-run outputs): 377 outermost quotes, 301 parts of 6+ characters, every part found (0 not found); in the title
and body alone 105 quotes, 89 parts, 0 not found; GAPS preamble and UPDATE 11 quotes, 7 parts, 0 not found. Line-precise: 111 of 111
(source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines. Every sha1, line count and
commit time cited was re-measured in this session (sha1sum, wc -l, cmp, git log -1). STALE STATUS in title and body (by script): the
word pending 0 times apart from the title fill; NOT YET once (REFEREE's L-1 verdict, history); not landed once, inside the quoted F-b
label, followed by R112's landing; L-3 0 times; the phrase signed but not yet landed 0 times. (6) DISCREPANCIES: (11) D-1 to D-6. I
found no error in a signed statement. (7) FLAGS FOR THE LEAD AND CHECKER: G-0 (C125; C126 for Note E-3), G-9 (i)-(iii) (F0, MOVES,
T-BOUND: the counter differs from the named clause, C124 E-1 class; line not changed, per the brief), G-9 (iv) (ALIGN's packet labels in
the DATA), G-8 (a) (the scope tail's description); NOTE G-C. (8) NOT VERIFIED: the referees' tools were not re-run (their logs were
read); the Lead brief of BOX 178 and the 05:32Z relay beyond the lane commits; scripts/verify.sh and the full check.sh were not run. (9)
LANDING SIMULATION (sim113.py, on in-memory copies of RESULTS and GAPS at the local trunk, R112 as landed): RESULTS 12,730 -> 12,941
lines (wc -l), a pure insertion of 211 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly after R112's
landed block (R112 l. 11,909-12,150, blank l. 12,151, byte-unchanged: True; R110's and R111's blocks byte-unchanged: True): True; R113
at l. 12,152-12,361, blank l. 12,362, the next line (**Erratum E-1**) moves to l. 12,363, the Erratum E-2 line to l. 12,376, the Dead
ends heading to l. 12,404; order R110, R111, R112, R113, E-1, E-2, Dead ends: True; every other line byte-unchanged (common prefix and
suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced by " " + the filled
UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); UPDATE 2026- heads 47 -> 47 plus 1 UPDATE head with the simulation
year 2099, directly after R112's and now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the simulation: <DATE>
2099-01-03, <HH:MM> 00:00, <checker> 0000000. (10) THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the
forty hex digits after the next colon replaced by forty «0» characters is: 5d3ab9913c17e8e229a3b750ec2f8e5a45a41489. The file's actual sha1 and line count are in the
hand-back to the Lead (and re-measurable with sha1sum).
