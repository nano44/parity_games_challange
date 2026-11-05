# P-IDEAL-FLIP fixes (append-only; the packet docs/new/P-IDEAL-FLIP.md, sha1 92803bd5…, frozen 9effea1f, is NOT edited)
L-NEW successor 53. Each entry: what is changed, why, by whose finding, and the full text of every new argument.

## Entry 1 (2026-11-05, date -u: see the commit; Lead 11:49Z fix round: REFEREE 23 claude/referee eaa941b9, REFEREE-2 27 claude/referee-2 dc622d03)
Makes line L-2 (docs/new/P-IDEAL-FLIP-line-L2.txt). No signed statement is weakened; F-a and F-b extend two statements, F-c corrects a
«does NOT claim» remark; L-2 changes the label of the DEAD item and two DATA / wording details.

### F-a (REFEREE FL-L1): NOW-ONCE (b) without ISO. CHOICE: extend (b); L-2 keeps L-1's unconditional wording for c_t-step sequences.
- Definition (extends packet §1). For any G ∈ 𝓛^R_d (d ≥ 2), ISO or not, a start u_0 and bits c_1, …, c_L, the c_t-step sequence is
  u_t := Step^(c_t)_G(u_(t−1)) (the c-step is defined on all of 𝓦_d, packet §1; it keeps the options of 0 and 1 at u_0's). Under ISO
  this is the packet's forced run.
- NOW-ONCE (b′) [G ∈ 𝓛^R_d, no ISO]. If c_t is the same for all t ∈ [a, b] ⊆ [1, L], every level-1 mover x has u_t(x) ≠ u_(t−1)(x) for
  at most one t ∈ [a, b].
- Proof (the packet's proof of (b), which uses no ISO, written for this case). Let x be a level-1 mover. Its option k W-points to mover
  k (𝓛^R_d), so key^c(x, k) = (κ^c_k, g(x, k)); the first entries differ, so x's key^c-smaller option is KP^c(x) := 0 if c = 1, else 1,
  for every state. If x changes at frame t, its new option u_t(x) lies in A_(u_(t−1))(x) (definition of the c-step) and differs from
  u_(t−1)(x); x has degree 2, so both options lie in that A-set and u_t(x) is the key^(c_t)-least of them: u_t(x) = KP^(c_t)(x). If x
  changed at t1 < t2 in [a, b] and not in between, then u_(t2)(x) = KP^(c_(t2))(x) = KP^(c_(t1))(x) = u_(t1)(x), while u_(t2)(x) ≠
  u_(t2−1)(x) = u_(t1)(x). Contradiction. ∎ (A-sets are those of G under u_(t−1), with or without ISO; no Ξ-value is used.)

### F-b (REFEREE FL-L2 = REFEREE-2 N-1): SWAP-RUN without the «some q with b_0(q) = c_1» caveat (exchange argument)
- Statement (replaces the reading of packet §4 Corollary SWAP-RUN, including its caveat paragraph). Let G ∈ 𝓛^R_d with ISO, u_0, …,
  u_L a forced run with flips ≤ k, and q ANY options of 0 and 1; put v := b_0(q) (computed from the gates of 0 and 1, which G and G^swap
  share). Cut [1, L] into the maximal blocks of constant c (at most k + 1). Then each block [a, b] with c = v is a prefix of the run of
  H_q from u_(a−1) with q at 0 and 1, and each block with c = 1 − v is a prefix of the run of (G^swap)_q from that state, each followed
  by frames that change nothing once that run has stopped. So a forced run with k flips is a concatenation of at most k + 1 runs of the
  two fixed IDEAL genomes H_q and (G^swap)_q, each started where the previous piece was cut; moves = the sum of the pieces' lengths.
- Proof. Setting the options of 0 and 1 to q changes no c-step on U (packet W-ONLY (b), ISO). Block with c = v: u_t = Step^v_G(u_(t−1))
  on U, and by W-ONLY (c) for G (c = b_0(q) = v) the run of H_q is the iterated Step^v_G, stopped at the first application that changes
  nothing. Block with c = 1 − v: by SWAP, Step^(1−v)_G = Step^v_(G^swap); G^swap ∈ 𝓦_d is ISO and has the same level-0 gates, so its
  b_0(q) is v too, and W-ONLY (c) for G^swap says the run of (G^swap)_q is the iterated Step^v_(G^swap). In both cases, once the iterated
  step changes nothing it keeps changing nothing (same state, same step), so the block is a prefix of that run followed by idle frames.
  The pieces are consecutive by construction. ∎
- The packet's caveat («If no q with b_0(q) = c* exists …») is no longer needed: q is arbitrary, and the bit c* = c_1 plays no role.
  L-1 already states the unconditional form («a concatenation of at most k + 1 runs of two fixed IDEAL genomes»); with this entry it is
  proved as stated. L-2 keeps it.

### F-c (REFEREE-2 F-1): SWAP-RUN's «Does NOT claim» remark corrected
- Wrong text (packet §4, last line): «The two genomes are in 𝓛_d, so T* (not T^R) caps each piece». H_q and (G^swap)_q have degree-1
  level-0 movers and no degree-2 mover at level 0, so they are NOT in R109's 𝓛_d (which needs exactly two degree-2 movers on every
  level). (G itself and G^swap are in 𝓛_d; the frozen genomes are not.)
- Corrected remark (not a signed statement; no bound is claimed): every level-0 mover of H_q and of (G^swap)_q has degree 1, so R109's
  SHIFT applies (quoted from the R109 statement: «(SHIFT) at any degree, if every level-0 mover has one option, lowering every level ≥ 1
  by one, the level-0 movers staying at level 0 (…), gives a genome with the same run from every start»). The shifted genomes have levels
  0, …, d − 2, the two degree-2 movers of old level 1 plus two degree-1 movers at the new level 0, and the old levels 2, … unchanged, so
  they lie in 𝓛_(d−1). Hence each piece has at most T*(d − 1) moves. This uses R109 SHIFT and nothing else; the packet's premise list
  is not changed for any signed statement (the remark is outside the signed text).

### Line L-2 (docs/new/P-IDEAL-FLIP-line-L2.txt), word diff against L-1 (3 hunks, `git diff --no-index --word-diff`):
- (1) REQUIRED (REFEREE FL-L3): [-DEAD:-]{+CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine):+}. The clause «together with the machine
  premise T^R(3) ≤ 8 (…; without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9)» is kept unchanged.
- (2) F-a choice: extension (entry above); L-1's NOW-ONCE wording «and in a c_t-step sequence on an interval over which c_t is
  constant» stays, now covered by (b′) without ISO. No hunk.
- (3) Optional, taken: REFEREE-2 P-3, frozen form: «gives an IDEAL genome whose run {+from any state with q at 0 and 1+} is the
  iterated b_0(q)-step»; REFEREE-2 P-1: «every [-start for d ≤ 4, 40 random starts otherwise);-]{+start);+}» (every genome checked has
  d ≤ 4: random d = 2, 3, 4, corpus d = 2, 3, 4, so the «otherwise» branch never ran).
- Nothing else changed. sha1s: see check.sh block «P-IDEAL-FLIP» (pins of L-2 and of this file added).
