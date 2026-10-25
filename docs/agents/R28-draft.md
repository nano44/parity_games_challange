# Draft RESULTS R28 (Lead, 2026-10-25 02:20Z by date -u) — LANDED in RESULTS Results 02:28Z (CHECKER C37 f5c4672 PASS), after R27

### R28 [refereed-only] N5 on one-Odd-choice games: off crossings σ̄(o) never outruns Even (Lemma OE, with a local used-level freeze U-loc), so non-tame transitions, fallbacks and carries per phase are polynomial in crossings and wakes (Corollary OX) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C37.md, checker PENDING)
- Object (packet P-N5-OE, pinned trunk 361d18c, unchanged during review): docs/new/P-N5-OE-box32.md, sha1
  adeccd898ad1e4de6532fc3a77a9d600d8a0bc16 (L-NEW successor 12, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-OE-fixes-box32.md (l-new 7ad82a9, on trunk; sha1 5f06276a32824c872493b92a82081c13e6d0ba01, L-NEW successor 13; a record,
  not itself refereed text).
  Setting as in RESULTS R27 (relevant changes, used level L_k, NU, phase with λ_Ξ and τ constant, R, F, crossing, wakes, K; Ξ_k = Θ_{H_k},
  ENG-1). E_k := the max level of the relevant Even changes at k → k+1 (⊥ if none); O_k := the level of the relevant σ̄(o) change (⊥ if
  none); on 𝒞^1O, L_k = max(E_k, O_k). The packet's phase key (λ_Ξ, τ) is coarser than R25's (λ_Ξ, λ_U, τ); the cited R22 TC (i) and R25
  FB, J1, CAP-1 use only λ_Ξ and τ or hold statewise, so they apply (N-OE-3, closed).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma U-loc (any game, inside a phase): if every relevant change at a vertex of v's H_{k+1}-path before its first visit of
      c := λ(v) has level ≤ L, then COARSE_L(Ξ_{k+1}(v)) = COARSE_L(Ξ_k(v)) (R27 (a) Lemma U's proof, localised).
  (b) Lemma OE (𝒞^1O): at a transition of a phase with R_k = R_{k+1} (no crossing), O_k ≤ E_k; so σ̄(o) makes no relevant change of
      level ≠ ⊥ when Even makes no relevant change. The packet's "In particular" sentence (no relevant σ̄(o) change at all when Even makes
      none) is stronger than the proof by a level-⊥ tie move at o; it is unproved, not refuted (0 such cases in all data; tie changes
      off crossings occur only with E_k ≠ ⊥: REFEREE library 2 / random 50, REFEREE-2 library 2 / random 5) and is not used (OE-1 =
      N-OE-1, wording). Step 1 uses CAP-1 (σ̄(o) a full Ξ-minimiser when λ(o) ≠ o, including o on its honest cycle: RESULTS R25 CAP-1,
      REFEREE's case proof, adopted by REFEREE-2 in R2-N5-FB §C.3; OE-2, closed); step 3 compares by (C1) and (C3) (OE-3, wording) and uses
      that under H1 x0's honest play is the tail of o's, so it avoids o (N-OE-2, wording).
  (c) Corollary OX (𝒞^1O): in a phase with X crossings, K wakes and f fallback transitions, (i) ε ≤ X; (ii) J ≤ X; (iii) ρ ≤ 2f + 2X + K;
      (iv) f ≤ n_E(2n − 1)(X + 1) + X; (v) T ≤ (m − n + 1)·((n + 1)(2f + 2X + K + 1)·n(n − 1) + X + 1) = O(m·n⁵·(1 + X + K)); f and T
      count transitions with both ends in the phase (R25 FB-2; OX-1, wording). (From R27 Theorem LP and Corollary LP′ step 2, R25 (d)
      Theorem FB and (e) J1, R15 (d); sharper than R27 (h) Corollary XJ: no S_o or Θ term.)
- Reading (not signed): per phase of o-cyclic 𝒞^1O, everything is polynomial in X (crossings, ≡ Z up to a factor n by R23 LV′, the
  direction a bound on Z needs) and K (wakes: in U1 pieces bounded by R24 Theorem U1; in U2 / U3 / U23 stretches by R26's corollaries in
  terms of the open (E) and (K_W)). RESULTS R25's (J-poly) and the fallback count follow from (X) with J ≤ X.
- Honest limits: (i) U-loc holds on every game inside a phase; OE and OX are on 𝒞^1O. (ii) X and K per phase are OPEN, so G-N5-TIME stays
  open; the phase count (Lemma Φ) is unrefereed. (iii) The wake term is barely exercised: K ≤ 1 in both referees' data. (iv) Both
  referees' DATA show O_k > E_k only at crossings and every non-tame transition at a crossing; J = X is attained (jcl_zcl_cu_n48:
  J 17 = X 17; Lead re-run n5 23/1, Oink zlk OK strategies verified, one Odd choice vertex).
- Data (DATA, not proof; every probe asserts one Odd choice vertex): REFEREE oe_probe.py (own code, trace asserted = n5.run): 234 library
  𝒞^1O files, 5,603 in-phase transitions, 0 failures (crossing-free σ̄(o) changes 436 H1 + 11 ¬H1; O_k > E_k 279 times, all crossings;
  235 non-tame, all crossings; the lane's oddlev.py gives identical counts); 11,000 random games, 0 failures. REFEREE-2 oe_check.py (own
  code): the 234-file library × 3 starts + 7,600 random runs (3,800 general for U-loc), 0 violations (U-loc 373,394 checks; OE 5,015
  crossing-free transitions; O_k > E_k 602 times, all crossings; 509 non-tame, all crossings; CAP-1 held at all 19,573 states with
  λ(o) ≠ o, and fails at 420 states with λ(o) = o, which OE never uses); climbs 27,200 runs (72,414 off-crossing σ̄(o) changes, 4,598
  under ¬H1; 30,002 non-tame transitions, all crossings; J − X never > 0). Three implementations agree on the canonical-start library
  counts (436 + 11 / 279 / 235).
- Signatures: REFEREE docs/referee/R-N5-OE.md (referee 5e98e33, stamp fix 696b08c; §C 8474881): U-loc SIGNED; OE SIGNED WITH GAPS OE-1,
  OE-2 (closed), OE-3; OX SIGNED (OX-1 wording); §C: no verdict differs; N-OE-3 missed by REFEREE, accepted. REFEREE-2
  docs/referee-2/R2-N5-OE.md (referee-2 ca6e5bd; §C ea6ad67): U-loc, OE, OX (i)-(v) SIGN (notes N-OE-1..3); §C: no disagreement of
  substance; its own "0 tie moves" corrected to the general count (library 2, random 5). Joint gap map (REFEREE §C, REFEREE-2 §C): OE-1 =
  N-OE-1 (wording); OE-2 (closed); OE-3 + N-OE-2 (wording); N-OE-3 (closed); OX-1 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
