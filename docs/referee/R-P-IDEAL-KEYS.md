# R-P-IDEAL-KEYS: REFEREE report on P-IDEAL-KEYS (L-NEW successor 55, box 172)
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: I did not open or list docs/referee-2/ on this
packet before this report was pushed.
- Stale-clone check: ls-remote origin claude/referee = HEAD = 5c02d44d before this work; ff-only had nothing to merge.
- Object: claude/l-new b302bbf5 (an ancestor of origin/claude/l-new). Re-measured:
  - docs/new/P-IDEAL-KEYS.md sha1 62b35bf7ed7616bb66ff512edc30fe30431db0e5, 282 lines;
  - docs/new/P-IDEAL-KEYS-line-L1.txt sha1 f36c6402064f61511048887bde28a72e270382ee, 1 line, 5,187 bytes;
  - instances: KILL_PM_compose_dd_d5_F14.json c025a4b6…, box172/inst/dd_d5_F14.json 06f0e501…, box170/out/T1_dd_top8.json 9aead80e…
- Trunk for premises: claude/vibrant-johnson-nxvvxo b5d154ad (= the packet's cited trunk).

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | LOCAL-KP (a), (b) | SIGN |
| §3 | PAIR-KF (a), (b) | SIGN |
| §3 | Corollary PAIR-MOVES | SIGN (KEYFLIP read with the E-2 (E2c) binder, correctly) |
| §4 | CASCADE (a), (b); Corollary F ≤ T; Corollary LADDER | SIGN |
| §5 | RENEW (a) (incl. the extension to every top-only t ≥ 2), (b) | SIGN |
| §6 | MERGE (a), (b) | SIGN |
| §6 | RETURN; Corollary RETURN-COUNT | SIGN |
| §7 (a) | DEAD PM (instance c025a4b6) | SIGN |
| §7 (b) | DEAD PMV (instance 06f0e501) | SIGN WITH GAP KY-1 (a false sentence in its «Does NOT claim»; text fix) |
| §7 (c) | DEAD «the doubling-tower step» | REFUSE as DEAD (KY-G1). The implication «a tower reaching F(l) in one run has T ≥ F(l) in that run» is Corollary F ≤ T and is signed; the instance values are re-measured (§3) |
| §8 | DATA, checks, exclusions, TARGET diff | not to sign; check.sh block PASS; TARGET diff agreed |
| line | L-1 | NOT YET: REQUIRED KY-L1 (tower clause under DEAD); optional KY-L2-L4 |

## 1. Premise route
- Every quoted premise was byte-tested against landed RESULTS (trunk b5d154ad; packet text with wrapped lines joined by single spaces,
  grep -F on RESULTS likewise joined). Each is FOUND exactly once:
  - R105 title line: ENC, MONO, XI-NEW, RISE, KEYFLIP, «KP_s(x) the key-preferred option under the keys of s».
  - R105 body item (e) (RESULTS l. 10225-10227), the signed form of RISE: «(a) …», «(b) …», «(c) …». The landed entry carries this
    signed form, so RENEW cites a landed text (not only the packet P-IDEAL-RED).
  - Erratum E-2 (E2c) (RESULTS l. 11617-11618).
  - R110's definition of 𝓛^R_d («the 2-wide degree-2 ladders in L-RED's R197 convention (…)»), RESULTS l. 11323.
- E-2 check (asked by the Lead). (E2c) is applied correctly:
  - moves(x) := #{t : x ∈ Mv_t}, as E-2's correction («Read KEYFLIP's moves(x) as the number of steps that move x»).
  - KF_x := #{t : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)} equals the signed definition in P-IDEAL-RED §5 l. 131-132 (claude/l-new 0ebddcf5,
    which I opened). The packet's KP_s for any degree (least key) agrees with it at degree 2. KEYFLIP is used only for genomes of
    degree ≤ 2 (PAIR-MOVES, LADDER).
  - (E2a) and (E2b) concern CHAIN-BACK and TOP-MONO, which are not used: correct, they do not bear.
- Not used: R105 LOCAL (LOCAL-KP is proved from the definition); no docs/lit, no lane file, no machine premise.

## 2. Proof checks
- LOCAL-KP: SIGN.
  - (a) by induction on lev(x): wt(x, k) ∈ W(x) and W(wt) ⊆ W(x). Correct.
  - (b): a step with Mv_t ∩ W(x) = ∅ leaves W(x) fixed, so (a) applies to s_(t−1), s_t.
