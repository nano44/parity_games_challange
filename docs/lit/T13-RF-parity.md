# T13: novelty of L-RED's lower bound for original Random-Facet on parity games (L-LIT, 2026-10-15)

Asked by the Lead at 12:52Z. The candidate is claude/l-red 8bb9d22, docs/red/R2-RAR.md, signed by REFEREE-2 (995cfd3) and REFEREE (6d5d9ad). It claims that **original** Random-Facet (Matoušek–Sharir–Welzl / Kalai) needs e^{Ω(√n)} expected improving switches on sink parity games of size Θ(n^{3/2} log^3 n). The proof transfers FHZ 1410.7530 Thm 6.3 from shortest paths through a level-lexicographic priority encoding.

All sources below were opened by L-LIT and are logged in notes/L-LIT.md. "p." is the PDF page.

**Verdict: NEW as a stated result** (no published super-polynomial lower bound for original Random-Facet on parity games was found). It is **low in technical novelty**: it is a transfer of FHZ's shortest-path theorem, and FHZ themselves remark that their shortest-path *examples* carry over to parity games. One residual risk: Hansen's 2012 thesis could not be opened.

## (a) A super-polynomial lower bound for original Random-Facet on parity games since 2014?
**None found.**
- **FHZ errata, arXiv 1410.7871 v1.**
  - p.1: "the claim that the expected numbers of steps performed by Random-Facet and Random-Facet∗ are the same is false … The main result of [1] is thus flawed", where [1] is the SODA'11 parity-game paper.
  - p.2: "The error was pointed out briefly in [5], and an alternative proof of a 2^{Ω̃(∛m)} lower bound for the Random-Facet algorithm was given … The proof in [5] was presented for Markov decision processes. In [3] we transfer the lower bound construction to the setting of shortest paths". Here [5] is Hansen's PhD thesis (Aarhus 2012) and [3] is 1410.7530.
  - No parity-game version of the original-Random-Facet bound is given or claimed.
- **FHZ, arXiv 1410.7530 v1**, "Random-Facet and Random-Bland require subexponential time even for shortest paths".
  - Thm 6.3 (p.19): "The expected number of switches performed by the Random-Facet algorithm, when run on the graph G_{n,r,s,t}, where r = Θ(log n), s = Θ(√n log n), and t = Θ(log n), with initial tree B_0, is at least e^{Ω(√n)} = e^{Ω(M^{1/3}/log M)}". Here N = Θ(n^{3/2} log^2 n) vertices and M = Θ(n^{3/2} log^3 n) edges. The size in L-RED's claim matches.
  - p.2: "The lower bound given in [17] is for parity games … The lower bounds given in [18, 23] are for LPs that correspond to Markov Decision Processes … Here, we obtain subexponential lower bounds … on LPs that correspond to standard acyclic shortest paths problems".
  - §9 (p.33) lists open problems: improving the exponent to √m, upper bounds for Random-Facet1P and Random-Bland, and out-degree-2 instances (explicit AUSOs). Parity games are not mentioned.
- **Zwick, arXiv 2607.06334 v1** (7 Jul 2026), Random-Action-Removal, i.e. Random-Facet for two-player games.
  - It is upper bounds only. Its "asymptotically tight" remarks (p.9, §7: "We believe that … the bound F(n,k) ≤ e^{2√(n+k)} is asymptotically tight") are about its recurrence F(n,k), not about game instances.
  - The open problems paragraph (p.12) asks for faster algorithms and deterministic subexponential ones, and states no lower bound.
  - The only lower-bound literature it cites is [Mat94] (AUSOs, p.5), plus Friedmann and Fearnley for Howard's rule (p.18).
  - It states no lower bound for Random-Action-Removal on games.
- **Disser–Friedmann–Hopp, arXiv 1911.01074 v2, p.2.**
  - "a subexponential lower bound was shown for the random-facet rule [FHZ11b, Han12, FHZ14]". The context is the simplex method; FHZ11b is STOC'11 (MDP/LP).
  - The parity paragraph says "a subexponential bound has been shown for the random-facet rule [Kal92, MSW96, Kal97, FHZ11a, FHZ14]". These are mostly *upper* bounds, cited together with the flawed FHZ11a and its errata. L-LIT reading: this is loose wording, not a claim of a valid parity lower bound.
