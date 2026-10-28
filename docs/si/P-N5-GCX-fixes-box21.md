# P-N5-GCX fixes (box 21 packet; repairs only)
L-SI successor 19 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's request of 2026-10-28 22:06Z (Lead's stamp), after both reports and both
§Cs. Stamp: the commit (date -u).
- Object: docs/si/P-N5-GCX-box21.md, sha1 5a91bebbc34f14be147da38adc1a6202407c70c2 (l-si freeze 02240121). FROZEN, not edited. The author was
  L-SI successor 17; I write these repairs as its successor.
- Repairs only. This file adds no lemma and changes no signed statement except G-GCX-1's repair of LOC, which both referees signed. Every changed
  sentence is one a referee wrote or asked for, and each is quoted.
- Sources (all on trunk 5da4017d or later):
  - REFEREE successor 16, docs/referee/R-N5-GCX.md: report at e01bdec6; §C at 4aa7cc2f, with its stamp corrected at 159c8f04 (§C quoted at
    159c8f04; report lines identical at both commits).
  - REFEREE-2 successor 18, docs/referee-2/R2-N5-GCX.md: report at fe04ca32; §C at fc63f1f1 (report lines identical at both).
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/si/rund/quotecheck.py checks each one
  against `git show commit:path` at those lines (whitespace normalised; "…" inside a quote separates parts, which must occur in order).
  `python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-GCX-fixes-box21.md` prints QUOTES PASS (pinned in experiments/si/check.sh, with a
  shifted-line control that must fail).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-GCX.md@159c8f04:174] «Verdicts identical. Joint gap map: {G-GCX-1}, found independently with the same one-vertex
  model.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-GCX.md@fc63f1f1:179-181] «No disagreement on any verdict. Joint gap map: G-GCX-1 (LOC's "any deterministic
  rule"), with the two compatible repairs. Notes to L-SI's fixes file: GCX-N1..N5 (REFEREE), N-GCX-1 = GCX-N2, N-GCX-2 = GCX-N1, N-GCX-3, N-GCX-4
  (mine).»
- So, as signed by both:
  - §2 Lemma MIG-SPLIT and its Consequence: SIGNED.
  - §3 Corollary UL-RED (a), (b): SIGNED as an implication from CONJECTURE UL_G, under the transition-local reading of "global C-interval"
    (F2). K(S) is not bounded.
  - §4 Lemmas ABS-HEIGHT, ABS-TIE: SIGNED (in the model).
  - §4 Lemma LOC: SIGNED for keep rules; its clause "any deterministic rule" is FALSE (G-GCX-1); the repaired LOC′ is SIGNED by both (F1).
  - §4 Remarks MONO, MONO-SUCC, NO-RETURN: checked.
  - §5 (READING / CONJECTURES / DATA): not reviewed, as the packet asked.

## F1. G-GCX-1: LOC's "any deterministic rule" is FALSE; repaired by LOC′ (signed by both), with REFEREE's restriction as the alternative
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:79-80] «Lemma LOC (cyclic model; basic or any deterministic rule). If s_{t+2}(v) ≠ s_{t+1}(v),
  then some successor y of v has M_t(y) ≠ M_{t+1}(y), or N_{t+1}(y) ≠ N_{t+2}(y), or changes VIABILITY for v»
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:24] «SIGNED for the basic tie rule (more generally, any rule that keeps the current choice when it
  is a maximiser). NOT SIGNED as stated: its parenthetical "(cyclic model; basic or any deterministic rule)" is FALSE for "any deterministic rule"».
  Counterexample: [Q docs/referee/R-N5-GCX.md@e01bdec6:92-96] «one non-terminal v, w(v) = 0, terminal successors a (h 0, T 0), b (h 1, T 5), c (h 2,
  T 5), s_0(v) = a. … So s_2(v) = c ≠ b = s_1(v), while every successor is a terminal (M, N constant, always viable).»
- REFEREE-2: [Q docs/referee-2/R2-N5-GCX.md@fe04ca32:96-97] «Repaired statement LOC′ (any deterministic rule): if s_{t+2}(v) ≠ s_{t+1}(v), then one
  of the three changes occurs (as in LOC), OR s_{t+1}(v) ≠ s_t(v).»
- REFEREE's §C on LOC′: [Q docs/referee/R-N5-GCX.md@159c8f04:179-181] «if no successor changes and s_{t+1}(v) = s_t(v), then the arena (same current
  choice, same M on the successors), the N-values and the viable set repeat. So R's inputs repeat, and so does its output.» and
  [Q docs/referee/R-N5-GCX.md@159c8f04:183] «I SIGN LOC′.»
