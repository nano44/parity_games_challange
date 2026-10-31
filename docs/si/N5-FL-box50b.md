# N5-FL (box 50b): FL_F, the W-flat transitions of a W-run. Z can only shrink there (Lemma FLAT-Z); every flat transition is Ξ-flat or carries a tied Ξ-climb (Lemma FLAT-TXC). In all data every flat transition keeps Z fixed: the core of FL-POLY is the same GXC / gate object as R92
L-SI successor 32 (Opus 5.5), D15 / D17 / D18, Lead reading L40. Lead 2026-10-30 13:09Z: «YOUR BOX 50 is FL-POLY: FL_F … ≤ p(n) on every
W-run of plain N5 … (1) State FL_F exactly as box 85 and R89 use it. Measure it on box 85's corpus … (2) Prove a polynomial bound, or give
the exact obstruction plus an instance.» (Numbered 50b to avoid a clash with box 50 = N5-ADD.) Working note, unrefereed, not a TARGET.md
claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tools: experiments/si/fl/flat.py (mine); fl/xirise_lnew_893b9346.py (read-only copy of L-NEW's box 85 xirise.py, for the definition);
  fl/run.sh. Outputs fl/flat_sbcg.txt (719), fl/flat_alt.txt (413). Pins: si/check.sh «box 50b».

## 1. FL_F, exactly
- R89 STRETCH-RED: FL_S := «transitions with σ_{t+1} ≠ σ_t and W_{t+1} = W_t». Box 85 / xirise.py read it on a W-run F (RESULTS R89):
  FL_F := the transitions t → t + 1 of F with W_{t+1} = W_t. Every transition of a W-run moves σ, so the two agree. NOTE: FL is NOT a
  fallback count. W-runs contain no S4c fallback by definition; FL counts W-FLAT S4a steps (the TIE residual of box 85 §4).
- flat.py reproduces xirise's FL: u23sw64_n32 FL 8 (xirise «'fl': 8»).

## 2. Lemma FLAT-Z (PROVED, lane) and Corollary FL-GAP
- Setting: a W-run F = [a, b], Z_t := {v : Ξ_t(v) ≠ W_t(v)} (RESULTS R91).
- (i) At every transition t → t + 1 of F, a vertex v ∈ Z_{t+1} ∖ Z_t has W_{t+1}(v) ≠ W_t(v).
- (ii) At every W-flat transition of F, Z_{t+1} ⊆ Z_t.
- Proof. If W_{t+1}(v) = W_t(v) and v ∉ Z_t, then Ξ_{t+1}(v) ⊵ Ξ_t(v) (RESULTS R15 (a), (d)) = W_t(v) = W_{t+1}(v) ⊵ Ξ_{t+1}(v) (XW,
  R88 / R57 (a)). So Ξ_{t+1}(v) = W_{t+1}(v), i.e. v ∉ Z_{t+1}. This gives (i). (ii) is (i) at a transition where no W changes. □
  (This is R91's REOPEN-W without the phase hypothesis.)
- Corollary FL-GAP (PROVED, lane). With ZFL_F := the W-flat transitions of F with Z_{t+1} = Z_t:
  FL_F ≤ |Z_a| + Σ_v WCH_F(v) + ZFL_F ≤ n + n(n − 1)(R*_F + 1) + ZFL_F.
  - Proof. A W-flat transition with Z_{t+1} ≠ Z_t removes at least one vertex from Z, by (ii). Removals ≤ |Z_a| + entries, and entries
    ≤ Σ_v WCH_F(v), by (i).
  - Σ_v WCH_F(v) ≤ n·WCH_F ≤ n(n − 1)(R*_F + 1), by R88 FW-R* on F (R89 GP*-RUN). □
- So FL-POLY ⇐ R*-POLY ∧ ZFL-POLY, and with box 85's FREE-RED: R3-POLY ⇐ R*-POLY ∧ ZFL-POLY.

## 3. Lemma FLAT-TXC (PROVED, lane): what happens at a flat transition
- At a W-flat transition t of F, exactly one of the following holds:
  - (a) Ξ_{t+1} = Ξ_t. By R15 (b), every switch is then a length-only switch at a Ξ-cycle node.
  - (b) Some u has Ξ_{t+1}(u) ≠ Ξ_t(u). Then Ξ_{t+1}(u) ▷ Ξ_t(u) (R15 (a); distinct values are distinct, R84 (a)) and W_{t+1}(u) = W_t(u),
    so (u, t) is a TXC event of RESULTS R92, and u ∈ Z_t.
- Proof: the definitions, with XW. □
- With R92's TXC-RED: FL_F ≤ XFL_F + |TXC_F| ≤ XFL_F + n(|GXC_F| + |GATE_F| + |CNW_F|) + n²·LCT_F, where XFL_F := the W-flat and Ξ-flat
  transitions of F.
- READING: the switching vertex v of a flat transition, when it climbs (case (b) at v), is a GXC event verbatim whenever λ_Ξ is fixed:
  v Even, switched, v ∈ Z_t, Ξ climbs, W(v) fixed.

## 4. DATA (flat.py; box 83 / 85 corpus: 719 sbcg + 413 alt = 1,132 runs; maxima per W-run, summed over games)
| count | value | instance of the max |
| --- | --- | --- |
| FL (sum of per-game maxima) / max per W-run | 61 / 8 | u23sw64_n32 (𝒞^1O, hill-climbed) |
| ZFL (flat transitions with Z unchanged) | 61 / 8 | the same: every flat transition keeps Z |
| flat switches | 357 (max 73 in one game) | u2flat73_n32 |
| flat switches that are GXC events (v ∈ Z_t, Ξ(v) climbs, W(v) fixed, λ_Ξ fixed) | 356 | |
| flat switches with no Ξ-climb at v (case (a)) | 4 | tog6a_n32 |
| FLAT-Z violations (Z grows at a flat transition; entry without a W-change) | 0 / 0 | |
| FL-GAP violations | 0 | |
| most flat switches of one vertex in one W-constant interval | 6 (> its out-degree − 1 in 12 cases) | u23sw64_n32 |
| flat switches to an edge already in the previous arena H_{t−1} | 24 (vs 214 to new edges) | cw11_n24 (5) |

## 5. Two candidate routes, DEAD on data
- DEAD: "index-monotone tie-break". Each vertex's flat switches within one W-constant interval would number at most its out-degree − 1 if
  S4a broke W-ties by a fixed order. Instance u23sw64_n32: one vertex switches 6 times in one W-constant interval, more than its
  out-degree − 1, in 12 (vertex, interval) cases. Of 357 flat switches, 225 go to a smaller index, and the rest do not.
  - Reason: SPEC S1's procedure breaks ties by longest / shortest path recursion and BFS order in the restricted graph, not by vertex
    index.
- DEAD: "a flat switch takes a newly offered edge". Instance cw11_n24: 5 flat switches go to edges already in H_{t−1}. 24 in the corpus.
  So a flat switch need not consume a new Ξ-entry.
- R71 FBC (configurations) restricted to a W-run: not attempted. FL transitions are S4a steps, not fallbacks, so FB-RISE_C does not
  apply as stated.

## 6. The exact obstruction (READING)
- In every instance of the corpus, every W-flat transition keeps the gap set Z fixed (ZFL = FL). So FLAT-Z's potential |Z| never moves
  on flat transitions, and the bound reduces to ZFL with nothing gained.
- ZFL transitions are pure Ξ-climbs inside a fixed gap set with W fixed. Their switching vertices are GXC events (356 / 357), and by R92
  TXC-DESCENT the tied climbs descend to gates. So FL-POLY's core is the same object as R92's [P-GATE] and L-NEW's TXC-RHO / GXC: Ξ-progress
  through Odd gates (σ̄ ≠ τ) while Even's W against τ is frozen.
- Why a flat climb needs a gate (READING, from R92 GP+'s prefix argument). If v switches d → e with W(e) = W(d), and d and e reach the same
  same-pair gate g along their τ-plays, then the prefix comparison decides both W and Ξ identically, so Ξ(e) = Ξ(d). A strict flat Ξ-climb
  therefore needs one of: a change of gate, a gate that is not same-pair, or (e gateless) leaving Z, which ZFL excludes.
  - Proposed next step: prove «every ZFL climb changes v's first gate or its gate's cycle-node pair», then look for a monotone order on
    gates.
- Instance for adversaries: u23sw64_n32 (FL = ZFL = 8, n = 32, |Z| = 32 throughout). It is a hill-climbed 𝒞^1O game; no growing family
  is known. FL ≤ 8 in all 1,132 runs.

## DONE / FINDINGS / NEEDS
- DONE: fl/flat.py; corpus (1,132 runs); si/check.sh «box 50b»; this note.
- FINDINGS:
  1. PROVED (lane): Lemma FLAT-Z. Z only shrinks at W-flat transitions, and entries into Z need a W-change.
  2. PROVED (lane): Corollary FL-GAP, FL_F ≤ n + n(n − 1)(R*_F + 1) + ZFL_F. Hence FL-POLY ⇐ R*-POLY ∧ ZFL-POLY, and
     R3-POLY ⇐ R*-POLY ∧ ZFL-POLY.
  3. PROVED (lane): Lemma FLAT-TXC. A flat transition is Ξ-flat or carries a TXC event, so FL_F ≤ XFL_F + R92's TXC-RED bound.
  4. DATA: FL ≤ 8 (u23sw64_n32); ZFL = FL everywhere; 356 / 357 flat switches are GXC events.
  5. DEAD: index-monotone tie-break (u23sw64_n32); new-edge-only flat switches (cw11_n24).
  6. READING: the obstruction is Ξ-progress through gates with W frozen, the same core as [P-GATE] / GXC. A gate-change lemma is the
     proposed next step.
- NEEDS: none from the owner.
