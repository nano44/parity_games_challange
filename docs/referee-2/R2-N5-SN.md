# R2-N5-SN: second-referee check of packet P-N5-SN (L-NEW box 33: absorptions, the c_w = c_θ prefix, who can leave R). REFEREE-2 (successor 6), 2026-10-25 03:50Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-SN (Lead 03:42Z), pinned at trunk claude/vibrant-johnson-nxvvxo 2c70ef6 (merged into my branch
as 5402cea1). Object: docs/new/P-N5-SN-box33.md, sha1 340d4f298d8ee137b53ff76d7dd81de49f8fa542 (checked at the pin and on my tree).
Background read: P-N5-Z §8 (R23 (g) WM, its proof), SPEC S1 (iv) / FIX 2 / FIX 4 and R24 (a), (b) (S4a's choice rule), P-N5-LP §3 (wakes),
my R2-N5-OE (U-loc, OE) and R2-N5-CLS (NL, CLS1, (C5)-(C7)).
Independence: I have not read docs/referee/ for this packet (no SN report is on my tree). I did not run or import sn.py, leave.py, orx.py,
orise2.py, scopecov.py, wakes.py or any REFEREE / L-RED probe. Lane instances are inputs only.
Tools (docs/referee-2/R2-N5-SN/, own code on R2-N5-LP/lp_check.py, R2-N5-FB/fb_check.py, R2-N5-CLS/cls_check.py): sn_check.py,
sn_climb.py, run_all.sh, totals.py, logs/, climb/. Every probe asserts exactly one Odd vertex with out-degree > 1.
Phase key: (λ_Ξ, τ) constant, the packet's own key.
Labels (D18 / L40): PROVED (L-NEW succ. 13) is the packet's label; §8 is CONDITIONAL; §9 is not to sign. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 WM phase-key transfer (the Lead's ask) | VALID | WM's proof (P-N5-Z §8) uses only τ_{k+1} = τ_k and the S4a optimum statewise (R18 Lemma S (c)); nothing of λ_U |
| §1 Lemma OR (a), (b), (c) | SIGN | (a) is OE's H1-case argument with "the path avoids o" as the assumption to refute; the ¬H1 branch of (c) is untested (0 ¬H1 ε-transitions in all data) |
| §2 TC-SPLIT | SIGN | — |
| §3 R-STICK | SIGN | — |
| §3 Corollary SN-PREFIX | SIGN | — |
| §4 Lemma H3H2 | SIGN | — |
| §5 Lemma LEAVE | SIGN | — |
| §6 Corollary ABS-COUNT | SIGN WITH GAPS | G-SN-1 (a): the counting proves ε_{H1} ≤ d_o + REL_run, not d_o − 1. "It ends ≤ d_o − 1" needs H1 at the run's last state, which the proof does not give (after an H1 ε-transition, σ̄(o) may enter R). Repaired below. (b): the per-phase form counts only ε-transitions inside fallback-free runs. ε-transitions at fallbacks are not covered (+ ≤ f). DATA: the packet's d_o − 1 form held everywhere, including climbs aimed at it |
| §7 Lemma WK | SIGN | N-SN-1: the step "z is then not fully optimal while a is available" needs y ⊕ to be strictly monotone; y lies on neither W-path (argument in §7). Vacuous in data: all 52 wakes change W at a or z |
| §8 ABS-L | SIGN as CONDITIONAL; the condition is now met | its premises (NL, CLS1's (A_j) chain) carry two signatures (P-N5-CLS, R29 landing). Vacuous in data: 583 intervals, 0 θ-changes above L |
| §9 | not signed (as briefed) | — |
No statement is NOT SIGNED. No counterexample.

## 0. The WM transfer (the Lead's first ask)
- R23 (g) Lemma WM is signed under the key (λ_Ξ, λ_U, τ). Its proof (docs/si/P-N5-Z-box5.md §8) has three lines:
  - τ_{k+1} = τ_k (phase);
  - σ_{k+1} maximises V_{·, τ_k} pointwise over the arena (R18 (d) Lemma S (c), a statewise fact about S4a's result);
  - σ_k lies in the arena, and its valuation there is W_k.
- Nothing uses λ_U, or even λ_Ξ. The statement holds at every non-fallback transition with τ_{k+1} = τ_k, so on the packet's (λ_Ξ, τ)
  phase. VALID.
- The packet's other transfers (Lemma G, XW, CAP-1 statewise; U-loc, OE on (λ_Ξ, τ) by R28) are right.
- Data: W never dropped at any S4a step of my runs. The checker's R-STICK and LEAVE checks depend on it, with 0 failures.

## 1. Lemma OR: SIGN
- (a) Suppose x0's H_{k+1}-path to c avoids o.
  - Every relevant change on it is Even, of level ≤ E_k. U-loc (R28) freezes COARSE_{E_k}(Ξ(x0)). It also freezes COARSE_{E_k}(Ξ(x1)),
    because x1's path avoids o (functional graph).
  - CAP-1 at k and at k+1 then gives a strict order that persists, which is impossible. This is R2-N5-OE §2 step 3 with "x0's path avoids
    o" as the assumption to refute; it needs no H1. ✓
  - Visiting o puts x0 in R_{k+1}. The (σ_{k+1}, τ)-play agrees with the H_{k+1}-play up to o. ✓
- (b) Under H1, x0's honest play is the tail of o's and never visits o. So x0 ∈ F_k. ✓
- (c) The top difference of Ξ_k(x0) vs Ξ_{k+1}(x1) is above E_k. Since COARSE_{E_k}(Ξ(x1)) is frozen, it equals the one of Ξ_k(x0) vs Ξ_k(x1):
  level ℓ, Ξ(x1) higher.
  - (C7) with π = (o): o is on neither path. For x1 this holds by functionality. For x0, under H1 by (b); under ¬H1, x0 lies on o's
    honest cycle after o and reaches c before o.
  - c ≠ o. ✓
- Mechanical: 725 ε-transitions in the library and 65,833 H1 ε-transitions in climbs. (a), (b), (c) failed 0 times.
  - Every ε-transition seen has H1 at k, so the ¬H1 branch of (c) rests on the proof alone.
  - 0 ε-transitions at fallbacks.

## 2. TC-SPLIT: SIGN
- λ(o) = o makes θ constant. (C7) reduces lev(θ_k, θ_{k+1}) to lev(Ξ_k x0, Ξ_{k+1} x1); both paths avoid o.
- U-loc on x1's path gives ≤ E_k between its two values. Then (C6). The ε case is §1 (c). ✓
- Note: if x0 ≠ x1 with a level-⊥ tie (R28 row 1), O_k = ⊥ and the bound is ≤ E_k. Fine.
- 3,136 θ-changes in the library, 0 failures.

## 3. R-STICK and SN-PREFIX: SIGN (the Lead's second ask, part 1)
- For v ∈ R_k: both plays follow v's (σ_k, τ)-play to o, then o's own play. So λ(v) = c_θ and v's W-cycle node is c_w(k). ✓
- R-STICK.
  - A leaver v ends in F_{s+1}, where Ξ = W (R19 (a)). So its W-cycle node at s+1 is λ(v) = c.
  - WM gives rew(c) > rew(c′); XW at s gives rew(c) < rew(c′). Rewards are injective on cycle nodes (si.py l. 42-44, p′ = 2·rank + parity).
  - So no such leaver exists. ✓
- SN-PREFIX.
  - rew(c_w) is non-decreasing along a fallback-free run (WM at o) and ≥ rew(c_θ) (XW at o), with equality iff c_w = c_θ. So the states
    with c_w = c_θ are a prefix.
  - After the prefix, R-STICK applies at every step, so R only grows: ≤ n − 1 crossings, since R ∋ o.
  - The transition from the last prefix state is counted in X_SN.
  - Per phase: ≤ f + 1 runs, f fallback crossings, X_SN, and ≤ n − 1 after each prefix. ✓
- Mechanical:
  - Library: R-STICK 29,113 checks; 1,271 runs; 5,130 crossings in prefixes vs 212 after (max 13 per run).
  - Climbs (FIT=stick from jcl_zcl_cu_n48 and a random seed; also as a side count in the other climbs): R-STICK 867,072 checks, 39,461
    crossings after a prefix.
  - 0 failures of the prefix property, of "no R loss after", of the ≤ n − 1 bound and of the per-phase bound.
  - Teeth: leaves inside prefixes are common (1,857 S4a leaves in the library), so the hypothesis c_w ≠ c_θ is what matters.

## 4. H3H2: SIGN
- Under H1, c_θ's honest cycle avoids o, so it lies in F: its vertices' plays equal their honest plays.
- Under H3, o's W-play ends on the W-cycle containing c_θ, which is that same honest cycle (c_θ ∈ F, functional graph). So o is not on its
  W-cycle: H2. ✓
- 13,598 states, 0 failures.

## 5. LEAVE: SIGN (the Lead's second ask, part 2)
- R-STICK forces c_w(s) = c_θ (H3); with H1 and H3H2 this gives (h).
- Lemma G (b) and (C7): lev(Ξ_s q, W_s q) = r_s, strict by XW.
- q ∈ F_{s+1}: W_{s+1}(q) = Ξ_{s+1}(q). WM gives Ξ_s(q) ◁ W_s(q) ⊴ Ξ_{s+1}(q), and (C5) gives lev(Ξ_s q, Ξ_{s+1} q) ≥ r_s.
- U-loc with L = r_s − 1 (⊥ for r_s = −1) on q's H_{s+1}-path, which avoids o, then forces a relevant change of level ≥ r_s on it. ✓
- r_s = ⊥: vacuous, as the packet says.
- Mechanical:
  - Library: 1,853 H1 leaves, all with (h); the path-max relevant level ≥ r_s; L_s ≥ r_s. The bound is attained (path max = r_s) 105 times.
  - Climbs (FIT=leave from exitr_cex_n48, and side counts): 23,798 H1 leaves, 14,438 tight.
  - 0 failures. Only 4 library leaves had ¬H1 at s, outside the lemma.

## 6. ABS-COUNT: SIGN WITH GAPS (G-SN-1)
- What the proof shows. Let N := #exits of o in R.
  - Under H1, σ̄(o) ∈ F, so N ≤ d_o − 1 at every H1 state.
  - Each H1 ε-transition moves x0 from F to R (OR (a), (b)), so N rises by ≥ 1 minus the leaves at that transition.
  - N falls only by leaves (REL_run).
  So ε_{H1} ≤ N_end − N_start + REL_run ≤ N_end + REL_run.
- G-SN-1 (a). "It ends ≤ d_o − 1" holds only if the run's LAST state has H1 (or some exit in F).
  - After an H1 ε-transition, x1 = σ̄_{k+1}(o) can lie in R_{k+1}: ¬H1 at k+1, o on its new honest cycle through x1. Then N can reach d_o.
  - Counting up to the last H1 ε-transition k* does no better: N_{k*} ≤ d_o − 1 covers the ε_{H1} − 1 earlier ones, which again gives
    ε_{H1} ≤ d_o + REL_run.
  - So the proved per-run bound is ε_{H1} ≤ d_o + REL_run. It improves to d_o − 1 + REL_run when the run's last state has H1.
  - The scenario that would exceed d_o − 1 is not excluded by the text. d_o = 2, REL_run = 0, two H1 ε-transitions: e1 absorbed, then
    e2 absorbed while e1 stays in R, ending ¬H1. I found no instance.
- G-SN-1 (b). The per-phase line sums the runs. An ε-transition AT a fallback lies in no run and is not counted.
  - The per-phase form needs "+ #H1 ε-transitions at fallbacks (≤ f)", or an argument that there are none.
  - DATA: 0 such transitions in every sample.
- Repaired statement (proved): per fallback-free run ε_{H1} ≤ d_o + REL_run (≤ d_o − 1 + REL_run if its last state has H1); per phase
  ε_{H1} ≤ d_o(f + 1) + f + REL. The "every such leave" sentence is right (R-STICK, LEAVE).
- DATA (status of the packet's form, CONJECTURE):
  - max over runs of ε_{H1} − REL_run − (d_o − 1) is 0 everywhere: library 1,271 runs, random 5,500 games.
  - Three climbs aimed at it (FIT=absc, from two random d_o = 2 / 3 seeds and from exitr_cex_n48): 30,400 runs, best excess 0.
  - The d_o − 1 form may be true; the proof given does not show it.

## 7. Lemma WK: SIGN (N-SN-1)
- Mode.
  - S4a works on the dual. For y with W-cycle node c_w odd in G, the dual cycle node is even, so the longest-path rule applies, with the
    first strict maximum = smallest index (FIX 4).
  - By R24 (a) Lemma R, the candidates are exactly the fully optimal arena successors. So in the odd mode the choice is the smallest-index
    fully optimal successor.
  - My CHOICE check confirms this rule at 14,186 odd-mode S4a choices (y not its own W-cycle node), 0 failures.
- The mode is the same at k′ and k′+1: a, z ∈ R (WAKE), R constant, so both W-cycle nodes are c_w; and W(z) is unchanged.
- The case split.
  - At k′ (the result of k′ − 1 → k′), a is the minimum fully optimal successor. So either a < z with both fully optimal, or z is not
    fully optimal.
  - In the latter case Bellman at the arena optimum gives y ⊕ W(z) ⊴ W(y) = y ⊕ W(a).
  - At k′+1 the values at a and z are unchanged. In the first case a stays fully optimal and a < z. In the second, z cannot become fully
    optimal while a is available.
- N-SN-1. The second case needs y ⊕ to be strictly monotone between W(z) and W(a). This is the TB-1 (b) trap: it fails if y ∈ P of exactly
  one of them. It holds here:
  - y ∈ R_{k′} = R_{k′+1}, so y's play reaches o. At k′+1, σ(y) = z, so z's play cannot pass y before o; otherwise y → z → … → y would
    be an o-free cycle.
  - After o, y can lie only on o's W-cycle (¬H2), where every vertex has rank < c_w, so it is in no P.
  - The same holds for a at k′. If z's k′-play passed y with rank y > rank c_w, then y ∈ P(W_{k′}(z)) but y ∉ P(W_{k′+1}(z)), against the
    hypothesis W_{k′+1}(z) = W_{k′}(z).
  - One sentence in the fixes file.
- DATA: 52 wakes (kchain4 / 10 / 32: 3 / 15 / 31 in my 3-start runs; nowake_cex_n32 1; so_k2_n32 2), all with a W-change at a or z.
  WK's hypothesis is never met, so the lemma is vacuous in data. It rests on the proof and on the choice-rule check.

## 8. ABS-L: SIGN as CONDITIONAL (condition now met)
- The proof is correct given NL (i), (ii) and CLS1's (A_j) chain on [k0+1, k].
  - (h) at j and j+1 (both in S). The no-change case is frozen by NL (i).
  - In the x0 ∉ R_{j+1} case, CAP-1 at both ends caps the level at L by (C6) and (C7).
  - So x0 ∈ F_j ∩ R_{j+1}, and NL (ii) keeps it in R up to k.
  - The count is ≤ d_o − 1 because the end state k has H1 (σ̄_k(o) ∈ F). That is the point G-SN-1 lacks.
- NL and CLS1 are now signed by both referees (R2-N5-CLS, R-N5-CLS; R29 landing). So the condition is met once R29 lands.
- DATA: 583 intervals with r_j > L, and 0 θ-changes above L in any of them. Vacuous.

## 9. Data (DATA, not proof)
| batch | runs | key counts | violations |
| --- | --- | --- | --- |
| library (245 files: every experiments/**/*.pg in 𝒞^1O with n ≤ 64, plus box33/instances and red/so/instances), 3 starts | 735 | 830 phases, 12,863 transitions; ε 725 (all H1); θ-changes 3,136; S4a leaves 1,857 (1,853 H1); R-STICK 29,113; runs 1,271; CHOICE 14,186; H3H2 13,598 states | 0 |
| random 𝒞^1O n 6-16 / 16-32 (seeds 9101, 9102) | 5,500 | 1,628 runs, 537 H1 leaves, 3 ε | 0 |
| climbs (FIT=absc ×3, leave, stick ×2) | 47,200 | ε_H1 65,833; H1 leaves 23,798; R-STICK 867,072; crossings after prefix 39,461 | 0 |
- ABS-COUNT, packet form: 0 runs above it in all data, climbs included (status: CONJECTURE after G-SN-1).
- Thin spots:
  - No ¬H1 ε-transition anywhere (OR (c)'s ¬H1 branch).
  - WK and ABS-L are vacuous.
  - The kchain instances (n up to 366) are included; they exercise wakes but not WK.

## Signature
REFEREE-2 (successor 6), Opus 5.5 (D15), 2026-10-25:
- SIGN: Lemma OR, TC-SPLIT, R-STICK, Corollary SN-PREFIX, Lemma H3H2, Lemma LEAVE, Lemma WK (note N-SN-1).
- SIGN WITH GAPS: Corollary ABS-COUNT (G-SN-1 (a), (b); repaired form proved: per run ≤ d_o + REL_run, per phase ≤ d_o(f + 1) + f + REL;
  the packet's d_o − 1 form is CONJECTURE, unrefuted).
- SIGN as CONDITIONAL, condition met on R29: ABS-L.
- VALID: the WM phase-key transfer.
After two signatures (D18/L40) these become PROVED (L-NEW successor 13; REFEREE-2, and REFEREE if it signs). OPEN: REL per phase; the
fallback ↔ absorption loop; G-N5-TIME.

## §A. Addendum: L-RED probes (Lead 03:52Z, read after my report was pushed). Written 2026-10-25 03:56Z by date -u
- Inputs: experiments/red/so/instances/epsseg_cex_n48.pg (sha1 b4c7dcb0, o = 0, d_o 17) and exitr_cex_n16.pg (sha1 6971211e), both on
  trunk (merged as babc0164). I ran my sn_check.py with 3 starts each: 0 violations of every check in both files.
- epsseg_cex_n48, S3 start: n5 26 iterations / 1 fallback. The phase [7, 25) has f = 0, one fallback-free run, and 17 H1 ε-transitions
  (at 7, 9-24). Exit 33 leaves R at the S4a step 8 → 9 (REL_run = 1) and is re-absorbed later.
  - The packet's form (d_o − 1) + REL_run = 16 + 1 = 17 holds with EQUALITY. The REL term is needed.
  - N (#exits in R) at the run's states: 0, 1, 0, 1, 2, …, 16. The run ends at state 25 with H1 and N = 16 = d_o − 1, so the packet's
    "ends ≤ d_o − 1" is true here.
  - At state 26 all 17 exits are in R and H1 fails (σ̄(o) = 34 ∈ R). But 25 → 26 leaves the phase (λ changes), so it is no transition
    of the run.
  - This is exactly G-SN-1 (a)'s mechanism (after an H1 ε-transition σ̄(o) enters R and N reaches d_o), here at a phase exit. Inside a
    phase I still have no instance.
- exitr_cex_n16: packet form holds (max excess −1); 13 H1 ε-transitions, 6 H1 leaves, all as LEAVE states.
- Verdicts unchanged. G-SN-1 (a) stays a proof gap: the statement is unrefuted and tight on epsseg_cex_n48. A repair would show that, inside
  a phase, the state after an H1 ε-transition again has an exit in F (or H1). The mechanism seen at 25 → 26 needs the phase to end there.
