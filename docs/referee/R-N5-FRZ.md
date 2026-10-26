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

## Addendum (written 2026-10-25 06:49Z by date -u): L-NEW's fixes file for FRZ-1..FRZ-3 (Lead 06:50Z)
Object: docs/new/P-N5-FRZ-fixes-box34.md at l-new 1dc42ba, sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd (checked with git show 1dc42ba:… |
sha1sum). It is on origin/claude/l-new; trunk 447a71b1 at my fetch does not yet contain it, and the Lead's "535c268" is not an object in my
clone. The packet is unchanged (sha1 39df373c…, checked). Independent of REFEREE-2 (not read). The fixes file's §11 / unpinned items are out of scope.
| gap | repair (fixes §1) | verdict |
| --- | --- | --- |
| FRZ-1 | (γ) added after (β): val_σ̂(x) = (c′, ∅, \|π\| + 1) = x ⊕ Ω_k(z); B-arena by B1's first sub-case; B-fallback: x ⊕ Ω_k(z) ▷ Ω_k(x), against arena-optimality | CLOSED |
| FRZ-2 | B-fallback B1 split: λ(x) ≠ x by (V2); λ(x) = x strict by cycle node (rew(c′) > rew(x)) | CLOSED |
| FRZ-3 | REL_Q ≤ d_o (C_P + 1), counting the transition from P's last state; C_P + 1 ≤ 13 (d_o + 1) n³ | CLOSED; the X-RUN bounds stand as stated |
- FRZ-1: I checked the B-fallback half of (γ), the only new step.
  - x lies on c′'s cycle and is not its top, so Ω_k(x) = x ⊕ Ω_k(s(x)). Its path to c′ runs along the cycle and does not return to x.
  - x ∉ π, and rank x < rank c′, so x enters neither path set.
  - So x ⊕ preserves the strict W-improvement Ω_k(z) ▷ Ω_k(s x) (both lengths +1, same cycle node, same sets), and val_σ̂(x) ▷ Ω_k(x)
    contradicts (F1) at the arena optimum σ_k.
  - The B-arena half is the (β) chain verbatim. Correct.
- FRZ-2: the text is the clause I proposed. Correct.
- FRZ-3:
  - A leave is a crossing, so a leave at a transition with both ends in P lies in C_P. The only other place a leave can occur is the
    transition from P's last state (R-STICK, R30 (c)). Each transition releases ≤ d_o exits.
  - C_P + 1 ≤ n + 6(d_o + 1)(n² + n³) ≤ (d_o + 1)n³ + 12(d_o + 1)n³ = 13(d_o + 1)n³ for n ≥ 1, which gives REL_Q ≤ 13 d_o (d_o + 1) n³.
  - The third consequence (≤ 13(d_o + 1)n³ + n crossings in Q) already counts that transition, and the main bound (crossings with both
    ends in P ≤ 13(d_o + 1)n³) is unaffected. All X-RUN bounds stand as stated.
- Labels: with these lines, every REFEREE gap on P-N5-FRZ is closed. The signed statements stand as in the verdict table. The second
  signature (REFEREE-2 successor 7) is pending; §C follows.

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-FRZ.md, referee-2 20a73ca1, with its §C f546b43c; on trunk 87265268). REFEREE successor 7, written 2026-10-25 08:45Z by date -u
Signature (Opus 5.5, D15). This report (3a520ce7 + Addendum 3171efc7) is my lane's prior work, written by successor 6. I opened R2-N5-FRZ
(sha1 2039d70d…) only after my own R-N5-L2 was pushed (7626354e). R2-N5-FRZ did not inform the L2 verdicts.

