# R2-N5-S4B: REFEREE-2 report on P-N5-S4B (L-SI box 63): Lemma S4B-OPT, Corollary S4B-KEEP
Referee: REFEREE-2 successor 25 (session_01V5yGRaPp26T6iMUpCRmXsW), Opus 5.5 (D15). Written 2026-11-01 02:53Z (date -u).
Independence: written without opening docs/referee/ for this packet.

## 0. Object
- docs/si/P-N5-S4B-box63.md at claude/l-si 68fa36619: sha1 f1b65da522d927406a403ae5d023bb48ac73d022, 81 lines. Re-hashed: match.
- Line: docs/si/P-N5-S4B-line.txt, sha1 f8559b5e539a461a0fac89a5a9bf6f4432721c74. Re-hashed: match.
- Opened:
  - SPEC docs/new/N5-ssi-global.md S1 (the procedure, (i)-(vi)), S2, S4 a-d, FIX 3.
  - RESULTS R57 (1E-N3).
  - docs/referee-2/R2-N5-1E.md §2 and note N-1E-1.
  - Lead reading L42 (docs/DECISIONS.md).

## 1. Claims table
| § | claim | verdict |
| --- | --- | --- |
| §2 | Lemma S4B-OPT (τ_new,k is a pointwise Odd optimum of H′_k against σ_k; τ_(k+1) = τ_new,k unless Odd fallback) | **SIGNED** |
| §3 | Corollary S4B-KEEP (at a τ-stretch transition with I_τ_k ≠ ∅, τ_k = τ_new,k) | **SIGNED** |

No gap. The premise is 1E-N3 alone, read as in §2 below.

## 2. The Lead's two checks
- **(a) Does SPEC S4b run exactly S1's procedure on H′?** Yes.
  - SPEC S4b: «τ_new = Odd's optimal counterstrategy (S1 procedure on H′, not dual) to σ».
  - SPEC S1 defines σ̄ by the procedure on «graph Gσ = Even vertices keep only σ(v), Odd vertices keep all edges». On the input H′ (Even
    already keeps only σ_k(v), Odd keeps A(v)), Gσ is H′ itself.
  - S1's ingredients are all determined by H′ and G's priorities on the same vertex set: ranks (Ω, v), reward order, alive / dead
    bookkeeping, list orders.
  - So τ_new,k is S1's σ̄ for σ_k on H′.
  - My tool builds H′ from the SPEC S4b text and recomputes τ_new with my engine's S1 procedure on H′. It equals the run's τ_(k+1) at
    every non-Odd-fallback state of the corpus (NEXT 0 violations, 7,736 states).
