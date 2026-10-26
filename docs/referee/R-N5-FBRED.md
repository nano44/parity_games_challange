# R-N5-FBRED: REFEREE report on packet P-N5-FBRED (L-NEW box 44: FB-POLY's κ lemmas in set form on every game; Theorem FB-RED; Lemma TV)
Referee: REFEREE (successor 11, session_01VH2ckvgGP9CGkb8Suno5f1), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 03:13Z (Lead's stamp).
- Object: docs/new/P-N5-FBRED-box44.md at trunk c3f6f2bf, sha1 11b15455f70d439c93a48d7e82fcdc14ef73854d (checked with
  `git show c3f6f2bf:docs/new/P-N5-FBRED-box44.md | sha1sum`; identical on my tree), 178 lines. Author: L-NEW successor 23.
- Written 2026-10-26T03:05Z-03:07Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file read for this packet. No lane code run (fbf.py, fbclimb.py not run). D1.
- Compared against: docs/new/P-N5-FBPOLY-box41.md (= RESULTS R48, "FBP"), which my predecessor signed (R-N5-FBPOLY) and whose proofs I
  re-read for R-N5-START (§1); RESULTS R48 (i), R38 (a), (f), R18 (d) Lemma S (a) with N5-time-box21 §2.2, R17 (a), R15 (a).
- Tool: scratch/fbred_probe.py (own engine; any number of Odd choice vertices). Logs scratch/fbred_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1.1 | (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class; κ-FB-ROUND_D | SIGNED |
| §1.2 | κ-HAT-FREEZE_D (a)-(c) | SIGNED |
| §1.2 | κ-PFZ_D (per q) | SIGNED |
| §1.2 | κ-Y-FORM_D (per q, repaired Y^q) | SIGNED (uses Lemma S (a) on every game: §1 below) |
| §2 | EXIT-SWITCH_D | SIGNED |
| §2 | FREEZE-EXIT_D (conservative indices) | SIGNED |
| §2 | CN-ONLY_D | SIGNED |
| §3.1 | Theorem FB-RED: f ≤ 1 + (n − 1)(2 + ρ) | SIGNED AS A REDUCTION (polynomial in n only given ρ; ρ is unbounded here) |
| §3.2 | FB-RED, late form: f ≤ 1 + (n − 1) + (n − 1)·N_late, N_late ≤ 1 + ρ_late | SIGNED AS A REDUCTION |
| §3.3 | Lemma TV | SIGNED |
| §4-§6 | step table (READING), THETA-AFTER / ρ-POLY (OPEN), data | not signed; §4 checked against my own diff (§2 below) |
No gap. Notes FBRED-N1 (convention: "the i-th fallback of its run" counts by SOURCE state), FBRED-N2 (vacuity: the late regime and TV
are never reached in any data, mine included). Not a running-time bound: ρ (Ξ-changes at Odd choice vertices per phase) is OPEN
(CONJECTURE ρ-POLY). On 𝒞^1O FB-POLY (R48) stays the unconditional form. G-N5-TIME stays OPEN; not a TARGET.md claim.

## 1. Lemma S (a) on every game (the READING the packet flags)
- Landed text, RESULTS R18 (d): "(a) L_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ … (VJ00 (11) on G and on G^d)". Its
  source, docs/new/N5-time-box21.md §2.2 (a): "L_σ(v) = min over τ′ of V_{σ,τ′}(v) … The first is VJ00 (11) (σ̄ is a best counter-strategy,
  pointwise; R17 (F1))."
- The proof is VJ00 (11) on G_σ (Even fixed to σ, Odd moving: a one-player game for Odd on EVERY game), equivalently R17 (a) (F1) on the dual
  one-player game. R17 (F1) is stated for every one-player game. No step uses one Odd choice vertex.
- VERDICT: Lemma S (a) holds on every game, with L_σ = Ξ_σ (SPEC S1's definition of Ξ_σ as the value against S1's optimal counterstrategy
  σ̄). This is the same point as REFEREE-2's N-1O-4 and my R-N5-1O §5 (R21 (a)'s parenthetical), and it covers L-SI's OUT-G premise in the
  same way. The packet's use in κ-Y-FORM_D ("≤": Ξ_t(q) ⊴ V_{σ_t, τ′}(q) for the strategy τ′ = σ̄_t[q ↦ y]) is exactly this statement.

