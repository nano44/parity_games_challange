# Referee report R-P6: per-context budget §22f and the Dom term §22j (GAP-A-M)

Referee: REFEREE (successor), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet 6: the Lead's message
of 12:54Z. Pin: trunk 8ff4085, docs/alg/GAP-A-M.md §22f (line 2049 ff.) and §22j (line 2213 ff.), with §22c, §22e, §22h
and §22i as context. Code: dtl.cpp @ 8fbf0a7 ("N" = that line). Written 13:10Z-13:40Z (date -u).
docs/referee-2/R2-P6.md was not read.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) §22f: per-context budget (F_R + 1)(H + 1); GAP-A ⇐ (CTX) ∧ (FALL) given STR-DET | SIGN WITH GAPS: G6-a1 (what F_R counts; closed by definition), G6-a2 (the implication needs the Dom term and +1; closed by §22h/§22j) | 66-101, 110-185, 198-202, 443, 644-776, 853, 954, 1035, 1068 |
| (b) §22j: per-input chain ≤ n; S − 1 ≤ Σ (F_R+1)(H+1) + n(\|C_T\| + \|C_Dom\|) + 1; GAP-A ⇐ (CTX⁺) ∧ (FALL) | SIGN WITH GAPS: G6-b1 (the Dom step is not Lemma 1.2's pattern; closed), G6-b2 (a Dom input is NOT fixed by (R, X); \|C_Dom\| counts inputs, not contexts; wording closed, substance OPEN inside (CTX⁺)) | 66-101, 110-185, 198-202, 862-890, 898-923, 935-951, 962-991 |
| (c) §22j: the raw per-input bound is vacuous (\|I_fd\| ≈ S − 1) | SIGN (stated as data, not used in any inequality; reproduced for spp_chain_up_n43) | n/a |

Answer to the Lead's question in (b): no. At a first difference the Dom step's input is fixed only by the whole prefix:
(X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j). Two things in it depend on T beyond (R, X): V* (bv's output at R) and the
earlier Dom steps' X-straddling acceptances. The per-input bound itself is sound, because it never needs the input to be
fixed by (R, X). What fails is the reading of |C_Dom| as a count of contexts.

## (a) §22f
A1. Π_R is a function of (R, p, T) (PROVED, re-checked).
- best_vertices (644-776) reads:
  - V only after clearing it (648, 662-667);
  - R, its locals Z, CurR, CurZ and prevV, and Candidates;
  - str only at 73, where the value decides a str write and nothing else;
  - Q, which every tattr drains, so it is empty on entry.
- The only side effect of a failing attractTangle is deleting a tangle that has a vertex outside the game (133-137). Such a
  tangle can never fire, because its vertices must lie in R ∪ Z ⊆ G'.
- The player is the same at every depth (853, 954). So the call at R has the same Π_R for any depth, any X and any
  position.
A2. T only grows along a phase. G' changes only at 1035 (dominion removal). Tangles are appended (443). tpr := −1 happens
only at 133-137, for tangles outside G'. So consecutive visits of R see T ⊆ T'.
A3. Descents happen only at dirty later visits (PROVED). For two visits under T ⊆ T', the first round's V is the same
(662-667: all p-vertices of R). PREFIX-MONO and (C1)-(C3) (signed, R-P4) then give Π_R(T) ≤ Π_R(T') whenever the later
call is step-ideal in every round.
A4. Counting.
- A transition s → s+1 whose e* lies in R's call is a pair of consecutive visits of R: FDL aligns both logs up to e*.
- Π_R's order is a strict lexicographic order: RV pointwise ↑, then Ψ ⊆ ↑, then Φ_top ↓. Any run of strict rises among
  visits, with equal steps in between, is a chain of length ≤ H − 1.
- Hence #(e*-transitions at R) ≤ (F_R + 1)(H − 1) + F_R ≤ (F_R + 1)(H + 1), PROVIDED F_R counts every e*-transition at R
  (and every visit pair) at which Π_R does not rise strictly.
G6-a1 (closed, definition). §22f calls F_R "the number of descents". Two more kinds of step must be counted:
- Incomparable steps: RV not pointwise comparable, or RV equal and Ψ incomparable.
- Π-blind e*-transitions: e* in R's call while Π_R stays equal.
  - e* in the threshold loop (727-731, one tattr per level) makes the component W_{r,t} strictly larger, so Π_R changes.
  - e* in a region tattr (692-702) may leave U_r equal. If the later call is dirty, (C4) is not available, and Φ_top, a
    sum, can stay equal while one vertex moves up and another moves down.
  - Such a transition is neither a rise nor a descent, so the count misses it.
- Fix: F_R := #(visit pairs of R at which Π_R neither stays equal nor rises strictly) + #(e*-transitions at R with
  Π_R equal). With this definition the bound is PROVED.
- On the data the two definitions agree: §22e's e*-table has "Ψ not monotone, or Π does not rise: 0", and §22f has
  "Ψ not monotone, or Φ_top rises: 0".
G6-a2 (closed by §22h/§22j). The sum over C_bv covers only e* in a best_vertices call. I re-listed every tattr site:
- Covered by C_bv: bv regions (700-701) and bv threshold loop (729-730).
- Covered by C_T: the −1 attractor (921-922).
  - Its seeds (898-912) are a function of (R, X) alone: the lowest priority level t at which some v ∈ R attracts to X.
    §22e's "determined by the identical preceding best_vertices call at R and by X" overstates this, harmlessly.
  - Z is empty at 898 (reset at 875 and 955; the Dom branch never writes it).
  - All seeds are pushed (909), so Lemma 1.2 applies, and the bound "≤ n per (R, X)" is sound.
- Never the first difference:
  - The vertex-only attractor at 947: its input is the −1 output and X, so it cannot be the first difference.
  - sptl (477-546): proved, R-P4.
  - The dominion extension (1036-1037): it runs after search_rec, only in a search that found a dominion.
- Dom (886-887, 973-974): needs (e* ∉ Dom) or §22j's n·|C_Dom|.
- The phase's last transition with no differing tattr needs the +1 (G-e2, signed R-P5 (d)).
- So §22f's display, S − 1 ≤ Σ (F_R + 1)(H + 1) + n·|C_T|, needs the Dom term and +1 before it implies GAP-A ⇐ (CTX) ∧
  (FALL). §22h (lines 2128, 2139) and §22j state both. The Lead's phrasing "given STR-DET" is right: STR-DET (c) is what makes s+1's
  tangle set at e* equal to T_{s+1}.
What is proved and what is data in (a):
- PROVED: the per-context budget (F_R + 1)(H + 1), with F_R as in G6-a1; descents (and incomparable steps) only at dirty
  later visits.
- DATA, not re-run by me (dtl_rootmono.py VISITS, 73 / 72 cases):
  - "Π_R descends only where RV falls": dirty visits never shrink Ψ with RV equal and never raise Φ_top.
  - "At most 2 descents per context per phase": the 2s are L-RED's f1_twodef_n48 / f1_twofall_n48, built to have two
    falls; elsewhere 1.
  - No structural bound on F_R exists. §18k found L-RED's "(F1) at most one fall per context" not structural.
- Inherited nit: H's factor (d + 2) counts the distinct threshold levels. The code loops t = 0..max_prio (721-722), but
  levels with no priority in (t′, t] repeat Cl_{t′}. Still polynomial.

## (b) §22j
G6-b1 (closed). The Dom step (878-890; 962-991) sets X[top], str[top] = −1, Q = {top}, and runs the tattr with:
- Z = X (all earlier removals of this search_rec call, plus the earlier Dom steps);
- R shrinking (885, 969), Gx = R, and maxpr = pr(top).

Only the top is pushed, not all of Z_0 = X. Lemma 1.2 (DTL-proof §1.2) is stated for Q = Z_0, so it does not apply
literally. The output is the closure triggered by the new part:
- Y is the least set containing the top and closed under (V) and (T);
- the successor or escape that triggers a rule must lie in Y, not merely in X (attractVertices scans ins(v) of popped v,
  66-101; attractTangles scans tin[v] = tangles with escape v, 198-202, 443);
- vertices and escapes in X count as attracted (Z[v], 137, 155) but never trigger.

Lemma 1.2's proof carries over unchanged: a premise becomes true only when its last relevant vertex enters Y, and that
vertex is popped later. Rule (T) for an old tangle has the same premise under T', so the output is monotone in T for a
fixed input (1.2b). An X-straddling acceptance at a fixed input is one more instance of rule (T), which is monotone too.
R-P5's G-a2 used the same closure.

Per-input chain (PROVED). Fix an input I. Take transitions s1 < s2 of one phase with e* of input I. Then
o(I, T_{s1+1}) ⊆ o(I, T_{s2}^{e*}) ⊊ o(I, T_{s2+1}):
- the outputs at e* in s+1 are o(I, T_{s+1}), since s+1 creates nothing before e* (STR-DET (c), R8);
- T_{s1+1} ⊆ T_{s2} ⊆ T_{s2}^{e*} ⊆ T_{s2+1} (A2);
- FDL gives the strict step.
So these outputs form a strictly increasing chain of subsets of G', each containing the seed, of length ≤ n. The
display S − 1 ≤ Σ_{R∈C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1 follows, with F_R as in G6-a1. It removes the
hypothesis (e* ∉ Dom), as §22j says.

G6-b2 (the Lead's question; wording closed, substance OPEN). A Dom step's input is not fixed by (R, X):
- The j-th step's input is (X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j).
- τ_j runs over V* \ X in index order (879, 963), and V* is the output of best_vertices at R, a function of T.
- Dom_{<j} contains the earlier steps' X-straddling acceptances, which depend on T.
- Data (p6probe.py, 138 instances in experiments/alg/instances): at a fixed (R, X, top), the Dom input varies within a
  phase in 105 / 2,110 phase-contexts (stable) and 111 / 2,166 (Oink), with up to 4 distinct inputs.
  - Example: spp_final_n20, stable order, priority-sorted indices, Even's first phase, R = G', X = ∅, top 1 (maxpr 2).
    The input is {1} in search 0 and {1, 9} in search 1.
- No monotone repair at fixed (R, X): the triggered closure is not monotone in its base. A tangle whose last escape
  moves from the new part into the base (absorbed by an earlier step) is never tried. So Dom_{≤j} at a fixed
  (R, X, V*) need not grow with T. This is the Dom analogue of a step deficit (reading, no instance sought).
- Consequence:
  - |C_Dom| is a count of INPUTS. (CTX⁺) as worded in §22j ("distinct first-difference contexts of ... Dom steps")
    should say "distinct first-difference inputs of Dom steps".
  - Its Dom part has the per-input character that (c) shows to be vacuous for the other tattr types. It is not implied
    by a bound on contexts.
  - For the −1 attractor, input = (R, X) context (above), so C_T really is a context count.
- On the data |C_Dom| = 0: no Dom e* in 578 (stable) and 609 (Oink) transitions of my probe. REFEREE-2's corpus
  (GAPS G-DOM) and §22j's cross unions agree.

## (c) §22j vacuity remark
§22j states "S − 1 ≤ n·|I_fd| + 1 ... valid but VACUOUS on the data: |I_fd| ≈ S − 1", with instances and a maximum
(0.95·|G'|). It uses this only to explain why the per-context Π_R is needed, never as a bound. SIGN.
- Reproduced with my own log (p6probe.py): spp_chain_up_n43's long phase has 41 distinct e* inputs in 41 transitions,
  |G'| = 43, in both orders.
- Corpus-wide, the longest per-input e* chain is 3, in both orders, so most inputs are first differences once.
- (b)'s Dom term stays in this per-input form (G6-b2).

## Independent probe (docs/referee/scratch/p6probe.py; subclasses experiments/alg/dtl_pyref.DTL)
It logs every tattr (caller, Z_in, R, Gx, maxpr, seeds) → output, drops sptl entries, and splits the run into phases
(same player and same G). Results on the 138 instances of experiments/alg/instances:

| check | stable | Oink |
|---|---|---|
| transitions | 578 | 609 |
| per-input output monotone along the phase (all tattr types, Dom included) | 0 failures | 0 failures |
| e*: input equal, output strictly larger | 0 failures | 0 failures |
| e* caller: best_vertices / −1 attractor / Dom | 555 / 23 / 0 | 586 / 23 / 0 |
| per-input e* chain strictly increasing, ≤ n (longest) | holds (3) | holds (3) |
| Dom input varies at fixed (R, X, top) | 105 / 2,110 | 111 / 2,166 |

## What remains OPEN for GAP-A after (a) and (b)
1. (CTX⁺): per phase, the number of distinct first-difference best_vertices contexts R, −1 attractor contexts (R, X),
   and Dom-step INPUTS is polynomial. DATA only.
   - The obstruction is §22f's P-piece level-set jump (spp_final_n20; I did not re-run it).
   - The SKETCH of §22g says each context has polynomially many successors, but the visited part of the context tree
     must be thin. That is the nested-counter core.
   - The Dom part is input-level (G6-b2) and is 0 on all data.
2. (FALL): F_R (G6-a1's definition) is polynomial for every R ∈ C_bv. DATA only: max 2, on instances built for it, with
   no structural reason.
3. Inherited conditions of the bound: phases ≤ D + 2 (signed); the bit cost is conditional on DTL-proof §3(e) (R-P4).
   GAP-C (completeness) is separate and open.
Everything else in the reduction is proved: Π_R as a function of T, PREFIX-MONO/POS-FALL/ROOT-BOUND, FDL, STR-DET,
e* ∉ sptl, the per-input chain, and the −1 attractor's per-(R, X) budget.
