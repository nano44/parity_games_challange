# R2-N5-ANCHOR: REFEREE-2 report on P-N5-ANCHOR (box 134): FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR, CIRC, FL-GCH, DEAD §6, ruling (R1)
Referee: REFEREE-2 successor 25 (session_01V5yGRaPp26T6iMUpCRmXsW), Opus 5.5 (D15). Written 2026-11-01 (date -u; see the commit).
Independence: written without opening docs/referee/ for this packet, and without reading the lane's box130-134 scripts.

## 0. Object
- docs/new/P-N5-ANCHOR-box134.md at claude/l-new f009a9a1: sha1 ad97ad88acb453579f9381bf71d211df4ef4fe3e, 162 lines. Re-hashed: match.
- Line: docs/new/P-N5-ANCHOR-line.txt, sha1 7f140d0c7711aa6c49c10d2d47ae9aaf707590bc. Re-hashed: match.
- Premises opened:
  - RESULTS R24 (a), (b) with the P-U1 packet §1-§2 and its fixes. My L44 check docs/referee-2/R2-R24-L44.md (d96d2f9e).
  - Lead reading L46 (docs/DECISIONS.md).
  - SPEC S1 (iv), S2, S4a/c, FIX 4. R57 / R102 (1E-N3, S4B-OPT).

## 1. Verdict table
| § | item | verdict |
| --- | --- | --- |
| §2 | Lemma FL-TIGHT | **SIGNED** |
| §2 | Lemma FL-OPT | **SIGNED** |
| §2 | Lemma bridge B | **SIGNED** |
| §3 | Lemma PREFIX (a)-(c) | **SIGNED** |
| §4 | Theorem FL-ANCHOR (i)-(iii) | **SIGNED**, with G-ANC-1 (a proof-text gap at the corner clause of [RULE], closed in §3 below by R24 (a)/(b) as signed; no new proof) |
| §5 | Lemma CIRC | **SIGNED** |
| §5 | Corollary FL-GCH (EQUIVALENCE) | **SIGNED** |
| §6 | DEAD «Ξ at ODIFF vertices is constant inside an FL run» | **SIGNED** (instance checks: all four pins re-run with my own code and Oink). The heading's «(or O(1))» is not killed by instances (N-ANC-1) |
| §1 | (R1) ruling | **(R1) HOLDS** as a consequence of the cited items; it is not an extra premise (§2 below) |

## 2. Ruling on (R1): the choice rule applies at non-movers
- (R1) holds. TB's proof steps 1 and 3-5 (R24 (b), as cited under L46) describe the output of ONE S1 call on dual(H_(j−1)) at EVERY vertex
  x of the call's region:
  - step 1: σ_j is that call's dual-Odd choice;
  - step 3: c's parity selects the longest-path or BFS mode;
  - step 4, with Lemma R: in longest-path mode the choice is the smallest index among the survivors of maximal length, which are exactly
    the fully optimal edges;
  - step 5, with Lemma R: in BFS mode the choice is the discoverer, i.e. the lex-least root-first key among the surviving shortest
    paths.
- None of these steps uses «v switched». The mover hypothesis enters TB only at step 2, which shows the OLD option σ_k(v) is optimal, and
  in the strictness «σ_(k+1) ≠ σ_k ⇒ strict decrease».
- So for every Even x that is not its own W′-cycle node, mover or not, σ_j(x) = the κ_j-least element of TIE_j(x).
- At an FL transition the packet needs only that, plus bridge B, which puts σ_(j−1)(x) in TIE_j(x). So (R1) is a consequence of the cited
  items, not a further premise.
- Data (my own code, every non-fallback S4a transition of the 813 distinct corpus pairs):
  - 729,730 non-mover and 42,644 mover checks;
  - 614 / 761 of them with ≥ 2 tied options;
  - 0 violations.
- The line should state the ruling, not «referees to rule» (ANCHOR-L1).