- PAIR-KF: SIGN.
  - Equal-length prefixes (F1). (a): equal prefixes, the gates decide. (b): distinct options of level lev(x) − 1 give distinct
    prefixes, which decide.
- PAIR-MOVES: SIGN.
  - The case split is exhaustive: degree 1 (moves 0); level 0 (KP constant); equal W-targets (KF 0); first kind (KF = flips).
  - T ≤ Σ moves because Mv_t ≠ ∅.
  - The hypothesis «every mover of degree ≤ 2» is exactly what KEYFLIP needs.
- CASCADE: SIGN.
  - If neither p nor q moves, their options and W-targets are the same in s_(t−1) and s_t.
  - With w_p = w_q the constant gates decide, so there is no flip. With w_p ≠ w_q, ord(p, q) = ord(w_p, w_q) under both states.
  - (own) and (below) are exclusive by definition.
- F ≤ T: SIGN. A flip is defined per step.
- LADDER: SIGN.
  - Below steps of level l are flip steps of the pair {2l − 2, 2l − 1}: the current W-targets of 2l, 2l + 1 are distinct movers of
    level l − 1, and there are only two. Orientation does not matter for flips.
  - moves(x) ≤ 1 + F(l − 1) by PAIR-MOVES (the wiring makes wt(x, 0) ≠ wt(x, 1)).
  - F(l) + 1 ≤ 3 (F(l − 1) + 1) with F(0) + 1 ≤ 3 gives 3^(l+1) − 1. Correct.
- RENEW: SIGN.
  - Maximality makes step a − 1 lower.
  - Every mover of a top-only step has the largest level, so each is «a least-level mover of step t». That is exactly XI-NEW's
    and body item (d)'s hypothesis («ANY mover of least level in Mv_t, and w := s_t(h)»), with the same w.
  - (i)-(iii) are XI-NEW and RISE (e) (a)-(c) verbatim. D(h) ⊇ the strict Ξ-descendants on a chain.
  - (b): steps in [a, b] move only level-τ movers, and W(h) lies below τ; LOCAL-KP (a) then gives equal keys.
  - The packet correctly says (iii) does not place z below the top.
- MERGE: SIGN.
  - ENC unrolled along a chain is correct (induction, cv(X) = 0).
  - The merge point is well defined, and after it the two chains coincide. Under s′ = s on Pre_a ∪ Pre_b, both chains reach m through
    the same movers.
  - The sets differ (β(x, a) is only in the first), so the difference is nonzero and its sign is the Ξ-order.
- RETURN: SIGN.
  - (F2) at t_1 and t_2 (degree 2, x stays at o in between). MONO through ENC makes v(x, o) non-decreasing.
  - The strict chain v(x, o′) at t_2 − 1 > v(x, o) at t_2 − 1 ≥ v(x, o) at t_1 − 1 > v(x, o′) at t_1 − 1. z = X would make v(x, o′)
    constant.
- RETURN-COUNT: SIGN.
  - Telescoping gives one rise step u_i ∈ [t_(i−1), t_i − 1] for z_i = xt(x, s_(t_i)(x)). The intervals are disjoint, so
    i ↦ (u_i, k_i) is injective.
- DEAD PM: SIGN. The instance is recomputed in §3: mover 12, desc 4, 6 moves > 5.
  - Optional KY-P1: the «…» text of PM in §7 (a) is a restatement with the quantifiers made explicit. box 165's text is
    «moves(x) ≤ (deg(x) − 1)(1 + desc(x))»; say «restated from».
- DEAD PMV: SIGN WITH GAP KY-1. The instance is recomputed in §3: mover 6, desc 7, VR 10 > 8.
  - KY-1 (REQUIRED text fix): §7 (b)'s «Does NOT claim» says «anything about moves(6) (it is 7 = 1 + desc(6))». That is false:
    1 + desc(6) = 8, and moves(6) = 7 = desc(6). Fix in a fixes entry, e.g. «(it is 7 ≤ 1 + desc(6) = 8)».
  - The source of PMV is box 166 (H-values) «VR(z) ≤ 1 + desc(z)»; the packet's «for every mover z» makes the quantifier explicit
    (as for KY-P1).
