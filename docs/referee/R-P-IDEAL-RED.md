# R-P-IDEAL-RED: REFEREE report on P-IDEAL-RED (L-NEW successor 50, box 150)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-03T20:40Z by date -u. Independent: I did not read docs/referee-2/.
- Object: claude/l-new 0ebddcf5, docs/new/P-IDEAL-RED.md, sha1 06f2c18609e355a1e62c138c420bd49dc401cae4, 261 lines.
  - I re-measured all three.
  - 0ebddcf5 is an ancestor of origin/claude/l-new.
  - I read the file from a detached worktree of 0ebddcf5.
- My pre-check of the lane lemma (docs/referee/R-XI-NEW-precheck.md, a4e7b4a9) was written before the packet. Its gaps are
  re-measured in §4 below against the packet's own text.

## 0. Verdicts
| § | statement | verdict | notes |
| --- | --- | --- | --- |
| §1 | Lemma ENC | SIGN | |
| §1 | Lemma LOCAL (a)-(c) | SIGN | |
| §2 | Lemma MONO | SIGN | REQUIRED text fix IR-1: the «Does NOT claim» parenthetical is false |
| §3 | Lemma XI-NEW | SIGN | |
| §3 | Corollary RISE (a)-(c) | SIGN | |
| §4 | Theorem CHAIN-BACK (i)-(ii) | SIGN | |
| §4 | Corollary U-EQ | SIGN WITH GAP U-1 | «U ≤ T − 1» is false at T = 0; the equivalence stands |
| §5 | Lemma KEYFLIP (deg ≤ 2) | SIGN | |
| §5 | Corollary KF-EQ (deg ≤ 2) | SIGN | |
| §6 | Lemma DECREMENT (a)-(c) | SIGN | |
| §6 | Corollary EXACT-ENERGY | SIGN | |
| §7 | Corollary TOP-MONO (deg ≤ 2) | SIGN | |
| §7 | Corollary RANK-BOUND (deg ≤ 2) | SIGN | optional P-1 (the R = 0 case) |
| §8 | Lemma INTERVAL-RESTRICT (i)-(iii) (deg ≤ 2) | SIGN | optional P-2 (option identification between G and H) |
| §8 | Corollary INTERVAL-CHARGE (deg ≤ 2) | SIGN | |
| §8 | Corollary RECURSION (deg ≤ 2) | SIGN | optional P-3 (the index of the sum is a count, not a position) |
| §9 | machine check, exclusions, TARGET diff | not to sign; re-run MATCHES (§5); exclusions checked (§4); diff agreed (§6) | |
- Labels.
  - Every signed item is PROVED (lane + REFEREE). None bounds anything polynomially.
  - G-N5-TIME stays OPEN. Not M3, not M4, not a gauntlet step.
  - All items are about the IDEAL-ACYC model of RESULTS R104 only.

## 1. Premise route
- The packet declares a single premise: RESULTS R104's DEFINITION of the IDEAL model and of the Ξ-graph. No theorem of R104 is used.
  - R104 is landed: «[refereed-only]», CHECKER C115 PASS.
- I grepped every reference in the packet: R104, R178, R188, R189, «box 14x», N5-IDEAL-STATE, docs/lit, docs/sources,
  N5-INTERVAL-box148.
  - Outside R104, every reference sits in a heading, a «Not used» list, a «Does NOT claim» line, the box-148 note, or §9.
  - None of them occurs inside a «Proof.».
  - No docs/lit premise is used (lesson C115 E-1).
- Every proof uses only §0's definitions and earlier lemmas of the packet. The dependency order is:
  ENC → LOCAL → MONO → XI-NEW → RISE → CHAIN-BACK; LOCAL → DECREMENT → EXACT-ENERGY / TOP-MONO → RANK-BOUND / INTERVAL-* → RECURSION.
  It has no cycle.
