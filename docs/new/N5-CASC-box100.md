# N5-CASC (box 100): FRESH-ROOT is PROVED in full (lane) with the EVEN root map (Lemma EVEN-ON-PLAY: a Ξ-change at z forces a switch of an Even vertex on z's OLD play; premises [R57] and R15 only). Lemma CHILD (PROVED, lane): a node (x, q) of the root forest has at most one child per Even edge (X, g) with x on g's old play, so ≤ #{(X, g) : x ∈ π_q(g)} ≤ m_E. CORRECTION of box 99: root chains are NOT of depth ≤ 2 (a memo bug); topfix_N has depth 6N − 11 (49 at N = 10), so «depth O(1)» is DEAD, but there every node has exactly one child. On the corpus a RETURN node has ≤ 6 children, while FRESH nodes carry the width (≤ 0.27 m_E)
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 21:49Z: «BOX 100 (proof side): (1) Close FRESH-ROOT's two open cases …, or
give the instance where the root map fails. (2) Then attack CASCADE-LIN directly … A rough candidate: CASC_F(e) ≤ #{g : x on g's play}. Then
show each such g is re-entered at most O(1) times per root … Depth: data says root chains have depth ≤ 2. Is there a structural reason …?»
Written 2026-10-30 21:50Z-22:1xZ (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA. Not a TARGET.md
claim. G-N5-TIME stays OPEN; CASCADE-LIN is not proved.

## 0. Setting, premises, tools
- Box 99 (N5-QRET-box99.md): returns, windows, fresh entries, CASC_F(e), CASCADE-EQ. Box 98: Lemma PAY.
- Premises, as quoted in P-N5-SETTLE §1 / P-N5-WRUN:
  - [R57]: «S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t»;
  - R15 (a), (d): Ξ_(k+1) ⊵ Ξ_k pointwise at every transition;
  - SPEC S4a: σ_new(v) ∈ {σ(v)} ∪ Iσ(v);
  - in a W-run every transition is an S4a step (no S4c fallback, τ fixed).
- Tool: experiments/new/box99/retcause.py, extended. EROOT is the Even root map of §1. «children per node» and «per return node» are as in
  §2. Box 99's relative-depth memo bug is fixed.
- Corpus re-run: box99/runcause.sh → box99/cause_*.txt (overwritten), summary in box100/corpus_summary.txt. Pin: new/check.sh «box 100 CASC».

## 1. FRESH-ROOT, closed (PROVED, lane)
### 1.1 Lemma EVEN-ON-PLAY
- Statement. If Ξ_(q+1)(z) ≠ Ξ_q(z) at a transition q → q + 1 of a W-run, then some Even vertex on z's (σ_q, σ̄_q)-play π_q(z) switches
  at q. The play is followed until it repeats a vertex.
- Proof.
  - Suppose no Even vertex of π_q(z) switches. Then the (σ_(q+1), σ̄_q)-play from z is π_q(z): every vertex of the play has the same
    successor (Even ones by assumption, Odd ones because the Odd strategy is σ̄_q in both).
  - The [S1-val] value of z is a function of z's play. So val(σ_(q+1), σ̄_q)(z) = Ξ_q(z).
  - [R57] at q + 1 (σ̄_(q+1) is Odd's pointwise optimum against σ_(q+1)) gives Ξ_(q+1)(z) ⊴ val(σ_(q+1), σ̄_q)(z) = Ξ_q(z).
  - R15 gives Ξ_q(z) ⊴ Ξ_(q+1)(z). So Ξ_(q+1)(z) = Ξ_q(z), a contradiction. □
- No prefix decomposition, cycle condition or own-node condition is needed. Box 99's two open cases came from the FIRST-DIVERGENCE map,
  whose Odd step needed Ξ(old target) to change. The Even map below never takes an Odd step.

### 1.2 Lemma WINDOW-RISE (the window form of RET-ΞRISE)
- Statement. If Even X leaves g at j → j + 1 and re-enters g at k → k + 1 (k > j, X not holding g on [j + 1, k]), then Ξ(g) changes at
  some transition of [j, k − 1].
- Proof.
  - By S4a, the target X adopts at j is in Iσ_j(X): Ξ_j(h) ▷ Ξ_j(g).
  - While X keeps a target, that target's Ξ does not decrease (R15). At each later switch the new target is strictly better at that
    time.
  - So Ξ_k(σ_k(X)) ⊵ Ξ_j(h) ▷ Ξ_j(g).
  - At k, g ∈ Iσ_k(X), i.e. Ξ_k(g) ▷ Ξ_k(σ_k(X)). If Ξ(g) were constant on [j, k], then Ξ_k(g) = Ξ_j(g) ◁ Ξ_k(σ_k(X)), a
    contradiction. □

### 1.3 The Even root map and Theorem FRESH-ROOT
- For a change of Ξ(z) at q, let x(q, z) := the first Even vertex on π_q(z) that switches at q (it exists by EVEN-ON-PLAY), and
  w := σ_(q+1)(x).
  - If (x, w) is a FRESH entry at q, then root(q, z) := (x, w, q).
  - Otherwise it is a return of x to w at q. Let q′ be the first transition of its window at which Ξ(w) changes (it exists by
    WINDOW-RISE, and q′ < q). Then root(q, z) := root(q′, w).
- The ROOT of a return of X to g is root(q₀, g), with q₀ the first change of Ξ(g) in its window.
- Theorem FRESH-ROOT. The root map is total. Every return's root is a fresh entry at a transition ≤ the return. Its chain depth (the number
  of return steps) is at most the number of transitions before the return. PROVED (lane): each step moves strictly back in time, and a
  step stops only at a fresh entry. □
- So CASCADE-EQ (box 99 §2.3) is now unconditional at lane level: WRUN-POLY ⇔ CASC-POLY, with |F| ≤ (m_E − n_E)(1 + max_e CASC_F(e)).
- DATA: EROOT kinds FRESH 9,455 of 9,455. On the three pins the top roots and their counts (45 / 71 / 93 per tick) are the same as box 99's
  first-divergence roots.

## 2. The root forest: width and depth
### 2.1 Lemma CHILD (PROVED, lane)
- A NODE is a pair (x, q) with x switching at q. A return is a CHILD of the node (x(q₀, g), q₀), where q₀ is its first window change.
- Statement. Node (x, q) has at most one child per Even edge (X, g), and only edges with x ∈ π_q(g) and Ξ(g) changing at q qualify. So
  children(x, q) ≤ #{(X, g) Even edge : x ∈ π_q(g), Ξ_q(g) ≠ Ξ_(q+1)(g)} ≤ m_E.
- Proof. Two returns of one edge (X, g) have disjoint windows: the second leave comes after the first re-entry. So their first window
  changes q₀ are distinct, and at most one of them is at q. A child of (x, q) has x(q, g) = x, so x ∈ π_q(g). □
- This is the Lead's candidate in edge form: CASC at depth 0 ≤ #{(X, g) : x ∈ π_q(g)}. Each g is re-entered at most d_E(g) times per node,
  and once per edge.

### 2.2 Corollary TREE (PROVED, lane)
- Let B(e) := children of the fresh node of e, c := the maximum number of children of a return node in F, and D(e) := the depth of e's
  root tree. Then CASC_F(e) ≤ B(e)·(1 + c + … + c^(D(e)−1)).
- If c ≤ 1 this is ≤ B(e)·D(e) ≤ m_E·|F|. Then |F| ≤ (m_E − n_E)(1 + m_E·D), with D ≤ |F|. Circular in general, but polynomial whenever D
  is.

### 2.3 Depth: CORRECTION of box 99, and «depth O(1)» is DEAD
- Box 99 reported «root-chain depth ≤ 2 (8,738 / 709 / 8)». That was WRONG. retcause.py memoised roots with the ABSOLUTE depth of the first
  caller, so a deeper chain that hit the memo was counted at depth 0.
  - Roots and CASC were not affected: the memo stores the same root.
  - Fixed: relative depths.
- Re-run (both maps; box100/corpus_summary.txt): depths 0-49. EVEN map: depth 0 for 6,697 returns, 1 for 2,078, 2 for 147, … 49 for 1.
- topfix_N (new/box52/out, default start, one W-run each):
  | N | n | |F| | returns | max CASC | max depth | max children per node |
  | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 63 | 16 | 14 | 8 | 7 | 1 |
  | 4 | 84 | 22 | 30 | 14 | 13 | 1 |
  | 6 | 126 | 34 | 80 | 26 | 25 | 1 |
  | 8 | 168 | 46 | 154 | 38 | 37 | 1 |
  | 10 | 210 | 58 | 252 | 50 | 49 | 1 |
  - Depth grows as 6N − 11, and every node has exactly one child: each root tree is a PATH of returns. «n» is read
    from the file header (n = header index + 1).
- DEAD: «root-chain depth O(1)» (any structural depth bound independent of n). Instance: topfix_N, depth 49 at N = 10 (sha1 in the commit's
  check pin).
- What survives (DATA):
  - Width sits at FRESH nodes: max children of a fresh node / m_E = 0.273 (latew 62 / 227), 0.261 (sbq2 30 / 115).
  - Return nodes are narrow: max children per return node is 1 on sbq2 / latew, 2 on obs, and ≤ 6 on the whole corpus (6 at
    u23sw64_n32, n 32; 3 at b6_xw_n40, b6_xl_n40, x31_cu48, run34_n40).
  - Deep chains (topfix) have width 1. Wide trees (the pins) have depth ≤ 2.
- CONJECTURE NARROW (new, data only): every return node has O(1) children, and a chain of return nodes with ≥ 2 children has length O(1).
  With TREE this would give CASC_F(e) ≤ B(e)·O(D(e)), and CASCADE-LIN would follow from D(e) ≤ O(n / B(e)). Not proved. No structural
  reason found. The Lead's form «a return cannot root a return more than once per W-change» was NOT tested here (W-changes per node were
  not measured).

