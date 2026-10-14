# RANKING: candidate attack approaches (L-LIT, T2)

Barrier ids (B1-B17) refer to docs/lit/BARRIERS.md; sources and theorem numbers are there and in notes/L-LIT.md.
Ranking = L-LIT judgement (opinion, labelled as such) of promise x distance from proven barriers x cost of a first result.
"New against the literature" means: not found in the sources opened on 2026-10-14 (arXiv sweep 2023-2026 included; best-effort,
not exhaustive). Each first problem is stated so a lane can start; TARGET.md §7e requires it to be restated in TARGET
vocabulary and approved before proof work. Whether lower bounds for algorithm classes count as M3 is not settled by
TARGET.md §4 (it lists only restricted-class and parameterised results): Lead/owner to rule.

| rank | approach | promise for M4 | distance from barriers | first problem (short) |
| --- | --- | --- | --- | --- |
| 1 | deterministic WEAK separators (beyond strong-safety) | high leverage, low probability | outside B1/B2 by definition; only B16 (time-bounded) touches it | exact minimal weak separators for small (n,d) |
| 2 | lower bounds for straight-line symbolic programs | none (negative evidence) | extends B3 to a strictly broader model | straight-line Cpre programs need universal-tree length |
| 3 | attractor / dominion methods incl. polynomial partial solvers | low (many failures) | no formal barrier (B4 gap); instance-level B5-B7 | Strahler threshold of psolQ-type solvers |
| 4 | strategy improvement / LP / LCP / USO | low-medium | B8-B14 dense but rule-specific; |V|-step rule exists | Random-Facet lower bound on parity games (withdrawn gap) |
| 5 | structural parameters | M3 only (TARGET §4) | not barrier-limited | parameters of the hard families |
| 6 | proof complexity (weak automatizability) | conditional | not barrier-limited; rests on an open proof-complexity problem | resolution size for Two Counters formulas |
| 7 | IPM / tropical LP | very low | B15 (strong-polynomial only) | are the LW_r instances parity games? |

## 1. Deterministic weak separators (and non-safety separators)
- Why: Czerwiński et al. (1807.10546) Prop. 3.2 reduces solving G to the safety game G ⊲ A for any DETERMINISTIC safety
  (n,d)-separator A of EvenCycles_{n,d} vs OddCycles_{n,d} (weak separation). Their lower bound (Thm 5.1) is only for strong
  separators (must also reject all of LimsupOdd_d), as they state in §3.3; §6 leaves the weak case open. A poly-size,
  poly-time-constructible deterministic weak separator would give a polynomial algorithm (|G ⊲ A| = |G|·|A|).
- Barrier that threatens it: none proven. B16 (Kozachinskiy-Vyalyi Thm 2) only for separators deciding within t = O(n^(5/4))
  steps; they note "Even super-linear lower bounds for unrestricted separation automata are not known" (p.6).
- Known to fail: every known construction (play summaries, universal trees, registers) is strong (1807.10546 §4).
  Non-deterministic weak separation is easy, but Prop. 3.2 "does not hold for non-deterministic automata" (§3.3).
- First problem (computational + proof, new as far as L-LIT found): for all n <= 5 and even d <= 6, compute exactly
  w(n,d) = minimum number of states of a deterministic safety automaton over the priority alphabet {1..d} that accepts every
  infinite path of every even graph with <= n vertices and priorities <= d (EvenCycles_{n,d}) and rejects every infinite path
  of every odd graph (OddCycles_{n,d}); compare with s(n,d) = minimum size of a deterministic STRONG separator (= minimum leaves of an (n, d/2)-universal
  tree by CFGO Thm 4.1 + Lemma 6.8; no closed form, so compute it with the same encoding; see T4-weak-separators.md §3). Deliverable: the table w vs s, a SAT/BDD encoding that L-COMP can rerun, and,
  if w(n,d) < s(n,d) for some (n,d), the explicit automaton (a new object); if w = s on the whole table, a conjecture with the
  smallest open case. Owner of the encoding: L-COMP; statement: L-LIT/attack lane.

## 2. Lower bounds for straight-line symbolic programs
- Why: B3 (Arnold-Niwiński-Parys Thm 5.1) forces universal trees only on recursions of the specific ‖F‖_{U,V} shape; B4 notes
  no theorem for attractor-based or set-based symbolic algorithms (Chatterjee-Dvořák-Henzinger-Svozil 1909.04983 p.19: open).
  Negative evidence for a broader model is achievable and is the kind of result the field produces (landscape opinion,
  re-checked: ANP p.16 calls the absolute version "an intriguing question").
- Barrier: this IS a barrier-building lane; risk is that the model is too strong (adaptive programs can isolate vertices and
  read the graph, so the model must be non-adaptive / symbolic).
- First problem (new as far as L-LIT found): a straight-line symbolic program over (n,d) is a fixed sequence of set
  operations X_i := X_j ∪ X_k | X_j ∩ X_k | V \ X_j | CpreE(X_j) | CpreO(X_j), starting from the priority classes
  P_0..P_d and V_E, V_O, and ending with a set claimed to be W_E. Prove: any such program correct on all games with n
  vertices and priorities <= d has length >= C(⌊lg n⌋+d/2-1, ⌊lg n⌋)/poly(n,d); or exhibit programs of length poly(n) for some
  d = ω(log n) (either answer is new). Start with the restriction "monotone programs" (no complement inside Cpre
  arguments) where ANP's Remark 5.5 AND/OR functions should embed.

