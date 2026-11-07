# R2-P-IDEAL-RED: REFEREE-2 report on P-IDEAL-RED (L-NEW 50, box 150): ENC, LOCAL, MONO, XI-NEW, RISE, CHAIN-BACK, U-EQ, KEYFLIP, KF-EQ, DECREMENT, EXACT-ENERGY, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE, RECURSION
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-03 (date -u; see the commit). Owner D19 / Lead reading L47.
Independence:
- I opened nothing in docs/referee/. At 20:46Z, a names-only `git ls-tree` on origin/claude/referee found 0 files matching this packet.
- My checker imports no lane code. I opened the lane's box150/check.py only for its header and genome loader, and ran it as a
  subprocess.

## 0. Object and premise route
- Packet: docs/new/P-IDEAL-RED.md at claude/l-new 0ebddcf5bc4f11fedd18b5cefffc78ff90464be9. sha1 06f2c18609e355a1e62c138c420bd49dc401cae4,
  261 lines. Re-hashed: match.
- **Premise route ✓.** The only premise is RESULTS R104's DEFINITION of the IDEAL model and the Ξ-graph.
  - I compared §0 with trunk RESULTS R104's landed text (l. 9864): «a W-target of level lev(x) − 1 (none at level 0), a Ξ-target
    xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and a start; … compared by the β of largest
    rank in the symmetric difference: … better … if its parity is even …; an IDEAL step moves every mover to the lexicographically least
    key (… under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the
    run stops when nothing is available or nothing changes».
  - §0 restates exactly this. Two additions are not R104 data but harmless: a topological order π, and the tie rule for h_t. Every
    statement is claimed for every π and every fixed tie rule, and my checker tests several π and both tie rules.
  - No theorem of R104 is used. No other RESULTS entry is used. Nothing comes from docs/lit, docs/sources or a lane file. R178's XI-NEW
    is re-proved in full (§3), and N5-IDEAL-STATE is named only for EXCLUDED items and conjecture labels.
  - The C115 E-1 lesson is respected.
- **TARGET.md diff ✓.**
  - TARGET.md §1-§3 are about parity games, winning regions, algorithms, the word-RAM running time and M4. §4 and §7 cover M3.
  - Every statement here is about the step sequence of the IDEAL model only.
  - None mentions a parity game, a region or a running time, and none bounds anything polynomially.
  - So nothing is an M3 / M4 claim or a gauntlet step. The packet's own §9 diff is correct. G-N5-TIME stays OPEN.

## 1. Verdict table
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma ENC | **SIGN** |
| §1 | Lemma LOCAL (a)-(c) | **SIGN** |
| §2 | Lemma MONO | **SIGN** |
| §3 | Lemma XI-NEW | **SIGN** (acyclicity indeed unused) |
| §3 | Corollary RISE (a)-(c) | **SIGN** |
| §4 | Theorem CHAIN-BACK (i), (ii) | **SIGN** |
| §4 | Corollary U-EQ | **SIGN** with precision N-1 («U ≤ T − 1» is false at T = 0; read max(T − 1, 0); the equivalence is unaffected) |
| §5 | Lemma KEYFLIP (degree ≤ 2) | **SIGN** |
| §5 | Corollary KF-EQ (degree ≤ 2) | **SIGN** |
| §6 | Lemma DECREMENT (a)-(c) | **SIGN** |
| §6 | Corollary EXACT-ENERGY | **SIGN** (D ≥ 2 as stated; D = 1 gives T = 0 trivially) |
| §7 | Corollary TOP-MONO (degree ≤ 2) | **SIGN** |
| §7 | Corollary RANK-BOUND (degree ≤ 2) | **SIGN** |
| §8 | Lemma INTERVAL-RESTRICT (i)-(iii) (degree ≤ 2) | **SIGN** |
| §8 | Corollary INTERVAL-CHARGE (degree ≤ 2) | **SIGN** |
| §8 | Corollary RECURSION (degree ≤ 2), all three bullets | **SIGN** |
| §9 | DATA, exclusions, TARGET diff (not to sign) | DATA reproduced exactly (§4); exclusions and labels ✓ |

No gap. One precision (N-1), two notes (N-2, N-3).

## 2. Paper check, statement by statement
- **ENC.**
  - The ranks of all options are distinct, so the elements of P △ Q other than β* have distinct ranks < r*.
  - Their total is at most 2^(r*) − 1 < 2^(r*), so β*'s term decides. That matches the definition's parity rule.
  - The recursion v = ε + v(y, s(y)) holds because the chain of (x, k) is (x, k) followed by the chain of (y, s(y)), and x is not on
    the latter (acyclic). ✓
- **LOCAL.**
  - (a) Induction along the chain.
  - (b) Every mover after x on a chain of an option of x is a strict Ξ-descendant.
  - (c) The key reads s only below lev(x), by induction on the level. ✓
- **MONO.**
  - Induction in decreasing π. k′ = s_t(x) ∈ A_(s_(t−1))(x) for EVERY mover, moved or not.
  - If xt = X the value is unchanged. Otherwise π(y) > π(x), so the inductive hypothesis applies to y.
  - The maximum-π mover has xt = X on all options (no y with larger π), so the base case is inside the same argument. ✓
- **XI-NEW.**
  - (1) h has least level in Mv_t, so levels < lev(h) are fixed at step t and its keys are equal under s_(t−1) and s_t.
  - (2) Step t − 1 exists (t ≥ 2). The step rule picks every mover's option, moved or not, so o = s_(t−1)(h) is key_(s_(t−1))-least
    in A_(s_(t−2))(h).
  - (3) o ∈ A_(s_(t−1))(h) (the current option is always available), and step t picks w ≠ o as key_(s_t)-least. This contradicts (1)
    and (2) if w ∈ A_(s_(t−2))(h). ✓
  - It holds for ANY least-level h, and acyclicity is not used.
- **RISE.**
  - w ∉ A_(s_(t−2))(h) gives w ≠ s_(t−2)(h) and v ≤ cv (ENC: total order).
  - The chain v_(t−1)(h, w) > cv_(t−1)(h) ≥ cv_(t−2)(h) ≥ v_(t−2)(h, w) uses MONO at step t − 1, and is strict. That is (a).
  - (b) by LOCAL (a) with s = s_(t−2), s′ = s_(t−1). The first option (h, w) is the same in both, so h ∈ Mv_(t−1) does not matter.
  - (c) acyclicity. ✓
- **CHAIN-BACK.**
  - (i) A chained step puts h_(t−1) (∈ Mv_(t−1)) on the chain of (h_t, s_t(h_t)) under s_(t−2), other than h_t. That is Z_t with
    h = h_t, so RISE (c) applies.
  - (ii) The maximal chained blocks partition [1, T]. Each block starts at 1 or at an unchained step, so there are ≤ 1 + U blocks.
    π strictly falls inside a block, so each block has ≤ N steps. ✓
- **U-EQ.**
  - U ≤ T − 1 for T ≥ 1. At T = 0, U = 0 > −1: precision N-1.
  - The growth-class equivalence holds: U ≤ max(T − 1, 0), and T ≤ N(1 + U).
- **KEYFLIP.**
  - With two options, consecutive moves go b → a at t1 and a → b at t2.
  - At t1, A = {a, b} and the rule takes the key_(s_(t1))-smaller, so KP_(s_(t1)) = a. At t2, KP_(s_(t2)) = b. So KP flips in
    (t1, t2].
  - The windows are disjoint. The bound also holds trivially for moves(x) = 0.
  - Only deg(x) = 2 of the moving mover is used. My checker tests it for every degree-2 mover in EVERY genome: 0 violations. ✓
- **KF-EQ.**
  - T ≤ Σ moves (each step has Mv_t ≠ ∅) ≤ Σ (1 + KF_x) ≤ N + KF.
  - KF ≤ N·T. ✓
- **DECREMENT.**
  - (a) is immediate.
  - (b) The strict descendants of y_t have π > π(y_t), so they are not in Mv_t, and LOCAL (b) fixes all of y_t's option values.
    v(k′) > v(k_old) in a total order, so {k : v(k) > v(k′)} ⊆ {k : v(k) > v(k_old)} \ {k′}, and c falls by ≥ 1.
  - (c) as stated, with c = |A| − 1 = the number of strictly better options. ✓
- **EXACT-ENERGY.**
  - Higher terms are unchanged (DECREMENT (c)). The y_t term falls by ≥ D^π(y_t).
  - The lower terms change by at most Σ_(p < π(y)) (D − 1) D^p = D^π(y) − 1, since 0 ≤ c ≤ D − 1.
  - So E strictly falls. E < D^N, so T ≤ E(s_0) ≤ D^N − 1. ✓
- **TOP-MONO.**
  - Degree ≤ 2 gives c ∈ {0, 1}. DECREMENT gives y_t ∈ S(s_(t−1)) \ S(s_t), and S is the same above π(y_t).
  - RANK_t > k: the top k entries both come from Hi.
  - RANK_t ≤ k: entry RANK_t falls from π(y_t) to something smaller. Newly unstable movers all have π < π(y_t).
  - ✓
- **RANK-BOUND.**
  - TOP_k is non-increasing, and falls exactly at the steps with RANK_t ≤ k.
  - Its values correspond to subsets of size ≤ k, so there are ≤ Σ_(j ≤ k) C(N, j) values, and the number of falls is that minus 1.
  - The U form uses k = R, the largest RANK over the unchained steps. R = 0 ⇒ U = 0. ✓
- **INTERVAL-RESTRICT.**
  - (i) Inside the interval TOP_k is constant, so RANK_t > k: at least k unstable movers lie above π(y_t), and the k-th entry
    p > π(y_t). The p = −1 case is vacuous, which also forces b ≤ a + 1.
  - (ii) Trimmed movers do not move during steps a + 1 … b − 1, by (i).
    - So for every j in range, s_(a+j) agrees with s_a on them. Every chain under s_(a+j) uses only kept options, so values and A agree
      for untrimmed movers, and A^H = {s(x)} for trimmed ones.
    - Keys agree.
    - H does not stop: a moving mover has |A^H| = |A^G| ≥ 2. The level-by-level choice agrees.
    - Validity of H: Ξ-subgraph, same levels and W-targets, distinct ranks and gates. ✓
  - (iii) The label reads only s_(t−2), s_(t−1), s_t with t − 2 ≥ a, plus a chain that uses only kept options. ✓
- **INTERVAL-CHARGE.**
  - The TOP_(r−1)-constant intervals number 1 + #{RANK ≤ r − 1}. A rank-r step has t − 1 and t in the same interval.
  - Inside an interval, q = the r-th entry of TOP_r strictly falls at the rank-r steps (the first r − 1 entries are fixed: TOP-MONO's
    proof), and is unchanged at RANK > r.
  - π(y_t) = q(s_(t−1)) ∈ {0, …, N − r}, so there are ≤ N − r + 1 such steps per interval. ✓
- **RECURSION.**
  - Every step t ∈ [2, T] is (α) an interval boundary (≤ m − 1), or (β) the first step inside an interval, or (γ) a later step inside
    one. (γ) is labelled exactly as step t − a_i of H_i (INTERVAL-RESTRICT (iii), k = 1) and is counted in U(H_i).
  - An interval with p_i = −1 has S = ∅, so the run stops there: it is the last interval and has no step inside.
  - p_i strictly decreases. Each p_i ≥ 0 is the position of an unstable mover, hence of degree 2.
  - H_i's degree-2 movers are those with π < p_i. Their number d_i strictly decreases with i and lies in {0, …, n − 1}, so m − 1 ≤ n and
    U(H_i) ≤ U*(d_i).
  - U* is finite: EXACT-ENERGY over the degree-2 movers alone (degree-1 movers have c = 0) gives T < 2^n uniformly in N.
  - So U*(n) ≤ n + Σ_(p < n) (U*(p) + 1). ✓
  - The note that box 148's form (without (α)) is NOT claimed is correct and honest.

## 3. Precision and notes
- **N-1 (precision, U-EQ).** «U ≤ T − 1» fails at T = 0 (U = 0). Read «U ≤ max(T − 1, 0)» or «for T ≥ 1». The equivalence is
  unaffected.
- **N-2 (note).** Degree ≤ 2 is needed where stated. On degree ≥ 3 genomes my checker counts:
  - the KEYFLIP inequality with KP := the key-least option failing: X_KEYFLIP_deg3, 35 on the 7 R178 champions (degree 3), 2,473 on the
    lane's all-start runs, 696 on mine;
  - TOP-MONO failing: X_TOP_deg3, 21 / 78,579 / 23,151.
  This confirms the §5 remark and the §9 exclusion of box 147's degree-D TOP forms. ENC, LOCAL, MONO, XI-NEW, RISE, CHAIN-BACK,
  DECREMENT and EXACT-ENERGY hold at every degree there: 0 violations.
- **N-3 (note).** «Every statement holds for every such π» and «any fixed tie rule works» are borne out: every π-dependent check runs
  under 3 random topological orders per genome, and CHAIN under both the min- and max-index tie rules. 0 violations.

## 4. Data
- **My checker:** docs/referee-2/R2-P-IDEAL-RED/ideal_check.py; logs in logs/run1.log and run2.log.
  - It is written from the packet text. Ξ-values are SETS, compared by the top-rank β (ENC checked separately against the integers).
    Keys are read under the new state.
  - INTERVAL-RESTRICT builds H and runs it, for every k and every maximal TOP_k interval, and compares states and labels.

| input | genomes | runs | steps | restricted intervals run | violations |
| --- | --- | --- | --- | --- | --- |
| corpus of boxes 140-149 (the 46 files the w99 block uses) | 46 | 46 | 386 | 15,699 | 0 |
| 7 R178 champions (degree 3; L 17-64) | 7 | 7 | 296 | — (degree 3) | 0 |
| lane box150/out/rand, every start for N ≤ 9 | 200 | 74,495 | 92,837 | 40,522 | 0 |
| my random, degree ≤ 2, every start (N ≤ 8, depth ≤ 4, ranks / gates distinct naturals with gaps) | 300 | 2,758 | 1,889 | 87,995 | 0 |
| my random, degree ≤ 4, every start (N ≤ 7, depth ≤ 3) | 200 | 33,104 | 34,819 | 439 | 0 |

- **Control** NEG=old (keys under the OLD state): XINEW fires, 6 on the lane's 200 random genomes (default starts) and 85 on the corpus.
- **The lane's own check at 0ebddcf5** (worktree; the exact w99 commands), all as §9 and the check.sh strings state:
  - corpus: «TOTAL genomes 46 runs 46 steps 386 … VIOL 0 (info REC148 0)»;
  - ALL=1: «TOTAL genomes 200 runs 75518 steps 93963 … VIOL 0»;
  - NEG=3: «XSIM 8 … XINEW 6 RISE 3 … VIOL 17»;
  - also NEG=1 (XSIM 168) and NEG=2 (MONO 93, DECR 66, TOPMONO 101, RESTR 5) fire.
  - My ALL run has 74,495 runs against the lane's 75,518, because my all-start cap is N ≤ 9 (ALLN) and the lane's is N ≤ 10.
- **D18 labels.**
  - Every signed statement: PROVED inside the IDEAL-ACYC model (refereed by me; the second referee is pending).
  - CONJECTURE U-LIN etc.: OPEN, excluded.
  - G-N5-TIME: OPEN.

## DONE / FINDINGS / NEEDS
- DONE: all 16 statements SIGNED (U-EQ with precision N-1). The premise route is R104's definition only. The TARGET diff is clean. The
  lane's §9 DATA is reproduced exactly. My own checker gives 0 violations on 110,410 runs, and its control fires.
- FINDINGS:
  - No gap.
  - N-1: U ≤ T − 1 fails at T = 0.
  - The degree ≤ 2 hypotheses are necessary: KEYFLIP and TOP-MONO fail at degree 3 on the champions.
- NEEDS: L-NEW: an optional fixes line for N-1.
