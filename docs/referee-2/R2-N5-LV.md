# R2-N5-LV: second-referee check of packet P-N5-LV (L-SI box 11: LV-SHAPE, LV-CN, LV-COUNT, FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL) and its not-to-sign addendum. REFEREE-2 (successor 9), written 2026-10-25 14:5xZ-15:30Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-LV (Lead queue 14:03Z by the Lead's stamp).
Objects:
- docs/si/P-N5-LV-box11.md, sha1 d0d797f084904f9ce4df641e90298cac53c61356. It agrees at the pin 601df6e, at origin/claude/l-si, on trunk
  and on my tree.
- docs/si/P-N5-LV-addendum-box11.md, sha1 a15a8871024d33d1734a41cbeb9c2dd75ecdadef (not to sign). It agrees at l-si, on trunk and on my
  tree; it is not in 601df6e (`git show 601df6e:<file>` is empty).
Background read:
- RESULTS R15 (a), (d); R19 (a); R20 (b) FBL; R21 (a); R25 (d), (e) (OFF: "a vertex leaving R̄ keeps its COARSE_{M_k} value", any M_k);
  R28 (a) U-loc ("any game … level ≤ L"); R29 (a)-(e); R30 (a)-(b); R31 (b)-(f) with docs/si/P-N5-FBW-box9.md §1-§3; R35 (a);
