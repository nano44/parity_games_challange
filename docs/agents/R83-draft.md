# Draft RESULTS R83 (Lead, 2026-10-29 05:45Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C92 (Lead reviewed 05:50Z by date -u: R82 now landed, reference updated) (rev. 06:24Z by date -u: C92 N-1, N-2; N-3 not applied)

### R83 [refereed-only] N5 on EVERY game, inside one phase: at an in-phase S4a transition t → t + 1, a change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u) of Odd's best reply at an Odd vertex u with (i) u on no honest cycle at t and at t + 1, (ii) y2's honest t-play not through u, and (iii) Ξ_t(y1) ≠ Ξ_t(y2) strictly raises Ξ at u itself, Ξ_{t+1}(u) ▷ Ξ_t(u) (Lemma GATE-RISE: the strict form, in Ξ and for every Odd u, of RESULTS R61 (e) Lemma ALT, proved without R61's conditionality on R56 and R58), so on a run S (a maximal stretch of states of one phase with no fallback between them) G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)) over the Odd vertices u of out-degree ≥ 2, G(S) the σ̄-changing transitions of S, XR_S(u) the transitions of S changing Ξ(u), and TIE_S(u), CYC_S(u), THRU_S(u) the σ̄(u)-changes of S at which (iii) fails, (i) fails, and (i) holds but (ii) fails (its Count); with E_2 the Even vertices of out-degree ≥ 2 and, at a state b of S, X_b the least set of Even vertices containing E_2 and every Even vertex on the W-play or honest play at b of one of its members, V^W_b (V^H_b) the vertices on the W-plays (honest plays) at b of the members of X_b (every Even vertex of V^W_b ∪ V^H_b is in X_b, and V^W_b (V^H_b) is closed under the W-successor (honest successor) at b), RO_b the Odd vertices on those honest plays, CW_b (CH_b) the W-cycles (honest cycles) at b on which those W-plays (honest plays) end, T_W, T_H their vertices and T := T_W ∪ T_H: if states [a, b] of S are REL-ADMISSIBLE (σ̄_t(u) = σ̄_b(u) for every u ∈ RO_b and t ∈ [a, b], and every cycle of CW_b (CH_b) a W-cycle (honest cycle) at every t ∈ [a, b]; σ̄ may move at Odd vertices outside RO_b, and other cycles may come and go), (H4′_rel) the depth recursion on V^W_b and V^H_b (dW := 0 on T_W, dH := 0 on T_H, through τ (W) or σ̄_b (honest) at Odd vertices and σ_b at Even vertices of T, d(v) := dW(v) := dH(v) := 1 + max(dW(σ_b v), dH(σ_b v)) at Even v ∉ T; it stays in its domains) is well founded, and GEN_W (RESULTS R77 (c)'s: for every v, different W-plays from v to the same cycle have different W-valuations) holds, then every v ∈ V^W_b has its W-play at b at every state of [a + dW(v), b] and every v ∈ V^H_b its honest play at b at every state of [a + dH(v), b], so σ_t = σ_b on [a + max_{v ∈ E_2 ∖ T} d(v), b] and b − a ≤ max_{v ∈ E_2 ∖ T} d(v) ≤ |Even ∖ T| ≤ n − 1 (Theorem STATIC-DEPTH-REL; its proof uses W-MONO and Ξ-SUCC at in-phase S4a transitions at which λ_W may change, a proof step signed by both referees for this entry: λ_W is not used); and a run S cut from its end into SEG(S) maximal REL-admissible segments [a_i, b_i] has |S| = Σ_i (b_i − a_i) + SEG(S) − 1 ≤ SEG(S)·n − 1 transitions if (H4′_rel) and GEN_W hold at every segment end b_i, each cut a_i − 1 → a_i (i ≥ 2) being a transition at which σ̄ changes at a vertex of RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears, so SEG(S) − 1 ≤ G(S) + CF(S), CF(S) the transitions of S at which a W-cycle or an honest cycle appears (Corollary REL-SPLIT) (2026-10-29) — structural lemmas for N5 and a REDUCTION of a run's length to its segment count SEG (SEG is not bounded here; CONJECTURE SEG-RUN, SEG = O(n), is OPEN, and with REL-SPLIT it would give O(n²) transitions per run on runs where (H4′_rel) and GEN_W hold at every segment end, not O(n); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C92.md, checker PENDING)
- Object (L-SI successor 21, Opus 5.5; frozen, unchanged during review): packet P-N5-REL, docs/si/P-N5-REL-box25.md, sha1
  f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb (l-si freeze 07f19760, 2026-10-29T04:13:22Z; quote base b28123a58; 17 quotes,
  experiments/si/rund/quotecheck.py "quotes=17 bad=0", pinned with the sha1 in experiments/si/check.sh; both referees measured the pin),
  Lemma GATE-RISE with its Count, Theorem STATIC-DEPTH-REL and Corollary REL-SPLIT. SELF-CONTAINED: the packet's §2 proves STATIC-DEPTH-REL
  in full and does not use P-N5-SDPRIME's Theorem STATIC-DEPTH′ (packet l. 8-9). Working note with data docs/si/N5-GRUN-box25.md (l-si
  3433460b). The referees' notes are collected by the lane in docs/si/P-N5-REL-fixes-box25.md (l-si 843cf5b5, sha1
  16a74626d77dddc088a573005481360d6ab2b699, L-SI successor 21: F1-F9 for REL-N1, REL-N2 = N-REL-6, REL-N3 = N-REL-4, REL-N5 = N-REL-1,
  REL-N4 ~ N-REL-7, N-REL-2, N-REL-3, N-REL-5, N-REL-8; 12 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=12 bad=0",
  pinned in experiments/si/check.sh with a shifted-line control); on trunk; repairs only, "This file changes NO signed statement" (fixes
  l. 3-4): F1 cites RESULTS R61 (e) Lemma ALT for GATE-RISE (REL-N1); F2 replaces the packet's citation of W-MONO and Ξ-SUCC (as RESULTS R77
  (c)'s landed steps "on in-phase S4a transitions") by a proof step signed by both referees, item (a) below (REL-N2 = N-REL-6); F3 renames
  the packet §2's Q (the Even vertices of out-degree ≥ 2) to E_2, the fleet's Q being the Odd vertices of out-degree ≥ 2 (REL-N3 =
  N-REL-4); F4 makes the (SW) quote strictly verbatim (REL-N5 = N-REL-1); F6 rewords GATE-RISE's step 3 (N-REL-2); F8 corrects the scope of
  the not-signed Remark (N-REL-5); F5, F7, F9 are records and change no statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; state t = (σ_t, τ); phases as in RESULTS R80's setting
  (λ and τ constant). A RUN S: a maximal stretch of states of one phase with no fallback between them; its transitions are in-phase S4a
  steps (λ_W, the W-frame's cycle-node map, need not be constant on S). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t at Even
  vertices, σ̄_t at Odd ones); W_t(v): that of v's (σ_t, τ)-play; ▷, ⊵ the S1 order, TOTAL on valuations (p′ injective, distinct sets have
  distinct signed weights); a valuation is a function of the play; u ⊕ x: the valuation of the play u followed by a play of valuation x
  (RESULTS R17 (a) (V1)). A W-cycle (honest cycle) at t: a cycle of the successor map v ↦ σ_t(v) / τ(v) (v ↦ σ_t(v) / σ̄_t(v)), as a vertex
  sequence up to rotation; a vertex on such a cycle has that cycle as its play. For a run S: G(S) := the transitions of S with σ̄_t ≠
  σ̄_{t+1}; CH_S(u) := the σ̄(u)-changes of S; XR_S(u) := the transitions of S at which Ξ(u) changes; CF(S) := the transitions of S at which
  a W-cycle or an honest cycle appears. E_2 := the Even vertices of out-degree ≥ 2 (F3). X_b, V^W_b, V^H_b, RO_b, CW_b, CH_b, T_W, T_H, T at a
  state b of S as in the title. Depths: dW on V^W_b, dH on V^H_b: dW(v) := 0 for v ∈ T_W; dH(v) := 0 for v ∈ T_H; Odd v: dW(v) := dW(τ v)
  (v ∉ T_W), dH(v) := dH(σ̄_b v) (v ∉ T_H); Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T:
  dW(v) := dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v); max ∅ := 0. (H4′_rel): this recursion is well founded. n: the number of
  vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation, order, Ξσ
  against σ̄), S2 (Iσ), S4a (arena {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R15 (a) Lemma A and (d); RESULTS R17
  (a) (V1), (V2); RESULTS R57 (a) premise (VJ); RESULTS R18 (d) Lemma S (a) on S4a's arena, the standing premise P2 as listed in RESULTS R69;
  (SW) "every Even switch of N5 is to an edge of Iσ", as listed among RESULTS R72's landed premises; RESULTS R77 (c) (GEN_W's definition;
  its proof steps W-MONO and Ξ-SUCC, landed under R77's (H1), which includes λ_W constancy, are replaced here by item (a)); RESULTS R80 (a)
  EVERY-SWITCH and R80's phase setting. RESULTS R61 (e) Lemma ALT (landed, CONDITIONAL on RESULTS R56 and R58) is cited for comparison only
  (item (b)); no item uses it as a premise. No item uses P-N5-SDPRIME or STATIC-DEPTH′.
  (a) Facts used as proof steps, signed by both referees for this entry (REL-N2 = N-REL-6, F2): (W-MONO) W_{t+1} ⊵ W_t at every in-phase S4a
      transition (P2; RESULTS R18 (d) Lemma S (a), at one S4a step); (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing along in-phase S4a transitions
      (RESULTS R15 (a), (d) and (SW)); λ_W is not used. (W-MONO: σ_t uses only arena edges, and σ_{t+1} is pointwise W-optimal over the
      strategies using arena edges. Ξ-SUCC: if v keeps, Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by R15 (a), (d); if v switches, (SW) gives
      Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v) and R15 (a), (d) give Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v).) This extends RESULTS R77's landed facts, which are
      stated under λ_W constancy, to the transitions at which λ_W changes; STATIC-DEPTH-REL needs it on runs, which do not fix λ_W.
      REFEREE §C (a343d6b4): "REL-N2 = N-REL-6 (W-MONO / Ξ-SUCC at λ_W changes; the same signed proof step as SDPRIME's §C)." REFEREE-2 §C
      (b6811cf1): "REL-N2 (W-MONO / Ξ-SUCC beyond R77 (H1)) = N-REL-6. The same signed proof step as SDPRIME §C.3. Identical." REFEREE-2's
      N-REL-6: "Both facts hold at every in-phase S4a transition: P2 at one step, and R15 (a), (d) with (SW)." The (M2κ) citation R77 gives
      for Ξ-SUCC is replaced by R15 (a), (d) (F2).
  (b) Lemma GATE-RISE (§1, with F1 and F6): let t → t + 1 be an in-phase S4a transition and u an Odd vertex with σ̄_t(u) = y1 ≠ y2 =
      σ̄_{t+1}(u), such that (i) u is on no honest cycle at t and at t + 1, (ii) y2's honest t-play does not pass through u, (iii) Ξ_t(y1) ≠
      Ξ_t(y2). Then Ξ_{t+1}(u) ▷ Ξ_t(u). (Step 1, (i) and (V1): Ξ_t(u) = u ⊕ Ξ_t(y1), Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2). Step 2: τ′ := σ̄_t with u's
      choice changed to y2; by (ii) y2's (σ_t, σ̄_t)-play is also its (σ_t, τ′)-play and u's (σ_t, τ′)-play is u followed by it, so
      V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2), and (VJ) gives u ⊕ Ξ_t(y1) ⊴ u ⊕ Ξ_t(y2). Step 3 (F6): "x ↦ u ⊕ x is strictly monotone on the values of
      plays avoiding u: monotone by (V2); for two such x with the same cycle node c it adds u to both path sets or to neither and 1 to both
      lengths, so the comparison is unchanged and x is recovered; for different cycle nodes u ⊕ keeps each cycle node, so the order (decided
      by the cycle nodes) is kept"; Ξ_t(y1) and Ξ_t(y2) are values of plays avoiding u, by (i) and (ii); with (iii) and totality, Ξ_t(y1) ◁
      Ξ_t(y2). Step 4: R15 (a), (d) give Ξ_{t+1}(y2) ⊵ Ξ_t(y2), so Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) ⊵ u ⊕ Ξ_t(y2) ▷ u ⊕ Ξ_t(y1) = Ξ_t(u).) F1
      (REL-N1): "GATE-RISE is the strict form, in Ξ and for every Odd u (not only u ∈ Q_c), of RESULTS R61 (e) Lemma ALT; its proof here uses
      only R57 (a), R17 (a) and R15 (a), (d), so it does not inherit R61's conditionality on R56 and R58." (R61 (e), landed: a clean change at
      q ∈ Q_c, q ≠ c, "has κ_{t+1}(q) ≥ κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t)".) REFEREE
      (report §1): "GATE-RISE is the strict form of RESULTS R61 (e) Lemma ALT"; REFEREE-2 §C C.3: "ACCEPTED, MISSED by me", after reading
      R61 (e)'s landed text.
  (c) Its Count (§1): for a run S and an Odd u, every σ̄(u)-change of S is clean ((i)-(iii) hold), TIE ((iii) fails), CYC ((i) fails) or
      THRU ((i) holds, (ii) fails) (the kinds may overlap; the sum still bounds), and each clean change is a transition at which Ξ(u) changes;
      so CH_S(u) ≤ XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u), and, summing over the Odd vertices of out-degree ≥ 2 (every σ̄-changing
      transition changes σ̄ at one of them), G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)).
  (d) Theorem STATIC-DEPTH-REL (§2, with F3), the domain-closure sentences of its definitions included (REFEREE: "SIGNED, including the
      domain-closure sentences of the definitions"; REFEREE-2: "SIGN (RCLOSE / RDOM checked)"). Definitions at a state b of a run S as in the
      Setting; every Even vertex of V^W_b ∪ V^H_b is in X_b, and V^W_b (V^H_b) is closed under the W-successor (honest successor) at b; the
      recursion stays in its domains: τ(v) (Odd v) and σ_b(v) (Even v) of v ∈ V^W_b are on the same W-play, so in V^W_b; σ̄_b(v), σ_b(v) of
      v ∈ V^H_b likewise in V^H_b; for Even v ∉ T, v ∈ X_b and y = σ_b(v) lies on both of v's b-plays, so y ∈ V^W_b ∩ V^H_b. [a, b] ⊆ S is
      REL-ADMISSIBLE if σ̄_t(u) = σ̄_b(u) for every u ∈ RO_b and t ∈ [a, b], and every cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every
      t ∈ [a, b]. Statement: let [a, b] ⊆ S be REL-admissible, with (H4′_rel) and GEN_W. Then every v ∈ V^W_b has its W-play at b at every
      t ∈ [a + dW(v), b], and every v ∈ V^H_b its honest play at b at every t ∈ [a + dH(v), b]; σ_t = σ_b for t ∈ [a + max_{v ∈ E_2 ∖ T} d(v),
      b]; and b − a ≤ max_{v ∈ E_2 ∖ T} d(v) ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅ when E_2 ≠ ∅; if E_2 = ∅ there is no in-phase S4a step and b = a).
      (Induction along the well-founded recursion: item 1, a cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every t, so its vertices are
      settled from a, and an Even v ∈ T has σ_t(v) = σ_b(v); item 2, Odd v ∈ V^W_b ∖ T_W settles through τ(v), and Odd v ∈ V^H_b ∖ T_H lies in
      RO_b, where REL-admissibility fixes σ̄(v) on [a, b], and settles through σ̄_b(v), the only use of σ̄; item 3, Even vertices of the other
      frame's T settle through σ_b(v); item 4 at Even v ∉ T (so v ∈ X_b): (A) y = σ_b(v) is kept or improving at v from a + max(dW(y), dH(y))
      on, by (SW), Ξ-SUCC and y's H-settledness; (B) W_{t+1}(v) = W_b(v) by P2's pointwise optimality and W-MONO; (C) v's W-cycle at b is in
      CW_b, so v's W-play at t + 1 ends in it, and GEN_W makes it the play at b, whence σ_{t+1}(v) = y and v's honest play at t + 1 is its
      honest play at b; item 5, from a + max_{E_2 ∖ T} d on σ_t = σ_b on E_2 (items 1, 4), the other Even vertices have out-degree 1, and a
      further transition would contradict R80 (a); a longest recursion path from v ∈ E_2 ∖ T visits distinct Even vertices outside T.)
  (e) Corollary REL-SPLIT (§3, with F3), a REDUCTION. Cut a run S = [s, e] from its end: b_k := e; a_k := the least state of [s, b_k] with
      [a_k, b_k] REL-admissible (with respect to b_k's sets); then b_{k−1} := a_k − 1, and so on down to s; SEG(S) := k. Claim: if (H4′_rel)
      and GEN_W hold at every b_i, then |S| = e − s = Σ_i (b_i − a_i) + SEG − 1 ≤ SEG·n − 1; every cut a_i − 1 → a_i (i ≥ 2) is a transition at
      which σ̄ changes at a vertex of RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears; hence SEG − 1 ≤ G(S) + CF(S). (REL-admissibility of
      [x, b_i] for b_i's sets is monotone in x, so a_i is well defined; STATIC-DEPTH-REL on each segment gives b_i − a_i ≤ n − 1; for i ≥ 2,
      [a_i − 1, b_i] is not REL-admissible though [a_i, b_i] is, so σ̄_{a_i − 1}(u) ≠ σ̄_{b_i}(u) = σ̄_{a_i}(u) for some u ∈ RO_{b_i}, or a cycle of
      CW_{b_i} ∪ CH_{b_i}, a cycle at a_i, is not one at a_i − 1; the cuts are distinct transitions.) REFEREE: "SIGNED (a REDUCTION: SEG
      unbounded)"; REFEREE-2: "SIGN (a REDUCTION)".
