# R-N5-CUT: REFEREE report on packet P-N5-CUT (L-SI box 43): N5's iteration count reduced to boundaries, repeat late adoptions, silent / own-cycle re-entries and Odd switches
Referee: REFEREE (successor 19), Opus 5.5 (owner ruling D15). Lead brief 2026-10-30 01:11Z (date -u). REFEREE-2 successor 21 reviews in parallel.
- Object and pin: docs/si/P-N5-CUT-box43.md at claude/l-si 2678f6c6a, `git show 2678f6c6:docs/si/P-N5-CUT-box43.md | sha1sum` =
  d6519d3d72d67d25bafd21b7034092eaa4315457 (221 lines), equal to the Lead's figure; unchanged at origin/claude/l-si f5f9a8c4 (same sha1).
  Fixes go to docs/si/P-N5-CUT-fixes-box43.md; the packet stays frozen.
- Runs 2026-10-30T01:13Z-01:30Z; report written 01:30Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ file opened.
- Premises opened: SPEC docs/new/N5-ssi-global.md at 7039eb524 (S1 l. 26-46: rank and p′ injective, so reward is injective; S2-S5
  l. 47-60: S4a and S4b are computed from the SAME (σ, τ) and applied together, S4d); RESULTS (this branch after the trunk merge): R15 (d), R17 (a)
  (F1), R47 (a) Lemma Φ, R57 (a) (VJ), R86, R88, R89 (landed, CHECKER C99); R89's object docs/new/P-N5-FRAME-box65.md at 938d87967 (sha1
  ce8c4803…, re-verified): §1 (τ-stretch, W-run, l. 68-71), §3.3 GP*-RUN, §3.5 STRETCH-RED's λ_W item (l. 170-172); the tool quotes at
  experiments/new/box64/late.py@9905dac36.
- Quotes: my own script (scratch/cut_quotes.py; fragments split at "…", whitespace normalised) finds 13/13 verbatim. The [SR-λ] quote elides
  the bound itself; the source line 171-172 carries it: «rewards are injective, so each vertex's W-cycle node changes at most n − 1 times per
  piece: at most n(n − 1) λ_W-changing transitions per piece». So the "Used for" reading is the source's own statement.
- Scope (D1): a REDUCTION of N5's iteration count on every game to four counts B*, REP*, SC*, O*, none bounded. Nothing bounds N5's iteration
  count; G-N5-TIME stays OPEN. Not a TARGET.md claim, not M3, not a step-4 pass.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, quotes, symbols, Fact B, τ*-piece, leave / re-entry / span | CHECKED (Fact B re-derived from S4a-S4d and R15 (d), §1 below) |