- P-N5-RL §1 (R-SAME) and §2 (BL Step 2a); P-N5-SCOPE §6 (CN-LAST).
Independence: nothing in docs/referee/ read for this packet (`ls docs/referee | grep -i lv` is empty). No lane script (lvm1.py) run or
imported.
Tools: docs/referee-2/R2-N5-LV/ (own code on R2-N5-ENT/ent_check.py and R2-N5-OUT/out_check.py):
- lv_check.py, lv_climb.py;
- files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt.
Traces own / rand / spec. Every game asserts exactly one Odd vertex with out-degree > 1.
Labels: PROVED (L-SI succ. 6); PROVED CONDITIONAL on CN-LAST. Not a running-time bound, a TARGET.md claim or a step-4 pass. G-N5-TIME
stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Proposition LV-SHAPE | SIGN | — |
| §2 Corollary LV-CN | SIGN CONDITIONAL ON CN-LAST | CN-LAST is signed by both referees (P-N5-SCOPE §6; REFEREE-2 R2-N5-SCOPE 6d6e4bcf) and landing |
| §2 Corollary LV-COUNT | SIGN CONDITIONAL ON CN-LAST | — |
| §3 Lemma FLAT-ALL_{−1} | SIGN | N-LV-1 (citation): "(i) uses only FBL and H2" repeats the text that R31's signed fix FBW-1 corrected. A switched cycle node's new cycle avoids o by H1 at k + 1, not by H2. (h) at k + 1 is assumed, so nothing changes |
| §3 Lemma STRETCH_{−1} | SIGN | N-LV-2 (wording, = R31's FBW-2 / N-FBW-1 at level −1): stated "s ≤ k < e", but PL_{−1} (a) applies it to the run containing f_N, which can end at e = f_N when (h) fails at f_N + 1. The proof covers k = e within the stated bound n: events at k < e make ≤ n − 1 strict length moves, plus one event at e |
| §4 Theorem PL_{−1} (a)-(c) | SIGN | — |
| §4 Corollary LV-PL | SIGN (its last sentence CONDITIONAL ON CN-LAST, via LV-COUNT) | — |
| §5, addendum | not signed (as briefed) | — |
Reachability. In the batch the (LV) setting never occurs, as in the lane's data: every in-scope THR fallback has M ≥ 0. My climbs DO
reach it, but only with u* = none (r = −1): 173,371 in-scope THR fallbacks with r = −1 and M = −1. That is the packet's §5 OPEN class,
where the lane's DATA line reads "0 in scope". LV-SHAPE held at all 1,037,743 gates there. The r ≥ 0 part (FLAT-ALL_{−1}, PL_{−1}, LV-PL)
stays vacuous in all my data. Details in §5 (N-LV-3).
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 66,655 batch runs or in 850,608 climb runs (4 climbs).

## 1. LV-SHAPE: SIGN
Setting: in scope, THR, M_k = −1, so every gate has level −1 (gates are strict). s := σ_k(y).
- (F, F): Lemma G gives Ξ = W at s and z, so δ = ⊥ < −1 = ℓ. FBW (b) then makes y its own W- and Ξ-cycle node. (α) ✓
- (R̄, R̄): this case does not occur.
  - R-SAME (the same symmetric difference (π_z Δ π_s) ∩ V_{>c} for θ and w) makes the gate W-improving.
  - BL Step 2a needs no (P): it is FBW Step 2 with V := W_k, plus P-OPT. It makes y its own W-cycle node.
  - y is Even and its successor s is in R̄, so y ∈ R. A W-cycle through y would then pass o, against H2. ✓
- (F, R̄):
  - W(z) = π_z ⊕ w ⊵ π_z ⊕ θ = Ξ(z) ▷ Ξ(s) = W(s), using XW through (C7): π_z ⊆ R is disjoint from P(θ), P(w) ⊆ {o} ∪ F and from c ∈ F.
    So the gate is W-improving, and Step 2a applies.
  - If r ≥ 0: Ξ(s) ◁ π_z ⊕ θ ◁ π_z ⊕ w at levels −1 and r. (C6) twice gives lev(W s, W z) = r. The second use, r ≤ max(−1, lev(W s, W z)),
    gives the lower bound because r > −1. That contradicts Step 2a's −1, so r = −1.
  - W(z) has the cycle node c (H3), and W(s) has the cycle node y (y tops its W-cycle, which contains s). Level −1 equates them, so y = c.
  - y ∈ F, so y is its own Ξ-cycle node as well. (γ) ✓
- (R̄, F): y ∈ R.
  - Level −1 gives P(Ξ z) = P(π_s ⊕ θ) = (π_s ∩ V_{>c}) ⊔ P(θ) ⊆ F, so π_s ∩ V_{>c} = ∅ and o ∉ P(θ).
  - H1 makes o a non-cycle-node first vertex, so o ∉ P(θ) means rank o < rank c.
  - If r ≥ 0: Ξ z agrees with π_s ⊕ θ above −1, so lev(Ξ z, π_s ⊕ w) = r with the same verdict ((C6) twice). (β) ✓
- The cases are exclusive and exhaustive by the membership of s and z.

## 2. LV-CN and LV-COUNT: SIGN CONDITIONAL ON CN-LAST
- (α) and (γ) gates have λ(y) = y and level −1, and S4c is Even's. These are CN-LAST's hypotheses verbatim (P-N5-SCOPE §6), and its
  (i)-(iii) are LV-CN's conclusions. ✓
- LV-COUNT: an (LV) fallback with no (β) gate ends its phase (LV-CN (iii)), so there is at most one per phase. (β) requires
  rank o < rank c. ✓

## 3. FLAT-ALL_{−1} and STRETCH_{−1}: SIGN (N-LV-1, N-LV-2)
- FLAT-ALL_{−1}. P-N5-FBW §3's proof uses M ≥ 0 only to get "THR with u* ≠ none" from FBW-S, and here r_k ≥ 0 is assumed.
  - FBL (R20 (b)): only R → F and flat cycle-node switches.
  - (ii) uses OFF at M_k = −1; R25 (e) is stated for any M_k, and COARSE_{−1} is defined.
  - (iii): OFF, Lemma G, (C7), (ii).
  - (iv): TRANSFER for L = −1 < ∞.
  - (i): the new cycle of a switched cycle node avoids o by H1 at k + 1 (FBW-1), not by H2 (N-LV-1). ✓
- STRETCH_{−1}, step (1): COARSE_{−1}(b y) is constant on [s, e].
  - An unswitched y has b(y) = Ξ(σ y), and COARSE_{−1}(Ξ) is constant at every vertex.
  - A switch along a level-−1 gate keeps COARSE_{−1}(b y).
  - A switch along a level > −1 gate at a non-cycle-node y would change COARSE_{−1}(Ξ y) = COARSE_{−1}(y ⊕ b y), and is excluded.
    - (filled in) The (C4) map x ↦ COARSE_{−1}(y ⊕ x) is injective here, because y lies on neither successor's pre-c path. As in
      P-N5-ENT BF: a return to y before c would make c unreachable or put c before y.
  - At a cycle node, CN (R29 (d)) gives level −1. ✓
  - Then b(y) moves only in length, monotonically (R15 (a), (d)), and strictly at each level-−1 tail event (FB step (2): the best
    target, a gate target). With lengths in {0, …, n − 1}, there are ≤ n − 1 events at k < e and ≤ n with k = e (N-LV-2). ✓

## 4. PL_{−1} and LV-PL: SIGN
- The block is consecutive among S's fallbacks: a fallback between two block fallbacks has level −1 (CLS2) and r ≥ 0 (Fact R). r ≥ 0 on
  [f_1, f_N] by Fact R. So there is no straddling interval. ✓
- (a): FLAT-ALL_{−1} (iii) at each f_i, i < N ((h) at f_i + 1, since S continues).
  - The fallbacks joined by clean intervals form ≤ 1 + D_{−1} groups with COARSE_{−1}(Ξ) constant.
  - Each group gets n·n_E from STRETCH_{−1}; the last group needs k = e (N-LV-2). ✓
- (b): M_{f_i+1} ≤ −1 (FLAT-ALL_{−1} (iv)).
  - TRANSFER keeps M_t ≤ −1 until the first change j, so E_j ≤ −1 and j is S4a.
  - U-loc at L = −1 forces a relevant σ̄(o) change with O_j > −1.
  - OR (c) / TC-SPLIT give lev(θ) = O_j, and OR (a)-(b) with H1 give the absorption. ✓
- (c): (A_t) at L = −1 (OFFGATE at f_i + 1 with M_{f_i} = −1, then NL (iii), valid since r_t ≥ 0 > −1).
  - NL (ii): no exit leaves R at an S4a step.
  - Each dirty interval's first change absorbs an exit (N_x + 1). N_x drops only at block fallbacks, by REL_{−1} in total, and
    0 ≤ N_x ≤ d_o − 1 under H1.
  - So D_{−1} ≤ (d_o − 1) + REL_{−1}. ✓
- LV-PL: the block bound with REL_{−1} ≤ REL(S). The last sentence is LV-COUNT. ✓

## 5. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O library files × 3 traces × 3 starts = 2,655 runs, 50,667 states; random 𝒞^1O:
  64,000 runs, 156,294 states. 893 / 893 logs end "RESULT OK violations=0".
  - In-scope fallbacks (library): THR with r ≥ 0 and M ≥ 0: 1,300 / 1,065 / 1,305 (own / rand / spec), none with M = 0 or M = −1. EQ with
    M = −1: 0 / 0 / 35 (EQ is outside the (LV) setting). THR with r = −1: 0.
  - Random games: EQ with M = −1 50 (rand) and 311 (spec); THR with M ≥ 0: 2; THR with r = −1: 0.
  - So no (LV) state occurs in the batch, and every check there is vacuous. This agrees with the packet's §6.
- Climbs (run_climbs.sh, climb/, totals_climb.txt), four 1200 s climbs with FIT lv:
  - seeds: random n 8-14 and n 10-16, tev_cex_n40, zcl_fb2_n32; own and rand traces;
  - totals: 212,652 evaluations, 850,608 runs, 4,097,234 states, 0 violations.
  - The two random-seeded climbs reach the (LV) setting, always with u* = none: 173,371 in-scope THR fallbacks with r = −1 and M = −1.
  - LV-SHAPE checked at all 1,037,743 of their gates: (β) 1,037,532, (α) 209, (γ) 2. All held the stated properties, and no (R̄, R̄) gate
    occurred.
  - LV-COUNT held per phase. No (LV) state lacked a (β) gate, so LV-CN's case (all gates (α) / (γ)) did not occur.
  - FLAT-ALL_{−1} / PL_{−1} (r ≥ 0) cases: 0 in the climbs too.
- A small witness of the class (N-LV-3; DATA, my files): docs/referee-2/R2-N5-LV/climb/best_lv_9401.pg, sha1 4b74cd847dbdb51ed3025e8853ed7a106a8ce229.
  - n 11, o = 7 (rank 4), succ(o) = {2, 3}. SPEC trace (experiments/new/n5.py via re_check.n5_spec) from the S3 start: 5 iterations,
    1 fallback.
  - State 2 is an in-scope Even fallback with (h), θ = (5, ∅, 2) ◁ w = (5, ∅, 6) (THR, r = −1, a length-only trust gap), and M = −1.
  - Its 7 gates (6, 1), (6, 3), (9, 1), (9, 3), (10, 1), (10, 3), (10, 8) are all (β): R → F, with rank o 4 < rank c 8.
  - The fallback evicts all of R = {6, 9, 10}.
  - My own N5 (own and rand) gives the same state. Oink was not run on it; the claim is about the run's states, not its output.

## 6. Notes for the lane (none blocks a signature)
- N-LV-1: FLAT-ALL_{−1} (i): cite H1 at k + 1 (R31 FBW-1), not H2.
- N-LV-2: STRETCH_{−1}: state it for s ≤ k ≤ e (the proof covers it within n), as R31 did for STRETCH (FBW-2). PL_{−1} (a) uses k = e
  for a run that ends at its last fallback.
- N-LV-3 (DATA, for §5 and the RESULTS entry):
  - §5's "THR fallbacks with u* = none (r = −1) … DATA: 0 in scope" is no longer true: my climbs reach 173,371 of them, and
    best_lv_9401.pg has one on the SPEC trace from the canonical start.
  - They are exactly the fallbacks that PL_{−1} / LV-PL do not count (r ≥ 0 is required). They are therefore the live part of §5's OPEN
    item, and a concrete target for L-RED and L-SI: count (β)-fallbacks with r = −1 per scope run.
  - LV-SHAPE, which has no r ≥ 0 hypothesis, holds on all of them.

## §C. Comparison with REFEREE's R-N5-LV (written 2026-10-25 16:12Z by date -u, after my report b1038bea was pushed and merged)
Read: docs/referee/R-N5-LV.md on trunk (REFEREE successor 9, report 8054da2f).
- Verdicts are identical. Both sign LV-SHAPE, LV-CN, LV-COUNT, FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1} (a)-(c) and LV-PL, and neither signs
  §5 or the addendum.
  - REFEREE notes that CN-LAST is landed (RESULTS R38 (f)), so LV-CN / LV-COUNT are unconditional. I agree: CN-LAST's hypotheses are
    LV-CN's verbatim. My "CONDITIONAL ON CN-LAST" is discharged by R38.
