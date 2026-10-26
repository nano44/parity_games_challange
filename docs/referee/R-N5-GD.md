# R-N5-GD: REFEREE report on packet P-N5-GD (L-NEW box 43: set-form Lemma G_D (a), (b), (c1), (c2), F1°_D, Wo_D on every game)
Referee: REFEREE (successor 11, session_01VH2ckvgGP9CGkb8Suno5f1), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 02:21Z (Lead's stamp).
- Object: docs/new/P-N5-GD-box43.md at trunk 3c6f6c16, sha1 b898ff8256bf444ef90d69eb3154f5fe16dddf10 (checked with
  `git show 3c6f6c16:docs/new/P-N5-GD-box43.md | sha1sum`; identical on my tree), 149 lines. Author: L-NEW successor 23 (from successor 22's
  working doc).
- Written 2026-10-26T02:25Z-02:29Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/R2-N5-GD* file read. No lane code run (f1d.py not run). D1.
- Premise texts read (not recalled): RESULTS R15 (a), R17 (a)-(c), R18 (c), (d) with their sources docs/new/N5-1Oacyc-box24.md (flat case)
  and docs/new/N5-time-box21.md §2.2 (Lemma S), R19 (a), (b) (P-N5-RE §1-§2 as quoted in the packet's port table), R21 (a), (c) with P-N5-X-box28
  §1-§3, R22 (a) (P-N5-NH-box30 §1), R25 (C2), (C4).
- Tool: scratch/gd_probe.py (own engine; dual_probe.run5 for start pairs; games with any number of Odd choice vertices). Logs scratch/gd_logs/.

## Verdicts
| statement | hypotheses | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| Lemma G_D (a) | none | SIGNED |
| Lemma G_D (b) | (h_D) at k | SIGNED |
| Lemma G_D (c1) | (h_D), (h3_D) at k | SIGNED |
| Lemma G_D (c2) | (h_D), (h3_D) at k | SIGNED |
| Lemma F1°_D | none (D-crossing-free interval of a phase) | SIGNED (note GD-N2) |
| Lemma Wo_D | (h_D) at k and k+1, τ_{k+1} = τ_k, u ∈ D_k ∩ D_{k+1} | SIGNED |
| premise class (READING in §0: the 𝒞^1O-setting premises are game-general) | — | CONFIRMED for every premise used (§1), with note GD-N1 |
| §2 port table | — | checked, correct |
| §3 (Δ1, Δ-RT, R20 coarse port), §4 data | not to sign | not signed |
No gap. Notes GD-N1 (citation direction of Lemma S (c)), GD-N2 (F1°_D step 4 wording), GD-N3 (data: Wo_D's (h_D) not shown necessary).
Nothing here bounds N5's running time; G-N5-TIME stays OPEN; not a TARGET.md claim.

## 1. The premises signed under a 𝒞^1O setting line (the Lead's first item)
Each was read in its source proof for a step that uses "one Odd choice vertex" (FO) or "σ̄ = τ off o" (HP):
| premise | where signed | proof read | one-Odd step? |
| --- | --- | --- | --- |
| R15 (a) Ξ_{k+1} ⊵ Ξ_k | R15 (N5 on every game; VJ00 Lemma 5.7) | statement + R15 (d) | none: VJ00 Lemma 5.7 is for any non-empty improving switch set of any game; R15 (d) is every N5 iteration. |
| R17 (a) (V1), (V2), (F1); (b), (c) Lemma P, Theorem PH | R17 "N5 on one-player games" | statements | none: one-player statements. Applied to G_τ, its arenas and 𝓕 = G_τ[F_D], which are one-player on every game (Odd fixed to τ). |
| R18 (c), flat case | R18 (o-acyclic 𝒞^1O) | N5-1Oacyc-box24 l. 62-85 | none: the case analysis B1 / B2 is about a strategy ρ of a one-player game at an arena optimum (★); "every improving edge of ρ is flat" and "flat switches change no valuation" use only the one-player game. |
| R18 (d) Lemma S (c) | R18 | N5-time-box21 §2.2 | none: "σ_{k+1} maximises V_{·,τ_k} pointwise over A(σ_k) (R17 (F1), on the one-player arena)". GD-N1 below. |
| R21 (a) XW | R21 (𝒞^1O) | P-N5-X §1 | none: "σ̄_k is a pointwise-optimal counter-strategy for Odd there: VJ00 §5.2, Prop. 5.1, Lemma 5.2, eq. (11); this is R17 (F1) on the dual game" (as in R-N5-1O §5; REFEREE-2 N-1O-4). |
| R21 (c) FBL-N (i) | R21 | P-N5-X §3 (i) via §2 | none: "Even's, since τ is fixed and τ_{k+1} = τ_k (S4c switches Odd only if Iσ_k = ∅, and then τ changes)"; "S4a returned σ_k, so σ_k is a pointwise arena optimum (R18 (d))". |
| R21 (c) FBL-N (ii) | R21 | P-N5-X §3 (ii) | YES in the landed form: "x's (σ_k, τ)-play avoids o, so σ_k(x) ∈ F_k". The packet does NOT cite (ii) as a premise; it re-proves it in set form inside F1°_D step 4 (closure of F_D, G_D (a)). Correct. |
| R22 (a) F1° | R22 | P-N5-NH-box30 §1 | YES in the landed form (step 1 "F contains no vertex with an Odd choice (o ∉ F)"). The packet re-proves it as F1°_D (§3 below), not citing it. Correct. |
- GD-N1 (citation direction): the packet's §0 renders R18 (d) Lemma S (c) as "S4a returns σ_k IFF σ_k is a pointwise optimum of its arena".
  The landed text gives one direction: σ_{k+1} is a pointwise optimum, so S4a returning σ_k makes σ_k one. The converse (a pointwise optimum
  is what S4a returns) depends on S1's tie-breaks and is not landed. F1°_D step 4 uses only the landed direction. Fixes line: "⇒" for "iff".

## 2. G_D (a), (b), (c1), (c2): SIGNED
- (a): along v's (σ_k, τ_k)-play no vertex is in D_k, so σ̄_k = τ_k at its Odd vertices (definition of D_k); the honest play equals the
  W-play step by step. Correct, every game.
- (b): the Odd vertices of π_v are outside D_k (u(v) is the first D_k vertex), so both plays follow π_v to u. If u's honest (W-) play met
  x ∈ π_v after leaving u, it would follow x's honest (W-) play, which is the same path back to u (HP_D on π_v), against (h_D). So the
  continuation avoids π_v, π_v's vertices are not on the cycle, and (V1) iterates. Correct.
- (c1): (h3_D) gives one cycle node c for Ξ(u), W(u); A_v ∩ P(T) = ∅ by (b); the order of π_y ⊕ T vs π_z ⊕ T depends on c, on A_y Δ A_z
  (the top and its parity) and on |π_y| − |π_z| (sign and c's parity), not on T. Correct.
- (c2): v ∈ F_D by (a); v ∈ R_D: lev(Ξ(u), W(u)) ≤ M_D ≤ L gives equal COARSE_L at u ((C2)); (C4) along π_v (each ⊕ is a (V1) step by (b))
  carries equality to v. L = ⊥ with M_D = ⊥ is equality at every terminal. Correct. The Remark (different terminals: NOT claimed, Δ-RT
  OPEN) is accurate.

## 3. F1°_D: SIGNED, note GD-N2 (the Lead's second item: the port of R22 (a))
Step by step against P-N5-NH-box30 §1:
1. R22 step 1 used FO ("o ∉ F", so F has no Odd choice). Here 𝓕 := G_τ[F_D] fixes every Odd vertex to τ, so it is one-player on every
   game; F_D is closed under σ_k and τ (a successor along x's play has the tail of x's play, which avoids D_k), so every vertex of 𝓕 has a
   successor. Ξ_k = W_k on F_D by G_D (a), and these are 𝓕's valuations (plays from F_D stay in F_D). Correct.
2. Gate edges inside F_D = 𝓕-improving edges (step 1 at both ends). Correct.
3. S4a steps: F_D is constant on I and closed under σ_{k+1}, so σ_{k+1}|F_D uses arena edges into F_D; every strategy ρ of 𝓕's arena,
   extended by σ_{k+1} off F_D, is in S4a's arena in G_τ, with plays from F_D inside F_D; (F1) in G_τ makes σ_{k+1}|F_D a pointwise optimum
   of 𝓕's arena. Correct: this is R17's step on 𝓕.
4. S4c steps: FBL-N (i) (game-general, §1) gives Even's fallback at an arena optimum; the set-form (ii) is re-proved: σ_k(x) ∈ F_D by
   closure, Ξ = W at σ_k(x) by G_D (a), XW at z, so the gate edge is W-improving at the optimum and flat (R18 (c) flat case). Correct.
   - GD-N2 (wording): "Since k+1 ∈ I, z ∈ F_D" should read "x's switched successor x* ∈ F_D (x ∈ F_D at k+1, F_D closed under σ_{k+1})"; the
     argument needs x*, the target S4c actually takes, not an arbitrary gate target z. The conclusion (switched F_D vertices are own cycle
     nodes, flat switches into their own regions, no value change; R18 (c)'s "different switched vertices do not interact") stands.
5. λ on F_D is λ_Ξ = λ_W, constant in the phase. Correct.
6. R17 Lemma P and Theorem PH on 𝓕 bound the value-changing steps by max(0, |F_D| − 1). Correct.
- The port table's "Crossing := a change of (D_k, R_D)" is the right interval notion: inside I, D_k and R_D (hence F_D) are fixed, which is
  all steps 1-6 use.

## 4. Wo_D: SIGNED
- (h_D) at j ∈ {k, k+1}: u is not its own W-cycle node and b := τ(u) ∈ F_D at j (b's play is the tail of u's, which avoids D_j after u).
  G_D (a): W_j(b) = Ξ_j(b), and b's honest play avoids u. (V1): W_j(u) = u ⊕ Ξ_j(b). R15 (a): Ξ_{k+1}(b) ⊵ Ξ_k(b). (V2) with u on neither
  play. Correct. No phase hypothesis and no (h3_D) used; only τ(u) unchanged.
- GD-N3 (DATA): in my random games Wo_D's conclusion also held at all 66 transitions where (h_D) failed at k or k+1; the data do not show
  (h_D) necessary. The proof needs it (b ∈ F_D, u not its own cycle node). Not a gap.

## 5. Data (DATA, not proof; scratch/gd_probe.py; logs scratch/gd_logs/)
| corpus | runs | checks (GA / GB / GC1 / GC2 / F1D intervals / WOD) | failures |
| --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt, n ≤ 64: 367 games, any class), S3 + 2 random start pairs | 1,101 | 444,276 / 83,348 / 726,207 / 1,984,737 / 10,941 (6,536 transitions) / 7,090 | 0 |
| 500 random games with 2-4 Odd choice vertices, n 5-14, S3 + 2 random starts | 1,500 | 31,138 / 1,101 / 558 / 37,476 / 4,110 / 36 | 0 |
- States with D_k ≠ ∅: 12,225 (lib41) and 2,364 (random); with (h_D): 13,339 / 2,580; with (h_D) ∧ (h3_D) and D ≠ ∅: 7,491 / 398.
- GC2 is checked at every L from max(M_D, −1) to n − 1 (and as full equality when M_D = ⊥), not only at one L.
- Mutation controls (gd_logs/mutations.txt, 600 random games × 2 starts): GC2 at L = M_D − 1 fails at all 85 states with M_D ≥ 0 (the
  threshold is sharp: the terminal itself differs at level M_D); Wo_D without (h_D): 0 of 66 fire (GD-N3).
- Thin: Wo_D on random games (36 checks); F1°_D intervals are short on random games (216 transitions).

## 6. Notes for the fixes file
- GD-N1: §0, Lemma S (c): "S4a returns σ_k ⇒ σ_k is a pointwise arena optimum" (landed direction; the only one used).
- GD-N2: F1°_D step 4: "x's switched successor x* lies in F_D" for "z ∈ F_D".
- GD-N3: DATA only.
- Premise class (§0 READING): confirmed for every premise the packet uses; the two landed lemmas with a genuine one-Odd step (R21 (c) (ii),
  R22 (a) step 1) are re-proved in set form, not cited.
