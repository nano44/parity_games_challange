# R2-P-IDEAL-CUBE: REFEREE-2 report on P-IDEAL-CUBE (L-NEW 50, box 154): DECOMP, MULTI→SINGLE, T ≤ LP, LADDER-LP, and line L-1
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-04 (date -u; see the commit).
Independence:
- I opened nothing in docs/referee/. A names-only `git ls-tree` on origin/claude/referee found 0 files matching «cube» at 02:50Z.
- My checker imports no lane code. I ran the lane's scripts only as the w102 / w103 commands, at the packet commit.

## 0. Object, source, premise route
- Packet: docs/new/P-IDEAL-CUBE.md at claude/l-new d97555d425d4995244dd1648d00b7c53418cd03d. sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb,
  186 lines. Re-hashed: match.
- Line: docs/new/P-IDEAL-CUBE-line-L1.txt, sha1 99ae8face50615b4ce1ce5cd5e69f223f17208e1. 1 line, 2,715 bytes, no «|». Re-hashed: match.
- **[WW22] opened by me.**
  - arXiv:2207.05985: the abstract page lists only v1 («Submitted on 13 Jul 2022»). I read the v1 LaTeX source, the e-print tarball
    (sha256 88e1f1b7074dfcd7bbd3ed01ba04ca071f5ecb3678c2a8d39cd16fbc48befa73), main.tex.
  - Numbering: one shared theorem counter (includes.tex: every environment is `[theorem]`). Two restatable theorems in the introduction
    are 1 and 2. So Hypercube Orientation = **Def. 3** (main.tex l. 126-128), Unique Sink Orientation = **Def. 4** (l. 130-132), and the
    JumpAntipodal theorem = **Thm 18** (l. 262; the remark is l. 269). §2.2 = «(Realizable) Matoušek-type USOs» (l. 142, sentence at
    l. 170). The packet's numbers are right.
  - **Every quote is verbatim**, with LaTeX math rendered:
    - Def. 3: «An orientation o of the n-dimensional hypercube … for all v∈V and i∈[n].» ✓
    - Def. 4: «A Unique Sink Orientation (USO) is an orientation of the hypercube, such that for each non-empty face F of the hypercube,
      the subgraph induced by F has a unique sink, i.e., a unique vertex which has no outgoing edges.» ✓
    - §2.2: «Thus, in each face there is a dimension which is not influenced by any other dimension, and all edges of that dimension
      point in the same direction. We therefore say that each face is combed, and that the whole Matoušek-type USO is decomposable.» ✓
    - After Thm 18: «JumpAntipodal requires only n vertex evaluations on all decomposable USOs, not only on the Matoušek-type USOs.» ✓
  - [WW22] has no formal definition of «decomposable» for general USOs. The packet's D-DEC is its OWN definition, and §1 says so
    («the §2.2 sentence with "not influenced …" dropped»). DECOMP (c) in fact proves the stronger §2.2 form too: the combed
    coordinate's direction is constant on F, so it is influenced by no free coordinate of F.
  - Only definitions are used. No [WW22] theorem is a premise (Thm 18 is quoted only for the word «decomposable»). ✓
- **Premise route ✓, with two remarks.**
  - The premises: R104's model definition (landed); P-IDEAL-RED §0, ENC, LOCAL (b) and (c) (signed by both referees; R105 per the Lead,
    CHECKER C116); [WW22] definitions. No docs/lit, no lane file.
  - (i) LOCAL (c) (keys) is listed but used nowhere. W plays no role in DECOMP, MULTI→SINGLE or LADDER-LP, and the step rule used in
    MULTI→SINGLE is §0's. Harmless, but the line should drop it (LC-P2).
  - (ii) The packet rests on P-IDEAL-RED. It must land after R105 (CHECKER ordering).
- **TARGET.md diff ✓.** Every statement is about the improvement cube of the IDEAL model: no game, no region, no running time, no
  algorithm claim. Not M3 or M4, not a gauntlet step. G-N5-TIME stays OPEN.