- §7 (c), «the doubling-tower step»: REFUSE as DEAD. Gap KY-G1.
  - What box 169 states. N5-PAIRLIN-box169 §0 (l-new b302bbf5, docs/new/N5-PAIRLIN-box169.md): «KILL CANDIDATE … (READING; NOT
    constructed): the doubling tower. … Predicted: F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l): exponential IDEAL-ACYC runs.»
  - The prediction INCLUDES T ≥ F(l). Corollary F ≤ T is consistent with it and refutes nothing in it.
  - The qualifier «over a fixed clock» under which the packet kills the step occurs neither in box 169 nor in box 170 (grep: 0
    hits). It is the packet's reading, not the lane statement.
  - The instance shows the step attained at level 3 and failing at level 4 on ONE run (dd_d5_F14 and two compositions with T 14). It
    does not show that no tower genome realizes the step at every level with growing T.
  - So no statement of record is refuted. Under L43 a DEAD needs a refuted statement (by instance or proof); here there is none.
  - What IS proved, and I sign it: «a run in which the tower reaches F(l) = 2^(l+1) − 2 at level l has T ≥ 2^(l+1) − 2» (Corollary
    F ≤ T). So the tower gives exponential T only if it is itself an exponential-T construction; it is not a shortcut around
    G-N5-TIME.
  - Recommendation: relabel §7 (c) as a READING / «NOT A SHORTCUT (by Corollary F ≤ T)», keeping the measured instance values as DATA.
  - Optional KY-P2: §7 (c) calls mover 10 of T1_dd_top8 the «top mover with 8 moves». Mover 10 has level 4; the genome's top level is
    5 (mover 14, 2 moves). Say «the level-4 reader».

## 3. Independent checks (docs/referee/scratch/; my simulator t3r_sim.py from R104's text; no lane code; logs keys_logs/)
- keys_probe.py on the three instances (dead_recompute.txt). Every value of §7 is EQUAL:
  - KILL_PM_compose_dd_d5_F14:
    - well-formed (W one level down, distinct gates and ranks, acyclic); N 15, T 14; the 15 states equal §7 (a)'s list;
    - mover 12: D = {10, 11, 13, 14}, moves at steps 1, 2, 5, 8, 9, 10 (6 > 5); the only PM violator;
    - the §7 (a) option-field listing equals the JSON (15 movers, 0 differences, parsed from the packet text).
  - dd_d5_F14:
    - in 𝓛^R_5 (R110's wiring); its genome equals movers 0-9 of the PM file; T 14; states equal §7 (b);
    - mover 6: D = {1, 2, 3, 5, 7, 8, 9}; cv(6) rises (by the R104 SET order, no ENC) at 2, 3, 4, 6, 7, 8, 10, 11, 12, 14: VR 10 > 8;
    - moves(6) = 7 (KY-1);
    - pair flips F(0..4) = 2, 3, 6, 14, 7; KF(6) = KF(7) = 6; moves(6) = moves(7) = 7.
  - T1_dd_top8: well-formed, N 18, T 14, largest pair flip count 14 = T; mover 10 (level 4) has 8 moves (KY-P2).
- keys_check.py: my own checks of LOCAL-KP (b), PAIR-KF, CASCADE, F ≤ T, PAIR-MOVES, RENEW (a) (i)-(iii) and «step a − 1 lower»,
  RENEW (b), RETURN, RETURN-COUNT and MERGE (b). MERGE is checked by the Ξ-order sign under a random s′ = s on Pre_a ∪ Pre_b; RETURN
  and RETURN-COUNT by the set order, no ENC.
  | run set | runs | checks (LOCALKP / PAIRKF / CASCADE flips / RENEWA / RETURN / RETCNT / MERGEB) | violations |
  | --- | --- | --- | --- |
  | 434 L-NEW in-tree genomes (box150-179 JSONs at b302bbf5, N ≤ 30), every start if ≤ 64 else stored + 15 random | 10,350 | 66,560 / 38,782 / 16,548 / 1,791 / 2,043 / 59,118 / 2,085 | 0 |
  | 1,500 random genomes, degree 1-3, 2-5 levels, 1-3 movers per level | 4,500 | 31,929 / 11,562 / 3,789 / 86 / 1 / 16,131 / 5,661 | 0 |
  | 1,500 random genomes, degree ≤ 2 | 4,500 | 31,527 / 16,944 / 3,329 / 73 / 1 / 23,763 / 5,680 | 0 |
  - Controls fire on the corpus: RETURN with z the Ξ-target of the option x moved TO, 1,576 fires; CASCADE looking for the below flip
    at t − 1, 1,825 fires.
  - The random sets are weak (short runs); the corpus carries the coverage.
- check.sh block «P-IDEAL-KEYS» at b302bbf5 (detached worktree): «… PASS», 1.9 s. keycheck.py regenerates keycheck.out identically
  (8 lines; «LOCALKP 0 LOCALCTL 48435 … KEYFLIP 0»). The three box150 checker lines read «TOTAL genomes 1 runs 1 steps 14 XSIM 0 …
  VIOL 0». All seven pins are equal.

## 4. Diff against TARGET.md
- Every statement is about the step sequence of R104's IDEAL model. None mentions a parity game, a winning region, a running time
  or a complexity class. Not M3, not M4, not a gauntlet step. LADDER's bound is exponential. G-N5-TIME OPEN. Agreed with §8.

## 5. Line L-1
- Shape: one line, 111 «(» / 111 «)», depth never negative, 0 «|», one « — », «2026» once.
- Definitions diffed against §0:
  - MATCH: KP_s, KF_x, W(x), WE_x, flip / flips, v_s / cv_s, moves(x) (E2c), desc, 𝓛^R_d (R110), F(l), τ, top-only step, top-only
    interval, R(x, k).
- Claims MATCH their signed forms:
  - The line's RENEW is part (a) at a plus part (b), inside «if a ≥ 2»: narrower than signed, fine.
  - CASCADE drops «exactly one»: fine.
- REQUIRED KY-L1 (the tower clause). The line lists «the doubling-tower step («F(l) = 2(1 + F(l − 1)) level after level, so F(l) =
  2^(l+1) − 2») cannot hold beyond T in one run, by flips ≤ T …» under «and DEAD:».
  - The sentence itself is true (it is F ≤ T).
  - Placed under DEAD it records a refutation that KY-G1 refuses.
  - Move it out of DEAD, e.g. «; and, by flips ≤ T, the doubling-tower step of box 169 reaches F(l) = 2^(l+1) − 2 in a run only if
    that run has T ≥ 2^(l+1) − 2 (on dd_d5_F14 it is attained at level 3, F(3) = 14 = T, and not at level 4, 30 > T = 14)».
  - The «…» around «F(l) = 2(1 + F(l − 1)) level after level, so F(l) = 2^(l+1) − 2» is not box 169's text (box 169 has
    «F(l) = 2(1 + F(l − 1))» and «F(l) = 2^(l+1) − 2» in separate places). Drop the guillemets or quote exactly.
