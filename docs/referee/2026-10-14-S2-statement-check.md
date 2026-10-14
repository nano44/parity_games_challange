# Referee report: S2 lower-bound statement (targets T1, T2), L-STRUCT 616cf77; T1 refutation (L-COMP 3e44d2c)

Referee: REFEREE. Date: 2026-10-14. Routed by the Lead 2026-10-14 19:51Z. Source: claude/l-struct 616cf77,
docs/struct/S2-lower-bound-statement.md, with S1 (D1–D5, Lemmas 1–3 as refereed in
docs/referee/2026-10-14-S1-C1-weak-separators.md). Sources opened: CDFJLP arXiv 1807.10546v2 §5 (Thm 5.1, Lemmas
5.1–5.3, the construction of G_t) and §2 (Thm 2.3, universal-tree lower bound), from the LaTeX source.

## Verdict (updated 2026-10-15 after the Lead's 20:07Z priority change): T1 is REFUTED at (n,d) = (2,10) in E, S and V
(section 0, checked independently). The S2 statement check below stands for T2 (CHANGES, finding 1) and for the record
(findings 2–4); the T1-specific items are now moot except as documentation.

## 0. T1 refuted: w(2,10) = 4 < 5 = s(2,8) (L-COMP claude/l-comp 3e44d2c, experiments/sat-hard)
Witness A (state 0 initial, ⊥ = rejecting sink), from results/weak_E_n2_d10_k4.json:
δ(0,·) = [1,0,2,0,2,0,2,0,3,0], δ(1,·) = [3,2,3,2,⊥,2,⊥,0,⊥,0], δ(2,·) = [1,2,3,2,3,2,⊥,0,⊥,0], δ(3,·) = [⊥,3,⊥,1,⊥,2,⊥,2,⊥,0].
1. A is a weak (2,10)-separator, my own tools (docs/referee/scratch/wsepref.py, wsepE2d.py, wsepsat.py):
   - V: all vertex-labelled graphs with ≤ 2 vertices, d = 10 (10 + 900 graphs; 340 even, 320 odd): (W1), (W2) hold.
   - S: all one-label-per-pair graphs (11 + 14,641; 2,720 even, 2,360 odd): (W1), (W2) hold.
   - E: exhaustive over all 2^10 × 2^10 cross-edge label-set pairs (A, B) with saturated same-parity self-loops
     (sound by monotonicity: every even graph is a subgraph of its saturated version with the same A, B; likewise
     odd): 11,264 even and 6,144 odd configurations, (W1), (W2) hold; (S2) fails (A is not strong), as expected.
   - Hand check of L-COMP's verify2.py characterisation (its docstring): on vertices {0,1} the simple cycles are the
     loops and the 2-cycles 0 →a 1 →b 0, and a closed walk's maximum is the maximum of its simple cycles' maxima, so
     "even iff every loop label is even and max(a,b) is even for all a ∈ A, b ∈ B" is right; maximal pairs are
     exactly those with B = Bmax(A) and A = Amax(B), which is what maximal_2 keeps; loops saturated and the
     one-vertex graph added. Correct and complete for n ≤ 2.
2. s(2,8) ≥ 5 in E, S, V: my SAT encoding (independent of L-COMP's: no symmetry breaking, (S2) on all states,
   maximal V/S-graphs by brute force): strong k = 4 UNSAT in V and in S (hence in E, since s^V ≤ s^S ≤ s^E);
   strong k = 5 SAT in V (re-verified). Universal tree (2,4): f(2,4) = g(2,4) = 5 (CFGO Props 6.10/6.11), so
   s^E(2,8) = 5 by CFGO Thm 4.1 + Lemma 6.8 + S1 Lemma 2(b); for n = 2 the pattern is h + 1 leaves (one split level
   per height, as in my 3-leaf argument of the C1 report). L-COMP's add_strong encoding (enc.py docstring) is sound
   and complete: for odd p, a rank ρ_p non-increasing on letters < p and strictly decreasing on letter p excludes
   every cycle with odd maximum p; conversely, if all cycles have even maximum, the subgraph of letters ≤ p has no
   cycle through a p-edge, so "maximum number of p-edges on a path from q in that subgraph" is finite (≤ k−1; p-edges
   cross SCCs) and satisfies both constraints. Its "all states reachable" requirement (BFS symmetry breaking) loses no
   generality: an automaton with unreachable states trims to a smaller one, which pads back to k states by
   duplicating a reachable state and redirecting one incoming transition (language and cycle maxima unchanged).
   And for a lower bound only necessary constraints matter: the even graphs used must be even (they are: verify2's
   characterisation), and (W1)'s closure encoding is implied by any separator.
