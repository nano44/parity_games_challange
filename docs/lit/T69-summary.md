# T69 summary for the Lead: box 208's Dijkstra-type potential against the literature (one page)
L-LIT successor, 2026-11-12 (date -u in the commit). Unrefereed. Not a TARGET.md claim; G-N5-TIME stays OPEN; box 208 stays CANDIDATE.
Details, quotes and locations: docs/lit/T69-dijkstra-potentials-policy-iteration.md; T68 item 3: docs/lit/T66 Addendum C.
Labels: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source). «NEW» = not found in about thirty
opened sources and six searches (T69 §6); a search result, not a theorem.

## 1. Verdicts
| claim (box 208, claude/l-new 8db300fe) | label | by what |
| --- | --- | --- |
| two-player shortest-path games with weights ≥ 0 are solved by a Dijkstra pass (settle the lowest label) | KNOWN | Khachiyan et al., DIMACS TR 2007-02, Theorem 1; Games on Graphs (arXiv 2305.10546) Theorem 5.14; Bertsekas arXiv 1608.01670 Prop. 5.1-5.3 |
| strategy iteration on that class, as an algorithm | KNOWN, finite termination only | Hansen–Ibsen-Jensen–Miltersen arXiv 1201.3498 §2, Theorem 2.5 («the number of strategies is finite»); Bertsekas §5.2 («a finite number of iterations»; p.30: Dijkstra vs PI «unclear») |
| §10 Statement ABS: Howard makes ≤ (edges of Max)·(vertices) steps, by the potential (lowest lagging value, −front size) | NEW, weakly (elementary; all ingredients classical) | not in the sources above, nor in Björklund–Vorobyov (pseudopolynomial bound, p.219), Guillot–Stauffer, Luttenberger, Cadilhac–Casares–Ohlmann |
| the same with ONE player | KNOWN (Bellman–Ford form) | Cochet-Terrasson–Gaubert Theorem 2.3: ≤ n − 1 steps |
| Lemma LEVEL on Γ(G); Lemma PLATEAU's reduction to a one-player run | NEW (fleet-internal class) | the bound PLATEAU calls is landed R118 (i); outside: T65 |
| WIN / K1-TCYC / FVS-TCYC: Howard's steps polynomial at fixed Ξ-feedback number k | NEW as a statement | no fixed-parameter bound on strategy-improvement STEPS found; nearest: Auger–Coucheney–Strozecki arXiv 1402.0471 Lemma 5 (MAX-acyclic simple stochastic games, ≤ 2·n_M steps: the k = 0 analogue, cf. R122) |
| parity games are solvable in polynomial time at fixed k (directed feedback vertex set; k vertices of one player; DAG-width; treewidth) | KNOWN, by other algorithms | Gajarský et al. MFCS 2015 Theorems 3, 4 (O*(4^k p^(log k))); Mnich–Röglin–Rösner arXiv 1512.03246 Theorem 1; Berwanger et al. Theorem 4.5; Fearnley–Schewe arXiv 1112.0221 |
| ABS or ALL-TCYC against the lower bounds (Friedmann; Zhong–Ye; Hansen–Zwick; Asadi et al.) | no CONTRADICTION | T69 §5 |

## 2. Where the known exponential families would break the abstract form (the two steps a referee should press)
- Friedmann's G_n (two players, Howard): the hypothesis «Odd's choices are decided at class level, and class-level weights are
  non-negative». In box 208: (K2) COARSE with (K3) (d) and NO-TIE, i.e. E-DOM; used in (L3), (P4) and QUIET-N. On G_n the coarsest
  class map leaves all flips inside one class-constant tail ((P4) / QUIET-N false); the finest makes the weights signed ((K3) false).
- Zhong–Ye / Hansen–Zwick (one player, mean payoff): the hypothesis «few classes of cycles». In box 208: (L3) case (β) with (L5)
  (m_t = (c, ∅) for a cycle node c: at most M values). For mean payoff the class of a cycle is its mean; Zhong–Ye's cycles have
  «strictly increasing mean rewards» and every state lags to the end. Everything else of the abstract form holds there.

## 3. Other items
- Orientation: in ABS the maximiser improves (Björklund–Vorobyov's LSP); in Hansen–Ibsen-Jensen–Miltersen and Bertsekas the
  minimiser does. A citation must say so.
- The Ξ-feedback number is not the directed feedback vertex number of Γ(G) (W-edges are not counted), so Gajarský et al. Theorem 3
  is not a statement about it.
- D18 lead: PPI (Cadilhac–Casares–Ohlmann arXiv 2110.07346, Question 19): iterating a two-player Dijkstra potential; no
  superpolynomial lower bound known to its authors (who expect one). Not a polynomial-time claim.
- T68 item 3 (T66 Addendum C): the ranking game (arXiv 2512.16684 Fig. 4.1) and the symmetric game (arXiv 2309.02223 Tables 1, 2)
  violate E-DOM at all gates but the top two; Mei's game (arXiv 2610.27386 Table 1) is a discounted game with signed costs, top
  scale −R: no parity table, cost analogue fails. No published family checked is E-DOM-compatible.
- NOT OPENED: Hansen–Kaplan–Zwick SODA 2014 (HTML wall), Khachiyan–Gurvich–Zhao CSR 2006, Schewe CSL 2008, Obdržálek CAV 2003.

## DONE / FINDINGS / NEEDS
- DONE: T69 note, this page, T66 Addendum C, notebook.
- FINDINGS: §1-§3.
- NEEDS: Lead: relay §2 to the referees of box 208 and §3's first bullet to L-NEW. Owner: nothing.

## Update (2026-11-12, after T70; append-only): docs/lit/T70-step-bounds-and-ppi.md
- §1 row 3 (Statement ABS) is to be read with this: a LINEAR step bound for all-switch strategy improvement on two-player
  non-negative-weight reachability games IS published, in the MIRROR orientation (the minimiser improves): Jurdziński–Trivedi arXiv
  0907.3414 Lemma 19; for finite games ≤ n − 1 steps by a Dijkstra-order induction (IMPLIED, READING). Box 208's orientation (the
  maximiser improves) is not covered and the induction fails there (designed instance, T70 §2.3). ABS stays NEW (searched), weakly.
- ABS and LEVEL are about the all-switch step only: single-switch rules are exponential on acyclic instances (Björklund–Vorobyov
  §10; R17 (f)).
- LEVEL is not PPI's potential under Howard's rule: the game of ONE PPI round is an ABS game; PPI solves it in one Dijkstra pass,
  ABS bounds Howard's steps on it; nothing transfers to or from the number of PPI rounds (Question 19). T70 §3.
- Schewe CSL 2008 and Rutkowski arXiv 1107.1199 are now OPENED: no step bound in either.

