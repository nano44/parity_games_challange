# Box 194: from D_E to R. Part 1: [LOC] is a lemma in IDEAL-CYC (Lemma LOC-GATE), so OVT-DV holds without it
L-NEW successor 62 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-07 22:35Z: «GO» and «Box 194 (a), your [LOC] idea: go, write it as a lane
lemma.» Written from 22:4xZ (date -u). Labels: PROVED (lane, unrefereed) / DATA / READING / CONJECTURE / DEAD.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).

## 0. Summary
- PROVED (lane): Lemma LOC-GATE. In IDEAL-CYC(G), for every genome G, every state t and every gate g: if Ω_t(e_g) ≠ Ω_t(β_g), then
  σ̄_t(g) is the face of ⊴-smaller value. Also σ̄_t(K2) = K1, and K1 is K2's ⊴-least successor value (Lemma LOC-K2). So [LOC]
  («σ̄_t(v) is a ⊴-least successor value at every Odd v», box 192 §1) holds at every Odd vertex of IDEAL-CYC.
- Consequence (PROVED, lane): L-RED's Lemma OVT-DV (R217 §2), with the citation fix of box 192 Addendum 9, holds with no [LOC]
  premise. The same holds for every lane statement marked PROVED-CONDITIONAL on [LOC] alone (list in §4).
- PROVED (lane): Theorem QUIET (§6). Call a step loud if some vertex changes (cycle node, e-set). Every run of consecutive non-loud
  steps has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps. Hence (Corollary T-QUIET) T ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1):
  the IDEAL-CYC run length, and so R, is polynomial in N, M and the total number of e-set changes. This replaces BOTH missing steps
  (OVT-DV and IN-BOUND) from D_E to R. Premises: landed R118 (F1, F3, F4′, DOM, STRICT) plus LOC-GATE and CN2.
- Corollary UP-T (under [E-LEV]): for genomes with boundedly many upward Ξ-edges U(G), the IDEAL-CYC run length T is polynomial in
  N + M (P-N5-ASC UP-B + T-QUIET). Corollary ASC-T: the same without [E-LEV] if every vertex's plays have boundedly many ascents.
- DEAD: CONJECTURE IN-BOUND in its constant form (RS2(L, 6): IN = L + 1). Not needed any more (§7).
- [E-LEV] (b): it is R104's own definition in the frozen packet R104 cites (§8).
- DATA: 0 failures of LOC-GATE, LOC-K2, OVT-DV and its face bounds on L-RED's LEAP_k64 and rd3_d4 (as the Lead asked), on the 13
  box 193 instances and on 1,000 random genomes (§5).

## 1. Premises, and where each one is landed
- [DEF] RESULTS R104's definitions of the genome and of Γ(G), as quoted in P-N5-ASC §1 (frozen, docs/new/P-N5-ASC.md). Used: movers are
  Even of priority 0 and their successors are gates; gates are Odd of priority 1 with exactly two successors, the W-face e_g and the
  Ξ-face β_g; e and β have priority ≥ 6; the core K0 → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 → {K1, K2}, start
  K1 → K1. LANDED (R104 definitions; the «Used shape» line is P-N5-XICYC §1 l. 39, «movers (Even, priority 0) → gates (Odd, priority 1)
  → {e-face e_g, β-face β_g}», inside RESULTS R118's premise «R104's definitions of the genome and of Γ(G) only»).
- [XICYC-a] IDEAL-CYC(G): Γ(G) with every non-mover Even vertex frozen at its start successor; «Odd is unrestricted (gates and K2)».
  LANDED: RESULTS R118 (a) (trunk docs/RESULTS.md l. 13677).
- [VJ] the value (Λ, Π, k) and its order ⊴: «first the reward of Λ (an even priority p gives +p, an odd one −p, with priorities made
  injective by rank); then Π, decided by the most relevant vertex of the symmetric difference, which is better for Even iff it is even
  and in the larger set; then k, where a longer prefix is worse for Even if Λ is even and better if Λ is odd» (P-N5-XICYC §1 l. 31-33).
  LANDED as a premise of RESULTS R118: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)» (R118 header).
