# P-N5-GATE fixes (the packet docs/si/P-N5-GATE.md stays frozen at 4066f579, sha1 f3a584e6…; every repair is here)

## Entry 1 (fix round 1; L-SI successor 50; Lead brief 2026-11-09)
Items: L-RED 63's packet-level read, docs/red/R229-box94.md Addendum A at claude/l-red 98143eab (byte copy and sha1 in
experiments/si/box95/fix1/): G1 (scope), G2 (premise), G3 (premise lists), G4 (naming), G5 (stale record), G6 (DATA line). All six are
taken. No PROVED statement changes; G1 narrows an open case to Γ3, G2 adds the tie rule that SAME-SUFFIX's Even half uses. Strings:
this text by experiments/si/box95/fix1/mkfix1.py (each Old asserted once in the frozen packet, wrapped lines joined by one space);
line L-1 (docs/si/P-N5-GATE-line-L1.txt) by fix1/mkL1.py, its premise quotes checked verbatim by fix1/quotesL1.py.

### G1 (scope, required): K10 «below» is EMPTY on IDEAL-CYC; on Γ3 it stays open
- Why (L-RED 63, R229-box92 Addendum A at claude/l-red 8c034440; R229-box94 Addendum A G1): on IDEAL-CYC, landed R123 Lemma B-ONLY says
  that Λ_t(v) is less relevant than every e-vertex for every v other than c_W and the e-vertices whose successor is c_W. A β-face is
  never such an exception, so Λ_t(p_b) ≠ c_W. If e_o's successor is c_W, Λ_t(p_e) = c_W ≠ Λ_t(p_b): no LAM step. Otherwise Λ_t(p_e) is
  less relevant than e_o: UP_t. So on IDEAL-CYC every LAM step is a UP step, K10 (LAM ∧ PRIV ∧ not UP) is empty, and GATE-LOW-NULL (b)
  covers every flip whose two sides are LAM ∧ PRIV steps. On Γ3 the same needs B-ONLY on Γ3, which is not among P-N5-CHAIN's facts
  (§1) and not landed: within this packet, K10 on Γ3 stays open (covered by §3.4 only).
- §3.2, scope bullet. Old: «- Scope (L-RED 63, R229-box92): the K3 / K4 / K9 consequences hold on LAM ∧ PRIV ∧ UP steps only; a flip at a LAM ∧ PRIV step with e_o not above Λ («below», row K10 of WAIT-CLOSED) is covered by no part of this lemma (but by §3.4).»
  New: «- Scope (L-RED 63, R229-box92 and its Addendum A): the K3 / K4 / K9 consequences hold on LAM ∧ PRIV ∧ UP steps only. A LAM ∧ PRIV
  step with e_o not above Λ («below», row K10 of WAIT-CLOSED) does not occur on IDEAL-CYC: by RESULTS R123 Lemma B-ONLY, LAM_t implies
  UP_t there (Λ_t(p_b) is a cycle node less relevant than every e-vertex, and Λ_t(p_e) = Λ_t(p_b)). On Γ3 that step needs B-ONLY on
  Γ3, which is not among this packet's premises; there a flip at a K10 step is covered by no part of this lemma (but by §3.4).»
- §3.4, after WAIT-QUIET's proof mark. Old: «(the classes K1-K10 of box 92's WAIT-CLOSED). ∎»
  New: «(the classes K1-K10 of box 92's WAIT-CLOSED; K10 is empty on IDEAL-CYC by RESULTS R123 B-ONLY, see §3.2's scope bullet, and
  open on Γ3 outside this lemma). ∎»
- §8, L-RED 63 R229-box92 row. Old: «scope corrected to LAM ∧ PRIV ∧ UP (§3.2); «below» named K10.»
  New: «scope corrected to LAM ∧ PRIV ∧ UP (§3.2); «below» named K10; Addendum A (claude/l-red 8c034440): K10 is empty on IDEAL-CYC
  by RESULTS R123 B-ONLY; on Γ3 it needs B-ONLY on Γ3 (not a premise here).»

