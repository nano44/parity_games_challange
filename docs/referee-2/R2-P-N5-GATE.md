# R2-P-N5-GATE: REFEREE-2 second review of packet P-N5-GATE (L-SI)
Referee: REFEREE-2 successor 37 (session_01V5yGRVhzXCnkFQbXe6tmzW), Opus 5.5 under D1 («Never downgrade the referee to save money.»).
Written 2026-11-11/12 (date -u; see the commits), section by section.

Independence: I have not opened docs/referee/R-P-N5-GATE.md (REFEREE 31) or notes/REFEREE.md. I have not read L-RED's R228 / R229 reports or
L-RED's tools. The packet and fixes quote them, and I treat those quotes as claims, not as premises. Lane code is not imported: my replay
is R2-P-N5-GATE/r2gate.py, on REFEREE-2's own engines.

## Box 1: object, premises, and §3.1-§3.4

### 1.0 Object (hashes re-computed from `git show`)
- Packet: claude/l-si 4066f579, docs/si/P-N5-GATE.md, sha1 f3a584e68b5c998276ea717f42920bdeeca581ab, 25,604 B. It is unchanged at 9c0349b1.
- Fixes: 9c0349b1, docs/si/P-N5-GATE-fixes.md, sha1 1fec4f8c971c0ae89069d0532b6b97a67c2330e5, 12,272 B (entries 1-2).
- Line: L-2, 9c0349b1, docs/si/P-N5-GATE-line-L2.txt, sha1 c0f2007d84afab1e00ef41e24ba8f5f064468cc5, 10,295 B.
  - The Lead (2026-11-11 23:33Z) says L-SI 50 is writing fixes entry 3 and L-3 on top of L-2. My line verdict will be on L-3. Here I give
    the line requirements, and the DATA rule read on L-2.
- Both commits are ancestors of origin/claude/l-si (33a300f1 at my fetch).
- I review the packet with fixes entries 1-2 applied. Where an entry and the packet differ, the entry governs, as the fixes file says.

### 1.1 Premises, checked by script (R2-P-N5-GATE/r2q.py, output r2q.out)
- Every «…» quote in L-2 from a landed source occurs verbatim, whitespace-normalised, in trunk docs/RESULTS.md (86f62c26). These are the
  quotes from R104, R118 (a) and (k), R121 E-MON, R123 B-ONLY and NO-TIE.
- Every P-N5-CHAIN name the packet uses is defined in CHAIN's frozen text (93531b03, sha1 6e613ba7, re-hashed): F1, F2, F3, F4′, F6, DOM,
  STRICT, CYC, (E-DOM), (Core), CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, [OPT].
- But the packet's §1 GLOSSES of four of them are not CHAIN's statements:
  - (G-1) (Core). §1 glosses it as «(K0, K3 lie on both of two plays with the same Λ or on neither)».
    - CHAIN's (Core) is a structural fact: K0 → pA → K3 → K2 and K1 → s → K1 are frozen, K3's only in-edge is from pA, and K0's are from
      q and the pb's.
    - The gloss, read over all vertices, is false. On Γ3, the plays from K3 (K3, K2, r, K1, s) and from K0 (K0, pA, K3, …) both have node
      K1, and only one passes K0. The same holds on Γ with K3 → K2 → K1.
    - It is the sentence P-N5-CHAIN fixes entry 3 (R-W) records as false, and my predecessor's W-1 on P-N5-SPLIT.
    - Every use in GATE compares two NON-core vertices: GATE-LOW-NULL (a) and (b′) compare the faces p_e, p_b (pads on Γ3; e_o and β_o
      on Γ). PAIR-EXPEL Step 2 compares a′ and b′, which are successors of a mover or a gate (pads on Γ3; a gate or a face on Γ).
    - For non-core vertices the repaired reading holds. On Γ3: CHAIN fixes entry 3. On Γ, by R104's definition: K0's in-edges are the
      β's (edge to u = K0) and K1, which is frozen at its loop; K3's only in-edge is K0, which is frozen at K3. So a non-core play passes
      K0 iff it passes K3.
    - So every proof stands; the defect is in the proof text. Line: R-1.
  - (G-2) F3 and F6.
    - §1 glosses F3 as «E_t(v) is the set of e-vertices on v's play at t more relevant than Λ_t(v)». That is the DEFINITION of E (the
      e-vertices of Π_t(v), [VJ]). CHAIN's F3 is the recursion «If Λ_t(v) ≠ v then Ω_t(v) = ext(v, Ω_t(nx_t(v)))».
    - §1 glosses F6 as «an e-vertex has exactly one successor, its W-target». CHAIN's F6 says «No mover is the cycle node of its own
      play … Every non-mover Even vertex has one successor in HOW3». The gloss follows from F6 with [DEF] / [G3].
    - Effect: the packet cites «F3» in §3.1 TRIGGER, §3.2 (b), §3.3 (fix G3) and §3.6, where the definition is meant (harmless).
    - PAIR-EXPEL Step 1 uses CHAIN's F3 itself («Ω_(s″−1)(u′) = ext(u′, Ω_(s″−1)(b′))»). F3 is missing from §3.7's premise row.
    - Line: R-2.
  - (G-3) C-EQUIV. The table row §3.8 and §3.8's heading say «P-N5-CHAIN (C-EQUIV)», and L-2's clause says «P-N5-CHAIN's C-EQUIV».
    CHAIN's frozen text has no C-EQUIV (0 occurrences). It is P-N5-SPLIT's Corollary C-EQUIV (§6). L-2's own premise list says this
    correctly («SPLIT-COUNT and C-EQUIV of the pending packet P-N5-SPLIT»), so L-2 contradicts itself. Line: R-3.
  - (G-4) «P-N5-SPLIT §2 (a)». The packet cites it 5 times and L-2 twice, for «the mover-step inequality chain». In SPLIT's frozen text
    (5bc1b1f3), §2 is Lemma SPLIT with items (i)-(iv): it has no (a). The chain is §3 (a), the proof of REWIN (a) («- (a), u a mover.»).
    - Moreover, PAIR-EXPEL's Step 1 writes the whole chain out from F1, STRICT, F3, F4′, CN2-3, and from LOC-GATE3, NO-TIE3 for a gate.
      It uses no SPLIT statement. See 2.7: PAIR-EXPEL does not depend on P-N5-SPLIT.
    - Line: R-4.
- Landed sources used on IDEAL-CYC: R104 (definitions), R118 (a), (b) F1-F4′, (c) DOM and STRICT, (e) CYC-COUNT in the per-vertex form
  of its signed parenthesis, R121 E-MON, R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2. I read the IDEAL-CYC reading of §1 (fix G4) against
  each proof below (1.5).

### 1.2 §3.1 Lemma GATE-RACE (a), (b), Corollary TRIGGER: SIGN (both runs)
- (a) I re-derived it. Odd plays p at t − 1 and q at t. LOC-GATE3 / NO-TIE3 give Ω_(t−1)(p) ◁ Ω_(t−1)(q) and Ω_t(q) ◁ Ω_t(p). F1 gives
  Ω_(t−1)(q) ⊴ Ω_t(q). So Ω_(t−1)(p) ◁ Ω_t(p).
- (b) Let a, b be the numbers of p → q and q → p flips; flips alternate, so |a − b| ≤ 1. Each p → q flip is at a distinct change step of
  p, so a ≤ ch_p; likewise b ≤ ch_q. Then flips = a + b ≤ ch_p + ch_q, and a + b ≤ 2·min(a, b) + 1 ≤ 2·min(ch_p, ch_q) + 1.
