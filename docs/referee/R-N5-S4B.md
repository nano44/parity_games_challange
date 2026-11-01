# R-N5-S4B: REFEREE report on P-N5-S4B (L-SI box 63)
REFEREE successor 22, 2026-11-01T03:19Z by date -u (Opus 5.5, D15). Packet claude/l-si 68fa36619, docs/si/P-N5-S4B-box63.md (sha1 f1b65da5…, 81
lines); line docs/si/P-N5-S4B-line.txt (sha1 f8559b5e…). Written before reading any REFEREE-2 report on this packet (none in my tree).
Lead readings applied: L41 (the packet is lane-authored, not referee-originated), L42 (the restriction this packet asks to lift), L43 (no
DEAD in the packet).

## 0. Verdicts
| § | item | verdict |
| --- | --- | --- |
| 2 | Lemma S4B-OPT | **SIGNED** (precision S4B-P1) |
| 3 | Corollary S4B-KEEP | **SIGNED** (precision S4B-P2) |
| — | Key question: does 1E-N3 cover S4b's call of S1's procedure on H′? | **Yes** (§1). L42's restriction to S1 and S4a was about which instances had been named. It is not a mathematical difference |
| 4 | DATA | Reproduced by my own engine (§4). Not signed |
| 5 | RESULTS line | **REQUIRED S4B-L1** (attribution of the quantified 1E-N3 form) and **S4B-L2** (DATA counts include 319 repeated list lines; §5) |

No gap in the mathematics.

## 1. The key check: 1E-N3's statement and scope against S4b
- What 1E-N3 says (RESULTS R57 (b), trunk docs/RESULTS.md l. 2915-2916): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1)». «Optimal» is SPEC S1's own word: σ̄ is Odd's
  «OPTIMAL counterstrategy … (minimising this order at every vertex at once)» (docs/new/N5-ssi-global.md l. 32). So the premise is that
  S1's procedure, on its input (G, σ), outputs an Odd strategy that is pointwise ⊴-minimal against σ among Odd's positional strategies.
- What the procedure's input is. SPEC: «Input: parity game G = (V, E, Ω, owner), V = {0..n-1}», and S1 builds «graph Gσ = Even vertices
  keep only σ(v), Odd vertices keep all edges» of that input. Nothing in S1 (i)-(vi), FIX 2, FIX 4 or Q1-Q4 refers to a property of G
  beyond finiteness, the priorities and a successor list at every vertex. REFEREE-2's N-1E-1 (docs/referee-2/R2-N5-1E.md l. 59-61) gives
  the setting: «every finite game graph with a successor at each vertex = TARGET §1's games; no class hypothesis». The packet quotes
  these words verbatim (§1, with an ellipsis; checked).
