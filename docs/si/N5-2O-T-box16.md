# N5 on 𝒞^2O: where R50's T-per-phase chain uses the single Odd choice vertex o, and what replaces it (lane note, box 16)
L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Lead's item (2) of 04:04Z (Lead's stamp): "T per phase
on 𝒞^2O given f, an R50 (h) analogue with D_k ⊆ {q1, q2} … Name exactly where R50's chain … uses a single o, and what replaces it."
Written 2026-10-26 04:2xZ onward (date -u; the stamp is the commit). LANE NOTE: not a packet, not frozen.
- Labels (D18 / L40): PROVED (L-SI 11, unrefereed) / CONJECTURE / OPEN / READING / DATA. D1: wrong until checked.
- Builds on:
  - docs/si/N5-FRONTIER-box15.md (successor 10): PAR_D, Lemma CR-D, Corollary CR-D′; "LEN is the first failing link"; CONJECTURE
    TC-SWITCH. Not repeated here; cited.
  - RESULTS R55 (P-N5-GD, LANDED): G_D (a), (b), (c1), (c2); F1°_D; Wo_D.
- Scope: one phase of N5 (SPEC S1-S5) on 𝒞^2O, with D_k ⊆ Q = {q1, q2}. Nothing here bounds N5's running time. G-N5-TIME stays OPEN.
- Not started, per the Lead: crossings X in set form (an R-STICK_D). It is listed as the next item (§4), unworked.

## 0. The two-gate setting (definitions from R55 §0; nothing new)
- D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)} ⊆ {q1, q2} on 𝒞^2O.
- u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play. R_D := {v : u(v) exists}, F_D := V ∖ R_D, and π_v is v's W-path before u(v).
- On 𝒞^1O these are R and F, with the single gate o. The replacements below substitute "the first gate on v's play" for "o".
- Hypotheses (R55): (h_D), no D-vertex's honest or W-play revisits D_k after leaving it; (h3_D), λ_Ξ(u) = λ_W(u) for u ∈ D_k.
- On 𝒞^2O, (h_D) can fail in two ways:
  - (¬h-cyc): a gate lies on its own honest or W cycle. This is the 1O case ¬H1 / ¬H2, per gate.
  - (¬h-route), NEW: one gate's play visits the other gate.
- Lemma ROUTE-2 (P-N5-2T §3) holds in each frame. In the W frame its proof is the same with the W-play: of two gates, at every state at
  least one is W-direct (on its own W-cycle, or its W-play never meets the other gate). So (¬h-route) is ONE-SIDED at every state: one
  gate routes through the other, and never both. (PROVED: the argument of P-N5-2T §3 uses only that plays are positional lassos.)
- STRETCH_D: a maximal run of states of a phase with D_k, R_D, and Ξ(u), W(u) (u ∈ D_k) constant. This is the 1O stretch (R, θ, w
  constant), with every gate's two values in place of θ, w.