## 2. The port, step by step against FB-POLY (R48): every use of the 𝒞^1O hypothesis and its replacement
| FBP step | 𝒞^1O use | set-form replacement | checked |
| --- | --- | --- | --- |
| terminals T = {o, c_θ}, class U = λ⁻¹(c_θ), Û = U ∖ {o} | one Odd choice vertex o, which lies in the class of c_θ | T := C ∪ Q per class (C = honest cycle nodes of the phase, Q = Odd choice vertices); every class U_c handled; on 𝒞^1O, T ∩ U_{c_θ} = {o, c_θ} and the other classes contain no Odd choice vertex (so FB-POLY's restriction to U loses nothing) | ✓ λ is constant on a phase, so C, the classes and T are static on the phase. |
| (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) | none | per class with c for c_θ; (SP′) stops at the first T ∩ U_c vertex | ✓ (V1), R15 (a), S1's order, lasso shape. |
| κ-FB-ROUND | none | verbatim per class | ✓ S4c's best-key rule; x* ∈ U_c by (Aκ) at k+1 (λ constant). |
| κ-HAT-FREEZE (a): G_Û drops o; "z Odd ⇒ forced" | FO (Odd vertices ≠ o forced) | G_c := U_c ∖ (Q ∖ {c}) with c a sink: Odd vertices of G_c other than c are not in Q, hence forced | ✓ base j = 0 at z = c; Even step via κ-FB-ROUND at g_j; (M2κ). |
| κ-HAT-FREEZE (b): "z ∈ F ⇒ honest play avoids o" | (HP) | hypothesis "z's honest play avoids Q ∖ {c}" (then its prefix to c is a path of G_c) | ✓ (b), (c) are stated for exactly those z. |
| κ-HAT-FREEZE (c) at g_{|U|−2} | Û has |U| − 1 vertices | conservative g_{|U_c|−1} (G_c has ≤ |U_c| vertices) | ✓ |
| κ-PFZ: G_U^o, θ-runs | o the only Odd choice | G_c^q := U_c ∖ (T ∖ {q}), q a sink; Q_c-runs (Ξ(q′) constant for all q′ ∈ Q ∩ U_c); z ∈ U_c ∖ T | ✓ Odd vertices of G_c^q ∖ {q} are forced; κ_t(q) constant on a Q_c-run; base trivial (the step at x = q is κ_t(q) ≥ κ_t(q)). |
| κ-Y-FORM: Y_t = succ(o) ∩ U ∩ F_t; "every other Odd vertex is forced" makes y's (σ, τ′)-play its honest play | FO, H1 | Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play avoids q}; τ′ := σ̄_t except τ′(q) := y, so y's (σ_t, τ′)-play IS its honest play (they differ only at q, which it avoids); at states where q is on no honest cycle | ✓ "≥": σ̄_t(q) ∈ Y^q_t; "≤": Lemma S (a) on every game (§1), both values with cycle node c, (M1κ), no double count (y's play avoids q). |
| EXIT-SWITCH: "Odd w ≠ o forced, so next_{k+1}(w) = next_k(w)" | FO | non-terminal Odd vertices are not in Q, so have out-degree 1; non-terminal Even vertices not switched keep σ | ✓ Odd vertices of Q can change σ̄ between k and k+1, but they are terminals, and the argument stops at the first T vertex. |
| FREEZE-EXIT: indices |U| − 1 | two terminals; p_u avoids one | conservative |U_c| for both the phase index j and the run index i | ✓ (the FBP sharpening is not needed). |
| CN-ONLY (1): switched y ∉ U is a cycle node via (HP) + FBL-N (ii) | (HP), FBL-N (ii) (one-Odd) | S = ∅ means every switched vertex is in T; switched vertices are Even, so in C | ✓ No W-frame fact needed at all (the packet's set form is simpler than FBP's). |
| CN-ONLY (2), case "meets o first": uses (YB) at ¬H1 | o, H1 | "meets some q ∈ Q ∩ U_y first": q and π lie on y's k+1 honest cycle with top y, so wt_y = 0 on π and P(Ξ_{k+1}(q)) = ∅; (Aκ) along π, (M2κ) at q, the gate and (A0κ) | ✓ |
| THETA-AFTER | Y ⊆ F ∩ U frozen by HAT-FREEZE (c) since Y's plays avoid the only terminal o | NOT ported (fails as proved: y ∈ Y^q may route through another q′ ∈ Q whose value moves) | — the packet replaces it by the count ρ: hence a reduction. |
| Theorem FB-POLY | THETA-AFTER | Theorem FB-RED with ρ; late form with ρ_late | ✓ (§4) |
The packet's own §4 table agrees with this diff row by row.

## 3. Lemma-by-lemma notes
- κ-PFZ_D, FREEZE-EXIT_D, FB-RED, TV use "the i-th fallback of its Q_c-run (Q-run)". FBRED-N1 (convention): as in FBP, a fallback k → k+1 is
  indexed in the run that contains its SOURCE state k. With this reading κ-PFZ's step ("k + 1 ≤ t and Θ is a run of consecutive states, so
  k + 1 ∈ Θ") holds because t ∈ Θ, t > k; a fallback at a run boundary (changing some Ξ(q)) is the last-indexed fallback of the run it leaves,
  and FREEZE-EXIT_D applies to it (its proof uses only the fallbacks of the run before k). FB-RED's third bullet counts each fallback once,
  in the Q-run of its source; ≤ 1 + ρ Q-runs. Correct; worth one line in the fixes file.
- CN-ONLY_D (2): the case split is exhaustive: the first T ∩ U_y vertex of the k-play from x*_y is y or some q ∈ Q (T ∩ U_y contains one cycle
  node, y).
- FB-RED (§3.1): fallbacks with S = ∅ ≤ 1 (CN-ONLY_D); S ≠ ∅ and j ≤ n − 1: ≤ n − 1; S ≠ ∅, j ≥ n: a class with S_c ≠ ∅, j ≥ n ≥ |U_c|, so by
  FREEZE-EXIT_D (contrapositive) its index in its Q_c-run is ≤ |U_c| − 1 ≤ n − 1, hence its index in its Q-run (a sub-run) is ≤ n − 1; ≤ 1 + ρ
  Q-runs (ρ counts (transition, q) pairs, at least the run-separating transitions). Arithmetic: 1 + (n − 1) + (n − 1)(1 + ρ). Correct.
- Late form: Q-runs holding a fallback g_j (j ≥ n) are separated by Ξ(q)-changes at transitions after g_n > g_{n−1}, so N_late ≤ 1 + ρ_late.
  Correct.
- TV: "≥" from κ-HAT-FREEZE (a) at t > g_{|U_c|−1} and κ-PFZ on the Q_c-run containing Θ (Θ's fallbacks are among that run's, so
  f^{Θ_c}_{|U_c|−1} ≤ f^Θ_{|U_c|−1} < t); "≤" from z's honest play to its first T ∩ U_c vertex. Correct.
- Reduction, stated plainly (the Lead's last item): Theorem FB-RED bounds f per phase by a polynomial in n and ρ. ρ is not bounded here; the
  packet says so and labels ρ-POLY a CONJECTURE (§5). I sign FB-RED as that implication. On 𝒞^1O, ρ = Θ (θ-changes), which R27 (g) TH bounds
  given X; R48's unconditional bound remains the 𝒞^1O form.

## 4. Data (DATA, not proof; scratch/fbred_probe.py; logs scratch/fbred_logs/)
| corpus | runs | phases | in-phase fallbacks (max per phase) | checks: FBR / YF / EXS / CNO | failures |
| --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64: 367 games, any class), S3 + 2 random start pairs | 1,101 | 5,393 | 1,049 (33) | 110,021 / 41,580 / 989 / 60 | 0 |
| box-43 + box-44 instances (10 games, incl. fb17_n32, sw21_n40, rtdis_k4_n24), S3 + 4 random starts | 50 | 281 | 64 (17) | 4,968 / 1,754 / 64 / 0 | 0 |
| 400 random games, 1-4 Odd choice vertices, n 5-12, S3 + 2 random starts | 1,200 | 3,049 | 29 (1) | 290 / 4,939 / 0 / 29 | 0 |
- FB-RED and its late form were checked on every phase (0 violations); max ρ per phase 51 (lib41).
- My engine reproduces the packet's frontier maximum of 17 in-phase fallbacks in one phase (fb17_n32.pg).
- Late fallbacks (index ≥ n): 0 in every corpus, so the FEX and TV counters stayed at 0 (FBRED-N2).
- FBRED-N2 (vacuity, honest): no phase in my data has n or more in-phase fallbacks (max 17 at n 32, fb17_n32.pg; the packet says the same),
  so FREEZE-EXIT_D's hypothesis, the late form's N_late and Lemma TV's hypothesis are never met: they rest on their proofs, checked above.
  κ-FB-ROUND_D, κ-Y-FORM_D, EXIT-SWITCH_D and CN-ONLY_D are exercised.

## 5. Notes for the fixes file
- FBRED-N1: "the i-th fallback of its Q_c-run / Q-run" counts the fallback k → k+1 in the run containing k (FBP's convention).
- FBRED-N2: DATA (vacuity of the late regime).
- §1: Lemma S (a) is game-general (proof VJ00 (11) / R17 (F1) on the one-player G_σ); a landing note may record it against R18 (d).
