# Draft RESULTS R68 (Lead, 2026-10-26 11:38Z by date -u; both reports and both §Cs filled; fixes file filled 12:03Z by date -u) — to CHECKER C77

### R68 [refereed-only] N5 on EVERY game: in every phase the W-honest states (Ξ = W) number at most f + 4n² − 3n (Lemma HON), a fallback at a W-honest state is flat and ends the phase at a saturated W-honest state (SAT0, HON-FB), so f may be replaced by the in-gap fallbacks f_in (HON′), and the D = ∅ states, the D = ∅ epochs and their transitions number at most f_in + 4n² − 3n (HON-0, which implies RESULTS R66's bound); a run with D ⊆ {u} is an N5^τ run on the one-Odd-choice game G^u (RESTRICT_u, REPRO_u), and the {u}-intervals of a phase number at most 1 + f_in + 4n² − 3n + X_dir + X_big (REC-1 (a)); as IMPLICATIONS from premise (Στ), u-runs have length ≤ T*(G^u) + 1 (EP-1u) and the |D| = 1 states of a phase are bounded by REC-1 (b)-(d) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (reductions to f_in, X_dir and X_big; not free of f; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C77.md, checker PENDING)
- Object (packet P-N5-HON, added at l-new 67a7b54d, pinned trunk 31835c4b, unchanged during review): docs/new/P-N5-HON-box46.md, sha1
  07f8e767cfca12d29c8f6f2e3f03358326abbef1 (L-NEW successor 25, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-HON-fixes-box46.md (l-new 0238b1cb, sha1 54985acfbfb0feb0e8bb3b04d882df78eaf72f1b, L-NEW successor 26: N-HON-1..5,
  HON-N1..N4, 46 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k; Ξ_k; W_k := V_{σ_k,τ_k} in G_τ; λ, λ_W; phases as in
  RESULTS R38 (a); f := the in-phase S4c fallbacks of a phase; Q, D_k, epochs as in RESULTS R64. A state is W-HONEST if Ξ_k = W_k pointwise
  (every D = ∅ state is); LEV(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of G_τ with ≤ j edges to a
  cycle node of λ (value as in RESULTS R17 Lemma P); SATURATED if LEV = n − 1. f_in := the in-phase fallbacks of a phase at non-W-honest
  states strictly between two W-honest states (f_in ≤ f). G^u: G with every Odd v ∈ Q ∖ {u} cut to τ(v) (u keeps its edges); a u-run is a
  maximal run of a phase with D_k ⊆ {u}; a {u}-interval is a maximal run with D_k = {u}. X_dir := the in-phase transitions with
  |D_k| = |D_{k+1}| = 1 and D_k ≠ D_{k+1}; X_big := those with |D_k| ≥ 2 and |D_{k+1}| = 1. T*(G^u) := RESULTS R51 (a)'s per-phase bound at
  G^u's parameters, T*_Q := max_u T*(G^u).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC (S2, S4a, S4c with FIX 3);
  RESULTS R15 (a), (d); R17 (a) (V1)/(V2), (F1)/(F2), R17 (b) Lemma P (its induction step), (c) Theorem PH's case split, (d); R18 (d) Lemma S
  (a), (c); R21 (a) Lemma XW (= (VJ), RESULTS R57); R23 (g) Lemma WM (game-general, RESULTS R63 XEP-N2); R64 (a), (b) with the repair EPR-1
  (proofs read with G^u in place of G′_E); for the implications, premise (Στ) of RESULTS R64 (e) and R51 (a); the standing SPEC premise 1E-N3
  (RESULTS R57), under which both referees sign (N-HON-3, REFEREE-2; accepted by REFEREE):
  (a) Lemma HON: in every phase, the W-honest states number at most f + 4n² − 3n.
  (b) Lemma SAT0: if σ_k has no W-improving edge in G_τ, then W_k(x) ⪰ value(r) for every x and every such simple path r. In its Odd case the
      packet's parenthesis "(r′ and z's play avoid x)" reads "z's path to its cycle node avoids x" (N-HON-1, REFEREE-2; a note, settled in
      both §Cs).
  (c) Lemma HON-FB: a fallback h → h + 1 at a W-honest state h is flat (values unchanged), leaves no W-improving edge, and lands on a
      W-honest, saturated state that is the phase's last ((i)-(iv)).
  (d) Corollary HON′: the W-honest states of a phase number at most f_in + 4n² − 3n.
  (e) Corollary HON-0: (a) the D = ∅ states, (b) N_0, the epochs with D_E = ∅, and (c) the in-phase transitions out of D = ∅ states each
      number at most f_in + 4n² − 3n. Relation to RESULTS R66 (REC-0), both confirmed by both referees: HON-0 (b) implies R66 (a) strictly,
      since (f + 1)(n + 1) + 4n(n − 1) + 1 − (f + 4n² − 3n) = f·n + 2 > 0 and f_in ≤ f, and HON-0 (c) implies R66 (b) without the factor n + m;
      neither proof uses the other, nor SN-PREFIX_D nor EP-0, but the premise sets overlap: XW is in both chains (HON-N1, REFEREE), so the
      packet's "HON-FB adds XW" is inexact.
  (f) Lemma RESTRICT_u: for every state k with D_k ⊆ {u}, RESULTS R64 (a) (i)-(iv) hold with G′_E replaced by G^u. Corollary REPRO_u: N5^τ on
      G^u from (σ_x, τ) reproduces a u-run J = (x, …, y) of N5 on G state by state, with the same fallback types, through y′ := x + len(J), in
      one N5^τ phase as read with EPR-1.
  (g) Theorem REC-1 (a): in every phase the {u}-intervals, over all u ∈ Q, number at most 1 + (f_in + 4n² − 3n) + X_dir + X_big.
  (h) IMPLICATIONS from (Στ) (signed as implications, as the packet states them): Corollary EP-1u: every u-run J has len(J) ≤ T*(G^u) + 1.
      Theorem REC-1: (b) every {u}-interval has at most T*(G^u) + 2 states; (c) the states with |D_k| = 1, and the epochs with |D_E| = 1, number
      at most (1 + f_in + 4n² − 3n + X_dir + X_big)·(T*_Q + 2); (d) if every state of the phase has |D_k| ≤ 1, then X_big = 0 and the phase has
      at most (f_in + 4n² − 3n) + (1 + f_in + 4n² − 3n + X_dir)·(T*_Q + 2) states. Both referees note that (Στ) is the premise of RESULTS R64
      (e) word for word, so (h) holds at RESULTS R65's audit strength (N-HON-4).
  Q-R17 (as in RESULTS R66 (c)), answered YES by both in HON's own use, with REFEREE's three-use list, accepted by REFEREE-2: Lemma HON's
  step 1 uses the full step at a W-honest state h, the absence of a cycle-node change coming from the sandwich W_h ⊴ W_{h+1} ⊴ W_{h′} (WM
  along a fallback-free gap); SAT0 uses Case A at one state, without (F2); HON-FB (i) uses the B1/B2 outcome list (re-derived by REFEREE).
- Not signed (packet §5, §6): CONJECTURE HON-FF (the level rises across every gap between W-honest states, fallbacks included; it would give
  W-honest states ≤ 4n² − 3n per phase, free of f), OPEN; its three DEAD routes, recorded in the packet with instances: IMM (immfail_n14, sha1
  db3fc2ca), IMM′ (immp_cex_n11, sha1 1dd7f585, and exitr_cex_n16), FB-WLEV (b5_o11, sha1 db4fe55a); also DEAD there as context: the
  permanent Ξ-level in H_C for |D_C| = 1 (thclimb_n12_s11) and "no in-phase fallback at a W-honest state" (b4_n5_other_0, replaced by
  HON-FB); the data. L-COMP successor 5's later add-on (l-comp 15bcfa06; DATA, not a referee check) finds 0 HON-FF failures with exact LEV
  and pins three more inside-fallback gaps (up to 12 fallbacks in one gap, ffin12_n32).
- Honest limits: (i) Reductions: f_in, X_dir and X_big are not bounded here, and (h) needs T*(G^u), which is polynomial but very large (R51 (a)).
  (ii) HON-FF would remove f_in; an HON-FF proof must replace both uses of the fallback-free hypothesis, the rise and the sandwich (HON-N3,
  REFEREE). (iii) Thin data where the proofs are subtle (N-HON-5): in-gap fallbacks occur in 9 phases (16 fallbacks) of REFEREE-2's library
  runs and in none of its random runs, and REFEREE's climbs produced none (one inside-gap case at LEV exact in its LEVMAX-20 lib41 pass); exact
  LEV meets 128 library step-1 checks in REFEREE-2's runs; the HON bound is never approached (max 57 W-honest states in a phase, both
  engines); REFEREE-2's mutation hon does not bite; T* is so large that (h) is tested only in its structural parts.
