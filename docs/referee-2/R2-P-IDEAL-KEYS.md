# R2-P-IDEAL-KEYS: second-referee report on packet P-IDEAL-KEYS (L-NEW successor 55, box 172)
REFEREE-2 successor 28 (Opus 5.5, D12/D20). Written 2026-11-05 23:49Z (date -u). Independent: docs/referee/ not read for this packet
before this push. Stale-clone check at start (23:43Z): ls-remote claude/referee-2 = local HEAD = 8fde383f; the clone was shallow
(rev-list said 0 / 8726, false); after fetch --deepen: 0 ahead / 93 behind trunk b5d154ad, fast-forwarded (0 / 0).

## Object
- claude/l-new b302bbf5. docs/new/P-IDEAL-KEYS.md sha1 62b35bf7ed7616bb66ff512edc30fe30431db0e5, 282 lines;
  docs/new/P-IDEAL-KEYS-line-L1.txt sha1 f36c6402064f61511048887bde28a72e270382ee, 1 line, 0 «|». Instances:
  box166/out/KILL_PM_compose_dd_d5_F14.json c025a4b61cd6…, box172/inst/dd_d5_F14.json 06f0e5015d09…, box170/out/T1_dd_top8.json
  9aead80e6123…. All re-hashed at b302bbf5: match.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma LOCAL-KP (a), (b) | **SIGN** (Opus 5.5, D12) |
| §3 | Lemma PAIR-KF (a), (b); Corollary PAIR-MOVES | **SIGN** (Opus 5.5, D12) |
| §4 | Lemma CASCADE (a), (b); Corollary F ≤ T; Corollary LADDER | **SIGN** (Opus 5.5, D12) (N-1 on a «Does NOT claim» remark) |
| §5 | Lemma RENEW (a), (b) | **SIGN** (Opus 5.5, D12) |
| §6 | Lemma MERGE (a), (b) | **SIGN** (Opus 5.5, D12) |
| §6 | Lemma RETURN; Corollary RETURN-COUNT | **SIGN** (Opus 5.5, D12) |
| §7 (a) | DEAD PM by KILL_PM_compose_dd_d5_F14 | **SIGN** (Opus 5.5, D12) (F-1: quote not verbatim) |
| §7 (b) | DEAD PMV by dd_d5_F14 | **SIGN** (Opus 5.5, D12) (F-1: quote not verbatim) |
| §7 (c) | DEAD doubling-tower step | **SIGN** (Opus 5.5, D12), in the scope stated in R-1 (F-2: «top mover» wording) |
| line | L-1 | **MATCHES** after the exact word changes W-1 to W-3 (W-1 and W-2 required, W-3 required for quote fidelity) |
No statement is REFUSED. No gap is listed: every proof is complete from the landed premises and the definition.

## Premise route (landed RESULTS only; docs/lit not used)
- R104: packet §0 restates R104's definition. Checked against RESULTS l. 9864 (verbatim text: «an IDEAL step moves every mover to the
  lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current option
  and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes»). The packet's
  recursive key «key_s(wt(x, k), s(wt(x, k))) followed by g(x, k)» is exactly that tuple (level 0 first, g(x, k) last); A-sets under the
  old state, keys under the new state, level by level, both stop rules. (F1) and (F2) are immediate. No R104 theorem used. ✓
- R105 quotes: every «…» the packet attributes to RESULTS was tested as a substring of docs/RESULTS.md at trunk b5d154ad (line-wrap
  whitespace normalised): ENC, MONO, XI-NEW (title, and the shorter quote in §5), RISE (title), body item (e) (a), (b), (c) (RESULTS
  l. 10224-10226, «Corollary RISE (§3, l. 106-115)»), KEYFLIP, «KP_s(x) the key-preferred option under the keys of s», «number of steps
  at which KP(x) changes»: all FOUND. ✓ ENC / MONO / XI-NEW / RISE are stated in R105 «at any degree»; KEYFLIP «at degree ≤ 2 only»,
  and the packet uses KEYFLIP only where every mover has degree ≤ 2 (PAIR-MOVES hypothesis; 𝓛^R_d is all degree 2). ✓