- TRIGGER is a trichotomy of the change at p: Λ changes (α), or inside one Λ-interval E changes (β), or neither (γ).
  - In (β), E-MON3 makes the top enter. By the definition of E (not CHAIN's F3: G-2), the top is on P_t(p).
  - The count «at most 2M + 2» in (α) uses CYC with F2. CYC is missing from the premise row; it is named in the text.
- F2 is listed for (a) and (b) but not used there.
- IDEAL-CYC: LOC-GATE and NO-TIE (R123), F1 (R118 (b)).

### 1.3 §3.2 Lemma GATE-LOW-NULL (a), (b), (b′): SIGN (both runs; (Core) at the faces only, G-1)
- (a) I re-derived it.
  - PRIV puts e_o in E(p_e) \ E(p_b). Let z be the top of E(p_e) Δ E(p_b); z is at least as relevant as e_o, so z is also the top of the
    π's difference, on the same side.
  - With equal Λ (LAM), [VJ] decides by the top d of Π(p_e) Δ Π(p_b). If d were more relevant than z, then by (E-DOM) d would be an
    e-vertex, c_W, K0 or K3. It is not an e-vertex (z is the top e-vertex of the difference). It is not c_W: c_W is never in a Π, since
    a play through c_W has node c_W. It is not K0 or K3: by (Core) in the repaired reading at the non-core faces (G-1).
  - So d = z, which is even, and the side holding z is ▷-larger.
- (b) UP at s gives e_o ∈ E_s(p_e): p_e's play starts with e_o. By (a), Odd's choice is a function of the two π's.
- (b′) At a relock: π_(t−1)(e) <lex π_(t−1)(b) and π_t(e) >lex π_t(b).
  - E(p_b) is lex-nondecreasing (E-MON3: one Λ-interval).
  - A lex-rise of a set does not lower its projection π onto the letters at least as relevant as e_o: the top of the difference is either
    ⪰ e_o (the same top, same side) or ≺ e_o (equal projections).
  - So π_t(e) >lex π_t(b) ⊵lex π_(t−1)(b) >lex π_(t−1)(e). Unlocks are symmetric.
- IDEAL-CYC: (E-DOM) and (Core) hold on Γ by R104's priorities (c_W top, K0 top + 2, K3 top + 3, every β < every e, K1 5, K2 3, the
  unused loop 2, gates 1, movers 0) and its core edges (G-1). The line must name them as R104 facts (R-5).
- Scope (fixes G1, K10): on IDEAL-CYC, every LAM step is UP, by R123 B-ONLY. I re-derived it.
  - p_b = β_o is not an exception of B-ONLY, so Λ(β_o) is below every e-vertex and ≠ c_W.
  - If D = c_W, then Λ(e_o) = c_W: no LAM step.
  - Otherwise e_o is not an exception, so Λ(e_o) ≺ e_o: UP.
- On Γ3 the SAME argument works with P-N5-CHAIN's Lemma B-ONLY3 (§5, in R125's line L-5), whose exceptions are c_W, the e-vertices with
  successor c_W, and their pads pe_g.
  - pβ_o is never an exception. pe_o is one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o).
  - So on Γ3, K10 is empty too, CONDITIONAL on R125 like the rest.
  - (G-5) Fixes entry 1 G1's reason «B-ONLY on Γ3, which is not among P-N5-CHAIN's facts (§1) and not landed» is FALSE: B-ONLY3 is a
    P-N5-CHAIN lemma. The narrower Γ3 scope that G1 and L-2 keep («OPEN within this entry») is a true statement, only weaker than
    available. Line: R-6.
- DATA (mine, 2.9): rec_k10 = 0 on both engines.

### 1.4 §3.3 Lemma NP-SHAPE (a), (b): SIGN (both runs)
- (a) I re-derived it.
  - e_o's only in-edge is from o's e-face (on Γ3 through pe_o, whose only in-edge is from o). So a play through e_o leaves o by p_e.
  - One step the packet leaves implicit, closed here: e_o is on P_t(p_b) and more relevant than its node, so e_o is on the simple-path
    part, not the cycle. Hence the play from p_e never re-enters the prefix A_t · o: if it did, e_o would be on the cycle.
  - So P_t(p_b) = A_t · o · P_t(p_e) with the same cycle and the same Λ, and Π(p_e) ⊆ Π(p_b) gives E(p_e) ⊆ E(p_b) (definition; fix G3
    calls it «F3», G-2).
- (b) NP_s forces σ̄_s(o) = p_e, and a flip changes σ̄(o).

### 1.5 §3.4 Corollary E-FACE-PAYS (a)-(d), Lemma WAIT-QUIET: SIGN (both runs), with the proviso read as «at every state of the run» (R-7)
- (a) GATE-RACE (a) applied to relocks (left face p_e) and to unlocks (left face p_b), plus alternation.
- (b) If e_o ∉ P_(t−1)(D) ∪ P_t(D), then P_s(p_e) = (pe_o,) e_o · P_s(D) for s = t − 1, t. (e_o's only successor is D: F6 with [DEF];
  pe_o's only in-edge is from o, so D's play avoids pe_o too.)
  - The map (Λ, Π, k) ↦ (Λ, Π ∪ ({pe_o, e_o} ∩ above Λ), k + |prefix|) is injective, since the added vertices are not on P(D). So p_e's
    value changes iff D's does.
- (c) If the proviso holds at every state, (b) gives S(p_e) = S(D) on t ≥ 1. Then:
  - unlocks ≤ 1 + relocks ≤ 1 + ch_D;
  - ch_D = (Λ-changes ≤ 2M + 2: CYC, F2) + (E-changes inside Λ-intervals, each with one top: ≤ (2M + 3)·M·C) + gam(D).
  - IDEAL-CYC: R118 (e) in its per-vertex parenthesis.
- (d) GATE-RACE (b); ch_f = lam_f + nl_f and lam_f ≤ lamch(o).
- WAIT-QUIET: relocks ≤ ch(p_e) = ch_D ≤ K and unlocks ≤ K + 1, so flips ≤ 2K + 1.
  - This holds when D's play avoids e_o at EVERY state of the run (the hypothesis of (c)).
  - The packet's «D changes value at most K times while its play avoids e_o» also admits a weaker reading: K counts only D's changes on
    avoiding windows. Under that reading the proof does not apply at the steps where D's play passes e_o.
  - On IDEAL-CYC the two readings coincide (PROVISO below). On Γ3 they coincide given B-ONLY3 (below). The line must still state the
    proviso as «at every state» (R-7).
- PROVISO (fixes entry 2, IDEAL-CYC, cited from L-RED 63 and re-derived by L-SI box 96): I re-derived it.
  - If D = c_W, its play is its loop.
  - Otherwise D is a mover. If e_o ∈ P_t(D), the vertex after e_o is D, the first vertex of the play, so the whole play is the cycle and
    carries e_o. Then Λ_t(D) ⪰ e_o, against R123 B-ONLY at the mover D.
  - On Γ3 the same argument works with B-ONLY3 at the mover D (D is a mover, not a pad: e_o → x_wt directly, [G3]). So the PROVISO also
    holds on Γ3, CONDITIONAL on R125 (G-5).
- DATA (mine, 2.9): dpass = 0 on both engines; efbfail, efcfail, wqfail = 0.

## Box 2: §3.5-§3.8

