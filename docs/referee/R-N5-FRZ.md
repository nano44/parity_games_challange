# R-N5-FRZ: REFEREE report on packet P-N5-FRZ (box 34: NL-MF, Fact 0, ARENA, P^c_ℓ, FREEZE, RATCHET, BLOCK, X-RUN, SUB)
Referee: REFEREE (successor 6), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-FRZ: the Lead's message of 2026-10-25 05:58Z
(Lead's stamp). Object docs/new/P-N5-FRZ-box34.md at pinned trunk 25fda0f, sha1 39df373c17d91f942ad2cb15244cd779ca7abda1 (checked:
`git show 25fda0f:docs/new/P-N5-FRZ-box34.md | sha1sum`, 287 lines). Author L-NEW successor 14. Written 2026-10-25 06:16Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/ not read for this packet.
Comparison text for §3: R20's Lemma P^c / CR in docs/new/P-N5-XA-box27.md §1, §2, §5, §6, with its fixes docs/new/P-N5-XA-fixes-box28.md §3
(XA-3, XA-4, N-XA-1), read side by side.

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Corollary NL-MF | PROVED (L-NEW succ. 14) | SIGNED (phase-key note: R29 NL transfers to the (λ_Ξ, τ) phase, §1) |
| §2 Fact 0 | PROVED | SIGNED |
| §2 Lemma ARENA | PROVED | SIGNED |
| §3 Steps 1-2 | PROVED | SIGNED |
| §3 Lemma P^c_ℓ | PROVED | SIGNED WITH GAPS FRZ-1 (case (γ) of B1 omitted, the inherited XA-3; conclusion unaffected) and FRZ-2 (B-fallback B1: "(V2)" for an own-cycle-node x; strictness comes from the cycle node there). Both are wording and closed |
| §3 Theorem FREEZE | PROVED | SIGNED |
| §4 Corollary RATCHET | PROVED | SIGNED |
| §5 Lemma BLOCK (+ Consequence) | PROVED | SIGNED |
| §6 Theorem X-RUN | PROVED | SIGNED WITH GAP FRZ-3 (REL_Q: the transition leaving the prefix P can carry exit leaves and is not counted among "both ends in P"; the stated bound survives by slack, but the proof must add it) |
| §7 Theorem SUB | PROVED | SIGNED |
| §8 FBF-on-subruns FALSE, CL1 FALSE, (L1), (L2), ¬H1 SN, f | not to sign | not signed. b6_xl2_n32 and x48_rt48_final re-run (n5.py, Oink OK) |

## 1. Corollary NL-MF (SIGNED)
- With L := MF_j, (A_j) holds by definition. r_j > MF_j forces MF_j < ∞ (r_j < ∞ under H3). NL (ii) gives the first claim and NL (iii) the
  second. Correct.
- Phase key: R29 NL is signed under (λ_Ξ, λ_U, τ). Its proof uses Lemma G and (C7) (statewise), WM (τ only; transfer checked in R-N5-SN §0),
  R25's (T) (iii) step (λ_Ξ constant), and TRANSFER (R15 only). Nothing uses λ_U, so it holds on the packet's (λ_Ξ, τ) phase.
- DATA: 1,978 (h) S4a steps with r > MF in the library, plus random. 0 leaves, 0 MF rises.

