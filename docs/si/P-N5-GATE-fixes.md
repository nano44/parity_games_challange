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

## Entry 3 (fix round 3; L-SI successor 50; Lead 2026-11-11 23:33Z and 2026-11-12 01:14Z: ONE entry answering both referees)
Governing: REFEREE-2 37 Addendum 1 (claude/referee-2 8983b3d8), Lead 01:38Z. Items: REFEREE 31 (claude/referee a401ce0e, docs/referee/R-P-N5-GATE.md; byte copy experiments/si/box95/fix3/ref_R-P-N5-GATE_a401ce0e.md,
sha1 8c24800e…): R-1..R-7, D-1..D-5 REQUIRED, G-a..G-c (GT-1) taken. REFEREE-2 37 (claude/referee-2 c035b35f, docs/referee-2/R2-P-N5-GATE.md;
byte copies fix3/ref2_R2-P-N5-GATE_c035b35f.md, sha1 aa0b4e5a…, and its l3req.py / l3req_applied.txt, sha1 30833fcc… / 1bd49ea1…):
G-1..G-7 and line items R-1..R-10, all taken. Verdicts (both): every statement SIGN; Γ3 rows CONDITIONAL on R125, which has LANDED
(trunk 0753fd71: «### R125 [refereed-only]»), so it is cited below as RESULTS R125; A*-EQUIV (ii), (iii) also on P-N5-SPLIT. Strings: this
text by fix3/mkfix3.py (each Old asserted once in the frozen packet); L-3 by fix3/mkL3.py, which parses both referees' strings from the
byte copies (never retyped), merges overlapping ones, and asserts every referee id answered.

### F3-1 (REFEREE GT-1 = REFEREE-2 G-5): B-ONLY on Γ3 IS a P-N5-CHAIN fact (now RESULTS R125); entries 1-2 corrected
- RETRACTED: entry 1's G1 sentences «On Γ3 the same needs B-ONLY on Γ3, which is not among P-N5-CHAIN's facts (§1) and not landed» and
  every New of entry 1 / entry 2 that says K10 or the PROVISO stays open, or is a hypothesis, on Γ3. They are FALSE: P-N5-CHAIN §5
  (claude/l-new 93531b03, l. 201) is Lemma B-ONLY3 with the same pad exceptions, signed by both referees, landed in RESULTS R125. My
  error: I took L-RED 63's G1 claim without opening P-N5-CHAIN §5. Box 96's B-ONLY3 is the same lemma, re-derived (P-N5-BONLY3 is
  WITHDRAWN as a landing packet: docs/si/P-N5-BONLY3-fixes.md entry 1).
- §3.2 scope bullet. Old: «- Scope (L-RED 63, R229-box92): the K3 / K4 / K9 consequences hold on LAM ∧ PRIV ∧ UP steps only; a flip at a LAM ∧ PRIV step with e_o not above Λ («below», row K10 of WAIT-CLOSED) is covered by no part of this lemma (but by §3.4).»
  New (supersedes entry 1's New): «- Scope: the K3 / K4 / K9 consequences hold on LAM ∧ PRIV ∧ UP steps only. A LAM ∧ PRIV step with
  e_o not above Λ («below», row K10 of WAIT-CLOSED) does not occur on either run: on IDEAL-CYC by RESULTS R123 B-ONLY, on Γ3 by RESULTS
  R125's B-ONLY3 (pβ_o is never an exception; pe_o is one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o)); referee-originated:
  REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5.»
- §3.4, WAIT-QUIET. Old: «(the classes K1-K10 of box 92's WAIT-CLOSED). ∎»
  New (supersedes entry 1's New): «(the classes K1-K10 of box 92's WAIT-CLOSED; K10 is empty on both runs, §3.2's scope bullet). ∎»
- §3.4, proviso note. Old: «- The proviso «D's play avoids e_o» was never violated on any measured instance (L-RED 63: dpass 0 on 29 instances).»
  New (supersedes entry 2's): «- The proviso «D's play avoids e_o» holds at every state of both runs: on IDEAL-CYC by Lemma PROVISO
  (L-RED 63, claude/l-red 2730ab90; premise RESULTS R123 B-ONLY), on Γ3 at every state 0, …, T3 by RESULTS R125's B-ONLY3 at the mover D,
  the same argument (referee-originated: REFEREE R-P-N5-GATE GT-1, REFEREE-2 R2-P-N5-GATE G-5). So (b), (c) and WAIT-QUIET hold with no
  proviso on both runs. DATA: dpass 0 (L-RED 63, 29 instances; L-SI box 96, 19 instances, two engines).»
- §8, R229-box92 row. Old: «scope corrected to LAM ∧ PRIV ∧ UP (§3.2); «below» named K10.»
  New (supersedes entry 1's New): «scope corrected to LAM ∧ PRIV ∧ UP (§3.2); «below» named K10; K10 is empty on IDEAL-CYC by RESULTS
  R123 B-ONLY and on Γ3 by RESULTS R125's B-ONLY3 (REFEREE GT-1, REFEREE-2 G-5).»
- §1, P-N5-CHAIN's status. Old: «- P-N5-CHAIN (L-NEW; frozen claude/l-new 93531b03; landing as R125, PENDING): the Γ3 facts used by name:»
  New: «- P-N5-CHAIN (L-NEW; frozen claude/l-new 93531b03, sha1 6e613ba7; LANDED as RESULTS R125, trunk 0753fd71): the Γ3 facts used by
  name (all in R125 except F2, CYC, (E-DOM), (Core), which are cited from the frozen text; REFEREE-2 R-10), with B-ONLY3 and LOC-K2-3 added:»

### F3-2 (REFEREE-2 G-1 = REFEREE R-7): (Core) in its W-1-repaired reading
- §1. Old: «(Core) (K0, K3 lie on both of two plays with the same Λ or on neither)»
  New: «(Core) (P-N5-CHAIN §2's frozen core edges; used here ONLY in its W-1-repaired reading for non-core vertices: a non-core play
  passes K0 iff it passes K3 (P-N5-CHAIN fixes entry 3, R-W); every use in this packet compares two non-core vertices, the faces of a gate
  (§3.2 (a), (b′)) or the successors of a mover or a gate (§3.7 Step 2); on Γ read off R104's priorities and core edges; referee-originated:
  REFEREE-2 R2-P-N5-GATE G-1)». The global gloss is false (plays from K3 and from K0 both have node K1; only one passes K0); no proof
  changes, since every use is at non-core vertices.

### F3-3 (REFEREE-2 G-2, R-2; REFEREE GT-8): the F3 / F6 / F4′ glosses and the premise rows
- §1. Old: «F3 (E_t(v) is the set of e-vertices on v's play at t more relevant than Λ_t(v))»
  New: «F3 (the recursion: if Λ_t(v) ≠ v then Ω_t(v) = ext(v, Ω_t(nx_t(v))); where §3.1 TRIGGER, §3.2 (b), §3.3 and §3.6 cite «F3» for
  «E_t(v) is the set of e-vertices on v's play more relevant than Λ_t(v)», they mean the definition of E_t(v) (§2), not F3)»
- §1. Old: «F6 (an e-vertex has exactly one successor, its W-target)»
  New: «F6 (no mover is the cycle node of its own play; every non-mover Even vertex has one successor in HOW3), with [Γ3] / [DEF] for
  «an e-vertex has exactly one successor, its W-target» where the packet cites F6 for it»
- §1. Old: «F4′ (the extension inequality used in P-N5-SPLIT §2 (a))»
  New: «F4′ (the extension inequality, used in PAIR-EXPEL Step 1)»
- Table §3.1. Old: «| §3.1 | Lemma GATE-RACE (a), (b); Corollary TRIGGER | PROVED | F1, F2, LOC-GATE3, NO-TIE3, E-MON3, [OPT] |»
  New: «| §3.1 | Lemma GATE-RACE (a), (b); Corollary TRIGGER | PROVED | F1, F2, LOC-GATE3, NO-TIE3, E-MON3, [OPT]; TRIGGER also CYC |»;
  heading. Old: «### 3.1 Lemma GATE-RACE and Corollary TRIGGER (PROVED; F1, F2, LOC-GATE3, NO-TIE3; TRIGGER also E-MON3, [OPT], F3)»
  New: «### 3.1 Lemma GATE-RACE and Corollary TRIGGER (PROVED; F1, F2, LOC-GATE3, NO-TIE3; TRIGGER also E-MON3, [OPT], CYC and the
  definition of E)»
- Table §3.5. Old: «| §3.5 | Lemma SAME-SUFFIX; Lemma STEP-BOUND | PROVED | [VJ], LOC-GATE3, NO-TIE3, [HOW] |»
  New: «| §3.5 | Lemma SAME-SUFFIX; Lemma STEP-BOUND | PROVED | [VJ], LOC-GATE3, NO-TIE3, LOC-K2-3 (R123 LOC-K2 on IDEAL-CYC; for K2), [HOW] |»;
  heading. Old: «### 3.5 Lemma SAME-SUFFIX and Lemma STEP-BOUND (PROVED; [VJ], LOC-GATE3, NO-TIE3, [HOW])»
  New: «### 3.5 Lemma SAME-SUFFIX and Lemma STEP-BOUND (PROVED; [VJ], LOC-GATE3, NO-TIE3, LOC-K2-3 / R123 LOC-K2, [HOW])»

### F3-4 (REFEREE R-1, R-2, GT-2 = REFEREE-2 G-4, R-4; REFEREE GT-5 = REFEREE-2 G-6, R-8): PAIR-EXPEL / EXPEL-COUNT need no P-N5-SPLIT premise
- Table §3.7, label. Old: «PROVED-CONDITIONAL on P-N5-SPLIT (Step 1 quotes its §2 (a))»
  New: «PROVED (on Γ3 CONDITIONAL on RESULTS R125 only; Step 1 is the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), written out here)»;
  premises: F3 added (Step 1 uses Ω(u′) = ext(u′, Ω(b′))).
- Heading. Old: «### 3.7 Lemma PAIR-EXPEL and Corollary EXPEL-COUNT (PROVED-CONDITIONAL on P-N5-SPLIT §2 (a); premises as in the table)»
  New: «### 3.7 Lemma PAIR-EXPEL and Corollary EXPEL-COUNT (PROVED; on Γ3 CONDITIONAL on RESULTS R125; premises as in the table, with F3)»
- Step 1. Old: «(P-N5-SPLIT §2 (a), with F1, STRICT, F4′, CN2-3)»
  New: «(the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), with F1, STRICT, F3, F4′, CN2-3; nothing of P-N5-SPLIT is a premise)»
- EXPEL-COUNT. Old: «(≤ 3M; L-RED R228 §2)»
  New: «(≤ 3M: u′ is the first vertex whose successor differs; non-mover Even vertices are frozen (F6; R118 (a)) and σ̄(K2) is fixed
  (LOC-K2-3 / R123 LOC-K2), so u′ is a mover or a gate and b′ one of its out-edges: M mover edges plus 2M gate faces; referee-originated:
  REFEREE-2 R2-P-N5-GATE G-6; REFEREE R-P-N5-GATE GT-5 re-derived the same count)»

### F3-5 (REFEREE R-3, GT-3, GT-4, GT-9 = REFEREE-2 G-3, G-7, R-3, R-5, R-8): A*-EQUIV
- Table §3.8. Old: «PROVED-CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT) and P-N5-CHAIN (C-EQUIV)»
  New: «(i) PROVED on both runs; (ii), (iii) on Γ3 (HOW3) only, PROVED-CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT, C-EQUIV) and RESULTS R125»
- Heading. Old: «### 3.8 Corollary A*-EQUIV (PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and P-N5-CHAIN's C-EQUIV)»
  New: «### 3.8 Corollary A*-EQUIV ((i) PROVED, both runs; (ii), (iii) Γ3 only, PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and
  C-EQUIV)»
- (i). Old: «(L-NEW, N5-CORE-forms §3 (5): cited, not re-proved here; uses E-MON3 only).»
  New: «Proof (referee-originated: REFEREE-2 R2-P-N5-GATE G-7; REFEREE R-P-N5-GATE GT-4 re-derived it): C ≤ A*_all: take b := v, J := I;
  each change of E(v) with top y makes y enter (E-MON3), which starts a new maximal run of y, so c_y(v, I) ≤ a_y(v, I). A*_all ≤ 1 + M·C:
  every run of z on J, except one present at J's first state, starts at a change of E(b) inside J, and those number Σ_y c_y(b, J) ≤ M·C.
  Uses E-MON3 (R121 E-MON on IDEAL-CYC) only; no lane file is cited.»
- (iii). Old: «(with C-EQUIV)»
  New: «(with P-N5-SPLIT's Corollary C-EQUIV; (ii) and (iii) are Γ3 statements only)»
- §1, P-N5-SPLIT row. Old: «C-EQUIV and the form list in L-NEW's docs/new/N5-CORE-forms.md (claude/l-new 14babccb).»
  New: «Corollary C-EQUIV (P-N5-SPLIT §6, frozen claude/l-new 399cda07, sha1 5bc1b1f3); the form list in L-NEW's docs/new/N5-CORE-forms.md
  (claude/l-new 14babccb) is context only, not a premise.»

### F3-6 (REFEREE D-4 = REFEREE-2 R-9): the copy rows, re-measured as sets
- §6. Old: «- §3.5: lev94 (unit level; box 94's 22): copy rows S(R_j) = S(R_(j−1)), flips(g_Qj) 0 on NDV / NDB.»
  New: «- §3.5 (a record of box 94's nesting families, not a test of SAME-SUFFIX's statement): copy rows S(R_j) = S(R_(j−1)) AS SETS on
  every level of 20 of box 94's 22 instances, all but NSQ2_4, NSQ3_4, whose levels run one after another and whose rows differ (|S(R_j)|
  18, 22, 26) (L-SI box95/fix3/copy95.py, both engines, rows identical, out/copy95_*.out; REFEREE 31's replay agrees; lev94 compared
  sizes only, and the frozen «22» was false); flips(g_Qj) 0 on NDV / NDB.»
- §6 controls. Old: «CTRL=a0 afail 14 / 96;»
  New: «» (deleted: EXP-PATHS's control, not a statement of this packet; REFEREE D-5b).

### F3-7 (L-3): the line, both referees' strings, one answer table
- docs/si/P-N5-GATE-line-L3.txt = L-2 with the replacements of fix3/mkL3.py, applied in its order; sha1 b60495b2c607e8e6c1e145e40478717fa6ed15f4, 12353 bytes (wc -c).
  Kind V: one referee's string verbatim; S: the two referees' strings coincide in meaning, REFEREE's taken; M: merged by the lane (both
  referees' Olds lie inside the merged Old, asserted; the New carries both referees' facts and credits).
  - 31:R-6, 31:R-7, 31:R-2, 31:G-c, 2:R-5c, 2:R-1/R-10 | M
  - 31:R-1, 2:R-4 | M
  - 31:R-3, 2:R-3/R-5d, 2:R-8a | M
  - 31:R-4, 2:R-5a | M
  - 31:R-5, 2:R-5b | S
  - 31:G-a, 2:R-6a | M
  - 31:G-b, 2:R-6b | M
  - 31:D-4, 2:R-9 | M
  - 31:D-1 | V
  - 31:D-2 | V
  - 31:D-3 | V
  - 31:D-5a | V
  - 31:D-5b | V
  - 2:R-8b | V
  - 2:R-7a | V
  - 2:R-7b | V
  - lane | M
- Absent from L-3 (asserted by mkL3.py): «§2 (a)», «P-N5-CHAIN's C-EQUIV», «lie on both of two plays», «not a premise here», «not among
  P-N5-CHAIN», «while its play avoids», «over the run then», «CTRL=a0». Parentheses balance; no «|».
- Governing list: REFEREE-2 37 Addendum 1 (claude/referee-2 8983b3d8; byte copy fix3/ref2_R2-P-N5-GATE_8983b3d8.md), as the Lead
  ruled (01:38Z). Choices made there: PAIR-EXPEL drops the P-N5-SPLIT condition (REFEREE-2 R-4; the argument of P-N5-SPLIT §3 (a) is
  written out in the packet, so it is no premise); Γ3 premises in REFEREE-2's R-1 / R-10 form (supersedes REFEREE R-7, G-c); A*-EQUIV in
  REFEREE's R-3 form ((i) on both runs, (ii) on Γ3 only) with REFEREE-2's G-7 proof credit; DATA by REFEREE's D-1..D-5 (supersede
  REFEREE-2's R-9); Γ3 K10 / PROVISO by G-a / G-b = R-6a / R-6b with «RESULTS R125»; REFEREE-2's R-7a / R-7b («at every state of the
  run») kept, though optional once G-b holds the proviso on both runs.

## Entry 4 (fix round 4; L-SI successor 50; Lead 2026-11-12 02:57Z, 03:00Z, 03:17Z, 04:09Z)
Items: REFEREE 31 (claude/referee fbc4d865, docs/referee/R-P-N5-GATE.md; byte copy experiments/si/box95/fix4/ref_R-P-N5-GATE_fbc4d865.md,
sha1 9aaf92a6…): §I (L-3 byte test: entry 3 CORRECT; L-3 MATCHES except LT-1) and §J (GT-10, strings GL-1..GL-3). REFEREE-2 37's L-3
byte test (claude/referee-2 6269fec5, Addendum 2): L-3 MATCHES, no new item. Strings: L-4 by fix4/mkL4.py (GL-1..GL-3 parsed from the byte
copy, never retyped); this text by fix4/mkfix4.py.

### F4-1 (LT-1, REQUIRED; Lead's ruling: the landing-order form)
- REFEREE 31: L-3 dropped P-N5-SPLIT's pending status. Lead's ruling (02:57Z): the landing order is fixed, R126 = P-N5-QN, then R127 =
  P-N5-SPLIT, then this entry; so SPLIT-COUNT and C-EQUIV are cited as «RESULTS R127 (P-N5-SPLIT)», and A*-EQUIV (ii), (iii) stay
  labelled CONDITIONAL with R127 as the premise; CHECKER confirms R127 = P-N5-SPLIT at this entry's landing. (REFEREE 31's own New, «of
  the pending packet P-N5-SPLIT … not landed», is superseded by the ruling.)
- L-4: «C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3);» → «C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW,
  frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry);», and «PROVED-CONDITIONAL
  on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV» → «PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV».
