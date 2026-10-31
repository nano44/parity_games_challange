# P-N5-ROOT (box 114): every descent copies a root descent; a root change is a fuel re-route or a relay — a referee packet from L-NEW box 113
Frozen 2026-10-31 (date -u: see the commit), L-NEW successor 42. For REFEREE and REFEREE-2.
- Scope: a REDUCTION / EQUIVALENCE inside W-runs.
  - No count is bounded here. G-N5-TIME stays OPEN. This is not M3, not a step-4 pass and not a TARGET.md claim.
  - DESC-LIN is DEAD (L-RED R162). DESC*-LIN is DEAD in the weak form (L-RED R163, as relayed by the Lead 14:47Z).
- Source note (history only): docs/new/N5-DESCSTAR-box113.md (l-new 9e4aefa6, f18315ce, 360d002f). This packet restates everything it
  uses; the note is not needed to check it.
- To sign: §2 Lemma DESC-ROOT; §3 Theorem ROOT-STAIR; §4 Lemma ORIGIN-NEW; §5 Lemma NEW-FUEL and Corollary ROOT-SPLIT; §6 Corollary
  FUEL-ROOT-STAIR.
- Not to sign: §7 (DEAD ends, DATA), §8 (READING).
- Line: docs/new/P-N5-ROOT-line.txt (one line, no heading marker).

## 1. Setting, premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md).
  - A run is the sequence of states (σ_k, τ_k), and a transition is k → k + 1.
  - Values (c, P, ℓ) and the order ⊴ ◁ ⊵ ▷ are SPEC S1's.
  - Ξ_k := Ξ_{σ_k}. Iσ_k := {(y, z) Even edge : z ≠ σ_k(y), Ξ_k(z) ▷ Ξ_k(σ_k(y))} (SPEC S2).
  - H_k := S4a's arena at k: Even y keeps {σ_k(y)} ∪ Iσ_k(y), and Odd follows τ_k.