- No gap in either report, so the joint gap map is empty.
- Notes map:
| REFEREE | REFEREE-2 | content | status |
| --- | --- | --- | --- |
| LV-N1 | (my status line on CN-LAST) | R-SAME / BL (R37) and CN-LAST (R38) are landed; §0 / §2 statuses stale | agreed |
| LV-N2 | N-LV-2 | STRETCH_{−1} must hold for k ≤ e; PL_{−1} (a) needs it for the run ending at f_N | same; agreed |
| LV-N3 | (in my §4: "the fallbacks joined by clean intervals form ≤ 1 + D_{−1} groups") | "[f_1, f_N] splits into at most 1 + D runs" is false when a dirty interval has several COARSE changes; read it as runs containing block fallbacks | ACCEPTED; I used the repaired form and should have flagged it |
| — | N-LV-1 | FLAT-ALL_{−1} (i) cites H2; R31's FBW-1 says H1 at k + 1 | mine only (citation); REFEREE checked the same proof step |
| — | N-LV-3 | the u* = none (LV) setting is reachable | mine only (DATA); see below |
- Data, the one real difference:
  - REFEREE's data and its three 20-minute climbs found 0 in-scope THR fallbacks with M = −1, and called the climb weak evidence.
  - My random-seeded climbs reached 173,371 such states, all with u* = none (r = −1). LV-SHAPE held at all 1,037,743 of their gates.
  - The witness best_lv_9401.pg (sha1 4b74cd84) was re-run by the Lead: one Odd choice vertex, n5 5 / 1, Oink zlk OK, strategies
    verified.
  - So the setting of §1-§2 is NOT vacuous for r = −1. The r ≥ 0 part (FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL) is vacuous in both
    referees' data.
- NL= (the addendum's CONJECTURE, not to sign) is now FALSE (L-RED nleq_cex_n48, sha1 e72e4034, Lead re-run). No signed item uses it:
  §1-§4 never cite NL at r_j = L. REFEREE checked this too.
- Joint state: all signable statements of P-N5-LV are signed by both referees (Opus 5.5, D15), unconditional after R38. No gap.
  Fixes-file lines for L-SI: LV-N1..N3, N-LV-1..N-LV-3.