- §0 against R104's statement, clause by clause:
  - movers, levels;
  - W-target of level lev − 1 (none at level 0);
  - Ξ-target a mover or X;
  - distinct β-ranks with parities, distinct gate indices, a start;
  - the Ξ-value as the β-set of the chain up to the first Ξ-target X;
  - comparison by the largest-rank β of the symmetric difference, the parity deciding;
  - availability = the current option plus the strictly better options, read at the OLD state;
  - the key = gate indices of the W-target chain under the NEW state, lowest level first;
  - stop when nothing is available or nothing changes; T = L(G).
  All agree. The additions N ≥ 1, deg ≥ 1 and «ranks ∈ ℕ» are implicit in R104 and change nothing.

## 2. Proof checks, statement by statement
- ENC: SIGN.
  - The other elements of P △ Q have distinct ranks below r*, so their sum has absolute value ≤ 2^r* − 1. The sign is the β* term.
  - The recursion v = ε + v(next) holds because a chain's options are distinct (acyclic). Correct.
- LOCAL: SIGN.
  - (a) is an induction along the chain.
  - (b): the movers after x on any chain of x's options are strict Ξ-descendants.
  - (c): a key reads only lower levels (by induction on the level).
- MONO: SIGN.
  - The induction runs in decreasing π. It applies to every mover x, moving or not: s_t(x) ∈ A_(s_(t−1))(x) always.
  - It is the same proof as my pre-check §3. XI-G1 is closed.
  - IR-1 (REQUIRED, text): «Does NOT claim: that any non-current option's value is monotone (it is not in general)» is FALSE in the
    IDEAL-ACYC model.
    - For every option, v_s(x, k) = ε(x, k) + cv_s(xt(x, k)), or ε(x, k) when xt = X (ENC).
    - cv of the mover xt(x, k) is monotone by MONO itself. So EVERY option's value is non-decreasing along the run.
    - DATA (mine): 0 failures of all-option monotonicity on the packet's 46 corpus genomes, its 200 random genomes, and 4,500 + 3,000
      own genomes (xinew_probe.py check «mono» compares every option).
    - Fix: delete the parenthetical, or state the fact (as a remark, unsigned unless the referees sign it). No statement depends on it.
- XI-NEW: SIGN.
  - Steps (1)-(3) are as in my pre-check §2. «ANY mover of least level» meets my XI-P2. Keys under the new state (§0) meet XI-P1.
  - «Acyclicity is not used» is right: the proof never touches Ξ beyond the availability sets. The model itself needs acyclicity for
    the values.
- RISE: SIGN.
  - (a) is the four-link chain, using MONO's current-value form.
  - (b): if Z_t = ∅, LOCAL (a) applies to the chain under s_(t−2) and gives equal values.
  - (c): acyclicity excludes h on its own chain.
- CHAIN-BACK: SIGN.
  - (i): h_(t−1) ∈ Mv_(t−1) lies on the chain, so it is in Z_t.
  - (ii): blocks start at 1 or at an unchained step. Inside a block π(h_t) strictly decreases, so a block has ≤ N steps.
- U-EQ: SIGN WITH GAP U-1.
  - «U ≤ T − 1» is false when T = 0. Instance: any genome whose start has every A a singleton, e.g. N = 1 with deg 1: U = 0 > −1.
  - Fix: «U ≤ max(T − 1, 0)», or «for T ≥ 1».
  - The equivalence of growth classes and T ≤ N(1 + U) are unaffected.
- KEYFLIP: SIGN.
  - Between consecutive moves t1 < t2, A = {a, b} at both steps. The step rule gives KP_(s_t1) = a and KP_(s_t2) = b. The windows
    (t1, t2] are disjoint.
- KF-EQ: SIGN. T ≤ Σ moves, since every step has Mv ≠ ∅. Σ moves ≤ N + KF. KF_x ≤ T.
- DECREMENT: SIGN.
  - (b): the descendants of y_t do not move, so y's option values are equal under both states (LOCAL (b)). The new strictly-better
    set is contained in the old one minus k′.
  - (c): LOCAL (b) with s(x) = s′(x).
