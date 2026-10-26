# Referee packet P-N5-NEEDB: Even's best reply needs a (β) gate (XG, ANTI, NEED-β with the A2* closure); OLD-THREAT; case (i) ⇐ INTO (box 13)
L-SI successor 8 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~17:55Z (date -u), at the Lead's request (17:39Z, 17:48Z;
Lead's stamps). Frozen at its commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, dependencies and their status, and the data with the scripts.
- Source texts (lane write-ups, frozen): docs/si/N5-LV3-box12.md (sha1 20ba05d7, L-SI succ. 7) §0-§3; docs/si/N5-A2STAR-box13.md
  (sha1 2a85601d) §1; docs/si/N5-RISE-box13.md (sha1 3b8fea13) §0-§2. Where they differ, this packet governs. §1-§3 here are N5-LV3
  §1-§3 verbatim, apart from the statuses and the (A2*) case.
- Labels: PROVED (by whom), unrefereed; CONJECTURE; DATA. Everything is on 𝒞^1O (one Odd vertex o with out-degree > 1; scripts assert it).
- Lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
  NEED-β does not prove "THR ⇒ M ≥ 0" (CONJECTURE, §5): it locates any counterexample's (β) gate.
- Statements to sign:

| § | statement | label | landed results used | hypothesis occurs in data? |
| --- | --- | --- | --- | --- |
| §1 | Lemma XG | PROVED (L-SI succ. 7) | R36 (via R37 BL (c)), R37, R19, (C5), (C7) | no: 0 cases (N5-LV3 §5, xg.py) — vacuous |
| §2 | Lemma ANTI (any one-player game), instances ANTI-Ξ, ANTI-W | PROVED (L-SI succ. 7) | R36 Lemma P1, R17 F1, R37 BL Step 2b, BL-FORM | general lemma; its instances are used only inside §3 |
| §3 | Corollary NEED-β, cases (B), (A1), (A2′), (A2″) | PROVED (L-SI succ. 7) | R36, R37 BL Steps 0-1, R41 (a) LV-SHAPE, F1 | no: setting (LV+) occurs 0 times in the lane's and the referees' data with a saved witness (REFEREE-2 reports 645 level −1 block fallbacks with r ≥ 0, none saved) — vacuous |
| §3 | Corollary NEED-β, case (A2*) | PROVED (L-SI succ. 8) | as above | no: 0 A2* shapes among 82 cycle-through-o plays (a2star.py) — vacuous |
| §4.1 | Lemma OLD-THREAT | PROVED (L-SI succ. 8) | R15 (a), R18 (d), R19 (a), R29 (c), (e), R31, R40 (b) | yes: 562 post-rise states, 0 failures |
| §4.2 | Reduction: INTO ⇒ no case (i) fallback | PROVED (L-SI succ. 8) | R20 (b) FBL | its conclusion matches all data; INTO itself is a CONJECTURE (425 / 425) |

