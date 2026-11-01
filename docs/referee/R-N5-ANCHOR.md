# R-N5-ANCHOR: REFEREE report on P-N5-ANCHOR (L-NEW box 134)
REFEREE successor 22, 2026-11-01T16:41Z by date -u (Opus 5.5, D15). Packet claude/l-new f009a9a1, docs/new/P-N5-ANCHOR-box134.md (sha1 ad97ad88…,
162 lines); line docs/new/P-N5-ANCHOR-line.txt (sha1 7f140d0c…). Written before reading docs/referee-2/ on this packet. Lead readings
applied: L41 (lane-authored proofs; nothing here is referee-originated), L43 (DEAD only at an explicit statement), L44 / L46 (R24's
class-free items), L45 (S4b; not used here).

## 0. Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | (R1): [RULE] at non-movers | **RULED: covered.** No separate premise (§1) |
| 1 | [RULE] citation vs my CF-1 | matches CF-1 verbatim ✓; reading of «corner» **REQUIRED ANC-1** (§1) |
| 2 | Lemma FL-TIGHT | **SIGNED** |
| 2 | Lemma FL-OPT | **SIGNED** |
| 2 | bridge B | **SIGNED** with ANC-1 (wording: «h occurs on neither play before its cycle node») |
| 3 | Lemma PREFIX | **SIGNED** |
| 4 | Theorem FL-ANCHOR (i)-(iii) | **SIGNED**, given ANC-1 |
| 5 | Lemma CIRC | **SIGNED** (precision ANC-P2: the range of j in the finer form) |
| 5 | Corollary FL-GCH (EQUIVALENCE) | **SIGNED** |
| 6 | DEAD «Ξ at ODIFF vertices is constant inside an FL run» | **SIGNED** (4 pins re-run by my engine, §6). Packet heading «(or O(1))»: L43 precision ANC-P3 |
| 7, 8 | DATA, READING | labelled as such ✓; not signed |
| — | RESULTS line | **REQUIRED ANC-L1** ((R1) wording) and **ANC-L2** («afterwards» unanchored) (§7) |

No gap in the mathematics.

## 1. Premises, [RULE], (R1), ANC-1
- [1E-N3]: the S4a form (σ_j is a pointwise optimum of H_(j−1)) is RESULTS R57's standing premise, which covers S4a. FL runs keep τ, so
  S4b (R102, L45) is never used. Citing it is harmless (optional precision ANC-P1: cite R57 only).
- [RULE] citation: «RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B …; its proof
  uses no 𝒞^1O hypothesis» is my CF-1 (R-R24-L44.md §3, 472f0dcd), word for word ✓. Bridge B is signed here (§2), as CF-1 required ✓.
- (R1), RULED **covered**. TB's steps 3-5 and Lemma R describe S1's length-step choice at every non-cycle-node vertex x of the region
  R_c: the first maximum in list order, or the BFS parent. TB's mover hypothesis (σ_{k+1}(v) ≠ σ_k(v)) is used only for the strict
  conclusion «and the two differ». For a non-mover the same steps give «σ_j(x) is the κ-least fully optimal option». The fully
  optimal options include σ_j(x) itself, by bridge B with w = o. So (R1) is no extra premise. It is the same citation.
  DATA: my tbcf_probe.py checks every Even x with ≥ 2 options, movers or not. Seed 2401: 2,135 non-movers among 7,947 checked; 0
  violations (§6).
- **ANC-1 (REQUIRED, wording; the ambiguity is in my own CF-1 words, which L46 repeats).**
  - The text has «An option whose play passes x is a corner and lies outside the rule» (packet §1, from CF-1 / L46).
  - Read with the FULL play (lasso), this excludes σ_j(x) itself whenever x ∉ CN lies on its own W-cycle: the play from σ_j(x) reaches c
    and then runs round the cycle through x.
  - Then σ_j(x) ∉ TIE_j(x), and the rule «σ_j(x) is the κ-least element of TIE_j(x)» fails at exactly the vertices §4 (i) needs. A
    cycle vertex x ≠ c has level ≥ 1.
  - The packet's own identity «TIE_j(x) = R_j(x) ∩ T_x» (§4 (i), Choice) holds only for the reading «x occurs on y's play BEFORE y's
    cycle node». With the formal ⊕, y ∈ T_x already excludes such y: if x precedes c on y's play, then ℓ(y) ≥ ℓ(x) + 1 and
    x ⊕ W(y) has the wrong length.
  - Bridge B's proof has the same slip: «h ∉ CN, so h lies on neither play (V1)». Correct: «h occurs on neither play before its cycle
    node», which is what (V1) needs.
  - Fix (packet fixes file, line unaffected): define a corner as «x occurs on y's play before y's cycle node». The Lead may wish to
    amend L46's precision note the same way.
  - With this reading the R24 citation covers cycle vertices. Lemma R and TB steps 4-5 assume only «x not its own cycle node».
  - DATA: my first L44 run (R-R24-L44 §4) had skipped these vertices as «corners» (1,371 + 1,393). Under the before-c reading
    (CORNER=pre), all 2,764 are tested: 0 violations (§6).