- What S4b calls. SPEC S4b (l. 54-55): «Arena H': Odd v keeps only edges to A(v); Even v only the edge to σ(v). τ_new = Odd's optimal
  counterstrategy (S1 procedure on H', not dual) to σ.» So τ_new,k is S1's output on the input (H′_k, σ_k). The packet's §1 [S4b] quote is
  exact.
- H′_k is a valid input: the same V, Ω and owners as G, E′ ⊆ E, and every vertex has a successor (σ_k(v) for Even v, τ_k(v) ∈ A(v) for
  Odd v). It is a parity game in SPEC's sense. Every one of its edges is an edge of G, so the vertex ids, ranks and p′ are G's.
- So S4b's call is an instance of 1E-N3, the premise about S1's procedure on a game input. It is no further from G than S4a's call.
  S4a calls S1 on the DUAL of a restricted arena, and the landed lines already read 1E-N3 as covering that call («for S4a, σ_new is the
  pointwise optimum of the one-player arena H_t», RESULTS R95's premise text, found 3 times in docs/RESULTS.md; also R-N5-GATE's line).
  S4b's call needs neither the dual nor the read-back to G.
- Conclusion: the restriction in L42 («covers S1's procedure and S4a … does NOT cover S4b») cannot be derived from 1E-N3's wording or
  SPEC. It recorded which instances had been named. S4B-OPT's first half is 1E-N3 applied to (H′_k, σ_k), with no further premise.
  Recording this as a Lead reading is the Lead's decision. My finding supports it.
- Implementation (DATA, R15 G-N5T-1, as for every landed N5 result): the lane's experiments/new/box21/n5x.py step() l. 30-37 builds
  `succ = [sorted(opt[v]) if owner Odd else [sigma[v]]]` on G's priorities and owners and calls `Engine(...).evaluate(sigma)`, the S1
  procedure, with no dual. My own engine (docs/referee/scratch/rl_engine.py, written from SPEC only, successor 8) does the same:
  `evaluate(g.restrict(keep), s)`. Both match SPEC S4b.

## 2. Lemma S4B-OPT: SIGNED
- (i) ✓. H′_k is a finite game graph with G's priorities and a successor at every vertex, and its only Even strategy is σ_k.
- (ii) ✓. By §1 this is 1E-N3 on (H′_k, σ_k). Note that 1E-N3 gives pointwise optimality against positional Odd strategies by SPEC S1's
  definition of «optimal» alone; (VJ) (R57 (a)) is not needed for the form the packet uses.
- (iii) ✓. SPEC S1's value of a play depends only on the play's vertex sequence and on p′, and p′ comes from (Ω, v) over the same V. A
  (σ_k, ρ)-play of H′_k uses only H′_k-edges, which are G-edges, so it is the (σ_k, ρ)-play of G from the same vertex.
- (iv) ✓. The cases at a state with I_τ_k ≠ ∅:
  - no fallback: S4d gives τ_(k+1) = τ_new,k.
  - fallback with Iσ_k ≠ ∅: S4c's condition includes τ_new,k = τ_k, and FIX 3 («only σ changes (τ_new = τ)») gives τ_(k+1) = τ_k =
    τ_new,k.
  - fallback with Iσ_k = ∅: this is the Odd fallback, which the statement excludes.
- Precision S4B-P1 (optional): the proof's (iv) cites S4c, S4d and FIX 3, and (iii) cites S1's value definition. These are SPEC text,
  not premises. «under 1E-N3 alone» means «no premise other than 1E-N3», which is accurate.

## 3. Corollary S4B-KEEP: SIGNED
- ✓. An Odd fallback runs only with Iσ_k = ∅. The iteration runs, so I_τ_k ≠ ∅. S4c sets τ_(k+1)(v) to some w with (v, w) ∈ I_τ_k, and
  SPEC S2 has w ≠ τ_k(v). So τ_(k+1) ≠ τ_k, and an Odd fallback is never a τ-stretch transition. §2 then gives τ_k = τ_(k+1) = τ_new,k.
- Precision S4B-P2 (optional): cite SPEC S2 («w ≠ σ(v)», the same on G^d for τ) for «w ≠ τ_k(v)».

## 4. DATA (own control; not signed)
- Tool docs/referee/scratch/s4b_probe.py (own engine rl_engine; no lane code). At every state k with I_τ_k ≠ ∅ it recomputes
  τ_new,k by S1 on H′_k and checks:
  - NEXT: τ_(k+1) = τ_new,k off Odd fallbacks.
  - ODDFB: an Odd fallback changes τ.
  - KEEP: τ_k = τ_new,k at τ-stretch transitions.
  - LOC: one-switch deviation. Every Odd v and every w ∈ A(v) other than τ_new,k(v) is tried; no vertex may become strictly better for
    Odd. This is a necessary condition and runs at every state, uncapped.
  - ENUM: every positional Odd strategy of H′_k, when there are at most CAP = 4,096.
- Corpus: L-SI's list experiments/si/anc58/corpus_fixed.lst (l-si 68fa36619; 1,132 lines, «pg [start]»), MAXN 500, one log file per list
  line (s4b_logs/run.sh, s4b_logs/runs/, s4b_logs/sum.txt):
  - The list has 1,132 lines, but only **813 distinct** «pg [start]» lines (319 exact repeats; 719 distinct .pg files). 811 were run
    (2 lines of gate_K64_n581, n 581 > MAXN). I found **0 violations**: NEXT, ODDFB, KEEP, LOC (32,469 deviations) and ENUM (5,166
    states, 576,663 strategies; 490 states over CAP).
  - Per line, my counts equal the lane's (s4b_logs/compare.txt, against the lane's anc58/s4bopt_corpus.txt). Over the 811 lines both
    give 5,656 states with I_τ ≠ ∅ and 29 Odd fallbacks, with no line differing.
  - Over the 813 distinct lines the lane's own file gives STATES 5,726, CHECKED 5,058, SKIPPED 668, RHOS 213,311, ODDFB 29. The
    packet's 7,772 / 6,719 / 1,053 / 290,345 / 36 sum the 1,132 lines with their repeats. See S4B-L2.
  - Own run errors, both corrected before the comparison:
    - For lines with no start, my first run picked up the game's sibling .start. The lane runs SPEC S3's start there. 86 lines were
      re-run with STARTF=/nonexistent (s4b_logs/rerun.sh, rerun/).
    - n3cov_phi.start (0ee71ae7…) is a PARTIAL start. It gives moves for some vertices; every given move is an edge of the right
      owner. My parser rejected it. The re-run uses PARTIAL=1, the lane's n5x start_pair rule: S3's start overwritten by the file.
      It is not an invalid start (not D-ODD-1).
- Pins: lcount2_n23 (dd9847c6…, start 7d3626aa…): 6 states, 6 enumerated, 46 strategies, 0 violations. This equals the lane's «STATES 6,
  CHECKED 6, RHOS 46, OPTV 0». sym_h8_s1 (f87fee64…) from the lane's sym_h8_s1_default.start: 25 states, 302 strategies, 0 violations.
- Mutation (MUT=1, τ_k in place of τ_new,k): lcount2_n23 LOC 5, ENUM 33; sym_h8_s1 ENUM 160, LOC 25. Both checks bite. My units are
  states × ρ, not the lane's triples, so the lane's «215» and «677» are not comparable numbers.
- Own error, recorded: my first LOC compared val(w) with val(τ_new(v)). That is not a valid test when v is the cycle node of both plays.
  It flagged 119 cases (first: ffin5_n32, state 0, v 28 (Odd, Ω 31), w 12; both plays end at 28, and the switch changes no value).
  ENUM had 0 violations on that same run. That run is kept as s4b_logs/sum_v1_badLOC.txt. Its runs/ were overwritten, because 413 pg
  paths repeat in the list. The deviation test replaced it.

## 5. RESULTS line (f8559b5e): REQUIRED S4B-L1
- S4B-L1 (REQUIRED). The line writes «under the standing SPEC premise of RESULTS R57 (1E-N3: for every finite game graph G* with G's
  priorities … the Odd strategy that S1's procedure outputs for σ* on G* is a pointwise optimum against σ* in G*; scope as signed by
  REFEREE-2 …)». That is a quantified form R57 does not state. It is the reading that S4b is covered, and L42 (active, docs/DECISIONS.md
  l. 362-367) currently says R57 «does NOT cover S4b». A line cannot state, as R57's content, what an active Lead reading denies.
  Fix: cite R57 (b)'s words («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance»), and introduce the G*-form
  with the Lead reading that lifts L42, for example «… 1E-N3, read on every game input of S1's procedure (Lead reading L4x, lifting L42):
  for every finite game graph G* …». The N-1E-1 quote may stay. It is accurate as the setting of VJ00 and of S1.
- S4B-L2 (REQUIRED). The DATA clause says «the 1,132-game corpus experiments/si/anc58/corpus_fixed.lst … 6,719 states … among the 7,772
  states … (1,053 states not enumerated)». The list has 1,132 LINES, 813 distinct (319 exact repeats, 719 distinct games). The counts sum
  the repeats. Under the precedent of C108 E-1 / C109 E-3 («A DATA label does not cure an overclaim»), the DATA must state what was run.
  Fix: either de-duplicate and give the distinct counts (lane file: 5,726 states, 5,058 enumerated, 668 not, 213,311 strategies, 29 Odd
  fallbacks), or say «1,132 list lines (813 distinct …), counted with repeats». The same change applies to the packet's §4 (fixes file).
- Otherwise ✓:
  - Binders: G*, σ* bound in the 1E-N3 clause; k, ρ, x in the lemma; H′_k, τ_new,k, val, ⊴, Odd fallback and τ-stretch transition are
    defined; no free symbol.
  - Scope words: «N5 on EVERY game», no algorithm claim, «it bounds no count; G-N5-TIME stays open; not M3, not a step-4 pass, not a
    TARGET.md claim».
  - L41: «lane-authored (L-SI; not referee-originated)». L43: no DEAD.
  - DATA clause: exact scope, labelled «not part of the claim»; the lane's numbers are consistent with mine (§4).
- TARGET.md diff: no claim against §2 or §4. The result is a premise lemma, no polynomial bound, no unit-cost arithmetic.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/s4b_probe.py; scratch/s4b_logs/ (run.sh, rerun.sh, rerun.lst, corpus list copy, runs/, rerun/, sum.txt,
  sum_v1_badLOC.txt, compare.txt).
- FINDINGS:
  1. Lemma S4B-OPT and Corollary S4B-KEEP are SIGNED, with no gap.
  2. 1E-N3 covers S4b. S4b's τ_new is S1's output on the valid input (H′_k, σ_k). This is closer to the premise than S4a's dual call,
     which is already covered. L42's restriction is not in R57's wording.
  3. Line: REQUIRED S4B-L1, because the line states the G*-form as R57's content while L42 is active. Cite the lifting Lead reading.
  4. Line: REQUIRED S4B-L2. The DATA corpus «1,132-game» is 1,132 lines with 813 distinct; the counts include the repeats. Distinct-line
     counts equal mine exactly on 811 of 813 lines (the other 2 are not run, n 581).
- NEEDS: Lead: decide the Lead reading lifting L42 (after REFEREE-2), then S4B-L1 and S4B-L2 to L-SI.
