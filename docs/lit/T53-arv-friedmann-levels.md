# T53: what the matroid lower bound exploits, whether Friedmann's counter runs inside one cycle-node phase, and level / ranking arguments for path valuations, all against XI-CH-POLY
L-LIT successor 4 (Opus 5.5), D18, D17/L39. Lead's brief 2026-10-30 13:34Z (T53 (1)-(3)). Written 2026-10-30 from 13:40Z (date -u). Working
note, unrefereed, not a TARGET.md claim. G-N5-TIME, R*-POLY, FL-POLY and XI-CH-POLY (T52 §4) stay OPEN.
Labels: PROVED-in-source / PROVED (L-LIT, elementary, unrefereed) / READING (every N5 implication) / DATA / DEAD / OPEN.
Fleet definitions (RESULTS R89, l. 5854): W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays. A W-run := a maximal run of one τ-stretch
with no S4c fallback and no change of λ_W. XI-CH-POLY := ΞCH_F(v) ≤ p(n) for every vertex v and W-run F (T52 §4).

## Summary
| item | opened source | what it exploits / proves | can N5 (S4a + σ̄) exhibit it in one W-run? | consequence for XI-CH-POLY |
| --- | --- | --- | --- | --- |
| (1) ARV Thm 3 (upper) | Ackermann-Röglin-Vöcking ECCC TR06-067 Thm 3, Lemma 4 | matroid bases + ADDITIVE (congestion) costs: a best response decomposes into 1-1 exchanges, each not worse (Schrijver's perfect matching), so a rank potential with ≤ n·m levels drops | the strategy space is a partition matroid (yes), but Ξ is not additive over chosen edges (no) | the "levels" half transfers as a target (T52); the exchange half has no N5 analogue |
| (1) ARV Thm 7 (lower) | same, Def. 8, Lemma 9, Lemma 10 | the 1-2-EXCHANGE PROPERTY: three resources a, b, c such that the optimum holds a alone or b and c together, depending on d(a) < or > d(b) + d(c) | per-vertex choices: NO (partition matroid, one edge per vertex). Per-vertex PLAYS (σ̄'s paths): YES, path systems are non-matroids, and a path through one edge vs a detour through two is exactly a 1-2 exchange | the ARV dichotomy does not decide N5 either way; N5 sits in the gap (matroid choices, non-additive valuation) |
| (2) Friedmann 0901.2731 | arXiv 0901.2731 v1, Thm 8 (PDF p.9) and PDF p.6 | locally optimizing (switch-all) SI needs 13·2^n − 9 iterations on G_n. All valuations keep the SAME cycle node q and the same length component; the counter lives only in the path set P | the mechanism needs only a constant cycle node, i.e. it runs inside one λ-phase. It is driven by switch-all. N5 runs Friedmann-type families in few steps (DATA, T44-T51) | PROVED (L-LIT): Ξ-monotonicity + constant cycle node do NOT imply XI-CH-POLY; some vertex has ≥ (13·2^n − 9)/|V_n| Ξ-changes in one phase under switch-all. XI-CH-POLY must use N5's rule |
| (3) level arguments | Koh-Loho 2108.13338 Thm 5.3 + Algorithm 4; HMZ 1008.0530 Thm 6.5 / Lemma 6.4; Post-Ye 1208.5083 Thm 3.7 | Bellman-Ford on ordered-tree labels: n − 1 rounds, independent of the lattice size (KL). Discounted: action elimination per (1/(1 − γ)) log levels (HMZ). DMDP with uniform discount: γ-free strongly polynomial simplex (Post-Ye) | one-player only (KL: G_τ for Even; Post-Ye: DMDP), or discounted (HMZ). N5's one-player pieces are already polynomial (R17 Theorem PH: n − 1 value changes per λ-phase) | the fleet's R17 / PH is itself the level argument for the one-player part. No opened source gives a level argument for a two-player lexicographic valuation |

- Main READING: XI-CH-POLY is not a consequence of any "monotone + levels" principle that also holds for the exponential SI rules.
  - Friedmann's G_n is a Ξ-monotone run at one fixed cycle node with exponentially many Ξ values at some vertex (§2).
  - A proof must use what N5's W-runs have and switch-all runs lack:
    - τ is fixed inside a W-run;
    - S4a picks the one-player W-optimum of the improving arena (W is the valuation against the FIXED τ, so a W-run is one-player in W);
    - R88 / R89's GP* bound (≤ n − 1 W-changing transitions per R*-epoch).
  - The W/Ξ gap (W against τ, Ξ against σ̄) is where Ξ can move while W does not. That is again R134's GAP-IN-PREFIX wall.

## 1. Ackermann-Röglin-Vöcking: what the lower bound exploits (PROVED-in-source)
Source: ECCC TR06-067 (April 2006; JACM 55(6) 2008, DOI 10.1145/1455248.1455249), sha256 d13b2032bc8f8721, PDF pp.5-8.
- Thm 3 (PDF p.5): «Let Γ be a matroid congestion game. Then players reach a Nash equilibrium after at most n²·m·rk(Γ) best responses.»
  - Lemma 4 + proof: Schrijver's bipartite exchange graph on S_i* Δ S_i has a perfect matching. «for every edge {r, r*} ∈ PM,
    d_r*(n_r*(S*)) ≤ d_r(n_r(S*) + 1)», so the same holds for the rank-delays d̃.
  - «since there are at most n·m different d_r(n_r)-values, d̃_r(n_r) ≤ n·m»; Rosenthal's potential in ranks is ≤ n²·m·rk(Γ).
  - PDF p.5: «Theorem 3 is independent of the delay functions. In particular, we do not assume monotonicity».
- PDF p.7: «The key insight for proving Theorem 3 is that best responses in matroids can be decomposed into sequences of pairwise exchanges
  of resources such that each of these exchanges does not increase the delay of the corresponding player … this 1-1-exchange property is
  not only sufficient but also necessary for fast convergence.»
- Def. 8 (1-2-exchange property, PDF pp.7-8): three distinct elements a, b, c ∈ R such that, for any k, delays on R \ {a, b, c} can be
  chosen so that for all 1 ≤ d(a), d(b), d(c) ≤ k: «If d(a) < d(b) + d(c), then for every set I from Σ with minimum delay, a ∈ I and
  b, c ∉ I. If d(a) > d(b) + d(c), then … a ∉ I and b, c ∈ I.»
- Lemma 9 (PDF p.8): every inclusion-free non-matroid (R, Σ) has the 1-2-exchange property (proof from X, Y ∈ Σ and x ∈ X \ Y with no
  valid single swap).
- Lemma 10 + Thm 7 (PDF p.7): «Let C be a class of inclusion-free optimization problems that contains a non-matroid problem. Then the
  corresponding class of freely configurable congestion games with non-decreasing, non-negative delays contains games with exponentially
  long best response sequences.» The construction needs the global structure to be free («no restrictions on the global structure»).
- READING (N5).
  - Model A, players = Even vertices, strategies = single successor edges: each strategy space is a uniform rank-1 matroid, so no 1-2
    exchange exists. But the "delay" of X's choice is Ξ(successor), which depends on other players' choices non-additively (no
    resource-sum structure). Thm 3's Lemma 4 has no analogue.
  - Model B, players = vertices, strategies = their plays (paths to a cycle) with path-additive P weights: path systems are not matroids,
    and the 1-2 exchange is visible. One edge (X, g) with a "heavy" continuation vs a detour through two edges, decided by
    d(a) vs d(b) + d(c), is exactly the leapfrog / Carstensen comparison (T48 §1.3, T51 §4).
  - So N5 does not meet ARV's polynomial hypotheses in either model. It meets the exponential hypotheses (1-2 exchange) in Model B, but
    ARV's Lemma 10 needs freely configurable global structure (players' resource sets and delay functions chosen by the adversary). N5's
    global structure is fixed by the game graph, by τ fixed in a W-run, and by S4a's joint arena optimum (not independent per-player best
    responses).
  - Whether N5's S4a + σ̄ can realise Lemma 10's construction inside one W-run is OPEN. It is L-RED's kind of question; §2 says that
    switch-all can, at a fixed cycle node.

