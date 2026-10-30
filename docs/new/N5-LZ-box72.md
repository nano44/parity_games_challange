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

## 6. GXC against L-SI's TXC (Lead 2026-10-30 05:29Z; l-si 4fb0bfba docs/si/N5-ADD-box50.md §6, odd/tied.py)
Written ~05:43Z (date -u). Tools:
- box72/txc.py: TXC, GXC, overlap and the SOURCE of each TXC event. The W-run is as in tied.py (τ fixed, no S4c, σ changes, W's
  cycle-node map fixed).
- tied_lsi_4fb0bfba.py: L-SI's tied.py, copied byte for byte.
- runlzc.py: runs any script on N5-LZC.
- run_txc.sh, txcsum.py; outputs txc_*.txt (1132 runs).
- L-SI's families copied to box72/inst: latew_K20_m32 (.pg sha1 063d173c…) and wdepth_K4_m16 (.pg sha1 8f1ab64d…), with their .start files.
- [Q l-si 4fb0bfba N5-ADD-box50.md §6] «A TIED Ξ-CLIMB of z at s ∈ [k, u − 1] is a transition with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z).»
  TXC_F(z) := the tied Ξ-climbs of z in the W-run F.
### 6.1 Exact relation
- (E1) GXC ∩ TXC = the GXC events at S4a transitions inside W-runs.
  - A GXC event at an S4a step has W_{t+1}(v) = W_t(v) (F1). In a W-run it is a TXC event at z = v.
  - A GXC event at a fallback is never TXC: W-runs contain no S4c transition.
  - A TXC event is GXC only if z is Even and switched, and λ_Ξ is fixed. z ∈ Z_s holds automatically (L-SI §6).
  - DATA: all 385 S4a GXC events of N5 lie in W-runs and are TXC; the 3251 fallback GXC are not. TXC has 37895 events in all, so
    GXC ∩ TXC is 1.0 % of TXC.
- (E2) Lemma TXC-SRC (PROVED, lane). Let (z, s) be a TXC event in a W-run. Follow the INHERITANCE CHAIN from x := z: if x is Even and not
  switched, step to σ_s(x); if x is Odd with σ̄_s(x) = σ̄_{s+1}(x) = τ(x), step to τ(x). Every vertex of the chain carries a tied climb.
  The chain ends at a SOURCE x of one of these types:
  - EVEN-TIE: x is Even and switched at s, Ξ(x) rises, W(x) is fixed. These are exactly Lemma TIE's events at x.
  - SBAR: x is Odd and σ̄_s(x) ≠ σ̄_{s+1}(x).
  - WIT: x is Odd with σ̄_s(x) = σ̄_{s+1}(x) ≠ τ(x).
  - CYC: x is its own Ξ- or W-cycle node at s or s + 1.
  - Proof. Let x be off its own cycle nodes with chain successor y, and put ρ := σ_s (Even) or τ (Odd). Then [V1] at s and s + 1 gives
    Ξ(x) = x ⊕ Ξ(y) and W(x) = x ⊕ W(y), with paths avoiding x. W's cycle-node map is fixed in a W-run, so x ⊕ · is injective on the two
    W-values: W_s(y) = W_{s+1}(y). Ξ_{s+1}(x) ≠ Ξ_s(x) forces Ξ_{s+1}(y) ≠ Ξ_s(y), and R15 makes it a strict rise. So y carries a tied
    climb (the chain never BREAKS).
  - The chain follows the (σ_s, τ)-play, so it ends at a source or at the W-cycle (CYC). □
  - DATA: BRK = 0 in 1132 runs.
- (E3) Corollary TXC-RHO (PROVED, lane). SBAR and WIT sources are Odd CHOICE vertices (σ̄ ≠ σ̄′ or σ̄ ≠ τ needs two successors) whose Ξ
  changes at s. So they are ρ-type events: RESULTS R56's «Ξ-changes at Odd choice vertices», counted here per W-run, not per phase. A W-run can
  cross λ_Ξ-changes, so ρ_F is not R56's per-phase ρ. Each TXC event (z, s) has exactly one
  source, at the same s, so for every z and W-run F:
  TXC_F(z) ≤ TIE_F + ρ_F + CYC_F,
  with all three counted as (vertex, transition) events in F. In N5-LZC, TIE_F = 0 (LZ-STRICT; DATA: EVEN-TIE = 0).
  - With L-SI's CONJECTURE TIED-RB and TOK1-type injectivity: re-blocked REP_F ≤ Σ_z d_E(z)·TXC_F(z) ≤ m_E·(TIE_F + ρ_F + CYC_F).
