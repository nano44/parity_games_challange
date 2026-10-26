# R-N5-H3: REFEREE report on packet P-N5-H3 (L-SI box 16: G_D-NC (b′), TC-CLASS, C2-H3, WM-G, P^c_L / CR-D, Corollary FRZ-U_H3; every game)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's message of 05:44Z (Lead's stamp). P-N5-NC (sha1 2036e7c8) was withdrawn unreviewed; I did not review it.
- Object: docs/si/P-N5-H3-box16.md at trunk d096e404, sha1 680e45287aed82ea3d9ac05ed9decdf9c260e849 (checked with
  `git show d096e404:docs/si/P-N5-H3-box16.md | sha1sum`; identical on my tree), 237 lines, frozen at l-si 10b11167. Author: L-SI successor 11.
- Written 2026-10-26T05:45Z-05:51Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ H3 file on my tree; none opened. No lane code run (experiments/si/fb2o/gdnc.py, tcdir.py);
  lib2o.txt is used as an input list only. D1.
- Cited text checked by script (whitespace-normalised substring search): R55 (a), (b), (c1) and the R17 (F1) / R55 premise phrases occur verbatim
  in docs/RESULTS.md; lev and COARSE_L verbatim in docs/si/P-N5-FB-box7.md §1 (the R25 packet); the (C1)-(C4) quote and R55's proof of (b)
  (docs/new/P-N5-GD-box43.md l.54-59) are verbatim up to the packet joining the sources' bullet lines (checked by eye).
- Tool: scratch/h3_probe.py (own engine; any game; random start pairs; given .start files). Logs scratch/h3_logs/ (run_all.sh).

## Verdicts
| § | statement | hypothesis | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §2 | Lemma G_D-NC (b′) | (NC) at k | SIGNED |
| §3 | Lemma TC-CLASS | none | SIGNED |
| §4 | Lemma C2-H3: COARSE_L(Ξ_k) = COARSE_L(W_k) on V, M_D ≤ L < ∞, L ≥ −1 | (h3_D) at k | SIGNED |
| §5 | Lemma WM-G | none (in-phase S4a step) | SIGNED (H3-N1: the standing SPEC premise) |
| §5 | Lemma P^c_L and Lemma CR-D | (i), (ii) on a fallback-free run | SIGNED (H3-N2: one step made explicit) |
| §6 | Corollary FRZ-U_H3 | (h3_D) at every state of a fallback-free in-phase run; max_S M_D ≤ L < ∞ | SIGNED |
| §7, §8 | READING, DATA | — | not signed (as briefed) |
No gap. Notes H3-N1, H3-N2, H3-N3 (DATA). Structural lemmas only: no running-time bound. Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. G_D-NC (b′)
- R55's proof of (b) (P-N5-GD §1, quoted in the packet) uses (h_D) once: "If u's honest play (resp. W-play) met x after leaving u, it would
  then follow x's play back to u ∈ D_k, against (h_D) at u." x ∈ π_v: x's W-play is the suffix of π_v, then u; x's honest play is the same
  path, because the Odd vertices on it are outside D_k (σ̄ = τ there; HP_D) ✓. So if u's F-play met x, it would return to u: u on its own
  F-cycle (positional plays are lassos), which (NC) forbids in both frames ✓. Nothing else uses (h_D); (V1) along π_v gives both equations
  (π_v avoids the cycle) ✓. (h_D) ⇒ (NC) ✓.
- VERDICT: SIGNED.

## 2. TC-CLASS
- Both plays from v ∈ R_D follow π_v to u(v) (HP_D; Even vertices use σ_k in both), then are u(v)'s plays (positional), so v and u(v) end
  on the same cycle in each frame ✓. λ_Ξ constant on a phase gives the class statement ✓.
- VERDICT: SIGNED.

