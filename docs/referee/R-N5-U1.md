# Referee report R-N5-U1: W-tie cascades and w-changes inside a joint λ-phase of N5 (box 31)

Referee: REFEREE (successor 5), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-U1: the Lead's brief (successor-5 spawn) and
GO of 2026-10-24 21:1xZ (read 21:11Z). Pin: trunk claude/vibrant-johnson-nxvvxo eee0d8a (an ancestor of my HEAD 4b6456dc, which merged
trunk cf66bff). Object: docs/new/P-N5-U1-box31.md, sha1 eb90788d2949050f316ed983fa56c34d7a1dd9c7, 200 lines (verified at the pin).
L-NEW successor 11. Context read: SPEC (docs/new/N5-ssi-global.md S1-S5, FIX 1-4, Q1-Q4); experiments/si/si.py l.29-205;
experiments/new/n5.py; P-N5-NH-box30.md (pin c7981ee) and its fixes file; RESULTS R22; my R-N5-NH; docs/new/N5-U1-box30.md and
N5-U1T-box31.md (background; the packet governs). VJ00 opened myself (below). docs/referee-2/ was NOT read for this packet.
Written 2026-10-24 21:26Z onward by date -u. Every verdict is labelled (Opus 5.5, D15). Labels for statements (D18/L40): PROVED (by whom) /
CONJECTURE / OPEN / DATA / READING.