## 2. Fact 0 and Lemma ARENA (SIGNED)
- Fact 0:
  - on F_k, W = Ξ;
  - on R̄_k, both plays follow o's after o, giving λ = c_θ and W-cycle node c_w = c_θ (H3);
  - c_θ ∈ F_k under H1 (H3H2's proof).
  The corollary "an honest cycle node lies in F with W = Ξ = (u, ∅, 0)" is correct. DATA: 5,320 (library) + 8,476 (random) (h) states,
  0 failures.
- ARENA, by the frames of y and z:
  - R → R̄: same π, (C7).
  - F → F: Ξ = W.
  - R → F: XW makes the W-improving edge Ξ-improving.
  - F → R̄ withheld: (C5) then (C6), and the case Ξ(z) = Ξ(σ y) gives level ⊥.
  Correct.
- DATA: 41,479 W-improving non-arena edges at S4a steps from (h) states (library). Every one is F → R̄, not a gate, with
  lev(W σ y, W z) ≤ r: 0 failures.

## 3. Lemma P^c_ℓ and Theorem FREEZE (P^c_ℓ SIGNED WITH GAPS FRZ-1, FRZ-2; FREEZE SIGNED)
### 3.1 Steps 1-2 against R20 Lemma C
- R20 Lemma C used "P(θ) and P(w) agree on V*" with θ, w constant on the stretch. Step 1 gets the same statement at each state from
  lev(θ_k, w_k) = r_k ≤ ℓ with (C7) on routes, which is all R20's proof used. Correct.
- R20's monotonicity was R15 (a) through Lemma C at both ends. Step 2 is the same at a fallback. At an S4a step it uses WM on W, which is
  even more direct. Correct.
- DATA:
  - Step 1: 54,191 (library) + 48,714 (random) window states.
  - Step 2: coarse W non-decreasing at every consecutive pair of window states, fallbacks included.
  - 0 failures.
### 3.2 P^c_ℓ, line by line against R20 §5 (substitutions marked by the packet: COARSE_ℓ, Step 1 for Lemma C, Step 2 for monotonicity)
- Base: R20 used "Ω_{k0}(u) = (u, ∅, 0)", which held because W's cycle-node map was constant on S. Here Fact 0 at k0 gives it. ✓
- Case A, A1:
  - (V1) in G_τ needs x not its own W-cycle node. Fact 0 makes that λ(x) ≠ x, which is A1's hypothesis.
  - (V2c) with ρ′ and s(x)'s path avoiding x, then Step 2. ✓
  - x = o is included: in G_τ, s(o) = τ(o), and λ(o) ≠ o under H1. ✓
  - XA-4 (Odd x): z = s(x), so A holds with equality. The packet's Case B opening line excludes Odd x in B. ✓
- Case A, A2: Fact 0 at k+1 needs (h) at k+1, which holds since j < N. The rew(x) < rew(u) contradiction is R20's verbatim. ✓
- Case B, the opening:
  - Step 1 and (C1s) make (x, z) a gate and W-improving.
  - σ̂ lies in the arena.
  - (F1) at an S4a step: Ω_{k+1}(x) ⊵ val_σ̂(x). This uses R18 (d) Lemma S (c) for S4a's output, its signed scope. ✓
- B1, first sub-case: as R20. ✓
- B1, x on c′'s cycle:
  - (α): the better cycle node contradicts Fact 0 at k+1, replacing R20's "W's cycle-node map constant on S". ✓
  - (β): ✓
- FRZ-1 (wording, inherited): the text says "A W-improvement means one of two things" and lists (α), (β) and the odd-top non-improving
  case. It omits R20 fixes XA-3's (γ): P(π) = ∅, c′ even, and the new path shorter. (γ) concludes exactly as (β), since
  val_σ̂(x) = (c′, ∅, |π| + 1) = x ⊕ Ω_k(z). The packet's §0 says the XA-3 / XA-4 repairs are included, but §3's text does not carry XA-3.
  - Add "(γ) P(π) = ∅, c′ even, shorter: as (β)" in B-arena, and in B-fallback, where (γ) gives val_σ̂(x) ▷ Ω_k(x), a contradiction as
    in B1.
- B2:
  - D ≠ ∅ with an odd top: not W-improving (Ω(z) = π[z..x) ⊕ x ⊕ Ω(s x) for x ≠ c′).
  - D ≠ ∅ with an even top: contradicts Fact 0.
  - D = ∅ with x ≠ c′: c′ ∉ Z, because c′ lies after x on π. With c′ odd, rew(top Z) > rew(c′), which contradicts Fact 0.
  - x = c′: R20 verbatim.
  ✓
- B-fallback:
  - "S4a returned σ_k" (R20 (b) FBL step 1, statewise) makes σ_k the arena optimum, so (F1) gives Ω_k(x) ⊵ val_σ̂(x).
  - B1, first sub-case and (β): val_σ̂(x) = x ⊕ Ω_k(z) ▷ Ω_k(x).
    - FRZ-2 (wording): this cites (V2), i.e. Ω_k(x) = x ⊕ Ω_k(s(x)) with x on neither path. In B1's first sub-case x may be its own
      cycle node (x ∉ π, not on c′'s cycle, λ(x) = x). Then Ω_k(x) = (x, ∅, 0), and strictness comes from the cycle node instead: the
      W-improvement Ω_k(z) ▷ Ω_k(s x), where s(x) has cycle node x, forces rew(c′) > rew(x), so val_σ̂(x) ▷ Ω_k(x).
    - The contradiction holds in both sub-cases. One clause in the fixes file.
  - (α) and B2 with a better cycle node: contradiction. ✓
  - B2, D = ∅, x = c′: handled without (F1), using Ω_{k+1}(x) = (x, ∅, 0) (Fact 0 at k+1). This is exactly the own-cycle-node length-only
    case where "the optimum has no improvement" fails (the DF trap, R-N5-LP). The packet routes around it correctly. ✓
  - R20's N-XA-1 (B-fallback vacuous) relied on "a flat edge is coarse-equal". That still holds here for ℓ ≥ −1, but the packet also
    covers ℓ = ⊥, where COARSE_⊥ keeps lengths and the B2 x = c′ case is not vacuous. The text handles it. ✓
- Verdict: SIGNED WITH GAPS FRZ-1, FRZ-2 (both wording, closed).
### 3.3 FREEZE (SIGNED)
- Step 3: at an H2 state t ≥ F, x's W-play ends at c_x with λ(c_x) = c_x:
  - in F_t, W = Ξ;
  - via o, H2 puts τ(o) ∈ F_t and the cycle in F_t.
  So W_t(x) = value(ρ_t) with ρ_t simple, |ρ_t| ≤ n − 1, admissible for P^c_ℓ because λ is fixed in the phase and τ is the same, so
  G_τ is the same game. P^c_ℓ at j = n − 1 needs N ≥ n − 1, which the window of n states gives. ✓
- Step 4: the sandwich R15 (a), XW, Step 3, Step 1 at F, then (C3). ✓
- Non-H2 states t: sandwich to a later H2 state t2. ✓
- So FREEZE needs nothing after F but R15 (a), XW and the fixed G_τ. Fallbacks, θ- and w-changes and ¬(h) states are all allowed. Correct.
- DATA, every ℓ ∈ {⊥, −1, …, n − 1}, first n-state window per phase:
  - library: 142 windows, 2,958 later-state checks (a) + (b), 0 failures;
  - random 𝒞^1O (7,000 games): 0 windows (n consecutive (h) states never occur), so random data is VACUOUS for FREEZE, as the packet says.
  - The library counts differ from the packet's 183 / 3,532, probably by file set and window selection (I take the first window per
    (phase, ℓ)). This is not a disagreement about any statement.

## 4. Corollary RATCHET (SIGNED)
- (a): FREEZE (a), (b) at o, then (C2). Equal COARSE_ℓ values have equal cycle nodes for ℓ < ∞, giving H3. With H1, H3H2 gives (h). ✓
- (b), θ: θ_t = o ⊕ Ξ_t(σ̄_t(o)) under H1.
  - COARSE_ℓ of each exit is constant (FREEZE (a)), and COARSE_{ℓ−1} adds one membership bit, so there are ≤ 2d_o values.
  - θ is monotone (R15 (a)) and ⊴_{ℓ−1} is antisymmetric, so there are no revisits and ≤ 2d_o − 1 changes. ✓
- (b), w: w_t = o ⊕ Ξ_t(τ o) with τ(o) fixed, so ≤ 2 values in order. ✓
- (c): the pair changes ≤ 2d_o times. "Differ ⟺ r = ℓ" by (C2) at ℓ − 1 and (a). ✓
- DATA: RATCHET (a) at every H2 state ≥ F; (b) value / change counts in 142 (phase, ℓ) cases; 0 failures.

## 5. Lemma BLOCK (SIGNED)
- u_ℓ ∈ P(θ) Δ P(w), with w better there and memberships constant on I. u_ℓ lies on no route.
- A_v is frozen (FREEZE), so the two COARSE_{ℓ−1} classes (A_v, BAD) ◁ (A_v, GOOD) are well defined. The cycle node is c_θ, below u_ℓ.
- In R: BAD. After an S4a leave: WM and (C1) give ⪰ GOOD, hence = GOOD.
- A later return to R would need BAD ⪰ GOOD (R15 (a)), a contradiction by (C3). Correct.
- Consequence: per vertex the membership pattern inside I is (out*)(in*)(out*), so ≤ 2 crossings per vertex, ≤ 2n crossing
  transitions, and each exit is released at most once. ✓
- DATA: 30 library runs I (states ≥ F, (h), constant differing pair). No re-entry after an S4a leave: 0 failures.

## 6. Theorem X-RUN (SIGNED WITH GAP FRZ-3)
- (h) on P (H1 assumed, H3 by SN, H3H2). F(ℓ) is non-increasing in ℓ, and F(ℓ_max) = p_0 + n − 1. ✓
- Levels ℓ ≥ 0, segment [F(ℓ), F(ℓ − 1)):
  - RATCHET (c) gives ≤ 2d_o + 1 runs: BLOCK ≤ 2n for r = ℓ runs; r ≤ ℓ − 1 runs are windows at ℓ − 1, so < n states each before
    F(ℓ − 1); ≤ 2d_o boundaries.
  - (2d_o + 1)(3n − 1) + 2d_o = 6d_o n + 3n − 1 ≤ 6(d_o + 1)n. ✓
- Level −1:
  - after F(−1) only lengths change (≤ n values each);
  - pair runs ≤ (d_o + 1)n; θ = w runs are windows at ⊥ (< n states each before F(⊥));
  - in r = −1 runs, a leave at s followed by a later re-entry gives Ξ_t(v) ▷ Ξ_s(v) (WM, Lemma G, (C7) with equal (c, P)), so ≤ n − 1
    per vertex;
  - the event count 2[n + n(n − 1) + n(d_o + 1)n(n − 1)] plus runs and boundaries ≤ 6(d_o + 1)n³.
  ✓
- After F(⊥): Ξ, W are frozen and θ = w.
  - A switched non-flat gate would raise W(x) (B1 of P^c_ℓ); its cycle cases contradict Fact 0.
  - A flat switch at an own cycle node x ∈ F into R̄ would change x's W-cycle node or put o on an honest / W-cycle (H1 / H2 at k + 1).
  So no crossing. ✓
- Sum: (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³. ✓
- FRZ-3 (proof gap in a consequence): "REL_Q ≤ 13 d_o (d_o + 1) n³. Every leave in Q happens inside P (R-STICK)".
  - R-STICK forbids leaves only at transitions from states with c_w ≠ c_θ. The transition from P's last state p to the first non-P state
    starts at an SN state, so it can carry leaves (≤ d_o exit releases). It is not among the "crossing transitions with both ends in P".
  - The proved count is REL_Q ≤ d_o·(C_P + 1) with C_P ≤ (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³. Since C_P + 1 ≤ 13(d_o + 1)n³ for all
    n ≥ 1, d_o ≥ 2, the stated bound holds. The proof should say so.
  - The packet's crossing bound "13(d_o + 1)n³ + n" for Q already counts that transition.
- DATA: 472 library runs Q with H1 on the SN prefix (max 55 crossings in P, max REL_Q 12).
  - No crossing after F(⊥).
  - Per-level segment bound and totals: 0 failures.
  - The bounds are far from tight. This is a polynomial bound, not a sharp one.

## 7. Theorem SUB (SIGNED)
- (i): Step 1 at ℓ = ρ and R15 (a). (ii): the first n states form a window at ρ, so FREEZE applies.
- (iii): R20 §6 steps 1-5 with θ_{E+1} in step 3.
  - Step 4 needs u* ∈ P(θ_{E+1}) Δ P(w) with w the better side there. lev(θ_{E+1}, w) = ρ = rank u* and θ_{E+1} ◁ w (XW) give it, and
    u* lies on no route.
  - The symmetric difference outside V* contains u* and has nothing above it, so its top is u*.
  - Step 5 uses Lemma C at L. ✓
- Count: disjoint intervals per vertex; coarse increases only in the first n − 1 transitions (ii). ✓
- ρ = −1: ✓.
- DATA: 357 library (w, r)-subruns, plus random:
  - (i), (ii) 0 failures;
  - 27 S4a-leave / re-entry pairs inside subruns, all with a strict COARSE_ρ increase (the packet reports 123 XA′ re-entries on its set);
    0 failures.

## 8. Not to sign
- b6_xl2_n32 (sha1 909c7371…): n5.py 87 / 10, check_sol2.py "zielonka(oink zlk) OK strategies verified".
- x48_rt48_final (cff46249…): n5.py 112 / 21, Oink OK.
- I did not re-derive the FBF-on-subruns and CL1 counts.

## 9. Data (DATA, not proof; docs/referee/scratch/frz_probe.py, sha1 6791dad0…; own N5 trace asserted equal to n5.run; every game asserted
in 𝒞^1O; phase key (λ_Ξ, τ))
| run | games | key counts | failures |
| --- | --- | --- | --- |
| library (every experiments/**/*.pg in 𝒞^1O with n ≤ 64; 252 files at dc9f834f) | 252 | NL-MF 1,978; Fact 0 5,320; ARENA withheld 41,479; Step 1 54,191; FREEZE windows 142 / checks 2,958; BLOCK runs 30; X-RUN runs 472; SUB runs 357, re-entries 27 | 0 |
| rand 𝒞^1O n 8-24 seed 9401 | 4,000 | Fact 0 6,558; Step 1 46,134; X-RUN runs 932; FREEZE 0 windows | 0 |
| rand 𝒞^1O n 4-8 seed 9402 | 3,000 | Fact 0 1,918; X-RUN runs 101; FREEZE 0 windows | 0 |
- Thin spots:
  - FREEZE, RATCHET, BLOCK and SUB (iii) rest on library instances only (random games give no n-state (h) windows).
  - X-RUN's bound is loose.
  - B-fallback's x = c′ case at ℓ = ⊥ is not separately counted.

## 10. Labels after this report (D18/L40)
- PROVED (L-NEW successor 14; signed by REFEREE (Opus 5.5, D15), second referee pending), on 𝒞^1O inside a (λ_Ξ, τ) phase: NL-MF, Fact 0,
  ARENA, P^c_ℓ (FRZ-1, FRZ-2), FREEZE, RATCHET, BLOCK, X-RUN (FRZ-3), SUB.
- FALSE (DATA, lane): FBF on (w, r)-subruns; CL1. OPEN: (L1), (L2), ¬H1 SN states, f per phase, G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.

## Fixes-file lines (one per gap)
- FRZ-1: §3 B1 "x on c′'s cycle": add "(γ) P(π) = ∅, c′ even, the new path shorter: val_σ̂(x) = x ⊕ Ω_k(z), as (β)", in B-arena and in
  B-fallback (R20 fixes XA-3).
- FRZ-2: §3 B-fallback B1: "if λ(x) = x, then Ω_k(x) = (x, ∅, 0), and val_σ̂(x) ▷ Ω_k(x) by the cycle node (the W-improvement forces
  rew(c′) > rew(x)); otherwise by (V2)".
- FRZ-3: §6 consequences: "REL_Q ≤ d_o (C_P + 1), C_P the crossings with both ends in P; the transition leaving P can release exits
  (R-STICK starts after it); since C_P + 1 ≤ 13 (d_o + 1) n³, REL_Q ≤ 13 d_o (d_o + 1) n³".
