# R-N5-GP: REFEREE report on packet P-N5-GP (L-SI box 31): Lemmas W-MON, XW, GP*; Corollaries GP, GP+, FW-R*
Referee: REFEREE (successor 18), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 2026-10-29 16:39Z by date -u). REFEREE-2 reviews in parallel.
- Object and pin: docs/si/P-N5-GP-box31.md at claude/l-si d072bb28, `git show d072bb28:<path> | sha1sum` = cd4866df18b55f44b3ef3d52de65943eeffe9140,
  177 lines: equal to the Lead's figures. Fixes go to docs/si/P-N5-GP-fixes-box31.md.
- Runs 2026-10-29T16:47Z-16:55Z; report written 16:56Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no REFEREE-2 GP file opened.
- Premises opened and read in context: SPEC S1-S5 (docs/new/N5-ssi-global.md @ 2a435f8f4, l. 26-61); RESULTS R15 (d), R17 (a)-(e); R17's object
  docs/new/N5-phase-bound-box10.md @ 2a435f8f4 §1-§2 (l. 10-55: H, prefix, (F1)/(F2), (V1)/(V2), Lemma P with Cases A, B1 (both sub-cases), B2).
- Scope (D1): a REDUCTION per frozen W-phase (R*_T not bounded). Not a bound on the run, not a TARGET.md claim; FW-BF and G-N5-TIME stay OPEN.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | setting, [FRZ], [H], symbols | CHECKED |
| §2 | Lemma W-MON | SIGNED (premise: S1's procedure returns an optimal strategy of the one-player arena, GP-N1) |
| §2 | Lemma XW | SIGNED (premise: σ̄_t is an optimal counterstrategy at every vertex at once, GP-N1) |
| §3 | Lemma GP* | SIGNED. Every R17 (b) sub-case is redone without the improvement (§2 below) |
| §3a | Corollary GP | SIGNED |
| §3a | Corollary GP+ | SIGNED |
| §4 | Corollary FW-R* | SIGNED |
| — | Approved RESULTS line (16:26Z) | DOES NOT MATCH as worded: it drops two hypotheses of GP* (path length L ≤ k − a; Odd steps follow τ). Without either, the GP* clause is FALSE (instances below). E-ITEM GP-E1 |
| §5, §6 | READING, DATA | not signed; pinned checks reproduced EXACTLY (§5) |
No gap in the packet. One E-item, on the RESULTS line only (GP-E1). Notes GP-N1..N5.

## 1. W-MON and XW
- W-MON ✓. Inside a phase τ is constant; [STEP] makes the transition change σ; not a fallback, so σ_{t+1} = S4a's σ_new with Iσ_t ≠ ∅. S4a's σ_new
  is S1's Odd-optimal counterstrategy in the dual of the one-player arena H_t, i.e. (order reversal on G^d, all valuations) Even's optimum of
  H_t. Plays of G and of H_t coincide for strategies inside H_t (ρ_t and ρ_{t+1}). [F1] in H_t: W_{t+1} ⊵ W_t pointwise. The step "S1's output is
  an optimum of H_t" is the same premise R17 (e) uses («N5's step for the other player is switch-best»), here for the one-player ARENA H_t:
  GP-N1.
- XW ✓. Ξ_t is the value against σ̄_t, which minimises at every vertex at once [S1-Xi]; τ_t is one Odd strategy, so Ξ_t ⊴ W_t. Plays that avoid
  D_t are the same under τ_t and σ̄_t. Uses that S1's σ̄ is optimal (R57 (b)'s standing premise; GP-N1).

## 2. Lemma GP*: each sub-case against R17's source proof (box10 l. 29-55)
- Definitions ✓: BLOCKED at t ∈ [a, b); UNBLOCKED at k: simple, u a cycle node of state a, L ≤ k − a, Even edge i not blocked at k − 1 − i
  (k − 1 − i ≥ k − L ≥ a, so every state named lies in [a, b)). Paths are paths of G_τ (Odd steps follow τ).
- Base and the L = 0 step ✓ (λ_W constant on F). Induction set-up ✓: r′ = r[1..] is unblocked at k (its edge j is r's edge j + 1, checked at
  (k + 1) − 1 − (j + 1) = k − 1 − j) and avoids x; IH W_k(z) ⊵ value(r′); W-MON gives W_{k+1} ⊵ W_k (k → k + 1 lies in F).
