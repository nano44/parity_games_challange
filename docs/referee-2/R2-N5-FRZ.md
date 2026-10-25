# R2-N5-FRZ: second-referee check of packet P-N5-FRZ (L-NEW box 34: a coarse freeze through θ-changes, w-changes and fallbacks; crossings per fallback-free run). REFEREE-2 (successor 7), 2026-10-25 08:21Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-FRZ (Lead brief 07:04Z, GO 07:13Z), object docs/new/P-N5-FRZ-box34.md, sha1
39df373c17d91f942ad2cb15244cd779ca7abda1 (287 lines; `sha1sum` on my tree). Pin: trunk 25fda0f3 ("Lead: P-N5-FRZ pinned"), where the
blob equals the one on my tree (67a871c7). The brief's "f10d381 or later" was a slip: the file does not exist at f10d381 (the Lead
confirmed this at 07:13Z). The object was added at l-new edbccb69 and is unchanged since.
Background read: RESULTS R15 (a), R17 (a), R19 (a), R20 (all of it, including XA-3/XA-4/N-XA-1), R21 (crossing, XW, FBL-N), R23 (g) WM,
R25 (lev, COARSE, (C1)-(C4)), R27-R30 (setting, NL, R-STICK, SN-PREFIX, H3H2, ABS-COUNT′); SPEC docs/new/N5-ssi-global.md S1-S5.
Independence: I have not opened docs/referee/R-N5-FRZ.md or notes/REFEREE.md; both are on my tree, and I only listed them. I read
the lane's fixes file docs/new/P-N5-FRZ-fixes-box34.md only after my verdicts below were fixed (§9). I did not run or import any lane
script (freeze.py, relfr.py, snvi.py, rsub*.py, rerel.py, the fb* scripts) or any REFEREE probe. Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-FRZ/ (own code on my lane's R2-N5-RE/re_check.py): frz_check.py, frz_climb.py, run_all.sh,
run_climbs.sh, run_climbs2.sh, oink_xcheck.py, h2need.py, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt. Every game asserts
exactly one Odd vertex with out-degree > 1. Phase key (λ_Ξ, τ), as in the packet.
Labels (D18 / L40): the packet's PROVED (L-NEW succ. 14) label is its own. §8 is not signed, as briefed. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Corollary NL-MF | SIGN | NL is used at L = ⊥ whenever no gate goes into F (R29 (e) allows every L < ∞; 2,610 library cases) |
| §2 Fact 0 | SIGN | — |
| §2 Lemma ARENA | SIGN | N-FRZ-1 (citation): the R → R̄ case is not (C7) (one prefix, two bases) but its two-prefix, one-base twin. One line, given below |
| §3 Lemma P^c_ℓ (Steps 1-2 included) | SIGN | N-FRZ-2 (wording): case B1 (β) lists "P(π) = ∅, c′ odd, longer" but not "P(π) = ∅, c′ even, shorter". This is R20's XA-3 again, closed the same way. N-FRZ-3 (wording): in B-fallback B1, "x ⊕ Ω_k(s(x)) = Ω_k(x)" needs x ≠ λ(x). At x = λ(x) the case is a contradiction by cycle node |
| §3 Theorem FREEZE (a), (b) | SIGN | The hypothesis "an H2 state t2 ≥ t" is used. DATA: x31_rx48 has a state with no later H2 where COARSE_ℓ(Ξ) moved (§3.3) |
| §4 Corollary RATCHET (a)-(c) | SIGN | — |
| §5 Lemma BLOCK | SIGN | Vacuous in all data: 0 S4a leaves inside an r = ℓ block, and in fact 0 S4a leaves at an (h) state after any freeze at ℓ ≥ 0 |
| §6 Theorem X-RUN | SIGN WITH GAPS | G-FRZ-1 (accounting, closed here). "Every leave in Q happens inside P" and REL_Q also need the transition leaving P, whose start is in P and whose end is not. That transition is not "with both ends in P", and R-STICK does not cover it. The proof's sum has room for it, so the bounds stand as stated. N-FRZ-4 (definitions): d_o and "crossing transition" are taken from R30 / R21 |
| §7 Theorem SUB (i)-(iii) | SIGN | (iii) re-proved directly below (§7) |
| §8 | not signed (as briefed) | — |
No statement is NOT SIGNED. No counterexample in 16,434 batch runs and 1,485,828 climb runs (12 climbs).

## 1. Corollary NL-MF: SIGN
- Taking L := MF_j makes (A_j) true by definition. With r_j > L, R29 (e) NL (ii) gives R_j ⊆ R̄_{j+1}, and NL (iii) is (A_{j+1}) for L, i.e.
  MF_{j+1} ≤ MF_j. ✓
- MF_j = ⊥ (no gate into F_j) uses NL at L = ⊥. R29 (e) is stated for every L < ∞, and ⊥ < ∞. The case is frequent: 2,610 of the 6,024
  library cases with r > MF, and 159,047 in climbs.
- The consequence ("a leave needs a gate into F_j of level ≥ r_j") is the contrapositive. ✓
- DATA (§10): 16,601 (h) S4a steps in the library, 6,024 with r > MF. 0 leaves there and 0 MF rises. Each of the 3,093 steps with a
  leave has a gate into F of level ≥ r. Climbs: 3,378,851 steps, 0 failures.

## 2. Fact 0 and Lemma ARENA: SIGN (N-FRZ-1)
- Fact 0.
  - On F, W = Ξ (R19 (a)).
  - On R̄: on 𝒞^1O, H_k and (σ_k, τ) differ only at o, so the plays agree up to o. λ(v) = c_θ, and the W-cycle node is c_w = c_θ (H3).
  - c_θ ∈ F: by H1 o's honest cycle avoids o, and the (σ, τ)-plays of that cycle's vertices are the same cycle. ✓
- ARENA. I checked the four edge classes for Even y.
  - R → F: W(z) = Ξ(z) and W(σ y) = π ⊕ w ⊵ π ⊕ θ = Ξ(σ y) (XW, then prefixing), so the edge is a gate. ✓
  - F → F: Ξ = W. ✓
  - F → R̄, withheld: Ξ(σ y) = W(σ y), since σ y ∈ F.
    - If the edge is not a gate: π_z ⊕ θ ⊴ W(σ y) ◁ π_z ⊕ w.
    - Equality on the left gives level ⊥. Otherwise (C5) gives lev(π_z ⊕ θ, W σ y) ≤ lev(π_z ⊕ θ, π_z ⊕ w) = r (C7, since π_z avoids both
      paths and c).
    - Then (C6) gives lev(W σ y, π_z ⊕ w) ≤ r. ✓
  - R → R̄ (N-FRZ-1, citation): the step compares π_z ⊕ θ with π_{σy} ⊕ θ, and π_z ⊕ w with π_{σy} ⊕ w. That is two prefixes on one base,
    not (C7)'s one prefix on two bases.
    - The right fact: for a base b with cycle node c, and prefixes a, a′ that avoid P(b) and c, the comparison of a ⊕ b with a′ ⊕ b
      depends only on (a Δ a′) ∩ V_{>c}, on |a| − |a′| and on the parity of c. The P(b) parts cancel.
    - H3 gives θ and w the same c. So the two frames order these edges alike. ✓ The conclusion stands.
- DATA: 16,601 (h) S4a steps, 145,248 W-improving edges, 105,757 withheld (in 9,052 steps). Every withheld edge is F → R̄, not a gate, of
  level ≤ r, and none occurs at θ = w. Climbs: 7,464,913 withheld edges, 0 failures.

## 3. Lemma P^c_ℓ and Theorem FREEZE: SIGN (N-FRZ-2, N-FRZ-3)
### 3.1 Steps 1-2
- Step 1. Under (h), R19 (a) gives Ξ = π_v ⊕ θ_k and W = π_v ⊕ w_k on R̄. π_v ⊆ R_k avoids both paths, which lie in F ∪ {o}, and avoids
  c_θ ∈ F. (C7) gives lev = r_k ≤ ℓ, and (C2) gives coarse equality. ✓
- Step 2 at an S4a step: WM (R23 (g); R30 (c) records that WM holds on the (λ_Ξ, τ) phase) and (C1).
- Step 2 at a fallback: Step 1 at both ends, R15 (a) and (C1). ✓ This is where the window needs r ≤ ℓ at k and k+1, and it has that.
### 3.2 Lemma P^c_ℓ: case by case
- Base. u is an honest cycle node, so u ∈ F and W(u) = (u, ∅, 0) (Fact 0). ✓
- A1 (x ≠ λ(x)).
  - x is not its own W-cycle node (Fact 0), so (V1) holds in G_τ.
  - The path of Ω_k(s(x)) avoids x: if x is on its own cycle, the walk from s(x) reaches c before x.
  - (V2c) applies, since x is on neither path and neither cycle node is x. ✓
  - Odd x, including o (H2: o is not its own W-cycle node), falls here with z = s(x). This is R20's XA-4, handled.
- A2 (x = λ(x)).
  - Both rew orders and x = u are covered.
  - "Ω_k(s(x)) has cycle node x" holds because s(x) is on x's own W-cycle. ✓
- Case B.
  - x is Even, and (C1s) gives a gate that is also W-improving. ✓
  - B-arena: (F1) in the arena, with τ_{k+1} = τ in the phase (an in-phase transition is an S4a step or an Even fallback). ✓
  - B1, x not on c′'s cycle: (V2c) with x ∉ π and ρ′ avoiding x. ✓
  - B1, x on c′'s cycle (α): the new cycle's top is the even top of P(π), which beats c′ = λ(x). That contradicts Fact 0 at k+1, which
    is in the window. ✓
  - B1 (β), N-FRZ-2 (wording): "A W-improvement means one of two things" omits P(π) = ∅ with c′ EVEN and π SHORTER.
    - That case is W-improving when x is on c′'s cycle and σ_k(x) is farther from c′ than z.
    - It is handled exactly like the listed (β): the new cycle still has top c′, and val_σ̂(x) = (c′, ∅, 1 + |π|) = x ⊕ Ω_k(z).
    - This is R20's XA-3 again. Fix: read (β) as "P(π) = ∅ and the length is better by c′'s parity".
    - The same sentence recurs in B-fallback ("first sub-case and (β)") with the same fix.
  - B2: I checked D ≠ ∅ odd (not improving), D ≠ ∅ even (Fact 0), D = ∅ (z's path contains x's, so it is strictly longer, so c′ is odd),
    x ≠ c′ (c′ ∉ Z, top(Z) beats c′: Fact 0), and x = c′ (Fact 0 at k+1, or the IH against cycle node u). ✓
  - B-fallback: S4a returned σ_k (R20 (b) step 1; R21 (c) FBL-N (i)), so σ_k is the arena optimum and (F1) gives Ω_k ⊵ val_σ̂ pointwise.
    - N-FRZ-3 (wording): "val_σ̂(x) = x ⊕ Ω_k(z) ▷ x ⊕ Ω_k(s(x)) = Ω_k(x) by (V2)" needs x ≠ λ(x).
    - If x = λ(x) in B1's first sub-case, then c′ ≠ x (x is not on c′'s cycle). Ω_k(z) ▷ Ω_k(s(x)) with different cycle nodes means c′
      beats x, so val_σ̂(x) beats Ω_k(x) = (x, ∅, 0) by cycle node. The contradiction stands.
    - The same remark applies to B-arena B1, where that case contradicts Fact 0 at k+1. No conclusion changes.