3. Lower bound w(2,10) ≥ 4: my SAT weak k = 3 UNSAT in V at d = 10 (and at d = 8, confirming L-COMP's w(2,8) ≥ 4 and
   S1 Lemma 2(a)); with the witness, w^V = w^S = w^E = 4 at (2,10).
Verdict: w^X(2,10) = 4 < 5 ≤ s^X(2,8) for X ∈ {E, S, V}. T1 ("w^X(n,d) ≥ s^X(n,d−2)") is refuted at n = 2, d = 10, in
all three conventions. Consistent with the refereed cells (T1 held at (2,6) with equality and at (2,8)). The data now
say that a weak separator can save more than one tree level; T2 is the live target.

## Verdict on the statement itself (as routed 19:51Z): CHANGES (statement sound; two consequences overclaimed; one record to fix)
| item | verdict |
| --- | --- |
| (1) T1, T2 well-posed in S1's definitions | OK for T1; CHANGES for T2 (⌊n/c⌋ = 0 undefined), see §1 |
| (2) consequence via CDFJLP Thm 5.1 for X = E; the binomial | OK, derivation correct, see §2 |
| (3) barrier for "solve G ⊲ A" algorithms on TARGET games (X = V) | CHANGES: does not follow from T1 + Thm 5.1 alone; needs a lower bound on s^V, which CDFJLP does not give; and the algorithm class must be stated, see §3 |
| (4) refutation attempts on small cells | none found; my V cells: see §4 |
| (5) dead end "restrict to letters ≤ d−2" | correctly diagnosed; the obstruction instance cited is not the committed automaton, see §5 |

## 1. Well-posedness
T1: "for all n ≥ 1, even d ≥ 4, X ∈ {E,S,V}: w^X(n,d) ≥ s^X(n,d−2)". Both sides are S1 D5 minima: w^X(n,d) exists
(S1 F1), s^X(n,d−2) exists since d−2 ≥ 2 is even and strong separators exist (CDFJLP Prop. 3.1 for E; restriction to
V/S-words only removes constraints). The "equivalently" paraphrase matches D5 ((W1), (W2) over Σ_d, state count
without ⊥). For X = S, V, s^X(n,d−2) has no closed form; S2 §5 says so. Letters for TARGET games are pr+2 ∈
{2..n+2} ⊆ Σ_{n+2} (S1 §1); T1 is stated for the full alphabet Σ_d, which is the right object for w^X. ✓
T2: "there is c ≥ 1 with w^X(n,d) ≥ s^X(⌊n/c⌋, d) for all n ≥ c". For c ≤ n the quantity is defined; the text's
"trivial for n ≤ c" is wrong at n < c, where ⌊n/c⌋ = 0 and s^X(0,d) is undefined (no graphs with 0 vertices; the
empty automaton?). Fix: quantify "for all n ≥ c" only (as the formula line already does) and drop the "trivial" remark,
or define s^X(0,d) = 0. Finding 1.
Consistency with the refereed data: (2,6): w = 3 ≥ s(2,4) = 3 ✓ (E, S, V); (3,6) V: 6 ≥ s^V(3,4) = 5 ✓; (3,6) E:
7 ≥ 5 ✓; (2,4) V: 3 ≥ s^V(2,2) = 2 ✓; (4,4): 8 (E) and 7 (V) ≥ s(4,2) = 4 ✓.

## 2. The consequence for X = E via CDFJLP Thm 5.1
CDFJLP Thm 5.1 (source §5, verbatim): "Every non-deterministic safety strong (n,d)-separator has at least
C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋) states, which is at least n^{lg(d/lg n) − 2}." It is derived from Lemma 5.1 (an
(n,d/2)-universal tree's leaves inject into the states) and Thm 2.3 (every (ℓ,h)-universal tree has at least
C(⌊lg ℓ⌋ + h − 1, h − 1) leaves), with ℓ = n, h = d/2; C(a + h − 1, h − 1) = C(a + h − 1, a). Three points checked:
- Which states are counted: the tree-decomposition (§5.1) is on the non-rejecting states and the injection of Lemma
  5.1 lands in non-rejecting states (leaf ↦ q_{e_1}, a class of ≼_1 on non-rejecting states), so the bound is on
  non-rejecting states, matching S1 D4 (⊥ not counted). ✓