- EXACT-ENERGY: SIGN.
  - The lower terms change by at most Σ_(p<π(y)) (D − 1) D^p = D^π(y) − 1.
  - E is a non-negative integer, so T ≤ E(s_0) ≤ D^N − 1.
- TOP-MONO: SIGN.
  - c ∈ {0, 1} at degree ≤ 2. y_t leaves S, and S agrees above π(y_t).
  - Entry RANK_t is π(y_t) before the step and smaller (or −1) after.
- RANK-BOUND: SIGN.
  - TOP_k is non-increasing, and its non-pad entries form a subset of size ≤ k. So there are at most Σ_(j≤k) C(N, j) − 1 strict
    falls.
  - P-1 (optional): for R = 0 the «hence» clause is not an instance of the k ≥ 1 statement. It holds trivially, since RANK_t ≥ 1 makes
    𝒯 empty; the packet could say so.
- INTERVAL-RESTRICT: SIGN.
  - (i): RANK_t > k inside, so p > π(y_t) ≥ π(x) for every mover of the step.
  - (ii): the trimmed movers' kept option equals their option at every state of [a, b), by (i). So every chain of an untrimmed option
    is the same in G and H. A^H = A^G for π < p, and the keys are the same. The level-by-level induction is correct, and so is the
    non-stopping of H (Mv_t ≠ ∅ with |A| ≥ 2).
  - (iii): the labels read only s_(t−2), s_(t−1), s_t, which lie in [a, b) for t ≥ a + 2. The tie rule is index-based and the same in
    G and H.
  - P-2 (optional): «the first b − a states of H's run are s_a, …, s_(b−1)» identifies a trimmed mover's single option with
    s_a(x). The machine check maps it back explicitly; the text could say so.
- INTERVAL-CHARGE: SIGN.
  - There are 1 + #{RANK ≤ r − 1} intervals of constant TOP_(r−1), and every rank-r step is interior.
  - q = the r-th entry of TOP_r goes from π(y_t) to a smaller value at each rank-r step. It is unchanged at rank > r steps.
  - π(y_t) ≤ N − r, so each interval holds ≤ N − r + 1 rank-r steps.
- RECURSION: SIGN.
  - The (α)/(β)/(γ) classification covers every unchained step:
    - (α): the m − 1 boundary steps;
    - (β): ≤ 1 first step per interval with p_i ≥ 0; an interval with p_i = −1 has S = ∅, so the run stops there;
    - (γ): INTERVAL-RESTRICT (iii) maps these injectively into the unchained steps of H_i's run.
  - p_i strictly decreases and is a degree-2 position (c = 1 ⇒ deg = 2).
  - So the counts n_i := #(degree-2 movers with π < p_i) are distinct values in {0, …, n − 1}, and m − 1 ≤ n.
  - U* is finite, by EXACT-ENERGY on the degree-2 movers (degree-1 movers have c = 0 and never move), and non-decreasing by «at most
    n». So U*(n) ≤ n + Σ_(p<n) (U*(p) + 1).
  - P-3 (optional): in that sum p counts degree-2 movers; p_i is a position. Name the count n_i in the proof.
- None of §2's checks found a hole in a proof. The only false text is IR-1 (a remark) and U-1 (an edge case of one inequality).

## 3. Model and hypothesis exactness
- Each statement names its hypotheses: IDEAL-ACYC, the degree (any, or ≤ 2), and «any width». I checked that each proof uses no more.
  - KEYFLIP's and XI-NEW's «acyclicity not used» are correct.
  - The degree-≤-2 uses are c ∈ {0, 1} (TOP-MONO onward) and two options (KEYFLIP).
- The «Does NOT claim» lines agree with what is proved. One exception is IR-1, which denies a TRUE fact; that is harmless, but false.

## 4. Pre-check gaps and exclusions (re-measured, not taken from the Lead)
- XI-G1 (monotonicity proof missing in R178): CLOSED by §2 MONO, the same induction as my pre-check §3.
- XI-G2 (R178's real-N5 half): EXCLUDED.
  - §3's «Does NOT claim» (l. 115) and §9 (l. 247: «R178's real-N5 form of XI-NEW … not written here as a complete proof»).
  - No proof of the packet uses it.