- W-run F = [p, q] := RESULTS R89's: a maximal run of consecutive states of one τ-stretch, none of whose transitions is an S4c fallback
  or changes λ_W. On F, τ and C := {v : λ_W(v) = v} are fixed, and every transition is an S4a step with τ fixed.
  - W_k := the valuation of the (σ_k, τ)-plays. s_k(v) := σ_k(v) for Even v, τ(v) for Odd v (v's successor at k).
  - Even y SWITCHES at k if σ_(k+1)(y) ≠ σ_k(y).
  - |F| := q − p. T1_F := the transitions with W_(k+1) = W_k, and WCT_F := |F| − T1_F.
- β, flips, first-difference positions and descents are as in P-N5-STAIR (l-new 9a58765f, sha1 31771241; line L-1 docs/new/P-N5-STAIR-line-
  L1.txt):
  - β(x) ∈ {0, 1}^(3n + 1) is the parity-oriented rank bits followed by the threshold bits [sl ≥ j], j = −n … n.
  - The first-difference position of a change of W(v) is the least index at which β changes.
  - A DESCENT of v at k is a change of W(v) at k whose first-difference position is strictly larger than that of v's previous change on
    F (the previous change is at some k′ with p ≤ k′ < k).
  - DESC_F := the number of descents on F (all vertices).
- Premises:
  - [1E-N3] RESULTS R57's standing SPEC premise: at S4a, σ_(k+1) is the pointwise optimum of the one-player arena H_k.
  - [R15] RESULTS R15:
    - (a) Lemma A (VJ00 Lemma 5.7, any game): for a non-empty set I of improvements of σ, Ω_σ ⊴ Ω_(Switch_I(σ)) pointwise.
    - (b) Lemma B: if equality holds everywhere, every (v, w) ∈ I is a length-only switch at an own cycle node (Λ_σ(v) = v).
    - (d) N5's steps are such switches, so Ξ_(k+1) ⊵ Ξ_k at every S4a step.
  - [W-MON] RESULTS R91: W_(k+1) ⊵ W_k on F.
  - [LEX] RESULTS R93 (a): ⊴ is the lexicographic order of a coordinate sequence; in particular it is LINEAR on values.
  - [COPY] P-N5-STAIR Lemma COPY in BOTH directions, as signed by both referees with fixes entry 1 (G-ST-1 / P-1):
    - if v ∉ C has the same successor z at k and k + 1, then β(W(v)) and β(W(z)) have the same flips at k, in the same directions,
      through a strictly increasing position map;
    - C-vertices keep the value (c, ∅, 0) on F.
  - [STAIR] P-N5-STAIR Theorem STAIR (signed by both): |F| ≤ T1_F + n(3n + 1) + (3n + 1)·DESC_F, and DESC_F ≤ n·WCT_F.
  - [FUEL-COUNT] P-N5-ODD Lemma FUEL-LEX / Corollary FUEL-COUNT (L-SI, l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6; signed by both
    referees per the Lead 14:22Z; landing pending). It is used ONLY in §6.

## 2. Lemma DESC-ROOT
- Types. Let (x, k) be a descent of x, with previous change at k′. Its type is:
  - R (ROOT) if x switched at k;
  - T (TIE) if not R, and x switched at some t with k′ < t < k;
  - S (STALE) if x switched at k′ and at no transition of (k′, k];
  - COPIED otherwise (x switched at no transition of [k′, k]).
- Statement. Let v have a descent at k, with previous change at k′.
  - Walk x_0 := v, x_(i+1) := s_(k+1)(x_i), and let j be the least index such that x_j ∈ C or x_j switched at some transition of [k′, k].
  - Then x_j ∉ C, and x_j has a descent at k whose previous change is at k′.
  - The descent (x_j, k) is of type R, T or S.
  - If (v, k) is itself of type R, T or S, then j = 0.
- Proof.
  - The walk follows v's (σ_(k+1), τ)-play. Before λ_W(v) no vertex repeats, and no vertex lies in C (its cycle node is λ_W(v), not
    itself). So the walk reaches λ_W(v) ∈ C, and j exists.
  - x_0, …, x_(j−1) are not in C and switched at no transition of [k′, k], so each x_i has the successor x_(i+1) at every state
    k′, …, k + 1.
  - Apply [COPY] (both directions) to each pair (x_i, x_(i+1)) at each transition of [k′, k]. At each such transition, W(v) changes iff
    W(x_j) changes, and the flips correspond through one strictly increasing composite map π. In particular the first-difference
    positions satisfy q(v) = π(q(x_j)).
  - If x_j ∈ C, W(x_j) is constant ([COPY]), so W(v) would not change at k. Hence x_j ∉ C.
  - v changes at k′ and at k and at no transition strictly between, and so does x_j. Since π is strictly increasing,
    q_k(x_j) > q_(k′)(x_j): x_j has a descent at k with previous change k′.
  - By the choice of j, x_j switched at some transition of [k′, k], so (x_j, k) is not COPIED.
  - If (v, k) is not COPIED, v itself switched in [k′, k], so j = 0. □
- Counting.
  - For fixed (x, k), the descents (v, k) mapped to it have distinct v, so there are at most n of them.
  - A T-descent (x, k) has a switch of x at some t ∈ (k′, k) at which W(x) does not change, since x's changes are at k′ and k only: a TIE
    SWITCH. For fixed x the windows (k′, k) of distinct descents are disjoint.
  - Hence, with R_F, T_F, S_F the descents of each type and TS_F the tie switches of F (pairs (y, t), y switched at t, W(y) unchanged at
    t): DESC_F ≤ n·(R_F + T_F + S_F) and T_F ≤ TS_F.

## 3. Theorem ROOT-STAIR (an EQUIVALENCE)
- Statement. |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·(R_F + S_F + TS_F). Conversely R_F + S_F ≤ DESC_F ≤ n·WCT_F, and TS_F ≤ n·|F|.
  - Hence, over any family of runs, |F| is polynomially bounded iff T1_F + R_F + S_F + TS_F is.
- Proof. §2 and [STAIR]. The converse: R- and S-descents are descents, [STAIR]'s converse bounds them, and at most n vertices switch per
  transition. □