## 2. FL-TIGHT, FL-OPT, bridge B: SIGNED
- FL-TIGHT ✓. x ∉ CN: x is not its own cycle node, so (V1) gives W_j(x) = x ⊕ W_j(σ_j(x)) with W_j = W. x ∈ CN: σ_j(x)'s play returns
  to x, so its cycle node is x.
- FL-OPT ✓. σ_(j−1) ∈ H_(j−1), and its value W_(j−1) = W_j = W*_j, the pointwise optimum.
- Bridge B ✓, with ANC-1's wording. W_j(h) = h ⊕ W_j(w), and h ⊕ W_(j−1)(o) = h ⊕ W_j(o) because W_(j−1) = W_j. So both equal
  W*_j(h). o, w ∈ R_j(h), and TIE ⊆ T_h because W′ = W.

## 3. Lemma PREFIX: SIGNED
- A exists within ℓ(y) steps ✓.
- (a) ✓: the plays agree at Even vertices (σ_j), and at Odd vertices outside ODIFF_j (σ̄_j = τ_a).
- (b) ✓: the level drops by 1 per W-step before the cycle node.
- (c) ✓: I checked the case where A's Ξ-play re-enters the prefix. The cycle node w is then either some p_i (first case), or every
  re-entered p_i lies on the cycle below w and contributes nothing to the relevant set. In both cases F depends only on (p_0 … p_(k−1),
  Ξ_j(A)) and the fixed priorities. This uses SPEC's Ξ = the (σ, σ̄)-play value (R57 (a)/(b), 1E-N3).

## 4. Theorem FL-ANCHOR: SIGNED (given ANC-1)
- (i) ℓ = 1 ✓: T_x = {c}, because only c has level 0 and cycle node c.
- (i) ℓ ≥ 2 ✓:
  - y ∈ T_x has level ℓ − 1, so y ∉ CN.
  - ξ(y) = Ξ_(j−1)(y) is fixed by PREFIX. The prefix's Even vertices have level ≤ ℓ − 1 and are constant on [s0 + ℓ − 2, s1] by
    induction, with j − 1 ≥ s0 + ℓ − 2 ≥ s0. Its Odd vertices are not in ODIFF and follow τ_a. A and Ξ_(j−1)(A) are gating data at a
    gating state.
  - κ_j(y) uses σ_j on the same levels, with j ≥ s0 + ℓ − 2 ✓.
  - TIE = R_j ∩ T_x (ANC-1).
  - The idempotence argument is correct. ▷ is transitive. κ is injective: an index, or a root-first key of equal length ending in y.
- (ii) ✓. For j − 1 ≥ s0 + ℓ* − 1 every ξ(y), y ∈ T_c, is fixed (y = c is the only CN element of T_c). Moves of c form a strict
  ▷-chain in ξ(T_c). No rule at cycle nodes is used.
- (iii) ✓. ≤ ℓ* − 1 early transitions, then only cycle-node moves, so the epoch has ≤ CAP transitions. Epochs = 1 + GCH exactly.
  CAP ≤ (n − 2) + m ≤ n + m.

## 5. Lemma CIRC, Corollary FL-GCH: SIGNED
- GCH ≤ FL − 1 ✓ (j ranges over a < j ≤ b − 1).
- The finer form ✓, but trivially so: at most one change per vertex per transition. Precision ANC-P2 (optional): write the range «a < j
  ≤ b».
- Corollary ✓: GCH ≤ FL − 1 and FL ≤ (n + m)(1 + GCH). It is an EQUIVALENCE and bounds neither side. «circular» is correctly flagged.

## 6. DEAD pins and DATA (own engine; tools in docs/referee/scratch/)
- anchor_probe.py (own engine rl_engine, no lane code) re-runs each pin from its start file. It checks FL-TIGHT, PREFIX (a)/(b) at every
  y ∉ CN, (i) timing, (ii) CN moves, epoch ≤ CAP, run ≤ CAP(1 + GCH) and CIRC. Logs: anchor_logs/pin_*.txt.