- Data (DATA, not proof): REFEREE (successor 14, own engine; lane code not run): 0 failures; lib41 1,101 runs, 5,365 phases, 20,473
  RESTRICT_u checks, max 57 W-honest states; lib41 n ≤ 20 at exact LEV (422 step-1 gaps); random games n 4-11 (9,000 runs) and n 12-22
  (4,500 runs); climbs: 48,751 candidates with LEV (235,399 step-1 gaps) and 19,754 without; controls: MUT=1 (G^u cut at u) RU1 55, RU2 46,
  REPU 15 failures, MUT=3 (a rise of 2) 5 of 70; IMM′'s failure reproduced on immp_cex_n11. REFEREE-2 (successor 16, own hon_check.py with
  exact LEV for n ≤ 11 and its own N5^τ for REPRO_u; lane code not run): 23,344 runs over its §4.2 rows (packet and lane instances, lib41
  minus referee games, its 503 𝒞^1O files, random games with 2-4 Odd choice vertices, random 𝒞^kO n 12-20), 0 violations; longest u-run
  reproduced by N5^τ on G^u 112 transitions (xsn91_n48); mutations fb4, ru, r1 and s1 bite.
- Signatures: REFEREE docs/referee/R-N5-HON.md (referee e7f9bc31, independence-line correction 59121877, §C a00a15c0, successor 14): all
  §1-§4 items SIGNED, (h) as implications, no gap; §2 claims TRUE; notes HON-N1..N4. REFEREE-2 docs/referee-2/R2-N5-HON.md (referee-2
  1566b439, §C 7f8bafdc, successor 16): all SIGN, (h) as implications, no gap; notes N-HON-1..5. §C (both): verdicts identical item by item;
  N-HON-1 settled as a note (REFEREE-2 withdrew "false", which applied only to the infinite play); HON-N1, HON-N2, HON-N3 accepted by
  REFEREE-2; N-HON-1, N-HON-3 accepted by REFEREE; N-HON-2, N-HON-4, N-HON-5 match REFEREE's report in substance; joint gap map empty;
  nothing open. Both signatures are under the standing SPEC premise 1E-N3 (P1, P2) (N-HON-3).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase reductions; no running-time bound). GAPS G-N5-TIME: open.
