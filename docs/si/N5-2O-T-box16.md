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
- Lemma ROUTE-2W (PROVED, every game; the W-frame form of P-N5-2T's ROUTE-2).
  - Statement: let u ≠ u′ be Odd vertices at a state k. Call u W-DIRECT if u lies on its own W-cycle (the cycle of its (σ_k, τ_k)-play),
    or its W-play never visits u′; likewise for u′. Then u or u′ is W-direct.
  - Proof:
    - Suppose u is not W-direct: u is not on its own W-cycle, and its W-play visits u′.
    - The W-play is positional (σ_k at Even vertices, τ_k at Odd ones), so from its first visit of u′ on, u's W-play is u′'s W-play.
    - If u′'s W-play visited u, then u's W-play would visit u a second time, so u would lie on its own W-cycle. That is excluded.
    - So u′'s W-play never visits u, and u′ is W-direct. □
  - The same proof with the honest play (σ_k, σ̄_k) is the honest-frame form. With u, u′ the two gates of D_k it says that (¬h-route) is
    ONE-SIDED in each frame at every state: one gate may route through the other, never both.
  - DATA (§3): 0 violations at all 406 two-gate states checked (lib2o and lib41 frontier, tcsw.py).
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

## 5. Update (box 16, after the Lead's 04:19Z GO): the gate-order route to TC-SWITCH is DEAD
- I tested the candidate of §4.2 and of N5-FRONTIER §4 ("a terminal change moves up a fixed order ≼_D of the gates, e.g. by W") on
  𝒞^2O, with own scripts experiments/si/fb2o/tcdir.py and climbtc.py.
- Library: with D_k fixed, 47 / 47 terminal changes went to the gate with the larger W (lib41's frontier games; logs/tcdir_lib41.txt).
- Random start pairs: FALSE. In 150,000 random 𝒞^2O games, 21 of 94 two-gate changes with D fixed go to the gate with the SMALLER W,
  some also against Ξ (logs/tcdir_rand2o_150k.txt). This persists when the gate is taken as the first W-direct gate, the gate structure is
  fixed, and v ∉ D_k: 5 of 21 (logs/tcdir_rand2o_150k_ult.txt).
- Instance (all three forms): experiments/si/fb2o/instances/tcwult2_against_n8.pg with its .start.json (n 8). Full record:
  docs/si/DEAD.md, "DEAD box 16".
- Mechanism: S4a takes Even's pointwise W-optimum of its arena, so a route to a lower-valued gate wins when its path part is better.
- Consequence: TC-SWITCH cannot be closed by a gate order. A terminal change is a W-rise (or a tie) at v, so counting terminal changes
  per run is as hard as counting W-changes on R_D per run, which is RUN_D itself.
- READING: the R50 chain's per-class structure (FRZ-U, LEN, KIND-MONO per class) does not reduce the two-gate case to the one-gate case
  by cutting at terminal changes. A different potential is needed: one that orders (path, gate) pairs jointly, as W does, but with a
  polynomial range. OPEN.

## 6. The (¬h-route) case of FRZ-U: R55's G_D (b), (c) and successor 10's CR-D′ need only (NC) (Lead's item (a), 04:54Z)
Hypothesis (NC) at a state k: no vertex of D_k lies on its own honest cycle, and none lies on its own W-cycle. (h_D) implies (NC). (NC)
allows one gate's play to visit another gate, the (¬h-route) case. It forbids only (¬h-cyc).
### Lemma G_D-NC (PROVED, every game; R55 G_D (b), (c1), (c2) with (h_D) weakened to (NC))
- (b′) Under (NC) at k: for v ∈ R_D with u := u(v), the honest and the W-play from u avoid π_v, and Ξ_k(v) = π_v ⊕ Ξ_k(u),
  W_k(v) = π_v ⊕ W_k(u).
- (c1′) and (c2′) Under (NC) and (h3_D) at k, R55 (c1) and (c2) hold verbatim. In particular COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)) for every
  v ∈ V and every L with M_D ≤ L < ∞.
Proof.
- (b′): R55's proof of G_D (b), with its one use of (h_D) re-read.
  - Both plays from v follow π_v to u, because the Odd vertices of π_v are outside D_k (HP_D).
  - Let x ∈ π_v. x's W-play is the suffix of π_v from x, then u. By (HP_D) its honest play is the same path to u.
  - R55's proof: "If u's honest play (resp. W-play) met x after leaving u, it would then follow x's play back to u ∈ D_k, against (h_D)
    at u." Plays are positional lassos, so returning to u means u lies on the cycle of its own play, in that frame. That is exactly
    what (NC) forbids. Visits of OTHER gates are never used.
  - So each play from v is π_v followed by u's play, which avoids π_v, and (V1) along π_v gives both equations.
