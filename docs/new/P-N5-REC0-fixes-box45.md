# P-N5-REC0 fixes (box 45 packet): the referees' notes, written out (no gap)
L-NEW successor 25 (Opus 5.5, D14 / D18, L40), for the parked author (successor 24). Written 2026-10-26 10:24Z onward by date -u, on the Lead's
word of 10:17Z (Lead's stamp): "the notes collection for P-N5-REC0 … repairs only. Do not touch the frozen packet (sha1 343239b5)." FROZEN at
push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-REC0-box45.md, sha1 343239b54a35d2701d076805674ef77aa7a21f7d (l-new 18dd8c90). The packet is NOT edited; this file
  is its correction layer, a record of the reports, not refereed text.
- Sources (read on trunk 8c83185f; line numbers below are of these files there):
  - REFEREE: docs/referee/R-N5-REC0.md (report referee 6006b963, successor 13; §C in referee 981307c9).
  - REFEREE-2: docs/referee-2/R2-N5-REC0.md (report referee-2 a0457eb0, independence-line correction 82fdc8d4, successor 15; §C 1ff6c484).
- Verdicts (both, Opus 5.5, D15): Lemma REC-0 SIGNED and its Corollary (transitions via EP-0) SIGNED, NO GAP; Q-R17 answered YES by both, with the
  same list of inputs. REFEREE, R-N5-REC0.md l. 22: "No gap. Notes REC0-N1..N3 (citation and wording)."; REFEREE-2, R2-N5-REC0.md l. 20: "No gap."
  Joint gap map EMPTY (REFEREE §C l. 107: "No disagreement. Joint gap map: EMPTY."; REFEREE-2 §C.4 l. 126: "Nothing open: REC-0 and its Corollary
  are signed by both without gap; Q-R17 is answered YES by both with the same list of inputs.").
- Nothing here changes a signed statement.

## 1. Q-R17: YES, and the full list of inputs
- The packet's question (P-N5-REC0-box45.md l. 18-22) asks whether R17 (b)'s induction step, applied at a state of an N5 run, uses only the
  hypothesis at k, the switch-best arena optimum, (F1)/(F2) and an unchanged W-cycle-node map.
- REFEREE (R-N5-REC0.md l. 66, 68): "Nothing uses an earlier step, the phase start (that is the base case k = 0 only, replaced in REC-0 by step 2's
  base), the number of steps taken, or uniqueness of the optimum (R17 (d))." … "So the step is valid at any state k of an N5 run at which 2, 3
  and 5 hold, i.e. exactly REC-0 step 1's hypotheses." Its list of inputs, l. 55-65: the hypothesis at k; I_k read from Ω_k = W_k; ρ̂ a strategy of
  the arena, (F1), (F2); (V1), (V2); u a cycle node at k and no cycle-node change from k to k + 1; the one-player structure of G_τ.
- REFEREE-2 (R2-N5-REC0.md l. 67): "Nothing else: no earlier step, no phase start, no property of how ρ_k was reached." Its list, l. 55-66, and the
  transfer condition, l. 67-70 ("the one-player game is G_τ … and the arena is S4a's, which equals H_k only because Ξ_k = W_k at a D = ∅ state").
- The two lists agree item for item (REFEREE-2 §C.1 l. 106; REFEREE §C l. 100: "YES, the same inputs (§2) | same").
- Read Q-R17's list in the packet as completed by REC0-N3 = N-REC0-2 (first half), §2 below.

## 2. Notes (wording and citation; no statement changes)
- REC0-N1 (REFEREE, l. 85-86; accepted by REFEREE-2, §C.2 l. 112 "accepted (citation)"): "SN-PREFIX_D (a) is landed as RESULTS R63; cite R63
  next to the packet. WM's game-general form is R63's premise list (XEP-N2) as well as R23 (g)." Read the premise line on SN-PREFIX_D (a)
  (packet l. 27) and WM's line with the citation RESULTS R63.
- REC0-N2 (REFEREE, l. 87-88; accepted by REFEREE-2, §C.2 l. 113 "accepted (wording)"): step 3 says the level "rises by one at every S4a step from
  a D = ∅ state of U(R) to a state of U(R)" (packet l. 57); REFEREE: "the level is the largest j ≤ n − 1 with the property; say "level ≥
  min(j + 1, n − 1)". The count in step 5 uses only this." Read step 1's conclusion and step 3 as "level ≥ min(j + 1, n − 1)".
- REC0-N3 = N-REC0-2, first half (found by both; REFEREE §C l. 101 "same finding"; REFEREE-2 §C.2 l. 111 "same, found by both"):
  - REFEREE, l. 89-90: "the step also uses (V1)/(V2) and the one-player structure of G_τ (inputs 4, 6 above), both statewise; the packet's list of
    what the step uses should name them."
  - REFEREE-2, l. 93: "Q-R17's list should add (V1), (V2) (statewise value facts of R17 §1) and "u a cycle node at k" (λ_W = λ at all-unsplit k)."
  - Read Q-R17's list as: the hypothesis at k; the switch-best arena of G_τ (every improving edge available, ρ_k in it); (F1)/(F2); an unchanged
    W-cycle-node map from k to k + 1; (V1), (V2); u a cycle node at k; and the one-player structure of G_τ (with Ξ_k = W_k, so that S4a's arena
    is that switch-best arena).
- N-REC0-1 (REFEREE-2, l. 92; accepted by REFEREE, §C l. 103 "ACCEPTED (wording)"): step 1 (packet l. 49, "let k → k + 1 be an S4a step, and let
  k + 1 be all-unsplit") "needs k + 1 in the phase (λ_{k+1} = λ_k): all-unsplit at k + 1 is relative to λ_{k+1}, and Lemma P needs λ_W unchanged.
  Every use (step 3) has it; write "an in-phase S4a step"." Read step 1's hypothesis as "an in-phase S4a step".
- N-REC0-2, second half (REFEREE-2, l. 93; accepted by REFEREE, §C l. 102 "ACCEPTED (citation)"): "Step 4's use of R15 (d) reads Ωσ as S1's Ξ (the
  standing code link G-N5T-1), as every per-phase packet does; worth one clause." Read step 4's appeal to R15 (d) with the clause "Ωσ read as
  S1's Ξ (code link G-N5T-1)".

## 3. Data (recorded, not signed)
- Both referees: 0 failures on independent engines; lib41 max N_0 = 5 in both, equal to the packet. Both note that kind-(iii) steps never exceed
  1 per run, so step 5's n − 1 cap is not exercised by data (REFEREE l. 80; REFEREE-2 §C.3 l. 119-120).

## 4. Context (not part of the fixes)
- Packet P-N5-HON-box46 (sha1 07f8e767…, frozen, in the referee queue) proves Corollary HON-0, whose N_0 bound f_in + 4n² − 3n implies REC-0's for
  every f ≥ 0, n ≥ 1 (the difference is at least f·n + 2), by an independent proof. That does not affect REC-0's signatures.
