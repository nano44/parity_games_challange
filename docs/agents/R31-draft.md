# Draft RESULTS R31 (Lead, 2026-10-25 07:20Z by date -u) (rev. 08:36Z: REFEREE-2 §C bc2e7b7 cited) — to CHECKER C40 — LANDED in RESULTS Results 08:50Z (CHECKER C40 737b193 PASS), after R30

### R31 [refereed-only] N5 on one-Odd-choice games: a fallback gate never outruns the Ξ/W gap (Lemma FBW, every game), so fallback levels never rise along a whole scope run (Theorem CLS2, (H-EQ) closed), fallbacks of level ≥ 0 freeze coarse values (FLAT-ALL), a tail repeats at most once per frozen stretch (STRETCH), and an additive per-level fallback count (Theorem PL, Corollary PL-S) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C40.md, checker PENDING)
- Object (packet P-N5-FBW, pinned trunk e69772b, unchanged during review): docs/si/P-N5-FBW-box9.md, sha1
  88337bd621d3467dde4b35aa93b254bf847bb330 (L-SI successor 4, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-FBW-fixes-box9.md (l-si 51491b7, on trunk; sha1 91ff42168f81a7b4ef2f5af10eea81c52225b42a, L-SI successor 4; repairs only,
  no strengthening of the reviewed text).
  Setting as in RESULTS R25 and R27-R30 (gates, gate levels, M_k, lev, COARSE_L, (C1)-(C7), Ξ_k = Θ_{H_k}; on 𝒞^1O: R, R̄, F, (h), EQ /
  THR, u*, scope runs, r_k := lev(θ_k, w_k), Fact R, OFF, Lemma G, Lemma S, TRANSFER, CN, NL, CLS1, U-loc, OR, TC-SPLIT, ABS-L). For an
  S4c fallback k and a gate (y, z) at k: u := σ_k(y), ℓ := lev(Ξ_k u, Ξ_k z), δ := max(lev(Ξ_k u, W_k u), lev(Ξ_k z, W_k z)). A BLOCK of
  a scope run S at level M ≥ 0 is the set f_1 < … < f_N of fallbacks of S at level M; an interval (f_i, f_{i+1}) is DIRTY if COARSE_M(Ξ)
  changes at some vertex inside it; D_M := #dirty intervals; REL_M := #exits of o leaving R at f_1, …, f_{N−1}; d_o := |succ(o)|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Premise P-OPT: at an S4c fallback k, σ_k is the arena optimum against τ_k (S4a ran at k and returned σ_k); RESULTS R18 G-1OA-6
      concerns σ_{k+1}, not σ_k (both referees VALID, same reason).
  (b) Lemma FBW (every game): at an S4c fallback k at which Even switches, every gate (y, z) has (i) ℓ ≤ max(δ, −1); (ii) if
      ℓ = −1 > δ, y is its own W_k-cycle node and its own Ξ_k-cycle node.
  (c) Corollary FBW-S (𝒞^1O): at an in-phase S4c fallback k with (h) at k, every gate has level ≤ max(r_k, −1); so M_k ≤ −1 at EQ states
      and at THR states with u* = none. Theorem CLS2 (𝒞^1O): along a scope run the fallback levels are non-increasing and M_k ≤
      max(r_k, −1) at each; R29's OPEN item (H-EQ) is closed.
  (d) Lemma FLAT-ALL (𝒞^1O): at a fallback k of a scope run with M := M_k ≥ 0 and (h) at k and k+1: (i) F_k ⊆ F_{k+1}, and every v ∈
      R̄_{k+1} lies in R̄_k with the same route to o; (ii) COARSE_M(θ_{k+1}) = COARSE_M(θ_k); (iii) COARSE_M(Ξ_{k+1} v) = COARSE_M(Ξ_k v)
      for every v; (iv) M_{k+1} ≤ M. In (i), a switched cycle node's new cycle avoids o by H1 at k+1, not by "o's W-cycle / H2"
      (FBW-1, citation, closed).
  (e) Lemma STRETCH (𝒞^1O): if COARSE_M(Ξ_t v) is constant in t ∈ [s, e] for every v (M ≥ 0), each Even y is a level-M tail at most
      once among the fallbacks k of the scope run with s ≤ k ≤ e (packet: "k < e"; the proof covers k = e: FBW-2 = N-FBW-1, wording,
      closed).
  (f) Theorem PL (𝒞^1O): for a block of a scope run S at level M ≥ 0, (a) N ≤ n_E(1 + D_M); (b) the first COARSE_M(Ξ)-change j of a
      dirty interval is an S4a ε-transition with O_j > M ≥ E_j, lev(θ_j, θ_{j+1}) = O_j > M, and an absorption; (c) if r_t > M on
      [f_1, f_N], D_M ≤ (d_o − 1) + REL_M, so N ≤ n_E(d_o + REL_M). Corollary PL-S: if every block of S has r > M on it, the
      fallbacks of S at levels ≥ 0 number at most n_E·Σ_M (d_o + REL_M) ≤ n_E(n·d_o + REL(S)), REL(S) := #exit releases at fallbacks
      of S. Levels never reset along a scope run (compare R25 (d) Theorem FB, which resets at every non-tame transition).
- Not signed (packet §6, not to sign): CONJECTURE NJB (no COARSE_M change strictly inside a level-M block; gives ≤ n_E fallbacks per
  level) and NJ-INT; Lemma ABS-O (true, vacuous); OPEN: blocks on which r drops to M, fallbacks at level −1, REL(S).
- Honest limits: (i) FBW holds on every game; the rest is on 𝒞^1O. (ii) PL bounds fallbacks per block GIVEN D_M (and REL_M under
  r > M); NJB, REL and the r-drop blocks are OPEN here, so G-N5-TIME stays open. (iii) PL (b), (c) are vacuous in all data: D_M = 0 in
  every block for both referees, including REFEREE-2's climbs aimed at dirty intervals. (iv) Lane work after the pin (RDROP, PL (c′),
  MINSET, NO-RF-OLD, ENT-SHAPE; l-si bb8ed9e, dd5fa25, d7e0441, 8bb1134) is unrefereed and not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every 𝒞^1O game): REFEREE fbw_probe.py (own trace = n5.run): named 65 /
  library 252 / climb bests 3 / random general 6,000 / random 𝒞^1O 4,000 games, 0 failures; Even fallbacks / gates 272 / 837 (named,
  equal to the packet), 798 / 2,618 (library); in-scope fallbacks library 596 THR u* ≠ none + 9 EQ, named 252 + 4; tails never repeat
  inside a constant-COARSE_M run (172 library + 75 named blocks, max block 37 = cl9_rep_b); climb bests re-run n5 29/27, 40/33, 45/37,
  Oink zlk OK strategies verified. REFEREE-2 fbw_check.py (own code): every arena single switch at every Even fallback fails to raise
  W(y) (44,611 library, 788 random, ~3.4 M in climbs); FBW (a) on 3,921 library + 409 random + 140,045 climb gates, tight (ℓ = δ ≥ 0) at
  69,184 climb gates, never exceeded; FLAT-ALL 956 library + 77,192 climb checks; STRETCH 1,328 library + 81,057 climb tail checks, 0
  repeats. Lead re-ran cl9_rep_b (8efbbc9e): n5 45/37, Oink OK, one Odd choice vertex.
- Signatures: REFEREE docs/referee/R-N5-FBW.md (referee 9a94dc7; §C a04615b): P-OPT VALID; FBW, FBW-S, CLS2, STRETCH, PL-S SIGNED;
  FLAT-ALL SIGNED WITH GAP FBW-1 (closed); PL SIGNED WITH GAP FBW-2 (closed). REFEREE-2 docs/referee-2/R2-N5-FBW.md (referee-2 2596285,
  successor 6; §C bc2e7b7, successor 7): P-OPT VALID; FBW, FBW-S, CLS2, STRETCH (N-FBW-1), PL, PL-S SIGN; FLAT-ALL SIGN, after §C SIGN WITH
  GAP FBW-1 (citation, closed; CONFIRMED: the cycle is y′'s honest H_{k+1}-cycle, which H2 does not exclude; H1 at k+1 does). §C: no
  verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C): FBW-2 = N-FBW-1 (wording, closed); FBW-1 (citation, closed; REFEREE's
  fixes line adopted by both).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
