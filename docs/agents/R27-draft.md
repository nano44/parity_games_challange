# Draft RESULTS R27 (Lead, 2026-10-25 01:47Z by date -u) — awaits CHECKER C36; lands in "## Results" after R26, before "## Dead ends"

### R27 [refereed-only] N5 inside a phase: the used-level freeze and a carry bound (Lemma U, HI, UL, GR, NU, Theorem LP), dormant edges and wakes on one-Odd-choice games (DF′, BAND, WAKE), and on those games σ̄(o)-changes, non-tame transitions and fallbacks per phase reduce to θ-changes and crossings (TH, SO, Corollaries LP′, XJ) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C36.md, checker PENDING)
- Objects (pinned, unchanged during review): packet P-N5-LP docs/new/P-N5-LP-box32.md, sha1 d2c8121a0089add13c9417080cfb57620f592c88,
  pinned trunk bc42f2c; packet P-N5-SO docs/new/P-N5-SO-box32.md, sha1 deb5ee4422da3ab7389ce35e4542977927b53886, pinned trunk 1ef02bb (both
  L-NEW successor 12, Opus 5.5). The referees' repairs are collected by the lane in docs/new/P-N5-LP-fixes-box32.md (l-new 459660c, on
  trunk; sha1 af17cce0ec8686994a64dbaf512e89be67809eb0) and docs/new/P-N5-SO-fixes-box32.md (l-new 078c05d, on trunk; sha1
  cae3bb5b9aa67e5d54f38cca0d5be8a2b6b0cd0a), L-NEW successor 12; records, not themselves refereed text.
  Setting: N5 (SPEC docs/new/N5-ssi-global.md) on any game unless marked 𝒞^1O; valuations x = (c, P, ℓ), lev and COARSE_L as in RESULTS
  R25; Ξ_k = Θ_{H_k} (ENG-1, inherited); a PHASE is a run of transitions with λ_Ξ and τ constant. RELEVANT CHANGE at k → k+1: an Even y
  with σ_{k+1}(y) ≠ σ_k(y) and λ_k(y) ≠ y, or an Odd u with σ̄_{k+1}(u) ≠ σ̄_k(u) and λ_k(u) ≠ u. USED LEVEL L_k := the max of
  lev(Ξ_k(old successor), Ξ_k(new successor)) over the relevant changes (⊥ if none); a transition is NU if L_k = ⊥, RELEVANT otherwise.
  A RISE is a pair of consecutive relevant transitions k < k′ (only NU between) with L_{k′} > L_k; ρ := #rises; ε := #relevant transitions
  whose used level is attained only by Odd changes. On 𝒞^1O: R, F, crossing, c_θ, c_w as in R21-R26; S_o := #transitions with a relevant
  σ̄(o) change; Θ := #transitions changing θ = Ξ(o); X := #crossings; J := #non-tame transitions (R25); d_o := |succ(o)|. A WAKE at k′ is
  a relevant Even switch at k′ of level > L_k (k < k′ consecutive relevant, no fallback in [k, k′], R constant on [k, k′ + 1]); K := #wakes.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma U (used-level freeze; any game, inside a phase): L_k < ∞ and COARSE_{L_k}(Ξ_{k+1}(v)) = COARSE_{L_k}(Ξ_k(v)) for every v; an
      NU transition leaves Ξ unchanged. (R25 TAME's proof with M_k replaced by L_k; checked line by line by REFEREE.)
  (b) Lemma HI: with L := L_k ≠ ⊥ and y an Even vertex that is not an own cycle node switched at k, for every ℓ > L, (y, z) is a gate edge
      of level ℓ at k iff at k+1. Its Consequence holds as M_{k+1} ≤ M_k; "=" is unproved when the level-M_k gate edges sit at switched own
      cycle nodes (HI-1 = G-LP-2); unused downstream.
  (c) Lemma UL (L_k = ℓ ≥ 0 is never attained by a relevant switch of the rank-ℓ vertex u_ℓ), Lemma GR (ℓ-goodness: (a) if L_k = ⊥ or
      L_k ≤ ℓ then G_ℓ(k) ⊆ G_ℓ(k+1); (b) if L_k = ℓ is attained by a relevant Even switch of y then y ∉ G_ℓ(k), y ∈ G_ℓ(k+1)), Lemma NU (a
      run of consecutive NU transitions has ≤ Σ_{y Even}(deg(y) − 1) ≤ m − n transitions).
  (d) Theorem LP (any game): a phase with T transitions, T_rel relevant, has T ≤ (m − n + 1)(T_rel + 1) and
      T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε (n ≥ 2). Step 4's "y ⊕ keeps order and strictness" holds here because the values compared share
      one path set (N-LP-1, wording).
  (e) On 𝒞^1O: Lemma DF′: at an S4a transition k → k+1 of a phase, if (y, z) is an edge of the arena H_k that is a gate edge at k+1 and y
      is not its own (W-)cycle node at k+1, then σ_{k+1}(y) ∈ R_{k+1} (two proofs: REFEREE, Bellman via R24 G-TB-1, (F1) only; REFEREE-2,
      R15 (a) Lemma A + (F1) + R15 (b) Lemma B). Lemma BAND: at a state with both frames in route form and c_θ ≠ c_w, a gate edge (y, z) of
      level ℓ ≥ 0 with σ(y), z ∈ R and W(z) ⊴ W(σ y) has rank c_θ < ℓ < rank c_w and equal W path sets. Lemma WAKE: a wake y: a → z has
      a, z ∈ R; if both frames are in route form, the state is in a U1 piece (cites DF′: W-1 = G-LP-1, closed).
  (f) Corollary LP′ (𝒞^1O): with f fallback transitions, T ≤ (m − n + 1)·((n + 1)(2f + S_o + 2X + K + 1)·n(n − 1) + S_o + 1) with
      f ≤ n_E(2n − 1)(S_o + 1) + S_o; so T = O(m·n⁵·(1 + S_o + X + K)). (Via ε ≤ S_o, ρ ≤ 2f + S_o + 2X + K, J ≤ S_o by R25 J1 and Lemma
      U, and R25 Theorem FB; it uses neither DF nor WAKE.)
  (g) On 𝒞^1O, per phase with λ_Ξ(o) ≠ o: Lemma TH: Θ ≤ (n − 1) + n(X + 1) + X (¬H1: θ = (c_θ, ∅, d), RESULTS R26's R-1; H1: σ̄(o) is a
      full Ξ-minimiser (R25 CAP-1, REFEREE's case proof, re-checked and adopted by REFEREE-2 in R2-N5-FB §C.3: SO-1, closed with two
      signatures) and a θ-change changes Ξ at that exit in F, one of R22 F1°'s F-changes (F1° transfers to this coarser phase: N-SO-1)).
      Lemma SO: S_o ≤ Θ + (d_o − 1)(Θ + 1) ≤ d_o(Θ + 1); at a relevant σ̄(o) change with θ unchanged, the old choice is no longer a
      minimiser (the R24 Lemma R / TB key of an exit that stays a minimiser is frozen; the strict rises use (SG), R19 (d), and the prefix
      vertices lie in no path set: G-SO-1, closed; N-SO-3 wording).
  (h) Corollary XJ (𝒞^1O): S_o ≤ d_o(2n + (n + 1)X) and J ≤ S_o, so f = O(d_o·n³(1 + X)) ⊆ O(n⁴(1 + X)) (XJ-1 = N-SO-2: the packet's
      O(n³(1 + X)) is corrected); with (f), a phase has T = O(m·n⁷(1 + X) + m·n⁵·K) transitions.
- Refuted: Lemma DF as stated (without "y not its own cycle node") is FALSE, NOT SIGNED by both referees: the cited VJ00 (BRICS
  RS-00-48) Lemma 5.8 step 2 ⇒ 3 ⇒ 1 ("a maximum has no improvement") fails at own cycle nodes, where a length-only improvement is kept by
  FIX 2's DFS (as in RESULTS R15's side finding). Counterexamples: docs/referee/R-N5-LP/df_cex.pg (n 11, sha1 a128663e…, o = 1) and
  docs/referee-2/R2-N5-LP/instances/df_cex.pg (n 5, sha1 0a98e1b7…, o = 3); Lead re-ran both: n5 2/1, Oink zlk OK strategies verified,
  one Odd choice vertex (the DF failure itself is the referees' own code). Lane forms refuted before the packets (P-N5-LP §5, not
  signed): NO-WAKE "K = 0" FALSE (experiments/new/box32/instances/nowake_cex_n32.pg, sha1 3a56e3fb…; reproduced by both referees and the
  Lead); (KW-M) FALSE (instances/kwm_cex_n24.pg, sha1 c2723e08…; Lead re-run).
- Reading (not signed): with Corollary XJ, RESULTS R25's open core (J-poly), NFB-O and the fallback count follow from (X); per phase of
  o-cyclic 𝒞^1O the open quantities are X (≡ Z up to a factor n, R23 LV′) and K (wakes: in U1 pieces bounded by R24 Theorem U1; in U2 /
  U3 / U23 stretches by R26's corollaries in terms of the open (E) and (K_W)).
- Honest limits: (i) Lemma U, HI, UL, GR, NU and Theorem LP hold on every game; DF′, BAND, WAKE, LP′, TH, SO and XJ are on 𝒞^1O.
  (ii) Theorem LP bounds nothing by itself: it moves the count to rises (carries) and ε. (iii) X and K per phase are OPEN, so G-N5-TIME
  stays open; the phase count (Lemma Φ) is unrefereed. (iv) The bounds are loose in d_o and n; the data show neither a growth law nor
  tightness beyond J = S_o (REFEREE-2). (v) DATA on K: every wake found (L-NEW climbs) is a U3 W-tie switch in the length-only regime,
  max 2 per run (lane DATA, not re-checked by the referees).
- Data (DATA, not proof; every probe asserts one Odd choice vertex where 𝒞^1O): REFEREE lp_probe.py (own code): 228 library 𝒞^1O files
  (5,482 in-phase transitions), 4,500 random 𝒞^1O runs, 1,500 random general games: 0 failures of §1-§2; DF 170 failures (all own W-cycle
  nodes), DF′ 0; so_probe.py: 234 library files (257 phases with λ(o) ≠ o) + 3,000 random runs: 0 failures of TH, SO, XJ (max Θ 51,
  S_o 49). REFEREE-2 (own code): 8,284 runs on LP, 0 violations of the signed statements (176 DF failures, all own-cycle-node length-only
  edges); SO batch 4,502 runs + 6 climbs (12,000 fully checked runs aimed at S_o − d_o(Θ + 1), J − S_o and θ-fixed σ̄(o) changes): 0
  violations, best margins −1 and 0; 3,915 relevant σ̄(o) changes with θ fixed, the old choice leaving the minimiser set every time.
  L-SI socheck.py on its climb bests and the named set: 0 failures (max J 18 ≤ S_o 19, n 48); Lead socheck on jcl_zcl_cu_n48: J 17 ≤ S_o
  18 = d_o.
- Signatures: REFEREE docs/referee/R-N5-LP.md (referee 4957b2c; Part 2 = P-N5-SO dcb4119; §C bb6f60f; SO-1 addendum 2a0cb30): U, UL, GR,
  NU, Theorem LP, BAND, LP′ SIGNED; HI SIGNED, Consequence WITH GAP HI-1; DF NOT SIGNED (FALSE), DF′ SIGNED; WAKE SIGNED WITH GAP W-1
  (closed); SO SIGNED; TH SIGNED (SO-1 closed in the addendum); XJ SIGNED WITH GAP XJ-1. REFEREE-2 docs/referee-2/R2-N5-LP.md (referee-2
  4949d6c; §8 = P-N5-SO ba67f41; combined §C caee2ae): U, HI, UL, GR, NU SIGN (HI Consequence G-LP-2); Theorem LP SIGN (N-LP-1); DF NOT
  SIGNED, DF′ SIGN; BAND SIGN; WAKE SIGN WITH GAPS (G-LP-1, closed); LP′ SIGN; TH SIGN (N-SO-1); SO SIGN WITH GAPS (G-SO-1, closed;
  N-SO-3); XJ SIGN WITH GAPS (N-SO-2). §C: no disagreement. Joint gap map (REFEREE §C, REFEREE-2 §C.2): DF FALSE, DF′ signed by both;
  HI-1 = G-LP-2; W-1 = G-LP-1 (closed); N-LP-1 (wording); SO-1 (closed, two signatures); XJ-1 = N-SO-2; G-SO-1 (closed), N-SO-1, N-SO-3.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
