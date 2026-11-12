# Box 212 (D18): RF-LEVEL — the rule-free part of P-N5-LEVEL: for EVERY improving rule on IDEAL-CYC(G) at most P = 2M(N + 2M) steps are not stalls, and every other step lies in a class-frozen window on a closed one-player sub-game; the Γ3 form reduces O1′ (KEY-CYC) to N5's key rule on such windows (CANDIDATES; not a bound for N5; G-N5-TIME stays OPEN)
L-NEW successor 74 (session_01V5yGRYHKYSjsfxFEDcsyEP), D1 / D14 / D18 / D21. Written 2026-11-12 from 20:45Z (date -u). Approved by the
Lead 18:32Z as successor 73 proposed (message of ~18:29Z), with changes (a)-(c) (the Lead's brief to successor 74): «(a) RF-D's first
step is a dated per-lemma reading of whether R125's static lemmas hold at every STANDARD state»; «(b) … cite the Lean status as it
stands on origin»; «(c) cite W-FLAT (box 104, claude/l-si 26704e01) as the source of «not proposed»». Lead «go» 20:37Z: «Start with BOX
212 (a), your per-lemma reading … Read each lemma's PROOF, not only its statement. Record the verdict per lemma, dated, with the
deciding line of the proof. Then do RF-A and RF-B.»
Labels: READING (§2: what landed proofs prove), CANDIDATE (lane, unrefereed: RF-A, RF-B, RF-C; RF-D is CONDITIONAL on a hypothesis and
on box 209's CANDIDATE lemmas), DATA (§7, not to sign). Nothing here is a RESULTS entry. Not M3, not M4, not a bound for N5 or N5′-xi;
**G-N5-TIME stays OPEN.**

## 0. Answer
1. **(a) READING, dated 2026-11-12 ~20:37-20:44Z.** None of the proofs of the landed static lemmas of R123 (CN2, B-ONLY, NO-TIE, LOC-GATE,
   LOC-K2) and R125 (CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3) uses F1, DOM, Howard's rule or any property of a run. CN2 and CN2-3
   are proved for every positional pair of Γ(G), resp. Γ3(G); the other eight for every state, i.e. every choice of the movers with
   the non-movers frozen (IDEAL-CYC), resp. every standard state, with σ̄ any pointwise-optimal reply. Table in §2.
2. **RF-A (CANDIDATE).** Let the run be ANY improving run of IDEAL-CYC(G): every step switches a non-empty set of movers, each to a
   gate of strictly larger Ω_t value. Then (K1)-(K4), (L1)-(L3), (L5) of P-N5-LEVEL hold verbatim along it. For every reference state
   b at most P = 2M(N + 2M) steps t → t + 1 with t < b and LAG_t ≠ ∅ are not stalls (at most M(N + 2M) if case (α) holds at every
   state). K5-NEW: class_(t+1)(x) ≥ class_t(σ_(t+1)(x)) for every mover x. Howard's rule is used only in (K5) (for EVERY gate of x),
   (L4) and PLATEAU's (P3), (P6), (P7).
3. **RF-B (CANDIDATE).** On a plateau of any improving run (a maximal interval [u, v], u < v, of constant Φ) the set Y = {x : class_u(x) ≤ m}
   is closed under plays, keeps its classes, and Odd's choice at every gate of Y is constant. The run restricted to Y is a sequence of
   identity steps and improving steps of the one-player game H_Y (Y, each mover of Y with its gates in Y, every other vertex with its
   one successor at u). Not claimed for a general rule: (P3), (P6), (P7) (DATA: they fail under single-switch rules).
4. **RF-C (CANDIDATE).** For any improving run and reference b = T: T ≤ P + (P + 1)·W, where W is the length of the longest class-frozen
   window of the run (a plateau of RF-B, or the tail after LAG empties, which is the same kind of window with Y = every vertex). For
   Howard's rule W ≤ N + 2M + 5 (P-N5-LEVEL's PLATEAU and QUIET-N) gives ALL-TCYC back; for other rules no bound on W is claimed.
5. **RF-D (CONDITIONAL; a reduction, not a bound).** If every step of N5 from S3 on Γ3(G) before its first fallback is an improving step
   at the movers (hypothesis [IMP3]; box 104's W-FLAT (lane) gives it, §6), and box 209's Γ3 class facts and LEVEL3 hold (CANDIDATES;
   by (a) their landed premises hold at every standard state), then the number T_key(G) of steps of N5's run before its first fallback
   satisfies T_key(G) ≤ P3 + (P3 + 1)·W_key(G), P3 = 2M(N + 4M), W_key(G) the longest class-frozen window of that run, each window a
   run of the KEY rule on a closed one-player sub-game of Γ3(G) with frozen classes. So O1′ (KEY-CYC) is equivalent, up to the polynomial factor P3 + 1, to a bound on the key
   rule inside such windows. This is a reduction of an OPEN question to another OPEN question.
6. **DATA (§7).** Every rule-free counter is 0 under seven improving rules (Howard and six others) on random and frozen genomes, and on
   N5's own key-rule run on Γ3(G); the Howard-only facts (K5), (P3), (P6) fire under the other rules, as RF-A / RF-B predict.

## 1. Premises
- P-N5-LEVEL (docs/new/P-N5-LEVEL.md, frozen at l-new 1e6df499, sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec; this lane's packet,
  under review by REFEREE 34 and REFEREE-2 39): its §1 (premises, quoted by script, box211/quotes211.py at trunk 68c8d293), §2
  (setting, ORDER ON CLASSES), §3-§5, §7. RF-A / RF-B / RF-C re-use its proofs line by line; they are lane statements, not premises.
- Landed premises used (as quoted in P-N5-LEVEL §1, re-quoted here where the scope matters; every «…» on a bullet marked [Q X] is checked
  by experiments/new/box212/quotes212.py, output quotes212.out):
- [Q R15] (a), the source of F1, for ANY improving set: «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4),
  Ωσ ⊴ Ω_{Switch_I(σ)}.»
- [Q docs/new/P-N5-XICYC.md@7fa6aff4] F1 as used on IDEAL-CYC: «F1 (from [R15a]): Ω_t ⊴ Ω_(t+1) pointwise, for every step t.»; why a
  step is such a set: «so I is non-empty and unambiguous (one switch per vertex).»
- [Q R118] (a), the game: «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is
  unrestricted (gates and K2).»
- [Q R123] the five static lemmas, as landed: CN2 «For every genome G, every positional pair of IDEAL-CYC(G) and every vertex v, the cycle
  node of v's play has priority ≥ 2.»; B-ONLY «In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than c_W and
  the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex»; NO-TIE «At every state and every gate g, Ω_t(e_g)
  ≠ Ω_t(β_g).»; LOC-GATE «Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a := σ̄_t(g), b := its other face, Ω :=
  Ω_t.»; LOC-K2 «At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).»
