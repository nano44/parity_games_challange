# R-N5-FRAME: REFEREE report on packet P-N5-FRAME (L-NEW box 65): Odd-side freeze and fixed-τ stretch reductions for N5 on every game
Referee: REFEREE (successor 18), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 2026-10-29 20:56Z by date -u). REFEREE-2 successor 21 reviews in parallel.
- Object and pin: docs/new/P-N5-FRAME-box65.md at claude/l-new 938d87967ce501058bc6d015e506403c73858034, `git show <commit>:<path> | sha1sum` =
  ce8c4803ee18dc90ee761863d006d0aca0476542, 194 lines; RESULTS line docs/new/P-N5-FRAME-box65-line.txt sha1 acf3234f840cb682d71444501e89cfd61247dcd6.
  Both equal the Lead's figures. Fixes go to docs/new/P-N5-FRAME-fixes-box65.md.
- Runs 2026-10-29T20:58Z-21:05Z; report written 21:06Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no REFEREE-2 FRAME file opened.
- Premises opened: SPEC at 9905dac3 (l. 28-57; the packet's 8 SPEC quotes checked by my own script: 8/8 verbatim, "…" elisions as parts);
  RESULTS at c9045f86: R85 (c) l. 5108-5109 (quote verbatim), R86 (e) l. 5345-5357, R56 (l. 2832, (f) l. 2865), R47 (Lemma Φ (a), (c)), R15
  (a), (c), (d), R17 (a); R88 and its object P-N5-GP (reviewed by me: R-N5-GP.md, §C R-N5-GP-C.md).
- Scope (D1): a REDUCTION for plain N5 on every game. Nothing bounds N5's iteration count; G-N5-TIME stays OPEN. Not a TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, premises, new definitions (τ-stretch, W-run, PROTECTED, PCH^U) | CHECKED |
| 2.1 | Lemma FRAME-τ (i)-(iv) | SIGNED |
| 2.2 | Lemma DUAL-ORDER | SIGNED |
| 2.3 | Lemma ODD-FREEZE | SIGNED (every inequality direction checked, §2; standing premise FR-N1) |
| 2.4 | Lemma ENT-FREEZE | SIGNED |
| 2.5 | Corollary COMPOSE-FREEZE (a)-(d) | SIGNED |
| 2.5 | Corollary COMPOSE-FREEZE (e) | SIGNED: [R86e] suffices (§3) |
| 3.1 | Lemma SUCC-MON | SIGNED |
| 3.2 | Lemma LATE-RISE | SIGNED |
| 3.3 | Lemma GP*-RUN (R88's GP* and FW-R* on W-runs, σ̄ and λ_Ξ free) | SIGNED: no step of R88's W-MON, GP*, FW-R* uses σ̄, D or λ_Ξ (§4) |
| 3.4 | Corollary R*-RISE | SIGNED |
| 3.5 | Theorem STRETCH-RED | SIGNED (fallback count checked, §5) |
| 3.5 | its "Consequence (to sign as stated)" | SIGNED |
| — | RESULTS line (box65-line.txt) | MATCHES §2-§3; claims nothing more; every hypothesis carried (§6) |
| 4 | READING, DATA | not signed; pinned checks reproduced EXACTLY (§7) |
No gap. Nothing FALSE. Notes FR-N1..N6.

## 1. FRAME-τ, DUAL-ORDER
- FRAME-τ ✓. (i) [S4a] verbatim. (ii) S4b's arena H′ keeps Odd o's edges to {τ(o)} ∪ Iτ(o); S4c's Odd branch picks from Iτ; S4c's Even branch
  and S4a leave τ. (iii) the distinct τ-values form a VJ00 run on G^d (each change Switch_I, ∅ ≠ I ⊆ Iτ, R15 (d)), so R15 (c) on G^d: no repeat.
  (iv) Iτ is defined from U = Ξτ on G^d, a function of τ ([S1-dual], R15 (d) mirrored). ✓
- DUAL-ORDER ✓. Ω + 1 preserves the (Ω, v) order, so ranks and triples agree. I re-derived the reversal: reward_d(c) = −reward(c) − 1 (Ω(c)
  even: 2r → −(2r + 1); odd: −(2r + 1) → 2r), so distinct cycle nodes reverse; signed weights negate (each sign is the parity of Ω, which flips);
  the length rule flips with c's parity. Strict "better for Even in G" ⇔ strict "worse for the G^d-Even player". (Same as REFEREE-2's N-GS-2,
  R2-N5-MPGS-s20.) Data: 0 violations in 110,975 value pairs (DUAL).

## 2. ODD-FREEZE: every inequality direction (special care (2))
Write ⊴ for G's order (Even's view), ⊴_d for G^d's (the G^d-Even player = Odd); DUAL-ORDER: X ◁ Y ⇔ Y ◁_d X.
- Play decomposition ✓: the (τ, σ_e)-play from e is P_e (ending at o, simple by (H1′)), then τ(o), then the (τ, σ_e)-play from τ(o). By (H2) the
  (τ, τ̄)-play from τ(o) never enters P_e; Odd vertices follow τ in both; at Even vertices outside P_e, σ_e = τ̄ (H1′): induction gives the same
  play π_o, disjoint from P_e, so the lasso's cycle is π_o's, cycle node w ∉ P_e. Path set P_o ∪ {y ∈ P_e : rank(y) > rank(w)}, length |P_e| + ℓ_o
  (P_e's vertices are the |P_e| steps from e to τ(o)). ✓
- Direction 1: V := val(τ, σ_e)(e) ▷ π_o's value U(τ(o)) in G's order: same cycle node w; the P-sets differ exactly in {y ∈ P_e above w}, whose
  top is x (H3: x is the top of P_e and above w) with Ω(x) even, in the larger set: DELTA gives weight rise, i.e. better for Even ✓.
- Direction 2: U(e) ⊵ V in G's order: τ̄ is the G^d-Odd optimum, minimising ⊴_d at every vertex at once ([S1-dual] with [S1-Xi]'s "minimising
  … at every vertex at once"), i.e. (DUAL-ORDER) maximising ⊴ among all positional Even α; σ_e is one such α ✓. (Uses that τ̄ realises U as
  (τ, τ̄)-play values: FR-N1.)