- (c1′), (c2′): R55's proofs of (c1) and (c2) use (h_D) only through G_D (b) (in (c1): "T's play avoids π_v (G_D (b))"; in (c2): "by G_D
  (b), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u)", and "both plays from u avoid π_v"). Replace G_D (b) by (b′). (h3_D) is used as
  before. □
- NOT ported: R55's Wo_D. Its proof uses (h_D) to put τ(u) ∈ F_D. Under (¬h-route) the W-play from τ(u) can reach the other gate.
### Corollary FRZ-U_D (coarse; PROVED, every game, given R55 and successor 10's Lemma CR-D)
Statement. Let S be a run of consecutive S4a transitions (no fallback) inside one phase of N5 on any game, with (NC) and (h3_D) at every
state of S. Let L ≥ max_S M_D (L ≥ −1). Then COARSE_L(W) = COARSE_L(Ξ) is constant on S from its (n − 1)-th state on.
Proof. Lemma CR-D (docs/si/N5-FRONTIER-box15.md §2) needs, at every state of S:
- (i) COARSE_L(Ξ) = COARSE_L(W) on V: this is G_D-NC (c2′);
- (ii) λ_W constant on S. On F_D, λ_W = λ_Ξ by G_D (a) (R55, no hypothesis). On R_D, by (b′), λ_W(v) = λ_W(u(v)) and λ_Ξ(v) = λ_Ξ(u(v)),
  and λ_W(u(v)) = λ_Ξ(u(v)) by (h3_D). So λ_W = λ_Ξ on V, and λ_Ξ is constant on the phase.
Successor 10's CR-D′ proved the same under (h_D) ∧ (h3_D). This replaces (h_D) by (NC). □
- Scope, exactly:
  - every game and every number of gates;
  - every fallback-free run inside a phase on which (NC) and (h3_D) hold at every state;
  - the coarse level L ≥ max_S M_D only.
  The routed gate needs no special treatment. In each frame it is a vertex on the routes into the gate it routes through, and (b′)
  handles it.
- Not covered:
  - (¬h-cyc): a gate on its own honest or W-cycle, the 1O cases ¬H1 / ¬H2, which R50 handled with kinds (KIND-MONO, CASC-B, CW-INT);
  - ¬(h3_D);
  - everything below L, which is LEN, the first failing link (§1). FRZ-U_D does not touch it.
### DATA (experiments/si/fb2o/gdnc.py; own checker; logs/gdnc_*.txt)
At every state it checks (b′) (both equations and both avoidances) when (NC) holds, and (c2′) at L = max(M_D, −1) when (NC) and (h3_D)
hold. On every fallback-free run inside a phase with (NC) ∧ (h3_D) throughout, it checks FRZ-U_D's freeze from the (n − 1)-th state.
| set | states | (h_D) | (NC) | (NC) ∧ ¬(h_D) | (b′) checks / viol. | (c2′) checks / viol. | FRZ-U_D runs / checks / viol. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib2o.txt (43 games) | 374 | 235 | 325 | 90 | 1,718 / 0 | 7,934 / 0 | 37 / 0 / 0 |
| lib41 frontier (93 games, ≥ 2 Odd choice vertices) | 1,039 | 389 | 603 | 214 | 3,229 / 0 | 17,604 / 0 | 57 / 0 / 0 |
| random 𝒞^2O, 40,000 games, n 5-12, half from random start pairs (seed 31) | 95,928 | 68,803 | 69,849 | 1,046 | 8,126 / 0 | 573,433 / 0 | 4,721 / 0 / 0 |
| random 𝒞^kO (k 2-4), 20,000 games, n 5-14 (seed 32) | 50,804 | 33,900 | 34,836 | 936 | 5,710 / 0 | 319,671 / 0 | 2,356 / 0 / 0 |
- Mutation control: MUT=1 checks (b′) without (NC). It fails on lib41 (absmono_viol_n44.pg, 3 violations): the hypothesis is needed.
- (NC) gains over (h_D): 90 more states of 374 on lib2o, 214 of 1,039 on the lib41 frontier.
- Still outside: (NC) fails at 49 / 374 (lib2o) and 436 / 1,039 (lib41 frontier) states. That is (¬h-cyc), a gate on its own cycle, the
  remaining FRZ-U case.
- FRZ-U_D's freeze is VACUOUS in all data: no fallback-free run with the hypotheses lasts n − 1 transitions (0 checks). It rests on CR-D's
  proof. For L-RED: a run of ≥ n transitions under (NC) ∧ (h3_D) is what a check needs, from random start pairs.

