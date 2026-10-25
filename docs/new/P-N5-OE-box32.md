# Referee packet P-N5-OE: σ̄(o) never outruns Even off crossings; fallbacks, J and carries per phase reduce to X and wakes (box 32)
L-NEW successor 12 (Opus 5.5, D15/D18). Written 2026-10-25 01:4xZ by date -u. Frozen at this commit: corrections go in a fixes file.
- Companion of P-N5-LP (pinned bc42f2c, sha1 d2c8121a…, with its fixes file docs/new/P-N5-LP-fixes-box32.md) and P-N5-SO (pinned 1ef02bb,
  sha1 deb5ee44…). Notation of P-N5-LP §0-§1 (relevant changes, used level L_k, NU, phase, R, F, crossing, wakes, K). This packet does not use
  Lemma DF or DF′.
- Status: L-NEW's proofs, unrefereed. Lemmas about the candidate N5 on 𝒞^1O (exactly one Odd vertex o with out-degree > 1), except §1 (any
  game). Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Statements: §1 Lemma U-loc; §2 Lemma OE; §3 Corollary OX. It sharpens P-N5-SO's Corollary XJ (same conclusion type, without S_o or Θ).
- Dependencies (signed): P-N5-LP Lemma U (its proof), Theorem LP, Corollary LP′ steps 1-2 (rise cases); R15 (a); R19 (a) Lemma G (a) (off R,
  Ξ = W, and the honest play of a vertex of F never visits o); R22 (b) TC (i) (H1 constant on a crossing-free interval); R25 (e) CAP-1 closure
  (λ(o) ≠ o: σ̄(o) is a full Ξ-minimiser over succ(o), REFEREE's case split), (d) Theorem FB, (e) J1; P-N5-U23 fixes §6 (REFEREE R-1: under
  ¬H1, θ = (c_θ, ∅, d)); VJ00 (P1)-(P3), Lemma 5.2.
- Notation: E_k := the max level of the relevant EVEN changes at k → k+1 (⊥ if none); O_k := the level of the relevant σ̄(o) change (⊥ if
  none). L_k = max(E_k, O_k) (on 𝒞^1O every Odd vertex but o has one successor).

## 1. Lemma U-loc (PROVED, L-NEW; any game, inside a phase)
Statement. Let k → k+1 be a transition of a phase, v a vertex, c := λ(v), and L ∈ {⊥, −1, 0, …}. If every relevant change at a vertex of v's
H_{k+1}-path before its first visit of c has level ≤ L, then COARSE_L(Ξ_{k+1}(v)) = COARSE_L(Ξ_k(v)).
Proof. P-N5-LP Lemma U's steps 2-4 verbatim with L in place of L_k: they use the bound only at the vertices p_0, …, p_{s−1} of that path. □

## 2. Lemma OE (PROVED, L-NEW; 𝒞^1O)
Statement. At a transition k → k+1 of a phase with R_k = R_{k+1} (no crossing), O_k ≤ E_k. In particular, if Even makes no relevant change, σ̄(o)
makes no relevant change.
Proof.
1. Setup. Assume O_k ≠ ⊥, so λ(o) =: c ≠ o (fixed in the phase), x0 := σ̄_k(o) ≠ x1 := σ̄_{k+1}(o), and ℓ := O_k = lev(Ξ_k(x0), Ξ_k(x1))
   (< ∞: λ(x0) = λ(x1) = c by (P1) and the phase). By CAP-1, x0 is a full Ξ_k-minimiser and x1 a full Ξ_{k+1}-minimiser over succ(o). Suppose
   ℓ > E_k (E_k = ⊥ included).
2. x1's H_{k+1}-path to c avoids o: otherwise Ξ_{k+1}(x1) = Q ⊕ θ_{k+1} = Q ⊕ o ⊕ Ξ_{k+1}(x1) for the path Q from x1 to o (P2 along the path;
   θ_{k+1} = o ⊕ Ξ_{k+1}(x1) since x1 = σ̄_{k+1}(o) and λ(o) ≠ o), which is impossible since the length grows. So the only possible relevant
   changes on that path are Even ones, of level ≤ E_k (Odd vertices on it are forced). By Lemma U-loc with L = E_k:
   COARSE_{E_k}(Ξ_{k+1}(x1)) = COARSE_{E_k}(Ξ_k(x1)).
3. Case H1 at k (then at k+1 too: TC (i)). x0 is an honest minimiser whose honest play does not return to o, so it never visits o and equals x0's
   (σ_k, τ)-play: x0 ∈ F_k = F_{k+1}. Its H_{k+1}-play is a play from a vertex of F_{k+1}, so it never visits o either (R19 (a)). As in step 2,
   Lemma U-loc gives COARSE_{E_k}(Ξ_{k+1}(x0)) = COARSE_{E_k}(Ξ_k(x0)). Since lev(Ξ_k(x0), Ξ_k(x1)) = ℓ > E_k, the COARSE_{E_k} values of x0 and x1
   differ, are the same at k and k+1, and decide the comparison (the top difference is above E_k). At k, Ξ_k(x0) ◁ Ξ_k(x1) strictly (x0 is a
   minimiser and the values differ). So Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1): x1 is not a minimiser at k+1. Contradiction.
