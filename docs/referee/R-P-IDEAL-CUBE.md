# R-P-IDEAL-CUBE: REFEREE report on P-IDEAL-CUBE (L-NEW successor 50, box 154)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-04T02:49Z by date -u. Independent: I did not read docs/referee-2/.
- Object: claude/l-new d97555d4, an ancestor of origin/claude/l-new. I re-measured both files:
  - docs/new/P-IDEAL-CUBE.md: sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb, 186 lines;
  - docs/new/P-IDEAL-CUBE-line-L1.txt: sha1 99ae8face50615b4ce1ce5cd5e69f223f17208e1, 1 line, no «|».
- I read the packet from git show d97555d4 and ran its checks in a detached worktree of d97555d4.

## 0. Verdicts
| § | statement | verdict | notes |
| --- | --- | --- | --- |
| §1 | Definitions D-ORI, D-USO, D-COMB, D-DEC; the [WW22] quotes | quotes VERBATIM (v1); definitions faithful | §1 below |
| §2 | Lemma DECOMP (o), (a), (b), (c) | SIGN | |
| §3 | Lemma MULTI→SINGLE | SIGN | |
| §3 | Corollary T ≤ LP | SIGN | |
| §4 | Theorem LADDER-LP (with Facts F0-F4, Claim UP(i)) | SIGN | |
| §5 | machine check, «does NOT claim», READING, TARGET diff | not to sign; w102 and w103 re-run MATCH; diff agreed | |
| line | L-1 | NOT YET | REQUIRED CUBE-L1 (§6) |
- Landing condition CUBE-P1. The premises include P-IDEAL-RED's ENC and LOCAL (b), (c). Both referees signed them, but they are NOT
  landed: RESULTS has no R105 at trunk bf60f418. Under the premise rule (landed RESULTS or proofs carried in the packet), this
  packet lands only after R105. The alternative is for the packet to carry ENC and LOCAL (b)'s proofs, which are 6 lines.
- Labels.
  - PROVED (lane + REFEREE): DECOMP, MULTI→SINGLE, T ≤ LP, LADDER-LP.
  - LADDER-LP is a lower bound for LP only, not for IDEAL runs. Nothing is bounded polynomially.
  - G-N5-TIME OPEN. Not M3, not M4, not a gauntlet step.

## 1. [WW22] quotes, against a source I opened myself
- Source: arXiv:2207.05985, «Realizability Makes a Difference: A Complexity Gap for Sink-Finding in USOs», S. Weber and J. Widmer.
  - Only version: v1, submitted Wed 13 Jul 2022 06:46:22 UTC (abs page).
  - I read the LaTeX source (e-print, main.tex), downloaded 2026-11-04 into the scratchpad. It is not committed.
- Numbering. includes.tex puts every environment on ONE counter (\newtheorem{definition}[theorem]). Two «restatable» theorems in the
  introduction (main.tex l. 90, 93) come first. So:
  - Hypercube Orientation = Definition 3 (l. 126); Unique Sink Orientation = Definition 4 (l. 130);
  - the JumpAntipodal theorem = Theorem 18 (l. 262).
  - The «§2.2» sentence is in \subsection{(Realizable) Matoušek-type USOs} (l. 142), the second subsection of §2 Preliminaries
    (l. 170). The packet's numbers are CORRECT.
- Verbatim, modulo LaTeX rendering (\emph, \xor → ⊕, \not= → ≠, \matousek{} → Matoušek):
  - Def. 3 (l. 127): EQUAL, including «for all v∈V», which leaves V undefined in the source too.
  - Def. 4 (l. 131): EQUAL.
  - §2.2 (l. 170, second and third sentences): EQUAL.
  - Remark after Thm 18's proof (l. 269, first sentence): EQUAL.
- D-DEC drops «not influenced by any other dimension» from the §2.2 sentence. In [WW22] «combed» is the same-direction property of a
  face, so D-DEC (every face of dimension ≥ 1 has a dimension whose edges all point the same way) is the paper's «decomposable».
  DECOMP (c) proves the stronger form anyway: C_b(y) is constant on F, so y is not influenced by the other free coordinates.
