# Draft RESULTS R85 (Lead, 2026-10-29 12:47Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C94

### R85 [refereed-only] N5 on EVERY game: (A) for a vertex v, a phase 𝒫 (λ and τ constant on 𝒫, c := λ(v)), v's path sets P_t := P(Ξ_t v) ⊆ R_c := the K ranks above rank(c) (K ≤ n − 1, r_1 < … < r_K), pos(r_k) := k, w(r) := +pos(r) if r is even and −pos(r) if r is odd (a rank's parity is Ω's of its vertex), Φ(A) := Σ_{r ∈ A} w(r), and a P-change A → B (a transition of 𝒫 with P_t ≠ P_{t+1}) MATCHED if some matching M ⊆ (A ∖ B) × (B ∖ A) has w(i) > w(o) on every pair (o, i) and leaves only even incoming and odd outgoing ranks uncovered, a CARRY otherwise: for distinct ranks o, i, w(i) > w(o) iff weight({i}) > weight({o}), and adding an even rank or removing an odd rank raises the weight (Fact A1); Φ(B) − Φ(A) ≥ 1 at every MATCHED P-change (Lemma MATCH-Φ); hence PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game, PCH and NM counting v's P-changes and carries in 𝒫 (Corollary, added statement (A)), with the same proof verbatim on any stretch of consecutive states with λ(v) constant (REFEREE §1b; REFEREE-2 §C "Joint: AGREED"); (B) at a state with τ(e) = h at an Odd vertex e, for a successor d ≠ h of e, a route π = (π_1 = d, …, π_m) of distinct Even vertices of G into e, Q := {π_1, …, π_m, e}, ρ the (τ̄, τ)-play from h and c_h the cycle node of Ξτ(h): (H1) every vertex of Q ranks above c_h, (H2) ρ (prefix and cycle) contains no vertex of Q and (H3) Q's vertex of largest rank has even Ω imply (e, d) ∉ Iτ (Lemma GATE-SHUT; via Fact B1: on valuations with the same cycle node and P ≠ P′, G^d's order reverses G's, and Fact B2: (VJ) of RESULTS R57 (a) on G^d), so on a stretch of states of one run with τ(e) = h and (H1)-(H3) at every state, (e, d) ∉ Iτ at each of them and τ never moves from h to d at a transition from one of them (added statement (B); the claim at t → t + 1 uses (H1)-(H3) at t only, π may differ from state to state, the Lemma uses no phase) (2026-10-29) — a REDUCTION of one vertex's path-set changes in one phase to its carries NM, and a structural lemma on Odd's improving edges that bounds no count (NM is OPEN, not bounded here; persistence of (H1)-(H3) not claimed; (H2)'s necessity not exhibited; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C94.md, checker PENDING)
- Object (L-LIT successor, Opus 5.5, D18, Lead reading L40; frozen, unchanged during review): packet P-N5-MPGS, docs/lit/P-N5-MPGS.md,
  sha1 24913a7f9efea437aa202b398113b7ce12890961, 246 lines (l-lit freeze a23179b01be61d7f85e37aa93c0ae55a2dde7de8,
  2026-10-29T11:03:06Z; quote base 1f15c91b; 9 quotes, docs/lit/P-N5-MPGS-quotecheck.py, sha1 74dbe8b4e6c4f37d4fdf7ca587eb479b5434579f,
  "quotes=9 bad=0"; all three referee reports measured the packet sha1 and the pins), Part (A) (A0 definitions, Fact A1, Lemma MATCH-Φ,
  added statement (A)) and Part (B) (B0 definitions, Fact B1, Fact B2, Lemma GATE-SHUT, added statement (B)). Superseded copies, not
  routed: P-N5-MATCHPHI (l-lit 12b7d12a, sha1 544705b74312e49ee31fd93ede1952396ebd12f1; Part (A)'s statements, reviewed before the
  supersession: REFEREE R-N5-MATCHPHI.md, REFEREE-2 R2-N5-MATCHPHI.md) and P-N5-GATESHUT (l-lit 1298d8b2, sha1
  affcae678b12bd8fc4ebc7a9b5759ee7b2442f39; no review). The fixes file's F1 ("WITHDRAWN") is withdrawn by F2 ("Lead ruling 11:27Z: F1
  withdrawn; P-N5-MPGS is the review object."). The referees' notes are collected by the lane in docs/lit/P-N5-MPGS-fixes.md (l-lit
  1bd2a11e, sha1 c0b0a0aaa0f2585492741bf228a97d4486c54303, L-LIT successor 2: F3-F10 answer MPGS-N1..N5, MATCH-N1..N4, N-MPGS-1..6,
  N-GS-1..5, N-MP-1..5, C.4 items 1-6 and J1-J15; 50 quotes checked by docs/lit/P-N5-MPGS-fixes-quotecheck.py, sha1
  dc3f8c0b1b447324183061385e4e3eb643e4f98c, "quotes=50 bad=0"); on trunk; "No statement of P-N5-MPGS changes; no item is FALSE" (fixes,
  Coverage). F3 appends the rise/fall summation to the proof of (A) and writes W as an equality; F4 appends to step 3 of GATE-SHUT's
  proof that h ∉ Q and that d = π_1 is Even; F5 adds two DATA notes to B3 (T34's (H1) test, T34's imports); F6 corrects B3's "The
  hypotheses are needed"; F7 corrects B4's "(H1) automatic"; F8 adds three optional one-liners (full order reversal; per-state reading
  of (B); (A) on λ-runs); F9 carries MATCHPHI's notes (sharpness at NM = 0 and the additivity line, both PROVED by L-LIT, unrefereed);
  F10 records notes needing no packet change. The statements below are in the frozen wording with those repairs.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; a phase is a maximal run of states with λ (Ξ's
  cycle-node map) and τ constant (RESULTS R38 (a), as in R84). Part (A): v a vertex, c := λ(v), constant on 𝒫; P_t := P(Ξ_t v), read
  as a set of ranks; R_c := {rank(u) : rank(u) > rank(c)} ⊇ P_t (by S1-rank, p'(u) > p'(c) iff rank(u) > rank(c)); K := |R_c| ≤ n − 1;
  a rank is even or odd as Ω of its vertex (R84 F5); weight(A) := Σ_{r ∈ A} s(r)2^r (R84 (a)); a P-change of v in 𝒫 is a transition
  t → t + 1 of 𝒫 (in-phase S4c fallbacks included) with P_t ≠ P_{t+1}, PCH_𝒫(v) their number; MATCHED: a matching M ⊆ (A ∖ B) × (B ∖ A)
  with (M1) "w(i) > w(o) for every (o, i) ∈ M", (M2) "every i ∈ B ∖ A not covered by M is even", (M3) "every o ∈ A ∖ B not covered by M
  is odd"; CARRY: a P-change that is not MATCHED; NM_𝒫(v) the number of carries of v in 𝒫. Part (B), at a state t of an N5 run (σ :=
  σ_t, τ := τ_t): G^d the dual game (owner swapped, Ω + 1); Ξτ S1's valuation of τ on G^d; τ̄ S1's optimal counterstrategy on G^d to
  τ, an Even strategy of G; ⊴ S1's order on G, ⊴_d S1's order on G^d (better for Odd of G); (e, w) ∈ Iτ iff e is Odd, w ≠ τ(e) and
  Ξτ(w) ▷_d Ξτ(τ(e)) (S2); π(x; σ′, τ) the play from x under (σ′, τ), a lasso, and V^d_{τ,σ′}(x) S1's valuation of it on G^d; the
  gate e, h := τ(e), d ≠ h, π, Q, ρ := π(h; τ̄, τ), c_h as in the title; (H1) "rank(u) > rank(c_h) for every u ∈ Q", (H2) "ρ, prefix and
  cycle, contains no vertex of Q", (H3) "the vertex of largest rank in Q has even Ω (in G)".
