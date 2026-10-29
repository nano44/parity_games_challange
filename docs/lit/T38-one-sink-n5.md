# T38: N5 on 1-sink games — what the landed results become, and what is still open (L-LIT, 2026-10-29)

Asked by the Lead at 11:47Z (date -u). Repo sources only. One line per claim, each with a status label and a source.

**Labels.**
- PROVED (Rxx) = landed.
- PROVED (lane, SHA).
- PROVED (L-LIT, unrefereed) = elementary, proved here.
- DATA, READING, OPEN as in D18 / L40.

**Sources.**
- [F] = Friedmann, arXiv 1106.0778 v2, §5 p.8: the 1-sink definition, Lemma 5.1. Opened, notebook.
- COMPOSE = L-SI's Theorem COMPOSE / Corollary COMPOSE-RUN, claude/l-si docs/si/N5-CHG-box28.md §9, f372bc6b (lane).
- MΦ = Lemma MATCH-Φ Corollary, docs/lit/P-N5-MPGS.md (A), a23179b0, under review.
- Box 16 = claude/l-comp experiments/friedmann-hn/README.md (aeff7b04 last change).

**Definition used** ([F] §5).
- (G, ι) is a 1-sink game if:
  - (1) there is a node v* with a self-loop and Ω(v*) = 1, reachable from all nodes, and no other node w with Ω(w) ≤ Ω(v*);
  - (2) Sink Seeking: for every Even strategy σ with Ξ_ι ⊴ Ξ_σ, the cycle component of Ξ_σ(w) is v* for every w.
- Lemma 5.1: under (1), (G, ι) is 1-sink iff Odd wins everywhere and every cycle component of Ξ_ι is v*.
- DFH (arXiv 1911.01074 §2.1 p.4) and H_n in box 16 use the same notion.

## (a) λ, λ^U and the collapse of COMPOSE-RUN
1. **λ along an execution.**
   - On a 1-sink game, every N5 execution whose start satisfies Ξ_{σ_0} ⊵ Ξ_ι has λ_t ≡ v* at every state, so the execution is ONE
     λ-run.
   - Proof: R15 (a) (MON) gives Ξ_t ⊵ Ξ_{σ_0} ⊵ Ξ_ι for all t; then apply Sink Seeking.
   - Status: PROVED (L-LIT, unrefereed; one line from R15 (a) and [F] §5 (2)).
   - In particular this holds from [F]'s own start ι (box 16's start F).
2. **λ from other starts.** From a start not dominating ι, λ may differ at first. It changes at most n(n − 1) times (R47 Lemma Φ);
   after it reaches v* everywhere it stays.
   - Status: PROVED (R47 (a)) for the count. The "stays" part is PROVED (L-LIT, unrefereed): a cycle node only rises (R47), and above
     v* lie only Even-won cycle nodes, which σ_t cannot reach because Odd wins everywhere ([F] Lemma 5.1).
3. **Box 16 data.** "Every run has fallbacks f = 0 and λ_Ξ changes = 0" on H_n from starts F and S3 (box 16 §2). DATA.
4. **λ^U is NOT constant on 1-sink games.**
   - Against τ, Even's best reply τ̄ may close Even-won cycles; [F]'s simple / stubborn cycles are Even-won when closed ([F] §6.1).
   - Box 16, start F: n τ-changes, one gate per iteration (e_i : d1_i → h_i), "λ_W ch" 6-19 per run.
   - Status: READING (from [F] §6.1 and box 16 DATA). The count of λ^U-runs is ≤ n(n − 1) + 1 (R47 (a), Odd's dual cycle nodes only
     fall): PROVED (R47).
5. **ℓ = |P| on 1-sink games.**
   - With c = v*, every other vertex has p′ > p′(v*) (rank(v*) = 0), so P is the whole prefix of the play before v*. The prefix of a
     lasso is simple, so ℓ = |P|.
   - Hence Ξ(v) changes iff P(Ξ v) changes: RISE = PCH. LEN-MONO's factor n disappears on the Even side.
   - Status: PROVED (L-LIT, unrefereed; SPEC S1's definition of P and ℓ). [F] §5 p.8 states the same: "the path-length component equals
     the cardinality of the path component, because all nodes except the sink node are more relevant than the cycle node itself".
6. **Collapse of COMPOSE-RUN (Even side).**
   - On a 1-sink execution with λ ≡ v* (item 1), every Even switch is counted by SW-RETURN on the whole execution:
     Even switches ≤ Σ_{(v,c) Even edge} (1 + RISE(c)) = Σ (1 + PCH(c)) ≤ m_E·(P* + 1).
   - Here P* is the most P-changes of one vertex over the WHOLE execution.
   - With MΦ: P* ≤ (n²/2)(NM* + 1) + NM*, NM* the most carries of one vertex over the execution.
   - Status: PROVED (as a composition: COMPOSE's SW-RETURN, lane f372bc6b; item 5, L-LIT; MΦ under review).
7. **Collapse of COMPOSE-RUN (whole run).**
   - T ≤ (Even switches) + (transitions with σ unchanged, i.e. τ-only steps).
   - The τ-only steps are bounded exactly as in COMPOSE (b): ≤ n(n − 1) λ^U-changes plus m_O·n·Σ_{λ^U-runs}(P*^U + 1).
   - So T ≤ m_E(P* + 1) + n(n − 1) + m_O·n·(n(n − 1) + 1)(P*^U + 1).
   - Status: PROVED (composition, as item 6).
   - Note: the Odd side does NOT collapse (item 4). P*^U is still governed by NM*^U (MΦ on G^d); there the cycle node of U need not be
     the lowest rank, so the factor n stays.
8. **Answer to (a).** Yes on the Even side: one λ-run, and T's Even part is m_E·(P* + 1) with P* governed by NM* alone (no factor n,
   no λ-run sum). No on the Odd side: λ^U varies, and the τ-side term keeps its λ^U-run sum. READING, from items 1-7.

## (b) Which landed results specialize
9. **R47 Lemma Φ.** It specializes to "λ constant" (item 1). Its Corollary Φ-1O (≤ deg(o) − 1 τ-changes, n(n − 1) + deg(o) phases) needs
   one Odd choice vertex. [F]'s G_n and H_n have n Odd choice vertices (the e_i), so Φ-1O does NOT apply to them. PROVED (R47) / READING.
10. **R48** (in-phase fallbacks ≤ 1 + (n − 2)(2n − 1)): one-Odd-choice only. Same remark as item 9. PROVED (R48) for its class; not
    applicable to G_n / H_n.
11. **R54 (mirror symmetry; 𝒞^1E).** Mirror-symmetric on every game. Nothing 1-sink-specific. The mirror of a 1-sink game is Even-won
    everywhere, with the sink as Even's lowest even cycle. Box 16's "dual" variant shows N5's counts are identical there (6n + 4 from
    S3). PROVED (R54) / DATA (box 16 §5).