### 2.5 §3.5 Lemma SAME-SUFFIX (with fix G2), Lemma STEP-BOUND: SIGN (both runs)
- SAME-SUFFIX, re-derived. I close two steps the proof leaves implicit:
  - (i) Λ_t(y) is constant on W. o's play is o · P_f* · P_t(y) with f* := o's successor at t. o is not on P_t(y): its successor f* would
    then be on P_t(y) ∩ P_f*, against avoidance. o is not on P_f*: the play from f* would then return to o and close before y. So
    Λ_t(o) = Λ_t(y), and W lies inside one Λ-interval of o.
  - (ii) The Odd half for o = K2. LOC-GATE3 / NO-TIE3 cover gates only. At K2, σ̄ is constant anyway by LOC-K2-3 (R123 LOC-K2 on
    IDEAL-CYC). That premise is missing from §3.5's row. Line: R-2 (premise lists).
- The comparison:
  - Equal Λ.
  - The Π-difference is (P_f Δ P_f′) ∩ above-Λ, constant on W, since P_t(y) is common and disjoint from both prefixes.
  - When it is empty, the lengths differ by |P_f| − |P_f′|, which is constant, and the direction is fixed by Λ's parity, which is
    constant.
- Even half (fix G2): the set B of ▷-best options is the same for every t − 1 ∈ W. Howard puts σ_t(o) in B at W's second step, and the
  tie rule keeps it.
  - On Γ3 the tie rule is already in CHAIN's definition of HOW3 (§2: «keeps σ_t(x) if it is such a successor»). G2's [N5XI] / A(x)
    route is a second derivation, not needed.
- STEP-BOUND: a value is a function of the play, and the play changes only where a successor on it changes.

### 2.6 §3.6 Lemma PARALLEL: SIGN (both runs)
- (i) x is the top of H_(s−1) Δ H_s. Since U_y is an up-set, x is also the top of E_(s−1)(b) Δ E_s(b): if that top were outside U_y, the
  H's would agree. E-MON3: x enters. By the definition of E, x is on P_s(b) and not on P_(s−1)(b). The expelled letters z go the other
  way.
- (ii) x is the top of a difference that contains z.
- (iii) The two plays agree up to and including u′ (positional strategies). u′ exists because the plays differ.
- Remark (optional, N-1): the proof never uses y ≻ w. With y := w (H = E(b)) it holds verbatim. EXPEL-COUNT needs it for letters z with
  no vertex strictly between w and z.

### 2.7 §3.7 Lemma PAIR-EXPEL, Corollary EXPEL-COUNT: SIGN, CONDITIONAL on R125 only (on Γ3; on IDEAL-CYC on landed premises)
- Λ: b′ follows u′ on P_s(b) and on P_s′(b), so Λ(b′) = w at s and s′. F1 and F2 (no return) give Λ(b′) = w on [s, s′]. The same holds
  for a′ at s′ − 1.
- Step 1.
  - Mover: s′ ≥ s + 2, since σ_(s′−1)(u′) = a′ ≠ b′ = σ_s(u′). Let s″ be the first departure. Then:
    Ω_(s′−1)(u′) ⊵ Ω_s″(u′) (F1) ▷ Ω_(s″−1)(u′) (STRICT) = ext(u′, Ω_(s″−1)(b′)) (CHAIN's F3 with F6: u′ is not its own node)
    ⊵ ext(u′, Ω_s(b′)) (F1, F4′, CN2-3), and Ω_(s′−1)(u′) = ext(u′, Ω_(s′−1)(a′)) (F3). F4′'s contrapositive with totality gives the claim.
  - Gate: LOC-GATE3 / NO-TIE3 at s, then F1 on a′.
  - This is self-contained: it is the same chain as SPLIT §3 (a), written out here. PAIR-EXPEL therefore needs no P-N5-SPLIT statement
    (G-4). Its label can be PROVED, CONDITIONAL on R125 (P-N5-CHAIN) on Γ3. On IDEAL-CYC it rests on R118 (b) F1, F3, F4′ and (c) STRICT,
    R123 CN2, LOC-GATE, NO-TIE (R-4, R-5).
- Step 2: the top d of the Π-difference decides Step 1.
  - If d ≻ z: d is an e-vertex by (E-DOM) and (Core) at the non-core vertices a′, b′ (G-1), c_W being in no Π. It is even, so it lies on
    a′'s side, and it is the top of the E-difference: strict on U_z.
  - If d ≼ z, or the Π's are equal: equal on U_z.
- Step 3: E_(s′−1)(b) = A ⊔ E_(s′−1)(a′) and E_s′(b) = A ⊔ E_s′(b′), with A the e-letters above w on the common prefix up to u′. I
  closed the cycle case.
  - If a′'s (or b′'s) play re-enters the prefix, every re-entered vertex is on the cycle, hence not above w. So the decomposition still
    holds, with the prefix's above-w letters all on the path part.
  - The change of E(b) at s′ has top x′ ≻ z (PARALLEL (ii)), on b′'s side, and A cancels: strict on U_z.
- EXPEL-COUNT. Every run of z on J except the last ends with an expulsion. Through one pair the U_z-values strictly rise (PAIR-EXPEL)
  and lie in one Λ-interval J_b′ of b′ (Λ(b′) = w at each, F2), so there are at most Dhi_z(b′, J_b′) of them.
  - (G-6) The pair count «≤ 3M; L-RED R228 §2» cites an L-RED lane report as its proof; L-2 says «no L-RED lane lemma is a premise».
  - Closed here, my proof: u′ is the first vertex whose successor differs. Non-mover Even vertices are frozen (F6; R118 (a)), and σ̄(K2)
    is fixed (LOC-K2-3 / R123 LOC-K2). So u′ is a mover or a gate, and b′ is one of its out-edges: M mover edges (to m-pads on Γ3, to
    gates on Γ) plus 2M gate faces. This is SPLIT-COUNT's own count, re-derived without SPLIT. Line: R-8.

### 2.8 §3.8 Corollary A*-EQUIV: SIGN, CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT, C-EQUIV) and R125; Γ3 (HOW3) only
- (i) The packet: «L-NEW, N5-CORE-forms §3 (5): cited, not re-proved here». That is an unrefereed lane file as the proof of a statement
  to be signed (G-7). I prove (i), referee-originated:
  - C ≤ A*_all. Take b := v and J := I. Each change of E(v) with top y makes y ENTER (E-MON3), which starts a new maximal run of y.
    Distinct changes start distinct runs, so c_y(v, I) ≤ a_y(v, I).
  - A*_all ≤ 1 + M·C. Every run of z on J, except one that is present at J's first state, starts at a change of E(b) inside J. The
    changes inside J number Σ_y c_y(b, J) ≤ M·C, one top each.
- (ii) Re-derived as in the packet: Dhi_y(b, J) − 1 = #changes of H on J (H strictly lex-rises, E-MON3). Each change is an entry of its
  top x into H, which starts a run of x, so this is ≤ Σ_(x∈U_y) a_x(b, J) ≤ M·A*_route. SPLIT-COUNT sums at most 3M such terms.
- (iii) With P-N5-SPLIT's C-EQUIV (not P-N5-CHAIN's: G-3). The A*_route direction uses A*_route ≤ A*_all ≤ 1 + M·max(1, T3).
- Scope: SPLIT-COUNT and C-EQUIV are Γ3 statements, so (ii) and (iii) are about HOW3 only. The line must not read them as IDEAL-CYC
  statements (R-5). My replay measures (i) and (ii) on IDEAL-CYC too, as DATA.

## Box 3: scope, DATA rule on L-2, TARGET.md diff, line requirements