- Optional KY-L2: MERGE «for two options a, b of x» → «two distinct options». The letters a, b also name PAIR-KF's W-targets and the
  interval [a, b]; consider renaming.
- Optional KY-L3: PMV's «…» («the number of steps at which cv(z) rises is at most 1 + desc(z) for every mover z») is a restatement,
  not box 166's «VR(z) ≤ 1 + desc(z)». Mark it as a restatement or quote exactly with VR defined.
- Optional KY-L4 (DATA scope): «PAIR-KF 0 on 34,113 (run, mover) pairs» and «RETURN-COUNT 0 on 50,260 (run, mover) pairs» count only
  degree-2 movers (of level ≥ 1 for PAIR-KF; §8). Within the statements' own scope, so not a C121 «wider than coverage» case. «(run,
  degree-2 mover) pairs» would be exact.
- DATA: every other count equals §8 and keycheck.out, and is scoped to its statement. The line says the DEAD instances are «replayed by
  the same tool and by the box 150 checker»: true (re-run here).
- Source note «(P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md; L-NEW successors 54-55)»: complete now (every proof is in the packet; no fixes
  file yet). Once KY-1 / KY-G1 fixes are written, the note must name the fixes file (C122 E-3 precedent).
- Verdict: NOT YET (KY-L1).

## DONE / FINDINGS / NEEDS
- DONE: this report; premise byte tests; proof checks; instance recomputation with my own simulator; my own lemma checks with controls;
  check.sh block re-run; TARGET diff; L-1 definitions / DATA / shape.
- FINDINGS:
  - Every lemma and corollary of §2-§6 SIGNED; DEAD PM SIGNED.
  - DEAD PMV SIGNED WITH GAP KY-1 (false «7 = 1 + desc(6)»).
  - The tower DEAD REFUSED (KY-G1): box 169's prediction includes T ≥ F(l), so F ≤ T refutes nothing in it; the signable content is
    the implication F ≤ T.
  - L-1 NOT YET (KY-L1).
- NEEDS: L-NEW (via the Lead): fixes entry for KY-1 and KY-G1 (relabel §7 (c)); line L-2 with KY-L1 (+ optional KY-L2-L4, KY-P1, P2).
