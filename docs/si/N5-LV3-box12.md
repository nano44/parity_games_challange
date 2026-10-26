# N5 box 12, part 1 (L-SI successor 7): "THR ⇒ M ≥ 0" in scope: Even's best reply to τ must use a (β) gate; what is left
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~14:50Z (date -u). Lead GO 14:18Z, box 12, item (1)(c):
"exclude an in-scope (β)-fallback, which gives THR ⇒ M ≥ 0. If that fails, record the exact obstruction." Lane write-up, unrefereed.
- Labels: PROVED (L-SI succ. 7); CONJECTURE; OPEN; DATA; READING.
- Everything is on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Result in one paragraph.
  - "THR ⇒ M ≥ 0" is NOT proved and NOT killed.
  - PROVED:
    - Lemma XG: if Even's optimal reply to τ leaves R into F and then stays in F, that exit edge is a gate of level ≥ r.
    - Lemma ANTI: a one-player "no improving edge used" lemma, from R36's Lemma P1.
  - With them: in setting (LV) with r ≥ 0, Even's optimal G_τ-play from x0 must pass a (β) gate (Corollary NEED-β). The one
    exception still open is a play whose cycle runs through o and is topped after o.
  - So a (β)-fallback is not just possible in shape. Its threat x0 is deficient only BECAUSE of (β) gates: Even's best reply to τ must
    use one.
  - DATA: 3,936 in-scope THR fallbacks (the two PERT-20 runs below: run states and perturbed start pairs), all with M ≥ 0. In the 519
    analysed with r ≥ 0, every optimal play from x0 passes a non-exceptional gate, as NEED-β predicts.