- Packet reading: wherever the packet (with entries 1-3) cites P-N5-SPLIT's SPLIT-COUNT or C-EQUIV as a premise (table §3.8, §3.8's
  heading and (ii), (iii), §1's P-N5-SPLIT row), read «RESULTS R127 (P-N5-SPLIT)»; the labels stay CONDITIONAL on it.

### F4-2 (GT-10 = L43, REQUIRED; GL-1..GL-3 verbatim): three asymptotic rows leave the DEAD list and become DATA
- L43 (Lead reading, docs/DECISIONS.md, quoted by REFEREE 31 §J): a lane DEAD of an ASYMPTOTIC statement enters a RESULTS line as DATA
  with its numbers and source commit, or not at all. The three rows below refute their statements only on finitely many instances.
- §5 rows relabelled DATA, not DEAD (the numbers and instances stand; the word «DEAD» goes):
  - «| RA-MULT(K) (constant re-arm multiplicity) | m = n, C = 2n + 1 | MW8_2, MW32_2 | 66b84dcb, 445031d1 | box91 inst |»
    → DATA: re-arm multiplicity m = n with C = 2n + 1 on MW8_2, MW32_2 (refutes a constant multiplicity only below 32).
  - «| polynomial P bound (RA path count) | P = F_(d+2) − 1 with C = 3 | FW8_2, FW16_2 | 108a63cf, 94df42b7 | box91 inst |»
    → DATA: RA path count P = F_(d+2) − 1 with C = 3 on FW8_2, FW16_2 (no finite instance set refutes «polynomial»).
  - «| K1-FLIP(c), every constant c, at k = 1 (L-RED 63) | flips 2n + 1 with lamch 0 | MWR4_2, MWR8_2, MWR16_2 | 856d369b, 918f1414, 2ccda9a9 | box93 inst (copies of claude/l-red 406ef2fd r229/inst) |»
    → DATA: per-gate flips 9 / 17 / 33 at lamch 0 on MWR4_2, MWR8_2, MWR16_2 (L-RED 63, claude/l-red 406ef2fd; refutes c·(lamch + 1)
    only for c ≤ 32).