## 4. Lemma ORIGIN-NEW
- Definitions.
  - A ROOT CHANGE is a pair (y, k) with y switched at k and W(y) changing at k. Then y ∉ C, by [COPY]'s second clause.
  - With z := σ_(k+1)(y), the root change is an ORIGIN if W(z) does not change at k.
  - It is a RELAY otherwise.
- Statement. Let (y, k) be an origin root change with k − 1 ∈ F. Then (y, z) ∉ H_(k−1). In particular z ≠ σ_(k−1)(y), and
  (y, z) ∈ Iσ_k \ Iσ_(k−1).
- Proof.
  - Suppose (y, z) ∈ H_(k−1). Write z0 := σ_k(y). Then z ≠ z0, since y switched.
  - Let G′ be the one-player game on H_(k−1) with Odd fixed to τ. Its VJ00 valuation of σ_k is W_k, and σ_k is its pointwise optimum
    [1E-N3]. y is not its own cycle node in G′, because Λ_(σ_k)(y) = λ_W(y) ≠ y (y ∉ C).
  - If W_k(z) ▷ W_k(z0), then (y, z) is an improvement of σ_k in G′. By [R15] (a), switching it gives Ω′ ⊵ W_k pointwise. By [R15] (b)
    (y not an own cycle node), Ω′ ≠ W_k. That contradicts pointwise optimality. So W_k(z) ⊴ W_k(z0) ([LEX], linear).
  - y is not in the path set of W_k(z0) (s_k(y) = z0), nor in that of W_(k+1)(z) (s_(k+1)(y) = z), as in [COPY]'s proof (G-ST-1). Both
    values have cycle node λ_W(y). So Φ(y; ·) (P-N5-SRC §2, [PLAY]) is order-preserving on them.
  - Using W_(k+1)(z) = W_k(z) (origin): W_(k+1)(y) = Φ(y; W_(k+1)(z)) = Φ(y; W_k(z)) ⊴ Φ(y; W_k(z0)) = W_k(y).
  - With [W-MON], W_(k+1)(y) = W_k(y), so (y, k) is not a root change. □
- Corollary RELAY. A root change (y, k) with k − 1 ∈ F that enters by an edge of H_(k−1) is a relay: W(σ_(k+1)(y)) changes at k.

## 5. Lemma NEW-FUEL and Corollary ROOT-SPLIT
- NEW-FUEL statement. Let Even y switch at k to z := σ_(k+1)(y), with k − 1 ∈ F and (y, z) ∉ H_(k−1). Then Ξ_(k−1)(z) ≠ Ξ_k(z).
  - So (y, z) is a FUEL RE-ROUTE at k in the sense of P-N5-ODD §6: y switches to z, k − 1 ∈ F, (y, z) ∉ H_(k−1), and
    Ξ_(k−1)(z) ≠ Ξ_k(z).
- Proof.
  - z0 := σ_k(y) ≠ z. S4a picks σ_(k+1)(y) in H_k(y) = {z0} ∪ Iσ_k(y), so (y, z) ∈ Iσ_k: Ξ_k(z) ▷ Ξ_k(z0).
  - z1 := σ_(k−1)(y). (y, z) ∉ H_(k−1) gives z ≠ z1 and not Ξ_(k−1)(z) ▷ Ξ_(k−1)(z1). So Ξ_(k−1)(z) ⊴ Ξ_(k−1)(z1) ([LEX]).
  - Claim: Ξ_k(z0) ⊵ Ξ_(k−1)(z1).
    - If z0 = z1, this is [R15] (d) at the S4a step k − 1.
    - Otherwise y switched at k − 1 to z0, so (y, z0) ∈ Iσ_(k−1): Ξ_(k−1)(z0) ▷ Ξ_(k−1)(z1), and Ξ_k(z0) ⊵ Ξ_(k−1)(z0) by [R15] (d).
  - If Ξ_k(z) = Ξ_(k−1)(z), then Ξ_k(z) ⊴ Ξ_(k−1)(z1) ⊴ Ξ_k(z0), against Ξ_k(z) ▷ Ξ_k(z0). □
- Corollary ROOT-SPLIT. Every root change (y, k) with k − 1 ∈ F is a fuel re-route (new edge, §5) or a relay through an old edge (§4).
  - Every R-descent has k − 1 ∈ F, since its previous change is at some k′ < k with k′ ≥ p.
  - So R_F = R^fuel_F + R^old_F, where R^old_F counts the R-descents entering by an edge of H_(k−1); each of those is a relay.