- [Q R121] E-DOM: «Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]»
- [Q R126] QUIET-N (Howard only; used in RF-C's Howard remark only): «every maximal window of quiet steps has at most N steps»
- For RF-D: R125's lemmas on HOW3(G) (P-N5-CHAIN §2, §5; §2 below), R124's standard state, box 209 (l-new 3f896099,
  docs/new/N5-LEVEL3-box209.md, CANDIDATES) §2-§3, and box 104's W-FLAT (claude/l-si 26704e01, lane, PROVED there, not refereed):
- [Q docs/si/box104-map.md@26704e01] W-FLAT: «Let R be any rule that picks σ_new(x) inside TIE(x) at every Even x in S4a (SPEC's root-first
  key, box 190's»; «until its first fallback, the run of N5 with R visits only standard states, and at each step every choosing vertex
  (v ∈ V_E, resp. a mover) takes R's pick in A(x) = {its current option} ∪ {its strictly Ξσ-better options}.»; O1′: «F(G) ≤ poly(N + M)
  for every R104 genome, F the first fallback of N5 from S3 on Γ3(G)»
- NOT used anywhere: R118 (c) DOM, R118 (e)'s reason, R121 E-MON (all three are statements about Howard's run; (K1) is re-proved
  below from F1), R118 (i) BR-SEG-G (Howard; used only in the Howard remark of RF-C, through P-N5-LEVEL's PLATEAU).

## 2. (a) The per-lemma reading (READING; dated 2026-11-12, proofs read ~20:37-20:44Z by date -u; trunk 7fa6aff4)
Question (Lead, 20:37Z): does «at every state» in R123 B-ONLY, NO-TIE, LOC-GATE, LOC-K2 mean every IDEAL-CYC RUN state or every state;
how far does «every positional pair» reach in CN2? Same for R125's Γ3 forms at STANDARD states. Files (sha1 of the file at trunk
7fa6aff4): docs/new/P-N5-QUIET.md 066dfc7d5a03b983a126ffc6866a13046b5e9724 (R123's packet), docs/new/P-N5-QUIET-fixes.md
cd3581f722d5f803ca9f661042b7e2bbf4d5d6dc (fixes entry 1: B-ONLY, NO-TIE), docs/new/P-N5-CHAIN.md 6e613ba762b6ecf67247ef6d8674b4c960013039
(R125's packet). A «state» of IDEAL-CYC is an Even strategy of R118 (a)'s game: any choice at the movers, every other Even vertex
frozen. A «state» of HOW3(G) is, in R125's words: [Q docs/new/P-N5-CHAIN.md@7fa6aff4] «a state is the frozen part plus a choice at
every mover» (the standard states of R124 with any mover choice).

| lemma (landed) | proof read (file, lines at trunk 7fa6aff4) | what the proof uses | deciding line of the proof | verdict |
| --- | --- | --- | --- | --- |
| CN2 (R123) | P-N5-QUIET §2, l. 79-86 | [DEF]'s shape only | see [Q] below (a): a cycle through a mover passes a gate, a cycle through a gate passes a face of priority ≥ 6, else all priorities ≥ 2 | every positional pair of Γ(G), frozen or not (the statement's «of IDEAL-CYC(G)» is narrower than its proof) |
| LOC-GATE (R123) | P-N5-QUIET §3, l. 89-111 | [OPT] at the state, Odd positional and unrestricted at gates, F3, F4′, CN2 | (b) | every state of IDEAL-CYC (the words «of a run» are not used by the proof; nor is the freeze) |
| LOC-K2 (R123) | P-N5-QUIET §3, l. 113-116 | the freeze of K1, [OPT], F3 | (c) | every state of IDEAL-CYC |
| B-ONLY (R123) | P-N5-QUIET-fixes entry 1, l. 11-25 | τ_β (Odd positional), [DEF]'s shape, E-DOM, the frozen core, [OPT], [VJ] (rewards first) | (d) | every state of IDEAL-CYC |
| NO-TIE (R123) | P-N5-QUIET-fixes entry 1, l. 26-29 | B-ONLY and the shape of plays | (e) | every state of IDEAL-CYC |
| CN2-3 (R125) | P-N5-CHAIN §2 (P) l. 93-95, §5 l. 170-174 | [DEF], R117's pads; the shape only | (f) | every positional pair of Γ3(G) |
| LOC-GATE3 (R125) | P-N5-CHAIN §5 l. 175-196 | as LOC-GATE, with CN2-3 | (g) | every standard state |
| LOC-K2-3 (R125) | P-N5-CHAIN §5 l. 197-200 | the freeze K1 → s → K1, [OPT], F3 | (h) | every standard state |
| B-ONLY3 (R125) | P-N5-CHAIN §5 l. 201-208, (Core) l. 97 | τ_β, the pads' in-edges, (E-DOM), (Core), [OPT] | (i) | every standard state |
| NO-TIE3 (R125) | P-N5-CHAIN §5 l. 209-212 | B-ONLY3, the shape of plays | (j) | every standard state |

Deciding lines (quoted by script):
- [Q docs/new/P-N5-QUIET.md@7fa6aff4] (a) «A cycle containing a mover contains its successor, a gate ([DEF] used shape). A cycle containing
  a gate contains one of its two successors, a face, of priority ≥ 6 ([DEF]).» (b) «Let τ := σ̄_t with g switched to b, a positional
  Odd strategy ([XICYC] (a)). Write val_τ(g) for the value of g's play under (σ_t, τ). By [OPT], Ω(g) ⊴ val_τ(g).» (c) «K1 is frozen at K1
  → K1 ([DEF] start, [XICYC] (a)), so Ω(K1) = (K1, ∅, 0), reward −5.»
- [Q docs/new/P-N5-QUIET-fixes.md@7fa6aff4] (d) «nor K0 or K3 (never cycle nodes: K0 → K3 → K2 frozen, nothing returns to K0)»; «By [OPT],
  Ω_t(v) ⊴ v's value under (σ_t, τ_β).» (e) «If e_g's successor is c_W, Λ(e_g) = c_W while Λ(β_g) ≠ c_W (B-ONLY): different.»
- [Q docs/new/P-N5-CHAIN.md@7fa6aff4] (f) «So every cycle other than c_X's loop has a vertex of Ω ≥ 3.»; «For every positional pair of
  Γ3(G) and every vertex v ≠ c_X, the cycle node of v's play has Ω ≥ 3» (g) «Let t be a state, g a gate, a := σ̄_t(g) ∈ {pe_g, pβ_g}, b
  the other face, Ω := Ω_t.»; «By [OPT], Ω(g) ⊴ val_τ(g), the value of g's play under (σ_t, τ).» (h) «K1 → s → K1 is frozen: Ω(K1) =
  (K1, ∅, 0)» (i) «For the v of the statement its cycle holds no e-vertex and not c_W, and not K0, K3 ((Core))»; «(Core) In standard
  states and in HOW3: K0 → pA → K3 → K2 and K1 → s → K1 are frozen» (j) «If e_g → c_W: Λ(pe_g) = c_W while Λ(pβ_g) ≠ c_W (B-ONLY3).»
- Why no run property enters: F3 and F4′ (P-N5-XICYC §3) are facts about the plays of ONE positional pair and the order ⊴; [OPT] is a
  property of σ̄_t against σ_t at that one state; τ := σ̄_t with one gate switched, and τ_β, are positional Odd strategies of the same
  game; the freeze is part of the definition of a state. None of the ten proofs compares two states.
- The same holds for what P-N5-LEVEL's (K2), (K3), (K4) use besides these lemmas: E-DOM («by [DEF]»), the readings (D1), (D3), (D4)
  of [DEF], and (K3 (e))'s frozen core. So (K2)-(K4) hold at every state of IDEAL-CYC (any two states for (K2)), whatever the rule.
- What IS a run property, and is not used by RF-A: R118 (c) DOM (Howard's step), R118 (e)'s «each vertex's Λ moves only to a vertex of
  strictly larger reward» (stated for the run), R121 E-MON (the run), R126 QUIET-N (Howard's run), R118 (i) BR-SEG-G (Howard runs under
  H0). F1 is a run property for EVERY improving rule (R15 (a)).
- Verdict, in one line: «at every state» in R123 / R125 means every state of the model (every mover choice, non-movers frozen; on Γ3
  every standard state), not only the states of Howard's run; CN2 / CN2-3 reach every positional pair of the game.

## 3. RF-A (CANDIDATE): the non-stall count for any improving rule
**Setting.** G any genome. An IMPROVING RUN of IDEAL-CYC(G) is a sequence of states σ_0, …, σ_T (σ_0 any mover state) such that, with
σ̄_t any pointwise-optimal reply to σ_t ([OPT]) and Ω_t the values under (σ_t, σ̄_t), every step t → t + 1 changes σ exactly at a
non-empty set I_t of movers, and every x ∈ I_t moves to a gate y with Ω_t(y) ▷ Ω_t(σ_t(x)). (Howard's step is one; so are single-switch
rules, random rules, the least improving switch, …; no stopping rule is assumed.) class, LAG_t, FRONT_t, Φ_t, stall, reference b: as in
P-N5-LEVEL §2, §4. P := 2M(N + 2M).
**Statement.** For every improving run and every reference state b:
- (i) (K1) class_t(v) ≤ class_(t+1)(v) for every v and step; (K2) for any two states of the run; (K3), (K4) at every state.
- (ii) (L1), (L2), (L3), (L5) of P-N5-LEVEL §4 hold verbatim.
- (iii) at most P steps t → t + 1 with t < b and LAG_t ≠ ∅ are not stalls; at most M(N + 2M) if case (α) of (L3) holds at every state.
- (iv) K5-NEW: class_(t+1)(x) ≥ class_t(σ_(t+1)(x)) for every mover x and every step t → t + 1.
**Proof.**
- (K2), (K3), (K4): their proofs (P-N5-LEVEL §3) use CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, E-DOM, (D1), (D3), (D4), [VJ] and the frozen
  core, each at the state(s) concerned; by §2 each holds at every state of IDEAL-CYC. Nothing in them refers to the step rule.
- F1 along the run: I_t is non-empty, has one switch per mover (unambiguous) and each switch is an improvement of σ_t (VJ00 §4.4: a
  successor of strictly larger value), so R15 (a) Lemma A gives Ω_t ⊴ Ω_(t+1) pointwise.
- (K1): for v outside the core, Ω_t(v) ⊴ Ω_(t+1)(v) (F1) and (K2) for the two values of v give class_t(v) ≤ class_(t+1)(v). For the core
  vertices the class is constant ((K3 (e))). This replaces P-N5-LEVEL's proof from R118 (e)'s reason and E-MON, which are statements
  about Howard's run (the packet's own remark, «Outside the core (K1) also follows from F1 and (K2)», is this proof).
- (ii): (L1) uses only (K1); (L2) uses (K3); (L3) uses (K3), (K4) at b, CN2, (D4); (L5) uses (L2), (L3). None uses (K5), the rule or (L4).
- (iii): let t_1 < t_2 < … < t_q be the non-stall steps with t_i < b and LAG_(t_i) ≠ ∅. By (L1), Φ never falls while LAG ≠ ∅, and
  Φ_(t_i + 1) > Φ_(t_i) unless LAG_(t_i + 1) = ∅, which can happen only at t_q (LAG only shrinks, (L1)). So Φ_(t_1) < Φ_(t_2) < … < Φ_(t_q):
  q distinct values of Φ, and q ≤ P by (L5) (≤ M(N + 2M) in case (α) everywhere).
- (iv): x is not an e-vertex, so class_(t+1)(x) = class_(t+1)(σ_(t+1)(x)) ((K3 (c)) at t + 1), and class_(t+1)(y) ≥ class_t(y) for
  y := σ_(t+1)(x) ((K1)). ∎
- Where Howard's rule enters (and only there): (K5) «for every gate y of x» (DOM); (L4) (its mover case uses (K5) for y = σ_b(z)); PLATEAU's
  (P3) (K5), (P6) (the rule of R118 (a) in (A)) and (P7) (BR-SEG-G, Howard). The non-stall count is rule-free; the stalls are not.
- Lean (as it stands on origin, change (b)): claude/l-formal e14f5508 / 6ed90b71 has the Howard form only (GenomeLevelStatement: L2, L3,
  L5, PlateauGStatement, ALL-TCYC «for EVERY run of IDEAL-CYC(G) (any first mover state, any optimal counterstrategy, any choice among
  best gates)», INDEX l. 46-51). The improving-rule form (IdealImpRun, ImpNonStall ≤ 2M(N + 2M), ImpK5New) was recovered by L-FORMAL 3
  and is NOT on origin at this writing (Lead, 20:37Z: «commit pending on claude/l-formal»). (i)-(iv) above are written to match those
  three names: IdealImpRun = the setting, ImpNonStall = (iii), ImpK5New = (iv). The Lead's routing gives the summary «the rule enters
  only at the stalls; the non-stall count is rule-free»; that sentence is in no file on origin.

## 4. RF-B (CANDIDATE): a plateau is a closed one-player window with frozen classes
**Statement.** For every improving run, reference b and maximal interval [u, v] of constant Φ with u < v (Φ = (m, −|J|) there; v < b):
put Y := {x : class_u(x) ≤ m}. Then for every s ∈ [u, v]:
- (P1) {x : class_s(x) ≤ m} = Y and class_s(x) = class_u(x) for x ∈ Y;
- (P2) Y is closed under plays: s_s(x) ∈ Y for x ∈ Y; in particular σ_s(x) ∈ Y for every mover x ∈ Y;
- (P4) for every gate g ∈ Y, σ̄_s(g) is the same face for all s ∈ [u, v] and lies in Y; σ̄_s(K2) = K1;
- (P5′) let H_Y be the game on Y in which every mover of Y keeps its gates IN Y and every other vertex x of Y keeps the single successor
  s_u(x). Ω_s on Y is the value of σ_s restricted to Y in H_Y (Odd has one strategy in H_Y); and for u ≤ s < v the step s → s + 1,
  restricted to the movers of Y, is the identity or a non-empty set of strictly improving switches of H_Y.
**Proof.** (P1), (P2), (P4): P-N5-LEVEL §7's proofs, which use (K1), (K3), (K4), (D1), LOC-K2 and the freeze only (RF-A (i)). (P5′): by
(P2), (P4), LOC-K2 and the freeze, the play from x ∈ Y under (σ_s, σ̄_s) stays in Y and uses only edges of H_Y; the order of relevance and
the parities are inherited, so the values agree. A mover x ∈ Y with σ_(s+1)(x) ≠ σ_s(x) moves to σ_(s+1)(x) ∈ Y ((P2) at s + 1) with
Ω_s(σ_(s+1)(x)) ▷ Ω_s(σ_s(x)) (the run is improving), and both gates are in Y, so these are H_Y values. ∎
- Not claimed for a general rule, and why: (P3) («every gate of a mover of Y lies in Y») needs (K5) for every gate; a mover of Y may have
  a strictly better gate outside Y that the rule does not take (DATA: platexit > 0). (P6) («every plateau step moves a mover of Y»)
  needs Howard's «keep a ⊴-largest gate» in its induction (A); a rule may move only movers outside Y for many steps (DATA: platidle > 0).
  (P7) is BR-SEG-G, a Howard statement; a plateau may be longer than the number of movers of Y (DATA: plat_gt_movers > 0).
- So the window on Y is «the rule's own run on the one-player game H_Y, interleaved with idle steps», with every class on Y frozen.

## 5. RF-C (CANDIDATE): the decomposition
**Statement.** For every improving run with b := T: T ≤ q + Σ_i (v_i − u_i) + (T − b′) with q ≤ P ((C1), (C2) of P-N5-LEVEL §5 with RF-A
(iii)), where the [u_i, v_i] are the plateaus of RF-B and [b′, T] is the TAIL (no vertex lags). On the tail every class is constant
((K1): class_(b′) ≤ class_t ≤ class_T = class_(b′)), and the tail is a window of RF-B's kind with Y := every vertex: Y is closed, every
gate keeps its face. Hence T ≤ P + (P + 1)·W, W the longest window (plateau or tail).
**Proof of the tail clause.** Classes constant: above. Gates: if the two faces of g have different classes, σ̄_t(g) is the face of lower
class at every t ((K4)), the same face. If they have equal classes and e_g's successor were c_W, β_g would have class (c_W, ∅), so
Λ(β_g) = c_W, against B-ONLY (β_g is not excepted); so e_g's successor is a mover and P-N5-LEVEL (P4) case (3) gives σ̄_t(g) = e_g at
every t. K2: LOC-K2. ∎
- For Howard: W ≤ N + 2M + 5 (P-N5-LEVEL PLATEAU for plateaus; QUIET-N for the tail), and the line is ALL-TCYC. For any other rule
  nothing bounds W here, and QUIET-N does not apply to the tail (DATA: tail_gt_N > 0 under single-switch rules).

## 6. RF-D (CONDITIONAL): the Γ3 form, and what it does to O1′
**Hypotheses.** [IMP3]: every step of N5 (SPEC S1-S5) from S3 on Γ3(G) before its first fallback visits only standard states and changes
σ exactly at a non-empty set of movers, each to a gate of strictly larger Ω_t (VJ value against Odd's pointwise-optimal reply).
Source: W-FLAT (box 104 §7, lane, PROVED there and not refereed) gives «visits only standard states» and «takes R's pick in A(x) =
{its current option} ∪ {its strictly Ξσ-better options}»; the set is non-empty because every iteration of N5 changes σ or τ (R15 (d))
and τ does not change on Γ3 before the first fallback (box 104 §8, «on Γ3(G) and on Γ3*(G*), τ never changes and there is one
fallback»; lane). Reading (not checked here line by line): Ξσ's order on Γ3 is Ω_t's. [L3]: box 209's (K0′)-(K4′) and LEVEL3 (L1′)-(L3′),
(L5′) (CANDIDATES), whose landed premises are R125's static lemmas: by §2 they hold at every standard state, and box 209's (K1′) is
proved from F1 + (K2′) (box 209 notes; E-MON3 not used), so they hold along any improving run of standard states.
**Statement (CONDITIONAL on [IMP3] and [L3]).** RF-A, RF-B and RF-C hold for N5's run on Γ3(G) up to its first fallback, with P3 =
2M(N + 4M) in place of P: T_key(G) ≤ P3 + (P3 + 1)·W_key(G), T_key(G) the number of steps before the first fallback, where every
window is a run of SPEC's key rule on a closed one-player sub-game of Γ3(G) whose classes are frozen. (READING: F(G), the iteration of
the first fallback, is T_key(G) plus a constant, as for N5′-xi, whose first fallback R118 places «at iteration T3 + 1».)
**What it does to O1′.** O1′ asks for F(G) ≤ poly(N + M) on every R104 genome. Under the hypotheses (and the READING above), O1′
holds iff W_key(G) ≤ poly(N + M) for every genome (⇐ by the line; ⇒ because a window is part of the run). So the open question moves from «the key rule
against Odd's replies on Ξ-cyclic genomes» to «the key rule on one-player class-frozen windows», a generalised O1 (O1 is the
Ξ-acyclic case, where LAG is empty from the start and the whole run is one window: the reduction says nothing new there). Not claimed:
any bound on W_key; anything after the first fallback; anything about N5 on other games.

## 7. DATA (not to sign; tools in experiments/new/box212/; outputs out/; summary by summ212.py)
[filled from summ212.py after the runs are final]

## 8. Not proposed, scope, TARGET.md diff
- Not proposed: a bound for N5, and a rule-free bound on the windows. Source (change (c)): W-FLAT, box 104 §7 (claude/l-si 26704e01):
  [Q docs/si/box104-map.md@26704e01] «So on these games the algorithm is a ONE-SIDED strategy improvement on the inner game». On W-flat
  wrappers of ANY parity game every tie rule turns N5′-xi / N5 into one-sided strategy improvement on the inner game, so a rule-free
  bound on windows would bound one-sided strategy improvement with that rule on every game; RF-A..RF-D stay on genome games.
- TARGET.md: no algorithm, M3 or M4 is claimed. RF-A..RF-C are statements about one restricted family (IDEAL-CYC on genome games,
  TARGET.md §4: a bound on a restricted class is not M4); RF-D is a conditional reduction. G-N5-TIME stays OPEN.