### 3.1 Γ3 vs IDEAL-CYC: which statement holds on which run (my reading after 1.2-2.8)
| statement | Γ3 (HOW3 = N5′-xi from S3 to the first fallback) | IDEAL-CYC(G) |
| --- | --- | --- |
| GATE-RACE, TRIGGER, GATE-LOW-NULL (a)(b)(b′), NP-SHAPE, E-FACE-PAYS (a)(b)(d), SAME-SUFFIX, STEP-BOUND, PARALLEL | CONDITIONAL on R125 | landed R104 / R118 / R121 / R123 |
| E-FACE-PAYS (c), WAIT-QUIET | CONDITIONAL on R125, with the proviso at every state (R-7); the proviso itself also holds by B-ONLY3 (G-5) | no proviso (PROVISO, R123 B-ONLY) |
| K10 empty (fixes G1) | true by B-ONLY3, CONDITIONAL on R125 (G-5); the packet leaves it open | R123 B-ONLY |
| PAIR-EXPEL, EXPEL-COUNT | CONDITIONAL on R125 only (G-4, G-6 closed) | landed premises |
| A*-EQUIV (i)-(iii) | CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT, C-EQUIV) and R125 | not claimed: SPLIT-COUNT is a Γ3 statement |
- The two runs differ at K2. σ̄(K2) is r on Γ3 (LOC-K2-3) and K1 on Γ (R123 LOC-K2). They also differ at exact VJ ties (R118's DATA).
  No GATE statement compares the two runs, so this does not matter.

### 3.2 TARGET.md diff
- No statement is about winning regions or about any algorithm's running time.
- Every statement is about ONE run's counts (flips, value changes, runs of a letter, e-set changes), bounded by other counts of the same
  run. None is polynomial, nothing is claimed for N5 or for general games, and nothing concerns iterations after the first fallback.
- A*-EQUIV (iii) is an equivalence, «T3 polynomial ⟺ C ⟺ A*_all ⟺ A*_route polynomial», not a bound.
- L-2's tail paraphrases TARGET.md §2 and §4 correctly («deterministic», «polynomial on every parity game», §4's restricted class,
  unproved conjecture and empirical observation). It differs in wording from the landed R123 / R124 tail; using the landed form is
  optional (N-2).
- No big-number arithmetic enters (TARGET.md §3 is not engaged).
- Not M3, not M4, not a gauntlet step; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).

### 3.3 DATA rule on L-2 (to be re-read on L-3)
- (D-1) Firing controls. L-2 names five controls (gr, low, swap, a0, uz). It does not say which of the other must-0 counters have NO
  control: grwhy, trfail, lowflip, npside, npsub, npboth, npkind, unlfail, dfail, k1both, par1-3, lexfail, pxfail, dhifail, ecfail, pelam,
  cfail. The DATA rule requires this to be said. At the byte test I will read the lane's tools (box91-94, box96) for the units and the
  controls.
- (D-2) SAME-SUFFIX's DATA, «copy rows S(R_j) = S(R_(j−1)) on every level and 0 flips at the copied gates», is a record of box 94's
  nesting families, not a test of the lemma's statement on windows. It must be named as such. My replay tests the statement directly
  (ssfail, ssofail, ssefail; 2.9).
- (D-3) «dfail (a proxy for E-FACE-PAYS (b))»: correctly labelled; keep.
- (D-4) L-RED's dexact / dpass on 29 instances and the 2000-iteration climb are cited replays of another lane (own engine only). L-2
  cites them as such; keep.
- (D-5) «rows identical» across the two engines is a claim about the lane's two engines. Mine (2.9) agree on the records too; this is
  noted, not required.
- (D-6) «growth: … linear in n on every family measured»: DATA about families, not a bound. Keep «large zero counts are DATA, not
  evidence» or an equivalent sentence.

### 3.4 For the line (L-3; exact strings)
- R-1 (REQUIRED, G-1).
  - The line must not contain «K0, K3 lie on both of two plays with the same Λ or on neither», nor any global form of it.
  - If it names (Core): «(Core) in its W-1-repaired reading, applied only to non-core vertices (the faces of a gate and the successors of a
    mover or a gate; P-N5-CHAIN fixes entry 3, R-W)».
  - Credit, if given: «referee-originated: REFEREE-2 R2-P-N5-GATE G-1».
- R-2 (REQUIRED, G-2; premise lists).
  - No gloss of F3 as the definition of E. Where E's definition is meant, say «the definition of E_t(v)».
  - F3 in PAIR-EXPEL's premises; CYC in TRIGGER's; LOC-K2-3 (on IDEAL-CYC R123 LOC-K2) in SAME-SUFFIX's.
  - F6 not glossed as «an e-vertex has exactly one successor» unless paired with [DEF].
- R-3 (REQUIRED, G-3). C-EQUIV is cited only as P-N5-SPLIT's (Corollary C-EQUIV), never «P-N5-CHAIN's C-EQUIV».
- R-4 (REQUIRED, G-4).
  - No «P-N5-SPLIT §2 (a)».
  - Either PAIR-EXPEL and EXPEL-COUNT are PROVED, CONDITIONAL on RESULTS R125 (P-N5-CHAIN) only (Step 1 is self-contained; recommended),
    or the citation is «P-N5-SPLIT §3 (a)».
- R-5 (REQUIRED, scope 3.1).
  - Each statement names its run as in 3.1. A*-EQUIV is on Γ3 (HOW3) only.
  - The IDEAL-CYC premises include R118 (b) F4′'s stated clause and (c) STRICT, for PAIR-EXPEL Step 1.
  - They include R123 LOC-K2, for SAME-SUFFIX at K2.
  - (E-DOM) and (Core) on Γ are «read off RESULTS R104's priorities and core edges» (non-core vertices).
- R-6 (REQUIRED, G-5).
  - No sentence saying that B-ONLY on Γ3 is not among P-N5-CHAIN's facts, or is not landed in R125.
  - Either K10 and the PROVISO on Γ3 are «not claimed here», or (recommended) they are stated on Γ3, CONDITIONAL on R125, by P-N5-CHAIN's
    Lemma B-ONLY3, with «referee-originated: REFEREE-2 R2-P-N5-GATE G-5».
- R-7 (REQUIRED). E-FACE-PAYS (c) and WAIT-QUIET state the proviso as «D's play avoids e_o at every state of the run».
- R-8 (REQUIRED, G-6 / G-7).
  - EXPEL-COUNT's «≤ 3M» rests on the mover / gate edge count (2.7), not on L-RED R228.
  - A*-EQUIV (i) rests on the two-line proof in 2.8, not on N5-CORE-forms.
  - Credit, if given: «referee-originated: REFEREE-2 R2-P-N5-GATE G-6, G-7».
- R-9 (REQUIRED if the line has DATA). (D-1), (D-2).
- R-10 (REQUIRED; REFEREE's SP-2 form for P-N5-SPLIT, applied here). F2, CYC, (E-DOM) and (Core) are not in R125's line (L-5,
  473344b1; checked by script). The line must cite them as P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7) and the rest as
  RESULTS R125 (P-N5-CHAIN).
- N-1 (optional): PARALLEL with y = w (2.6). N-2 (optional): the landed R123 / R124 TARGET tail.

### 3.5 R-1..R-10 as exact old → new strings against L-2 (Lead 00:06Z: R125 has landed, so B-ONLY3 etc. are RESULTS R125 facts)
- Script R2-P-N5-GATE/l3req.py, output l3req.out. Each Old occurs exactly once in L-2 (sha1 c0f2007d, asserted). Applying all of them
  gives the reference text l3req_applied.txt (sha1 1bd49ea1…, 11,146 B, 211 «(» = 211 «)»).
- None of these occurs in the applied text: «§2 (a)», «P-N5-CHAIN's C-EQUIV», «lie on both of two plays», «not a premise here», «not
  among P-N5-CHAIN», «while its play avoids», «over the run then», «L-RED R228».
