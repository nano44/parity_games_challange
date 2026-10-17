# R28: adversarial read of L-ALG's (NT-f) proof, step (D): no gap found (L-RED box 6, 08:58Z by date -u; produced on Opus 5.5)
Target (Lead 08:49Z): l-alg ced9921, docs/alg/GAP-C.md §18k, Lemma NT-f ("the final round f of a −1 best_vertices call
accepts no stored tangle in its region loop"). Question asked: at round r_1's rescue loop, at level q−1, is the escape e
actually POPPED (so attractTangle(t) is called), i.e. is e in the rescue set at that level, not merely in Z^{r_1}?
Checked against tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7 (the pinned source), not against the pseudocode.

## 1. The pop happens
dtl.cpp 721-740 (best_vertices, rescue loop): `for (int t=0; t<=max_prio; t++) { for (auto v = Z.find_first(); ...)
Q.push(v); while (Q.nonempty()) { u = Q.pop(); attractVertices(player, u, R, Z, R, t); attractTangles(player, u, R, Z,
R, t); } ... candidate test ... }`. At EVERY level t the stack is refilled with ALL of Z, and every vertex of Z is popped
and passed to attractTangles. Z at round r_1 starts as Z^{r_1} (the union of the round's regions; it is reset only after
the loop) and only grows. By (B) every escape of t in R lies in Z^{r_1}, so e is popped at level q−1 (and at every
level). attractTangles(u) runs attractTangle for every tangle in tin[u], so attractTangle(t) is called. The level loop
runs over every integer t ≤ max priority (C++), so level q−1 exists; L-ALG's pyref iterates only existing priorities,
which gives the same sets.

## 2. attractTangle(t) at level q−1 (dtl.cpp 110-185)
- vertices of t: those of priority q are M_q ⊆ V_{r_1} ⊆ Z^{r_1} (skipped as "in Z"); all others have priority < q, so
  ≤ q−1 = maxpr; t ⊆ R (it was accepted inside R in round f, and R is the same in all rounds of one call);
- escapes: an escape in R \ Z would reject t; there is none (all in Z by (B)); escapes outside R are ignored (Gx = R);
- tangle alive: no tangle is learned or deleted between rounds of one best_vertices call except by attractTangle
  itself on a solved vertex, which cannot happen inside one call (G does not change).
Wording nit only: if t ⊆ Z already at that level, attractTangle returns false ("nothing new") and t does not "join";
t is then already inside Z, so the candidate test still finds m_1 attracting. The conclusion is unchanged.

## 3. The candidate test (dtl.cpp 733-739)
Candidates are collected in descending index (= descending priority, 712-715) and tested until the first with priority
≤ t. pr(m_1) = q > q−1, so m_1 is tested at level q−1 unless it was rescued at an earlier level (also a contradiction).
attracts(p, m_1, Z, R) holds: a p-owned m_1 has its tangle successor in t ⊆ Z; an opponent-owned m_1 has all its R-edges in
t ∪ escapes ⊆ Z and one in t.

## 4. Also re-read
(A) induction (vertex-rule additions of round f lie in A^r(τ_x) for every r): holds in this reading. The opponent case
uses the LAST successor in processing order of round r. Each successor lies in a region of a top with index ≥ index(τ_x),
so pr(top) ≥ pr(τ_x) ≥ pr(x), and the threshold permits the attraction. (B) and (C) as written.
Verdict: no gap found in steps (A)-(D) for any order datum; the argument uses only R being fixed within one call and
the per-level refill of Q. Not a referee signature.
