# Box 198 (D18): the pair-level charge for A, upper side (L-NEW successor 65, Opus; 2026-11-08, date -u)
Lead brief 15:25Z: «try to PROVE a recursion of the form A_v(x, y) ≤ c + 2·#(changes of the High above (x, y) in the interval), and then
bound the depth of such High chains …; state exactly where Howard's rule enters (BIN shows the abstract model alone cannot). If the depth
is unbounded, say what the recursion gives … and what extra property would make it polynomial.»
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Setting, notation and premises: box 197 (docs/new/N5-CORE-box197.md §1, §3,
Addenda 2-3): a vertex v of Γ3(G), a Λ-interval I of v in HOW3(G), the e-sets E_t(v) (t ∈ I), their changes and tops, tops(v, I).
Tools: experiments/new/box198/pair198.py; output box198/pair198.out (record); check198.sh, output check198.out, re-run by check.sh block
«BOX 198 PAIR».

## 0. Answer (one paragraph)
- PROVED: the recursion holds with «the High» read as the WHOLE part of v's e-set above the pair (Lemma PAIR-HIGH), and it needs only
  lex monotonicity (E-MON3), so it holds in the abstract model too. Its unrolled form bounds c_y (how often one letter is top) by the
  number of paths from y in a «re-arming DAG» on the letters (Lemma RA-PATHS). In BIN that DAG is complete and the path count is 2^depth:
  the recursion alone gives only an exponential bound, with depth up to M.
- T3 is polynomial iff C := max c_y is (Corollary C-EQUIV), a one-letter restatement of G-N5-TIME on Γ3, sharper than ALT-EQUIV.
- What would make it polynomial: a bound on the paths of the re-arming DAG, e.g. fan-in ≤ k and depth O(log(N + M)) (then C ≤
  (N + M)^O(log k)). That is where Howard's rule must enter; I have no proof that it does.
- DATA: a single «High» per letter (fan-in 1, which would give C ≤ M) is FALSE on climbed instances (fan-in 3 on NK6_cl21, 4 on
  DSALT9_n416). Measured on the test set (§4): C ≤ 5, RA depth ≤ 3, paths ≤ 8, fan-in ≤ 4; designed towers C ≤ 3, depth ≤ 2.

## 1. Lemma PAIR-HIGH (PROVED, lane; uses only E-MON3)
For letters y and x of tops(v, I) with y more relevant than x, let c_y := the number of changes in I whose top is y, and Dhi_y := the
number of distinct values of E_t(v) ∩ U_y over t ∈ I, U_y := the e-vertices more relevant than y. Then
(a) c_y ≤ Dhi_y; (b) A_xy ≤ 2·Dhi_y + 1 (A_xy the longest x/y alternation in tops(v, I)); (c) Dhi_y = 1 + Σ_{z ∈ U_y} c_z.
Proof.
- At a change with top z, z ∈ E_t \ E_(t−1) and nothing more relevant than z changes (E-MON3: the change is a strict lex increase).
- (a) Let t1 < t2 be consecutive y-tops. After t1, y ∈ E; just before t2, y ∉ E. So some change in (t1, t2) removes y; its top z is in
  the new set, y is not, and z is the most relevant element of the change's symmetric difference, so z is more relevant than y. That
  change alters E ∩ U_y. A y-top alters nothing in U_y. So between consecutive y-tops E ∩ U_y takes a new value, and by lex monotonicity
  of E ∩ U_y (a change with top in U_y raises it, any other leaves it) no value returns: c_y ≤ Dhi_y.
- (b) An x/y alternation of length L contains at least ⌊L/2⌋ y's, all y-tops: ⌊L/2⌋ ≤ c_y ≤ Dhi_y.
- (c) E ∩ U_y changes exactly at the changes whose top lies in U_y, and its values are distinct (lex increasing). ∎
- Reading: this IS the form «A ≤ c + 2·#(changes of the High)», with c = 3 and «the High» = E_t(v) ∩ U_y, the part of v's own e-set
  above the pair (#changes of it = Dhi_y − 1). L-RED 60's mechanism («A ≈ 1 + 2·#(High values under which the whole low counter
  replays)», R226 §9) is the tight case c_y = Dhi_y (counter «tight» in pair198.py).

## 2. Unrolling: the re-arming DAG (PROVED, lane; abstract)
- For a letter y, RA(y) := the set of letters z that are the most relevant top strictly between two consecutive y-tops. By §1 (a)'s proof
  every z ∈ RA(y) is more relevant than y, so RA is a DAG on the letters, edges pointing up.
**Lemma RA-PATHS.** c_y ≤ P(y), where P(y) := 1 + Σ_{z ∈ RA(y)} P(z), i.e. P(y) = the number of directed paths from y in RA (the
trivial path included).
Proof. Each of the c_y − 1 gaps between consecutive y-tops contains a top of its most relevant letter z ∈ RA(y); the gaps are disjoint,
so c_y − 1 ≤ Σ_{z ∈ RA(y)} c_z. Induction from the most relevant letter down. ∎
- If every letter has |RA(y)| ≤ 1 (one «High» per letter), then P(y) ≤ depth(y) ≤ Mact_I(v) and C ≤ M: polynomial.
- If |RA(y)| ≤ k and the longest RA-chain has d letters, P ≤ (k^d − 1)/(k − 1).
- BIN: RA(item j) = all items above j (the top between two item-j tops is the lowest set bit above j, and every one occurs), so
  P(item j) = 2^(M−j) = c_(item j): the bound is tight and exponential. The abstract model (CS(M)) has no restriction on RA.