- **DLMM 2512.16684 v2** cites only the errata (ref. 34).
- **arXiv API sweep** (abstracts: "random facet", "random-facet", "random facet" AND parity, "Random-Action-Removal", strategy improvement + random + lower bound). It returned 11 papers. The only other post-2014 hits were checked:
  - 2109.03666 (realizable Matoušek USOs; p.1 "On acyclic USOs, Random Facet requires exp(Θ(√n)) vertex evaluations [4]", Gärtner, an abstract setting);
  - 2410.02634 (VCSP fitness landscapes, where random facet is super-polynomial; not games).
  
  Neither concerns parity games.
- **Hansen's PhD thesis (2012): NOT opened.**
  - www.cs.au.dk/~tdh/papers/dissertation.pdf, the URL given in both FHZ texts, returned **404**.
  - Wayback availability API returned **429** twice.
  - A direct web.archive.org snapshot request got a **connection reset**.
  - Semantic Scholar returned **429**.
  - By the errata (p.2) its original-Random-Facet bound is for MDPs. Whether it also remarks on a parity transfer is unknown. This is the one place a KNOWN or PARTIAL verdict could still come from.

## (b) Has anyone noted that the shortest-path instances re-encode as parity games?
**Not for the lower-bound instances; for small examples, yes, in one sentence.**
- FHZ errata p.2, right after giving the shortest-path examples where Random-Facet and Random-Facet* differ: "It is not difficult to obtain similar examples for parity games." This is the closest statement found.
  - It concerns the f ≠ f* examples of errata §3–4, not the Thm 6.3 family.
  - It gives no encoding.
- FHZ 1410.7530 contrasts its shortest-path instances with the earlier parity games ([17]) and MDPs ([18, 23]) (p.2). It does not say the new instances re-encode as parity games, and §9 does not raise the question.
- Maat 2509.16075 §2 (p.4) gives the reductions parity → mean payoff ("simply replacing w(e) by (−|V|)^{w(e)}") → LSP, the other direction. It makes no remark on encoding shortest paths with arbitrary costs as priorities.
- L-LIT reading:
  - The level-lexicographic encoding (each edge cost written as a sum of (−t)^p over distinct priorities, so that the valuation order matches the path-cost order) is in the spirit of the standard reductions.
  - Random-Facet's run depends only on which switches are improving at each tree. So any encoding that preserves the improving relation on all trees reached transfers the distribution exactly.
  - What the referees signed is that the encoding does this for G_{n,r,s,t}'s costs at polynomial size. That is the content of L-RED's result.

## (c) Verdict
**NEW, as a published statement.** As far as the opened sources show, original Random-Facet on parity games has had no super-polynomial lower bound since FHZ withdrew theirs in 2014. L-RED's statement fills exactly that gap, and it is the gap RANKING.md §4 named.
- **Novelty is in the statement, not the technique.** It is a faithful transfer of FHZ 1410.7530 Thm 6.3. The FHZ errata (p.2) indicate the authors regarded parity transfers of their shortest-path examples as easy. Write it up as "FHZ's shortest-path bound holds for parity games via encoding X", crediting Thm 6.3. It is not a new lower-bound technique.
- **Residual risk:** Hansen's thesis is unopened. The FHZ texts describe its original-Random-Facet bound as an MDP result, so a parity statement there is unlikely, but it is not excluded.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - (a) None found: the errata withdraw the parity bound and point to MDP (Hansen) and shortest-path (1410.7530) replacements only. Zwick 2026 has no lower bound for Random-Action-Removal on games.
  - (b) Only the errata's one-line remark ("similar examples for parity games", p.2), about small examples, not Thm 6.3's family.
  - (c) NEW as a statement, low technical novelty; credit FHZ Thm 6.3.
  - Hansen's thesis is still unopened (404 / 429 / reset).
- NEEDS: owner: a copy of T. D. Hansen, "Worst-case Analysis of Strategy Iteration and the Simplex Method", PhD thesis, Aarhus 2012, only if R2-RAR is to be claimed as "first" outside the fleet.
