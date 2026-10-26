# P-N5-VILB fixes (box 44 packet): the referees' notes, written out
L-NEW successor 24 (Opus 5.5, D14/D18, L40). Written 2026-10-26 05:40Z by date -u, at the Lead's GO of 05:39Z (Lead's stamp), step 2 (a):
"repairs only, frozen". FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-VILB-box44.md, sha1 872d4400194ed9d0f6ad9f6a2cc82f2f0821cd9f (l-new 999e73f4; re-measured on my tree).
  The packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-VILB.md (referee dcb1451c, successor 12): §1 and Lemma VI-LB SIGNED, no gap; notes VILB-N1, VILB-N2.
    §C (referee 09b5dbf5; 906247c6 touches R-N5-2T only): no disagreement, no gap.
  - REFEREE-2: docs/referee-2/R2-N5-VILB.md (referee-2 f0e82d8a, successor 13): all SIGN, no gap; notes N-VILB-1, N-VILB-2.
    §C (referee-2 5ad79417, successor 14): identical verdicts; nothing open.
- Signed scope: §1 ((Aκ), (M1κ), (M2κ), κ-FB-ROUND) and §2 Lemma VI-LB, every game. The §2 relation to R48's κ-HAT-FREEZE (a) is an
  agreed READING (not signed); §3, §4 not signed. VI-LB is a LOWER bound on progress: no count, no running time. Not a TARGET.md claim;
  G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| VILB-N1 (REFEREE) = N-VILB-1 (REFEREE-2); identical per both §Cs | §0, definition of Val^{≤j}_c; the clause "(max / min over an empty set: −∞ / +∞; −∞ + a = −∞)" | The empty-set conventions never fire for z ∈ U_c ∖ {c}: by (Aκ), next_t(z) ∈ succ(z) ∩ U_c, so succ(z) ∩ U_c ≠ ∅ and +∞ never enters Val^{≤j}_c. Only −∞ (from Val^{≤0} off c) occurs, and it is absorbing under +. The recursion and the gloss "the best payoff Even can force from z while reaching c within j steps" agree: Val^{≤j}_c is the backward induction of the j-step truncation of Γ_c (not reaching c within j steps pays −∞). Optional wording. |
| N-VILB-2 (REFEREE-2); REFEREE §2 has the same step, "identical in substance" per REFEREE-2 §C | §2 proof, Odd step | The Odd step uses only (Aκ) at t and the induction hypothesis at t (t > g_j > g_{j−1}): κ_t(z) = κwt_c(z) + κ_t(σ̄_t z) with σ̄_t(z) ∈ succ(z) ∩ U_c, hence κ_t(z) ≥ κwt_c(z) + min over succ(z) ∩ U_c of Val^{≤j−1}_c. It needs no fallback at z and holds for forced and choice Odd vertices alike, so VI-LB treats EVERY Odd vertex as a minimiser: the two-player strengthening of R48's κ-HAT-FREEZE (a). No class hypothesis. |
| VILB-N2 (REFEREE; REFEREE-2 §3 reaches the same conclusion by another control) | §3; packet data | DATA, not proof: VI-LB is exercised and often TIGHT at round j. REFEREE: tight at 61,861 of 105,188 finite lib41 checks (59%), up to 33 in-phase fallbacks in a phase; the mutation oddmax (Odd maximises in Val) gives 46,067 failures; the j + 1 bound fails at 1,216 lib41 states. REFEREE-2: the control "κ_t ≥ Val^{≤j+1}" fails 774 times on lib41 (S3), max 37 in-phase fallbacks in a phase. Both: 0 violations (REFEREE 777,048 checks, REFEREE-2 2,677,247); the regime of §4 (exponentially many fallbacks in one phase) is not reached. |

## 2. Status lines
- Both referees: no NOT SIGNED item, no gap. Nothing in this file changes a signed statement; the packet's §1 and §2 stand as written.
