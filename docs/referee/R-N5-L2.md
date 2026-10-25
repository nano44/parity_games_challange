# R-N5-L2: REFEREE report on packet P-N5-L2 (box 34: H3-CONST, H2-STICK, G′, FREEZE′, R-CONST, H1-INT, X-RUN′)
Referee: REFEREE (successor 7, session_01TWT1diK1Z9x2eK56iBVbZu), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-L2: the Lead's
brief of 2026-10-25 08:07Z and GO of 08:20Z (Lead's stamps). Object docs/new/P-N5-L2-box34.md at pinned trunk 04b3f48, sha1
cbea07392521bcdfbce137ba361bb581f9df11d7 (checked: `git show 04b3f48:docs/new/P-N5-L2-box34.md | sha1sum`, 187 lines; the same on trunk
5071ce71). Author L-NEW successor 14. Written 2026-10-25 08:30Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/ not read for this packet. Not reviewed (Lead 08:20Z): L-NEW successor 15's TOGGLE (docs/new/N5-DROP-box35.md).
Premise for §4 and §7: P-N5-FRZ (docs/new/P-N5-FRZ-box34.md, sha1 39df373c…, fixes sha1 168de464…), signed by my lane in
docs/referee/R-N5-FRZ.md (referee 3a520ce7) with its Addendum (3171efc7: FRZ-1..3 closed). I re-read that report and the FRZ text as my own
lane's prior work; REFEREE-2's R2-N5-FRZ does not exist yet, so FREEZE′ and X-RUN′ can land only after P-N5-FRZ has both signatures.

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Lemma H3-CONST | PROVED (L-NEW succ. 14) | SIGNED |
| §2 Lemma H2-STICK (+ Corollary) | PROVED | SIGNED WITH GAP L2-1 (wording: the case τ(o) = o, where "τ(o) ∈ R_s" is false because R excludes o; the claim is trivial there; 400 of the 520 library cases are this case). Closed |
| §3 Lemma G′ | PROVED | SIGNED |
| §4 Theorem FREEZE′ | PROVED (rests on P-N5-FRZ §3, FRZ-1, FRZ-2) | SIGNED (premise P-N5-FRZ: REFEREE signed, REFEREE-2 pending). DATA thin: no n-state H3 window containing a ¬H1 state and no H3 ∧ ¬H2 state after a window was found anywhere (library, random, climbs); the new case of Lemma P^c_ℓ is tested directly on short windows (§4.3) |
| §5 Lemma R-CONST | PROVED | SIGNED |
| §6 Lemma H1-INT | PROVED | SIGNED WITH GAP L2-2 (wording: in (b), "every state k with H1 at k and ¬H1 at k+1" holds only for a transition k → k+1 INSIDE the phase, which is what R30 (f) gives; read literally with k+1 outside the phase it is FALSE: docs/referee/R-N5-L2/exitdrop_n3.pg). Closed by that reading |
| §7 Theorem X-RUN′ | PROVED (rests on P-N5-FRZ §6, FRZ-3) | SIGNED (premise P-N5-FRZ: REFEREE signed, REFEREE-2 pending) |
| §8 ONE-H FALSE, ONE-DROP FALSE, DROP-LEN OPEN, open list | not to sign | not signed. oneh_cex_n32 and onedrop_cex_n32 re-run with my own trace and Oink. FINDING: DROP-LEN and its weaker per-run form are FALSE (docs/referee/R-N5-L2/droplen_cex_n12.pg: two drops in one fallback-free run, θ constant; §8) |

Fixes-file lines (one per gap):
- L2-1 (§2 H2-STICK, wording): add "If τ(o) = o, ¬H2 holds at every state with this τ, in particular at s+1; assume τ(o) ≠ o below." before "¬H2 at s: τ(o) ∈ R_s".
- L2-2 (§6 H1-INT (b), wording): replace "every state k with H1 at k and ¬H1 at k+1" by "every state k such that k → k+1 is a transition of the phase with H1 at k and ¬H1 at k+1".

## 0. Setting, citations, tools
- Setting as in P-N5-FRZ §0: 𝒞^1O, phase = λ_Ξ and τ constant, R_k excludes o, R̄_k = R_k ∪ {o}. Every citation was checked for the
  setting it was signed in:
  - R19 (a) "off R̄, Ξ = W" is statewise (a play avoiding o is the same in both graphs).
  - R21 (a) XW is statewise.
  - R15 (a) holds at every transition.
  - R23 (g) WM transfers to the (λ_Ξ, τ) phase (R30 (c) note, both referees).
  - R30 (c) R-STICK, SN-PREFIX, (d) H3H2 and (f) H1-DROP were signed on the (λ_Ξ, τ) phase.
  - SN-PREFIX has no H1 hypothesis (RESULTS R30 (c)), which §7's "no hypothesis on H1" needs.
- One citation is of a step inside a signed proof, not of a signed statement:
  - §2 and §0 use "under H1, c_θ ∈ F" from R30 (d)'s proof. The step holds; my one-line proof: under H1, o's honest cycle avoids o.
    Its vertices' honest plays never visit o, so their (σ, τ)-plays coincide with them and never reach o. So the cycle, c_θ included,
    lies in F.
  - FRZ Fact 0 (signed by me) states it only under (h), so it does not cover this use.
  So this is a citation note, not a gap.
- Tools (docs/referee/scratch/, own code, run with `python3 -I`). Every game is asserted to be in 𝒞^1O (exactly one Odd vertex with
  out-degree > 1) before use. N5 comes from my own trace (u1_probe.trace = the n5.py loop, asserted equal to n5.run's iteration and
  fallback counts). No lane script is imported; lane instances are inputs only.
  - l2_probe.py: every check named per section below.
  - l2_pc.py: Lemma P^c_ℓ on H3 windows by enumerating simple paths. Negative control NEG=1 (drop "λ(u) = u") gives 44,018 failures on
    2,000 random games, so the check can fail.
  - l2_exitdrop.py: phase-exit drops, for L2-2.
  - l2_climb.py: climbs FIT=frz | tog | h2s.
  - l2_oink.py: compares N5's final regions with Oink `--zlk -v` at 8fbf0a7.
- "Library" = every experiments/**/*.pg in 𝒞^1O with n ≤ 64 at referee head 3e86cb10: 258 files.

## 1. Lemma H3-CONST (SIGNED)
- Under H2, τ(o) ∈ F, and F is closed under (σ, τ)-successors (a vertex whose play avoids o has successors whose plays avoid o).
  - So o's W-play is o followed by τ(o)'s play inside F, and its cycle avoids o.
  - On F, W = Ξ (R19 (a), statewise), so the cycle node of W(τ(o)) is λ(τ(o)), and c_w = λ(τ(o)).
- λ and τ are phase constants, so "H3 at an H2 state" is the single condition λ(τ(o)) = c_θ for the whole phase. The two consequences
  follow. Correct.
- DATA (l2_probe H3C):
  - Library: 5,886 H2 states, 319 phases, 0 failures (c_w = λ(τ(o)), all-or-none per phase, (h) ⟺ H1 ∧ H2 in phases with an (h) state).
  - Random: see §9.

## 2. Lemma H2-STICK and Corollary (SIGNED WITH GAP L2-1)
- For τ(o) ≠ o:
  - τ(o) ∈ R_s, and its W-play enters o's W-cycle, so its W-cycle node is c_w(s) ∈ R̄_s (every vertex of a cycle through o reaches o).
  - Its honest play agrees with its (σ_s, τ)-play up to o and then follows o's honest play, so λ(τ(o)) = c_θ.
  - Under H1, c_θ ∈ F_s (§0).
  - So the two cycle nodes differ, and R-STICK (R30 (c), S4a transition of the phase) keeps τ(o) in R_{s+1}. With τ unchanged, o lies
    on a W-cycle at s+1. Correct.
- L2-1 (wording):
  - If τ(o) = o, then "τ(o) ∈ R_s" is false (R excludes o), and R-STICK says nothing about o.
  - The claim is trivial there: o's W-play is its self-loop at every state with this τ, so ¬H2 holds at s+1.
  - This is not a corner case: 400 of the 520 library S4a steps with H1 ∧ ¬H2 have τ(o) = o.
- Corollary:
  - In a fallback-free run of a phase, every transition is an in-phase S4a step. With H1 at every state, ¬H2 propagates forward, so the
    H2 states form a prefix.
  - With an (h) state in the phase, §1 gives (h) ⟺ H2 on such a run.
  - Correct.
- "Of a phase" is needed:
  - In 5,000 random games, 228 S4a steps with H1 ∧ ¬H2 leave the phase, and 115 of them regain H2 (l2_exitdrop.py; there τ changes in
    the same iteration).
  - The lemma states the in-phase hypothesis, so this is no gap.
- DATA (H2S): library 520 steps (400 with τ(o) = o), 0 failures. Climb FIT=h2s (§9) found games with up to 8 non-self-loop cases each, 0
  failures.

## 3. Lemma G′ (SIGNED)
- (a):
  - ¬H1: o lies on its honest cycle, whose top is λ(o) = c.
  - A vertex y ≠ o of that cycle follows the cycle in the (σ, τ)-graph until o (the graphs differ only at o), so y ∈ R_k. Hence c ∈ R̄_k.
  - H2 would put c_w in F_k. Correct.
- (b), c-first v:
  - Both plays coincide up to the first o, and c comes earlier.
  - λ(v) = c (the honest play reaches o, then o's honest cycle), and the W-cycle node is c_w = c.
  - VJ00's value is read off the prefix up to the first visit of the cycle node, which the two plays share. So Ξ(v) = W(v). Correct.
- (b), o-first v:
  - Every vertex x of π_v lies in R̄_k, so λ(x) = c (R-CONST's ⊆ argument), and its W-cycle node is c too.
  - x ≠ c, because π_v reaches o before c. So (V1) applies at every x in both frames, and the honest and (σ, τ)-successors agree off o.
  - Disjointness:
    - o's honest path o → σ̄(o) ⇝ c runs along the honest cycle and avoids o after its start.
    - o's W-path o → τ(o) ⇝ c runs along o's W-cycle (¬H2) and reaches the top c before returning to o.
    - Every vertex y ≠ o of either path has a (σ, τ)-play that reaches c without visiting o. If π_v met such a y, or c, then v would be
      c-first.
  - Correct.
- (c): F: equality. c-first: (b). o-first: (C7) with (b)'s disjointness, giving lev = r_k. The remark c = o is correct (θ = w = (o, ∅, 0)).
- DATA (GP):
  - Library: 373 H3 ∧ ¬H1 states; 4,319 c-first and 3,144 o-first vertices; 101 states with c = o.
  - All of (a), the two frame identities (o-first values recomputed as π ⊕ θ and π ⊕ w with si.py's extend), disjointness, and
    lev ≤ r: 0 failures.
  - Random: §9.

## 4. Theorem FREEZE′ (SIGNED; premise P-N5-FRZ)
### 4.1 Each use of (h) and H2 in P-N5-FRZ §3, checked against the H3-only window
- Step 1:
  - With H1, H3 ⇒ (h) (R30 (d)), so FRZ Step 1 applies.
  - Without H1, G′ (c) gives lev(Ξ v, W v) ≤ r_k ≤ ℓ for every v, then (C2).
  - Correct.
- Fact 0 at H3 states, the two uses:
  - (i) the W-cycle node of every v is λ(v). On F this holds because W = Ξ. On R̄, the W-cycle node is c_w = c_θ (H3), and λ(v) = c_θ
    (R-CONST ⊆).
  - (ii) an honest cycle node u has W(u) = (u, ∅, 0). Either u ∈ F, where W = Ξ; or u ∈ R̄, where u = λ(u) = c_θ = c_w is the top of
    o's W-cycle and lies on it.
  - FRZ's third Fact 0 item, c_θ ∈ F, is FALSE under ¬H1 (G′ (a)). So I checked where P^c_ℓ and FREEZE use it: nowhere.
    - The base case needs only (ii).
    - A1 needs (i) at k.
    - A2, B1 (α), B2 need (i)/(ii) at k+1.
    - FRZ-1 (γ) concludes as (β). FRZ-2's λ(x) = x branch needs (ii) at k.
    - "c_θ ∈ F" is used in FRZ §5 BLOCK and §6 X-RUN, which FREEZE′ does not extend.
- Step 2: WM at S4a steps (no (h)); Step 1 at both ends plus R15 (a) at a fallback. Correct.
- Rest of P^c_ℓ:
  - (F1) in the arena (S4a's σ_{k+1} is an optimum of the arena game against τ: a property of the algorithm, no (h)).
  - FBL step 1 at a fallback (a fallback happens exactly when S4a returned σ_k and S4c returned τ: algorithmic).
  - (C1)-(C7), (V1), (V2c).
  - Nothing else. Correct.
- Step 3 at an H3 state t:
  - W-plays through o end at c_w = c_θ, an honest cycle node. W-plays inside F end at λ(x), which is a cycle node of a cycle inside F
    with W = Ξ there.
  - So W_t(x) is the value of a simple G_τ path of ≤ n − 1 edges to an honest cycle node (λ is a phase constant), and P^c_ℓ at
    j = n − 1 applies. Correct.
- Step 4 and the case "t without H2 or H3, t2 ≥ t with H2 or H3": R15 (a), XW, Step 3, Step 1 at F; (C3). Correct.
### 4.2 DATA on FREEZE′ itself (l2_probe FRZ)
- Library:
  - 144 windows (n consecutive H3 states with r ≤ ℓ, per level ℓ, with a later H2-or-H3 state); 2,960 later-state checks; Steps 1-2 on
    62,147 window states; 0 failures.
  - None of the windows contains a ¬H1 state, and no checked state t is H3 ∧ ¬H2. So the data covers only FRZ's original statement.
- Random: no window at all (§9).
- Climbs FIT=frz:
  - From random games at n 3-8: best fitness −1, i.e. H3 runs of n − 1 states with a ¬H1 H3 state in the same phase, never n.
  - From the library seeds thclimb_n12_s11, fts_best16, j5_n16: §9.
  - The new content of FREEZE′ (windows through ¬H1 states, conclusion (b) at H3 ∧ ¬H2 states) is UNEXERCISED by any game I have.
- Statewise ingredients that are exercised: Fact 0 (i)/(ii) at every H3 state (5,828 library states, 0 failures) and Step 3's
  "every W-cycle node u at an H3 state has λ(u) = u" (l2_pc STEP3).
### 4.3 DATA on the new case of Lemma P^c_ℓ (l2_pc.py)
- Setting: every maximal run of consecutive H3 states with r ≤ ℓ that contains a ¬H1 state, every j ≤ N, every x, and every simple G_τ
  path ρ from x with ≤ j edges to an honest cycle node.
- Check: COARSE_ℓ(W_{k0+j}(x)) ⪰ COARSE_ℓ(value ρ).
- Library (n ≤ 14): 491 windows, 2,097 checks. Random (40,000 games, n 4-9): 267,221 windows, 641,105 checks. 0 failures.
- Windows are short (N ≤ 3).

## 5. Lemma R-CONST (SIGNED)
- ⊆: v's honest play agrees with its (σ, τ)-play up to o and then follows o's honest play, so λ(v) = c_θ. This holds without any
  hypothesis on H1.
- ⊇:
  - Under ¬H1, c_θ lies on o's honest cycle.
  - In the functional graph H_k the cycle through c_θ is unique, so v's honest play with λ(v) = c_θ ends on o's cycle and visits o.
  - Up to that visit it is the (σ, τ)-play.
  - Correct.
- U is a phase constant (λ_Ξ, c_θ), so R is constant across any in-phase transition between ¬H1 states: no crossing.
- DATA (RC):
  - Library: 790 ¬H1 states, R̄ = λ^{-1}(c_θ) at all of them; 442 in-phase ¬H1 → ¬H1 transitions, none a crossing; 0 failures.
  - Random: §9.

## 6. Lemma H1-INT (SIGNED WITH GAP L2-2)
- (a):
  - θ is non-decreasing (R15 (a)) with a fixed cycle node.
  - VJ00's set order "top of P Δ P′" equals the order of the signed weight Σ_{x∈P} ±2^{rank x} (+ for even, − for odd ranks): the top
    of the symmetric difference dominates the difference of the sums.
  - That weight is injective with weight(∅) = 0, so the sandwich forces P(θ_k) = ∅. Correct.
- (b):
  - At ¬H1, θ's path runs along o's honest cycle to its top, so P(θ) = ∅.
  - Pre-drop states: R30 (f) H1-DROP, which is signed for k → k+1 INSIDE a phase. Correct for that reading.
- L2-2:
  - The statement says only "In a phase: … every state k with H1 at k and ¬H1 at k+1". If k is the last state of its phase and k+1
    starts the next phase, the claim is false.
  - Witness docs/referee/R-N5-L2/exitdrop_n3.pg (sha1 73c7a21b07e37c504bfdc8922fde9456deb5195e; n 3, o = 0; N5 1 iteration, 0 fallbacks;
    Oink zlk verified, regions agree).
  - State 0 forms a phase of one state with H1 and θ = (1, {2}, 1), so P(θ_0) ≠ ∅ and I_∅ = ∅. State 1 has ¬H1 and θ = (0, ∅, 0); λ has
    changed.
  - DATA: 43 of 83 phase-exit drops in the library (for example b5_os_n32.pg at 67, so_th_n32.pg at 34) and 198 of 278 in 5,000 random
    games have P(θ_k) ≠ ∅ (l2_exitdrop.py). The proof's citation already carries the in-phase reading, so the repair is the
    fixes-file line above.
- (c): on I_∅ the order is the length order by the parity of c_θ, and lengths of simple paths are in [0, n − 1]. Correct.
- DATA (HI):
  - Library: 149 phases with I_∅ ≠ ∅; (a), (b) (in-phase drops: 7), (c) with at most 3 length changes per phase; 0 failures.
  - Random: §9.

## 7. Theorem X-RUN′ (SIGNED; premise P-N5-FRZ)
- (a), splitting:
  - P's states all have H3 (definition of the SN prefix).
  - The maximal H1 runs and ¬H1 runs of P number t_Q + 1 in total, joined by the t_Q toggle transitions.
  - Inside a ¬H1 run there is no crossing (§5).
- (a), each H1 run P_i:
  - P_i is a run of consecutive (h) states (R30 (d)) of a fallback-free run. I re-read P-N5-FRZ §6 for every place its proof uses
    "P is the SN prefix of Q".
    - Windows and F(ℓ) are defined inside the set.
    - FREEZE is applied with F in the set, and with H2 states ≥ t inside it.
    - RATCHET (c)'s ≤ 2d_o + 1 runs: the pair is monotone along T, so a consecutive subset of T has at most as many runs.
    - BLOCK needs consecutive (h) states ≥ F with S4a transitions.
    - The level −1 and "after F(⊥)" arguments use (h) at both ends of each transition inside the set.
  - None of these uses the start of Q or the SN property. So FRZ's bound 13 (d_o + 1) n³ applies to the crossing transitions with
    both ends in P_i.
- (a), sum: ≤ (t_Q + 1)·13 (d_o + 1) n³ plus the t_Q toggle transitions. Correct.
- (b):
  - A release is an exit leaving R, so it happens at a crossing transition and releases ≤ d_o exits.
  - R-STICK (R30 (c)) puts every leave of Q at a transition with both ends in P, or at the one transition out of P's last state.
  - So REL_Q ≤ d_o (C_P + 1) with C_P the actual number of crossing transitions in P, and C_P ≤ C. Correct; this is FRZ-3's form.
- DATA (XR):
  - Library: 661 fallback-free runs; SN prefix an initial segment in all (SN-PREFIX); 38 prefixes contain a ¬H1 state; no crossing inside
    a ¬H1 run; at most t_Q = 2; 4 crossing toggle transitions; REL_Q ≤ d_o (C_P + 1) with the actual C_P everywhere (max REL 12,
    max C_P 55); 0 failures.
  - Climb FIT=tog: §9.
  - The cubic bound itself is far above every observed count, so data cannot test it. It rests on the proof.

## 8. Not to sign: re-runs
- oneh_cex_n32.pg (sha1 51dab086…) and onedrop_cex_n32.pg (sha1 5793d5a3…): checked with my own trace, the 𝒞^1O assertion (o = 27), and
  l2_oink.py (Oink `--zlk -v` exit 0, "verified", N5's final regions agree with Oink's).
- oneh: 3 iterations, 1 fallback. One phase over states 1-3:
  - (h) at 1;
  - at 2, ¬H1 ∧ ¬H2 ∧ H3 with c_θ = c_w = 13 and |R| = 31 (R̄ = V);
  - the fallback 2 → 3 returns to (h).
  - The (h) states 1 and 3 are not consecutive: ONE-H is false, as the packet says.
- onedrop: 6 iterations, 1 fallback. One phase over states 2-6:
  - drops at 2 → 3 (S4a) and 5 → 6 (fallback);
  - θ = (13, ∅, 10) at 2-3 and (13, ∅, 8) at 4-6.
  - ONE-DROP is false, as the packet says.
- Every L2 check on both instances: 0 failures.
- FINDING against §8's OPEN CONJECTURE DROP-LEN ("between two drops of a phase, θ changes") and against its weaker form ("at most one
  drop per fallback-free run"): both are FALSE on docs/referee/R-N5-L2/droplen_cex_n12.pg.
  - Instance: sha1 a6af26db3f75540aa0f519cf0420b890fd2d4cc9; n 12, o = 0, d_o = 10; found by my climb l2_climb.py FIT=tog, seed 21.
  - N5 (own trace = n5.run): 4 iterations, 0 fallbacks. Oink `--zlk -v` verified, regions agree. One Odd choice vertex asserted.
  - All 5 states form ONE phase, which is one fallback-free run. Its SN prefix is all 5 states (c_w = c_θ = 2 throughout).
  - H1 at states 1 and 3; ¬H1 at states 0, 2 and 4. Drops 1 → 2 and 3 → 4 (S4a steps), t_Q = 4.
  - θ = w = (2, ∅, 1) at every state.
  - Mechanism: only σ(2) changes (0 → 1 → 7 → 9 → 10). Vertex 2 is c_θ, its own cycle node (priority 13, odd), and τ(o) = σ̄(o) = 2.
    Each switch of σ(2) lengthens or rearranges the odd cycle through 2 without changing any value. o lies on the cycle exactly when
    σ(2)'s play returns to o.
  - Every signed L2 statement holds on it:
    - R-CONST: R̄ = λ^{-1}(2) = V at the ¬H1 states, no crossing between them;
    - H1-INT: I_∅ = all states, the length is constant;
    - X-RUN′: 4 crossing transitions, all at toggles, ≤ t_Q.
  - So DROP-LEN's consequence "≤ n drops and ≤ 2n + 1 H1-toggles per phase" cannot come from θ-changes. Drops and toggles must be
    counted differently, for example by flat switches at c_θ.
  - Not reviewed here: L-NEW successor 15's TOGGLE (docs/new/N5-DROP-box35.md, after the pin). Whoever reviews it should run this
    instance against it.
- DATA: library and random have no DROP-LEN case (§9); the climb found one within minutes.

## 9. DATA summary (DATA, not proof)
- Packet instances: §8.
- Library (258 files, 319 phases, 7,155 states): §1-§7, 0 failures; phases with two in-phase drops: 1; DROP-LEN cases: 0.
- Random: `l2_probe.py rand 30000 4 14 7501`, i.e. 30,000 𝒞^1O games at n 4-14, with 5,522 phases and 63,961 states. 0 failures in
  every check:
  - H3C: 37,260 H2 states;
  - GP: 24,250 H3 ∧ ¬H1 states (21,108 c-first and 84,972 o-first vertices; 16,345 states with c = o);
  - RC: 29,866 ¬H1 states, 1,987 ¬H1 → ¬H1 transitions;
  - HI: 3,854 phases with I_∅ ≠ ∅, 55 in-phase drops;
  - XR: 4,756 runs, 1,816 with ¬H1 in the prefix, t_Q ≤ 1;
  - FRZ: no window;
  - H2S: 1 case.
- Random with back-edges into o (`randb 15000 4 14 7502`; 2,364 phases): 0 failures, same pattern (16,821 H3 ∧ ¬H1 states, 1,000 runs
  with ¬H1 in the prefix, no window).
- Phase exits (l2_exitdrop.py, for L2-2 and §2's "of a phase"):
  - library: 83 exit drops, 43 with P(θ_k) ≠ ∅; 106 S4a exits with H1 ∧ ¬H2, 26 regaining H2;
  - random 5,000: 278 exit drops, 198 with P(θ_k) ≠ ∅.
- Climbs (l2_climb.py, own code; every candidate asserted 𝒞^1O, every hit re-run through l2_probe):
  - FIT=tog (seed 21, n 5-12): t_Q up to 4 → droplen_cex_n12 (§8); 0 L2 failures.
  - FIT=h2s (seed 31): up to 8 non-self-loop H2-STICK cases per game; 0 failures.
  - FIT=frz from random n 3-8 (seeds 11-13, 2, 1): best fitness −1, no n-state window through a ¬H1 state.
  - FIT=frz seeded from thclimb_n12_s11, fts_best16 and j5_n16 (seeds 41-43, 30 min each; 560,747 / 321,659 / 360,557 steps): best
    fitness −2, no hit. (Final numbers added at 09:02Z by date -u, after the first push 7626354e.)
- Thin spots (named):
  - FREEZE′'s new content is unexercised: no H3 window of n states contains a ¬H1 state, and no H3 ∧ ¬H2 state follows a window.
  - P^c_ℓ on ¬H1 windows is tested only for N ≤ 3.
  - X-RUN′'s bounds are far above every observed count.
  - Random 𝒞^1O games give no windows at all.
  - H2-STICK's non-self-loop case has 120 library cases plus the climb.

## Addendum (written 2026-10-25 09:17Z by date -u): L-NEW's fixes file
- Object: docs/new/P-N5-L2-fixes-box34.md on trunk eb3f659, sha1 7a110bca8d52b532d531c0836547b2d22b7437cd (checked with sha1sum after
  merging trunk). The packet itself is unchanged.
- L2-1: the inserted sentence is my fixes-file line, verbatim. CLOSED.
- L2-2: the replacement clause is my fixes-file line, verbatim. CLOSED.
- §2 of the file records the DROP-LEN finding with my instance and the lane's re-run: 4 iterations, 0 fallbacks, Oink OK; the same
  states and drops as in my §8.
- Its references to P-N5-TOG / TOGGLE are outside this review. I have not reviewed TOGGLE.
- Labels: every REFEREE gap on P-N5-L2 is closed. The verdict table stands. FREEZE′ and X-RUN′ still depend on P-N5-FRZ (R32, at CHECKER).

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-L2.md, referee-2 388caf6, on trunk f87c5fdd). REFEREE successor 7, written 2026-10-25 09:45Z by date -u (stamp corrected from an estimated 09:50Z)
Signature (Opus 5.5, D15). I opened R2-N5-L2 only after my report (7626354e), its addendum (524d93f5) and the fixes-file check
(d3ccb9cd) were pushed. Also read: L-NEW's second fixes file docs/new/P-N5-L2-fixes2-box34.md (l-new ea78e9b5, on trunk), sha1
e343d74e1502e7c75ca5c40fd79350a3b8662b26, checked with sha1sum.

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| H3-CONST, G′, R-CONST | SIGNED | SIGN | signed by both |
| H2-STICK (+ Corollary) | SIGNED WITH GAP L2-1 (wording) | SIGN (N-L2-1, wording) | signed by both; L2-1 = N-L2-1, same repair (fixes 7a110bca §1) |
| FREEZE′ | SIGNED (premise P-N5-FRZ) | SIGN (premise now signed by both; N-L2-3 thin) | signed by both; premise P-N5-FRZ = R32 at CHECKER |
| H1-INT | SIGNED WITH GAP L2-2 (wording) | SIGN | signed by both. L2-2 is a REFEREE-only row (C.2), already repaired in fixes 7a110bca §1 |
| X-RUN′ | SIGNED (premise P-N5-FRZ) | SIGN (N-L2-2, wording) | signed by both; N-L2-2 accepted with Lemma X-RUN° (fixes2 §2, C.2) |
| §8 | not signed; FINDING DROP-LEN FALSE | not signed; DATA: §8 (2) restart occurs | — |
- No verdict differs in substance.
- The two label differences (H2-STICK, H1-INT) are gap labelling of wording points: REFEREE-2 calls the same H2-STICK point a note, and
  raised no item on H1-INT (b).
- Neither referee has a counterexample to a signed statement.

### C.2 Items found by one referee only
- L2-2 (REFEREE only; H1-INT (b) at phase exits). REFEREE-2's §6 reads the pre-drop clause in-phase without remarking on it.
  - The literal reading is false: exitdrop_n3.pg; 43 of 83 library and 198 of 278 random exit drops.
  - The lane accepted it verbatim (fixes 7a110bca §1), and REFEREE-2's reading agrees with the repaired line.
  - I keep it as a wording row.
- N-L2-2 (REFEREE-2 only as a row; X-RUN′ (a) applies X-RUN to the H1 runs P_i). My §7 made the same check: I re-read FRZ §6 for
  every use of "SN prefix" and found that the proof uses only consecutive (h) states of one fallback-free run. I recorded it as
  verified, not as a gap.
  - REFEREE-2's request to state it once as a lemma is accepted.
  - Fixes2 §2, Lemma X-RUN°: "I a set of consecutive states of Q at all of which (h) holds; crossing transitions with both ends in
    I ≤ 13 (d_o + 1) n³; FRZ-3's extra transition added where used". That is exactly the form my §7 verified. The replacement lines for
    §7 (a) are correct.
- N-L2-3 = my FREEZE′ thin spot. Both referees: FREEZE′'s conclusion beyond FREEZE is never exercised.
  - REFEREE-2 (its N5 with arbitrary S4a optima) reached n-state H3 windows through ¬H1 states at n ≤ 10, all ending at the phase's
    last state, so no later state could be checked.
  - My SPEC-trace climbs never reached such a window (best: n − 1 from random starts, n − 2 from library seeds).
  - P^c_ℓ on ¬H1 windows: both referees tested it directly, 0 failures (mine 641,105 path checks; REFEREE-2 about 17 M).
- DROP-LEN FINDING (REFEREE only, §8). REFEREE-2 saw phases with 2 drops in its variant (tog_61). My droplen_cex_n12 is a SPEC run with
  θ constant between the drops. The lane recorded it (fixes 7a110bca §2) and re-ran it.
- §8 (2) restart (REFEREE-2 only; DATA, not to sign): REFEREE-2 found it in its variant (j5_n16); the lane records a SPEC witness
  (fbrestart_cex_n12, fixes2 §3). Not a signed statement, so no row. I did not re-run either.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | L2-1 | N-L2-1 | wording, closed | §2 H2-STICK: "If τ(o) = o, ¬H2 holds at every state with this τ, in particular at s+1; assume τ(o) ≠ o below." (fixes 7a110bca §1) |
| 2 | L2-2 | — | wording, closed | §6 H1-INT (b): "every state k such that k → k+1 is a transition of the phase with H1 at k and ¬H1 at k+1" (fixes 7a110bca §1) |
| 3 | verified in §7 (not a gap) | N-L2-2 | wording, closed | §7 (a): Lemma X-RUN° and its replacement lines (fixes2 e343d74e §2) |
| 4 | thin spot (§4.2, §9) | N-L2-3 | DATA thin, recorded | none (claim rests on the proof) |

### C.4 Joint label (D18/L40)
- PROVED (L-NEW successor 14; REFEREE and REFEREE-2, Opus 5.5, D15), on 𝒞^1O inside a (λ_Ξ, τ) phase, pending CHECKER:
  - H3-CONST, H2-STICK (row 1), G′, R-CONST, H1-INT (row 2);
  - FREEZE′ (premise R32 = P-N5-FRZ, rows 1-6 of R-N5-FRZ §C) and X-RUN′ (row 3, premise R32).
- Honest limits: FREEZE′'s new case is unexercised (row 4). X-RUN′'s bound is far above every observed count.
- FALSE (DATA): ONE-H, ONE-DROP (lane), DROP-LEN and its per-run form (REFEREE, droplen_cex_n12).
- OPEN: G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE successor 7 (Opus 5.5, D15).
