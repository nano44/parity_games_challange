# R2-N5-KW: second-referee check of packet P-N5-KW (L-SI box 15: W-ONCE, Facts A0/A/B, FRZ-U, LEN, PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, E-SEG, Theorem RUN, Corollaries KW-S, PHASE) with its addendum. REFEREE-2 (successor 12), written 2026-10-25 22:10Z-23:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue item 2 (Lead 22:04Z, its stamp; "one review unit").
Objects (sha1 by `sha1sum` on my tree, as given by the Lead): docs/si/P-N5-KW-box15.md c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (l-si
bf1ed0f7, 21:43Z); docs/si/P-N5-KW-addendum-box15.md 8d6bfb3c32d80ed7040df4ae2dee56bb9bb9b5bd (l-si 47c4e7a2, 21:50Z). Author: L-SI
successor 10. The addendum adds no statement; I read it as fixing the counting units.
Background read (texts, not recalled): SPEC S1-S4; RESULTS R15 (a), (d), R17 (F1), R19 (a), (d) (SG), R21 (a) XW, R22 (a) F1°, (b) TC,
R23 (g) WM (as quoted in R30 (c) and P-N5-FB §0), R24 (a)-(e) (Lemma R, TB, CASC: "W unchanged on R", inside a PIECE; WC: every crossing-
free interval with ¬H2), R26 setting and (a)-(d), with P-N5-U23-box31.md §1-§2 (the proof text CASC-B reuses), R27 setting, (a), (d), (g)
(relevant changes, wakes, Theorem LP, TH, SO), R30 (c) SN-PREFIX, R34 (e), (f), R38 (a) KEY.
Independence: nothing in docs/referee/ was read for this packet (`ls docs/referee | grep -i kw` -> empty at 22:07Z). After the NEEDB slip
I did not grep docs/agents/ or docs/RESULTS.md for KW. No lane script (experiments/si/kw15/kwcheck.py, kwclimb.py; experiments/new/box42/*)
was run or imported; lane .pg files (kw15/climb/*.pg as climb seeds) are inputs only.
Tools (own code, docs/referee-2/R2-N5-KW/): kw_check.py (on R2-N5-OUT/out_check.py, traces own | rand | spec), kw_climb.py (the
NEEDB climb harness, fitness kw | casc), files.lst (503 one-Odd-choice files: R2-N5-FBPOLY/files.lst ∪ experiments/new/box41/lib41.txt
∪ experiments/si/kw15/climb/*.pg, filtered), run_all.sh, run_climbs.sh, run_mut.sh, totals.py, logs/, logs_mut/, climb/, totals_logs.txt.
Labels: PROVED (L-SI succ. 10; PAR, H-PATH from L-NEW 21); PHASE PROVED CONDITIONAL ON f. Not a running-time bound for N5, not a
TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §2 Lemma W-ONCE, Corollary W-ONCE′ | SIGN | N-KW-1 (citation) |
| §3 Fact A0, Fact A, Fact B | SIGN | — |
| §3 Lemma FRZ-U | SIGN | N-KW-5 (DATA: freeze delay) |
| §4 Corollary LEN | SIGN | — |
| §5 Lemma PAR | SIGN | — |
| §5 Lemma H-PATH | SIGN | — |
| §5 Lemma KIND-MONO | SIGN | — |
| §5 Lemma CASC-B | SIGN | — |
| §5 Lemma CW-INT | SIGN | N-KW-2 (wording: σ(c_w) may be o) |
| §5 Proposition E-SEG (i)-(v) | SIGN | N-KW-3 (precision: (i) as literally counted is off by e(Q); N_cut as a union count keeps (ii)-(iv)) |
| §6 Theorem RUN (a)-(c) | SIGN | N-KW-4 (degenerate r = 1 in (b)'s explicit sum) |
| §7 Corollary KW-S ((K_W), (E), K) | SIGN | N-KW-6 ((E) has no explicit bound in the text; one is written below); addendum units accepted |
| §8 Corollary PHASE (conditional on f only) | SIGN | — |
| §8 READINGs, §9, §10, §11 | not signed (as briefed) | — |
No statement is NOT SIGNED, and no gap is open. No (P).

## 1. W-ONCE (§2): SIGN
- A_{k+1}(v) ⊆ A_k(v): σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) (R15 (d)), so Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v); a gate target z ≠ σ_{k+1}(v) at k + 1 has
  Ξ_k(z) = Ξ_{k+1}(z) ▷ Ξ_{k+1}(σ_{k+1} v) = Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v), so z ≠ σ_k(v) is a gate target at k. ✓
- W_{k+1} = Opt(H_k), W_{k+2} = Opt(H_{k+1}) (τ is the same at k, k + 1, k + 2 inside a phase). σ_{k+1} ∈ H_{k+1} ⊆ H_k gives both
  inequalities. A step with Iσ = ∅ has the trivial arena {σ}, which is its own optimum, so the lemma also covers it. ✓
- W-ONCE′ is the contrapositive inside one phase. ✓
- N-KW-1 (citation): "the S4a result is the pointwise optimum of its one-player arena in G_τ" is R18 (d) Lemma S (c) (as P-N5-FBW §0 cites
  it) together with R17 (F1); the dependency table names only R17 (F1). Nothing changes.

## 2. Facts A0, A, B (§3): SIGN
- A0: only o has an Odd choice, so v's honest play and W-play follow σ and the forced edges along π_v until they reach o or stop at their
  cycle node. (V1) iterates along that prefix. The ¬H1, c_θ ≠ o case: π_v after c_θ is c_θ's honest arc c_θ → … → o of C_Θ (the
  (σ, τ) and honest successors agree off o), and the arc o → … → c_θ avoids π_v (a meeting point q ≠ o would lie on the arc c_θ → o,
  disjoint from o → c_θ). The terminals θ and (c_θ, ∅, 0) are stretch constants (θ by definition, c_θ by the phase). ✓ W frame alike.
- Fact A: under H1, P(θ) ⊆ F ∪ {o} is disjoint from π_v; under ¬H1, c_θ ≠ o, P(Ξ v) = π_v ∩ V_{>c_θ} because π_v after c_θ and the arc lie
  on C_Θ below c_θ; c_θ = o gives π_v ∩ V_{>o}. m* ⪰ c_θ, c_w. C_Ξ, C_W are constant: H1, H2 are constant on the stretch (TC (i), R
  constant). ✓ (For v = o, P(θ) ∩ V_{>m*} = C_Ξ in both regimes.)
- Fact B: in each frame the cycle node is common (c_θ, resp. c_w), the constant parts are common and disjoint, and the top of the path-set
  difference is the top t of κ(π_y) Δ κ(π_z) (every other differing vertex is ranked ≤ m*, below t). Path sets differ, so lengths never
  decide. ✓

## 3. FRZ-U (§3): SIGN
- (MON): WM at the run's non-fallback in-phase transitions; both values have cycle node c_w (A0); (C1) at level rank(m*); C_W cancels. ✓
- Claim P^c, Case A: transitivity of ⪯ (a total order on sets), x ∉ ρ′ and x ∉ π_a (π_x = x·π_a simple), then (MON). ✓
- Case B: x is Even (an Odd x ≠ o has a = z). κ(π_z) ≠ κ(π_a), so Fact B makes (x, z) a gate and σ̂ = σ_k[x ↦ z] an arena strategy;
  W_{k+1}(x) ⊵ val_σ̂(x) (S4a optimum).
  - B1: z's play (π_z, o, then F under H2 or C_W under ¬H2) avoids x, so val_σ̂(x) = x ⊕ W_k(z); COARSE_{m*} and (A-W) at k + 1
    (x ∈ R_{k+1} = R) give the claim. ✓
  - B2: π_z = (z … before x) ⊔ {x} ⊔ π_a, so Z := {x} ∪ (z … before x) is the σ̂-cycle from x; κ(Z) ≠ ∅ with an even top t, which is
    Z's top. reward(t) > reward(c_w), but x ∈ R_{k+1} has W cycle node c_w (A0 at k + 1, w constant): contradiction. ✓
  - B3: π_x ⊆ C_W, so κ(π_a) = ∅ (C_W ⪯ c_w ⪯ m*); π_z avoids C_W's arc from o to x (a meeting point q on it would carry π_z through x);
    so Z = x · π_z · (arc o … before x) is a simple cycle with top t ∉ C_W, the same contradiction. ✓
  - The three subcases are exhaustive (x ∈ π_z; x ∉ π_z with H2 or x ∉ C_W; ¬H2, x ∈ C_W, x ∉ π_z). ✓
- Closing: π_x^t ∪ {o} is a simple G_τ-path in R with ≤ r − 1 edges, so Claim P^c at k0 + r − 1 and (MON) give equality. ✓
- The Lead's "weak step" (FRZ-U's transfer of R20 CR): the packet does not transfer CR; it proves FRZ-U in full, and I checked that proof
  on its own. Nothing is inherited from CR.

## 4. LEN (§4): SIGN
- m* = c_θ: under H1, P(θ) ⊆ V_{>c_θ} (path sets lie above their cycle node), so the whole P(Ξ v) is κ(π_v) ⊔ C_Ξ; under ¬H1 it is κ(π_v).
  FRZ-U freezes it after f0; the cycle node is c_θ; Ξ is ⊵-monotone (R15 (a)); so only the length moves, monotonically, among ≤ r − 1
  values: ≤ r − 2 changes per v ∉ {o, c_θ}. Counts: (r − 1) before f0 plus (r − 1)(r − 2) after. ✓
- m* = c_w ≻ c_θ: the same in the W frame, with WM. The W-flat segment count after f0 is ≤ (r − 1)(r − 2) + 1. ✓

## 5. c_w ≻ c_θ: PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, E-SEG (§5): SIGN
- PAR: XW, distinct cycle nodes, injective rewards; both parities of c_θ contradict an odd c_w. ✓
- H-PATH: c_w ∉ C_Θ (c_θ tops it); after c_θ, π_v runs along C_Θ; P(θ) ⊆ F ∪ {o} ∌ c_w. ✓
- KIND-MONO: after f0, P(Ξ v) ∩ V_{>c_w} is frozen (FRZ-U, m* = c_w); a kind change makes c_w the top difference (H-PATH); Ξ rises
  (R15 (a)) with cycle node c_θ, so the new set contains c_w iff c_w is even, which PAR gives: B → A only, once. ✓
- CASC-B (the Lead's second weak step): P-N5-U23 §2 step 2 (kind B) uses event-freeness only through step 1 (kinds constant): its tied-
  successor case split ("kind A would be an event") is CASC-B's "would change v's kind", excluded by Γ's hypothesis. The honest values
  of kind-B vertices are route functions of kind-B routes with constant terminals (A0), so c_w's and kind-A switches do not enter them.
  The keys: the root-first sequence from c_w is (A1 part, o) followed by the route; A1 may change between steps (kind-A re-routings;
  c_w's switches change A2, not A1), but at one step the prefix is common to all kind-B candidates, so the order among them is decided
  by the route parts. Levels |π_v| are constant on Γ (W(v) = π_v ⊕ w, w constant, W-flat). The induction (U23 §1 step 4 / R24 CASC step
  3) then goes through verbatim. ✓ The transfer is sound.
- CW-INT: σ(c_w) of kind A would put c_w on a cycle avoiding o (c_w ∈ R constant). Kind-B values are constant on [t1, t2]. Each c_w
  switch moves to a strictly better gate target (R15 (d)) among those constant values, so the successors are distinct. ✓
  - N-KW-2 (wording): when A2 = ∅, σ(c_w) = o, which has no kind; its value θ is constant on the stretch, so steps 1-4 hold with
    "kind B or o".
- E-SEG (ii)-(v): CW-INT on the ≤ N_cut + 1 cut-free gaps; events ⊆ kind-change ∪ c_w-switch transitions; R26 (c) (iii) per maximal
  event-free sub-run (a part of Q inside one such sub-run has ≤ 2r − 4 switching transitions even when the sub-run starts before Q);
  KIND-MONO for (v) (o and c_w never change kind; r − 2 vertices remain). The arithmetic in (iii) holds with slack Δ·e(Q). ✓
- N-KW-3 (precision, E-SEG (i)): "N_B(Q) counts the transitions of Q with a kind-B switch", but CASC-B is applied only on the
  kind-change-free parts, and every kind-change transition contains a kind-B switch (a B → A change needs a kind-B vertex to switch to a
  kind-A target). As literally defined, N_B(Q) ≤ (e(Q) + 1)(r − 2) + e(Q). The proof gives (i) for the kind-B-switch transitions OUTSIDE
  the kind-change transitions. (ii) then needs N_cut(Q) := the number of cut transitions (kind change or kind-B switch, counted once),
  which is ≤ e(Q) + (e(Q) + 1)(r − 2) = (e(Q) + 1)(r − 1) − 1, so (ii)-(iv) stand as stated. The fixes file should define N_B(Q) as the
  kind-B-switch transitions without a kind change, or N_cut as the union count. Nothing downstream changes.

## 6. Theorem RUN (§6): SIGN
- (S1): Ξ on R \ {o} is a function of σ along routes and of θ, c_θ (A0); Ξ(o) = θ. So a Ξ-change on R needs a switch at an R-vertex. ✓
- (a) LEN-Ξ. (b) LEN-W plus: a stretch with both frames in route form lies in one PIECE (H1, H2 constant by TC (i); c_θ by the phase;
  c_w = o decided by w); R24 (c) CASC is stated for W-flat runs "with W unchanged on R", the same notion as the packet's segments, so a
  segment has ≤ r − 2 switching transitions (its steps are a contiguous part of one CASC run); the U2 case is R26 (a). (c) E-SEG with
  Σ_Q (e(Q) + 1) ≤ r², (Δr + 1)(2r − 3) ≤ 2Δr². The U3 / U23 split (honest frame in route form or not) is exhaustive under ¬H2,
  c_w ≠ o. ✓
- N-KW-4 (precision): (b)'s explicit sum (r − 1)² + ((r − 1)(r − 2) + 1)(r − 2) is −1 at r = 1 (R = {o}), where the true count is 0. The
  stated bound r³ is right. Seen once in data (s_elim24_final.pg, run 2, case (b) with r = 1; my checker first flagged "0 > −1"). Use
  max(0, ·) or "≤ r³".

## 7. KW-S and the addendum (§7): SIGN
- (K_W): per run, m* = c_w by LEN-W; m* = c_θ by W-ONCE′ inside a run (no fallback between two run transitions), with Ξ-changing run
  transitions ≤ (r − 1)² on R and ≤ |F| − 1 on F (F1° on the crossing-free interval containing the stretch, a fortiori per run). ✓
- K: wakes (R27 setting) are relevant Even switches, so K_t ≤ T_rel; the addendum's K_s ≤ n_E·K_t is right (one switch per Even vertex per
  transition). The addendum's unit reading matches R26 (b), (d) ("non-fallback transitions with a W-change on R"; "E transitions
  containing an event") and P-N5-LP §3's K. Accepted.
- N-KW-6 (wording, (E)): "(E) per W-flat run … polynomial, by E-SEG and KIND-MONO" gives no number. From the packet: the events of a
  run S (c_w ≻ c_θ, ¬H2, c_w ≠ o) number ≤ (r − 1) + Σ_Q E(Q) ≤ (r − 1) + r²(Δr + 1), so per W-flat run as well. The fixes file could state it.

## 8. Corollary PHASE (§8): SIGN (conditional on f only, as labelled)
- Step 1 is Theorem LP (R27 (d)), as signed: T ≤ (m − n + 1)(T_rel + 1).
- Step 2: a relevant transition has a relevant σ̄(o) change (S_o; on 𝒞^1O no other Odd vertex changes) or a relevant Even switch with
  λ(y) ≠ y, which raises Ξ(y) strictly by (SG). ✓
- Steps 3-5: each transition is a fallback, a stretch boundary or a run transition (over-counting a fallback that is also a boundary is
  harmless); runs ≤ N_st + f; Ξ-changes on F ≤ (X + 1)(n − 1) by F1° per crossing-free interval; on R ≤ 3Δn⁴ per run. ✓
- The cited bounds match their landed texts: X ≤ (f + 1)(n − 1) + f + X_SN (R30 (c) SN-PREFIX), X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T with
  T ≤ n² + 2n − 1 (R34 (e), (f)); Θ (R27 (g) TH, for λ_Ξ(o) ≠ o; Θ = 0 at c_θ = o since θ = (o, ∅, 0)); S_o ≤ d_o(Θ + 1) (R27 (g) SO;
  at c_θ = o there is no relevant σ̄(o) change, so S_o = 0); W_ch per interval by R24 (e) WC under ¬H2 (it covers c_w = o too), by F1° under
  H2 (w = o ⊕ Ξ(τ o), τ(o) ∈ F). The O-forms follow. ✓
- The READINGs (with FB-POLY and Φ-1O) are not signed; G-N5-TIME stays OPEN.

## 9. Data (DATA, not proof; own code)
- Checks per trace (kw_check.py header): W-ONCE, A0, Fact A (both frames), Fact B (all pairs), MON, FRZ-U, LEN, PAR, H-PATH, KIND-MONO,
  CASC-B, CW-INT, E-SEG (i′), (ii)-(v), RUN (a)-(c), KW-S per stretch, and PHASE's inequalities per phase (LP, T_rel, N_Ξ, N_st, X, X_SN,
  W_ch, S_o).
- Batch: 503 files × 3 starts × own / spec / rand = 4,527 runs; 24,082 / 24,395 / 23,342 states; 6,269 / 6,280 / 6,285 phases; 19,610 /
  19,671 / 18,911 stretches; 1,487 / 1,530 / 1,475 runs of stretches (case a / b / c: 1,250 / 194 / 43 own); A0 276,949 / 282,216 /
  269,059; Fact B 1.90 M / 1.90 M / 1.85 M pairs; H-PATH 12,719 / 14,170 / 11,640; PAR 3,093 / 3,206 / 3,097 states with c_w ≻ c_θ (all
  even). 0 violations, 0 nonzero exits (totals_logs.txt), after the r = 1 fix of N-KW-4 (one file re-run in all three traces).
- Thin in the batch: W-ONCE's hypothesis (Ξ_{k+1} = Ξ_k at an S4a step followed by another) 0 / 8 / 2; KIND-MONO runs 4 / 4 / 5; CW-INT
  3 / 0 / 8 c_w switches; no kind-B switch inside a W-flat segment (CASC-B vacuous in the batch); no E-SEG segment after f0; no post-freeze
  kind change or c_w switch. Climbs (§10) aim at these.
- N-KW-5 (DATA): the packet's §10 says "the largest observed freeze delay is 1 transition". On my engine κ above m* changes as late as run
  step 39 on experiments/red/xing/instances/kw_n48.pg (sha1 9b051da6, L-RED 97654ed9, 00:43Z, before the packet; S3 start, one
  fallback-free run of 39 transitions, r = 48, m* rank 45), and ≥ 2 in 91 of 503 files (own trace). FRZ-U's index r − 1 = 47 is never
  exceeded (FRZ-U holds), but the lane's sentence does not match my measurement; perhaps it measures something else. Not a gap.
- Mutations: see §10.

## 10. Climbs and mutations
Climbs (kw_climb.py, 1,200 s each, 22:39Z-22:59Z by date -u; an earlier set, 22:2xZ, was discarded: it stopped on the N-KW-4 checker
artifact before my fix). Each evaluation runs kw_check on 4 runs (S3 and a random pair in the own trace, two random pairs in the rand
trace; seeds are inputs only). Totals from climb/*.txt:

| climb | seed game | evaluations | runs (a / b / c) | c_w ≻ c_θ, ¬H2 runs | kind changes (c_w ≻ c_θ) | c_w switches (c_w ≻ c_θ) | kind-B W-flat switches | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| kw 13001 | kw15/climb/best_kind3_1541.pg | 26,839 | 60,825 / 456 / 48,236 | 48,236 | 238,518 | 5,093 | 9 | 0 |
| kw 13002 | kw15/climb/best_kind2_1521.pg | 83,354 | 99,437 / 272 / 154,365 | 154,365 | 457,303 | 92,262 | 0 | 0 |
| casc 13003 | kw15/climb/best_long_1513.pg | 6,612 | 24,873 / 13 / 6,533 | 6,533 | 53,650 | 3 | 0 | 0 |
| kw 13004 | random n 10-18 | 43,358 | 71,007 / 369 / 79,343 | 79,343 | 403,278 | 60,219 | 1 | 0 |

- 0 violations in 160,163 evaluations (640,652 runs). W-ONCE's hypothesis 571 times, CW-INT 324 c_w switches between cuts, KIND-MONO 160
  runs, RUN case (b) at r = 1 6 times (counted under r³).
- VACUOUS IN MY DATA TOO (as the packet's §10 says): no post-freeze kind change and no post-freeze c_w switch (counters
  RECORD_*_after_freeze_cw_above = 0 in every climb and the batch), although 1.15 M kind changes and 157,577 c_w switches with c_w ≻ c_θ,
  ¬H2 occur BEFORE the freeze index. So KIND-MONO's and CW-INT's post-freeze uses and E-SEG (no segment after f0 occurred) rest on the
  proofs, which I checked line by line (§5).
- CASC-B is exercised: 10 kind-B switches inside kind-change-free W-flat segments, the latest at step exactly |π_v| − 2 (slack 0), never
  later. Those evaluations were not saved (pre-patch dump). Two later 600 s climbs (casc 13011, kw 13012, 23:10Z-23:20Z, the patched
  dump) saved witnesses: climb/witness_cascb_13011.pg (sha1 eaba4e37) and witness_cascb_13012.pg (59641419), each with the start pairs
  evaluate() ran in its .txt; the switch is in a rand-trace run, so it reproduces through evaluate(g, o, fit, seed) (13011 casc / 13012 kw):
  one kind-B switch each, slack 1, 0 violations. Neither shows in the own or spec trace from the saved pairs.
- Mutations (logs_mut/, own trace, whole list): frz0 (freeze index k0 instead of k0 + r − 1) FIRES (2,668 lines; first fl_n16_y4.pg run 0,
  FRZ-U at state 1, x 18, r 7); par (PAR demands c_w odd) FIRES (2,745); casc (CASC-B bound |π_v| − 3) does not fire on the list, which has
  no kind-B W-flat switch, nor on the two saved witnesses (slack 1, so the tightened bound still holds there). The slack-0 cases
  above would make it fire, but none was saved; CASC-B's bound is shown to be reached, not shown necessary, by saved data.
- Random games: kw_check.py random 3000 6 16 13100 own: 3,000 runs, 7,614 states, 0 violations.

## 11. Summary
All statements to sign: SIGN, no gap. Notes N-KW-1 (citation, R18 (d) S (c)), N-KW-2 (σ(c_w) may be o), N-KW-3 (E-SEG (i)'s literal count
is off by e(Q); N_cut as a union count), N-KW-4 (RUN (b)'s explicit sum at r = 1), N-KW-5 (DATA: freeze delay up to 39), N-KW-6 ((E)'s
explicit bound). None changes a statement's truth.

## §C. Comparison with REFEREE: docs/referee/R-N5-KW.md (REFEREE successor 11; report referee 56ac6538, Addendum 1 1d6cbf32; sha1 038bc8c9 on my tree at 84b57e9c)
REFEREE-2 successor 12, written 2026-10-25 23:4xZ (date -u). Opened at the Lead's word (23:28Z), after my report (8a47fd92) was pushed. (Opus 5.5, D15)
- C.1 Verdicts: identical in substance. Both sign W-ONCE (+′), A0 / A / B, FRZ-U, LEN, PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, RUN, KW-S
  and PHASE (conditional on f). On E-SEG REFEREE writes SIGNED WITH GAP KW-1, I wrote SIGN with N-KW-3: the same defect.
- C.2 KW-1 vs N-KW-3: SAME finding, same repair. REFEREE: (i) "as written … unproved; the proof gives N_B(Q) ≤ e(Q) + (e(Q) + 1)(r − 2)";
  repair N_B without kind changes, or N_cut := #transitions with a kind change or a kind-B switch, then N_cut ≤ (e + 1)(r − 1) and
  (ii)-(iv), RUN (c) unchanged. Mine: the identical bound and the same two repairs. The label: (i) as literally stated is a statement
  the proof does not give, so I ACCEPT REFEREE's "SIGNED WITH GAP KW-1, closed by the one-line repair" as the joint form; with the
  fixes-file line, E-SEG is signed by both without a gap. My E-SEG (i′) checks were of the repaired form; REFEREE also checked the literal
  (i) on 293,621 post-freeze segments (vacuous for KW-1's case, as in my data).
- C.3 Notes:
  - KW-N1 (PHASE W_ch: c_w = o vs c_w ≠ o is not fixed on a ¬H2 interval; cite R24 (e) WC for every ¬H2 interval): ACCEPTED. I reached
    the same reading in §8 ("WC … covers c_w = o too") but did not flag the packet's sentence; it is a wording line.
  - KW-N2 (LEN: the length range is the whole length to the cycle node, in [1, r − 1]): ACCEPTED (wording; my §4 used the same range).
  - KW-N3 = my N-KW-4 (RUN (b) at r = 1). Same.
  - KW-N4 = my N-KW-6 ((E) explicit). REFEREE's (r − 1) + (Δr + 1)(r − 1)² uses E-SEG (iii) with Σ_Q (e(Q) + 1) bounded via (v) per
    segment count; mine, (r − 1) + r²(Δr + 1), is the cruder Σ_Q (e + 1) ≤ r². Both valid; REFEREE's is sharper. Take REFEREE's.
  - KW-N5 = my N-KW-5 (freeze delay). REFEREE explains the packet's §10 line: it is the max over runs that REACH k0 + r − 1 (lane
    kwcheck.py l. 60-68); over all runs the delay reaches the run length (kw_n48: 40 / 40 transitions, r 48). My 39 on kw_n48 is the same
    run measured to the last change (transition index vs. state). ACCEPTED: the lane's sentence is true for its measure; the fixes file
    should name the measure.
  - My N-KW-1 (citation of R18 (d) S (c)) and N-KW-2 (σ(c_w) may be o) have no REFEREE counterpart; both are wording and stand.
- C.4 Addendum 1, REFEREE's CASC-B witness docs/referee/scratch/kw_logs/cascb_witness.pg (sha1 3bda89ce), S3 start, re-run on my tracer:
  - spec trace (re_check.n5_spec, SPEC S1-S5): CASC-B exercised, one kind-B switch in a kind-change-free W-flat segment of a case (c) run,
    at step 0 against the bound 1 (slack 1), 0 violations; o = 2, θ = (2, ∅, 0), w = (14, ∅, 2), ¬H2, c_w = 14 ≻ c_θ = o: REFEREE's U3
    stretch. REPRODUCED.
  - own trace (my S4a tie-breaks): the same game falls back already at state 0, so the run differs and has no such switch; not a
    contradiction (S4a's optimum is not unique; the spec trace is the reference).
  - This is the first deterministic, start-pair-free CASC-B instance in my data (my climb witnesses witness_cascb_13011/13012 need the
    climb's evaluate()). It confirms REFEREE's point that CASC-B's content is exercised; my 10 + 2 climb switches agree.
- Joint note map (one fixes-file line each): KW-1 = N-KW-3 (E-SEG (i): N_cut as the union count); KW-N1 (W_ch via WC on every ¬H2
  interval); KW-N2 (LEN range); KW-N3 = N-KW-4 (RUN at r = 1); KW-N4 = N-KW-6 ((E), REFEREE's form); KW-N5 = N-KW-5 (name the freeze-delay
  measure); N-KW-1 (citation), N-KW-2 (σ(c_w) may be o). Vacuous for both: post-freeze kind changes (KIND-MONO after f0). No disagreement
  remains. No verdict of mine changes. (Opus 5.5, D15)