- **(b) Does N-1E-1 say what the packet needs?** Yes in substance, with one precision (P-1).
  - N-1E-1 (R2-N5-1E.md l. 56-61) says two things:
    - (VJ)'s mathematics, VJ00 §4.3 plus (11), holds in «VJ00's setting (§2) … every finite game graph with a successor at each vertex =
      TARGET §1's games; no class hypothesis»;
    - «What remains SPEC's requirement … that S1's PROCEDURE outputs an optimal σ̄ (VJ00 §6)».
  - The second item, 1E-N3, is a requirement on the procedure for its input graph. VJ00 §6's algorithm is stated in that same setting, so
    it covers any finite game graph with a successor at each vertex.
  - H′_k is such a graph (packet §2 (i): σ_k(v) at Even v, τ_k(v) ∈ A(v) at Odd v, G's priorities).
  - This is the same premise the fleet already applies to S4a, where S1 runs on dual(H_k) (L42: «covers S1's procedure and S4a»). S4b
    runs it on H′_k with no dual at all, so it needs no more than S4a does.
  - P-1 (precision, optional): N-1E-1 was written about G. The step «the procedure's requirement is likewise scoped to every finite game
    graph, including arenas H′_k» is the reading confirmed here, not a sentence of N-1E-1.
    - The line's «scope as signed by REFEREE-2, docs/referee-2/R2-N5-1E.md §2, note N-1E-1» would be exact if it added «and confirmed
      for arena inputs in docs/referee-2/R2-N5-S4B.md §2».
    - The packet's quotation keeps both halves of N-1E-1 and is accurate.
- So lifting L42's S4b restriction by a Lead reading is consistent with my signature. The premise used is 1E-N3 applied to H′_k, exactly
  as it is applied to S4a's dual arena.

## 3. Review notes
- §2 (i): H′_k is a finite game graph with a successor at every vertex, and σ_k is its only Even strategy. ✓
- §2 (ii) is 1E-N3 with G* := H′_k, σ* := σ_k. ✓
- §2 (iii): a play of H′_k is a play of G, with the same vertices, the same priorities and the same rank order, so SPEC S1 gives the same
  value. ✓
- §2 (iv): by S4d, τ_(k+1) = τ_new,k unless S4c fires (σ_new = σ_k and τ_new,k = τ_k).
  - If Iσ_k ≠ ∅, FIX 3 gives τ_(k+1) = τ_k = τ_new,k.
  - Otherwise it is an Odd fallback. ✓
- §3: an Odd fallback moves every Odd v with an improving edge to some w with (v, w) ∈ I_τ_k, hence w ≠ τ_k(v) (SPEC S2).
  - Since I_τ_k ≠ ∅, τ changes, so it is not a τ-stretch transition.
  - Hence τ_k = τ_(k+1) = τ_new,k. ✓
- Remark (no dual) is correct. Not to sign.

## 4. Re-runs with my own code
- Tool docs/referee-2/R2-N5-S4B/s4b_check.py.
  - It runs on my N5 loop with validated starts. H′ is built from the SPEC text, and τ_new comes from my S1 procedure on H′.
  - Brute force over every positional Odd strategy of H′ when there are ≤ CAP = 1,024 (OPTV). Also NEXT, KEEP, and the MUT=1 control.
  - The lane's anc58/s4bopt.py is not imported.
- Corpus: the packet's experiments/si/anc58/corpus_fixed.lst at l-si 68fa36619 (1,132 games; 94 with start files run on those starts, 1,038
  on the default start).
  - Logs: logs/cf_st.txt, cfns_00..02.txt; totals in logs/corpus_totals.txt. RESULT PASS, 0 violations, in all four.

| quantity | packet §4 | mine |
| --- | --- | --- |
| states with I_τ ≠ ∅ | 7,772 | 7,772 |
| enumerated (CAP 1,024) / not enumerated | 6,719 / 1,053 | 6,719 / 1,053 |
| strategies compared | 290,345 | 290,345 |
| OPTV | 0 | 0 |
| τ_(k+1) = τ_new / Odd fallbacks | 7,736 / 36 | 7,736 (NEXT 0 violations) / 36 |
| KEEP checks (τ-stretch transitions with I_τ ≠ ∅) | — | 3,768, 0 violations |

- Pins (logs/pins.txt): lcount2_n23 with its start, and sym_h8_s1 with anc58/inst/sym_h8_s1_default.start. 0 violations.
- Mutation (MUT=1, τ_k for τ_new; logs/pins_mut_each.txt): lcount2_n23 has 33 violating (state, ρ) pairs and sym_h8_s1 has 160.
  - So the control bites on both.
  - My unit is (state, ρ) pairs; the lane counts (state, ρ, vertex) triples, 215 / 677, so the numbers are not comparable.
- As the packet says, all of this is DATA about code. The procedure's conformance to SPEC stays R15 G-N5T-1.

## 5. Line diff against TARGET.md's scope words
- «N5 on EVERY game», with no class hypothesis and no count bounded. The tail reads «a premise result under 1E-N3 only, lane-authored …;
  it bounds no count; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim». This is consistent with TARGET §2 and §4.
- The DATA clause states the exact enumerated scope (6,719 of 7,772; 1,053 not enumerated) and is marked «not part of the claim»;
  reproduced exactly. No DEAD (L43). No referee-originated proof (L41).
- Binder pass:
  - k, ρ, x bound. σ_k, τ_k, I_τ_k, Iσ_k, H′_k, τ_new,k, val, ⊴, Odd fallback and τ-stretch transition are defined.
  - G* and σ* are bound inside the 1E-N3 gloss. No free symbol.
- Verdict on the line: **MATCHES** (Opus 5.5, D15). The optional P-1 wording is in §2 (b).

## DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-S4B/s4b_check.py; logs/ (corpus, pins, mutation).
- FINDINGS:
  - Lemma S4B-OPT and Corollary S4B-KEEP are SIGNED (Opus 5.5, D15), with no gap. The line MATCHES.
  - SPEC S4b runs exactly S1's procedure on H′, which is its Gσ.
  - N-1E-1 supports the premise as used: VJ00's setting is every finite game graph, and S1's procedure correctness stays SPEC's
    requirement on its input graph. H′_k is such a graph, as is S4a's dual arena.
  - The packet's DATA is reproduced exactly.
- NEEDS: Lead:
  - the L42 lift by reading, which is consistent with this signature;
  - optionally, the P-1 wording in the line.
