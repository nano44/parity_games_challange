# N5-STRETCH (box 64): FRAME-STRETCH DEAD (mkr, L-RED 29; reproduced); FRAME-STRETCH_P = box 21's (FO) open; composition with ODD-FREEZE and R86
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 19:29Z (BOX 64 (a)-(d)).
Written 2026-10-29 from ~19:55Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
Labels: PROVED (lane) / DATA / READING / CONJECTURE / OPEN / DEAD.
- Engine: box21/n5x (plain N5, SPEC S1-S5), S3 start unless "own start" is said. Tools: experiments/new/box64/stretch.py, frozen.py,
  climb1p.py. Outputs: box64/stretch_all.txt, frozen_all.txt (719 games, box59/sbcg.lst), dual_start.txt, frozen_dual.txt.
- Read for this box: box 21 Theorem B (docs/new/N5-time-box21.md §2.4-§2.6), RESULTS R17, R86, R87, R88, N5-K8-box8.md §3b-§3c (SB1′).

## 1. (a) FRAME-STRETCH: DEAD as stated (§1.5); the polynomial form is not given by landed results
### 1.1 What it is
- A τ-stretch of N5 is box 21's "τ-constant block". Theorem B (a) (box 21 §2.4, PROVED lane): inside it, σ_{k+1} = F_τ(σ_k).
  F_τ is the frozen-τ run: S4a's arena on G_τ (Odd follows τ, Even may use σ ∪ Iσ), with Iσ computed against σ̄(σ), plus S4c's
  Even fallback.
- So FRAME-STRETCH (< n + m σ-changes per τ-stretch) is (FO) of box 21 §0 with the explicit bound n + m.
- Theorem B (b): N5 ≤ (C_τ + 1)(F_E + 1), F_E = longest F_τ run over all τ and starting σ, C_τ = τ-changing iterations.
  This is the "#σ − 1 < (n + m)·#τ" consequence of box 62, with F_E in place of n + m.
### 1.2 Why R17 / R38 / R47 / R86 / R88 do not give it (READING, each point checked against the RESULTS text)
- (i) R17 (c) bounds one λ-PHASE of switch-best on a one-player game by n + m. A τ-stretch is not one λ-phase.
  - Even on a genuine one-player game, a run has up to n(n − 1) + 1 λ-phases. R17 (d)'s bound is (n² − n + 1)(n + m), not n + m.
  - DATA: inside one τ-stretch, λ_W (cycle nodes of W = val(σ, τ)) changes up to 7 times (red/so/instances/rise_thin51_n40, longest
    stretch). Summed over the 719 longest stretches: 1376 λ_W-changes.
- (ii) Even when τ is fixed, F_τ is NOT switch-best on G_τ. The gate Iσ is Ξ-improving (against σ̄), not W-improving (against τ).
  - Box 21 Lemma PT: R17 transfers exactly when the gate contains G_τ's improving edges. That inclusion is false (box 21 §3.1).
  - fts_ph16 / fts_best16 (box 21 §3.2, §3.4) exceed the per-phase bound n − 1 (22 and 27 value-changing steps in one joint λ-phase).
- (iii) R88 GP* / FW-R* is the landed piece. It bounds W-changing transitions per FROZEN W-phase: no fallback; τ, σ̄, λ_Ξ, λ_W
  constant; at most (n − 1)(R*_T + 1).
  - A τ-stretch is a union of frozen W-phases. They are cut by fallbacks, σ̄-changes, λ_Ξ-changes and λ_W-changes.
  - λ_Ξ: at most n(n − 1) per run (R47 (a), as cited in R86).
  - λ_W: W rises (⊵) at every arena step of F_τ (box 21 Lemma W, lane; R88 §2 W-MON signs it inside a phase). So λ_W changes
    at most n(n − 1) times between fallbacks.
  - σ̄-changes and fallbacks inside a stretch: NOT bounded by any landed result.
