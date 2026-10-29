# T36: the N5 reduction map — from N5's iteration count down to the counts still open (L-LIT, 2026-10-29)

Asked by the Lead at 11:19Z (date -u), for the owner. Owner ruling D18:
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

**Scope.** Repo sources only, cited with their SHAs. No new literature. No runs. Nothing here is a new result.

**Labels.**
- PROVED (Rxx): landed in docs/RESULTS.md with two referee signatures and a CHECKER pass.
- PROVED (lane, SHA): proved in a lane's working note. Unrefereed unless said.
- PROVED (REFEREE-2 signed, REFEREE pending): one of the two referee signatures given.
- CONJECTURE (with data). OPEN. DEAD (killed by a pinned instance).

**Read this first.**
- N5 is NOT proved polynomial on general games. G-N5-TIME (docs/GAPS.md) is open.
- What this map shows: through the chain in §1, N5's running time on every game is now REDUCED to two counts, NM* and NM*^U (§3).
  - Every link above them is proved. Some links are proved only by a lane or only by one referee; their status is marked.
  - Neither count is bounded. The best known lower bound for each is linear in n (DATA).
- A parallel route (§2) reduces N5 to the VC dimension of the strategies it visits.

## 0. Notation (from SPEC docs/new/N5-ssi-global.md and RESULTS)
- **Basic objects.** n vertices, m edges; m_E (m_O) the edges leaving Even (Odd) vertices.
- **Valuations.** Ξ_t(v) = (c, P, ℓ): v's S1 valuation at state t, with cycle node c, path set P and length ℓ. λ maps each vertex to
  its cycle node. U is the dual valuation of τ on G^d; λ^U is its cycle-node map.
- **λ-run.** A maximal stretch of states with λ constant (τ free). A λ^U-run is the same for λ^U.
- **Phase.** λ and τ constant (RESULTS R38 (a)).
- **Run.** A maximal fallback-free stretch of a phase.
- **P-change of v.** A transition at which P(Ξ v) changes.
- **Carry.** A P-change that is not MATCHED (docs/lit/P-N5-MATCHPHI.md §1): it cannot be split into individually improving
  one-for-one rank exchanges.
- **The two open counts.**
  - NM*: the largest number of carries of one vertex's Ξ in one λ-run.
  - NM*^U: the same for U in one λ^U-run.

## 1. The main chain (top to bottom)

| # | link | statement (short) | status | source |
| --- | --- | --- | --- | --- |
| 1 | iterations → λ-runs | λ changes ≤ n(n − 1) times per run, λ^U likewise; ≤ 2n(n − 1) + 1 joint λ-runs | PROVED (R47, Lemma Φ, every game) | docs/RESULTS.md R47 |
| 2 | iterations → switches inside λ-runs | every N5 transition changes σ or τ (R15 (d)); inside a λ-run each σ-change is an Even switch, and dually for τ in λ^U-runs | PROVED (R15 (d); R80 (a) EVERY-SWITCH) | RESULTS R15, R80 |
| 3 | switches → successor rises | SW-RETURN: v re-enters a successor c at most 1 + (number of Ξ(c) rises) times, on any stretch | PROVED (lane, L-SI s24, l-si 884fea80 / f372bc6b) | claude/l-si docs/si/N5-CHG-box28.md §7, §9 |
| 4 | rises → P-changes | LEN-MONO: on a λ-run, RISE(c) ≤ PCH(c) + (PCH(c) + 1)(n − 1); under a fixed P the length moves one way | PROVED (lane, l-si f372bc6b); same bound in GRUN §5 (l-si e03c3988) | N5-CHG-box28 §9; N5-GRUN-box25 §5 |
| 5 | **composition** | Theorem COMPOSE / Corollary COMPOSE-RUN: iterations ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + m_O(P*^U + 1)), with P* (P*^U) the most P-changes of one vertex in one λ-run (λ^U-run). Needs no bound on phases. | PROVED (lane, l-si f372bc6b), a REDUCTION | N5-CHG-box28 §9 |
| 6 | P-changes → carries | MATCH-Φ: PCH ≤ (K(K+1)/2)(NM + 1) + NM, K ≤ n − 1. It holds for any sequence of subsets of R_c with c fixed, so on λ-runs. COMPOSE uses it as an ASSUMED premise | PROVED (L-LIT), under review. Review object P-N5-MPGS (A) (l-lit a23179b0), REFEREE-2 20 reviewing. REFEREE-2 19 already signed every item of the identical statements in P-N5-MATCHPHI (docs/referee-2/R2-N5-MATCHPHI.md, referee-2 5ba3e21d). REFEREE pending | docs/lit/P-N5-MPGS.md (A); docs/lit/P-N5-MATCHPHI.md (12b7d12a, superseded) |
| 7 | **open** | NM*, NM*^U = poly(n)? | OPEN | §3 |

