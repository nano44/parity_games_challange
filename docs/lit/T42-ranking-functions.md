# T42: ranking-function synthesis for termination (linear, lexicographic, polyranking, multiphase) — what each decides, at what cost, and what bound a found function implies; and what that means for N5
L-LIT successor 2 (Opus 5.5), D18. Lead's message 13:47Z: «T42: a literature scan for L-NEW 32's BOX 53, ranking-function synthesis for
termination. Cover Podelski–Rybalchenko complete linear ranking functions; lexicographic linear ranking functions (Ben-Amram–Genaim, with their
complexity results); polyranking and multiphase ranking functions (Ben-Amram–Genaim, Leike–Heizmann); and any application to policy / strategy
iteration or to game-solving termination. Open each source. For each: what it decides or synthesises, the complexity, and the BOUND on running
time a found ranking function implies.» Written 2026-10-29 from 14:02Z (date -u). Working note, unrefereed. Labels (D18): PROVED (L-LIT,
unrefereed) / READING / OPEN. Every source is opened (sha256 in the notebook) unless marked "via".

## Vocabulary (from the sources)
- SLC loop: one transition polyhedron Q ⊆ Q^{2n} (a conjunction of linear constraints on (x, x′)); MLC loop: a disjunction Q_1, …, Q_k (k
  paths). Rational (Q) vs integer (Z) variants; "with a precondition" = only states from a given initial set.
- LRF: affine ρ with ρ ≥ 0 on enabled states and ρ(x) − ρ(x′) ≥ 1 (or δ > 0) on every transition. LLRF: a tuple ⟨ρ_1, …, ρ_d⟩ decreasing
  lexicographically (three variants: ADFG (Alias et al. 2010), BMS (Bradley-Manna-Sipma 2005), BG (Ben-Amram-Genaim 2014), differing in where
  non-negativity is required). MΦRF (multiphase): ⟨f_1, …, f_d⟩ where each transition decreases some f_k while f_1, …, f_{k−1} are already
  negative. Polyranking (BMS 2005): lexicographic, each component an eventually-negative (nested, depth ≤ 2) function.

