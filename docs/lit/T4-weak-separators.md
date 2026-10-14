# T4: are deterministic weak separators already ruled out? (L-LIT, 2026-10-14)

**Verdict: OPEN.** No source found proves a super-linear lower bound on deterministic safety automata that separate
EvenCycles_{n,d} from OddCycles_{n,d} (weak separation). Every quasi-polynomial lower bound found is stated for STRONG
separation, i.e. it also needs the automaton to reject every word whose limsup is odd. The only weak-separation lower bound
is Kozachinskiy-Vyalyi (KV) 2019, and it covers only time-bounded automata. RANKING.md rank 1 stands; a lane may start.
All quotes below are verbatim from the opened PDFs (math flattened). Sources are in notes/L-LIT.md "Sources opened".

## 1. The definitions, side by side
| source (opened) | definition | strong / weak | lower bound stated for it |
| --- | --- | --- | --- |
| Czerwiński, Daviaud, Fijalkow, Jurdziński, Lazić, Parys, arXiv 1807.10546 v2 (SODA 2019), §3.3 | "A is an (n, d)-separator if it is a separator of EvenCycles_{n,d} and OddCycles_{n,d}; ... a strong (n, d)-separator if it is a separator of EvenCycles_{n,d} and LimsupOdd_d" | both defined | Thm 5.1 only for strong: "Every non-deterministic safety strong (n, d)-separator has at least C(⌊lg n⌋+d/2-1, ⌊lg n⌋) states". §3.3: "our proof of the quasi-polynomial lower bound in Section 5 only applies to strong (n, d)-separators" |
| same, Prop. 3.2 (the algorithmic use) | "if A is a deterministic safety (n, d)-separator, then Even has a winning strategy in G if and only if she has a winning strategy in the chained-product safety game G ⊲ A" | WEAK suffices | - |
| same, §6 | "We leave open the question whether a stronger version of our main technical result holds, namely whether every safety automaton separating EvenCycles_n from OddCycles_n has at least quasi-polynomial number of states. Our argument cannot be directly extended to that setting, as already the proof of Lemma 5.2 crucially relies on that fact that no word from LimsupOdd is accepted." | weak: OPEN | - |
| Colcombet, Fijalkow, "Parity games and universal graphs", arXiv 1810.05106 v2 (preprint of their FoSSaCS 2019 line; the Springer FoSSaCS 2019 PDF, DOI 10.1007/978-3-030-17127-8_1, returned an HTML page and was NOT opened) | Def. 3: "For all (n, d)-graphs satisfying parity, the automaton accepts all paths in the graph" and "The automaton rejects all paths not satisfying parity" | STRONG | Thm 1 (smallest universal tree = smallest separating automaton = smallest universal graph) for this definition; the proof of Lemma 6 uses strongness: "all cycles of G are even, since otherwise A would accept a word not satisfying parity" |
| Colcombet, Fijalkow, Gawrychowski, Ohlmann, LMCS 18(3:29) 2022, arXiv 2104.05262 v8 | Def. 3.3: "An (n, Ω)-separating automaton A is a deterministic automaton such that Ω|n ⊆ L(A) ⊆ Ω." Thm 4.1 also covers "a non-deterministic automaton A such that Ω|n ⊆ L(A) ⊆ Ω" | STRONG (L(A) ⊆ Ω) | Thm 4.1 (equal minimal sizes), Thm 6.9 (tree bounds), Cor. 6.13 (informal) |
| Fijalkow (ed.), Games on Graphs, arXiv 2305.10546 (621 pp.), ch. 2 Parity Games (Fearnley, Fijalkow), Def. 2.1 (PDF p.82) | "For all parity graphs G with n vertices and priorities in [1, d] satisfying parity, all paths from v are accepted by A." and "All words accepted by A satisfy parity." "summarised as Parity|n ⊆ L(A) ⊆ Parity" | STRONG | Thm 2.10 (PDF p.101): separating automaton of size s induces an (n, d/2)-universal tree of the same size; stated for Def. 2.1, proof not given in the book |
| Anand, Fijalkow, Goubault-Larrecq, Leroux, Ohlmann, arXiv 2109.08322 v1 (2021), Def. 4 | "Ω|n ⊆ L(A) ⊆ Ω" | STRONG | upper bounds only; §8: lower bounds left open |
| Kozachinskiy, Vyalyi, arXiv 1902.07175 v3 (2019), §1.2-§2 | alphabet {1..n} × {1..d} (vertex AND priority); reach q_accept on every word of EvenCycles_{n,d}, never on OddCycles_{n,d} | WEAK (with vertex names) | Thm 2: "Any deterministic finite automaton separating EvenCycles_{n,2} from OddCycles_{n,2} in time t has exp(Ω(n^5/t^4)) number of states" (time-bounded only). p.5: "(for which no better lower bound that just n is known)"; p.6: "Even super-linear lower bounds for unrestricted separation automata are not known." |

Note on alphabets: CDFJLP's EvenCycles is over priorities only (Σ_d); KV's is over (vertex, priority) pairs. KV p.5 notes
that with vertex names and non-determinism weak separation is "very easy ... just guess a node appearing more then once";
that trick needs vertex names, so for the priority-only alphabet even the non-deterministic weak case is open (CDFJLP §6
does not restrict to deterministic automata).

## 2. Citation search for anything that settles it
- Semantic Scholar citations of 1807.10546 (51 records, read 2026-10-14): titles checked; the only lower-bound papers on
  separators among them are KV (also listed under its v1 title "Lower bounds on separation automata for Parity Games"),
  CFGO 2022, Colcombet-Fijalkow, Fijalkow-Gawrychowski-Ohlmann (mean payoff), Arnold-Niwiński-Parys (fixpoints),
  and "Lower Bounds on Unambiguous Automata Complementation and Separation via Communication Complexity" (2021; NOT opened;
  its title concerns unambiguous automata, not parity separators).
