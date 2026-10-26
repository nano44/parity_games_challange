# P-N5-FBRED fixes (box 44 packet): the referees' notes, written out
L-NEW successor 23 (Opus 5.5, D14/D18, L40), session_011WFfFqRNrU1a8LQwbwazZN. Written 2026-10-26 03:54Z by date -u, at the Lead's order of
03:54Z (Lead's stamp): "repairs only, and freeze it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-FBRED-box44.md, sha1 11b15455f70d439c93a48d7e82fcdc14ef73854d (l-new 3732ab55). The packet is NOT edited; this
  file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-FBRED.md (referee 1feff548, successor 11): all SIGNED, FB-RED and its late form SIGNED AS A REDUCTION in ρ;
    Lemma S (a) game-general; notes FBRED-N1, FBRED-N2. §C (referee 1ea0d317, successor 12): no disagreement, no gap; N-FBRED-1, N-FBRED-2
    accepted (N-FBRED-2 "MISSED by us").
  - REFEREE-2: docs/referee-2/R2-N5-FBRED.md (referee-2 814ac456, successor 13): all SIGN, no gap; N-FBRED-1..4. §C (referee-2 a4a642b6):
    identical; FBRED-N1 accepted; FBRED-N2 = N-FBRED-4; nothing open.
- Signed scope: Theorem FB-RED and its late form are a REDUCTION (fallbacks per phase given ρ, resp. ρ_late). CONJECTURE ρ-POLY stays a
  CONJECTURE (packet §5). Not a TARGET.md claim; G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| N-FBRED-1 (REFEREE-2; accepted by REFEREE §C) | §1.2 κ-PFZ_D, "z ∈ U_c ∖ T" | Read the range as z ∈ (U_c ∖ T) ∪ {q}. The induction's base case j = 0 is the one-vertex path p = (q), i.e. z = q, where the claim κ_t(q) ≥ κwt_c(∅) + κ_t(q) is trivial; with z ∈ U_c ∖ T alone the base case would be empty. (R48's κ-PFZ ranges over U ∖ {c_θ}, which contains o, with base z = o; same fix.) The uses in FREEZE-EXIT_D and Lemma TV apply it at z = u ∈ U_c ∖ T, unchanged. |
| N-FBRED-2 (REFEREE-2; accepted by REFEREE §C, which notes it was missed in REFEREE 11's report) | §1.2 κ-Y-FORM_D | Y^q_t is used in the signed text but defined only in §4's not-to-sign table (packet l. 131). Read, in §1.2 before κ-Y-FORM_D: "Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}." The proof in §1.2 already uses exactly this set (its "≥" puts σ̄_t(q) in Y^q_t; its "≤" uses that y's play avoids q). |
| FBRED-N1 (REFEREE; REFEREE-2 uses the same convention) | §0 (Q_c-run, Q-run), §1.2 κ-PFZ_D, §2 FREEZE-EXIT_D, §3 FB-RED, Lemma TV | "The i-th fallback of its Q_c-run (Q-run)" counts the fallback k → k+1 in the run containing its SOURCE state k (FBP's convention). κ-PFZ_D's step "k + 1 ≤ t, Θ consecutive, so k + 1 ∈ Θ" needs exactly this. |
| N-FBRED-3 = REFEREE §1 (both CONFIRMED) | Premises, "READING for the referees: Lemma S (a) …" | CONFIRMED by both referees: RESULTS R18 (d) Lemma S (a) holds on every game (VJ00 (11) / R17 (F1) on the one-player G_σ; consistent with N-1O-4, N-GD-2). Landing note against R18 (d). |
| N-FBRED-4 = FBRED-N2 (DATA) | §6 Data | Neither referee's data nor REFEREE-2's four climbs aimed at it reach the late regime: max (f − n) per phase = −2 in the library (REFEREE-2: lib41 × 3 starts, 503 𝒞^1O files × 2), and no fallback within 4 of FREEZE-EXIT_D's indices in the climbs (closeness −4). So FB-RED's third bullet, its late form and Lemma TV are vacuous in all data and rest on their proofs. (REFEREE 12 reproduced ρ = 194 at REFEREE-2's start pair, tcL_N8.) |
