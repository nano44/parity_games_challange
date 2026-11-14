# R-P-N5-GATE: first referee report on packet P-N5-GATE (L-SI boxes 91-96)
REFEREE successor 31 (Opus 5.5, D15; D1). Date -u at writing of §1-§2: 2026-11-11T22:50Z. Written section by section; §0 (verdicts) comes last.
Not read before my own verdict: docs/referee-2/, L-RED 62-64's records (R228-box91, R229-box92/93/94/203, R230). Read: the packet, its
fixes, line L-2, and the premise packets P-N5-CHAIN / P-N5-SPLIT with my lane's reports on them (R-P-N5-CHAIN.md, R-P-N5-SPLIT.md).

## 1. Objects and premises
### 1.1 Objects (measured with git, not copied)
- Packet: claude/l-si 4066f579 (ancestor of origin/claude/l-si, checked), docs/si/P-N5-GATE.md sha1
  f3a584e68b5c998276ea717f42920bdeeca581ab, 25,604 B, 230 lines. Fixes: docs/si/P-N5-GATE-fixes.md at 9c0349b1 (ancestor, checked), sha1
  1fec4f8c971c0ae89069d0532b6b97a67c2330e5, entries 1 (G1-G6, line L-1) and 2 (F2-1 PROVISO on IDEAL-CYC, line L-2).
- Line: docs/si/P-N5-GATE-line-L2.txt at 9c0349b1, sha1 c0f2007d84afab1e00ef41e24ba8f5f064468cc5, 10,295 B.
- Premise packets (pending, my lane's earlier reviews): P-N5-CHAIN claude/l-new 93531b03, docs/new/P-N5-CHAIN.md sha1 6e613ba7… (348 lines;
  R125, second fill at CHECKER C139 Add. 1; line L-5 473344b1… on origin/claude/l-new); P-N5-SPLIT claude/l-new 399cda07, sha1
  5bc1b1f3… (both referees SIGN, conditional on R125).
- Instances: box 91 inst/SHA1SUMS 11/11 OK and box 93 inst/SHA1SUMS 8/8 OK (`sha1sum -c` on `git archive 9c0349b1`).

