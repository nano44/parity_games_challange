# Draft RESULTS R55 (Lead, 2026-10-26 03:03Z by date -u; both §Cs and the fixes file filled) — to CHECKER C64

### R55 [refereed-only] N5 on EVERY game: with the disagreement set D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)} in place of o, the honest and the W-valuation agree off the D-region (G_D (a)), factor through the first D-vertex under (h_D) (G_D (b)) and agree in coarse form above M_D under (h_D) ∧ (h3_D) (G_D (c1), (c2)); Ξ changes on F_D at most max(0, |F_D| − 1) times per D-crossing-free interval (F1°_D); W(u) does not drop at u ∈ D_k ∩ D_{k+1} under (h_D) (Wo_D) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (not M3, not a step-4 pass, not a TARGET.md claim; nothing here bounds N5's running time on any class; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C64.md, checker PENDING)
- Object (packet P-N5-GD, added at l-new 205c9ed7, pinned trunk 3c6f6c16, unchanged during review): docs/new/P-N5-GD-box43.md, sha1
  b898ff8256bf444ef90d69eb3154f5fe16dddf10 (L-NEW successor 23 from successor 22's working doc, Opus 5.5). The referees' notes are
  collected by the lane in docs/new/P-N5-GD-fixes-box44.md (l-new b93f6c7d, sha1 dfa6dd2b4cc51f95285dcdd4f9df14ff55a01d09, L-NEW
  successor 23: GD-N1 = N-GD-1, GD-N2, GD-N3, the premise-class note); on trunk; repairs only, no signed statement changes.
  Setting (every game; no class hypothesis): N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4); n := |V|; state k = (σ_k, τ_k);
  σ̄_k := SPEC S1's optimal Odd counterstrategy to σ_k; Ξ_k(v) := the value of the (σ_k, σ̄_k)-play from v; G_τ := G with every Odd
  vertex fixed to τ_k; W_k(v) := the value of the (σ_k, τ_k)-play from v; λ_Ξ, λ_W the cycle-node maps; values and ⊴ as in VJ00 (RESULTS
  R15). Phase as in RESULTS R38 (a) KEY. D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play (v
  included), if any; R_D := {v : u(v) exists}, F_D := V ∖ R_D; π_v := the (σ_k, τ_k)-path from v to u(v), u(v) excluded. (h_D) at k: for
  every u ∈ D_k, neither the honest play nor the W-play from u visits D_k after leaving u. (h3_D) at k: λ_Ξ(u) = λ_W(u) for every u ∈ D_k.
  lev, COARSE_L, (C2), (C4) as in RESULTS R25; M_D := max over u ∈ D_k of lev(Ξ_k(u), W_k(u)), ⊥ if D_k = ∅. On 𝒞^1O with D_k = {o}:
  R_D = R, F_D = F, (h_D) = H1 ∧ H2, (h3_D) = H3.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R15 (a), R17 (a)-(c), R18 (c) flat
  case, R18 (d) Lemma S (c) in its landed "⇒" form, R21 (a) XW, R21 (c) FBL-N (i), R25 (C2), (C4), R38 (a). Each is signed under a
  𝒞^1O setting line; both referees read each proof and CONFIRM that it uses no one-Odd step (R17 and R18's flat case are one-player
  statements, applied to G_τ, its arenas and 𝓕, which are one-player on every game; XW is VJ00 (11) on G_σ). R21 (c) FBL-N (ii) and
  R22 (a) step 1 DO have a one-Odd step; the packet does not cite them and re-proves both in set form (F1°_D steps 1 and 4) (premise-class
  note; N-GD-2 + REFEREE §1; fixes):
  (a) Lemma G_D (a) (no hypothesis): for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v).
  (b) Lemma G_D (b) (under (h_D) at k): for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and
      the W-play from u avoid π_v.
  (c) Lemma G_D (c) (under (h_D) and (h3_D) at k): (c1) if y, z ∈ R_D and u(y) = u(z) = u, then π_y ⊕ Ξ_k(u) ⊴ π_z ⊕ Ξ_k(u) iff
      π_y ⊕ W_k(u) ⊴ π_z ⊕ W_k(u); (c2) for every L with M_D ≤ L < ∞ (L = ⊥ allowed when M_D = ⊥) and every v ∈ V,
      COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)), hence the COARSE_L-orders of Ξ_k and W_k coincide on V. Nothing is claimed for routes to
      different terminals below M_D (Δ-RT, OPEN).
  (d) Lemma F1°_D (no (h_D), no (h3_D)): on a D-crossing-free interval I (a maximal run of states of one phase on which (D_k, R_D) is
      constant), the transitions at which Ξ changes at some vertex of F_D number at most max(0, |F_D| − 1). In step 4, R18 (d) Lemma S
      (c) is read in its landed "⇒" form (S4a returning σ_k makes σ_k a pointwise arena optimum; only "⇒" is used) (GD-N1 = N-GD-1, both
      referees, independently), and the sentence "Since k+1 ∈ I, z ∈ F_D" is read for x's switched successor x* := σ_{k+1}(x), which lies
      in F_D because F_D is closed under σ_{k+1}; the conclusion stands (GD-N2, REFEREE; accepted by REFEREE-2).
  (e) Lemma Wo_D (under (h_D) at k and at k+1): if k → k+1 is an N5 transition with τ_{k+1} = τ_k and u ∈ D_k ∩ D_{k+1}, then
      W_{k+1}(u) ⊵ W_k(u). (No (h3_D) and no phase hypothesis; the honest-side statement is not claimed.)