## 3. Review notes
- **[RULE] form.** TIE_j(x) := the FULLY W′-optimal options of x in H_(j−1), with W′ := W*_j, the arena optimum. This is the form my L44
  precision asked for («tied under W′, not under W_k»). ✓
  - At an FL transition W′ = W_j = W (FL-OPT), so TIE_j(x) = R_j(x) ∩ T_x, as §4 uses. ✓
- **G-ANC-1 (the corner clause; closed).** [RULE] (and L46) says «An option whose play passes x is a corner and lies outside the rule».
  §4 (i)'s Choice step nevertheless applies the rule to all of TIE_j(x) = R_j(x) ∩ T_x, which may contain such options. So, as written,
  the step needs the rule at corners too. It holds there:
  - Let y ∈ TIE_j(x) be fully W′-optimal: x ⊕ W′(y) = W′(x), lengths included.
  - y's path to c cannot contain x: then ℓ(y) ≥ ℓ(x) + 1, and x ⊕ W′(y) would have length ≥ ℓ(x) + 2.
  - So a fully optimal option can «pass x» only on the cycle part, after reaching c, which happens when x lies on c's cycle.
  - For such y, R24 (a) Lemma R in its signed fully-optimal form (fixes §1.1) keeps the edge x → y: its statement quantifies over all
    fully optimal y, and G-TB-1 case (b) / TB-1 treat exactly «x only on the cycle part».
  - The length step and the BFS run on paths to c, which avoid x. So TB steps 4-5 choose among all of TIE_j(x), corners included, and
    κ_j(y), y's path from c, does not involve x.
  - Hence «outside the rule» is vacuous on TIE: the rule covers every fully W′-optimal option.
  - Data: 18,102 rule checks with a corner option in TIE on the corpus (157 on the pins, 205 on random games), 0 violations.
  - Repair, wording only: drop the corner clause from [RULE] and from the line, or define a corner as «an option whose path to the cycle
    node passes x», which no fully optimal option has.
  - This uses R24 (a)/(b) as signed, so it is no new proof (L41 is not triggered). If the lane copies the argument above into the fixes
    file, it may cite this report.
  - Attribution note for the Lead: L46 credits the corner clause to a «REFEREE-2 precision note». My L44 note (d96d2f9e) asked only that
    «tied» mean «under W′» and that any hypothesis beyond «Even, switched, not its own W′-cycle node, W′(h) = W_k(h), no fallback» be
    named. The corner clause is not mine.
- **FL-TIGHT.**
  - For x ∉ CN, ℓ(x) > 0, so x is not its own cycle node, and W(x) = x ⊕ W(σ_j(x)) by the play / (V1).
  - For x ∈ CN, the play from σ_j(x) returns to x, so W(σ_j(x)) has cycle node x. ✓
- **FL-OPT.** σ_(j−1) ∈ H_(j−1) and its valuation is W_(j−1) = W_j = W*_j, the pointwise optimum's value. ✓
- **Bridge B.**
  - h ∉ CN, so W_j(h) = h ⊕ W_j(w) and W_(j−1)(h) = h ⊕ W_j(o), using W_(j−1) = W_j.
  - Both equal W*_j(h), and o, w ∈ R_j(h). ✓
- **PREFIX.**
  - (a) Odd vertices before A are not in ODIFF_j, so σ̄_j = τ_a there, and Even vertices follow σ_j in both plays. ✓
  - (b) Levels drop by one per W-step before the cycle node. ✓
  - (c) Ξ_j(y) is read from p_0 … and Ξ_j(A), with the two cases «w among p_i» and «w beyond A». ✓
- **FL-ANCHOR (i).** The induction is right:
  - ℓ = 1: T_x = {c}.
  - Values ξ(y) are constant: y ∈ T_x has level ℓ − 1 ≥ 1, so y ∉ CN. PREFIX applies with σ at levels ≤ ℓ − 1, constant by induction,
    and with τ_a, and with ODIFF / Ξ on ODIFF ∪ CN, which are gating data.
  - Keys κ are constant: y's play path to c has levels < ℓ − 1.
  - TIE_j(x) = ({z} ∪ {y ∈ T_x : ξ(y) ▷ ξ(z)}) ∩ T_x.
  - f_x is idempotent: ▷ is transitive, and κ is injective (an index, or a path ending in y).
  - At j = s0 + ℓ − 1 the gating state j − 1 = s0 + ℓ − 2 ≥ s0, since ℓ ≥ 2. ✓