## 7. (¬h-cyc) per gate (Lead's item (2), 05:05Z): the coarse freeze needs only (h3_D); kinds are needed only for ¬(h3_D)
### Lemma TC-CLASS (PROVED, every game)
Statement. At every state k and for every v ∈ R_D: λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)). Hence, inside a phase, a terminal change
u_k(v) ≠ u_{k+1}(v) happens only between two vertices of D with the same honest cycle node, namely λ_Ξ(v).
Proof.
- Both plays from v follow π_v to u(v) (HP_D), and then continue as u(v)'s play in their frame (plays are positional). So v's play and
  u(v)'s play end in the same cycle in each frame.
- λ_Ξ is constant on a phase, so λ_Ξ(u_k(v)) = λ_Ξ(v) = λ_Ξ(u_{k+1}(v)). □
- Consequence on 𝒞^2O: if q1 and q2 have different honest cycle nodes at a state, each honest class holds at most one of them, and no
  vertex can move between them. The two-gate obstruction (Δ-RT, terminal changes, TC-W's dead end) lives only inside ONE honest class
  holding both gates.
- DATA: 0 cross-class terminal changes (tcdir.py TCCLASS_V, 150,000 random 𝒞^2O and lib41). The gates share their honest class at
  7,922 / 9,939 random 𝒞^2O two-gate states, 216 / 224 lib41, 180 / 182 lib2o (hcyc.py). So the hard case is the common one.
### Lemma C2-H3 (PROVED, every game): R55's coarse agreement (c2) needs only (h3_D)
Statement. Let (h3_D) hold at k and let L satisfy M_D ≤ L < ∞, L ≥ −1. Then COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)) for every v ∈ V.
No (h_D) and no (NC) is assumed.
Proof.
- v ∈ F_D: Ξ_k(v) = W_k(v) (R55 (a)).
- v ∈ R_D: let u := u(v) and c := λ_Ξ(u) = λ_W(u), by (h3_D). By TC-CLASS, c is v's cycle node in both frames. For a frame F, let P_F(v)
  be the vertices of v's F-play before its first visit of c, ranked above c (the path set of its value).
- Lasso fact: c lies on the cycle of v's F-play, and every vertex of a lasso's cycle is visited before the first repetition. So the
  prefix of the play up to the first visit of c repeats no vertex.
- Case c ∈ π_v: both plays follow π_v up to c, so P_Ξ(v) = P_W(v), and the coarse values are equal (COARSE_L ignores lengths).
- Case c ∉ π_v: v's F-play is π_v, then u's F-play, and c is first visited inside u's F-play. The prefix before c is π_v followed by Q_F,
  the prefix of u's F-play before c. Q_F ∩ π_v = ∅, by the lasso fact (a vertex of π_v in Q_F would be repeated before c). So
  P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u).
- lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L. By (C2), COARSE_L(Ξ_k(u)) = COARSE_L(W_k(u)), so P_Ξ(u) ∩ V_{>L} = P_W(u) ∩ V_{>L}. Hence
  COARSE_L(Ξ_k(v)) = (c, ((π_v ∩ V_{>c}) ⊔ P_Ξ(u)) ∩ V_{>L}) = COARSE_L(W_k(v)). □
- This contains G_D-NC (c2′) (P-N5-NC §2) and R55 (c2) as special cases. R55's proof went through the exact factorisation (b), which needs
  (h_D) (or (NC)). The coarse statement does not need it: the path set above c factors through u(v) whatever the play does after c.
### Corollary FRZ-U_H3 (PROVED, every game; strengthens P-N5-NC's FRZ-U_D)
Statement. Let S be a run of consecutive S4a transitions inside one phase, with (h3_D) at every state of S, and let L satisfy
max_S M_D ≤ L < ∞, L ≥ −1. Then COARSE_L(W) = COARSE_L(Ξ) on V at every state of S, and it is constant from state k_0 + n − 1 on.
Proof. Lemma CR-D (P-N5-NC §3):
- (i) is C2-H3;
- (ii): λ_W = λ_Ξ on V by TC-CLASS and (h3_D) on R_D, and by R55 (a) on F_D. λ_Ξ is constant on the phase. □
- Scope: every game; any configuration of the disagreement vertices on their cycles. (¬h-cyc) and (¬h-route) are both covered. Only
  (h3_D) is needed.