### G2 (premise, required): [HOW]'s tie rule, which the Even half of SAME-SUFFIX uses
- Why: two options of an Even mover can have equal values (their first vertices are gates, in no Π by CN2). «σ_t(o) constant from W's
  second step» needs a rule that keeps a ▷-best current option. Both runs have one:
  - IDEAL-CYC: RESULTS R118's Howard step, quoted verbatim by fix1/quotesL1.py: «every mover x goes to a successor of ⊴-largest Ω_t
    value, and keeps σ_t(x) if σ_t(x) is such a successor» (as L-RED R221 own.py and R123's QUIET use it).
  - Γ3: N5′-xi's rule [N5XI] (RESULTS R118, box 190's S4a tie rule by Ξσ; P-N5-CHAIN §1: «σ_new(v) := the Ξσ-best element of TIE(v)
    := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}»), with SPEC S4a's «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}» (docs/new/N5-ssi-global.md) and S2's
    strict improving edges. The line that makes it constant: if σ_t(x) is ▷-best for the values at t, no edge at x is strictly
    improving, so A(x) = {σ_t(x)} and σ_(t+1)(x) = σ_t(x) whatever TIE's order (P-N5-CHAIN §3, REACH3-ALL's proof: «A(x) = {σ(x)}
    when nothing is strictly better»).
- §1, [HOW]. Old: «[HOW]: at each step every Even mover switches to a ▷-best option for the values of the previous step (Howard);»
  New: «[HOW]: at each step every Even mover switches to a ▷-best option for the values of the previous step (Howard), and keeps its
  current option when that option is ▷-best (tie rule: on IDEAL-CYC R118's «keeps σ_t(x) if σ_t(x) is such a successor»; on Γ3
  [N5XI] picks in A(x) = {σ(x)} ∪ Iσ(x), which is {σ(x)} when no successor is strictly better: P-N5-CHAIN §3);»
- §3.5, proof's last sentence. Old: «an Even mover switches at t to a ▷-best option for the values at t − 1 ([HOW]); both are constant. ∎»
  New: «an Even mover is at t on a ▷-best option for the values at t − 1 ([HOW]). The set B of ▷-best options is the same for every
  t − 1 ∈ W, so σ_t(o) ∈ B at W's second step, and at every later step of W the current option is still in B and is kept by [HOW]'s
  tie rule. Both are constant. ∎»
- The Odd half (unique ◁-least face, NO-TIE3) is unchanged.

### G3 (premise lists, required)
- Table, §3.3 row. Old: «| §3.3 | Lemma NP-SHAPE (a), (b) | PROVED | [Γ3] gate structure, [VJ], [OPT] |»
  New: «| §3.3 | Lemma NP-SHAPE (a), (b) | PROVED | [Γ3] gate structure, [VJ], [OPT], F3 |» (F3 gives E_t(p_e) ⊆ E_t(p_b)).
- §3.3 heading. Old: «### 3.3 Lemma NP-SHAPE (PROVED; [Γ3], [VJ], [OPT])»
  New: «### 3.3 Lemma NP-SHAPE (PROVED; [Γ3], [VJ], [OPT], F3)»
- Table, §3.4 row. Old: «| §3.4 | Corollary E-FACE-PAYS (a)-(d); Lemma WAIT-QUIET | PROVED | GATE-RACE (a); F6; CYC (for (c)); [VJ] |»
  New: «| §3.4 | Corollary E-FACE-PAYS (a)-(d); Lemma WAIT-QUIET | PROVED | GATE-RACE (a); F6; CYC and F2 (for (c)); [VJ] |» (F2: «≤ 2M + 2
  Λ-changes»).
- §3.4 heading. Old: «(PROVED; GATE-RACE (a), F6, [VJ]; (c) also CYC)»
  New: «(PROVED; GATE-RACE (a), F6, [VJ]; (c) also CYC, F2)»

