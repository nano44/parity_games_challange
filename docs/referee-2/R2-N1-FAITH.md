# R2-N1-FAITH: faithfulness check of L-NEW's N1 kill (deep traps on switchallexp) — REFEREE-2, 2026-10-18 18:06Z (date -u)
(Opus 5.5, D12). The Lead asked for this at 18:16Z (Lead clock). It is not a packet. Files read at claude/l-new 8ac5e5c, in a
detached worktree; my branch did not merge l-new:
- experiments/new/anneal.cpp (125 lines, read in full) and anneal.py (for the comments it ports);
- experiments/new/gen_deeptrap.sh and alltrap.py;
- docs/new/N1-KILL.md.
Sources opened (arXiv e-prints, downloaded today):
- 2402.03975 (Loff-Skomra, "Smoothed analysis of policy iteration and value iteration…"), section_algorithms.tex:
  - Fig. alg:switches: SwitchMax / SwitchMin, greedy all-switches;
  - Fig. alg:policy_iteration: DiscPI;
  - Fig. alg:increasing_discount_mpg: IncreasingDiscountPI.
- 2610.22149, arxiv_version.tex lines 1528-1600: IncreasingDiscountPI (Fig. alg:increasing_discount_mpg) and the text
  "DiscPI(σ,τ,γ) is ANY procedure that … outputs a pair of optimal policies. One way … is policy iteration equipped with
  the Howard greedy all-switches rule".
Tools are in R2-N1-FAITH/ (dualg.py, trapcheck.py).

## Verdict: FAITHFUL WITH CAVEATS (Opus 5.5, D12)
The kill is real. One caveat is material for how the dead end is worded (C1). The other two are wording only.
- C1 (material). The roles of the two players are swapped relative to 2402.03975's DiscPI figure.
  - In that figure Max best-responds in the inner loop (repeated SwitchMax) and Min makes ONE all-switch per outer step.
  - anneal.cpp has Odd best-respond in the inner loop and Even make one Howard all-switch per outer step. With rewards +n^p
    for even p, Even = Max, so anneal runs the paper's DiscPI with Max := Odd, i.e. LS on the negated game.
  - This changes the count drastically. Running LS's literal orientation on the SAME family G_N (Even best-responds by
    Howard, Odd switch-all; implemented as anneal_c --odd-howard on dual(G_N)) gives 1 outer iteration and 7, 11, 9, 11,
    13, 15 inner Howard iterations for N = 1..6, all regions verified. So on G_N the paper's orientation is NOT slow.
  - But the kill transfers by duality. LS's literal orientation on H_N := dual(G_N) (owners swapped, priorities + 1, so
    rewards −n·r) is anneal_c --odd-howard on dual(H_N), which is G_N with priorities shifted by 2: the same run. It gives
    11, 31, 71, 151, 311 outer Min switch-all iterations in ONE phase (N = 1..5), with regions verified.
  - Also, 2610.22149 §7.4 explicitly allows ANY optimal DiscPI, and anneal's orientation is "policy iteration with Howard's
    rule" for the other player, so it is a legitimate instance there.
  - Conclusion: IncreasingDiscountPI with Howard PI is exponential in EITHER orientation, on G_N for anneal's orientation and
    on dual(G_N) for the paper's literal one. The dead end should name both families, or state the orientation.
- C2 (wording). The general claim "the parity-certificate stop fires no later than LS's mean-payoff-optimality test" is not
  proved, and I do not believe it in general (§1.5). It is not needed: on this family LS's test cannot fire before the release
  phase (§1.5), which is all the kill uses.
- C3 (wording). N1-KILL.md's 5·2^(N+1) − 9 fits N = 1..6 (11, 31, 71, 151, 311, 631; I reproduced N = 1..5 exactly).
  N = 7's 1244 is not 1271, so the closed form is a fit to N ≤ 6, and the growth claim ~2^N is what stands.

## 1. anneal.cpp against the papers' pseudocode
1.1 Discount schedule. LS: γ ← 0; repeat γ ← (1+γ)/2, so γ_j = 1 − 2^(−j), j = 1, 2, … anneal: j from j0 = 1 (default) with
γ = (2^j − 1)/2^j (lines 33, 98). MATCHES.

1.2 Warm start. LS passes (σ, τ) from one DiscPI call to the next. anneal keeps sigma and tau across the j loop (92, 98-113),
and the initial pair is arbitrary in LS ("any initial policies"). MATCHES.
- Start: Even's highest-reward successor (93-95), which on G_N is the trap at every Even choice vertex; Odd's first successor.

1.3 Even's update. LS SwitchMax: at every Max vertex whose value is not the max of (1−γ)r_ij + γ x_j, switch to an argmax
("any state in argmax").
- anneal 110-112 does exactly this. Rewards sit on vertices, so r_ij = r_i is constant over i's choices and argmax over j
  of x_j is the same set. It switches only on a strict improvement, with ties broken by smallest index. Values are exact
  (cpp_int, 32-54). Scaling x by Q and dropping (1−γ) does not change any comparison.