### What this does to the (¬h-cyc) item, and what breaks with two gates each on its own cycle (READING)
- On 𝒞^1O, R50 uses kinds (H-PATH, KIND-MONO, CASC-B, CW-INT) exactly in case (c): ¬H2, c_w ≠ o and c_w ≻ c_θ. That case has c_w ≠ c_θ,
  so H3 fails. Under H3, R50 uses only FRZ-U and LEN (Theorem RUN (a), (b)). So in set form:
  - under (h3_D): the coarse freeze holds for every cycle configuration (FRZ-U_H3). What remains is LEN below M_D, i.e. the fine order
    of routes inside one honest class with two gates (Δ-RT; TC-W is dead).
  - under ¬(h3_D) at a gate u (λ_Ξ(u) ≠ λ_W(u)): R50's case (c), per gate. PAR_D gives λ_W(u) even when λ_W(u) ≻ λ_Ξ(u)
    (N5-FRONTIER §2). The kind of v ∈ R_D with u(v) = u is "λ_W(u) ∈ π_v". That is where the KIND-MONO port is needed.
- Two gates each on its own W-cycle:
  - Different W-cycles: the cycles are disjoint, so they have different cycle nodes. Under (h3_D) the gates then have different honest
    cycle nodes, so they lie in different honest classes. By TC-CLASS they never exchange vertices. Each class is a one-gate (1O-like)
    class: nothing breaks.
  - The same W-cycle C with cycle node c_w: going along C from either gate, exactly one of them (the LEAD ℓ) reaches c_w before the
    other (the TRAIL t). In the W frame, W(t) = (C-arc from t to ℓ) ⊕ W(ℓ). So the W frame is R50's ¬H2 structure C_W = o → A1 → c_w → A2
    → o with o := ℓ and t ∈ A2.
    - The honest frame deviates at t as well as at ℓ. Under (h3_D) this costs nothing coarse (C2-H3).
    - What breaks is fine: inside the one class, vertices route to t or to ℓ, and the honest comparison of π_y ⊕ Ξ(t) with π_z ⊕ Ξ(ℓ)
      need not match the W comparison below M_D (Δ-RT). This is the LEN failure again, now with t on A2.
    - Under ¬(h3_D), the kind bit is c_w (as on 𝒞^1O). With t ∈ A2, every vertex routed to t is of kind B (its path to ℓ runs along A2,
      after c_w). So the kinds are those of R50 with o := ℓ. KIND-MONO's proof also needs FRZ-U's freeze above m* = c_w, and that
      freeze is proved only coarse above M_D, which is ∞ under ¬(h3_D). So KIND-MONO does not port as it stands. The full (κ, above
      m*) FRZ-U of R50 would have to be ported with two deviation points on C_W. Not done.
### DATA (experiments/si/fb2o/gdnc.py with H3ONLY=1, hcyc.py, tcdir.py; logs gdnc_h3_*.txt, hcyc_*.txt)
| set | states | (h3_D) | (h3_D) ∧ ¬(NC) | C2-H3 checks / viol. | of which at ¬(NC) states |
| --- | --- | --- | --- | --- | --- |
| lib2o.txt | 374 | 314 | 3 | 7,972 / 0 | 38 |
| lib41 frontier | 1,039 | 526 | 23 | 18,323 / 0 | 719 |
| random 𝒞^2O, 40,000 games (seed 31) | 95,928 | 72,780 | 7,658 | 637,911 / 0 | 64,478 |
| random 𝒞^kO, 20,000 games (seed 32) | 50,804 | 36,271 | 4,124 | 358,424 / 0 | 38,753 |
- Mutation control (MUTL=1: one level below M_D) on lib41: 2,504 violations. The level M_D is sharp in data.
- Cycle configurations at two-gate states (hcyc.py), random 𝒞^2O:
  - W frame: no gate on its own cycle 4,121; one gate 4,664; both on one cycle 500; both on different cycles 654.
  - honest frame: no gate 3,296; one gate 5,075; both on one cycle 854; both on different cycles 714.
- (h3_D) fails at 24 % of the random 𝒞^2O states and at 49 % of the lib41 frontier states. That is the KIND-MONO territory, still open.