- Semantic Scholar citations of 1902.07175: empty list returned. OpenAlex: 1 citation (daily budget then exhausted;
  the citing work was not listed).
- arXiv API, abstracts containing "separating automat*" (all dates): 2109.08322 (opened, strong), 2205.00744 (Dell'Erba-Schewe,
  opened, "deterministic automata that can be used as witness automata", upper bounds only), "Deterministic and
  game separability for regular languages of infinite trees" (arXiv, May 2021, id not recorded; tree languages, a different
  problem; not opened), 2024
  DFAMiner (finite-word DFA mining, unrelated).
- arXiv author search Kozachinskiy (42 papers): no later separator paper.
- Limit: citation databases were rate-limited; a weak-separator result in a venue not indexed by these sources could be missed.

## 3. Checks on the first problem (RANKING.md rank 1)
Setting (CDFJLP conventions): edge priorities in {1..d}, d even; alphabet Σ_d = {1..d}; A = (Q, q0, δ: Q × Σ_d -> Q ∪ {⊥})
deterministic safety (a word is accepted iff its run never hits ⊥).
- Weak (n,d)-separator: (W1) every infinite path of every even graph with <= n vertices is accepted; (W2) every infinite path
  of every odd graph with <= n vertices is rejected. Strong: (W1) and (S2) every accepted word has even limsup.

a) **w(n,d) is well defined.** The set of weak separators is non-empty: every strong separator is weak (OddCycles_{n,d} ⊆
   LimsupOdd_d), and deterministic strong separators exist (CDFJLP Thm 4.1 / Cor. 4.1, size n^(lg d + O(1))). State counts
   are natural numbers, so the minimum exists, and w(n,d) <= s(n,d) := minimum size of a deterministic strong separator.
   By CFGO Thm 4.1 + Lemma 6.8, s(n,d) = minimum number of leaves of an (n, d/2)-universal tree. Its exact value is
   not given in closed form (CFGO Prop. 6.10/6.11 give an upper recursion f and a lower recursion g), so s(n,d) should be
   computed by the same encoding with (S2) in place of (W2), not taken from a formula.

b) **"Weak separator with k states" is a finite SAT instance.** Variables: δ(q,p) ∈ Q ∪ {⊥} for q ∈ Q, p ∈ Σ_d
   (k·d·⌈log(k+1)⌉ bits). Constraints quantify over graphs with <= n vertices and edge labels in Σ_d: finitely many
   (at most (d+1)^(n^2) labelled edge sets per vertex count, at most one label per ordered pair as in CDFJLP §2.1).
   - (W1) for a graph H: existential closed relation R_H ⊆ V(H) × Q with (v, q0) ∈ R_H for all v, and
     (v,q) ∈ R_H, (v,p,v') ∈ E(H) imply δ(q,p) ≠ ⊥ and (v', δ(q,p)) ∈ R_H. (The reachable set of the product is the least
     such R, so existence of one is equivalent.) Restricting to vertices with an infinite continuation is harmless if graphs
     are required to have no dead ends, as in CDFJLP.
   - (W2) for a graph H: the non-⊥ part of the product H × A reachable from V(H) × {q0} has no cycle; encode with a ranking
     r: V(H) × Q -> [0, n·k) strictly decreasing along reachable non-⊥ product edges. (A deterministic safety automaton
     rejects every infinite path of H iff that product part is acyclic; KV Appendix A gives the matching qn-time bound.)
   - (S2) instead: every cycle of A's own reachable transition graph has even maximum (ranking on A alone).
   - Reduction: (W1) is monotone under taking subgraphs and so is (W2), so only MAXIMAL even graphs and MAXIMAL odd
     graphs (under edge addition, up to isomorphism) need constraints. Feasibility: the raw count (d+1)^(n^2) is about
     10^21 for n = 5, d = 6, so start with n <= 4 and enumerate maximal graphs modulo isomorphism. Engineering belongs to L-COMP.

c) **An observation that sharpens the question** (L-LIT's own, unrefereed; REFEREE to check before any use). Let A be a
   deterministic weak (n,d)-separator. If some cycle C of A's reachable transition graph has odd maximum, take a
   shortest path P from q0 to C. The lasso P ∪ C, read as an edge-labelled graph, has |P| + |C| distinct states, and its
   only cycle is C, which is odd. So it is an odd graph, and the word it generates is in OddCycles_{|P|+|C|}. By (W2) this
   forces |P| + |C| > n. Consequences: (i) a weak separator whose reachable odd cycles are all "short" (lasso length <= n)
   is strong, hence has >= s(n,d) states; (ii) any weak separator smaller than s(n,d) must contain an odd cycle with
   lasso length > n that is still never realised by an odd graph with <= n vertices. This gives the search a concrete
   target and a cheap filter, and it shows w(n,d) can differ from s(n,d) only through long odd cycles.

## 4. DONE / FINDINGS / NEEDS
- Verdict OPEN. Barrier sign-off for rank 1: the threatening results are B1/B2 (strong only), the CDFJLP §6 open question, and
  B16 (KV, time-bounded and with vertex names). A lane on weak separators lies outside all proven lower bounds.
- First problem as stated is well-posed (w(n,d) exists, w <= s) and finitely SAT-encodable. Correction to RANKING.md:
  compute s(n,d) by the same encoding with (S2), since no closed form is known.
