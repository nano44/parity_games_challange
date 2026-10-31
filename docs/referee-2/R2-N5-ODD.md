# R2-N5-ODD: second-referee report on P-N5-ODD (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/si/P-N5-ODD-box57.md @ l-si 0afc0d70a, sha1 03eec41d3bfc63a6945d0f30d831a46f14e46b84 (re-hashed: match), 146 lines.
  Line: docs/si/P-N5-ODD-line.txt, sha1 cd121dffd06dbc794f3154e34aa238d8df81f837 (re-hashed: match).
- Independence: written before opening any docs/referee/ file on ODD.
- Scope: a RELOCATION. Nothing is bounded. G-N5-TIME stays OPEN.
- Lead brief 12:40Z: sign §2 OLD-PLAY; §3 ODD-STEP (Case II = NO-RET); §4 ODD-RELAY, ODD-ADD; §5 SRC-ROOT; §6 FUEL-LEX, FUEL-COUNT.

## 1. Claims table
| § | item | verdict | gap |
| --- | --- | --- | --- |
| 1 | (Φ-comp) | checked ✓ (a formal identity of [PLAY]'s formula) | none |
| 2 | Lemma OLD-PLAY | SIGNED | none |
| 3 | Lemma ODD-STEP, Case I and Case II (Lemma NO-RET) | SIGNED | none |
| 4 | Lemma ODD-RELAY; Corollary ODD-ADD | SIGNED | none |
| 5 | Corollary SRC-ROOT | SIGNED | none |
| 6 | Lemma FUEL-LEX | SIGNED with G-ODD-1 closed (§3) | G-ODD-1 (proof covers keys < a, not ≤ a) |
| 6 | Corollary FUEL-COUNT | SIGNED with G-ODD-2 closed (§3) | G-ODD-2 (EQHI / REP overlap at (0, 0)) |
| 7 | DATA, pins, DEADs | not signed | F-1 (sbq2 start invalid) |
| line | cd121dff | REQUIRED ODD-L1 to ODD-L3 (§5) | — |
- Gap map: G-ODD-1 and G-ODD-2, both proof-text, both closed here by one-line repairs (referee-originated; L41: they need REFEREE's
  signature or the lane's fixes entry).

## 2. Premises against the landed text
- [R15a]: Ξ_(k+1) ⊵ Ξ_k at every transition. R15 (d) makes every N5 iteration a Switch_I with I ⊆ Iσ (or no σ-change), and (a) gives
  monotonicity, as R96 / R97 use it. My tools check XIMON on the whole run. ✓
- [R57]: «S1's procedure realises the pointwise optimum», read as Ξ_k(x) ⊴ val(σ_k, ρ)(x) for every positional Odd ρ. That is the
  meaning of R57's 1E-N3. ✓
- [PLAY]: R97 (l. 8032), the proof of PLAY-CAUSE^S. The quoted text matches P-N5-SRC §2, which I signed.
- (Φ-comp) is a formal identity of [PLAY]'s formula, as the packet needs it. (E2) composes an old-play Φ with a new-play Φ, which is not one
  play. Checked case by case:
  - w first in a at j: both sides give (w, rel(a_<j), j);
  - w in b only, at j: both give (w, rel(a) ∪ rel(b_<j), |a| + j);
  - neither: both give (w, rel(a) ∪ rel(b) ∪ P, |a| + |b| + ℓ). ✓
- R97's W-run notation (τ, C, D_k, S_k, H_k): as landed. ✓

## 3. Item checks
- OLD-PLAY: with no switch on x's old play, val(σ_(k+1), σ̄_k)(x) = Ξ_k(x). [R57] at k + 1 gives ⊴, and [R15a] gives ⊵. ✓
- ODD-STEP.
  - (E1) Ξ_k(o) = Φ(o; v_x). ✓
  - Case I: ρ := σ̄_(k+1)[o ↦ x]. o's (σ_(k+1), ρ)-play is o followed by x's new play (o is not on it), so its value is Φ(o; v_x) =
    Ξ_k(o) ◁ ξ, against [R57]. ✓
  - Case II (NO-RET).
    - (E2), (E3): Z = oγ is a pure cycle under ρ. ✓
    - w = o: Φ(oγ; ξ) = (o, ∅, 0) = ξ. ✓
    - w ∉ γ: o's new path to w avoids γ. If it met z_t first, the play would return to o along γ with no w on its cycle, but w is that
      cycle's top. ✓
      - A (o above w): o ∈ P(v_x), and x's OLD play then cycles x … o x … with the first w before o: a contradiction. ✓
      - B (o below w): Ξ_k(o) = (w, P ⊔ R, ℓ + j + 1). If R ≠ ∅, Q1 makes the top t odd and m = t, so val ◁ ξ. If R = ∅, w is even and
        every vertex of Z is below w, so val ◁ ξ. ✓
    - w = z_i ∈ γ: o and z_(i+1) … lie on the cycle topped by w, so P = ∅, v_x = (w, R, i) and Ξ_k(o) = (w, R, i + 1).
      - R = ∅: val = Ξ_k(o) ◁ ξ.
      - R top even: Ξ_k(o) ▷ ξ.
      - R top odd: m = t and val ◁ ξ.
      Each case contradicts [R57] or ξ ▷ Ξ_k(o). ✓
- ODD-RELAY: π moves identically at k and k + 1, so Ξ_j(x) = Φ(π; Ξ_j(u)) for both j, and ODD-STEP closes it. ✓ ODD-ADD: each change of o
  at k ∈ I is matched with a change at the same k. ✓
- SRC-ROOT.
  - u_k(o) exists: a play avoiding D_k is the W-play, whose cycle top is in C.
  - ODD-RELAY applies along the chain.
  - Each o_(j+1) lies on o_j's old play, a suffix of o_0's.
  - The chain stops only at (a) an Odd vertex with a prefix event, or (b) an Even C-node. An Odd C-node continues.
  - A repeat would mean o_0's whole old play is covered by first segments and Odd o_j with no Even switch, against OLD-PLAY. ✓
- **FUEL-LEX, G-ODD-1 (proof-text gap; CLOSED).**
  - The proof supposes «every change of Ξ(z) strictly between t and t′ has key < (1, r)». The negation of EQHI is «≤ (1, r)». The case of
    an intermediate change with key exactly (1, r) and none higher is not covered by the text.
  - Repair: let u be the first change in (t, t′] with key ≥ (1, r). It exists, since t′ has key (1, r).
    - Between t + 1 and u the cycle node and the bits at ranks ≥ r are fixed, and the bit at r is the better one β (the rise at t).
    - If u's key is (1, r), u moves r away from β with the higher bits fixed: a fall, against [R15a]. This covers both u = t′ and u < t′.
    - So u < t′ with key > (1, r), which is EQHI.
  - Mechanical: MID_EQKEY (a key-(1, r) change strictly between two (1, r) re-routes) = 0 everywhere, as the repair predicts.
- **FUEL-COUNT, G-ODD-2 (proof-text gap; CLOSED).**
  - A boundary with b = a = (0, 0) satisfies REP whatever happens between t and t′. It may also satisfy EQHI (a change with key > (0, 0)
    in (t, t′)).
  - The proof's «along consecutive REP (0, 0) boundaries no change of key > (0, 0) happens» holds only if such a boundary is counted as
    EQHI (charged to HC), and only the remaining «pure» REP (0, 0) boundaries are chained.
  - Repair: classify a boundary as ASC, else EQHI, else REP. Then the stated count n(1 + A), with A ≤ HC + n − 1, goes through:
    - along a chain of pure REP (0, 0) boundaries, only length changes occur, at a fixed (cycle node, path set), strictly monotone over
      ≤ n lengths;
    - REP (2, 0) boundaries are cycle-node rises, ≤ n − 1;
    - ASC and EQHI are charged to HC through disjoint windows (t, t′]. The last re-route at a transition ≤ u is the boundary's first one.
  - Mechanical: REP00_with_higher (the overlap) = 0 on everything run. FCNT = 0.

## 4. Mechanical checks and pins (own code)
- Tool: docs/referee-2/R2-N5-ODD/odd_check.py.
  - It is my LATEP state loop with my WRUN start reader. The lane's src54 / fseg55 / grow56 tools are not imported.
  - Fuel re-routes are taken over ALL Even y, as the packet defines them. The lane's srcfuel.py restricts y to first segments.
  - Logs: R2-N5-ODD/logs.
| run | runs | violations | OLD / STEP / RELAY checks | STEP Case II configs | SRC-ROOT (a) / (b) | fuel re-routes; ASC / EQHI / REP |
| --- | --- | --- | --- | --- | --- | --- |
| sbcg.lst (runs=1) | 719 | 0 | 190,916 / 368,435 / 548,570 | 18,237 | 12,459 / 14 | 15,913; 723 / 197 / 0 |
| alt_all, with start (runs=0) | 94 | 0 | 32,294 / 39,432 / 25,920 | 3,371 | 7,435 / 7 | 5,493; 17 / 7 / 0 |
| alt_all, start-less (runs=1) | 319 | 0 | 109,902 / 120,194 / 435,800 | 8,337 | 3,115 / 10 | 6,133; 25 / 54 / 0 |
| random seed 51 (3,000 games, n 8-16, 4 starts) | 12,000 | 0 | 81,995 / 143,359 / 58,693 | 47,123 | 1,009 / 9 | 147; 0 / 0 / 0 |
| pins (6 with valid starts) | 6 | 0 | 25,868 / 447,088 / 28,497 | 42 | 18,679 / 0 | 5,114; 2 / 0 / 0 |
| so_th_n32 (default start) | 1 | 0 | 465 / 72 / 70 | 19 | 22 / 0 | 56; 0 / 10 / 0 |
- Corpus 1,132 games: 0 violations of OLD, STEP, RELAY, ROOT, FLEX and FCNT, and of XIPLAY / XW / XIMON. MID_EQKEY = 0 and
  REP00_with_higher = 0 on every run, so neither G-ODD-1's nor G-ODD-2's uncovered case occurs.
- Pins (from 0afc0d70a; obs, src2, rcl, latew, hit_b6a_1 and nep56 with their start files): 0 violations.
  - nep56_n32: ASC 2 = the lane's «ASC 2».
  - so_th_n32 (default start): EQHI 10 against the lane's 6. The lane counts only y on first segments; I count every y, as the packet's
    definition (§6) says. This is a definition difference, not an engine difference.
- **F-1 (DATA / DEAD; not to sign, but recorded).** sbq2_K8_m16.start (experiments/si/src54/inst, sha1 98b0927a) sets «TAU0 … 242:243».
  - 243 is not a successor of the Odd vertex 242 (succ(242) = 244, 246, …, 258).
  - Run without validation, τ(242) = 243 at all 153 states, and τ(259) = 243 as well.
  - So the box-54 DEAD «the W-rank potential (sbq2: W(242) = W(259) at all 153 states, σ̄(260) flips 128)» holds because both vertices
    point at 243, one through a non-edge.
  - That DEAD is killed by an invalid instance. Under CLAUDE.md's faithfulness rule it needs a valid instance, or a correction in
    docs/si/DEAD.md.
  - n5x.start_pair applies start entries unvalidated. Oink's verification of the final solution does not check the start.
  - The pinned box-54 OLD-PLAY counts on sbq2 (VOLD 0 and the MUT control's VOLD 2,881) are on the same non-game. DATA only.
  - My reader rejects this start, so my pin run skipped sbq2.

## 5. Line (cd121dff): strict symbol test, TARGET.md scope words
- **ODD-L1 (REQUIRED; unbound or unquantified symbols).**
  - OLD-PLAY «if Ξ_(k+1)(x) ≠ Ξ_k(x)»: x is unquantified. Write «for every vertex x».
  - ODD-RELAY «if moreover u lies on …»: u, likewise.
  - SRC-ROOT «if Ξ changes at k at an Odd o_0»: k is not tied to F. Write «at a transition k → k + 1 of F».
  - FUEL-LEX / FUEL-COUNT use F (the fuel re-route definition «k − 1 ∈ F», «in F»), but F is bound only inside the SRC-ROOT clause
    («in every W-run F»). Write «for every N5 run on every game and every W-run F of it» for the W-run clauses. This is the WRUN-L3 /
    SETTLE-L1 class.
- **ODD-L2 (REQUIRED).** FUEL-LEX's «the two rise transitions» is undefined in the line. Add «its rise transition k − 1 → k» to the fuel
  re-route definition.
- **ODD-L3 (REQUIRED; wider than signed).** «(Corollary ODD-ADD) the Ξ-changes of o on a set of transitions are at most the transitions at
  which one of the relayed vertices changes (no degree factor)» drops ODD-ADD's hypothesis, and «relayed vertices» is undefined.
  - Fix: «if at every k ∈ I at which Ξ(o) changes ODD-RELAY's hypothesis holds for some u_k ∈ U, then those k number at most the k ∈ I at
    which Ξ(u) changes for some u ∈ U».
- ODD-L4 (precision). «DATA: corpus 0 violations of every statement».
  - §7 lists corpus checks for OLD-PLAY / ODD-STEP / ODD-RELAY, SRC-ROOT and FUEL-LEX (FS-restricted y), but not FUEL-COUNT or ODD-ADD.
  - Write «of every statement checked in packet §7», or cite my checks (which cover all of them, with unrestricted y).
- ODD-L5 (precision). If G-ODD-1 / G-ODD-2 are closed by the lane's fixes entry, nothing changes in the line. If they are closed by these
  repairs, the tail should say so (L41).
- TARGET.md scope words: «a RELOCATION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim;
  …)» ✓. n is bound by TARGET.md l. 8.

## Verdict (Opus 5.5, D15)
- SIGNED: OLD-PLAY, ODD-STEP (with NO-RET), ODD-RELAY, ODD-ADD and SRC-ROOT.
- SIGNED with repairs: FUEL-LEX (G-ODD-1) and FUEL-COUNT (G-ODD-2), both proof-text gaps with one-line repairs. Statements unchanged.
- Line: REQUIRED ODD-L1, ODD-L2, ODD-L3; precisions ODD-L4, ODD-L5.
- DATA / DEAD finding F-1: the sbq2_K8_m16 start uses the non-edge 242 → 243. The box-54 W-rank DEAD rests on it.