### C.1 Verdicts that differ
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| NL-MF, Fact 0, Steps 1-2, FREEZE, RATCHET, BLOCK, SUB | SIGNED | SIGN | signed by both |
| ARENA | SIGNED | SIGN (N-FRZ-1, citation) | signed by both; N-FRZ-1 ACCEPTED (C.2) |
| P^c_ℓ | SIGNED WITH GAPS FRZ-1, FRZ-2 (wording, closed) | SIGN with notes N-FRZ-2, N-FRZ-3; label aligned to mine in its §C | signed by both, SIGNED WITH GAPS FRZ-1 = N-FRZ-2, FRZ-2 = N-FRZ-3 (closed) |
| X-RUN | SIGNED WITH GAP FRZ-3 | SIGN WITH GAPS G-FRZ-1 (+ N-FRZ-4) | signed by both; FRZ-3 = G-FRZ-1 (closed by the fixes file) |
| fixes file 168de464 | CLOSED (Addendum) | CLOSED (§9) | agree |
- No verdict differs in substance.
- The only label difference (P^c_ℓ) is already resolved by REFEREE-2's §C, which adopts this report's label.
- Neither referee has a counterexample.

### C.2 Items found by one referee only
- N-FRZ-1 (REFEREE-2 only; ARENA R → R̄, citation). MISSED by this report. ACCEPTED.
  - This report's §2 repeated the packet's "same π, (C7)".
  - The comparison is between the two endpoints σ_k(y) and z of the edge. They have different routes π_{σy} and π_z on one base (θ in Ξ,
    w in W). (C7) is one route on two bases.
  - Re-derived: write a ⊕ b for a route a (vertices before o, disjoint from P(b) and from c) prefixed to b = (c, P, ℓ).
    - The path set is (a ∩ V_{>c}) ⊔ P.
    - So between a ⊕ b and a′ ⊕ b, the symmetric difference of path sets is (a Δ a′) ∩ V_{>c}, and the length difference is |a| − |a′|.
    - The order (and equality) therefore depends on c's parity and on a, a′ only, not on P or ℓ.
  - θ and w share c (H3), and every route avoids both paths (R19 note), so the two frames order R → R̄ edges alike.
  - REFEREE-2's line (row 4 below) is correct.
- N-FRZ-4 (REFEREE-2 only; wording): d_o, "crossing transition" and "leaves R" are not defined in the packet. ACCEPTED. This report read
  them from R30 / R21, as REFEREE-2 did.
- NL phase-key note (this report only, §1): accepted by REFEREE-2 (its row 6).
- Everything else was found by both, independently: FRZ-1 = N-FRZ-2, FRZ-2 = N-FRZ-3, FRZ-3 = G-FRZ-1.
- REFEREE-2's addition to FRZ-1: in (γ), x = c′ is impossible, because it would put x ∈ π, which is B2. Checked: x on c′'s cycle with
  x = c′ means z's path to c′ ends at x, so x ∈ π. Agreed.

### C.3 REFEREE-2's two data questions, answered from my lane's data
These come from frz_probe.py with three counters added at this §C. The checks are unchanged. Library = 261 files at referee head
(trunk 87265268 merged). Totals: 0 failures; FREEZE windows 144, BLOCK runs 30, X-RUN runs 482 (max 55 crossings in P, max REL_Q 12),
SUB re-entries 27.
- (i) BLOCK: 0 S4a leaves inside my 30 runs I (counter BLOCK_S4a_leaves). So BLOCK is VACUOUS in both referees' data. The "no re-entry
  after an S4a leave" in this report's §5 was vacuous.
- (ii) X-RUN past F(⊥) and segment −1:
  - 0 transitions of P after an F(⊥) (counter XRUN_afterbot_tr);
  - 0 runs reaching F(−1) (XRUN_seg_m1_runs);
  - so this report's "no crossing after F(⊥)" was vacuous too. X-RUN's segment −1 and post-F(⊥) parts are proof-only in both referees'
    data.
- Also counted: 0 leaves at the transition from P's last state (XRUN_leaves_from_last_P). FRZ-3 = G-FRZ-1 was never observed in my data
  either.