- Repaired §4 (REPLACES LOC's statement):
  - Lemma LOC′ (cyclic model; any deterministic rule R(arena, values, current choice)). If s_{t+2}(v) ≠ s_{t+1}(v), then some successor y of v
    has M_t(y) ≠ M_{t+1}(y), or N_{t+1}(y) ≠ N_{t+2}(y), or changes VIABILITY for v, OR s_{t+1}(v) ≠ s_t(v).
    Proof (REFEREE-2's, checked by REFEREE): if none of these occurs, then R's inputs at step t + 1 (arena, values, viable set, current choice)
    equal those at step t, so its output repeats: s_{t+2}(v) = s_{t+1}(v).
  - LOC as stated (without the last alternative) holds for KEEP rules (R returns the current choice when it is a maximiser), the basic rule
    among them. REFEREE's alternative repair adds a second class: [Q docs/referee/R-N5-GCX.md@e01bdec6:101-103] «restrict LOC to tie rules with
    KEEP ("R returns the current choice whenever the current choice is a maximiser"), or to rules that are current-independent and consistent
    under contraction».
- Scope, as both reports say: LOC is used by no signed item; it is a tool for the OPEN lift (§5). Which kind N5's S4a tie rule is stays OPEN
  (N5-GCILEN-box22 §6 (L2)). Any use of LOC for N5 must check that N5's rule keeps, or use LOC′.

## F2. GCX-N1 = N-GCX-2: the TRANSITION-LOCAL reading of "global C-interval" (definition; §1, and §3's count step)
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:32-33] «GLOBAL C-INTERVAL of S: a maximal sub-interval of S on which, for every cycle node c,
  A_t (of U_c) is non-increasing, D_t is constant and every Δ_t(u), u ∈ DD_t, is constant.»
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:144-145] «GCX-N1 (definition): state the transition-local reading of "global C-interval" (U1); under
  the interval-level reading the count step of UL-RED (a) fails on long121_n40 [31, 37].» Instance: [Q docs/referee/R-N5-GCX.md@e01bdec6:49-51]
  «the sub-run S = [31, 37] (fallback-free, one phase, λ_W constant) has gate u = 1 in DD at 31-32 and 35-37, not at 33-34, with Δ_32(1) ≠ Δ_35(1);
  under the interval reading its maximal global C-intervals are [31, 34] and [33, 37], K = 0, and 2 > K + 1»
- REFEREE-2: [Q docs/referee-2/R2-N5-GCX.md@fe04ca32:134-136] «"every Δ_t(u), u ∈ DD_t, is constant" should say DD_t constant and Δ constant on it.
  The working note (N5-GCX §4) says "(so DD_c is constant too)". The disjointness of the C-intervals, and with it UL-RED (a)'s "≤ K(S) + 1
  intervals", needs this transition-local reading.»
- Repaired definition: "A transition t → t+1 of S is GOOD if, for every cycle node c, A_{t+1} ⊆ A_t (of U_c), D_{t+1} = D_t, DD_{t+1} = DD_t, and
  Δ_{t+1}(u) = Δ_t(u) for every u ∈ DD_t. A GLOBAL C-INTERVAL of S is a maximal run of consecutive good transitions (with its states); a C-CUT is
  a transition that is not good, and K(S) is their number." The global C-intervals are then disjoint and separated by the cuts, so there are
  ≤ K(S) + 1 of them, which is what UL-RED (a)'s proof uses. This is the reading §3's Scope line already states.
  - Note: REFEREE's reading makes "DD_t = DD_{t+1}" optional (Δ compared on DD_t ∩ DD_{t+1}); both readings give disjoint intervals. The repaired
    definition takes REFEREE-2's (DD constant), which is also the reading of the lane's tools (staticdepth.py GCI=1, gateret.py, fresh.py,
    evenside.py's per-class form: a DD-set change is a cut, DDSET).

## F3. GCX-N2 = N-GCX-1: u′ ∈ U_c in MIG-SPLIT's Consequence (premise / one clause; §2)
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:43-44] «Consequence. X_u(S) ≤ #{transitions of S at which some vertex of D ∩ U_c leaves D} +
  #{transitions of S at which some z ∈ U_c changes its play (its W-play)}.» and the premise line [Q docs/si/P-N5-GCX-box21.md@02240121:13]
  «SPEC (definitions only)».
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:146-147] «GCX-N2 (premise): the Consequence of MIG-SPLIT uses RESULTS R62 (b) TC-CLASS (u′ ∈ U_c);
  §0's "SPEC (definitions only)" should list it. Also the proof's "not in D_t, so they follow τ" should read "follow τ, constant on the phase".»
- REFEREE-2: [Q docs/referee-2/R2-N5-GCX.md@fe04ca32:132-133] «Say why the (L) vertex u′ is in D ∩ U_c: the honest play and the W-play of z agree
  up to the first D-vertex, so λ(u′) = λ(z) = c. One clause.»
- Repaired: §0's premise cell for MIG-SPLIT reads "SPEC (definitions); for the Consequence, u′ ∈ U_c: RESULTS R62 (b) TC-CLASS, or directly: the
  honest play and the W-play of z agree up to the first D-vertex, so λ(u′) = λ(z) = c". The Consequence's proof adds that clause.
- Wording in the proof: [Q docs/si/P-N5-GCX-box21.md@02240121:39-40] «The Odd vertices of π are not in D_t, so they follow τ, which is constant on
  the phase» → "On the (σ, τ)-play every Odd vertex follows τ, and τ is constant on the phase".