### G4 (naming, required)
- §1, IDEAL-CYC reading. Old: «R118's monotonicity in place of LOC-GATE3, NO-TIE3, E-MON3, F1, F2 (no pads).»
  New: «RESULTS R118 (b) F1, F2 in place of LOC-GATE3, NO-TIE3, E-MON3, F1, F2 (no pads).» (R123's own naming.)

### G5 (stale record, required; the §5 row optional, taken)
- §8, last row. Old: «- SAME-SUFFIX (box 94): attack pending (routed to L-RED 63 at 06:33Z).»
  New: «- L-RED 63 R229-box94 (claude/l-red 6d2ace10): SAME-SUFFIX and STEP-BOUND SURVIVE; the echo at MW's race gate holds as the
  INCLUSION S(g_Q) ⊆ S(v) ∪ (S(v) + 1) on every level measured (DATA, 14 levels); the non-common-suffix nesting Db / Dbr (each High
  reads a different lower High; SAME-SUFFIX does not apply) is DEAD (DATA: the counters of one MW(n)). Packet-level read: R229-box94
  Addendum A (claude/l-red 98143eab): statements match; G1-G6 answered in fixes entry 1.»
- §5, new row (instances copied byte for byte from claude/l-red 6d2ace10 experiments/red/r229/inst/ into experiments/si/box95/fix1/inst/,
  sha1 in fix1/inst/SHA1SUMS, equal to L-RED's SHA1SUMS lines at 6d2ace10, checked by fix1/check_fix1.sh):
  «| non-common-suffix nesting Db / Dbr (L-RED 63, H = 2, 3) | C, max flips of one MW(n) | NDb2_4, NDb3_4, NDb2_8, NDb3_8, NDbr2_4,
  NDbr3_4, NDbr2_8, NDbr3_8 | 83f00267, 113e8b59, 48fbe8c2, ab097163, 6e9ea0df, 5233e0d1, b95993b9, e34134a3 | box95 fix1/inst (copies of claude/l-red 6d2ace10 r229/inst) |»

### G6 (DATA line, minor, taken)
- §6, §3.3-§3.4 counters. Old: «relfail, unlfail, dfail (proxy), k1both = k1c2»
  New: «relfail, unlfail, dfail (proxy), k1both = k1c2; and the EXACT form of (b): L-RED 63's dexact (D's play followed vertex by
  vertex; unit (gate, step) with D's play avoiding e_o at t − 1 and t: p_e's value changes iff D's does) = 0 and dpass (steps at which
  D's play passes e_o) = 0 on 29 instances (own engine, IDEAL-CYC, cap 3000; R229-box93 §2, claude/l-red fa4e50fe, e93_229.py)»

### Line L-1
- docs/si/P-N5-GATE-line-L1.txt: the proposed RESULTS-entry text with this entry applied; one paragraph, no «|»; model RESULTS R123.
  sha1 a44647db487dcd5193d11ff83f80006b3533dac4, 9541 bytes (wc -c). Premises: landed R-ids (R104, R117, R118, R121, R123) with quotes checked verbatim against trunk's
  docs/RESULTS.md by fix1/quotesL1.py; P-N5-CHAIN (R125) and P-N5-SPLIT named as PENDING packets.

## Entry 2 (fix round 2; L-SI successor 50; Lead ruling 2026-11-09 09:24Z (a): the IDEAL-CYC PROVISO only)
Item: the proviso «D's play avoids e_o» of §3.4 (b), (c) and WAIT-QUIET, on IDEAL-CYC. Γ3 is NOT changed here: B-ONLY on Γ3 (box 96's
Lemma B-ONLY3) goes to a separate packet P-N5-BONLY3 after L-RED 64's attack (ruling (b)). Strings: this text by
experiments/si/box95/fix2/mkfix2.py (quotes asserted verbatim once, in L-RED's text and in the frozen packet); L-2 by fix2/mkL2.py.

### F2-1 (PROVISO on IDEAL-CYC): cited, and derived independently
- Cited: L-RED 63, claude/l-red 2730ab90, docs/red/R229-box93.md Addendum B (byte copy experiments/si/box95/fix2/ref_R229-box93_2730ab90.md,
  sha1 in fix2/fix2.sha1): «**Lemma PROVISO (PROVED, L-RED lane; premises: landed R123 B-ONLY; [DEF]: e_o's only successor is its W-target D, or c_W).** On IDEAL-CYC(G), for every genome, every gate o and every state t, D's play does not pass e_o.»
- Independent derivation (L-SI box 96 §1, docs/si/box96-bonly3.md at claude/l-si 6ee19b24, written before L-RED's text was on origin;
  the same argument). D := e_o's successor (RESULTS R104: e has one edge, to the W-target or to c_W). If D = c_W, P_t(D) is c_W's
  loop. Otherwise D is a mover; if e_o ∈ P_t(D), the vertex after e_o is D, the play's first vertex, so the play closes there and its
  cycle is the whole play, which carries e_o; then Λ_t(D) is e_o or more relevant. RESULTS R123 Lemma B-ONLY («at every state t and
  every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex») at the
  mover D says the opposite. ∎
- Shared premise: RESULTS R123 B-ONLY is the one premise of both G1's IDEAL-CYC clause (entry 1: K10 empty) and PROVISO.
- Effect on the frozen text (IDEAL-CYC only; no statement is weakened; Γ3 unchanged):
  - §3.4 «(b) At every t with e_o ∉ P_(t−1)(D) ∪ P_t(D): Ω_t(p_e) ≠ Ω_(t−1)(p_e) ⟺ Ω_t(D) ≠ Ω_(t−1)(D).»: on IDEAL-CYC the hypothesis holds at every t, so S(p_e) = S(D) for every gate over the whole run (both values
    constant when D = c_W).
  - §3.4 «(c) If D's play avoids e_o over the run:» and «Lemma WAIT-QUIET (= (a) + (b)). A gate whose e-face continuation D changes value at most K times while its play avoids e_o»: on IDEAL-CYC the proviso is always met; read them there with it deleted.
  - §3.4 «- The proviso «D's play avoids e_o» was never violated on any measured instance (L-RED 63: dpass 0 on 29 instances).» New, after it: «On IDEAL-CYC it holds at every state (Lemma PROVISO, L-RED 63, claude/l-red 2730ab90 R229-box93
    Addendum B; premise RESULTS R123 B-ONLY). On Γ3 it remains a hypothesis of (b), (c) and WAIT-QUIET in this packet.»
  - §1 premises: RESULTS R123 B-ONLY is now used on IDEAL-CYC (it is already in §1's landed list, «R123 (LOC-GATE, NO-TIE, B-ONLY, …)»).
- DATA: L-RED 63's dpass 0 on 29 instances (own engine; R229-box93 §2, fa4e50fe; and its 2000-iteration DP climb, Addendum A); L-SI
  box 96's dpass 0 (unit (gate, state); 19 instances: box 91's 11, box 93's 8; 307,737 pairs per engine; own and g3, rows identical;
  experiments/si/box96/out/own96.out, g396.out); control CTRL=anti (Odd non-optimal: e-face at o, β-face elsewhere; own engine) fires
  on 14 of 19 (out/ctrl96.out).

### Line L-2
- docs/si/P-N5-GATE-line-L2.txt = L-1 with three replacements (fix2/mkL2.py, each Old asserted once in L-1): the proviso clause (IDEAL-CYC
  PROVISO stated, with its proof in one sentence; Γ3 a hypothesis), PROVISO's DATA clause, «fixes entries 1-2». sha1 c0f2007d84afab1e00ef41e24ba8f5f064468cc5, 10295
  bytes (wc -c). L-1 stays as written (a44647db…, 9,541 bytes).