12. **R81 FB-C^K** (f ≤ n_K·|K-configurations of fallback sources| per phase): holds as on every game. No 1-sink sharpening is proved.
    DATA: f = 0 on every H_n run (box 16, 1,612 runs + variants). PROVED (R81) / DATA.
13. **R83 (GATE-RISE, STATIC-DEPTH-REL, REL-SPLIT).**
    - Holds as on every game.
    - On a 1-sink execution with λ ≡ v*, the HONEST cycles of every state are v*'s self-loop alone. So CF (cycle appearances) counts
      only W-cycle appearances, and the honest-frame cycle set CH_b is {v*} and constant.
    - Status: PROVED (R83) + READING (from item 1).
14. **R84 TOP-SHAPE.**
    - Signed per phase.
    - With c = v* (rank 0), P_t is the whole prefix and top_t is the highest-ranked vertex on v's honest play.
    - The referee strengthening N-TS-1 (TOP-SHAPE holds at every transition with λ(v) unchanged) is a REMARK, not signed (RESULTS
      R84 l. 4997). With it, top changes ≤ n − 1 per vertex over the WHOLE 1-sink execution.
    - Status: PROVED (R84) per phase; per execution only via the unsigned remark.
15. **GATE-SHUT (P-N5-MPGS (B), under review).**
    - (H1) holds automatically for a gate whenever the cycle node of the exit's τ-play is v*, since v* has the lowest rank.
    - Box 16 / T34 check: from S3 and F on H_n, (H1), (H2) held at 100% of gate-states (n = 3..8), 0 reopenings.
    - Status: READING + DATA (docs/lit/T34-gateshut-check.py, sha1 7c33508b).
16. **R57 1E-POLY, R51 (𝒞^1O polynomial).** These are one-choice subclasses, unrelated to 1-sink. A 1-sink game with one Odd or one
    Even choice vertex is covered by them. PROVED (R51, R57) for those subclasses.

## (c) Bounds on carries on 1-sink games
17. **No landed or lane-proved statement bounds carries (NM*) or P-changes on 1-sink games in general.** OPEN.
    - Search: RESULTS headers for "sink"; docs/si, docs/new, docs/red for "1-sink" / "sink game". Only box 16 (data), ALTLIT §2
      (L-NEW 29, READING) and T34 / T37 (L-LIT, READING) discuss 1-sink games.
18. **H_n (box 16).** N5 is linear: iterations 6n + 4 (S3, exact), 8.06n + 9.4 (F); longest phase ≤ 9n; XR ≤ 24 over 1,612 starts (n ≤ 12).
    - Implied (READING): carries on H_n are O(n) in these runs (P-changes ≤ XR).
    - Status: DATA (box 16 §3-§4), not a theorem.
19. **Why H_n is linear.** τ shuts every gate early (box 16 §2), GATE-SHUT keeps it shut (item 15), and S4a's W-choice sees full bit
    values (docs/lit/T34-friedmann-vs-n5.md §3).
    - CONJECTURE NO-HIDE (T34 §4): no 1-sink family with Friedmann-type gates is super-polynomial for N5 from S3 or F.
    - Status: CONJECTURE (data: box 16 + T34), OPEN.
20. **What a 1-sink counter for N5 must do** (T37 §3).
    - Every gate reopening must break (H1), (H2) or (H3).
    - (H1) needs the exit's τ-play to end in a cycle node above the gate. On a 1-sink game that cycle is a λ^U-cycle of the dual side
      (Even-won under τ̄), possible because λ^U varies (item 4).
    - Status: READING.

## DONE / FINDINGS / NEEDS
- DONE: this note.
- FINDINGS:
  1. On a 1-sink game from any start dominating ι, the whole N5 execution is one λ-run, and ℓ = |P|, so RISE = PCH. COMPOSE-RUN's Even
     part collapses to m_E·(P* + 1), with P* over the whole execution and governed by NM* through MΦ. The Odd part does not collapse:
     λ^U varies, as Friedmann's gates are Even-won cycles under τ̄.
  2. Φ-1O and R48 need one Odd choice and do not reach G_n / H_n.
  3. No statement bounds carries on 1-sink games; H_n is linear in data only. NO-HIDE stays a conjecture.
- NEEDS (Lead; nothing for the owner): if wanted, a two-line packet for items 1, 5, 6. They are elementary, but only L-LIT has checked
  them.