### 3.3 Theorem FREEZE
- Step 3: under H2 at t, x's W-play ends at a cycle inside F_t, where W = Ξ, so its top c_x has λ(c_x) = c_x. λ is fixed in the phase,
  and the W-value is value(ρ_t) for the simple path ρ_t to c_x, of length ≤ n − 1. Lemma P^c_ℓ at j = n − 1 needs the window to have
  n states, which it has. ✓
- Step 4: the sandwich R15 (a) ⪯ XW ⪯ Step 3 = Step 1 at F, then (C3). ✓
- The non-H2 case uses t2. ✓
- The hypothesis "some t2 ≥ t has H2" is used: without it COARSE_ℓ(Ξ) can move.
  - DATA, not a claim of the packet: x31_rx48.pg (experiments/red/xing/instances, sha1 34b44d5d…), S3 start, phase states [2, 51],
    ℓ = 44, F = 49, t = 51 (H1, ¬H2, ¬H3, the last state before a phase change). COARSE_44(Ξ) differs at 44 vertices; at v = 0 the path
    set {4, 5, 7, 10, 14, 16, 17, 19, 31, 38} becomes ∅. Script h2need.py.
  - The library has 13 such states, the climbs 31. None of them falls under the theorem.
- Window length is used, as a sensitivity test of my checker. With windows of ⌊n/2⌋ states instead of n (FRZ_WINF=0.5), FREEZE (a) and (b)
  fail on x32_sc32_final.pg (experiments/new/box28/instances, sha1 c871404f…): run 0, phase [4, 76], F = 70, ℓ = 22, 96 violations. At
  0.75 n and 0.9 n, and at n, there are none.
