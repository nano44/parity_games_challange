# Referee packet P-N5-SO: σ̄(o)-changes, J and fallbacks per phase reduce to crossings on 𝒞^1O (box 32)
L-NEW successor 12 (Opus 5.5, D15/D18). Written 2026-10-25 00:5xZ by date -u. Frozen at this commit: corrections go in a fixes file, never here.
- Self-contained companion of P-N5-LP (docs/new/P-N5-LP-box32.md, pinned or to be pinned; its §0 notation is used here). Source text:
  docs/new/N5-L-box32.md §4b; where they differ, this packet governs.
- Status: L-NEW's proofs, unrefereed. Lemmas about the candidate N5 on 𝒞^1O (exactly one Odd vertex o with out-degree > 1). Not a running-
  time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Statements: Lemma TH, Lemma SO, Corollary XJ. Labels: PROVED (L-NEW), DATA.
- Dependencies (signed): R15 (a) (Ξ monotone), R15 (d) (switches go to gate-edge targets); R22 (a) F1° (on a crossing-free interval Ξ changes
  on F at ≤ max(0, |F| − 1) transitions) and (b) TC (i) (H1 constant on a crossing-free interval); R24 Lemma R (the length step chooses among
  the fully optimal successors: first in list order in the longest-path mode, first discovered in the BFS mode) and Lemma TB step 5 (BFS
  queue order = lex order of root-first index sequences of tree paths); R25 (e) CAP-1 closure (λ(o) ≠ o: σ̄(o) is a full Ξ-minimiser over
  succ(o), REFEREE's case split), (d) Theorem FB, (e) J1; P-N5-U23 fixes §6 (REFEREE's R-1: under ¬H1, θ = (c_θ, ∅, d)); VJ00 (P2), (P3).
- Phase, R, F, crossing, relevant change: P-N5-LP §0-§1. S_o := transitions with a relevant σ̄(o) change; J := non-tame transitions (R25).

## 1. Statements and proofs (PROVED, L-NEW)
Setting: a phase on 𝒞^1O; d_o := |succ(o)|; Θ := the number of transitions of the phase that change θ = Ξ(o); X := crossings.
If λ_Ξ(o) = o, θ = (o, ∅, 0) is constant and no σ̄(o) change is relevant; so assume λ_Ξ(o) ≠ o (fixed in the phase).
**Lemma TH.** Θ ≤ (n − 1) + n(X + 1) + X.
Proof.
- H1 is constant on each crossing-free interval (R22 (b) TC (i)), so a θ-change at a crossing is counted by X. Take a crossing-free θ-change
  k → k+1.