- Claims signed (both referees "(Opus 5.5, D15)", L37: REFEREE successor 17; REFEREE-2 successor 19, report of record); on every game;
  no item uses (P); premises LANDED: SPEC S1 (rank, valuation (c, P, ℓ), order, Odd's side on G^d), the SPEC ambiguity row A3 (G^d has
  G's ranks), S2, S4b, S4c (quote base 1f15c91b); RESULTS R57 (a) (VJ); RESULTS R84 (a) Fact DELTA; RESULTS R38 (a), as the phase
  definition only. Part (A) uses neither (MON) nor R84's TOP-SHAPE (packet A2: "Fact A1 also uses [DELTA]. It does not use (MON) or
  R84's TOP-SHAPE"; this repairs MATCH-N1 = N-MP-1, J11 "closed"). Standing premise, as in RESULTS R57 (b) (J6, REFEREE §C: "the RESULTS
  entry should carry the clause as R57 (b) does"): Ξτ(x) = V^d_{τ,τ̄}(x) is S1-val's definition (B0: "by definition"); that S1's
  procedure outputs it is SPEC conformance, the premise R57 (b) records ("that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance"); the code's match to SPEC is DATA (REFEREE-2 19 DENG, REFEREE-2 20 ENGXI, 0 differences).
  (a) Fact A1 (A2): "For distinct ranks o, i: w(i) > w(o) iff weight({i}) > weight({o}). Adding an even rank or removing an odd rank
      raises the weight." ([DELTA] with d = max(o, i): for i > o the exchange raises the weight iff i is even, and then w(i) = pos(i) >
      pos(o) ≥ w(o), else w(i) = −pos(i) < −pos(o) ≤ w(o); for o > i iff o is odd, and then w(o) = −pos(o) < −pos(i) ≤ w(i), else w(o) =
      pos(o) > pos(i) ≥ w(i); additions and removals: [DELTA] with d the added or removed rank.)
  (b) Lemma MATCH-Φ (A2): "At every MATCHED P-change A → B, Φ(B) − Φ(A) ≥ 1." (Φ(B) − Φ(A) = Σ_{(o,i) ∈ M}(w(i) − w(o)) +
      Σ_{uncovered i ∈ B∖A} pos(i) + Σ_{uncovered o ∈ A∖B} pos(o); every term is an integer ≥ 1 by (M1), (M2), (M3), and some term exists
      since A ≠ B.)
  (c) Added statement (A), Corollary (A2): "PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game"; in the
      packet's words "For every game, vertex v and phase 𝒫: PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)." (Proof with F3: W := max Φ −
      min Φ over subsets of R_c = Σ_{k=1}^{K} k = K(K+1)/2, an equality; Φ_t := Φ(P_t) changes only at P-changes; with R the sum of the
      positive and F of the absolute negative increments, R − F = Φ_end − Φ_start ≤ W; every MATCHED change adds ≥ 1 to R (Lemma
      MATCH-Φ), so #MATCHED ≤ R; negative increments occur only at carries, each ≤ W, so F ≤ W·NM_𝒫(v); so #MATCHED ≤ W + W·NM_𝒫(v) and
      PCH_𝒫(v) = #MATCHED + NM_𝒫(v). REFEREE MPGS-N1 = J4: "the inference is valid as a sketch"; REFEREE-2 §C D1: "Restore MATCHPHI's three
      lines". K ≤ n − 1 gives K(K+1)/2 ≤ n²/2 (A0; REFEREE-2 19 §1).)
  (c′) Signed as a proof step by REFEREE §1b and REFEREE-2 §C, not as an item of either REFEREE-2 MPGS report: (A) and its proof hold
      verbatim with 𝒫 replaced by any stretch of consecutive states of one run on which λ(v) is constant (a λ-run with τ free, fallbacks
      included), PCH and NM counted over that stretch (fixes F8 (c)). REFEREE §1b: "YES (Opus 5.5, D15), verbatim, on ANY sequence of
      consecutive states (phase, λ-run with τ free, or any stretch, fallbacks included) on which v's own cycle node c = λ(v) is
      constant", "No step reads τ, the phase, (MON) or the direction of the weight change. (Even only λ(v) for the single vertex v is
      needed, not all of λ_Ξ.)". REFEREE-2 §C (e1ec568a): "REFEREE-2 20 reached the same conclusion independently in R2-N5-COMPOSE §2.5
      (pushed 4b8afa95 before §1b was read), and added that the Odd side reads parities on G^d (N-C3)", "Joint: AGREED. This is the premise
      P-N5-COMPOSE §6 needs." (R2-N5-COMPOSE §2.5: "So "phase → λ-run" is not merely a reading: it is the same proof verbatim. ✓")
      REFEREE §C (8da7b717): "REFEREE-2 did not address this question (it was asked of the first referee); nothing in either REFEREE-2
      report contradicts it (N-MPGS-6: the Lemma uses no phase)."; it does not cite REFEREE-2's §C, pushed 21 s before it.
  (d) Fact B1 (B1): "For valuations X = (c, P, ℓ) and X′ = (c, P′, ℓ′) with the same cycle node c and P ≠ P′: X ◁_d X′ iff X′ ◁ X."
      (By [A3] G^d has G's ranks, so P and the cycle node (the vertex of maximal rank on the cycle) are the same in both readings; G^d's
      signed weight of P is −weight(P); with equal cycle nodes and P ≠ P′ both orders decide on the weights; ℓ is never reached.)
  (e) Fact B2 (B1): "For every positional Even strategy σ′ of G and every x: Ξτ(x) ⊴_d V^d_{τ,σ′}(x)." ([VJ] holds "on every game",
      hence on G^d, whose "Even" strategy is τ and whose "Odd" strategies are G's Even strategies; instantiate with σ := τ, τ′ := σ′.)
  (f) Lemma GATE-SHUT (B2): "At a state t with τ(e) = h, (H1), (H2) and (H3) imply (e, d) ∉ Iτ." (1: σ′ := τ̄ except σ′(π_k) := π_{k+1}
      (k < m), σ′(π_m) := e, a positional Even strategy of G differing from τ̄ only on π. 2 ((H2)): π(h; σ′, τ) = ρ. 3: π(d; σ′, τ) is π_1,
      …, π_m, e, then ρ, with F4: "Here h ∉ Q, because ρ starts at h and (H2) says ρ contains no vertex of Q; so the play, after π·e,
      enters ρ at its first vertex h and then follows step 2. And d = π_1 is an Even vertex of G (π consists of Even vertices, B0), so
      σ′(d) = π_2 (or e if m = 1) is set by step 1."; its cycle node is c_h and by (H1) its set is P(ρ) ∪ Q, Q ∩ P(ρ) = ∅ by (H2): V :=
      V^d_{τ,σ′}(d) = (c_h, P(ρ) ∪ Q, ℓ(ρ) + |Q|). 4 ((H3)): the top rank of Q is even and in the larger set, so [DELTA] gives
      weight(P(ρ) ∪ Q) > weight(P(ρ)), Ξτ(h) ◁ V, and V ◁_d Ξτ(h) by Fact B1. 5 ((VJ)): Fact B2 at x = d: Ξτ(d) ⊴_d V. 6: Ξτ(d) ⊴_d V
      ◁_d Ξτ(h) = Ξτ(τ(e)), so (e, d) ∉ Iτ by [S2].)
  (g) Added statement (B), Corollary (B2): "(H1)-(H3) at every state of a stretch on which τ(e) = h ⇒ (e, d) ∉ Iτ at every state of it,
      and τ never moves from h to d at a transition from it"; in the packet's words "Let [t_0, t_1] be a stretch of states of one run with
      τ_t(e) = h and (H1)-(H3) at every t ∈ [t_0, t_1]. Then (e, d) ∉ Iτ_t for every such t, and τ_{t+1}(e) ≠ d for every t ∈ [t_0, t_1]."
      (The first claim is the Lemma at each t; S4b: τ_{t+1}(e) ∈ A(e) = {τ_t(e)} ∪ {w : (e, w) ∈ Iτ_t}; S4c's Odd fallback moves e only to
      an Iτ_t-target; S4a and an Even fallback (FIX 3) leave τ.) Scope, as both referees read it (J8; fixes F8 (b)): the claim at t → t + 1
      uses (H1)-(H3) at t only and π may differ per state (REFEREE §C J8: "the Corollary (B) uses only the hypotheses at the transition's
      source state; π may differ per state"; REFEREE §2: "the first claim is the Lemma per state"); REFEREE-2 19 N-MPGS-6: "The Lemma holds
      at any state of any N5 run, in-phase or not (it uses no phase). The added statement (B) is per transition. Both are stated that way;
      nothing to repair." (Also REFEREE-2 20 N-GS-4, concurring.) B0, A0: REFEREE "CHECKED", REFEREE-2 19 "SIGNED (well formed)"; REFEREE's
      §C: "same content".
- Not signed: A3, B3 (DATA) and A4, B4 (READING), as the packet says, with their corrections: B3's last bullet "The hypotheses are needed:
  the unhypothesised form is false on these instances." is true of the three together, of (H1) alone and of (H3) alone, and NOT exhibited
  for (H2) alone (F6; REFEREE MPGS-N3, REFEREE-2 19 N-MPGS-1, REFEREE-2 20 N-GS-3; bullet "Honest limits" (iii)); B4's first bullet "(H1)
  is automatic" holds only at states where c_h is the sink (F7; REFEREE-2 19 N-MPGS-4: "consistent with my H_n data only where c_h is the
  sink"; REFEREE J9; "These are the reopenings §B3 describes"); B3's T34 tests (H1) only as rank(c_h) < rank(d1_i), exact on H_n (hn.py
  l. 46-49: d1_i < d2_i < d3_i < e_i) and not a test of (H1) on other games (F5; MPGS-N4 = J2, N-MPGS-2, N-GS-5). The to-sign table's
  line for Fact A1, "MATCHED = decomposes into individually weight-raising one-rank moves", is not the signed Fact A1 (REFEREE §1: Fact A1
  "drops MATCHPHI's last sentence", "which the to-sign table still carries"; REFEREE-2 20: "N-MP-3 (additivity, one line) still applies to
  the table's wording"); it needs the additivity line (bullet "Referee strengthening" (iii)). The packet's A4 CONJECTURE NM = O(n) per
  vertex per phase (READING, OPEN) and B4's CONJECTURE NO-HIDE (not part of the packet). CONJECTURE H2-FREE (F6: at a state with τ(e) = h,
  (H1) and (H3) imply (e, d) ∉ Iτ): OPEN, "not claimed, not signed" (F6); REFEREE J1 "whether (H1) + (H3) suffice is OPEN", REFEREE-2 20
  N-GS-3 "NOT claimed by the packet and NOT signed here" (its partial argument is incomplete: "which I have not completed"). F9 (a) and
  F9 (b) are PROVED by L-LIT, unrefereed, and are not signed (bullet "Referee strengthening" (ii), (iii)).
- Referee strengthening (NOT part of this entry; REFEREE-2 20 is cited as "REFEREE-2 concurring" (Lead ruling 11:54Z, s20 status line),
  never as a third signature):
  (i) J7, the full order reversal (fixes F8 (a), a remark after Fact B1): "For ALL valuations X ≠ X′, X ◁_d X′ iff X′ ◁ X. GATE-SHUT uses
  only the case of Fact B1." REFEREE-2 concurring N-GS-2: "G^d's order is the exact reverse of G's on ALL valuations, not only on equal
  cycle nodes with P ≠ P′", "the Lemma needs only the packet's B1" (b1_general.txt, 200,000 random valuation pairs, 0 violations);
  REFEREE §C J7: "I re-derived it: Ω(c) even, p′ = 2r → p′_d = 2r + 1, reward −(2r + 1); Ω(c) odd, −(2r + 1) → 2r; both = −reward − 1.
  Correct"; not raised by REFEREE-2 19 (REFEREE-2 §C D7: "Not raised by the others"). (ii) J12, sharpness at NM = 0: as a statement about
  subset sequences of R_c the bound is attained with NM = 0 (PCH = W = K(K+1)/2). In REFEREE-2 19's verdict line for (A) as an addition
  ("SIGNED. The first term is SHARP at NM = 0 (N-MP-2)"; R2-N5-MATCHPHI N-MP-2: "all-odd parities, K ≤ 7, exhaustive"); REFEREE
  R-N5-MATCHPHI MATCH-N4: "attained by abstract all-matched chains (§3); the bound is sharp as a statement about subset sequences. Its N5
  tightness is open." (its §3: "for all-even ranks and K = 1..8"); REFEREE §C: "may carry J7, J8, J12 as referees' remarks". F9 (a) gives
  an explicit all-odd construction, PROVED (L-LIT, unrefereed). Whether N5 attains it is OPEN. (iii) J13, additivity (F9 (b), PROVED by
  L-LIT, unrefereed): weight(S ∖ {o} ∪ {i}) − weight(S) = weight({i}) − weight({o}), so a MATCHED change raises the weight of the current
  set (weight(B) > weight(A)); in the superseded reviews REFEREE-2 19 (F1add, F1b: "Hence a MATCHED change always raises the weight (F1b:
  0 failures on all 2,374,900 ordered pairs, K ≤ 7)") and REFEREE ("immediate from additivity of the weight": MATCH-N2). READING (F9 (b),
  not signed): in a phase, where every P-change raises the weight (R84), the carries are exactly the weight-raising P-changes that do
  not decompose so. (iv) J1, (H1) alone gives e ∉ ρ (F6, PROVED by L-LIT, unrefereed as an item): REFEREE J1: "I checked the e ∉ ρ step:
  correct"; REFEREE-2 concurring §2.4: "(H1) already excludes e ∈ ρ"; so (H2) adds only "ρ avoids π_1, …, π_m". (v) REFEREE-2
  concurring N-C3 (R2-N5-COMPOSE, quoted in REFEREE-2 §C): on the Odd side (G^d), MATCHED, w and NM^U are read with G^d's parities.