## 2. Friedmann, arXiv 0901.2731 (LICS 2009): the mechanism lives in ONE cycle-node phase
Source: arXiv 0901.2731 v1, «A super-polynomial lower bound for the parity game strategy improvement algorithm as we know it», sha256
6c56adb207f38468. Opened 2026-10-30 (body; L-NEW had the abstract).
- PROVED-in-source.
  - PDF p.6: «every approach trying to construct a game family of polynomial size requiring exponentially many iterations to be solved, needs to
    focus on the second component of game valuations: There are only linearly many different values for the first and third component while
    there are exponentially many for the second. The games G_n therefore are designed in such a way that the first and the third component
    of all occurring game valuations in a run of the algorithm on G_n remain unaltered … the worst (w.r.t. player 0) dominating cycle node
    that can be reached is q. Additionally note that G_n is completely won by player 1 … Thus, we will only focus on the paths leading to q.
    The basic idea is to create a binary counter in G_n».
  - Gadgets (§3): deceleration lanes (absorb update activity, Fig. 1-2) and simple / stubborn cycles (bits).
  - Thm 8 (PDF p.9): «The strategy improvement algorithm requires 13·2^n − 9 iterations on G_n using the locally optimizing improvement policy.»
- PROVED (L-LIT, elementary). Along the run of Thm 8, every iteration strictly improves Ξ at some vertex (VJ00, quoted there as Theorem 3 [16]), and the cycle
  node q never changes (quote above). Hence some vertex v has at least (13·2^n − 9)/|V(G_n)| Ξ-changes inside one cycle-node phase.
  |V(G_n)| is polynomial: the abstract says «a family of games of quadratic size». So ΞCH(v) is exponential in one λ-phase.