## 3. C2-H3
- v ∈ F_D: R55 (a) ✓. v ∈ R_D, u := u(v), c := λ_Ξ(u) = λ_W(u) ((h3_D)), which is v's cycle node in both frames (TC-CLASS) ✓.
- c ∈ π_v: both plays share the prefix up to c, so the path sets agree ✓ (coarse values ignore length).
- c ∉ π_v: each play is π_v then u's play; c is first met inside u's play; the prefix before c is π_v · Q_F with Q_F ∩ π_v = ∅ (the prefix
  of a lasso up to a cycle vertex repeats nothing) ✓; so P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) ✓ (P_F(u) is u's path set: vertices of u's play
  before its first visit of its cycle node c, ranked above c). lev(Ξ(u), W(u)) ≤ M_D ≤ L gives P_Ξ(u) ∩ V_{>L} = P_W(u) ∩ V_{>L} ((C2)), hence
  the coarse values of v agree ✓. v ∈ D (π_v empty) is the same computation ✓; D = ∅ gives L = −1 and only F_D ✓.
- No (h_D), no (NC): correct; the argument never looks past c.
- VERDICT: SIGNED.

## 4. WM-G, P^c_L, CR-D
- WM-G: σ_{k+1} is Even's pointwise optimum on the S4a arena H_k against τ (SPEC S4a); σ_k is a strategy of H_k; (F1) on the one-player
  H_k ✓. This is R23 (g) WM, whose proof I checked as game-general for P-N5-XEP (R-N5-XEP, XEP-N2). H3-N1: like every N5 result, it
  takes SPEC's requirement that S1's procedure returns the optimal counterstrategy (here: the arena optimum); my R-N5-1E 1E-N3.
- P^c_L, re-derived case by case:
  - base: by (ii) a W-cycle node u keeps Ω(u) = (u, ∅, 0) on S ✓.
  - A1 (x ≠ λ_W(x)): (V1) Ω_k(x) = x ⊕ Ω_k(a); x ∉ P(value(r′)) (r′ avoids x) and x ∉ P(Ω_k(a)) (if a's play passes x, x is on its own
    W-cycle below its top) ✓; (V2c) applied to COARSE(value(r′)) ⪯ Ω^c_k(z) ⪯ Ω^c_k(a), then (C4) and (MON) ✓. (V2c) itself: different cycle
    nodes are kept by x ⊕; equal ones get x added to both coarse sets or neither, which leaves the top of the symmetric difference ✓.
  - A2 (x = λ_W(x) ≠ u): the reward comparison; the case reward(x) < reward(u) contradicts the IH via a's cycle node x ✓.
  - B (x Even, Ω^c_k(z) ≻ Ω^c_k(a)): (i) and (Cstrict) make (x, z) a gate, so σ̂ = σ_k[x ↦ z] lies in H_k and (F1) gives Ω_{k+1}(x) ⊵ val_σ̂(x) ✓.
    B1, x not on c′'s cycle: val_σ̂(x) = x ⊕ Ω_k(z) and the chain (C1), (C4), IH, (V2c) ✓. B1, x on c′'s cycle: the coarse gap forces an even
    top t of P(π) above L ✓; x's σ̂-play closes the cycle x → z → π → c′ → (arc of c′'s cycle) → x. H3-N2: the packet does not say why this
    cycle is simple; it is: if π enters c′'s cycle at e before c′, the cycle segment e … c′ lies on π, the arc c′ … x is the rest of the
    cycle, and x ∉ π keeps them disjoint. Its top is t (every other vertex is ≤ c′), so the cycle node changes, against (ii) ✓. B2 (x ∈ π):
    Z := x, z, π[z..x); COARSE(Ω_k(z)) and COARSE(Ω_k(a)) differ exactly by D ∩ V_{>L} (P(z) = P(a) ⊔ D, disjoint as π is simple), so the top
    t of D is even and t = top(Z) > c′; the cycle node changes, against (ii) ✓.
- CR-D: x's W-play at t follows a simple G_τ-path of ≤ n − 1 edges to the W-cycle node λ_W(x) (constant by (ii)), so Ω_t(x) = value(r_t);
  P^c_L at j = n − 1, (MON), (C3) ✓.
- VERDICT: WM-G, P^c_L, CR-D SIGNED.