- No theorem of [WW22] is a premise. The Thm 18 remark is quoted only to show that the paper uses the word for general USOs.

## 2. Premise route
- Premises used:
  - RESULTS R104's model definition (landed);
  - P-IDEAL-RED §0 (notation only) and ENC: used in §0 for «faces never tie» and «C_s(x)»;
  - LOCAL (b): used in DECOMP (o), (b), (c), MULTI→SINGLE and F1/F4;
  - LOCAL (c): stated as a premise. In this degree-≤-2 cube argument the keys do not enter, so it is cited but not needed.
- Other references: N5-CUBE-box153 appears only as «Source»; L-RED R178 and R201 appear only in attributions and the READING. No
  docs/lit and no docs/sources (grep).
- CUBE-P1 (above): ENC and LOCAL are not yet landed. They are signed by both referees with CHECKER C116 PASS (Lead 02:46Z).

## 3. Proof checks
- DECOMP: SIGN.
  - (o): x is not its own strict Ξ-descendant, so C(x) is the same at b and b ⊕ e_x (LOCAL (b)). Exactly one endpoint differs from
    it.
  - (c): the strict Ξ-descendants of the largest-π free coordinate y have larger π, so they are fixed in F (degree-1 movers never
    vary). C(y) is constant on F, and every y-edge points to the facet {b(y) = C(y)}.
  - (a): induction on dim F through that facet. A vertex off the facet has an outgoing y-edge. A facet vertex is a sink of F iff it
    is a sink of the facet.
  - (b): E(b) = Σ o(b)_x 2^π(x). The x-term drops, the terms above π(x) are unchanged (LOCAL (b)), and the terms below change by at
    most 2^π(x) − 1. So E falls strictly, and no cycle exists.
- MULTI→SINGLE: SIGN. At degree 2 every x ∈ Mv_t moves to C_(s_(t−1))(x). Switching in increasing π changes only coordinates of
  smaller π, so the C of later x_j is unchanged (LOCAL (b)), and each edge is directed. b^m = s_t.
- T ≤ LP: SIGN. Σ_t |Mv_t| ≥ T because Mv_t ≠ ∅. The concatenation is a directed path from s_0, and LP is finite by (b).
- LADDER-LP: SIGN. I checked every fact.
  - F0: rank order u0,0 < v0,0 < u0,1 < v0,1, all parities even. So C(u_0) = C(v_0) = 1, B_0 = 1 at (0,0) and (1,1), and B_0 = 0 at
    (1,0).
  - F1: the symmetric difference of x's two faces is {β(x,0), β(x,1)} ∪ (Cur(u_(i−1)) △ Cur(v_(i−1))). The second part is non-empty
    and of higher rank, so C(x) = B_(i−1).
  - F2: same option, same tail. They differ only in β(u_i,k) < β(v_i,k), since both of v_i's ranks are above both of u_i's.
  - F3: different targets decide.
  - F4: Cur of pair j reads only pairs ≤ j.
  - Settled pairs above i sit on option 1 by F2 (both movers on one option ⇒ B = 1), whatever the lower pairs do. So «unchanged» in
    UP(i)'s hypothesis is right.
  - UP(i): two directed switches, with UP(i + 1) run twice on the hypotheses it needs (b′ = 1, then b′ = 0). F4 keeps B_(i−1) and
    C(v_i) fixed during the recursion. Count 2 + 2(2^(K−i) − 2) = 2^(K−i+1) − 2, with base i = K − 1.
  - Main proof: start settled, B_0 = 1. u_0 then v_0, each followed by UP(1), gives 2^(K+1) − 2. K = 1 gives 2.
  - L_K is a valid IDEAL-ACYC genome: level 0, distinct ranks, Ξ-edges from pair i to i − 1, any distinct gates.

## 4. Machine checks
- w103 at d97555d4 (box154/ladder.py 10): ten «OK» lines. The K = 7 line equals check.sh's expected string verbatim (path 254, flips
  [2, …, 128], DP_longest 254, ideal_T 0). MATCHES.
- w102 at d97555d4: «DECOMP genomes 25 faces 478953 USO 0 COMB 0 ORDER 0 ACYC 0 JUMP 0 maxjump 7» and «LONGPATH ladlp_5.json n2 10
  longest 114 ideal_T 1». These equal packet §5 (25 genomes, 478,953 faces, LP 114 at N = 10).
