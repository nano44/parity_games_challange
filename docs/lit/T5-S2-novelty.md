# T5: novelty of L-STRUCT S2 (lower bound for deterministic weak separators) (L-LIT, 2026-10-14)

Statement checked: claude/l-struct 616cf77, docs/struct/S2-lower-bound-statement.md.
T1: for all n >= 1, even d >= 4, X ∈ {E, S, V}: w^X(n,d) >= s^X(n,d-2). T2 (fallback): w^X(n,d) >= s^X(⌊n/c⌋, d).

**Verdict: NEW** (as far as L-LIT can see, with the search limits in §4), plus one wording correction (§2c).
No source states T1, T2, or ANY super-linear lower bound for deterministic or non-deterministic weak separators over
a priority alphabet. Two primary sources state the question is open. T1 would answer the deterministic case of both.

## 1. Question (1): is T1/T2 or any weak-separator lower bound already known?
Sources opened for T5 (in addition to the T4 set: 1807.10546, 2104.05262, 1810.05106, 2305.10546, 2109.08322, 2205.00744,
1902.07175, CSL 2020.32):
- **Colcombet, Fijalkow, "Universal graphs and good for games automata: new tools for infinite duration games", FoSSaCS
  2019** (author PDF www.irif.fr/~colcombe/Publications/FOSSACS19-colcombet-fijalkow.pdf; this is the paper the Lead named,
  NOT opened in T4).
  - Def. 8: A is "good for (V, n)-games if for all V-games G with at most n positions, G and G × A have the same winner";
    "strongly good for (V, n)-games if it is good for (V, n)-games and the language accepted by A is contained in V."
  - Def. 9: "An automaton A is strongly (W, n)-separating if W|n ⊆ L(A) ⊆ W".
  - Thm 9: equality of the least sizes of strongly separating deterministic safety automata, strongly good for
    (W,n)-games safety automata, strongly separating safety automata, and (W,n)-universal graphs. Every item is STRONG.
  - Footnote 5 (p.14), verbatim: "Note that there is a natural, more symetric, notion of (W, n)-separating automata in
    which the requested inclusions are W|n ⊆ L(A) ⊆ ((W^∁)|n)^∁. However, nothing is known about this notion."
    The symmetric notion is exactly weak separation (accept W|n, reject (W^∁)|n).
  - Note: a deterministic weak separator is "good for (Parity, n)-games" in the sense of Def. 8 (by CDFJLP Prop. 3.2),
    and nothing in the paper bounds non-strong good-for-small-games automata from below.
- **Czerwiński et al. 1807.10546 §6** (T4): "We leave open the question whether ... every safety automaton separating
  EvenCycles_n from OddCycles_n has at least quasi-polynomial number of states."
- **Kozachinskiy-Vyalyi 1902.07175** (T4): only time-bounded weak separators, over the (vertex, priority) alphabet;
  p.5 "no better lower bound that just n is known", p.6 "Even super-linear lower bounds for unrestricted separation
  automata are not known".
- **Parys, CSL 2020** (LIPIcs.CSL.2020.32), Def. 3.2: a "PG separator" accepts PosEven_{n,d} and rejects PosOdd_{n,d}
  (weak, over edge triples); "strong PG separator" additionally rejects LimsupOdd. Intro p.2: "Czerwiński et al. [9] show
  a quasi-polynomial lower bound for the size of a PG separator". This is NOT a weak-separator theorem. The same intro
  paragraph describes the separator as one that "rejects all words encoding plays in which the player loses", i.e. strong,
  and Def. 3.2 itself notes the QPT separators "are actually strong PG separators". Read literally against Def. 3.2 the
  sentence over-states CDFJLP. A referee may raise it, so S2 should cite it and explain it.
- **Göös, Kiefer, Yuan, arXiv 2109.09155 v2** (ICALP 2022; cites CDFJLP): lower bounds for unambiguous finite automata
  (complement, union, separation of NFA-recognisable pairs). Mentions parity separating automata only in passing (l.85-86);
  nothing on parity weak separators.
- **Citers of 1807.10546** (Semantic Scholar, 51 records, T4) and **of 1902.07175** (none listed): no weak-separator result.
  arXiv author sweep Ohlmann (2023-2026: positionality, memory, mean-payoff recursion) and arXiv search
  "history-deterministic" + parity + "lower bound" (2310.13498, 2501.12302: complexity of HD checking, 2-token theorem):
  none concern separator size.