- The construction rows (WC, K6 LAG TOWER, K7 probe, nesting multipliers, Db / Dbr) stay DEAD: each records that a named construction
  fails to produce growth, with measured numbers; they claim no asymptotic bound (REFEREE 31 §J; the Lead, 03:00Z).
- L-4: GL-1 and GL-2 delete the three from the DEAD clause; GL-3 adds them as DATA after «… inst with sha1 files» (strings in fix4/mkL4.py,
  parsed from REFEREE 31 §J).

### F4-3 (L-4)
- docs/si/P-N5-GATE-line-L4.txt = L-3 + LT-1 (two strings) + GL-1..GL-3 + «fixes entries 1-4»; sha1 6bfde78ef050b47f43527875256c65a205869e77, 12562 bytes (wc -c).
  mkL4.py asserts each Old once, that «RA-MULT», «K1-FLIP(c)» and «a polynomial bound on the RA path count» are absent, no «|», and
  balanced parentheses.

## Entry 5 (fix round 5; L-SI successor 52; Lead 2026-11-12 17:47Z; CHECKER C142)
Items: CHECKER C142 (claude/checker 269effb3, docs/checker/C142.md; byte copy experiments/si/box95/fix5/chk_C142_269effb3.md, sha1
8b005c61…): FAIL on the first fill of R128, with three line items E-1, E-2, E-3 (§2) and one entry-text item E-4 (the Lead's; not in
this entry). Mathematics, tools, box checks, UPDATE and placement PASS there. Strings: L-5 by fix5/mkL5.py, which parses C142 §4's nine
old → new pairs from the byte copy and applies them to L-4 in §4's order, each old string asserted once, and then a tenth pair
ruled by the Lead (F5-4); this text by fix5/mkfix5.py, which prints the same parsed strings. No string of CHECKER's is retyped.

