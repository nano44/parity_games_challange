# Referee report R-P7: Lemmas EXACT and PREFIX-MONO-X, new steals (GAP-A-M §22r)

Referee: REFEREE (successor), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet 7: the Lead's message
of 15:00Z. Pin: trunk d461a76, docs/alg/GAP-A-M.md §22r (line 2458 ff.), with §22c, §22q and R-P4/R-P5 as context. Code:
dtl.cpp @ 8fbf0a7 ("N" = that line). fallv_viol_n28 read from claude/l-red fdef212 (not yet on trunk). Written from
15:01Z-15:05Z (date -u). docs/referee-2/R2-P7.md was not read.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) Lemma EXACT: region step = Cl_{pr τ}(P(τ⁺) ∪ {τ}; T \ E_τ) | SIGN WITH GAPS: G7-a1 (line cite 137 → 138-139; closed), G7-a2 (the "remaining instances" step written out; closed) | 66-101, 110-185, 198-202, 443, 689-706 |
| (b) Lemma PREFIX-MONO-X under (NS) | SIGN (the absorbed case closes with EXACT's closedness claim; it does not need τ processed in run 2) | as (a), plus 713-741 |
| (c) Corollary: a non-rise of Π_R needs a new steal; F_R ≤ #(new-steal visit pairs at R) | SIGN WITH GAPS: G7-c1 (covers G6-a1's Π-blind e* via POS-FALL with C4 from (NS); closed), G7-c2 (the bound is one-sided and loose: necessary, not sufficient; stated, not a defect) | 713-776 |
| (d) fallv_viol_n28 | AGREES with (c): both falls of the vertex are at new steals, both orders | probe |

## (a) Lemma EXACT
Setting (689-706): CurR := R once per round (690). For each top τ ∈ V \ Z in decreasing index: CurZ = {τ}, Q = {τ},
pop loop with CurR[v] := false (699), attractVertices / attractTangles with (R, Z, Gx) = (CurR, CurZ, CurR) and threshold
pr τ (700-701). So at τ, CurR = R \ P(τ⁺) minus the vertices already popped in τ's own region, and every vertex of
P(τ⁺) is outside both CurR and CurZ.
(⊆) The code applies only closure rules ((S0), signed R-P4), with premises in P(τ⁺) ∪ CurZ:
- p-vertex rule: edge into a popped vertex of CurZ (74, 88).
- Opponent rule (75-85): an escape is a successor in Gx = CurR outside CurZ (80). Successors in P(τ⁺) or outside R are
  never escapes. This is Cl's "all R-successors in the set" with P(τ⁺) in the set.
- Tangle rule (110-185): a vertex in CurZ is skipped (136-137); a vertex outside CurR ∪ CurZ rejects the tangle (138-139);
  that covers every vertex of P(τ⁺) and every vertex outside R. Escapes in CurZ pass (155); escapes in CurR do not (156);
  escapes in P(τ⁺) or outside R pass. Trigger: tin[v] = tangles with escape v (443), tried at v's pop (198-202).
- So a fired tangle has t ∩ P(τ⁺) = ∅, i.e. t ∈ T \ E_τ (t ⊆ P(τ⁺) is rejected too and would add nothing).
G7-a1 (closed): the rejection is at 138-139 ("not contained in Z+R"); 137 is the "already attracted" skip. §22q cites
138-139 correctly; §22r's "137" is a slip.
(⊇) Claim: P(τ⁺) is closed under the threshold-pr τ rules of T \ E_τ in R. Checked case by case, using O1 (every top
processed before τ has priority ≥ pr τ):
- p-vertex u ∉ P(τ⁺), pr u ≤ pr τ, edge to w ∈ P(τ⁺): at w's pop (region of τ_w, pr τ_w ≥ pr τ) u was in CurR, so it
  was attracted (74, 88). So u ∈ P(τ⁺): no such u.
- Opponent u ∉ P(τ⁺), pr u ≤ pr τ, ≥ 1 successor in P(τ⁺), all R-successors in P(τ⁺): at the pop of the LAST of them,
  every other R-successor is in an earlier region (outside CurR) or in CurZ, so no escape (80) and u is attracted.
- Tangle t ∈ T \ E_τ with t ∩ P(τ⁺) = ∅, all escapes in P(τ⁺) or outside R, ≥ 1 in P(τ⁺), new vertices of priority
  ≤ pr τ (all of t is new): at the pop of its last escape in P(τ⁺) (region of τ″, pr τ″ ≥ pr τ), every vertex of t is
  in CurR or CurZ (t misses P(τ⁺)), every other escape is popped earlier or outside R, and some vertex is new. So it
  fires (110-185), and t meets P(τ⁺): contradiction. A tangle with t ⊆ P(τ⁺) adds nothing.
G7-a2 (closed). §22r's last step ("the pop loop computes the closure of the remaining instances") is right, but it
should say why the triggered rules with a premise in P(τ⁺) and one in Z_τ are covered:
- p-vertex: its trigger edge goes into Z_τ (else the case above), tried at that pop.
- Opponent with ≥ 1 successor in Z_τ: tried at the pop of its last successor in Z_τ; its successors in P(τ⁺) are not
  escapes (80), so it is attracted iff Cl's premise holds.
- Tangle with ≥ 1 escape in Z_τ: tried at the pop of its last escape in Z_τ; escapes in P(τ⁺) pass (156 tests Gx = CurR).
- Tangle with every escape in P(τ⁺) ∪ (outside R): the closedness case.
So P(τ⁺) ∪ Z_τ is closed under the rules of T \ E_τ and contains the base: ⊇. With ⊆, EXACT holds.
DATA (p7probe.py, my own closure, not dtl_ideal.lfp): EXACT holds at every region step (0 failures in 233,399 stable /
244,057 Oink steps; table below).
Note the strength of EXACT: it holds at DIRTY steps too. Of the steps checked, a large share have a step deficit
(the plain closure over all of T differs), and EXACT still matches every one.

## (b) Lemma PREFIX-MONO-X
- Cl here is dtl_ideal's triggered closure: the trigger is ≥ 1 escape in the SET, base included (R-P4 R-a1). Every
  premise is positive in the set and in the tangle list ("new vertices ≤ q" weakens as the set grows). So Cl is monotone
  in its base and in its tangle set. (This is not the Dom-step closure of R-P6 G6-b1, which triggers only on the new part
  and is not monotone in its base. EXACT does not use that one.)
- (NS) gives T \ E_τ ⊆ T′ \ E′_τ: for t ∈ T \ E_τ, t ∈ T′, and t ∈ E′_τ would put t in E′_τ ∩ T ⊆ E_τ.
- τ not processed in run 1: P(τ) = P(τ⁺) ⊆ P′(τ⁺) ⊆ P′(τ). ✓.
- τ processed in both: EXACT twice and monotonicity. ✓.
- τ processed in run 1 only (τ ∈ P′(τ⁺)): the Lead asked whether this closes with EXACT. It does. EXACT's closedness claim
  for run 2 at index τ uses only O1 (all tops processed before τ in run 2 have priority ≥ pr τ) and the pops of run 2; it
  does NOT use that τ is processed in run 2. So P′(τ⁺) is closed under the threshold-pr τ rules of T′ \ E′_τ, with
  E′_τ from P′(τ⁺) as (NS) defines it. It contains P(τ⁺) ∪ {τ}. Hence Cl(P(τ⁺) ∪ {τ}; T \ E_τ) ⊆ Cl(P(τ⁺) ∪ {τ};
  T′ \ E′_τ) ⊆ P′(τ⁺) = P′(τ). ✓.
SIGN. Wording note on §22r's "PREFIX-MONO is the special case in which the later run is step-ideal": step-ideality does
not obviously imply (NS) as a hypothesis. What is true is that the same induction proves PREFIX-MONO with T′ in place of
T′ \ E′_τ, because a step-ideal run's prefixes are closed under all of T′. It is the same proof pattern, not a special
case of the hypothesis. Nothing depends on the remark.

## (c) Corollary
- Round induction (V_1 = V′_1, the p-vertices of R, 662-667). If (NS) holds at every processed step of round r of the
  earlier run, then U_r ⊆ U′_r (C1); the threshold loop (722-731) has Gx = R, no consumption, all of Z pushed, so
  W_{r,t} = Cl_t(U_r) over all of T (C2, signed) and W_{r,t} ⊆ W′_{r,t}; survivors V_{r+1} ⊆ V′_{r+1} (C3). If the
  later run stops first with "no candidates" (716, 765), its survivors are INF; if it stops with V′ = ∅ (768-771), then
  V_{r+1} = ∅ too. So RV does not fall and Ψ does not shrink; (C4) holds per round.
G7-c1 (closed). F_R in the sense of R-P6 G6-a1 also counts e*-at-R transitions with Π_R EQUAL. POS-FALL's proof
(signed, R-P4) uses step-ideality only through (C4) for the vertices other than the moved one. Under (NS), (C4) holds,
so Φ_top falls strictly there too. So a Π-blind e* also needs a new steal, and F_R (G6-a1) ≤ #(visit pairs at R with a
new steal) holds as stated.
G7-c2 (stated, not a defect). The corollary is necessary, not sufficient: L-ALG's own table has 661 / 624 new-steal pairs
WITHOUT a descent against 86 / 85 with one. A bound on new steals per context is a strictly stronger statement than
(FALL). If new steals per context are not polynomial, (FALL) could still hold.

