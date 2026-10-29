# N5-STRETCH (box 64): FRAME-STRETCH is box 21's (FO), contains SB1′, and is not closed; the composition with ODD-FREEZE and R86
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 19:29Z (BOX 64 (a)-(d)).
Written 2026-10-29 from ~19:55Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
Labels: PROVED (lane) / DATA / READING / CONJECTURE / OPEN / DEAD.
- Engine: box21/n5x (plain N5, SPEC S1-S5), S3 start unless "own start" is said. Tools: experiments/new/box64/stretch.py, frozen.py,
  climb1p.py. Outputs: box64/stretch_all.txt, frozen_all.txt (719 games, box59/sbcg.lst), dual_start.txt, frozen_dual.txt.
- Read for this box: box 21 Theorem B (docs/new/N5-time-box21.md §2.4-§2.6), RESULTS R17, R86, R87, R88, N5-K8-box8.md §3b-§3c (SB1′).

## 1. (a) FRAME-STRETCH: not given by landed results, not closed, not killed
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
- FRAME-STRETCH: CONJECTURE (n + m form; contains SB1′). FRAME-STRETCH_P = (FO): OPEN. Neither landed nor killed.
- No referee packet is proposed (task (d) does not apply).

## 2. (b) The mirror (DATA)
- Mirror: τ-changes inside one σ-stretch (σ constant), against n + m.
- 719 games (S3): 0 violations; max 0.104 (new/box54/out/d_hntop_n3: 22 / 211). τ-changes > σ-changes in 123 games.
- Global form #τ − 1 < (n + m)·#σ: 0 violations.
- Dualised / coupled families, own starts (dual_start.txt):
  - d_hntop_n8: σ constant; 291 τ-changes in one σ-stretch, 0.409 (n + m 711);
  - d_runquad_K8_m30_n192: 264, 0.551 (n + m 479);
  - d_s3quad_K3_m4: 21, 0.069; dewin_runquad_K3_m4: 21, 0.153;
  - relay_L3 / L10 / L10_s3: 2; ewin_runquad_K3_m4: 0.
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
