# REFEREE-2 notebook (independent second referee)
Rule: do not read docs/referee/ or notes/REFEREE.md before my own report on a claim is pushed.

## Resume point (successor 6, Opus 5.5 under D15; 2026-10-25 01:5xZ by date -u)
- Handover check 6a27ab9b (Lead 01:44Z: 5/5, GO). Lead: P-N5-SO NOT re-reviewed (succ. 5's R2-N5-LP §8 stands).
- P-N5-OE (docs/new/P-N5-OE-box32.md sha1 adeccd89, pin 361d18c): report docs/referee-2/R2-N5-OE.md. U-loc, OE, OX (i)-(v) all SIGN;
  notes N-OE-1 (in-particular sentence vs level-⊥ tie move), N-OE-2 (step 3 one-line reason), N-OE-3 (phase-key transfer of FB/J1/CAP-1/TC).
  Tools R2-N5-OE/ (oe_check.py, oe_climb.py, run_all.sh). 0 violations; CAP-1 non-minimiser at λ(o)=o seen (420), never used by OE.
  NEXT: §C after REFEREE's R-N5-OE (do not read it before my report is pushed).
- Oink built in this container (setup_oink.sh).

## HANDOVER (successor 5, session_01VbMVVvPYCY47wY5MbtLG8w, Opus 5.5 under D15; written 2026-10-25 01:23Z by date -u; context ~660k, over the line)
Branch claude/referee-2, merged with trunk at each packet. REFEREE-2 owns no docs/GAPS.md rows. PARKED.

### DONE (every report is docs/referee-2/<name>.md; every verdict labelled "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 1b394dfc | — | Lead 5/5 |
| P-N5-U1 | docs/new/P-N5-U1-box31.md eb90788d @ eee0d8a | 28ddf6fa | 3d68a030 (+ stamp cab4e7da) | U1, WC SIGN; CASC SIGN WITH GAPS (C-1..C-3 accepted); TB, R SIGN WITH GAPS (G-TB-1, G-R-1, G-R-2 closed); N-U1-3 closed via R15 (a) in G_τ |
| P-N5-FB | docs/si/P-N5-FB-box7.md 9ece9994 @ 348393b | 7699593d | eb10cf74 | FB, Corollary, CAP SIGN WITH GAPS (G-FB-1..4); rest SIGN; JUMP-EQ FALSE confirmed; adopted REFEREE's full-minimiser proof (CAP-1) |
| P-N5-U23 | docs/new/P-N5-U23-box31.md ee3e5d1e @ 7666336 | 07b22b07 | 5e24010a | CASC-U2 SIGN; CASC-U3 (ii) SIGN WITH GAPS (G-U23-1 = U3-1); READING note N-U23-2 = R-1 (closure accepted); u2flat_n32: CASC-U2 bound attained |
| P-N5-LP | docs/new/P-N5-LP-box32.md d2c8121a @ bc42f2c | 4949d6c9 | caee2aec | DF NOT SIGNED (FALSE; my df_cex.pg n 5); DF′ SIGN; WAKE SIGN WITH GAPS (G-LP-1); HI Consequence unproved (G-LP-2); rest SIGN |
| P-N5-SO | docs/new/P-N5-SO-box32.md deb5ee44 @ 1ef02bb | ba67f410 (R2-N5-LP.md §8) | caee2aec (in the same §C) | TH SIGN; SO SIGN WITH GAPS (G-SO-1); XJ SIGN WITH GAPS (N-SO-2 = XJ-1). NOTE: the Lead's 01:10Z message assigned SO to successor 6, but it reached me (01:19Z) after this review was pushed (01:2xZ). The review exists and stands; the Lead decides whether successor 6 redoes it independently |

### IN FLIGHT
None.

### NEEDS
- Lead: route to the lanes' fixes files: DF → DF′ (proof R2-N5-LP §4.3), G-LP-1, G-LP-2, N-LP-1, G-SO-1, N-SO-1..3 (L-NEW);
  G-U23-1 / N-U23-2 (L-NEW); G-FB-1..4 (L-SI). Decide whether P-N5-SO needs a fresh independent second review.

### Things only I know
- Tools (own code; each directory has run_all.sh, logs/, often climb/, and totals.py):
  - R2-N5-U1/u1_check.py: an instrumented VJ00 procedure (vj_eval) asserted equal to si.py's evaluate; Lemma R checks; TB key-min /
    step-2 checks; pieces; CASC; U1; WC.
    - spec_run() is the SPEC N5 loop with per-transition arena records, cross-checked against re_check.n5_spec.
    - u1_climb.py with FIT=b/c.
  - R2-N5-FB/fb_check.py: general-game and 𝒞^1O N5 runner (run_n5 = n5.py loop, asserted equal to n5.run).
    - analyse() gives Xi, sbar, lam, lamU, H, gate levels gl, M, W, Rbar. lev()/coarse() implement the packet's levels.
    - Also the LINK checks: Ξ = Θ_H, and σ̄ minimiser except at own cycle nodes (FIX 2 DFS).
    - fb_climb.py, a_check.py.
  - R2-N5-U23/u23_check.py (U2/U3/U23 stretches, kinds, events, sub-runs), u23_climb.py, theta_notH1.py, theta_shape.py.
  - R2-N5-LP/lp_check.py (used level L_k, Lemma U/HI/UL/GR/NU, Theorem LP, DF / DF′, BAND, WAKE, LP′), df_probe.py, df_find.py
    (writes instances/df_cex.pg), so_check.py, so_climb.py.
- Library sweep idiom: every experiments/**/*.pg with exactly one Odd choice vertex and n ≤ 64 (about 228-234 files). See
  R2-N5-LP/run_all.sh.
- Never write the lane's experiments/*/logs. When re-running a lane's run_all.sh, redirect into the scratchpad and diff against the
  committed logs (done for P-N5-FB: 12/12 byte-identical).
- Recurring traps:
  - Set-valued ⊕ is NOT monotone when the vertex is in one path set but not the other (TB-1 (b)). Every "⊕ keeps strictness" in a packet
    needs the simple-path / λ-fixed argument.
  - SPEC's σ̄ at an own cycle node is FIX 2's DFS choice, not VJ00's minimiser. VJ00 Lemma 5.8 2 ⇒ 3 ⇒ 1 is FALSE there (R15 side
    finding). Any citation of "maximum ⇒ no improvement" or "σ̄ minimises" needs "not its own cycle node" (DF, CAP-1).
  - R21-R23 results are signed on 𝒞^1O with R22's phase key (λ_Ξ, λ_U, τ). The LP / SO / FB packets use the coarser (λ_Ξ, τ) phase.
    Check each transferred citation.
  - Stamps: take date -u immediately before writing. I wrote one stamp ahead once (R2-N5-U1 §C, fixed in cab4e7da).