- [OPT] σ̄_t is an optimal counterstrategy at every vertex at once: Ω_t(v) ⊴ (value of the play from v under (σ_t, τ)) for every
  positional Odd strategy τ of IDEAL-CYC(G) and every vertex v. Source: VJ00 §5 as cited in [VJ]. LANDED as used inside R118 (b): F3's
  proof, P-N5-XICYC l. 75, «σ̄_t is optimal at every vertex at once ([VJ])», inside the range «Facts F1-F6 (§3 l. 68-83)» that R118 (b)
  signs. The same fact is RESULTS R21 (a)'s parenthetical «(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})» (l. 933).
- [F3] RESULTS R118 (b), F3: if Λ_t(v) ≠ v then Ω_t(v) = ext(v, Ω_t(nx_t(v))), ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more relevant
  than Λ}, k + 1). LANDED (R118 (b)).
- [F4′] RESULTS R118 (b), quoted there: «if v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B), and A ◁ B ⇒ ext(v, A) ◁ ext(v, B).»
  LANDED (R118 (b)). Only this landed clause is used; the extra clause of the fixes file («It also holds whenever v ranks below Λ(A) and
  Λ(B)») is NOT used. So F4′ is not a hypothesis of anything below.
- Not used: [LOC] (that is the point), F4 as printed, F5, F6, E-DOM, any L-RED lane lemma, [E-LEV].

## 2. Lemma CN2 (PROVED, lane): every cycle node of IDEAL-CYC has priority ≥ 2
Statement: for every genome G, every positional pair of IDEAL-CYC(G) and every vertex v, the cycle node of v's play has priority ≥ 2.
In particular no gate (priority 1) and no mover (priority 0) is ever a cycle node, and no gate is ever in a set Π.
Proof.
- The cycle node is the most relevant vertex of the play's cycle. A cycle that contains a mover contains its successor, a gate ([DEF]).
  A cycle that contains a gate contains one of its successors, a face, of priority ≥ 6 ([DEF]). A cycle with neither consists of vertices
  of priority ≥ 2 (every vertex other than movers and gates has priority ≥ 2 by [DEF]). In all cases the cycle has a vertex of
  priority ≥ 2, so its most relevant vertex has priority ≥ 2.
- A vertex is in Π only if it is more relevant than the cycle node ([VJ]); a gate has priority 1 < 2. ∎

## 3. Lemma LOC-GATE (PROVED, lane)
Statement: let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate with faces e_g, β_g. Write a := σ̄_t(g), b := the other
face, and Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).
Proof. Suppose Ω(b) ◁ Ω(a). Let τ be σ̄_t with g switched to b; τ is a positional Odd strategy of IDEAL-CYC(G) ([XICYC-a]: Odd is
unrestricted at gates). Write val_τ(g) for the value of g's play under (σ_t, τ). By [OPT], Ω(g) ⊴ val_τ(g). We derive val_τ(g) ◁ Ω(g).
- Ω(g) = ext(g, Ω(a)): g is not its own cycle node (CN2), so [F3] applies with nx_t(g) = a.
- Case 1: the play from b under (σ_t, σ̄_t) does not visit g.
  - τ agrees with σ̄_t off g, so the play from b under (σ_t, τ) is the same play, and the play from g under (σ_t, τ) is g followed by it.
    g is not its cycle node (CN2), so by the definition of the value ([VJ]), val_τ(g) = ext(g, Ω(b)).
  - g ∉ Π(Ω(a)) ∪ Π(Ω(b)) by CN2. [F4′] (strict part) with Ω(b) ◁ Ω(a) gives ext(g, Ω(b)) ◁ ext(g, Ω(a)), i.e. val_τ(g) ◁ Ω(g).
