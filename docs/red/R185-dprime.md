# R185 Box 136 retarget: D″-cycles EXIST (first observed: dcyc3_n48, d2cyc4_n72; confirmed with L-NEW's own dmerge2.py), but they are inert and short (stretch ≤ 4, the cycle vertices do not move). CN moves inside FL runs never return: they go UP in index, or DOWN only by a shortcut onto the current W-cycle (Lemma CN-UP, PROVED, lane). CNMAX does not grow with n in the climbs (L-RED successor 43)
Started 2026-11-01 19:44Z (Lead message 19:37Z, read 19:43Z; date -u). Brief: «(1) A D″-cycle: a NON-head-dominated mutual dependency
through a gate … Your D′-cyclic climb should score D″-cycles instead. (2) CNMAX: W-cycle-node moves in one FL run. cw11_n24 has 7.
Measure the trend against n.»
Labels: PROVED (lane), DATA, READING. Premises: packet P-N5-ANCHOR (f009a9a1) §1-§2; box 135 (MERGE, CASC-M) and box 136 (C-STATIC-Ξ,
DOM, CASC-M″; claude/l-new 15d35408, docs/new/N5-SELF-box136.md); SPEC S1 with FIX 2 and Q2 (docs/new/N5-ssi-global.md); si.py
l. 182-195. Not a TARGET.md claim. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- (1) D″-cycles exist. Box 136 §3 lists «none observed»; that is now answered.
  - dcyc3_n48 (my R184 pin) has a D″-cyclic stretch [6, 9]: cycle 6 ↔ 11, levels 4 and 7.
  - d2cyc4_n72 (climb, this box) has a D″-cyclic stretch [6, 10]: cycle 0 ↔ 13.
  - Both are confirmed by L-NEW's own dmerge2.py (STRETCH=1 DOM=1: CYC 1, printed cycles [6, 11, 6] and [0, 13, 0]) and by my port
    (dcyc.py DM2=1). That port reproduces box 136 on odxi_many_n32 (3 / 3 acyclic) and odxi_n37 (18 own-segment hits).
  - The cycles are not head-dominated. In dcyc3_n48, 11's comparison of 1 against 31 is decided by the Odd vertex 4 (priority 26) in
    the TAIL of 31's segment 31, 4, 6, 8, 27, past the head [31]. 6 lies on that tail, so 11 → 6 survives DOM.
  - They are INERT:
    - dcyc3_n48: 6 never moves in the stretch; 11 moves once (1 → 31 at 7).
    - d2cyc4_n72: neither 0 nor 13 moves.
    - Each stretch is a cascade of one mover per transition (dcyc3: 11, 22, 36; d2cyc4: 31, 11, 22, 5).
  - Time structure (READING, dcyc3_n48). The edge 6 → 11 exists only at state 6, while σ(11) = 1. Once 11 has moved to 31, 6's
    option 47 runs 47 … 11 → 31 → 4 → 6. That is 6's own segment, the static C-STATIC-Ξ case. So the two edges of the cycle are
    never present at the same state.
  - Climb trend: longest D″-cyclic stretch 3 at n 48, 4 at n 72 (5,000 mutations each). This is DATA, not a growth claim.
- (2) CNMAX does not grow with n in the climbs:
  - cw11_n24: CNMAX 3 (CNMOV 7 over 4 runs);
  - climb from cw11 + 24 random vertices (n 48): 3;
  - from cw11 + 72 (n 96): 2;
  - the gadget family (R184) reaches 6 at n 57, one move per gadget.
- Lemma CN-UP (PROVED, lane; §2): at an FL transition, a W-cycle node c's new option has index ≥ its old one, unless another option
  of c lies on the old option's W-cycle path back to c (a shortcut), or the new option is c's self-loop.
  - Corollary: when no option of c lies on another option's W-cycle path (e.g. gates with τ → c, as in all R184 gadgets), c moves at
    most |T_c| − 1 times per FL run and never returns.
  - DATA: corpus 13 CN moves, 10 up / 3 down, 0 returns, 0 down moves without a shortcut.
- Erratum to R184: its «returns at a cycle node happen inside one FL run» was wrong (the moves of c = 33 lay in different FL runs).
  R184 is corrected in place; the corrected lines are marked ERRATUM.

## 1. D″-cycle details (DATA)
| instance | n | D″-cyclic stretch | cycle | moves of the cycle vertices in it | stretch movers | DOM cuts | own-segment hits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dcyc3_n48 (R184 pin) | 48 | [6, 9], L 3 | 6 ↔ 11 (levels 4, 7) | 6: 0, 11: 1 | 11, 22, 36 | 18 | 15 |
| d2cyc4_n72 (this box) | 72 | [6, 10], L 4 | 0 ↔ 13 (levels 5, 4) | 0, 13 | 31, 11, 22, 5 | 32 | 10 |
| odxi_many_n32 (R179) | 32 | none (3 / 3 acyclic) | – | – | – | 117 | 0 |
- dcyc3_n48 in detail (state 6, z-world, w = 13):
  - 11 → 6: 11's pair (31 vs 1) has Y′ = 31, 4, 6, 8, 27 and Z′ = 1, 0. The relevant vertices above w are 4 (Odd, 26) on Y′ and 1 (Even,
    26) on Z′. Rank by (priority, index): 4 is more relevant. 4 lies in Y′'s tail (head = [31]), so DOM does not cut it.
  - 6 → 11: 6's pair (47 vs 8) has Y′ = 47, 24, 17, 26, 20, 11, 1, 0 at state 6.
  - From state 7 on, Y′ = 47, 24, 17, 26, 20, 11, 31, 4, 6, which ends at 6 itself: C-STATIC-Ξ, static.