### F5-1 (E-1, L43, REQUIRED): the RA-MULT and RA-path DATA rows get their numbers and their source commits
- CHECKER: GL-3's two rows gave formulas (m = n, P = F_(d+2) − 1) but no numbers and no source commit. R-E1, verbatim:
  «re-arm multiplicity m = n with C = 2n + 1 on MW8_2, MW32_2 (refutes a constant multiplicity only below 32), the RA path count P = F_(d+2) − 1 with C = 3 on FW8_2, FW16_2,»
  → «re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8_2 / MW32_2 (refutes a constant multiplicity only below 32), the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on FW8_2 / FW16_2 (m and P: L-SI 47 box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines),»
- Re-read here by column name (mkfix5.py asserts them, both engines): box90/out/mw90.out maxm 8 / 32 and C 17 / 65 on MW8_2 / MW32_2;
  box90/out/fw90.out maxP 54 / 2583 and C 3 / 3 on FW8_2 / FW16_2.
- Packet reading: fixes entry 4 F4-2's two DATA rows are read with these numbers and sources.

### F5-2 (E-2, L43, REQUIRED): the growth clause as numbers on named instances; A*_all leaves it
- CHECKER: «growth: … linear in n on every family measured» named no instance, and A*_all has no lane counter. R-E2, verbatim:
  «growth: C, A*_all and the largest gate flip count are linear in n on every family measured (MW(n): C = 2n + 1, flips 4n + 2; MWR(n): flips 2n + 1 = 2·ch_D + 1 with lamch 0, which makes E-FACE-PAYS (d) tight)»
  → «growth, as numbers on the named instances only (both engines; box91/out/own91.out and g391.out C and maxflip, box93/out/mwr93_own.out and mwr93_g3.out mx_flips and mx_ch_D): C 17 / 65 and the largest per-gate flip count 34 / 130 on MW8_2 / MW32_2, and per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / 8 / 16) with lamch 0 on MWR4_2, MWR8_2, MWR16_2, where E-FACE-PAYS (d) holds with equality»
