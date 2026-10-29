# R-N5-FBCK: REFEREE report on packet P-N5-FBCK (L-NEW box 49: Facts K1-K3, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, Theorem FB-C^K, Corollaries)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 2026-10-28 23:44Z by date -u).
- Object and pin: docs/new/P-N5-FBCK-box49.md, sha1 7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f, 131 lines, author L-NEW successor 30: the same
  sha1 at l-new 0e63596d (an ancestor of origin/claude/l-new) and at the l-new head. Not on trunk at my fetch. Quote base 6d863a4d.
- Probe and data runs 2026-10-28T23:46Z-23:53Z; report written 2026-10-28T23:54Z-23:55Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on FBCK on my tree, on trunk or on origin/claude/referee-2 (names re-listed in the same
  turn as the fetch, 23:54Z: 0 / 0 / 0). No lane code run or imported (experiments/new/box49/fbconf.py, quotecheck3.py untouched). D1.
- Premises read against their text at 6d863a4d: RESULTS R71 (l. 3712, 3715) with its source P-N5-FBC-box47 §0-§1 (sha1 32d3776c, the pin);
  P-N5-HONFF-box47 §0-§1 (FB-RISE (a) items 1-3, question Q-A); RESULTS R73 with P-N5-EPC-box48 §3 (sha1 9f48ded7, the pin: SAT-FB, SAT-FB1,
  FB-C′); SPEC S2, S4c, FIX 3; READER-INV and its Lemma (one state) in docs/referee/R-N5-READER.md at e83fd19d §1.