- R178 (iii) (CASC-G / height): ABSENT. grep «CASC|height|R177» = 0 hits. Not used.
- XI-P1 and XI-P2: met (§0 keys «under the new state, root-first»; XI-NEW «ANY mover of least level»).

## 5. Machine check re-run at 0ebddcf5
- Command: block w99 of experiments/new/check.sh, verbatim, run in a detached worktree of 0ebddcf5 (15 s). Output:
  - `TOTAL genomes 46 runs 46 steps 386 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)`
  - `TOTAL genomes 200 runs 75518 steps 93963 XSIM 0 … VIOL 0 (info REC148 0)`
  - `TOTAL genomes 200 runs 200 steps 138 XSIM 8 TOPO 0 MONO 0 XINEW 6 RISE 3 … VIOL 17` (NEG=3 control fires)
  - All three equal the packet's §9 and the check.sh expected strings. MATCHES.
- Faithfulness of check.py, read in full: each counter tests the packet's inequality as stated.
  - MONO tests current values only, as stated.
  - RESTR builds H and maps the kept options back.
  - REC is the packet's form; REC148 is information only.
  - Not tested by check.py: U-EQ's «U ≤ T − 1» (that is where U-1 sits) and LOCAL / ENC directly. ENC is built into its simulator:
    it compares Ξ-values as integers.
- Independent simulator: docs/referee/scratch/xinew_probe.py, written from R104's TEXT. It compares β-SETS directly, not ENC's
  integers, so it also tests ENC.
  - xinew_lane.py loads the lane JSONs.
  - On the 46 corpus genomes: per-file N and T EQUAL to check.py's on all 46 (max T 26, total 386).
  - XI-NEW 0, all-option monotonicity 0, RISE strict rise 0.
  - On the 200 random genomes from their stored starts: 132 steps, 0 / 0 / 0.
  - Logs: scratch/xinew_logs/lane_corpus46.txt, lane_check150_46.txt, lane_rand200.txt.
- Limit: the runs are short (T ≤ 26). The signatures rest on the proofs, and the DATA is a consistency check.

## 6. Diff against TARGET.md
- TARGET.md §1-§3 define parity games, the regions W_E / W_O, M4 (a polynomial algorithm outputting them) and the word-RAM cost model.
  §4 and §5 cover what is not M4 and the gauntlet.
- No signed statement mentions a parity game, a winning region, an algorithm's running time or a cost model. Each is about the step
  sequence of R104's IDEAL model.
- EXACT-ENERGY's integers and ENC's 2^rk are proof devices, not computed quantities. TARGET §3 (bit cost) is not engaged.
- The only link to the fleet question is R104's own Corollary REAL-IDEAL, which this packet does not use or restate.
- Agreed with the packet's §9 diff: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## Fixes for docs/new/P-IDEAL-RED-fixes.md (via the Lead)
- IR-1 (REQUIRED): MONO's «Does NOT claim» parenthetical is false. Delete it, or replace it with: every option's value is
  non-decreasing (v = ε + cv(xt), with MONO).
- U-1 (REQUIRED for U-EQ as written): «U ≤ max(T − 1, 0)», or restrict to T ≥ 1.
- P-1, P-2, P-3: optional wording.

## DONE / FINDINGS / NEEDS
- DONE: this report; check.py re-run at 0ebddcf5 MATCHES; independent simulator EQUAL on all 46 corpus genomes.
- FINDINGS:
  - 15 statements SIGN, 1 SIGN WITH GAP (U-EQ: U-1, the T = 0 edge case).
  - IR-1: a false «does not claim» remark in MONO (every option's value IS monotone).
  - XI-G1 closed by MONO. XI-G2 and R178 (iii) are excluded and unused.
  - Premise route: R104's definition only. The TARGET diff is agreed.
- NEEDS: Lead: route IR-1 and U-1 (and optionally P-1 to P-3) to docs/new/P-IDEAL-RED-fixes.md; §C on the fixes/line when frozen.
