# Draft RESULTS R5 (Lead, 2026-10-17 10:20Z) (rev. 10:35Z per CHECKER C5 c14c09f: header, N-1, N-2, N-4, N-5) — NOT LANDED; awaiting CHECKER re-diff

### R5 [refereed-only] Eleven structural lemmas on A_DTL (GAP-C support and GAP-A conditional bound) (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet: the
  fleet's unrefereed PROVED readings, pinned at trunk 43d63b0 (REFEREE) and 20fe2ed (REFEREE-2); statements as in the cited
  sections at those pins, with the readings fixed by the referees (below).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma SCC1 (GAP-C §3): in a closed sptl region Z_τ every vertex reaches τ in extractTangles' graph, so extractTangles(τ)
      finds at most one nontrivial SCC, the set C_τ reachable from τ.
  (b) Lemma B-thr (GAP-C §3), in the stronger form "(a) always": if C_τ equals a stored tangle t, then τ ∈ t, every escape of t
      lies outside the context R, and the last escape of t to leave the current call's context chain was popped in an
      attractor with threshold < pr(τ). Branch (b) of the stated lemma is vacuous (F-b3), so GAP-β = (β-a).
  (c) Theorem A (GAP-C §13): if the root call of search(p) is stable, the lowest region of its first sptl pass lies in W_p(G')
      and, if closed (no (α)), is productive (learns a new tangle or finds a dominion).
  (d) Lemma O0 (GAP-C §6): at the start of search(p) there is no orphan. Lemma O1 (GAP-C §6) as stated there.
  (e) Lemma OPP-EXIT (GAP-C §11), with conclusion π(o) ∉ Z_τ: the SCC C_τ extracted at a closed top τ meets W_{1-p} only
      where the opponent's winning move is an edge the region forgives.
  (f) Lemma K0 (GAP-C §18b): K(G') holds when W_p(G') ≠ ∅ and K(R_end) fails, with edges of G'.
  (g) Phases ≤ D + 2, where D ≤ n is the number of searches that find a dominion (GAP-A-M §21c; run() loops C5-DTL.md
      lines 141-142; --dtl is non-interleaved).
  (h) First-Difference Lemma (GAP-A-M §21d), stated on the call log with repeated sptl passes (dtl.cpp 870-874) deleted.
  (i) Lemma DV*-MONO (GAP-A-M §21h), reading INF as "never dropped".
  (j) The per-context LRN budget: at most n(n + 1) LRN transitions per distinct context per phase (GAP-A-M §21j), with
      REFEREE-2's reading of LRN (R2-PROVED2 §10).
  (k) Conditional bound: if (SPP) "searches per phase ≤ |G'|" holds for every order datum, then A_DTL makes ≤ n(n + 2)
      searches and runs in O(n^10 (m + n²)) word operations, and unit cost equals bit cost under TARGET.md §3.
- Signatures: REFEREE docs/referee/R-PROVED2.md (referee 50f2546; comparison §C ef6cf37, §C5 88d8e4c): (a),(c),(d),(f),(g),(i),
  (j),(k) SIGN; (b),(e),(h) SIGN WITH GAPS, all closed. REFEREE-2 docs/referee-2/R2-PROVED2.md (referee-2 581902f; comparison
  §13 72d1cd2): (a),(d),(g),(i),(j) SIGN; (b),(c),(e),(f),(h),(k) SIGN WITH GAPS, all closed. Independent (each read the other's
  report only after pushing its own). No REJECT. After comparison no gap of the packet is open in either report.
- Gaps (union of both reports and comparisons). G-R5-1..7 are closed in the reports and imported into the author's text
  (l-alg d67c5c8); G-R5-8 lists dependencies:
  G-R5-1 B-thr: escapes solved before the search via O0 (REFEREE G-b1 = REFEREE-2 G-b3); "last escape" = the pop at which it
         leaves the current call's context chain (REFEREE G-b2); tangles created in the current search cannot recur in a
         later context of that search (REFEREE-2 G-b1, closed R2 §13.2, signed by REFEREE §C5, dtl.cpp 879-880, 885, 914-955).
  G-R5-2 Theorem A: read on the first sptl pass with premise "Z_k closed" (REFEREE-2 G-c1, same reading in REFEREE §c).
  G-R5-3 OPP-EXIT: conclusion π(o) ∉ Z_τ; proof needs the tangle-rule and top cases (G-e1, G-e2).
  G-R5-4 K0: edges of G' (REFEREE-2, as R2-STEP5 G1).
  G-R5-5 FDL: log alignment with repeated sptl passes deleted (G-h1; closed by REFEREE-2 §13.1, accepted by REFEREE §C).
  G-R5-6 DV*-MONO: INF read as "never dropped" (R-i, adopted by both).
  G-R5-7 (k): Lemma W needs SCC1 (G-k1, closed by (a)); DTL-proof §3(c) off by a factor 2, harmless (G-k2).
  G-R5-8 Dependencies: DTL-proof §2.3 K4 and K5(ii) (Theorem A) and DTL-proof §3 (b)-(e), checked in outline only for
         this use; code facts C1-C6 of docs/referee/R-STEP5.md §0 (REFEREE hypothesis 5); (α) and Case B (GAP-K') remain
         open (REFEREE hypothesis 3), which is why (c) is conditional on no (α). Priorities renumbered to ≤ 2n + 2 under L26
         (REFEREE's (k) text says ≤ n; the O(log n)-bit conclusion is unchanged). Nothing Lean-checked.
- Finding outside the signed statements: DTL-proof.md K5 (i)/(iii) is FALSE as written (REFEREE-2, docs/referee-2/
  R2-PROVED2/k5.pg, 4 vertices; confirmed by REFEREE; pinned Oink solves k5.pg in 1 iteration, verified: the run is correct,
  the lemma statement is wrong). Corrected form in R2-PROVED2 §3. Theorem A uses only K4 and K5(ii) and is unaffected; the
  definition of (α) is to be restated against the corrected K5 (GAPS G-K5).
- Scope: (a)-(f) support GAP-C but do not establish completeness (GAP-K / K-in open). (g)-(k) do not establish GAP-A: (k) is
  conditional on (SPP), which is DATA only. Gauntlet step 4 stays open.