- ¬H1 at k: o lies on its honest cycle, whose top is c_θ, so θ = (c_θ, ∅, d) with d ∈ [0, n − 1] (REFEREE's R-1, P-N5-U23 fixes §6). c_θ is
  fixed in the phase and θ is monotone (R15 (a)), so d moves in one direction: ≤ n − 1 such changes in the whole phase.
- H1 at k: σ̄_k(o) =: x0 is a full Ξ_k-minimiser over succ(o) (λ(o) ≠ o; R25 CAP-1, REFEREE's case split), and θ_k = o ⊕ Ξ_k(x0) (P2).
  x0's honest play never returns to o (H1), so it equals its (σ_k, τ)-play, which therefore never reaches o: x0 ∈ F_k = F_{k+1}. Let
  x1 := σ̄_{k+1}(o). If Ξ_{k+1}(x0) = Ξ_k(x0), then Ξ_{k+1}(x1) ⊴ Ξ_{k+1}(x0) = Ξ_k(x0) ⊴ Ξ_k(x1) ⊴ Ξ_{k+1}(x1) (minimisers; R15 (a)), so
  θ_{k+1} = o ⊕ Ξ_{k+1}(x1) = θ_k. So a θ-change changes Ξ at x0 ∈ F: it is one of the ≤ max(0, |F| − 1) F-changing transitions of its
  crossing-free interval (R22 (a) F1°). There are ≤ X + 1 intervals. □
**Lemma SO.** S_o ≤ Θ + (d_o − 1)(Θ + 1) ≤ d_o(Θ + 1). More precisely: at a relevant σ̄(o) change with θ unchanged, the old choice is no
longer a minimiser.
Proof.
- Fix a maximal run of the phase with θ constant, and μ with o ⊕ μ = θ (⊕ is injective for a fixed cycle node). T_k := {x ∈ succ(o) :
  Ξ_k(x) = μ}, the full minimisers (μ = min, since σ̄_k(o) ∈ T_k by CAP-1). T only shrinks along the run: x ∈ T_{k+1} gives Ξ_k(x) ⊴
  Ξ_{k+1}(x) = μ ⊴ Ξ_k(x).
- The choice inside T. By RESULTS R24 Lemma R, σ̄_k(o) is chosen among the fully optimal successors, i.e. T_k: in the longest-path mode
  (Ω(λ(o)) even) the first in list order, i.e. the smallest index; in the BFS mode (Ω(λ(o)) odd) the first discovered, i.e. the
  lexicographically least root-first index sequence of its BFS-tree path (R24 Lemma TB step 5).
- Keys are frozen on T_k ∩ T_{k+1}. For x ∈ T_k, x ≠ o, and x's H_k-path to c := λ(o) avoids o: if it passed o, then Ξ_k(x) = (path) ⊕ θ,
  and Ξ_k(x) = μ with o ⊕ μ = θ would make μ strictly longer than itself. Every vertex on that path other than o has one successor in the
  graph G_σ of Engine.evaluate (Even: σ; Odd: forced), so the BFS-tree path of x is this path. If some vertex of it switches at k, take the
  first one, p (an Even vertex with λ(p) = c ≠ p): its new successor is a strictly better gate-edge target (R15 (d)), so Ξ_{k+1}(p) ▷ Ξ_k(p)
  (P2, R15 (a), ⊕ keeps strictness), and then Ξ_{k+1}(x) = (the unchanged prefix) ⊕ Ξ_{k+1}(p) ▷ Ξ_k(x), so x ∉ T_{k+1}. Hence for
  x ∈ T_k ∩ T_{k+1} the path, and so the key, is the same at k and k+1. (In the longest-path mode the key is the index anyway.)
- So if σ̄_k(o) =: s0 ∈ T_{k+1}, it is still the key-minimum of T_{k+1} ⊆ T_k (keys of distinct exits differ: they end in the exit), and
  σ̄_{k+1}(o) = s0. A relevant change with θ fixed therefore removes s0 from T: ≤ d_o − 1 per run. There are Θ + 1 runs, and ≤ Θ changes
  at θ-changes. □
**Corollary XJ (PROVED, L-NEW, given RESULTS R22 (a)-(b), R24 Lemma R / TB, R25 CAP-1, FB and J1).** In a phase on 𝒞^1O:
- S_o ≤ d_o·(2n + (n + 1)X) and J ≤ S_o (P-N5-LP §4 proof, step 3), so f ≤ n_E(2n − 1)(J + 1) + J = O(n³(1 + X)) (R25 Theorem FB).
- With P-N5-LP Corollary LP′: T = O(m·n⁷·(1 + X) + m·n⁵·K).
- So (J-poly) (R25's open core), NFB-O and the fallback count all follow from (X); per phase the open cores of o-cyclic 𝒞^1O are now X
  (≡ Z up to a factor n, R23 LV′) and K, the wakes, which live in U1 pieces (R24) and in U2 / U3 / U23 stretches ((E), (K_W)).
- DATA (socheck.py, LIB, 255 phases): 0 failures of Lemma TH (incl. its two cases), Lemma SO (incl. "the old choice leaves T"), and J ≤ S_o.
  Maxima: Θ 51 and S_o 49 at n 32 (lev_l_x, d_o 14, X 21); J 17 ≤ S_o 18 at n 48 (jcl_zcl_cu_n48, d_o 18, X 17).