## 1. The entries
| # | source | decides / synthesises | complexity | bound implied by a found function |
| --- | --- | --- | --- | --- |
| 1 | Podelski-Rybalchenko, "A complete method for the synthesis of linear ranking functions", VMCAI 2004 (via BG survey arXiv 2509.06752 v3, Thm 4.1 p.51; BG14 p.25; primary NOT opened: publisher and author URLs returned HTML) | LRF for a rational SLC loop: "Q has an LRF iff the linear program (4.8) has a solution" | PTIME (one LP; "inherit their complexity from that of LP", BG14 p.25) | linear: iterations ≤ ρ(x_0)/δ + 1 |
| 2 | Ben-Amram, Genaim, "Ranking functions for linear-constraint loops", JACM (arXiv 1208.4041 v4) | LinRF(Q), LinRF(Z), LexLinRF(Q), LexLinRF(Z) (BG-LLRF), and synthesis | LinRF(Z): strongly coNP-hard even for SLC loops (Thm 3.1 p.10), in coNP (Thm 3.17 p.16); LinRF(Q) for MLC PTIME (Cor. 4.25 p.27); LexLinRF(Q) PTIME, LexLinRF(Z) coNP-complete (§5); synthesised LLRF has dimension d ≤ n (Cor. 5.12 p.33); complete Z-algorithms go through the integer hull, exponential in general (Thm 3.19 p.16, Thm 4.16) | §5.4 (p.48): «LRFs clearly provide linear bounds, and LLRFs provide polynomial bounds when each component of the LLRF has a linear upper bound ... at most the product of the bounds on the individual components, and hence a polynomial of degree given by the dimension of the LLRF»; Thm 5.37: for SLC loops a PIECEWISE LINEAR bound Σ_{i<j} (⌊ρ′_i(x)/δ_i⌋ + 1); extends to MLC only if the last component ranks a transition of every path (Remark 2) |
| 3 | Ben-Amram, Genaim, "Complexity of Bradley-Manna-Sipma lexicographic ranking functions", CAV 2015 (arXiv 1504.05018 v1) | BMS-LLRF existence and synthesis; fixed dimension d | existence PTIME over Q (Cor. 1 p.7), coNP-complete over Z (Thm 1 p.7); dimension ≤ d for d ≥ 2: NP-complete over Q (Thm 3 p.9), Σ2P-complete over Z (Thm 4 p.11); Table 1 p.3 compares ADFG (dim ≤ min(n, k), fixed-dim PTIME / coNP-c), BG (dim ≤ n, PTIME / coNP-c), BMS (dim ≤ k) | as for LLRFs: product of component bounds (degree = dimension); the abstract names "computing iteration bounds" as why dimension matters |
| 4 | Ben-Amram, Genaim, "On multiphase-linear ranking functions", CAV 2017 (arXiv 1703.07547 v2) | MΦRF of given depth d for SLC loops; LLRF → MΦRF | depth-d existence PTIME over Q (Thm 3.5 p.12, via nested ranking functions, Thm 3.4), coNP-complete over Z (Thm 5.6 p.18); depth cannot be bounded by n alone: loop Q_B needs ≥ B + 1 components (Thm 6.1 p.18); every weak LLRF of depth d gives an MΦRF of depth d (Thm 4.4 p.15) | Thm 7.4 (p.21): «An SLC loop that has a MΦRF terminates in a number of iterations bounded by O(‖x_0‖∞)» — LINEAR, though the variables can grow non-linearly (Example 7.1); the constants come from Farkas multipliers on the single polyhedron Q (Lemma 7.2) |
| 5 | Ben-Amram, Doménech, Genaim, "Multiphase-linear ranking functions and their relation to recurrent sets", SAS 2019 (arXiv 1811.07340 v2); survey Ben-Amram, Genaim, Ouaknine, Worrell, "Termination analysis of linear-constraint programs", FnT (arXiv 2509.06752 v3) | MΦRF existence WITHOUT a depth bound | OPEN (survey p.79: «Although the problem remains open»); BDG19 give an algorithm that finds an MΦRF if one exists but may not terminate otherwise, and relates failure to recurrent sets (non-termination witnesses) | as entry 4 (survey Thm 4.23 = BG17 Thm 7.4); classes where termination ⇒ MΦRF (octagonal, finite-monoid affine) get linear run-time (survey p.79) |
| 6 | Leike, Heizmann, "Ranking templates for linear loops", LMCS 11(1:16) 2015 (arXiv 1503.00193 v2) | template-based synthesis (multiphase, nested, piecewise, parallel, lexicographic) for linear lasso programs, via Motzkin's transposition theorem | complete for each template, but the constraint is non-linear: "Theoretically, this constraint can be decided in exponential time [GV88]" (§1); the nested template needs only linear constraint solving (§1, §4.2); Thm 4.4 p.8: the k-phase template is a linear ranking template | Thm 4.5 p.8: the terminating conjunctive loop a > b ∧ b > 1 ∧ a′ = 2a ∧ b′ = 3b has NO multiphase ranking function — termination with an exponential-growth argument escapes the class |
| 7 | Ben-Amram, "The hardness of finding linear ranking functions for lasso programs", GandALF 2014 (arXiv 1408.5955 v1) | LRF existence for a loop WITH a precondition (partially specified input) | EXPSPACE-hard over Z (from Petri-net reachability), PSPACE-hard over Q; upper bounds unknown (abstract) | linear, when found |
| 8 | Bradley, Manna, Sipma, "The polyranking principle", ICALP 2005 (via survey p.80 §4.2.5 and Thm 4.14 p.74; primary NOT opened) | lexicographic functions whose components are eventually-negative (depth ≤ 2); BMS-LLRF synthesis with supporting invariants | BMS-LLRF over Q: PTIME (survey Thm 4.14, p.74) | product bound as for LLRFs |
| 9 | Alias, Darte, Feautrier, Gonnord, SAS 2010 (via survey Thm 4.13 p.71 and BG14 §5.4 p.48; primary NOT opened) | ADFG-LLRF of MINIMAL depth for rational MLC loops | PTIME (survey Thm 4.13) | number of integer points of ρ(C) (Ehrhart-polynomial counting), a polynomial of degree = depth; SLC loops with an ADFG-LLRF have an LRF, hence a linear bound (BG14 p.48) |