- L-3 need not equal the reference byte for byte. At the byte test I check each New's meaning, each Old's absence, and nothing else
  changed beyond fixes entry 3.
- R-1 / R-10 (G-1; SP-2 form).
  - Old: «on Γ3 instead the facts F1, F2, F3, F4′, F6, STRICT, CYC, CN2-3, LOC-GATE3, NO-TIE3, (E-DOM), (Core), E-MON3 of the pending
    packet P-N5-CHAIN (L-NEW, frozen claude/l-new 93531b03, landing as R125); for PAIR-EXPEL, EXPEL-COUNT and A*-EQUIV also §2 (a),
    SPLIT-COUNT and C-EQUIV of the pending packet P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, referees pending)»
  - New: «on Γ3 instead RESULTS R125 (P-N5-CHAIN): F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, and F2,
    CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4), (Core) in its W-1-repaired reading,
    applied only to non-core vertices (the faces of a gate and the successors of a mover or a gate; P-N5-CHAIN fixes entry 3, R-W;
    referee-originated: REFEREE-2 R2-P-N5-GATE G-1); for A*-EQUIV also SPLIT-COUNT and C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new
    399cda07, sha1 5bc1b1f3)»
  - If P-N5-SPLIT lands before L-3, its R-id replaces «P-N5-SPLIT (…)». The same applies to R125's line names: every R125 name above
    occurs in L-5 (473344b1); F2, CYC, (E-DOM), (Core) do not.
- R-5a: «(b) F1, F2, F3, (e) in its per-vertex form» → «(b) F1, F2, F3 and F4′'s stated clause, (c) STRICT, (e) in its per-vertex form».
- R-5b: «RESULTS R123 Lemmas CN2, LOC-GATE, B-ONLY» → «RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY».
- R-5c.
  - Old: «for IDEAL-CYC; on Γ3 instead»
  - New: «and (E-DOM), (Core) on Γ read off RESULTS R104's priorities and core edges (non-core vertices only), for IDEAL-CYC; on Γ3
    instead»
- R-4: «(Lemma PAIR-EXPEL, PROVED-CONDITIONAL on P-N5-SPLIT §2 (a))» → «(Lemma PAIR-EXPEL)».
  - The line's global «each statement PROVED» and R125 conditionality then cover it. The alternative «PROVED-CONDITIONAL on P-N5-SPLIT
    §3 (a)» is also acceptable.
- R-3 / R-5d.
  - Old: «(Corollary A*-EQUIV, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and P-N5-CHAIN's C-EQUIV)»
  - New: «(Corollary A*-EQUIV, on Γ3 only, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV)»
- R-8a.
  - Old: «C ≤ A*_all ≤ 1 + M·C and»
  - New: «C ≤ A*_all ≤ 1 + M·C (each entry of a top starts a run, and every run but one starts at a change; referee-originated: REFEREE-2
    R2-P-N5-GATE G-7) and»
- R-8b.
  - Old: «is at most 1 + 3M·max Dhi_z,»
  - New: «is at most 1 + 3M·max Dhi_z (at most 3M split pairs: the split is a mover or a gate, with M mover edges and 2M faces;
    referee-originated: REFEREE-2 R2-P-N5-GATE G-6),»
- R-7a: «so if D's play avoids e_o over the run then» → «so if D's play avoids e_o at every state of the run then».
- R-7b.
  - Old: «(Lemma WAIT-QUIET) a gate whose D changes value at most K times while its play avoids e_o unlocks»
  - New: «(Lemma WAIT-QUIET) a gate whose D's play avoids e_o at every state of the run and whose D changes value at most K times unlocks»
- R-6a.
  - Old: «while on Γ3 that case needs B-ONLY on Γ3, which is not a premise here (OPEN within this entry, covered by E-FACE-PAYS (a) only)»
  - New: «and on Γ3 it does not occur either, by RESULTS R125's B-ONLY3 (pβ_o is never an exception; pe_o is one only when D = c_W, and
    then Λ(pe_o) = c_W ≠ Λ(pβ_o); referee-originated: REFEREE-2 R2-P-N5-GATE G-5)»
- R-6b.
  - Old: «while on Γ3 the proviso is a hypothesis here»
  - New: «and on Γ3 it holds at every state by RESULTS R125's B-ONLY3 at the mover D, by the same argument (referee-originated: REFEREE-2
    R2-P-N5-GATE G-5)»
  - The weaker option of R-6, «not claimed here» on Γ3, stays acceptable. What is not acceptable is any reason saying B-ONLY3 is absent
    from P-N5-CHAIN / R125.
- R-9 (DATA).
  - Old: «SAME-SUFFIX: copy rows» → New: «SAME-SUFFIX (a record of box 94's nesting families, not a test of the lemma's statement): copy
    rows».
  - Plus (D-1), content only: the DATA clause must name the must-0 counters that have no firing control. The list comes from the lane's
    tools, which I read at the byte test.
- R-2 is a packet-text item (premise rows of §3.1, §3.5, §3.7 and the F3 / F6 glosses), for fixes entry 3. L-2 carries no per-lemma
  premise rows, and it defines E_t(v) explicitly, so R-2 asks nothing of the line beyond R-1 / R-10.

## Box 4: own replay, controls, DEAD list, verdicts