### 1.2 Landed premises, quoted by script
- scratch/gate_quotes.py (every outermost «…» of L-2, located in trunk docs/RESULTS.md at 8ba1b23b by entry; log
  gate_logs/quotes_L2.out): 9 quotes; 8 are premise quotes and each occurs verbatim: R104 (the e-vertex sentence), R118 (IDEAL-CYC(G)
  definition, also in R121; the Howard step with its tie rule; «T3 is the first state …»; «an N5′-xi run (box 190's S4a tie rule by Ξσ)»),
  R121 (Lemma E-MON), R123 (B-ONLY; NO-TIE). The 9th («D's play avoids e_o») is the packet's own proviso, not a premise.
- The cited R118 items exist as signed in R118's entry: (a) definitions with the tie rule, (b) F1-F6 with F4 REPLACED by F4′, (c) DOM and
  STRICT, (e) CYC-COUNT, (k) REACH3-CYC; R123's CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2 are in R123's title.
- Not landed, named as pending in the line: P-N5-CHAIN (R125) and P-N5-SPLIT. Every Γ3 statement rests on P-N5-CHAIN; PAIR-EXPEL,
  EXPEL-COUNT and A*-EQUIV are labelled conditional on P-N5-SPLIT as well (see §2.7-§2.8 for what each really needs).

### 1.3 Premise findings (each is used in §0 and §5)
- **GT-1 (B-ONLY on Γ3 IS a P-N5-CHAIN fact).** Fixes entry 1 G1 says «On Γ3 the same needs B-ONLY on Γ3, which is not among P-N5-CHAIN's
  facts (§1) and not landed», and entry 2 keeps the proviso as a Γ3 hypothesis. The frozen P-N5-CHAIN (6e613ba7) §5 contains **Lemma
  B-ONLY3** (l. 201-208: «At every state t and every vertex v other than c_W, the e-vertices whose successor is c_W, and the pads pe_g of
  those e-vertices, Λ_t(v) is less relevant than every e-vertex»), in its «To sign» table (§5 row, «PROVED, every genome»), SIGNED by
  both referees (R-P-N5-CHAIN.md §0 row «CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3 (§5)»: SIGN; REFEREE-2 R2-P-N5-CHAIN.md «Lemma
  B-ONLY3 | SIGN»), and stated in R125's line L-5 («(Lemma B-ONLY3) at every state and every vertex v other than c_W, the e-vertices
  whose successor is c_W and their pads pe_g, …»). NO-TIE3, which this packet already uses, is proved FROM it (CHAIN l. 209-211). Its
  states are HOW3's states 0, …, T3, exactly this packet's Γ3 run. So the K10 case and the PROVISO on Γ3 hold under the SAME pending
  condition (R125) as every other Γ3 statement here (derivations §2.2, §2.4). The packet's text is not wrong to call them open «within
  this packet» (B-ONLY3 is not in its §1 list), but the reason given in G1 is false, and the open case is closable at no extra premise.
- **GT-2 (citation «P-N5-SPLIT §2 (a)»).** P-N5-SPLIT §2 is Lemma SPLIT (i)-(iv); it has no item (a). The mover-step chain PAIR-EXPEL
  Step 1 uses is P-N5-SPLIT §3 (a) (Lemma REWIN (a), l. 89 and its proof l. 93-96). Moreover PAIR-EXPEL's text writes the whole chain
  itself with F1, STRICT, F3, F6, F4′, CN2-3 (all P-N5-CHAIN facts, or R118 (b)/(c) and R123 CN2 on IDEAL-CYC): nothing of P-N5-SPLIT is
  used (§2.7). The conditional label is harmless but not needed.
- **GT-3 (C-EQUIV is P-N5-SPLIT's).** §3.8's heading, the §3.8 table row and L-2's statement clause say «P-N5-CHAIN's C-EQUIV». C-EQUIV is
  P-N5-SPLIT §6 (Corollary C-EQUIV, l. 188-189); P-N5-CHAIN has no C-EQUIV (0 occurrences). §1 of the packet and L-2's premise list place
  it correctly. Required fix in the line (§5).
- **GT-4 (A*-EQUIV (i) is cited from a lane document).** §3.8 (i): «(L-NEW, N5-CORE-forms §3 (5): cited, not re-proved here …)». A lane
  notebook is not a premise and the packet says it «carries every proof in full». Re-derived in §2.8 (two lines, no premise beyond the
  definitions); no change of statement, but the line must not rest on that document.
- **GT-5 (EXPEL-COUNT's 3M is cited from L-RED R228 §2).** L-2 says «no L-RED lane lemma is a premise». The count is elementary:
  split pairs (u′, b′) are edges out of movers and gates; on Γ (R104) a mover x has one edge per option to its gate, and a gate two faces;
  on Γ3 ([G3]) a mover's edge per option goes to its pad m_(x,k), a gate's to pe_g and pβ_g; K2 never splits (σ̄(K2) constant: R123
  LOC-K2 / P-N5-CHAIN LOC-K2-3). So at most M + 2M = 3M pairs. Re-derived; also = P-N5-SPLIT's SPL ≤ 3M. Citation fix (optional in the
  line: it does not name R228).
- **GT-6 (IDEAL-CYC premises not named).** On IDEAL-CYC the packet's §1 substitutes landed items only for LOC-GATE3, NO-TIE3, E-MON3, F1,
  F2. Its IDEAL-CYC proofs also use F3, F4′, F6 (R118 (b)), STRICT (R118 (c)), CN2 (R123), CYC (R118 (e)), and (E-DOM), (Core) on Γ.
  L-2's IDEAL-CYC list names (b) F1, F2, F3, (e), CN2, but not F4′, F6, STRICT, (E-DOM), (Core). F4′ / F6 / STRICT are landed (R118 (b),
  (c)); (E-DOM) is read off R104's priorities (every β < every e < c_W = top < K0 = top + 2 < K3 = top + 3; K1 5, K2 3, movers 0, gates 1,
  c_X 2); (Core) on Γ, for NON-CORE vertices, is my derivation in §2.2. Required: the line names them (§5).
- **GT-7 ((Core) as paraphrased is the W-1 sentence).** The packet's §1 paraphrases (Core) as «K0, K3 lie on both of two plays with the same
  Λ or on neither». Over all vertices this is false (W-1, R-P-N5-CHAIN §D follow-up 1: a play from K1 has node K1 and neither, a non-core
  play entering the core has node K1 and both; on Γ3 a play from pA or K3 has K3 and not K0). Every use in this packet compares two
  NON-CORE vertices (GATE-LOW-NULL (a): the faces; PAIR-EXPEL Step 2: a′, b′, which are pads m_(x,k) / face pads on Γ3, gates / e, β on Γ;
  TRIGGER (γ): a face against itself), where the repaired reading holds (§2.2). So no statement changes; the line should carry the W-1
  clause as P-N5-SPLIT's does (SP-1 of R-P-N5-SPLIT), i.e. (Core) «in its W-1 repaired reading (non-core vertices)».
- **GT-8 (paraphrased fact names).** The packet's §1 glosses F3 as «E_t(v) is the set of e-vertices on v's play more relevant than Λ_t(v)» and
  F6 as «an e-vertex has exactly one successor, its W-target». In P-N5-CHAIN, F3 is the ext-recursion Ω_t(v) = ext(v, Ω_t(nx_t(v))) and
  F6 is «No mover is the cycle node of its own play … Every non-mover Even vertex has one successor in HOW3»; E_t(v) is a definition
  (P-N5-CHAIN §6/§7) and e's single successor is [DEF] (R104). The facts used are true and present in the premise packets; only the names
  are off. Same class as SP-2 of R-P-N5-SPLIT; optional in the line (L-2 does not repeat the glosses).

## 2. Proofs, each step re-derived (frozen text, with fixes entries 1-2)
Notation as the packet's §2. «Both runs» = Γ3 (HOW3, states 0..T3; P-N5-CHAIN facts, pending R125) and IDEAL-CYC (landed R118/R121/R123).

### 2.1 GATE-RACE (a), (b) and TRIGGER: CORRECT, both runs
- (a) Flip at t from p to q: σ̄_(t−1)(o) = p, σ̄_t(o) = q. LOC-GATE3 + NO-TIE3 at t − 1 and t: Ω_(t−1)(p) ◁ Ω_(t−1)(q) and Ω_t(q) ◁ Ω_t(p);
  F1 at q: Ω_(t−1)(q) ⊴ Ω_t(q). Chain: Ω_(t−1)(p) ◁ Ω_t(p). The face LEFT changed. (F2 is listed but not used.)
- (b) Flips alternate p → q / q → p; one flip per step; each p → q flip is a change step of p, each q → p a change step of q; the two
  counts differ by ≤ 1, so flips ≤ ch_p + ch_q and ≤ 2·min(ch_p, ch_q) + 1.
- TRIGGER: (α) Λ(p) changes: by F2 + CYC (R118 (e) per vertex on IDEAL-CYC) at most 2M + 2 changes over the run. (β) Λ fixed, E(p) changes:
  E-MON3 / R121 E-MON says E rises lex, so the top of the difference lies in the later set, i.e. on P_t(p). (γ) otherwise: Λ and E fixed;
  the change is in Π's non-e part or in k. «Π below every e-letter» needs that no vertex more relevant than an e-letter (c_W, K0, K3,
  (E-DOM)) differs: c_W is in no Π; K0, K3 by (Core) for the non-core face p (GT-7). Correct. (REL-G, an L-RED lemma, is cited as context
  only, not as a premise: fine.)