**Consequence.** If links 3-6 are refereed as they stand, N5 is polynomial on every game IF NM* and NM*^U are polynomial
(N5-CHG-box28 §9 (c)). Monotonicity and the set order alone allow exponentially many carries: an ascending binary counter of path
sets has 2^(k−2) − 1 carries (docs/lit/T33-match-phi.md §2.2, Part B of docs/lit/T33-match-phi-check.py). So a bound on NM must use
S4a's rule, i.e. how an edge enters the arena Iσ_t (T33 §2.4; T34).

## 2. Other reductions and the counts they leave

**(a) Phases × fallbacks × run length** (the older chain; still informative).

| link | statement | status | source |
| --- | --- | --- | --- |
| phases per run | λ-runs ≤ 2n(n − 1) + 1 (R47). τ-changes inside a λ-run: bounded only on one-Odd-choice games (≤ deg(o) − 1, R47 Cor. Φ-1O) and, by mirror symmetry, one-Even-choice games (R54) | PROVED on 𝒞^1O, 𝒞^1E; OPEN on general games | RESULTS R47, R54 |
| fallbacks per phase | R81 FB-C^K: f ≤ n_K·(number of K-configurations of fallback sources); R71: f ≤ \|𝒞_f\|(4n² − 3n); R48: ≤ 1 + (n − 2)(2n − 1) on one-Odd-choice games | PROVED (R48, R71, R81); configurations per phase OPEN | RESULTS R48, R71, R81 |
| fallbacks per phase | CONJECTURE FB-LIN: f ≤ n per phase | CONJECTURE (data 0.79n; 5 L-RED boxes R100-R104, no kill; l-red 899b274d, 92754453) | docs/NOW.md l.2; claude/l-red docs/red/R100-R104 |
| phase length | R80 PHASE-SW: \|P\| ≤ Σ_w SW_P(w) (every transition of a phase switches some Even vertex) | PROVED (R80) | RESULTS R80 |
| run length, structure | R83 REL-SPLIT: \|S\| ≤ SEG(S)·n − 1 if (H4′_rel) and GEN_W hold at every segment end; SEG − 1 ≤ G + CF; GATE-RISE: G ≤ Σ_gates (XR + TIE + CYC + THRU) | PROVED (R83) | RESULTS R83 |
| run length, conjectures | RUN-LIN (O(n) per run) DEAD (runfam_K10, l-si 90bcc50c). RUN-LIN′ DEAD and "a REL segment is ≤ n − 1 without (H4′_rel)" DEAD (runquad, R106). SEG-COUNT DEAD (R105) | DEAD | claude/l-red R105 22d7c6ab, R106 86f24219 |
| run length, lower bound | runquad: one fallback-free in-phase run = one REL segment of L = 4K² + 3K − 1 transitions at n = 24K + 6 (≈ n²/144; 263 at n = 192). Explicit start pairs; the SPEC S3 default start NOT tested on this family | DATA (two engines, Oink, L-SI relcheck) | claude/l-red docs/red/R106-quadratic-run.md, 86f24219 |
| segments per run | CONJECTURE SEG-RUN: SEG = O(n) | CONJECTURE (data ≤ 1.00n after climbs) | claude/l-si N5-GRUN-box25 §5, e03c3988 |
| switches per vertex | CONJECTURE SW-PER-VERTEX: O(n) switches per Even vertex per run | CONJECTURE (SW-RUN data ≤ 0.667n; runquad reactors O(K)) | docs/NOW.md (L-SI roster); N5-CHG-box28 |
| per-vertex forms | SW-LIN, XR-LIN DEAD; per-vertex counts are reader-inflatable (READER-INV, REFEREE e83fd19d) | DEAD / PROVED (by REFEREE under (R)) | docs/NOW.md l.2 |

- Reading of (a): this chain needs a bound on phases per run, which is open on general games. That is why link 5 of §1, which needs
  none, supersedes it as the top-level reduction.