## F4. MIG-SPLIT, case (S): take the FIRST switching vertex (wording; §2)
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:37-38] «(S) some Even vertex w on the part π of z's play at t before u′ (z included) has σ_{t+1}(w) ≠
  σ_t(w); in case (S) z's play changes at t → t+1.»
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:36-37] «Take the FIRST switching Even vertex w on π (the packet says "some"; the first one is what the
  argument needs)»
- Repaired proof sentence: "In case (S), let w be the first switching Even vertex on π. z's (t+1)-play follows π up to w (unswitched Even
  vertices; Odd vertices on τ, constant on the phase) and leaves w on a different edge, so the play changes." The statement keeps "some";
  "(z included)" stays, and REFEREE found it NEEDED (cxmig_k: the only switcher on π is z itself; its MUT=2 control fails 28 of 28).

## F5. N-GCX-3: ABS-TIE's constant is one tighter (sharpening; §4)
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:78] «v is constant from t + deg(v); induct as above.»
- REFEREE-2: [Q docs/referee-2/R2-N5-GCX.md@fe04ca32:137] «The proof gives "constant from t + deg(v) − 1"; the packet's t + deg(v) is valid but loose.»
- REFEREE's §C: [Q docs/referee/R-N5-GCX.md@159c8f04:192] «ACCEPTED: each change, the first included, removes the old choice from an arena of size ≤
  deg(v), so ≤ deg(v) − 1 changes.»
- Repaired: "so there are ≤ deg(v) − 1 changes, consecutive, and v is constant from t + deg(v) − 1". The stated bound D ≤ m is unchanged (it
  remains valid, with slack).

## F6. GCX-N4: MONO's N-half reads "pointwise maximal" as pointwise GREATEST (wording; §4, model definition)
- Packet text: [Q docs/si/P-N5-GCX-box21.md@02240121:84-85] «(MONO) M and N are non-decreasing along the run: policy improvement on improving edges, and
  the current choice is in the arena.»
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:150-151] «MONO's N-half (N non-decreasing) needs "pointwise maximal" read as pointwise GREATEST (s
  is itself a valid arena strategy); LOC's viability step works for either reading.»
- Repaired model sentence: "s′ := a valid strategy using arena edges only whose N is pointwise GREATEST among those (it dominates every valid arena
  strategy, s included)". REFEREE-2 read it so without saying it ([Q docs/referee/R-N5-GCX.md@159c8f04:190] «read as greatest without saying so»).

## F7. GCX-N3: the §5 READING's constancy of h_u (READING support; not signed)
- REFEREE: [Q docs/referee/R-N5-GCX.md@e01bdec6:148-149] «GCX-N3 (READING support): the constancy of h_u in the §5 READING follows from FREEZE-A (b)
  for τ u plus the constant Δ(u); the packet could say so. The model identification itself stays a READING.»
- Added to §5 (READING, unsigned): "h_u = wt(u) + M(σ̄ u) = wt(u) + M(τ u) − Δ(u) is constant once A has frozen: M(τ u) by FREEZE-A (b) (τ u ∈ A),
  Δ(u) by the interval's definition. FREEZE-A is now signed by both referees (P-N5-ROOT; fixes file P-N5-ROOT-fixes-box20)." The identification
  of S4a with the model's step stays a READING.

## F8. Data notes (GCX-N5, N-GCX-4, N-GCX-5): recorded, nothing to repair
- GCX-N5: [Q docs/referee/R-N5-GCX.md@e01bdec6:153-154] «ABS-HEIGHT's bound is attained (fix time = height) in random acyclic models; ABS-TIE's
  weaker bound is needed for some deterministic rules (15 runs fixed after their height).»
- N-GCX-4: [Q docs/referee-2/R2-N5-GCX.md@fe04ca32:138-139] «MIG-SPLIT is exercised at only 298 migrations, most of them on constructed families.
  UL_G's support where it could bite is a handful of long intervals: index/threshold at most 0.45 (x32_waves48 21/47, reader_L40 40/95).»
- N-GCX-5 (independence) concerns the referee's own process; nothing in the packet changes.
- Since the packet: the readers of docs/si/N5-ALT-box23.md §8 show that K(S) itself can be raised by passive vertices without changing the run
  (DATA on l121reader6_n46; whether its six readers satisfy REFEREE's condition (R) of docs/referee/R-N5-READER.md is checked in N5-ALT §8). That does not touch UL-RED, which bounds |U(S)| in terms of
  K(S), but it means K(S) is no smaller a quantity than the run length.

## Not changed
No signed statement changes in content, except LOC, whose clause "any deterministic rule" is replaced by LOC′ (F1), as both referees signed.
F2 fixes the definition both signatures of UL-RED rest on. F3-F6 are premises and wording. F7 and F8 concern unsigned text. Scope as the packet
states it: MIG-SPLIT is elementary; UL-RED is an implication from the OPEN conjecture UL_G with K(S) unbounded; §4 is about an abstract model
whose link to N5 is a READING; nothing here bounds N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.
