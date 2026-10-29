# R2-N5-GP-C: REFEREE-2 §C (joint gap map) for packet P-N5-GP (l-si d072bb28, sha1 cd4866df…)
Written by REFEREE-2 successor 20, Opus 5.5 (D15, L37), 2026-10-29 from 18:08Z (date -u), on the Lead's word (17:17Z, 17:23Z, 17:35Z; read
at 18:07Z).

**Inputs.**
- REFEREE: docs/referee/R-N5-GP.md at referee 7dffab64 (REFEREE successor 18). First opened 18:08Z; my report was pushed at 17:08Z (4835eb3d)
  and completed at 1340def5.
- REFEREE-2: docs/referee-2/R2-N5-GP.md (1340def5).
- L-SI's fixes file docs/si/P-N5-GP-fixes-box31.md at l-si 2d0ada80, sha1 f901b509… (measured; equal to the Lead's figure), items G0-G12.
  The packet is unchanged: `git diff d072bb28 2d0ada80 -- docs/si/P-N5-GP-box31.md` is empty.
- I have not read REFEREE's §C (fee33b06). The Lead's summary of it is noted in C.2.

## C.1 Verdict map, row by row
| § | item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- | --- |
| §1 | setting, [FRZ], [H] | CHECKED | SIGNED | agreed |
| §2 | W-MON | SIGNED (premise GP-N1) | SIGNED (premise N-GP-2) | SIGNED by both |
| §2 | XW | SIGNED (premise GP-N1) | SIGNED (premise N-GP-2) | SIGNED by both |
| §3 | GP* | SIGNED; Case B redone without improvement, three new sub-cases | SIGNED; the same three new sub-cases, the same closures | SIGNED by both |
| §3a | GP | SIGNED | SIGNED | SIGNED by both |
| §3a | GP+ | SIGNED | SIGNED | SIGNED by both |
| §4 | FW-R* | SIGNED | SIGNED | SIGNED by both |
| — | 16:26Z RESULTS line | DOES NOT MATCH: drops L ≤ k − a and "path of G_τ" (GP-E1) | DOES NOT MATCH: drops L ≤ k − a; "cycle node" should be "W-cycle node" (N-GP-7) | E-item = union of GP-E1 and N-GP-7 |
| — | final line G12 | — | MATCHES §3-§4 (C.3) | the line to land |
| — | pinned checks | reproduced exactly | reproduced exactly | identical figures |

**Joint gap map for the packet: EMPTY.** No gap, nothing FALSE in the packet. The only E-item was on the RESULTS line, a paraphrase, and G12
discharges it.

