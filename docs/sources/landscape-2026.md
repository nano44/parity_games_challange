# Parity Games: A Research Landscape

Oct 14, 2026 · @Nano

## Reader's guide

The short answer: deciding who wins a parity game is in NP ∩ coNP (indeed UP ∩ coUP), and since 2017 it can be done in quasi-polynomial time, roughly n^O(log d). Whether it is in polynomial time is still open as of October 2026. Every known quasi-polynomial algorithm belongs to a family that provably cannot go below quasi-polynomial, so a polynomial algorithm would need a genuinely new idea.

Claims are labelled throughout:

- **Established** — a peer-reviewed theorem or published measurement.
- **Claim** — a result posted but not yet refereed or independently checked.
- **Conjecture / opinion** — a belief widely held in the community, or my own assessment, said as such.

Scope: two-player, turn-based, zero-sum parity games on finite graphs. Stochastic, timed and quantitative variants appear only where they connect back to that core problem.

## What parity games are, and why they matter

A parity game is a two-player game of infinite duration on a finite directed graph, where the winner is decided by the parity of the largest priority seen infinitely often.

**The game.** The vertices are split between two players, Even and Odd (often called Eve and Adam). Every vertex carries a natural-number priority, and every vertex has at least one outgoing edge. A token starts on a vertex; whoever owns the current vertex picks an outgoing edge, and play continues forever. The resulting infinite path v0 v1 v2 … is won by Even exactly when this holds:

```latex
\max\{\, p \;:\; \mathrm{pr}(v_i) = p \text{ for infinitely many } i \,\} \text{ is even}
```

Otherwise Odd wins. Some papers use the minimum instead of the maximum; the two conventions are interchangeable. The size parameters are n vertices, m edges and d distinct priorities (d ≤ n).

**A tiny example.** Suppose Odd can trap the token in a cycle through priorities 1 and 3, while Even can escape to a cycle through priorities 1 and 2. If Even owns the exit, she escapes and wins (largest recurring priority 2). If Odd owns it, he stays and wins (largest recurring priority 3). The difficulty comes from many such cycles nested inside each other, with priorities interleaved.

**Two foundational facts (Established).**