- Case 2: the play from b visits g; write it b = z_1, …, z_m, g, … with z_1, …, z_m distinct and ≠ g (m ≥ 1), P := {z_1, …, z_m}.
  After g it follows σ̄_t(g) = a, so the plays from b, g and a end in the same cycle; Λ := its cycle node = Λ(a) = Λ(b) = Λ(g).
  Under τ, the play from g is g, z_1, …, z_m, g: a cycle C = {g} ∪ P with cycle node c, the most relevant vertex of C; c ∈ P (CN2).
  - Case 2-i: a's play does not visit g. Then a's play does not meet P either (from any z_i the σ̄-play runs to g). So
    Π(b) = Π(a) ∪ Rel(P), with Rel(P) := the elements of P more relevant than Λ, disjoint from Π(a) (g adds nothing, CN2), and
    k(b) = k(a) + m + 1.
    - 2-i-a: Rel(P) ≠ ∅. Its most relevant element r is the most relevant vertex of P (the other elements of P are less relevant than
      Λ < r), so c = r. Ω(b) ◁ Ω(a) with equal Λ is decided by Π, and Π(b) Δ Π(a) = Rel(P), so r is odd ([VJ]). Then c is odd and more
      relevant than Λ, so reward(c) = −p(c) < reward(Λ) (positive if Λ is even; −p(Λ) > −p(c) if Λ is odd). By [VJ] val_τ(g) ◁ Ω(g).
    - 2-i-b: Rel(P) = ∅. Then Π(b) = Π(a), k(b) > k(a), and Ω(b) ◁ Ω(a) means a longer prefix is worse: Λ is even ([VJ]). Every vertex
      of C is less relevant than Λ, so reward(c) ≤ p(c) < p(Λ) = reward(Λ), and val_τ(g) ◁ Ω(g).
  - Case 2-ii: a's play visits g. Then g lies on the σ̄-cycle Q = (g, a = w_1, …, w_l, g), Λ ∈ Q ∖ {g} (CN2), and every vertex of Q
    other than Λ is less relevant than Λ. So Π(a) = ∅ and k(a) = the distance from a to Λ along Q; Ω(g) = (Λ, ∅, k(a) + 1) by [F3].
    The play from b reaches Q first at a vertex q (q = g, or q = w_j = z_i for some i, j, and then z_i, …, z_m = w_j, …, w_l). Let
    P0 := the part of P before q. Then Π(b) = Rel(P0), k(b) = |P0| + dist_Q(q, Λ), and C = {g} ∪ P0 ∪ arc, where arc := the vertices
    of Q from q up to (not including) g (arc = ∅ if q = g).
    - 2-ii-a: Rel(P0) ≠ ∅. As in 2-i-a, Ω(b) ◁ Ω(a) = (Λ, ∅, ·) forces the most relevant element r of Rel(P0) to be odd; r is the most
      relevant vertex of C (arc and g are less relevant than Λ < r, and so are the elements of P0 outside Rel(P0)). So c = r and
      val_τ(g) ◁ Ω(g) by the reward order.
    - 2-ii-b: Rel(P0) = ∅ and Λ ∈ arc. Then c = Λ, the play from g under τ runs g, P0, then arc up to Λ, with no vertex more relevant
      than Λ before Λ; so val_τ(g) = (Λ, ∅, 1 + |P0| + dist_Q(q, Λ)) = (Λ, ∅, k(b) + 1). Against Ω(g) = (Λ, ∅, k(a) + 1) this is the same
      comparison as Ω(b) against Ω(a), so val_τ(g) ◁ Ω(g).
    - 2-ii-c: Rel(P0) = ∅ and Λ ∉ arc. Then Λ ∈ {w_1, …, w_(j−1)} (or anywhere on Q ∖ {g} if q = g), so the path from q to Λ along Q
      passes g and then a: dist_Q(q, Λ) > k(a), hence k(b) > k(a) with Π(b) = Π(a) = ∅. Ω(b) ◁ Ω(a) then means Λ is even ([VJ]). Every
      vertex of C is less relevant than Λ, so reward(c) < p(Λ) = reward(Λ), and val_τ(g) ◁ Ω(g).
- In every case val_τ(g) ◁ Ω(g), against [OPT]. ∎
Remark. Case 1 needs only g ∉ Π (CN2) for the landed F4′; Case 2 uses only the order [VJ] and CN2. No case uses a VJ00 improvement lemma.