- Re-read here by column name (both engines): box91/out/own91.out and g391.out C 17 / 65 and maxflip 34 / 130 on MW8_2 / MW32_2;
  box93/out/mwr93_own.out and mwr93_g3.out mx_flips 9 / 17 / 33 and mx_ch_D 4 / 8 / 16 on MWR4_2, MWR8_2, MWR16_2.
- For the record (Lead 17:47Z): box 91's counter «maxa» is NOT A*_all. On MW8_2 / MW32_2 maxa is 9 / 33 (re-read here) while C is 17 / 65;
  CHECKER cites REFEREE-2 Add. 4 for A*_all = 66 on MW32_2. The lane has no A*_all counter; the clause no longer names A*_all.

### F5-3 (E-3, REQUIRED): the part markers of GATE-LOW-NULL and E-FACE-PAYS enter the line (seven insertions, no word changed)
- CHECKER: the line cites E-FACE-PAYS (b), (c), (d) and GATE-LOW-NULL (a), (b′), but its statements did not mark those parts. The
  markers are the packet's (§3.2, §3.4). R-E3, verbatim, in §4's order:
  - «(Lemma GATE-LOW-NULL) at a LAM ∧ PRIV step» → «(Lemma GATE-LOW-NULL) (a) at a LAM ∧ PRIV step»
  - «(and they differ), so a flip at t» → «(and they differ), so (b) a flip at t»
  - «changes π(E(p_e)) or π(E(p_b)) at t, and if Λ(p_e) = Λ(p_b)» → «changes π(E(p_e)) or π(E(p_b)) at t, and (b′) if Λ(p_e) = Λ(p_b)»
  - «(Corollary E-FACE-PAYS) relocks(o) ≤ ch_(p_e),» → «(Corollary E-FACE-PAYS) (a) relocks(o) ≤ ch_(p_e),»
  - «UP hypothesis, at every t with e_o ∉» → «UP hypothesis, (b) at every t with e_o ∉»
  - «that of D does, so if D's play avoids e_o at every state of the run then» → «that of D does, so (c) if D's play avoids e_o at every state of the run then»
  - «unchanged), and flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1» → «unchanged), and (d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1»
- mkfix5.py asserts that each new string is its old string with exactly one marker «(a) », «(b) », «(b′) », «(c) » or «(d) » inserted.

### F5-4 (the tenth pair: Lead ruling 2026-11-12 17:58Z, flagged by REFEREE-2 38)
- The Lead: L-5's source note must say «with its fixes entries 1-5», not «1-4». Precedent: L-4 changed «1-3» to «1-4» when the
  line-only entry 4 was added. So L-5 gets a tenth pair on top of CHECKER's nine:
  «docs/si/P-N5-GATE.md with its fixes entries 1-4,» → «docs/si/P-N5-GATE.md with its fixes entries 1-5,».
  The successor list «L-SI successors 48-50» stays (the Lead, citing CHECKER C142 G-1: no action).

### F5-5 (L-5)
- After CHECKER's nine pairs (R-E1, R-E2, R-E3's seven) the line is CHECKER's target byte for byte (C142 §4: «sha1
  **7ebcf7355be9838473f05a7defe913940b6fd723**, 12,923 B»): mkL5.py asserts it and prints it with --nine; check_fix5.sh re-checks it.
- docs/si/P-N5-GATE-line-L5.txt = that line + the tenth pair; sha1 459fd88d2d1959647f6aeb065bf8ac58cce684f9, 12923 bytes (wc -c). mkL5.py asserts each old
  string once, one line with its newline, no «|», and 238 «(» = 238 «)» before and after the tenth pair.
