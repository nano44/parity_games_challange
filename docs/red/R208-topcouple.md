# R208 Top level with Ξ-couplings: Lemma TOP-SPLIT (proved, lane) and the gain-per-coupling attack (L-RED successor 50)
Started 2026-11-06 00:2xZ (date -u). Lead BOX R208 (00:15Z): (1) generalise TOP-ADD to «gain ≤ 2 + c·(#Ξ-couplings into the top)»,
state it precisely and try to prove it from SEG-ONCE + RENEW; (2) attack it with top extensions of the best d − 1 witnesses that
maximise gain per coupling.
Model: IDEAL-ACYC (RESULTS R104), degree ≤ 2, 𝓛_d with one-option helpers (R109). Labels: PROVED (lane, unrefereed), DATA, CONJECTURE,
READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answers
- (1) Precise form.
  - Setting: G has top level τ and top movers U. A COUPLING is a lower option (x, k) with Ξ-target in U; C is the number of couplings
    (every lower Ξ-chain that reaches U does so through a coupling).
  - The naive gain T(G) − T(G with U deleted and each coupling sent to X) is useless. Re-routing one option to X can wreck the lower
    run (DATA: gain_x 26 with C = 1, because T drops to 2).
  - Robust gain: gain′(G) := T(G) − max over all re-routings r of T(G^-_r), where r sends each coupling to X or to any lower mover
    (keeping acyclicity) and G^-_r deletes U. This compares G with the best (d − 1)-level genome that differs only at the coupled
    options.
  - CONJECTURE TOP-C: gain′(G) ≤ 2 + C. TOP-ADD is the case C = 0 (gain′ ≤ 2, PROVED).
- (1) Proof status: NOT proved. What I can prove is Lemma TOP-SPLIT (§1). It is multiplicative, not additive:
  T(G) ≤ (m + 1)·T*(d − 1) + m, with m := #steps that move a top mover.
  - Between two top moves the lower part runs exactly as one (d − 1)-level genome L_q with proxy helpers. Each top move can therefore
    re-arm a fresh lower run.
  - An additive 2 + C bound needs a reason why a re-armed lower run is short. SEG-ONCE does not give one: it bounds moves of the level
    just above a frozen block, which here is the top, not the lower levels.
  - RENEW / CHARGE-I (L-NEW P-IDEAL-KEYS §5, box 174) bound the number I of top-only blocks, not the lower steps that follow a top move.
    So the route «SEG-ONCE + RENEW» stops at TOP-SPLIT. The missing piece is exactly SLOT-TRADE's (a re-armed run is short).
- (2) Attack. Climbs over top extensions of fixed d − 1 witnesses (the base is never changed; C couplings placed freely):

  | base (d − 1, T) | C | best T(G) | best lower re-routing | gain′ | T(G) − T(base) |
  | --- | --- | --- | --- | --- | --- |
  | Tstar_d5_T17 (5, 17) | 1 | 20 | 17 | 3 | 3 |
  | Tstar_d6_T25 (6, 25) | 1 | 28 | 25 | 3 | 3 |
  | Tstar_d7_T31 (7, 31) | 1 | 34 | 31 | 3 | 3 |
  | Tstar_d9_T42 (9, 42) | 1 | 44 | 42 | 2 | 2 |
  | Tstar_d5_T17 (5, 17) | 2 | 21 | 17 | 4 | 4 |
  | Tstar_d6_T25 (6, 25) | 2 | 29 | 25 | 4 | 4 |
  | Tstar_d5_T17 (5, 17) | 3 | 21 | ≥ 17 (base routing) | ≤ 4 | 4 |
  | Tstar_d6_T25 (6, 25) | 3 | 29 | ≥ 25 (base routing) | ≤ 4 | 4 |
  | Tstar_d7_T31 (7, 31), long climb (60k) | 1 | 34 | ≥ 31 (base routing) | ≤ 3 | 3 |
  - Bound rows: for C = 3, and the long C = 1 climb (climbed on T, GAIN=t), only gain′ ≤ T(G) − T(base) is stated (the base routing is
    one of the re-routings). The exhaustive re-routing was not run there.  - DATA: gain′ = 2 + C at C = 1, 2 (3 and 4; the d 9 row stopped at 2 after a short climb). gain′ ≤ 4 < 2 + 3 at C = 3. It does not grow with T(d − 1) from 17 to 31 at fixed C.
  - No kill of TOP-C. Labels: the bases are R207 champions, so only extensions of near-extremal genomes were tried; climbs are
    heuristic.

## 1. Lemma TOP-SPLIT (PROVED, lane; unrefereed)
Statement.
- Setting: G is IDEAL-ACYC of degree ≤ 2 with top level τ ≥ 1, U the top movers, and any couplings. The run is s_0, …, s_T. A SEGMENT
  is a maximal interval of steps between consecutive steps that move a top mover. Its first state s_a is s_0 or the state after a
  top-moving step, and its last step is the next top-moving step (or T).
- L_q: the genome on the lower movers in which every coupled Ξ-target u ∈ U is replaced by a proxy. The proxy is a new level-0
  one-option mover whose option has u's current option's β (same rank and parity) and u's current option's Ξ-target; one proxy per top
  mover. L_q is in 𝓛_(d−1).
- Claim: through the segment's last step inclusive, the lower parts of G's states are the states of the run of L_q from the lower part
  of s_a, kept constant after that run stops.
- Hence #(steps of the segment that move a lower mover) ≤ T(L_q from s_a) ≤ T*(d − 1), and T(G) ≤ (m + 1)·T*(d − 1) + m, with
  m = #top-moving steps ≤ Σ_(u ∈ U) moves(u).
Proof.
- Keys. The key of a lower mover uses only its W-chain, which lies below τ. The keys are the same in G and in L_q, and proxies have no
  W-role.
- Values. Inside a segment, before its last step, the top state is constant (= s_a on U). The Ξ-chain of a lower option in G, read
  from s_(t−1), passes the top only through couplings (x, k) → u, and then continues with u's option s_a(u) and its chain. That chain
  is exactly the chain of (x, k) → proxy in L_q: the same β-sets, so the same values and the same availability.
- The step rule computes the lower part of s_t from availability under s_(t−1) and keys under the new lower state. So it agrees with
  L_q's step, including at the segment's last step, where only the top's own choice differs.
- Stopping: if L_q's run stops (nothing available, or no change), G's lower part does not move until the top moves. ∎
- DATA check (r208/split_ck.py, random coupled extensions of Tstar_d5_T17 (C = 1, 3) and max_d5_L15 (C = 2)): 957 segments, 0
  violations. Max lower steps in a segment: 17 and 15 = the base T.

## 2. Reading (where TOP-C would come from, and why it is SLOT-TRADE again)
- TOP-SPLIT reduces T(G) to how far each top move can re-arm the lower genome. A top move changes L_q only at the coupled options
  (their proxies' β and Ξ-targets). So a re-armed run is a run of a genome that differs from the old one at C options, from a state
  where the old one was stuck or running.
- TOP-C says such a change buys at most about one step per coupling. That is the «one bit buys O(1)» half of SLOT-TRADE. At the
  bottom (level-0 bit, R110 W-ONLY / T_2), the champions DO buy far more: Tstar_d6_T25 replays 11 steps after its level-0 flip. At the
  top, in the climbs, they do not.
- Asymmetry (READING): a level-0 flip changes the KEYS of the whole level 1 (W side). A top coupling changes only VALUES of C
  options (Ξ side), and a value change at x re-arms only x and its Ξ-ancestors.

## 3. Files (experiments/red/r208/)
- coupext.py (climber; GAIN=best | t | x); gain.py (gain_x, gain′ of a file); split_ck.py (TOP-SPLIT check).
- keep/: best extension per row. All 9 replayed: box166/verify_kill.py well-formed and acyclic; box150/check.py XSIM and every
  counter 0. Climb logs in out/ (not committed).