- §5 is NOT TO SIGN: CONJECTURE INTO; CONJECTURE "THR ⇒ M ≥ 0"; case (ii) of the rise question (OPEN); the reading after NEED-β; the
  dead conjectures RISE-DROP, GATE-ABOVE, FEED (FALSE, recorded for the referees' information). §6: data.
- Dependency statuses (all LANDED on trunk): R36 (P-N5-P1, Lemma P1 = (P) for one-player games); R37 (P-N5-RL: R-SAME, BL-FORM, BL (a)-(e)
  with Steps 0, 1, 2a, 2b; unconditional given R36); R41 (P-N5-LV: LV-SHAPE, LV-CN, LV-COUNT). Also R15, R17-R20, R25, R29, R31, R40.

## 0. Objects and dependencies (as in N5-LV3 §0; statuses updated)
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
  - RESULTS R41 (a) (P-N5-LV §1, LANDED): LV-SHAPE.
- Setting (LV+): setting (LV) of P-N5-LV with r_k ≥ 0. That is:
  - k is an in-scope S4c fallback, THR at k with u* ≠ none, and M_k = −1;
  - by LV-SHAPE every gate is of kind (α) or (β), and (γ) is excluded by r ≥ 0.


## 1. Lemma XG (PROVED, L-SI succ. 7; no (P) beyond R36)
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


## 3. Corollary NEED-β (PROVED: L-SI succ. 7 for (B), (A1), (A2′), (A2″); L-SI succ. 8 for (A2*))
Setting (LV+). Let 𝒫 be the σ*-play from x0 in G_τ.
- (F) Facts used:
  - (F-a) U(x0) ⊵ U(t). (o, x0) ∉ Iτ_k (BL Step 1), and Iτ_k at o is {x : U(x) ◁ U(t)} (BL Step 0).
  - (F-b) U(t) ⊵ W(t) (F1), and W(t) ▷ W(x0) = Ξ(x0) at level r ((C7), from θ = o ⊕ Ξ(x0) ◁ w = o ⊕ W(t)).
  - (F-c) Hence U(x0) ▷ Ξ(x0), and lev(Ξ x0, U x0) ≥ r ≥ 0 ((C5)).
- Claim. 𝒫 uses an edge (y, σ*(y)) that is a (β) gate. The cases are exhaustive:
  - (B) 𝒫 avoids o;
  - (A1) 𝒫 visits o, and its cycle avoids o;
  - (A2′) 𝒫's cycle K′ contains o, and its top m′ lies in λ ∪ {o}, where λ := 𝒫 before o;
  - (A2″) 𝒫's cycle K′ contains o, and rank m′ < rank m_K, where m_K := the top of λ ∪ {o}.
  - (A2*) K′ contains o, m′ lies on the part of K′ after o (t and its successors before K′ closes), and every vertex of λ ∪ {o}
    ranks below m′.
  (If K′ contains o, then m′ lies in λ ∪ {o} (A2′) or after o; after o, either some vertex of λ ∪ {o} ranks above m′ (A2″) or none
  does (A2*).)
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
- (A2*) (L-SI succ. 8; N5-A2STAR-box13.md §1). Under the assumption (no (β) gate on 𝒫), case (A2*) is impossible.
- Step 1: m′ is odd.
  - U(t) = (m′, ∅, ℓ_t), with ℓ_t the number of steps from t to m′ along K′. Every vertex of K′ ranks at most m′.
  - U(x0) = (m′, ∅, ℓ_{x0}). The play from x0 meets m′ only after λ, o and t: m′ lies after o, and λ ∪ {o} does not contain it.
    - Its vertices before m′ are λ, o and K′'s vertices from t to m′, and all of them rank below m′. So the path set is ∅.
    - ℓ_{x0} = |λ| + 1 + ℓ_t > ℓ_t (|λ| ≥ 1, as x0 ∈ λ).
  - (F-a) gives U(x0) ⊵ U(t). With equal cycle nodes and equal (empty) path sets, the order is by length. The longer value is ⊵ only if
    the cycle node is odd (SPEC S1). So m′ is odd.
- Step 2: c = m′, or c is odd with rank c > rank m′.
  - F1 gives U(t) ⊵ W(t) = (c, P(W t), ·).
  - If m′ ≠ c, this forces rew(m′) > rew(c). With m′ odd, rew(m′) = −pp(m′) < 0. So rew(c) < −pp(m′), which forces c odd and
    pp(c) > pp(m′), i.e. rank c > rank m′.
- Step 3: contradiction with σ″.
  - σ″ (σ* on λ's Even vertices, σ_k elsewhere) is the strategy of N5-LV3 §3 (A1). It uses on λ only σ*-edges, which by the assumption
    are non-gates or (α) gates. In G_σ̄ its play from x0 is the cycle K = λ ∪ {o}, with top m_K.
  - ANTI-Ξ gives (m_K, ∅, ·) ⊴ Ξ(x0) = (c, ·, ·), so rew(m_K) ≤ rew(c), as in (A2′) / (A2″).
  - rank m_K < rank m′ ≤ rank c, so m_K ≠ c. By Step 2, c is odd.
  - So rew(m_K) ≥ −pp(m_K) > −pp(c) = rew(c). This contradicts rew(m_K) ≤ rew(c). □
- Remark. Steps 1-2 use only (F-a) and F1; the "no (β) gate" assumption enters only in Step 3, through σ″.
  - Successor 7's unchecked idea (ANTI-W on K′, "a blocked edge on K′ unless m′ = c") is true but not needed.
  - The parity of m′ already decides the case.

## 4. Lemma OLD-THREAT and the reduction "case (i) ⇐ INTO" (PROVED, L-SI succ. 8)
Source: docs/si/N5-RISE-box13.md §0-§2 (sha1 3b8fea13). Additional dependencies: RESULTS R15 (a), R18 (d) Lemma S (a), R19 (a) Lemma G,
R20 (b) FBL, R29 (c) OFFGATE, (e) NL, R31 FLAT-ALL (iii), R40 (b) Lemma FZ's proof. No (P), no ENT-X.
Objects as in RESULTS R31, R35, R40 (scope run S, fallbacks, gates, M_k, lev, COARSE_L, (C1)-(C7), θ, w, r, R̄ / R / F, (h), THR, (A_s)).
- RISE SETTING (R2-N5-ENT rise_end.py's definition):
  - k0 is an in-scope fallback of S with L := M_{k0} ≥ 0.
  - j > k0 is the first S4a step after k0 that changes COARSE_L(θ). Between k0 and j there is no fallback, every transition is in S,
    and r > L.
  - A POST-RISE STATE is a state t > j such that every transition s → s+1 with k0 < s < t is an in-scope S4a step with r_s > L.
- TARGET (REFEREE-2's DATA observation, R2-N5-ENT §6): after a rise, the scope run S has no further fallback.
  - Case (i): a later fallback k with r > L on [k0+1, k]. Then k is a post-rise state, and the transition k → k+1 lies in S.
  - Case (ii): r drops to ≤ L at some state before the next fallback.

### 4.1 Lemma OLD-THREAT
Let t be a post-rise state. Let x be an exit of o (x ≠ o) with x ∈ F_{k0} and COARSE_L(o ⊕ Ξ_{k0} x) = COARSE_L(θ_{k0}). Then x ∈ R_t.
In particular, the k0-threat x_{k0} := σ̄_{k0}(o), which is in F_{k0} by H1, lies in R_t.
Proof. Suppose x ∈ F_t.
- FREEZE (Lemma FZ's proof, R40 (b), with the fallback k replaced by t; FZ's proof never uses that k is a fallback).
  - Each s ∈ [k0, t − 1] is the source of a transition of S, so (h) holds there.
  - (A_s) holds on [k0+1, t − 1]: OFFGATE at k0+1, then NL (iii).
  - NL (ii) at each S4a step gives F_{s+1} ⊆ F_s, so x ∈ F_s for every s ∈ [k0+1, t].
  - Across k0, FLAT-ALL (iii) (R31; M_{k0} = L ≥ 0, (h) at k0 and k0+1) gives COARSE_L(Ξ_{k0+1} x) = COARSE_L(Ξ_{k0} x).
  - At each S4a step s → s+1 with k0 < s < t, NL (i) (r_s > L, (A_s), x ∉ R̄_{s+1}) gives COARSE_L(Ξ_{s+1} x) = COARSE_L(Ξ_s x).
  - Hence COARSE_L(Ξ_t x) = COARSE_L(Ξ_{k0} x).
- SANDWICH.
  - x ∈ F_t, so x's (σ_t, τ_t)-play avoids o. o is the only Odd vertex with a choice, so this is x's play under σ_t and every Odd
    strategy.
  - Lemma S (a) (R18 (d)), with Odd choosing x at o, gives θ_t ⊴ o ⊕ W_t(x) = o ⊕ Ξ_t(x) (Lemma G, R19 (a): Ξ = W off R̄).
  - (C1), and (C7) through o ⊕ (o lies on neither path), give
    COARSE_L(θ_t) ⊴_L COARSE_L(o ⊕ Ξ_t x) = COARSE_L(o ⊕ Ξ_{k0} x) = COARSE_L(θ_{k0}).
- MONOTONICITY. θ is ⊴-monotone (R15 (a)), so COARSE_L(θ) is ⊴_L-monotone (C1).
  - The rise at j ∈ (k0, t) is a strict step, and it cannot be undone (C3; as in (Σ6)). So COARSE_L(θ_t) ▷_L COARSE_L(θ_{k0}).
  - This contradicts the sandwich. So x ∈ R̄_t ∖ {o} = R_t. □
- Reading. A rise happens only because Odd's L-best exits at k0 have all been absorbed into R. Odd's new threat is a different exit whose
  COARSE_L value has been frozen since k0.
- DATA (experiments/si/lv13/oldthreat.py, REFEREE-2's traces imported read-only; logs experiments/si/lv13/logs/oldthreat_lib*.txt):
  - REFEREE-2's 295-file 𝒞^1O library (R2-N5-ENT/files.lst), S3 + 2 random starts, own + spec traces: 137 rises, 562 post-rise
    states, 0 failures;
  - 12 climb seeds (REFEREE-2's rise / LV climbs and my box-13 bests): 30 rises, 40 states, 0 failures.
  - The script's minimality test is COARSE_L(Ξ_{k0} x) = COARSE_L(Ξ_{k0} x_{k0}), which is equivalent by (C7).

### 4.2 Reduction: case (i) ⇐ CONJECTURE INTO (the reduction is to sign; INTO is NOT)
**CONJECTURE INTO.** At every post-rise state t with r_t > L, some gate (y, z) has z ∈ R̄_t.
**Reduction.** INTO implies that case (i) never occurs.
- Proof. Let k be a case (i) fallback. It is an in-phase S4c fallback with (h) at k and r_k > L ≥ 0, so THR with u* ≠ none.
- FBL (R20 (b), strong form) then says: no F → R̄ and no R → R̄ gate at k. So every gate at k has its target in F_k.
- k is a post-rise state with r_k > L, so this contradicts INTO. □
- This uses neither ENT-X nor (P). Compare R40: ENT-X excludes case (i) with M_k = L; INTO would also exclude M_k < L.
- DATA: INTO held at all 425 post-rise states with r > L in the library, 0 failures (logs/oldthreat_lib4.txt).
  - In 241 of them some gate into R̄ has level > L.
  - In the other 184, every gate has level ≤ L (GATE-ABOVE is FALSE, §5).
  - The INTO gates are F → R̄ (absorptions) or R → R̄ (route improvements).
- Why it stalls (OPEN). An R → R̄ gate is a pure route comparison. Ξ(z) = π_z ⊕ θ against Ξ(σ y) = π_{σy} ⊕ θ, so it is W-improving
  exactly when it is Ξ-improving. An F → R̄ gate (y, z) is always W-improving under THR: W(σ y) = Ξ(σ y) ◁ π_z ⊕ θ ◁ π_z ⊕ w = W(z)
  (Lemma G, (C7)).
  - So INTO says: after a rise, while r > L, Even always has a W-improving switch onto o's region.
  - The data shows absorption chains: each S4a step puts a new vertex into R̄, and its Even predecessor gains a gate into it
    (tevlast7_n32, s = 18-40; §5).
  - I found no argument that the chain cannot stop with r > L. Nothing above links "a vertex entered R̄ at t − 1" to "some Even
    predecessor gains".
- Case (ii) (r ≤ L before the next fallback): OPEN. Not attempted beyond the data (REFEREE-2: no fallback there either).


## 5. NOT TO SIGN
- CONJECTURE INTO: at every post-rise state t with r_t > L, some gate (y, z) has z ∈ R̄_t. DATA 425 / 425 (§6). With §4.2 it would exclude
  case (i). L-RED box 41 is attacking it (Lead 17:25Z).
- OPEN: case (ii) of the rise question (r ≤ L before the next fallback).
- CONJECTURE "in scope, THR ⇒ M ≥ 0" (N5-LV3 §4-§5). Reading after NEED-β: a counterexample's threat x0 has a best reply to τ that crosses
  R → F along a (β) gate, and so does the reply of every (β) exit (XG step (ii): U(z) ⊵ W(σ y) ▷ W(z)). There is no (A2*) branch any more.
- FALSE (instances; docs/si/DEAD.md, box 13): RISE-DROP (experiments/red/so/instances/tevlast7_n32.pg, sha1 d905038c), GATE-ABOVE
  (rise_thin51_n40.pg, sha1 47aaf46e), FEED (tevlast11_n40.pg, sha1 8421ab30). None of them is used above.

## 6. DATA (DATA, not proof)
- §1-§3: experiments/si/lv/xg.py (N5-LV3 §5; log experiments/si/lv/logs/) and experiments/si/lv13/a2star.py (log
  experiments/si/lv13/logs/a2star_named.txt), on NAMED (experiments/si/lv/named.lst) with run states and perturbed start pairs:
  - 519 in-scope THR fallbacks with r ≥ 0, all with M ≥ 0 (so (LV+) occurs 0 times); XG's hypothesis 0 times;
  - in the analogue at M ≥ 0, every U-play from x0 passes a non-exceptional gate (311 (B), 123 (A1), 85 with the cycle through o);
  - 82 cycle-through-o plays in the a2star run, 0 of A2* shape.
  - So §1-§3 rest on their proofs.
- §4: experiments/si/lv13/oldthreat.py (REFEREE-2's traces imported read-only: docs/referee-2/R2-N5-OUT, -FRZ, -ENT, -RE), on REFEREE-2's
  295-file 𝒞^1O library (docs/referee-2/R2-N5-ENT/files.lst), S3 + 2 random starts, own + spec traces; logs
  experiments/si/lv13/logs/oldthreat_lib*.txt:
  - 137 rises, 562 post-rise states: OLD-THREAT 0 failures; 425 states with r > L: INTO 425 / 425;
  - 12 climb seeds: 30 rises, 40 states, 0 failures.
  - REFEREE-2's R2-N5-ENT §6 (own code): no rise is followed by a fallback of its scope run (library and 26,665 climb rises).