## Verdict
| item (brief order) | packet label | verdict (Opus 5.5, D15) |
|---|---|---|
| (1) §4 Theorem U1, incl. the κ_w-freeze and the transferred P3-1 repair | PROVED (L-NEW) | SIGNED. Every step re-derived (§1). It inherits CASC's gap C-1 (closed). The freeze transfer and the P3-1 vacuity argument are correct with κ_w in place of κ |
| (2) §3 Lemma CASC | PROVED (L-NEW) | SIGNED WITH GAPS: C-1 (step 1 invokes TB, whose TB-even hypothesis covers o's W-continuation into F under H2, where W-flatness is not given; closed: only TB's choice rule is needed, §2.2), C-2 and C-3 (wording). The induction is correct |
| (3) §2 Lemma TB, and its match with SPEC S1 / si.py | PROVED (L-NEW) | SIGNED WITH GAPS: TB-1 (step 2's two inequalities with set-valued ⊕ need one more case; closed, §3.2), TB-2 (wording: exclude c from "v's play from v to c"). The tie-breaks it uses are exactly SPEC S1 (iv) + FIX 4 as coded in si.py (§3.1) |
| (4) §1 Lemma R | PROVED (L-NEW) | SIGNED WITH GAPS: R-1 (the statement as written, "optimal in the cycle-node and path-set components", is FALSE in the case x = u; 3-vertex instance, 4,074 random cases; the fully-optimal form, which is the only one used, holds; closed by restating), R-2 (citation: VJ00 §6 (15), (22), Prop. 6.1; VJ00 states only that ONE shortest path survives, so Lemma R is a strengthening the packet proves, not a citation) |
| (5) §5 Lemma WC | PROVED (L-NEW) | SIGNED |
| (6) §6 reduction to (NH') | READING | Checked as a READING: correct. It uses signed results (R21 Theorem X and TF; R22 F1°, TC, P3′, Corollary) plus this packet's U1 and WC, and two unsigned inputs: the P-N5-NH §4 assembly (itself a READING, checked by both referees) and the fixes file's §4 one-liner (L-NEW READING), which I checked here (true by TC (iv)). So §6 stays a READING |
No statement is NOT SIGNED. No counterexample. All pinned test instances re-run (§6). G-N5-TIME, (NH'), (X), NFB-O, U2/U3 stay OPEN.

## 1. Theorem U1 (§4)
Setting re-stated: J is a (θ, w)-piece of a crossing-free interval (both frames in route form, θ, w constant), c_w = λ_W(o) strictly more
relevant than c_θ = λ_Ξ(o); f = fallback transitions of J. Transitions of J are k → k+1 with k, k+1 ∈ J.
### 1.1 Step 1, the κ_w-freeze (P3′ step 1 with roles swapped)
Checked substitution by substitution against my R-N5-NH §1.2 (P3′ step 1, signed in R22 (c)):
- (R3 swapped). If κ_w(ρ) ≠ κ_w(ρ′), the top t of the difference lies above c_w ≻ c_θ. A_θ(ρ) Δ A_θ(ρ′) = (κ_w difference) ∪
  (V_mid differences), V_mid = vertices strictly between c_θ and c_w; all V_mid vertices are below c_w ≺ t. c_θ, c_w lie on no route
  (under H1 c_θ ∈ F; c_w ∈ F under H2, c_w = o under λ_W(o) = o). P(θ), P(w) are disjoint from route sets ((R2)). So t tops both
  differences and both frames decide by t's parity. Correct.
- (R4 swapped). Ξ(v) = π_v ⊕ θ is non-decreasing at every transition (R15 (a)), θ constant. A κ_w-change is decided by its top t (above
  every V_mid vertex), so κ_w(π_v) only goes up, at S4a and S4c steps alike. Correct.
- Lemma C swapped (both frames induce the same κ_w-order on routes) and "κ_w-strict improving ⇒ gate edge": by (R3 swapped). Correct.
- CR's B2 (λ_W constant on J: c_w on R by (R1)) and the squeeze (simple routes of ≤ |R| − 1 edges): unchanged. Correct.
- P3-1 transfer (¬H2, λ_W(o) = o). Then c_w = o; U1 forces c_θ ≺ o, so the honest frame is in route form only by H1 (λ_Ξ(o) = o would
  give c_θ = c_w), c_θ ∈ F. C_W's top is o, so every route inside C_W \ {o} has κ_w = ∅. A κ_w-strict switch x → z with x ∈ C_W \ {o},
  x ∉ π_z needs κ_w(π_z) ≠ ∅ with an EVEN top t ≻ o. Under σ̂ = σ_k[x → z] the play from x is the cycle x → z → π_z → o → (C_W arc) → x
  with top t (arc ⪯ o; π_z outside κ_w lies below c_w = o). t is even and above o, so its reward exceeds reward(o) whatever o's parity.
  (F1) puts W_{k+1}(x) at a cycle node ≠ o, against (R1) at k+1 ∈ J. Vacuous inside J. x ∈ π_z (B2): a cycle inside R not through o,
  same value in G_τ and 𝓡*_w, R17's B2 analysis applies. Correct. (When k+1 ∉ J the transition leaves J and is not used by the freeze
  inside J, as in R22.)
- So κ_w(π_v) is constant for all v ∈ R from transition |R| − 1 of J on (R-N5-NH §1.2's index); the packet's |R| is safe.
### 1.2 Steps 2-5
- Step 2. After the freeze, W(v) = (c_w, κ_w(π_v) ∪ P(w), |π_v| + ℓ(w)) (vertices of π_v above c_w are exactly κ_w(π_v); P(w) ∩ route = ∅).
  At an S4a step W_{k+1} = value of (σ_{k+1}, τ_k) since τ is constant in the phase, and W_{k+1} ⊵ W_k pointwise ((F1), TB step 1).
  |π_v| ∈ [1, |R| − 1] moves monotonically (direction by c_w's parity) between fallbacks: ≤ |R| − 2 changes per v ∈ R \ {o} per
  fallback-free stretch; W(o) = w constant. Hence K ≤ (f + 1)(|R| − 1)(|R| − 2). Correct.
- Step 3. Post-freeze non-fallback non-W-changing transitions are W-flat; maximal W-flat runs meeting the post-freeze part are
  separated by the K W-changing transitions and the post-freeze fallbacks: ≤ K + f + 1 runs. CASC: switches on R only at run steps
  ≤ L − 2, L ≤ |R| − 1 (π_v ⊆ R \ {o}), so ≤ |R| − 2 transitions with a switch on R per run. Correct, given CASC (§2).
- Step 4. A Ξ- or W-change on R needs a switch on R: Ξ = π ⊕ θ, W = π ⊕ w on R with θ, w constant ((R1)); the only Odd choice is o, τ
  fixed. Correct.
- Step 5. Sum ≤ |R| + f + K + (K + f + 1)(|R| − 2). With f = 0: 2|R| − 2 + (|R| − 1)²(|R| − 2) = |R|³ − 4|R|² + 7|R| − 4 ≤ |R|³
  (4r² − 7r + 4 > 0 for all r). Multiplied out: correct.
- Note: the theorem bounds R-changing transitions per U1 piece given f; it is not a per-vertex bound (U1-T is FALSE, §7 of the packet,
  re-checked in §6).

## 2. Lemma CASC (§3)
### 2.1 The induction (checked line by line)
- Levels. On a W-flat run W(v) = π_v ⊕ w is constant on R, so ℓ(v) = |π_v| is constant. Along a route the level drops by exactly one per
  step (π_{σv} = π_v minus v). So a tied successor z of v (W(z) ⊕ v = W(v)) has level ℓ(v) − 1, and v ∉ π_z.
- Choice rule. At an S4a step with W′ = W at v (v ∉ {c_w}; c_w ∈ F ∪ {o}), σ_{k+1}(v) is the key-minimum over the fully optimal
  edges of the arena (Lemma R + the longest/BFS rule, §3, §4). With W′ = W on R, the fully optimal R-successors are the tied arena
  successors in R. A tied successor in F can be chosen only at a crossing; inside J the choice is in R and equals the key-minimum over the
  tied R-candidates. Keys: index (odd mode); in the even mode the root-first index sequence of z's σ_{k+1}-play to c_w, whose part from c_w
  to o is common to all of R (it may change at F-ties under H2, but identically for every candidate), so comparisons inside R depend
  only on σ_{k+1} along π_z.
- Step 2's dependence claim: Ξ_k(z) = π_z ⊕ θ depends on σ_k at z and below, the key on σ_{k+1} at z and below (wording C-2: the packet
  says "levels < ℓ(z)"; z's own successor is at level ℓ(z); step 3 only uses candidates z of level ℓ(v) − 1, for which "levels ≤ ℓ(v) − 1"
  is what is needed and is what holds).
- Step 3. Let j = S_{ℓ−1}: no vertex of level ≤ ℓ − 1 switches at transitions ≥ j, so σ_j = σ_{j+1} = … there. For a candidate z of v
  (level ℓ − 1), Ξ_{j′}(z) = Ξ_j(z) and key_{j′}(z) = key_j(z) for all j′ ≥ j; tiedness is constant on the run. z1 := σ_{j+1}(v) is the
  key-minimum of the tied arena candidates at j (the choice rule holds whether or not v switches at j). If σ_{j′}(v) = z1 (j′ > j), the
  arena at j′ is {z1} ∪ {z : Ξ(z) ▷ Ξ(z1)}, and Ξ_j(z1) ⊵ Ξ_j(σ_j v) (z1 is in the arena at j). So every tied z ≠ z1 in the arena at j′
  was in the arena at j (z ≠ σ_j(v) since Ξ_j(z) ▷ Ξ_j(σ_j v)), hence key(z) > key(z1): v keeps z1. Induction on j′. So S_ℓ ≤ S_{ℓ−1} + 1,
  S_1 = 0 (the only tied R-successor of a level-1 vertex is o). Correct.
- Conclusion: a level-ℓ vertex switches only at run steps ≤ ℓ − 2; no switch at steps ≥ |R| − 2 (L ≤ |R| − 1). Correct.
### 2.2 Gaps
- C-1 (hypothesis of TB on o's W-continuation; CLOSED). CASC step 1 invokes TB, whose TB-even hypothesis is "W′ = W_k on v's whole
  σ_k-play from v to c". Under H2 that play runs through o's W-continuation o → τ(o) → … → c_w inside F, where "W-flat" (defined on R)
  says nothing. Closure: CASC does not need TB's statement, only its CHOICE RULE: at an S4a step, every optimiser vertex v that is not its
  own W′-cycle node gets σ_{k+1}(v) = the key-minimum over the fully optimal arena edges w.r.t. W′ (Lemma R in its fully optimal form +
  the longest/BFS selection, TB steps 3-5 without the old play). This holds with no hypothesis on the old play. With W′ = W on R, the
  fully optimal R-candidates of v are its tied R-candidates, and the keys are σ_{k+1}-plays. That is all step 3 uses. DATA: TBc (the
  choice rule at every Even vertex not its own cycle node, every S4a step) 0 failures in 381,241 checks; C1 (W unchanged on o's
  W-continuation at W-flat transitions of pieces under H2) 0 failures. Wording repair: in CASC step 1, cite "TB's choice rule (steps 3-5
  and Lemma R)" instead of "TB applies".
- C-3 (wording). "Transitions of J" must mean k → k+1 with both ends in J; J's exit transition can be a crossing, at which v's choice may
  leave R. It is counted elsewhere (X, or a θ/w change).

## 3. Lemma TB (§2)
### 3.1 Match with SPEC S1 and si.py (the brief's item (3))
- σ_{k+1} = the dual-Odd counterstrategy of ONE Engine.evaluate call on dual(H_k) with dual-Even fixed to τ (n5.py l.46-50; SPEC S4a).
  The dual has Ω + 1 (n5.py dual()), so c odd in G is dual-even: longest-path mode; c even in G: BFS mode (SPEC S1 (iv); TB step 3). The
  dual-Odd minimises the dual order, which is G-Even's order reversed (rew_d = −rew − 1 at every vertex, weights negated, length rule
  flipped). Correct.
- Longest mode: si.py l.154-168, `if d > best` over hs[x] in list order = the smallest index among survivors of maximal length (SPEC FIX 4).
  hs[x] inherits the sorted order of succ (si.py l.33; n5.py passes sorted(opt[v]); restrict keeps order, l.128-134).
- BFS mode: si.py l.172-180: layers FIFO, predecessor lists hp in increasing index (gp built by increasing v, l.87-90; removals keep order,
  l.133), tau[y] = x at first discovery (SPEC FIX 4). TB step 5's induction (queue order of a layer = lex order of the root-first index
  sequences of the tree paths; a tree path is the lex-minimum over surviving shortest paths) is correct for exactly this code.
- The cycle node's own choice (SPEC S1 (v), FIX 2: the DFS) is excluded by "v not its own cycle node". So TB is a statement about SPEC N5.
### 3.2 Proof
- Step 1. W′ = value of (σ_{k+1}, τ_k) = the H_k-optimal value (S4a returns a one-player optimum; R17 (F1)); σ_k is an H_k strategy.
  Correct.
- TB-1 (step 2; CLOSED). The chain W*(x) ⊵ W*(σ_k x) ⊕ x ⊵ W_k(σ_k x) ⊕ x uses ⊕ on sets. (a) The first inequality is VJ00 (7) (§5.1) for
  the optimal valuation; with set-valued ⊕ it also holds when the optimal play from y = σ_k x passes x: the loop x → y → … → x has top t′;
  t′ even and above c, or t′ below c with c odd, would give Even a better cycle at x than c (contradicting optimality); otherwise the formal
  triple is worse (odd t′ in P, or a longer length at even c). (b) The second inequality needs monotonicity of · ⊕ x, which can fail only if
  x ∈ P*(y) \ P_k(y) (x ∉ P_k(y): else x lies on its own W_k-cycle above its cycle node). Then W*(y) = (seg ⊕ W*(x)) with
  W*(x) = W_k(x) = W_k(y) ⊕ x, and W*(y) ⊵ W_k(y) forces the top of seg ∪ {x} to be even: an even cycle through x above c, against W*(x) =
  W_k(x). So the case does not occur. With (a) and (b) the sandwich gives the full triple equality W*(σ_k x) ⊕ x = W*(x).
- Steps 4-5 (TB-odd / TB-even) via Lemma R in its fully-optimal form (§4): correct. Forced vertices' single edges survive the
  restriction (a forced q ∈ M_u reaches c, resp. u, only through its edge) and lie on shortest paths. The tree path of v is its
  σ_{k+1}-play; it differs from the old play at v's successor, so it is strictly lex smaller.
- TB-2 (wording). TB-even's hypothesis should read "every vertex of v's σ_k-play before c". Step 2 is false at c itself (W(c) ≠ W(σ c) ⊕ c),
  and the proof uses only the vertices before c.

## 4. Lemma R (§1)
### 4.1 Source (opened myself)
VJ00 = J. Vöge, M. Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000),
https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65 (downloaded
and opened 2026-10-24 21:18Z by date -u). §6 "Efficient implementation" (pdf pp. 24-27): procedure "Shortest paths", lines 1-10; claims
(15)-(19) for r ∈ R+; Proposition 6.1 (clauses 1-4) with its proof and claims (20)-(22) for r ∈ R−; Theorem 6.2. §5.1 (3)-(10) for the
characterisation Π_σ(v) = shortest-path weight and (6), (7).
Correspondence: si.py l.135-150 = VJ00 lines 2-8 (Even likes u ↔ r ∈ R+, lines 4-5: W = vertices reaching t avoiding r, delete
(W ∪ {r}) × (V \ W); Odd likes u ↔ r ∈ R−, lines 7-8: U = vertices reaching r, delete (U \ {r}) × (V \ U)); longest/BFS = lines 9-10.
- R-2 (citation; CLOSED). VJ00 Prop. 6.1 clause 1 says only that G(r) contains A shortest path from every v. Lemma R ("every optimal edge
  survives") is stronger and is NOT in VJ00. What the packet's step 2 needs from VJ00 is the membership-path-set correspondence: for
  r ∈ R+, r ∉ Σ(v) iff some path avoids r ((15) and its Prop. 6.1 analogue), for r ∈ R−, r ∈ Σ(v) iff v reaches r ((22)), both in G(r).
  With the packet's step-1 invariant and the induction "every fully optimal edge has survived so far" (so the optimal plays lie in G(r)),
  the case analysis of step 2 is correct. Cite VJ00 §6 (15), (22), Prop. 6.1 for it.
### 4.2 R-1: the statement as written is false in one case (CLOSED by restating)
- The packet's hypothesis: y "optimal for the optimiser at x in the cycle-node and path-set components" (box-31 text: "the value through y,
  extended by x, has the same cycle node and path set as x's optimal value"), with set-valued ⊕.
- Case x = u, y ∉ M_u (u processed, Even likes u): y's optimal play passes u, so P*(y) ∋ u and P*(y) ⊕ u = P*(y). If the segment
  y → … → u has no vertex above c, (c, P) of y ⊕ u equals (c, P*(u)), yet the edge u → y is deleted (si.py l.136-143).
- Instance (scratch/lemr_probe.py corner): vertices 0 = c (Even, Ω 1, self-loop), 1 = u (Odd = optimiser, Ω 2, edges to 0 and 2),
  2 = y (Even, Ω 0, only edge to 1). Engine.evaluate: val[u] = (c, {u}, 1), val[y] = (c, {u}, 2), u ⊕ val[y] = (c, {u}, 3): same (c, P);
  the restricted graph after the loop is {0: [0], 1: [0], 2: [1]}: u → y deleted.
- Random: 20,000 games (n 2-12, seed 61): 4,074 deleted edges with (c, P) equal to x's; in every one y's optimal play passes x and x is
  above c (the case above).
- The FULLY optimal form (W*(y) ⊕ x = W*(x) in all three components) holds: the length separates the case (ℓ*(y) ≥ 1 + ℓ*(u), so
  ℓ*(y) + 1 ≠ ℓ*(u)). DATA: 57,885 fully optimal edges, 0 deleted; at all 54,995 optimiser vertices the survivors of optimal length are
  EXACTLY the fully optimal edges; the engine's choice is always fully optimal. VJ00's multiset weights (§4.3, M(V)) also exclude the case
  (u would count twice).
- Every use in the packet is the fully optimal form (TB step 2 delivers full equality; §1's "Hence" sentence). Repair: replace "optimal
  for the optimiser at x in the cycle-node and path-set components" by "fully optimal: W*(y) ⊕ x = W*(x)", and in step 2, case
  "Even likes u, x = u", say that the length differs (y's play returns to u).

## 5. Lemma WC (§5)
- Step 1: under ¬H2, o ∈ C_W ⊆ R (TC (i), constant on I); o's W-play is C_W, so w = (c_w, ∅, d), d ≤ |C_W| − 1 ≤ |R| − 1. Correct.
- Step 2: W non-decreasing at S4a steps (τ fixed), at o included; reward(c_w) strictly rises at a c_w-change, c_w ∈ R; with c_w fixed
  only d moves, monotonically. Correct.
- Step 3: per fallback-free stretch w takes at most |R| · |R| distinct values (c_w ∈ R, d ∈ [0, |R| − 1]), strictly increasing, so
  ≤ |R|² − 1 changes; ≤ f_I + 1 stretches plus ≤ f_I fallback transitions. (f + 1)(r² − 1) + f = (f + 1)r² − 1. Correct.
- DATA: 3,928 intervals with ¬H2: shape w = (c_w, ∅, d ≤ |R| − 1) with c_w ∈ R at every state, max WC(I) = 1, 0 violations.

## 6. §6 reduction (READING)
- Base: P-N5-NH §4 with fixes §5 (NH-1 boundary transitions) and §6 (NH-2): a READING checked by both referees (R22, "not signed").
- ROI on route-form pieces: P3′ (c_θ ≻ c_w; R22 (c), signed), Theorem U1 (c_w ≻ c_θ; this report), c_θ = c_w: no OTHER state. Under
  H1 ∧ H2, H3 holds, hence (h). Mixed patterns: H1 ∧ ¬H2 has c_θ ∈ F, c_w ∈ R; ¬H1 ∧ H2 has c_θ ∈ R, c_w = λ_Ξ(τ(o)) ∈ F (TC (i), (ii)).
  ¬H1 ∧ ¬H2 (fixes §4, L-NEW one-liner, unrefereed): route form forces λ_Ξ(o) = λ_W(o) = o, θ = w = (o, ∅, 0), every state EQ by TC (iv)
  (signed). I checked this one-liner: correct. Theorem U1 counts Ξ-, W- AND σ-changes on R, so NH-2's extra line is not needed in U1.
- Pieces per interval: under H2 ≤ max(1, |F|) (R22 (d)). Under ¬H2 the W frame is in route form iff c_w = o (definition), and then
  w = (o, ∅, 0); a piece boundary is a θ-change (an F-change by TF under H1, ≤ max(0, |F| − 1) by F1°; none if λ_Ξ(o) = o), a c_w-change
  (≤ |R| − 1 per fallback-free stretch, WC step 2) or a fallback. So ≤ 1 + max(0, |F| − 1) + (f_I + 1)(|R| − 1) + f_I pieces: polynomial
  given f_I. Correct.
- So the reading "(NH') reduces to (X), the fallbacks at OTHER states (NFB-O), and U2/U3 re-routings" is correct as a READING. The
  inputs are signed results within their hypotheses, plus Theorem U1 and Lemma WC (signed here, pending REFEREE-2), plus the two unsigned
  inputs named above. U2/U3 and Lemma CASC-C (N5-U1T-box31.md §7) are outside this packet and were not refereed.

## 7. Data (DATA, not proof; tools in docs/referee/scratch/, written from the packet's definitions, independent of experiments/new/box31/)
- u1_probe.py: own N5 trace (n5.py's loop, recorded; asserted equal to n5.run's iteration/fallback counts on every game); W from the
  play of (σ, τ) via Engine on the game with Odd fixed to τ; phases (λ_Ξ, λ_U, τ); crossing-free intervals; route-form pieces; checks
  TBc (choice = key-min over tied arena successors, at EVERY Even vertex not its own cycle node, every S4a step), TB (the statements),
  R1, CASC, C1, U1 (freeze, bound, W monotone), WC. Every game asserts exactly one Odd vertex with out-degree > 1.
- lemr_probe.py: si.py's evaluate with one hook after the restriction loop (source read at run time, nothing else changed).
- casc_climb.py: hill climb maximising CASC's margin (run step − level + 2; violation iff > 0), then W-flat switches, then U1 changes.
| run | games | key numbers | failures |
|---|---|---|---|
| pinned test instances (3) | u1t_cex_n32, u1t_cex2_n32, u1t_own6_n32 | U1 pieces of 7 / 5 / 6 transitions, R-changing 7 / 5 / 6 (bounds 21,224 / 21,224 / 13,296), freeze index 0, TB-even 17 / 35 / 15, CASC switches 13 / 35 / 13 | 0 |
| named sweep: experiments/new/box21-31, n5-exhaustive, red/n5, red/n5inj, red/xing (98 files; 78 in 𝒞^1O, n ≤ 200; 20 skipped) | 78 | 1,671 pieces, 92 U1 pieces (longest 12 transitions, max 12 R-changing, max freeze index 3), 112 W-flat runs (longest 20), 109 CASC switches, 130 ¬H2 intervals, 64,080 TBc | 0 |
| random o-cyclic/acyclic 𝒞^1O, n 8-24 (seed 3201) / n 24-48 (seed 3202) | 4,000 / 1,500 | 921 / 407 U1 pieces, ALL single-state (vacuous for U1 and CASC); 86,440 / 123,244 TBc; 2,969 / 829 ¬H2 intervals | 0 |
| random arenas (TB's proof uses only σ_k ∈ H_k), n 3-14 (seed 51) / 15-40 (seed 52) | 20,000 / 3,000 | TB-odd 102 / 11, TB-even 374 / 161, TBc 68,985 / 38,492 | 0 |
| Lemma R on random games, n 2-12 (seed 61) | 20,000 | 57,885 fully optimal edges, 54,995 EXACT checks | 0 (R-1: 4,074 (c, P)-only cases deleted, as predicted) |
| casc_climb from the three pinned instances (seeds 11-13), 3,000 steps each | 7,599 candidates, all fully checked | best margin −2 in all three (every W-flat switch at a run step ≤ ℓ − 4); W-flat switches 14 / 25 / 21 | 0 |
- Re-runs (brief): n5.py + check_sol2.py (Oink 8fbf0a7 built here, zlk): u1t_cex_n32 (sha1 63dfd7850222…) 12 iterations / 1 fallback;
  u1t_cex2_n32 (6162a26f6f87…) 9 / 1; u1t_own6_n32 (f6368500a3a1…) 9 / 1; all "zielonka(oink zlk) OK strategies verified".
- Packet §7 / §8 claims re-checked: u1t_cex2_n32 vertex 23 switches at all 5 transitions of its U1 piece (states 0..5, c_θ = 27, c_w = 8)
  [confirmed]; u1t_cex_n32 vertex 10 has 7 Ξ-changes in the piece [confirmed], but σ(10) is NOT fixed throughout: it switches once,
  12 → 29 at transition 0 (DATA note D-2); vertex 6: 2 → 18 → 19 → 18, vertex 14: 25 → 5 → 28 → 25 [confirmed]; u1t_own6_n32: vertex 6
  switches 6 times in a 6-transition U1 piece (c_w = 2), 5 of them in one W-flat run [confirmed, = the Lead's 21:1xZ description].
- D-1 (DATA note): |R| at the U1 pieces is 29 on u1t_cex_n32 and u1t_cex2_n32 and 25 on u1t_own6_n32 with R as defined (o ∈ R,
  P-N5-NH §0; the lane's own thtrace.Rset gives the same 29). The packet (§7), R22 and the Lead quote 28 / 28 / 24, i.e. |R \ {o}|. No
  bound is affected (all are loose by orders of magnitude).
- Honest limit: random 𝒞^1O runs are vacuous for U1 and CASC (single-state pieces); the evidence for long W-flat runs comes from the
  named instances and the climbs. Theorem U1 rests on the proof.

## Signature
REFEREE (successor 5), Opus 5.5 (D15), 2026-10-24: Theorem U1 SIGNED; Lemma CASC SIGNED WITH GAPS C-1 (closed), C-2, C-3 (wording);
Lemma TB SIGNED WITH GAPS TB-1 (closed), TB-2 (wording); Lemma R SIGNED WITH GAPS R-1 (statement restated to the fully optimal form;
closed), R-2 (citation; closed); Lemma WC SIGNED; §6 reduction checked as a READING (correct; unsigned inputs named). Labels after two
signatures (D18/L40): TB, CASC, R, U1, WC would be PROVED (L-NEW; REFEREE, and REFEREE-2 if it signs), on 𝒞^1O, given f (U1, WC).
G-N5-TIME OPEN.