### 2.2 GATE-LOW-NULL (a), (b), (b′): CORRECT, both runs; K10 empty on BOTH runs
- (Core) on non-core vertices, Γ (for IDEAL-CYC; my derivation, GT-6): the core {K0, K1, K2, K3} is closed; its only in-edge from outside
  is β → u = K0 ([DEF]). K0, K1, K3 are non-mover Even vertices, frozen in IDEAL-CYC; σ̄(K2) = K1 at every state (R123 LOC-K2). So every
  non-core play that enters the core follows ONE fixed suffix from K0, and a non-core play enters the core iff its node is a core vertex.
  Hence for non-core v, {K0, K3} ∩ Π_t(v) is a function of Λ_t(v). On Γ3 this is R-P-N5-CHAIN §D follow-up 1 (signed by both referees).
- (a) PRIV: e_o ∈ E_t(p_e) \ E_t(p_b); z := top of the e-set difference, at least as relevant as e_o, so z is also the top of the
  π-difference, same side. [VJ] with equal Λ decides by the top d of Π_t(p_e) Δ Π_t(p_b). If d ≠ z, d is more relevant than z, so (E-DOM)
  an e-vertex (impossible: z is the top e-vertex of the difference), c_W (in no Π), or K0 / K3 (not in the difference: p_e, p_b non-core,
  same Λ). So d = z, even (e-priorities even, [DEF]); the side holding z is ▷-larger. And the two π's differ (z in one only). Correct.
- (b) UP at s gives e_o ∈ E_s(p_e) (p_e's play starts (pad,) e_o; e_o more relevant than Λ, so not on the cycle unless it is Λ, which UP
  excludes). By (a) the ⊴-order of the faces at s is a function of the π-pair; LOC-GATE3 / NO-TIE3 make σ̄_s(o) a function of the order.
  A flip changes the order, hence the π-pair. Correct.
- (b′) Relock at t: by (a), π(E_(t−1)(p_e)) <lex π(E_(t−1)(p_b)) and π(E_t(p_e)) >lex π(E_t(p_b)). Λ(p_b) fixed over {t − 1, t}: E(p_b) rises
  (E-MON3 / E-MON); projection to π of a lex rise does not fall (top above e_o: same top, same side; top below e_o: projections equal).
  So π(E_t(p_e)) >lex π(E_t(p_b)) ⊵lex π(E_(t−1)(p_b)) >lex π(E_(t−1)(p_e)). Unlock symmetric. Correct.