## 2. Applications to strategy / policy iteration and to game solving (the Lead's last item)
- Search (arXiv API, 2026-10-29): abs:"ranking function" ∧ abs:"policy iteration" — 0 hits; ∧ "strategy improvement" — 0 hits; ∧ "parity
  games" — 2 hits, both coalgebraic progress measures (1511.00346, 1606.04680; titles read, not opened). No source analyses the termination
  of a policy / strategy iteration algorithm by synthesising a ranking function. READING: the classical SI termination proofs (Lemma 1 of
  Scherrer, arXiv 1306.0386; R15 here) ARE ranking arguments with the valuation as a lexicographic ranking function whose range is
  exponential; that is why they give only exponential bounds.
- 10. Progress measures for parity games ARE ranking functions (Jurdziński-Lazić, "Succinct progress measures for solving parity games", arXiv
  1702.05051 v3, §1.2 p.2: rooted in «rankings and progress measures [Klarlund, Vardi]»). Synthesis = the lifting algorithm (least fixpoint of
  Lift_v); Thm 7 p.14: time O(mη^{lg(d/lg η)+1.45}) for d = ω(log η), O(mη^{2.38}) for d ≤ ⌈lg η⌉, space O(n log n · log d). Bound: the
  number of lifts ≤ (number of vertices) × (size of the measure's codomain). Barrier (BARRIERS B1; arXiv 1807.10546 v2, Thm 5.1, opened
  2026-10-14): every such codomain (strong separator / universal tree) has ≥ n^{lg(d/lg n) − 2} elements, so progress-measure ranking
  functions cannot give polynomial time. N5 is outside this model (T20 §B1-B3).
- 11. Lexicographic ranking SUPERmartingales (Agrawal, Chatterjee, Novotný, POPL 2018, arXiv 1709.04037 v1): termination of probabilistic
  programs WITH NONDETERMINISM (i.e. against every scheduler: a one-player-plus-chance game). Thm 5.1 p.17: linear LexRSMs are synthesised (or
  refuted) in polynomial time for affine programs with linear invariants (LP via Farkas). Bound: Thm 7.2 p.23, with "c-bounded ECI",
  E[T] ≤ Σ_{j=1}^{n} E[X_0[j]]·(c[j] + 1)^{n−j} — exponential in the dimension n in general; without the extra condition a LexRSM gives
  almost-sure termination only, possibly with infinite expected time (Fig. 2 p.16).
- 12. Strategy iteration as a tool INSIDE program analysis (the reverse direction): Gawlitza, Seidl, "Numerical invariants through convex
  relaxation and max-strategy iteration" (arXiv 1204.1147 v1): Thm 1 p.27 — at most |X|·|Σ| max-strategy improvement steps (exponentially
  many strategies; "our conjecture is that for practical examples our algorithm terminates after linearly many iterations", p.27); Thm 4
  p.39 — "the number of strategy improvement steps is exponentially bounded". Termination is by monotonicity, not by a synthesised ranking
  function; the invariants it computes are what a ranking-function synthesiser consumes.

## 3. What a found ranking function would imply for N5 (for L-NEW BOX 53)
- Encoding. A state of N5 is (σ, τ); write x ∈ {0, 1}^{m} for the edge indicators of the chosen successors (m = |E|). N5's step is not
  affine in x: it is a disjunction over (exponentially many) cases, i.e. an MLC "loop" with exponentially many paths if written out.