## 0. Objects and dependencies
- As in P-N5-LV §0 (packet sha1 d0d797f0) and P-N5-RL §0 (R37): S4a / S4c, Ξ, W, gates, levels, M_k, COARSE_L, (C1)-(C7), R̄ / R / F, (h),
  r, THR, phase, scope run, c, x0 := σ̄_k(o), t := τ(o) (P-N5-RL's e*).
- G_τ: the one-player game "Odd fixed to τ" (R37).
  - U := Opt(G_τ), the pointwise optimum (R37 / P-N5-RL's W*).
  - σ*: any optimal strategy of G_τ, so V_{σ*,τ} = U.
- G_σ̄: the one-player game "Odd fixed to σ̄_k". Only o has a choice in 𝒞^1O, so this is "o → x0".
  - σ_k's valuation in G_σ̄ is Ξ_k (SPEC S1: Ξσ is the valuation of σ against σ̄).
- An Even edge (v, u) of a one-player game with σ-valuation V is V-EXCEPTIONAL if:
  - v is its own V-cycle node,
  - u ≠ σ(v),
  - V(u) = (v, ∅, ·).
- Used:
  - R17 (a) F1: the optimum of a one-player game dominates every strategy pointwise.
  - R36 Lemma P1: in a one-player game, a positional Even strategy with no improving edge is optimal.
  - R37 (a) R-SAME, BL-FORM; R37 (b) BL (a)-(e), with BL's proof Steps 0, 1, 2a, 2b (P-N5-RL §2). R36 makes all of BL unconditional.
  - R31 P-OPT; R20 (b) FBL (u* ≠ none); R19 (a) Lemma G; (C1)-(C7) (R25, R29 (a)).
  - Lane, in review (P-N5-LV §1): LV-SHAPE.
- Setting (LV+): setting (LV) of P-N5-LV with r_k ≥ 0. That is:
  - k is an in-scope S4c fallback, THR at k with u* ≠ none, and M_k = −1;
  - by LV-SHAPE every gate is of kind (α) or (β), and (γ) is excluded by r ≥ 0.

## 1. Lemma XG (PROVED, L-SI succ. 7)
Let k be an in-phase THR S4c fallback with (h). Let y ∈ R_k be Even, s := σ_k(y), and z := σ*(y) ∈ F_k, where z's (σ*, τ)-play stays in
F_k. Then (y, z) is a gate at k of level ≥ r_k. In particular M_k ≥ r_k.
Proof.
- (i) U(z) = W(z) = Ξ(z).
  - Extend σ* on z's play by σ_k on the rest of F_k. This is a strategy of G_τ[F_k] with the same play from z.
  - So U(z) ⊴ Opt(G_τ[F_k])(z) = W(z) (BL (c)).
  - U(z) ⊵ W(z) (F1), and W(z) = Ξ(z) (Lemma G, z ∈ F).
- (ii) U(z) ⊵ W(s).
  - y's W-play reaches o, and its cycle avoids o (H2). So y is not on its own W-cycle, and W(y) = y ⊕ W(s).
  - z's σ*-play stays in F, so it avoids y ∈ R. So U(y) = y ⊕ U(z).
  - F1 gives U(y) ⊵ W(y), so y ⊕ U(z) ⊵ y ⊕ W(s).
  - y lies on neither play, so (C7) cancels y.
- (iii) Conclusion.
  - Lemma G: W(s) = π_s ⊕ w and Ξ(s) = π_s ⊕ θ.
  - (C7) gives π_s ⊕ w ▷ π_s ⊕ θ at level exactly r.
  - So Ξ(z) = U(z) ⊵ π_s ⊕ w ▷ Ξ(s): (y, z) is a gate.
  - (C5) gives lev(Ξ s, Ξ z) ≥ lev(π_s ⊕ θ, π_s ⊕ w) = r. □
- Note: CLU (R29 (a)) bounds every SWITCHED R → F edge by r from above. XG bounds Even's optimal-reply exits from below.

## 2. Lemma ANTI (PROVED, L-SI succ. 7; any one-player game)
Let H be a one-player game (only Even has choices), σ an Even strategy, and V its valuation. Suppose σ′ chooses, at every Even vertex
v, either an edge (v, u) with V(u) ⊴ V(σ v) or a V-exceptional edge. Then V_{σ′} ⊴ V pointwise.
Proof.
- Let T be the set of Even vertices that have a V-exceptional edge. For c ∈ T let z_c be a ⊴-best vertex among σ(c) and c's exceptional
  targets. Put σ_ex := σ[c ↦ z_c for c ∈ T].
- Step 1: V_{σ_ex} = V. This is BL Step 2b's argument (P-N5-RL §2, signed in R37), with V in place of W_k.
  - V(z_c) = (c, ∅, ·), so z_c's σ-play reaches c through vertices ranked below c.
  - It meets no other c′ ∈ T first: c′'s σ-play is its own cycle, which would make c′ its cycle node.
  - A play that first meets some c ∈ T agrees with its σ-play up to c, then runs on a cycle topped by c. Its value, measured to the first
    visit of the cycle node, is unchanged. A play meeting no c ∈ T is unchanged.
- Step 2: σ_ex is optimal in a restricted game.
  - Let H′ be H with each Even vertex v restricted to σ_ex(v), the edges (v, u) with V(u) ⊴ V(σ v), and v's V-exceptional edges.
  - σ_ex is a strategy of H′, and its valuation is V (Step 1). It has no improving edge in H′:
    - at v ∉ T, an allowed u has V(u) ⊴ V(σ v) = V(σ_ex v);
    - at c ∈ T, an allowed u has V(u) ⊴ V(σ c) or is an exceptional target, so V(u) ⊴ V(z_c).
  - By R36 Lemma P1 in H′, σ_ex is optimal in H′.
- σ′ is a strategy of H′. So V_{σ′} ⊴ V_{σ_ex} = V (F1 in H′). □
- Instance ANTI-Ξ: H := G_σ̄, σ := σ_k, V := Ξ_k. Gates are exactly the Ξ-improving edges.
  - In setting (LV+), every non-gate is allowed, and every (α) gate is Ξ-exceptional: y is its own Ξ-cycle node, Ξ(σ y) = (y, ∅, ·),
    and level −1 gives Ξ(z) = (y, ∅, ·).
  - So: a G_σ̄-strategy that agrees with σ_k except along (α) gates and non-gates has valuation ⊴ Ξ_k.
- Instance ANTI-W: H := G_τ, σ := σ_k, V := W_k. The W-improving edges at an in-phase THR fallback are the W-exceptional gates (BL Step 2a)
  and the BLOCKED edges (BL-FORM). So a G_τ-strategy that uses no blocked edge has valuation ⊴ W_k.

## 3. Corollary NEED-β (PROVED, L-SI succ. 7; one sub-case OPEN)
Setting (LV+). Let 𝒫 be the σ*-play from x0 in G_τ.
- (F) Facts used:
  - (F-a) U(x0) ⊵ U(t). (o, x0) ∉ Iτ_k (BL Step 1), and Iτ_k at o is {x : U(x) ◁ U(t)} (BL Step 0).
  - (F-b) U(t) ⊵ W(t) (F1), and W(t) ▷ W(x0) = Ξ(x0) at level r ((C7), from θ = o ⊕ Ξ(x0) ◁ w = o ⊕ W(t)).
  - (F-c) Hence U(x0) ▷ Ξ(x0), and lev(Ξ x0, U x0) ≥ r ≥ 0 ((C5)).
- Claim. 𝒫 uses an edge (y, σ*(y)) that is a (β) gate, in each of these cases:
  - (B) 𝒫 avoids o;
  - (A1) 𝒫 visits o, and its cycle avoids o;
  - (A2′) 𝒫's cycle K′ contains o, and its top m′ lies in λ ∪ {o}, where λ := 𝒫 before o;
  - (A2″) 𝒫's cycle K′ contains o, and rank m′ < rank m_K, where m_K := the top of λ ∪ {o}.
- OPEN, case (A2*): K′ contains o, m′ lies on the part of K′ after o (t and its successors before K′ closes), and every vertex of λ ∪ {o}
  ranks below m′.
Proof. Suppose 𝒫 uses no (β) gate. Every σ*-edge on 𝒫 is then a non-gate or an (α) gate (setting (LV+)).
- (B) 𝒫 avoids o, so it is also a G_σ̄-play.
  - Let σ′ := σ* on 𝒫's Even vertices and σ_k elsewhere. By ANTI-Ξ, U(x0) = V^{G_σ̄}_{σ′}(x0) ⊴ Ξ(x0), against (F-c).
- (A1) Write 𝒫 = λ, o, then 𝒬 (the play from t). 𝒬 avoids o and λ, since the cycle avoids o.
  - First, U(t) = W(t).
    - 𝒬 is a G_σ̄-play without (β) gates. So ANTI-Ξ gives U(t) ⊴ Ξ(t) = W(t) (t ∈ F by H2; Lemma G).
    - F1 gives the reverse.
  - Next, the loop K := λ ∪ {o}.
    - Let σ″ := σ* on λ's Even vertices and σ_k elsewhere. In G_σ̄ its play from x0 is the cycle K (o → x0 is σ̄'s edge).
    - Its value at x0 is (m_K, ∅, ·), and ANTI-Ξ gives (m_K, ∅, ·) ⊴ Ξ(x0) = (c, ·, ·). So rew(m_K) ≤ rew(c), with equality only if
      m_K = c.
    - m_K ≠ c: if c ∈ λ, then 𝒬, whose value has cycle node c, would revisit c, so 𝒫's cycle would contain o.
    - So rew(m_K) < rew(c).
  - Now compare with U.
    - U(x0) = K ⊕ U(t) = K ⊕ W(t), since K is disjoint from 𝒬, and P(U t) = P(W t) lies on 𝒬.
    - (F-a) gives K ⊕ W(t) ⊵ W(t). Both have cycle node c. Let H := the vertices of K ranked above c. Then:
      - if H ≠ ∅, its top is m_K and must be even. So m_K is even and ranked above c, and rew(m_K) > rew(c);
      - if H = ∅, the comparison is by length (|K| ≥ 1 more), so c is odd. m_K ranks below c, so again rew(m_K) > rew(c).
    - Either way this contradicts rew(m_K) < rew(c).
- (A2′, A2″) K′ = (λ's part from the re-entry vertex v) ∪ {o, t} ∪ (the part after t). Its top is m′.
  - U(x0) and U(t) both have cycle node m′. U(t) ⊵ W(t) gives rew(m′) ≥ rew(c), with equality only if m′ = c.
  - σ″ as in (A1) gives rew(m_K) ≤ rew(c), with equality only if m_K = c.
  - (A2′) If m′ ∈ λ ∪ {o}, then m′ ∈ K, so rank m_K ≥ rank m′.
    - If m_K = m′, then rew(m′) ≤ rew(c) ≤ rew(m′), so m′ = c ∈ λ.
      - t lies on K′, whose top is c, so U(t) = (c, ∅, ·).
      - U(t) ⊵ W(t) = (c, P(W t), ·) gives ∅ ⊵ P(W t) as path sets.
      - σ″ gives (c, ∅, ·) ⊴ Ξ(x0) = (c, P(Ξ x0), ·), so ∅ ⊴ P(Ξ x0).
      - But P(W t) ▷ P(Ξ x0) (F-b, level r ≥ 0). So ∅ ⊵ P(W t) ▷ P(Ξ x0) ⊵ ∅: contradiction.
    - If rank m_K > rank m′, this is case (A2″).
  - (A2″) rank m_K > rank m′. Then m_K lies on λ before the re-entry vertex v, because every vertex of K′ ranks at most m′.
    - P(U t) = ∅ (t is on the cycle), and P(U x0) = (the vertices of λ before v ranked above m′), whose top is m_K.
    - (F-a) U(x0) ⊵ U(t) forces m_K to be even.
    - Then rew(m_K) ≤ rew(c) forces c to be even with rank c ≥ rank m_K > rank m′. But rew(m′) ≥ rew(c) with m′ ranked below the even
      c is impossible.
- (A2*) is not reached by these arguments. □
**Reading.** NEED-β does not exclude a (β)-fallback; it locates one. If M = −1 at an in-scope THR fallback with r ≥ 0, then:
- Even's best reply to τ from the threat x0 must cross R → F along a (β) gate (y, z): Ξ(z) beats Ξ(σ y) by length only, while W(σ y)
  beats W(z) at level r;
- or that reply must cycle through o, topped after o (A2*).
At every (β) exit z of such a reply: U(z) ⊵ W(σ y) ▷ W(z), by XG's step (ii). So z is again deficient, and its own reply needs another
(β) gate or (A2*). The reply's cycle therefore carries a (β) gate (or is of kind A2*).

## 4. The exact obstruction for "THR ⇒ M ≥ 0" (for L-RED: the shape a killer must have)
A counterexample is an in-scope THR fallback with r ≥ 0, every gate of level −1, and at least one (β) gate (so rank o < rank c). Even's
optimal G_τ-reply σ* from x0 then:
- (i) leaves F along a blocked edge (q, e): π_e ⊕ θ ⊴ Ξ(σ q) ◁ π_e ⊕ w (BL (e), BL-FORM);
- (ii) never ends in F after a last R → F step (XG);
- (iii) crosses back R → F along a (β) gate, possibly several times, and its cycle carries a (β) gate (NEED-β); or it is of kind (A2*).
Two further consequences when c is odd, both PROVED by the σ″ argument of §3 applied to the prefix up to the first blocked edge:
- The loop L := (𝒫 up to q) ∪ {e} ∪ π_e ∪ {o} has top m_L with rew(m_L) ≤ rew(c).
  - So either 𝒫 passes c before its first blocked edge (m_L = c),
  - or L has a vertex ranked above c, and its top is odd.
  - (With c odd, every vertex ranked below c beats c.)
- If 𝒫 passes c, then t's own reply can follow W's route to c and then copy 𝒫 from c. Since t's route carries the level-r vertex of
  P(w), this should give U(t) ▷ U(x0), i.e. x0 ∈ Iτ, and so no fallback. READING, not a proof: positional consistency of the copied
  tail is the gap.
  - My hand-built candidate failed exactly there: experiments/si/lv/hand9.py (9 vertices, c odd, low cycle {5, 8}).
  - The engine shows it is not a fallback at all: (5, 8) is a gate, Iτ = {(0, 4)} (x0 ∈ Iτ), and Even's best reply to τ cycles through
    o, topped by the level-r vertex h = 2.
CONJECTURE (unchanged): in scope, THR ⇒ M ≥ 0.

## 5. DATA (DATA, not proof)
Scripts (logs in experiments/si/lv/logs/):
- experiments/si/lv/betasearch.py: in-scope THR fallbacks, at run states and at perturbed start pairs (SPEC allows a start pair).
- experiments/si/lv/xg.py: XG, the kind of 𝒫, and NEED-β's analogue at any M (𝒫 passes a non-exceptional gate).

| corpus | THR fallbacks (run / perturbed) | M ≥ 0 | rank o < rank c | with an R → F gate |
| --- | --- | --- | --- | --- |
| NAMED (102 files, experiments/si/lv/named.lst: coarse/named.txt, coarse/instances, riselast/instances, red/so/instances), PERT 20 | 387 / 1,205 | all | not measured | not measured |
| NAMED, PERT 3 (seed 3) | 387 / 181 | all | 165 / 84 | all |
| LIB (experiments/new/box33/lib.txt, 234), PERT 20 | 526 / 1,818 | all | not measured | not measured |
| random 𝒞^1O, n 8-18, 40,000 random start pairs × 2 generators | 0 | — | — | — |

- Random 𝒞^1O games give no in-scope THR fallback at all: the corpus instances are built for them.
- xg.py (NAMED, PERT 2): 519 THR fallbacks with r ≥ 0.
  - XG's hypothesis occurs 0 times, so XG is vacuous in data.
  - Kind of 𝒫: 311 avoid o (B); 123 are (A1); 85 have the cycle through o (A2-type).
  - Every one of the 519 plays passes a non-exceptional gate. This is the analogue of NEED-β at the data's M ≥ 0; (A2) is included.
  - For the 187 (B)-type plays with M < r, the cycle's top has rank ≤ r (the COARSE_r reading of Lemma CR, below).
- Lemma CR (PROVED, used only for the last check). Assume r ≥ 0 and M < r. Then for every Even edge (v, u),
  COARSE_r(W u) ⊴ COARSE_r(W σ v). By kind of edge:
  - F → F: by the gate level;
  - R → F: from Ξ(u) ⊴_r π ⊕ θ, together with COARSE_r(π ⊕ θ) = COARSE_r(π ⊕ w);
  - R → R̄: FBL, then R-SAME;
  - F → R̄: no gate (FBL), so Ξ(u) = π_u ⊕ θ ⊴ Ξ(σ v) and COARSE_r(π_u ⊕ w) = COARSE_r(π_u ⊕ θ).
  The step from CR to "the cycle's top has rank ≤ r" passes through a coarse anti-improvement, which can fail when switches jointly
  close a new cycle. So that statement is DATA, not proved.