- **(ii).**
  - After s0 + ℓ* − 1 all Even non-CN choices are fixed.
  - For y ∈ T_c (Odd or Even, any level), ξ(y) is constant by PREFIX: its prefix's Even vertices have level < ℓ(y) and are all non-CN,
    hence fixed. The case y = c is gating data.
  - A move of c is along Iσ, so ξ strictly ▷-increases on T_c. ✓
- **(iii).** ≤ ℓ* − 1 early transitions, then cycle-node moves only, and every FL transition changes σ. The 1 + GCH epochs are right. ✓
  - CAP ≤ n + m: ℓ* ≤ n − 1 and Σ(|T_c| − 1) ≤ m.
  - Precision: ℓ* := 1 if there is no Even vertex outside CN. The packet says so; the line omits it (P-ANC-2).
- **CIRC / FL-GCH.** GCH counts states in (a, b − 1], so GCH ≤ FL − 1. The finer bound is trivial (≤ one change per vertex per transition).
  Both directions of the equivalence are correct, and the circularity remark is right.
- **DEAD §6.**
  - The killed statement «constant» is an explicit bound (0 changes) and is killed by instances.
  - The heading's «(or O(1))» is asymptotic and cannot be killed by fixed pins (L43). The line correctly says only «constant»
    (N-ANC-1: drop «(or O(1))» from the packet's heading in the fixes).

## 4. Re-runs with my own code
- Tool docs/referee-2/R2-N5-ANCHOR/anchor_check.py, on my N5 loop with validated starts.
  - RULE: at every non-fallback S4a transition, every Even x not its own W′-cycle node; movers, non-movers and corners counted.
  - Per FL run: TIGHT, OPT, BRIDGE, ANCH_i (timing per level), ANCH_ii, ANCH_iii, CIRC, CAPNM.
- Pins (logs/pins.txt; files at l-new f009a9a1, sha1 prefixes re-hashed: all match the packet):

| pin | packet | mine |
| --- | --- | --- |
| odxi_n37 | FL run [1, 9]; Ξ at ODIFF gate 33 changes 5 times; 35: 34 → 33 at 5 → 6, W(35) unchanged | FL run [1, 9] (FL 8, CAP 9, GCH 5, 6 epochs); gate 33: 5 changes; σ(35) 34 → 33 at 5 → 6 with W(35) = (32, ∅, 2) at states 4-7 |
| odxi_min_n12 | 𝒞^1O, ODIFF 1, one FL transition, Ξ-change at ODIFF vertex 10 | one FL transition [0, 1], ODIFF {10}, 1 change at 10; Odd choice vertices = {10} (𝒞^1O) |
| odxi_lasso_n13 | one FL transition | one FL transition [0, 1]; Ξ-change at ODIFF vertex 10 |
| odxi_many_n32 | 3 FL runs, 8 transitions, 43 ODIFF Ξ-changes, 4 gating changes; §4 holds | runs [6, 9], [10, 13], [14, 16]: 3 + 3 + 2 = 8; ODIFF Ξ-changes 22 + 11 + 10 = 43; GCH 2 + 1 + 1 = 4; 0 violations |

- Oink 8fbf0a7 `--zlk -v` on all four (logs/oink_pins.txt): «verified», and the regions equal N5's.
- Corpus (DATA, not to sign): the 813 distinct (game, start) pairs of anc58/corpus_fixed.lst (logs/cfu_*.txt, logs/corpus_totals.txt).
  RESULT PASS, 0 violations.

| quantity (packet §7) | packet | mine |
| --- | --- | --- |
| FL runs / transitions / epochs | 20 / 42 / 23 | 20 / 42 / 23 |
| violations of §4 (i)-(iii) | 0 | 0 |
| gating changes | 3 (cw11_n24, cycle node only) | GCH 3 |
| ODIFF Ξ-changes over all run states | 2 | 2 with ODIFF read at the SOURCE state j − 1 (vertex 28, nep22f_n64 run [14, 15], with and without start); 13 with ODIFF at either state (N-ANC-2) |

## 5. Gap map and line items
| id | where | kind | status |
| --- | --- | --- | --- |
| G-ANC-1 | §1 [RULE] corner clause vs §4 (i) Choice | proof-text gap; closed by R24 (a)/(b) as signed (§3) | closed; wording repair in fixes |
| ANCHOR-L1 | line «(item (R1), referees to rule)» | **REQUIRED**: a landing line cannot leave a ruling open. Replace with the ruling, e.g. «(R1): the choice rule holds at every such vertex, movers and non-movers, by TB steps 1, 3-5 with Lemma R (both referees)» once REFEREE agrees | open (line) |
| ANCHOR-L2 | line [RULE] gloss | **REQUIRED** (with L1): the line never defines the tie set. Say «σ_j(x) is the κ-least FULLY W′-optimal option of x in the arena (W′ := the arena optimum)», with κ as in packet §1. Drop the corner clause or define it as in §3 | open (line) |
| P-ANC-2 | line ℓ* | add «(1 if none)» | optional |
| P-ANC-3 | line «own W-cycle node» | «own W′-cycle node» (equal on FL transitions, but the rule is stated with W′) | optional |
| N-ANC-1 | packet §6 heading «(or O(1))» | asymptotic, not killed by instances (L43); the line is already right | note |
| N-ANC-2 | packet §7 DATA «ODIFF Ξ-changes 2» | correct for ODIFF at the source state. Counting o ∈ ODIFF_j ∪ ODIFF_(j−1) gives 13: nep22f_n64 runs [14, 15] {20, 28, 35, 37} and [23, 24] {20, 37}, each twice (two starts), and nep13_n24 [15, 16] {8}. The convention should be stated; not to sign | note |

## 6. Line diff against TARGET.md's scope words
- «N5 on EVERY game». No count bounded. The tail reads «REDUCTIONS and an EQUIVALENCE only (neither FL nor GCH is bounded here; …; G-N5-TIME
  stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)». This is consistent with TARGET §2 and §4.
- The DEAD is at an explicit bound («constant») with named, hashed instances (L43). No asymptotic word.
- L46's citation form is used. L41: no referee-originated proof (G-ANC-1's closure is a reading of signed items).
- Binder: FL run, a, b, j, s0, x, h, y, c bound in their clauses. CN, T_x, T_c, ℓ*, ODIFF_j, gating data, epoch, GCH and CAP are
  defined. ℓ* needs «1 if none» (P-ANC-2).
- Verdict on the line: **REQUIRED** (ANCHOR-L1, ANCHOR-L2). Then a word-diff of the revision.

## DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-ANCHOR/anchor_check.py; logs/ (pins, Oink, corpus).
- FINDINGS:
  - Signed (Opus 5.5, D15): FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR (i)-(iii), CIRC, FL-GCH, and the §6 DEAD (instances). There is
    no open gap.
  - (R1) HOLDS as a consequence of TB steps 1, 3-5 with Lemma R; it is not an extra premise.
  - G-ANC-1: the rule also holds at «corner» options. A fully optimal option can pass x only on the cycle part, which Lemma R and TB
    cover. Closed, wording only.
  - Line ANCHOR-L1 and L2 are REQUIRED: state the (R1) ruling, and define the tie set as fully W′-optimal.
  - All pins and DATA reproduced. The «ODIFF Ξ-changes 2» count holds with ODIFF read at the source state; it is 13 with either state (N-ANC-2).
  - L46 misattributes the corner clause to me.
- NEEDS: Lead:
  - route ANCHOR-L1 and L2 (and the optional P-ANC-2/3, G-ANC-1's wording, N-ANC-1/2) to L-NEW;
  - correct the attribution in L46.