- Not signed (packet §2, §3, §4): the port table (a READING); CONJECTURE Δ1 (D-changes per phase poly(n)); Δ-RT (OPEN); the R20
  coarse port (CONJECTURE); docs/new/N5-MULTI-box43.md §2-§4; the data. DATA, not a gap (GD-N3, REFEREE): in REFEREE's random games
  Wo_D's conclusion also held at all 66 transitions where (h_D) failed; the proof uses (h_D).
- Honest limits: (i) Structural lemmas only: they bound no count of transitions, crossings or phases on any class beyond what F1°_D
  states per interval; the frontier 𝒞^(≥2E,≥2O) stays open, and Δ1 and Δ-RT are what an R_D-side count would need. (ii) The premises'
  game-generality is a reading of their proofs by both referees (above), not a re-signature of the landed entries. (iii) F1°_D's bound is
  not approached in the data (REFEREE-2's mutation f1 with |F_D| − 2 does not bite), so its tightness is untested; Wo_D is thin on
  random multi-Odd games (36 checks in REFEREE's, 225 in REFEREE-2's).
- Data (DATA, not proof): REFEREE (own gd_probe.py; logs scratch/gd_logs/): lib41 (n ≤ 64: 367 games, any class) from S3 and 2 random
  start pairs, 1,101 runs, and 500 random games with 2-4 Odd choice vertices × 3 starts, 1,500 runs; G_D (a), (b), (c1), (c2) (at every L
  from max(M_D, −1) to n − 1), F1°_D and Wo_D checked; 0 failures; mutation: (c2) at L = M_D − 1 fails at all 85 states with M_D ≥ 0 (the
  threshold is sharp). REFEREE-2 (own gd_check.py, own play values): lib41 × 3 starts (1,236 runs), 503 𝒞^1O files × 2 (1,006), the
  box-43 instances × 5 (25), 20,000 random 𝒞^kO runs; 92,210 states, G_D (a) at every state, (c2) at every level L ≥ M_D, 7,039 + 8,420
  + 28 + 225 Wo_D checks; 0 violations; max Ξ-changes on F_D per interval 55 (x32_rand64.pg); mutations gda, c2, wo bite, f1 does not.
- Signatures: REFEREE docs/referee/R-N5-GD.md (referee a50f6623, successor 11; §C a639e39e): G_D (a), (b), (c1), (c2), F1°_D, Wo_D
  SIGNED; premise class CONFIRMED; notes GD-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-GD.md (referee-2 ab4a5af0, successor 13;
  §C 6e12b2bc): all SIGN; premise class CONFIRMED (N-GD-2); notes N-GD-1, N-GD-2; no gap. §C (both): verdicts identical; joint gap map
  empty; GD-N1 = N-GD-1 (found independently); GD-N2 accepted by REFEREE-2; GD-N3 REFEREE only (data); nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running time). GAPS G-N5-TIME: open for general games.