- KEYFLIP's KF_x: the packet reads «number of steps at which KP(x) changes» as #{t : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}. RESULTS body item
  (h) (l. 10236) binds KF_x as «the number of steps at which KP(x), the option of x with the smaller key, changes»; same reading. ✓
- Erratum E-2 (RESULTS l. 11611-…): the (E2c) quote is verbatim; its correction «Read KEYFLIP's moves(x) as the number of steps that move
  x» is exactly the packet's moves(x) (§0) and the line's «moves(x) the number of steps t with x ∈ Mv_t». (E2a) concerns CHAIN-BACK /
  U, (E2b) TOP-MONO's RANK_t: neither item is used (I read every proof step: no U, no RANK, no π-order argument). E-2 applied correctly. ✓
- R110: only the definition of 𝓛^R_d, quoted verbatim (FOUND), used only in Corollary LADDER (and in naming the PMV instance's class). ✓
- No R105 LOCAL, CHAIN-BACK, U-EQ, DECREMENT, EXACT-ENERGY, TOP-MONO, RANK-BOUND, INTERVAL-*, RECURSION used: confirmed by reading.
  No machine premise in any signed proof. ✓

## Proof check
### LOCAL-KP
- (a) Induction on lev(x): the key of (x, k) reads s only at y = wt(x, k) ∈ W(x) and, recursively, inside W(y) ⊆ W(x). ✓ (b) A step
  with Mv_t ∩ W(x) = ∅ keeps s on W(x), so KP is unchanged; hence KF_x ≤ WE_x. ✓

### PAIR-KF, PAIR-MOVES
- (a) equal prefixes, the distinct own gates decide, independent of s. ✓ (b) the prefixes are the keys of two options of distinct movers
  of level lev(x) − 1, hence distinct (F1), so the lexicographic order is decided inside the prefix: KP_s(x) = 0 ⇔ ord_s(a, b); the
  change counts coincide. ✓
- PAIR-MOVES: KEYFLIP (degree ≤ 2 genome) + (a)/(b); degree 1 ⇒ A-set singleton ⇒ 0 moves; level 0 ⇒ keys constant ⇒ KF = 0;
  T ≤ Σ moves since Mv_t ≠ ∅. ✓

### CASCADE, F ≤ T, LADDER
- If p, q ∉ Mv_t the options of p and q are the same in s_(t−1) and s_t, hence so are w_p, w_q. Level 0: constant keys. w_p = w_q:
  equal prefixes, constant gates decide. w_p ≠ w_q: ord(p, q) = ord(w_p, w_q) in both states. So not-(own) ⇒ (below); exclusive by
  definition. ✓ F ≤ T: one flip per pair per step. ✓
- LADDER: own flip steps ≤ moves(2l) + moves(2l + 1) (each moves one of them); below flip steps are distinct steps at which the pair
  {2l − 2, 2l − 1} flips (the only two movers of level l − 1, and ord is antisymmetric, so the flip does not depend on the order of the
  pair); level-0 movers move at most once (PAIR-MOVES); moves(x) ≤ 1 + F(lev(x) − 1) because wt(x, k) = 2(lev(x) − 1) + k are distinct.
  F(l) + 1 ≤ 3(F(l − 1) + 1), F(0) + 1 ≤ 3. ✓
- N-1 (note, no fix required): «tight at level 3 of one instance, §7 (c)» is true of the SECOND inequality (moves(6) = moves(7) = 7 =
  1 + F(2)); the first inequality is not tight there (F(3) = 14 < moves(6) + moves(7) + F(2) = 20). My numbers: r2sim_dead.out.

### RENEW
- a − 1 is a step (a ≥ 2) and not top-only by maximality, so LOWER. ✓ Every mover of a top-only step has level τ, so each is a
  least-level mover; XI-NEW gives (i), RISE body (e) (a), (b), (c) give (ii), (iii) (Z_t nonempty, Z_t ⊆ strict Ξ-descendants = D(h)). ✓
  The extension to every top-only t ≥ 2 uses the same two premises. ✓
- (b) steps a, …, b move only level-τ movers; W(h) has levels < τ; LOCAL-KP (a) on s_(a−1), …, s_b. ✓ (Holds also for a = 1, with s_0.)

### MERGE
- ENC unrolled along a chain gives v_r(x, a) = ε(x, a) + Σ_(i′<i) ε(y_i′, r(y_i′)) + cv_r(y_i). (a) at the merge mover m both cv_s(m)
  cancel (cv(X) = 0 if no merge). I checked that «first y_i equal to some z_j» is well defined and that the two chains coincide after m
  (deterministic successor, acyclic), so Pre_b contains no mover of the a-chain after m. ✓ (b) under s′ = s on Pre_a ∪ Pre_b the two
  chains reach m through the same movers with the same options; the prefix sums are those of (a). ✓ The order is the sign (ENC). ✓

### RETURN, RETURN-COUNT
- (F2) at t_1 and t_2 (degree 2) gives v(x, o) > v(x, o′) at s_(t_1−1) and the reverse at s_(t_2−1); v(x, o) = ε(x, o) + cv(xt(x, o))
  is non-decreasing (MONO, through ENC's integer order); so v(x, o′) rose strictly; v(x, o′) = ε(x, o′) is constant if z = X. ✓
- RETURN-COUNT: rises located in the disjoint windows [t_(i−1), t_i − 1] (telescoping over the states s_(t_(i−1)−1), …, s_(t_i−1));
  (u_i, k_i) injective; equal Ξ-targets of the two options are counted twice in R(x, 0) + R(x, 1), which only weakens the bound. ✓

### DEAD items: recomputed with my OWN simulator (docs/referee-2/R2-P-IDEAL-KEYS/r2sim.py, written from R104's text: Ξ-values compared
as β-SETS by the largest-rank β of the symmetric difference, not through ENC integers; no lane code imported). Output r2sim_dead.out.
- (a) PM, KILL_PM_compose_dd_d5_F14 (well-formed: W-targets one level down, gates and ranks distinct, Ξ acyclic, all degree 2): N 15,
  T 14, my run is state for state the packet's run; mover 12: D = {10, 11, 13, 14}, moves 6 at steps 1, 2, 5, 8, 9, 10 > (2 − 1)(1 + 4)
  = 5. ✓ Levels 1 and 4 have 5 and 4 movers (not in 𝓛^R_d or 𝓛_d). ✓
- (b) PMV, dd_d5_F14 (𝓛^R_5 by its fields): T 14, run identical; mover 6: D = {1, 2, 3, 5, 7, 8, 9}, cv rises (by β-set comparison) at
  steps 2, 3, 4, 6, 7, 8, 10, 11, 12, 14: VR 10 > 8. moves(6) = 7. ✓
- (c) tower: F(0..4) = 2, 3, 6, 14, 7, T = 14; moves(6) = moves(7) = 7 = 1 + F(2); F(3) = 14 = 2(1 + 6) = T; 2(1 + F(3)) = 30 > 14. ✓
  KILL_PM composition: T 14, largest pair flip count 14 ((6, 7)); T1_dd_top8: N 18, T 14, largest 14 ((6, 7)); mover 10 (desc 6,
  D = {12, …, 17}) moves 8 times. ✓
- R-1 (scope of (c), recorded reading of what I sign): box 169 §0 predicted «F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l)» (verbatim, l.
  38), i.e. a family whose T grows; it did not say «over a fixed clock» (that phrase is the packet's, outside the guillemets, and is
  box 170 §0's reading). What I sign as DEAD is: the step cannot be iterated within one run beyond T (F ≤ T), so over a fixed clock
  (T unchanged, as in both verified compositions) it stops once F reaches T (here at level 4), and the tower is not a reduction: an
  exponential flip count is an exponential T. NOT signed as dead: a tower whose gadgets add steps; the packet's «Does NOT claim» says
  exactly this («that no IDEAL-ACYC family has exponential T», «that a gadget can never add steps»), so no gap.
- F-1 (text, packet §7 (a), (b); fixes entry): the guillemet quotes are not verbatim of their sources. §7 (a) «for every IDEAL-ACYC
  genome and every start, moves(x) ≤ (deg(x) − 1)(1 + desc(x)) for every mover x»: box 165 l. 18-19 reads «… moves(x) ≤ (deg(x) − 1) ·
  (1 + desc(x)) for every mover x.» (with «·»). §7 (b) «VR(z) ≤ 1 + desc(z) for every mover z»: box 166 l. 41 reads «VR(z) ≤ 1 +
  desc(z)» only. Meaning unchanged; quotes must be byte-verbatim.
- F-2 (text, packet §7 (c)): «top mover with 8 moves» for T1_dd_top8 means the gadget's top, mover 10 (level 4); under the packet's own
  §0 notation the top level of T1_dd_top8 is τ = 5 (mover 14). Suggest «gadget top mover 10 (level 4) with 8 moves».

## Independent checks (DATA, not a signature) — docs/referee-2/R2-P-IDEAL-KEYS/r2lemmas.py on r2sim.py
- Random IDEAL-ACYC genomes (seed 28, 4,000 genomes: 1 in 4 a random 2-wide ladder of 𝓛^R_d, d 2-6; the others levels 1-5 with 1-3
  movers per level, half all-degree-≤-2, half degree 1-3; every start if ≤ 32, else 32 random): 88,082 runs, 82,990 steps.
  0 violations of: LOCAL-KP (a) (80,000 random state pairs), (b) (694,710 run-mover pairs); PAIR-KF (335,842 runs × degree-2 level ≥ 1
  movers); PAIR-MOVES (385,633, degree-≤-2 genomes only); CASCADE (89,258 flips, 15,129 of them (below)); F ≤ T (433,534 pairs);
  LADDER both inequalities and F(l) ≤ 3^(l+1) − 1 (28,864 ladder runs); RENEW (a) (1,858 first-step pairs, 167 later top-only steps),
  (b) (12,501 intervals); MERGE (b) (62,744); RETURN (146); RETURN-COUNT (450,412). Controls fire: LOCAL-KP with a W(x) mover changed
  38,919, MERGE with a pre-merge mover changed 27,046, RENEW (i) with s_(t−1) in place of s_(t−2) 2,025 / 2,025 (as (F2) forces).
  Output r2lemmas_seed28_4000.out (13.6 s).
- The lane's in-tree genomes in my own loader's format (CORPUS=<l-new b302bbf5>/experiments/new, box150-box172, N ≤ 30, stored start):
  119 files (the lane's 413 include formats my loader skips), 890 steps, 95 of them 𝓛^R ladders: 0 violations of every check above
  (RETURN 618 pairs). Output r2lemmas_corpus.out.
- The packet's own check: the check.sh block «P-IDEAL-KEYS» (l. 911-919) run standalone at b302bbf5: exit 0, «P-IDEAL-KEYS: keycheck 0
  violations (controls fire, output = frozen keycheck.out), DEAD instances PM / PMV / tower replayed (XSIM 0); pins packet 62b35bf7, line
  L-1 f36c6402, tool 6ce4693d, output 5100eb30, instances c025a4b6 / 06f0e501 / 9aead80e: PASS» (1.8 s). keycheck.py re-run separately:
  output byte-identical to keycheck.out.

## TARGET.md diff
No statement mentions a parity game, winning regions, an algorithm, a running time on games or a complexity class; all are about the
step sequence of R104's IDEAL model on acyclic Ξ-graphs. No M3 / M4 / M4-R claim, no gauntlet step; the only bound (LADDER) is
exponential. G-N5-TIME stays OPEN. ✓

## Line L-1 (clause by clause)
- Definitions diffed against packet §0: Mv_t, T, KP_s(x), KF_x, W(x), WE_x, flip / flips(p, q), v_s, cv_s, moves(x) (E2c binder), τ,
  top-only, top-only interval, F(l), desc(x), R(x, k): each equal to the packet's. 𝓛^R_d by R110's definition. ✓
- Claims: LOCAL-KP, PAIR-KF (the line drops (a)'s smaller-gate clause: weaker, fine), PAIR-MOVES, CASCADE (+ flips ≤ T), LADDER,
  RENEW (the line states the first step of the interval only, and «some strict Ξ-descendant … moving at step a − 1», a consequence of
  (iii)), MERGE (as (b)), RETURN + RETURN-COUNT, the three DEAD items: each matches or is weaker than the signed statement. The line's
  tower clause («cannot hold beyond T in one run, by flips ≤ T», attained at level 3, blocked at level 4) is exactly R-1's scope. ✓
- Hedges: PAIR-LIN, PM′_S, RENEW-COUNT not claimed; Ξ-cyclic and degree ≥ 3 exclusions; G-N5-TIME OPEN; not M3 / step 4 / TARGET. ✓
- Parentheses balanced (depth never negative, 0 at end); 3 «, 3 »; 0 «|»; one line. ✓
- Source note «(P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md; L-NEW successors 54-55)»: the packet states that no other file carries a proof,
  and no fixes file exists at b302bbf5. ✓
- DATA: every count names its statement. ✓ Two index ranges are wider in the line than in the packet:
- Exact word changes:
  - W-1 (required; binder): RENEW's «w ∉ A_(s_(a−2))(h)» uses A_s(h), which the line never defines. After «and RISE» in the premise
    parenthesis, or at first use, add: «(A_s(h): h's current option under s and its options strictly better under s)» (R105's own
    wording, verbatim).
  - W-2 (required; DATA index ranges): «PAIR-KF 0 on 34,113 (run, mover) pairs» → «PAIR-KF 0 on 34,113 (run, degree-2 mover of level
    ≥ 1) pairs»; «RETURN-COUNT 0 on 50,260 (run, mover) pairs» → «RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs» (packet §8).
  - W-3 (required for quote fidelity): guillemets enclose paraphrases. PM: «moves(x) ≤ (deg(x) − 1)(1 + desc(x)) for every mover x» →
    «moves(x) ≤ (deg(x) − 1)(1 + desc(x))» for every mover x (box 165 title, verbatim). PMV: («the number of steps at which cv(z) rises
    is at most 1 + desc(z) for every mover z») → («VR(z) ≤ 1 + desc(z)» for every mover z, VR(z) the number of steps at which cv(z)
    rises). Tower: («F(l) = 2(1 + F(l − 1)) level after level, so F(l) = 2^(l+1) − 2») → (the step «F(l) = 2(1 + F(l − 1))» iterated
    level after level, so F(l) = 2^(l+1) − 2) (box 169 l. 26, verbatim).
- Verdict: L-1 MATCHES the signed statements once W-1 to W-3 are applied; no claim word changes.

## Files
- r2sim.py (own simulator), r2sim_dead.out; r2lemmas.py, r2lemmas_seed28_4000.out, r2lemmas_corpus.out (all in
  docs/referee-2/R2-P-IDEAL-KEYS/). Re-run from repo root: `python3 -I docs/referee-2/R2-P-IDEAL-KEYS/r2lemmas.py 28 4000`;
  `python3 -I docs/referee-2/R2-P-IDEAL-KEYS/r2sim.py <genome.json>`.

## Addendum 1: fixes entry 1 and line L-2 (REFEREE-2 successor 28, Opus 5.5, D12/D20; 2026-11-06 01:26Z by date -u)
- Object: claude/l-new 1a178aff. docs/new/P-IDEAL-KEYS-fixes.md sha1 26088848b6a80621fb46a4887be0b2b8ad2a8ebc, 100 lines;
  docs/new/P-IDEAL-KEYS-line-L2.txt sha1 fb1b22763f5cc5e64fa2cab78468718b1321a846, 5,542 B, 1 line. Re-hashed: match. The packet
  (62b35bf7), line L-1 (f36c6402), keycheck.py (6ce4693d) and keycheck.out (5100eb30) are unchanged at 1a178aff.
- Independence: written after reading the fixes entry, which names the other referee's items (KY-*); docs/referee/ itself not read.
- **Fixes entry 1: CORRECT.**
  - F-a TOWER: **SIGN** (Opus 5.5, D12). Statement: a run with a pair flipping 2^(l+1) − 2 times has T ≥ 2^(l+1) − 2; proof is
    Corollary F ≤ T, which I signed. The iteration of «F(l) = 2(1 + F(l − 1))» from F(0) = 2 gives 2, 6, 14, … = 2^(l+1) − 2. ✓ Both
    quotes are verbatim in docs/new/N5-PAIRLIN-box169.md (l. 38, l. 26). The READING (not a shortcut) is labelled not to sign, and the
    DATA numbers are those I recomputed (r2sim_dead.out). Dropping DEAD is right: as my R-1 said, box 169 predicted T ≥ F(l), so F ≤ T
    refutes no statement of record. This supersedes my §7 (c) DEAD SIGN, which I withdraw in favour of TOWER.
  - F-b (KY-1): my miss. The packet's «it is 7 = 1 + desc(6)» is false arithmetic (desc(6) = 7, so 1 + desc(6) = 8); my own output
    (r2sim_dead.out: D of mover 6 has 7 elements, moves 7) shows it, and I did not flag it. The fix «7 = desc(6) ≤ 1 + desc(6) = 8» is correct. ✓
  - F-c: box 165's title has «moves(x) ≤ (deg(x) − 1)(1 + desc(x))» verbatim; box 166 l. 41 (in its §1) has «VR(z) ≤ 1 + desc(z)»
    verbatim. ✓ F-d: mover 10 is level 4 with 8 moves, τ = 5 (mover 14), as I measured. ✓ F-e: the N-1 numbers (7 = 1 + F(2); 14 < 20). ✓
  - F-f (MERGE letters k, k′ in the line): a renaming only. ✓
  - W-2 counts: keycheck.py l. 147-149 counts pairkf_movers only for degree 2, level ≥ 1, and l. 177-187 counts retcnt_movers only for
    degree 2 (continue otherwise). So the narrowed ranges are the tool's real ranges. ✓
- **Line L-2: MATCHES.** Byte test (Python): R1-R10 parsed from the fixes entry; each old string occurs exactly once; applying them in
  order to L-1 gives a string byte-identical to L-2 (5,542 B). Parentheses 120 / 120, depth never negative; 3 «, 3 »; 0 «|»; one line.
  The TOWER clause (R3) is no stronger than F-a, read over 𝓛^R_d's F(l) or over any pair. The source note (R10) names the packet and the
  fixes file, the only two files that carry proofs. W-1, W-2 and W-3 are applied as I worded them.
- P-1 (optional, DATA wording, present in L-1 too; my miss in the first report): «RENEW 0 … and, for the constant keys, on 2,704
  intervals». keycheck.py l. 174 checks that KP is constant on [a − 1, b], not that every key is. That is the weaker half of RENEW (b).
  The full key form is covered by my own check (r2lemmas.py RENEWB, keys of every option: 0 on 12,501 intervals). Optional rewording:
  «for the constant key preference».
- The check.sh block «P-IDEAL-KEYS» at 1a178aff, run standalone: exit 0, «… fixes 26088848, line L-2 fb1b2276: PASS».