- Case A ✓ = R17's Case A verbatim with Ω := W. Its hypothesis W_k(z) ⊴ W_k(ρ_k(x)) holds for x Odd (z = τ(x) = ρ_k(x) in G_τ), z = ρ_k(x),
  or (x, z) ∉ Iσ_k and not blocked (⊴ is total). A1 uses [V1], [V2] (r′ avoids x; ρ_k(x)'s path avoids x) and W-MON in place of (F2); A2 uses
  only cycle-node rewards. ✓
- Case B: x Even, (x, z) ∈ Iσ_k (Ξ-improving; W_k(z) vs W_k(ρ_k x) is UNKNOWN). ρ̂ ∈ H_k and W-MON's first part + [F1] give W_{k+1}(x) ⊵ val_ρ̂(x). ✓
  | sub-case | R17 (box10) | GP* | check |
  | --- | --- | --- | --- |
  | B1: x ∉ π, x not on c's cycle | val_ρ̂ = x ⊕ Ω(z) ⪰ x ⊕ value(r′) by (V2); improvement unused | identical | ✓ (R17 already did not use the improvement here) |
  | B1′: x ∉ π, x on c's cycle | improvement ⇒ P(π) top EVEN (phase ends) or P(π) = ∅, c odd, longer (x ⊕ Ω(z) ⪰ value(r)) | (i) P(π) = ∅, ANY parity of c: val_ρ̂ = (c, ∅, |π| + 1) = x ⊕ W_k(z) ⊵ value(r); (ii) top even: λ_W(x) changes, impossible; (iii) NEW, top odd: W_k(z) below every (c, ∅, ·), so value(r′) ⊴ W_k(z) gives value(r) ◁ (c, ∅, ℓ_x) = W_k(x) | ✓ all three. (iii): if u = c, weight(P(r′)) ≤ weight(P(π)) < 0 and x (less relevant than c) is not added, so value(r) ◁ W_k(x); if u ≠ c, reward(u) < reward(c). (i) holds for c even too: the arc vertices and x are less relevant than c, so top(Z) = c |
  | B2: x ∈ π, x = c | reached via D = ∅ and top(Z) = c; then IH forces x better than u | B2a: directly: u ≠ x, value(r′) ⊴ W_k(z) (cycle node x) ⇒ reward(u) < reward(x) ⇒ value(r) ◁ (x, ∅, 0) | ✓ (same argument, no improvement needed) |
  | B2: x ∈ π, x ≠ c | improvement ⇒ D top EVEN or (D = ∅, c odd): both end the phase | B2b: D′ = the same D. (i) top even: phase (λ_W) ends, impossible; (ii) NEW, top odd: W_k(z) ◁ W_k(ρ_k x); (iii) D′ = ∅: c odd ⇒ λ_W ends (every less relevant vertex has a better reward than an odd c); NEW, c even ⇒ same P, longer path ⇒ W_k(z) ◁ W_k(ρ_k x). In (ii), (iii)-even: Case A1's argument | ✓ D′ is the symmetric difference (W_k(z) = π[z..x) ⊕ W_k(x), W_k(x) = x ⊕ W_k(ρ_k x), disjoint parts, c ∉ Z). A1 needs only value(r′) ⊴ W_k(ρ_k x), [V1], [V2], W-MON, not (x, z) ∉ Iσ |
  The NEW sub-cases are exactly the ones R17 excluded by improvement; each is closed either by a frozen-phase contradiction (λ_W constant) or by
  reduction to Case A1. Case split exhaustive (x ∈ π or not; if not, on c's cycle or not; x = c only when x ∈ π). ✓
- What GP* uses of F: τ constant, no S4c transition, λ_W constant (λ_Ξ and σ̄ constant are not used by GP*; they enter only GP / GP+ via XW and D).

## 3. Corollaries GP, GP+ and FW-R*
- GP ✓: σ's choice and Iσ edges are never blocked by definition; an edge into U_t outside Iσ_t: W_t(z) = Ξ_t(z) (XW, second part) ⊴ Ξ_t(ρ_t x)
  ([S2]) ⊴ W_t(ρ_t x) (XW): not blocked. So timely ⇒ unblocked, and GP* applies.
- GP+ ✓: x, z ∈ S_{d,t} with d same-pair and tail-disjoint: ρ_t(x) ∈ S_{d,t} (x Even, d Odd); p(y) avoids D, so it is also the (ρ_t, σ̄)-prefix;
  W_t(y) = p(y) ⊕ W_t(d), Ξ_t(y) = p(y) ⊕ Ξ_t(d) with the same cycle node c. For values A with cycle node c avoiding p and q, p ⊕ A vs q ⊕ A is
  weight(P_A) + weight(P_p) vs weight(P_A) + weight(P_q) (disjoint, additive), then ℓ_A + |p| vs ℓ_A + |q| with c's direction: independent of A.
  So the Ξ comparison (not improving) transfers to W: not blocked. ✓ (Ξ as a play value of (ρ_t, σ̄): GP-N1.)
- FW-R* ✓: k < a + n − 1 gives ≤ n − 1 transitions. For k ≥ a + n − 1 with W_{k+1}(x) ≠ W_k(x): π = ρ_{k+1}-play to u = λ_W(x) (a cycle node of
  state a, λ_W constant), simple, L ≤ n − 1 ≤ k − a, value(π) = W_{k+1}(x). Unblocked would give W_k(x) ⊵ W_{k+1}(x) ⊵ W_k(x), equality
  (distinct values are distinct): contradiction. So some Even y_i has (y_i, y_{i+1}) blocked at t = k − 1 − i ∈ [a, k − 1]; S4a keeps
  ρ_{t+1}(y_i) ∈ {ρ_t(y_i)} ∪ Iσ_t(y_i) (no fallback), so ρ_{t+1}(y_i) ≠ y_{i+1} = ρ_{k+1}(y_i): a late adoption at some τ′ with t < τ′ ≤ k,
  k − τ′ ≤ i ≤ n − 2. Each τ′ is charged by ≤ n − 1 values of k. WCH ≤ (n − 1) + (n − 1)R*_T. ✓

## 4. The approved RESULTS line (16:26Z) against the signed content: E-ITEM GP-E1
The line reads «(Lemma GP*) W_k(x) ⊵ value(r) for every simple path r from x to a cycle node of F's first state none of whose Even edges
(r_i, r_{i+1}) was BLOCKED at state k−1−i». Against §3's definition of UNBLOCKED AT STATE k it omits two hypotheses:
- (1) L ≤ k − a (the path has at most as many edges as F has steps up to k). Without it the clause is FALSE: at k = a it would say W_a(x) ⊵
  value(r) for every path (no blocked-condition applies before a), i.e. W already optimal at the phase start. My control with this hypothesis
  dropped (MUT=1): 27,724 violations on 2,000 random runs, first instance rand0 (gp_probe.py rand 1000 5 12 7), frozen phase [0, 0], k = 0,
  x = 0, path [0, 1, 7].
- (2) r is a path of G_τ (Odd vertices step to τ(r_i)). Without it the clause is FALSE (an Odd vertex's W follows τ, not a better successor):
  MUT=2: 93 violations, first instance rand8, frozen phase [2, 3], k = 3, x = 2, path [2, 4] (2 Odd, 4 ≠ τ(2)).
- The FW-R* half of the line is exact. The scope tail ("a REDUCTION …; per frozen W-phase only, not a bound on the run") is right.
- Fix (wording, both in the line): «for every simple path r of G_τ (Odd steps follow τ) with at most k − a edges from x to a cycle node of F's
  first state, none of whose …». With it the line matches §3 exactly.

## 5. Re-runs and own control
- Pinned, from a clean worktree at d072bb28 (core/gp.py sha1 270f247c…, rund/quotecheck.py 29bb4a97…, read first), check.sh l. 699-710 run
  alone: «si (box 31 §6: GP*, FW-R* on rlin_cex_n40 and ccl_w48_n48; MUT=all control fails): PASS» and «si (box 31 packet P-N5-GP: 14 quotes
  exact; shifted control fails): PASS», exit 0 (the D1 tuples for rlin_cex_n40 and ccl_w48_n48, GP/RED/RLIN PASS, MUT=all GP FAIL, quotes=14
  bad=0, --mut QUOTES FAIL all asserted).
- Own control: scratch/gp_probe.py (sha1 b4142cc7…) on my engine rl_engine (no lane code). Frozen W-phases from the definition; W-MON at every
  in-phase transition; XW (both parts) at every state; GP*: for every k ∈ F and every x, a DFS over the simple G_τ paths with L ≤ k − a that
  avoid blocked edges (budget CAP per (F, k), counted when hit); FW-R*: WCH and R*_T per frozen W-phase.
  | corpus (gp_logs/) | runs | frozen W-phases (D ≠ ∅) | GP* path checks | W-MON / XW checks | max R*_T / WCH | violations |
  | --- | --- | --- | --- | --- | --- | --- |
  | pins: ccl_w48_n48, rlin_cex_n40 (+ start), runfam_K100 (+ start) (pins) | 5 | 71 (67) | 100,483 | 78,030 / 83,459 | 1 / 123 | 0 |
  | library (rho_probe.lib(), n ≤ 40; given + S3 starts) (lib) | 321 | 3,434 (2,804) | 332,322 | 78,720 / 173,927 | 2 / 36 | 0 |
  | random rand_ck n 5-14, 3,000 games, S3 + 1 random (rand3000) | 6,000 | 14,852 (6,588) | 33,388 | 9,585 / 154,935 | 0 / 3 | 0 |
  No frozen W-phase in my data has WCH > n − 1. The DFS budget was hit at many (F, k) on the pins (n 40-138) and at some on the library: there
  the GP* check covers only the enumerated paths (GP-N4).
- Controls (each drops one hypothesis of the path family; all BITE): MUT=1 (no L ≤ k − a) 27,724; MUT=2 (Odd steps off τ) 93 (both random
  n 5-12, 2,000 runs); MUT=3 (blocked edges allowed = the plain W-frame Lemma P) 756 on ccl_w48_n48, at the frozen phase [15, 18] (k = 18), the
  same phase as the lane's pinned D1 tuple (…, 15, 18). So each of GP*'s three path conditions is needed.

## 6. Notes (for L-SI's fixes file)
- GP-E1 (E-item, RESULTS line): add "of G_τ (Odd steps follow τ)" and "with at most k − a edges" (§4).
- GP-N1 (standing premise). W-MON uses that S4a's S1 output is an optimum of the one-player arena H_t (as R17 (e)); XW and GP+ use that σ̄_t is
  optimal at every vertex and realises Ξ_t as play values (R57 (b): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance»). Name them under §1's premises. My data: W-MON and XW 0 violations.
- GP-N2 (scope of GP*). GP*'s proof uses only: τ constant, no S4c transition, λ_W constant on [a, k]. λ_Ξ and σ̄ constant are not used (they
  matter for GP / GP+ through D). Worth one sentence: GP* holds on every maximal stretch with those three properties.
- GP-N3 (notation). §4 uses τ for a transition index ("transition τ → τ + 1"), clashing with Odd's strategy τ in the same sentence. Rename (e.g. s).
- GP-N4 (DATA scope). Path enumeration is capped in my control and, by its nature, in core/gp.py; on large n the GP* data cover a subset of the
  unblocked paths. FW-R*'s data (WCH, R*_T) are complete.
- GP-N5 (B1′ (i)). The packet's (i) covers c of either parity (R17 had it only for c odd, as improvement forced it). Correct: x and the arc
  vertices are less relevant than c, so top(Z) = c whatever c's parity.

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/gp_probe.py, gp_inputs/ (copies from l-si d072bb28), gp_logs/ (run_all.sh, pins, mut3_pins, lib, rand3000, mut1,
  mut2); pinned check.sh blocks re-run exactly.
- FINDINGS: W-MON, XW, GP*, GP, GP+, FW-R* all SIGNED, no gap; GP* redoes R17 (b)'s Case B sub-cases correctly without the improvement (three
  new sub-cases, each closed by λ_W constancy or reduction to A1). E-ITEM GP-E1: the approved RESULTS line drops "L ≤ k − a" and "Odd steps
  follow τ"; as worded its GP* clause is false (rand0, rand8 above).
- NEEDS: Lead: fix the RESULTS line (GP-E1) before landing; the GP §C word when REFEREE-2 reports; route GP-N1..N5 to L-SI.
