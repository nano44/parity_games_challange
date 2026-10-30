# P-N5-WRUN fixes (box 92; APPEND-ONLY). Frozen packet docs/new/P-N5-WRUN-box92.md (sha1 fae68aa0…) and line docs/new/P-N5-WRUN-box92-line.txt (sha1 0faa5b80…) at l-new 7668bc9b are NOT edited; errata and cross-reads are given here.
L-NEW successor 39 (Opus 5.5), D14 / D18. Newest entry last.

## Entry 1 (2026-10-30 16:34Z by date -u): CONJECTURE BIP-REL-1 DEAD (L-RED successor 34, R143 §5, l-red 717f407a, docs/red/R143-settle.md). Lead 16:34Z: «Open docs/new/P-N5-WRUN-fixes-box92.md (append-only) with an erratum: BIP-REL-1 DEAD (instance, SHA).»
### L-RED's text (verbatim, R143-settle.md l. 121-130)
> - DATA (strictrel.py = L-RED R142b; relpe.py STRICT=1 = L-NEW box 89's own counter on its n5x engine; xeng; Oink zlk + verify):
> 
>   | pin | n | iterations | strict releases of (y, z) in one frozen stretch | relpe frozen_edge | xeng | Oink |
>   | --- | --- | --- | --- | --- | --- | --- |
>   | rel2/instances/rel2_R2_n82 | 82 | 10 | 2 | 2 | identical | OK |
>   | rel2/instances/rel2_R4_n322 | 322 | 22 | 4 | 4 | identical | OK |
>   | (generator only) R = 3, 6 | 183, 714 | 16, 34 | 3, 6 | — | — | — |
> 
> - DEAD: CONJECTURE BIP-REL-1 (≤ 1 strict release per edge per frozen stretch). Instance rel2_R2_n82, edge (y, oz).
>   - The family gives R strict releases of ONE edge in ONE stretch at n ≈ 20R², so R° ≥ ⌊√(n/20)⌋.
### Reproduction (L-NEW, own counter)
- experiments/red/rel2/instances/rel2_R2_n82.pg sha1 064a8309e6fe1052a09c929f5f02d5118de7731d, .start sha1 2988324fb0f300b4407bc076e1473d5ce16deb7e
  (read from l-red 717f407a; sha1s equal L-RED's pins.sha1). `STRICT=1 python3 -I new/box89/relpe.py rel2_R2_n82.pg rel2_R2_n82.start`
  (from experiments/): «RELPE n 82 mE 55 runs 1 maxima {'late_edge': 2, 'rstar': 2, 'F': 10, 'frozen_edge': 2} argmax-edge (81, 80)».
  One W-run, two strict releases of edge (81, 80) in one frozen stretch: BIP-REL-1 is DEAD. Obstruction (L-RED): box 90's one-line
  obstruction realised with one-player delay chains as a clock (τ-branch climb, then ρ-branch climb, twice).
### Errata to the frozen packet
- §12: CONJECTURE BIP-REL-1 is DEAD (instance above; family R strict releases at n ≈ 20R², so R° ≥ ⌊√(n/20)⌋ there).
- §3.3 row E10 («BIP-REL-1 ∧ SB-POLY ∧ FL-POLY ⇒ WRUN-POLY (under [SUB])»): still a true implication, now VACUOUS (its premise is false).
- §9 last bullet («With CONJECTURE BIP-REL-1 (§12) R° ≤ m_E»): void. BIP-RED itself is unaffected; it needs R°-POLY (R° ≤ p(n)), not
  R° ≤ m_E. Row E8 (WRUN-POLY ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY under [SUB]) is unaffected. R143's family has R° ≈ √(n/20): polynomial.
- §13 DATA «BIP-REL-1 0 violations (box89/relpe.py STRICT=1)» holds for the 1132-run corpus only; DEAD row to add: BIP-REL-1, rel2_R2_n82.
- The line (0faa5b80) does not state BIP-REL-1 as a hypothesis or conclusion except in «BIP-REL-1 … are open» (the status parenthesis):
  read «BIP-REL-1 is DEAD (L-RED R143)». A revised line will be issued if the Lead asks.
- CONJECTURE BIP-POLY is NOT killed (R143's runs are short: 10 / 22 iterations).

## Cross-reads (lane level; NOT packet changes) — Lead 16:34Z: «Note these in the fixes file as cross-reads, not packet changes.»
### L-SI successor 33, l-si 78788761, docs/si/N5-GATE-box51b.md §11 (verbatim, l. 308-318)
> - Lemma RETURN-CHARGE′ (PROVED, lane). In ANY stretch of an N5 run (S4a steps, τ-changes and S4c fallbacks alike), let Even v leave d at k1
>   and re-adopt d at k2 > k1. Then Ξ_{k2}(d) ▷ Ξ_{k1}(d).
>   - The hypotheses of §10.3 (λ_Ξ fixed, v not its own Ξ-cycle node) are dropped.
>   - Proof. Every Even switch at j goes to an edge of Iσ_j: S4a's arena is σ_j ∪ Iσ_j, and S4c picks from Iσ_j (n5x.py step()). So the
>     sequence j ↦ Ξ_j(σ_j(v)) is non-decreasing.
>     - Without a switch at j, it is one vertex, and Ξ is pointwise non-decreasing (R15 (a), (d)).
>     - With a switch a → b at j: Ξ_{j+1}(b) ⊵ Ξ_j(b) ▷ Ξ_j(a).
>   - Hence Ξ_{k2}(d) ▷ Ξ_{k2}(σ_{k2}(v)) ⊵ Ξ_{k1+1}(σ_{k1+1}(v)) ▷ Ξ_{k1}(d). □ (This replaces §10.3's reflection through v ⊕ ·.)
> - Corollary SEG-XCH (PROVED, lane). For every segment [p, q] of a run, let SWT := the transitions of [p, q] that switch some Even vertex.
>   Then SWT ≤ m_E + Σ_d d_E(d)·XCH_{[p,q]}(d).
>   - A switch either adopts an edge v has not held in [p, q] (≤ deg(v) − 1 per v), or is a return.
- L-NEW reading: RETURN-CHARGE′ is the no-hypothesis form of RET-ΞRISE (packet §5.1) and of landed R86 SW-RETURN's chain; Corollary
  SEG-XCH (i) is packet §3.2 XI-RUN, derived independently (L-SI via a direct return count, L-NEW via R86 SW-RETURN). RX = 0 in both. Two
  independent derivations of the same bound; the packet's form needs only landed lemmas.
### L-RED successor 34, R143 §1, l-red 717f407a (verbatim, R143-settle.md l. 39-47)
> - (C) Count. Every transition of I switches some Even vertex. Inside a window only vertices outside C switch (a CN switch is an event).
>   So a window has at most D := max{layer(v) : v switches in I} transitions, and |I| ≤ E_I + (E_I + 1)·D = (D + 1)(E_I + 1) − 1. □
> - Corollary INT-LIN-EF (PROVED, lane). An event-free W-constant interval has |I| ≤ D ≤ n − 1. That covers in particular every interval
>   with σ̄ frozen, no CN switch and every upward head's Ξ constant.
> - Corollary SETTLE-RED (PROVED, lane). E_I ≤ SBF_I + CN_I + Σ_(u ∈ U*) XCH_I(u), where U* := ∪_k U_k (|U_k| ≤ #Odd + |C|), SBF_I is the
>   number of σ̄-changing transitions and CN_I the number of CN switches. Hence [P-INT] ⇐ «in-interval Ξ-changes at upward heads, σ̄-flips
>   and CN switches are polynomial».
>   - This sharpens L-SI's INT-XCH (Σ over EVERY vertex d, weighted by its in-degree) to the heads alone.
>   - It replaces CONJECTURE LAYER-RESET's mixed-radix bound Π_d(1 + m_d) by a product (D + 1)(E_I + 1).
- L-NEW reading: Lemma SETTLE (lane, modulo L-SI's Claim RG and L-LIT's LEX-BFS / IDX-MONO) sharpens packet §11 INT-XCH⁰ (all vertices,
  in-degree weights) to E_I (σ̄ flips, CN switches, Ξ-changes at upward heads). It bears on row E11 ([P-INT] ⇐ …) only; not in the packet.

## Entry 2 (2026-10-30 16:47Z by date -u): REFEREE successor 20 report R-N5-WRUN (claude/referee 8c0b2e69, docs/referee/R-N5-WRUN.md): every packet item SIGNED, [SUB] checked independently, no packet gap; the LINE does not match yet (G-WRUN-1, WRUN-L1, WRUN-L2) plus notes WRUN-N1..N4. Lead 16:47Z: «Add WRUN fixes entry 2 and line revision L-1, quoting each item verbatim … Also: the status parenthesis now reads BIP-REL-1 as DEAD (rel2_R2_n82, l-red 717f407a).»
### G-WRUN-1 (REFEREE, verbatim, R-N5-WRUN.md l. 187-203) — GAP in the line; the packet is right
> - G-WRUN-1 (GAP in the line; the packet is right). The line defines blocks as «(X, g) not improving and the (σ_t, σ̄_t)-play from g reaching
>   X, E0 iff X is the cycle node of Ξ_t(X) and every vertex of the route is below X». §4.1 also requires:
>   - g ≠ σ_t(X);
>   - «If X lies on the cycle Z* of its own (σ_t, σ̄_t)-play, π is also required to avoid Z*».
>   WAIT-CYCLE′'s Case 2 uses the second requirement (c* ∉ C). Without it, a REG "block" can have c* on C, so Claim A (rew(top C) < rew(c*))
>   fails and the proof gives nothing.
>   - FALSE as worded (instance). docs/referee/scratch/wrun_logs/wc_line_cex.pg (sha1 a8a5013bbb4860a2d700b0f554b065b08487d65a; n 4;
>     0: prio 6, Odd → 3; 1: prio 1, Even → 1, 3; 2: prio 0, Even → 1, 3; 3: prio 3, Even → 0, 1, 2), N5 from the best-reward start.
>   - At state 0, σ_0(3) = 0, and the (σ_0, σ̄_0)-play of X = 3 is the cycle {3, 0} with cycle node c* = 0 ≠ X.
>   - Take g := 0 = σ_0(X). (X, g) is not improving, and the play from g reaches X with route π = [0]. X is not the cycle node of Ξ_0(X), so
>     under the line's wording the block is not E0, i.e. it is REG.
>   - At state 1, σ_1(3) = 0 again and π has no Even vertex, so «σ never again has X → g together with the block's choices on π» fails at t = 1.
>   - Under the packet's §4.1 definition this is not a block at all: g = σ_0(X), and π meets Z*.
>   - My probe with the line's definition (MUT 5) finds 21 such recurrences on nep92_n40 and 8 on 100 random games of n ≤ 6. With the packet's
>     definition: 0.
>   Fix: restore both clauses in the line's block definition, e.g. «… (X, g) not improving, g ≠ σ_t(X), and the (σ_t, σ̄_t)-play from g
>   reaching X along a route that avoids the cycle of X's own play when X lies on it, …».
- Applied in L-1: the block definition now reads «a self-routed block of (X, g) at state t: (X, g) not improving, g ≠ σ_t(X), and the
  (σ_t, σ̄_t)-play from g reaching X, its vertices before X (the route) pairwise distinct and, when X lies on the cycle of its own
  (σ_t, σ̄_t)-play, avoiding that cycle; E0 iff …» = packet §4.1. Recorded as a line error of successor 39 (the packet was right).
### WRUN-L1 (REFEREE, verbatim, l. 204-206)
> - WRUN-L1 (FREE SYMBOL). In «(Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED) with fixed cycle node the first k signed path-set terms are
>   non-decreasing … and PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v)», k is not quantified, and DEEP_{k,F}'s definition in the parenthesis uses the
>   same free k. Fix: «for every k ≥ 1, …».
- Applied in L-1: «for every k ≥ 1, DEEP_{k,F}(v) counts …» in the definitions, and «(Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED) for
  every k ≥ 1: …».
### WRUN-L2 (REFEREE, verbatim, l. 207-209)
> - WRUN-L2 (UNBOUND ORDER). «the first k signed path-set terms are non-decreasing» names no order on terms. §7.2's order (plus terms by rank
>   upwards, NONE, minus terms by rank downwards; prefixes lexicographic) must be stated, or the clause dropped. LEVEL-RED's inequality does not
>   need it.
- Applied in L-1 (order stated, = packet §7.2): «the first k terms of the path set of Ξ(v) in decreasing rank, each signed + (even priority)
  or − (odd priority), padded with NONE and compared lexicographically with terms ordered by (r, +) above (r′, +) iff r > r′, every (r, +)
  above NONE above every (r′, −), and (r, −) below (r′, −) iff r > r′, are non-decreasing in t and take at most (2n + 1)^k values».
### WRUN-N1 (REFEREE, verbatim, l. 51-54)
> - WRUN-N1 (Fact EXT). «strictly order-preserving and order-reflecting» needs y ∉ P(x) for both arguments. If y lay in one path set and not
>   the other, adding y would change the symmetric difference. Every use satisfies y ∉ P:
>   - REL2-WRISE (i): y's plays to z and to h avoid y, by (A2) and (A1);
>   - TRIPLE-RED / RSTAR-PCH / RETURN-CHARGE: v is not its own cycle node, so the successor's play does not revisit v.
- Erratum to packet §1 Fact EXT (the line does not state EXT): read «ext(y, ·) is strictly order-preserving and order-reflecting on values
  whose path sets do not contain y». Every use satisfies this (REFEREE's list above).
### WRUN-N2 (REFEREE, verbatim, l. 139-142)
>   - WRUN-N2: RESULTS R91 Lemma LATE-W (landed) already states «in a piece, if v leaves c at s → s + 1 and (v, c) is blocked at a later state
>     t′ of the piece, with v not its own W-cycle node on [s + 1, t′], then W_{t′}(c) ▷ W_{s+1}(c)». That is REL2-WRISE's conclusion without
>     (A2) and without the frozen-stretch / strict-release setting. REL2-WRISE's second conclusion, Ξ_q2(z) ⊴ Ξ_q2(h2), is the definition of
>     BLOCKED. Suggest citing R91 LATE-W instead (used by no reduction, as the packet says).
- Applied in L-1: premise list «R91 (Lemmas XW, W-MON, W-SUCC, LATE-W)», and the REL2-WRISE clause ends «(a special case of RESULTS R91
  Lemma LATE-W, which needs neither (A2) nor the frozen stretch)». REL2-WRISE stays as stated (signed); it is used by no reduction.
### WRUN-N3 (REFEREE, verbatim, l. 70-74)
>   - E7 ⇐: FL_F = Σ_I |I| over the WCH_F + 1 maximal W-constant intervals of F (I checked this counting step myself: the transitions of the
>     W-constant intervals are exactly the FL transitions), then E4. ⇒: |I| ≤ |F| ✓. This direction needs [P-INT] to be read on W-constant
>     intervals OF W-RUNS. The line does that («a W-constant interval I of F is a maximal run of states of F with W constant»). L-SI's own
>     wording, «every W-constant interval of every run» (packet l. 108), would allow intervals that span W-run boundaries (a τ-change or
>     fallback that keeps W), and those are not bounded by |F|. WRUN-N3: say «of a W-run» at l. 108 as the line does.
- Erratum to packet l. 108: read [P-INT] as «every W-constant interval of every W-run has ≤ p(n) transitions». L-1 states it so explicitly:
  «[P-INT] := for a polynomial p, every W-constant interval of every W-run has at most p(n) transitions».
### WRUN-N4 (REFEREE, verbatim, l. 79-80)
> - WRUN-N4. «XI-CH-POLY ⇒ R*-POLY, FL-POLY, SB-POLY and WRUN-POLY ⇒ R3-POLY are one-way» (line) could be read as "the converse is false".
>   The packet means only that no converse is proved (E10's «as far as known»). Suggested: «… are proved in one direction only».
- Applied in L-1: «… and WRUN-POLY ⇒ R3-POLY are proved in one direction only».
### Status parenthesis (Lead 16:47Z)
- Applied in L-1: «…, BIP-POLY, INT-LIN and the other POLY statements are open; CONJECTURE BIP-REL-1 is DEAD (L-RED R143, rel2_R2_n82,
  l-red 717f407a)». Row E10 is not in the line; entry 1's errata stand.
### Revised line L-1 (also stored as docs/new/P-N5-WRUN-box92-line-L1.txt; sha1 in the commit message and the Lead report)
### R?? [proposed, P-N5-WRUN, revision L-1] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even v keeps {σ_t(v)} ∪ Iσ_t(v), Odd follows τ_t)); premises RESULTS R15 (a), (b), (d), R86 (a) (Lemma SW-RETURN), R88 (Lemma GP*, Corollary FW-R*), R89 (Lemmas SUCC-MON, GP*-RUN, Corollary R*-RISE), R91 (Lemmas XW, W-MON, W-SUCC, LATE-W) and R93 (Fact LEX, Lemma NEW-BOUND); a run is the sequence of states (σ_t, τ_t) from any start pair; a transition is written t → t + 1 (states t, t + 1); n the number of vertices, n_E the number of Even vertices, m_E the number of edges leaving Even vertices and d_E(c) the number of Even vertices with an edge to c; v is switched at t if σ_{t+1}(v) ≠ σ_t(v), and then enters (adopts) σ_{t+1}(v) and leaves σ_t(v); Ξ_t := Ξ_{σ_t} (SPEC S1: the [S1-val] valuation of the (σ_t, σ̄_t)-plays, σ̄_t Odd's pointwise-optimal counterstrategy to σ_t), a value (c, P, ℓ) having cycle node λ = c, path set P and length ℓ; W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays and val(ρ, τ) that of the (ρ, τ)-plays; λ_W the cycle-node map of W_t; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Iσ_t Even's improving edges (SPEC S2); a τ-stretch and a W-run F = [a, b] as in RESULTS R89, |F| := b − a its transitions; blocked edges, late adoptions and R*_F (R88's R*_T read on F) as in RESULTS R88 / R89; for a stretch R of consecutive states, ENT_R(v, c), SW_R(v) and RISE_R(c) as in RESULTS R86 (entries of v into c, switches of v, transitions changing Ξ(c)), |R| its transitions; for a W-run F, ΞCH_F(c) := RISE_F(c), WCH_F(c) the transitions of F changing W(c), WCH_F those changing W somewhere, FL_F those changing W nowhere, TIE_F as in RESULTS R93, PCH_F(c) the transitions of F changing the path set of Ξ(c) but not its cycle node, P*_F := max_c PCH_F(c); for a per-W-run quantity Q_F (maximised over vertices or edges when indexed by them), Q-POLY means: there is a polynomial p with Q_F ≤ p(n) for every W-run F of every N5 run on every game from every start pair, and WRUN-POLY := |F|-POLY, XI-CH-POLY := (max_c ΞCH_F(c))-POLY; for an Even edge (X, g), a return of X to g is a transition of F at which X enters g having held g at an earlier state of F, RET_F(X, g) their number, and REG_F(X, g), E0_F(X, g), FREE_F(X, g) the returns whose window (from X's last leave of g) contains a state with a REG self-routed block of (X, g), else an E0 one, else neither (P-N5-WRUN §4.1: a self-routed block of (X, g) at state t: (X, g) not improving, g ≠ σ_t(X), and the (σ_t, σ̄_t)-play from g reaching X, its vertices before X (the route) pairwise distinct and, when X lies on the cycle of its own (σ_t, σ̄_t)-play, avoiding that cycle; E0 iff X is the cycle node of Ξ_t(X) and every vertex of the route is below X in the SPEC S1 rank); a change of the path set of Ξ(v) with fixed cycle node has depth the number of path-set vertices above the most relevant vertex of the symmetric difference, and, for every k ≥ 1, DEEP_{k,F}(v) counts the changes of depth ≥ k in F; a frozen stretch Φ of F is a maximal interval of states of F with σ̄ constant, SB_F the transitions of F changing σ̄, R°_Φ the transitions of Φ adopting an edge blocked at an earlier state of Φ and R° := max_Φ R°_Φ; [SUB] := for every sub-interval F′ of every W-run, at most (n − 1)(R*_T(F′) + 1) transitions of F′ change W, R*_T(F′) the transitions of F′ adopting an edge blocked at an earlier state of F′; a W-constant interval I of F is a maximal run of states of F with W constant, XCH_I(d) the transitions of I changing Ξ(d); R*-POLY, FL-POLY, P*-POLY, DEEP_k-POLY, TIE-POLY, SB-POLY and R°-POLY are Q-POLY for these Q, R3-POLY := (max_e WCH_F(e))-POLY, ALT-POLY := (max REG_F)-POLY, FREE-POLY := (max FREE_F)-POLY and [P-INT] := for a polynomial p, every W-constant interval of every W-run has at most p(n) transitions): (Theorem XI-RUN) every stretch R of consecutive states of a W-run has |R| ≤ Σ_v SW_R(v) ≤ m_E + Σ_c d_E(c)·RISE_R(c), so every W-run F has |F| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c) and every W-constant interval I has |I| ≤ m_E + Σ_d d_E(d)·XCH_I(d) (Corollary INT-XCH⁰); (Lemmas WAIT-CYCLE′, E0-BOUND, Theorem TRIPLE-RED) after a REG self-routed block of (X, g) with route π, σ never again has X → g together with the block's choices on π, E0_F(X, g) ≤ n, and |F| ≤ m_E + Σ RET_F ≤ m_E(n + 1) + Σ_{(X, g)} REG_F(X, g) + Σ_{(X, g)} FREE_F(X, g); (Lemma RET-ΞRISE, Theorem FREE-RED) RET_F(X, g) ≤ ΞCH_F(g) and FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F; (Lemmas GAP-DEV, ΞCH-PCH, Theorem RSTAR-PCH) a target z of an edge blocked at q has Ξ_q(z) ◁ W_q(z) and an Odd vertex o with σ̄_q(o) ≠ τ(o) on its (σ_q, σ̄_q)-play, ΞCH_F(z) ≤ n(n + 1 + PCH_F(z)) and R*_F ≤ Σ_{(y, z)} ΞCH_F(z) ≤ m_E·n·(n + 1 + P*_F); (Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED) for every k ≥ 1: while the cycle node of Ξ(v) is fixed, the first k terms of the path set of Ξ(v) in decreasing rank, each signed + (even priority) or − (odd priority), padded with NONE and compared lexicographically with terms ordered by (r, +) above (r′, +) iff r > r′, every (r, +) above NONE above every (r′, −), and (r, −) below (r′, −) iff r > r′, are non-decreasing in t and take at most (2n + 1)^k values, and PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v); (Lemmas BIP-MON, NO-DEV) on a frozen stretch with σ̄ ≡ ρ both val(σ_t, ρ) and val(σ_t, τ) are non-decreasing, and if Ξ_t = W_t at every state of F then R*_F = 0 and |F| ≤ (n − 1) + 4n²(n − 1); (Theorem BIP-RED, an implication from [SUB]) |F| ≤ SB_F + (SB_F + 1)(n − 1)(R° + 1) + FL_F; (Lemma REL2-WRISE, under (A1) y not its own W-cycle node on [s + 1, q2] and (A2) the τ-play from z under σ_{s+1} with y → z avoiding y) if (y, z) has a strict release in a frozen stretch, y leaves z at s and (y, z) is blocked again at q2 > s in it, then W_q2(z) ▷ W_{s+1}(z) (a special case of RESULTS R91 Lemma LATE-W, which needs neither (A2) nor the frozen stretch); and (Corollary WRUN-EQ) WRUN-POLY ⇔ XI-CH-POLY ⇔ P*-POLY ⇔ DEEP_k-POLY (each fixed k ≥ 1) ⇔ R*-POLY ∧ FL-POLY ⇔ ALT-POLY ∧ FREE-POLY ⇔ R3-POLY ∧ TIE-POLY ⇔ R*-POLY ∧ [P-INT], and, under [SUB], ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY, while XI-CH-POLY ⇒ R*-POLY, FL-POLY, SB-POLY and WRUN-POLY ⇒ R3-POLY are proved in one direction only (2026-10-30) — REDUCTIONS and EQUIVALENCES (none of these quantities is bounded here; WRUN-POLY, XI-CH-POLY, BIP-POLY, INT-LIN and the other POLY statements are open; CONJECTURE BIP-REL-1 is DEAD (L-RED R143, rel2_R2_n82, l-red 717f407a); W-runs are not whole runs; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)

## Entry 3 (2026-10-30 17:24Z by date -u): REFEREE-2 successor 23 report R2-N5-WRUN (claude/referee-2 a281189a, docs/referee-2/R2-N5-WRUN.md): every item SIGNED, no gap, nothing FALSE in the signed items; L-1's content MATCHES; one REQUIRED line fix (R2-L-1), precision R2-L-2..L-5, packet notes R2-N-1, R2-N-2. Lead 17:24Z: «Add WRUN fixes entry 3 and line revision L-2, quoting each item verbatim.»
(REFEREE-2's labels L-1 … L-5, N-1, N-2 are written R2-L-1 …, R2-N-… here, to keep them apart from this file's line revisions.)
### R2-L-1 (REQUIRED; REFEREE-2, verbatim, R2-N5-WRUN.md l. 128-131)
> - **L-1 (REQUIRED).** REL2-WRISE: «if (y, z) has a strict release in a frozen stretch …»: «strict release» is not bound in the line. The
>   line defines R°_Φ («the transitions of Φ adopting an edge blocked at an earlier state of Φ») but not the term. Fix: «if (y, z) is adopted
>   at a transition of a frozen stretch Φ at which it had been blocked at an earlier state of Φ (a strict release), y leaves z at s and
>   (y, z) is blocked again at q2 > s in Φ, then …». Alternatively drop that hypothesis: the proof never uses the release.
- Applied in L-2 (REFEREE-2's first fix, keeping the hypothesis as signed): «if (y, z) is adopted at a transition of a frozen stretch Φ at
  which it had been blocked at an earlier state of Φ (a strict release), y leaves z at s and (y, z) is blocked again at q2 > s in Φ, then …».
### R2-L-2 (REFEREE-2, verbatim, l. 132-133)
> - L-2 (precision). τ is unbound in two clauses: GAP-DEV «σ̄_q(o) ≠ τ(o)» (read τ_q) and BIP-MON «val(σ_t, τ)» (the W-run's τ). Elsewhere
>   the line writes τ_t.
- Applied in L-2: GAP-DEV «a target z of an edge blocked at a state q of a W-run has … σ̄_q(o) ≠ τ_q(o) …»; BIP-MON «on a frozen stretch of a
  W-run with σ̄ ≡ ρ and τ_t ≡ τ (the W-run's Odd strategy) both val(σ_t, ρ) and val(σ_t, τ) are non-decreasing».
### R2-L-3 (REFEREE-2, verbatim, l. 134-135)
> - L-3 (precision). «[P-INT] := for a polynomial p, every W-constant interval …» should read «there is a polynomial p such that every …»
>   (as in the packet's Q-POLY).
- Applied in L-2: «[P-INT] := there is a polynomial p such that every W-constant interval of every W-run has at most p(n) transitions».
### R2-L-4 (REFEREE-2, verbatim, l. 136)
> - L-4 (precision). RSTAR-PCH «Σ_{(y, z)}»: «over Even edges (y, z)».
- Applied in L-2: «R*_F ≤ Σ_{(y, z) Even edge} ΞCH_F(z) ≤ …».
### R2-L-5 (REFEREE-2, verbatim, l. 137)
> - L-5 (precision). «REG self-routed block» relies on «else an E0 one»; a REG block could be said explicitly to be one that is not E0.
- Applied in L-2: «a REG (that is, not E0) self-routed block» in the definitions and «a REG (not E0) self-routed block» in WAIT-CYCLE′.
### R2-N-1 (REFEREE-2, verbatim, l. 46-53)
> - **N-1 (Fact EXT, FALSE as worded).** «ext(y, ·) is strictly order-preserving and order-reflecting» fails when y lies in the path set of
>   one argument. Instance: c with p′(c) < p′(y), x := (c, {y}, ℓ), x′ := (c, ∅, ℓ): x ≠ x′, but ext(y, x) = ext(y, x′) = (c, {y}, ℓ + 1). Its
>   justification («either both arguments gain y or neither … the symmetric difference … unchanged») assumes y ∉ P(x) ∪ P(x′). My tool
>   counts such pairs among Ξ-values actually met (control X_EXT_GLOBAL, hundreds of pairs, §4). TRUE with that hypothesis. The two uses
>   satisfy it: §10 (i) applies it to W_{s+1}(h) and W_{s+1}(z), whose plays avoid y by (A1) and (A2); the quoted RETURN-CHARGE (§2.3, not
>   signed) applies v ⊕ · to values of plays avoiding v. The second sentence («Ω(v) = ext(v, Ω(succ))» off own cycle node) is correct, and
>   there y ∉ P(Ω(succ)) holds automatically (the successor's play reaches the cycle node before v). Fix: add «for values x, x′ with
>   y ∉ P(x) ∪ P(x′)». No signed item changes.
- Packet erratum (§1 Fact EXT; supersedes entry 2's WRUN-N1 wording, same content): read «for values x, x′ with y ∉ P(x) ∪ P(x′), ext(y, ·)
  is strictly order-preserving and order-reflecting». Every use satisfies it (REFEREE-2's list). The line does not state EXT (checked: no
  «ext(» in L-1 or L-2), so no line change.
### R2-N-2 (REFEREE-2, verbatim, l. 61-62)
>   ⇒ REG, FREE ≤ RET ≤ |F|. ✓ E6: R93 NEW-BOUND; ⇒ WCH_F(e) ≤ |F|, TIE_F ≤ n_E·|F|. ✓ (N-2: «R3-POLY» is used in E6, E13 and §12 but defined
>   only in the line, as (max_e WCH_F(e))-POLY; with that definition E6 and E13 check.)
- Packet erratum (§3.3 rows E6, E13 and §12): R3-POLY := (max_e WCH_F(e))-POLY, i.e. there is a polynomial p with WCH_F(e) ≤ p(n) for every
  W-run F and vertex e (as in the line; = box 83's CONJECTURE R3-POLY quoted in box 84 §1).
### Revised line L-2 (also stored as docs/new/P-N5-WRUN-box92-line-L2.txt; sha1 in the commit message and the Lead report)
- Changes from L-1: the heading tag and the eight phrase edits above; nothing else.
### R?? [proposed, P-N5-WRUN, revision L-2] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even v keeps {σ_t(v)} ∪ Iσ_t(v), Odd follows τ_t)); premises RESULTS R15 (a), (b), (d), R86 (a) (Lemma SW-RETURN), R88 (Lemma GP*, Corollary FW-R*), R89 (Lemmas SUCC-MON, GP*-RUN, Corollary R*-RISE), R91 (Lemmas XW, W-MON, W-SUCC, LATE-W) and R93 (Fact LEX, Lemma NEW-BOUND); a run is the sequence of states (σ_t, τ_t) from any start pair; a transition is written t → t + 1 (states t, t + 1); n the number of vertices, n_E the number of Even vertices, m_E the number of edges leaving Even vertices and d_E(c) the number of Even vertices with an edge to c; v is switched at t if σ_{t+1}(v) ≠ σ_t(v), and then enters (adopts) σ_{t+1}(v) and leaves σ_t(v); Ξ_t := Ξ_{σ_t} (SPEC S1: the [S1-val] valuation of the (σ_t, σ̄_t)-plays, σ̄_t Odd's pointwise-optimal counterstrategy to σ_t), a value (c, P, ℓ) having cycle node λ = c, path set P and length ℓ; W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays and val(ρ, τ) that of the (ρ, τ)-plays; λ_W the cycle-node map of W_t; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Iσ_t Even's improving edges (SPEC S2); a τ-stretch and a W-run F = [a, b] as in RESULTS R89, |F| := b − a its transitions; blocked edges, late adoptions and R*_F (R88's R*_T read on F) as in RESULTS R88 / R89; for a stretch R of consecutive states, ENT_R(v, c), SW_R(v) and RISE_R(c) as in RESULTS R86 (entries of v into c, switches of v, transitions changing Ξ(c)), |R| its transitions; for a W-run F, ΞCH_F(c) := RISE_F(c), WCH_F(c) the transitions of F changing W(c), WCH_F those changing W somewhere, FL_F those changing W nowhere, TIE_F as in RESULTS R93, PCH_F(c) the transitions of F changing the path set of Ξ(c) but not its cycle node, P*_F := max_c PCH_F(c); for a per-W-run quantity Q_F (maximised over vertices or edges when indexed by them), Q-POLY means: there is a polynomial p with Q_F ≤ p(n) for every W-run F of every N5 run on every game from every start pair, and WRUN-POLY := |F|-POLY, XI-CH-POLY := (max_c ΞCH_F(c))-POLY; for an Even edge (X, g), a return of X to g is a transition of F at which X enters g having held g at an earlier state of F, RET_F(X, g) their number, and REG_F(X, g), E0_F(X, g), FREE_F(X, g) the returns whose window (from X's last leave of g) contains a state with a REG (that is, not E0) self-routed block of (X, g), else an E0 one, else neither (P-N5-WRUN §4.1: a self-routed block of (X, g) at state t: (X, g) not improving, g ≠ σ_t(X), and the (σ_t, σ̄_t)-play from g reaching X, its vertices before X (the route) pairwise distinct and, when X lies on the cycle of its own (σ_t, σ̄_t)-play, avoiding that cycle; E0 iff X is the cycle node of Ξ_t(X) and every vertex of the route is below X in the SPEC S1 rank); a change of the path set of Ξ(v) with fixed cycle node has depth the number of path-set vertices above the most relevant vertex of the symmetric difference, and, for every k ≥ 1, DEEP_{k,F}(v) counts the changes of depth ≥ k in F; a frozen stretch Φ of F is a maximal interval of states of F with σ̄ constant, SB_F the transitions of F changing σ̄, R°_Φ the transitions of Φ adopting an edge blocked at an earlier state of Φ and R° := max_Φ R°_Φ; [SUB] := for every sub-interval F′ of every W-run, at most (n − 1)(R*_T(F′) + 1) transitions of F′ change W, R*_T(F′) the transitions of F′ adopting an edge blocked at an earlier state of F′; a W-constant interval I of F is a maximal run of states of F with W constant, XCH_I(d) the transitions of I changing Ξ(d); R*-POLY, FL-POLY, P*-POLY, DEEP_k-POLY, TIE-POLY, SB-POLY and R°-POLY are Q-POLY for these Q, R3-POLY := (max_e WCH_F(e))-POLY, ALT-POLY := (max REG_F)-POLY, FREE-POLY := (max FREE_F)-POLY and [P-INT] := there is a polynomial p such that every W-constant interval of every W-run has at most p(n) transitions): (Theorem XI-RUN) every stretch R of consecutive states of a W-run has |R| ≤ Σ_v SW_R(v) ≤ m_E + Σ_c d_E(c)·RISE_R(c), so every W-run F has |F| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c) and every W-constant interval I has |I| ≤ m_E + Σ_d d_E(d)·XCH_I(d) (Corollary INT-XCH⁰); (Lemmas WAIT-CYCLE′, E0-BOUND, Theorem TRIPLE-RED) after a REG (not E0) self-routed block of (X, g) with route π, σ never again has X → g together with the block's choices on π, E0_F(X, g) ≤ n, and |F| ≤ m_E + Σ RET_F ≤ m_E(n + 1) + Σ_{(X, g)} REG_F(X, g) + Σ_{(X, g)} FREE_F(X, g); (Lemma RET-ΞRISE, Theorem FREE-RED) RET_F(X, g) ≤ ΞCH_F(g) and FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F; (Lemmas GAP-DEV, ΞCH-PCH, Theorem RSTAR-PCH) a target z of an edge blocked at a state q of a W-run has Ξ_q(z) ◁ W_q(z) and an Odd vertex o with σ̄_q(o) ≠ τ_q(o) on its (σ_q, σ̄_q)-play, ΞCH_F(z) ≤ n(n + 1 + PCH_F(z)) and R*_F ≤ Σ_{(y, z) Even edge} ΞCH_F(z) ≤ m_E·n·(n + 1 + P*_F); (Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED) for every k ≥ 1: while the cycle node of Ξ(v) is fixed, the first k terms of the path set of Ξ(v) in decreasing rank, each signed + (even priority) or − (odd priority), padded with NONE and compared lexicographically with terms ordered by (r, +) above (r′, +) iff r > r′, every (r, +) above NONE above every (r′, −), and (r, −) below (r′, −) iff r > r′, are non-decreasing in t and take at most (2n + 1)^k values, and PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v); (Lemmas BIP-MON, NO-DEV) on a frozen stretch of a W-run with σ̄ ≡ ρ and τ_t ≡ τ (the W-run's Odd strategy) both val(σ_t, ρ) and val(σ_t, τ) are non-decreasing, and if Ξ_t = W_t at every state of F then R*_F = 0 and |F| ≤ (n − 1) + 4n²(n − 1); (Theorem BIP-RED, an implication from [SUB]) |F| ≤ SB_F + (SB_F + 1)(n − 1)(R° + 1) + FL_F; (Lemma REL2-WRISE, under (A1) y not its own W-cycle node on [s + 1, q2] and (A2) the τ-play from z under σ_{s+1} with y → z avoiding y) if (y, z) is adopted at a transition of a frozen stretch Φ at which it had been blocked at an earlier state of Φ (a strict release), y leaves z at s and (y, z) is blocked again at q2 > s in Φ, then W_q2(z) ▷ W_{s+1}(z) (a special case of RESULTS R91 Lemma LATE-W, which needs neither (A2) nor the frozen stretch); and (Corollary WRUN-EQ) WRUN-POLY ⇔ XI-CH-POLY ⇔ P*-POLY ⇔ DEEP_k-POLY (each fixed k ≥ 1) ⇔ R*-POLY ∧ FL-POLY ⇔ ALT-POLY ∧ FREE-POLY ⇔ R3-POLY ∧ TIE-POLY ⇔ R*-POLY ∧ [P-INT], and, under [SUB], ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY, while XI-CH-POLY ⇒ R*-POLY, FL-POLY, SB-POLY and WRUN-POLY ⇒ R3-POLY are proved in one direction only (2026-10-30) — REDUCTIONS and EQUIVALENCES (none of these quantities is bounded here; WRUN-POLY, XI-CH-POLY, BIP-POLY, INT-LIN and the other POLY statements are open; CONJECTURE BIP-REL-1 is DEAD (L-RED R143, rel2_R2_n82, l-red 717f407a); W-runs are not whole runs; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)