## 6. Corollary FUEL-ROOT-STAIR (uses [FUEL-COUNT])
- Notation. For an Even edge (y, z), N_F(y, z) := the fuel re-routes of (y, z) in F, and HC_F(y, z) := FUEL-COUNT's HC: the transitions u of
  F at which Ξ(z) changes at a key strictly greater than the key of the last fuel re-route of (y, z) at a transition ≤ u.
- Statement. R^fuel_F ≤ Σ_(y,z) N_F(y, z) ≤ Σ_(y,z) n(n + 2)(HC_F(y, z) + n). Hence
  |F| ≤ T1_F + n(3n + 1) + (3n + 1)·n·( n(n + 2)·Σ_(y,z) (HC_F(y, z) + n) + R^old_F + S_F + TS_F ).
- Proof.
  - Each fuel R-descent at (y, k) is a fuel re-route of (y, σ_(k+1)(y)) at k, and distinct R-descents are distinct (y, k).
  - [FUEL-COUNT] gives N_F(y, z) ≤ n(n + 2)(HC_F(y, z) + n).
  - Insert into §3. □
- The sum is over the Even edges (y, z) with N_F(y, z) ≥ 1.

## 7. DEAD ends and DATA (not to sign)
- Instances are faithful: n5b SPEC = xeng state by state («state sequences identical: True»), and Oink 8fbf0a7 --zlk winners equal N5's with
  verify OK (red/rel2/oinkcmp.sh «OINK OK»). Every start is valid (checked; the repaired ones are noted).
- DEAD:
  - (a) «Every root descent is a fuel re-route» (without «new edge»): red/n5inj/instances/frz32 (with its start) has 3 R-descents entering by
    old edges (k 3: 2 → 17; k 7: 17 → 5 and 13 → 5), all relays. w_re3_1 (L-RED R160) has 2.
  - (b) «T_F = 0»: red/h3/instances/lcount2_n23 (with its start) has T_F = 1.
  - (c) «U = the switch sites is a witness set immune to passive vertices»: L-RED R162's cp_K4, whose observers are switching vertices
    (descents at switch sites = all descents = 388).
- DATA (experiments/new/box113/desc5.py; corpus = L-SI box 53's 1,132 games, 14,028 W-run transitions):
  - DESC 14,755: R 7,606, S 932, T 1, COPIED 6,216; TS 397. DESC-ROOT misses 0.
  - Origin root changes 25,679, ORIGIN-NEW violations 0.
  - New-edge switches with k − 1 ∈ F 27,539, NEW-FUEL violations 0.
  - R^old 47.
  - Two corpus games had invalid starts (comp54_n80, n3cov_lean, L-RED files). On repaired starts (experiments/new/box113/inst/*_fixed.start)
    their lines are identical.
- Pins (check.sh «box 113 DESCSTAR»): w_re3_1, hit_b6a_1, frz32, lcount2_n23, cp_K4.
  - fbg_K4_m6_m48 on its repaired start (box113/inst/fbg_K4_m6_m48_fixed.start, identical to L-RED's startck --repair) has DESC 640 =
    430 pure copies of 210 R-descents, all fuel re-routes.

## 8. READING (not to sign)
- Passive vertices inflate DESC by at most a factor n (§2 counting), which is harmless for polynomiality.
- The chain descents → R-descents → fuel re-routes closes, through FUEL-COUNT's HC, into the landed XI-CH-POLY core (RESULTS R95, XI-RUN).
  It does not reach a smaller named statement.
- The open terms are HC (higher-key Ξ-changes at fuel targets), R^old, S and TS.

## DONE / FINDINGS / NEEDS
- DONE: this packet, line docs/new/P-N5-ROOT-line.txt, and the pins above.
- FINDINGS: to sign DESC-ROOT, ROOT-STAIR, ORIGIN-NEW, NEW-FUEL, ROOT-SPLIT, FUEL-ROOT-STAIR.
- NEEDS: Lead: route to REFEREE and REFEREE-2.