## 5. FRZ-U_H3
- (i) at every state: C2-H3 with L ≥ max_S M_D ≥ M_D(k) ✓ (M_D < ∞ under (h3_D)). (ii): λ_W = λ_Ξ on F_D (R55 (a)) and on R_D (TC-CLASS +
  (h3_D) at u(v) ∈ D_k), so λ_W = λ_Ξ on V, constant on the phase ✓. CR-D gives the freeze from k_0 + n − 1 ✓.
- Scope as stated (any number and configuration of disagreement vertices; ¬h-cyc and ¬h-route allowed) ✓: the proof uses (h3_D) only.
- VERDICT: SIGNED.

## 6. Data (DATA, not proof; scratch/h3_probe.py, own engine; logs scratch/h3_logs/)
Checks: BP ((b′) at (NC) states), TCC (TC-CLASS per vertex, and terminal changes inside a phase stay in one honest class), C2H3 (every v, at
every (h3_D) state, L = max(M_D, −1)), WMG (in-phase non-fallback transitions), FRZ (maximal fallback-free in-phase runs with (h3_D) at every
state, L = max(max_S M_D, −1): COARSE_L(W) constant from k_0 + n − 1; non-vacuous runs counted). Mutation H3_MUT=1: C2-H3 at L = M_D − 1.
| set | runs | states ((h3_D) / (h3_D) ∧ ¬(NC)) | BP | C2H3 | TCC (terminal changes) | WMG | FRZ runs (non-vacuous; max length) | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games), S3 + 4 random + 29 given .start pairs | 1,864 | 27,454 (20,519 / 338) | 122,925 | 718,471 | 237,961 (416) | 612,745 | 5,947 (4; 55) | 0 |
| lib2o.txt (lane list, input only; 43 𝒞^2O), S3 + 6 random (+ 1 given) | 302 | 2,046 (1,610 / 19) | 7,275 | 39,066 | 10,889 (23) | 28,610 | 665 (0; 23) | 0 |
| 5,000 random 𝒞^2O, n 5-12, seed 82, S3 + 2 random | 15,000 | 39,805 (28,025 / 2,971) | 10,710 | 245,436 | 76,490 (37) | 18,110 | 26,172 (0; 4) | 0 |
| 4,000 random 𝒞^kO, k 2-4, n 5-14, seed 83, S3 + 2 random | 12,000 | 34,238 (21,935 / 2,445) | 11,240 | 216,263 | 89,818 (52) | 15,837 | 20,553 (0; 3) | 0 |
| frz1_n24.pg (L-COMP's instance) S3 + 6 random + its .start | 8 | 179 (162 / 0) | 559 | 3,888 | 738 | 3,432 | 24 (2; 24) | 0 |
| MUTATION (C2-H3 at L = M_D − 1), lib41 n ≤ 64, S3 + 2 random + given | 1,130 | 17,800 | — | 263,140 | — | — | — | 76,353 C2H3 failures (control bites) |
- H3-N3 (DATA): C2-H3 is exercised at 5,773 (h3_D) states where (NC) fails (beyond the withdrawn P-N5-NC), 0 failures. The freeze of CR-D /
  FRZ-U_H3 is NON-vacuous on 6 runs (4 in lib41, not split by (NC); 2 on frz1_n24, where (NC) holds at every state), 0 failures; elsewhere fallback-free (h3_D) runs
  are shorter than n − 1. Terminal changes (588) always stay inside one honest class.
- Reproduce (from docs/referee/scratch): `sh h3_logs/run_all.sh` (fixed seeds; file starts seeded by the RELATIVE path; X.start files used
  when present).

## 7. Notes for the fixes file
- H3-N1: WM-G (and so CR-D) rests on SPEC's requirement that S4a's S1 run returns the arena optimum, as every N5 result does (1E-N3).
- H3-N2: P^c_L case B1 (x on c′'s cycle): one sentence that the σ̂-cycle is simple (π's part on c′'s cycle and the arc c′ → x are disjoint
  because x ∉ π).
- H3-N3: DATA.