- Honest limits: (i) MATCH-Φ and (A) are a REDUCTION of the path-set changes of one vertex in one phase to its carries NM. NM is OPEN and
  not bounded here (packet: "It does not bound the carries; NM is OPEN"; REFEREE-2 19: "(A) is a REDUCTION to NM (OPEN)"). DATA only,
  not refereed: carries of one vertex in one phase reach NM = 2n² + 5n − 5 on L-RED's R109 topfix family (claude/l-red e5c9b628,
  docs/red/R109-hn-topgate.md §5, phases keyed by (λ_Ξ, τ); n is Friedmann's index, N = 21n vertices: max NM 343 = 1.361 N at n 12,
  N 252; "Carries of ONE vertex in ONE phase are Θ(N²) on this family"). Lead reading: these DATA are against the packet's A4
  CONJECTURE "NM = O(n) per vertex per phase" (READING, OPEN, not signed) on that family. T33 Part B (DATA): under abstract monotone set
  sequences with a fixed top NM can be exponential (k = 8: 255 P-changes, NM 63); these are not N5 runs. (ii) (B) bounds no count and does not claim that (H1)-(H3) persist (packet "What is not claimed": "a cycle node above
  the gate can appear"; REFEREE-2 19: "8,829 h → d moves of τ at gates where some hypothesis fails (CTL_flip_nohyp)"). On L-RED's R109
  family (H1) fails at the τ-gates (DATA, R109 FINDINGS 2: "τ-gates never shut, because (H1) fails"). (iii) (H2)'s necessity is not
  exhibited, in all three data sets: REFEREE MUT 2 (8,975 relaxed hits, all still shut); REFEREE-2 19 noH2 0 of 15,528; REFEREE-2 20 X2
  0 of 1,648 (426 under every τ of their game). (H1) and (H3) each bite alone (REFEREE MUT 3: Lemma 576, Corollary 66; MUT 1: Lemma 240,
  Corollary 89; REFEREE-2 19 noH1 5,673, noH3 4,422; REFEREE-2 20 X1, X3 > 0). Whether (H1) + (H3) suffice is OPEN (CONJECTURE
  H2-FREE). (iv) The referees' gate enumerations are capped (REFEREE DFS budget 4,000 nodes; REFEREE-2 19 π ≤ 6 vertices, ≤ 40 per
  (e, d); REFEREE-2 20 ≤ 64 per (state, e, d)); the proof has no length condition (J10). (v) Nothing here bounds N5's running time;
  not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet A3, B3), run as `python3 -I`: docs/lit/T33-match-phi-check.py (sha1
  6853179bf10bdf1c3d9cae61c939b1054aa4b70c) "A: improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534" (80640 / 0 /
  32534; Part A brute-forces the Lemma for K = 6), Part B k = 1..8 strict-rise=True, fixed-top=True, P-changes 1, 3, 7, …, 255, NM 0, 0,
  1, 3, 7, 15, 31, 63; docs/lit/T34-gateshut-check.py (sha1 7c33508b2ef6639da2ce736028bcf013f152ed75, N5 by L-COMP's n5b on Friedmann's
  H_n by L-COMP's hn.py, mode fig) four lines, gate-states with τ(e) = h / with (H1), (H2) / violations / h → d1 flips, of which with
  (H1), (H2): "3 0 0" 135 / 135 / 0 / 0, 0; "3 200 3" 14385 / 14217 / 0 / 102, 0; "4 100 4" 12045 / 11911 / 0 / 97, 0; "5 30 5" 5783 /
  5705 / 0 / 48, 0; S3 and F only, n = 4, 5, 6, 8: 228, 350, 510, 872 gate-states, all with (H1), (H2), 0 violations, 0 flips; the 247
  flips all fail (H1) or (H2) (B3's example rand4 fails (H1), F6). T34 imports hn, census, n5b from a hard-coded ROOT, the checkout at
  run time, not the freeze commit (F5, J3: tree ids of the six directories equal at a23179b0 and trunk 923b5b12, measured by L-LIT).
  Quote checks: P-N5-MPGS-quotecheck.py "quotes=9 bad=0"; P-N5-MPGS-fixes-quotecheck.py "quotes=50 bad=0". All three referees
  reproduced T33, T34 (four lines and S3 + F) and the quote check exactly; both quote checks re-run for this draft on trunk (docs/lit
  equal to l-lit 1bd2a11e): 9/0, 50/0. L-COMP
  box 18 (claude/l-comp fc0758fc, via the Lead; packet A3): the MATCHED test agrees with L-COMP's on 258,048 pairs; NM per (vertex,
  phase) at most 62 (n 581), max NM/n 1.18 (pl130_n40). REFEREE (successor 17; own scratch/matchphi_probe.py, mp_chain.py (Part (A),
  R-N5-MATCHPHI.md, carried over) and scratch/gateshut_probe.py (sha1 84a77eb7…) on its engine rl_engine; no L-COMP / L-LIT import; H_n
  exported once to .pg): Part (A) exhaustive K = 6, 7: 258,048 + 2,080,768 ordered pairs (78,268 + 571,298 MATCHED), 0 failures; 3,000 +
  2,000 arbitrary and as many weight-increasing sequences, 0 failures; N5: pl130_n40 1 run, 962 P-changes, 688 carries, max PCH / NM per
  (v, phase) 62 / 47 (1.175 n); alt_all n ≤ 100 379 runs, 45,234, 25,585, 67 / 41 (0.90); L-RED instances 319 runs, 29,501, 15,978,
  62 / 47; lib41 349 runs, 30,700, 15,751, 37 / 18; λ-runs (§1b, LAMRUN=1) lib41 38,243 (vertex, λ-run) checks, 31,662 P-changes, 16,291
  carries, 0 failures (the L-RED λ-run batch stopped unfinished, recorded); MUT1 ((M2) dropped) bites 43,975, MUT3 (W := K) bites on
  all-matched chains. Part (B): H_3, H_4 8 runs, 915 (e, d) pairs, 761 states with an (H1)-(H3) route, 733 Corollary checks; H_5, H_6 8,
  1,983, 1,722, 1,678; lib1140 1,857, 334,123, 10,198, 9,052; lib41 1,076, 198,065, 7,857, 6,825; rand_ck 12,000, 176,427, 1,949,
  1,196; 0 failures; step 4 and Fact B2 at every hit, 22,487 checks, 0 failures; Fact B1 on 3,712,665 dual-valuation pairs, 0 failures;
  MUT 1 / 2 / 3 as in "Honest limits" (iii). REFEREE-2 19 (own R2-N5-MATCHPHI/mphi_check.py and R2-N5-MPGS/gateshut_check.py on its
  lane's SPEC loop; no lane module imported): Part (A) every ordered pair, K ≤ 7, every parity pattern, 2,374,900 pairs (661,892
  MATCHED), 0 failures; 25,000 arbitrary subset sequences; N5 alt_all 413 runs, 53,549 P-changes, 23,330 / 30,219 MATCHED / carries,
  max NM 62 (gate_K64_n581, n 581), max NM/n 0.90 (ret22_n40), max PCH 67; lib41_noref × 3 1,230, 70,808, 31,014 / 39,794, 18, 0.469,
  37; named 19, 13,282, 3,763 / 9,519, 47 (pl130_n40), 1.175, 72 (l121_d29); random kO 9,000, 1,221, 872 / 349, 1, 0.125, 2; controls
  CTL_noM2 375,337, CTL_noM1 547,514, CTL_carry_rise 525,558. Part (B): gates with (H1)-(H3) / CORB transitions: H_n 71 runs 22,798 /
  22,412; lib41_noref × 3 1,230 runs 33,572 / 8,934; alt_all 413 runs 12,713 / 4,820; random 30,000 runs 3,902 / 2,123; 72,985 gates,
  0 violations of DENG, B1, GS, S3, S4, S5, CORB; Fact B1 on 10,036,398 same-cycle-node pairs; controls noH1 28/28 (H_n), 2,938/214,496,
  871/104,971, 1,836/20,780; noH2 0/10,837, 0/4,450, 0/241; noH3 2,777/210,912, 1,064/239,267, 581/2,539. REFEREE-2 concurring (successor
  20; own gs_check.py on R2-N5-DUAL/dual_check.Runner and si.py; L-COMP's n5b and hn.py not imported): (state, e, d) with (H1)-(H3) on
  run states (random n 5-14, n 15-24, lib41_noref, H3-H6) 1,523 / 419 / 6,017 / 2,348 and at arbitrary or every τ (tau n 5-10, n 8-14;
  alltau n 4-8, n 8-11) 6,174 / 2,219 / 7,778 / 5,193; 0 violations of GS, GS2-GS5, GSC, B1, ENGXI; X1 / X2 / X3 as in its §3.2 (H3-H6:
  X1 32 of 32); B1 on 76.3M random pairs; λ-run data (REFEREE-2 §C): 56,999 Even and 21,286 Odd (vertex, λ-run) pairs, 0 failures. Run
  counts differ by start set and corpus (REFEREE lib41 1,076 runs in Part (B) and 349 in Part (A); REFEREE-2 lib41_noref × 3 1,230); not
  reconciled in any report. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-MPGS.md (report c3a0b5d7, sha1 b1a0310d1020ad7d9182d954666f4da4071bdc6b there, successor 17; §1b
  7cd20b05, sha1 988945c360be9b48a41f2db799536c365dfd54a2 there; §C 8da7b717, sha1 7c293a20af130a968df5e91cfee29f072db397dd there,
  successor 18): A0 CHECKED; Fact A1 SIGNED; Lemma MATCH-Φ SIGNED; added statement (A) SIGNED ("proof condensed; MPGS-N1"); B0-B1
  definitions CHECKED; Fact B1 SIGNED; Fact B2 SIGNED; Lemma GATE-SHUT (steps 1-6) SIGNED; added statement (B) SIGNED; A3, B3 reproduced
  exactly, not signed; A4, B4 not signed; §1b λ-runs "YES (Opus 5.5, D15), verbatim"; quotes 9 of 9 (own scratch/flip_quotes.py:
  "QUOTES 9 FAILED 0"); notes MPGS-N1..N5 (MATCH-N2..N4 carried over); "No gap." REFEREE-2 of record docs/referee-2/R2-N5-MPGS.md (report
  0c4524f0, sha1 5ed019b764708f5c61d09e46db4b591672a5a1bf there; successor 19): A0 SIGNED; Fact A1, Lemma MATCH-Φ SIGNED; added
  statement (A) SIGNED ("The first term is SHARP at NM = 0 (N-MP-2)"); B0 "SIGNED (well formed)"; Fact B1, Fact B2, Lemma GATE-SHUT (6
  steps), added statement (B) SIGNED; pinned re-runs "REPRODUCED exactly"; quotes "9/9 VERBATIM" (own qcheck 9/9, SHIFT=1 control 0/9);
  A3, A4, B3, B4 not signed; notes N-MPGS-1..6 (N-MP-2..5 carried over); "No gap." REFEREE-2 concurring docs/referee-2/R2-N5-MPGS-s20.md
  (report c1c4676a, sha1 b34e67d55479895fa3cafa6dad84734a8edb8dc1 there; marked c5f9e76e, sha1 ee4ca241ed54be2f19b3d0dd1076775c92364cd9
  there, and 152503ca, sha1 15f14eb487418908a4e063e407676f85827c0af5 there; successor 20; written without reading 19's report): every
  item SIGNED, no gap, no item FALSE; notes N-GS-1..5; not a third signature. REFEREE-2 §C docs/referee-2/R2-N5-MPGS-C.md (cfc77e84,
  sha1 8d8245369966b60611f9a8ea59dd7cca1e9bfe8a there; final e1ec568a, sha1 6a023656a417841297077b9db5aba6383196442f there; successor 20).
  Superseded-copy reviews (P-N5-MATCHPHI, not routed for landing): REFEREE docs/referee/R-N5-MATCHPHI.md (2f2c40dc, sha1
  b17f092b18e49eccd17c52ac3fb14fca840922b8 there; definitions CHECKED, Fact 1, Lemma MATCH-Φ, Corollary SIGNED, no gap, MATCH-N1..N4)
  and REFEREE-2 docs/referee-2/R2-N5-MATCHPHI.md (5ba3e21d, sha1 097e9858569e2623175b4ab2e314c39cd25c42d3 there; all SIGNED, no gap,
  N-MP-1..5); both carried over to Part (A) by content after a diff (REFEREE §1; REFEREE-2 19 §1; REFEREE-2 20 §1). INDEPENDENCE: REFEREE
  had no docs/referee-2/ MPGS file on its tree and saw 16 names matching "mpgs" on origin/claude/referee-2 at 11:42Z ("names only, none
  opened"); it did not open R2-N5-MATCHPHI.md; it read both REFEREE-2 reports after c3a0b5d7 and 7cd20b05 were pushed (§C). REFEREE-2 19
  opened no file under docs/referee/ on MPGS or MATCHPHI (name counts 0 at 11:17:40Z and 11:25:43Z); REFEREE-2 20 opened no file under
  docs/referee/ before its report (0 at 11:33:19Z and 11:36:04Z), first opened c3a0b5d7 at 12:05Z and §1b at 12:17Z, after both
  REFEREE-2 reports were pushed (§C Inputs). No review imported lane code; the lane's pinned scripts were read, then run, in worktrees
  at a23179b0. §C (both): verdicts identical (REFEREE §C: "VERDICTS IDENTICAL. Every item (A0-A2, B0-B2, Added statements (A), (B)) is
  SIGNED by all three reports; none FALSE; no gap on any side"; REFEREE-2 §C C.1: "SIGNED by both"); joint gap map EMPTY (REFEREE "JOINT
  GAP MAP: EMPTY."; REFEREE-2 "Joint gap map: EMPTY."); REFEREE "E-ITEMS (must change before landing): NONE. Every signed statement and
  proof is correct as frozen at a23179b0."; REFEREE-2 classes C.4 items 1-5 (D1-D4 and C.2's (H2) point) as E, text fixes for the fixes
  file, done as F3-F7 (fixes: "Both agree no statement or proof changes"); J1-J15 / D1-D10 answered in F3-F10; REFEREE: "Nothing open on
  MPGS. NM is OPEN; G-N5-TIME stays OPEN."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction of one vertex's path-set changes in one phase of N5 to its
  carries NM, which are not bounded, and a structural lemma on Odd's improving edges in N5; no running-time bound, no algorithm claim).
  GAPS G-N5-TIME: open.