## 1. Verdict table
| § | statement | verdict |
| --- | --- | --- |
| §1 | Definitions D-ORI, D-USO (= [WW22] Def. 4), D-COMB, D-DEC; quotes | ✓ (quotes verbatim against v1; D-DEC is the packet's own) |
| §2 | Lemma DECOMP (o) orientation | **SIGN** |
| §2 | Lemma DECOMP (a) USO | **SIGN** |
| §2 | Lemma DECOMP (b) acyclic | **SIGN** |
| §2 | Lemma DECOMP (c) combed / decomposable | **SIGN** |
| §3 | Lemma MULTI→SINGLE | **SIGN** |
| §3 | Corollary T ≤ LP | **SIGN** |
| §4 | Theorem LADDER-LP (with facts F0-F4, Claim UP(i)) | **SIGN** |
| §5 | DATA, «does NOT claim», TARGET diff (not to sign) | DATA reproduced exactly; READING noted (§4 below) |
| line | P-IDEAL-CUBE-line-L1.txt | **does NOT match yet**: REQUIRED LC-1, LC-2 (§5) |

No gap in the mathematics. Packet precision P-1 (§2).

## 2. Paper check
- **§0, C_s(x) well defined.** The two options of x carry different β-sets because β(x, 0) lies only on (x, 0)'s chain. That needs
  acyclicity (x is not revisited on its own chain); ENC alone does not give it. Then ENC's total order gives a strict winner.
  - P-1 (precision): the packet cites ENC only. Cite acyclicity as well (as the line's «on acyclic Ξ-graphs» does).
- **DECOMP (o).** C_b(x) reads only strict Ξ-descendants of x (LOCAL (b)), and x is not one. So C is the same at b and b ⊕ e_x, and
  exactly one endpoint differs from it. That is Def. 3's consistency. ✓
- **DECOMP (c).** The free coordinate y of largest π has all its strict descendants at larger π, so they are fixed in F. C(y) is then
  constant on F (LOCAL (b)), and every y-edge of F points to {b(y) = C(y)}. ✓
- **DECOMP (a).** Induction on dim F via (c). A vertex off the facet F′ has an outgoing y-edge. On F′ the y-edge is incoming, so the
  sinks of F are exactly the sinks of F′. ✓
- **DECOMP (b).**
  - E = Σ_(D2) o(b)_x 2^π(x).
  - Along b → b ⊕ e_x: the x term drops out by (o).
  - Terms of z with π(z) > π(x) are unchanged: x is not a strict descendant of z (strict descendants of z have π > π(z)).
  - Terms of z with π(z) < π(x) change by at most Σ_(p < π(x)) 2^p, over positions of all movers, so the bound only loosens.
  - So E strictly decreases. ✓
- **MULTI→SINGLE.**
  - At degree 2, a mover of Mv_t moves to its other option, which is strictly better: s_t(x) = C_(s_(t−1))(x), and the coordinate is
    improving.
  - Switching in increasing π, the earlier-switched coordinates have smaller π, so none is a strict descendant of x_j. C(x_j) is
    unchanged and x_j is still unswitched, so the edge is directed. b^m = s_t. ✓
  - The corollary: consecutive directed edges in an acyclic orientation never repeat a vertex, so they form a directed path of length
    Σ|Mv_t| ≥ T. ✓
- **LADDER-LP.** I checked every fact against the rank layout.
  - (F0): u_0 and v_0 prefer option 1 (higher rank). B_0 is 1 on (0, 0), 1 on (1, 1), and 0 on (1, 0).
  - (F1): the two faces of a pair-i mover differ by its own two pair-i β's plus Cur(u_(i−1)) △ Cur(v_(i−1)) ≠ ∅, whose ranks are all
    higher. So C(x) = B_(i−1).
  - (F2): same option, same target; v's β outranks u's. So B_i = 1.
  - (F3): different targets; the better target decides. So B_i = 0 iff k = B_(i−1).
  - (F4): chains go downward.
  - Claim UP(i), by induction on K − 1 − i:
    - The precondition at UP(i + 1)'s calls holds: after u_i's switch, B_i changed 1 → 0 and pair i + 1 still sits on the old value 1.
      After v_i's switch, B_i changed 0 → 1, and pair i + 1 sits on 0, as the first UP(i + 1) left it settled.
    - v_i stays improving across UP(i + 1) (F4: C(v_i) = B_(i−1) reads only pairs < i).
    - Count 2 + 2(2^(K−i) − 2) = 2^(K−i+1) − 2; base 2 = 2^2 − 2.
  - The theorem's start is settled. u_0 and v_0 are improving throughout, since C = 1 is constant. Total 2^(K+1) − 2. ✓
  - The path is a path, not merely a walk, by DECOMP (b). My checker also confirms no repeated vertex.

## 3. Data
- **The lane's checks at d97555d4** (worktree; the exact w102 / w103 commands) reproduce the check.sh strings:
  - «DECOMP genomes 25 faces 478953 USO 0 COMB 0 ORDER 0 ACYC 0 JUMP 0 maxjump 7»;
  - «LONGPATH ladlp_5.json n2 10 longest 114 ideal_T 1»;
  - LADDER K = 1..10 all «OK»: paths 2 … 2046; flips [2, 4, …, 2^K]; DP_longest = 2^(K+1) − 2 for K ≤ 7; ideal_T 0.
- **My checker:** docs/referee-2/R2-P-IDEAL-CUBE/cube_check.py; logs in logs/run1.log and logs/control.log.
  - Values come from my own R2-P-IDEAL-RED simulator (sets, top-rank rule). L_K is built from the §4 text.
  - The ladder is exact for K = 1..12: every switch on the UP procedure's path is directed, there is no repeated vertex, and the length
    is 2^(K+1) − 2. Facts F0-F3 hold at every state of the path. DP longest path from b_0 = 2^(K+1) − 2 for K ≤ **8**, one further
    than the lane's 7. ideal_T 0.
  - DECOMP brute force over every face, with COMB under 3 random topological orders each, and MULTI→SINGLE / T ≤ Σ|Mv| ≤ LP on every
    start:

| input | genomes | faces (dim ≥ 1) | runs (all starts) | steps | violations |
| --- | --- | --- | --- | --- | --- |
| corpus box14x out/inst + box152 d5 (degree ≤ 2, ≤ 9 degree-2 movers; 30 files skipped as degree 3 or larger) | 18 | 62,730 | 2,880 | 5,906 | 0 |
| my random, degree ≤ 2, N ≤ 8, depth ≤ 4 | 400 | 27,975 | 4,507 | 3,293 | 0 |
| my random, degree ≤ 2, N ≤ 9, depth ≤ 2 (wide) | 150 | 11,227 | 1,265 | 779 | 0 |

  - Control: the SMALLEST-π free coordinate is not combed in 1,495 of 18,095 faces of dimension ≥ 2. So (c)'s choice «largest π»
    matters, and COMB detects failures.
  - Gate-order probe (for the line): with gates DECREASING in k, L_K's IDEAL run from b_0 has T = 1 (K = 1..5). With gates increasing in
    k, T = 0, as §4 says.

## 4. Notes on §5 (not to sign)
- READING «The route "bound LP" is DEAD by Theorem LADDER-LP». The theorem gives explicit instances with LP = 2^(N/2+1) − 2 or more,
  so «LP is polynomially bounded on degree-2 IDEAL-ACYC» is false, with a refereed proof. L43 is satisfied.
- «any proof of IDEAL-ACYC-POLY must use the W-key gate» is a READING. What is proved is narrower: T ≤ LP alone cannot give a
  polynomial bound. See LC-2 for the line.

## 5. Line L-1 (99ae8fac): clause check and required changes
Clause by clause, against the packet:
- premise list ✓ (but see LC-P2);
- D2, Q_G, C_s, o_G ✓;
- DECOMP: USO per [WW22] Def. 4; acyclic via the potential; combed coordinate of largest π; decomposable ✓;
- MULTI→SINGLE and T ≤ Σ #Mv_t ≤ LP ✓;
- LADDER-LP: the genome description matches §4 exactly (pairs, targets, even parities, rank blocks and orders, start); the bound
  2^(K+1) − 2 = 2^(N/2+1) − 2 ✓;
- label «STRUCTURE / REDUCTION … exponential lower bound for LP, not for IDEAL runs» ✓;
- the not-covered list ✓; DATA numbers ✓.

Required changes:
- **LC-1 (REQUIRED: a DATA clause false as written).**
  - The line never fixes L_K's gate indices, and «DATA: on L_K the IDEAL run from that start is empty» holds only for gates increasing
    in the option index. My probe: decreasing gates give T = 1.
  - Old: «(DATA: on L_K the IDEAL run from that start is empty)»
  - New: «(DATA: on L_K with gate indices increasing in the option index, the IDEAL run from that start is empty)»
- **LC-2 (REQUIRED: a reading stated as a fact; D18).**
  - Old: «T ≤ LP cannot by itself give a polynomial bound, and the W-key rule must carry any such bound;»
  - New: «T ≤ LP cannot by itself give a polynomial bound (READING: a polynomial bound on T must use the W-key rule);»
- **Precision (optional).**
  - LC-P1: π is used in the acyclicity clause («Σ_x … 2^π(x)») before it is bound in the comb clause. Move «(π a topological order of
    the Ξ-graph)» to its first use.
  - LC-P2: drop «(c)» from «Lemma LOCAL (b), (c)»; no proof uses it.
  - LC-P3: name the version read, «arXiv:2207.05985 (v1)».
- With LC-1 and LC-2 applied and nothing else changed, I expect MATCHES on the L-2 word-diff.

## DONE / FINDINGS / NEEDS
- DONE:
  - DECOMP (o)-(c), MULTI→SINGLE, T ≤ LP and LADDER-LP are all SIGNED. Every [WW22] quote is verbatim against v1; the numbering is
    checked.
  - The premise route is clean. The TARGET diff is clean.
  - The lane's DATA is reproduced exactly. My own checker gives 0 violations; its control fires.
- FINDINGS:
  - No mathematical gap.
  - Line L-1 needs LC-1 (the gate-dependent DATA clause) and LC-2 (a reading labelled as such).
  - LOCAL (c) is listed but unused.
  - P-IDEAL-CUBE must land after R105.
- NEEDS: L-NEW: line L-2 with LC-1 and LC-2 (LC-P1 to LC-P3 optional).