## 8. ¬(h3_D) KIND-MONO with two deviation points (Lead's item (3), 05:30Z): what reduces, and what breaks
### Lemma W-CN (PROVED, every game)
Statement. Along a run of consecutive S4a transitions inside a phase, the reward of λ_W(v) is non-decreasing for every v. Hence λ_W(v) changes
at most n − 1 times per vertex per run.
Proof. WM-G (P-N5-H3 §5): W_{k+1}(v) ⊵ W_k(v). The S1 order compares cycle-node rewards first, so reward(λ_W,k+1(v)) ≥ reward(λ_W,k(v)),
strictly if the cycle node changes (rewards are injective). There are at most n distinct rewards. □
### Corollary TC-CN (PROVED, every game)
Statement. Inside a run S as above, call a terminal change of v at k → k+1 (u_k(v) ≠ u_{k+1}(v)) W-MOVING if λ_W,k+1(v) ≠ λ_W,k(v), and
TWIN otherwise. Then:
- (a) the W-moving terminal changes of S number at most n(n − 1) in all, at most n − 1 per vertex;
- (b) at a twin change, the old and the new gate have the same honest cycle node and, across the transition, the same W-cycle node:
  λ_Ξ(u_k(v)) = λ_Ξ(u_{k+1}(v)), and λ_W,k(u_k(v)) = λ_W,k+1(u_{k+1}(v)).
Proof. (a) is W-CN. (b): TC-CLASS (P-N5-H3 §3) gives λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)) at each state, and λ_Ξ is constant on the
phase. □
- So TC-SWITCH (terminal changes per run) reduces to TWIN changes. Their gates sit in one honest class and share their W-cycle node.
- DATA (tcdir.py; TCCN_V = a W-moving change that does not raise the reward of λ_W(v)): 0 violations.
  - Random 𝒞^2O, 150,000 games: 69 twin and 25 W-moving changes.
  - lib41 frontier: 32 twin, 15 W-moving.
  - Random 𝒞^kO, 30,000 games: 16 twin, 0 W-moving.
  - TC-W's dead-end instance (DEAD box 16) is a twin change.
### What KIND-MONO needs, and where it breaks (READING)
- R50's KIND-MONO (𝒞^1O, case (c): ¬H2, c_w ≠ o, c_w ≻ c_θ) needs:
  - FRZ-U's κ-freeze above m* = c_w;
  - H-PATH (c_w ∈ P(Ξ(v)) iff v is of kind A, i.e. c_w ∈ π_v);
  - PAR (c_w even).
- PAR ports per gate (PAR_D, N5-FRONTIER §2).
- FRZ-U's freeze above m* rests on Fact B: two R-vertices are ordered the same way in both frames above m*. On 𝒞^1O this holds because
  every route ends at o with common constant parts C_Ξ, C_W.
- Two twin gates u, u′ in one honest class, with ¬(h3_D) (c_w ≠ c):
  - Within one terminal class (routes to the same gate), Fact B holds per terminal, as on 𝒞^1O.
  - ACROSS the twins: Ξ(y) = π_y ⊕ Ξ(u) versus Ξ(z) = π_z ⊕ Ξ(u′), with the same cycle node c; and W(y) = π_y ⊕ W(u) versus
    W(z) = π_z ⊕ W(u′), with the same cycle node c_w. The verdicts agree above max(rank m*, L_X, L_W), where
    L_X := top(P(Ξ(u)) Δ P(Ξ(u′))) and L_W := top(P(W(u)) Δ P(W(u′))).
  - If max(L_X, L_W) > rank(m*), Fact B fails across the twins above m*. FRZ-U's Case B then cannot turn a κ-gain into a gate edge, and
    the kind bit c_w lies BELOW the cross-terminal disagreement level, so KIND-MONO's "c_w is the top difference" step fails.
  - That is the exact obstruction for two deviation points under ¬(h3_D): the Δ-RT levels of the twin pair lie above the kind bit.
  - When max(L_X, L_W) ≤ rank(m*), the 𝒞^1O argument has its Fact B above m*. The port is then plausible but NOT checked line by line
    here (FRZ-U's B2 / B3 use C_W's two arcs with one deviation point on them, and with twins there are two).
- DATA (twin.py), at two-gate states whose gates are twins with ¬(h3_D):

  | set | twin states | ¬(h3_D) twin | above m* | below m* | c_w above c |
  | --- | --- | --- | --- | --- | --- |
  | lib41 frontier | 190 | 48 | 40 | 8 | 26 |
  | random 𝒞^2O, 40,000 (seed 31) | 6,158 | 4,039 | 1,013 | 3,026 | 2,336 |

  - "above m*" is max(L_X, L_W) > rank(m*): there the obstruction is present. It is 83 % on the lib41 frontier and 25 % in random games.
- km2.py (FRZ-U's set-form freeze test on such runs): VACUOUS. The runs are shorter than |R_D| − 1, so the data neither confirm nor
  refute the freeze in this configuration.
- Status:
  - PROVED: W-CN, TC-CN.
  - READING: the obstruction above.
  - OPEN: KIND-MONO with two deviation points. It needs a Δ-RT bound for twin gates, i.e. an ordering of the twins' terminal values that
    both frames respect above the kind bit.