1. *Determinacy.* From every starting vertex, exactly one of the two players has a winning strategy. Solving a game means computing the two winning regions.
2. *Positional (memoryless) strategies suffice.* The winner can always win by choosing a fixed successor at each of their vertices, independent of history. This was shown by Emerson and Jutla and by Mostowski in 1991, and re-proved by [Zielonka (1998)](<https://doi.org/10.1016/S0304-3975(98)00009-7>). A positional strategy is a polynomial-size certificate that can be checked in polynomial time, which is why the problem sits in NP ∩ coNP.

**Two working tools.** An *attractor* is the set of vertices from which one player can force the token into a target set; it is computable in linear time. A *dominion* is a region that one player can win without the token ever leaving it. Most algorithms are ways of finding dominions cheaply.

**Why they matter.**

- *Verification.* Deciding the winner is polynomial-time equivalent to model checking the modal μ-calculus and to checking emptiness of parity tree automata; it is also at the heart of Church's synthesis problem ([Czerwiński et al., SODA 2019](https://arxiv.org/abs/1807.10546)).
- *Synthesis in practice.* The leading LTL synthesis tool [Strix](https://strix.model.in.tum.de/) translates specifications into deterministic parity automata, builds a parity game, and extracts a controller from the winning strategy.
- *Complexity theory.* It is one of very few natural problems known to lie in NP ∩ coNP (indeed UP ∩ coUP) but not known to be in P. Parity games are also the simplest of a family of such games: they reduce in polynomial time to mean-payoff, discounted and simple stochastic games, with no reverse reductions known ([Parys, MFCS 2019](https://arxiv.org/abs/1904.12446)).
- *Lower bounds elsewhere.* Hard parity-game instances built by Friedmann were transferred to Markov decision processes and the simplex method, settling questions open for decades about pivoting rules ([Friedmann, thesis talk 2012](https://talks.cam.ac.uk/talk/index/37305/)).

As an informal measure of standing: when the quasi-polynomial result appeared, a complexity blog noted that some researchers rank the problem's importance above graph isomorphism ([Computational Complexity blog, 2017](https://blog.computationalcomplexity.org/2017/03/parity-games-in-quasipolynomial-time.html)). That is opinion, but it is a common one.

## The classic era, 1991–2016

For 25 years the field had tight complexity-class bounds (NP ∩ coNP, then UP ∩ coUP) but only exponential or mildly subexponential algorithms, and a growing collection of lower bounds showing why each algorithm family failed.

Three algorithmic families came out of this era and still organise the field:

- **Recursive / attractor-based** (McNaughton 1993, Zielonka 1998): peel off the top priority's attractor, solve the rest recursively. Exponential in the worst case, but the strongest family in practice.
- **Progress measures / value iteration** (Jurdziński 2000): assign each vertex a tuple of counters and "lift" until a fixpoint; the counters certify that Odd cannot keep visiting odd priorities. Runs in time roughly n^(d/2).
- **Strategy improvement / policy iteration** (Vöge and Jurdziński 2000, building on Puri and Hoffman–Karp): fix one player's strategy, evaluate it, switch to better edges, repeat. Fast in practice; worst case depends on the switching rule.

Key results, newest first (all **Established**):

| Year | Result | Why it mattered |
| --- | --- | --- |
| 2015 | [Symmetric strategy improvement](https://doi.org/10.1007/978-3-662-47666-6_31) (Schewe, Trivedi, Varghese, ICALP) | Improves both players' strategies at once; solved the known hard instances quickly. Shown exponential in 2024 (see Barriers). |
| 2011 | [Recursive algorithm requires exponential time](https://doi.org/10.1051/ita/2011124) (Friedmann, RAIRO) | Zielonka's algorithm, the practical favourite, has exponential worst case. |
| 2009–11 | [Exponential lower bounds for strategy improvement](https://lmcs.episciences.org/1026/pdf) (Friedmann, LICS 2009 Kleene Award; LMCS 2011) | The standard switching rules take exponentially many iterations; the same games give lower bounds for mean-payoff, discounted and stochastic games. |
| 2006–08 | [Deterministic subexponential algorithm](https://wrap.warwick.ac.uk/28789) (Jurdziński, Paterson, Zwick, SODA 2006 / SICOMP 2008) | First deterministic n^O(√n) algorithm; matched the earlier randomized subexponential bounds and stood as the record until 2017. |
| 2000 | [Small progress measures](https://doi.org/10.1007/3-540-46541-3_24) (Jurdziński, STACS) and discrete strategy improvement (Vöge, Jurdziński, CAV) | Founded the value-iteration and strategy-improvement lines that the 2017 breakthroughs rebuilt. |
| 1998 | [UP ∩ coUP](https://www.dcs.warwick.ac.uk/~mju/Papers/Jur98-IPL.abstract) (Jurdziński, IPL) | Simple reduction from parity to mean-payoff games; winning is "unambiguously" certifiable, making NP-hardness even less plausible. |
| 1998 | [Recursive algorithm and positional determinacy](<https://doi.org/10.1016/S0304-3975(98)00009-7>) (Zielonka, TCS) | Clean recursive solver, adapted from McNaughton's 1993 algorithm for Muller games. |
| 1991–93 | [NP ∩ coNP](<https://doi.org/10.1016/S0304-3975(00)00034-7>) and positional determinacy (Emerson, Jutla, Sistla; Mostowski) | Positional strategies are short, checkable certificates for both players. |

The era also introduced the idea of *dominions* as the unit of progress: the subexponential algorithm works by brute-force searching for small dominions before recursing ([Chatterjee et al. describe the method](https://arxiv.org/pdf/1706.04889)).

## The 2017 breakthrough and what followed

In 2017 Calude, Jain, Khoussainov, Li and Stephan showed parity games can be solved in quasi-polynomial time, an exponential improvement over n^O(√n); within three years at least five structurally different quasi-polynomial algorithms existed and were unified by one combinatorial object, the universal tree.

**The breakthrough (Established).** [Calude et al. (STOC 2017, best paper)](https://www.cs.auckland.ac.nz/~cristian/crispapers/paritygame-stoc.pdf) gave an algorithm running in time O(n^(log d + 6)). In the [journal version](https://www.cs.auckland.ac.nz/~cristian/crispapers/siamj2020.pdf) they also showed the problem is fixed-parameter tractable in the number of priorities, with time O(n^5 + 2^(d log d + 6d)); in particular it is polynomial when d ≤ log n. The idea: Even keeps a compact *winning statistic*, a short record of increasing even-priority runs seen so far, of only O(log n) entries. The statistic turns the parity game into a much larger but simple *safety* game, of quasi-polynomial size, which is solved in linear time in its size. [Gimbert and Ibsen-Jensen](https://ar5iv.arxiv.org/html/1702.01953) quickly gave a short correctness proof.

**Descendants, newest first (Established unless marked):**

| Year | Result | Contribution |
| --- | --- | --- |
| 2025 | [Strategy iteration with universal trees](https://arxiv.org/abs/2108.13338) (Koh, Loho, LMCS) | A strategy-iteration framework over any universal tree, at least as fast as value iteration and able to take bigger leaps; an attempt to sidestep the barrier below. |
| 2023 | [Improved complexity analysis](https://arxiv.org/abs/2305.00308) (Parys, Wiącek, CiE) | Best concrete bound for vertex-priority games: O(m · n^(1.45 + log₂(d / log₂ n)) / d), a Θ(d²) gain. |
| 2020–22 | [Universal attractor decomposition](https://arxiv.org/abs/2001.04333v2) (Jurdziński, Morvan, Thejaswini) | One meta-algorithm that yields Zielonka, Parys and Lehtinen–Schewe–Wojtczak as special cases, given different universal trees; symbolic space O(lg d). |
| 2020 | [Strahler number of a parity game](https://arxiv.org/abs/2003.08627) (Daviaud, Jurdziński, Thejaswini, ICALP) | A structural parameter k (equal to Lehtinen's register number, and at most logarithmic in n); time polynomial in n and linear in (d/2k)^k. Polynomial whenever k · lg(d/k) = O(log n). |
| 2019–22 | [Recursive quasi-polynomial algorithm](https://lmcs.episciences.org/8953) (Lehtinen, Parys, Schewe, Wojtczak, LMCS 2022) | Refines Parys's algorithm to n^O(log(1 + d / log n)), matching the best bounds. |
| 2019 | [Zielonka's algorithm in quasi-polynomial time](https://arxiv.org/abs/1904.12446) (Parys, MFCS) | Adds precision parameters to the recursion so most calls are cheap; keeps Zielonka's simplicity. |
| 2018 | [Register games](https://arxiv.org/abs/1902.10654) (Lehtinen, LICS; journal with Boker, LMCS 2020) | A third independent approach from the μ-calculus side; introduces the register index (O(log n)); also gives a quasi-polynomial translation of alternating parity word automata to weak automata. [Parys (CSL 2020)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2020.32) later tightened its running time to n^O(log n). |
| 2017 | Ordered approach in quasi-polynomial time and quasi-linear space (Fearnley, Jain, de Keijzer, Schewe, Stephan, Wojtczak, SPIN 2017 / STTT 2019) | Brings the statistics approach down to quasi-linear space. |
| 2017 | [Succinct progress measures](https://arxiv.org/abs/1702.05051) (Jurdziński, Lazić, LICS) | Rebuilds the 2000 progress-measure algorithm with succinctly encoded counters; quasi-polynomial time. |

**The unifying insight (Established).** [Czerwiński, Daviaud, Fijalkow, Jurdziński, Lazić and Parys (SODA 2019)](https://wrap.warwick.ac.uk/110346) showed that play summaries, progress measures and register games are all instances of one *separation approach*: build an automaton that accepts plays decisively won by Even and rejects plays decisively won by Odd, then solve the product safety game. Every such separating safety automaton contains a *universal ordered tree* in its state space. [Colcombet, Fijalkow, Gawrychowski and Ohlmann](https://lmcs.episciences.org/10012) generalised this to *universal graphs* for any positionally determined objective, and showed that all quasi-polynomial algorithms fall into one of two families (value iteration and attractor decomposition), both driven by universal trees.

## Where the field stands in 2026

The upper bound is quasi-polynomial and the problem is in UP ∩ coUP; no polynomial algorithm is accepted, no hardness result is expected, and the known lower bounds are for algorithm families, not for the problem itself.

| Question | Status | Strongest known result |
| --- | --- | --- |
| Is deciding the winner in P? | **Open** | No accepted polynomial algorithm. One unrefereed 2025 claim exists (see Research frontier). |
| Best general upper bound | Established | Quasi-polynomial: n^(log₂(d / log₂ n) + O(1)) up to polynomial factors ([Parys, Wiącek 2023](https://arxiv.org/abs/2305.00308)); polynomial when d = O(log n) ([Calude et al.](https://www.cs.auckland.ac.nz/~cristian/crispapers/siamj2020.pdf)). |
| Complexity class of the decision problem | Established | UP ∩ coUP ([Jurdziński 1998](https://www.dcs.warwick.ac.uk/~mju/Papers/Jur98-IPL.abstract)). NP-hardness would imply NP = coNP, so it is not expected. |
| Complexity class of computing strategies | Established | In UEOPL ⊆ EOPL ⊆ CLS, together with mean-payoff, discounted and simple stochastic games ([Fearnley, Gordon, Mehta, Savani, JCSS 2020](https://livrepository.liverpool.ac.uk/3089393/)). No hardness for any of these classes is known. |
| Fixed-parameter tractability | Established | FPT in the number of priorities d ([Calude et al.](https://www.cs.auckland.ac.nz/~cristian/crispapers/siamj2020.pdf)); polynomial for bounded Strahler / register number ([Daviaud et al. 2020](https://arxiv.org/abs/2003.08627)). |
| Lower bound for separation-based algorithms | Established | Quasi-polynomial, nearly matching the upper bound ([Czerwiński et al. 2019](https://wrap.warwick.ac.uk/110346)). |
| Lower bound for universal-tree attractor algorithms | Established | Quasi-polynomial, inherited from universal trees ([Colcombet et al. 2022](https://lmcs.episciences.org/10012); [Jurdziński et al.](https://arxiv.org/pdf/2010.08288)). |
| Lower bound for black-box nested fixpoint evaluation | Established | Quasi-polynomial for the class of algorithms considered; upper bound n^(lg(d / lg n) + O(1)) queries ([Arnold, Niwiński, Parys, CSL 2021](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2021.9)). |
| Strategy improvement | Partly open | Exponential for the standard switching rules ([Friedmann 2011](https://lmcs.episciences.org/1026/pdf)) and for symmetric strategy improvement under any rule ([van Dijk, Loho, Maat 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2024.24)). Whether some rule is polynomial is open. |
| Classic practical solvers | Established | Exponential worst cases for Zielonka ([Friedmann 2011](https://doi.org/10.1051/ita/2011124)), priority promotion and tangle learning ([van Dijk, Two Counters, 2019](https://doi.org/10.4204/EPTCS.305.8)). |
| Mean-payoff games (the next game up) | **Open**, weaker | No quasi-polynomial algorithm known; universal graphs provably cannot give one ([Fijalkow, Gawrychowski, Ohlmann 2020](https://drops.dagstuhl.de/opus/volltexte/2020/12701/)). |

**Conjecture / opinion.** Most researchers who have written on the question expect a polynomial algorithm to exist: van Dijk calls the problem one of the simplest expected to be in P ([CORDIS project report](https://cordis.europa.eu/project/id/893732/reporting/es)), and NP ∩ coNP membership is the usual reason. This is belief, not evidence: other problems once in NP ∩ coNP (primality, linear programming) did turn out to be in P, but that is an analogy, not an argument.

## Barriers and bottlenecks

The main bottleneck is not a missing trick but a set of proven ceilings: each known algorithm family has a matching lower bound, and the problem's complexity-class position makes conventional hardness proofs impossible.

**1. The separation (universal-tree) barrier — Established.** Any algorithm that solves a parity game by pairing it with a deterministic safety automaton reading the priorities of a play must carry a universal tree inside that automaton, and universal trees have quasi-polynomial size ([Czerwiński et al. 2019](https://wrap.warwick.ac.uk/110346)). This covers the Calude et al., Jurdziński–Lazić and Fearnley et al. algorithms, and, via [Parys's analysis](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2020.32), Lehtinen's nondeterministic register automata. Parys and Wiącek note one fine print: the necessity proof is for edge-priority games, and vertex-priority games need only n/2-universal trees ([CiE 2023](https://arxiv.org/abs/2305.00308)). That changes constants in the exponent, not the barrier.

**2. The attractor-decomposition barrier — Established.** The quasi-polynomial versions of Zielonka's algorithm are driven by universal trees too, so they inherit the same lower bound ([Jurdziński, Morvan, Ohlmann, Thejaswini](https://arxiv.org/pdf/2010.08288); [Colcombet et al. 2022](https://lmcs.episciences.org/10012)). The [black-box fixpoint result](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2021.9) extends a quasi-polynomial lower bound to the abstract nested-fixpoint algorithms underlying both families.

**3. Strategy-improvement lower bounds — Established.** Friedmann's constructions force exponentially many iterations for the standard rules ([LMCS 2011](https://lmcs.episciences.org/1026/pdf)), later extended to further rules such as Cunningham's ([Avis, Friedmann](https://ar5iv.arxiv.org/html/1305.3944)). In 2024 symmetric strategy improvement fell too, and notably for *every* improvement rule ([van Dijk, Loho, Maat](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2024.24)). Whether some cleverly chosen rule is polynomial remains open, and is tied to the same question for the simplex method.

**4. Lower bounds for practical heuristics — Established.** The Two Counters family is exponential for a wide range of attractor-based solvers, including priority promotion with delayed promotion and tangle learning ([van Dijk 2019](https://doi.org/10.4204/EPTCS.305.8)). An EU-funded fellowship (project PIGGY) aimed at a polynomial tangle-attractor algorithm reported that its attempts produced exponential counterexamples ([CORDIS](https://cordis.europa.eu/project/id/893732/reporting/es)).

**5. Proof-technique limits — Established facts, opinion on consequences.** Because the problem is in NP ∩ coNP, NP-hardness would collapse NP and coNP; because strategy computation is in UEOPL, hardness would have to be shown inside a small total-search class, and no such hardness is known for any of the related games. An unconditional super-polynomial lower bound for all algorithms would separate P from NP ∩ coNP, so it is out of reach of current techniques. *Opinion:* the realistic forms of negative evidence are therefore lower bounds for broader and broader algorithm models, which is exactly where the field has been producing results.

**6. The theory–practice gap — Established measurement, opinion on cause.** The quasi-polynomial algorithms are the slowest in practice: on Keiren's model-checking benchmarks, Parys reported the Fearnley et al. algorithm last, with many timeouts ([Parys 2019](https://arxiv.org/abs/1904.12446)). Zielonka's exponential algorithm consistently does best on real inputs ([Jurdziński et al.](https://arxiv.org/pdf/2010.08288)), and simple fixpoint iteration is fastest on model-checking games ([van Dijk, Rubbens 2019](https://arxiv.org/pdf/1909.07659)). *Opinion:* in applications the cost is dominated by building the game (automaton determinisation, state explosion), not by solving it; on-the-fly construction in tools such as Strix reflects this.

**7. The quantitative gap — Established.** Techniques do not transfer upward: universal graphs cannot give a quasi-polynomial algorithm for mean-payoff games ([Fijalkow, Gawrychowski, Ohlmann 2020](https://drops.dagstuhl.de/opus/volltexte/2020/12701/)), so the quasi-polynomial ideas exploit something specific to parity.

## Research frontier, 2020–2026

Since the barrier results, work has moved in four directions: structural parameters that explain when games are easy, a general theory of universal graphs and positionality, attempts to escape the barrier with new algorithm shapes, and extensions to richer game models.

**Competing approaches at a glance:**

| Approach | Best worst-case bound | In practice | Known ceiling |
| --- | --- | --- | --- |
| Value iteration / progress measures (Jurdziński; Jurdziński–Lazić) | Quasi-polynomial | Slow; asymmetric between players | Quasi-polynomial (universal trees) |
| Play summaries / statistics (Calude et al.; Fearnley et al.) | Quasi-polynomial, quasi-linear space | Slowest in benchmarks | Quasi-polynomial (separating automata) |
| Register games (Lehtinen) | n^O(log n) | Not competitive | Quasi-polynomial (separating automata) |
| Attractor decomposition (Zielonka; Parys; Lehtinen–Schewe–Wojtczak) | Quasi-polynomial for the modified versions | Classic Zielonka is the strongest general solver | Classic: exponential; modified: quasi-polynomial |
| Strategy improvement (incl. symmetric, universal-tree variants) | Exponential for analysed rules; quasi-polynomial for Koh–Loho | Good; used by synthesis tools | Exponential for many rules; open for others |
| Priority promotion, tangle learning | Exponential | Among the fastest | Exponential (Two Counters) |
| Fixpoint iteration (DFI) | Exponential | Fastest on model-checking games | Exponential on crafted games |

**Structural parameters — Established.** The Strahler number of a game equals its register number, is at most logarithmic in n, and gives a running time polynomial in n times (d/2k)^k ([Daviaud, Jurdziński, Thejaswini 2020](https://arxiv.org/abs/2003.08627)). This explains why games with "simple" nesting are easy and gives a precise trade-off between priorities and structure. *Opinion:* finding a parameter that is small on all games, or proving none exists for a given algorithm class, is the most concrete route to new results.

**Universal graphs and positionality — Established.** [Colcombet, Fijalkow, Gawrychowski, Ohlmann (LMCS 2022)](https://lmcs.episciences.org/10012) turned universal trees into a theory of *universal graphs* for any positionally determined objective, giving generic value-iteration algorithms with matching lower bounds. [Ohlmann (TheoretiCS 2023)](https://theoretics.episciences.org/9724) then showed that an objective is positional over all game graphs exactly when it admits well-ordered monotone universal graphs (under a mild assumption), and [Casares and Ohlmann](https://lmcs.episciences.org/15411/pdf) extended this to memory bounds. The barrier object has become a structural tool.

**Trying to escape the barrier — Established results, open goal.** [Koh and Loho (LMCS 2025)](https://arxiv.org/abs/2108.13338) run strategy iteration over a universal tree, aiming to jump across large parts of the tree instead of walking it. The [symmetric attractor-decomposition lifting algorithm](https://arxiv.org/pdf/2010.08288) combines the two quasi-polynomial families. [Parys and Wiącek](https://arxiv.org/abs/2305.00308) squeezed the exponent further. None of these breaks the quasi-polynomial ceiling, and the stated aim is to find a framework the barrier does not cover.

**Mapping what fails — Established.** Lower-bound constructions keep pace with new heuristics: Two Counters for attractor and tangle methods, exponential symmetric strategy improvement in 2024, and a [2024 survey of tangle-learning variants and the games that delay them](https://research.utwente.nl/en/publications/solving-parity-games-very-slowly/) (van Dijk). Opinion: these hard families share recurring patterns (binary counters, distraction by high priorities), and a common framework for them could explain *why* parity games resist polynomial algorithms.

**Richer models — Established, recent.** Parity objectives in stochastic and timed settings remain active: a direct reduction from stochastic parity games to simple stochastic games ([Berthon, Katoen, Zhou, CONCUR 2025](https://arxiv.org/abs/2506.06223)); a recursive algorithm for sure plus almost-sure parity conditions ([arXiv, Jan 2026](https://arxiv.org/html/2601.03381v1)); the first value-iteration algorithm for stochastic parity games ([Phalakarn, Hasuo, arXiv, Jul 2026](https://arxiv.org/abs/2607.18355)); a zone-based solver for timed parity games ([Geeraerts et al., FSTTCS 2025](https://arxiv.org/abs/2510.07361)). Other angles include a sound and complete equational theory of parity games as string diagrams ([Piedeleu 2025](https://arxiv.org/abs/2501.18499)) and incomplete polynomial-time predictors using graph neural networks ([Hecking et al. 2022](https://arxiv.org/abs/2210.09924)).

**The November 2025 polynomial-time claim — Claim, unverified.** [van der Heijden (arXiv 2511.03752)](https://arxiv.org/abs/2511.03752) claims an O(n² · (n + m)) algorithm based on a new attractor that finds a minimal dominion. As of 14 October 2026 the arXiv record shows only version 1, and I found no peer-reviewed publication, independent confirmation or published refutation. *Opinion:* treat it as unverified. A correct proof would settle a 35-year-old question, and would have to explain how an attractor-based method avoids the exponential families that defeat related attractor algorithms. The fastest community check would be running it on the published hard families in Oink.

## Parity games in practice

In practice parity games are solved routinely: exponential-time algorithms with good engineering handle real model-checking and synthesis instances, and the theoretical champions are rarely used.

| Tool or resource | What it is | Relevance |
| --- | --- | --- |
| [Oink](https://arxiv.org/pdf/1801.03859) (van Dijk, TACAS 2018; [reproduction study 2024](https://www.tvandijk.nl/pdf/2024rrrr_oink.pdf)) | High-performance implementation of modern solvers, including Zielonka variants, the priority promotion family, tangle learning, progress measures and strategy improvement | The standard platform for empirical comparisons; also hosts the code behind recent lower-bound work |
| PGSolver (Friedmann, Lange) | Earlier solver collection and research platform | Historical baseline; reported to be much slower than Oink ([van Dijk, Rubbens](https://arxiv.org/pdf/1909.07659)) |
| Keiren's benchmarks (FSEN 2015) | Parity games from model checking and equivalence checking | The usual real-world test set, cited across the papers above |
| [Strix](https://strix.model.in.tum.de/) (Luttenberger, Meyer, Sickert) | LTL synthesis via deterministic parity automata and parity games | Has taken first place in all SYNTCOMP LTL tracks since 2018 |
| [SYNTCOMP](https://arxiv.org/pdf/2206.00251) | Annual reactive-synthesis competition | Source of a reactive-synthesis benchmark family for parity solvers |

**What wins in practice (Established measurements).** Tangle learning was the fastest solver on large random games in its original evaluation ([van Dijk, CAV 2018](https://link.springer.com/chapter/10.1007/978-3-319-96142-2_14)). Distraction fixpoint iteration (DFI), a simple fixpoint method, was the fastest on model-checking games ([van Dijk, Rubbens 2019](https://arxiv.org/pdf/1909.07659)). In 2021 Strix replaced its strategy-iteration solver with a Rust implementation of DFI ([SYNTCOMP 2018–2021 report](https://arxiv.org/pdf/2206.00251)).

**Symbolic solving.** For games given implicitly (BDDs), space matters more than time: the universal attractor algorithm runs symbolically in O(lg d) symbolic space, improving the O(d lg n) of Chatterjee, Dvořák, Henzinger and Svozil ([Jurdziński, Morvan, Thejaswini](https://arxiv.org/abs/2001.04333v2)).

**Where the real cost lies — Opinion.** Synthesis tools spend most effort constructing the game: Strix builds the automaton on the fly, guided by the solver, so that only relevant states are explored ([Strix](https://strix.model.in.tum.de/)). Recent synthesis work also targets the step before the game, converting Emerson–Lei automata to parity automata via Zielonka trees ([SYNTCOMP report](https://arxiv.org/pdf/2206.00251)). For practitioners, smaller games often buy more than faster solvers.

## Connections to related areas

Parity games are where three areas meet: in logic and automata they are equivalent to core decision problems, in synthesis they are the computational engine, and among quantitative games they are the easiest member of a chain.

&#91;embedded content: how parity games connect · 7 problems, 3 kinds of link\]

The top row lists problems equivalent to parity games or reducing to them; the bottom row lists harder quantitative games that parity games reduce to.

- **Fixpoint logics.** Winning regions are nested least and greatest fixpoints, with priorities playing the role of alternation depth, so solving games and μ-calculus model checking are the same problem ([Czerwiński et al.](https://arxiv.org/abs/1807.10546)). The quasi-polynomial ideas carry over to nested fixpoints of arbitrary monotone functions on finite lattices ([Hausmann, Schröder](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979196); [Arnold, Niwiński, Parys](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2021.9); [Jurdziński, Morvan, Thejaswini](https://arxiv.org/abs/2001.04333v2)).
- **Automata on infinite objects.** Parity games decide emptiness of parity tree automata. Register games gave a quasi-polynomial translation from alternating parity word automata to alternating weak automata, and a logarithmic collapse of the parity index hierarchy on structures between words and trees ([Lehtinen, Boker](https://arxiv.org/abs/1902.10654)). Parys characterised when nondeterministic separating automata can be used to solve games, linking the area to good-for-games automata ([CSL 2020](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2020.32)).
- **Verification and synthesis.** LTL specifications are translated to deterministic parity (or Emerson–Lei) automata, composed into a parity game, and solved; the winning strategy becomes a Mealy machine or circuit ([Strix](https://strix.model.in.tum.de/); [SYNTCOMP report](https://arxiv.org/pdf/2206.00251)).
- **Infinite-duration quantitative games.** Jurdziński's 1998 reduction maps parity games to mean-payoff games, which reduce to discounted and then simple stochastic games ([Parys 2019](https://arxiv.org/abs/1904.12446)). Hard instances travel the same way: Friedmann's parity games yield lower bounds for strategy improvement in all four game classes and, via Markov decision processes, for simplex pivoting rules ([Friedmann 2011](https://lmcs.episciences.org/1026/pdf)).
- **Strategy structure.** Positional determinacy is now understood through universal graphs: an objective is positional exactly when it admits suitable well-ordered monotone universal graphs ([Ohlmann 2023](https://theoretics.episciences.org/9724)), with memory bounds characterised similarly ([Casares, Ohlmann](https://lmcs.episciences.org/15411/pdf)).
- **Total search problems.** Computing strategies lies in UEOPL, alongside the P-matrix linear complementarity problem, piecewise-linear contraction maps and unique sink orientations ([Fearnley, Gordon, Mehta, Savani](https://arxiv.org/abs/1811.03841)).
- **Stochastic and timed variants.** Stochastic parity games reduce directly to simple stochastic games and stay in NP ∩ coNP ([Berthon, Katoen, Zhou 2025](https://arxiv.org/abs/2506.06223)); timed parity games now have a zone-based implementation inspired by Zielonka's algorithm ([Geeraerts et al. 2025](https://arxiv.org/abs/2510.07361)).

## Summary: open questions and opportunities

The central question is unchanged since 1991 — is there a polynomial algorithm? — but the map around it is far sharper: quasi-polynomial is achievable, and the methods that achieve it provably cannot go further.

**Most important open questions**

1. **Polynomial time.** Can the winner be decided in polynomial time? Open; the November 2025 claim is unverified.
2. **Beyond universal trees.** Is there any algorithmic framework not covered by the separating-automaton, attractor-decomposition and black-box-fixpoint lower bounds? A framework that provably escapes them would be progress even without a polynomial bound.
3. **Strategy improvement.** Does any improvement rule run in polynomial time? An answer would also inform the simplex-method question for related linear programs.
4. **Mean-payoff games.** Can they be solved in quasi-polynomial time? Universal graphs cannot do it, so a different idea is needed.
5. **Hardness evidence.** Is there any evidence of hardness beyond the easy P-hardness inherited from reachability games, for example hardness for a total-search class such as UEOPL? Nothing of the kind is known for parity, mean-payoff, discounted or simple stochastic games.
6. **Right parameters.** Is there a structural parameter, beyond Strahler / register number, that is small on all games or on all games produced by verification?

**Promising opportunities (Opinion)**

- *Lower bounds for broader models* — e.g. formal models that capture strategy improvement and attractor methods together — are the most achievable form of negative evidence and have produced steady results.
- *Universal graphs as a general theory* of positionality and memory link algorithms to structure; extending it to stochastic, concurrent or quantitative objectives is active and productive.
- *Independent verification of polynomial-time claims* against the published hard families (Oink, Two Counters, Friedmann games) is a small, high-value service to the community.
- *Practical gains lie upstream:* smaller automata and on-the-fly game construction matter more for synthesis than faster worst-case solvers.
- *Fixpoint generalisations* carry the quasi-polynomial ideas to nested fixpoints over lattices, which reach beyond games into logics and program analysis.

## Sources

Primary sources opened for this review, grouped by topic. For a textbook treatment, start with the parity-games chapter of [Games on Graphs (Fijalkow, ed.; arXiv 2305.10546)](https://arxiv.org/abs/2305.10546v2), published by [Cambridge University Press in 2026](https://www.cambridge.org/core/books/games-on-graphs/parity-games/7777ACE955A751CCB2DF25ECF265883E).

**Foundations and classic algorithms**

- Emerson, Jutla, Sistla. [On model checking for the μ-calculus and its fragments](<https://doi.org/10.1016/S0304-3975(00)00034-7>). TCS, 2001 (conference 1993).
- Zielonka. [Infinite games on finitely coloured graphs](<https://doi.org/10.1016/S0304-3975(98)00009-7>). TCS, 1998.
- Jurdziński. [Deciding the winner in parity games is in UP ∩ co-UP](https://www.dcs.warwick.ac.uk/~mju/Papers/Jur98-IPL.abstract). IPL, 1998.
- Jurdziński. [Small progress measures for solving parity games](https://doi.org/10.1007/3-540-46541-3_24). STACS, 2000.
- Jurdziński, Paterson, Zwick. [A deterministic subexponential algorithm for solving parity games](https://wrap.warwick.ac.uk/28789). SICOMP, 2008.
- Schewe, Trivedi, Varghese. [Symmetric strategy improvement](https://doi.org/10.1007/978-3-662-47666-6_31). ICALP, 2015.

**Quasi-polynomial algorithms**

- Calude, Jain, Khoussainov, Li, Stephan. [Deciding parity games in quasipolynomial time](https://www.cs.auckland.ac.nz/~cristian/crispapers/paritygame-stoc.pdf). STOC, 2017; [journal version](https://www.cs.auckland.ac.nz/~cristian/crispapers/siamj2020.pdf).
- Gimbert, Ibsen-Jensen. [A short proof of correctness of the quasi-polynomial time algorithm](https://ar5iv.arxiv.org/html/1702.01953). 2017.
- Jurdziński, Lazić. [Succinct progress measures for solving parity games](https://arxiv.org/abs/1702.05051). LICS, 2017.
- Lehtinen, Boker. [Register games](https://arxiv.org/abs/1902.10654). LMCS, 2020 (from LICS 2018).
- Parys. [Parity games: Zielonka's algorithm in quasi-polynomial time](https://arxiv.org/abs/1904.12446). MFCS, 2019.
- Parys. [Parity games: another view on Lehtinen's algorithm](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2020.32). CSL, 2020.
- Lehtinen, Parys, Schewe, Wojtczak. [A recursive approach to solving parity games in quasipolynomial time](https://lmcs.episciences.org/8953). LMCS, 2022.
- Jurdziński, Morvan, Thejaswini. [Universal algorithms for parity games and nested fixpoints](https://arxiv.org/abs/2001.04333v2). 2020–22.
- Daviaud, Jurdziński, Thejaswini. [The Strahler number of a parity game](https://arxiv.org/abs/2003.08627). ICALP, 2020.
- Jurdziński, Morvan, Ohlmann, Thejaswini. [A symmetric attractor-decomposition lifting algorithm](https://arxiv.org/pdf/2010.08288). 2020.
- Parys, Wiącek. [Improved complexity analysis of quasi-polynomial algorithms](https://arxiv.org/abs/2305.00308). CiE, 2023.
- Koh, Loho. [Beyond value iteration for parity games: strategy iteration with universal trees](https://arxiv.org/abs/2108.13338). LMCS, 2025.

**Lower bounds and barriers**

- Friedmann. [Exponential lower bound for the latest deterministic strategy iteration algorithms](https://lmcs.episciences.org/1026/pdf). LMCS, 2011; [LICS 2009 Kleene Award paper](https://lics.siglog.org/2009/Friedmann-AnExponentialLowerB.html).
- Friedmann. [Recursive algorithm for parity games requires exponential time](https://doi.org/10.1051/ita/2011124). RAIRO, 2011.
- Avis, Friedmann. [An exponential lower bound for Cunningham's rule](https://ar5iv.arxiv.org/html/1305.3944).
- Czerwiński, Daviaud, Fijalkow, Jurdziński, Lazić, Parys. [Universal trees grow inside separating automata](https://wrap.warwick.ac.uk/110346). SODA, 2019; [arXiv](https://arxiv.org/abs/1807.10546).
- Arnold, Niwiński, Parys. [A quasi-polynomial black-box algorithm for fixed point evaluation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2021.9). CSL, 2021.
- Fijalkow, Gawrychowski, Ohlmann. [Value iteration using universal graphs and the complexity of mean payoff games](https://drops.dagstuhl.de/opus/volltexte/2020/12701/). MFCS, 2020.
- van Dijk. [A parity game tale of two counters](https://doi.org/10.4204/EPTCS.305.8). GandALF, 2019.
- van Dijk, Loho, Maat. [The worst-case complexity of symmetric strategy improvement](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2024.24). CSL, 2024.
- van Dijk. [Solving parity games, very slowly](https://research.utwente.nl/en/publications/solving-parity-games-very-slowly/). LNCS 15262, 2024.
- [PIGGY project report (CORDIS)](https://cordis.europa.eu/project/id/893732/reporting/es).

**Theory of universal graphs, positionality, total search**

- Colcombet, Fijalkow, Gawrychowski, Ohlmann. [The theory of universal graphs for infinite duration games](https://lmcs.episciences.org/10012). LMCS, 2022.
- Ohlmann. [Characterizing positionality in games of infinite duration over infinite graphs](https://theoretics.episciences.org/9724). TheoretiCS, 2023.
- Casares, Ohlmann. [Characterising memory in infinite games](https://lmcs.episciences.org/15411/pdf). LMCS.
- Fearnley, Gordon, Mehta, Savani. [Unique end of potential line](https://livrepository.liverpool.ac.uk/3089393/). JCSS, 2020; [arXiv](https://arxiv.org/abs/1811.03841).
- Hausmann, Schröder. [Quasipolynomial computation of nested fixpoints](https://pmc.ncbi.nlm.nih.gov/articles/PMC7979196). TACAS, 2021.

**Practice and tools**

- van Dijk. [Oink: an implementation and evaluation of modern parity game solvers](https://arxiv.org/pdf/1801.03859). TACAS, 2018; [Reproducing parity game algorithms with Oink](https://www.tvandijk.nl/pdf/2024rrrr_oink.pdf), 2024.
- van Dijk. [Attracting tangles to solve parity games](https://link.springer.com/chapter/10.1007/978-3-319-96142-2_14). CAV, 2018.
- van Dijk, Rubbens. [Simple fixpoint iteration to solve parity games](https://arxiv.org/pdf/1909.07659). GandALF, 2019.
- Meyer, Sickert, Luttenberger. [Strix](https://strix.model.in.tum.de/); [SYNTCOMP 2018–2021 report](https://arxiv.org/pdf/2206.00251).

**Recent extensions (2025–2026)**

- van der Heijden. [Attractors is all you need: parity games in polynomial time](https://arxiv.org/abs/2511.03752). arXiv, Nov 2025 (unrefereed claim).
- Berthon, Katoen, Zhou. [A direct reduction from stochastic parity games to simple stochastic games](https://arxiv.org/abs/2506.06223). CONCUR, 2025.
- Geeraerts, Herbreteau, Raskin, Reynouard. [A zone-based algorithm for timed parity games](https://arxiv.org/abs/2510.07361). FSTTCS, 2025.
- Piedeleu. [The algebra of parity games](https://arxiv.org/abs/2501.18499). arXiv, 2025.
- [Algorithm and strategy construction for sure-almost-sure stochastic parity games](https://arxiv.org/html/2601.03381v1). arXiv, Jan 2026.
- Phalakarn, Hasuo. [Value iteration for stochastic parity games](https://arxiv.org/abs/2607.18355). arXiv, Jul 2026.
- Hecking, Muthukrishnan, Weinert. [Predicting winning regions in parity games via graph neural networks](https://arxiv.org/abs/2210.09924). 2022.