- Which graph class: the proof's even graph G_t (§5.2, "Construction of G_t") has, at every vertex, one self-loop per
  even priority p with 1 < p ≤ d: parallel edges with distinct labels on the same ordered pair. So Thm 5.1 is a
  theorem about convention E (EvenCycles^E), exactly as S2 states ("for X = E"). It does not by itself bound s^S or
  s^V (fewer words to accept). ✓ as written.
- Arithmetic: with d even, d ≥ 4, apply Thm 5.1 at d−2 (even, ≥ 2): s^E(n,d−2) ≥ C(⌊lg n⌋ + (d−2)/2 − 1, ⌊lg n⌋) =
  C(⌊lg n⌋ + d/2 − 2, ⌊lg n⌋). With T1: w^E(n,d) ≥ s^E(n,d−2) ≥ that. ✓ The regime remark (n^{lg(d/lg n) − O(1)})
  inherits Thm 5.1's side condition (the closed form needs 2h ≤ ℓ, i.e. d − 2 ≤ n); harmless as a remark.
Also correct: it would answer CDFJLP §6's question for deterministic automata and give a super-linear bound where KV
p.6 has none; KV's model is S with vertex names, and S1 Lemma 3 handles the role swap (refereed).

## 3. The barrier claim (X = V) and the algorithm class
S2 §1 last sentence: "For X = V it is a barrier for every algorithm of the form 'solve the safety game G ⊲ A for a
fixed deterministic automaton family A_{n,d}' on TARGET games, by S1 Lemma 1."
(a) What T1 gives for V: w^V(n,d) ≥ s^V(n,d−2). A barrier (super-polynomial size of A) needs s^V(n, n) to be
super-polynomial. CDFJLP Thm 5.1 bounds s^E only (§2 above); s^V ≤ s^E, and the data show s^V < s^E ((4,4): 7 vs 8).
No source in S1/S2 gives a super-polynomial lower bound on s^V. So "it is a barrier" does not follow from T1 +
Thm 5.1; it follows from T1 + a strong-separator lower bound in convention V, which is itself an open item (plausible:
CDFJLP's G_t could perhaps be re-encoded with vertex labels at the cost of more vertices, but that is a proof to be
written, not a citation). Finding 2.
(b) Which quantity: an algorithm that is correct on all TARGET games with ≤ n vertices needs A to be a weak separator
only for the letters that occur, {2..n+2}. Conversely such an A must be a weak separator for V-graphs over {2..n+2}:
for an even V-graph H make all vertices Odd's (Even wins everywhere, and Even wins G ⊲ A iff all runs avoid ⊥, i.e.
(W1)); for an odd H make all vertices Even's (Odd wins everywhere, and Odd wins G ⊲ A iff no path's run avoids ⊥,
i.e. (W2)). Shifting {2..n+2} down by 2 gives the alphabet {0..n} with 0 neutral, so by S1 Lemma 2(b) (as repaired)
the relevant minimum is w^V(n, n), not w^V(n, n+2). The barrier should be stated with w^V(n,n) (and T1 applied at
d = n, which needs n even or the obvious rounding). Finding 3.
(c) The class covered, exactly: deterministic algorithms that (i) build an automaton A_{n,d} depending only on (n,d)
(not on G), deterministic, safety, over priority letters, (ii) decide v ∈ W_E by solving the safety game G ⊲ A_{n,d}
from (v, q0), and (iii) whose running time is at least the number of product vertices n·|A| (any explicit construction
of the product). It gives |A_{n,n}| ≥ w^V(n,n), hence time ≥ n·w^V(n,n). Not covered: non-deterministic or
good-for-games automata (CDFJLP §7, CFGO GFSG), automata built from G, symbolic or implicit solving of the product
in time below its size, and all algorithms not of product form (attractor recursions, strategy improvement, …).
CDFJLP §3.3's remark that all known quasi-polynomial algorithms are of product form with STRONG separators means the
weak barrier would be new for exactly the deterministic weak sub-class. S2 should spell (i)–(iii) out. Finding 3.

## 4. Refutation attempts (my own tools, docs/referee/scratch/wsepsat.py, wsepref.py)
A refuting cell is w^X(n,d) < s^X(n,d−2). In convention V the cheapest open cell is (4,6): s^V(4,4) = 7 (table), so a
weak (4,6) V-separator with ≤ 6 states would refute T1 for X = V. My encoding (maximal V-graphs with 1..4 vertices
computed by brute force, one labelling per vertex-permutation orbit) ran:
- V (4,6), 6 states strong: still running after 16 min when the Lead's priority changed (my maximal-graph enumeration
  for 4 vertices is slow); the weak 6- and 7-state cells did not start. Moot for T1 now (section 0); L-COMP reports
  w^E(4,6) ≥ 8 with LRAT-checked proofs (3e44d2c), which SUPPORTS T1 at (4,6) E, so the refutation is specific to the
  high-d cell (2,10). If my job finishes, its line goes into a later commit.