| 2 | Lemma OPT-OFF (i) | SIGNED; standing premise CUT-N1 (R17 (a) (F1) with R57 (a) (VJ)) |
| 2 | Lemma OPT-OFF (ii) | SIGNED (Cases 1-3 re-derived, exhaustive; §2) |
| 2 | Lemma W-MON′ | SIGNED |
| 2 | Lemma W-SUCC | SIGNED |
| 3 | Lemma W-RETURN-G | SIGNED (every link's step and frame checked, §3) |
| 4 | Corollary CUT-CHARGE (ENT bound; FC ≤ B_R) and its Remark (#FR ≤ 1 per τ*-piece and pair) | SIGNED (§4) |
| 5 | Lemma FRESH-SPLIT and its ENT bound | SIGNED (not used by §8) |
| 6 | Lemma LATE-SPLIT (i)-(iii), its Consequence, Corollary R*-REP | SIGNED |
| 7 | Lemma WV-R | SIGNED (W-runs inside Q = pieces of Q between λ_W-cuts, §7) |
| 8 | Theorem CUT-RED | SIGNED (bookkeeping and each sum re-derived, §8) |
| 8 | Corollary CUT-POLY (the conditional) | SIGNED as an implication; its "about …" order is an upper estimate (CUT-N5) |
| 8 | "Notes on the premises" | READING, not signed; the [P-REP] note is STALE: REP-LIN is DEAD (L-RED R128), CUT-N3 |
| 9 | READING, DATA | not signed; pinned blocks «box 40», «box 42», «box 43» reproduced EXACTLY (§9) |
| — | RESULTS line | NONE in the packet or on any branch at 01:2xZ; not checked. Symbol list a line must carry: §10 |
No gap. Nothing FALSE. Notes CUT-N1..N7. The packet does not depend on CONJECTURE REP-LIN (dead): REP* is a premise; no proof step of §2-§8
uses a bound on REP (checked line by line); REP-LIN appears only in the unsigned §8 notes.

## 1. Setting and Fact B
- Fact B ✓. S4 computes S4a and S4b from the same (σ_t, τ_t) and S4d applies both. A non-fallback transition with σ_{t+1} ≠ σ_t has
  σ_{t+1} = S4a's σ_new with Iσ_t ≠ ∅: an S4a step (τ free). A non-fallback transition with σ_{t+1} = σ_t changes τ (R15 (d)). An S4c
  transition with Iσ_t ≠ ∅ sets only σ (τ_new = τ, by S4c's precondition): an Even fallback; with Iσ_t = ∅ it sets only τ: a τ-change. So every
  transition is an S4a step with τ kept, or a boundary. ✓ (My data: 0 transitions outside these classes, FACTB.)
- τ*-piece: the maximal intervals are well defined (a union of overlapping such intervals is one); every state lies in exactly one. A
  transition between two consecutive pieces is not "S4a with τ kept", hence a boundary (used by §4 FC and §8).
- The frame convention W^τ_t (σ_t against a fixed τ) is used consistently: at an S4a step t → t + 1 every comparison is in the frame τ_t,
  including the state t + 1 when τ_{t+1} ≠ τ_t. My probe computes W[t] = val(σ_t, τ_t) and Wn[t] = val(σ_{t+1}, τ_t) separately.

## 2. OPT-OFF, W-MON′, W-SUCC
- (i) ✓. In A = G_{τ*} restricted to H_t, Odd has out-degree 1; in the dual of H (the arena S4a evaluates) the G-Even vertices are the
  optimiser, and S4a's σ_new is S1's optimal counterstrategy there, minimising the G^d order at every vertex at once; DUAL-ORDER (R89 §2.2,
  signed) turns that into maximising G's order at every vertex among positional Even strategies inside H_t. That S1's procedure does return a
  pointwise optimum is R17 (a) (F1) (the optimum of a one-player game dominates every strategy pointwise) with R57 (a) (VJ) (S1's Ξ is VJ00's
  Ω); the packet cites only [S1-Xi] + [DO] (CUT-N1; R88's W-MON, the τ-kept case, cites [R17-F1] on H_t for the same step).
- (ii) ✓. ext(v, (c, P, ℓ)) := (c, P ∪ {v if rank(v) > rank(c)}, ℓ + 1). For two triples with the same cycle node and v ∉ P, ext adds the same
  term to both signed weights and 1 to both lengths: it preserves and reflects ⊴; for different cycle nodes the order is decided by the
  rewards, which ext keeps and which are injective (SPEC S1: rank injective, p′ = 2·rank + parity). (Implicit in the packet: CUT-N2.)
  - Case 1 (v not on y's σ′-play): σ″ := σ′[v → y] is a positional Even strategy inside H_t; its play from v is v then y's σ′-play, so
    W″(v) = ext(v, W(y)); (i) gives W″(v) ⊴ W(v) = ext(v, W(σ′ v)); reflection gives W(y) ⊴ W(σ′ v). ✓
  - Case 2 (v on y's play before its cycle node c, which includes v on the cycle before c): W(y) = (c, D ⊔ P(σ′ v), ℓ_y) with D := the
    vertices of the segment y … v (v included) above c, ℓ_y > ℓ(σ′ v). σ″ closes C = segment y … v. D ≠ ∅ with even top x: x is C's top,
    rank(x) > rank(c), reward(x) > reward(c) whatever c's parity: W″(v) ▷ W(v), against (i). D's top odd: the top's 2^rank dominates the
    other (distinct) ranks of D, so D's signed weight is negative: W(y) ◁ W(σ′ v). D = ∅, c even: same P, longer: ◁. D = ∅, c odd: C lies
    below c (c ∉ segment), its top t has rank < rank(c) and reward(t) > −p′(c) = reward(c): against (i). ✓
  - Case 3 (v on y's cycle after c): σ′ v runs along the cycle to c, all cycle vertices are below c, so P(σ′ v) = ∅ and CN(y) = c. C =
    y's path, the cycle from its entry to c, on to v. P(y) = ∅: C's top is c and W″(v) = (c, ∅, ℓ_y + 1) = ext(v, W(y)) by direct count (v
    is below c, so not added); then reflection as in Case 1 (ext is applied as an operation on triples with v ∉ P(y); the packet's
    "whose plays avoid v" is not literally true here, the triple identity is: CUT-N2). P(y) ≠ ∅: C's top is P(y)'s top x (rank > c); x even
    gives W″(v) ▷ W(v), against (i); x odd gives weight(P(y)) < 0 = weight(∅): W(y) ◁ W(σ′ v). ✓
  - Exhaustive: v on y's play lies on the part before c (Case 2) or on the cycle after c (Case 3); v = c is excluded by off-cycle. y = v and
    y = σ′ v fall into these cases and the claim holds there too. ✓
  - Necessity of off-cycle: MUT 1 (premise dropped) gives 249 violations on the corpus (n ≤ 40), incl. tog6b_n32 vertex 13 at t = 2 → 3,
    y = 21 (the packet's instance) and also at t = 0 → 1 (y = 4, 15).
- W-MON′ ✓: σ_t ⊆ H_t is one of the strategies of (i). Data: 545,448 vertex checks, 1,568 of them at τ-changing S4a steps (WMONX), 0
  violations. MUT 5 (the same comparison in the NEW frame τ_{t+1} at τ-changing S4a steps): 22 violations — the old-τ frame is essential.
- W-SUCC ✓: each step of [q, p] is an S4a step with τ = τ*; (ii) is applied at t → t + 1 with v off-cycle at t + 1 ∈ [q + 1, p] and
  (v, σ_t v) ∈ σ_t ⊆ H_t; W-MON′ for the other link.

## 3. W-RETURN-G
Each link re-derived with its frame: q − 1 ∈ [a, j − 2] and j − 1 ≤ b, so q − 1 → q, …, j − 2 → j − 1 are transitions inside the piece
(S4a steps, τ = τ*), and j − 1 → j is an S4a step whose arena H_{j−1} and frame are τ_{j−1} = τ*.
- W*_q(c) ⊴ W*_q(σ_q v): (ii) at q − 1 → q, (v, c) ∈ H_{q−1} (anchor), v off-cycle at q ✓.
- ⊴ W*_{j−1}(σ_{j−1} v): W-SUCC on [q, j − 1] (off-cycle on [q + 1, j − 1]) ✓. ⊴ W*_j(σ_{j−1} v): W-MON′ at j − 1 → j ✓.
- ⊴ W*_j(c) = W*_j(σ_j v): (ii) at j − 1 → j, (v, σ_{j−1} v) ∈ H_{j−1}, v off-cycle at j ✓. W*_q(c) = W*_j(c) by hypothesis: all equal. ✓
- The anchor's lower bound s is not used by the proof (it is used by §4's window disjointness). MUT 2 (anchor allowed before the piece, i.e.
  across a cut, read with W[t] there): 313 violations on the corpus (16 on rise_thin51_n40 = the lane's MUT=nofresh 16, independently).

## 4. CUT-CHARGE
- The class of every re-entry is well defined: j − 1 → j changes σ(v), so it is an S4a step or an Even fallback (Fact B) ✓. F / FR / C / P / S
  partition (F first; then anchor or not; with the smallest anchor q: own-cycle somewhere on [q, j], else W*(c) changes, else S) ✓.
- ENT ≤ 1 + #F + #FR + #C + #P + #S (every entry after the first in R has an earlier leave in R) ✓. S re-entries are W-silent by §3 ✓.
- #P ≤ WCH*: the changing transition t → t + 1 has q ≤ t ≤ j − 1, q ≥ a + 1, so t ∈ [a, b], τ_t = τ*, and W^{τ_t}_{t+1}(c) = W*_{t+1}(c) ≠
  W*_t(c) = W^{τ_t}_t(c) (for t = j − 1, W*_j = W^{τ_{j−1}}_j); t ∈ [s + 1, j − 1] lies in span(v, c); windows [s + 1, j] of distinct
  re-entries are disjoint ✓.
- FC ≤ B_R: F uses its own transition j − 1 → j. FR: if a ≤ s then q − 1 := s is an anchor (σ_s v = c ∈ H_s, s ≤ j − 2), so a ≥ s + 1 and
  a − 1 → a (start index a − 1 ∈ [s, j − 2]) is a boundary (the piece is maximal; Fact B), inside R since s ∈ R. The start indices used lie
  in [s, j − 1]; for consecutive re-entries s′ ≥ j, so these ranges are disjoint ✓ (the packet's "inside [s, j − 1]" is exactly this).
- Remark ✓: a later re-entry j′ in the same piece has its leave s′ ≥ j > a, and q′ − 1 := s′ is an anchor.
- MUT 4 (FC := #F, FR re-entries uncharged): 77 violations of the ENT inequality on the corpus. Unmutated: 0 of 16,527 (pair, λ-run) checks.

## 5. FRESH-SPLIT
- The five cases partition ✓. (LATE): j − 2 ≥ a ≥ s + 1 (FR), so q − 1 := j − 2 would be an anchor if (v, c) ∈ H_{j−2}: hence (v, c) ∉
  Iσ_{j−2} (and σ_{j−2} v ≠ c). The chain W*_{j−2}(c) = W*_j(c) ▷ W*_j(σ_{j−1} v) ⊵ W*_{j−1}(σ_{j−1} v) (W-MON′) ⊵ W*_{j−1}(σ_{j−2} v) ((ii)
  at j − 2 → j − 1, inside the piece, v off-cycle at j − 1) ⊵ W*_{j−2}(σ_{j−2} v) (W-MON′) ✓; τ_{j−2} = τ*, so it is BLOCKED at j − 2 in
  R88's sense ✓. ENT bound: F + FR = F + WC + G0 + CY + LATE + SAME, WC windows ⊆ [a, j] ⊆ [s + 1, j], so WC + P ≤ WCH* ✓.
- Data: 573 (LATE) re-entries, every one BLOCKED at j − 2 (FS 0).

## 6. LATE-SPLIT, R*-REP
- F has no fallback and τ constant: its transitions are S4a steps with τ kept (Fact B), W = W^τ on F ✓. (i) ✓.
- (ii) ✓: σ_{u₁+1}(y) = z, σ_{u₂}(y) ≠ z, so some leave k with u₁ < k < u₂; the chain's four links use (ii) at k → k + 1 ((y, z) ∈ σ_k),
  W-SUCC on [k + 1, u₂] (off-cycle on [k + 2, u₂]), W-MON′, (ii) at u₂ → u₂ + 1 (off-cycle at u₂ + 1); u₂ + 1 ∈ F (u₂ → u₂ + 1 is a
  transition of F). Any leave k in (u₁, u₂) works. (iii) ✓ (W-SUCC on [k + 1, t], then BLOCKED at t).
- Consequence ✓: consecutive intervals [k + 1, u₂ + 1] are disjoint (the next leave is > u₂); a W(z)-change in [k + 1, u₂ + 1] is a
  transition t → t + 1 with t ∈ [k + 1, u₂].
- R*-REP ✓: R*_T counts transitions with ≥ 1 late adoption ≤ late adoptions = FIRST + REPEAT ≤ m_E + REP_F. ([GPR]'s and R88's R*_T: the
  same "transitions of F containing a late adoption".)
- Data: 1,509 late adoptions, 20 REPEAT (n ≤ 120, both starts); every REPEAT off-cycle on its interval and with a W(z)-change; W-silent 0;
  (iii) checked once (the only REPEAT with a blocked state in (k, u₂]). MUT 3 (off-cycle premise of (ii) dropped) NEVER bites: no REPEAT in
  the data has y its own cycle node on its interval (LS_cyc 0). As for (H2) in GATE-SHUT / ODD-FREEZE, the premise is used by the proof and
  its necessity is not exhibited (CUT-N6).

## 7. WV-R
- Q is a τ*-piece; a W-run meeting Q lies inside Q: Q's end transitions are boundaries (an Even fallback, excluded from W-runs, or a τ-change,
  which ends the τ-stretch) ✓ (data: 0 W-runs crossing a piece end). Inside Q the W-runs are the pieces between λ_W-changing transitions,
  at most Λ_Q + 1, each with ≤ (n − 1)(R*_T + 1) W-changing transitions (R89 GP*-RUN, landed), and a per-vertex count is at most that ✓.
- Λ_Q ≤ n(n − 1): Q is a fallback-free piece of a τ-stretch, so the landed R89 STRETCH-RED λ_W item applies verbatim (W-MON′ with τ kept,
  injective rewards) ✓. Data: 55,052 (Q, w) checks, 0 violations, largest ratio WCH_Q(w) / bound = 0.40.

## 8. Theorem CUT-RED, Corollary CUT-POLY
- Bookkeeping ✓: ≤ 2n(n − 1) transitions change λ or λ^U (R47 (a)); every other one has both states in one λ-run R and one λ^U-run R′ and
  changes σ (≥ 1 switch counted in Σ_v SW_R(v)) or τ (one of R′'s τ-changing transitions; a transition changing both is counted twice: an
  upper bound). ≤ n(n − 1) + 1 λ-runs and λ^U-runs. ✓
- Σ_v SW_R(v) = Σ_{(v, c)} ENT_R(v, c) ≤ Σ_{(v, c)} (1 + B_R + WCH*_R(v, c)) + Σ (SIL_R + CYC_R) ≤ m_E(1 + B* + max WCH*) + SC* ✓.
- WCH*_R(v, c) ≤ B_R + (B_R + 1)K ✓: a counted transition is a boundary (≤ B_R, all inside R) or an S4a step with τ kept, which lies inside
  one piece Q and is a W(c)-changing transition of Q (W^{τ_t} = W on Q); the pieces having such a transition in span ⊆ R are separated by
  boundaries of R: ≤ B_R + 1 of them; each ≤ WCH_Q(c) ≤ K(n, m_E, REP*) (WV-R with Λ_Q ≤ n(n − 1), R*_Q ≤ m_E + REP*_Q ≤ m_E + REP*; the bound
  is monotone in Λ and R*) ✓. The formula in §0 / FINDINGS equals §8's (1 + B* + B* = 1 + 2B*) ✓.
- Data: T ≤ the bound and T ≤ the bookkeeping bound 2n(n − 1) + (n(n − 1) + 1)(E* + O*) on all 765 runs (+ 1,200 random runs).
  Largest values seen (n ≤ 120, both starts): B* 61, REP* 2, SC* 31, O* 41, T 172.
- CUT-POLY ✓ as an implication (m_E ≤ n²). It is the iteration half only; the time half needs R57 BIT-G (per-iteration bit cost), as the
  packet's "iteration half" says.

## 9. Pinned checks and data
- Pinned: experiments/si/check.sh l. 796-813 («box 40», «box 42», «box 43») run alone in a clean `git worktree add --detach` at 2678f6c6
  (Oink not needed by these blocks): all three PASS lines printed, exit 0, 1 min 12 s. Includes MUT=nofresh (16) and MUT=off1 (92) firing and
  quotecheck.py 13/0 with --mut failing.
- Own control: docs/referee/scratch/cut_probe.py on rl_engine (my SPEC engine; no lane code), inputs = the lane's sbcg.lst (719 games, files
  at 2678f6c6) plus the given .start where valid; logs in docs/referee/scratch/cut_logs/.
  - n ≤ 120 (671 games, 765 runs, 13,137 transitions): 0 violations of FACTB, OPT1 (78,486 one-edge deviations, every x), OPT2 (492,243),
    WMON, WRETG, CC, FCB, FRREM, FS, LS2, LS3, RREP, LAM, WV, WRUN_CROSS, THM, BOOK.
  - Re-entry classes there: F 912, FR 6,060, C 4, P 4,304, S 42 (C and S equal the lane's 4 and 42; the other counts differ because my set adds
    the given starts and skips 48 games with n > 120; S3-only, all 719 games: F 557, FR 6,031, C 4, P 5,035, S 42 = 11,669, EXACTLY the lane's §9 cuts.py figures; FR split (LATE) 313 = the
    lane's cutsx.py 313; late adoptions 1,141, REPEAT 41, W-silent 0 = the lane's laterep.py 1,141 / 41 / 0; most REPEATs in one run 6 = the
    lane's 6; 0 violations of every check on these 719 runs (11,621 transitions; B* 55, O* 55, SC* 31, T 264)).
  - Pins: fc_3 FR 97 (lane 97); rise_thin51_n40 F 14 / FR 92 / P 19 (lane CUTRE 14 / FRESH 92 / WPAID 19); hntop_n3 with its start: 61
    transitions, 0 late adoptions (lane R* 0).
  - MUT 1 / 2 / 4 / 5 bite (249 / 313 / 77 / 22, n ≤ 40); MUT 3 never (§6). Random n 8-20 with 3 random starts: 1,200 runs, 0 violations
    (short runs, T ≤ 8: weak evidence).

## 10. RESULTS line (none yet): what it must carry
No RESULTS-line proposal exists (packet FINDINGS is a formula; nothing on claude/l-si at f5f9a8c4 or on trunk). A line for this packet must define IN
THE LINE, or cite a landed entry for, every one of: N5 (SPEC S1-S5); W^τ_t (val of (σ_t, τ) on G_τ), W_t, λ_W; H_t; S4a step; boundary (Even
S4c fallback or τ-change); τ*-piece (guided stretch); λ-run, λ^U-run (R86); B_R; leave, re-entry, span(v, c); anchor (with max(s, a) ≤ q − 1 ≤
j − 2 and (v, c) ∈ H_{q−1}); the classes F, FR, C, P, S (smallest anchor; frame τ_{j−1}); ENT_R, SW_R (R86); WCH*_R(v, c) (frame τ_t);
FC_R, SIL_R, CYC_R (§4's, not §6's SIL_F / CYC_F: CUT-N4); W-run (R89); late adoption, BLOCKED (R88 / R89); FIRST, REPEAT, REP_F; R*_T;
WCH_Q, Λ_Q; K(n, m_E, r); B*, REP*, SC*, O*; m_E; T. Scope words: REDUCTION; B*, REP*, SC*, O* not bounded; CONJECTURE REP-LIN DEAD (R128);
G-N5-TIME open; not M3, not a step-4 pass, not a TARGET.md claim. Premises: R15 (d), R17 (a) (F1), R47 (a), R57 (a), R86, R88, R89 (incl.
DUAL-ORDER, GP*-RUN, STRETCH-RED's λ_W item). I check the line symbol by symbol when the Lead pins it.

## Notes (for docs/si/P-N5-CUT-fixes-box43.md; none changes a verdict)
- CUT-N1 (standing premise, citation): OPT-OFF (i) is R17 (a) (F1) on the one-player arena A, with R57 (a) (VJ) that S1's Ξ is VJ00's Ω, plus
  G-N5T-1 (code = SPEC) for every DATA line. The packet cites only [S1-Xi] + [DO]. Same item as SF F7, GP G1, FRAME H1.
- CUT-N2 (implicit facts): OPT-OFF (ii)'s ext step uses injective rewards (SPEC S1) and the top-dominance of signed weights (R84 Fact DELTA);
  in Case 3 the "as in Case 1" step is the triple identity W″(v) = ext(v, W(y)) (y's play contains v there; "plays avoid v" is not literal).
- CUT-N3 (stale READING): §8's "[P-REP]: CONJECTURE REP-LIN (REP_F ≤ n)" — REP-LIN is DEAD (L-RED R128, latew_K20_m32: REP 570 > n 538,
  Θ(n²) per W-run). [P-REP] (REP* ≤ p(n)) is OPEN and is not implied by anything in the packet.
- CUT-N4 (names): SIL_R / CYC_R (§4, re-entry classes in a λ-run, the ones SC* sums) vs SIL_F / CYC_F (§6, REPEAT classes in a W-run, unused
  by §8). A RESULTS line should name only §4's.
- CUT-N5 (order): CUT-POLY's "about n²·m_E·p·n³ m_E p" overestimates: the leading term is n²·m_E·(B* + 1)·K ≈ n²·m_E·p·n³(m_E + p). Harmless
  (an upper estimate, inside "about").
- CUT-N6 (premise not exhibited): LATE-SPLIT (ii)'s off-cycle premise never bites in my data (no REPEAT with y its own cycle node); the
  proof uses it ((ii) of OPT-OFF at k → k + 1 and u₂ → u₂ + 1). OPT-OFF's own off-cycle premise does bite (MUT 1).
- CUT-N7 (DATA reproduced): with the S3 start on all 719 games my engine reproduces every §9 count exactly (classes, LATE 313, late
  adoptions 1,141 / REPEAT 41 / W-silent 0, most REPEATs 6). With the given .start files added the counts differ (F, FR, P), as expected.

## DONE / FINDINGS / NEEDS
- DONE: this report (verdict table, derivations, pinned re-run, own control with 5 MUTs).
- FINDINGS: every PROVED item of P-N5-CUT SIGNED (Opus 5.5, D15); no gap; Theorem CUT-RED holds as stated: T ≤ 2n(n − 1) + (n(n − 1) + 1)
  (m_E[1 + 2B* + (B* + 1)K(n, m_E, REP*)] + SC* + O*); a REDUCTION, the four counts unbounded; G-N5-TIME OPEN. Notes CUT-N1..N7.
- NEEDS: Lead: the RESULTS-line proposal (path@commit) for a symbol-by-symbol check; the §C word after REFEREE-2's report.
