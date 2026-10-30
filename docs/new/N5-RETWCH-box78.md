# N5-RETWCH (box 78): every Even RETURN in a W-run is paid by a W-change of its target (N5-LZC), or by that or a tie-leave (N5). So the W-run length reduces to per-vertex W-changes
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 07:56Z (read 08:28Z; box 77 had already been used for the 07:23Z pair
potential brief): «BOX 77: GO. Prove RETE(v, e) ≤ WCH_F(e) for N5-LZC first, then for N5 with the TIE term … State it as a reduction,
not a bound. After BOX 77, write a handover and PARK.» This is that box, numbered 78. Written 08:29Z-08:37Z (date -u). Working note,
unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
- Read first, as asked: L-LIT T51 (l-lit 09eed297, docs/lit/T51-parametric-best-reply.md, Summary and §3-§4). Its findings: no source
  bounds the opponent's best-reply count along an SI run; thetaA_n7 is one-parametric (SEGRET 0); arbitrary monotone costs bound nothing.
  No T51 theorem is used below.
- Definitions:
  - W-run F = [a, b]: as in R89 (τ fixed, no S4c, σ changes at every transition, λ_W fixed). W := val(σ, τ_F).
  - A RETURN of Even v to e at transition u: σ_{u+1}(v) = e ≠ σ_u(v), and v held e at some earlier state of F. Its LEAVE is v's last
    leave of e before u, at transition k < u: σ_k(v) = e ≠ σ_{k+1}(v).
  - RET_F(v, e): the returns of v to e in F.
  - WCH_F(e): the transitions of F at which W(e) changes. By F1, W only rises on a W-run (σ_t is a strategy of H_t), so these are strict
    rises.
  - TIE-LEAVE: a leave at k with e still W_{k+1}-CONSISTENT at v. That means v ⊕ W_{k+1}(e) = W_{k+1}(v) if v is off its own W-cycle
    node, or W_{k+1}(e) = (v, ∅, ·) if v is its own W-cycle node (the two forms of Lemma TIE, box 72 §2). TL_F(v, e) counts them.
- Tool: box78/retwch.py; run.sh gives retwch_*.txt (1132 runs × N5 and N5-LZC).

## 1. Theorem RET-WCH (PROVED, lane)
- Statement. For every W-run F, Even v and successor e: RET_F(v, e) ≤ WCH_F(e) + TL_F(v, e).
- In N5-LZC, TL_F ≡ 0, so RET_F(v, e) ≤ WCH_F(e). Reason: the lazy rule keeps σ_t(v) whenever it is consistent in either form (box 72
  §3, --lzc). By LZ-OPT the rule's W* is W_{k+1}.
