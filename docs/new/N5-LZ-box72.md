# N5-LZ (box 72): GXC splits into S4a TIE switches, gap CLOSINGS and fallback OPEN climbs. A lazy S4a tie-break (N5-LZC) removes the first part, and with it every W-silent re-entry
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 (after 04:56Z): BOX 72+, a polynomial bound on GXC per
λ-run (or per phase), or the exact obstruction with an instance; measure first with silent.py / zflat.py; a NEW angle under D18. Written
from ~05:10Z to 05:17Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- GXC, Z, phases, [S1-val], [S1-ord], [S4a], [S4c], [V1], [V2], [⊕], F1 (= RESULTS R17 (a)), XW, GAP-MON: as quoted in P-N5-GAP-box69.md §1
  and N5-SC-box70.md §3; not restated. W := val(σ_t, τ_t). At an S4a transition t → t + 1, put τ := τ_t, H := S4a's arena,
  W' := val(σ_{t+1}, τ). GXC reads W_{t+1} with τ_t, so W' = W_{t+1} for GXC. P(x) is the path-set component of a value. It includes
  the start vertex when that vertex is more relevant than the cycle node ([⊕]). "v rel" means v is more relevant than the cycle node in question.
- Tools in experiments/new/box72:
  - gxc.py: the anatomy of GXC events, and the TIE and CLOSE checks.
  - n5lz.py: N5-LZ / N5-LZC.
  - silentlz.py: box70/silent.py run unchanged on N5-LZC.
  - wincmp.py, cmp.py.
  - run*.sh: drivers over the 719-game corpus box59/sbcg.lst plus alt_all (413 runs, with starts); 1132 runs in all.
  - Outputs: gxc_*.txt, gxclz_*.txt, gxclzc_*.txt, silentlz_*.txt, wincmp.txt.

## 1. DATA first (N5, 1132 runs; gxc_*.txt)
- GXC events: 3636 in all. Max per λ-run 64 (u23sw64_n32, n = 32). Max per (λ-run, v) 9 (cw11_n24).
- By kind:
  | kind | events | W (read with τ_t) | gap at v after the event |
  | --- | --- | --- | --- |
  | S4a step | 385 | always equal (382 open, 3 close) | — |
  | Even fallback | 3251 | falls in 3228, equal in 23 | closes (v ∉ Z_{t+1}) in 3012 |
- The S4a events are W-TIES. In 359 of 359 off-cycle cases the old successor d is still W'-consistent at v (v ⊕ W'(d) = W'(v)). The
  other 26 are own-cycle-node cases.
- u23sw64_n32: all 64 events are S4a ties. The gap level is 'C' (Ξ(v) and W(v) have different cycle nodes). One witness (Odd 27, σ̄ ≠ τ)
  serves all 64. W ≡ (13, ·, ·) is flat, so the ceiling plays no role. Ξ climbs in P under a fixed cycle node.
- READING, the sandwich candidate: Ξ ⊴ W with W fixed gives nothing when the gap sits at the cycle level. That is 933 of the 3636 events,
  and every one of the record run's 64. The lex-monotonicity of the gap level (check (M), 0 violations) is true but too weak. It is a counter.
- Gap inheritance (I) holds: an off-cycle x has the same gap level as σ(x) (0 violations in all checks). Ξ and W agree up to the first Odd
  vertex with σ̄ ≠ τ.