- Answer to the Lead's question. The mechanism does NOT need the W-region / cycle nodes to change: it works within one constant cycle-node
  map, in the P component alone. The gadget that contradicts "XI-CH-POLY from Ξ-monotonicity and constant cycle nodes alone" is Friedmann's
  binary counter of simple cycles fed through a deceleration lane, all reaching the single cycle node q.
- READING (N5).
  - The contradiction is to the TEMPLATE, not to XI-CH-POLY for N5. Friedmann's count is driven by the locally optimizing rule (switch-all
    against the best reply).
  - In an N5 W-run, τ is fixed and S4a takes the one-player W-optimum of the improving arena against τ. That step closes a simple cycle
    in one move when closing is W-better, which is what switch-best / global rules do and what Friedmann's stubborn cycles are built to
    delay (thesis p.140-144, T48 §3).
  - DATA: plain N5 and N5-SF run the PGSolver ports of these families in few steps (switchallexp_4: 9 distinct σ; T51 §5, T48 §3).
  - So a proof of XI-CH-POLY must use S4a's arena optimum and the fixed τ. A kill must defeat them in one W-run (L-RED).

## 3. Level / ranking arguments for path or lexicographic valuations (opened sources)
- Koh-Loho 2108.13338 (LMCS 2025), Algorithm 4 and Thm 5.3 (PROVED-in-source). The Bellman-Ford analogue on ordered-tree labels «runs
  for n − 1 iterations». Given an initial labeling between the least fixed point and the base nodes' threshold labels, «Algorithm 4
  returns µ↑Gτ». Running time O(mnγ(T)), independent of |L(T)| except through γ(T). This is a level argument by HOP DEPTH: labels settle
  in path-length order, not by value levels. It is one-player (G_τ for Even).
- Hansen-Miltersen-Zwick 1008.0530 v1 (opened T48): Thm 6.5, iterations ≤ (m + 1)(1 + log_{1/γ}(n²/(1 − γ))), via Lemma 6.4 (a
  non-optimal player-1 action is eliminated after O(log_{1/γ}(n/(1 − γ))) iterations). This is a level argument in which the discount
  makes value gaps shrink geometrically; BLOCKED for parity (1/(1 − γ) = n^Θ(d), T39 row 13, T30).
