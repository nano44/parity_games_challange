# Draft RESULTS R53 (Lead, 2026-10-26 ~02:42Z, before commit 8371145b at 02:43:14Z; stamp corrected 03:02Z, the first stamp was not from date -u; both §Cs and the fixes file filled) — to CHECKER C62

### R53 [refereed-only] N5 on one-Odd-choice games: inside one phase, the OTHER-touching transitions and all transitions are bounded by explicit polynomials in four per-phase counts X, f^O, K_W and E (Theorem NH: O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E), T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E)), with Lemmas SW, ST, CL, STR-COUNT and NR (2026-10-26) — a REDUCTION signed as an implication (partial step-4 lemmas for N5; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C62.md, checker PENDING)
- Object (packet P-N5-NH-box42, added at l-new 44088266, pinned trunk 54ac72e6, unchanged during review): docs/new/P-N5-NH-box42.md, sha1
  93d19be8018e07a2727bbe1db5920198a0beb1eb (L-NEW successor 21, Opus 5.5). It is a different object from the box-30 packet P-N5-NH (RESULTS
  R22). The referees' notes are collected by the lane in docs/new/P-N5-NH-fixes-box43.md (l-new 478dd6e1, sha1
  7c499640460eb360bb0407ff051bdfb4907d4f1b, L-NEW successor 23: NH42-N1 + N-NH42-1, N-NH42-2, NH42-N2 + N-NH42-3, NH42-N3); on trunk;
  repairs only, no signed statement changes.
  Setting as in RESULTS R21, R22, R24 and R26 (𝒞^1O; phase; Ξ, W; θ := Ξ(o), w := W(o), c_θ := λ_Ξ(o), c_w := λ_W(o); H1, H2, H3, (h);
  EQ / THR / OTHER). R_k := the vertices whose (σ_k, τ)-play reaches o, with o ∈ R_k (the R22 convention; NH's counts are the same without
  o, NH42-N3), F_k := V ∖ R_k; a CROSSING is a transition with R_{k+1} ≠ R_k, X their number in the phase; a CROSSING-FREE INTERVAL I is a
  maximal run of the phase with R constant; a STRETCH is a maximal run of the phase with R, θ and w constant (R26); π_v is v's σ-route
  (the vertices of v's (σ, τ)-path before its first visit of o); route form and the classes P3′, U1, U2, U3, U23 as in R22 (c) and R26.
  O := the OTHER-touching transitions of the phase (an end is OTHER); f^O := its fallback transitions with an OTHER start state; K_W := the
  sum over the OTHER stretches of class U2, U3 or U23 of their non-fallback transitions with a W-change at some vertex of R; E := the sum
  over the OTHER stretches of class U3 or U23 of their transitions containing an event (R26 (c)); f_S, K_S, E_S the same inside a stretch
  S; Θ_I, WC_I the transitions of I at which θ, respectively w, changes; D := 4n(n − 1) + 1; n ≥ 2.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (a), (d), R19 (a),
  R21 (g), (i), R22 (a)-(c), R24 (d), (e), R26 (b), (d)):
  (a) Lemma SW: on a stretch S and for v ∈ R, (a) Ξ_k(v) is determined by π_v and θ, and W_k(v) by π_v and w; (b) hence a transition of S
      that changes Ξ or W at some vertex of R has some Even vertex of R switching.
  (b) Lemma ST: on a crossing-free interval I, (a) under H1 ∧ H2, H1 ∧ ¬H2 or ¬H1 ∧ H2 either every state of I is OTHER or none is; (b)
      under ¬H1 ∧ ¬H2 a state of I is OTHER iff θ ≠ w; (c) so OTHER status is constant on every stretch.
  (c) Lemma CL: for an OTHER stretch S, (a) H1, H2, c_θ, c_w and the route form of each frame are constant on S; (b) if both frames are in
      route form, c_θ ≠ c_w, so S is a P3′ or U1 piece, and a route-form stretch is a piece in the sense of R22 (c) and conversely; (c)
      otherwise S is a U2, U3 or U23 stretch in the sense of R26.
  (d) Lemma STR-COUNT: for a crossing-free interval I, (a) Θ_I ≤ n − 1 (under H1 every θ-change is a transition with a Ξ-change at some
      vertex of F); (b) under H2 every w-change is a transition with a Ξ-change at some vertex of F, so WC_I ≤ n − 1, and under ¬H2
      WC_I ≤ (f^O_I + 1)(|R|² − 1) + f^O_I; (c) I has at most 1 + Θ_I + WC_I ≤ n − 1 + (f^O_I + 1)n² stretches; (d) summed over the
      phase, N := Σ_I (1 + Θ_I + WC_I) ≤ n²(2X + 2 + f^O). (a) under ¬H1 proves RESULTS R26's READING R-1.
  (e) Lemma NR: for an OTHER stretch S with r := |R| and N_R(S) := its transitions with a Ξ-change at some vertex of R: P3′ N_R(S) ≤ (n + 1)r
      ≤ n³; U1 N_R(S) ≤ r + f_S + K + (K + f_S + 1)(r − 2) with K ≤ (f_S + 1)(r − 1)(r − 2), ≤ (f_S + 1)n³; U2 N_R(S) ≤ f_S + K_S +
      (K_S + f_S + 1)(r − 2) ≤ n(K_S + f_S + 1); U3, U23 N_R(S) ≤ f_S + K_S + E_S + (K_S + f_S + E_S + 1)(2r − 4) ≤ 2n(K_S + f_S + E_S
      + 1); in every class N_R(S) ≤ n³(1 + f_S) + 2n(K_S + E_S). K_S and E_S are the counts R26 defines; R26 (d)'s "R-changing" is read
      as "a transition with a switch on R", and by SW (b) a Ξ-change on R comes with a switch on R, so NR's use of U3C is exact in either
      reading (NH42-N1 + N-NH42-1, complementary, both referees).
  (f) Theorem NH: in one phase of N5 on 𝒞^1O, (a) O ≤ X + N + D·(n(X + 1) + (n³ + 1)N + n³f^O + 2n(K_W + E)), with N ≤ n²(2X + 2 + f^O);
      (b) O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E); (c) the phase has T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E) transitions. Signed as an
      implication: (NH′) (O polynomial per phase, RESULTS R21 limit (ii)) follows from (X), NFB-O, (E) and (K_W), each read as polynomial
      per phase; not a claim that any input is polynomial (NH42-N2 + N-NH42-3, both referees). "Event" (R26 (c)) may be read narrowly or
      broadly; the transition counts are equal by R26 (c)'s kinds-constant, and the theorem holds in both readings (N-NH42-2).