- Quotes: all 9 [Q path@commit:lines] passages verbatim in their cited ranges (own checker scratch/flip_quotes.py: QUOTES 9 FAILED 0).
- Tool: scratch/fbck_probe.py (sha1 deeb2391…; own engine rl_engine; exact levels by simple-path enumeration in H^K_C via ff_probe, as my
  predecessor's fbc_probe.py; checks K1-K3, REAL, MONO, RISE, SATB, SATW, SATFB, SATFB1, THM, COR1; MUT 1-4). Logs scratch/fbck_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 | Facts K1, K2, K3 (and LEV^K_C ≥ 0, non-decreasing; 𝒞^K_f is the image of 𝒞_f) | SIGNED |
| §1 | Lemma FB-RISE^K | SIGNED |
| §1 | Lemma SAT^K (both parts) | SIGNED |
| §1 | Lemma SAT-FB^K | SIGNED |
| §1 | Corollary SAT-FB1^K | SIGNED |
| §2 | Theorem FB-C^K: f ≤ n_K·|𝒞^K_f(P)| | SIGNED |
| §2 | Corollary (i) (implies R73's FB-C′) | SIGNED |
| §2 | Corollary (ii), as an IMPLICATION from its three hypotheses | SIGNED as an implication, with one implicit step made explicit (FBCK-N1); its "(READER-INV gives this for a reader satisfying (R))" is true for ONE reader as READER-INV is stated; READER-INV itself is refereed by one referee only and not landed |
| §3, §4 | READING / OPEN / DATA | not signed. §4's figures reproduced where checked (§4 below) |
No gap. Notes FBCK-N1..N4. Theorem FB-C^K bounds f by a count of K-configurations and does not bound that count (FB-LIN OPEN); not M3, not a
step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. §0 re-derived
- K1 ✓: if x ∈ K is reached from an Even choice vertex e, so is every y ∈ succ(x). Hence the honest play from x ∈ K stays in K, and λ(x) ∈ K ✓.
- K2 ✓: an Even vertex of out-degree ≥ 2 is in K (0-edge path); S2 gives Iσ(x) ⊆ succ(x) ∖ {σ(x)} = ∅ for out-degree 1 ✓.
- K3 ✓: an in-phase fallback is Even's (FIX 3) and fires with Iσ ≠ ∅, which by K2 needs an Even vertex in K. (Remark: K ≠ ∅ forces n_K ≥ 2,
  since an Even choice vertex has two distinct successors in K.)
- H^K_C ✓: at a K-C-state the honest play from x ∈ K uses σ_k at Even vertices (all their edges are in H^K_C), C at Q_K and the unique
  successor at the other Odd vertices of K, all inside K (K1). So it is a play of H^K_C ✓.
- LEV^K_C ✓: defined at every state; non-decreasing on P since H^K_C and λ are fixed on P and Ξ is pointwise non-decreasing (MON) ✓;
  LEV^K_C ≥ 0 since a 0-edge path is x = u a cycle node with Ξ_k(u) = (u, ∅, 0) on the phase ✓.
- 𝒞^K_f(P) is the image of 𝒞_f(P) under restriction to Q_K ✓, so |𝒞^K_f| ≤ |𝒞_f| ✓.

## 2. §1 re-derived (against R71 / HONFF / R73 text, step by step)
- FB-RISE^K ✓. The landed proof (FBC §1 l. 51-56, HONFF §1 items 1-3) is local at x: it reads the edge (x, z), the bound Ξ_t(z) ⪰ value(r′),
  and, at Even x, S4c's rule and Lemma P's Case A at x, σ_t(x), z, z* (all in succ(x)), (V1)/(V2) at x, (MON) and λ_{t+1} = λ. With x ∈ K,
  every vertex named lies in K (K1). The only use of the configuration is z = σ̄_t(x) at an Odd x ∈ Q_K, which a K-C-state gives. r = x → z →
  r′ with r′ an H^K_C-path from z ∈ K of ≤ LEV^K_C(t) edges gives Ξ_t(z) ⪰ value(r′) by the definition of LEV^K_C (quantified over x ∈ K) ✓.
  - Odd case, subcase λ(x) = x: "Ξ_t(z) has cycle node x while value(r′) has cycle node u ≠ x; Ξ_t(z) ⪰ value(r′) makes x better than u"
    ✓ (z ∈ K, u ∈ K). Even cases 2, 3a, 3b ✓ verbatim; 3b's "z*'s play returns to x" stays in K ✓.
- SAT^K ✓. First part: the honest play from x ∈ K at a K-C-state follows the simple H^K_C-path r_x to the first visit of λ(x), and
  Ξ_t(x) = value(r_x) ⪯ B^K_C(x) ✓; simple paths of G[K] have ≤ n_K − 1 edges, so LEV^K_C(t) = n_K − 1 gives Ξ_t ⪰ B^K_C on K ✓. Second part:
  the (MON) sandwich on K ✓. (R71's window bound t′ − t ≤ 4n(n − 1) is dropped; nothing below needs it ✓.)
- SAT-FB^K ✓. Ξ_{t+1} = Ξ_t on K (SAT^K, t + 1 ≤ t′). Even x ∉ K: K2. Even x ∈ K: succ(x) ⊆ K, so S2 at t + 1 reads only values on K, equal to
  those at t; R73's two cases then hold verbatim (EPC §3 l. 100-103) ✓. The rest (S4a keeps σ; S4b moves τ, or S4c fires for Odd, or N5 stops;
  τ constant on P) is R73 verbatim and does not involve the frame ✓.
- SAT-FB1^K ✓ (R73's proof with K-C-states; it needs only that the second source is a K-C-state after the first).

## 3. §2 re-derived
- Theorem FB-C^K ✓. K = ∅: f = 0 (K3). Else per C ∈ 𝒞^K_f(P): unsaturated sources have LEV^K_C strictly rising between consecutive ones
  (FB-RISE^K + monotonicity) in {0, …, n_K − 2}: ≤ n_K − 1; saturated ≤ 1 (SAT-FB1^K); so ≤ n_K; sum over C ✓.
- Corollary (i) ✓: n_K ≤ n and |𝒞^K_f| ≤ |𝒞_f|.
- Corollary (ii), as an implication ✓, with FBCK-N1. K(G′) = K(G) ✓: G′ adds no Even choice vertex, and no old vertex reaches H. f and the
  phases are equal by the third hypothesis. For 𝒞^K_f(P) one also needs σ̄′ = σ̄ on Q_K (Q_K consists of old vertices). "The run on the old
  vertices is unchanged" does not state this. It is TRUE under the first hypothesis, by the argument of READER-INV's one-state Lemma (a)
  extended to H: no old vertex reaches H, so in S1 every cycle test and choice DFS from an old vertex sees only old vertices; a cycle node in H
  kills only vertices of H (its reach set lies in H); the restriction steps of (iii) at an old cycle node only add H vertices to M or delete
  edges of H vertices; the BFS over predecessors discovers H vertices only from H vertices (their predecessors lie in H), so first discoveries of
  old vertices are unchanged; ranks change by an order-preserving relabelling. So σ̄′|V = σ̄ and Ξ′|V = Ξ (as triples) at every state.

## 4. Data (scratch/fbck_logs/; 0 failures in every MUT=0 run)
| run | N5 runs | fallback phases | f | Σ|𝒞_f| / Σ|𝒞^K_f| | phases with n_K < n | RISE checks (unsat.) | saturated FB (SATFB checks) | SATB / SATW | exact-level phases skipped (budget) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| named.txt: box49/inst/l121_* (9), farrise25_n32, wd16_s2, zcl_rx_n32, long121_n40, swlin_kill_n26, l121reader_n41; given + S3 | 27 | 16 | 145 | 71 / 68 | 5 | 44 (44) | 0 | 3 / 3 | 12 |
| lib1140_part00-03 (fbc_lib.txt, n ≤ 40; given + S3 + 2 random) | 2,725 | 575 | 1,956 | 710 / 710 | 90 | 870 (662) | 208 | 707 / 508 | 203 |
| lib41.txt (n ≤ 48; given + S3 + 1 random) | 726 | 206 | 901 | 261 / 259 | 17 | 254 (215) | 39 | 206 / 166 | 104 |
| rand3000.txt (rand_ck, n 6-18, k ≤ 6) | 9,000 | 315 | 315 | 315 / 315 | 145 | 315 (3) | 312 | 627 / 313 | 0 |
- THMtot (f ≤ n_K·|𝒞^K_f|, needs no levels) and COR1 are checked on EVERY fallback phase, including the budget-skipped ones; K1, K2 (and
  Iσ ⊆ K at every state), K3 (1,277 phases with K = ∅ checked: no fallback) and REAL on every run.
- §4 figures reproduced: max fallbacks from one K-configuration / n_K = 0.781 (farrise25_n32, sha1 8941d1c9: 25 of 32), as the packet's 0.78;
  l121_cf35_39: f = 8, |𝒞_f| = 8, |𝒞^K_f| = 5 (vertex 40 ∉ K, n_K = 40); l121_cf_emb12: |𝒞^K_f| = 8 = f (n_K = n = 41); l121_a: 5.
- Vacuity: every hypothesis met (unsaturated and saturated sources, K-C-state returns, K = ∅ phases). Thin spot (FBCK-N2): the theorem is
  STRICTLY stronger than R73's FB-C′ only when n_K < n or |𝒞^K_f| < |𝒞_f|. The first happens in 90 of 575 fallback phases (lib1140); the
  second only on the dressing l121_cf35_39 and 2 phases of lib41 in my data.

## 5. Mutation controls (scratch/fbck_logs/mut*.txt; named set farrise25_n32, wd16_s2, zcl_rx_n32, swlin_kill_n26 unless said)
| MUT | change | result |
| --- | --- | --- |
| 1 | FB-RISE^K demanded with + 2 | BITES: 51 of 53 |
| 2 | configuration read at t + 1 instead of t | does NOT bite on the named set (recorded) |
| 3 | THM per-configuration bound n_K // 2 | BITES: 3 (farrise25_n32 among them) |
| 4 | engine with S4c's (Ξ, w)-MINIMUM | BITES: RISE 3 (named); on rand3000: SATFB 20, SATFB1 12, RISE 1 |

## 6. Notes (for L-NEW's fixes file; none changes a verdict)
- FBCK-N1 (Corollary (ii), implicit step): add "and σ̄ on the old vertices" to the third hypothesis, or give the closure argument of §3 (no old
  vertex reaches H, so S1's choices at old vertices are unchanged). The parenthesis "(READER-INV gives this for a reader satisfying (R))" is
  right for ONE new vertex o (Odd, no predecessors), which is what READER-INV states; for a set H with edges inside H it is not READER-INV's
  statement, and (R) must then be read for every Odd vertex of H.
- FBCK-N2 (thin spot): in natural data the K-frame rarely improves on R73 (§4). Its use is the reader-proofness of §2 (ii); the open case of §3
  (an old Even choice vertex pointing at a reader) is exactly where it does not help (l121_cf_emb12: 8 = f).
- FBCK-N3 (wording): SAT^K omits R71's window bound t′ − t ≤ 4n(n − 1); correct, since FB-C^K counts saturated sources through SAT-FB1^K.
  SAT-FB1^K needs only that the second source is a K-C-state, not that it is saturated (as in R73).
- FBCK-N4 (premise status): Corollary (ii)'s source READER-INV (R-N5-READER §1) has one referee (L-COMP agreed on data); the corollary is an
  implication and stays one until READER-INV is refereed twice.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-FBCK.md (this file), scratch/fbck_probe.py, scratch/fbck_logs/ (named, lib1140 ×4, lib41, rand3000, mut1-4, mut4_rand3000).
- FINDINGS: every item SIGNED, no gap; Corollary (ii) SIGNED as an implication with its implicit step (σ̄ unchanged on old vertices) proved
  (FBCK-N1); the K-frame gain is rare in natural data (FBCK-N2).
- NEEDS: Lead: route FBCK-N1..N4 to L-NEW's fixes file after REFEREE-2 reports; the FBCK §C word when REFEREE-2's report is pushed.