**(b) VC-BOUND** (an alternative top level).
- Theorem VC-BOUND (PROVED, lane, L-NEW s31, l-new af20b1e1, docs/new/N5-VC-box50.md §2): iterations ≤ Φ_{dσ}(m_σ) + Φ_{dτ}(m_τ) − 2,
  with dσ, dτ the VC dimensions of the visited Even / Odd strategy families (Sauer-Shelah, proved in the note).
- Two-sided: N5 polynomial ⇒ dσ, dτ = O(log n); dσ, dτ = O(1) ⇒ polynomial; O(log n) ⇒ quasi-polynomial.
- CONJECTURE VC-N5: dσ, dτ = O(1). DATA: max 4 on the library; 3 on every scaling family tried (runfam, ladder, cxmig, Oink counters).
  OPEN.
- Lower bound: the data show only constants.
- Reading: an exponential N5 family must run a binary counter on n^{Ω(1)}/log m strategy edges (a shattered set). This is the same
  obstruction as carries, seen on σ instead of on path sets.

## 3. The minimal list of OPEN counts

| count | what a polynomial bound would give | best known lower bound | source of the lower bound |
| --- | --- | --- | --- |
| **NM*** (carries of one vertex's Ξ path set in one λ-run) | with §1 links 1-6: N5 polynomial on every game (together with NM*^U) | Θ(n) on families: NM = K at n = 24K + 6 on runquad, also on R105's family. Max in data 42 at n = 41 (1.02n, l121reader_n41); L-COMP: 62 at n = 581, max NM/n 1.18 (pl130_n40). Exponential only without N5's dynamics (T33 Part B) | N5-CHG-box28 §9 DATA (l-si f372bc6b); claude/l-comp fc0758fc |
| **NM*^U** (the same for Odd's dual valuation U in one λ^U-run) | the τ-side half of the same statement | small in data: Odd-side PCH ≤ 13 on the corpora. No family targets it; by mirror symmetry (R54) Even-side families dualize | N5-CHG-box28 §9 DATA |

**Equivalent alternative.** Replace both by dσ, dτ = O(1) (§2 (b)). Best known lower bound: constant (max 4).

**Not minimal, kept for orientation.** These are implied by, or would bypass, the two counts above:
- phases per run on general games (OPEN);
- configurations per phase (OPEN);
- FB-LIN, SEG-RUN, SW-PER-VERTEX (CONJECTURES).

**Overall lower bound for N5 known in the repo.**
- Θ(n²) iterations in one run from an explicit start (runquad, R106; DATA).
- Nothing super-polynomial.
- Friedmann's H_n and its variants run linearly (claude/l-comp experiments/friedmann-hn README, box 16). Friedmann-type gates cannot
  delay N5 (docs/lit/T34-friedmann-vs-n5.md; Lemma GATE-SHUT, packet P-N5-MPGS (B), l-lit a23179b0, under review).

## 4. Status of the links that are not yet two-referee
- SW-RETURN, LEN-MONO, COMPOSE (§1 links 3-5): lane-proved by L-SI (l-si 884fea80, f372bc6b). Not yet packeted or refereed.
- MATCH-Φ (link 6): review object P-N5-MPGS (A), per the Lead's ruling of 11:27Z. REFEREE-2 19 signed the identical P-N5-MATCHPHI
  items with notes N-MP-1..5 (no gap; R2-N5-MATCHPHI 5ba3e21d). REFEREE-2 20 is reviewing MPGS; REFEREE pending.
- GATE-SHUT (T34, not a link of the map): review object P-N5-MPGS (B); P-N5-GATESHUT is a verbatim copy and is not routed.
- VC-BOUND: lane-proved by L-NEW (af20b1e1). Not refereed.

## DONE / FINDINGS / NEEDS
- DONE: this map.
- FINDINGS:
  1. With L-SI's COMPOSE (lane) and MATCH-Φ (one referee so far), G-N5-TIME on every game reduces to two counts, NM* and NM*^U. No
     phase count is needed.
  2. The best known lower bounds are Θ(n) for NM* (families) and Θ(n²) for N5's iterations (runquad, explicit start).
  3. VC-BOUND is an equivalent-up-to-quasi-polynomial alternative top level; its open count (dσ, dτ) is constant in all data.
- NEEDS (Lead; nothing for the owner): packet and two referees for SW-RETURN + LEN-MONO + COMPOSE (L-SI). Then the reduction in §1
  is fully two-referee up to NM.
