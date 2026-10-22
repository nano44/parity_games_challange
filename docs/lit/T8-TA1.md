# T8: novelty of L-ATTR's T-A1 (completeness class PA for psolB / psolQ) (L-LIT, 2026-10-14)

Statement checked: claude/l-attr fdb5092, docs/attr/A1-results.md §3. T-A1: "psolB, and psolQ, completely solve every parity
game G such that each of W_E(G) and W_O(G) admits an attractor decomposition (D1) in which every trap S_i, at every level,
is a trap for the opponent in the subgame being decomposed at that level" (predicate PA).

**Verdict: NEW** (no source found that states PA or an equivalent completeness class). There is one CORRECTION to L-ATTR's
expectation: PA does NOT contain HKP's Büchi class (Thm 7) or SCC-constant class (Thm 8). It does contain HKP's
deterministic class (Lemma 5). So PA is incomparable with HKP's known complete classes, not an extension of them.

## (1) Is T-A1 or an equivalent class already known?
Sources opened (notes/L-LIT.md):
- **HKP** (arXiv 1405.0386 v2):
  - Thm 7: "Let G be a parity game whose colors are only 0 and 1. Then G is in S, i.e. psolB completely solves G." This is
    the Büchi class, in min-parity.
  - Lemma 5: "Let G be a deterministic parity game. Then psolB solves G completely."
  - Thm 8: "Let G be a parity game such that for each of its maximal strongly connected components C there is some color c
    such that c(v) = c for all v in C. Then psolB completely solves G."
  - No other completeness class is stated, and none uses attractor decompositions.
- **Ah-Fat, Huth, "Partial Solvers for Parity Games: Effective Polynomial-Time Composition"** (arXiv 1609.04085 v1, GandALF 2016).
  - Thm 1: composed solvers containing scc0, ari and fa leave no residual 1-player game.
  - Conclusions, verbatim: "we do not, at present, have a good understanding of what types of parity games are solved
    completely for certain partial solvers. More powerful versions of Theorem 1, which extend to classes of 2-player games,
    would be a first step in addressing that weakness."
  - This names T-A1's question as open.
- **Vester, "Winning Cores in Parity Games"** (arXiv 1602.01963 v1).
  - Abstract: "the winning core contains all fatal attractors but is not necessarily a dominion itself"; Thm 1 and Thm 3
    concern the winning core.
  - No completeness class is given for psolB or psolQ.
- **Bruyère, Pérez, Raskin, Tamines, "Partial Solvers for Generalized Parity Games"** (arXiv 1907.06913 v2).
  - It combines partial solvers with Zielonka's algorithm and reports benchmarks.
  - It states no completeness class.
- **arXiv searches** ("partial solver", "fatal attractor", au:Huth AND parity, au:Piterman AND parity) returned no further
  completeness result.
- **Not checked:** citers of 1405.0386 beyond these arXiv hits (Semantic Scholar was rate-limited earlier today).
  Also the FoSSaCS 2013 conference version of HKP; L-LIT read the arXiv v2 journal-style version.

## (2) Does PA contain HKP's complete classes?
- **Deterministic games (HKP Lemma 5): YES.**
  - In a game where every vertex has exactly one successor, a set closed under successors in a subgame G_i is closed in
    the whole level subgame R, because the unique successor of each vertex lies in the set.
  - So every S_i of any attractor decomposition is a trap for the opponent in R, and PA holds.
  - This is L-LIT's argument; L-ATTR's checker can confirm it.