| pin (sha1 = packet) | FL runs / transitions | my ODIFF Ξ-changes in run states | GCH | violations |
| --- | --- | --- | --- | --- |
| odxi_n37 (83f263c1…, start e2ed6715…) | 1 / 8, run [1, 9], CAP 9 | **5, all at gate 33** (states 2, 3, 5, 6, 7) | 5 | 0 |
| odxi_min_n12 (51661a75…, start 91ae8cad…) | 1 / 1 | 1 (vertex 10, at the run's last state) | 0 | 0 |
| odxi_lasso_n13 (5cf18798…, start c2a4e074…) | 1 / 1 | 1 (vertex 10) | 0 | 0 |
| odxi_many_n32 (42094483…, start c7565702…) | 3 / 8 | **22 + 11 + 10 = 43** | 2 + 1 + 1 = **4** | 0 |

- Release on odxi_n37 (anchor_logs/release_odxi_n37.txt): the Ξ(33) path-set weight rises between states 4 and 5, with the cycle node
  and the length unchanged.
  - At state 5, 33 is improving for 35 (Ξ_5(33) ▷ Ξ_5(34)); at state 4 it is not.
  - σ_6(35) = 33 (was 34). W(35) = (32, ∅, 2) is unchanged.
  - 33 is Odd, with σ̄(33) = 2 ≠ τ(33) = 32, so 33 ∈ ODIFF ✓.
- Oink 8fbf0a7 --zlk -v on all four pins: «verifying solution» completed, and my engine's final regions equal Oink's
  (anchor_logs/oink_regions.txt; all four games are won by Even everywhere). I did not re-run --tl or n5b; that is the lane's pin.
- [RULE] / (R1) DATA (tbcf_probe.py, CORNER=pre; random games with 2-5 Odd choice vertices, so none is in 𝒞^1O):
  - seed 2401: 3,000 games, 7,947 vertices checked, of which 2,135 are non-movers and 1,371 lie on their own cycle;
  - seed 2403: 3,000 games, 7,823 checked, of which 1,393 lie on their own cycle;
  - 0 violations; 41 even ties with κ-min ≠ index-min, all following κ (tbcf_logs/pre_*.txt).
- Packet §7 is labelled DATA, on the 813 distinct pairs (E-1) ✓. §8 is labelled READING ✓.
- ANC-P3 (precision, L43): the packet §6 heading kills «constant (or O(1))». A finite instance cannot kill «O(1)». The line correctly
  states only «constant». Drop «(or O(1))» in the fixes file, or label it DATA.

## 7. RESULTS line (7f140d0c)
- **ANC-L1 (REQUIRED).** «applied at every Even vertex that is not its own W-cycle node including non-movers (item (R1), referees to
  rule)». A landing line cannot defer a ruling. Replace «(item (R1), referees to rule)» with the ruling, e.g. «(non-movers included:
  the same TB steps 3-5 with Lemma R; REFEREE R-N5-ANCHOR §1 and REFEREE-2 …)».
- **ANC-L2 (REQUIRED).** «… moves only at transitions j with j − s0 ≤ ℓ(x) − 1, afterwards each Even c ∈ CN moves at most #T_c − 1
  times». «afterwards» has no anchor. Write «at transitions j ≥ s0 + ℓ*, each Even c ∈ CN moves at most #T_c − 1 times in the epoch».
- Optional: ANC-P1 (cite R57 only for the S4a premise); «Ξ_j» / «σ̄_j» could be glossed «(SPEC S1 at σ_j)»; «level» = ℓ.
- Otherwise ✓:
  - Definitions: FL run, ℓ, CN, T_x, T_c, ℓ*, ODIFF_j, gating data, epoch, GCH and CAP are bound.
  - The lemma clauses match §2-§5.
  - The DEAD is explicit, with numbers that equal mine (L43 ✓).
  - «REDUCTIONS and an EQUIVALENCE only (neither FL nor GCH is bounded here …); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
    TARGET.md claim» ✓. TARGET.md diff: no bound, no algorithm claim.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/anchor_probe.py, anchor_logs/; tbcf_probe.py CORNER=pre mode and non-mover counter, tbcf_logs/pre_*.txt.
- FINDINGS:
  1. Every to-sign item is SIGNED, with no gap: FL-TIGHT, FL-OPT, bridge B, PREFIX, FL-ANCHOR, CIRC, FL-GCH, and the DEAD.
  2. (R1) is ruled covered by the same R24 citation.
  3. ANC-1 (REQUIRED wording): «corner» must mean «x before y's cycle node». The full-play reading breaks the rule at vertices on their
     own W-cycle, which §4 needs. The ambiguity came from my CF-1; L46 repeats it.
  4. Line: REQUIRED ANC-L1 ((R1) ruling in place of «referees to rule») and ANC-L2 (anchor «afterwards»).
  5. All four DEAD pins are reproduced exactly by my engine (5 at gate 33; 43 ODIFF changes, GCH 4).
- NEEDS: Lead: ANC-1, ANC-L1, ANC-L2 to L-NEW 46 (fixes file + line L-1); consider amending L46's «passes h» to «… before its cycle
  node».
