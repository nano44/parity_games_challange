# Draft RESULTS R81 (Lead, 2026-10-29 01:38Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C90 (Lead reviewed 01:41Z by date -u: FBCK-N1's σ̄|V step kept inside signed item (i), since both referees' verdict entries for Corollary (ii) include it) (rev. 02:09Z by date -u: C90 N-2, N-3)

### R81 [refereed-only] N5 on EVERY game, inside one phase: with K the vertices reachable from an Even vertex of out-degree ≥ 2 (K is closed under successors, so the honest play from a vertex of K stays in K; every Even vertex outside K has out-degree 1; K = ∅ leaves no in-phase fallback: Facts K1-K3), n_K := |K| and a K-configuration C = σ̄|Q ∩ K (Q the Odd vertices of out-degree ≥ 2), an in-phase S4c fallback from a K-C-state raises the level LEV^K_C, taken over the simple paths of the frame H^K_C (G[K] with every Odd vertex of K cut to its σ̄_C edge), to at least min(LEV^K_C + 1, n_K − 1) (Lemma FB-RISE^K); LEV^K_C = n_K − 1 at a K-C-state t gives Ξ_t = B^K_C on K, and Ξ constant on K from t to any later K-C-state of the phase (Lemma SAT^K); a fallback from such a saturated K-C-state is followed by the end of the phase or by no further K-C-state of it (Lemma SAT-FB^K), so per phase and K-configuration at most one in-phase fallback has a saturated source (Corollary SAT-FB1^K); hence in every phase P, f ≤ n_K·|𝒞^K_f(P)|, f the number of in-phase S4c fallbacks of P and 𝒞^K_f(P) the K-configurations of their sources (Theorem FB-C^K), which implies RESULTS R73's Theorem FB-C′, f ≤ n·|𝒞_f(P)| (Corollary (i)); and, signed only AS AN IMPLICATION (Corollary (ii)): if G′ is G plus new vertices H with no edge from an old vertex into H, no Even vertex of out-degree ≥ 2 in H, and the run on the old vertices, the fallbacks and the phases unchanged (an assumption for a general H; for ONE added Odd vertex with no predecessors satisfying (R) it is supplied by REFEREE's Theorem READER-INV, which has one referee and is NOT landed), then n_K, 𝒞^K_f(P) and f are the same for G′ as for G, the step σ̄′|V = σ̄ following from the first hypothesis alone (2026-10-28) — a REDUCTION of f to the number of K-configurations at the fallback sources of a phase (that number is not bounded here; FB-LIN, f ≤ n per phase, is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C90.md, checker PENDING)
- Object (L-NEW successor 30, Opus 5.5; frozen, unchanged during review): packet P-N5-FBCK, docs/new/P-N5-FBCK-box49.md, sha1
  7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f (l-new freeze 0e63596d, 2026-10-28T23:25:01Z; quote base 6d863a4d; 9 quotes, quotecheck3.py
  "quotes=9 bad=0"; both referees measured the pin), RESULTS R71 (a), (b) and R73's SAT-FB / SAT-FB1 / FB-C′ re-run on the successor-closed
  set K; source docs/new/N5-READER-box49.md §7-§8 (working note). The referees' notes are collected by the lane in
  docs/new/P-N5-FBCK-fixes-box49.md (l-new e0fda64f, sha1 19237624d32db379db858ea961861bd094441db1, L-NEW successor 30: F1-F8 for
  FBCK-N1 = N-FBCK-1, FBCK-N2, FBCK-N3, FBCK-N4, N-FBCK-2..5, in REFEREE-2's §C C.4 order; 25 quotes checked by script,
  experiments/new/box49/quotecheck3.py "quotes=25 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the file's sha1);
  on trunk; repairs only, "No signed statement changes. Corollary (ii) stays an IMPLICATION." (fixes l. 6): F1 replaces Corollary (ii)'s
  third bullet and adds one sentence after the bullets (FBCK-N1); F3 adds a sentence after Lemma SAT^K (FBCK-N3); F2, F4-F8 are records and
  change no statement. The statements below are in that repaired wording.
  Setting (every game): as in RESULTS R71 (N5 = SPEC S1-S5 with FIX 3, an in-phase fallback being Even's; Ξ_k the value of the honest
  (σ_k, σ̄_k)-play; λ its cycle-node map; phases as in RESULTS R38 (a), λ and τ constant on one; value(r) := (u, P(r), |r|) for a simple path
  r ending at a cycle node u of λ; f := the in-phase S4c fallbacks of a phase; Q := the Odd vertices of out-degree ≥ 2; R71's configurations
  C = σ̄|Q, H_C, LEV_C, B_C, 𝒞_f(P)). K := the vertices reachable in G, by a path with ≥ 0 edges, from an Even vertex of out-degree ≥ 2;
  n_K := |K|; Q_K := Q ∩ K. A K-CONFIGURATION is C = σ̄|Q_K, and k is a K-C-STATE if σ̄_k|Q_K = C. H^K_C := G[K] with every Odd v ∈ K cut to
  its one edge σ̄_C(v) (C(v) for v ∈ Q_K, the unique successor otherwise). LEV^K_C(k) := the largest j ≤ n_K − 1 such that Ξ_k(x) ⪰ value(r)
  for every x ∈ K and every simple path r of H^K_C with ≤ j edges from x to a cycle node of λ; B^K_C(x) := the maximum of value(r) over the
  simple H^K_C-paths r from x ∈ K to a cycle node of λ. 𝒞^K_f(P) := the K-configurations of the sources of P's in-phase S4c fallbacks. For
  Corollary (ii): G′ is G plus new vertices H, V the old vertices, primes for G′'s objects.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1-S5 with FIX 3 (S2's Iσ,
  S4c's rule); the standing premise 1E-N3, form P1 (RESULTS R57); RESULTS R71's setting, (a) Lemma FB-RISE_C and its proof (P-N5-FBC-box47
  §1, sha1 32d3776c…, the pin), (b) Lemma SAT_C and its proof (first part and the (MON) sandwich only; its 4n(n − 1) window is not used,
  N-FBCK-4 = F7, FBCK-N3 = F3); R71's premises (MON) (RESULTS R15 (a) with R15 (d)), RESULTS R17 (a) (V1), (V2), R17 (b) Lemma P's Case A
  with Ω := Ξ_t (RESULTS R70's Q-A, YES by both of its referees), R38 (a); RESULTS R73 (d) Lemma SAT-FB and its proof (P-N5-EPC-box48 §3,
  sha1 9f48ded7…, the pin; its last step in the post-fix R6 form, without HON-FB), Corollary SAT-FB1, Theorem FB-C′. NOT landed, for Corollary (ii) = item (i) only: REFEREE's Theorem READER-INV under (R) (docs/referee/R-N5-READER.md at e83fd19d, §1; one referee), which item (i) does
  not use as a premise, only as the source that supplies Corollary (ii)'s third hypothesis in one case:
  (a) Facts K1-K3 (§0). K1: K is closed under successors; hence the honest play from x ∈ K stays in K at every state, λ(x) ∈ K, and at a
      K-C-state the honest play from every x ∈ K is a play of H^K_C. K2: every Even vertex outside K has out-degree 1, so Iσ_k(x) = ∅ at
      every state for Even x ∉ K (S2). K3: if K = ∅ there is no in-phase fallback (an in-phase fallback is Even's, FIX 3, and needs Iσ ≠ ∅).
  (b) The setting facts (§0; REFEREE's K1-K3 row, REFEREE-2's own row "LEV^K_C ≥ 0 and non-decreasing on P (setting sentences)", the §C
      joint row "K1-K3 (with LEV^K_C ≥ 0, non-decreasing; 𝒞^K_f the image of 𝒞_f)"): LEV^K_C is defined at every state of P and is
      non-decreasing along P (H^K_C and λ fixed on P; (MON)); LEV^K_C ≥ 0 (a 0-edge path has x = u a cycle node, and Ξ_k(u) = (u, ∅, 0)
      throughout the phase); 𝒞^K_f(P) is the image of R71's 𝒞_f(P) under restriction to Q_K, so |𝒞^K_f(P)| ≤ |𝒞_f(P)|.
  (c) Lemma FB-RISE^K (§1): let t → t + 1 be an in-phase S4c fallback of P whose source t is a K-C-state. Then
      LEV^K_C(t + 1) ≥ min(LEV^K_C(t) + 1, n_K − 1). (R71 (a)'s proof with x ∈ K, H^K_C for H_C and n_K for n; the configuration is used only
      at an Odd x ∈ Q_K, and every vertex the proof names lies in K by K1.)
  (d) Lemma SAT^K (§1, with F3): if t is a K-C-state with LEV^K_C(t) = n_K − 1, then Ξ_t = B^K_C on K; if t < t′ are K-C-states of P with
      LEV^K_C(t) = n_K − 1, then Ξ is constant on K on the states t, …, t′. F3: "R71 (b)'s window bound t′ − t ≤ 4n(n − 1) is not used:
      saturated sources are counted by SAT-FB1^K, which needs only that the second source is a K-C-state after the first (not that it is
      saturated)."
  (e) Lemma SAT-FB^K (§1): let t be a K-C-state of P with LEV^K_C(t) = n_K − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then
      t + 1 is the last state of P, or P has no K-C-state after t. (Iσ_{t+1} = ∅ at Even x ∉ K by K2 and at Even x ∈ K since succ(x) ⊆ K
      (K1); the rest is R73's text. This is the one step that needs more than restriction to K, N-FBCK-2 = F5.)
  (f) Corollary SAT-FB1^K (§1): for every phase P and K-configuration C, at most one in-phase fallback of P has a saturated K-C-state as its
      source.
  (g) Theorem FB-C^K (§2): in every phase P of N5 on every game, f ≤ n_K·|𝒞^K_f(P)|. (K = ∅: f = 0 by K3. Otherwise, per C ∈ 𝒞^K_f(P), at
      most n_K − 1 unsaturated sources, LEV^K_C strictly rising between consecutive ones in {0, …, n_K − 2}, and at most 1 saturated one
      (SAT-FB1^K); sum over C.)
  (h) Corollary (i) (§2): n_K ≤ n and |𝒞^K_f(P)| ≤ |𝒞_f(P)|, so FB-C^K implies RESULTS R73's Theorem FB-C′ (f ≤ n·|𝒞_f(P)|).
  (i) Corollary (ii) (§2, repaired by F1), signed AS AN IMPLICATION by both (REFEREE: "SIGNED as an implication"; REFEREE-2: "SIGN AS AN
      IMPLICATION from its three bullets"). Let G′ be G plus new vertices H such that: no old vertex has an edge into H; no Even vertex of H has
      out-degree ≥ 2; the run on the old vertices, the fallbacks and the phases are unchanged. "This is an ASSUMPTION for a general H, with (R)
      read for every Odd vertex of H. READER-INV supplies it for ONE added Odd vertex with no predecessors that satisfies (R)." Then
      K(G′) = K(G) (no new Even choice vertex is added, and no new vertex is reachable from an old one), and "Moreover σ̄′|V = σ̄ and Ξ′|V = Ξ
      at every state, by the first bullet alone. No old vertex reaches H, so S1's choices at old vertices are unchanged (REFEREE's proof,
      R-N5-FBCK §3; checked by REFEREE-2 against SPEC S1 and on 100,000 cases). Hence 𝒞^K_f(P), which reads σ̄ on Q_K ⊆ V, is unchanged." So
      n_K, 𝒞^K_f(P) and f are the same for G′ as for G. The step σ̄′|V = σ̄ (Ξ′|V = Ξ as triples, ranks relabelled order-preservingly; the
      argument of READER-INV's one-state Lemma (a) extended to H) is part of this item: REFEREE's report signs (ii) "with one implicit step made
      explicit (FBCK-N1)" and proves it (§3), and REFEREE-2's §C joint verdict for (ii) reads "SIGN as an implication; the σ̄ step is proved
      (C.3)" after checking the argument step by step against SPEC S1 (i)-(vi) ("ACCEPTED"; its own N-FBCK-1 reading SUPERSEDED). It uses
      the first hypothesis only, not READER-INV. The corollary's conclusion stays an IMPLICATION from its three hypotheses, and stays one until
      READER-INV is refereed twice (FBCK-N4 = F4, agreed by REFEREE-2).
- Not signed: Corollary (ii) as the packet wrote it, as an application of READER-INV to a general H: its parenthesis "(READER-INV gives this
  for a reader satisfying (R))" is right for ONE new Odd vertex with no predecessors, which is what READER-INV states, not for a set H with
  several readers, Even vertices or edges inside H (FBCK-N1 = N-FBCK-1, both referees); and its implicit step (σ̄ on the old vertices) was
  not stated by "the run on the old vertices is unchanged". Not false; repaired by F1 into (i). Repeated single-reader additions would need H
  acyclic, each new vertex without predecessors when added, and (R) at each step; not proved (REFEREE-2 N-FBCK-1). Also not signed (packet
  §3-§4, as the packet says): the DATA, including Corollary (ii)'s closing instance sentence (RESULTS R71 / R73's |𝒞_f(P)| inflated by a
  reader on l121_cf35_39, 5 → 8 = f; DATA, reproduced by both, below); the READING and OPEN items of §3: CONJECTURE FB-C° in the read frame
  of N5-READER §8 (OPEN; an Even choice vertex puts everything it reaches into K, even along an edge it never uses: on l121_cf_emb12
  |𝒞^K_f| = 8 = f), and FB-LIN, which FB-C^K does not imply.
- Referee strengthening (NOT part of this entry; REFEREE's remark outside its verdict table; REFEREE-2 AGREED in its §C only): K ≠ ∅ forces n_K ≥ 2, since an Even choice vertex has two distinct successors
  in K (REFEREE's remark under K3, report §1); REFEREE-2 in its §C: "AGREED (an Even choice vertex has two distinct successors in K). It is
  not in my report."
- Honest limits: (i) A REDUCTION, not a bound: f is bounded by n_K times the number of K-configurations at fallback sources; |𝒞^K_f(P)| is not
  bounded here, FB-LIN (f ≤ n per phase) is OPEN, and the CONJECTURE FB-C° in the read frame is OPEN (packet §3; fixes "What this file does
  not do"). Nothing here bounds N5's running time. (ii) READING (Lead): FB-C^K does not shrink FB-LIN. Two of L-NEW's dead ends
  (docs/new/N5-READER-box49.md §9, l-new 95714e3e; L-NEW's records, not refereed): MONO-CONF ("there is an order on K-configurations in which
  the configurations at successive fallback sources of a phase never go back") DEAD on the plain long121_n40 (sha1 c667c085…; phase [1, 122],
  8 fallback sources with K-configurations C0 C1 C2 C3 C4 C1 C2 C3) and on njb_reabs65_n48 (sha1 3388d0be…; phase [2, 68], f 29, 2
  alternating K-configurations); SMALL-CK ("|𝒞^K_f(P)| ≤ g(n) with g smaller than the trivial f") DEAD by
  experiments/new/box49/inst/l121_cf_emb12.pg (sha1 5440021b27bb0ab23cd4db682ae73bfbf5aaf39a): an embedded reader (the old Even vertex 12 →
  o) lifts |𝒞^K_f| from 5 to 8 = f with the run SAME (L-NEW's DATA; READER-INV does not cover it, o has a predecessor), so a bound
  |𝒞^K_f| ≤ g(n) gives f ≤ g(n + 1) on the base game. Both referees reproduce |𝒞^K_f| = 8 = f, n_K = n = 41 there. Plain readers cannot
  inflate the K-count (Corollary (ii), an implication); edges from an Even choice vertex can. (iii) The K frame rarely improves on R73 in
  natural data (FBCK-N2 = F2): FB-C^K is strictly stronger than FB-C′ only when n_K < n or |𝒞^K_f| < |𝒞_f|; REFEREE: n_K < n in 90 of 575
  fallback phases of lib1140, |𝒞^K_f| < |𝒞_f| only on the dressing l121_cf35_39 and 2 phases of lib41; REFEREE-2: the gain appears when
  vertices outside K are added (lib41 + 5, no old → new edges: Σ |𝒞_f| / Σ |𝒞^K_f| 414 → 257, |𝒞^K_f| < |𝒞_f| in 76 of 205 phases). Its use
  is reader-proofness, not a better count on undressed games. (iv) The closure of K is needed (N-FBCK-2 = F5): REFEREE-2's control open1
  (K′ := the Even choice vertices and their successors, not closed) bites 2,528 + 1,281 on its dressed k4 and random kO sets, among them
  795 + 418 SAT, 1 + 1 SATFB and 1 SATFB1 failures; REFEREE's §C: "ACCEPTED, stronger evidence". (v) The per-configuration bound n_K is not
  approached (N-FBCK-3 = F6): max fallbacks from one K-configuration / n_K = 0.781 (farrise25_n32, sha1 8941d1c9…: 25 of 32; REFEREE, as the
  packet's 0.78) and 0.75 (wd16_s2: 12 of 16; ccl_fbx_n32 + 5: 24 of 32; REFEREE-2); REFEREE-2's nk1 ((n_K − 1) per configuration) does not
  bite, REFEREE's MUT3 (n_K // 2) bites 3. SAT-FB^K's alternative "P has no K-C-state after t" never occurs on its own in REFEREE-2's data
  (every saturated case, 36 + 20 + 6,188, has a later K-C-state and t + 1 the last state of P), so it rests on the proof alone.
- Data (DATA, not proof): REFEREE (successor 17; own docs/referee/scratch/fbck_probe.py (sha1 deeb2391…) on its engine rl_engine, exact levels
  by simple-path enumeration in H^K_C; lane code not run; 0 failures in every MUT=0 run): named (box49/inst/l121_* (9), farrise25_n32,
  wd16_s2, zcl_rx_n32, long121_n40, swlin_kill_n26, l121reader_n41; given + S3) 27 runs, 16 fallback phases, f 145, Σ |𝒞_f| / Σ |𝒞^K_f|
  71 / 68; lib1140_part00-03 (n ≤ 40; given + S3 + 2 random) 2,725 runs, 575 fallback phases, f 1,956, 710 / 710, "RISE checks (unsat.)"
  870 (662), 208 saturated fallbacks; lib41 (n ≤ 48; given + S3 + 1 random) 726 runs, 206 fallback phases, f 901, 261 / 259; rand3000
  (n 6-18, k ≤ 6) 9,000 runs, 315 fallback phases, f 315, 312 saturated. THM and COR1 on EVERY fallback phase (also the 12 + 203 + 104
  phases whose exact levels were skipped at the budget); K1, K2 (and Iσ ⊆ K at every state), K3 (1,277 phases with K = ∅: no fallback) and
  REAL on every run. Reproduced: l121_cf35_39 f = 8, |𝒞_f| = 8, |𝒞^K_f| = 5 (vertex 40 ∉ K, n_K = 40); l121_cf_emb12 |𝒞^K_f| = 8 = f
  (n_K = n = 41); l121_a 5. Controls: MUT1 (FB-RISE^K with + 2) bites 51 of 53; MUT2 (configuration read at t + 1) does not bite on the named
  set; MUT3 above; MUT4 (S4c's (Ξ, w)-MINIMUM) bites RISE 3 (named) and SATFB 20, SATFB1 12, RISE 1 on rand3000. REFEREE-2 (successor 19;
  own docs/referee-2/R2-N5-FBCK/fbck_check.py, percase.py, sbar_ext.py on its lane's Runner (si.py); lane tools not run; every non-mutation
  run 0 violations; LEV^K_C exact by enumeration, or min(LEV^K_C, D) exactly in deep mode): named (18 runs) 15 fallback phases, f 117,
  78 / 75; lib41_noref × 3 starts (1,230 runs) 240, f 1,103, 299 / 297; lib41 dressed + 5 (820 runs) 205, f 887, 414 / 257; random dressed
  k4 and kO (60,000 runs each) 1,743 and 1,944; random k2 (60,000) 1,712; random kO (30,000) 847 fallback phases; K3 on 409 + 267 + 6,434
  phases with K = ∅; RISE exact at 276 + 213 + 6 + 6,249 sources, 401 + 352 + 98 more in deep mode, 426 + 322 + 13 undecided at the cap;
  THM and CNT (≤ n_K sources per K-configuration) decided in every fallback phase. Same instance figures as REFEREE on l121_cf35_39,
  l121_cf_emb12, l121_a; swlin_kill_n26: 6 fallbacks, |𝒞^K_f| 3. σ̄ extension (sbar_ext.py; random G plus random H, Even H vertices of
  out-degree ≥ 2 included, random σ): S1's σ̄ and Ξ agree on V in 100,000 / 100,000 cases (h = 4 and h = 10); control MUT=backedge (one old →
  H edge) 8,203 differences in 20,000. Controls: plus2 bites 4 + 6, tau (Q_K cut to τ instead of C) 263 + 264, open1 above, nk1 does not
  bite. The packet's §4 (lane, experiments/new/box49/fbconf.py): KVIOL 0 on named (17 runs), lib41 (1,047) and L-RED (311). Counts differ by
  start choice (N-FBCK-5 = F8): lib41 Σ |𝒞_f| / Σ |𝒞^K_f| 303 / 301 (packet, 1,047 runs), 299 / 297 (REFEREE-2, 1,230), 261 / 259 (REFEREE,
  726); no conflict, no violation on any side.
- Signatures: REFEREE docs/referee/R-N5-FBCK.md (report f2d22ad7, sha1 913f31be56428f515652a482750cbd8c8cd3e67c there; §C 6b752e89; successor
  17): K1-K3 (with LEV^K_C ≥ 0, non-decreasing; 𝒞^K_f the image of 𝒞_f), FB-RISE^K, SAT^K (both parts), SAT-FB^K, SAT-FB1^K, Theorem FB-C^K,
  Corollary (i) SIGNED; Corollary (ii) SIGNED as an implication, its implicit step σ̄′|V = σ̄ made explicit and proved (FBCK-N1); quotes 9/9;
  notes FBCK-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-FBCK.md (report 30237ebb, sha1 e2d7eb8db4064b7ce3a9292ae506d132e0716e40 there; §C
  991f9e27; successor 19): K1-K3, LEV^K_C ≥ 0 and non-decreasing, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, Theorem FB-C^K, Corollary (i) SIGN;
  Corollary (ii) SIGN AS AN IMPLICATION (in its §C: "SIGN as an implication; the σ̄ step is proved (C.3)"); quotes 9/9 (SHIFT=1 control 0/9);
  notes N-FBCK-1..5; no gap. INDEPENDENCE: REFEREE opened no REFEREE-2 FBCK file before its push (names re-listed at 23:54Z: 0 / 0 / 0) and
  ran no lane code; REFEREE-2 did not open REFEREE's report before pushing 30237ebb (names-only count of FBCK files on origin/claude/referee,
  14 at 00:13:33Z and at 00:42:38Z) and declared one read of docs/referee/R-N5-READER.md @ e83fd19d l. 1-30 (another packet, READER: the
  premise of Corollary (ii)), to check that implication; REFEREE's §C: "No effect on any verdict". §C (both): verdicts identical; joint gap
  map EMPTY; FBCK-N1 = N-FBCK-1 (REFEREE's wording with its proof; supersedes the σ̄ half of N-FBCK-1; the scope half stands for both),
  FBCK-N2, FBCK-N3 and FBCK-N4 AGREED by REFEREE-2, N-FBCK-2..4 ACCEPTED by REFEREE, N-FBCK-5 no conflict; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase reduction of N5's in-phase fallback count to a configuration count; no
  running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