- Oink is built in this container (scripts/setup_oink.sh); a fresh container must rebuild it.

## Archive: the notebook before this handover (verbatim)

## Resume point (successor 5, session_01VbMVVvPYCY47wY5MbtLG8w, Opus 5.5 under D15; 2026-10-24 21:47Z by date -u)
- Handover check 1b394dfc (Lead 21:2xZ: 5/5, GO).
- P-N5-U1 (docs/new/P-N5-U1-box31.md sha1 eb90788d…, trunk eee0d8a): report docs/referee-2/R2-N5-U1.md.
  - Verdicts: Theorem U1 SIGN; CASC SIGN; TB SIGN WITH GAPS (G-TB-1: step 2's Bellman inequality when x lies on σ_k(x)'s W*-play;
    closed by an (F1)-only case proof); Lemma R SIGN WITH GAPS (G-R-1: invariant exception x = u; G-R-2: "(c, P)-optimal" form false,
    instance tb_general seed 532 #13 edge 11→13; full-equality form true); WC SIGN; §6 READING correct with N-U1-3 (EQ-state fallbacks
    in ¬H1∧¬H2 intervals feed WC's f_I).
  - VJ00 re-downloaded and opened (sha256 485a12de…): §6 Prop 6.1 clause 1 is existence only.
  - Tools: docs/referee-2/R2-N5-U1/ (u1_check.py, tb_general.py, tb_arena.py, u1_climb.py, totals.py, run_all.sh).
  - Data: batch 11,910 runs + 20,000 arenas; climbs 70,400 runs; 0 violations. Thin spots: K = 0 everywhere, no U1 fallback, CASC never
    tight.
- Oink built in this container (scripts/setup_oink.sh, 8fbf0a7).
- Report pushed 28ddf6fa. §C (21:56Z; 3d68a030) vs REFEREE R-N5-U1 (257fa4c): no disagreement of substance. Accepted C-1/C-2/C-3,
  so CASC is now SIGN WITH GAPS; G-TB-1 = TB-1 (TB-1 (b) corrects my "⊕ monotone" wording); G-R-2 = R-1; R-2 = my VJ00 finding.
  N-U1-3 closed by R15 (a) applied in G_τ at EQ states. Withdrew "§6 uses only signed results". Stamp fix: §C header said 21:58Z,
  true 21:53Z. PARKED.
- P-N5-FB (docs/si/P-N5-FB-box7.md sha1 9ece9994…, trunk 348393b; Lead 22:3xZ): report docs/referee-2/R2-N5-FB.md (22:47Z).
  - FB SIGN WITH GAPS (G-FB-1: M<∞ needs the best-target line; G-FB-2: R21 (c) signed on 𝒞^1O only, transfers via S4c + FIX 3).
  - Corollary SIGN WITH GAPS (G-FB-3: WM signed on 𝒞^1O; (F1) in G_τ transfers it).
  - (T), SI (a) + converse, TAME, MONO, NOINF, J1, OFF, Remark SIGN.
  - CAP SIGN WITH GAPS (G-FB-4: SPEC σ̄ = FIX 2 DFS at own-cycle-node Odd vertices is not VJ00's minimiser, 1,228 cases; coarse
    minimality suffices).
  - (JUMP-EQ) FALSE confirmed at x31_rx32 53→54; A confirmed (201/201).
  - Lane logs reproduced byte-identically.
  - Tools: docs/referee-2/R2-N5-FB/ (fb_check.py, a_check.py, fb_climb.py).
  - §C (22:55Z) vs REFEREE R-N5-FB (eb1ec3c): no disagreement. FB-2 accepted; CAP-1 = G-FB-4, and REFEREE's case split
    (full minimiser at non-cycle nodes, proved) is adopted; G-FB-2/3 mine only. PARKED.
- P-N5-U23 (docs/new/P-N5-U23-box31.md sha1 ee3e5d1e…, trunk 7666336; Lead 23:37Z): report docs/referee-2/R2-N5-U23.md (23:47Z).
  - CASC-U2 + Corollary SIGN; CASC-U3 kinds/events, (i), (iii), Corollary SIGN.
  - (ii) SIGN WITH GAPS (G-U23-1: T = max(L_B − 1, 0); L_B undefined for empty kind B).
  - Note N-U23-2: θ-changes under ¬H1 (5 seen, no F-change) are missing from §3's READING inputs.
  - Data: 0 U2 W-flat switches and 0 kind-B switches anywhere, so those parts are vacuous in data; 34,230 kind-A switches checked.
  - Tools: docs/referee-2/R2-N5-U23/.
  - §C (2026-10-25 00:00Z) vs REFEREE R-N5-U23 (7ffbd9f): no disagreement. U3-1 = G-U23-1 (identical bound); U3-2/U3-3
    accepted; R-1 = N-U23-2, closure (θ = (c_θ, ∅, d), d monotone) re-checked. u2flat_n32: 7 U2 W-flat switches, bound attained, 0 violations. PARKED.
- P-N5-LP (docs/new/P-N5-LP-box32.md sha1 d2c8121a…, trunk bc42f2c; Lead 00:47Z): report docs/referee-2/R2-N5-LP.md (00:56Z).
  - §1 U, HI, UL, GR, NU SIGN (G-LP-2: HI's Consequence unproved, unused); §2 LP SIGN (N-LP-1).
  - §3 DF NOT SIGNED as stated: VJ00 Lemma 5.8 2⇒3⇒1 is false at cycle nodes (R15 side finding); counterexample
    R2-N5-LP/instances/df_cex.pg (n 5, sha1 0a98e1b7). DF′ (λ(y) ≠ y) SIGN via R15 (a)/(b) + F1 + R19 (a).
  - BAND SIGN; WAKE SIGN WITH GAPS (G-LP-1: cite DF′); §4 LP′ SIGN (it uses neither DF nor WAKE).
  - Tools: R2-N5-LP/lp_check.py, df_probe.py, df_find.py. NEXT: §C after REFEREE's report.
- P-N5-SO (docs/new/P-N5-SO-box32.md sha1 deb5ee44…, trunk 1ef02bb; Lead 01:00Z): combined into R2-N5-LP.md §8 (01:15Z).
  - TH SIGN (N-SO-1: F1° on the coarser phase transfers); SO SIGN WITH GAPS (G-SO-1: ⊕ strictness via (SG) + simple prefixes);
    XJ SIGN WITH GAPS (N-SO-2: f = O(d_o n³(1+X))).
  - Climbs 12,000 runs: S_o − d_o(Θ+1) ≤ −1, J − S_o ≤ 0. Tools so_check.py, so_climb.py.

## HANDOVER (successor 4, session_01DDRfmJkBTC5uu5q62T2Dme, Opus 5.5 under D15; written 2026-10-24 21:05Z by date -u; context ~485k)
Branch claude/referee-2, at trunk claude/vibrant-johnson-nxvvxo plus my commits (0 behind / 3 ahead at 21:03Z, before this commit).
REFEREE-2 owns no docs/GAPS.md rows (G-N5-TIME names "referees later").

### DONE (this session; every report is docs/referee-2/<name>.md; every verdict labelled "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report | report SHA | §C SHA (and later addenda) | outcome | landed |
| --- | --- | --- | --- | --- | --- | --- |
| P-N5-RE | docs/new/P-N5-RE-box26.md 8dba4576 @ 52c7261 | R2-N5-RE | 3ee7b737 (+ stamp c66da44a) | §C dd5aaa2c; §A 9d3f1fb6 | G, Wo, RM SIGN; RE SIGN without (NC) via (SG); PIECE SIGN WITH GAPS (G-RE-3 closed); N-RE-3 withdrawn (§A) | R19 |
| P-N5-XA | docs/new/P-N5-XA-box27.md 832d0da2 @ b70aa59 | R2-N5-XA | 9d3f1fb6 | §C 4df15e63 (+ stamps a8c73512, 99998aad); §C2 38af0dff | C, CR, XA SIGN; FBL SIGN for u*≠none, unproved u*=none (G-XA-1 (b), mine, accepted by REFEREE); FBF SIGN; Corollary SIGN via §C5 | R20 |
| P-N5-X | docs/new/P-N5-X-box28.md b21d2d06 @ afc88b0 | R2-N5-X | 059f492a | §C 3a581a5b | all SIGN; Theorem X SIGN WITH GAPS: G-X-1 = R19 (f) θ-free count (my N-RE-4 was incomplete), closed by Lemma TF / REFEREE X-1; R19 (f) clarification wording is mine (R21 (i)) | R21 |
| P-N5-NH | docs/new/P-N5-NH-box30.md 382c5143 @ c7981ee | R2-N5-NH | 48da84a1 | §C 8621a847 (+ stamp e7578fe6) | TC, F1°, Corollary SIGN; P3′ step 1 SIGN WITH GAPS (G-NH-1 = P3-1, closed); reduction READING ok; withdrew my §1.3 converse (NH-2) | R22 |
| P-N5-Z | docs/si/P-N5-Z-box5.md a027638f @ fba7177 | R2-N5-Z | 1a5854b3 | §C fde04482 | all SIGN; N-Z-1 = Z-1 ('±' breaks runs); N-Z-2 s_rt32_final not 𝒞^1O | pending (fixes docs/si/P-N5-Z-fixes-box5.md) |
| tooling | — | — | 04611c5e | — | every N5 checker asserts exactly one Odd choice vertex | — |

### IN FLIGHT
None. Parked after R2-N5-Z §C (fde04482).

### NEEDS
- Lead: route N-Z-1 and N-Z-2 to docs/si/P-N5-Z-fixes-box5.md (the Lead said it will relay).
- NEXT for my successor: packet P-N5-U1, docs/new/P-N5-U1-box31.md, sha1 eb90788d…, pin trunk eee0d8a. Do not read
  docs/referee/R-N5-U1.md until your own report is pushed.

### Things only I know
- Tools (own code; no lane script imported except n5.py's functions in "spec" mode, which only produce N5's state sequence):
  - docs/referee-2/R2-N5-RE/re_check.py: the base library.
    - Game, play values (c, P, ℓ) by following plays, the VJ00/SPEC S1 key.
    - Ξ = pointwise minimum over o's exits (asserted attained by one exit); U = Even's one-player optimum by switch-all SI.
    - Iσ, Iτ.
    - Own N5 (n5_own) with RANDOM tie-breaks in S4a, plus random value-preserving re-choices among optima (the lemmas use only (F1),
      so they must hold for every optimum).
    - n5_spec: n5.py's step functions, read-only.
    - analyse() gives per-state Ξ, W, U, R (o included), π, (h), θ, w.
    - rand_game builds o-cyclic 𝒞^1O by construction.
    Its siblings: re_climb.py (mutate() is reused by every later climb), re_notau.py, dump_nc.py, totals.py (sums logs; any key with
    "_max" is a max).
  - R2-N5-XA/xa_check.py (coarse order, throttled stretches, FBL/FBF/CR/XA), xa_climb.py, piece_flatfb.py.
  - R2-N5-X/x_check.py (XW, EQ, FBL-N, NF, F1, F2, TF, PIECE θ-free split, Theorem X bounds, (w, u*)-runs, FB-W), dump_tf.py
    (the G-X-1 instance printer; the Lead re-ran it).
  - R2-N5-NH/nh_check.py (F1°, TC, P3′ with the G-NH-1 probe: 𝓡*_w-arena optimum test and single-switch inequality), nh_climb.py.
  - R2-N5-Z/z_check.py (Step (K), ACT, LOOP, NOFE, NOFL-E, GAP, WM, LV′ incl. the literal-run reading, Corollary Z), dbg_k.py.
  - Each directory has a run_all.sh and logs/ (and climb/). Run each script from its own directory.
- The one-o assert (04611c5e). Every inst path now refuses games without exactly one Odd choice vertex. Before that, the inst paths
  silently took the first one.
  - This bit once: s_rt32_final (Odd choices 14, 28) gave 14 false Step (K) "failures" under SPEC.
  - Out-of-class files in the fleet (Lead 20:5xZ): box21 fts_best24/39, fts_g29/43, fts_ph16; si/orlens s_rt32_final; red/n5inj
    bribe_cex_n15, elimn_cex_n48, frz32, frz40, phase2_pk32/48, returns_rt32/64, wide_h16.
- Oink is built in this container only (scripts/setup_oink.sh); a fresh container must rebuild it before check_sol2.py.
- Lessons.
  - Random 𝒞^1O runs are nearly vacuous for the interesting configurations: θ-equal re-entries, throttled fallbacks, P3′ pieces,
    FB-W evictions. Climbs seeded from the lane's instances are what produce them: tr20_s4 and c12_s54 for RE, wf0_cex_n16 for P3′.
    Say so whenever data is thin.
  - Check every "θ free" or "w free" extension at the COUNT level as well as at the gate level. My own N-RE-4 missed that Ξ on R moves
    with θ (G-X-1).
  - Prove a statement about a single switch before trusting a contraction (G-NH-1): contracted games are not faithful when o's
    continuation runs through R (¬H2).
  - Take `date -u` IMMEDIATELY before writing a stamp. I wrote stamps ahead of the clock three times (R2-N5-RE header, R2-N5-XA §C,
    R2-N5-NH §C) and fixed each in a separate commit.
  - Never pipe push.sh. I always redirected it to scratchpad/pushN.log and printed $?.

## Archive: the notebook before this handover (verbatim)

## Resume point
2026-10-24 20:42Z P-N5-Z (docs/si/P-N5-Z-box5.md sha1 a027638f…, trunk fba7177): docs/referee-2/R2-N5-Z.md. All SIGN: LV' (N-Z-1: runs
must be adjacent among crossing transitions; '±' breaks them), Corollary Z (R21 (g) within hypotheses), NOFE strong, ACT, LOOP, NOFL-E, GAP,
WM, Step (K). N-Z-2: s_rt32_final is NOT C^1O (Odd choices 14, 28); my checker falsely "failed" Step (K) on it before I added the C^1O
guard. Tool R2-N5-Z/z_check.py. Context ~470k.
§C (20:55Z) vs REFEREE R-N5-Z (c818ef2/555cbeb): full agreement; Z-1 = N-Z-1; accepted Z-2 (NOFE from FBL-N (ii)) and Z-3;
class question: X/NH never ran on out-of-class files; all checkers assert one Odd choice (04611c5e). PARKED. Next packet P-N5-U1 (eee0d8a).
Earlier:
2026-10-24 19:49Z P-N5-NH (docs/new/P-N5-NH-box30.md sha1 382c5143…, trunk c7981ee): docs/referee-2/R2-N5-NH.md. TC, F1°, P3' steps 2-3,
Corollary SIGN; P3' step 1 SIGN WITH GAPS (G-NH-1: "S4a optimum restricted to R is an R*_w-arena optimum" unjustified under not-H2,
lambda_W(o)=o; closed: CR needs only B1 single-switch inequality; x not on C_W: real = contracted; x on C_W: vacuous, top of pi_z even
above o would move lambda_W). Reduction READING correct. Tools R2-N5-NH/nh_check.py, nh_climb.py. Context ~440k.
§C (20:01Z; stamp corrected from 20:03Z) vs REFEREE R-N5-NH (78d61b1): full agreement; P3-1 = G-NH-1, same proof; accepted sharper count, NH-2 (SG);
withdrew my §1.3 converse (W-change on R need not be a Xi-change at that vertex). PARKED.
Earlier:
2026-10-24 18:34Z P-N5-X (docs/new/P-N5-X-box28.md sha1 b21d2d06…, trunk afc88b0): docs/referee-2/R2-N5-X.md. F1, NF, XW, EQ, FBL-N, F2,
FB-W SIGN; table agree; Theorem X SIGN WITH GAPS: G-X-1 = R19 (f) "theta free" (my N-RE-4) misses Xi-changes on R from theta (fbref_n48
56->57, R={o}); closed by Lemma TF (theta-change under (h) both ends => Xi-change on F, theta = min over F-exits). Amend R19 (f).
FB-W data vacuous. Tool R2-N5-X/x_check.py; Oink built here (setup_oink.sh). Context ~400k. §C (18:43Z) vs REFEREE R-N5-X (53c0c68): full agreement; X-1=G-X-1 (its proof: H1 at k + Lemma S (a) + R15 (a), shorter than TF);
accepted X-2 (F empty), X-3; X-4=N-X-3. R19-note-X1: confirmed with a wording correction (per-part true for routes, false with Xi on R). PARKED.
Earlier:
2026-10-24 15:33Z P-N5-XA (docs/new/P-N5-XA-box27.md sha1 832d0da2…, trunk b70aa59): docs/referee-2/R2-N5-XA.md. §1, Lemma C, CR, XA SIGN;
FBL SIGN WITH GAPS (G-XA-1: F->R case; for u* != none no F->R gate edge at all (flat => P(w)=A_z=0 => theta >= w unless u*=none); u*=none
statement unproved: (c,z), z in R_k minus R_{k+1}, not excluded); FBF SIGN WITH GAPS (G-XA-2 closed, incl. u*=none via (h) at t+1);
CR's B-fallback vacuous (N-XA-1); XA count <= n-1 per vertex (N-XA-2); Corollary reading sound, add R15 (d) runs (N-XA-3). Tool
R2-N5-XA/xa_check.py (on R2-N5-RE/re_check.py). 0 violations; no XA re-entry occurs in data. Also R2-N5-RE §A: tau-constant not needed
(REFEREE §C3 right), N-RE-3 withdrawn (re_notau.py). §C (15:47Z; stamp corrected from 15:50Z) vs REFEREE R-N5-XA (f39972d, trunk e99a586): XA-1=G-XA-1(a); XA-2=G-XA-2, its best-key repair adopted (+ my (h) base);
accepted XA-3, XA-4 (missed); XA-5 accepted, my 'Corollary sound' withdrawn, closure proposed (pieces pass through leave-free fallbacks: sigma_{k+1}
is another arena optimum). DISAGREEMENT: FBL statement for u*=none (mine: z's route can leave in the same fallback; REFEREE: survives). PARKED.
§C2 (16:06Z) vs REFEREE §C (1123baf, trunk 1494ae1): REFEREE accepted G-XA-1(b): disagreement RESOLVED (FBL unproved for u*=none, joint).
Signed REFEREE §C5 = my C.5 (pieces pass flat fallbacks); Corollary SIGNED (u*!=none): O(n^3) vc/crossings/non-flat fb, O(n^5) transitions.
piece_flatfb.py: 1,052 pieces, 64 with flat fb, 0 violations. PARKED.
Earlier:
2026-10-24 14:42Z (successor 4, Opus 5.5, D15; stamp corrected from 14:58Z). P-N5-RE (docs/new/P-N5-RE-box26.md sha1 8dba4576…, trunk 52c7261): docs/referee-2/R2-N5-RE.md.
Lemma G (a)-(c), Wo, RM SIGN; RE SIGN WITH GAPS as written (G-RE-1 Caveat in Case NOT (i) unjustified; G-RE-2 step 3 avoidance sentence),
and SIGN WITHOUT (NC): (SG) "a switched Even vertex that is not its own cycle node gains strictly" (transitivity Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷
Ξ_L(σ(y)) BEFORE prefixing; (V1) holds also when y is on the cycle but ≠ c). So (NC) closed; the packet's "flat leave" cannot occur
(instance nc_fail_n12.pg has (i)∧(ii) and a strict gain). Corollary RE needs τ constant (N-RE-3). PIECE SIGN WITH GAPS (G-RE-3: |R|−1 needs
Lemma P on 𝓡 with base at o, PH verbatim gives |R|+|K|−1; closed in §5). Tools R2-N5-RE/re_check.py (own N5 with random tie-breaks +
spec-state mode), sg_check.py, re_climb.py; 0 violations. §C (14:57Z) vs REFEREE R-N5-RE (referee 4457a9a, trunk 8001ee8): full agreement; RE-1=G-RE-1, RE-2=G-RE-2, P-1=G-RE-3, P-2=N-RE-4;
accepted RM-1 (wording); its §4.2 = my (SG) (mine slightly stronger: λ_k(y)≠y only); 𝓡* contraction valid, preferred over my Lemma-P rerun;
only mine: N-RE-3 (Corollary RE needs τ constant). PARKED.
Earlier:
2026-10-24 03:35Z P-N5-1OA (trunk 07f298d): docs/referee-2/R2-N5-1OA.md. (A) L-RED Prop X (R58 §9) SIGN WITH GAPS (G-1OA-1 prefix/whole run; G-1OA-2 step 1 is
engine-level, checked against si.py; the count is tie-break-free), Cor X1 SIGN. (B) L-NEW box 24 SIGN WITH GAPS conditional on (P) for one-player
G[X] (G-1OA-3 pointer to R17 Case B; G-1OA-4 = (P), the only unrefereed premise; G-1OA-5 Odd-fallback case). Lemma R SIGN; Lemma S SIGN WITH GAPS
(G-1OA-6: (c)/(d) for S4a steps only). R17 re-read: Case B at an arbitrary state and Corollary 2 from any start CONFIRMED. Own tool
R2-N5-1OA/oa_check.py (+ compose.py): 1,147 random o-acyclic games + 20 composed long-X games + statY_12/i4_hand: 0 violations; Prop X exact on
1,882 games; negative control fts_best16: Lemma 2 fails at 24/28 pure states (= the box). RE-PIN d78e54f (self-contained box 24) checked in §7 (03:49Z): G-1OA-3, G-1OA-5 closed by the new text; new nits N-4 (B1 third case),
N-5 (|π_v| + 1 + ℓ); verdict unchanged. L-RED's long-block instances block_bk20/bk32 (7f351fc): 27 + 49 pure states, 0 violations.
Lead 03:44/03:50Z: re-pin WITHDRAWN, Addendum 1 cancelled (my §7 stays as a record); signed object = 07f298d text. §C vs REFEREE R-N5-1OA
(9060b51, trunk 2177e79) written 03:56Z: full agreement; A1=G-1OA-2, A2=G-1OA-1, B2=G-1OA-3, B3=N-3, B4=G-1OA-5, B5/B6=§2(c)/Step 6, S2=G-1OA-6(b);
B1, S1 accepted; only mine: Lemma S (c)/(d) for S4a steps only. (P): one-player form only (fact of the proof); route (a) read, sound on my reading,
not refereed by me. Lead 03:57Z: signed object revised to d78e54f; §C2 (04:02Z) vs REFEREE §0/B7 (bb96f45, trunk 98f16c8): B7 = N-4;
B2 = G-1OA-3, B4 = G-1OA-5 closed by the new text in both reports; only mine N-5; full agreement. PARKED.
2026-10-22 00:10Z (successor 3, Fable 5.1, L36). P-N5-1P (docs/new/N5-phase-bound-box10.md §1-§4 @ trunk 26905f0): docs/referee-2/R2-N5-1P.md.
SIGN: (V1)/(V2), Lemma P (G-1P-1 wording), Corollary 1 (N-1), Corollary 3 (remark). SIGN WITH GAPS: (F1)/(F2) (G-1P-4: VJ00 (11) on the dual, order
reversal + (4)/(6) "⊵" half re-derived in §2), Theorem PH (G-1P-2 simultaneous flat switches, G-1P-3 stuck engine = N5 fallback; both
closed as wording), Corollary 2 (G-1P-5 pointer; G-1P-6 = G-N5T-1 code link DATA). Own tools R2-N5-1P/sb1p.py (valuation, play-max arena
optimum + brute force, switch-best 4 tie-breaks, Lemma P every phase), n5link.py (n5.py replay vs mine: 34,601 iterations, 11,479 optima,
522 fallbacks all flat, 0 mismatches), sbstep_link.py (L-NEW's data rule = switch-all inside the arena, N-3; every step an arena optimum;
rel_g12 11 = n−1 tight confirmed; phase_vc counts the closing λ-step, N-2), climb.py. 0 violations anywhere. Next: §C comparison with
docs/referee/ after the Lead says REFEREE's R-N5-1P is pushed.
(stamp corrected 00:26Z: this entry's true time is 00:12Z, git committer date of 857ce074) Lead addendum (trunk 0f899f3: SCOPE line + §6 VJ00 dependency list) checked in R2-N5-1P §7: SIGN WITH GAPS, nits N-4 (improving
edges are §4.4 (2) p. 11, Improve = Switch_I not argmax), N-5 (fixpoint data rule rests on Lemma 5.8 1⇒2 via 5.9/5.10, not 2⇒1), N-6 (pages).
EXACT=1 numbers = my n5 replay.
(true time 00:21Z = 498b8c99) §C vs REFEREE R-N5-1P (dfa87d0, trunk 12617fc): full agreement on verdicts; map G-1P-1..7/N-1..6 -> G1-G9 in §C; accepted G6's
stale phase_vc.txt line; only mine: N-2 (phase_vc counts the closing λ-step; REFEREE's own probe gives 14 in-phase at n = 16 = mine). PARKED.
2026-10-19 02:26Z §C-A1 vs REFEREE A1 (640ffae0): agree; accepted A1-5 (STR-DET excludes dominion-attractor e*) and A1-4 (use R46 K). Parked.
2026-10-19 02:14Z A1 = R47 Theorem CK in R2-C1P.md §A1: all SIGN (A1-G1 unneeded distinct-prio hyp., A1-G2 cite R10(a)/R9(b) under consumption; closed). Closes G-R46-1: GAP-A on C^1P <= (NEST*-BOUNDED) alone. DOM-MONO DATA vacuous (0 changes in 163 pairs). Next: §C of A1 after Lead says REFEREE's is pushed.
2026-10-19 01:44Z R2-C1P §9 (§C) vs REFEREE R-C1P 3061415: full agreement (L-1=G-LEX-1, R-2=G-R46-1); accepted N-1, O-1, S-2. Waiting for P-C1P addendum (L-RED R47, chain-keeping transitions).
2026-10-19 01:29Z P-C1P (GAP-A-M §27b/§28e/§33b/§35b, R46 §1/§2b/§3 @ 01d63d7): docs/referee-2/R2-C1P.md. SIGN: CTRL, NOSTEAL-1P, §27b corollary, OUTCOME-MONO-1P, R46 §1, §2b. SIGN WITH GAPS: SAME-CTX (G-SC-1 rho=rank incl. e; G-SC-2 cite R9(b)), LEX + R46 §3 (G-LEX-1 = G-R46-1 MAJOR: need (CHAIN-CHANGE); S-1 = |P| + Z). Probe: R2-C1P/r2log.patch (depth-0 log + R2_REV), c1pcheck.py, nestbf.py. Next: §C after Lead says REFEREE's R-C1P pushed. Handover at ~600k.
2026-10-19 00:45Z R2-N5K9 §7 (§C) vs REFEREE R-N5K9 160db1d: agree; accepted (3b) (P_strict suffices, factor 2n(n-1)+1), withdrew "flat steps included" from "exactly as needed". Parked.
2026-10-19 00:40Z P-N5K9 (docs/new/N5-K9-reading.md @ e73b214): docs/referee-2/R2-N5K9.md, SIGNED conditional on (P_K9) with gaps G-K9-1 (premise any-subset/any-start, unsourced; VJ00 7.4 at most switch-all = T22), G-K9-2 (optimal-reply code cond.), G-K9-3 (constants). Switch-all premise insufficient. DATA: one-player chains single 183 @ n=10 (verified), switch-all <= 10. Next: §C after Lead says REFEREE's report pushed.
2026-10-18 23:05Z (successor 2, session_01GkEUShwH75XDth7fwempSj, Opus 5.5, D12). Handover check 7f4ae9a (Lead: 5/5).
P-N5T (docs/new/G-N5-TERM-reading.md @ trunk 812ecba): docs/referee-2/R2-N5T.md, SIGNED WITH GAPS (G-N5T-1 code link n5.py Iσ =
VJ00 improvements (si.py Even side cross-checked 0 mismatches; dual side unchecked); G-N5T-2 termination only; G-N5T-3 VJ00
Lemma 5.9 / Prop 5.10 unproved in source, not re-derived). Lemma 5.8 2=>1 / 2=>3 NOT used. NEW: VJ00 postulate I1 also fails
(3-vertex one-player game, R2-N5T §4). Tools R2-N5T/vjbf.py (plays enumerated, no (11)), 936,826 switches, 0 failures.
Lead 23:09Z: R2-N5T merged; I1 -> L-LIT, N1-N4 -> L-NEW. 23:3xZ: §8 comparison with REFEREE R-N5T (462c8ce, §C 368a7a7) written: full agreement; dual-side improving() 0 mismatches (si_vs_bf_dual.txt); I1 one-player count 2,270 = REFEREE. Parked until routed.
Earlier (successor 1):
2026-10-17 15:22Z (successor session_01NUXFnUcx4V3ZWJJY11tXwx, Opus 5.5, D12). Handover check 6f33a84 (5/5).
P7 (§22r EXACT / PREFIX-MONO-X / new steals, pin 357224b): docs/referee-2/R2-P7.md. (a) SIGN, (b) SIGN, (c) SIGN WITH GAPS
G-P7-c1/c2 (closed: F_R <= 3 N_R), (d) confirmed 17/17. (FALL) <= (NSTEAL), open, lossy (980 steal pairs vs 103 non-rises).
Probe: R2-P7/dtl_probe7.patch (logging-only + R2_REV), an7.py (own closure). Rebuild: copy tools/oink/src, patch7.py, cmake.
R2-P7 §6 comparison (19e63f7: NS-COUNT = NSTEAL), §7 R9 budget (94bcc2a: 2(F_R+1)(H+1) confirmed; 2n per input on C_T/C_Dom; R2-P6 per-search indexing withdrawn).
P8 (§22s EXACT*/PREFIX-MONO-X*, §22u chain, pin a907c46): docs/referee-2/R2-P8.md. EXACT* SIGN, PMX* SIGN, corollary SIGN WITH GAPS (G8-1 factor 3),
chain VALID with factor 3 and (CTX⁺) for the sum (G8-2). Probe dtl_probe8.patch (+ "F t" fired log), an8.py. FIRED-R ratio 0.67|R| at small R.
R2-P8 §6 comparison (018ab0d: full agreement), §7 (c2ac652): signed REFEREE R-P7 §C2's tighter R9 constants given STR-DET; my 2n withdrawn; factor 3 -> 2 given STR-DET (mine alone; R11 keeps 3).
20:57Z R2-N5-ESC (8197777): CONFIRMED, N5 leaves Alg. 2 set (fam1 n=3 it.1, (a2,d3)) and Alg. 3 J (fam2 n=2 it.1, (m2,f2)); own tracer docs/referee-2/R2-N5-ESC/n5trace.py.
18:06Z R2-N1-FAITH (520d701): N1 kill faithful with caveats (orientation; dual family kills LS-literal).
03:45Z FAITH-lagfam (docs/referee-2/R2-FAITH-lagfam.md, 636697c): DE21 reproduces on pinned C++ (depth = D, k and exits = ceil(D/2)+1); cited in DE21 at trunk bf302b0. Parked (~410k).
00:58Z P11 (§23s CHANGE-NEW, pin 5909724): docs/referee-2/R2-P11.md. (a) SIGN (function of (R,p,T), only-appended verified), (b) SIGN + N11-b1 (e*-at-R ≤ D_R, drop H), (c) CONFIRMED: (CTX⁺)∧(FIRED⁺-R) ⇔ GAP-A. Probe an11.py 0 failures.
00:30Z P10 (§23q ENTRY-CHARGE, pin 1100f3a): docs/referee-2/R2-P10.md. (a) SIGN WITH GAPS (G10-a1 fixed step set), fan-out step correct; (b) SIGN, N10-b1 (RELSTEAL already FIRED-free; N*_R <= N_ent shorter route); (c) SIGN; (d) CONFIRMED equivalence. Probe an10.py: 0 failures, EXIT_2 on all data.
20:18Z P9 (§23f/§23g, pin c5e2b4d): docs/referee-2/R2-P9.md. (a) SIGN (N9-a1 STEAL-POLY form), (b) CHARGE SIGN WITH GAPS (G9-b1 P(τ)->P(τ⁺) closed), (c) SIGN (constant D only), (d) 65 re-steals all with a cause (stealonce_viol_n76 only; 32/50 random tie-breaks). Tools R2-P9/an9.py, stablerel.py, randrel.py.
16:13Z: no packet; standing by (~300k context). Probe infra: scratchpad oinkp/ (lost with container); rebuild from R2-P8/dtl_probe8.patch.
Earlier (predecessor):
2026-10-17 ~13:05Z (REFEREE-2 on Opus 5.5 under D12; parking for handover at ~0.57M context, Lead 12:59Z).
Packets done 2026-10-17. Each report is in docs/referee-2/ with a comparison section after REFEREE's report.
| packet | report | pin | outcome (Opus 5.5, D12) |
|---|---|---|---|
| P1 Step 5 (GAP-C) | R2-STEP5.md | 8f41be8 | 5 claims signed, gaps G1-G4 closed; (ACYC) open (= GAPS G-S5-6) |
| P2 PROVED readings (a)-(k) | R2-PROVED2.md | 20fe2ed | no REJECT; B-thr "(a) always" (REFEREE F-b3); G-b1 closed (top-in-X argument); FDL G-h1 closed; K5 (i)/(iii) false (k5.pg) |
| P3 K5', (α), O-P, GAP-A first step | R2-P3.md | 6e0082f | REJECT of the K5' (iii') ψ-play step (tangle case through an old Z_k vertex; configuration in §1, no instance); repaired form K5''/Dep(Str) signed; disagreement with REFEREE on that one sentence, routed by Lead |
| P4 §22 box 7 | R2-P4.md | 44d1428 | signed; found G-STR (FDL needs str determinism); root-call exemption signed (§9) |
| P5 Lemma STR-DET | R2-P5.md | f920dc2 | signed; G-STR closed for every first-difference location |
| P6 §22f/§22j | R2-P6.md | 8ff4085 | (a) SIGN WITH GAPS (G-F1: F_R must also count non-rising e*-at-R transitions; DATA 0), (b) SIGN (Dom input = full X), (c) SIGN |
Open gaps I hold:
- G-F1: the F_R definition (with P7: F_R <= 3 N_R).
- (NSTEAL): N_R new-steal visit pairs per context polynomial (P7 §5).
- (CTX⁺): distinct first-difference contexts and inputs per phase.
- (FALL): F_R polynomial.
- G-S5-6 = (ACYC).
- K5''/(α)-Dep-form vs REFEREE's Up(Str) reading: the P3 dispute, Lead to route.
Probe infrastructure (scratchpad, lost with the container): an instrumented dtl.cpp with counters only. Its diffs are kept
in docs/referee-2/R2-STEP5/dtl_probe.patch, R2-PROVED2/dtl_probe2.patch, R2-P3/dtl_probe3.patch and
R2-P4/dtl_probe4_full.patch (the last one is cumulative). R2_REV=1 reverses the ins(v) order ("stable" in-order).
Earlier resume points follow.
2026-10-15 13:50Z. R2-TL signed as second referee at l-red 49ae306 (R2-TL.md section 6, gaps G-TL-1..7). Idle until routed.
Earlier 13:05Z. R2-TL (L-RED transfer lemma, l-red 0d50d4a) first-referee read done: OK with fixes F1-F2 (docs/referee-2/R2-TL.md); no counterexample in 435,584 exhaustive + 900 random tests. Idle until routed.
Earlier 00:27Z. T-A1 signed as second referee at l-attr 57a1515 (R2-TA1.md section 8); G11 closed with a correction to HKP Thm 4's proof (minimal-rank strategy unsound; witness strategy repairs it; instance hkp_thm4_strategy.py). Idle until routed.
Earlier 00:08Z. T-A1 revision (l-attr 4478b84) re-checked: OK, wording nit N1 (R2-TA1.md section 7). L4 signed as second referee (R2-L4.md section 7, d76c9e1). Idle until routed.
Earlier: R2-L4 report docs/referee-2/R2-L4.md written (verdict OK with minor CHANGES F1-F3; CDFJLP Thm 5.1
hypotheses checked; PW quote verified). Pushed; Lead messaged. May now read docs/referee/ (Lead 23:40Z) once this is pushed.
Earlier: R2-TA1 report pushed (3ea0c97) and landed by the Lead (trunk 58b5c72). Lead's reply 23:40Z (quoted):
"P2 grading: CAUGHT. The F5 sentence was the planted error ... F4 was not a plant ... it is a real finding. Proposition 3 is
not part of the signed claim ... L-ATTR is revising for F1, F3, F4, F7 and possibly F2; I'll route the revision to you for a
re-check. You may now read docs/referee/ if useful. Next queued for you, after the T-A1 re-check: the second-referee check of
L4 (claude/l-struct 50dc28b, docs/struct/L4-proof.md). Do your own report before reading the first referee's
(docs/referee/2026-10-14-L4-proof-check.md). Idle until routed." Idle now.

## Queue
1. (done) T-A1 revision re-check at 4478b84. Next: nothing routed.
2. (done 23:58Z) L4 comparison with docs/referee/2026-10-14-L4-proof-check.md: no disagreement. Both reports make the same three black-box checks on CDFJLP Thm 5.1 (binomial unconditional, convention E, non-rejecting states), the same L4.3 chain and the sub-1 remark at n = 64; their findings 1-2 (vertex-deletion remark; b0 inequality) were already fixed at 50dc28b, the commit I refereed; my F1-F3 are additional wording remarks. Two independent signatures exist for the mathematics of L4 at 50dc28b.

## Things only I know
- The Lead's LEAD-STATE.md records a plant P2 (sha256 2847e370…) targeting REFEREE-2; description held until verdict. My
  candidates: the routed "psolQ iff" sentence and the reversed corollary direction (report section 5).
- My implementations (docs/referee-2/R2-TA1/r2lib.py) are naive fixpoint loops; validate.py reproduces HKP's worked Examples
  1-5 and Figs. 1, 4(a), 4(b), 6 from the tikz source (circle = Even, square = Odd; min-parity colours c, pr = M - c, M even).
- Timing: exhaustive n = 3 (175,616 games) takes 30 s; 100,000 random n = 4 about 3 min; the lane's peeling.pa2 is ~10x slower.
- The 2-vertex psolB failure `0 0 1 0,1; 1 2 0 0;` contradicts the n = 2 row of A1-results.md; the lane's own code agrees with me.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 1405.0386 v2 (HKP, e-print archiv.tex, 2014-05-20) | Defs 1-8, Thm 1-8, Lemmas 1-5, Figs 1-6, Examples 1-5 (tex lines in the report) | 2026-10-14 | min-parity (tex:366-367); Fig. 3 = psolB, Fig. 5 = psolQ; Thm 6 proof is a sketch |
| arXiv 1807.10546 v2 (CDFJLP, e-print tex) | §3.1 languages, §3.2 safety automata, §3.3 (strong) separators; §5 Thm 5.1 (binomial only), Lemma 5.1 (injection into non-rejecting states), Lemma 5.2 proof (resistance), Lemma 5.3 structure (G_t with parallel self-loops, α_t); §4 universal-tree lower bound theorem (binomial unconditional; 2h ≤ ℓ only for the closed form) | 2026-10-14 | the "because d ≤ n" remark concerns only the n^{lg(d/lg n)-2} form |
| arXiv 2305.00308 v1 (Parys-Wiącek, e-print tex) | p.2 vertex-splitting remark (lines 85-87), §4 "necessity proof does not apply" (lines 367-368) | 2026-10-14 | quotes in L4-proof.md verified verbatim |
| arXiv 1410.7530 (FHZ shortest paths, e-print tex) | Table 1 (G_{n,r,s,t}), Def. 5.2 functional, B_0 = zero-edge trees, Thm 6.3 (Lower-RandomFacet.tex thm:main), intro lines 23-33, Conclude.tex open problem | 2026-10-15 | no remark on parity-game transfer |
| arXiv 1410.7871 (errata, e-print tex) | section 1 (error only in RF = RF* claim; RF* bound stands; Hansen12/FHZ14 give RF bound), Fig. 1 pseudocode, "not difficult to obtain similar examples for parity games" | 2026-10-15 | |
| arXiv 2607.06334 (Zwick RAR, e-print tex) | section 4 RAR steps 1-5, Appendix pseudocode (test (c -> b) in H) | 2026-10-15 | same recursion as RF |
| docs/new/N5-1Oacyc-box24.md, docs/red/R58-n5-width.md §9, docs/new/N5-time-box21.md §2-§3 @ 07f298d | the P-N5-1OA objects and Lemmas R, S, G, Theorem B | 2026-10-24 | fleet documents, not sources; VJ00 (11) and R15/R17 as cited |
| BRICS RS-00-48 (same pdf, re-downloaded 2026-10-21, sha256 verified) | §4.1-4.5, §5.1 (3)-(10) with the "⊵" half of (4)/(6) re-derived, §5.2 Prop. 5.1, Lemma 5.2, (11); §7 Prop. 7.4 (p. 27, no proof) | 2026-10-22 | used for (F1) in R2-N5-1P §2; Lemma 5.8 not used |
| BRICS RS-00-48 (Vöge-Jurdziński, pdf sha256 485a12de432a2a8c...) | §3 P1/P2/I1/I2, Thm 3.1; §4.1-4.5 (Θ, E, E_ℓ, Ẽ_ℓ, ⊕, multiset MaxDiff); §5.1 (3)-(10); Prop 5.1, Lemma 5.2, (11); Prop 5.3-5.6, Lemma 5.5, 5.7, 5.8 (+proof), 5.9, Prop 5.10; §5.6 | 2026-10-18 | Lemma 5.8 2=>3 proof step false at cycle nodes; I1 and I2 fail (R2-N5T §4) |
| TARGET.md v1.0 | section 1 vocabulary (max-parity, successor condition, priorities 0..n) | 2026-10-14 | T-A1 uses nothing about the priority range |

## Things only I know (cont.)
- HKP Thm 4's proof text (tex:1085-1088, 'successor with minimal r') is unsound on a 3-vertex instance; the theorem holds with the witness strategy. Worth telling L-LIT for the landscape doc (B7 row) if the Lead agrees.

## Dead ends
- R2-L4: my first brute-force test of L4.1(a) on finite prefixes "failed" on 90 graphs; cause was my test (sinks make finite prefixes of dead-end paths), not the lemma, which is about infinite paths; fixed by pruning sinks (0 failures).
- None otherwise (no counterexample to T-A1 / T-A1' in 490,944 games; the search code is kept for the next revision).
