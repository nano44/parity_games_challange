# M2: audit of arXiv 2511.03752 v1 (van der Heijden, "Attractors Is All You Need: Parity Games In Polynomial Time")
Closed 2026-10-14 ~18:35Z, about 5 hours after the M2 clock started. Verdict: BROKEN (the algorithm outputs wrong winning regions).

## Evidence
- CE1 (L-COMP), claude/l-comp 19b5ce2, experiments/m2/counterexamples/ce1_4v.pg (max-parity, 4 vertices, all Odd-owned):
  v0 pr1 -> v1; v1 pr0 -> v2,v3; v2 pr2 -> v0; v3 pr0 -> v1. Truth: Even wins all. Algorithm 1 (L-COMP avh.py): Odd wins all.
  Found in a 100-game seeded corpus (game r00036, 18 vertices), shrunk to 8, then hand-reduced to 4 vertices.
- cex1 (REFEREE, independent read and implementation), claude/referee 936d47c, docs/referee/scratch/cex1-minparity.pg
  (paper's min-parity convention) and cex1-maxparity.pg (max-parity twin): v Odd pr3 -> u,x; u Even pr2 -> v; x Even pr4 -> y;
  y Odd pr4 -> x,u. Truth: Even wins all. Algorithm 1, traced by hand from the paper and by aiayn.py: Odd wins all.
- Lead cross-check (2026-10-14 18:33Z, Oink 8fbf0a7): avh.py on cex1-maxparity.pg -> Odd wins all; aiayn.py on ce1_4v.pg
  -> Odd wins all (DISAGREE with its own Zielonka); Oink --zlk -v on both max-parity files -> Even wins all, solution verified.
  So two independent implementations fail on two independent games.

## Obstruction (REFEREE)
- Earliest false step: Theorem 1/2 ("A(G,d) is a player(d)-dominion"), proof sentence "However, as v must be visited, it follows that
  u ∉ U^k". U^{k+1} = U^k \ opp-Attr((V \ A^k) ∪ A'(A^k)) removes only U-vertices from which the opponent can FORCE a visit to A'.
  On cex1 the player avoids A' by never returning to U (cycling x,y at priority 4, excluded from A' by the "ρ(v) < d" filter), so the
  fixpoint A(G,3) = V is not an Odd-dominion. Lemma 2 also fails on cex1; Lemma 3 fails under the charitable reading.
- Readings tested by REFEREE (all fail): (a) literal: wrong answer; (b) drop the ρ<d filter in A': no progress (loop never ends);
  (c) A* restricted to A^k: wrong answer; (d) both changes: no progress. Random search with n ≤ 6: the literal reading is wrong on ~0.3% of games.
- Positioning (L-LIT, claude/l-lit a6c530f, docs/lit/2511.03752-position.md): a psolQ-style partial solver in the
  Huth-Kuo-Piterman "fatal attractors" family (arXiv 1405.0386), polynomial by construction, so it fails on correctness, not on time.

## Pending (not blocking the verdict)
- REFEREE full report landed: claude/referee 7750fa1, docs/referee/2026-10-14-arxiv-2511.03752.md (10 gaps; second counterexample cex2, solitaire; all 16 readings of 4 ambiguities fail on random games; literal reading wrong on 0.4%-2.2% of random games). Pending: AM1-AM9 verdicts on L-COMP pseudocode.
- Nothing is sent to the author or posted anywhere (D1: anything external is the owner's decision).

## Update 2026-10-14 18:40Z (REFEREE claude/referee 120ee69)
- Numbering per the paper's shared counter: the false dominion claim is Theorem 2 (tex:322); minimal-dominion lemma is Lemma 3 (tex:341);
  progress is Lemma 4 (tex:397). The REFEREE's earlier messages were one lower; L-COMP's numbering was right.
- Faithfulness of L-COMP's pseudocode (51f1d1b): AM1-AM9 all faithful (AM4 faithful to intent and sound; AM8 faithful in effect).
  Calibration: L-COMP on opus-5-5 produced a faithful paper-to-code transcription; no redo needed.
- PGSolver generator ports (recursiveladder, switchallexp, switchbestexp; l-comp 135888c): OK by reading; cosmetic citation offsets only.
  Gap: no execution of the OCaml originals (owner Q4).