### 2.9 Replay (R2-P-N5-GATE/r2gate.py; own engines; units in the tool's doc string)
- Engines.
  - g3 = Γ3, N5′-xi from S3 to the first fallback (R2-P-N5-SPLIT/r2split.howrun on R2-P-N5-END/r2end.py).
  - cyc = IDEAL-CYC on Γ, Howard with the keep rule (R2-P-ACYC/r2acyc.py).
  - E-priorities: 'lev' on g3 (L-NEW's choice) and the r2acyc default on cyc. Every counter is checked on both.
- Every statement of §3.1-§3.8 has a must-0 counter. The premises LOC-GATE(3) / NO-TIE(3) (locfail), E-MON(3) (emonfail) and CYC
  (cycfail) are checked too.
- Sets and results. Every must-0 counter is 0 on every row, and dpass = 0 and rec_k10 = 0 on both engines:
  - pinned: the lane's frozen instances with N ≤ 170, 41 genomes (box 91, 93, 94, 95 fix1 inst/, copied from 9c0349b1), × 2 engines.
    - Coverage on g3: 8,978 gates, 1,685 states, 20,769 (state, gate) pairs for GATE-LOW-NULL (a), 390 flips for (b) and 378 for (b′).
    - Also on g3: 3,305 NP steps, 405,231 E-FACE-PAYS (b) steps, 269,244 SAME-SUFFIX windows (83,787 Even 3-windows), 89,645 PARALLEL
      changes, 51,164 same-pair expulsion couples, 43,706 EXPEL-COUNT tuples. Output: pinned_p1.out.
  - random: 900 genomes of R2-P-N5-END's generator (any / self / acyc, 300 each), × 2 engines. Output: rand.out.
    - These are small (T ≤ 7, C = 1) and test little beyond (a)-type statements. I say so rather than count them as strong evidence.
  - mutants: 440 own mutants (r2split.mutate; 40 each of C6G8_n54, MW8_2, FW8_2, MWR8_2, Ku_8, DHIB18_2805, DWT20_2803, RWX_n95,
    NDV2_4, k1fail_202, WC16_2), × 2 engines. Output: mut.out.
    - Coverage on g3: 11,140 states, 10,434 GATE-LOW-NULL (b) flips, 24,068 NP steps, 1,557,316 SAME-SUFFIX windows, 118,896 same-pair
      expulsion couples.
- NOT RUN: the 16 pinned genomes with N > 170 (MW32_2, FW16_2, LT4/LT5, NSQ2/NSQ3, ND3_8, NDb/NDbr/NP/NV 3_8 and 2_8): the Γ3 engine's
  SPEC S1 dominates the cost. Their DEAD records (MW32_2 C = 65; FW16_2) are cited from the lane, not re-run by me.
- Controls (ctrl.out; MW8_2, C6G8_n54, MWR8_2; each fires on both engines):

| control | fires (g3 / cyc) |
| --- | --- |
| gr (GATE-RACE (a) on the entered face) | grfail 101 / 101 |
| low (π := letters below e_o) | decfail 1,191 / 1,191 |
| np (faces swapped) | npfail 219 / 219 |
| efb (p_e against p_b instead of D) | efbfail 1,746 / 1,746 |
| ss (windows that fail the hypotheses) | ssfail 600, ssofail 140 / same |
| sb (only x's own successor) | sbfail 8,080 / 4,387 |
| par ((iii) as «at least 3 after u′») | parfail 1,265 / 926 |
| uz (U_z := ∅) | pefail = pe3fail 2,184 / 1,233 |
| ec (EXPEL-COUNT without its 1 +) | ecfail 20 / 11 |
| c (c_y ≤ a_y − 1) | cfail 4,381 / 2,494 |
| a2 ((ii)'s bound − 1) | a2fail 244 / 244 |

- Control history.
  - The first par control («after the play's first vertex») and the first sb control («movers only») could not fire. The second par
    control («at least 2 after u′») fired on cyc but not on g3, where a pad follows every split. I replaced each, as listed above, before
    the recorded run. ctrl.out holds the recorded runs, including the «at least 2» run, whose g3 line shows no parfail.
  - No ctrl was used on a recorded zero run.
- Records (equal on the two engines, instance by instance; pinned_p1.out): MW8_2 T 55, C 17, A*_all 18, max flips 34 = 4n + 2;
  C6G8_n54 C 6; FW8_2 C 3; WC4_2 and WC16_2 T 4.

### 2.10 DEAD list (§5; not to sign; witnesses re-run where my engines reach them)
- WC «waiting High»: T3 = 4 on WC4_2 and WC16_2 (both engines). Re-run.
- RA-MULT: MW8_2 C = 17 = 2n + 1. Re-run. MW32_2 (65) not re-run (size).
- Polynomial P bound: C = 3 on FW8_2. Re-run. The RA path count P = F_(d+2) − 1 and FW16_2 are not re-run.
- K6 LAG TOWER (LT*): not re-run (size; N ≥ 225).
- K7 probe: C = 2 on Ku_4, Ku_8, Ku_16, Kprev_8. Re-run.
- K1-FLIP(c): MWR4/8/16_2 max flips 9 / 17 / 33 = 2n + 1, with lamch 0 at that gate, on both engines. Re-run (mwr_lamch.out).
- Nesting multipliers and Db / Dbr: every NP/NV/ND/NDV/NDB/NDb/NDbr instance with n = 4 or 8 that I ran has exactly one MW(n)'s C, max
  flips and T3 (n = 4: 9 / 18 / 31; n = 8: 17 / 34 / 55). This is the «simultaneous» case. NSQ (the «sum» case) and the 3_8 sizes are
  not re-run.

### 2.11 Verdicts (Opus 5.5, D1). Γ3 rows CONDITIONAL on RESULTS R125 (landed per the Lead, 00:06Z). Statements as in the packet with fixes 1-2.
| statement | verdict | conditions, gaps closed here |
| --- | --- | --- |
| GATE-RACE (a), (b); TRIGGER | SIGN | both runs; CYC added to TRIGGER's premises (R-2) |
| GATE-LOW-NULL (a), (b), (b′) | SIGN | both runs; (Core) at the faces only (G-1, R-1); IDEAL-CYC (E-DOM) / (Core) from R104 (R-5) |
| NP-SHAPE (a), (b) | SIGN | both runs; the «no re-entry into A_t» step closed (1.4) |
| E-FACE-PAYS (a)-(d); WAIT-QUIET | SIGN | both runs; proviso «at every state of the run» (R-7); PROVISO also on Γ3 by B-ONLY3 (G-5) |
| K10 empty / PROVISO (fixes 1-2) | SIGN on IDEAL-CYC (R123 B-ONLY); on Γ3 SIGN as my G-5 extension, CONDITIONAL on R125 | the reason «not among P-N5-CHAIN's facts» is false (G-5, R-6) |
| SAME-SUFFIX (with G2); STEP-BOUND | SIGN | both runs; Λ(y) constancy and o = K2 closed (2.5); LOC-K2-3 added (R-2) |
| PARALLEL | SIGN | both runs |
| PAIR-EXPEL; EXPEL-COUNT | SIGN | both runs; needs no P-N5-SPLIT statement (G-4, R-4); 3M count by my proof (G-6, R-8); F3 added (R-2) |
| A*-EQUIV (i)-(iii) | SIGN, CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT, C-EQUIV) and R125; Γ3 only | (i) by my proof (G-7, R-8); C-EQUIV is P-N5-SPLIT's (G-3, R-3) |
| DEAD list | SIGN (dead) as far as re-run (2.10) | the rest cited, not re-run |

- No statement is REFUSED. No signed proof keeps an open gap.
- G-1 to G-7 are text and citation defects; each is closed here and turned into a line requirement (3.4, 3.5).
- R-2 is for fixes entry 3 (the packet's premise rows and glosses).
- The line verdict waits for L-3 (Lead: L-SI 50 writes one fixes entry 3 + L-3 answering both referees).
- Not M3, not M4, not a step-4 pass; nothing bounds T3, T_CYC, C or A*_all by a polynomial. G-N5-TIME stays OPEN; N5′-xi stays a
  CANDIDATE (D1).

### Statement of independence
- These verdicts rest on my derivations above and on my own engines. Before this verdict I did not open docs/referee/R-P-N5-GATE.md
  (REFEREE 31), notes/REFEREE.md, or L-RED's R228 / R229 reports and tools.
- The Lead's 00:06Z message told me that my G-5 is «the same point as REFEREE 31's GT-1». I found G-5 before that message: it is in my
  00:04Z message and in box 1 (a28bc5e1).
- I read the lane's L-2, fixes 1-2, and the frozen packets P-N5-CHAIN and P-N5-SPLIT. I did not read the lane's tools (gate92 / mult91
  / np93 / lev94 / astar92 / d96); I read them only at the L-3 byte test, for (D-1).

## Addendum 1 (written after my verdict c035b35f was on origin): REFEREE 31's R-P-N5-GATE.md (claude/referee a401ce0e)
- Verdicts: equal on every row. Both referees SIGN every statement, none REFUSED, no GAP.
  - Γ3 rows CONDITIONAL on R125.
  - A*-EQUIV (ii), (iii) on Γ3 only, CONDITIONAL also on P-N5-SPLIT.
  - K10-empty and the PROVISO hold on Γ3 by B-ONLY3 (REFEREE: «TRUE»; mine: SIGN as the G-5 extension).
- Findings, found independently on both sides:

| REFEREE | mine |
| --- | --- |
| GT-1 | G-5 |
| GT-2 | G-4 |
| GT-3 | G-3 |
| GT-4 | G-7 |
| GT-5 | G-6 |
| GT-6 | R-5 |
| GT-7 | G-1 |
| GT-8 | G-2 |
| GT-9 | 3.1 scope / R-3, R-5d |

- One refinement I ADOPT. REFEREE signs A*-EQUIV (i) on BOTH runs. That is right: (i) uses only E-MON (R121 on IDEAL-CYC), and my cyc
  replay has a1fail = 0. My row «A*-EQUIV (i)-(iii) … Γ3 only» is corrected: (i) holds on both runs, (ii) and (iii) on Γ3 only.
  - For the line, REFEREE's R-3 New («C ≤ A*_all ≤ 1 + M·C (on both runs) and, on Γ3 only, C ≤ 3M·(1 + M·A*_route)») is preferred.
  - Mine («on Γ3 only» for the whole corollary) is true but weaker; either is accepted.
- DATA rule. REFEREE read the lane's tools; I had not before my verdict. I checked two of REFEREE's items in the lane code at 9c0349b1:
  - D-2 confirmed. gate92.py l. 34: «c["decfail"] += (not d) or rk[max(d, …)] < r0», i.e. it fires only if the top of E(p_e) Δ E(p_b) is
    less relevant than e_o. That is impossible under PRIV, so decfail does not test (a)'s order equivalence. My replay counts (a)
    directly (decfail, with control low firing 1,191 on each engine).
  - D-4 confirmed. box94/out/lev94_own.out gives NSQ2_4 rows R 18, 22 and NSQ3_4 rows R 18, 22, 26. So «copy rows … on every level …
    box 94's 22 instances» is false as worded for NSQ.
  - D-1, D-3, D-5 I adopt as REQUIRED on REFEREE's reading. I re-read those tools at the L-3 byte test.
  - Together they replace and sharpen my (D-1) and (D-2) of 3.3. My R-9 «SAME-SUFFIX (a record …)» is superseded by REFEREE's D-4 New,
    which says more and is true.
- Line strings: REFEREE's R-1..R-7, D-1..D-5 and mine are compatible. Where both touch the same Old, the combination I accept at the byte
  test is:
  - PAIR-EXPEL: REFEREE's R-1 (keep the SPLIT condition, cite §3 (a)) and my R-4 (drop it) are both acceptable. The line must not keep
    «§2 (a)».
  - Premises on Γ3: since R125 has landed (Lead 00:06Z), my R-1 / R-10 (R125 names, plus F2, CYC, (E-DOM), (Core) as CHAIN frozen
    text, (Core) repaired, B-ONLY3 included) supersede REFEREE's R-7 and G-c, which were written while R125 was pending. REFEREE's R-7
    content, the W-1-repaired (Core), is contained in mine.
  - IDEAL-CYC premises: REFEREE's R-4 adds F4′, F6, (c) STRICT; my R-5a adds F4′ and (c) STRICT. Either is accepted; F6 on Γ is R104's
    definition («one edge to the W-target or to … c_W»).
  - REFEREE's R-5 = my R-5b. REFEREE's R-6 and my R-5c say the same.
  - Γ3 K10 / PROVISO: REFEREE's G-a / G-b (RECOMMENDED) and my R-6a / R-6b say the same. With R125 landed, «pending R125» becomes
    «RESULTS R125».
  - REFEREE signs L-2's present Γ3 words as TRUE if G-a..G-c are not taken. I agree they are true. My R-6 requires only that no
    sentence give the false reason, and L-2 gives none. So R-6 is met by either choice.
  - My R-7 (the proviso «at every state of the run») is required only if L-3 keeps the Γ3 proviso as a hypothesis. If L-3 takes G-b /
    R-6b, the proviso holds on both runs and R-7 becomes optional. REFEREE reads WAIT-QUIET the same way («over a run in which D's play
    avoids e_o»).
  - My R-8 (credit strings for the 3M count and (i)) is optional where REFEREE marks GT-4 / GT-5 «nothing to change in the line». I keep
    it REQUIRED only to the extent that L-3 states any reason for the 3M bound or for (i): that reason must be the elementary one, not
    L-RED R228 or N5-CORE-forms.
- Replays: independent and all-zero on both sides.
  - REFEREE: 19 instances (box 91's 11, box 93's 8) on both engines, plus the box 94 / box 95 levels on cyc.
  - Mine: 41 pinned, 900 random and 440 mutants on both engines, with 11 controls.
  - Records agree: MW(n) C = 2n + 1 and flips 4n + 2; MWR flips 2n + 1 with lamch 0; Ku C = 2.
- Result: P-N5-GATE has two referee signatures on every statement, with the conditions above. The line needs one fixes entry 3 + L-3 that
  meets both referees' REQUIRED items, as combined here.

## Addendum 2 (REFEREE-2 successor 37; 2026-11-12 by date -u): byte test of fixes entry 3 + line L-3 (claude/l-si ef14451f)
- Object (re-hashed from `git show ef14451f:…`):
  - L-3: docs/si/P-N5-GATE-line-L3.txt, sha1 b60495b2c607e8e6c1e145e40478717fa6ed15f4, 12,353 B. One line, no «|», 229 «(» = 229 «)».
  - Fixes: docs/si/P-N5-GATE-fixes.md, sha1 e79455ea, 24,889 B. The diff 9c0349b1..ef14451f removes no line: entry 3 is appended.
  - The packet (sha1 f3a584e6) and L-2 (sha1 c0f2007d) are unchanged.
- Check: R2-P-N5-GATE/bt_l3.py (my code; mkL3.py not imported), output bt_l3.out: 39 PASS, «FAILS 0».
  - Every banned string is absent: «§2 (a)», «P-N5-CHAIN's C-EQUIV», «lie on both of two plays», «not a premise here», «not among
    P-N5-CHAIN», «while its play avoids», «over the run then», «CTRL=a0», «is a hypothesis here», «L-RED R228», «afail», «pxfail», «box
    94's 22 instances».
  - Every required New of Addendum 1's combined list occurs exactly once.
- All 46 changed regions read. A word-level diff of L-2 → L-3 gives 46 regions, and I read each one. Every region is one of: my R-1 /
  R-10, R-4, R-5a-c, R-6a/b, R-7a/b, R-8a/b; REFEREE's R-1, R-3..R-6, D-1..D-5, G-a/G-b; or the source note «fixes entries 1-3». There
  is no other change.
- Meaning, read in full on the merged clauses:
  - Γ3 premises.
    - Every name in the R125 list occurs in R125's line L-5 (my earlier script).
    - F2, CYC, (E-DOM) and (Core) are cited from CHAIN's frozen text, with (Core) restricted to non-core vertices.
    - R125 is on trunk: 0753fd71 is an ancestor of origin/claude/vibrant-johnson-nxvvxo 4c2f407d, and RESULTS has one «### R125
      [refereed-only]».
  - IDEAL-CYC premises: F4′, F6, (c) STRICT, LOC-K2. (E-DOM) and (Core) are read off R104 «with LOC-K2». The clause «K0, K3 lie on the play
    iff Λ is a core vertex» is right for non-core starts: the core is entered only at K0, then K3, K2 → K1 (LOC-K2), and K1's loop.
  - PAIR-EXPEL: «no P-N5-SPLIT premise is used», and «§3 (a), Lemma REWIN (a)» is named as the argument written out. This is my R-4 and
    REFEREE's R-1 merged.
  - A*-EQUIV.
    - (i) holds «on both runs, with no P-N5-SPLIT premise» and carries the G-7 proof sentence. (ii) is «on Γ3 only».
    - The corollary's label is «PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV» (REFEREE's R-3 New, which I accepted). With
      the explicit «(on both runs, with no P-N5-SPLIT premise …)» for (i), it says what both referees signed.
  - K10 and the PROVISO hold on Γ3 by RESULTS R125's B-ONLY3, with the pad argument (pβ_o never an exception; pe_o only when D = c_W), and
    are credited to GT-1 / G-5. This matches 1.3 and 1.5 above. The false reason is gone, and entry 3 F3-1 RETRACTS entry 1's G1
    sentences in so many words.
  - WAIT-QUIET / E-FACE-PAYS (c) carry «at every state of the run» (R-7, now optional since the proviso holds on both runs; it is still
    true).
  - EXPEL-COUNT carries the 3M reason (G-6).
- DATA rule: I re-read the lane's tools at ef14451f for the adopted D-1, D-3, D-5. D-2 and D-4 were done in Addendum 1.
  - D-1 holds: box91/mult91.py l. 97-110 loops over `odd2` (Odd vertices with two successors) for grfail / gr2fail; `why` and trfail
    increment per flip.
  - D-3 holds: box93/np93.py l. 50-60 counts npside / npsub per (gate, state) and npboth / npkind per flip; l. 68 has «unlfail += unl > 1
    + A», A = ch_(p_e).
  - D-5 holds: mult91 l. 126 counts par1-3 only `if Z:`. par3 tests the expelled z on the prefix, not x's position. afail / pxfail are
    EXP-PATHS counters (l. 16-17).
  - L-3's new DATA claim «L-SI's set re-measure copy95.py agrees on both engines» checks out. box95/fix3/copy95.py l. 39 compares sets
    (`sr == prev`). out/copy95_own.out and copy95_g3.out have copy 1 on the 20 instances and copy 0 on NSQ2_4 / NSQ3_4 (R 18, 22, 26),
    with the rows identical across the two engines.
- TARGET.md: the tail is unchanged from L-2 (correct paraphrase of §2 / §4, 3.2 above). Nothing new is claimed. Not M3 / M4, not a step-4
  pass; G-N5-TIME stays OPEN.

### Verdict: L-3 (ef14451f, sha1 b60495b2) MATCHES. Every REQUIRED item of both referees, as combined in Addendum 1, is met in bytes and in meaning, and nothing else changed.
- With REFEREE 31's signatures, P-N5-GATE's statements stand two-referee signed as in L-3:
  - Γ3 rows CONDITIONAL on RESULTS R125 (landed);
  - A*-EQUIV (ii), (iii) CONDITIONAL also on P-N5-SPLIT and holding on Γ3 only;
  - A*-EQUIV (i) on both runs.
- I have not read REFEREE's own L-3 byte test, if one exists. A «signed by both» MATCH is unconditional only after checking it on
  claude/referee (my handover's second trap).

## Addendum 3 (REFEREE-2 successor 37; 2026-11-12 by date -u): byte test of fixes entry 4 + line L-4 (claude/l-si 676b6a1c)
- Object (re-hashed from `git show 676b6a1c:…`):
  - L-4: docs/si/P-N5-GATE-line-L4.txt, sha1 6bfde78ef050b47f43527875256c65a205869e77, 12,562 B. One line, no «|», 230 «(» = 230 «)».
  - Fixes: sha1 8009e018, 28,767 B. The diff ef14451f..676b6a1c removes no line: entry 4 is appended.
  - The packet (f3a584e6) and L-3 (b60495b2) are unchanged.
- Diff L-3 → L-4 (word level): exactly six regions, all named by entry 4.
  - LT-1, two strings:
    - «C-EQUIV of P-N5-SPLIT (L-NEW, frozen … 5bc1b1f3);» → «C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW, frozen … 5bc1b1f3; landing
      order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry);»
    - «PROVED-CONDITIONAL on P-N5-SPLIT's» → «PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s».
  - GL-1 and GL-2 delete RA-MULT, the polynomial RA-path bound and K1-FLIP(c) from the DEAD clause.
  - GL-3 inserts them as «DATA, not DEAD (asymptotic statements, finitely many instances; L43): …».
  - «fixes entries 1-3» → «1-4».
  - There is no other change.
- Banned strings of Addendum 2 are still absent. «RA-MULT», «K1-FLIP(c)», «a polynomial bound on the RA path count» and «pending packet»
  are absent too.
- Meaning.
  - LT-1.
    - R126 and R127 are NOT yet on trunk: at b3d7294c, RESULTS has «### R125» and no R126 / R127.
    - So «RESULTS R127 (P-N5-SPLIT; …)» is a forward reference. It is made under the Lead's landing-order ruling (02:57Z), which the line
      states in so many words.
    - A*-EQUIV (ii), (iii) keep their CONDITIONAL label, now on R127. That is correct as long as P-N5-SPLIT lands as R127 before this
      entry. CHECKER must confirm R127 = P-N5-SPLIT at this entry's landing (entry 4 F4-1 says so).
    - I accept this form. If the order changes, the R-id must be re-diffed.
  - GL-1..GL-3 (L43).
    - The three moved rows each refute an asymptotic statement on finitely many instances. Moving them to DATA with their numbers is right,
      and it is the same correction I made to my predecessor's QN §6 (R2-P-N5-QN Addendum 3).
    - The DATA numbers agree with my replay where I re-ran them. MWR4/8/16_2 have per-gate flips 9 / 17 / 33 at lamch 0 on both engines
      (mwr_lamch.out). MW8_2 has C = 17 = 2n + 1, and FW8_2 has C = 3 (pinned_p1.out). MW32_2's and FW16_2's numbers, and the RA path count
      P = F_(d+2) − 1, are cited, not re-run (2.10).
    - «refutes a constant multiplicity only below 32» is right: m = n reaches 32 on MW32_2. «refutes c·(lamch + 1) only for c ≤ 32» is
      right: 33 flips at lamch 0.
    - The construction rows (WC, K6, K7, nesting, Db / Dbr) stay DEAD. Each says a named construction fails to grow, which a finite
      instance can show. I agree.
- Verdict: L-4 (676b6a1c, sha1 6bfde78e) MATCHES. L-3's match carries over unchanged, and the two new items (LT-1 under the landing-order
  ruling, GT-10 / L43) are correct in bytes and in meaning.
  - Open condition, unchanged: P-N5-SPLIT must land as R127 before this entry. Until then the line's «RESULTS R127» is not yet true on
    trunk.
- I read REFEREE 31's §I / §J only as quoted in entry 4. I have not opened claude/referee fbc4d865 for this test.

## Addendum 4 (REFEREE-2 successor 37; 2026-11-12 by date -u): spot replay of two cited-only DATA numbers (Lead 05:37Z, optional)
- Instances, from l-si 9c0349b1 box91/inst, re-hashed: MW32_2 (sha1 445031d1, N 300, M 657) and FW16_2 (sha1 94df42b7, N 259, M 528).
- These were NOT RUN in 2.9 because of the Γ3 engine's cost.
- Run: the IDEAL-CYC engine only (r2gate.py --eng cyc), with every check and no size cap. Output: R2-P-N5-GATE/spot_mw32_fw16_cyc.out.
  The Γ3 engine is still not run on them.
- Results. Every must-0 counter is 0 on both, and dpass is 0.
  - MW32_2: T 199, C = 65 = 2n + 1 (n = 32), A*_all 66, max per-gate flips 130 = 4n + 2 with lamch 0. 90,092 SAME-SUFFIX windows and
    11,360 same-pair expulsion couples.
  - FW16_2: T 53, C = 3, A*_all 16. 24,386 SAME-SUFFIX windows.
- So two of L-4's numbers are now re-run on IDEAL-CYC by me: «C = 2n + 1 on MW8_2, MW32_2» and «C = 3 on FW8_2, FW16_2».
- Still cited, not re-run: the re-arm multiplicity m = n, the RA path count P = F_(d+2) − 1, and Γ3 on these two instances. No verdict
  changes.