- Own check: docs/referee/scratch/cube_probe.py, on xinew_probe's β-SET simulator written from R104's text; log in
  xinew_logs/cube_probe.txt.
  - L_K is built from §4's TEXT. The DP longest directed path from b_0 is 2, 6, 14, 30, 62, 126 = 2^(K+1) − 2 for K = 1..6. This
    agrees with the theorem and with the packet's «equality for K ≤ 7».
  - 400 random degree-≤-2 IDEAL-ACYC genomes (1-7 degree-2 movers), 95,136 faces: unique sink 0 failures; acyclicity (DFS) 0; the
    largest-π free coordinate combed 0; MULTI→SINGLE 0; T ≤ LP(s_0) 0.
  - No negative control was run for the cube checks. The proofs carry the signatures.

## 5. Diff against TARGET.md
- No statement mentions a parity game, a winning region, an algorithm's running time, or a cost model (TARGET §1-§3). Each statement
  is about the improvement orientation of R104's IDEAL model.
- LADDER-LP is an exponential lower bound on directed paths, not on any algorithm's run. Its own DATA says the IDEAL run of L_K is
  empty.
- Agreed with packet §5: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## 6. Line L-1, word by word against the packet
- MATCHES:
  - scope: IDEAL model of R104, acyclic Ξ-graphs, degree ≤ 2;
  - premises;
  - definitions of D2, Q_G, C_s(x) and o_G (= D-ORI);
  - DECOMP: USO per [WW22] Def. 4 (the parenthesis is the definition); acyclic with E falling (proof (b)); the largest-π free
    coordinate combed; decomposable as in §2.2;
  - MULTI→SINGLE and T ≤ Σ #Mv_t ≤ LP_G(s_0);
  - LADDER-LP: L_K's description equals §4 clause by clause (targets, parities, rank blocks, both in-pair orders, start). The gate
    indices are unstated, which the theorem allows. The bound is 2^(K+1) − 2 = 2^(N/2+1) − 2;
  - the tail: not for IDEAL runs, Ξ-cyclic and degree ≥ 3 not covered, OPEN, not M3 / step 4 / TARGET;
  - DATA: equal to my re-runs.
- REQUIRED CUBE-L1. «T ≤ LP cannot by itself give a polynomial bound, and the W-key rule must carry any such bound» puts the packet's
  §5 READING into the line as a statement.
  - The first half follows from T ≤ LP plus LADDER-LP, as a statement about this route.
  - «the W-key rule must carry any such bound» is not proved. Which runs the step rule allows without the key is not defined, so
    «must» has no signed content.
  - New: «… not for IDEAL runs: a bound on LP alone cannot give a polynomial bound on T (READING: a polynomial bound on IDEAL runs
    must use the W-key rule); …».
- OPTIONAL:
  - CUBE-L2: cite [WW22] with its version, «arXiv:2207.05985v1, Def. 4».
  - CUBE-L3: «where both options of u_0 and v_0 go to the exit» → «… (all movers of degree 2, distinct gate indices) …», so that the
    genome is visibly complete.
- VERDICT: line L-1 NOT YET. It matches once CUBE-L1 is applied. CUBE-P1 (landing after R105) is a landing condition, not a line
  change: the line already says «RESULTS R105 when landed».

## DONE / FINDINGS / NEEDS
- DONE:
  - this report;
  - w102 and w103 re-run at d97555d4: MATCH;
  - [WW22] v1 quotes and numbering verified against the LaTeX source;
  - own cube_probe.py: L_K LP = 2^(K+1) − 2 for K ≤ 6; 0 violations on 400 random genomes.
- FINDINGS:
  - DECOMP, MULTI→SINGLE, T ≤ LP and LADDER-LP are SIGNED, with no proof gap.
  - Line L-1 NOT YET: CUBE-L1 (a READING stated as fact).
  - CUBE-P1: lands only after R105.
- NEEDS: Lead: route CUBE-L1 (and optionally CUBE-L2/L3) to L-NEW 50; land after R105. I will do a §C on line L-2 when it is frozen.