- DATA (FREEZE, through what): library 302 freezes, all at ℓ ≥ 0, with 5,502 later states checked for (a) and 5,502 for (b). Of those,
  4,052 are past a fallback after F and 4,532 past a θ-change. Climbs: 125,028 freezes, 296,219 later states, 198,210 past a fallback,
  250,625 past a θ-change. 0 failures.
- Thin spots: no freeze at ℓ = −1 or ℓ = ⊥ anywhere (library, random, all climbs, including three aimed at them). No later state is
  past a w-change or a ¬(h) state with an H2 state after it. Those parts of FREEZE rest on the proof alone.
- Lemma P^c_ℓ DATA: library 3,386 windows (longest 2.62 n), 3,755 exhaustive (n ≤ 10) and 927,530 sampled path comparisons. Climbs:
  1,370,078 windows, about 77.6 M comparisons. 0 failures.

## 4. Corollary RATCHET: SIGN
- (a) FREEZE (a) and (b) at x = o, then (C2). Equal coarse values at ℓ < ∞ have equal cycle nodes (H3), and r ≤ ℓ. With H1, R30 (d)
  gives (h). ✓
- (b), θ.
  - Under H1, θ = o ⊕ Ξ(σ̄(o)) with σ̄(o) ∈ succ(o).
  - (C4) passes COARSE_{ℓ−1} through o ⊕.
  - Per exit, COARSE_ℓ(Ξ) is frozen, so COARSE_{ℓ−1}(Ξ) has ≤ 2 values (the rank-ℓ vertex in or out). That gives ≤ 2d_o values,
    monotone by R15 (a), (C1), (C3). ✓