- So U(e) ▷ U(τ(o)) in ⊴, hence U(e) ◁_d U(τ(o)) (DUAL-ORDER, strict). [S2] on G^d: (o, e) ∈ Iτ needs U(e) ▷_d U(τ(o)). Not the case ✓.
- Note: G^d's U-triples are the same triples as G's (DUAL-ORDER), so "U(τ(o)) = π_o's value" is literal. Every inequality points the right way.
- ENT-FREEZE ✓: (o, e) ∉ Iτ_t and τ_t(o) ≠ e with FRAME-τ (ii).
- Hypothesis controls (my data, §7): dropping (H3)'s "more relevant than w" (MUT 1) or "Ω(x) even" (MUT 3) BITES (454 + 175 / 586 + 374
  violations of the Lemma / of ENT, random n 5-12); dropping (H2) (MUT 2) never bites (as for GATE-SHUT's (H2): MPGS J1). (H2) is used by the
  proof (the play decomposition); its necessity is not exhibited (FR-N2).

## 3. COMPOSE-FREEZE, and (e) on [R86e] (special care (1))
- (a) ✓: an entry at t → t + 1 inside R needs τ_t(o) ≠ e = τ_{t+1}(o); for (o, e) ∉ UNP_R it is protected at that t, and ENT-FREEZE excludes it.
  (b) ✓ R86 SW-RETURN (dual, any stretch) then LEN-MONO (dual, λ^U-run): 1 + PCH + (PCH + 1)(n − 1) = n(PCH + 1). (c) ✓. (d) ✓: ≤ n(n − 1)
  λ^U-changing transitions ([R47a], R47 Lemma Φ (b)/(c), every game); the rest lie inside ≤ n(n − 1) + 1 λ^U-runs, each with an Odd switch.
- (e): does [R86e] suffice? YES. What (e) needs is, for ONE vertex e and ONE λ^U-run R, MATCH-Φ's per-vertex bound read on G^d:
  PCH^U_R(e) ≤ (K(K+1)/2)(NM^U_R(e) + 1) + NM^U_R(e), K = ranks above rank(λ^U(e)) ≤ n − 1. [R86e] (l. 5345-5357) records both referees' signed
  cells: the λ-run replacement "HOLDS" because MΦ's proof reads verbatim with c fixed, and for λ^U-runs "it holds for U on G^d (… MATCHED is
  then read with G^d's parities)" (my R-N5-COMPOSE §6; REFEREE-2 §2.5 / N-C3, F3). MΦ (R85 (c)) is itself a per-vertex statement (PCH_𝒫(v),
  NM_𝒫(v)), and its proof uses only "c = λ(v) fixed" for that v; on a λ^U-run λ^U(e) is fixed. So the per-vertex form on λ^U-runs is exactly
  what was signed (P*_R in R86 (e) is the max over vertices of this per-vertex bound). Condition: NM^U is read with G^d's parities (R86 (e)'s
  F3), which the packet says ([R86e]: "with NM^U read with G^d's parities (F3)"). ✓