**Corollary C-EQUIV (PROVED, lane, on P-N5-CHAIN's premises).** With C := max over v, I, y of c_y: |tops(v, I)| ≤ Mact_I(v)·C ≤ M·C, so
T3 ≤ (1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1), and C ≤ max(1, T3). T3 is polynomial iff C is.
Proof. |tops| = Σ_y c_y; then as in box 197's RE-EQUIV (D_I = 1 + |tops|, at most 2M + 3 intervals, T-QUIET3). ∎

## 3. Where Howard's rule has to enter, and what would suffice
- Nothing in §1-§2 uses the game: they hold for any lex-monotone set sequence. BIN realizes them with equality. So a polynomial bound
  must restrict the re-arming DAG through the game: which tops can separate two y-tops of one vertex.
- In the game a y-top at v (y = e_(x,k)) means: after it, v's play passes the mover x, σ_t(x) = k, Odd plays pe at y's gate, and v's e-set
  above y is unchanged. A re-arm by z means z (more relevant) entered v's set while y left, i.e. v's play was re-routed through z's gate.
  A Howard-specific bound would have to show that the routes through the high letters cannot be re-taken in all 2^d orders.
- Sufficient properties (each would give C polynomial; none proved):
  - (S1) fan-in 1: |RA(y)| ≤ 1. DEAD as a property of HOW3 (DATA §4: fan-in up to 4).
  - (S2) fan-in ≤ k and RA-depth O(log(N + M)): C ≤ (N + M)^O(log k). Consistent with L-RED 60's A ≈ 0.9·log2(N + M) trend, which is weak.
  - (S3) P(y) ≤ poly directly. Equivalent to the open core (C ≤ P ≤ … and C-EQUIV), so not a reduction.
- CONJECTURE RA-LOG: for every genome G with [E-LEV], every (v, I) and letter y, the longest RA-chain from y has O(log(N + M)) letters.
  Stated so that it can be attacked; with fan-in ≤ M it gives C ≤ M^O(log(N+M)), quasi-polynomial, NOT polynomial. Polynomial needs
  in addition a fan-in bound k independent of N + M (S2). I give both little weight beyond the data in §4.

## 4. DATA (tool pair198.py on the box 196/197 engine; unit: (genome, v, I), maxima over the genome; scope [E-LEV])
- Counters, all 0 on every row: ph1fail (PAIR-HIGH (a)), ph2fail ((b)), rafail (a re-arming letter not above y), rpfail (RA-PATHS).
| instance | T3 | C | max paths | RA depth | fan-in | A | tight |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | NK6_cl21 | 11 | 4 | 6 | 3 | 3 | 6 | 8 |
  | DSALT6_n108 | 21 | 4 | 6 | 3 | 3 | 6 | 13 |
  | DSALT7_n108 | 11 | 4 | 6 | 3 | 3 | 7 | 8 |
  | DSALT9_n416 | 30 | 5 | 8 | 3 | 4 | 9 | 0 |
  | CL2_21 | 23 | 4 | 5 | 3 | 3 | 5 | 0 |
  | CL2_22 | 28 | 3 | 4 | 3 | 2 | 5 | 29 |
  | CL3_31 | 15 | 2 | 2 | 2 | 1 | 3 | 0 |
  | CL3_32 | 24 | 1 | 1 | 1 | 0 | 2 | 0 |
  | TC2 | 12 | 2 | 2 | 2 | 1 | 3 | 0 |
  | TC2d | 10 | 1 | 1 | 1 | 0 | 2 | 0 |
  | TC3 | 18 | 2 | 2 | 2 | 1 | 4 | 0 |
  | TC3d | 14 | 1 | 1 | 1 | 0 | 2 | 0 |
  | TC3m | 17 | 2 | 2 | 2 | 1 | 3 | 0 |
  | TC4m | 37 | 2 | 2 | 2 | 1 | 4 | 0 |
  | TC5m | 43 | 3 | 3 | 2 | 2 | 5 | 0 |
  | H8C | 80 | 2 | 2 | 2 | 1 | 4 | 0 |
  | H6C | 51 | 2 | 2 | 2 | 1 | 4 | 0 |
  | LEAP_k64 | 129 | 2 | 2 | 2 | 1 | 3 | 6 |
  | rd2_d9 | 21 | 3 | 3 | 2 | 2 | 5 | 0 |
- Controls fire (NK6_cl21): ctrl1 (Dhi_y := 1) ph1fail 13, ph2fail 5; ctrl2 (paths := 1) rpfail 13 (box198/check198.out).
- Instances: NK6_cl21 (claude/l-si experiments/si/box88/inst, sha1 408b9988, = the Lead's), DSALT6_n108 / DSALT7_n108 / DSALT9_n416
  (claude/l-red 9c17e8c7 experiments/red/r226/inst, sha1 4136b27d / 16d48b3c / da3308b5), L-SI box-85 towers (box196/inst_si85), the
  box 197 tower family H6C, H8C, LEAP_k64, rd2_d9. Copies in box198/inst/ (the four external ones).
- Reading: the climbed instances (NK6, DSALT) reach fan-in 3-4 but depth only 3; the designed towers have depth 2 and fan-in ≤ 2. No
  instance has a re-arming chain longer than 3 letters, so the exponential of RA-PATHS never gets going here. Short runs (T3 ≤ 129).