- K10 (LAM ∧ PRIV ∧ not UP): IDEAL-CYC — fixes G1's argument from R123 B-ONLY: correct (p_b = β is no exception; e_o → c_W gives
  Λ(p_e) = c_W ≠ Λ(p_b); else Λ(p_e) less relevant than every e-vertex, so UP). **Γ3 — the same argument from P-N5-CHAIN B-ONLY3 (GT-1):**
  p_b = pβ_g is no exception (exceptions: c_W, e's with successor c_W, their pads pe_g); if e_o → c_W then Λ(pe_g) = c_W ≠ Λ(pβ_g), not
  LAM; otherwise pe_g is no exception, Λ(pe_g) is less relevant than every e-vertex, so UP. K10 is empty at every state 0..T3.

### 2.3 NP-SHAPE (a), (b): CORRECT, both runs
- e_o's only in-edge is from o (Γ: [DEF]) or from pe_o, whose only in-edge is from o (Γ3: [G3]). NP_t: e_o on P_t(p_b) (more relevant than
  Λ, so on the prefix). Its predecessor on the play is pe_o (Γ3) and before that o; positional play, so σ̄_t(o) = p_e, and from o the play
  is P_t(o) = o · P_t(p_e) ((PL)); A_t := the part before o. Same cycle: Λ equal; E_t(p_b) = (e-letters of A_t above Λ) ⊔ E_t(p_e) (pads
  and o in no Π, CN2-3). (b) NP_s forces σ̄_s(o) = p_e; a flip changes σ̄(o): at most one side, a relock if before, an unlock if after.
  Correct (premise F3 added by G3; with GT-8's naming).

### 2.4 E-FACE-PAYS (a)-(d), WAIT-QUIET: CORRECT, both runs; PROVISO holds on BOTH runs
- (a) Relocks leave p_e: each is a change step of p_e (GATE-RACE (a)); unlocks leave p_b: change steps of p_b; alternation gives unlocks ≤
  1 + relocks. No PRIV / LAM / UP used. Correct.
- (b) If e_o ∉ P(D) at s, the pad pe_o is not on P(D) either (its only successor is e_o), so P_s(p_e) = (pe_o,) e_o · P_s(D), both prefix
  vertices on the path; Ω_s(p_e) = ext(pe_o, ext(e_o, Ω_s(D))) (F3; on Γ only e_o). For fixed vertices not in Π_s(D) the map
  (Λ, Π, k) ↦ (Λ, Π ∪ ({e_o, pad} above Λ), k + const) is injective. So Ω(p_e) changes iff Ω(D) changes, at each t with the hypothesis
  at t − 1 and t. Correct.
- (c) (a) + (b); ch_D splits into Λ-changes (≤ 2M + 2, CYC + F2), E-changes inside ≤ 2M + 3 Λ-intervals (each has one top, a letter;
  ≤ M letters; ≤ C per (letter, interval)), and the rest (gam). Correct.
- (d) GATE-RACE (b); ch_f = lam_f + nl_f, lam_f ≤ lamch(o). Correct.
- WAIT-QUIET = (a) + (b) with the proviso over the whole run: relocks ≤ ch_(p_e) = ch_D ≤ K, unlocks ≤ K + 1, flips ≤ 2K + 1. Correct. Its
  words «D changes value at most K times while its play avoids e_o» read naturally as «over a run in which D's play avoids e_o»; the proof
  needs that reading (if the proviso fails at some steps, changes of p_e there are not bounded by D's). Moot once the proviso always holds.
- PROVISO on IDEAL-CYC (fixes entry 2, from R123 B-ONLY): D = c_W: its loop. D a mover: if e_o ∈ P_t(D), the vertex after e_o is D, the
  play's first vertex, so the play is one cycle through e_o and Λ_t(D) is e_o or more relevant, against B-ONLY at the mover D. Correct.
  **On Γ3 the same proof from P-N5-CHAIN B-ONLY3 (GT-1):** e_o's successor on Γ3 is D itself ([G3] puts no pad on e → W-target); D a
  mover is no exception; if e_o ∈ P_t(D), the play is the one cycle D … o, pe_o, e_o, D, which carries e_o, so Λ_t(D) is e_o or more
  relevant; B-ONLY3 at D contradicts. So on Γ3 too, at
  every state 0..T3, D's play avoids e_o, and (b), (c), WAIT-QUIET hold with no proviso (conditional on R125 like every Γ3 statement).

### 2.5 SAME-SUFFIX, STEP-BOUND: CORRECT, both runs (with fixes G2)
- SAME-SUFFIX: o's play passes its chosen successor f*; P_t(f*) = P_f* · P_t(y) is a lasso, so o ∉ P_f* (else f*'s play would close at o
  before y) and o ∉ P_t(y) (else y's play would reach f* ∈ P_f*). So Λ_t(o) = Λ_t(y) = Λ_t(f) for every f: constant on W. Π_t(f) =
  Rel(P_f) ⊔ Π_t(y) (disjoint, P_t(y) avoids P_f), so Π_t(f) Δ Π_t(f′) = Rel(P_f) Δ Rel(P_f′), constant; if empty, k-difference |P_f| −
  |P_f′|, constant. Every pairwise order is constant on W. Odd gate: the ◁-smaller face (LOC-GATE3, NO-TIE3): constant. Even mover:
  G2's argument (the set B of ▷-best options is constant for t − 1 ∈ W; [HOW] puts σ in B at W's second step and keeps it after).
  G2's tie rule is right on both runs: R118 (a) (quoted, verbatim), and on Γ3 P-N5-CHAIN §2's HOW3 definition says the same in its own
  words («a HOWARD step: every mover x goes to a successor of ⊴-largest Ω_t value and keeps σ_t(x) if it is such a successor»; l. 88-89)
  — a more direct citation than G2's route through [N5XI] and REACH3-ALL's proof, which is also correct.
- STEP-BOUND: if no vertex of P_(t−1)(x) changes successor at t, P_t(x) = P_(t−1)(x) and the value, a function of the play, is unchanged.
  ch_x ≤ T. Trivially correct.

### 2.6 PARALLEL (i)-(iii): CORRECT, both runs
- The projection H = E(b) ∩ U_y of a lex rise rises (as in §2.2 (b′)); so the top x of the H-change enters: x ∈ H_s \ H_(s−1). x is an
  e-vertex above w = Λ(b): on P_s(b) (it is in Π_s(b)) and not on P_(s−1)(b) (else, being above w, it would be in E_(s−1)(b) ∩ U_y).
  Expelled z: symmetric. (ii) x is the top of a difference containing z. (iii) The two plays agree from b up to and including u′; z (resp.
  x) is on one play only, so not in that common prefix: after u′. Correct.

### 2.7 PAIR-EXPEL, EXPEL-COUNT: CORRECT, both runs; no P-N5-SPLIT premise needed (GT-2), 3M re-derived (GT-5)
- Λ: b′ follows u′ on P_s(b) and P_s′(b) (§2.6 (iii)), so Λ_s(b′) = Λ_s′(b′) = w; Λ(b′) moves only up in reward (F1, F2), so it is w on
  [s, s′]. Same for u′, and a′ at s′ − 1.
- Step 1, u′ a mover: σ_s(u′) = b′, σ_(s′−1)(u′) = a′ ≠ b′ (u′ moves to b′ at s′), so s′ − 1 > s and a first s″ ∈ (s, s′ − 1] with
  σ_s″(u′) ≠ σ_(s″−1)(u′) = b′ exists. Ω_(s′−1)(u′) ⊵ Ω_s″(u′) (F1) ▷ Ω_(s″−1)(u′) (STRICT) = ext(u′, Ω_(s″−1)(b′)) (F3, F6: u′ not a cycle
  node) ⊵ ext(u′, Ω_s(b′)) (F1, F4′; u′ in no Π, CN2-3). Ω_(s′−1)(u′) = ext(u′, Ω_(s′−1)(a′)); ⊴ total and F4′ monotone, so
  Ω_(s′−1)(a′) ▷ Ω_s(b′). u′ a gate: Ω_s(b′) ◁ Ω_s(a′) ⊴ Ω_(s′−1)(a′) (LOC-GATE3, NO-TIE3, F1). Correct; every fact is a P-N5-CHAIN fact
  (Γ3) or R118 (b)/(c) + R123 (IDEAL-CYC); this is P-N5-SPLIT's REWIN (a) argument, re-written in full, not cited (GT-2).
- Step 2: equal Λ = w; [VJ] decides Step 1 by the top d of the Π-difference of a′ (at s′ − 1) and b′ (at s). If d ≻ z: d is an e-vertex
  (E-DOM; c_W in no Π; K0, K3 not in the difference: a′, b′ non-core, same Λ, GT-7), even, so on a′'s side: strict lex on U_z. If d ≼ z,
  every element of the difference is ≼ z, so the two agree on U_z. So ⊵lex. Correct.
- Step 3: u′ is not an e-vertex (one successor), plays agree up to u′: E_(s′−1)(b) = A ⊔ E_(s′−1)(a′), E_s′(b) = A ⊔ E_s′(b′) (same A).
  The change of E(b) at s′ expels z, so its top x′ ≻ z (§2.6 (ii)) and x′ ∈ E_s′(b) \ E_(s′−1)(b), hence x′ ∈ E_s′(b′) \ E_(s′−1)(a′), and the
  two sets agree above x′. Restricted to U_z the top of the difference is x′ (x′ ∈ U_z), on b′'s side. Correct.
- Steps 2, 3: E_s′(b′) ∩ U_z >lex E_(s′−1)(a′) ∩ U_z ⊵lex E_s(b′) ∩ U_z. Correct.
- EXPEL-COUNT: every run of z in E(b) on J but the last ends with an expulsion; each expulsion has a split pair (u′, b′); the expulsions
  through one pair lie in one Λ-interval J_b′ of b′ (Λ(b′) = w from the first to the last, as above) and carry pairwise distinct
  E(b′) ∩ U_z (strict rise along time); so their number ≤ Dhi_z(b′, J_b′); ≤ 3M pairs (GT-5). a_z ≤ 1 + Σ ≤ 1 + 3M·max Dhi_z. Correct.

### 2.8 A*-EQUIV: (i) CORRECT both runs (re-derived, GT-4); (ii), (iii) CORRECT ON Γ3 ONLY, conditional on P-N5-SPLIT (and R125)
- (i) C ≤ A*_all: every y-top of (v, I) is an entry of y into E(v) (E-MON3 / E-MON: the top enters), and two y-tops are separated by an
  exit, so each y-top starts a different run: c_y(v, I) ≤ a_y(v, I). A*_all ≤ 1 + M·C: every run of z but the first in J starts at a
  change of E(b) (z enters); the changes in J number Σ_y c_y(b, J) ≤ M·C. Both directions use only the definitions and E-MON3 / E-MON.
- (ii) H := E(b) ∩ U_y rises at each change (projection, §2.2 (b′)), so Dhi_y(b, J) − 1 = #changes of H; each change's top x ∈ U_y enters
  H, i.e. E(b), and starts a new run of x: #changes ≤ Σ_(x ∈ U_y) a_x(b, J) ≤ M·A*_route for a route vertex b. SPLIT-COUNT: c_y(v, I) ≤
  Σ over ≤ 3M split pairs of Dhi_y(b, J_b). Correct given SPLIT-COUNT, which is a Γ3 statement (P-N5-SPLIT's scope: «nothing outside
  Γ3(G)»). On IDEAL-CYC (ii) is not proved by any premise named.
- (iii) C-EQUIV (P-N5-SPLIT §6, GT-3) is a Γ3 statement about T3. So (iii) is a Γ3 statement. With (i), (ii): C poly ⇒ A*_all poly ⇒
  A*_route poly (subset maximum) ⇒ C poly. Correct on Γ3.
- **GT-9 (scope, required):** the line states A*-EQUIV with no run named except through «T3». It must say that (ii) and (iii) are on Γ3
  only (their premises SPLIT-COUNT, C-EQUIV are Γ3 statements), (i) on both.

## 3. Replays with my own code (no lane code; scratch/gate_replay.py, scratch/gate_lev.py; logs scratch/gate_logs/)
### 3.1 Engines and counters
- Own engine: my lane's xicyc_replay.howard on my lane's own Γ / Γ3 builder (from R104 / R117's text; REFEREE successor 26). 'cyc' =
  IDEAL-CYC Howard on Γ(G); 'g3' = HOW3, Howard on Γ3(G) until no mover has a strictly better successor (states 0..T3, N5′-xi's mover phase
  up to its first fallback by REACH3-ALL). Tie rule: keep the current option if best, else the larger index (allowed by R118 (a) and
  P-N5-CHAIN §2). Caps 3000 (cyc) / 20000 (g3); no run reached its cap.
- gate_replay.py counts every stated claim at its own unit (header of the script): GATE-RACE (a) per flip and (b) per gate; TRIGGER per
  flip; GATE-LOW-NULL (a) per (gate, state) as the ORDER equivalence, (b) and (b′) per flip; K10 states; NP-SHAPE (a) all four parts incl.
  P(p_b) = A·o·P(p_e), (b) per flip; E-FACE-PAYS (a) both unlock bounds, (b) exact (dexact) with dpass, (c) both inequalities, (d); STEP-BOUND
  per (vertex, step); PARALLEL (i)-(iii) incl. x after u′, at EVERY vertex b, every Λ-interval and every y ∈ {w} ∪ (e-letters above w);
  PAIR-EXPEL per same-pair couple at every (b, J, z); EXPEL-COUNT per (b, J, z); split pairs ≤ 3M per run; A*-EQUIV (i) both inequalities and
  (ii) per run.
- Controls (must fire): cJoin (flips whose JOINED face kept its value: the left-face test is not vacuous), cLow (order vs π taken strictly
  below e_o), cNP (NP states tested), cD (steps where p_e and p_b change differently), cU (couples tested with U_z := ∅).
### 3.2 Results (19 instances: box 91's 11 and box 93's 8, sha1-checked §1.1)
- cyc (replay_cyc.out) and g3 (replay_g3.out): EVERY must-be-0 counter is 0 on every instance, on both engines, including k10 = 0 and
  dpass = 0 on g3 (as GT-1 predicts from B-ONLY3). Controls fire on both: cJoin 588, cLow 14,013, cNP 1,469, cD 13,048 (totals, each
  engine); cU 16,929 (cyc) / 29,758 (g3) couples. Flips 891 per engine; T ≤ 199.
- Growth rows reproduced (both engines identical on these): MW8_2 / MW32_2: C 17 / 65 = 2n + 1, max flips 34 / 130 = 4n + 2, A*_all
  18 / 66 = 2n + 2; MWR4/8/16_2: max flips 9 / 17 / 33 = 2n + 1, C 5 / 9 / 17 = n + 1, at the max-flip gate lamch 0 and ch_D = n
  (flips = 2·ch_D + 1: E-FACE-PAYS (d) / WAIT-QUIET tight).
### 3.3 DEAD list and copy rows (gate_lev.py, cyc engine; lev_cyc.out; instances sha1-checked: box94 44/44, box95 fix1 16/16, box93 k6 16/16)
- WC: T 4 on WC4_2, WC16_2 (n = 8 not pinned, D-7). RA-MULT: C 17 / 65 on MW8_2 / MW32_2 (= 2n + 1, m = n). RA path count: C = 3 on FW8_2,
  FW16_2 (P = F_(d+2) − 1 NOT re-counted). K7: C = 2 on Ku_4, Ku_8, Ku_16, Kprev_8 (§3.2, both engines). K1-FLIP(c): flips 2n + 1 with lamch 0
  on MWR4/8/16_2 (both engines). Nesting multipliers: on the 20 simultaneous instances C, max flips and T equal one MW(n)'s (n = 4: 9, 18, 31;
  n = 8: 17, 34, 55); NSQ2_4 / NSQ3_4: T 103 / 271 (sequential sum), C 9, flips 18. Db / Dbr: C, max flips, T of one MW(n) (9 / 18 / 31, 17 /
  34 / 55). K6 LAG TOWER: its CNT measure is box 86's and was NOT re-counted (my C on the LT4 / LT5 instances is 1-2, context only).
- SAME-SUFFIX copy rows: S(R_j) = S(R_(j−1)) as SETS on every level ≥ 2 of the 20 simultaneous box 94 instances and the 8 Db / Dbr
  instances; NOT on NSQ2_4, NSQ3_4 (sizes 18, 22, 26; seteq 0), see D-4. flips(g_Qj) = 0 at levels ≥ 2 on NDV and NDB (all 8); 2 on NV;
  18 / 34 on ND, NP, NSQ, Db, Dbr (not claimed there).
- Not re-run: L-RED's records (context only, read after my verdict, §7); the lane's d96 CTRL=anti (my cD / cJoin are other controls).

## 4. DATA rule on L-2, clause by clause (each counter's predicate and increment read in the lane's code at 9c0349b1)
Tools read: box91/mult91.py (l. 98-112 GATE-RACE / TRIGGER; l. 118-175 PARALLEL, EXP-PATHS, PAIR-EXPEL), box92/gate92.py (l. 22-44),
box92/astar92.py, box93/np93.py (l. 30-75), box94/lev94.py + check94.sh, box96/d96.py. Every count is 0 where the line says 0; the defects
below are in what the words say is counted. None changes a statement; all are covered by my own replay (§3), which counts each stated
claim with the stated unit.
- D-1 (GATE-RACE / TRIGGER, required). «(unit gate, whole run; …)». In mult91 the unit of grfail, gr2fail is an Odd vertex with two
  successors (the gates and K2), but grwhy is incremented once per FLIP (`why += 1` per flip, summed) and trfail once per flip whose left
  face changed its e-set (`c["trfail"] += 1` inside the flip loop). New unit: «(unit: Odd vertex with two successors for grfail and gr2fail,
  flip for grwhy and trfail; whole run; …)».
- D-2 (GATE-LOW-NULL, required). gate92's decfail counts LAM ∧ PRIV ∧ e_o ∈ E(p_e) states at which the top of E(p_e) Δ E(p_b) is LESS
  relevant than e_o — impossible under PRIV (e_o itself is in the difference), so decfail does not test (a)'s claim (the ⊴-order of the faces
  equals the lex order of the π's). glnfail and lowflip are counted per FLIP (on LAM ∧ PRIV steps at t − 1 and t, UP not required), not per
  (gate, state); (b′) has no lane counter. New words: «GATE-LOW-NULL: decfail 0 (unit (gate, state): the decider is at least as relevant
  as e_o; (a)'s order equivalence is not counted by the lane), glnfail and lowflip 0 (unit: flip with LAM ∧ PRIV at t − 1 and t; S11),
  (b′) no separate lane DATA». (My replay counts (a), (b), (b′) directly: §3.)
- D-3 (NP-SHAPE / E-FACE-PAYS, required). np93: npside, npsub are per (gate, state); npboth, npkind per flip; relfail, unlfail, dfail per
  gate / step as written. unlfail is `unl > 1 + ch_(p_e)`: it tests neither of the two stated bounds «unlocks(o) ≤ 1 + relocks(o)» and
  «unlocks(o) ≤ ch_(p_b)» (it is implied by the first and relfail). New words: «npside, npsub (unit (gate, state)), npboth, npkind (unit
  flip), relfail (relocks > ch_(p_e)) and unlfail (unlocks > 1 + ch_(p_e); the bounds unlocks ≤ 1 + relocks and unlocks ≤ ch_(p_b) are not
  counted by the lane) (unit gate), dfail (a proxy …) …».
- D-4 (SAME-SUFFIX, required; a number in the clause is FALSE as worded). «copy rows S(R_j) = S(R_(j−1)) on every level … (unit level; box
  94's 22 instances)». (1) lev94 prints |S(R_j)| (a size, `R {len(sr)}`) and check94 compares printed rows: set equality is not measured.
  (2) On NSQ2_4 and NSQ3_4 the lane's own rows (box94/out/lev94_own.out and lev94_g3.out) give |S(R_1)|, |S(R_2)|, |S(R_3)| = 18, 22, 26:
  the copy rows do NOT hold there (NSQ's levels run one after another, box94-nest.md l. 20; SAME-SUFFIX is not claimed there). My replay
  (§3.3): S(R_j) = S(R_(j−1)) AS SETS on every level of the other 20 instances and of the 8 Db / Dbr instances; seteq 0 on NSQ's levels 2-3.
  New words: «SAME-SUFFIX: copy rows S(R_j) = S(R_(j−1)) as sets on every level of box 94's 20 simultaneous-clock instances (all but NSQ2_4,
  NSQ3_4, whose levels run one after another) (REFEREE replay, own engine; the lane's lev94 compares sizes), and 0 flips at the copied gates
  on NDV and NDB (unit level)».
- D-5 (PARALLEL / PAIR-EXPEL / EXPEL-COUNT, required). In mult91: afail is `a_z > 1 + Σ_(x∈X(z)) a_x` and pxfail `Dhi > 1 + Σ P_X(z)`,
  the counters of box 91's Corollary EXP-PATHS (a), (b), which is NOT a statement of this packet; CTRL=a0 is EXP-PATHS's control. par1-3 are
  incremented only at changes of H that expel a letter (`if Z:`), only at route tuples (b reached as a new successor of a split pair of
  some (v, I, y)), and par1-3 do not test «x lies strictly after u′». New words: «PARALLEL: par1-3 0 (unit: change of H with an expelled
  letter, at route tuples; x's position after u′ not counted); PAIR-EXPEL and EXPEL-COUNT: pefail, ecfail, pelam 0; lexfail and dhifail 0
  (E-MON3 on H)» and drop «afail, pxfail» and «CTRL=a0 afail 14 / 96» (or label them «counters of box 91's EXP-PATHS, not a statement
  here»).
- D-6 (A*-EQUIV): cfail is per (v, I, y) with y a top (astar92); «(unit (v, I, z))» names the same tuple with another letter. Optional.
- D-7 (PROVISO, E-FACE-PAYS (b) exact form, growth, DEAD): read and CORRECT as worded (d96 dpass per (gate, state); L-RED's dexact cited as
  L-RED DATA, not a premise; growth numbers reproduced by my replay, §3). WC's «n = 8» has no frozen instance (only WC4_2, WC16_2):
  optional, say «n = 4, 16» or pin the n = 8 instance.

## 5. Line L-2: does NOT match yet. Strings (old must occur once in L-2; apply in this order; each old string checked to occur exactly once)
REQUIRED (statement scope, premise names, DATA words):
| id | old (in L-2) | new |
| --- | --- | --- |
| R-1 (GT-2) | «PROVED-CONDITIONAL on P-N5-SPLIT §2 (a))» | «PROVED-CONDITIONAL on P-N5-SPLIT §3 (a), Lemma REWIN (a)'s argument, which the packet writes out in full from P-N5-CHAIN's F1, STRICT, F3, F6, F4′, CN2-3)» |
| R-2 (GT-2) | «also §2 (a), SPLIT-COUNT and C-EQUIV» | «also §3 (a), SPLIT-COUNT and C-EQUIV» |
| R-3 (GT-3, GT-9) | «(Corollary A*-EQUIV, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and P-N5-CHAIN's C-EQUIV) C ≤ A*_all ≤ 1 + M·C and C ≤ 3M·(1 + M·A*_route), so T3 is polynomial» | «(Corollary A*-EQUIV, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV) C ≤ A*_all ≤ 1 + M·C (on both runs) and, on Γ3 only, C ≤ 3M·(1 + M·A*_route), so T3 is polynomial» |
| R-4 (GT-6) | «(b) F1, F2, F3, (e) in its per-vertex form» | «(b) F1, F2, F3, F4′, F6, (c) STRICT, (e) in its per-vertex form» |
| R-5 (GT-6) | «RESULTS R123 Lemmas CN2, LOC-GATE, B-ONLY («» | «RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY («» |
| R-6 (GT-6, GT-7) | «Corollary NO-TIE («at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»), for IDEAL-CYC;» | «Corollary NO-TIE («at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»), and (E-DOM) and (Core) read off R104's priorities and closed core with LOC-K2 (for non-core vertices: the core is entered only at K0 and then follows one fixed suffix, so K0, K3 lie on the play iff Λ is a core vertex), for IDEAL-CYC;» |
| R-7 (GT-7) | «NO-TIE3, (E-DOM), (Core), E-MON3 of the pending packet P-N5-CHAIN» | «NO-TIE3, (E-DOM), (Core) in its W-1 repaired reading (non-core vertices; every use here compares two non-core vertices), E-MON3 of the pending packet P-N5-CHAIN» |
| D-1 | «grfail, gr2fail, grwhy, trfail 0 (unit gate, whole run;» | «grfail, gr2fail, grwhy, trfail 0 (unit: Odd vertex with two successors for grfail and gr2fail, flip for grwhy and trfail; whole run;» |
| D-2 | «GATE-LOW-NULL: decfail, glnfail, lowflip 0 (unit (gate, state); S11), with» | «GATE-LOW-NULL: decfail 0 (unit (gate, state): the decider is at least as relevant as e_o; (a)'s order equivalence is not counted by the lane), glnfail and lowflip 0 (unit: flip with LAM ∧ PRIV at t − 1 and t; S11), (b′) no separate lane DATA, with» |
| D-3 | «npside, npsub, npboth, npkind, relfail, unlfail, dfail (a proxy for E-FACE-PAYS (b)) 0, and k1both = k1c2 (unit gate;» | «npside, npsub (unit (gate, state)), npboth, npkind (unit flip), relfail (relocks > ch_(p_e)), unlfail (unlocks > 1 + ch_(p_e); the bounds unlocks ≤ 1 + relocks and unlocks ≤ ch_(p_b) are not counted by the lane), dfail (a proxy for E-FACE-PAYS (b)) 0, and k1both = k1c2 (unit gate for relfail, unlfail, k1both, k1c2;» |
| D-4 | «SAME-SUFFIX: copy rows S(R_j) = S(R_(j−1)) on every level and 0 flips at the copied gates on NDV and NDB (unit level; box 94's 22 instances)» | «SAME-SUFFIX: copy rows S(R_j) = S(R_(j−1)) as sets on every level of box 94's 20 simultaneous-clock instances (all but NSQ2_4, NSQ3_4, whose levels run one after another and whose rows differ) (REFEREE replay, own engine; the lane's lev94 compares sizes), and 0 flips at the copied gates on NDV and NDB (unit level)» |
| D-5a | «PARALLEL, PAIR-EXPEL and EXPEL-COUNT: par1-3, lexfail, afail, pxfail, dhifail, pefail, ecfail, pelam 0 (unit change of H, tuple (b, J, y) or same-pair couple;» | «PARALLEL: par1-3 0 (unit: change of H with an expelled letter, at route tuples; x's position after u′ not counted); PAIR-EXPEL and EXPEL-COUNT: pefail, ecfail, pelam 0, with lexfail and dhifail 0 (E-MON3 on H) (unit change of H, tuple (b, J, y) or same-pair couple;» |
| D-5b | «, CTRL=a0 afail 14 / 96» | «» (delete: EXP-PATHS's control) |
Equivalent wording is acceptable for R-6, R-7 and D-1..D-5 if it says the same; R-1..R-5 as given or with the same facts.

RECOMMENDED, the Lead's call (GT-1; a ruling exists, 2026-11-09 09:24Z (b), sending B-ONLY on Γ3 to P-N5-BONLY3, made on the premise that
B-ONLY on Γ3 is not a P-N5-CHAIN fact; it is):
| id | old | new |
| --- | --- | --- |
| G-a | «while on Γ3 that case needs B-ONLY on Γ3, which is not a premise here (OPEN within this entry, covered by E-FACE-PAYS (a) only)» | «and on Γ3 it does not occur either, by P-N5-CHAIN's Lemma B-ONLY3 (pending R125; the same argument with the pads pβ_g, pe_g)» |
| G-b | «while on Γ3 the proviso is a hypothesis here» | «and on Γ3 it holds at every state 0, …, T3 by the same argument from P-N5-CHAIN's Lemma B-ONLY3 (pending R125), so there too (b), (c) and WAIT-QUIET hold with no proviso» |
| G-c (after R-7) | «LOC-GATE3, NO-TIE3, (E-DOM)» | «LOC-GATE3, B-ONLY3, NO-TIE3, (E-DOM)» |
If G-a..G-c are not taken, L-2's present words are TRUE (they speak of this entry's premises) and I sign them as they stand.
OPTIONAL: GT-8 (fact names), D-6 («(v, I, y)»), D-7 (WC «n = 4, 16» or pin n = 8), GT-4 / GT-5 (the packet's citations of N5-CORE-forms
and L-RED R228 §2 are not in L-2; nothing to change in the line).

## 6. TARGET.md diff: CLEAN
- TARGET.md v1.0 §2 (M4: a deterministic algorithm, polynomial p, every parity game, outputs (W_E, W_O)) and §4 (restricted class,
  d constant, hidden super-polynomial term, conjecture / empirical observation / «clearly»: not M4). The statements are lemmas about ONE
  run of Howard / VJ on Γ3(G) (up to T3) and on IDEAL-CYC(G), for every genome; each is a reduction between counts of the same run and none
  bounds T3, T_CYC, C or A*_all. L-2's closing sentence paraphrases §2 and §4 correctly, says «not M4 and not M3», «G-N5-TIME stays OPEN»,
  «not a step-4 pass, not a TARGET.md claim». No TARGET object (ParityGame, EvenWins, W_E) is redefined. Nothing to change.

## 0. Verdicts (date -u at writing: see the commit; REFEREE successor 31). Γ3 rows CONDITIONAL on R125 (P-N5-CHAIN), as the packet states.
| § | statement | verdict | run |
| --- | --- | --- | --- |
| 3.1 | GATE-RACE (a), (b); TRIGGER | **SIGN** | both |
| 3.2 | GATE-LOW-NULL (a), (b), (b′) | **SIGN** (premises as R-4..R-7; (Core) for non-core vertices) | both |
| 3.2 + G1 | K10 empty | **SIGN** on IDEAL-CYC (R123 B-ONLY); on Γ3 also TRUE by P-N5-CHAIN B-ONLY3 (GT-1, §2.2) | both |
| 3.3 | NP-SHAPE (a), (b) | **SIGN** | both |
| 3.4 | E-FACE-PAYS (a)-(d); WAIT-QUIET | **SIGN** (WAIT-QUIET read «over a run in which D's play avoids e_o», moot below) | both |
| fixes 2 | PROVISO (IDEAL-CYC; R123 B-ONLY) | **SIGN**; on Γ3 also TRUE by P-N5-CHAIN B-ONLY3 (GT-1, §2.4) | both |
| 3.5 | SAME-SUFFIX (with G2's tie rule); STEP-BOUND | **SIGN** | both |
| 3.6 | PARALLEL (i)-(iii) | **SIGN** | both |
| 3.7 | PAIR-EXPEL; EXPEL-COUNT | **SIGN** (labelled conditional on P-N5-SPLIT, PENDING; the proof needs no SPLIT statement, GT-2; 3M re-derived, GT-5) | both |
| 3.8 | A*-EQUIV (i) | **SIGN** (re-derived, GT-4) | both |
| 3.8 | A*-EQUIV (ii), (iii) | **SIGN, Γ3 ONLY** (R-3), CONDITIONAL on P-N5-SPLIT (PENDING: SPLIT-COUNT, C-EQUIV) and R125 | Γ3 |
| §5 | DEAD list | reproduced as stated (own engine, §3.3) except K6's CNT and FW's P (not re-counted; their C / flips / T rows reproduced) | — |
No GAP; nothing REFUSED. Pending-packet premises: P-N5-CHAIN (R125, at CHECKER C139 Add. 1) for every Γ3 row; P-N5-SPLIT (both referees SIGN,
conditional on R125; not landed) for A*-EQUIV (ii), (iii), and by the packet's own label for PAIR-EXPEL / EXPEL-COUNT.
Line L-2: does NOT match; required R-1..R-7, D-1..D-5 (§5); recommended G-a..G-c (Lead's call).

## 7. Adversary records, read AFTER §0 (context only, not signatures)
- L-RED 63 R229-box94 Addendum A (claude/l-red, read at origin): its G1-G6 match the packet's fixes entry 1; its «MATCHES» items agree
  with my §2. Its G1 says «On Γ3 the same needs B-ONLY on Γ3: it is not in P-N5-CHAIN's fact list (§1)» — true of the PACKET's §1 list,
  and the source of fixes G1's sentence; neither record noticed that P-N5-CHAIN itself proves B-ONLY3 (GT-1). Its sha1 list agrees with
  mine. It reports the echo INCLUSION on levels including NSQ; it does not address the copy-row sizes on NSQ (D-4).
- Nothing in the records changes a verdict of §0. GT-2, GT-3, GT-6, GT-7, GT-9 and D-1..D-5 are not raised there.

## 8. Tools and outputs (committed, docs/referee/scratch/)
- gate_quotes.py (L-2's quotes vs trunk RESULTS) → gate_logs/quotes_L2.out; gate_replay.py (both engines, all statements, controls) →
  gate_logs/replay_cyc.out, replay_g3.out; gate_lev.py (DEAD numbers, copy rows as sets) → gate_logs/lev_cyc.out. Engines: xicyc_replay.py,
  xicyc_vj.py (my lane's, unchanged). Instances: `git archive 9c0349b1 experiments/si/box9{1,3,4,5}` into the scratchpad, sha1-checked.