**Lemma LOC-K2 (PROVED, lane).** At every state σ̄_t(K2) = K1, and Ω_t(K1) ◁ Ω_t(K2), so K1 is K2's ⊴-least successor value.
Proof. K1 is Even and frozen at K1 → K1 ([DEF] start, [XICYC-a]), so Ω(K1) = (K1, ∅, 0) with reward −5. If σ̄_t(K2) = K2, K2's play is its
self-loop, value (K2, ∅, 0), reward −3; switching K2 to K1 gives the play K2, K1, K1, … with reward −5 < −3: strictly ⊴-smaller, against
[OPT]. So σ̄_t(K2) = K1 and Ω(K2) = (K1, ∅, 1) by [F3]. With equal Λ = K1 odd and equal Π, the longer prefix is better for Even ([VJ]):
Ω(K1) ◁ Ω(K2). ∎ (The landed Lemma K2-r of R118's fixes is the Γ3 form; this is the IDEAL-CYC form, proved directly.)

## 4. Consequences (PROVED, lane)
- Lemma OVT-DV (L-RED 54, R217 §2, «PROVED-CONDITIONAL on [LOC]»; checked line by line in box 192 Addendum 9) now holds unconditionally
  in IDEAL-CYC: its only use of [LOC] is «with no tie, σ̄_t(g) is the face of ⊴-smaller value», which is LOC-GATE. Its other steps use F1
  (landed, R118 (b)) and the face bound D_I(e_g) ≤ D_I(y) + 1, D_I(β_g) ≤ D_I(x′) + 1, which needs only F3 and the count of images under
  ext(e_g, ·) (box 192 Addendum 9's fix; no injectivity and no F4).
  Statement as it now stands: for any gate g and consecutive states I = [a, b] with Ω_t(e_g) ≠ Ω_t(β_g) for every t ∈ I, the number F of
  σ̄-flips at g inside I is ≤ 2·min(D_I(e_g), D_I(β_g)) − 1, and D_I(e_g) ≤ D_I(y) + 1, D_I(β_g) ≤ D_I(x′) + 1 (D_I(β_g) = 1 when xt = X).
- The same replacement makes these lane statements conditional on nothing but their own other premises (each used [LOC] only at gates
  or at K2): box 192 MERGE-CHOICE, X-GATE, R-SPLIT; L-RED R217 TOP-DEC (d), HIDE-BUSY, CHAIN-SHIELD (READING for L-RED's lemmas: I checked
  only that their [LOC] step is a gate or K2 choice; their other steps are L-RED's).
- What it does NOT give: a bound on R. With OVT-DV unconditional, the chain from D_E to R is
  R ≤ Σ_g flips(g) + (K2 term), flips(g) ≤ Σ over tie-free intervals 2·min(D_I(e_g), D_I(β_g)) + 2·L_g, D(v) ≤ (IN(v) + 1)·D_E(v),
  and the only unproved link is CONJECTURE IN-BOUND (IN(v) bounded by a polynomial). Ties L_g: 0 in all data, not bounded by a lemma.
  READING (not a claim): even with IN-BOUND, R ≤ Σ_g 2·D(e_g) needs D_E(e_g) bounded, which P-N5-ASC gives only for boundedly many
  ascents (HUB-ASC-G) or under [E-LEV] with bounded U(G) (UP-B).

## 5. DATA (experiments/new/box194/; check194.sh, output check194.out; block «BOX 194 LOC» in experiments/new/check.sh)
Tool loc194.py (IDEAL-CYC runs via box192/rpot192.py). Counters, all 0 everywhere:
- locfail: (gate, state) pairs with no tie and σ̄_t(g) not the ⊴-least face (LOC-GATE).
- k2fail: states with σ̄_t(K2) ≠ K1 (LOC-K2). cnlow: (state, vertex) pairs with a cycle node of priority < 2 (CN2).
- ovtfail: (gate, maximal tie-free interval) pairs with F ≥ 1 and F > 2·min(D_I(e_g), D_I(β_g)) − 1 (OVT-DV); efail / bfail: the
  same pairs with D_I(e_g) > D_I(y) + 1 / D_I(β_g) > D_I(x′) + 1.
- ties: (gate, state) pairs with Ω(e_g) = Ω(β_g): 0 everywhere (so every interval is a whole run).
Sets:
- L-RED's LEAP_k64 (claude/l-red d1a11af6, experiments/red/r217/inst/, sha1 b09b2745…) and rd3_d4 (experiments/red/r219/inst/, sha1
  10a37f90…, equal to box192/inst/rd3_d4.json), copied into box194/inst/ with L-RED's SHA1SUMS lines:
  - LEAP_k64: T 129, 66,950 (gate, state) pairs, 515 intervals, 128 flips, maxF 128 (= 2k; D_I(Y) = k + 1 = 65 makes the bound 129).
  - rd3_d4: T 18, 380 pairs, 20 intervals, 34 flips, maxF 6.
- The 8 box 193 instances (L-RED R217) and 5 box 192 instances: 0 on all counters (lines in check194.out).
- 1,000 random genomes (rand191.rgen, seed 2, d 1-6, width 1-3, degree 2-3): 68,549 pairs, 15,945 intervals, 3,158 flips, maxF 4;
  tight (F ≥ 2·min − 2) on 672 intervals.
Scope: IDEAL-CYC. No separate DATA: the list of lane statements in §4 (each was already checked by its own tool).

## 6. Theorem QUIET: the run length is polynomial in the number of e-set changes (PROVED, lane)
This bypasses IN-BOUND: it bounds T (hence R ≤ T) by the total number of (cycle node, e-set) changes, with no per-vertex IN.
Extra premises (all LANDED, RESULTS R118): F1 and DOM (R118 (c): «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵
ext(x, Ω_t(y)).»), STRICT (R118 (c): «If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x).»), and the Howard step of IDEAL-CYC (R118 (a)).
From [DEF] (P-N5-ASC §3, E-MON's proof): every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3; e lies above every β.
Also used: LOC-GATE (§3) and CN2 (§2).

Definitions.
- class_t(v) := (Λ_t(v), E_t(v)) with E_t(v) the e-vertices of Π_t(v) (P-N5-ASC §2). A step t → t+1 is LOUD if class_t(v) ≠ class_(t+1)(v)
  for some vertex v, else QUIET. Q := the number of loud steps. A quiet window is a maximal interval [a, b] of states whose steps are
  all quiet.
- D^tot_E(v) := the number of distinct classes of v over the run. Each class is a convex set of values (the order compares Λ's reward,
  then the e-part, which is the top layer of Π below the common K0, K3 (E-MON's proof)), so by F1 each vertex is in each class during one
  interval of states, and Q ≤ Σ_v (D^tot_E(v) − 1).
- A class (w, S) is a B-class if w is less relevant than every e-vertex, else an E-class. By [DEF] and CN2, the cycle node w of an
  E-class is an e-vertex or c_W (K0, K3 are never cycle nodes: K0 → K3 → K2 are frozen and nothing returns to K0).

**Theorem QUIET.** Every quiet window has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps.
**Corollary T-QUIET.** T ≤ Q + (Q + 1)·L ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1). In particular R ≤ T is polynomial in N, M and Σ_v D^tot_E(v).

Proof of QUIET. Fix a quiet window [a, b]. Every vertex keeps its class on [a, b].
- (Q1) Faces in different classes. If at a gate g the two faces are in different classes, their order is the order of the classes,
  constant on [a, b]; by LOC-GATE σ̄_t(g) is constant on [a, b]. (Ties: a tie needs equal classes.)
- (Q2) Options stay in class. For a mover x and a step t → t+1 inside [a, b], x's chosen option at t+1 has its gate's value in class(x):
  ext at x and at its gate changes neither Λ nor the e-part (CN2). In particular no option of x has a gate value in a class above class(x)
  at a state t < b (Howard would switch to it, and class(x) would change).
- (Q3) E-classes. If class(v) = (w, S) is an E-class, Π_t(v) = S on [a, b]: every vertex more relevant than w is an e-vertex, c_W, K0 or
  K3; c_W is never in Π (only its self-loop), and K0, K3 lie only on plays with cycle node K1 or K2, which are less relevant than every e.
  So Ω_t(v) = (w, S, k_t) and, by F1, k_t is monotone on [a, b] with values in {0, …, n − 1}: v's value changes at most n − 1 times.
- (Q4) B-classes: structure. Let C = (w, S) be a B-class. Every e-vertex is more relevant than w, so:
  - a β-face β_g has Π(β_g) = Π(z) ∪ {β_g if more relevant than w} with z its Ξ-target (or u), so class(β_g) = class(z) (β_g ∉ Π(z):
    if z's play passed β_g it would return to z, so β_g would be on z's cycle);
  - an e-face e_g has class (w, {e_g} ∪ E(y)) with y its W-target, e_g ∉ E(y) by the same argument; so if e_g ∈ C then e_g ∈ S and
    class(y) = (w, S ∖ {e_g}), a B-class with one e fewer.
  - G_C := the movers of class C with, at each, its options whose gate's chosen face is in C. A C-mover's play is a path in G_C that
    leaves C only at a boundary point: an e-face into a class (w, S ∖ {e}), the exit β → u (value constant: the core is frozen and
    σ̄(K2) = K1, LOC-K2), or w itself (when w is a β on the play's cycle; Ω(w) = (w, ∅, 0)). It cannot close a cycle before reaching
    w, since every cycle of its play has cycle node w.
- (Q5) B-classes: stabilisation. For s = 0, 1, …, M let a_s := a + (s + 1)(2M + 1)(N + 1). Claim: every vertex of a B-class (w, S)
  with |S| = s has constant value on [min(a_s, b), b].
  - Assume the claim for s − 1 (nothing for s = 0). Fix C = (w, S), |S| = s. From a_(s−1) (from a if s = 0) every boundary value of C
    is constant: e-faces into (w, S ∖ {e}) by the induction, the exit and w always.
  - Gates of G_C with both faces in C: then the e-face is in C, so its value ext(e, Ω(y)) is constant after a_(s−1), while the
    β-face's value only rises (F1). By LOC-GATE such a gate flips at most twice after a_(s−1) (β to a tie to e). Gates with faces in
    different classes do not flip (Q1). So after a_(s−1), G_C and its chosen faces change at most 2M times: at most 2M + 1 sub-windows.
  - In a sub-window starting at c with G_C fixed: let opt(x) := the ⊴-largest value of a simple G_C-path from x to a boundary point
    (values of such paths are constant). Upper bound: x's current play is such a path (Q4), so Ω_t(x) ⊴ opt(x). Lower bound
    (Bellman-Ford): Ω_(c+h)(x) ⊵ the value of every such path with at most h movers. Induction on h: by DOM Ω_(t+1)(x) ⊵ ext(x, Ω_t(g)) for
    the path's first gate g; by F3 Ω_t(g) = ext(g, Ω_t(face)) and Ω_t(β) = ext(β, Ω_t(z)) or Ω_t(e) = ext(e, Ω_t(y)); by the induction
    and F1 Ω_t(z) ⊵ the rest of the path; and F4′ applies at each prepended vertex: x and g are never in a Π (CN2), and the face is in
    neither Π (not in Ω_t(z)'s, by Q4's argument, nor in the simple path's). A simple G_C-path has at most N movers, so
    Ω_t(x) = opt(x) for t ≥ c + N: from then on every C-vertex is constant (non-movers by F3).
  - A sub-window ends only at a flip, which needs a change of a β-face value, i.e. of a C-value. So every sub-window after the first
    starts within N + 1 steps of the previous one, and C is constant from a_(s−1) + (2M + 1)(N + 1) = a_s on. ∎ (claim)
- (Q6) Counting. |S| ≤ M, so every B-class vertex is constant from a_M = a + (M + 1)(2M + 1)(N + 1). Every step t → t+1 changes σ at
  some mover, whose value strictly rises (STRICT). After a_M that mover is in an E-class, and by (Q3) the E-class movers change at most
  N(n − 1) times in all. So b − a ≤ (M + 1)(2M + 1)(N + 1) + N(n − 1) = L. ∎

**Corollary UP-T (under [E-LEV], the hypothesis of P-N5-ASC §6).** For every genome G, the IDEAL-CYC run has
T ≤ (1 + n·((2M + 3)·F′_(U(G))(M) − 1))·(L + 1). For bounded U(G) this is a polynomial in N + M; R ≤ T.
Proof: P-N5-ASC Corollary UP-B gives D^tot_E(v) ≤ (2M + 3)·F′_(U(G))(M) for every vertex v (its D_E(v), summed over the ≤ 2M + 3
Λ-intervals); then T-QUIET. ∎
**Corollary ASC-T.** Without [E-LEV]: if, for every vertex v, every seq_t(v) has at most B ascents, then T ≤ (1 + n·((2M + 3)·F′_B(M) −
1))·(L + 1) (HUB-ASC-G's whole-run form, then T-QUIET).

What these do NOT give (D1): no algorithm is shown polynomial on all parity games; [E-LEV] is a hypothesis; bounded U(G) and bounded
ascents are restrictions on the genome or its runs. READING: by R118 REACH3-CYC (CONDITIONAL there), T3 ≤ C + R + (C + R + 1)·N for
N5′-xi on Γ3(G), so these corollaries would bound N5′-xi's FL run on Γ3 for such genomes; not claimed here. The open core is now one
quantity: Σ_v D^tot_E(v) (equivalently, P-N5-ASC with unboundedly many ascents).

DATA for QUIET (quiet194.py; counters: wfail = quiet windows longer than L, Tfail = runs with T > Q + (Q + 1)L, crossflip = σ̄ flips at a
gate on a quiet step whose faces are in different classes (Q1)): 0, 0, 0 on rd3_d4, the 8 box 193 instances, rd2_d9, rd2_d10, L-RED's
RS2(L, 6) for L = 32 (generated by L-RED's rs2.py; RS2_L8M6 reproduces box193/inst's sha1 982d5911…), and 1,000 random genomes (seed 2).
Longest quiet window W: W ≤ N in every run (RS2_L32M6: W 32, N 77; random: max W/N = 1.0). Unit: runs / quiet windows / steps. Scope:
IDEAL-CYC. The bound L is far from tight (L ≥ 8,334 on these runs).

## 7. IN-BOUND: the constant form is DEAD; the polynomial form is no longer needed
- DEAD (constant IN-BOUND, box 192 Addendum 9 «IN(v) ≤ c (a constant …)»): L-RED's RS2(L, 6) (deceleration lane of length L) has
  IN = L + 1 exactly for L = 2, 4, 8, 16, 32 (IN 3, 5, 9, 17, 33; all inner changes are β-part changes, none k-only), at mover
  ('x', 2L + 10). Instance: RS2_L32M6 (rs2.py 32 6). Unit: value changes of one vertex inside one stretch of constant (Λ, e-part). Tool:
  in194.py. The polynomial form stays OPEN but is not needed for T-QUIET.
- DATA: IN on the other sets: rd3_d4 2, rd2_d9 2, CLR_k8s16 2, FPORT_n2 / n3 5, RS2 5, RS2_L8M6 9, RS3 9, LEAP_k8 / RSG_K4 0, LEAP_k64 0;
  300 random genomes (seed 5): max 3.

## 8. (b) Is [E-LEV] fixed by R104 / R117? (READING with quotes; Lead decides whether it counts as landed)
- The landed R104 line describes e only as «e of even priority above every β with one edge to the W-target or to the top even self-loop
  c_W», and says (R104 (vi), trunk RESULTS l. 10085): «The line's description of Γ(G) leaves the β-vertex order and the exact
  e-priorities to packet §3.1; both are immaterial by the referees' controls (MUT=border, MUT=eprio)».
- Packet §3.1 (docs/red/P-N5-REALIZE.md on trunk, frozen; l. 88): «e_g: indices N + 2M, … allocated in GATE-INDEX order, Even,
  Ω(e_g) := eb + 2·i, eb := the least even number > bmax, i := the position of g in the order by (lev(owner), gate index)». That order is
  [E-LEV] exactly: lev(x) < lev(x′) ⇒ Ω(e_(x,k)) < Ω(e_(x′,k′)).
- R117 and R118 take Γ(G) from «R104's definitions»; the fleet's builder (box189/gamma3.py) uses the same order.
- So [E-LEV] holds for Γ(G) as R104's packet defines it. It is not stated in a landed line's own text, and R104's «immaterial» covers
  R104's theorem (REALIZE), not UP-B. Lead reading needed: is packet §3.1 part of «R104's definitions» for P-N5-ASC §6 and UP-T?
- An e-order violating [E-LEV] on which UP-B / NOUP fail exists (DEAD without [E-LEV]; instances of others, as the Lead asked):
  REFEREE-2 control CTRL=elevrev, «UPB/NOUP fail on 209 of 21,116 plays of U = 0 genomes (up to 2 ascents)» (claude/referee-2 533744a5);
  L-RED R220, e-order (−level, gate): NOUPC_1 / 2 / 3 with U(G) = 0 and max ascents 2 / 3 / 4, witness NOUPC_1, t 0, v 10 (claude/l-red
  68a1f609, experiments/red/r220/inst/, one route only). Not re-run here. P-N5-ASC fixes entry 1 (19cc23e3) carries the scope change.

## 9. (c) D18 angle: well-quasi-orders (Higman / Kruskal) and tableau structures for hubs with ω(1) ascents
Question (Lead): does a wqo or nested-tableau structure of the hub's chains give a length bound for hubs with ω(1) ascents?
Answer: NO in the abstract model. The reason and the source are below. Labels: DATA / READING / DEAD (conditional on ASC-EXP).

Source opened (pdftotext of arXiv:1103.4399, S. Schmitz and Ph. Schnoebelen, «Multiply-Recursive Upper Bounds with Higman's Lemma»,
ICALP 2011): §2 «A sequence x = x0, x1, x2, . . . over a qo is good if xi ≤ xj for some positions i < j. It is bad otherwise.»;
Definition 2.4 (controlled sequences: |x_i| < g^i(n)); Proposition 2.5 (a finite maximal length L_(A,g)(n) of (g, n)-controlled bad
sequences exists); Theorem 5.3 (Main Theorem: for a smooth control g eventually bounded in F_γ and an exponential nwqo of maximal order
type < ω^(β+1), L_(A,g) is bounded by a function in F_β (γ < ω, β ≥ ω) or F_(γ+β) (γ ≥ 2, β < ω)). Also opened, abstract only:
arXiv:1007.2989 (Figueira, Figueira, Schmitz, Schnoebelen, LICS 2011, Dickson's lemma, «Ackermannian and primitive-recursive bounds»).

- READING 1 (why wqo theory does not apply). Every wqo length theorem bounds BAD sequences: those with no i < j and x_i ≤ x_j. A hub
  sequence is the opposite: strictly increasing in the total lex order. Under the natural wqo's on its values it is good almost
  everywhere: under ⊆ (Dickson on {0,1}^M), under Higman's subword order on chains read as words, or under Kruskal's tree order on the
  forests, the step {3} → {3, 1} is an embedding. A chain in a total order has no bad structure to exploit. Reversing the order does not
  help either: the reversed sequence is decreasing in a total order, and a total order of height 2^M has decreasing chains of length 2^M.
- READING 2 (why the bound would be useless anyway). Even where a translation to controlled bad sequences exists, Theorem 5.3's bounds
  are functions in classes F_β / F_(γ+β) of the fast-growing hierarchy, not polynomials. On the finite universe 2^[M] the trivial
  bound 2^M is already better.
- DATA (the abstract obstruction): Construction ASC-EXP (box 193 §3) is a run of CS(M) whose hub takes all 2^M sets, verified exactly
  for M ≤ 12 (ascexp193.py; M ≤ 10 in check193.sh). Its hub has up to M − 1 ascents. So no statement that depends only on the CS
  axioms (CHAIN-DECOMP + E-MON), wqo-based, tableau-based or otherwise, can give a polynomial bound for ω(1)-ascent hubs, unless
  ASC-EXP fails for some M > 12. DEAD (conditional on ASC-EXP for all M, a CONJECTURE with exact data M ≤ 12): «an abstract structure
  of the hub's chains bounds ω(1)-ascent hubs polynomially».
- READING 3 (tableaux). Insertion tableaux (RSK) bound monotone SUBSEQUENCES of one word (Greene); here the object is a long sequence of
  words, each a chain, linked only by lex monotonicity. HUB-ASC(B)'s recursion is already a tableau-like nesting (levels by τ-tops,
  then segments, then B − 1 ascents inside), and its degree 5·2^B − 3 shows the nesting cost doubles per ascent. No source opened for
  RSK, so nothing is cited.
- Consequence for the programme: after Theorem QUIET (§6), the only open quantity is Σ_v D^tot_E(v). By ASC-EXP it cannot be bounded
  from CS alone; any bound must use which e-set walks are REALISABLE by Howard / Odd in Γ(G) (box 192 Addendum 10). That is L-RED's
  third-bit question, and UP-B is the only realisability fact proved so far (it needs [E-LEV] and bounded U(G)).

## 10. Next (box 194 continues)
- (a) is done in the sense of §6: the step D_E → R is PROVED (T-QUIET); the remaining core is Σ_v D^tot_E(v) for plays with
  unboundedly many ascents.
- (c) done (§9): no abstract structure gives it; next is realisability of e-set walks in Γ(G) (third-bit question).