- Not signed: the packet's §4 (as the packet says): the DATA, the reader-proofness READING ("a reader is on no play of another vertex, an
  anchor's plays are its own loop") and CONJECTURE SEG-RUN (SEG(S) = O(n), OPEN). The packet's §2 Remark (not in its to-sign table), as
  written "STATIC-DEPTH-REL contains STATIC-DEPTH′ (P-N5-SDPRIME) and, through it, RESULTS R77 (c)": its corrected scope (N-REL-5 = F8;
  REFEREE ACCEPTED it in its §C, correcting its own "true as stated") is "STATIC-DEPTH-REL contains STATIC-DEPTH′'s length bound and its
  per-vertex settling on V^W_b ∪ V^H_b; it does not give STATIC-DEPTH′'s settling at other vertices" (e.g. a reader). STATIC-DEPTH′ is
  P-N5-SDPRIME's theorem (RESULTS R82 (landed)); no signed item of this entry uses it. GATE-RISE's remark that (i) at t + 1 can
  be weakened to u ≠ λ(u) (REL-N1; F1: "remark, not signed"; REFEREE §1: "Not needed for any signed statement", 4 data cases, all rising;
  REFEREE-2 §C C.3: "The weakening holds", 1 + 4 own cases); (i) at t stays (REFEREE-2's cyc control: 8 of 23 CYC changes without a rise);
  REFEREE-2's further data on a weakening at t ("a data point, not a checked statement. Not proposed for signature"). The packet's wording
  as frozen, repaired by the fixes and not false: GATE-RISE without the R61 (e) citation (F1); W-MONO and Ξ-SUCC cited as R77 (c)'s landed
  steps, whose scope (H1) includes λ_W constancy (F2); Q for the Even vertices of out-degree ≥ 2 (F3; "The statement is unambiguous as
  written, since §2 defines it", REFEREE-2 N-REL-4); the (SW) quote with "…" where the source has only a line break (F4; content
  identical); step 3's injectivity sentence without "u-free" (F6; both values it is applied to are u-free).
- Honest limits: (i) REL-SPLIT is a REDUCTION, not a bound: SEG is not bounded here, nor are the runs of a phase or the phases. CONJECTURE
  SEG-RUN (SEG = O(n)) is OPEN; its DATA bound is SEG ≤ 1.00n over all starts (F5: max SEG / n 0.79 on alt_all with default S3 and with
  pinned starts, REFEREE 0.83 on lib41 and lib1140 (run_m_n24, SEG 20 at n 24), REFEREE-2 0.95 (lib41 lev_l_n20, random start), the lane's
  climb 1.00 (grun/out/sg_2, SEG 29 at n 29)). READING (Lead): with SEG-RUN, REL-SPLIT gives |S| ≤ SEG·n − 1 = O(n²) transitions per run, not
  O(n), and only on runs where (H4′_rel) and GEN_W hold at every segment end. (ii) G is not intrinsic (the lane's DATA and READING,
  N5-GRUN-box25 §3, not refereed as a claim): Odd readers (no predecessors) lift G on runfam_K10 from 9 to 91 at n 74 (grun/out/rdr_K10,
  .pg sha1 a7ac4830…) with the run fixed (99 transitions), and Even anchors put the readers into RESULTS R81's K with G^K 91 at n 99
  (grun/out/anc_K10, .pg sha1 13833299…); SEG stays 9 on all three. Reproduced: REFEREE on runfam_K10, rdr_K10, anc_K10 (G 9 / 91 / 91 inside
  the run, SEG 9; "So the readers inflate G tenfold and leave SEG unchanged"); REFEREE-2 on rdr_K10, anc_K10 (|S| = 99, G = 91, SEG = 9).
  READING (Lead): GATE-RISE's Count reduces G(S) to the gates' XR_S plus exception counts, and XR per vertex is not bounded (RESULTS R80:
  XR-LIN DEAD); REL-SPLIT's clause SEG − 1 ≤ G(S) + CF(S) bounds SEG by a count that readers inflate, so it is not a route to SEG-RUN; SEG
  itself was reader-proof in these instances (DATA). (iii) GEN_W and (H4′_rel) are hypotheses. Where GEN_W's used form fails the
  conclusions still held (REFEREE 34 / 52 / 76 intervals; REFEREE-2 132 + 164 + 1). (H4′_rel) is not vacuous: it fails at 45 of 1,908
  segment ends (lane, alt_all, default starts; 49 with pinned starts) and at 8 + 27 REL-admissible intervals (REFEREE-2); REFEREE: REL-SPLIT's
  hypotheses hold on 3,029 of 3,286, 4,279 of 4,353 and 11,229 of 11,445 runs; the other runs are not bounded by REL-SPLIT. (iv) The
  hypotheses carry weight in data: σ̄ constant on RO_b carries the length bound (REFEREE MUT4: SDV 26,383, SIG 1,274, LEN 283, SPLIT 3;
  REFEREE-2 nosbar: 212,050, including RLEN 1,450 and RSIG 1,450); GATE-RISE's (iii) (REFEREE MUT3 128 of 129 ties without a rise; REFEREE-2
  tie 167 of 168) and (i) (REFEREE-2 cyc 8 of 23) are needed; the depth is exact (REFEREE MUT1 SDV 15,442; REFEREE-2 dm1 18,837); X_b's
  closure is structurally needed (REFEREE-2 qonly: RDOM 246, RCLOSE 14,331; REFEREE's MUT5 did not bite because its depth routine is not
  restricted to the domains, REFEREE §C: "ACCEPTED"). Thin spot (N-REL-3 = F7): (ii) is not shown necessary in data (REFEREE MUT2: 13 THRU
  changes, all rising; REFEREE-2: 239; lane 73 + 176 + 56); it is used in step 2 and stays a hypothesis. (v) What the freedom buys (N-REL-8 =
  F9): REL-admissible intervals on which σ̄ moves at an Odd vertex off RO_b: REFEREE 789 + 495 + 1,122 + 175 (readers: 175 of 273);
  REFEREE-2 4,094 + 3,281 + 539 + 2,947 + 192 (lane instances: 2,947 of 3,012; REFEREE-2's logs carry the strict counter REL_sbar_moves_off_RO with these values; its wider REL_beyond_SDPRIME is equal in every log, and rel_check.py's _nonrel_cycle_breaks never fires). (vi) Nothing here bounds N5's running time.