## 4. GP*-RUN: R88's proofs on W-runs (σ̄ and λ_Ξ free)
I reviewed R88 (R-N5-GP.md) and recorded then (GP-N2) that GP*'s proof uses only τ constant, no S4c transition, λ_W constant. Re-checked line
by line for W-runs:
- W-MON: "inside a phase" enters only through τ_{t+1} = τ_t (true on a τ-stretch) and "not a fallback" (W-run); then [STEP] makes σ change, σ_new
  is S4a's one-player optimum of H_t ∋ σ_t, [F1]. λ_Ξ never used ✓.
- GP*: base and B1′(ii), B2a, B2b(i), (iii) use λ_W constant; Case A uses "not blocked at state k" with Iσ_k at that state (blocked is
  state-local); Case B uses ρ̂ ∈ H_k and W-MON. No σ̄, D, λ_Ξ ✓.
- FW-R*: GP*, W-MON, λ_W constant (u a W-cycle node of state a), S4a's ρ_{t+1}(y) ∈ {ρ_t(y)} ∪ Iσ_t(y) (no fallback) ✓.
- σ̄, D, U_t, S_{d,t}, λ_Ξ appear only in R88 §3a (GP, GP+), not restated ✓. So GP*-RUN is a true widening of R88, with R88's final
  hypotheses (G12: paths of G_τ, ≤ k − a edges, W-cycle node of the W-run's first state) carried "verbatim".
- Data: 0 violations on 2,257 W-runs (pins + library), of which 224 contain a σ̄-change and 10 a λ_Ξ-change (the widening is exercised);
  MUT 4 (no blocked condition) bites on ccl_w48_n48 at [15, 18], as in R88.

## 5. SUCC-MON, LATE-RISE, R*-RISE, STRETCH-RED (special care (3))
- SUCC-MON ✓ (= R86 SW-RETURN's Ξ-SUCC, signed): σ_{t+1}(y) ∈ {σ_t(y)} ∪ Iσ_t(y); R15 (a) pointwise; [S2] for the switch.
- LATE-RISE ✓: Ξ_u(z) ▷ Ξ_u(σ_u y) ⊵ Ξ_t(σ_t y) ⊵ Ξ_t(z), the last since (y, z) ∉ Iσ_t and ⊴ is total (or z = σ_t(y)).
- R*-RISE ✓: t_1 = a blocked state (∉ Iσ), t_i = u_{i−1} + 1 (σ(y) = z there, so ∉ Iσ); t_i < u_i since σ_{u_i}(y) ≠ z; each adoption is
  from Iσ_{u_i} (S4a, no fallback in F); LATE-RISE gives a Ξ(z)-change in [t_i, u_i); intervals disjoint, inside F. Note RISE_F counts Ξ-changes
  (not W): correct, LATE-RISE is about Ξ. R*_T ≤ Σ_{(y,z)} late(y,z) ≤ Σ_z d_E(z)·RISE_F(z) ✓.
- STRETCH-RED ✓:
  - |S| = all transitions of S change σ (τ constant, [STEP]). Q-transitions (fallback or λ_W-change) cut S into ≤ Q + 1 W-runs; each W-run
    has ≤ (n − 1)(R*_S + 1) W-changing (GP*-RUN) plus W-flat transitions (≤ FL_S in total; Q-transitions double-counted at worst): the bound ✓.
  - Q ≤ fb_S + n(n − 1)(fb_S + 1): on a fallback-free piece W rises pointwise (W-MON: τ constant, no fallback), so each vertex's W-cycle node
    strictly rises in reward at each change (injective), ≤ n − 1 per vertex per piece ✓.
  - fb_S (the fallback count from R56 and R47 when τ is constant): every S4c transition inside S is an EVEN fallback (an Odd fallback sets some
    τ(v) to an improving w ≠ τ(v), so it would leave S) — the packet leaves this implicit (FR-N3). With τ constant, phases ((λ_Ξ, τ) constant,
    R38 (a)) inside S are separated only by λ_Ξ-changes, ≤ n(n − 1) of them on the whole run (R47 Lemma Φ (c), every game), so ≤ n(n − 1) + 1
    phases meet S, each lying inside S (phases need τ constant and S is a maximal τ-constant run). A fallback transition that does not change
    λ_Ξ has both states in one phase: in-phase, counted by R56 (f) (≤ 1 + (n − 1)(2 + ρ) per phase, every game, ρ ≤ ρ_S). The others change
    λ_Ξ: ≤ n(n − 1). fb_S ≤ n(n − 1) + (n(n − 1) + 1)(1 + (n − 1)(2 + ρ_S)) ✓.
- Consequence ✓: RISE_F(z) ≤ (λ_Ξ-changing transitions in F, ≤ n(n − 1)) + Σ over the ≤ n(n − 1) + 1 λ-run pieces of F of RISE there ≤ n(PCH_R(z)
  + 1) (LEN-MONO on the piece, a stretch with λ constant: R86 N-C2); Σ_z d_E(z) = m_E. So R*_S ≤ m_E(n(n − 1) + (n(n − 1) + 1)n(P + 1)), P the
  largest PCH_R(z) over λ-runs R meeting S: polynomial in n, m_E, P ✓ (the packet's parenthetical omits the n(n − 1) λ-change term: harmless,
  "each λ-change is one transition" covers it).

## 6. The RESULTS line (special care (4))
Clause by clause against §2-§3: FRAME-τ (i)-(iv) ✓; ODD-FREEZE with (H1′) [positional σ_e = τ̄(τ) outside P_e; the play reaches o before
repeating; P_e up to and including o], (H2), (H3) [top of P_e even, above the cycle node of the (τ, τ̄(τ))-play from τ(o)] ✓, conclusion
(o, e) ∉ Iτ ✓; ENT-FREEZE ✓; COMPOSE-FREEZE (a), (b), (d), with (e) cited as "R85 (c)'s per-vertex MATCH-Φ on λ^U-runs (the premise R86 (e)
signs as holding)" ✓ ((c) omitted: the line may claim less); SUCC-MON, LATE-RISE ✓; GP*-RUN "R88's Lemma GP* and Corollary FW-R* hold on every
W-run (σ̄ and λ_Ξ need not be constant there)" ✓ (R88's own final hypotheses carried by reference); R*-RISE ✓; STRETCH-RED's three inequalities
and every symbol (fb_S, R*_S, FL_S, ρ_S) ✓; DUAL-ORDER and the Consequence are not in the line (it claims less) ✓. Scope tail (NM^U on unprotected
targets, R*_S, FL_S, ρ_S unbounded; G-N5-TIME open) ✓. MATCHES; no hypothesis missing. Optional: say "NM^U read with G^d's parities (R86 (e) F3)"
(FR-N4).

## 7. Re-runs and own control
- Pinned, clean worktree at 938d8796, `python3 -I`, read first (box59/freeze2.py b71e8e9c…, box64/frozen.py 7c47dd61…, box64/stretch.py
  ddd2328a…, dw_3.pg 67eb4bff…): check.sh l. 291-314 run alone, exit 0: «box 63 ODD-FREEZE: dw_3 81 hypothesis hits, 0 improving: PASS»,
  «box 64 STRETCH: … PASS», «box 64 FRAME-STRETCH DEAD family: mk_4_16 one tau-stretch of 76 sigma-changes: PASS», «box 64 GP*-RUN: dw_3 one
  W-run of 26 W-changing transitions, 4 late adoptions, FW-R* holds: PASS». All exactly as check.sh asserts.
- Own control: scratch/frame_probe.py (sha1 af5f7e99…) on my engine rl_engine (no lane code): FRT, DUAL, ODD-FREEZE / ENT-FREEZE (every state,
  Odd o, e: DFS for an (H1′) witness path, then (H2), (H3); assert (o, e) ∉ Iτ and τ_{t+1}(o) ≠ e), SUCC-MON, LATE-RISE (all t < u, runs ≤ 150),
  W-runs: W-MON, GP* (capped DFS), FW-R*, R*-RISE; STRETCH-RED's three inequalities per τ-stretch (ρ_S in its SMALLEST reading: transitions of
  the phase at which some Odd choice vertex's Ξ changes, so the check is the strictest).
  | corpus (frame_logs/) | runs | transitions | ODD-FREEZE hits / pairs | LATE-RISE checks | W-runs (σ̄ / λ_Ξ change inside) | GP* path checks | τ-stretches (max length; max fb_S) | violations |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | pins: dw_3, mk_4_16 (+ start), ccl_w48_n48, rlin_cex_n40 (+ start); given + S3 + 1 random (pins) | 10 | 249 | 130 / 1,730 | 17,665 | 153 (2 / 0) | 23,409 | 20 (76; 33) | 0 |
  | library (rho_probe.lib(), n ≤ 40; given + S3) (lib) | 321 | 5,798 | 8,450 / 60,682 | 378,188 | 2,104 (222 / 10) | 257,358 | 821 (105; 24) | 0 |
  | random rand_ck n 5-14, 3,000 games, S3 + 1 random (rand3000) | 6,000 | 9,817 | 6,621 / 81,243 | 5,154 | 14,872 | 33,542 | 11,495 (6; 1) | 0 |
  mk_4_16's τ-stretch of 76 and dw_3's 4 late adoptions are reproduced by my engine. R*-RISE: 644 edge checks, 0 violations; max R*_T 11 (library).
- Controls: MUT 1 (no "above w") and MUT 3 (no "even") BITE on ODD-FREEZE / ENT-FREEZE; MUT 4 (no blocked condition) BITES on GP*-RUN
  (ccl_w48_n48, 17); MUT 2 (no (H2)) does not bite (FR-N2).

## 8. Notes (for L-NEW's fixes file; none changes a verdict)
- FR-N1 (standing premise). ODD-FREEZE's direction 2 uses that τ̄(τ) is the G^d-Odd optimum at every vertex at once AND realises U as the
  (τ, τ̄)-play values (R57 (b)'s premise, mirrored on G^d; cf. P-N5-SF F7). Name it with [S1-dual].
- FR-N2 ((H2)). Its necessity is not exhibited in my data (MUT 2: 0), as for GATE-SHUT (MPGS J1). It is used by the proof; nothing to change.
- FR-N3 (STRETCH-RED). Say that every S4c transition inside a τ-stretch is an Even fallback (an Odd fallback changes τ), which is what lets R56
  (Even in-phase fallbacks) count fb_S.
- FR-N4 (RESULTS line, optional). Add "NM^U read with G^d's parities (R86 (e), F3)" to the COMPOSE-FREEZE (e) clause.
- FR-N5 (Consequence). The parenthetical's count omits the ≤ n(n − 1) λ_Ξ-changing transitions of a W-run in RISE_F(z); harmless (polynomial).
- FR-N6 (GP*-RUN wording). "R88's Lemma GP* … verbatim, with F in place of the frozen W-phase" should name the hypotheses it inherits (R88's
  final line, G12: paths of G_τ, ≤ k − a edges, end a W-cycle node of the W-run's first state), since the earlier R88 wording dropped two of them.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/frame_probe.py, frame_inputs/ (copies from l-new 938d8796 and l-si d072bb28), frame_logs/; pinned box 63/64 blocks
  re-run exactly.
- FINDINGS: all ten items and the Consequence SIGNED, no gap, nothing FALSE; [R86e] suffices for COMPOSE-FREEZE (e) (per-vertex, λ^U-run, G^d
  parities); every ODD-FREEZE inequality points the right way; STRETCH-RED's fallback count is right (all in-stretch fallbacks are Even); the
  RESULTS line matches and carries every hypothesis.
- NEEDS: Lead: the FRAME §C word when REFEREE-2 reports; route FR-N1..N6 to L-NEW.