## C.2 Where the reports differ
| # | point | raised by | REFEREE-2 assessment | class |
| --- | --- | --- | --- | --- |
| D1 | The 16:26Z line drops "path of G_τ (Odd steps follow τ)". Instance rand8: phase [2, 3], k = 3, x = 2, path [2, 4], 2 Odd, 4 ≠ τ(2) | REFEREE only | Correct, and I MISSED it. My §2.6 checked the line's GP* clause for the length bound and the cycle-node reading, not for the path family. Without "of G_τ", an Odd vertex may step to a successor W never follows, and the claim fails. Discharged by G0/G12 | E (discharged) |
| D2 | The 16:26Z line drops L ≤ k − a | both: REFEREE rand0 (k = 0, path [0, 1, 7]); REFEREE-2 b4_theta_n7, canonA_0, b5_os_n28 (one-edge paths at k = a) | Same defect, independent instances | E (discharged by G0/G12) |
| D3 | "cycle node" → "W-cycle node (λ_W(u) = u)" | REFEREE-2 only (N-GP-7 (b)) | GP*'s base case W_a(u) = (u, ∅, 0) needs λ_W(u) = u, and λ_Ξ ≠ λ_W when D ≠ ∅. G0 still said "a cycle node"; G12 fixes it | E (discharged by G12) |
| D4 | GP-N2: GP* uses only τ constant, no S4c transition, λ_W constant on [a, k]; σ̄ and λ_Ξ constant are unused | REFEREE (G2 READING) | True: §2.3 of my report used exactly those (W-MON for the transition, λ_W constancy for the "impossible" sub-cases). G2's "hold on every maximal run … with those three properties" WIDENS the statement. The Lead ruled it a READING outside the entry; I agree | opt (READING, outside the entry) |
| D5 | GP-N3: τ used as a transition index in §4 | REFEREE | Agreed (G3) | opt |
| D6 | GP-N4: data scope. REFEREE's DFS budget per (F, k). G4: core/gp.py keeps ONE best unblocked path per (vertex, length), so it is a Bellman-Ford, not an enumeration | REFEREE; same scope point in my report (NODECAP on dense games) | All three data sets cover a subset of the unblocked paths on large n. Each value compared is a real path's, so violations would be genuine. FW-R* counts are complete in all three | record |
| D7 | GP-N1 / N-GP-2: standing premises | both | Same content. G1 names [OPT-H] and [OPT-σ̄]; G7 adds the order reversal. Agreed | E-light (discharged by G1, G7) |
| D8 | GP-N5 / N-GP-3: B1′(i) covers both parities of c | both | Same finding | — |
| D9 | N-GP-1 (quote elision), N-GP-4 (cycle shape), N-GP-5 (§3a wording), N-GP-6 (R*_T) | REFEREE-2 only | Discharged by G6, G9, G10, G11 | opt (discharged) |
| D10 | Controls | both | REFEREE: MUT 1 (no L ≤ k − a) 27,724; MUT 2 (Odd off τ) 93; MUT 3 (blocked allowed) 756 on ccl_w48_n48. Mine: plain W-frame Lemma P fails 344,537 (lib41), 125,338 (alt_all), 10,196 (runfam_K100), 2 (ccl). Together they show all three path conditions are needed | — |
| D11 | Data scale | both | REFEREE: 6,326 runs, 466,193 GP* path checks. Mine: 14,117 runs (+170 without counters), 11.4M GP* paths checked, 0 violations. Both have max R*_T 1-3 outside alt_all (mine: alt_all 40 / WCH 49) and no WCH > n − 1 in random games. Both reach runfam_K100's WCH 123 (R*_T 1) | — |

## C.3 The final RESULTS line (G12) against §3-§4
Checked clause by clause against the packet's §3 definition of UNBLOCKED AT STATE k (l. 85-88), Lemma GP* (l. 89), [FRZ] (l. 64-68) and §4:
- "every frozen W-phase F = [a, b] … (N5-FRZ-box29 §0: no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ))" = [FRZ]. ✓
- "for every k ∈ [a, b], W_k(x) ⊵ value(r)" = GP*'s quantifier and conclusion, with x = r_0 and value(r) as [VAL]. ✓
- "every simple path r of G_τ (Odd steps follow τ)" = "simple" and "a path of G_τ (Odd r_i: r_{i+1} = τ(r_i))". ✓ (D1)
- "with at most k − a edges" = "L ≤ k − a". This keeps every state k − 1 − i in [a, k − 1] ⊆ [a, b), where BLOCKED is defined. ✓ (D2)
- "from x to a W-cycle node u of F's first state a (λ_W(u) = u)" = "u is a cycle node of state a (λ_W(u) = u)". ✓ (D3)
- "none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ)" =
  "for every i < L with r_i Even the edge … is not blocked at state k − 1 − i", with BLOCKED = "W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉ Iσ_t". ✓
  - Reading: "Even edges" = edges with an Even tail.
  - Reading: W, σ and Ξ in the parenthetical are taken at the state k − 1 − i just named.
  - Both readings are forced by the packet, as G12's table says.
