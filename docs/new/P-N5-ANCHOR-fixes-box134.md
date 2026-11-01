# P-N5-ANCHOR fixes (append-only): repairs to the frozen packet docs/new/P-N5-ANCHOR-box134.md (sha1 ad97ad88acb453579f9381bf71d211df4ef4fe3e) and its line
L-NEW successor 46. The packet and docs/new/P-N5-ANCHOR-line.txt stay frozen. Each entry names the referee item, the packet place, the
replacement text and its reason. The corrected line is docs/new/P-N5-ANCHOR-line-L1.txt (line L-1).
Sources: REFEREE claude/referee 732198a9, docs/referee/R-N5-ANCHOR.md; REFEREE-2 claude/referee-2 b431ec81, docs/referee-2/R2-N5-ANCHOR.md
(both relayed by the Lead 17:38Z; every to-sign item SIGNED by both, (R1) RULED COVERED by both).

## Entry 1 (2026-11-01, after both reports)
### 1.1 ANC-1 (REFEREE) = G-ANC-1 (REFEREE-2): corner wording (REQUIRED)
- §1 [RULE], replace «An option whose play passes x is a corner and lies outside the rule.» by: «An option of x is a CORNER if x occurs on
  its play BEFORE that play's cycle node. Corners lie outside the rule. On fully W′-optimal options the clause is vacuous (REFEREE-2): a
  fully W′-optimal option y of x ∉ CN has W′(y) of length ℓ(x) − 1, while a play from y through x before the cycle node is at least 2
  longer. So TIE_j(x) is the set of ALL fully W′-optimal options of x.»
- Choice made: KEEP the before-cycle-node definition (not drop). It is the reading bridge B uses, and with it the vacuity remark makes
  TIE_j(x) = R_j(x) ∩ T_x exact.
- Why the full-lasso reading was wrong: x ∉ CN can lie on its own W-cycle (a cycle vertex other than the cycle node). Then σ_j(x)'s
  lasso passes x, and the clause would wrongly exclude exactly the option §4 (i) needs the rule for.
- §2 bridge B, replace «h ∉ CN, so h lies on neither play (V1).» by «h ∉ CN, so h occurs on neither play before its cycle node (V1);
  the values below are therefore h ⊕ (the option's value).»
- §4 proof of (i), «TIE_j(x) = R_j(x) ∩ T_x (bridge B and W′ = W)» now holds under the before-cycle-node reading of 1.1; no other change.
- L46 is amended the same way (Lead, DECISIONS 17:3xZ); this entry follows it.
### 1.2 ANC-L1 (REFEREE) = ANCHOR-L1 (REFEREE-2): the (R1) ruling in the line (REQUIRED)
- §1 (R1): it is RULED COVERED by both referees. (R1) holds as a consequence of R24 (a) Lemma R and R24 (b)'s choice rule (TB steps 1,
  3-5), with no extra premise. It is no longer an open item. Line L-1 states the ruling.
### 1.3 ANCHOR-L2 (REFEREE-2): ties in the line (REQUIRED)
- Line L-1 defines the tie-break as «the κ-least FULLY W′-optimal option, W′ := the arena optimum». The corner clause is in the
  before-cycle-node form, marked vacuous for fully W′-optimal options.
### 1.4 ANC-L2 (REFEREE): anchor of the cycle-node count in the line (REQUIRED)
- Line L-1: «at transitions j ≥ s0 + ℓ* each Even c ∈ CN moves at most #T_c − 1 times in the epoch» replaces «afterwards each Even c ∈ CN
  moves at most #T_c − 1 times». This matches §4 (ii).
### 1.5 OPTIONAL items taken
- ANC-P1 (REFEREE): §1 [1E-N3] needs RESULTS R57 only. FL keeps τ, so R102's S4B-OPT is not used. The premise list now reads «[1E-N3]
  (RESULTS R57)». Line L-1 cites R57 only.
- ANC-P2 (REFEREE): §5 Lemma CIRC's finer form ranges over transitions j = a + 1, …, b of the run. The count is #{j ∈ [a + 1, b] :
  Ξ_j(v) ≠ Ξ_(j−1)(v)}, summed over v ∈ ODIFF ∪ CN, where ODIFF is the union over the run's states a..b.
- REFEREE-2 wording:
  - ℓ* := 1 if no Even vertex lies outside CN (now also in line L-1).
  - In [RULE], «not its own W′-cycle node» replaces «not its own W-cycle node». They agree at FL transitions (W′ = W).
- N-ANC-2 (REFEREE-2): §7's ODIFF convention. «Ξ-changes at ODIFF vertices» counts vertices in ODIFF at the SOURCE state j − 1 (as in
  box 132's XIB and GCH): 2 in the corpus. Counting vertices in ODIFF at EITHER state j − 1 or j gives 13 (REFEREE-2's count, not re-run by me). Both conventions are stated.
- §6 heading (both referees, L43): «DEAD: «Ξ at ODIFF vertices is constant (or O(1)) inside an FL run»» is replaced by «DEAD: «Ξ at ODIFF
  vertices is constant inside an FL run»». An O(1) bound is not a statement an instance can kill. The instances refute constancy, and
  odxi_many_n32's 43 changes are DATA only. The line already says «constant».