- Indirect routes checked: history-deterministic / good-for-games automata. GFG ⇒ strongly good for small games (CF19
  Example 1), so GFG lower bounds bound strong objects only; no route found from HD/GFG results to weak separators.

## 2. Question (2): would T1 be new and count as M3 under D1?
a) New: yes, by §1. T1 resolves the deterministic case of CDFJLP §6 and of CF19 footnote 5, up to one tree level.
   T2 also would be new: both T1 and T2 give super-linear (indeed quasi-polynomial for d = ω(log n)) bounds where none is known.
b) M3 under D1 (quoted by the Lead: "a lower bound for a broader algorithm model ... Each must be new against the literature
   map"): Lead reading needed, but L-LIT sees no obstacle. Deterministic weak separators strictly contain deterministic strong
   ones (every strong separator is weak), and by CDFJLP Prop. 3.2 each one yields an algorithm ("solve G ⊲ A"). So T1 is a
   lower bound for a strictly broader algorithm model than B1. It is new against docs/lit/BARRIERS.md (B1, B2, B16)
   and the landscape doc.
c) Wording correction for S2 §1: "give the first super-linear bound for unrestricted (not time-bounded) weak separators
   (KV p.6 ...)" over-claims. KV's sentence is about automata over (vertex, priority) letters; T1 is over priority-only
   letters (conventions E/S/V). An automaton over priorities can be run on (vertex, priority) words by ignoring vertex names,
   so a lower bound for the vertex-name alphabet would imply one for priorities, NOT conversely. Suggested wording: "the
   first super-linear lower bound for unrestricted deterministic weak separators over the priority alphabet; the
   vertex-alphabet question of KV p.6 stays open."
d) Scope for barrier use (gauntlet step 3): T1 covers algorithms that solve G ⊲ A for a deterministic automaton reading
   only priorities. It does NOT cover automata that read vertex names or edges (Parys's SFPG model), nor non-deterministic
   weak separators. With vertex names, non-deterministic weak separation is easy (KV p.5: "just guess a node appearing more
   then once").

## 3. Question (3): any known reason T1 should be false?
None found. Specifically:
- No construction of a weak separator smaller than the strong minimum appears in any source opened; CF19 says "nothing is
  known" about the notion.
- Known small weak separators: (i) KV p.5, non-deterministic, guessing a repeated vertex name; not in T1's model (T1 is
  deterministic, priority-only), but it shows a proof of T1 must use determinism or the absence of vertex names.
  (ii) KV p.6: "a simple O(n)-state deterministic automaton, separating EvenCycles_{n,2} from OddCycles_{n,2} in O(n^2)-time
  (namely, accept if and only if at least n + 1 priorities which are equal to 2 have been already seen)". This one reads
  priorities only. It is d = 2, outside T1 (d >= 4), and O(n) matches the strong size there, so it is no counterexample.
- Boundary sanity: at d = 4, T1 reads w(n,4) >= s(n,2) = n (an (n,1)-universal tree has n leaves), which matches the "just n"
  level KV report as the best known. So T1 is informative only from d = 6 on.
- L-STRUCT's own table (unrefereed except cell C1) shows no violation (S2 §3); the decisive open cells are (4,6) E and n = 5.

## 4. Limits of this search
Not opened: Fijalkow, "The theory of universal graphs for games: past and future" (CMCS 2020, LNCS 12094; hal-03232352,
bot challenge on dl.ifip.org and hal.science); Ohlmann's PhD thesis (not located on arXiv); Bojańczyk-Czerwiński "An
automata toolbox" (2018). OpenAlex daily budget was exhausted, so OpenAlex citers of 1902.07175 were not listed.
Semantic Scholar's citation index may miss recent or non-indexed work. The novelty verdict is "not found in the sources
above", not a proof of absence.

## DONE / FINDINGS / NEEDS
- FINDINGS: verdict NEW; CF19 footnote 5 is a second primary source stating weak separation is open; S2 §1 KV sentence over-claims
  (alphabet), corrected wording above; Parys CSL 2020 intro sentence could be misread as a weak bound, so S2 should explain it.
- NEEDS: Lead: rule (b) formally (M3 under D1); L-STRUCT: adopt §2c wording; REFEREE: none new from L-LIT.
