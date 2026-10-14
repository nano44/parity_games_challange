# BARRIERS: known lower-bound frameworks for parity-game algorithms (L-LIT, T3)

Reference for gauntlet step 3 (TARGET.md §5): an algorithm claim must say, for EACH row below, whether it lies
inside the row's model, and if not, why. L-LIT signs off against this file.
Every source was opened by L-LIT or one of its research agents in this session (2026-10-14); the opened copy, version and
page are recorded in notes/L-LIT.md "Sources opened". Text in quotes is verbatim from the opened PDF (superscripts
flattened by pdftotext are restored in plain notation). "L-LIT reading" marks interpretation, not a stated theorem.
Edge/vertex priorities: the separation lower bounds are proved for EDGE priorities; TARGET.md uses vertex priorities
(see B1 fine print).

## Summary table
| id | framework | proven statement (source, theorem) | kind | covers | outside it |
| --- | --- | --- | --- | --- | --- |
| B1 | separating safety automata / universal trees | every non-deterministic safety strong (n,d)-separator has >= C(⌊lg n⌋+d/2-1, ⌊lg n⌋) >= n^(lg(d/lg n)-2) states (Czerwiński et al., arXiv 1807.10546 v2, Thm 5.1) | theorem | CJKLS play summaries, Jurdziński-Lazić, Fearnley et al., Lehtinen via non-det. | weak separators; parity (non-safety) separators; non-priority alphabets |
| B2 | universal graphs / GFSG automata | sizes of minimal separating automaton, GFSG automaton, universal graph coincide (Colcombet-Fijalkow-Gawrychowski-Ohlmann, LMCS 18(3:29) 2022, arXiv 2104.05262 v8, Thm 4.1; Thm 6.9 tree bounds; Cor. 6.13 "informal") | theorem + informal corollary | value iteration over any (n,Parity)-universal graph | as B1 |
| B3 | black-box nested fixpoints, tree-driven | if ‖F‖_{U,V} = ‖F‖ for all F over B^n then U, V are (n,h)-universal (Arnold-Niwiński-Parys, CSL 2021, LIPIcs.CSL.2021.9, Thm 5.1; Remark 5.5: holds already for AND/OR functions, i.e. games) | theorem | non-adaptive universal attractor decomposition (Jurdziński-Morvan; LPSW recursion with fixed trees) | adaptive (input-dependent) trees; algorithms using graph structure beyond fixpoint queries |
| B4 | attractor-decomposition (Zielonka family) | NO general theorem. JMOT arXiv 2010.08288 v1 p.2: "not formally subject to the lower bound from universal trees"; formal coverage only via B3 | gap | - | - |
| B5 | classic recursive (Zielonka) | exponential families: Friedmann RAIRO-ITA 2011 (NOT opened, 403); robust version against memoization + dominion decomposition: Benerecetti-Dell'Erba-Mogavero, arXiv 1709.02099 (abstract, §1) | per-algorithm families | ZLK and variants with memoization/decomposition | quasi-poly variants (LPSW) |
| B6 | priority promotion, tangle learning, FPI ("Two Counters") | Ω(2^sqrt(n)) for zlk, pp, dp, rr, rrdp, tl, atl: van Dijk, GandALF 2019, EPTCS 305.8, §7-§9; "clear from the empirical data", proof only "sketch[ed]" (§8-9) | EMPIRICAL + sketch | the listed Oink solvers | RTL, ORTL, PTL, DTL, PSI solve tc in poly time (Oink README 8fbf0a7) |
| B7 | polynomial partial solvers (fatal attractors) | incompleteness by example: HKP arXiv 1405.0386 v2, Fig. 6 (psol, psolB, psolQ leave an 8-vertex game untouched), Fig. 4 | counterexample | psol, psolB, psolQ (and, L-LIT reading, 2511.03752's A(G,d), see 2511.03752-position.md) | - |
| B8 | classical strategy improvement, deterministic rules | 2^n steps: switch-all (Friedmann LMCS 7(3:19) 2011, Thm 6.14), switch-best (Thm 8.4); Zadeh with a specific tie-break (Disser-Friedmann-Hopp arXiv 1911.01074 v2, Thm 6.18); Cunningham (Avis-Friedmann arXiv 1305.3944, Thm 4) | theorem per rule, fixed start | the named rule + start + tie-break | other rules: a rule with <= |V| iterations EXISTS (Friedmann LMCS Lemma 4.3, from Vöge 2000) |
| B9 | SI, index-based rules | for any ℓ-index-based rule with ℓ(m) = o(m/log m): m^ω(1) iterations on sink parity games (Disser-Loho-Maat-Mosis arXiv 2512.16684 v2, Thm 4.3) | theorem | single-switch rules ranking edges only by global index, o(m/log m) memory | multi-switch; rules using valuations; ~m memory (Obs. 4.1: n memory states suffice for linear time) |
| B10 | randomized SI | Random-Edge: 2^n expected steps on games of size O(n^4) (Friedmann thesis LMU 2011, Thm 4.76). Random-Facet: the SODA 2011 parity bound is WITHDRAWN ("The main result of [1] is thus flawed", errata arXiv 1410.7871 v1 p.1); only Random-Facet* (one permutation) keeps 2^Ω~(sqrt m) | theorem / withdrawn | Random-Edge; Random-Facet* | ORIGINAL Random-Facet: no lower bound on parity games known to L-LIT; upper bound e^O(sqrt(n ln(m/n))) (Zwick arXiv 2607.06334 v1, Thm 8.2) |
| B11 | symmetric SI | exponential "independently of the improvement rule" (van Dijk-Loho-Maat, CSL 2024, arXiv 2309.02223, Thm 1; Lemma 13; Prop. 8: 2^(n+1)-3 iterations, 2n+2 nodes) | theorem, fixed start pair | Schewe-Trivedi-Varghese symmetric SI, any local rule f | other start pairs; "more than only local information" (p.24:3); paper admits instances are trivial for SCC/self-loop preprocessing (p.24:16) |
| B12 | all-switches SI path prediction | EdgeSwitch and OptimalStrategy for Vöge-Jurdziński SI are PSPACE-complete (Fearnley-Savani, LMCS 14(4:9) 2018, arXiv 1507.04500 v4, Thm 1.2, 1.5) | hardness of predicting a run | all-switches SI | not an iteration bound; says nothing about other rules |
| B13 | LCP pivoting (discounted games) | Lemke 2^(n+1)-2 and Cottle-Dantzig 2^(n+1)-1 iterations, "also hold for parity games" (Fearnley-Jurdziński-Savani arXiv 0909.5653 v1, Thm 18-19) | theorem, fixed covering vector / order | those two methods | other covering vectors / orders (p.2) |
| B14 | unique sink orientations | AUSO lower bounds (Matoušek-Szabó Thm 1, Schurr-Szabó Cor. 1, Hollanders et al.) are for ABSTRACT cubes; Matoušek-Szabó p.12: "We do not expect our methods to yield realizable AUSOs" | does NOT transfer | - | no opened source shows game-realizable AUSOs with these bounds |
| B15 | interior point methods (LP view) | no log-barrier (Allamigeon-Benchimol-Gaubert-Joswig arXiv 1708.01544 v2, Thm B = Cor. 31) and no self-concordant-barrier IPM (Allamigeon-Gaubert-Vandame arXiv 2201.02186 v1, Thm 1) is STRONGLY polynomial | theorem (strong-polynomiality only) | path-following IPMs in the stated neighbourhoods | bit-model polynomiality untouched; instances have exponential bit size (2201.02186 p.2: L = Ω(u_n log t)) |
| B16 | weak separation, time-bounded | DFA separating EvenCycles_{n,2} from OddCycles_{n,2} "in time t" needs exp(Ω(n^5/t^4)) states (Kozachinskiy-Vyalyi arXiv 1902.07175 v3, Thm 2) | theorem | deterministic weak separators that decide within t = O(n^(5/4)) steps | t >= n^2: an O(n)-state DFA exists (p.6); "Even super-linear lower bounds for unrestricted separation automata are not known" (p.6) |
| B17 | complexity-theoretic | UP ∩ coUP (Jurdziński IPL 68(3) 1998, Thm 8); solving is in UniqueEOPL ⊆ EOPL ⊆ CLS (Fearnley-Gordon-Mehta-Savani arXiv 1811.03841 v1, Thm 4); P-hard (cited in Fearnley-Schewe arXiv 1112.0221 p.3) | membership | rules out NP-hardness unless NP = coNP | no TFNP-hardness of parity games known (none found) |

## Detail and "what an algorithm must do to lie outside"
B1. Model (1807.10546 §3): safety automaton (deterministic or not) reading only priority sequences over Σ_d; strong
(n,d)-separator = accepts every word of EvenCycles_{n,d} and rejects every word of LimsupOdd_d. Prop. 3.2: a DETERMINISTIC
safety (n,d)-separator (weak: EvenCycles vs OddCycles) already reduces solving G to the safety game G ⊲ A.
§3.3 (after Prop. 3.2): "our proof of the quasi-polynomial lower bound in Section 5 only applies to strong (n, d)-separators". §6 leaves weak
separation and parity separators open. To lie outside: (i) a deterministic WEAK separator (allowed by Prop. 3.2, lower bound
open beyond B16); (ii) acceptance beyond safety (parity separators with few priorities, open per §6); (iii) reading more
than priorities (vertex names, edges: Parys CSL 2020 SFPG automata read (u,p,v) and neither paper states the bound
transfers; Kozachinskiy-Vyalyi use (vertex, priority) letters); (iv) not being a single product with an automaton at all.
Fine print: necessity proofs are for edge priorities; for vertex priorities "the necessity proof does not apply" and
⌊n/2⌋-universal trees suffice (Parys-Wiącek arXiv 2305.00308 v1, §4 p.8). Effect on the exponent: constant only.

B2. CFGO Thm 4.1 needs Ω|n ⊆ L(A) ⊆ Ω (strong). Cor. 6.13 ("All algorithms based on separating automata, GFSG automata,
or universal graphs, have at least quasipolynomial complexity") is explicitly informal (p.28). The intro's claim that ALL
quasi-polynomial algorithms fall into two universal-tree families is prose, not a theorem. Outside: as B1.

B3. Model: compute θ_d x_d ... θ_1 x_1. f with queries to a monotone f: ({0,1}^n)^d -> {0,1}^n, by the tree-parameterised
recursion ‖F‖_{U,V} with trees fixed for all f. Not an absolute query lower bound (ANP p.2, p.16: open whether it can be
strengthened). Outside: choose the recursion adaptively from query answers; use the game graph beyond f (attractors on
explicit edges, SCCs, strategies). ANP p.16: "any polynomial algorithm for parity games – if it exists – should involve some
other structure of the game".

B4-B7. There is NO theorem lower-bounding "attractor-based" or "dominion-based" algorithms as a class, nor set-based
symbolic algorithms (Chatterjee-Dvořák-Henzinger-Svozil arXiv 1909.04983 p.19 lists it as open). Claims in this family are
checked against B5-B7 families (instances, not theorems); a claim must say why it is complete where psolQ (B7) is not.

B8-B13. Every SI/pivoting lower bound fixes a rule (and usually a start strategy or tie-break). For classical SI a
|V|-iteration rule exists (non-constructively). A claim in this family must name its rule, show it is outside B8-B11
(not index-based with o(m/log m) memory, not symmetric-local, not the named rules) and argue polynomial iterations AND
polynomial bit-size per iteration (TARGET §3: valuations over Jurdziński's weights (-n)^p carry Θ(d log n)-bit numbers;
discounted-game reductions need 1 - γ exponentially small, Hansen-Miltersen-Zwick arXiv 1008.0530 Thm 6.5 bound then
exponential).

B15. Irrelevant to bit-model polynomiality; relevant only to "strongly polynomial via LP/tropical" claims.

## Re-verification of the landscape doc's "Established" rows (used by TARGET.md / owner brief)
| landscape claim | primary source and theorem | verdict |
| --- | --- | --- |
| best upper bound n^(log2(d/log2 n)+O(1)) (Parys-Wiącek 2023) | PW23 Thm 4.1: O(m·n^(1.45+log2(d/log2 n))/d) for d = ω(log n), vertex priorities; same exponent already in Jurdziński-Lazić arXiv 1702.05051 v3 Thm 7(4) (O(dmη^(lg(d/lg η)+1.45)), corrected to d^2 by PW23 Remark 4.3) | bound CORRECT; credit misleading (PW23 gains Θ(d^2) only); hypotheses d = ω(log n) and vertex priorities omitted |
| polynomial when d = O(log n) (attributed to Calude et al.) | CJKLS STOC 2017 Thm 2.8: O(n^5) "If m < log(n)"; SICOMP Thm 16: m <= log(n). d = O(log n) is Jurdziński-Lazić Thm 7(3) and Fearnley et al. arXiv 1703.01296 v2 Cor. 3; DJT arXiv 2003.08627 v2 Remark 33 states this split | DISCREPANCY: misattributed; Calude et al. only give d <= log n |
| FPT: O(n^5 + 2^(d log d + 6d)) | SICOMP DOI 10.1137/17M1145288, Cor. 19: O(n^5 + 2^(m(log(m)+6))); STOC version gives only "O(n^5) + g(m)" | matches journal version only; journal PDF says published electronically 14 Jan 2020 (vol. 51(2)), landscape's "2022"/"2020" label unverified |
| quasi-poly O(n^(log d + 6)) (Calude et al.) | STOC Thm 2.9 / SICOMP Thm 18: O(n^(log(m)+6)) | matches (log base not stated in the text found) |
| UP ∩ coUP (Jurdziński 1998) | IPL 68(3) Thm 8 (full author PDF opened); via Thm 4 reduction to MPG with weights (-m)^p(u) | matches |
| NP ∩ coNP (Emerson-Jutla-Sistla) | TCS 258 (2001) Thm 3.3, stated for μ-calculus model checking; parity games via the paper's equivalence | matches in substance; CAV'93 version not opened |
| computing strategies in UEOPL ⊆ EOPL ⊆ CLS | arXiv 1811.03841 v1 Thm 4: "Solving a parity game" is in UniqueEOPL | matches in substance (wording differs) |
| LPSW n^O(log(1+d/log n)) | LMCS 18(1:8) Thm 3.3: O(m·n^(4.9+2 log(1+d/(2 log n)))), d = maximal priority | matches |
| Strahler: poly(n)·(d/2k)^k; poly if k lg(d/k) = O(log n); Strahler = register number; <= log n | DJT Thm 32; Prop. 3 (Str <= ⌊lg n⌋+1); Lemma 7 + Thm 8: Strahler = Lehtinen (defensive register) number; register number differs by at most 1 (p.7) | matches; "= register number" is loose (off by <= 1) |
| separation lower bound "quasi-polynomial, nearly matching" | B1 | matches; add: strong separators, safety, edge priorities |
| universal-tree attractor lower bound (CFGO 2022; JMOT) | CFGO proves none for attractor algorithms; JMOT p.2 says the family is "not formally subject"; the formal result is ANP Thm 5.1 (B3) | DISCREPANCY: wrong sources; correct source is ANP 2021, non-adaptive trees only |
| symmetric SI exponential "for every rule" | B11 | matches; add fixed start pair |
| "Strategy improvement: exponential for the standard switching rules" incl. random rules | B8, B10 | landscape omits that the Random-Facet parity bound was withdrawn (errata 1410.7871) |
| Two Counters lower bound "Established" | B6 | DISCREPANCY: partly empirical, proof sketched; label "established measurement + sketch" |