- Joint thin spots for the result:
  - BLOCK is vacuous.
  - X-RUN's segment −1 and post-F(⊥) are unexercised.
  - Random 𝒞^1O games have no n-state (h) window, so FREEZE, RATCHET and SUB (iii) rest on library instances (mine) and on library plus
    climbs (REFEREE-2).
  - X-RUN's bound is far from tight (max 55 crossings in P for both).

### C.4 Joint gap map (one fixes-file line per row; rows as in R2-N5-FRZ C.4)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | FRZ-1 | N-FRZ-2 | wording, closed | §3 B1: "(γ) P(π) = ∅, c′ even, the new path shorter: as (β)" (already in fixes §1) |
| 2 | FRZ-2 | N-FRZ-3 | wording, closed | §3 B-fallback B1: "if λ(x) = x, strict by the cycle node (rew(c′) > rew(x)); otherwise by (V2)" (already in fixes §1) |
| 3 | FRZ-3 | G-FRZ-1 | proof gap in a consequence, closed; never observed | §6: "REL_Q ≤ d_o (C_P + 1); C_P + 1 ≤ 13 (d_o + 1) n³" (already in fixes §1) |
| 4 | missed, accepted | N-FRZ-1 | citation, closed | §2 ARENA R → R̄: replace "(C7)" by "for a fixed base b with cycle node c, the order of π_z ⊕ b against π_{σy} ⊕ b depends only on (π_z Δ π_{σy}) ∩ V_{>c}, |π_z| − |π_{σy}| and c's parity; θ and w share c (H3), so both frames order the edge alike" |
| 5 | accepted | N-FRZ-4 | wording | §0: "d_o := \|succ(o)\| (R30); a crossing transition changes R (R21); v leaves R at s → s+1 if v ∈ R_s and v ∉ R̄_{s+1}" |
| 6 | NL phase-key note | accepted | citation transfer, closed | §0 R29: "NL is signed on (λ_Ξ, λ_U, τ); its proof uses no λ_U, so it holds on (λ_Ξ, τ) (R-N5-FRZ §1)" |
- Rows 4-5 are new for the lane's fixes file. Rows 1-3 are already there.

### C.5 Joint label (D18/L40)
- PROVED (L-NEW successor 14; REFEREE and REFEREE-2, Opus 5.5, D15), on 𝒞^1O inside a (λ_Ξ, τ) phase, pending CHECKER:
  - NL-MF (row 6), Fact 0, ARENA (row 4), Steps 1-2;
  - P^c_ℓ (rows 1-2), FREEZE, RATCHET, BLOCK;
  - X-RUN (row 3, row 5), SUB.
- Honest limits: the C.3 thin spots. X-RUN bounds crossings per fallback-free run with H1 on its SN prefix, not f or the number of runs
  per phase.
- FALSE (DATA, lane): FBF on (w, r)-subruns; CL1.
- OPEN: (L1), (L2), f per phase, G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.
- With both signatures on P-N5-FRZ, the premise of P-N5-L2's FREEZE′ and X-RUN′ (R-N5-L2 §4, §7) is met once CHECKER passes.

Signed: REFEREE successor 7 (Opus 5.5, D15).

### C.6 Addendum to §C (Lead 08:41Z), written 2026-10-25 08:58Z by date -u
- (a) N-FRZ-1 and N-FRZ-4: both ACCEPTED, as in C.2.
- (b) REFEREE-2's question, in its broader form:
  - Question: does any S4a leave occur at an (h) state after a freeze?
  - Count: frz_probe.py counter LEAVE_h_afterF, library 261 files, for every FREEZE window at ℓ ≥ 0, over every (h) S4a transition
    t ≥ F of the phase. Transitions are counted once per (window, ℓ), so one transition can be counted several times.
  - Result: 2,410 such transitions, 0 vertices leaving R.
  - Together with C.3 (0 leaves inside the 30 BLOCK runs), BLOCK is vacuous in all data of both referees.
- (c) Joint label confirmed as in C.5: PROVED (L-NEW succ. 14; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER, with the C.3
  thin spots.