## 2. Lemma TIE (PROVED, lane): an S4a switch that does not raise W(v) is a pure tie-break
Setting. Let t → t + 1 be an S4a transition. σ_{t+1} is an optimum of the one-player game H against τ ([S4a]). By F1, W' ⊵ val_ρ pointwise
for every Even strategy ρ of H; in particular W' ⊵ W. Let v be Even with d := σ_t(v) ≠ σ_{t+1}(v) and W'(v) = W(v). (By F1, "W'(v) ⊴ W(v)",
the GXC condition, is the same as equality.) Then:
- (a) if v is not its own W'-cycle node: v ⊕ W'(d) = W'(v), and d's σ_{t+1}-path to its cycle node avoids v (d is W'-CONSISTENT at v);
- (b) if v is its own W'-cycle node: W'(d) has cycle node v and empty path set.
Facts used. rew is injective (p' injective). (R1) A vertex u that is even and more relevant than x has rew(u) > rew(x). (R2) If x is odd,
every vertex u less relevant than x has rew(u) > rew(x). Two values with the same cycle node compare by the most relevant vertex of the
symmetric difference of their path sets: the set that holds it is better iff that vertex is even. ρ := σ_{t+1}[v ↦ d] is a strategy of H,
because d ∈ A(v).
Proof of (a). If v were its own W-cycle node, W(v) = (v, ∅, 0) = W'(v), against (a)'s hypothesis. So by [V1], W(v) = v ⊕ W(d), and d's
σ_t-path avoids v. Let c* be the common cycle node of W(v) = W'(v), so also of W(d). Let π be d's σ_{t+1}-play.
- (a1) π never visits v. Under ρ, v's play is v·π, so val_ρ(v) = v ⊕ W'(d). F1 gives v ⊕ W'(d) ⊴ W'(v) = W(v) = v ⊕ W(d). [V2] with
  W(d) ⊴ W'(d) (F1; both paths avoid v) gives v ⊕ W(d) ⊴ v ⊕ W'(d). So the two are equal.
- (a2) v lies on π's cycle. Then v's σ_{t+1}-play is that cycle, so its node is c*, P(W'(v)) = ∅, and v is less relevant than c*. π's path
  to c* avoids v, so [V2] gives W(v) ⊴ v ⊕ W'(d) = (c*, P(W'(d)), ·).
  - If P(W'(d)) = ∅: under ρ, v's play closes the cycle v·(π's path)·(c*'s cycle back to v), whose top is c*. So val_ρ(v) = v ⊕ W'(d),
    F1 gives ⊴ W'(v), and equality follows.
  - Otherwise let u be the top of P(W'(d)). It is more relevant than c* and tops ρ's cycle. F1 gives rew(u) < rew(c*), so u is odd (R1).
    Then v ⊕ W'(d) ◁ (c*, ∅, ·) = W'(v) = W(v), against W(v) ⊴ v ⊕ W'(d).
- (a3) v lies on π's path part, before π's cycle: d = x_0, …, x_q = v, q ≥ 1. Then c* ∉ X := {x_0, …, x_q}, and
  W'(d) = (c*, R ∪ P(W'(v)), q + ℓ'(v)), with R := {x_i : i < q, x_i rel}. P(W'(v)) = P(W(v)) = P(W(d)) ∪ {v if rel}.
  Let u be the most relevant vertex of X. Under ρ, v's play is the cycle X, with top u ≠ c*. F1 gives rew(u) < rew(c*).
  - u more relevant than c*. Then u is odd (R1).
    - If u ∉ P(W(d)): the new elements of P(W'(d)) over P(W(d)) are (R ∪ {v if rel}) \ P(W(d)). Their top is u, which is odd, so
      W'(d) ◁ W(d), against F1.
    - If u ∈ P(W(d)): then u ≠ v (d's σ_t-path avoids v), and u ∈ P(W'(v)), so u lies on v's σ_{t+1}-path. But u = x_i with i < q, so
      u's σ_{t+1}-play passes v. Hence u and v lie on one σ_{t+1}-cycle, the cycle of v's play, whose most relevant vertex is c*. That
      contradicts u being more relevant than c*.
  - u less relevant than c*. Then R = ∅ and v is not rel, so W'(d) = (c*, P(W(d)), ℓ(W(d)) + q + 1).
    - If c* is odd, R2 gives rew(u) > rew(c*), against F1.
    - If c* is even, W'(d) has the same path set as W(d) and is longer, so W'(d) ◁ W(d), against F1.
  So (a3) cannot occur, and (a1), (a2) give (a). □
Proof of (b). W(v) = W'(v) = (v, ∅, 0), so d lies on v's σ_t-cycle and W(d) = (v, ∅, ·).
- If π never visits v: val_ρ(v) = v ⊕ W'(d), whose cycle node is λ'(d) ≠ v. F1 gives rew(λ'(d)) < rew(v), so W'(d) ◁ W(d), against F1.
- Otherwise π reaches v and then stays on v's σ_{t+1}-cycle, so λ'(d) = v. If P(W'(d)) ≠ ∅, its top u is more relevant than v, and it
  must be even, since W'(d) ⊵ W(d) = (v, ∅, ·). ρ's cycle d … v d has top u, so by R1 val_ρ(v) ▷ W'(v), against F1. So P(W'(d)) = ∅. □
- READING: in N5, every S4a GXC event (385 / 3636) is a choice between W'-equal options at v. The old option is still optimal, and the S1
  procedure moved v anyway. This is box 71's mechanism (s2piece_n32: three W*-tied options), now in general form.

## 3. N5-LZC: N5 with a lazy S4a tie-break (own approach, D14)
- Definition (n5lz.py, with --lzc). N5-LZC is N5 except in S4a. Let σ* be S4a's output (the S1 procedure's optimum of H) and W* := val(σ*, τ).
  - For every Even v with ℓ(W*(v)) ≥ 1, keep σ_t(v) if v ⊕ W*(σ_t v) = W*(v).
  - For every Even v with W*(v) = (v, ∅, 0), keep σ_t(v) if W*(σ_t v) has cycle node v and empty path set.
  - Every other Even vertex takes σ*(v).
  If the result equals σ_t, then σ_new = σ_t, and S4c applies exactly as in SPEC. Odd's side is unchanged.
  Without the second rule the variant is N5-LZ (--lz).
- Lemma LZ-OPT (PROVED, lane). The lazy strategy σ' has valuation W*, so it is again an optimum of H.
  - Proof. Every choice of σ' is W*-consistent. Off-cycle vertices: v ⊕ W*(σ' v) = W*(v); for σ*'s own choices this is [V1]. Cycle nodes:
    W*(σ' c) = (c, ∅, ·). Odd vertices follow τ, as σ* does.
  - Consistency decreases ℓ by exactly 1 per step and keeps the cycle node. So from any x, σ' reaches c := λ*(x) in ℓ*(x) steps without
    repeating a vertex. The only vertex of length 0 with node c is c itself.
  - From c the chain is (c, ∅, ·) and P shrinks along consistent steps (P_x = P_y ∪ {x if rel}). So every vertex on the way back to c has
    P = ∅ and is less relevant than c, and the play from c is a cycle with top c.
  - Along the path, P accumulates exactly P(W*(x)). Hence val_{σ'}(x) = W*(x). □
  - DATA: n5lz.py asserts val(σ') = W* at every S4a step. No assertion failed in 1132 runs.
- Theorem LZ-STRICT (PROVED, lane). In N5-LZC, every Even v switched at an S4a transition has W'(v) ▷ W(v) (W read with the old τ).
  - Proof. F1 gives ⊵. Suppose equality. σ_{t+1} = σ' is an optimum of H with valuation W* = W' (LZ-OPT), so Lemma TIE applies to it.
    So σ_t(v) satisfies (a) or (b) with respect to W*, the keep-rule's condition. If σ*(v) = σ_t(v), then σ'(v) = σ_t(v) at once.
    Otherwise the rule keeps σ_t(v). Either way v does not switch. □
- Corollary LZ-NOGXC (PROVED, lane). N5-LZC has no S4a GXC events. Every GXC event of N5-LZC is an in-phase Even fallback.
- Corollary LZ-NOSIL (PROVED, lane, given SIL-Z (a)).
  - Statement: N5-LZC has no class-S re-entry (P-N5-CUT §4).
  - Proof: SIL-Z (a) (box 70) gives W*_j(v) = W*_{j−1}(v), with W* read with τ_{j−1} and v off its own W*-cycle node, at every S
    re-entry j − 1 → j. That is an S4a switch with no W-rise, which LZ-STRICT excludes.
  - Dependency: SIL-Z (a) uses L-SI's W-RETURN-G. ASSUMPTION OPT-ONLY: W-RETURN-G's proof uses S4a's output only as AN optimum of H, not
    the S1 procedure's tie-break. I believe this from the quoted chain (box 70 §0), which is F1 / [V2] only. Not re-checked line by line;
    a referee should check it.
  - DATA: S = 0 on N5-LZC in 1132 runs (silentlz_*.txt); N5 has S = 84.
- DATA C (own-cycle re-entries): C = 0 on N5-LZC in 1132 runs; N5 has C = 8. No proof. CONJECTURE LZ-NOC: N5-LZC has no class-C re-entry.
- DATA, N5-LZC against N5 on the same 1132 runs (cmp.py):
  | | iterations | fallbacks (S4c, all) | GXC | S4a GXC |
  | --- | --- | --- | --- | --- |
  | N5 | 21845 | 1486 | 3636 | 385 |
  | N5-LZC | 21542 | 1445 | 3214 | 0 |
  - Max GXC per λ-run: N5 64, N5-LZC 54 (all fallback events).
  - Run lengths: N5-LZC is shorter in 100 runs and longer in 34; worst +5 on tcL_N10 (27 → 32), best −41 on j7_n48 (78 → 37). The max
    iterations/n is 3.5 for both (lend107_n32).
  - Winning regions SAME in 1132 / 1132 (wincmp.txt).
  - The tie-break does not just push the work into fallbacks: N5-LZC makes fewer fallbacks than N5.

## 4. Lemma GXC-CLOSE (PROVED, lane; any optimum in S4a, so N5 and N5-LZC)
Let P = [a, b] be a phase, CL_P the GXC events (v, t) in P with v ∉ Z_{t+1}, and WCH^S4a_P the pairs (x, t) with t → t + 1 an in-phase S4a
transition of P and W_{t+1}(x) ▷ W_t(x). Then CL_P ≤ |Z_a| + WCH^S4a_P.
- Proof. τ is constant on P, so Z_t is read with one τ. Each CL event is an exit of v from Z, and distinct events are distinct (vertex,
  transition) exits. An entry x ∉ Z_t, x ∈ Z_{t+1} at an in-phase transition needs Ξ_{t+1}(x) ◁ W_{t+1}(x), with
  Ξ_{t+1}(x) ⊵ Ξ_t(x) ([R15]) = W_t(x). So W_{t+1}(x) ▷ W_t(x).
  - At an in-phase fallback there are no entries (GAP-MON: Z never grows at a τ-fixed Even fallback).
  - Every in-phase transition is S4a or such a fallback (P-N5-GAP §1).
  So entries ≤ WCH^S4a_P, and exits ≤ |Z_a| + entries. □
- DATA: 0 violations in 1132 runs (N5) and 1132 (N5-LZC); max CL / bound = 0.683 (rise_fb38_n48).
- In N5-LZC, every S4a switch is a strict W-rise at the switched vertex (LZ-STRICT). So the S4a switches of N5-LZC in P are ≤ WCH^S4a_P.

## 5. The composition (PROVED, lane) and what is left
- For a phase P of N5: GXC_P ≤ TIE_P + |Z_a| + WCH^S4a_P + FBO_P, where:
  - TIE_P := the S4a GXC events (Lemma TIE: pure tie-breaks);
  - FBO_P := the GXC events at in-phase fallbacks with v ∈ Z_{t+1} (the gap stays OPEN at v).
- For N5-LZC: GXC_P ≤ |Z_a| + WCH^S4a_P + FBO_P (LZ-NOGXC, GXC-CLOSE).
- Fold with P-N5-GAP. A Z-flat fallback has Z_{k+1} = Z_k, so all its GXC events are FBO. Hence ZF_P ≤ FBO_P + NZ_P (box 70 (ii)), and
  Theorem GAP-RED's premises become, per phase: per-vertex WCH^S4a and FBO.
- Fold with P-N5-CUT, for N5-LZC under OPT-ONLY: SC*'s S part vanishes. SIL ≡ 0, so SC* = CYC (DATA 0).
- Hence, under OPT-ONLY: GXC for N5-LZC is polynomial per phase iff FBO_P is (with WCH^S4a per vertex per phase poly, already a GAP-RED
  premise). The residual is the open count FBO.
- FBO DATA:
  | | FBO events | max per phase | max per (v, phase) |
  | --- | --- | --- | --- |
  | N5 | 239 | 46 (nep22f_n64, n = 64) | 5 |
  | N5-LZC | 242 | 45 | 4 |
  In FBO, v moves at an Even fallback to its Ξ-best improving successor ([S4c]). Ξ(v) rises strictly, W(v) falls or stays, and v stays in
  the gap. nep22f_n64 is box 68's saturated gap (|Z| 59 / 64, one Ξ cycle node).
- CONJECTURE FBO-LIN (OPEN): FBO_P ≤ n per phase. DATA: max 46 / 64 = 0.72 n on N5, 45 on N5-LZC.
- What is NOT proved:
  - FBO itself;
  - C re-entries in N5;
  - that every RESULTS lemma of N5 holds for N5-LZC (only those whose proofs use S4a's output as an arbitrary optimum of H transfer;
    R15 (d) transfers, since σ' differs from σ_t only on improving edges);
  - TIE_P for N5 itself: it is the S1 procedure's tie-break (box 71), unbounded by this note.

## DONE / FINDINGS / NEEDS
- DONE:
  - box72/gxc.py, n5lz.py, silentlz.py, wincmp.py, cmp.py, run*.sh;
  - outputs gxc_*, gxclz_*, gxclzc_*, silentlz_*, wincmp.txt (1132 runs each);
  - this note; check.sh "box 72".
- FINDINGS:
  1. DATA: GXC = 385 S4a events (all W-tied) + 3251 fallback events (3012 close the gap). The record u23sw64_n32's 64 are all S4a ties at
     the cycle level. The W-ceiling sandwich is DEAD as a bound there (the gap is at the cycle level).
  2. PROVED (lane): Lemma TIE. An S4a switch with no W-rise leaves the old successor W-optimal (consistent) at v.
  3. PROVED (lane): Lemma LZ-OPT and Theorem LZ-STRICT. In N5-LZC (lazy S4a tie-break), every S4a switch strictly raises W at the
     switched vertex. Corollaries: no S4a GXC; no class-S re-entry (given SIL-Z (a) under OPT-ONLY).
  4. PROVED (lane): Lemma GXC-CLOSE. Gap-closing GXC events per phase ≤ |Z_a| + WCH^S4a_P (N5 and N5-LZC).
  5. DATA: N5-LZC makes fewer iterations (21542 vs 21845) and fewer S4c fallbacks (1445 vs 1486), has the same winners, and has S = C = 0.
  6. OPEN: FBO (fallback climbs that keep the gap open), max 46 per phase. CONJECTURE FBO-LIN, CONJECTURE LZ-NOC.
- NEEDS: none from the owner. From the Lead: a ruling on whether N5-LZC (a different S4a tie-break) may replace N5 as the lane's object
  for the SC* / GXC premises, and a referee check of OPT-ONLY.
