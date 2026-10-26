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

## §C. Comparison with REFEREE-2 (REFEREE successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN; written 2026-10-26T03:40Z-03:41Z by date -u; (Opus 5.5, D15))
- Routing: the Lead's GO of 03:41Z (Lead's stamp), item (a).
- Objects: this report (1feff548, by successor 11; §1-§5 above unchanged) and REFEREE-2's docs/referee-2/R2-N5-FBRED.md at
  origin/claude/referee-2 814ac456 (successor 13; not yet on trunk when I read it). Packet sha1 11b15455f70d439c93a48d7e82fcdc14ef73854d
  re-measured (`sha1sum docs/new/P-N5-FBRED-box44.md`, = pin c3f6f2bf). Both reports were written independently (each says so; 1feff548
  at 03:07Z, 814ac456 at 03:08Z). I read R2's report after this report was pushed.

### C.1 What I checked myself, and what I only accept from successor 11
I did not write §1-§5. Before comparing I read the packet (all 178 lines), FBP (docs/new/P-N5-FBPOLY-box41.md) §0.3-§4, and RESULTS R18 (d).
- Re-checked by me against FBP's text, line by line: the port of (Aκ) (no double count with c for c_θ) and (SP′); κ-FB-ROUND (FBP §1; S4c's rule
  and λ constant on the phase are class-free); κ-HAT-FREEZE (a) (Odd vertices of G_c other than c are not in Q, so forced); κ-PFZ (FBP's range
  z ∈ U ∖ {c_θ} contains o, so its base case j = 0 is z = o; see N-FBRED-1); κ-Y-FORM "≥" and "≤" (τ′ = σ̄_t[q ↦ y]); EXIT-SWITCH (the one
  changed sentence: non-terminal Odd vertices have out-degree 1; σ̄ changes only at vertices of Q ⊆ T); FREEZE-EXIT_D (both cases, conservative
  indices); CN-ONLY_D (1) and (2), both cases (first T-vertex y; first T-vertex q ∈ Q ∩ U_y: π on y's k+1 cycle with top y, wt_y = 0 on π,
  M_{k+1}(q) = 0, (M2κ), gate, (A0κ)), and (3) = FBP §4 (3) verbatim; Theorem FB-RED's count (some S_c ≠ ∅ since every non-terminal v has
  λ(v) ∈ C; index in the Q-run ≤ index in the Q_c-run ≤ |U_c| − 1; ≤ 1 + ρ Q-runs); the late form; Lemma TV. I agree with every verdict.
- Accepted from successor 11's reading without re-deriving: κ-HAT-FREEZE (b), (c) beyond checking that (b)'s hypothesis replaces (HP); the
  claim that the packet's §4 step table matches FBP row by row for the rows I did not list above ((YB), (HP)). Lemma S (a) on every game:
  I checked the landed text (RESULTS R18 (d): "(VJ00 (11) on G and on G^d)"; box 21 §2.2 (a): "VJ00 (11) ... R17 (F1)"), which has no class
  step; I did not open VJ00 (BRICS RS-00-48) itself, and accept the citation as both referees and the landed R18 read it.
- FBRED-N1 (indexing by source state): checked; κ-PFZ's step "k + 1 ≤ t, Θ consecutive, so k + 1 ∈ Θ" needs exactly this convention.

### C.2 Verdicts side by side
| § | statement | REFEREE (1feff548) | REFEREE-2 (814ac456) | joint |
| --- | --- | --- | --- | --- |
| §1.1 | (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′); κ-FB-ROUND_D | SIGNED | SIGN | signed |
| §1.2 | κ-HAT-FREEZE_D (a)-(c) | SIGNED | SIGN | signed |
| §1.2 | κ-PFZ_D | SIGNED (base at x = q seen in §2 table, not flagged) | SIGN, N-FBRED-1 | signed; wording N-FBRED-1 |
| §1.2 | κ-Y-FORM_D | SIGNED (Lemma S (a) game-general, §1) | SIGN, N-FBRED-2, N-FBRED-3 | signed; wording N-FBRED-2 |
| §2 | EXIT-SWITCH_D | SIGNED | SIGN | signed |
| §2 | FREEZE-EXIT_D | SIGNED | SIGN | signed |
| §2 | CN-ONLY_D | SIGNED | SIGN | signed |
| §3.1 | Theorem FB-RED | SIGNED AS A REDUCTION | SIGN (as a reduction in ρ), N-FBRED-4 | signed as a reduction in ρ |
| §3.2 | late form | SIGNED AS A REDUCTION | SIGN, N-FBRED-4 | signed as a reduction in ρ_late |
| §3.3 | Lemma TV | SIGNED | SIGN | signed |
| §4-§6 | step table, THETA-AFTER / ρ-POLY, data | not signed; §4 agrees with own diff | not signed; §4 agrees with own diff | not signed; THETA-AFTER fails as proved (both); ρ-POLY CONJECTURE |
No disagreement. Neither report has a gap; neither has a NOT SIGNED statement. Both: not a TARGET.md claim; G-N5-TIME stays OPEN.

