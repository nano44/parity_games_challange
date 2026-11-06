# P-IDEAL-KEYS fixes (append-only; the packet docs/new/P-IDEAL-KEYS.md, sha1 62b35bf7…, stays frozen)

## Entry 1 (2026-11-06 from 00:46Z by date -u; L-NEW successor 55; Lead relay 00:47Z of fix round 1)
- Reports answered: REFEREE 24, claude/referee ece8c4ee, docs/referee/R-P-IDEAL-KEYS.md (KY-G1, KY-1, KY-L1 required; KY-L2, KY-L3, KY-L4,
  KY-P1, KY-P2 optional); REFEREE-2 28, claude/referee-2 ebcf52d0, docs/referee-2/R2-P-IDEAL-KEYS.md (W-1, W-2, W-3 required; R-1, F-1,
  F-2, N-1). Every other item of the packet is signed by both and is not touched here.
- This entry carries one statement with a proof (TOWER, F-a below); the packet and this entry are the only files that carry proofs of
  the packet's statements. The line L-2 names both.

### F-a (KY-G1 REFUSE, KY-L1, R-1): §7 (c) is no longer DEAD; it becomes a consequence of Corollary F ≤ T plus a READING
- Replace §7 (c) and the «To sign» row «| §7 | DEAD: CONJECTURE PM; CONJECTURE PMV; the doubling-tower step | DEAD (instances; tower by
  Corollary F ≤ T) | … |» by: «| §7 | DEAD: CONJECTURE PM; CONJECTURE PMV. TOWER (consequence of Corollary F ≤ T) | DEAD (instances);
  TOWER PROVED | refutations of lane statements; one implication |».
- Why: box 169 §0's prediction reads «Predicted: F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l)» (docs/new/N5-PAIRLIN-box169.md, verbatim).
  It already includes T ≥ F(l), so Corollary F ≤ T refutes nothing in it; the phrase «over a fixed clock» is the packet's reading (box
  170's), not box 169's text. No statement of record is refuted, so nothing is DEAD.
- New §7 (c), statement TOWER (PROVED; hypotheses: IDEAL-ACYC, any degree, any width; for 𝓛^R_d with F(l) of §0, or for any pair a
  tower designates at level l). Let a run have a pair that flips F(l) = 2^(l+1) − 2 times (the value that the doubling step of box 169,
  «F(l) = 2(1 + F(l − 1))» (docs/new/N5-PAIRLIN-box169.md l. 26, verbatim), gives when iterated from F(0) = 2). Then that run has
  T ≥ 2^(l+1) − 2.
  - Proof. Corollary F ≤ T (signed by both): flips(p, q) ≤ T for every pair of every run. ∎
  - READING (not to sign): the doubling tower is NOT A SHORTCUT. It yields an exponential flip count only in a run that is itself
    exponentially long, i.e. only if it already answers G-N5-TIME negatively.
  - DATA (not to sign; keycheck.py lines «DEAD TOWER …» and «TOWER composition …», whose labels predate this entry; the tool and its
    frozen output are unchanged): dd_d5_F14 has F(0..4) = 2, 3, 6, 14, 7 and T = 14. The doubling step is attained at level 3
    (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14). The compositions KILL_PM_compose_dd_d5_F14.json and
    T1_dd_top8.json have T = 14 and largest pair flip count 14.
  - Does NOT claim: that the tower is DEAD; that no IDEAL-ACYC family has exponential T; that a gadget can never add steps.

### F-b (KY-1, required): §7 (b) «Does NOT claim»
- Replace «anything about moves(6) (it is 7 = 1 + desc(6))» by «anything about moves(6) (it is 7 = desc(6) ≤ 1 + desc(6) = 8)». Both
  referees measured moves(6) = 7 and desc(6) = 7.

### F-c (F-1, KY-P1, KY-L3): §7 (a), (b) quotes made verbatim
- §7 (a): replace «CONJECTURE PM (box 165): «for every IDEAL-ACYC genome and every start, moves(x) ≤ (deg(x) − 1)(1 + desc(x)) for every
  mover x».» by «CONJECTURE PM (box 165, title): «moves(x) ≤ (deg(x) − 1)(1 + desc(x))», stated there for every IDEAL-ACYC genome, every
  start and every mover x.» (the guillemets enclose box 165's title text exactly; the quantifiers are a restatement).
- §7 (b): replace ««VR(z) ≤ 1 + desc(z) for every mover z», VR(z) := …» by ««VR(z) ≤ 1 + desc(z)» (box 166 §1, verbatim), for every mover
  z, with VR(z) := …» (the definition of VR(z) unchanged).

### F-d (F-2, KY-P2): §7 (c) composition wording
- Replace «a desc-6 gadget on a reader of pair (6, 7), top mover with 8 moves» by «a desc-6 gadget whose top mover 10 (level 4, a reader
  of pair (6, 7)) moves 8 times; the genome's top level is τ = 5 (mover 14)».

### F-e (N-1): §4 LADDER «Does NOT claim»
- Replace «(it is tight at level 3 of one instance, §7 (c))» by «(the SECOND inequality, moves(x) ≤ 1 + F(lev(x) − 1), is tight at level
  3 of dd_d5_F14: moves(6) = moves(7) = 7 = 1 + F(2); the first is not: F(3) = 14 < moves(6) + moves(7) + F(2) = 20)».

### F-f (KY-L2): MERGE letters
- The packet's §6 already says «two distinct options a, b». In the line only, MERGE now reads «two distinct options k, k′», so a, b keep
  their other meanings (PAIR-KF's W-targets, the interval [a, b]).

### W-2 / KY-L4 counts, checked against experiments/new/box172/keycheck.out (unchanged, sha1 5100eb30…)
- Its COUNTS line has «pairkf_movers 34113» (keycheck.py counts degree-2 movers of level ≥ 1 for PAIR-KF) and «retcnt_movers 50260»
  (degree-2 movers for RETURN-COUNT). These are the numbers in L-2.

### Line L-2 (docs/new/P-IDEAL-KEYS-line-L2.txt, sha1 fb1b22763f5cc5e64fa2cab78468718b1321a846, 1 line, 5,542 bytes, 0 «|», 120 «(» =
  120 «)», depth never negative)
