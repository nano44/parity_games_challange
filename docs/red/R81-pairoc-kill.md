# R81: CONJECTURE PAIR-OC is FALSE (pairoc_n58; L-SI's lvl2.py and my h3_19 agree); LC2 survives on it (L-RED successor 20, box 48; Lead 08:32Z, 10:11Z, date -u)
Target: CONJECTURE PAIR-OC (and LC2), docs/si/N5-RUND-box17.md §15 (L-SI successor 13 lane note; read at l-si 873c8e71, which has §15 of
l-si 4b0aeae6 unchanged). Labels per L40. Every game. Nothing here bounds N5. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result
- **KILL: CONJECTURE PAIR-OC is FALSE.** In one stretch_D segment the W score of v rises at the same level at two offset changes:
  levels 47, 48, 47 at three offset changes (B = 48 > A = 47). The segment is states 0..3 of a fallback-free in-phase run with (h3_D) at
  every state, and D, R_D and every gate's (Ξ, W) are constant on it. This is exactly the ruler pattern a, b, a that §15 names.
  - Instance experiments/red/usplit/instances/pairoc_n58.pg, sha1 4824c73cd544c12533a894d1ace902da6c73de3d. n 58, five Odd choice
    vertices (the gates u0-u3 and the zero-offset gate). Start pair: pairoc_n58.start (n5.py / L-SI format, sha1 2f5630e9) and .start.json (a7112802).
  - Run: `n5.py n5 pairoc_n58.pg out.sol --start <SIGMA0> <TAU0>` gives 5 iterations and 0 fallbacks. check_sol2 gives "zielonka(oink
    zlk) OK strategies verified". usplit20 --oink gives OUT_OINK OK.
  - L-SI's lvl2.py (l-si 873c8e71, `--one <pg> <start> -v`) reports:
    `EVENTS … 0 3 v 57 oc 3 SL [('W', 47), ('W', 48), ('X', 49), ('X', 51), ('X', 52)] [(0, 47, 52, True), (1, 48, 51, True), (2, 47, 49,
    True)]`, `VIOLATION ('PAIROC', …, 0, 3, 57, …)`, `LVL FAIL`. It also reports PAIR and PAIR_ALL.
  - My h3_19.py (new PAIROC / LC2 checks, written from §15's text): `PAIROC v=57 states 0..3 pairs={('W', 47): 2, …}`, pairoc_max 2.
  - LC2 holds here: |OC| = 3 ≤ |SL| = 5. lc2_slack −1 (mine) and no LC2_V (lvl2).
- Larger sibling: mkpairoc.py 2 4 10 (n 90, 11 iterations) gives the same violation: v = 89, W levels 79, 80, 79; lvl2 PAIROC_V = 1.
  The family kills at (db, dt, LG) = (2, 2, 4), (2, 2, 5), (2, 3, 5), (2, 2, 6), (2, 3, 6), …. None of the grid points with db = 1 kills (db 1-2, dt 1-4, LG 4-8 tested); I did not analyse why.

## 1. The construction (experiments/red/usplit/mkpairoc.py db dt LG OUT)
- High even cycle node c = 1000, so fillers are in no path set. Every route ends at a gate, so R_D is constant (R80 §0a's device).
- Four gates G0..G3. Each is an Odd u_i with τ = a_i → c (W tail ∅) and σ̄ = b_i = odd o_i → chain → g_i (Ξ tail {o_i}). Offsets
  are 2^rank(o_i), all distinct, and LG keeps each gate in D. A zero-offset gate Z serves the exit routes.
- Rank order: o0 > o1 > Q > o2 > B > A > H3 > qt > o3 > c.
- v (Even) has successors s0 → G0, a and b.
  - a (even A) → w; w has successors s1 → G1 and t1. t1 … t_dt is a delay line ending at h3 (even H3) → G3; its exits go to qt (odd)
    → Z.
  - b (even B) has successors L1 and a. L1 … L_db is a delay line ending at G2; its exits go to Q (odd) → Z.
- Change 1, v → a: W {} → {A}, level A. It is Ξ-improving because o0 > o1.
- Change 2: b's line delivers (b's route loses Q); then v → b: W {A} → {B}, level B. It is Ξ-improving because o1 > o2.
  - Throughout, b → a is W-tempted (A) and Ξ-blocked (o1 > o2): a forbidden edge.
- Change 3: w's line delivers and w → t1. This is Ξ-improving all along (o1 > o3) and W-better once h3 arrives. Now Ξ(a) beats Ξ(L1),
  because o2 is the odd top of b's route. So b → a (a U event), and v's W goes {B} → {B, A, H3}, level A.
  - Each change moves v to another gate class: G0 → G1 → G2 → G3, offsets 2^rank(o0) → 2^rank(o1) → 2^rank(o2) → 2^rank(o3), all
    distinct.
- Why §15's reason for hope fails: the second use of level A comes from un-blocking a Ξ-forbidden edge (b → a). The forbidden edge holds
  a back while a higher rise (B) happens, and the unblocking is paid by a gate change downstream (w: G1 → G3), not at A.

## 2. Side results on the same instance (DATA)
- It is also a U-SPLIT kill with no stretch_D boundary of any kind (usplit20: U 1, neither_full 1).
  - The event is b's switch to a. b's offset falls from G2's to G3's (2^rank 30003 → 2^rank 1001), so it is not UP.
- LC2 (|OC| ≤ |SL|) survives here. Ξ's levels at the three changes are distinct (52, 51, 49: o0, o1, o2 removed in turn).
  - A kill of LC2 needs Ξ to reuse levels as well (a ruler in both scores at the offset changes). With 2^k − 1 changes on k levels per
    score, that would need ≥ 7 changes on 3 + 3 levels. Not attempted in this box.

## 3. Tools
- mkpairoc.py (generator).
- h3_19.py: PAIROC and LC2 checks added, written from §15's text. PAIROC is a counter now (pairoc_viol), since PAIR-OC is dead (the R78
  trap). LC2 stays a FAIL check while it is live.
- usplit20.py (U-SPLIT, R80).
- L-SI's lvl2.py was run read-only from a detached worktree of origin/claude/l-si at 873c8e71, removed afterwards.