### C.3 Joint gap / note map
| REFEREE | REFEREE-2 | relation | joint status |
| --- | --- | --- | --- |
| — | N-FBRED-1 (κ-PFZ_D range: the induction passes through z = q, outside "z ∈ U_c ∖ T") | ACCEPTED. Confirmed: FBP's κ-PFZ ranges over z ∈ U ∖ {c_θ} (contains o) with base z = o; the packet's range drops q, so its j = 0 case is empty and the step at x = q uses an unstated (trivial) instance. Our §2 table wrote "base trivial (the step at x = q is κ_t(q) ≥ κ_t(q))" but did not flag it: a miss of wording, not of substance. | fixes file: state κ-PFZ_D for z ∈ (U_c ∖ T) ∪ {q} |
| — | N-FBRED-2 (Y^q_t defined only in §4, a not-to-sign table) | ACCEPTED; MISSED by us. Confirmed with `grep -n "Y\^q"`: the only definition is packet l.131 (§4 table); §1.2 (l.62-63) uses Y^q_t undefined. Our §2 table quoted the §4 definition without flagging it. | fixes file: move the definition into §1.2 or §0 |
| §1 (Lemma S (a) on every game) | N-FBRED-3 | SAME (both CONFIRMED; consistent with N-1O-4, N-GD-2, R-N5-1O §5) | landing note against R18 (d) |
| FBRED-N1 (a fallback is indexed in the run of its SOURCE state) | — (R2 uses the same convention implicitly: §2 "k ∈ Θ_c and k > f^{Θ_c}_{|U_c|−1}"; §3 "k's index in its Q_c-run") | ADDITIONAL note from us; R2's text reads the same way, so no conflict | fixes file: one line |
| FBRED-N2 (vacuity: late regime, FEX, TV never reached) | N-FBRED-4 (same; plus 4 climbs aimed at it, best f − n = −4) | SAME. R2 went further with climbs; neither reached j ≥ n. | DATA note: FB-RED's third bullet, late form and TV rest on their proofs only |

### C.4 Data
| item | REFEREE (§4 + this §C) | REFEREE-2 §5 | agree? |
| --- | --- | --- | --- |
| lib41, S3 + 2 random starts | 1,101 runs (367 games, n ≤ 64), 5,393 phases, max f 33, max ρ 51, 0 failures; + this §C: the 45 games with n > 64 (n 67-492), 135 runs, 1,834 phases, max f 1, max ρ 218 (tcL_N10, n 350, my random start 1), 0 failures | 1,236 runs (412 games), 7,193 phases, max f 33 (ccl_w48_n48), max ρ 194 (tcL_N8#2), 0 violations | YES. Max f 33 on the same game. The ρ difference was the n ≤ 64 skip in fbred_probe.main and different random starts; at R2's start pair for tcL_N8 #2 (replayed: random.Random(5151) over lib41 with R2's reader's successor order, scratch/fbred_r2start.py) my engine gives max ρ 194, max f 1, 0 failures: exact agreement. |
| box-43/44 instances | 50 runs, max f 17 (fb17_n32) | 50 runs, max f 17 (fb17_n32) | YES |
| random games | 1,200 runs, 1-4 Odd choice vertices, max f 1 | 20,000 runs 𝒞^kO, max f 1 | YES (shape) |
| extra | — | 503 𝒞^1O files × 2: max f 37 (dirty_a_best); exhaustive HAT / PFZ / TV for n ≤ 11; mutation controls (yf, cno bite; fex, red do not) | not re-run by me |
| late regime (j ≥ n) | never reached | never reached (max f − n = −2; climbs −4 at best) | YES (vacuous in both data sets) |
- Commands (my tools, scratch/, own engine): `RANDSTARTS=2 python3 -I fbred_big.py $(cat fbred_logs/big_files.txt)` →
  fbred_logs/lib41_big_rs2.txt; `python3 fbred_r2start.py experiments/red/tcpert/instances/tcL_N8.pg 2` → "max_f=1 max_rho=194 phases=26".
  Seeds: random starts seeded by the file path RELATIVE to the repo root (fbred_probe convention), so the runs reproduce from any worktree.

### C.5 Joint state (for the Lead and CHECKER)
- Every to-sign statement is signed by both referees; FB-RED and its late form as a REDUCTION in ρ (ρ unbounded; CONJECTURE ρ-POLY OPEN).
- No gap. Wording items for the fixes file: N-FBRED-1 (κ-PFZ_D range), N-FBRED-2 (define Y^q_t in §1.2), FBRED-N1 (source-state index).
- Landing note: Lemma S (a) is game-general (N-FBRED-3 = our §1).
- DATA: the regime where FB-RED's ρ term matters (a fallback g_j with j ≥ n) is reached by no sample or climb of either referee.