- Not signed (packet §4 Remarks, §5, §6, §7): the remarks; the input statuses of §5 (a READING, dated trunk 6d78b8f4 and superseded:
  FB-POLY LANDED as RESULTS R48, P-N5-FX signed by both referees (RESULTS R52 at CHECKER), (E) and (K_W) bounded per stretch given its
  fallbacks by RESULTS R50, a READING for this assembly; fixes file); the map to the R22, R24 and R26 readings (checked, consistent, a
  READING); the data.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside one phase. (ii) A REDUCTION: in its own terms (E) and (K_W) are OPEN; that R50 bounds them is a
  READING outside this entry. The 𝒞^1O running-time result is RESULTS R51, by another route (R50 (h)); NH is a second route to a
  per-phase transition bound. (iii) The exponents are loose; the bounds are far from the data (max O / Theorem NH (a) bound 1.47·10⁻⁴ in
  REFEREE-2's data). (iv) Thin data: random runs barely reach OTHER states (46 of 16,880 phases in REFEREE-2's data); the library carries
  the data; the R15d run step of Theorem NH is not exercised (no OTHER stretch in the data has two consecutive Ξ-flat transitions, so
  REFEREE-2's mutation "run" does not bite) and rests on RESULTS R15 (d); the U3 / U23 bounds near tightness are not exercised.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own nh42_probe.py on rl_engine): 253 𝒞^1O library games
  from SPEC S3's start, 990 phases, 101 with O > 0, ΣO = 833, OTHER stretches P3′ 131 / U1 353 / U2 66 / U3 104 / U23 51, per-phase maxima
  O 77, X 100, T 112, f^O 12, K_W 25, E 15, equal to the packet's §7 counts on an independent engine; with 3 random start pairs per game
  (759 more runs) 4,202 phases, 388 with O > 0; 0 failures. REFEREE-2 (own nh42_check.py, own definitions): 1,509 library runs (503 files,
  S3 + 2 random starts) 6,205 phases, 529 with O > 0; 1,006 runs on its own trace 4,123 phases; 7,000 random 𝒞^1O runs (n 6-16); 0
  violations; mutation controls sw, stc, nr bite, run does not (limit (iv)).
- Signatures: REFEREE docs/referee/R-N5-NH42.md (referee a47f8540, successor 10; §C 5fc234ba, successor 11): SW, ST, CL, STR-COUNT, NR,
  Theorem NH (a)-(c) SIGNED; notes NH42-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-NH42.md (referee-2 d2142087, successor 13; §C
  253fe5c5): all SIGN; notes N-NH42-1..3; no gap. §C (both): verdicts identical; joint gap map empty; NH42-N1 and N-NH42-1 complementary,
  N-NH42-2 accepted, NH42-N2 = N-NH42-3, NH42-N3 REFEREE only; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 (a subclass, inside a phase, a reduction). GAPS G-N5-TIME: open for general games
  (its 𝒞^1O part closed by RESULTS R51).