## 1. R50's chain, item by item (READING with the status of each port; PROVED items say so)
| R50 item | where it uses the single o | replacement on 𝒞^2O | status |
| --- | --- | --- | --- |
| W-ONCE, W-ONCE′ | nowhere ("every game", R50 (a)) | verbatim | PORTS (landed, every game) |
| Fact A0 (full values on R) | "Every Odd vertex other than o is forced", so honest and W-plays agree along π_v up to o. The arc o → c_θ under ¬H1 avoids π_v. | (HP_D): σ̄ = τ off D_k, so the plays agree along π_v up to u(v) (R55 G_D (b), first bullet). The value is then the prefix of π_v up to the first of {u(v), its cycle node}, extended onto the terminal value Ξ(u(v)), (c, ∅, 0), W(u(v)) or (c_W, ∅, 0). All are constants of a stretch_D. | PORTS by iterated (V1) along the common prefix; needs no (h_D) when stated as "prefix up to the first terminal" (lane sketch, to write out). The 1O arc argument is not needed |
| Fact A (coarse values above m*) | one constant part C_Ξ (P(θ) above m*) and one C_W, shared by all of R | the constant part depends on the terminal: C_Ξ(u), C_W(u) for u = u(v). m*_D := the most relevant of λ_Ξ(u), λ_W(u) over u ∈ D_k | PORTS per terminal class (same proof with u for o) |
| Fact B (agreement above m*) | y, z ∈ R share the terminal o, so the constant parts cancel | same terminal: R55 G_D (c1) (under (h3_D)), or Fact B per class. DIFFERENT terminals: the comparison involves P(Ξ(u)) Δ P(Ξ(u′)) and P(W(u)) Δ P(W(u′)), which need not agree below their tops (Δ-RT, R55 Remark) | PORTS within a terminal class; ACROSS classes only above L_D := the top level at which the terminal values Ξ(u), Ξ(u′), W(u), W(u′) differ pairwise (plus M_D). Below L_D: OPEN (Δ-RT) |
| FRZ-U (κ-freeze of every run of a stretch) | paths ρ to o inside R (Claim P^c); Case B turns a κ-gain into a gate edge via Fact B; B2 / B3 use "x ∈ R_{k+1} has W cycle node c_w" | coarse form above max(M_D, L_D): successor 10's CR-D / CR-D′ under (h_D) ∧ (h3_D) on the run, with paths to D_k ∪ {W-cycle nodes} | PORTS in coarse form under (h_D) ∧ (h3_D) (N5-FRONTIER §2, PROVED unrefereed). Without (h_D) (37 % of the lib2o states, 63 % of the lib41 frontier states; DATA §3): OPEN |
| LEN (lengths only after the freeze) | after the freeze, all of R ends at o, so only lengths move | none for routes to different terminals: below L_D the path sets themselves can move (a terminal change) | FAILS as stated. FIRST FAILING LINK (N5-FRONTIER §3). Within one terminal class it holds verbatim |
| PAR | XW at o: θ ⊴ w with different cycle nodes ⇒ c_w even | PAR_D at each gate u (N5-FRONTIER §2) | PORTS (PROVED, every game) |
| H-PATH, KIND-MONO | kinds A / B: does π_v pass c_w (o's W-cycle node under ¬H2)? One bit, frozen above m* = c_w | per gate u with (¬h-cyc) in the W frame: kinds A_u / B_u for v with u(v) = u. Under (¬h-route) the routed gate's W-cycle is the other gate's, so the kinds are relative to that gate's c_W | PORTS per gate class under (¬h-cyc) (the proof is about one gate and its own cycle; the other gate is off π_v by the definition of u(v)). Under (¬h-route): OPEN, not attempted |
| CASC-B (via R26 (c), R24 (b) TB, R24 (c) CASC) | key step 4: kind-B candidates share the common prefix (A1 reversed, o) of the TB-even key pk | per terminal class, the prefix (A1(u) reversed, u) is common within the class. Candidates of DIFFERENT classes have different prefixes, so the TB key compares them by the gate part | PORTS within a class. ACROSS classes: a tied candidate of the other class is a terminal change (TC-SWITCH), counted separately. OPEN |
| CW-INT | c_w's successors are kind B, with constant values between cuts | per gate u: c_W(u)'s successors in u's class | PORTS per class, under the same cut set augmented by terminal changes (sketch) |
| E-SEG, RUN | sums over W-flat segments with LEN's length counts and KIND-MONO's ≤ r − 2 kind changes | the same sums per terminal class, plus one cut per terminal change | REDUCES to TC-SWITCH: RUN_D ≤ (TC + 1) · (1O-type bound per class), IF FRZ-U holds on the run (needs (h_D) ∧ (h3_D)). READING |
| KW-S, PHASE (R50 (h)) | Θ (R27 (g) TH: θ-changes), S_o (R27 (g) SO: σ̄(o)-changes), W_ch (R24 (e) WC: w-changes), X (R30 (c), R34), R27 (d) LP, R19 (d) SG, F1° (R22 (a)) | LP and SG: every game (landed). F1° → F1°_D (R55, LANDED; per D-crossing-free interval). Θ → ρ (Ξ(q1), Ξ(q2)-changes: ALL of them, not only N_late). S_o → σ̄(q_i)-changes. W_ch → W(q_i)-changes. X → X_D (changes of (D_k, R_D)) | see §2 |

## 2. What T per phase on 𝒞^2O needs, in R50 (h)'s form (READING)
R50 (h)'s proof is: T ≤ (m − n + 1)(T_rel + 1) (R27 (d) LP, any game); T_rel ≤ S_o + N_Ξ ((SG), any game); and
N_Ξ ≤ f + (stretch boundaries) + (F-side changes) + (R-side changes per run) × (runs). The 𝒞^2O form:
| count | 𝒞^1O source | 𝒞^2O replacement | status |
| --- | --- | --- | --- |
| f | R48 | P-N5-2T Corollary FB-2O (CONDITIONAL on FBRED, R56 at CHECKER) | lane-PROVED |
| F-side Ξ-changes | F1°: ≤ \|F\| − 1 per crossing-free interval | F1°_D: ≤ \|F_D\| − 1 per D-crossing-free interval (R55) | LANDED; needs X_D |
| X_D (D-crossings) | R30 (c) SN-PREFIX, R34 (f) | an R-STICK_D (the next item, §4); L-NEW's CONJECTURE Δ1 | OPEN (not started, per the Lead) |
| stretch_D boundaries | X + Θ + W_ch | X_D + ρ + Σ_i W(q_i)-changes + D_k-changes | OPEN through ρ and W(q_i) |
| ρ (all Ξ(Q)-changes) | Θ: R27 (g) TH, via ¬H1 lengths (YB) and an F1° F-change at o's exit under H1 | a direct gate q: as TH (its exit y lies in F_D or routes to c; the change is an F1°_D change, or a Cyc_c length step by (YB_q)). A gate routed through the other gate (¬h-route, honest frame): Ξ(q) = (path) ⊕ Ξ(q′); a change is a Ξ(q′)-change or a change on the path (an R-side change) | REDUCES (sketch): ρ ≤ 2·(TH-type count) + (R-side changes on routed paths). Not proved |
| S_o → σ̄(q_i)-changes | R27 (g) SO: ≤ d_o(Θ + 1) | per gate: ≤ d_{q_i}(ρ_{q_i} + 1), IF SO's "frozen key of an exit that stays a minimiser" ports per gate. SO's proof uses CAP-1 (σ̄(o) a full Ξ-minimiser, R25) | OPEN (CAP-1 per gate not checked) |
| W(q_i)-changes | R24 (e) WC (¬H2), F1° (H2) | (¬h-cyc): WC per gate; W-direct gate with exit in F_D: F1°_D; (¬h-route) in the W frame: W(q) = (W-path) ⊕ W(q′) | OPEN |
| R-side Ξ-changes per run | Theorem RUN, 3Δr⁴ | (TC + 1) × per-class RUN, under (h_D) ∧ (h3_D) on the run (§1) | REDUCES to TC-SWITCH; OPEN without (h_D) |
- READING: on 𝒞^2O, "T per phase ≤ poly(n, m, f)" would follow from four new pieces:
  - (i) X_D polynomial (R-STICK_D);
  - (ii) TC-SWITCH (terminal changes per run polynomial);
  - (iii) the (¬h-route) cases of FRZ-U and KIND-MONO;
  - (iv) per-gate SO and WC.
  (ii)-(iv) are about two gates and one-sided routing (ROUTE-2 in both frames). The structural fact that should carry them is the one
  FB-2T used: at every state one gate is direct in each frame, so the routed gate's terminal value is the direct gate's plus a path.
- The ρ in this table is all Ξ(Q)-changes. P-N5-2T bounds only the Q-runs that hold late fallbacks, which is all that f needs. T needs
  ρ itself, and ρ includes the fallback-free changes, so it sits inside the R-side count.

## 3. DATA (DATA, not proof): experiments/si/fb2o/tcsw.py
Own script (N5 via n5x.py step, read-only). Per state it computes D_k, u(v) on W-plays, (h_D), (h3_D) and W-frame ROUTE-2. Per
fallback-free run of each phase it counts terminal changes: transitions at which some v ∈ R_D at both ends changes u(v).
| set | games | phases | runs | transitions | terminal-change transitions (max per run; max per vertex per run) | (h_D) states | (h3_D) states | W-ROUTE-2 viol. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib2o.txt (43 games, exactly two Odd choice vertices) | 43 | 129 | 173 | 201 | 2 (1; 1) | 235 / 374 | 314 / 374 | 0 / 182 |
| lib41.txt, games with ≥ 2 Odd choice vertices, n ≤ 48 | 93 | 642 | 681 | 358 | 27 (9; 2) | 389 / 1,039 | 526 / 1,039 | 0 / 224 |
- Terminal changes are rare in the library: at most 9 per run, and at most 2 per vertex per run. This is weak support for TC-SWITCH,
  on short runs.
- (h_D) fails at 37 % of the lib2o states (139 / 374) and at 63 % of the lib41 frontier states (650 / 1,039). So the coarse freeze CR-D′, which needs (h_D) ∧ (h3_D) on the whole run, does not cover the library
  phases. The (¬h-route) and (¬h-cyc) cases are not exotic.
- The W-frame ROUTE-2 holds at all 406 two-gate states (structural; a checker of the lemma's proof, not of N5).
- Reproduce (from experiments/si/fb2o): `python3 -I tcsw.py --list lib2o.txt 2` and
  `python3 -I tcsw.py --list ../../new/box41/lib41.txt 2` (≈ 10 s and ≈ 1 min).

## 4. Next items (for the Lead's routing)
1. X_D: an R-STICK_D (R30 (c) in set form: at an S4a step of a phase, which R_D vertices can leave R_D). NOT started, per the Lead
   (possibly L-NEW).
2. TC-SWITCH on two gates. A candidate monotone quantity: at a W-flat terminal change y: route to u → route to u′, Ξ(y) rises strictly
   ((SG)) at a level ≤ L_D (the levels where the two gates' values differ). With one-sided routing (ROUTE-2), one gate's value is the
   other's plus a fixed path when both are constant on a stretch_D, so L_D is the top of that path's κ-difference. That makes the
   two-gate case an ordering of two values, not of |D_k|. Not attempted.
3. (¬h-route) FRZ-U: the routed gate behaves like a vertex of the direct gate's class with a constant route. Sketch only.