## 3. CASCADE-LIN: status
- Unchanged: CONJECTURE. Corpus max CASC / n = 0.483 (switchbestexp_2). On the three pins the two root maps give the same maximal roots and
  counts; on the corpus the root kinds agree (all FRESH) and the max CASC is the same; a per-return comparison of the two maps was not run.
- A proof needs the product B(e) · (width of the deeper levels) · D(e) ≤ n / 2. The data shows a trade-off: B large ⇒ D ≤ 2, and D large ⇒
  width 1. That trade-off is the lemma to find. The natural potential is the set of observers on the clock's play (B) against the length
  of the relay chain (D); both live on π_q(g).
- L-RED kill shapes (for the Lead's routing):
  - a return node with many children at depth ≥ 2;
  - a topfix-like path whose nodes branch.
  Either would make CASC super-linear.

## DONE / FINDINGS / NEEDS
- DONE: this note; retcause.py (EVEN map EROOT, relative-depth memo, children per node / per return node); box99/cause_*.txt re-run;
  box100/corpus_summary.txt; new/check.sh «box 100 CASC»; box 99 note marked CORRECTED in its depth lines. SHA: see the commit.
- FINDINGS:
  - PROVED (lane): EVEN-ON-PLAY, WINDOW-RISE, FRESH-ROOT (all cases, Even root map), so CASCADE-EQ is unconditional at lane level; CHILD
    (children ≤ #{(X, g) : x ∈ π_q(g)}, one per edge); TREE.
  - CORRECTION: box 99's «depth ≤ 2» was a tool bug.
  - DEAD: depth O(1), killed by topfix_N (depth 6N − 11, width 1).
  - CONJECTURE NARROW: return nodes have O(1) children (corpus ≤ 6).
  - CASCADE-LIN: still a CONJECTURE (0.483n).
- NEEDS: Lead: route NARROW and the two kill shapes (§3) to L-RED with CASCADE-LIN.
