# R-N5-LATEP: REFEREE report on packet P-N5-LATEP (L-SI box 53): LATE′, FW-R*′, LATE-SPLIT′ / CIRCLE′, GAP-CLIMB, CHAIN, TXC-DESCENT / TXC-RED
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 06:26Z (date -u). REFEREE-2 successor 22 reviews in parallel.
- Object and pin: docs/si/P-N5-LATEP-box53.md at claude/l-si b63f2554, `git show b63f2554:<path> | sha1sum` =
  b15223e53157d7d0a14767bb3c71dae07066a4da (204 lines); line docs/si/P-N5-LATEP-line.txt at b63f2554, sha1
  4a68934d832c483c5b28c552fd26526f7de4abea. Both equal the Lead's figures. Fixes go to docs/si/P-N5-LATEP-fixes.md.
- Runs 2026-10-30T06:27Z-06:32Z; report written 06:34Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ file opened for this packet.
- Premises opened: R88's object P-N5-GP at 170e5316 (§3 BLOCKED l. 85-86, §4 FW-R* and its proof l. 143-156); SPEC S4a; R17's object
  ([V1], [V2]); R89 (GP*-RUN, LATE-RISE, SUCC-MON); R90's object P-N5-CUT §2 (OPT-OFF (ii), W-SUCC; which I signed); R15; L-NEW box 70 §3 at
  170e5316 (the GXC definition; NOT landed: RESULTS R91 excludes boxes 70-71, l. 6545-6546).
- Quotes: my script scratch/cut_quotes.py finds 6/6 verbatim.
- Scope (D1): lemmas on one W-run of N5 on every game; REDUCTIONS and structural facts. No count is bounded; G-N5-TIME stays OPEN. Not a
  TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, premises | CHECKED; standing premise named (R57) ✓ |
| 2 | Definition LATE′ and its diff against R88 §4 | CHECKED: the diff is exactly «t ∈ [a, τ)» → «t ∈ [max(a, p + 1), τ)»; LATE′ ⊆ late, R*′_T ≤ R*_T, REP′_F ≤ REP_F ✓ |
| 3 | Corollary FW-R*′ | SIGNED (§3) |
| 4 | Lemma LATE-SPLIT′ (i), (ii) | SIGNED (§4) |
| 4 | Corollary CIRCLE′ (four inequalities and the ⟺) | SIGNED; X′_F depends on the choice of the blocked state t (any fixed choice works): LATEP-N2 |
| 5 | Lemma GAP-CLIMB | SIGNED (§5) |
| 6 | Proposition CHAIN | SIGNED |
| 7 | Lemma TXC-DESCENT | SIGNED (§7) |
| 7 | Corollary TXC-RED (and Σ_F LCT_F ≤ n(n − 1)) | SIGNED |
| 7 | closing sentence (Σ LATE′_F ≤ n_E·TXC_F + Σ_z d_E(z)·WZ_F(z) ≤ …) | SIGNED (d_E(z) ≤ n_E) |
| 8 | READING on R90 | not signed; one slip: «REP′* ≤ REP* ≤ T» should read «≤ n·T» (K1 gives REP* ≤ n·T): LATEP-N4 |
| 9 | the lane's symbol test | my own test in §9: one source is not landed and not pinned (GXC, box 70): LATEP-L1 |
| 10 | DATA, pins | not signed; pinned blocks «box 51»-«box 53» PASS; but box 52's «TXC 63» on so_th_n32 comes from a FRAME BUG in txcd.py (true count 73): LATEP-D1; «0 T4» is a tool artifact (no T4 test): LATEP-D2 |
| — | RESULTS line (4a68934d) | MATCHES §3-§7 and claims nothing more, after LATEP-L1 (required by the every-symbol rule) and two precisions (LATEP-L2, L3) |
No gap. Nothing FALSE in §2-§7. Two DATA defects in the lane's txcd.py (LATEP-D1 frame bug, LATEP-D2 no T4 test), affecting no proof.

## 2-3. LATE′ and FW-R*′
- Diff ✓ (R88 §4 quote verbatim; LATE′ replaces only the left end of the block window). An earlier LATE′ adoption is an earlier R88-late one,
  so REPEAT′ ⊆ P-N5-CUT's REPEAT ✓.