## (d) fallv_viol_n28 (L-RED R32, claude/l-red fdef212, sha1 per R32 21b235f4...)
p7probe.py, both orders. Indices are pyref's priority-sorted ones; the vertex is the one with priority 27 (index 15 in
Oink order, 16 in stable; R32's "vertex 14" labelling differs). At the root context (R = G′, player 1's phase):
- rise, then fall 6 → 5 (Oink: search 3 → 4 in global numbering; R32's phase-local 1 → 2), then fall 5 → 4 (4 → 5).
  Matches R32: RV 4, 6, 5, 4, 4.
- Fall 1: new steals at round 3, at tops (Oink) 26, 25, 24, 20, 15, 14, 13 (tangle 2) and 7 (tangle 3).
- Fall 2: new steals at round 4, tops 26, 25, 24, 20, 15 (tangle 2), and round 5, tops 26, 25, 15, 14 (tangle 2).
- Stable order: the same pattern (tangle 2 at both falls, tangle 3 at fall 1).
- Over all 75 consecutive visit pairs of all contexts: 17 falls, all with a new steal; 58 pairs with neither. EXACT: 0
  failures in 2,156 (Oink) / 2,071 (stable) region steps, 506 of them with a step deficit.
So each fall is at a new steal, as (c) predicts. One more fact: the SAME stored tangle (2) is newly stolen at both
consecutive falls, at different rounds. So a potential of the form "each tangle is newly stolen at most once per
context" is false here; a per-(round, top, tangle) form is not refuted by this instance.

## Corpus data (p7probe.py, experiments/alg/instances, 138 files; a different corpus from L-ALG's 238-file set)
| check | stable | Oink |
|---|---|---|
| region steps checked against EXACT | 233,399 | 244,057 |
| of which with a step deficit (closure over all of T differs) | 9,672 | 10,354 |
| EXACT failures | 0 | 0 |
| consecutive visit pairs (all contexts, all phases) | 4,286 | 4,542 |
| RV falls, with a new steal | 20 | 20 |
| RV falls, no new steal | 0 | 0 |
| new steal, no RV fall | 259 | 313 |
| neither | 4,007 | 4,209 |
My probe detects a non-rise only through an RV fall (pointwise); Ψ-shrink and Φ_top non-rises are not separately
detected (L-ALG's data has none). New steals outnumber falls about 13:1 here (8:1 in L-ALG's table): G7-c2.

## What (FALL) reduces to after (a)-(c)
(NS-COUNT): for every context R ∈ C_bv, the number of consecutive-visit pairs of R within a phase at which some top τ
processed in the earlier visit's round r has a tangle of the earlier visit's T that the later visit's round-r prefix
P′_r(τ⁺) meets without containing, and that P_r(τ⁺) did not, is polynomial.
- GAP-A ⇐ (CTX⁺) ∧ (NS-COUNT), given STR-DET (R8) and the signed per-context budget (R9).
- (NS-COUNT) ⇒ (FALL), not conversely (G7-c2).
- DATA only. No potential is proposed; L-ALG notes that a count over (step, tangle) pairs is circular as it stands
  (stored tangles grow with S), and (d) shows a per-tangle count is false.