- DATA, sources (1132 runs):
  | | TXC | SBAR | WIT | CYC | EVEN-TIE | max TXC per (z, W-run) | max per W-run |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | N5 | 37895 | 29667 | 6632 | 1035 | 561 | 50 (pp_K48_n449) | 483 (pft35_n48) |
  | N5-LZC | 38749 | 30146 | 7137 | 1466 | 0 | 50 | 483 |
- DATA, L-SI's REP families (the ones that drive REP):
  | instance | n | iterations N5 / N5-LZC | GXC | TXC | sources | tied.py REPEATs, tied / reblk |
  | --- | --- | --- | --- | --- | --- | --- |
  | wdepth_K4_m16 | 146 | 76 / 76 | 0 | 184 | SBAR 93, WIT 91 | 21, 21 / 21 |
  | latew_K20_m32 | 538 | 700 / 700 | 0 | 3941 | SBAR 938, WIT 3003 | 570, 570 / 570 |
  - tied.py gives the same counts on N5 and N5-LZC. Winning regions are SAME.
  - Corpus tied.py, 1132 runs: rep 50, tied 13, untied 37, reblk 5, untied_reblk 0, on both N5 and N5-LZC.
### 6.2 READING
- A GXC bound does NOT bound REP*. On both REP families GXC = 0 and the tied climbs that pay the 591 re-blocked REPEATs are all
  Odd-sourced (SBAR / WIT). N5-LZC leaves those runs unchanged, so the lazy tie-break does not touch REP.
- So TIED-RB, if proved, charges re-blocked REP to ρ (Odd-choice Ξ-changes per W-run) plus CYC, not to GXC. That is a per-W-run form of R56's
  ρ-POLY, the premise FB-RED already needs. The two premises would then coincide, a possible economy, but not a closing.
- GXC (S4a part) and TXC meet only in Lemma TIE's events (E1). These are 1 % of TXC on the corpus and 0 on the REP families.

## DONE / FINDINGS / NEEDS
- DONE:
  - box72/gxc.py, n5lz.py, silentlz.py, wincmp.py, cmp.py, run*.sh;
  - outputs gxc_*, gxclz_*, gxclzc_*, silentlz_*, wincmp.txt (1132 runs each);
  - §6: txc.py, runlzc.py, tied_lsi_4fb0bfba.py, run_txc.sh, txcsum.py, txc_*.txt, inst/ (L-SI's latew_K20_m32, wdepth_K4_m16);
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
  7. §6 PROVED (lane): TXC-SRC and TXC-RHO. GXC ∩ TXC = S4a GXC events in W-runs (385 / 37895). Every tied climb inherits from an
     EVEN-TIE, Odd-choice (ρ) or CYC source, and TXC_F(z) ≤ TIE_F + ρ_F + CYC_F.
     DATA: L-SI's REP families have GXC = 0, all sources Odd (SBAR / WIT), identical under N5-LZC. So GXC does not bound REP*;
     TIED-RB would charge REP to ρ.
- NEEDS: none from the owner. From the Lead: a ruling on whether N5-LZC (a different S4a tie-break) may replace N5 as the lane's object
  for the SC* / GXC premises, and a referee check of OPT-ONLY.

## Addendum (2026-10-30 ~08:15Z, date -u): code hazard fixed (L-RED R133, l-red 5d78e948, via the Lead 07:34Z)
- box72/n5lz.py cached its W-engine in a module-level dict `_wc` keyed by τ alone. Two games run in ONE process could reuse another game's
  engine and give wrong N5-LZC runs.
- Fixed (box 77 push): the cache is now per game (g.__dict__["_n5lz_wc"], keyed by τ).
- Every tool of boxes 72-77 runs one game per process (wincmp.py runs two ENGINES on the SAME game), so no number in this note is affected.
  check.sh's box 72-76 pins pass unchanged.
