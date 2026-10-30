# N5-FBO (box 73): FBO-LIN is DEAD (cf_n24: 96 = 4n in one phase, ρ = 0). FBO is (vertex, fallback) pairs at gap level C, and R56 bounds it by ρ; plus N5-LZC's output correctness
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 05:40Z: «Next box, BOX 73: FBO … Aim at CONJECTURE FBO-LIN,
FBO_P ≤ n per phase, or a polynomial bound. Failing that, give the exact obstruction plus an instance.» Also asked: check N5-LZC's output
correctness (LZ-OPT keeps every SPEC step's premise). Written 06:00Z-06:20Z (date -u). Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- FBO, GXC, Z, phases, WCH^S4a_P: N5-LZ-box72.md §4-§5. L-SI's notation (Lead 05:49Z, l-si 7dd85b02): inside a W-run, GXC ⊆ TXC ⊆ ZXC.
  FBO events are at fallbacks, hence outside every W-run: FBO ∩ TXC = ∅.
- Tools in experiments/new/box73:
  - fbo.py: FBO anatomy (gap level before / after, the worst phase's fallbacks, ρ and the R56 bound);
  - climb_fbo.py: hill climb on max FBO per phase, using n5-epoch/climb.py's mutations;
  - run.sh: the 1132-run corpus, N5 and N5-LZC, written to fbo_*.txt;
  - out/*.log: climb logs.
- Instances (inst/, with .start):
  - cf_n24.pg: sha1 68c2b49d24672f9c5eb5dbc487d4fb60883a8018, start be6bff76…;
  - cf_n64.pg: b74bd3e8…;
  - cfz_n64.pg: 6deb5d8d… (climbed on N5-LZC).

## 1. DATA first
- Corpus (1132 runs, fbo_*.txt): FBO 239 on N5 and 242 on N5-LZC. The gap level never moves UP at an FBO event (0 in 1132 runs).
  | level move at the FBO event | N5 | N5-LZC |
  | --- | --- | --- |
  | SAME at level C, W's cycle node fixed | 151 | 155 |
  | SAME at level C, W's cycle node changes | 31 | 30 |
  | SAME below C (P or L level) | 21 | 21 |
  | DOWN (strictly less significant) | 36 | 36 |
  - Level C means Ξ(v) and W(v) have different cycle nodes.
  - nep22f_n64: all 46 events of its worst phase are SAME-C.
- Hill climbs (15 min each, seeds n5-epoch nep13_n24 / nep22f_n64):
  | instance | n | engine | max FBO per phase | ratio to n | per (v, phase) | worst phase: length, in-phase fallbacks, ρ | levels |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | cf_n24 | 24 | N5 | 96 | 4.0 | 9 | 11, 9, 0 (abs Q 3) | all SAME-C-fixed |
  | cf_n64 | 64 | N5 | 328 | 5.1 | 15 | 42, 17, 189 | SAME-C 262 + 66 |
  | cfz_n64 | 64 | N5-LZC | 313 | 4.9 | 13 | 34, 13, 102 | SAME-C 280 + 33 |
  - The climbs were still improving when stopped (log BEST lines).
  - cf_n24: FBO events per fallback of the worst phase are 18, 15, 15, 13, 11, 9, 7, 5, 3. Every fallback switches many gap vertices at
    once. On N5-LZC, cf_n24 gives 59 in one phase (7 fallbacks). The winners are SAME.

## 2. DEAD: CONJECTURE FBO-LIN
- FBO-LIN (FBO_P ≤ n per phase) is DEAD on N5 and on N5-LZC.
  - N5: experiments/new/box73/inst/cf_n24.pg + .start (sha1 68c2b49d…) has 96 FBO events in one phase, n = 24, ρ = 0, 9 in-phase fallbacks.
  - N5-LZC: cfz_n64 has 313 > 64.
- Exact obstruction:
  - FBO counts (vertex, fallback) pairs. One Even S4c fallback switches EVERY Even vertex with an improving edge ([S4c]).
  - In a saturated gap at the cycle level (Ξ's cycle node below W's, both fixed), each switched vertex is an FBO event. The W ceiling sits
    one coordinate above the climb and constrains nothing.
  - So FBO_P ≈ n_E × (in-phase fallbacks). The count is not a long chain at one vertex: per (v, phase) it is ≤ 15 in all data.

## 3. What does hold
- Lemma LEVEL-MON (PROVED, lane; N5 and N5-LZC). Inside a phase, between two consecutive strict W-rises of v, the gap level of v never
  becomes more significant.
  - Proof. [S1-ord] is lexicographic on the coordinate sequence (rew(c); P-bits from the top rank down, each with its parity's
    orientation; ±ℓ). In a phase, Ξ_t(v) only rises ([R15]), and W(v) only rises at a strict W-rise. So on such a stretch, x ⊴ x′ ⊴ y′ ⊴ y
    with x = Ξ_t(v), x′ = Ξ_{t′}(v), y′ = W_{t′}(v), y = W_t(v) (XW: Ξ ⊴ W).
  - In a lexicographic order every element of [x, y] carries the common prefix of x and y. So the first coordinate where x′ and y′ differ
    is at or below the one where x and y differ. □
  - DATA: UP 0 in 1132 + 1132 runs and on the climbed instances.
- Corollary DOWN-PAID (PROVED, lane). The FBO events at which v's level strictly drops (DOWN) number ≤ (n + 1)·(1 + WCH^S4a_P(v)) per
  (v, phase).
  - The level takes ≤ n + 2 values.
  - Inside a phase, W(v) rises only at S4a steps ([F1] at S4a, FB-W at fallbacks; P-N5-GAP §2.3), so the stretches between W-rises number
    ≤ 1 + WCH^S4a_P(v).
- Corollary FBO-R56 (PROVED, lane; N5 only; composition with landed RESULTS R56). FBO_P ≤ n_E·FB^in_P ≤ n_E·(1 + (n − 1)(2 + ρ_P)).
  - n_E := the number of Even vertices; FB^in_P := the in-phase fallbacks of P; ρ_P is R56's ρ.
  - Proof: each FBO event is a (switched vertex, in-phase fallback) pair; then [Q RESULTS R56] «in-phase fallbacks per phase are at most
    1 + (n − 1)(2 + ρ)».
  - DATA: cf_n24 96 ≤ 23·47 = 1081; cf_n64 328 ≤ 493394.
  - For N5-LZC this needs R56 for N5-LZC, which is NOT transferred (Lead ruling 05:40Z).
- The useful residue for GAP is per FALLBACK, not per vertex. ZF_P ≤ FBOF_P + NZ_P, with FBOF_P := the in-phase fallbacks that hold an FBO
  event, and FBOF_P ≤ FB^in_P. So GAP's Z-flat residue is again bounded by R56 in ρ. GAP-RED's ZF premise is implied by ρ-POLY (with R56).
- READING, the shared target. Collecting box 72 and box 73, for N5 per phase P (and per W-run F inside it):
  - SC*'s S part: SIL ≤ GXC at S4a ⊆ TIE (Lemma TIE; zero in N5-LZC);
  - GAP's ZF: ZF ≤ FB^in ≤ 1 + (n − 1)(2 + ρ) (R56);
  - GXC: GXC_P ≤ TIE_P + |Z_a| + WCH^S4a_P + n_E·(1 + (n − 1)(2 + ρ_P));
  - REP via TXC (TXC-RHO, box 72 §6): TXC_F(z) ≤ TIE_F + ρ_F + CYC_F.
  So the premises reduce to TIE (Even-side tie-breaks of S1), WCH^S4a (per vertex), ρ (Odd-choice Ξ-changes) and CYC. L-SI's
  TXC ≤ poly·(GXC + 1) is the wrong direction to expect: on wdepth_K4_m16 and latew_K20_m32, GXC = 0 and TXC = 184 / 3941, all Odd-sourced
  (box 72 §6). Since n is fixed there, this is not a refutation, only the direction of the charge: ρ, not GXC.

## 4. N5-LZC output correctness (Lead's ask; PROVED, lane, given what N5's own correctness rests on)
- What N5's correctness rests on: R15 (d) termination, «every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with
  ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them». On top of that, the output at S5 is read from a state with
  Iσ = Iτ = ∅ (R15 honest limit (iii), G-N5T-3: VJ00 Lemma 5.8 "1 ⇒ 2").
- N5-LZC keeps both premises:
  - (a) S4a's σ′ differs from σ_t only at Even v with σ′(v) = σ*(v) ≠ σ_t(v), and σ*(v) ∈ A(v) ∖ {σ_t(v)} = {w : (v, w) ∈ Iσ}. So σ′ =
    Switch_I(σ_t) with I := {(v, σ′ v) : σ′(v) ≠ σ_t(v)} ⊆ Iσ, which is unambiguous (one target per vertex). If σ′ = σ_t, no Even switch
    is made at S4a.
  - (b) If σ′ = σ_t and τ_new = τ, S4c fires exactly as in SPEC (S4c's own premise is "σ_new = σ and τ_new = τ"; N5-LZC evaluates it on
    σ′). If Iσ ≠ ∅ it switches Even; else Odd with Iτ (R15 (d) needs Iσ ∪ Iτ ≠ ∅ at a non-final state, which S5 guarantees).
  - So every N5-LZC iteration is of R15 (d)'s form. R15 (c)'s potential then gives termination, and no (σ, τ) state repeats.
  - (c) The stop rule and the output (S5) are unchanged: N5-LZC stops at a state with Iσ = Iτ = ∅ and outputs as N5 does. Its correctness
    is N5's (G-N5T-3, same premise).
  - (d) LZ-OPT (box 72 §3) is not needed for correctness. It is needed only for the SPEC reading "σ_new is Even's one-player optimum in
    H". That holds: σ′ has valuation W* = the optimum (LZ-OPT).
    It is also the premise that P-N5-GAP's FB-W proof uses, «S4c fires only if σ_new = σ_k, and S4a computed σ_new as the optimal strategy
    of H_k». In N5-LZC σ_new = σ′ is an optimum by LZ-OPT, so FB-W holds for N5-LZC (used by DOWN-PAID and GXC-CLOSE there).
- DATA: winners SAME on 1132 + the climbed instances (wincmp.py). This is data, as the Lead notes; the proof is (a)-(c).

## DONE / FINDINGS / NEEDS
- DONE: box73/fbo.py, climb_fbo.py, run.sh, fbo_*.txt (1132 × 2), out/ logs, inst/cf_n24, cf_n64, cfz_n64; this note; check.sh "box 73".
- FINDINGS:
  1. DEAD: CONJECTURE FBO-LIN. cf_n24 (sha1 68c2b49d…) has 96 = 4n FBO events in one phase with ρ = 0 and 9 in-phase fallbacks. N5-LZC:
     cfz_n64, 313 > n. Obstruction: FBO counts (vertex, fallback) pairs; one fallback switches up to n_E gap vertices at level C, where the
     W ceiling constrains nothing.
  2. PROVED (lane): LEVEL-MON (no UP; DATA 0) and DOWN-PAID (DOWN events ≤ (n + 1)(1 + WCH^S4a(v)) per (v, phase)).
  3. PROVED (lane): FBO-R56 (N5). FBO_P ≤ n_E(1 + (n − 1)(2 + ρ_P)), so FBO is polynomial under ρ-POLY. GAP's ZF ≤ FB^in ≤ R56's bound.
  4. READING: SC*'s S part, ZF, GXC and (via TXC-RHO) REP all reduce to TIE + WCH^S4a + ρ (+ CYC). ρ is the one Odd-side count left, and
     TIE is gone in N5-LZC.
  5. PROVED (lane): N5-LZC output correctness. It keeps R15 (d)'s premise and N5's stop / output rule.
- NEEDS: none from the owner. From the Lead: whether the next box goes to ρ (per phase, R56's ρ-POLY, or per W-run for REP), or to TIE for
  plain N5 (S1's tie-break), or to LZ-NOC.