- (iv) R86 COMPOSE bounds switches per λ-run by path-set changes P*. It is a different reduction (to P*), not a per-τ-stretch bound.
- (v) The n + m form contains SB1′. Take a game with every Odd out-degree 1 (one-player). Then τ never changes, so the whole run is
  one τ-stretch, and N5 = switch-best (R17 (e)).
  - So FRAME-STRETCH there says: switch-best on one-player games makes < n + m steps.
  - That is the open conjecture SB1′ (N5-K8-box8.md §3b: O(n); DATA ≤ n + 1; Lemma T §3c reduces it to "cycle tops settle in
    O(n)", not done) in its n + m form.
  - A short proof of FRAME-STRETCH through R17 is therefore impossible without proving SB1′ (n + m form) first.
  - The POLYNOMIAL form is true on one-player games, by R17 (d).
- Restated target (CONJECTURE FRAME-STRETCH_P = (FO)): F_E ≤ poly(n, m). The n + m form stays as the data-level CONJECTURE.
### 1.3 DATA (box64/stretch.py, frozen.py)
- FRAME-STRETCH on 719 games (S3): 0 violations. Max 89 / 137 = 0.650 (red/n5inj/instances/frz40). Max per n: 2.69 (b6_xl2_n32).
  (Box 62 counted the boundary transition too: 90 / 137.)
- Frozen-phase anatomy of each game's longest τ-stretch (frozen_all.txt):
  - up to 265 frozen W-phases in one stretch; max phases / n = 1.65 (rise_thin51_n40: 66 phases, cut by 56 σ̄, 7 λ_Ξ, 7 λ_W, 7 fb);
  - cut causes summed over the 719 stretches: σ̄ 2277, λ_W 1376, λ_Ξ 826, fallback 609;
  - longest frozen phase 67 W-changing transitions (red/usplit/instances/gate_K64_n581, n 581); max W-changing / n 0.917;
  - R*_T > 0 in 58 games (max 5, red/fbx/instances/kt6_n58); W-flat transitions in 9 games (max 8, u23sw64_n32);
  - control: R88 FW-R* holds in every frozen phase (FWR-viol 0 in 719 games).
- READING: the stretch is long because of MANY short frozen phases. σ̄-changes are the main cut. So (FO) is a bound on the σ̄-changes
  of Odd's best reply while τ is frozen. That is N5-SF's SBC question localised to one τ-stretch. On dwN that count is 3 per stretch
  in plain N5 (dw_3: 26 = 4 frozen phases), where N5-SF's is exponential.
- One-player climbs (climb1p.py, n 10, 4 seeds × 1500 mutations, start σ_0 searched): best 9 / 27 = 0.33 of n + m. No kill.
### 1.4 Verdict for (a)
- FRAME-STRETCH (n + m form): DEAD (§1.5). FRAME-STRETCH_P = (FO): OPEN, reduced in §1.6. Not landed.
- No referee packet is proposed (task (d) does not apply).

### 1.5 Addendum (Lead 19:37Z, relaying L-RED 29): FRAME-STRETCH DEAD (DATA, reproduced here)
- Kill: L-RED's R106 family (docs/red/R106-quadratic-run.md) experiments/red/seg/mkr.py K m with its designed explicit start (SPEC S3 allows start pairs).
  One fallback-free run, τ constant (Iτ = ∅ at every state, so by box 21 Theorem B (c) the run IS F_τ), L = K(m + 3) − 1.
- My reproduction (box64/stretch.py --start, box64/mkr/; my S3-start corpus could not see it):
  | instance | n | n + m | σ-changes in the one τ-stretch | ratio | λ_W-changing transitions | σ̄-changes |
  | --- | --- | --- | --- | --- | --- | --- |
  | mk_4_16 | 102 | 253 | 76 | 0.300 | 76 | 1 |
  | mk_6_24 | 150 | 373 | 162 | 0.434 | 162 | 1 |
  | mk_8_32 | 198 | 493 | 280 | 0.568 | 280 | 1 |
  | mk_16_100 | 498 | 1225 | 1648 | 1.345 | 1648 | 1 |
- mk_16_100.pg sha1 49ba9a59…; the L-RED number (1648, ratio 1.345) is reproduced exactly. With m = 4K the stretch is Θ(n²).
- Obstruction: every transition changes λ_W (W-cycle node of some vertex). The stretch is n(n−1)-many one-step frozen phases, not
  one long phase. Lemma P / R17 (c)'s "< n + m per λ-phase" is still true per phase; the n + m form of FRAME-STRETCH confused a
  stretch with a phase (§1.2 (i)).
- Restated: CONJECTURE FRAME-STRETCH_P: every τ-stretch has at most poly(n, m) σ-changes (target O(n²(n + m)), the one-player R17 (d)
  shape). mkr is consistent with it (≤ n(n − 1) λ_W-cuts, §1.6).
### 1.6 Proposition STRETCH-CUT (PROVED, lane; a reduction of FRAME-STRETCH_P)
Let S be a τ-stretch. Write fb_S, SB_S for the S4c fallbacks and σ̄-changing transitions in S, R*_S for the largest R*_T of a frozen
W-phase of S (R88), FL_S for the W-flat transitions in S. Then
  |S| ≤ Q_S + (Q_S + 1)·((n − 1)(R*_S + 1) + FL_S),  Q_S ≤ fb_S + SB_S + n(n − 1) + n(n − 1)(fb_S + 1).
Proof.
- Cut S at every transition that is a fallback or changes σ̄, λ_Ξ or λ_W. The pieces are frozen W-phases (R88's definition: τ is
  constant in S). Q_S = the number of cut transitions.
- λ_Ξ: at most n(n − 1) changes in the whole run (R47 (a), as cited in R86).
- λ_W: at every arena (non-fallback) step of F_τ, W_{k+1} ⊵ W_k pointwise (box 21 Lemma W: σ_k lies in the arena and the arena
  optimum of the one-player game H dominates pointwise, R17 (a) F1). The cycle node is the first key component and rewards are
  injective, so between two fallbacks each vertex's W-cycle node changes at most n − 1 times: at most n(n − 1) λ_W-cuts per
  fallback-free piece.
- Each frozen W-phase has at most (n − 1)(R*_T + 1) W-changing transitions (R88 FW-R*), plus its W-flat ones. □
Consequences (READING).
- FRAME-STRETCH_P ⇐ fb_S, SB_S, R*_S, FL_S polynomial per stretch. On mkr all four are ≤ 1, and the n(n − 1) λ_W term is what grows.
- DATA (§1.3): on the 719 corpus the dominant cut is SB_S (σ̄), then λ_W; R*_S ≤ 5; FL_S ≤ 8.
### 1.7 The Lead's question: does R86 bound a fixed-τ stretch with NM*^U = 0? (READING, checked against R86's text)
- In a τ-stretch Odd makes no switch, so R86's Odd term contributes nothing there. But the stretch is still bounded only by Even's
  term: |S| ≤ n(n − 1) + (n(n − 1) + 1)·n·m_E·(P*_S + 1) (R86 COMPOSE on each λ-run meeting S; λ changes ≤ n(n − 1)).
- P* is NOT bounded by any landed result (R86: "none of which is bounded here"). So R86 gives FRAME-STRETCH_P only conditionally on P*
  (or NM*_Even via MATCH-Φ). On mkr, R106 reports NM = K, PCH = 2K − 1: polynomial there.
- R17 does not apply: G_τ is one-player, but F_τ's gate is honest (against σ̄), so F_τ is not switch-best on G_τ (box 21 Lemma PT).
- R38 / R47: R38's phases are on 𝒞^1O; R47 (a) bounds λ / λ^U changes (n(n − 1) each), not run length inside a λ-run.
- So "N5 is polynomial whenever min(#σ, #τ) is" is NOT landed with a polynomial factor. What holds: T ≤ (#τ)(F_E + 1) (Theorem B, lane),
  with F_E bounded only through STRETCH-CUT or P*.

### 1.8 Addendum (Lead 19:45Z / 19:52Z: prove FRAME-STRETCH_P under the mixed frame or say what it needs; written ~20:20Z)
Lemma GP*-RUN (PROVED, lane; R88's proofs read on a larger interval). Call a W-RUN a maximal run of consecutive states of one τ-stretch
with no S4c fallback and λ_W constant. σ̄ and λ_Ξ MAY change inside it. On every W-run, R88's Lemma GP* and Corollary FW-R* hold verbatim,
with "blocked at t" read at state t (W_t(z) ▷ W_t(ρ_t x), (x, z) ∉ Iσ_t). So a W-run has at most (n − 1)(R*_T + 1) W-changing transitions.
Proof: the R88 packet (docs/si/P-N5-GP-box31.md §2-§4) uses
- W-MON: its proof uses only τ_{t+1} = τ_t, "not a fallback", [S4a] and [F1] on H_t. "Inside a phase" (λ_Ξ constant) is never used.
- GP*: the base case, B1′ (ii), B2a, B2b use λ_W constant. Case A uses "not blocked" at state k, with Iσ_k of that state. Case B uses
  ρ̂ ∈ H_k. Nowhere σ̄ or λ_Ξ.
- FW-R*: GP*, W-MON, λ_W constant (the cycle node u of the ρ_{k+1}-play is a cycle node of state a), [S4a].
- σ̄ and D are used only in §3a (Corollaries GP, GP+), which this lemma does not need. □
DATA (box64/frozen.py --wrun, wrun_all.txt, 719 games): FW-R* on W-runs, 0 violations. W-runs up to 159 W-changing transitions
(si/runlin/instances/runfam_K40, n 79; 2.01n, with late adoptions). R*_T > 0 in 120 games (max 17, red/so/instances/so_j19_n48).
W-flat transitions in 10 games (max 8). mkr (mk_8_32): 281 W-runs of length 0; all 280 cuts are λ_W.
Fallbacks are NOT W-flat (DATA, box64/wdrop.py, wdrop_all.txt; 119 games with W-drops):
- arena steps never lower W (0 cases; box 21 Lemma W);
- 603 of 607 in-stretch fallbacks lower W; 121 of them change λ_W.
- So box 21 §2.5's OPEN "W-flatness of fallbacks" is false. A fallback can undo λ_W-progress.
Theorem STRETCH-RED (PROVED, lane; a reduction). Every τ-stretch S of N5 satisfies
  |S| ≤ Q + (Q + 1)·((n − 1)(R*_S + 1) + FL_S),  Q ≤ fb_S + n(n − 1)(fb_S + 1),  fb_S ≤ n(n − 1) + (n(n − 1) + 1)·(1 + (n − 1)(2 + ρ_S)),
with R*_S the most late-adoption transitions of one W-run of S, FL_S the W-flat transitions of S, and ρ_S the most Ξ-changes at Odd choice
vertices in one phase meeting S.
Proof.
- Cut S at fallbacks and λ_W-changes. The pieces are W-runs; apply GP*-RUN.
- λ_W-cuts: between two fallbacks W only rises (box 21 Lemma W, = W-MON), so each vertex's W-cycle node changes at most n − 1 times.
- fb_S: the phases ((λ_Ξ, τ)-constant runs, R38 (a)) meeting S number at most n(n − 1) + 1, since λ_Ξ changes at most n(n − 1) times
  (R47 (a)). Each phase has at most 1 + (n − 1)(2 + ρ) in-phase fallbacks (R56 FB-RED). A fallback that changes λ_Ξ is not in-phase;
  there are at most n(n − 1) such transitions. □
- So FRAME-STRETCH_P ⇐ ρ-POLY (R56's open conjecture, per phase) ∧ R*_S poly ∧ FL_S poly. The σ̄-changes, which are the dominant
  frozen-phase cut, drop out entirely.
- With L-SI 29's composition (Lead 19:52Z: G-N5-TIME ⇐ FRAME-STRETCH_P + poly NM*^U), G-N5-TIME ⇐ ρ-POLY ∧ R* poly ∧ FL poly
  ∧ NM*^U poly (READING; I have not read l-si 33f04452).
- What proving FRAME-STRETCH_P would take (READING):
  - (1) R*: a late adoption is an edge whose W-advantage the honest gate saw only later. Each needs Ξ(z) to rise past Ξ(ρ x)
    while W(z) was already ahead. A charge to Ξ-rises of z (R86 RISE) looks natural, but RISE is unbounded too.
  - (2) FL: W-flat σ-changes; R17 (c)'s "< m value-flat steps per phase" is the one-player template, not checked under the honest gate.
  - (3) ρ: Odd choice vertices' Ξ-changes per phase, open since R56.

## 2. (b) The mirror (DATA)
- Mirror: τ-changes inside one σ-stretch (σ constant), against n + m.
- 719 games (S3): 0 violations; max 0.104 (new/box54/out/d_hntop_n3: 22 / 211). τ-changes > σ-changes in 123 games.
- Global form #τ − 1 < (n + m)·#σ: 0 violations.
- Dualised / coupled families, own starts (dual_start.txt):
  - d_hntop_n8: σ constant; 291 τ-changes in one σ-stretch, 0.409 (n + m 711);
  - d_runquad_K8_m30_n192: 264, 0.551 (n + m 479);
  - d_s3quad_K3_m4: 21, 0.069; dewin_runquad_K3_m4: 21, 0.153;
  - relay_L3 / L10 / L10_s3: 2; ewin_runquad_K3_m4: 0.
- READING (not run): the dual of mkr (box54/mkdual.py) should kill the mirror's n + m form the same way; the mirror's poly form is
  FRAME-STRETCH_P on G^d.
- On the dualised families, σ never changes. So the whole run is one σ-stretch, i.e. Odd's own F_σ run on G^d. These are dual
  one-player-like runs below n + m, consistent with the mirror and with SB1′'s dual.

## 3. (c) What is still missing for G-N5-TIME
### 3.1 Lemma ENT-FREEZE (PROVED, lane; from ODD-FREEZE, FRAME-τ)
Let t → t + 1 be a transition of N5. Let (o, e) be an Odd edge with τ_t(o) ≠ e, satisfying box 63's H1 (or H1′), H2 and H3 at state t
("protected at t"). Then τ_{t+1}(o) ≠ e: the transition does not enter e at o.
Proof.
- Box 63 ODD-FREEZE: (o, e) ∉ Iτ_t.
- Every change of τ is a switch to Iτ edges (S4b's arena; S4c's Odd branch picks from Iτ), as in FRAME-τ / SF-TERM (i).
  So τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o). □
### 3.2 Corollary COMPOSE-FREEZE (PROVED, lane; R86 SW-RETURN and LEN-MONO, dual form, with ENT-FREEZE)
- Notation: λ^U-runs R as in R86. UNP_R = Odd edges (o, e) that are unprotected at some state t of R with t + 1 ∈ R.
  ENT_R(o, e) = R86's entries.
- (a) ENT_R(o, e) = 0 for (o, e) ∉ UNP_R (ENT-FREEZE at every transition of R).
- (b) ENT_R(o, e) ≤ 1 + RISE^U_R(e) ≤ n(PCH^U_R(e) + 1) for (o, e) ∈ UNP_R (R86 SW-RETURN, LEN-MONO on G^d).
- (c) Hence, Odd's switches in R satisfy Σ_o SW_R(o) ≤ Σ_{(o, e) ∈ UNP_R} n(PCH^U_R(e) + 1).
  - Summing over λ^U-runs: at most n(n − 1) transitions change λ^U (R47 (a) as cited in R86).
  - So C_τ ≤ n(n − 1) + (n(n − 1) + 1)·n·|UNP|·(P*^U_unp + 1). Here |UNP| ≤ m_O is the most unprotected Odd edges in one
    λ^U-run, and P*^U_unp is the most PCH^U_R(e) over targets e of unprotected edges.
- Check of the step "the Odd term of R86 COMPOSE-RUN, m_O(P*^U + 1), may be replaced by |UNP|(P*^U_unp + 1)": it uses only (a) and
  the per-edge form of SW-RETURN. R86's sum is already written per edge (o, e) with SW_R(o) > 0. □
### 3.3 What is missing (READING)
- Odd side: yes, it is "the τ-changes along unprotected Odd options". Exactly, it is P*^U_unp, the U-path-set changes of the TARGETS
  of unprotected Odd edges inside one λ^U-run.
  - Relation to NM*^U: R86 COMPOSE-NM bounds P*^U by (n²/2)(NM*^U + 1) + NM*^U through MATCH-Φ.
  - Restricting to unprotected targets needs MATCH-Φ's per-vertex form (PCH_R(c) bounded by c's own carries). I have not checked
    that R85 states it per vertex. If it does, the Odd term is NM*^U restricted to unprotected targets; if not, plain NM*^U.
  - Either way, protected options cost nothing, so a kill must clock Odd through UNPROTECTED options (box 63 §4).
- Even side: ODD-FREEZE says nothing. Two routes remain, and either one suffices:
  - R86 route: T ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + |UNP|(P*^U_unp + 1)). Missing: P* (or NM*_Even) AND P*^U_unp.
  - Theorem B route: T ≤ (C_τ + 1)(F_E + 1). Missing: F_E (= FRAME-STRETCH_P = (FO)) AND C_τ, i.e. P*^U_unp via 3.2.
  - So G-N5-TIME ⇐ (FO) ∧ (P*^U_unp polynomial). The mirror route ⇐ (FO)^d ∧ (P*_unp polynomial, Even's protection, dual of box 63).
- The class "all Odd options protected" (box 63 §3) is |UNP| = 0. Then C_τ ≤ n(n − 1) + m; with (FO), N5 is polynomial. Box 63's
  READING used FRAME-STRETCH; FRAME-STRETCH_P suffices.
- What a kill must do (READING): either make (FO) fail (many σ̄-changes of Odd's best reply inside one τ-stretch, each followed by
  a W-rise; DATA's dominant cut), or clock unprotected Odd options many times while Even's run stays short per stretch.

## 4. (d) Packet
- Not proposed: (a) did not close.
- ODD-FREEZE, ENT-FREEZE, FRAME-τ and COMPOSE-FREEZE are short and PROVED at lane level. A packet of those four would sign a
  REDUCTION (the Odd term of R86 restricted to unprotected options). It is the Lead's call whether that is worth a referee cycle.
  It would not close G-N5-TIME.

## DONE / FINDINGS / NEEDS
- DONE: box64/stretch.py, frozen.py, climb1p.py; stretch_all.txt, frozen_all.txt (719), dual_start.txt, frozen_dual.txt (8 coupled /
  dual instances, own starts); check.sh "box 64" pin; this note.
- FINDINGS:
  (0) DEAD: FRAME-STRETCH (n + m form), L-RED 29's mkr kill (R106 mkr.py, designed start), reproduced: mk_16_100 one τ-stretch of
  1648 σ-changes, n + m 1225 (§1.5). PROVED (lane): Proposition STRETCH-CUT (§1.6), (FO) ⇐ polynomial σ̄-changes, fallbacks, R*, flat
  steps per stretch. R86 bounds a stretch only through Even's P* (NM*^U = 0 does not help).
  (0b) PROVED (lane): Lemma GP*-RUN (R88's GP*/FW-R* hold on fallback-free λ_W-runs; σ̄, λ_Ξ may change; 0 / 719) and Theorem
  STRETCH-RED: FRAME-STRETCH_P ⇐ ρ-POLY ∧ R* poly ∧ FL poly (§1.8). DATA: fallbacks lower W (603 / 607); box 21's W-flat question is false.
  (1) READING: FRAME-STRETCH = box 21's (FO) with bound n + m. No landed result gives it. R17 bounds one λ-phase, and a τ-stretch has
  many. R88 bounds one frozen W-phase; σ̄-changes and fallbacks inside a stretch are unbounded.
  (2) READING: the n + m form contains SB1′ (one-player switch-best < n + m steps; open since box 8). The polynomial form (FO) is
  the real target, true on one-player games by R17 (d).
  (3) DATA: 0 / 719 violations (max 0.650). The longest stretch is up to 265 frozen phases, cut mostly by σ̄-changes (2277), then
  λ_W (1376), λ_Ξ (826), fallbacks (609). FW-R* control 0 violations.
  (4) DATA: the mirror has 0 / 719 violations (max 0.104); the dual families have σ constant and 264-291 τ-changes (≤ 0.551(n + m)).
  (5) PROVED (lane): Lemma ENT-FREEZE and Corollary COMPOSE-FREEZE. The Odd term of R86 restricts to unprotected options:
  P*^U_unp (NM*^U via MATCH-Φ). G-N5-TIME ⇐ (FO) ∧ (P*^U_unp polynomial).
- NEEDS: none from the owner.

## 5. BOX 65 start (Lead 20:00Z; σ̄ version superseded by §1.8, Lead told 20:09Z). Written ~20:25Z (date -u)
### 5.1 DATA: ρ per phase (box64/rho.py; rho_all.txt 719 games, rho_mkr.txt)
- ρ is counted as (Odd choice vertex, in-phase transition) pairs at which Ξ of that vertex changes. Control: R56 FB-RED holds in every
  phase (0 violations).
- 719 games: max ρ 225 (red/seg/instances/s3quad_K8_m30, n 479); max ρ / n 2.67 (nconf61_n48); max in-phase fallbacks 37 (rise_fb38_n48).
- mkr, own starts: ρ = 49, 121, 225, 961 at K = 4, 6, 8, 16, i.e. exactly (2K − 1)². With m = 4K this is Θ(n²) per phase
  (mk_16_100: 961 > n = 498). So any "ρ = O(n)" form is DEAD on mkr. ρ-POLY (R56) is untouched. mkr has 0 fallbacks, so its ρ does not
  enter STRETCH-RED's fallback term there.
### 5.2 READING: late adoptions charge to Ξ-rises, i.e. back to R86's RISE / P*
- A late adoption of (y, z) at transition u, blocked at t < u in the same W-run:
  - at t, (y, z) ∉ Iσ_t, i.e. Ξ_t(z) ⊴ Ξ_t(ρ_t y);
  - at u, the adoption needs (y, z) ∈ Iσ_u, i.e. Ξ_u(z) ▷ Ξ_u(ρ_u y).
- Ξ is pointwise non-decreasing along N5 (R15 (a), box 21 Lemma S (b)). If also Ξ_u(ρ_u y) ⊵ Ξ_t(ρ_t y), then Ξ(z) rose strictly in
  (t, u]. That holds when y is not on its own Ξ-cycle at t or u, by [V2]'s order-reflection.
- So, modulo that cycle case (not checked), R* ≤ Σ_{(y, z)} RISE_Ξ(z) over the W-run, and R86 LEN-MONO bounds RISE by path-set changes
  PCH. Hence the (FO) route, too, comes back to Even's P*, exactly the term of R86's route.
- READING: the two routes of §3.3 are not independent. Both need P* (or a sharper R* argument than "one Ξ-rise per late adoption").
### 5.3 Next (proposed)
- (a) Close the cycle case of 5.2. That would make R* ≤ m_E·(1 + max RISE_Ξ) a lane lemma.
- (b) Look for a charge of late adoptions to W-rises instead of Ξ-rises. W-rises inside a W-run are bounded by GP*'s propagation, and
  that would avoid P*. DATA first: is every late adoption preceded by a W-rise of z after the block?
### 5.4 (i) closed: Lemma LATE-RISE (PROVED, lane), the W-charge DEAD, and what it means (Lead 20:14Z approved the revised box)
Lemma SUCC-MON (PROVED, lane; R15 (a), [S4a], [S4c]). For every Even y, Ξ_k(σ_k(y)) is non-decreasing in k along every N5 run.
Proof. At each transition, σ_{k+1}(y) ∈ {σ_k(y)} ∪ Iσ_k(y): S4a's arena allows only these, S4c's fallback picks from Iσ_k, and a τ-only
transition keeps σ. If σ_{k+1}(y) = σ_k(y), then Ξ_{k+1}(σ_k y) ⊵ Ξ_k(σ_k y) by R15 (a) (Ξ pointwise non-decreasing). Otherwise
Ξ_{k+1}(σ_{k+1} y) ⊵ Ξ_k(σ_{k+1} y) ▷ Ξ_k(σ_k y), by R15 (a) and then [S2]. □ (This is the fact R106 §1 uses: "Ξ_t(σ_t v) is non-decreasing".)
Lemma LATE-RISE (PROVED, lane). If (y, z) ∉ Iσ_t and (y, z) ∈ Iσ_u with t < u, then Ξ_u(z) ▷ Ξ_t(z).
Proof. Ξ_u(z) ▷ Ξ_u(σ_u y) ⊵ Ξ_t(σ_t y) ⊵ Ξ_t(z): [S2] at u, SUCC-MON, and [S2] at t. □
- No cycle case arises; §5.2's caveat is removed. Being "blocked" is not used, only "not Ξ-improving at t".
Corollary R*-RISE (PROVED, lane). In a W-run F, the late adoptions of a fixed edge (y, z) number at most RISE_F(z), the Ξ-changes of z
inside F. Hence R*_T ≤ Σ_{z} indeg_E(z)·RISE_F(z) ≤ m_E·max_z RISE_F(z).
Proof.
- Every adoption at u is from Iσ_u (S4a, S4c). A late one has an earlier block at t, with (y, z) ∉ Iσ_t.
- LATE-RISE puts a Ξ-rise of z in (t, u]. Take t = the latest block before u: it comes after y's previous adoption of z, so the
  intervals of distinct late adoptions of (y, z) are disjoint. □
- With R86 LEN-MONO (RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1) on λ-runs) and at most n(n − 1) λ-changes (R47 (a)), R* is
  polynomial in P*.
DATA (box64/late.py, late_all.txt, 719 games): 1141 late adoptions; 1141 with a Ξ-rise of z since the latest block (LATE-RISE, as
proved); only 254 with a W-rise of z. So §5.3 (b), "charge late adoptions to W-rises", is DEAD (887 counterexamples; first instance
dw_3: 11 late adoptions, 2 W-rises).
### 5.5 READING: where this leaves the two routes
- (FO) ⇐ ρ-POLY ∧ P* poly ∧ FL poly (STRETCH-RED + R*-RISE).
- R86's route needs only P* ∧ P*^U_unp (COMPOSE-RUN with COMPOSE-FREEZE).
- So the Theorem B / FRAME line is SUBSUMED by R86's route: every premise it adds (ρ, FL) is extra, and it still needs P*.
  It would beat R86 only with a non-P* bound on R*, and the W-charge, the natural candidate, is DEAD.
- Recommendation to the Lead: the remaining target is P* (Even path-set changes per λ-run; NM* via MATCH-Φ) together with
  P*^U_unp. FRAME-STRETCH_P is no longer an independent half.