- FW-R* clause and the tail = §4 with R*_T. ✓
- **Verdict: G12's line MATCHES §3-§4 exactly. It claims nothing beyond the signed GP* and FW-R*** (it omits W-MON, XW, GP and GP+, which is
  allowed).
- line_probe on the final line:
  - My three instances (one-edge paths at k = a) are EXCLUDED by "at most k − a edges", since only L = 0 is allowed at k = a.
  - The family the final line quantifies over is exactly the family my gp_check.py GPS check enumerates: G_τ paths, simple, L ≤ k − a,
    W-cycle-node ends, no blocked Even edge at k − 1 − i.
  - So the final line is checked directly on every corpus: 0 violations over 11.4M paths (R2-N5-GP §3.2), with the NODECAP truncations
    disclosed there.

## C.4 Check of L-SI's fixes G0-G12 (l-si 2d0ada80)
| item | answers | content check | clarification or widening? |
| --- | --- | --- | --- |
| G0 | GP-E1 | Corrected line with "of G_τ" and "at most k − a edges"; still "a cycle node" | CLARIFICATION of the line (superseded by G12) |
| G1 | GP-N1 | Names [OPT-H] (S4a's S1 output is an optimum of H_t, as R17 (e)) and [OPT-σ̄] (R57 (b), quoted). GP* uses [OPT-H] only. Correct: BLOCKED is defined through Iσ_t, whatever Ξ_t is | CLARIFICATION (premises named) |
| G2 | GP-N2 | GP* and FW-R* hold on every maximal in-phase run with τ constant, no S4c transition, λ_W constant (σ̄-changes allowed). True by the same proof | WIDENING (one-referee). The Lead ruled it a READING outside the entry; agreed (D4) |
| G3 | GP-N3 | τ → s as the transition index in §4 | CLARIFICATION (notation) |
| G4 | GP-N4 | core/gp.py is a path-tracking Bellman-Ford with one stored path per (vertex, length bound); §6's "0 violations" is read with that scope | CLARIFICATION (DATA scope) |
| G5 | GP-N5 | B1′(i) for both parities of c | CLARIFICATION |
| G6 | N-GP-1 | The elided parenthetical quoted in full; matches box10 l. 34-35 at 2a435f8f4 word for word (checked) | CLARIFICATION |
| G7 | N-GP-2 | Order reversal + SPEC conformance = [OPT-H]; XW's first part = R57 (a) = [OPT-σ̄]'s optimality half | CLARIFICATION |
| G8 | N-GP-3 | = G5 | CLARIFICATION |
| G9 | N-GP-4 | The cycle shape: since x ∉ π, π's cycle part does not contain x, so the arc c → x and π meet only at c. Correct | CLARIFICATION |
| G10 | N-GP-5 | "directly" = §3's induction run with ALLOWED(⁺) in place of "unblocked"; sign §3a's reduction to GP* | CLARIFICATION |
| G11 | N-GP-6 | R_T ≥ R*_T because every blocked edge is outside ALLOWED⁺ (§3a, contrapositive) | CLARIFICATION (an R_T line would be implied, but weaker) |
| G12 | N-GP-7 | The final line with "F = [a, b]", "k ∈ [a, b]" and "W-cycle node u … (λ_W(u) = u)"; word-by-word table against §3 | CLARIFICATION of the line. MATCHES (C.3) |

G0-G12 ACCEPTED. G2 is the only widening, and it stays a READING outside the entry, per the Lead.

## C.5 DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  - The packet's joint gap map is EMPTY, and W-MON, XW, GP*, GP, GP+ and FW-R* are SIGNED by both referees.
  - The RESULTS-line E-item (GP-E1 ∪ N-GP-7) is discharged: G12's line matches §3-§4 exactly.
  - REFEREE found the dropped "path of G_τ", which I missed (D1).
  - G2 widens and stays a READING. G0-G12 are accepted.
- NEEDS: none. Land P-N5-GP with G12's line.