- **Büchi (Thm 7) and SCC-constant (Thm 8): NO.** Witness, 3 vertices, max-parity (TARGET convention):
  - v: priority 1, only edge v -> v.
  - x: priority 2, owned by Odd, only edge x -> v.
  - w: priority 1, owned by Even, edges w -> w and w -> x.
  - Every play eventually stays at priority 1, so W_O = {v, x, w} and W_E = ∅.
  - Under max -> min translation (p -> 2 - p) its colours are 0 and 1, so it is in HKP's Thm 7 class. Its maximal SCCs {v},
    {w}, {x} are each single-coloured, so it is in Thm 8's class too. So psolB solves it completely.
  - PA fails for W_O, for every choice of d in DJT's Audrey decomposition (arXiv 2003.08627 v2 §2):
    1. w cannot be in an Odd attractor of a set avoiding w, because it is Even's with a self-loop. So w must lie in some
       trap S_i whose priorities are <= 1 (x, of priority 2, is excluded from that piece).
    2. Even's edge w -> x then leaves S_i while x is still in the level subgame R.
    3. So S_i is not a trap for Even in R, at any level containing both.
  - Hence PA ⊉ Büchi, PA ⊉ SCC-constant.
  - This is consistent with L-ATTR's own table: "psolQ solves => PA" fails on 6,914 / 7,813 games.
- **Consequence for the statement:** T-A1 stands as written (it is only a sufficient condition). But A1-results.md §3's
  sentence "which it should contain" is false for Thm 7 and Thm 8. L-ATTR should either drop it, or strengthen the theorem
  to PA ∪ Büchi ∪ SCC-constant (trivially, by HKP), or find a common generalisation.
  - A natural candidate is to relax PA so that S_i only needs to be a trap in R minus the vertices already decided at
    lower levels. The witness escapes into x, which lies in A_1 = Attr_O({v}).
  - L-ATTR's PB ("trap in R \ A") is a different relaxation, and it fails.

## (3) Is PA decidable in polynomial time?
- **Not established by any source, and not by L-ATTR.** PA quantifies over attractor decompositions, of which there can be
  exponentially many.
- **L-LIT reading** (unproved, a candidate for L-ATTR):
  - Traps for the opponent in a fixed R are closed under union, so at each level there is a largest admissible union of
    candidate pieces. That suggests a greedy canonical decomposition that might decide PA level by level in polynomial time.
  - What blocks a quick proof: each piece must itself be PA-decomposable, and it is not clear that PA-decomposable pieces
    are closed under union.
- **Membership decidability does not matter for D1's "new polynomial class" reading:**
  - The algorithm "run psolQ; if the residual game is empty, output; else fall back to any exact solver" is correct on all
    games, and by T-A1 it runs in polynomial time on every PA game.
  - Its outputs are sound by HKP Thm 2 / Thm 4.
  - So PA is a polynomial class in the promise-free sense, like classes defined by a parameter that is hard to compute.
  - Lead to rule whether D1 needs decidable membership.

## M3 value (L-LIT reading, opinion)
- **New:** yes, as far as searched. It answers the open direction Ah-Fat-Huth named, in a first partial form.
- **Fit with D1:** "tighter analysis of a known algorithm" or "a new polynomial class", for psolB and psolQ (both
  O(|V|^2·|E|) or O(|V|^2·|E|·|c|), HKP Thm 5).
- **Value:** low-medium. It is a sufficient condition only, incomparable with HKP's own complete classes, and with unknown
  membership complexity. Its explanatory value for M2 is real: the three 2511.03752 counterexamples are psolQ-undecided,
  and PA names the trap-versus-return obstruction they share.
- **What would raise it:** (a) a version containing Thm 7 and Thm 8 (see the relaxation above); (b) polynomial
  decidability of the class; (c) an exact characterisation of psolQ's complete class.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - T-A1 NEW.
  - PA ⊇ deterministic games, but PA ⊉ Büchi and PA ⊉ SCC-constant (3-vertex witness above).
  - Ah-Fat-Huth 2016 explicitly leave 2-player completeness classes open.
  - PA's membership complexity is open, but a fallback algorithm makes PA a polynomial class without it.
- NEEDS:
  - L-ATTR: check the witness with its checker, and fix the "should contain" sentence.
  - Lead: D1 ruling on whether a polynomial class needs decidable membership.