- FW-R*′ ✓. In R88's proof (l. 150-156) the blocked state is t = k − 1 − i ≥ a with ρ_{t+1}(y_i) ≠ y_{i+1} = ρ_{k+1}(y_i), so some adoption
  of (y_i, y_{i+1}) lies in (t, k]; τ := the first. The previous adoption p of that edge is < τ, not in (t, τ) (choice of τ), and p ≠ t
  (adoption at t would give ρ_{t+1}(y_i) = y_{i+1}): so p + 1 ≤ t, and the block at t is in LATE′'s window [max(a, p + 1), τ) ✓. k − τ ≤ k − t
  − 1 = i ≤ n − 2 as in R88; the charging is unchanged. GP*-RUN carries R88's proof to every W-run ✓.

## 4. LATE-SPLIT′, CIRCLE′
- (ii) ✓. Between the previous adoption p and u no adoption of (y, z) occurs, so y leaves z exactly once in (p, u) — at k — and the LATE′
  block t ∈ [p + 1, u) has σ_t(y) ≠ z, hence t ≥ k + 1 (y holds z on [p + 1, k]). Chain: OPT-OFF (ii) at k → k + 1 ((y, z) = (y, σ_k y) ∈
  H_k, off-cycle at k + 1), W-SUCC on [k + 1, t] (off-cycle on [k + 2, t]; F lies in one τ-piece, P-N5-CUT's frame τ* = τ, W^τ = W), blocked at
  t: W_t(z) ▷ W_{k+1}(z) ✓ (so t ≥ k + 2 automatically). W-silent and SELF repeats are excluded ✓ (the block lies after the leave).
- CIRCLE′ ✓: REP′ ≤ n_E·R*′ (≤ n_E adoptions per transition); R*′ ≤ #LATE′ = FIRST′ + REP′ ≤ m_E + REP′; for one edge the intervals
  [k + 1, u − 1] of distinct REPEAT′s are disjoint (k > p ≥ the previous REPEAT′'s u), so a non-X′ REPEAT′ gets its own W(z)-change: per edge
  ≤ WCH_F(z), summed over the d_E(z) edges into z ✓; FW-R*′. The ⟺ ✓ (WCH_F(z) ≤ WCH_F; X′ ≤ REP′).
- LATEP-N2: X′_F is defined with "t a blocked state as in the definition of LATE′". If several blocked states exist, X′ depends on the choice
  (existential and universal readings differ); the inequality holds under every fixed choice (the chain needs only off-cycle on [k + 1, t]
  for the t used). Fix one, e.g. the EARLIEST blocked state of [p + 1, u) (smallest window, smallest X′), as for P-N5-GAP's CL (H4).

## 5. GAP-CLIMB
✓. (y, z) ∈ Iσ_u ([S4a]: F's transitions are S4a steps, σ_{u+1}(y) = z ≠ σ_u(y)); (y, z) ∉ Iσ_{t_b} (blocked); LATE-RISE (R89): Ξ_u(z) ▷
Ξ_{t_b}(z), so a first change s ∈ [t_b, u − 1] exists and is a strict rise (R15). z ∈ Z_s: Ξ_s(z) = Ξ_{t_b}(z) ⊴ Ξ_{t_b}(σ_{t_b} y) ([S2], not
improving, total order) ⊴ W_{t_b}(σ_{t_b} y) (XW) ◁ W_{t_b}(z) (blocked) ⊴ W_s(z) (W-MON on F) ✓. Disjointness: t_b(u) ≥ p + 1 ≥ u′ + 1 for the
previous LATE′ adoption u′ ✓. (The LATE′ window is what makes the tokens distinct: MUT 5, R88-late adoptions in its place, BITES.)

## 6. CHAIN
✓. GXC ⊆ TXC by W-MON (⊴ and ⊵ give equality); TXC ⊆ ZXC by XW; the split by "W(z) changes" ✓; WZ_F(z) ≤ WCH_F(z) ✓.

## 7. TXC-DESCENT, TXC-RED
- Step ✓: for a non-terminal TXC event (x, s), c := λ_Ξ(x) at s and s + 1 (not T1); x ≠ c (a cycle node's value is (x, ∅, 0) at both
  states); x's successor y is the same in the (σ_t, σ̄_t)- and (σ_t, τ)-plays for t = s, s + 1 (Even: not T2; Odd: not T3, so σ̄_s(x) = τ(x) =
  σ̄_{s+1}(x)); [V1] at both states for Ξ (x not its own Ξ-cycle node) and for W (not T4); [V2] strict both ways turns the Ξ-climb into a
  Ξ-climb at y and the W-equality into a W-equality at y ✓. The walk follows z's (σ_{s+1}, σ̄_{s+1})-lasso and reaches its cycle node c
  before any repetition; a non-terminal c would be its own Ξ-cycle node at s + 1 and, not T1, at s: no climb, contradiction ✓. T2 with λ_Ξ
  fixed is a GXC event verbatim (τ fixed on F, x_j ∈ Z_s by CHAIN, W equal) ✓.
- TXC-RED ✓: the map (z, s) ↦ (x_j, s) has fibres of size ≤ n; at λ_Ξ-fixed s every terminal is T2 (GXC), T3 (GATE) or T4 (CNW); at
  λ_Ξ-changing s at most n TXC events (the packet's n² is a weaker valid bound); Σ_F LCT_F ≤ the λ_Ξ-changing transitions of the run ≤ n(n − 1)
  (R47 (a); rewards injective, Ξ non-decreasing) ✓.
- MUT 3 (no T3) and MUT 4 (no T4): MUT 3 BITES (22,586 descents fail: the gates are where the descent breaks, as §10 reads); MUT 4 never bites (dropping T4, the 36 T4-terminated descents continue to a later T2 / T3 terminal): the T4 case is needed by the proof ([V1] for W fails at an own W-cycle node) but not exhibited (LATEP-N5).

## 8. Notes
- LATEP-N1 (standing premise): named (R57) ✓; OPT-OFF (i)'s R17 (a) (F1) + R57 (a) chain is inherited from R90 (P-N5-CUT K2).
- LATEP-N2: X′_F's blocked state t (above).
- LATEP-N3 (naming): the line labels CIRCLE′'s three inequalities «(Lemma LATE-SPLIT′)»; the packet calls them Corollary CIRCLE′.
- LATEP-N4 (§8 READING, not signed): «The converse (fixes K1) is unaffected, since REP′* ≤ REP* ≤ T» — K1 gives REP* ≤ n·T, not ≤ T. The
  conclusion (the converse holds) stands.
- LATEP-N5 (premise not exhibited): T4 is used by the proof but dropping it never bites in my data (MUT 4).
- LATEP-D2 (DATA): §10's «0 T4» is a tool artifact: txcd.py has no T4 test (its kinds are T1, T2G/T2L, T3 only; it walks past own W-cycle
  nodes). My engine finds 36 TXC descents that end at a T4 terminal (CNW 110 TXC events at own W-cycle nodes).
- LATEP-D1 (DATA tool defect): experiments/si/odd/txcd.py, after a τ-changing transition, keeps w0 := W(σ_{s}, τ_OLD) (it stores w1 = W(ns,
  t) computed with the old τ, then sets t := nt), so the FIRST transition after each τ-change compares W_{s+1} (new τ) with W(σ_s, old τ): the
  tied test and the λ_W-change test use the wrong frame there. On so_th_n32 (S3) it reports TXC 63 / T3 63; the true count is 73 (my engine,
  and a frame-by-frame reproduction of the lane's comparison gives exactly the lane's 63; the 10 missing TXC events sit at s = 1, right after
  the τ-change 0 → 1). latep.py resets its W-run on a τ-change and is not affected (my counts equal its pins: wdepth LP 37 / REPP 21,
  tiedmut LP 6 / REPP 1). §10's "TXC descent failures 0" is unaffected in substance (my corrected sets: 0 failures), but the pinned «TXC 63 …
  T3 63 … GATE 15» in check.sh «box 52» should be re-derived after the fix. No proof uses DATA.

## 9. My strict symbol test of the line (4a68934d)
Every symbol, and where it is bound:
- IN the line: F, W-run's gloss (τ, λ_W constant, no S4c fallback), τ, λ_Ξ, n, n_E, m_E, d_E(z), adoption (y, z, u), LATE′ (t, p), REPEAT′,
  R*′_T, REP′_F, X′_F (k, t), WCH_F, WCH_F(z), Z_s, D_s (o), s and «transitions of F», ZXC_F(z), TXC_F(z), WZ_F(z), GATE_F, CNW_F (x),
  LCT_F, TXC_F / ZXC_F as sets, "a set stands for its number".
- By a named LANDED source: N5 / SPEC S1-S5 (Ξ_t, σ̄_t, Iσ_t, ⊴, ▷, S4c); R57 (premise); R89 (W-run, W_t, λ_W); R88 (BLOCKED); P-N5-CUT §2
  = R90's object (off-cycle).
- LATEP-L1 (REQUIRED by the every-symbol rule): «GXC_F the GXC events (v, s) of L-NEW box 70 §3 (docs/new/N5-SC-box70.md)» cites a file that is
  NOT landed (RESULTS R91 excludes boxes 70-71) and gives no commit, so the symbol's meaning is not fixed. The packet's §9 table calls it
  "landed"; it is not. Fix: inline the definition (the packet quotes it, box 70 @ 170e5316 l. 48-49): «GXC_F the pairs (v, s) with v Even,
  σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v)» (τ_{s+1} = τ_s holds on F).
- LATEP-L2 (precision): X′_F's «t a blocked state as in the definition of LATE′» — fix the choice (LATEP-N2).
- LATEP-L3 (precision): name the landed premises the lemmas use, as K15 / H18 do: R15, R17 (a), R47 (a), R88 (W-MON, XW, GP*, FW-R*), R89
  (GP*-RUN, LATE-RISE), R90 (OPT-OFF (ii), W-SUCC); and label the three inequalities «(Lemma LATE-SPLIT′, Corollary CIRCLE′)» (LATEP-N3).
- Displayed inequalities: each equals the packet's (§3, §4, §5, §6, §7). The scope tail matches.
Verdict on the line (Opus 5.5, D15): MATCHES; NOT YET landable by the every-symbol rule until LATEP-L1; L2, L3 are precisions.

## 10. Pinned checks and own control
- Pinned: experiments/si/check.sh l. 845-860 («box 51», «box 52», «box 53») in a clean `git worktree add --detach` at b63f2554: three PASS
  lines, exit 0 (3 s). The «box 52» so_th pin reproduces the lane's tool, including its frame defect (LATEP-D1).
- Own control: docs/referee/scratch/latep_probe.py (rl_engine; no lane code), on the lane's corpus (sbcg.lst, 719 games, + wdepth_K4_m16 and
  tiedmut_so_th_n32_11 with their starts; given start and S3; n ≤ 120): 672 games (49 with n > 120 skipped), 767 runs, 13,205 transitions, 1,089 W-runs of length ≥ 1: 0 violations of SUB (LATE′ ⊆ late),
  FW-R*′, LATE-SPLIT′ (ii) (unique leave; block after the leave; W-rise), CIRCLE′ (all four), GAP-CLIMB (1,500 LATE′ adoptions; s exists, z ∈
  Z_s, strict climb; distinct tokens; #LATE′ ≤ ZXC_F(z)), CHAIN (ZXC 28,114 = TXC 23,975 ⊔ WZ 4,139; GXC 198 ⊆ TXC), TXC-DESCENT (23,975 descents:
  terminals T1 497, T2 319, T3 23,123, T4 36; every step a TXC event; every T2 with λ_Ξ fixed a GXC event), TXC-RED, Σ LCT ≤ n(n − 1).
  REPEAT′s are rare: 2 (both off-cycle, X′ 0) against 1,520 R88-late adoptions, 1,500 LATE′.
- MUTs: 1 (LATE-SPLIT′ (ii) on R88-late REPEATs: the block may precede the last leave) BITES, 20; 2 (GAP-CLIMB's s searched from a) BITES,
  490 (+2 token collisions); 3 (no T3) BITES, 22,586; 4 (no T4) never; 5 (GAP-CLIMB on R88-late adoptions) BITES, 20 token collisions.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/latep_probe.py, latep_logs/.
- FINDINGS: every PROVED item of §3-§7 SIGNED; no gap; LATE′'s diff against R88 exactly as stated; line MATCHES but needs LATEP-L1 (GXC cites an
  unlanded, unpinned file); DATA tool defects LATEP-D1 (txcd.py frame bug: so_th TXC 73, not 63) and LATEP-D2 (no T4 test; 36 T4 terminals exist); notes LATEP-N1..N5.
- NEEDS: Lead: route LATEP-L1..L3, N2..N4, D1 to L-SI (docs/si/P-N5-LATEP-fixes.md); the §C word after REFEREE-2 22's report.