- So a time-resolved D″ (edges taken per state, cycles counted only among edges present at one state) would be acyclic here. Whether
  CASC-M″'s induction can use the per-state digraph is a question for the proof side.

## 2. Lemma CN-UP (PROVED, lane)
Setting: an FL transition j (gating state j − 1); c an Even W-cycle node (W-length 0) with o := σ_(j−1)(c) and y := σ_j(c).
Q := o's W-play (σ_(j−1), τ) from o up to its return to c: q_0 = o, q_1, …, q_r, then c.
Claim: y = c (c's self-loop), or index(y) ≥ index(o), or some option of c other than o lies on q_1 … q_r.

Proof.
1. Where c's choice comes from. σ_j is S4a's arena optimum: S1 run on the dual of H_(j−1), where Odd of the dual (= Even of G) keeps
   A_(j−1)(v) ∋ σ_(j−1)(v), and Odd of G keeps τ. W*_j = W_j = W_(j−1) = W, and W(c) = (c, ∅, 0), so c is a cycle node of that
   valuation and gets its choice from S1 (v), as FIX 2 / Q2 spell out:
   - a DFS from c over the arena graph;
   - successors in ascending index, each alive vertex of rank < rank(c) marked when pushed, last pushed popped first;
   - the scan stops at the first successor equal to c;
   - c's choice is the child of c on the tree path to the vertex whose scan found c.
2. Q is eligible.
   - Q ∪ {c} is the W-cycle through c, and c is its most relevant vertex, so every q_i has rank < rank(c).
   - Every q_i reaches c, so it lies in R(c). If some q_i had died earlier, in R(v′) of an earlier cycle node v′, then c, which
     reaches q_i (along the cycle), would also be in R(v′), so c would be dead and not processed as a cycle node. Contradiction.
   - All edges of Q are arena edges: σ_(j−1)(v) ∈ A_(j−1)(v), and τ at Odd.
3. The scan of c. If c's self-loop is in A_(j−1)(c), the scan of c's own list stops there and y = c. Otherwise every eligible option of
   c is pushed; o is eligible by 2.
4. Options above o are explored first (LIFO). Suppose no option of c other than o lies on q_1 … q_r. Two cases:
   - (a) Some subtree of an option y′ > o, explored before o, visits a vertex q_i. At that moment q_(i+1), …, q_r are unvisited: they
     are not options of c, so they were not pushed by c's scan, and an earlier subtree that visited one of them would have found c along
     Q first and stopped the search. So the DFS from q_i, which explores everything reachable and unvisited before backtracking, finds
     c through Q. The choice is then the root of that subtree or of an earlier one: an option > o.
   - (b) Otherwise, o's own subtree finds c: by the same argument along Q, or earlier by another route. The choice is o.
   In both cases index(y) ≥ index(o). ∎

Corollary. If no option of c lies on another option's W-cycle path back to c (for example, each option is a gate whose τ returns
directly to c), then inside one FL run c's option index strictly increases at each move (or c takes its self-loop, after which it stays,
since the self-loop then stays in A). So c moves ≤ |T_c| − 1 times per FL run and never returns.
- DATA:
  - r184/cnidx.py on the corpus: CN moves 13, up 10, down 3, returns 0, down without a shortcut 0. On cw11_n24: 7 / 6 / 1 / 0 / 0; its
    down move is 23 → 0 at j = 8, and 0 lies on 23's W-cycle path back to 7.
  - All R184 gadgets: each c moves once, up.
  - Adversarial climbs (score = down moves without a shortcut, then down moves) from cw11_n24 and cnmov_k8_n57 (3,000 / 2,000 mutations): best 7 CN moves with 2 down (both shortcuts) / 6 up; 0 down moves without a shortcut,
    0 returns.
- Use for the proof side (READING): inside an FL run, CNMOV ≤ Σ_c (|T_c| − 1) plus the shortcut moves. A shortcut makes c's W-cycle
  pass through a strictly later point of the old cycle Q. The open part is to bound how often «up» moves can re-lengthen the cycle
  after a shortcut, i.e. whether index-up and shortcut moves can alternate. The data show no alternation (0 returns).

## 3. Tools and pins
- r184/dcyc.py:
  - DM2=1: box 136's z-world D″ with DOM cuts (port of dmerge2.py, same counts).
  - REFINE=1: R184's D″ without DOM.
  - SHOWCYC=1: print one cycle.
- r184/cnidx.py: CN moves per FL run (UP / DOWN / RET / DOWN_NOSHORT).
- r184/cnupclimb.py: adversarial climb against CN-UP.
- r184/climb184.py: DM2=1 MODE=cyc for D″-cycles; MODE=cn for CNMAX.
- Pins (r184/instances, pins.sha1): d2cyc4_n72 (new), dcyc3_n48 and cnmov_k8_n57 (R184). Each passes startck, Oink --zlk + verify
  (OINK OK), --tl verify (exit 0) and xeng (state sequences identical).

## 4. Next (Lead decides)
- Proof side:
  - Try CASC-M″ with a per-state D″ (both observed D″-cycles are temporally split).
  - Bound shortcut/up alternation at cycle nodes (CN-UP covers everything else).
- Attack side:
  - An ACTIVE D″-cycle: both cycle vertices move inside one stretch, with a tail-decided comparison on each side.
  - At a cycle node: an alternation of shortcut and up moves (a long option path that contains a smaller option, re-lengthened by a
    lower move).