- (b), w: under H2, w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F. ✓
- (c) ≤ (2d_o − 1) + 1 changes. "Differ" means lev ≥ ℓ, and with (a) that is r = ℓ. ✓
- DATA: 5,804 (a) checks in the library, 421,247 in climbs. Max 2 θ-values, 1 θ-change, 0 w-changes, 2 runs; the bounds hold with room.

## 5. Lemma BLOCK: SIGN
- Re-derived.
  - u_ℓ ∈ P(θ) Δ P(w), and w has the GOOD side (XW). Its membership is fixed on I, because the pair is constant.
  - u_ℓ lies in F ∪ {o} paths, and u_ℓ ≠ o, so it is on no route.
  - On R, u_ℓ's membership in Ξ(v) is θ's (BAD). After an S4a leave, WM and R19 (a) give COARSE_{ℓ−1} ⪰ (A_v, GOOD), hence = (A_v, GOOD).
  - A later re-entry would need (A_v, BAD) ⪰ (A_v, GOOD) (R15 (a)). ✓
- The consequence (≤ 2 crossings per vertex inside a fallback-free I, so ≤ 2n crossing transitions) follows. ✓
- DATA: VACUOUS.
  - The library has 60 blocks (longest 51 states) and the climbs 3,610 (three climbs aimed at leaves, FIT=leave). There are 0 S4a leaves
    inside a block, and 0 S4a leaves at an (h) state after any freeze at ℓ ≥ 0 (counter LEAVE_* never fired).
  - Crossings in fallback-free blocks (entries only): at most 7 in the library and 10 in climbs.
  - BLOCK rests on the proof alone.

## 6. Theorem X-RUN: SIGN WITH GAPS (G-FRZ-1 closed here; N-FRZ-4)
- Set-up. P's states have (h): H1 by hypothesis, H3 by the definition of P, and R30 (d). F(ℓ) is non-increasing, and F(ℓ_max) = p_0 + n − 1.
  ✓
- Segment ℓ ≥ 0.
  - RATCHET (c) bounds the runs by 2d_o + 1.
  - r = ℓ runs: BLOCK gives ≤ 2n crossings each.
  - Agree runs are windows at ℓ − 1 and so have < n states in the segment. The run holding F(ℓ − 1) has < n states before it.
  - Boundaries: ≤ 2d_o.
  - (2d_o + 1)(3n − 1) + 2d_o = 6d_o n + 3n − 1 ≤ 6(d_o + 1)n. ✓
  - The transition into F(ℓ − 1) starts in the agree run that creates F(ℓ − 1), so it is counted. Counting states, each starting one
    transition, makes this exact.
- Segment −1.
  - (c, P) is frozen, so each Ξ(x) has ≤ n lengths. θ has ≤ d_o n values and w ≤ n, so there are ≤ (d_o + 1)n pair runs.
  - θ = w runs have < n states.
  - θ ≠ w runs: a leave at s, then re-entry at t, gives Ξ_t(v) ⊵ Ξ_{s+1}(v) = W_{s+1}(v) ⊵ π ⊕ w ▷ π ⊕ θ = Ξ_s(v), a strict rise. So
    each vertex has ≤ n − 1 such re-entries.
  - Entries ≤ first entries + re-entries, and leaves ≤ initial members + entries, so crossing events ≤ 2(n + re-entries). This matches
    the packet's 2[n + n(n − 1) + n(d_o + 1)n(n − 1)]. ✓