## 3. Attractor / dominion methods, incl. polynomial partial solvers
- Promise: lowest per unit of effort for M4: classic members are exponential (B5 Friedmann; robust B5 Benerecetti et al.;
  B6 Two Counters, empirical + sketch), and polynomial members are incomplete (B7, HKP Fig. 6). It is also where new claims
  appear (arXiv 2511.03752, see 2511.03752-position.md).
- Barrier: no theorem covers the class (B4); ANP Thm 5.1 (B3) covers only non-adaptive tree-driven versions.
- First problem (new as far as L-LIT found; HKP prove psolB solves Büchi and weak games, not a Strahler statement):
  determine the largest k such that psolQ (HKP 1405.0386 Fig. 5) decides every vertex of every parity game of Strahler
  number <= k (Strahler number per Daviaud-Jurdziński-Thejaswini 2003.08627 §2), and give a game of Strahler number k+1
  it leaves undecided; repeat for Algorithm 1 of 2511.03752 (if M2 finds it incomplete). Deliverable: theorem + minimal
  instance; serves M2 directly (explains WHY the claim fails, not just that it fails).

## 4. Strategy improvement / LP / LCP / USO
- Promise: low-medium. A |V|-iteration rule exists (Friedmann LMCS Lemma 4.3), so no rule-free SI barrier exists for classical
  SI; but every analysed natural rule fails (B8-B11), symmetric SI fails for all local rules (B11), path prediction is
  PSPACE-complete (B12). AUSO lower bounds do not transfer (B14). Bit cost per iteration must be counted (TARGET §3).
- First problem (closes a gap the literature reopened): the SODA 2011 Random-Facet lower bound for parity games is withdrawn
  (errata 1410.7871); only Random-Facet* survives, and the best upper bound is e^O(sqrt(n ln(m/n))) (Zwick 2607.06334 Thm 8.2).
  Construct sink parity games G_N of size poly(N) on which ORIGINAL Random-Facet strategy improvement (fresh uniform random
  choice at every recursive call) needs 2^(N^Ω(1)) expected iterations, or prove an n^O(log n) upper bound for it on parity
  games. Before starting: open Hansen's 2012 thesis (MDP Random-Facet bound, cited in the errata; 404 today) to rule out
  that it already transfers.

## 5. Structural parameters (M3 only)
- Known polynomial classes: bounded treewidth (Obdržálek thesis Thm 4.3; Fearnley-Schewe 1112.0221 Thm 7.5, NC^2 Cor. 8.8),
  DAG-width (Berwanger et al. Thm 4.5; Fearnley-Schewe Thm 6.4), entanglement of a strategy subgame (Berwanger-Grädel
  LPAR 2004 Thm 21), tree-depth (AC0, Staniszewski CSL 2023 Cor. 29), k·lg(d/k) = O(log n) for Strahler number k
  (DJT Thm 32), few vertices of one player (Mnich-Röglin-Rösner 1512.03246). Clique-width: secondhand only (not opened).
- First problem (new as far as L-LIT found): compute the Strahler number, and upper bounds on treewidth and DAG-width, of the
  hard families tc N, counter_core N, recursiveladder N and Friedmann's SI games G_n; prove the asymptotics for tc N. If some
  standard parameter is O(1) on a family, its exponential lower bound is explained by an algorithm's blindness to that
  parameter (and the family is no longer a hard family for a parameterised algorithm).

## 6. Proof complexity
- Beckmann-Pudlák-Thapen (ECCC 2013/092) Cor. 2.4: "both players win" has poly-size Res(k) refutations for a constant k;
  Cor. 2.6: if resolution is weakly automatizable, parity games are in P. Atserias-Maneva (ECCC 2010/197) Cor. 1: the
  analogue for mean-payoff games and Σ2-Frege.
- First problem: for the BPT formulas Win0 ∪ Win1 of the Two Counters games tc N, prove a polynomial upper bound or an
  n^ω(1) lower bound on Resolution (Res(1)) refutation size; start by measuring proof sizes from a SAT solver's proof log for
  N <= 5 (L-COMP). A polynomial Res(1) upper bound for all games would reduce M4 to weak automatizability of resolution itself.

## 7. Interior point / tropical LP
- B15 shows IPMs are not strongly polynomial; parity games via Jurdziński's weights have polynomial bit size, so B15 does not
  bite in the bit model, but no IPM-based parity algorithm is known to L-LIT. Akian-Gaubert-Guterman 0912.2462 Thm 3.2
  links tropical cones to mean-payoff values.
- First problem: decide whether the long-and-winding LPs LW_r(t) of 1708.01544 tropicalize (via AGG Thm 3.2) to mean-payoff
  games that are images of parity games under Jurdziński's reduction. If yes, B15 becomes a barrier for IPM-on-parity
  claims; if no, record why.
