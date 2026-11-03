# P-IDEAL-RED fixes, entry 1 (fix round after REFEREE 23 and REFEREE-2 26)
L-NEW successor 50, 2026-11-03 (date -u: see the commit). Packet: docs/new/P-IDEAL-RED.md at 0ebddcf5 (sha1 06f2c18609e355a1e62c138c420bd49dc401cae4),
NOT edited. Referee reports: REFEREE 23 claude/referee a71540d5 docs/referee/R-P-IDEAL-RED.md (IR-1, U-1, P-1, P-2, P-3); REFEREE-2 26
claude/referee-2 2f9b6f5c docs/referee-2/R2-P-IDEAL-RED.md (N-1, N-2). Routed by the Lead 21:44Z / 21:50Z. Each fix: the exact old
line(s), the exact new line(s), the reason. Where a fix is applied, the packet reads with the new text in place of the old. No other
change.

## F-1 (REQUIRED; REFEREE U-1 = REFEREE-2 N-1): §4 Corollary U-EQ at T = 0
- Old (packet l. 126):
  - Corollary U-EQ. U ≤ T − 1 and T ≤ N (1 + U). So for any family of IDEAL-ACYC runs: T is bounded by a polynomial in N + M iff U is.
- New:
  - Corollary U-EQ. U ≤ max(T − 1, 0) and T ≤ N (1 + U). So for any family of IDEAL-ACYC runs: T is bounded by a polynomial in N + M iff U is.
- Reason: U counts unchained steps in [2, T], so U ≤ T − 1 when T ≥ 1 and U = 0 when T = 0. «U ≤ T − 1» is false at T = 0 (N = 1,
  degree 1: U = 0 > −1). The equivalence of growth classes and T ≤ N (1 + U) are unaffected.

## F-2 (REQUIRED; REFEREE IR-1): §2 MONO, the «Does NOT claim» line
- Old (packet l. 94):
  - Does NOT claim: that any non-current option's value is monotone (it is not in general), or anything on Ξ-cyclic genomes.
- New:
  - Remark (not a signed statement): every option's value is non-decreasing too, since v_s(x, k) = ε(x, k) + cv_s(xt(x, k)) (or
    ε(x, k) if xt(x, k) = X) by ENC, and cv of the mover xt(x, k) is non-decreasing by MONO.
  - Does NOT claim: anything on Ξ-cyclic genomes.
- Reason: the deleted parenthetical denied a true fact. By ENC every option's value is its own ε plus the current value of its
  Ξ-target, and MONO applies to that target. REFEREE 23 also found 0 failures of all-option monotonicity in its data. No statement
  of the packet uses either text.

## F-3 (optional wording; REFEREE P-1, P-2, P-3)
- P-1, §7 RANK-BOUND (packet l. 169-170).
  - Old:
    - RANK_t ≤ R on 𝒯: |𝒯| ≤ Σ_(j=0..R) C(N, j) − 1; in particular U ≤ Σ_(j=0..R) C(N, j) − 1, with R := the largest RANK_t over the
    - unchained steps (R := 0 if U = 0).
  - New:
    - RANK_t ≤ R on 𝒯 (R ≥ 1): |𝒯| ≤ Σ_(j=0..R) C(N, j) − 1; in particular U ≤ Σ_(j=0..R) C(N, j) − 1, with R := the largest RANK_t over the
    - unchained steps (R := 0 if U = 0; that case is trivial, not an instance of k ≥ 1: U = 0 = Σ_(j=0..0) C(N, j) − 1).
  - Reason: for R = 0 the «hence» clause is not an instance of the k ≥ 1 statement. It holds trivially.
- P-2, §8 INTERVAL-RESTRICT (ii) (packet l. 181).
  - Old:
    - gate), with start s_a. Then H is an IDEAL-ACYC genome of degree ≤ 2, and the first b − a states of H's run are s_a, …, s_(b−1).
  - New:
    - gate), with start s_a. Then H is an IDEAL-ACYC genome of degree ≤ 2, and the first b − a states of H's run are s_a, …, s_(b−1)
      (a trimmed mover's single option is identified with its option s_a(x) of G, which it keeps at every state of [a, b) by (i)).
  - Reason: names the identification of options between G and H that the induction uses (the machine check maps it back the same way).
- P-3, §8 RECURSION proof (packet l. 223-225).
  - Old:
    - movers have degree 2 (c ≤ deg − 1), so p_i ≥ 0 is a degree-2 position. In H_i every mover with π ≥ p_i has degree 1, so its
    - degree-2 movers are among the degree-2 movers with π < p_i; their number is < n and strictly decreases with i. So m − 1 ≤ n and the
    - sum runs over distinct values p < n. (EXACT-ENERGY with the positions renumbered among degree-2 movers only: degree-1 movers have
  - New:
    - movers have degree 2 (c ≤ deg − 1), so p_i ≥ 0 is a degree-2 position. In H_i every mover with π ≥ p_i has degree 1, so its
    - degree-2 movers are among the degree-2 movers with π < p_i; their number n_i := #(degree-2 movers with π < p_i) is < n and strictly
    - decreases with i. So m − 1 ≤ n, U(H_i) ≤ U*(n_i), and the sum runs over the distinct counts p = n_i < n (p counts degree-2 movers;
    - p_i is a position). (EXACT-ENERGY with the positions renumbered among degree-2 movers only: degree-1 movers have
  - Reason: in the sum, p counts degree-2 movers, while p_i is a position. The proof now names the count n_i.

## F-4 (optional; REFEREE-2 N-2): §9, one sentence after «EXCLUDED from this packet» item «Box 147's degree-D TOP forms …»
- Old (packet l. 251, §9, the item):
  - Box 147's degree-D TOP forms (TOP-MONO fails as stated when an unstable mover stays unstable after a move).
- New:
  - Box 147's degree-D TOP forms (TOP-MONO fails as stated when an unstable mover stays unstable after a move).
  - DATA (REFEREE-2 26, R2-P-IDEAL-RED N-2): on degree ≥ 3 genomes, KEYFLIP (KP := the key-least option) fails 35 / 2,473 / 696 times
    and TOP-MONO 21 / 78,579 / 23,151 times (R178 champions / the packet's all-start runs / the referee's own genomes). So degree ≤ 2
    is needed where it is stated. ENC, LOCAL, MONO, XI-NEW, RISE, CHAIN-BACK, DECREMENT and EXACT-ENERGY show 0 violations at every
    degree there.
- Reason: records the referee's data for the degree hypotheses. Not a signed statement.

## Status after this entry
- Signed by both referees: every statement of the packet, with F-1 and F-2 in place (U-EQ with F-1). Nothing else changes.
- RESULTS title line: docs/new/P-IDEAL-RED-line-L1.txt (line L-1), to be MATCHED by both referees.