- Data (DATA, not proof): the packet's §4 (lane, experiments/si/grun/gaterise.py and relseg.py; one engine, n5x): GATE-RISE 2,114 clean
  changes on alt_all (default S3 starts; TIE / CYC / THRU 75 / 8 / 73), 3,752 with pinned starts (82 / 10 / 176), 1,889 on lib41 (76 / 10 /
  56), 0 failures (grun/gaterise_alt.txt, _alt_start.txt, _lib41.txt); MUT (a strict rise of Ξ(y2) demanded instead) fails 1,892 times (packet
  §4; N5-GRUN-box25 §2); REL 1,908 segments on alt_all (2,890 with pinned starts), 0 violations, (H4′_rel) fails at 45 (49) ends, max SEG 26
  (62, gate_K64_n581), longest segment 67 (55) (grun/relseg_alt.txt, _alt_start.txt); MUT (d − 1) 994 (packet §4; N5-GRUN-box25 §4); max SEG /
  n 0.79 in both start sets (F5), ≤ 1.00n after climbs. REFEREE (successor 17; own docs/referee/scratch/rel_probe.py (sha1 4b35aabd…) on its
  engine rl_engine; lane code not run; 0 failures in every MUT=0 run; logs scratch/rel_logs/): alt_all (413 games, n ≤ 600, given start else
  S3) 413 runs (3,286 fallback-free runs S), GATE-RISE clean / TIE / CYC / THRU 3,700 / 82 / 10 / 118, 5,385 REL intervals (789 with σ̄ moving
  off RO_b), REL-SPLIT hypotheses on 3,029 / 3,286 runs, 1,951 cuts checked, max SEG / n 0.79; lib41 (n ≤ 48; given + S3 + 1 random) 727
  (4,353), 2,438 / 129 / 15 / 13, 5,814 (495), 4,279 / 4,353, 2,210, 0.83; lib1140 (n ≤ 40; given + S3 + 1 random; two halves) 1,857 (11,445),
  4,063 / 169 / 68 / 91, 8,741 (1,122), 11,229 / 11,445, 3,077, 0.83 (n ≥ 2; the only SEG = n case is the one-vertex strfam_S1_n1); readers
  (rdr_K10, anc_K10, runfam_K10; given starts) 3 (6), 445 / 22 / 0 / 0, 273 (175), 6 / 6, 24, 0.18; per-vertex settling, σ_t = σ_b, the length
  and the cap, the Count, REL-SPLIT's sum, cuts and SEG − 1 ≤ G + CF: 0 failures. REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-REL/rel_check.py (reusing its R2-N5-SDPRIME/sdprime_check.py) and seg_case.py; lane tools not run, lane instance files
  copied as inputs; every non-mutation run 0 violations; REL-admissible intervals up to length 60, RELCAP 60): alt_all (413 runs; given start
  else S3) GATE-RISE 3,713 / 82 / 10 / 125, 36,502 REL-admissible intervals (GEN_W used 36,362), Remark checks 32,400, runs S 920 (874 with
  the hypotheses), 2,874 segments; lib41_noref × 3 (1,230 runs) 3,751 / 168 / 23 / 109, 53,652 (53,461), 50,344, 1,612 (1,536) / 4,671; named
  (8 runs) 390 / 0 / 1 / 3, 1,173, 634, 48 (45) / 198; lane instances grun/out (28 runs) 870 / 71 / 9 / 0, 3,012, 65, 29 (29) / 407; random kO
  n 8-20 and k2 n 6-16 (18,000 runs) 325 / 55 / 70 / 2, 2,325 (2,324), 2,132, 2,518 (2,517) / 3,047; max SEG / n 0.792 on alt_all
  (so_sor5_n24), 0.95 on lib41 with a random start (lev_l_n20), 1.00 on sg_2; |S| / (SEG·n) ≤ 0.917 ("The bound is never reached"); longest
  REL interval 55 transitions (x32_rand64), sharp in 395 + 442 intervals; Remark (RREM, RREM_d): 0 on 85,575 checks. Run counts differ by
  definition: REFEREE's 3,286 counts every run, those of 0 transitions included (rel_probe.py l. 44-53), REFEREE-2's 920 only runs with ≥ 1
  transition (rel_check.py l. 46), the lane's 921 (pinned starts) likewise (grun/relseg.py l. 48); READING (Lead) of the three tools' code, no
  report states the cause; the remaining difference 920 / 921 is not determined. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-REL.md (report 69b12910, sha1 8ae211bd760e7a7347cdc979e22a674c4ddd5d01 there; §C a343d6b4;
  successor 17): Lemma GATE-RISE SIGNED; its Count SIGNED; Theorem STATIC-DEPTH-REL SIGNED, including the domain-closure sentences of the
  definitions; Corollary REL-SPLIT SIGNED (a REDUCTION: SEG unbounded); the Remark not to sign; quotes 17 in their ranges (own
  scratch/flip_quotes.py, QUOTES 17 FAILED 0, "…" read as a separator), 16/17 strictly verbatim (the (SW) "…"); notes REL-N1..N5; no gap.
  REFEREE-2 docs/referee-2/R2-N5-REL.md (report eb5aa2b5, sha1 b75ae5caa74662f491f2fe80164e77ec16e32e4a there; §C b6811cf1; successor 19):
  Lemma GATE-RISE SIGN (step 3's injectivity used on u-free values only, N-REL-2); its Count SIGN; Theorem STATIC-DEPTH-REL SIGN; Corollary
  REL-SPLIT SIGN (a REDUCTION); the Remark not signed (correct for the length bound and for settling on V^W_b ∪ V^H_b, N-REL-5); quotes
  16/17 verbatim, the (SW) "…" (N-REL-1), SHIFT=1 control 0/17; notes N-REL-1..8; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/
  file on REL (names matching "N5-REL" at 04:53Z: 0 on its tree, 2 on origin/claude/referee-2, 0 on trunk; names only) and ran no lane code
  (only the data files grun/out/rdr_K10, anc_K10 copied by git show at 07f19760); REFEREE-2 opened no REL file under docs/referee/ before
  pushing eb5aa2b5 (names-only count 0 at 04:40:50Z and at 04:54:13Z) and ran no lane tool; its one declared overlap is REFEREE's SDPRIME
  report, read for its SDPRIME §C, on the W-MONO / Ξ-SUCC point it had found itself first (R2-N5-SDPRIME §1); REFEREE's §C: "No effect on any
  verdict". §C (both): verdicts identical (GATE-RISE, its Count, STATIC-DEPTH-REL, REL-SPLIT); joint gap map EMPTY; REL-N1 ACCEPTED by
  REFEREE-2 ("MISSED by me") and checked against R61 (e)'s landed text; REL-N2 = N-REL-6, REL-N3 = N-REL-4, REL-N5 = N-REL-1 identical;
  REL-N4 ~ N-REL-7 (start sets; no conflict); N-REL-2 ACCEPTED as wording, N-REL-3 = REFEREE's MUT2, N-REL-5 ACCEPTED by REFEREE (the Remark),
  REFEREE-2's cyc and qonly controls ACCEPTED as stronger evidence; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase and a reduction of a run's length to its
  segment count SEG; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