The E cell (weak (4,6) E with ≤ 7 states) needs the maximal E-multigraphs on 4 vertices, which my brute-force tools
cannot enumerate (64^16 graphs); I did not run it (L-COMP is). My S1 report's cells are consistent with T1.

## 5. The dead end (S2 §3–§4): restriction to Σ_{d−2}
Claim: "a weak (n,d)-separator restricted to Σ_{d−2} is a strong (n,d−2)-separator" is false, because minimum-size
weak separators with a reachable odd simple cycle of maximum ≤ d−3 exist; instance "(3,6) V, 6 states, cycle maximum
3; probe_oddcycles.py 3 6 V 6 3".
Checked: (i) The restriction of any weak (n,d)-separator is a weak (n,d−2)-separator (S1 Lemma 2(a)); only strongness
can fail, and it fails iff the restricted reachable transition graph has an odd cycle, i.e. iff the original has a
reachable odd cycle with maximum ≤ d−3 (letters d−1, d are gone). So the diagnosis "odd cycles of maximum ≤ d−3 are
the obstruction" is exactly right. (ii) I ran L-STRUCT's probe at 616cf77 for (3,6) V, k = 6, pmax = 3; it returned
δ = [[1,0,1,0,1,0],[2,1,3,4,3,0],[5,4,3,4,⊥,0],[⊥,3,⊥,4,⊥,0],[2,4,5,4,⊥,0],[3,1,3,4,⊥,0]]. My checker: it is a weak
(3,6)-separator in V over all 74,088 + 330 graphs; its transition graph restricted to letters ≤ 3 has an odd cycle
("mixed" class); its restriction to Σ_4 satisfies (W1), (W2) for (3,4) but not (S2). Dead end confirmed. (iii) The
committed automaton results/automata/weak_V_n3_d6.json (also 6 states) is NOT such an instance: restricted to Σ_4 it
IS a strong (3,4)-separator (all cycles with letters ≤ 4 even; (W1), (W2) hold), and its only odd cycles use letter 5.
So the obstruction depends on which minimum automaton the solver returns; the record should commit the probe's
automaton (as a JSON next to the others) rather than cite a non-deterministic script run. Finding 4.
Also worth recording in §4: the proof route's Step 1 replaces CDFJLP's "resistance" by counts along even-realisable
paths; the probe automaton is a concrete test case for whether that quantity is finite and tree-like.

## T2 after the refutation
T2 ("there is c ≥ 1 with w^X(n,d) ≥ s^X(⌊n/c⌋, d)") is unaffected by (2,10): with c = 2 it asks w(2,10) ≥ s(1,10) = 1.
Well-posed for n ≥ c (finding 1). Its consequence for X = E: w^E(n,d) ≥ s^E(⌊n/c⌋, d) ≥ C(⌊lg⌊n/c⌋⌋ + d/2 − 1,
⌊lg⌊n/c⌋⌋) by CDFJLP Thm 5.1 (E-convention, non-rejecting states, as in §2), which is quasi-polynomial in the same
regime with n replaced by n/c; correct as stated. For X = V the same caveat as §3 applies (no s^V lower bound is cited).
Note that T2 is also the shape a KV-style argument would produce; L-LIT's novelty check (S2 §5) should compare against
KV's time-bounded bound rather than against CDFJLP.

## Findings
1. T2: restrict to n ≥ c (or define s^X(0,d)); the "trivial for n ≤ c" remark is wrong at n < c.
2. The X = V barrier does not follow from T1 + CDFJLP Thm 5.1 (which is for E and uses parallel self-loops in G_t);
   it needs a super-polynomial lower bound on s^V(n, ·), which no cited source provides. State it as conditional on
   that, or add it as a target.
3. State the barrier with w^V(n,n) (letters {2..n+2}, neutral 0 removed by Lemma 2(b)) and list the algorithm class
   (i)–(iii) and what is excluded.
4. Commit the probe's obstruction automaton; the committed weak_V_n3_d6.json does not exhibit the dead end.

## Gaps
- My SAT encoding has no formal proof; its answers agree with L-COMP's LRAT-checked ones on every cell both ran.
- E was checked exhaustively only through the 2-vertex characterisation (sound by monotonicity); V and S by all graphs.
- Nothing machine-checked; T1/T2 are statements only, as S2 says.