- Post-Ye 1208.5083 v2 Thm 3.7 (opened T48): simplex with the highest-gain rule on DMDPs with uniform discount, O(n³m²log²n) pivots,
  INDEPENDENT of γ. A strongly polynomial one-player result that survives the lexicographic (γ → 1) limit for single switches. It does
  not cover multi-switch policy iteration (p.2) and is one-player.
- The fleet's own: RESULTS R17 Theorem PH (one-player switch-best: after n − 1 steps every further in-phase step is value-flat; fewer
  than n + m steps per λ-phase). It is the level argument for the one-player piece and is already landed.
- READING. Every opened level argument is one-player (Bellman-Ford depth; Post-Ye's γ-free DMDP bound; R17) or discounted (HMZ). N5's
  W-run is one-player in W (τ fixed), which is why GP* gives ≤ n − 1 W-changes per R*-epoch. XI-CH counts Ξ, the TWO-player valuation
  against σ̄, and no opened source gives a level argument for that. The bridge must be a lemma tying Ξ-changes in a W-run to W-changes:
  - Ξ changes only through W-changes plus σ̄-changes (SBC-type), with the σ̄-changes inside one W-run bounded by a one-player argument on
    G_σ (R17 applies to Odd's problem with σ fixed, not along σ's moves). OPEN.
  - That bridge is the precise missing step. Friedmann's §2 shows it fails for switch-all, where Ξ changes 2^n times at a fixed W-region.

## 4. Pointers for L-NEW 38 (box 87, XI-CH-POLY via the rank trick)
- The rank trick needs polynomially many LEVELS of Ξ(v) per W-run. Friedmann 0901.2731 (PDF p.6, Thm 8) shows that a fixed cycle node does
  not supply them under switch-all (exponentially many P values at one vertex). The levels must come from N5-specific structure:
  - τ fixed (W one-player);
  - S4a's arena optimum;
  - GP*'s n − 1 W-changes per R*-epoch.
- ARV's matroid half applies to Even's per-vertex choices (partition matroid) but its exchange lemma needs additive costs. The non-additive
  (path) view is where ARV's 1-2-exchange lower-bound property appears.
- Level arguments that exist are one-player (KL Thm 5.3, Post-Ye Thm 3.7, R17 PH). The missing bridge is "ΞCH in a W-run ≤ poly ×
  (W-changes + one-player-bounded σ̄-changes)".

## DONE / FINDINGS / NEEDS
- DONE: this note; notebook rows (Friedmann 0901.2731 body; ARV PDF pp.7-8 re-read; Koh-Loho Thm 5.3 re-read).
- FINDINGS:
  1. ARV Thm 7's lower bound exploits the 1-2-exchange property (Def. 8, Lemma 9: equivalent to non-matroid). N5's per-vertex choices are
     matroid but non-additive; its plays are additive but non-matroid (1-2 exchange = leapfrog). N5 meets neither ARV hypothesis set fully;
     realising Lemma 10 in one W-run is OPEN.
  2. Friedmann 0901.2731 (Thm 8, PDF p.6 and p.9): the exponential VJ counter keeps cycle node and length fixed and counts in P alone, so it lives in
     ONE cycle-node phase. PROVED (elementary): some vertex has ≥ (13·2^n − 9)/|V| Ξ-changes in one phase under switch-all. So
     XI-CH-POLY cannot follow from monotonicity + a fixed cycle node; it must use N5's fixed τ and S4a. N5 runs these families in few
     steps (DATA).
  3. Level arguments found are one-player (Koh-Loho Thm 5.3, Post-Ye Thm 3.7, R17) or discounted (HMZ). The missing bridge for N5 is
     Ξ-changes per W-run bounded by W-changes plus one-player-bounded σ̄-changes (OPEN).
- NEEDS: none from the owner.