- Premises:
  - F1 ([R17 (a)]: S4a's σ_{t+1} is an optimum of H_t, and both σ_t and σ_{t+1}[v ↦ e] are strategies of H_t);
  - [V1], [V2];
  - λ_W constant on F (R89's W-run).
  For N5-LZC, F1 holds by LZ-OPT. No OPT-ONLY transfer of a fleet lemma is needed: the proof uses F1 directly.
- Proof. Fix a return u with leave k. If the leave is a tie-leave, charge the return to it. Otherwise suppose, for contradiction, that W(e)
  is constant on the states [k + 1, u + 1].
  - Cycle-node case. λ_W is fixed on F, so v is its own W-cycle node at every state of F or at none.
    - If it is, then at u + 1, σ_{u+1}(v) = e lies on v's cycle, so W_{u+1}(e) = (v, ∅, ·).
    - So W_{k+1}(e) = W_{u+1}(e) = (v, ∅, ·), and the leave is a tie-leave (form (b)): a contradiction.
  - Off-cycle case. v is never its own W-cycle node on F. Let c := λ_W(v), fixed on F. Let π be e's σ_{k+1}-play and ρ := σ_{k+1}[v ↦ e]
    ∈ H_k.
    - (i) π never visits v. Then val_ρ(v) = v ⊕ W_{k+1}(e), and F1 gives ⊴ W_{k+1}(v). The leave is not a tie-leave, so the two values
      differ: v ⊕ W_{k+1}(e) ◁ W_{k+1}(v).
    - (ii) v lies on π's cycle. Then the cycle node is c and W_{k+1}(v) = (c, ∅, ·).
      - If P(W_{k+1}(e)) = ∅, ρ closes a cycle with top c and val_ρ(v) = v ⊕ W_{k+1}(e). Then ⊴ (F1) and ≠ (not a tie-leave) give ◁.
      - Otherwise the top u′ of P(W_{k+1}(e)) tops ρ's cycle. F1 forces u′ odd (an even vertex more relevant than c would beat c). So
        v ⊕ W_{k+1}(e) ◁ (c, ∅, ·) = W_{k+1}(v).
    - (iii) v lies on π's path part, before its cycle: e = x_0 … x_q = v, q ≥ 1. This case is impossible.
      - Here W_{k+1}(e) = (c, R ∪ P(W_{k+1}(v)), ℓ(W_{k+1}(v)) + q), with R the vertices x_i, i < q, more relevant than c.
      - At u + 1, v is off-cycle with σ_{u+1}(v) = e, so [V1] gives W_{u+1}(v) = v ⊕ W_{u+1}(e) = v ⊕ W_{k+1}(e) =
        (c, P(W_{k+1}(v)) ∪ R, ℓ(W_{k+1}(v)) + q + 1).
      - Let u* be the most relevant vertex of {x_0, …, x_q}. ρ's v-play is that cycle, with top u*.
      - If v is more relevant than c, then v ∈ P(W_{k+1}(e)) = P(W_{u+1}(e)). So v lies on e's σ_{u+1}-path, while σ_{u+1}(v) = e:
        e's play returns to e before reaching c, and the cycle then contains v, which is more relevant than c. Contradiction. So v is less
        relevant than c, and u* ≠ v when u* is more relevant than c.
      - If u* is more relevant than c, F1 forces u* odd.
        - If u* ∉ P(W_{k+1}(v)), the new top element u* is odd, so W_{u+1}(v) ◁ W_{k+1}(v), against F1-monotonicity.
        - If u* ∈ P(W_{k+1}(v)), then u* lies on v's σ_{k+1}-path and v on u*'s, so u* and v share a cycle with top c, against u*
          being more relevant than c.
      - If u* is less relevant than c, then R = ∅ and W_{u+1}(v) has W_{k+1}(v)'s path set and is longer.
        - If c is even, that is ◁, against monotonicity.
        - If c is odd, ρ's cycle top u* beats c (R2 of box 72 §2), against F1.
    - From (i) / (ii): W_{u+1}(v) = v ⊕ W_{u+1}(e) ([V1], v off-cycle at u + 1) = v ⊕ W_{k+1}(e) ◁ W_{k+1}(v) ⊴ W_{u+1}(v) (F1 at each
      S4a step of [k + 1, u]). That is a contradiction.
  - So W(e) changes at some transition s ∈ [k + 1, u].
  - Distinctness: for consecutive returns u₁ < u₂ of (v, e), the leave k₂ of u₂ satisfies k₂ ≥ u₁ + 1, so the intervals [k + 1, u] are
    disjoint. Different returns use different leaves. □

## 2. Corollary RUN-WCH (PROVED, lane): the W-run length reduces to per-vertex W-changes
- By box 76's NEW-BOUND, |F| ≤ m_E + RETR_F ≤ m_E + Σ_{(v,e)} RET_F(v, e). Hence:
  - N5-LZC: |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) ≤ m_E·(1 + max_e WCH_F(e)).
  - N5: |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TL_F.
- With box 74's RHO-LEN, ρ_F ≤ |Q|·|F|, so ρ per W-run is poly once per-vertex WCH per W-run is.
- This is a REDUCTION, not a bound: WCH_F(e) ≤ |F| trivially.
- The ONE-PREMISE reading (as the Lead asked):
  - A W-run and a phase each lie inside one τ-stretch. Every W-change counted here is at an S4a step (W-runs hold no S4c).
  - So the single premise [P-WCHτ] «for every τ-stretch and vertex e, the S4a transitions at which W(e) rises are poly(n)» implies:
    - RUN-WCH's hypothesis: W-run length, ρ per W-run, and with them REP* via L-SI's FW-R*′ / GAP-CLIMB;
    - GAP-RED's per-vertex WCH^S4a premise (per phase).
  - So REP* and GAP-RED share one premise. Not proved, and not refereed.

## 3. DATA (1132 runs × 2; retwch_*.txt)
| engine | returns | paid by a W(e)-change | paid by a tie-leave | UNPAID | per-edge violations |
| --- | --- | --- | --- | --- | --- |
| N5-LZC | 6100 | 6100 | 0 | 0 | 0 |
| N5 | 6265 | 6179 | 86 | 0 | 0 |
- Max returns per (W-run, edge): 17 (new/box52/out/topfix_n10, n 210).
- First run: 2 N5 returns on red/so tog6b_n32 looked UNPAID, because the check knew only the off-cycle consistency form. There v 13 is its
  own W-cycle node, (13, ∅, 0), and goes 21 → 29 → 21 with W(21) = (13, ∅, 8) fixed: a cycle-node tie-leave (form (b)). The check was
  extended to both forms, and the proof covers it (cycle-node case).

## DONE / FINDINGS / NEEDS
- DONE: box78/retwch.py, run.sh, retwch_*.txt; this note; check.sh "box 78" (pins tog6b_n32 and runfam_K10).
- FINDINGS:
  1. PROVED (lane): Theorem RET-WCH. In a W-run, RET_F(v, e) ≤ WCH_F(e) + TL_F(v, e), and TL ≡ 0 in N5-LZC. DATA: 0 unpaid in 12365
     returns.
  2. PROVED (lane): Corollary RUN-WCH. |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) (+ TL_F for N5). The REDUCTION puts the W-run length, ρ per
     W-run and REP* on per-vertex W-changes.
  3. READING: one premise [P-WCHτ] (per-vertex S4a W-rises per τ-stretch) implies both RUN-WCH's hypothesis and GAP-RED's WCH^S4a.
- NEEDS: none from the owner. Lead: this was my last box; handover in notes/L-NEW.md (FINAL resume point). PARKING.