- MATCHES for the improving player, in anneal's orientation (C1).

1.4 Odd's best response. LS: inner repeated SwitchMin, Howard. anneal: by default Dantzig single switches until no improving
Odd switch (103-106), i.e. an exact best response; --odd-howard gives LS's Howard (107).
- For a fixed σ the optimal one-player values are unique, and Even's switches read only those values. So the inner method
  cannot change Even's sequence. Data: G_3 gives 71 Even iterations with either inner rule.
- MATCHES in effect. Only the inner count differs, and it is not the counted quantity.

1.5 Stopping test. LS 2402.03975: stop when (value, Blackwell bias) solves the ergodic equation; 2610.22149: stop when (σ, τ)
is optimal in the mean-payoff game. Both tests are applied after DiscPI completes a phase. anneal: after each phase, win =
sign of the discounted values, plus a full parity certificate of both strategies (115-116, 78-85).
- On G_N, LS cannot stop before the release phase. Before release σ = all traps (no Even switch occurs before it; one
  nonzero phase). A trap's mean payoff is −n^q with q = B+1. Every vertex's mean-payoff value in the original game is a
  cycle mean ≥ −n^B > −n^q, and adding losing traps does not change Even's value. So σ = all traps is not mean-payoff
  optimal, and LS's test fails at every pre-release phase. The release phase is then run to completion by both versions.
- So on this family LS executes the same exponential phase. Its total is at least anneal's count, since the switches LS
  counts are ≥ the rounds anneal counts.
- The general claim (C2) can fail. A mean-payoff-optimal pair can have a discounted value whose sign differs from the
  mean-payoff winner while 1/(1−γ) is below n^(p_path − p_cycle). anneal's certificate would then fire LATER than LS's test,
  so "no later" is not right in general. It is not used.

## 2. Count semantics — CORRECT
- ev/ph count Even all-switch ROUNDS that change at least one vertex (113). There is one per outer iteration of DiscPI, inside
  the phase j (per[] at 114, printed as nonzero=[…]).
- Each round needs one exact evaluation of all n values (values(), 32-54). So the count is a lower bound on work, and bit cost
  only adds.
- LS counts switches, and switches ≥ rounds, so the reported numbers are lower bounds on LS's switch count in this orientation.
- Reproduced: N = 1..5 give 11 / 31 / 71 / 151 / 311, each in ONE phase (nonzero=[k]), at phases 184 / 309 / 442 / 580 / 723.
  This matches deeptrap_sae.csv. The N = 3 solution is verified by check_sol2.py (oink zlk + harness/verify.py).

## 3. Generator — CORRECT
- gen_deeptrap.sh N: switchallexp(N) from pgsolver_port.py (REFEREE-checked earlier, per the Lead), then alltrap.py with
  k = ⌊B_max/2⌋ + 2.
- The output sha1 for N = 1..4 equals the pinned deeptrap_sae_N*.pg (f44eeb9c656e, 99c96a0d913e, 594d25f5c9f4,
  8f6af4677bf0).
- My trapcheck.py compares G_N with switchallexp(N) vertex by vertex. Results for N = 1, 2, 3:
  - every original vertex keeps its priority, owner and successors;
  - every Even vertex with ≥ 2 successors gains exactly one successor t_v (13 / 22 / 31 traps);
  - t_v is Odd, of even priority P = B + 2 + 2k (62 / 94 / 126), with the single successor c_v;
  - c_v is Odd, of odd priority q = B + 1 (29 / 45 / 61), with only a self-loop;
  - no other edge is added;
  - n = 21 + 2·13 = 47, 35 + 44 = 79, 49 + 62 = 111;
  - B = max priority rounded up to even.
  So the traps are as described, and P − q = 2k + 1 > B + 2.

## 4. Data of this check
| N | G_N anneal (Even outer) | G_N, LS literal (dual + --odd-howard): outer / inner | dual(G_N), LS literal: outer Min switch-alls |
|---|---|---|---|
| 1 | 11 | 1 / 7 | 11 |
| 2 | 31 | 1 / 11 | 31 |
| 3 | 71 | 1 / 9 | 71 |
| 4 | 151 | 1 / 11 | 151 |
| 5 | 311 | 1 / 13 | 311 |
| 6 | 631 (L-NEW) | 1 / 15 | — |
- All counts are in one phase. Solutions were verified by check_sol2.py on G_3, dual(G_3), dual(G_6) and dual(dual(G_5)).
- dual(G_N) sha1 prefixes, N = 1..6: b8b7734f4ec0, 26627f7bee34, 441e794ddea1, a958f4afcf62, c6f737b15342, 87d895754cca
  (R2-N1-FAITH/dualg.py).