- After F(⊥).
  - Ξ = W everywhere (θ = w), so gates are W-improving edges.
  - A non-flat gate would raise W strictly ((F1), case B1) or contradict Fact 0 (cycle cases). The only gates left are flat:
    x = λ(x) ∈ F, z with W-cycle node x.
  - Several flat switches at once still keep F_k closed under (σ_{k+1}, τ) (each switched x ∈ F goes to z ∈ F), and leave R's routes
    untouched (no R vertex switches). So R_{k+1} = R_k. ✓ (I checked the simultaneous case the packet does not spell out.)
- Sum: (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³. ✓
- G-FRZ-1 (accounting).
  - The statement counts crossing transitions "with both ends in P". The consequences then say "every leave in Q happens inside P
    (R-STICK)" and REL_Q ≤ 13 d_o (d_o + 1) n³.
  - The transition p_last → p_last + 1 leaving P (when P ≠ Q) has its start in P, where c_w = c_θ. R-STICK protects only starts with
    c_w ≠ c_θ, so exits may leave R at that transition, and neither the main count nor "inside P" covers it.
  - Closure: count crossing transitions that START in P. The proof bounds the same quantity plus this one transition, and
    (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ + 1 ≤ 13(d_o + 1)n³ for n ≥ 1 (the slack is ≥ 7(d_o + 1)n³ − 6(d_o + 1)n² − n > 0).
  - So REL_Q ≤ d_o · 13(d_o + 1)n³ and "Q has ≤ 13(d_o + 1)n³ + n crossing transitions" both hold as stated.
  - DATA: 0 leaves at a transition leaving P, in the library and in climbs.
- N-FRZ-4 (definitions): d_o (= |succ(o)|, R30), "crossing transition" (changes R, R21) and "leaves R" (v ∈ R_s, v ∉ R̄_{s+1}) are not
  defined in the packet. I used R30's and R21's.
- DATA:
  - Library: 4,799 maximal fallback-free runs, 2,883 with H1 on P, the longest P 56 states, at most 55 crossings in P, REL_Q ≤ 10.
    Every sub-count of the proof was checked on its own: F monotone, F(ℓ_max) = p_0 + n − 1, runs per segment, ≤ 2n per r = ℓ run,
    < n agree states, segment ≤ 6(d_o + 1)n. 0 R-STICK leaves after P. 0 SN-PREFIX failures.
  - Climbs: 1,092,901 runs with H1 on P, 0 failures.
  - Thin spots: only 3 library segments at ℓ ≥ 0 (104,690 in climbs, almost all at n 6). There are 0 segments at −1, 0 transitions
    after F(⊥), and 0 crossings inside r = ℓ runs. The −1 and after-F(⊥) parts rest on the proof alone.

## 7. Theorem SUB: SIGN
- (i) Step 1 at each state with ℓ = ρ, plus R15 (a). (ii) The first n states form a window at ρ, so FREEZE applies.
- (iii), re-derived directly rather than "R20 §6 verbatim".
  - Ξ_L(x) = π_L ⊕ θ_L, whose u*-membership is BAD.
  - Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x) = W_{L+1}(x) ⊵ π_L ⊕ w (WM). π_L ⊕ w has COARSE_ρ equal to Ξ_L's (lev(θ_L, w) = ρ), with GOOD membership.
  - Ξ_{E+1}(x) = π_{E+1} ⊕ θ_{E+1} has BAD membership, because lev(θ_{E+1}, w) = ρ = rank u* and w is the better side (XW).
  - So COARSE_ρ(Ξ_{E+1}(x)) cannot equal COARSE_ρ(π_L ⊕ w), and with ⊵ and (C1)/(C3) it is strictly above. ✓
- Count: disjoint intervals, strict coarse rises only in the first n − 1 transitions by (ii), ≤ n − 1 per vertex. ✓
- ρ = −1: strict Ξ rise as written. ✓
- DATA: library 1,742 subruns with ρ ≥ −1 (60 of length ≥ n) and 7 re-entries; climbs 529,619 subruns and 155 re-entries
  (max 15 in one subrun). 0 failures.

## 8. §8 (not signed)
Not reviewed for signature, as briefed. FBF-on-subruns FALSE and CL1 FALSE are the lane's DATA findings; I did not re-run them.

## 9. The fixes file, read after the verdicts above were fixed (08:20Z)
docs/new/P-N5-FRZ-fixes-box34.md, sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd (`sha1sum` on my tree). It is the lane's record of
REFEREE's three gaps. Reading it shows those gaps' content, but not REFEREE's report itself, which I have still not opened.
- REFEREE FRZ-1 (B1 (γ): P(π) = ∅, c′ even, shorter) = my N-FRZ-2, found independently. The lane's (γ) text is correct, in B-arena and
  in B-fallback; x ≠ c′ there, since x on c′'s cycle with x = c′ would put x ∈ π (B2).
- REFEREE FRZ-2 (B-fallback B1 when λ(x) = x) = my N-FRZ-3, found independently. The lane's two-case replacement is correct and is the
  argument I gave in §3.2.
- REFEREE FRZ-3 (X-RUN: the transition from P's last state) = my G-FRZ-1, found independently. The lane's replacement, REL_Q ≤ d_o (C_P + 1)
  with C_P + 1 ≤ 13(d_o + 1)n³, is my closure in §6. Correct.
- What I found that the fixes file does not carry:
  - N-FRZ-1, ARENA's R → R̄ case cites (C7) for a two-prefix comparison (wording);
  - N-FRZ-4, d_o / crossing / leave are undefined in the packet (wording);
  - the FREEZE H2-later hypothesis shown to be used (DATA, x31_rx48);
  - window length n shown to be used by my checker's sensitivity test (DATA, x32_sc32_final at n/2);
  - BLOCK vacuous in all data, including leave-aimed climbs;
  - no freeze at ℓ ∈ {−1, ⊥} anywhere, so X-RUN's segment −1 and post-F(⊥) parts are proof-only;
  - the simultaneous flat-switch case after F(⊥), checked in §6;
  - 0 leaves at the transition leaving P in all data (FRZ-3 / G-FRZ-1 is a proof gap, never seen).
- With the fixes file's three repairs, my verdicts are unchanged: X-RUN stays SIGN WITH GAPS (G-FRZ-1, closed by FRZ-3's text); the
  rest SIGN.

## 10. DATA (DATA, not proof). Commands from docs/referee-2/R2-N5-FRZ/
- N5 used: my own (re_check.py primitives). S4a is a pointwise arena optimum in G_τ, by deterministic switch-all SI, or with --rand by
  random-subset SI plus random value-preserving re-choices. S4b takes Odd's pointwise-best option at o. The S4c fallback is as in SPEC
  (best key, ties to the larger index).
  - This is NOT SPEC's tie-break (FIX 2 / FIX 4), so the state sequences differ from n5.py's.
  - The packet's proofs use only (F1) of the S4a optimum, so every statement must hold under any optimum. The data tests that.
  - oink_xcheck.py: on all 234 LIB files (S3 start, deterministic and --rand), the final W-regions of my N5 equal Oink --zlk's (8fbf0a7):
    468 / 468.
- run_all.sh (logs/, totals_logs.txt):
  - LIB = experiments/new/box34/lib.txt (234 files) × 3 starts (S3 + 2 random) × {deterministic, --rand};
  - b6_xl2_n32, x48_rt48_final and oneh_cex_n32 × 10 --rand;
  - random 𝒞^1O: 4 × 3,000 at n 4-8, plus 2 × 1,500 at n 8-16 --rand.
  - Totals: 16,434 runs, 42,962 transitions, 2,362 fallbacks, 3,879 phases, 477 logs, all RESULT OK, 0 violations.
  - Per-statement counts are in §1-§7.
- run_climbs.sh / run_climbs2.sh (climb/, totals_climb.txt): 12 climbs of 600-900 s each.
  - FIT block ×3, leave ×3, low ×3, fb ×3. Seeds: b6_xw_n32, fb32_inr2_final, fbref_cex_n32, j10_n24, j8_n32, b6_xw_n40, x32_sc32_final,
    my climb/best_block_11.pg and best_fb_31.pg, and random n 5-14.
  - 371,457 evaluations, 1,485,828 runs, 5,436,194 transitions, 0 violations.
  - The first wave's last four climbs were killed by my session's background time limit and re-run in wave 2. Their partial outputs
    were discarded.
- Mutation / sensitivity test: FRZ_WINF=0.5 (§3.3). Without the H2-later hypothesis: h2need.py (§3.3).
- Random 𝒞^1O games: the 15,000 random runs of the batch contain no freeze at all (no window of n states; 1,022 shorter windows were
  checked for P^c). Freezes on small games came only from the climbs (low_21 at n 6). This is consistent with the packet's §9 note that
  random games are nearly vacuous.

Signed: REFEREE-2 successor 7 (Opus 5.5, D15).

## §C. Comparison with REFEREE (docs/referee/R-N5-FRZ.md: report 3a520ce7, Addendum 3171efc7). REFEREE-2 successor 7, 2026-10-25 08:31Z (date -u)
I opened R-N5-FRZ.md only after my report (20a73ca1) was pushed. Before that I had seen REFEREE's three gaps only through the lane's fixes
file, which I read after my verdicts were fixed (§9). Signature (Opus 5.5, D15).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| NL-MF | SIGNED (phase-key note) | SIGN | signed by both; REFEREE's phase-key transfer accepted (C.2, row 6) |
| Fact 0 | SIGNED | SIGN | signed by both |
| ARENA | SIGNED | SIGN (N-FRZ-1, citation) | signed by both; row 4 |
| Steps 1-2 | SIGNED | SIGN (inside P^c_ℓ) | signed by both |
| P^c_ℓ | SIGNED WITH GAPS FRZ-1, FRZ-2 (wording, closed) | SIGN with notes N-FRZ-2, N-FRZ-3 (wording) | LABEL DIFFERS, content identical: the same two wording points. I adopt REFEREE's label, SIGNED WITH GAPS FRZ-1, FRZ-2 (closed) |
| FREEZE | SIGNED | SIGN | signed by both |
| RATCHET | SIGNED | SIGN | signed by both |
| BLOCK (+ Consequence) | SIGNED | SIGN (vacuous in my data) | signed by both; data thin (C.3) |
| X-RUN | SIGNED WITH GAP FRZ-3 | SIGN WITH GAPS G-FRZ-1 | signed by both; FRZ-3 = G-FRZ-1, closed by the fixes file |
| SUB | SIGNED | SIGN | signed by both |
| §8 | not signed | not signed | — |
| Addendum (fixes file 168de464: FRZ-1..3 closed) | CLOSED | CLOSED (my §9) | agree |
The only difference is the label on P^c_ℓ, and it is resolved by adopting REFEREE's. No verdict differs in substance. Neither referee
found a counterexample.

### C.2 Item by item
- FRZ-1 = N-FRZ-2 (B1 case (γ): P(π) = ∅, c′ even, shorter; R20's XA-3 inherited). Found independently, with the same repair.
  - REFEREE's Addendum checks the B-fallback half of (γ): x not the top, x ⊕ strict.
  - I add only that x = c′ cannot occur in (γ): x on c′'s cycle with x = c′ puts x ∈ π, which is B2.
- FRZ-2 = N-FRZ-3 (B-fallback B1 at λ(x) = x: strictness by cycle node). Found independently. REFEREE's clause and my §3.2 argument are
  the same.
- FRZ-3 = G-FRZ-1 (X-RUN: the transition from P's last state can release exits, and R-STICK does not cover it). Found independently.
  - Both repairs give REL_Q ≤ d_o (C_P + 1) with C_P + 1 ≤ 13(d_o + 1)n³. The fixes file carries it.
  - I add the data point: 0 leaves at that transition in my library and climbs, so this is a proof gap that was never observed.
- Row 4, N-FRZ-1 (REFEREE-2 only; ARENA R → R̄, citation). REFEREE's §2 reads "same π, (C7)". The packet's "same π" is the route shared by
  Ξ(v) and W(v) at ONE endpoint v. The ARENA comparison is between the two endpoints σ y and z, which have different routes.
  - (C7) compares π ⊕ a with π ⊕ b (one prefix, two bases). That is Ξ(z) against W(z), not Ξ(z) against Ξ(σ y).
  - The step needs the twin fact: for one base b with cycle node c, the order of π_z ⊕ b against π_{σy} ⊕ b depends only on
    (π_z Δ π_{σy}) ∩ V_{>c}, on |π_z| − |π_{σy}| and on c's parity. H3 then makes θ and w give the same order.
  - The conclusion is unaffected. I propose one fixes-file line (C.4) and ask REFEREE to accept or contest it.
- Row 5, N-FRZ-4 (REFEREE-2 only; wording): d_o, "crossing transition" and "leaves R" are used but not defined in the packet. REFEREE
  read them from R30 / R21, as I did.
- Row 6, REFEREE's NL phase-key note (REFEREE only), ACCEPTED.
  - R29 (e) NL is signed under R21's key, a joint λ-phase (λ_Ξ, λ_U) with τ constant. The packet's phase is (λ_Ξ, τ).
  - My report cited NL without checking that transfer. That was my miss; it is the trap my lane's notebook names.
  - REFEREE's transfer argument: NL's proof uses Lemma G and (C7) (statewise), WM (τ only, transfer recorded in R30 (c)), R25's (T)
    (iii) step (λ_Ξ constant) and TRANSFER (R15 only), and nothing uses λ_U. I re-read the list against R29 (e) and accept it.
  - My data used the (λ_Ξ, τ) key throughout and had 0 NL-MF failures (6,024 library and 852,832 climb cases with r > MF). The other
    citations in the packet are statewise (R19 (a), XW, Fact 0), every-transition (R15 (a)), or already transferred (WM in R30 (c);
    FBL step 1 = R21 (c) FBL-N (i), τ only).
- REFEREE's remark on ℓ = ⊥ (B-fallback B2 x = c′ is not vacuous there, and the packet handles it): agreed. In my data no window at ⊥
  ever occurred, so that case is proof-only on my side too.

### C.3 Data, compared (DATA, not proof)
- Both referees: 0 failures. Random 𝒞^1O games give no n-state (h) window for either of us, so FREEZE, RATCHET, BLOCK and SUB (iii) rest
  on library instances (REFEREE) and on library plus climbs (me).
- Counts differ by N5 trace and selection, not by any statement:
  - REFEREE traces SPEC (n5.py-equal); I use my own N5 with arbitrary arena optima, 3 starts, and deterministic plus --rand.
  - FREEZE windows: REFEREE 142, me 302 (library); 125,028 in my climbs.
  - X-RUN runs: REFEREE 472, me 2,883 with H1 on P.
  - SUB re-entries: REFEREE 27, me 7 (library); 155 in my climbs.
- Joint thin spots, to be recorded with the result:
  - (i) BLOCK: my data has 0 S4a leaves inside any r = ℓ block, and 0 S4a leaves at (h) states after any freeze at ℓ ≥ 0, including
    three leave-aimed climbs. REFEREE reports "30 runs I, no re-entry after an S4a leave" without a leave count. I ask REFEREE (via the
    Lead) whether any S4a leave occurred in its 30 runs; if none, BLOCK is vacuous in all data.
  - (ii) No freeze at ℓ ∈ {−1, ⊥} in my data, so X-RUN's segment −1 and its post-F(⊥) part are proof-only. REFEREE's "no crossing after
    F(⊥)" does not say whether any post-F(⊥) transition existed.
  - (iii) The X-RUN bound is far from tight: max 55 crossings in P for both.

### C.4 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | FRZ-1 | N-FRZ-2 | wording, closed (fixes §1) | §3 B1: "(γ) P(π) = ∅, c′ even, the new path shorter: as (β)" (in the fixes file) |
| 2 | FRZ-2 | N-FRZ-3 | wording, closed (fixes §1) | §3 B-fallback B1: "if λ(x) = x, strict by the cycle node (rew(c′) > rew(x)); otherwise by (V2)" (in the fixes file) |
| 3 | FRZ-3 | G-FRZ-1 | proof gap in a consequence, closed (fixes §1); never observed | §6: "REL_Q ≤ d_o (C_P + 1); the transition leaving P can release exits; C_P + 1 ≤ 13(d_o + 1)n³" (in the fixes file) |
| 4 | — | N-FRZ-1 | citation, closed in R2 §2; REFEREE to accept or contest | §2 ARENA, R → R̄: "Ξ and W at v are π_v ⊕ θ and π_v ⊕ w. For a fixed base b with cycle node c, the order of π_z ⊕ b against π_{σy} ⊕ b depends only on (π_z Δ π_{σy}) ∩ V_{>c}, on |π_z| − |π_{σy}| and on c's parity, and θ, w share c (H3); so both frames order the edge alike" (replaces "(C7)") |
| 5 | — | N-FRZ-4 | wording | §0: "d_o := |succ(o)| (R30); a crossing transition changes R (R21); v leaves R at s → s+1 if v ∈ R_s and v ∉ R̄_{s+1}" |
| 6 | NL phase-key note | accepted here | citation transfer, closed (REFEREE §1) | §0 R29 (c): "NL is signed on the joint (λ_Ξ, λ_U, τ) phase; its proof uses no λ_U, so it holds on (λ_Ξ, τ) (REFEREE R-N5-FRZ §1)" |

### C.5 Joint label (D18/L40)
- PROVED (L-NEW successor 14; REFEREE and REFEREE-2, Opus 5.5, D15), on 𝒞^1O inside a (λ_Ξ, τ) phase, pending CHECKER:
  - NL-MF (row 6), Fact 0, ARENA (row 4);
  - P^c_ℓ (rows 1-2), FREEZE, RATCHET, BLOCK;
  - X-RUN (row 3; consequences as stated), SUB.
- Honest limits:
  - BLOCK is vacuous in my data (C.3 (i)).
  - X-RUN's segment −1 and post-F(⊥) parts were never exercised (C.3 (ii)).
  - X-RUN bounds crossings per fallback-free run with H1 on its SN prefix. It bounds neither f nor the number of runs per phase.
- FALSE (DATA, lane, not re-derived): FBF on (w, r)-subruns; CL1.
- OPEN: (L1), (L2), ¬H1 SN states, f per phase, G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE-2 successor 7 (Opus 5.5, D15).