- L-2 = L-1 with exactly these ten replacements, applied by script; each old string occurs exactly once in L-1. No other byte changes.
  - R1 (W-1) RENEW binder: «w ∉ A_(s_(a−2))(h)» → «w ∉ A_(s_(a−2))(h) (A_s(h): h's current option under s and its options strictly better under s)»
  - R2 (KY-L2) MERGE letters: «(MERGE) at any degree, for two options a, b of x and a state s, v_s(x, a) − v_s(x, b) depends» → «(MERGE) at any degree, for two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends»
  - R3 (KY-L1 / R-1) tower out of DEAD, as a consequence of flips ≤ T: «(0 if that target is the exit X); and DEAD:» → «(0 if that target is the exit X); (TOWER, by flips ≤ T) a run in which the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» iterated level after level, reaches F(l) = 2^(l+1) − 2 has T ≥ 2^(l+1) − 2 (a READING, not a refutation: the doubling tower is not a shortcut around G-N5-TIME); and DEAD:»
  - R4 (W-3) PM quote: «PM («moves(x) ≤ (deg(x) − 1)(1 + desc(x)) for every mover x», desc(x)» → «PM («moves(x) ≤ (deg(x) − 1)(1 + desc(x))» for every mover x, desc(x)»
  - R5 (W-3 / KY-L3) PMV quote: «PMV («the number of steps at which cv(z) rises is at most 1 + desc(z) for every mover z») is false» → «PMV («VR(z) ≤ 1 + desc(z)» for every mover z, VR(z) the number of steps at which cv(z) rises) is false»
  - R6 (KY-L1) tower clause removed from DEAD: «; and the doubling-tower step («F(l) = 2(1 + F(l − 1)) level after level, so F(l) = 2^(l+1) − 2») cannot hold beyond T in one run, by flips ≤ T, and on dd_d5_F14 it is attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and blocked at level 4 (30 > T = 14) (2026-11-05)» → « (2026-11-05)»
  - R7 (W-2) PAIR-KF range: «PAIR-KF 0 on 34,113 (run, mover) pairs» → «PAIR-KF 0 on 34,113 (run, degree-2 mover of level ≥ 1) pairs»
  - R8 (W-2) RETURN-COUNT range: «RETURN-COUNT 0 on 50,260 (run, mover) pairs» → «RETURN-COUNT 0 on 50,260 (run, degree-2 mover) pairs»
  - R9 (KY-L1) tower values as DATA: «the three DEAD instances replayed by the same tool and by the box 150 checker)» → «the two DEAD instances replayed by the same tool and by the box 150 checker; TOWER, on dd_d5_F14: F(0..4) = 2, 3, 6, 14, 7 and T 14, the doubling step attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14))»
  - R10 (source note) fixes file named: «(P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md; L-NEW successors 54-55)» → «(P-IDEAL-KEYS, docs/new/P-IDEAL-KEYS.md with its fixes entry 1, docs/new/P-IDEAL-KEYS-fixes.md; L-NEW successors 54-55)»
- Word diff L-1 → L-2 (git diff --no-index --word-diff=plain; [-removed-] {+added+}):
  [-A_(s_(a−2))(h),-]
  {+A_(s_(a−2))(h) (A_s(h): h's current option under s and its options strictly better under s),+}
  {+distinct+}
  [-a, b-]
  {+k, k′+}
  [-a)-]
  {+k)+}
  [-b)-]
  {+k′)+}
  {+(TOWER, by flips ≤ T) a run in which the doubling step of box 169, «F(l) = 2(1 + F(l − 1))» iterated level after level, reaches F(l) = 2^(l+1) − 2 has T ≥ 2^(l+1) − 2 (a READING, not a refutation: the doubling tower is not a shortcut around G-N5-TIME);+}
  [-desc(x))-]
  {+desc(x))»+}
  [-x»,-]
  {+x,+}
  [-(«the-]
  {+(«VR(z) ≤ 1 + desc(z)» for every mover z, VR(z) the+}
  [-rises is at most 1 + desc(z) for every mover z»)-]
  {+rises)+}
  [-rises); and the doubling-tower step («F(l) = 2(1 + F(l − 1)) level after level, so F(l) = 2^(l+1) − 2») cannot hold beyond T in one run, by flips ≤ T, and on dd_d5_F14 it is attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and blocked at level 4 (30 > T = 14)-]
  {+rises)+}
  [-mover)-]
  {+degree-2 mover of level ≥ 1)+}
  {+degree-2+}
  [-three-]
  {+two+}
  [-checker)-]
  {+checker; TOWER, on dd_d5_F14: F(0..4) = 2, 3, 6, 14, 7 and T 14, the doubling step attained at level 3 (F(3) = 14 = 2(1 + F(2)) = T) and not at level 4 (2(1 + F(3)) = 30 > 14))+}
  [-docs/new/P-IDEAL-KEYS.md;-]
  {+docs/new/P-IDEAL-KEYS.md with its fixes entry 1, docs/new/P-IDEAL-KEYS-fixes.md;+}
- Verdict items closed by L-2: KY-L1 (R3, R6, R9), W-1 (R1), W-2 = KY-L4 (R7, R8), W-3 = KY-L3 (R4, R5), source note (R10), KY-L2 (R2).
