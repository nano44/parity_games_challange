# R192 High-rank unchained steps (L-NEW box 147 RANK) in IDEAL-ACYC ladders: no super-polynomial family; high rank is CHEAP (almost every unchained step of a U-climb has RANK ≥ 3), so the count of high-rank unchained steps is limited by U itself, and it grows LINEARLY in d at k = 2, 3, 4, degree 2 and 3, also when frozen padding is excluded (L-RED successor 46)
Started 2026-11-02 13:39Z (Lead item 12:51Z, queued after R191; date -u). Brief: «R192: a family with super-polynomially many
freeze/release events of READY movers … Target: an acyclic IDEAL genome where high-rank unchained steps recur super-polynomially.
Equivalently, the W-side freezes and releases of ready movers above the least mover compound. Score: the number of unchained steps with
RANK > k, for k = 2, 3, 4, against d. Realise any candidate with the REALIZE gadgets.»
Labels: DATA, READING, OPEN. Definitions from L-NEW box 147 (claude/l-new 5c93eaf8, docs/new/N5-COARSE-box147.md §0-§1, read, not used
as a premise): π = a topological order of the Ξ-graph (the genome's π), y_t = the max-π mover of step t, UNST(x) = x has an option with
a strictly better face, RANK_t = 1 + #{x unstable at s_(t−1), π(x) > π(y_t)}; unchained = box 144 (all least movers). Model: IDEAL-ACYC
width-2 ladders of degree D (r190/delclimb format). Not a TARGET.md claim. G-N5-TIME OPEN. No kill, no family.

## 0. Answer
- No family. Climbs maximising HIGH_k := #{unchained t : RANK_t > k} (r192/rkclimb.py, 60,000 mutations; seeds 1-2) give, at width 2:

| d | D 2: k 2 / k 3 / k 4 | D 3: k 2 / k 3 / k 4 | U of the same runs (D 2, k 2 / D 3, k 2) |
| --- | --- | --- | --- |
| 3 | 2 / 2 / 1 | 2 / 3 / 1 | 2 / 3 |
| 4 | 3 / 3 / 1 | 6 / 5 / 4 | 3 / 7 |
| 5 | 5 / 6 / 2 | 8 / 7 / 4 | 6 / 10 |
| 6 | 7 / 7 / 5 | 13 / 12 / 8 | 8 / 14 |
| 8 | 11 / 11 / 8 | 16 / 17 / 12 | 13 / 17 |
  (best of the seeds run; k 3 has two seeds.) Linear in d at every k (DATA).
- High rank is not the bottleneck. In every champion HIGH_k is close to U (e.g. D 3, k 3, d 8: HIGH 17, U 18; D 2, k 2, d 8: 11 / 13).
  Most unchained steps already have 2-6 unstable frozen movers above y_t. The climbs gain HIGH only by gaining U.
- Padding excluded (RELRANK: count only frozen movers above y_t that move again later, r192/relrank.py; climbs with REL=1, 40,000
  mutations, seed 3): HIGH_2 = 2 / 4 / 8 at d 4 / 6 / 8 (D 2), 4 / 11 / 12 (D 3); HIGH_3 (D 2) = 0 / 3 / 6. Still linear. On the R191
  champion u_d8_D3 (U 21) the RELRANKs of the unchained steps are 1-7 (step 11: 6 frozen movers above y_t, all released later).
- DECREMENT check at degree 2 and 3 (box 147 Lemma DECREMENT, read at degree D: y_t unstable before, no UNST bit above π(y_t)
  changes): asserted on every evaluated genome of every climb (≈ 2.9 M runs): 0 violations (DATA; box 147 proves it at degree 2 and
  sketches degree D).

## 1. READING
- Box 147 RANK-BOUND says #{t : RANK_t ≤ k} ≤ Σ_(j ≤ k) C(n, j), so a super-polynomial run needs super-polynomially many steps of
  RANK > k for every fixed k. The data say the converse direction is free: high rank comes with any unchained step (frozen movers
  above y_t are abundant, and most of them are released later). The score HIGH_k is therefore ≈ U and inherits U's linear growth
  (box 144 U-LIN data, R190, R191 §3).
- Where a compounding of freeze/release would have to come from: a frozen mover x is released by a flip of R_(lev(x)−1) (R191 KEY-ALT
  for key-alone moves) and its next freeze needs x to be unstable again, i.e. a Ξ-descendant move (degree 2: R189 RE-REVERSAL; degree
  D: at most D − 2 key-alone answers per help, R191 ROT-CAP). So the freeze/release events of x number O(D · (1 + H_x)), H_x = steps
  with a desc(x) move: the compounding must again come from the Ξ side (descendant moves), not from W-side freezes. A TOP_k-constant
  stretch (all moves below the k-th highest unstable mover) is a run of the sub-genome below it with a fixed environment; nothing
  shown here makes those stretches long.
- OPEN: whether HIGH_k (equivalently U) is polynomial; nothing here decides it.

## 2. Files (experiments/red/r192/)
rkclimb.py (climb on HIGH_k, any degree; REL=1 for RELRANK; asserts DECREMENT), relrank.py (RANK / RELRANK / padding per unchained step).
lag/rk_D3_k3_d8.json, lag/rk_D2_k2_d8.json (champions). Outputs in r192/out are container-local (gitignored). No candidate family to realise;
the champion rk_D3_k3_d8 (L 20, U 18, HIGH_3 17) is pinned anyway: instances/rk_D3_k3_d8_n214 (lemck 0 violations, startck, Oink --zlk +
verify, --tl + verify, xeng). check.sh block «R192».