4. Case ¬H1 at k (and k+1). o lies on its honest cycle, whose top is c (= c_θ), so θ_k = (c, ∅, d) and Ξ_k(x0) = (c, ∅, d − 1): P(Ξ_k(x0)) = ∅
   (R-1: no vertex of the cycle is above c). If ℓ ≥ 0, the top difference of P(Ξ_k(x0)) = ∅ and P(Ξ_k(x1)) is a vertex of rank ℓ in
   P(Ξ_k(x1)). Likewise P(Ξ_{k+1}(x1)) = ∅ (x1 is σ̄_{k+1}(o) under ¬H1). But step 2 gives P(Ξ_{k+1}(x1)) ∩ V_{>E_k} = P(Ξ_k(x1)) ∩ V_{>E_k} ∋ the
   rank-ℓ vertex (ℓ > E_k). Contradiction. If ℓ = −1, then E_k = ⊥ (ℓ > E_k): no relevant Even change at k at all. Then x0's H_{k+1}-path equals
   its H_k-path (its vertices before c are Even or forced, or o, which is not on it: x0's path runs along the honest cycle from x0 to c before
   o), so Ξ_{k+1}(x0) = Ξ_k(x0) by Lemma U-loc with L = ⊥, and Ξ_{k+1}(x1) = Ξ_k(x1) by step 2. Then x0 is still strictly better for Odd than
   x1 at k+1. Contradiction. □
- DATA (oddlev.py, LIB = the 220-file 𝒞^1O library): relevant σ̄(o) changes at 431 crossing-free H1 transitions, 11 crossing-free ¬H1
  transitions and 791 crossings; O_k > E_k at 217 transitions, ALL crossings (H1); 0 off crossings.

## 3. Corollary OX (PROVED, L-NEW; 𝒞^1O, given P-N5-LP and R25)
Statement. In a phase on 𝒞^1O with X crossings, K wakes and f fallback transitions:
- (i) ε ≤ X, where ε = relevant transitions with an Odd-only used level (P-N5-LP Theorem LP).
- (ii) J ≤ X, where J = non-tame transitions (R25).
- (iii) ρ ≤ 2f + 2X + K, where ρ = rises of the used level (P-N5-LP Theorem LP).
- (iv) f ≤ n_E(2n − 1)(X + 1) + X.
- (v) T ≤ (m − n + 1)·((n + 1)(2f + 2X + K + 1)·n(n − 1) + X + 1) = O(m·n⁵·(1 + X + K)).
Proof.
- (i) An Odd-only used level means O_k > E_k, so the transition is a crossing (Lemma OE).
- (ii) By J1 (R25 (e)) a non-tame transition switches σ̄(o) at a level above M_k; that change is relevant (P-N5-LP §4 step 3: an own-cycle-node
  change of σ̄(o) leaves the transition tame), and M_k ≥ E_k (Even switches go to gate edges, R15 (d)). So O_k > E_k: a crossing (Lemma OE).
- (iii) P-N5-LP Corollary LP′ step 2 splits rises into: a fallback in [k, k′] (≤ 2f), a crossing in [k, k′] (≤ 2X), a σ̄(o) case at k′ with
  every relevant Even level ≤ L_k < L_{k′} = O_{k′} (so O_{k′} > E_{k′}: a crossing at k′ by Lemma OE, already in the previous case), or a wake
  (≤ K).
- (iv) R25 Theorem FB with (ii).
- (v) P-N5-LP Theorem LP with (i), (iii), (iv). □
- Reading (not to sign): per phase of o-cyclic 𝒞^1O, everything is polynomial in X (crossings, ≡ Z up to a factor n by RESULTS R23 LV′) and
  K (wakes: R → R switches in the W-blind band, bounded in U1 pieces by R24 and in U2 / U3 / U23 stretches by the CASC-U2 / CASC-U3
  corollaries of RESULTS R26 in terms of (E) and (K_W)). R25's (J-poly) and the fallback count follow from (X) with J ≤ X, sharper than P-N5-SO's
  J ≤ S_o ≤ d_o(Θ + 1).
- DATA (oddlev.py, LIB): all 175 non-tame transitions are crossings (H1). jcl_zcl_cu_n48: J 17, X 17 (tight). Rises (lcheck.py, LIB): 413 =
  284 with a fallback + 129 with a crossing (orise.py: every σ̄(o)-type rise has a crossing in its interval) + 0 wakes.