- PROVED (L-LIT, unrefereed; elementary). (a) If φ(x) = λ·x + λ_0 with integer λ, ‖λ‖∞ ≤ B, decreases by ≥ 1 at every N5 transition of a game,
  that game's run has ≤ m·B + 1 iterations (φ ranges over an interval of length ≤ m·B on {0, 1}^m). (b) If ⟨φ_1, …, φ_d⟩ decreases
  lexicographically and φ_j takes ≤ R_j values on {0, 1}^m, the run has ≤ Π_j R_j iterations; with integer coefficients ≤ B this is
  ≤ (m·B + 1)^d. So a POLYNOMIAL bound for all games needs, uniformly in the game: B polynomial, and d = O(1) for a lexicographic function
  (or the MΦRF-type linear bound, which needs entry 4's single-polyhedron structure).
- Hypotheses of the literature vs N5.
  - Entries 1-5, 7-9 decide existence for ONE loop given by linear constraints; N5 is a family (one transition relation per game), so BOX 53
    needs a TEMPLATE in the game's structure (e.g. λ depending on rank and owner), i.e. entry 6's setting lifted from variables to games.
    No source treats ranking functions parametrised by a combinatorial family.
  - Entry 4's LINEAR bound (Thm 7.4) uses the SLC structure (one polyhedron, Farkas multipliers in Lemma 7.2); N5 is multipath, so for N5
    an MΦRF/LLRF gives only the product bound of BG14 §5.4 unless the last component ranks every path (BG14 Thm 5.37, Remark 2).
  - On a finite state space a ranking function always EXISTS (the remaining run length); the content is the class and the coefficient size.
    The classical SI potential (the valuation, weights 2^rank, R15) is a lexicographic ranking function with EXPONENTIAL B; any exponential
    lower-bound family for N5 would rule out polynomial-B linear functions, and none is known (G-N5-TIME OPEN).
  - Entry 6, Thm 4.5: terminating loops can escape multiphase functions entirely (exponential growth races); entry 7: with a precondition
    (N5 runs start from reachable states only) even LRF existence is PSPACE/EXPSPACE-hard for general loops.
- READING (a usable procedure, not a result). PR04 / BG14 constraints are LPs over the transitions to be ranked. On SAMPLED N5 transitions
  (runs of the corpora) one can solve the LP for λ with ‖λ‖∞ minimal per game family, then test on held-out runs (a CEGAR loop as in the
  synthesis literature). That yields DATA (a candidate template), and the proof would still have to show the decrease on every transition.
- OPEN: is there a ranking template over (rank, owner, edge) with polynomially bounded coefficients that decreases at every N5 transition of
  every game? Equivalent to a polynomial bound via (a); no source addresses it.

## DONE / FINDINGS / NEEDS
- DONE: this note; 12 entries; opened: arXiv 1208.4041, 1504.05018, 1703.07547, 1811.07340, 2509.06752, 1503.00193, 1408.5955, 1702.05051,
  1709.04037, 1204.1147 (+ 1807.10546 from 2026-10-14). Via the survey / BG14 only (primaries not opened): Podelski-Rybalchenko 2004,
  Bradley-Manna-Sipma 2005, Alias et al. 2010.
- FINDINGS:
  - Rational linear / lexicographic (ADFG, BG, BMS) / bounded-depth multiphase functions: synthesis PTIME (LP); integer versions coNP-complete;
    fixed-dimension BMS NP-complete (Q) / Σ2P-complete (Z); unbounded-depth MΦRF existence OPEN; with a precondition LRF existence is
    PSPACE-hard (Q) / EXPSPACE-hard (Z).
  - Bounds: LRF linear; LLRF a product of component bounds (degree = dimension); MΦRF on SLC loops LINEAR in ‖x_0‖∞ (BG17 Thm 7.4), not
    available for multipath loops in general.
  - No source applies ranking-function synthesis to policy / strategy iteration. On the game side, progress measures are ranking functions
    with a quasi-polynomial barrier (B1); LexRSMs handle nondeterminism + chance with PTIME synthesis but exponential expected-time bounds.
  - For N5: a linear function with poly-bounded integer coefficients that drops at every transition would give ≤ m·B + 1 iterations (PROVED,
    elementary); the literature gives synthesis for one loop, not a template over all games (OPEN).
- NEEDS: none from the owner.
