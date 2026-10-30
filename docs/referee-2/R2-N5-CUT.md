# R2-N5-CUT: REFEREE-2 report on packet P-N5-CUT (L-SI box 43): N5's iteration count reduced to boundaries, repeat late adoptions, silent / own-cycle re-entries and Odd switches
Referee: REFEREE-2 successor 21, Opus 5.5 (D15, L37; D1 "Never downgrade the referee to save money"), independent second referee.
Written 2026-10-30 from 01:02Z (date -u).

**Object.**
- docs/si/P-N5-CUT-box43.md at l-si 2678f6c6: sha1 d6519d3d72d67d25bafd21b7034092eaa4315457, 221 lines (`git show 2678f6c6:<path> |
  sha1sum`, `| wc -l`); equal to the Lead's figures. 2678f6c6 is an ancestor of origin/claude/l-si.
- Premises read in context:
  - SPEC S1-S5;
  - RESULTS R15 (a), (c), (d), R47 (a), R56, R86 and R88, as in my FRAME report;
  - R89 (P-N5-FRAME, which I signed: R2-N5-FRAME.md), whose DUAL-ORDER, W-run definition, GP*-RUN and STRETCH-RED's λ_W item the packet
    cites as "R89 draft". R89 has since LANDED (RESULTS 4d85668e), so the citation should say so (N-CUT-1).
- L-RED R128 (l-red 0e91e875): CONJECTURE REP-LIN dead on latew. Instances copied to R2-N5-CUT/inst/ from 0e91e875 (latew_K8_m32.pg
  3498a23d, .start 89195cae; latew_K20_m32.pg 063d173c, .start f6ac6560).

**Independence.** `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic cut`: 0 at 01:03Z and 01:21Z. Names only; no
docs/referee/ file opened; no `git log` on origin/claude/referee. The lane's odd/*.py, box64/*.py and rund/quotecheck.py were RUN only as the
pinned blocks (check.sh l. 797-813, in a detached worktree at 2678f6c6, under `set -euo pipefail`: logs/pinned_check.txt), never imported. My
control is my own code: R2-N5-CUT/cut_check.py, on my lane's dual_check.Runner (SPEC N5 on si.py, read-only) and my FRAME helpers.

**Scope (D1, D18).** A REDUCTION of N5's iteration count on every game to four counts B*, REP*, SC* and O*, none bounded here. CUT-POLY is
an implication. G-N5-TIME stays OPEN. Not a TARGET.md claim, not M3, not a gauntlet pass.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| 1 | setting, Fact B, symbols, premises | well formed; 13 quotes: 10 strictly verbatim, 3 faithful "…" elisions (§1) |
| 2 | Lemma OPT-OFF (i), (ii) | SIGNED (case analysis of (ii) checked case by case, §2.1; standing premise as R89's FR-N1: N-CUT-2) |
| 2 | Lemma W-MON′ | SIGNED |
| 2 | Lemma W-SUCC | SIGNED |
| 3 | Lemma W-RETURN-G | SIGNED |
| 4 | Corollary CUT-CHARGE (and its Remark) | SIGNED |
| 5 | Lemma FRESH-SPLIT and its ENT bound (separately; not used by §8) | SIGNED |
| 6 | Lemma LATE-SPLIT (i)-(iii), its Consequence, Corollary R*-REP | SIGNED. The body has the CORRECT form (a REPEAT is W-paid, W-silent or own-cycle). §0's table summary omits own-cycle (N-CUT-4) |
| 7 | Lemma WV-R | SIGNED |
| 8 | Theorem CUT-RED | SIGNED |
| 8 | Corollary CUT-POLY (the conditional) | SIGNED as an implication. REP* is a PREMISE, not REP-LIN; R128's Θ(n²) does not touch [P-REP] (§8, N-CUT-5) |
| 9 | READING, DATA | not signed. Pinned blocks PASS. My code reproduces the lane's class counts (§4) |
| — | the lane's RESULTS-line proposal (as quoted by the Lead) | formula MATCHES Theorem CUT-RED. The definitions behind "…" were not given to me: the list of what must be in it is in §5 |

No gap. Nothing FALSE. Notes N-CUT-1..N-CUT-10 (§6).

## 1. Setting, Fact B, quotes
- Quotes: my strict qcheck (R2-N5-CORE/qcheck.py at 2678f6c6) reports 10/13 OK; SHIFT=1 gives 0/13 (logs/quotes*.txt). The 3 misses are each
  a "…" elision, and I checked the parts by hand:
  - FRAME l. 170-172 elides «and rewards are injective, so each vertex's W-cycle node changes at most n − 1 times per piece: at most n(n − 1)
    λ_W-changing» (the packet states the elided count in its "Used for" sentence);
  - late.py l. 2-3 elides the prefix «L-NEW box 65:» and «(--start: GAME.start).»;
  - late.py l. 21-22: the "…" stands only for a line break.
  All three are faithful.
- Fact B ✓ ([S4a]-[S4c], [R15d]).
  - A non-fallback transition either changes σ (σ_{t+1} = σ_new ≠ σ_t, so Iσ_t ≠ ∅: an S4a step) or keeps σ and then changes τ.
  - A fallback with Iσ ≠ ∅ is Even: it changes σ and keeps τ.
  - A fallback with Iσ = ∅ is Odd: it changes τ.
  - So every transition is an S4a step with τ kept, or a boundary. Data FB: 0 violations on every transition.
- A τ*-piece is well defined and contains no boundary.

## 2. One-player facts
**2.1 OPT-OFF.**
- (i) [S4a]: σ′ is S1's optimal counterstrategy in the dual of H against τ* = τ_t. Under the standing premise (S1-Xi read on the dual: pointwise
  optimum, realised by plays; R89's FR-N1 / R57 (a), (b)), with DUAL-ORDER, σ′ maximises G's order at every vertex over the Even strategies
  inside A = G_{τ*}|H_t. ✓ (N-CUT-2: name the premise.)
- (ii): I checked each case.
  - "off-cycle" means CN(v) ≠ v, so v may still lie ON its cycle (below its top). The packet's first bullet says "σ′v's play avoids v",
    which is false for such v. The formula W(v) = ext(v, W(σ′v)) still holds:
    - v is below c, so it is not added to P;
    - ℓ_v = ℓ_{σ′v} + 1, because from σ′v the cycle reaches c before v.
    - Reflection needs only v ∉ P(W(σ′v)), which holds because v is below c.
    So the bullet's justification needs one clause; the statement is unaffected (N-CUT-3).
  - Case 1 (v not on y's σ′-play): W″(v) = ext(v, W(y)) ⊴ W(v) = ext(v, W(σ′v)). Reflection applies: either the cycle nodes differ (reward
    kept by ext), or they are the same and v ∉ either P. ✓
  - Case 2 (v on y's path to its cycle node, which includes v on y's cycle before c):
    - W(y) = (c, D ⊔ P(σ′v), ℓ + L), where D = the y…v segment above c, v included.
    - σ″ closes C = v → y → … → v, and C's vertices are exactly that segment.
    - D's top even ⇒ a better reward than c ⇒ W″(v) ▷ W(v), contradicting (i).
    - D's top odd ⇒ W(y) ◁ W(σ′v).
    - D = ∅, c even ⇒ W(y) is longer ⇒ ◁.
    - D = ∅, c odd ⇒ C's top is below c and so has a better reward than c ⇒ contradicts (i).
    - The self-loop y = v is this case with D = {v} ∩ (above c). ✓
  - Case 3 (v on y's cycle, reached after c):
    - CN(y) = c, and P(σ′v) = ∅.
    - σ″'s cycle C = v → y → … → c → … → v has top c when P(y) = ∅, giving Case 1's formula; otherwise its top is P(y)'s top, above c.
    - P(y)'s top even ⇒ contradicts (i); odd ⇒ W(y) ◁ W(σ′v). ✓
  - The cases are exhaustive. ✓
- The off-cycle premise is needed: control X_OO2_own (OPT-OFF (ii) evaluated at own-cycle-node v) bites (§4). The lane's tog6b_n32 instance
  is in my pins.
- Data:
  - OO1: Wn_t ⊵ W^{τ_t}(σ″) pointwise for every single switch σ″ = σ_{t+1}[v → y], (v, y) ∈ H_t (all of them for n ≤ 60, else sampled), plus
    random strategies inside H_t.
  - OO2: every off-cycle v, every (v, y) ∈ H_t.
  - Both 0 violations.

**2.2 W-MON′.** σ_t ⊆ H_t, then (i). ✓ The frame is τ_t, and τ_{t+1} may differ. Data WM: 0 violations.

**2.3 W-SUCC.** Per step inside the piece: if σ(v) is unchanged, W-MON′. Otherwise:
W_{t+1}(σ_{t+1}v) ⊵ W_{t+1}(σ_t v) (OPT-OFF (ii) at t → t + 1, needing v off-cycle at t + 1 and (v, σ_t v) ∈ H_t) ⊵ W_t(σ_t v) (W-MON′). ✓
Data WS (per step, whenever v is off-cycle at t + 1): 0 violations.

## 3. W-RETURN-G
- Range: q − 1 ≥ a and j − 1 ≤ b, so q − 1 … j − 1 lie in one τ*-piece. The transitions q − 1 → q, …, j − 2 → j − 1 are S4a steps with τ*
  kept, and j − 1 → j is an S4a step in the frame τ* (τ_j may differ).
- The chain:
  - W*_q(c) ⊴ W*_q(σ_q v): OPT-OFF (ii) at q − 1 → q, with (v, c) ∈ H_{q−1} and v off-cycle at q;
  - ⊴ W*_{j−1}(σ_{j−1}v): W-SUCC on [q, j − 1], with off-cycle on [q + 1, j − 1];
  - ⊴ W*_j(σ_{j−1}v): W-MON′;
  - ⊴ W*_j(σ_j v) = W*_j(c): OPT-OFF (ii) at j − 1 → j, with off-cycle at j.
- The constancy hypothesis makes the ends equal, so every link is an equality. ✓
- W*_j is W^{τ*}(σ_j), the old-τ frame of state j. The packet's definitions say so (W^τ_t, τ* := τ_{j−1}); the RESULTS line must carry it
  (§5).
- Data WRG: the conclusion holds for EVERY anchor (not only the smallest) whose hypotheses hold, 0 violations. Control X_WRG_cut: an
  "anchor" taken across a boundary (q − 1 = s < a) fails the conclusion, so the piece condition max(s, a) ≤ q − 1 is needed.

## 4. CUT-CHARGE, FRESH-SPLIT
- Classes. A re-entry changes σ(v), so by Fact B it is an S4a step or an Even fallback (an Odd fallback keeps σ).
  - F: an Even fallback.
  - FR: an S4a step with no anchor.
  - C: the smallest anchor q exists and v is its own cycle node somewhere on [q, j].
  - P: otherwise, and W*(c) changes on [q, j].
  - S: the rest, silent by §3.
  - The classes partition the re-entries. ✓
- ENT_R ≤ 1 + #re-entries: the first entry counts 1, and every later entry is preceded inside R by a leave. ✓
- P: its change transition t ∈ [q, j − 1] has τ_t = τ* (it lies in the piece), so W^{τ_t} = W*. It lies in [s + 1, j] ⊆ span. One WCH*
  transition per P re-entry, distinct because windows are disjoint. ✓
- FR: a > s (otherwise q = s + 1 is an anchor: σ_s v = c and s ≤ j − 2, because s + 1 ≤ j − 1 by the re-entry definition). So a − 1 → a is
  a boundary (maximality of the piece; Fact B) with s ≤ a − 1 < a ≤ j − 1.
- F: the re-entry is itself a boundary, j − 1 → j.
- The transition sets {s → s + 1, …, j − 1 → j} of consecutive re-entries are disjoint (j_prev ≤ s). So F / FR re-entries use distinct
  boundaries of R, both ends in R. FC ≤ B_R ✓.
- Remark: a second re-entry in one piece has its own leave s′ ≥ a as an anchor (q = s′ + 1). #FR ≤ 1 per (pair, piece) ✓.
- Data CC1-CC3: classes partition; every P has its WCH* witness; every FR has its boundary at a − 1 ∈ [s, j − 1], none reused; ENT
  inequality; FC ≤ B_R; #FR ≤ 1 per pair and piece. All 0 violations.
- FRESH-SPLIT:
  - The five cases partition FR. My checker assigns exactly one, in the packet's order.
  - (LATE): no anchor and j − 2 ≥ a > s give (v, c) ∉ H_{j−2}, so (v, c) ∉ Iσ_{j−2}. The chain W*_{j−2}(c) = W*_j(c) ▷ W*_j(σ_{j−1}v) ⊵
    W*_{j−1}(σ_{j−1}v) ⊵ W*_{j−1}(σ_{j−2}v) ⊵ W*_{j−2}(σ_{j−2}v) is checked link by link (W-MON′, OPT-OFF (ii) with v off-cycle at j − 1,
    W-MON′).
  - BLOCKED at j − 2 is R88's (τ_{j−2} = τ*). ✓
  - ENT bound: BA + LATE + CY = #F + #G0 + #SAME + #LATE + #CY ≤ FC, and WC joins WCH* (its change lies in [a, j] ⊆ [s + 1, j]). ✓
  - Data FS: the LATE claim and the §5 ENT bound, 0 violations.
- Reproduction of the lane's pins by my code:
  - rise_thin51_n40 (S3): F 14, FR 92, P 19, C 0, S 0 (= «REENT 125 CUTRE 14 FRESH 92 CYC 0 WPAID 19 SILENT 0»).
  - Its FR split: WC 68, G0 9, LATE 15, CY 0, SAME 0 (= «FR_WC 68 … FR_GAIN0 9 FR_CYC 0 FR_LATE 15»).
  - Late adoptions: 23, all FIRST.
  - so_th_n32: late 6 = FIRST 4 + REPEAT 2 (= «'late': 6, … 'first': 4, 'repeat': 2»).

## 4.2 Own control: data (cut_check.py; every log RESULT PASS, 0 violations of FB, OO1, OO2, WM, WS, WRG, CC1-CC3, FS, LS1-LS3, RREP, WV, CR)
| corpus | runs / transitions | OO1 / OO2 / WS checks | re-entries (F / FR / C / P / S) | WRG checks | late adoptions (FIRST / REPEAT) | max B* / REP* / T | controls that bite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| box59/sbcg.lst, all 719 games, S3 (n ≤ 100 at full deviations; n > 100 sampled, OO1S 10) | 719 / 11,621 | 86,336 / 647,486 / 473,219 | 11,669 (557 / 6,031 / 4 / 5,035 / 42); FR split WC 3,925, G0 1,787, LATE 313, CY 1, SAME 5 | 50 | 1,141 (1,100 / 41) | 55 / 6 / 264 | OO2_own 534, WRG_cut 472 |
| lane pins (rise_thin51_n40, fc_3, so_th_n32, tog6b_n32, hntop_n3 + start) | 6 / 246 | 2,316 / 10,909 / 8,854 | 530 | 0 | 42 (39 / 3) | 6 / 2 / 78 | OO2_own 15, WRG_cut 18 |
| L-RED's red/ (carryobs, spanobs, tobs, wobs ×2, d_wobs; start + S3) | 12 / 3,154 | 46,671 / 272,572 / 229,116 | 5,502, all P | 0 | 0 | 280 (d_wobs: Odd-heavy, O* 279) / 0 / 1,072 | — |
| hntop_n2..n8 (start + S3) | 14 / 1,267 | 15,962 / 108,717 / 92,484 | 8,282, all P | 0 | 0 | 0 / 0 / 291 | — |
| latew_K8_m32, latew_K20_m32 (R128; start + S3) | 4 / 986 | 19,325 / 117,516 / 97,346 | 3,348, all P | 0 | 898 (118 / 780) | 2 / **570** (n 538; K8: 210, n 370) / 700 | — |
| random 3,000 games n 5-14 + 300 n 15-30 (S3 + 2 random) | 9,900 / 16,717 | 51,815 / 85,402 / 24,053 | 32 | 0 | 1 | 6 / 0 / 9 | OO2_own 346, WRG_cut 22 |

- The lane's §9 DATA is reproduced EXACTLY by independent code on the same 719 games:
  - re-entries 11,669 with F 557, FR 6,031, C 4, P 5,035, S 42;
  - FR split WC 3,925, G0 1,787, LATE 313, CY 1, SAME 5;
  - late adoptions 1,141 = FIRST 1,100 + REPEAT 41;
  - largest REP_F 6.
- REPEAT census (LATE-SPLIT (ii)):
  - every REPEAT in every corpus is W-paid (X_REP_rise 41 sbcg + 780 latew + 3 pins);
  - W-silent REPEATs 0 and own-cycle REPEATs 0.
  - So the corrected form's two extra cases are never exhibited: they come from the proof, not from data (N-CUT-10).
- latew confirms R128 on my engine: REP* = 570 > n = 538 on latew_K20_m32 (REP-LIN false). Polynomial behaviour is not claimed.
- W-RETURN-G's hypotheses hold jointly 50 times (all on sbcg; class S 42 uses the smallest anchor, and WRG checks every anchor). Its
  conclusion holds every time.
- Caps: OPT-OFF (i)'s single-switch deviations are exhaustive for n ≤ 60. Above that, 30 per step (10 on sbcg n > 100) are sampled, plus 2
  random H_t strategies per step: OO1_sampled_steps 780 on sbcg. OPT-OFF (ii), W-SUCC and all counting checks are exhaustive.

## 5. LATE-SPLIT, R*-REP, WV-R, CUT-RED (the Lead's context points)
- **LATE-SPLIT, the corrected form.** On a W-run, every transition is an S4a step with τ kept (Fact B), and W = W^τ.
  - (ii) The leave k is UNIQUE in (u₁, u₂): u₁, u₂ are consecutive late adoptions, and every adoption of z after u₁ is late, because the edge
    was blocked before u₁. My data confirm a unique leave every time (LS2).
  - Chain: OPT-OFF (ii) at k → k + 1 (σ_k y = z, so (y, z) ∈ H_k), then W-SUCC, then W-MON′, then OPT-OFF (ii) at u₂ → u₂ + 1.
  - So, off-cycle on [k + 1, u₂ + 1], either W(z) changes there or the adoption is W-silent. Equality, not a strict rise, is what the chain
    gives: the Lead's correction is right, and the packet's (ii) and Consequence carry it.
  - The own-cycle case is excluded from (ii) and counted in CYC_F.
  - (iii) holds via W-SUCC on [k + 1, t] and blocked-at-t. ✓
  - Consequence: the intervals [k + 1, u₂ + 1] are disjoint, so #REPEAT ≤ WCH_F(z) + SIL_F + CYC_F. ✓
  - But **§0's table** says «a REPEAT needs a W-rise of z or is W-silent», omitting own-cycle (N-CUT-4).
  - Data: REPEAT census in §4.2 (all W-paid); LS1-LS3 0 violations.
- **R*-REP:** R*_T ≤ #late ≤ FIRST + REP ≤ m_E + REP_F. ✓ Data RREP: 0 violations.
- **WV-R:**
  - Inside a τ*-piece Q there are no fallbacks and τ is constant, and Q's end transitions are boundaries, which also end W-runs. So the W-runs
    inside Q are exactly Q's pieces between its λ_W-changes. My checker compares the two partitions run by run: equal everywhere.
  - Then GP*-RUN, plus Λ_Q ≤ n(n − 1) ([SR-λ]; W-MON on a fallback-free piece), plus R*-REP. ✓
  - Data WV: 0 violations.
- **CUT-RED.**
  - Bookkeeping as R86 COMPOSE-RUN: ≤ 2n(n − 1) λ / λ^U changes, and ≤ n(n − 1) + 1 runs of each kind.
  - Per pair: ≤ 1 + B_R + WCH* + SIL + CYC.
  - WCH* ≤ B_R + (B_R + 1)K. A non-boundary WCH* transition is an S4a step with τ kept, so it is a W(c)-change inside one piece. The pieces
    meeting R are ≤ B_R + 1, separated by boundaries (Fact B). Each piece contributes ≤ WCH_Q(c) ≤ K(n, m_E, REP*_Q) ≤ K(n, m_E, REP*)
    (K is monotone; a W-run inside Q is a W-run of the run).
  - Sum over ≤ m_E pairs. ✓
  - The formula «m_E·[1 + B* + B* + (B* + 1)·K] + SC* + O*» equals the line's «m_E·[1 + 2B* + (B* + 1)·K] + SC* + O*».
  - Data CR: the bound per run, and its two intermediate inequalities per λ-run, 0 violations.
- **CUT-POLY and REP-LIN (the Lead's point).**
  - §8 takes REP* as a parameter. [P-REP] asks REP* ≤ p(n) for SOME polynomial p. R128's REP = Θ(n²) per W-run on latew kills only REP-LIN
    (REP_F ≤ n), which the packet names only in a READING note. [P-REP] stands. ✓
  - The note «[P-REP]: CONJECTURE REP-LIN (REP_F ≤ n)» is now out of date and should say "REP-LIN DEAD (R128); [P-REP] open" (N-CUT-5).
  - CUT-POLY's "polynomial in n" uses m_E ≤ n² (E ⊆ V × V); one clause (N-CUT-6).

**The RESULTS-line proposal.**
- The Lead quoted: «N5 on EVERY game: T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E
  + REP* + 1) … a REDUCTION (none of B*, REP*, SC*, O* bounded here)».
- The formula and K match §8 exactly.
- I have not seen the text behind "…". For it to carry every hypothesis, it must define each of these (my REQUIRED list; three line errors
  today were undefined symbols):
  1. T = the transitions of the run; m_E (Even out-edges).
  2. λ-run (Ξ's cycle-node map constant) and λ^U-run (U on G^d), as in R86.
  3. BOUNDARY := an Even S4c fallback or a τ-changing transition; B* := max over λ-runs R of the boundaries with both ends in R.
  4. W-run (R89), late adoption and BLOCKED (R88 / R89), FIRST / REPEAT; REP* := max over W-runs F of REP_F.
  5. For SC*, the most delicate part (it MUST be the §4 per-λ-run classes, not §6's per-W-run SIL_F / CYC_F, which share the names):
     - leave / re-entry of (v, c) in R;
     - the τ*-piece of j − 1 (a maximal run with τ = τ* and every inside transition an S4a step), with τ* := τ_{j−1};
     - the frame W* := the values of the (σ_t, τ*)-plays, including at t = j;
     - an anchor q (max(s, a) ≤ q − 1 ≤ j − 2, (v, c) ∈ σ_{q−1} ∪ Iσ_{q−1}) and the smallest anchor;
     - C (v its own W*-cycle node at some state of [q, j]); S (anchored, off-cycle on [q, j], W*(c) constant on [q, j]);
     - SC* := max_R Σ_{(v, c)} (#S + #C).
  6. O* := max over λ^U-runs R′ of the τ-changing transitions with both ends in R′.
- Without item 5's frame, "silent" and "own-cycle" are ambiguous: the frame is τ_{j−1}, not τ_t.
- Please send me the full proposed line, and I will check it word by word against this list.

## 6. Notes (not gaps)
- N-CUT-1 (citation). [DO], [GPR], [SR-λ] cite "R89 draft"; R89 has LANDED (RESULTS 4d85668e). Cite RESULTS R89.
- N-CUT-2 (standing premise, = R89's FR-N1 / H1). OPT-OFF (i) uses that S4a's σ_new is the pointwise optimum of the dual arena AND
  realises its values by plays (R57 (a), (b) on the dual). Name it.
- N-CUT-3 (OPT-OFF (ii), first bullet). «the play from v is v followed by σ′v's play, which avoids v» is false when v lies on its cycle
  below the top c. The formula W(v) = ext(v, W(σ′v)) and the reflection still hold (v is below c, so it is in no P-set, and ℓ adds 1).
  Add one clause.
- N-CUT-4 (§0 table). «a REPEAT needs a W-rise of z or is W-silent» should read «… or is W-silent, or y is its own cycle node on the
  interval» (the body is right). Any RESULTS wording of LATE-SPLIT must use the body's form.
- N-CUT-5 (§8 READING note). REP-LIN is DEAD (L-RED R128); [P-REP] (polynomial) is unaffected. Update the note.
- N-CUT-6 (CUT-POLY). "T ≤ q(n)" uses m_E ≤ n²; say so.
- N-CUT-7 (W-RETURN-G and CUT-CHARGE, the frame). All W* values, including W*_j, are in the frame τ* = τ_{j−1}. When τ_j ≠ τ_{j−1}, W*_j ≠
  W_j. The packet is consistent; a line or a reading that drops "τ*" changes the classes.
- N-CUT-8 (FRESH-SPLIT's LATE). The blocked conclusion is about state j − 2 in R88's sense (τ_{j−2} = τ*), so a FRESH-LATE re-entry is a
  late adoption only if j − 2 and j − 1 lie in one W-run (no λ_W change between): DATA, not claimed.
- N-CUT-10 (DATA). No W-silent and no own-cycle REPEAT occurs in any corpus (sbcg, pins, red/, hntop, latew, random). The corrected form
  of LATE-SPLIT (ii) is required by the proof, not by data. CONJECTURE-level question for the lane: is every REPEAT W-paid? Open; not used.
- N-CUT-9 (name clash). SIL / CYC are used twice: §4's per-λ-run classes (in SC*) and §6's per-W-run REPEAT classes (SIL_F, CYC_F). Rename
  one, e.g. SIL^RE / CYC^RE.

## 7. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-CUT/{cut_check.py, pins.lst, red.lst, hn.lst, latew.lst, inst/ (latew copies), run_all.sh,
  logs/ (pinned_check.txt, quotes*.txt)}.
- FINDINGS:
  - All items SIGNED, with no gap. CUT-POLY is signed as an implication.
  - LATE-SPLIT's body has the correct form (W-paid, W-silent or own-cycle); §0's summary omits own-cycle.
  - REP* is a premise: R128 kills only REP-LIN.
  - My code reproduces the lane's pinned class counts exactly.
  - The line's formula matches. Its definitions behind "…" must include the six items in §5 (SC*'s frame and classes above all).
- NEEDS: Lead: send the full proposed RESULTS line for a word-by-word check; route N-CUT-1..10 to L-SI. §C on your word after REFEREE 19's
  report.

## 8. Addendum: the RESULTS-line proposal, symbol by symbol (Lead 01:22Z; written 01:3xZ by date -u)
Object: docs/agents/P-N5-CUT-line-proposal.md at trunk 09d6f0c4, the lane's text (verbatim per the Lead), checked against §1-§8.
| symbol / clause | in the line | verdict |
| --- | --- | --- |
| formula and K | «T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1)» | = Theorem CUT-RED with K(n, m_E, REP*) ✓ |
| T, n, m_E | not defined | precision: "T the transitions (iterations) of the run, m_E the edges leaving Even vertices" |
| λ-run, λ^U-run | not defined, no citation | REQUIRED: "as in RESULTS R86" |
| B* | «the largest number of Even S4c fallbacks plus τ-changing transitions inside one λ-run» | ✓ = §8 B* (BOUNDARY; "inside" = both ends in R) |
| REP* | «repeat late adoptions (a second or later late adoption of the same Even edge) inside one W-run» | ✓ = §6 REPEAT. But W-run and late adoption are not defined or cited. REQUIRED: "W-run as in RESULTS R89, late adoption as in RESULTS R88 / R89" |
| SC* | «the largest number of W-silent plus own-cycle re-entries of Even edges in one λ-run» | **UNDERDEFINED; REQUIRED fix** (below) |
| O* | «τ-changing transitions inside one λ^U-run» | ✓ = §8 O* |
| "via … LATE-SPLIT (first late adoptions ≤ m_E per W-run)" | | ✓ (§6 (i)) |
| scope: «polynomial iff they are, Corollary CUT-POLY» | | **claims more than CUT-POLY** (below) |

- **SC* (REQUIRED).** "W-silent re-entry" and "own-cycle re-entry" are §4's classes S and C, which the line does not define. They depend on:
  - the τ*-piece of j − 1 and the frame τ* := τ_{j−1}, applied also at state j (N-CUT-7);
  - an anchor and the SMALLEST anchor q;
  - C: v its own W*-cycle node at SOME state of [q, j]; S: the rest of the anchored, off-cycle-throughout re-entries with W*(c) constant on
    [q, j].
  Natural readings of the line's words give different, possibly SMALLER, counts, and SC* is an upper-bound parameter, so a smaller count
  would not support the theorem:
  - "W-silent" in the frame τ_j, or with no anchor requirement;
  - "own-cycle" at j only;
  - §6's per-W-run SIL_F / CYC_F, which carry the same names (N-CUT-9).
  I cannot exhibit a numerical failure (the theorem's bound is far from tight: max T 1,072 against bounds of order 10⁸ on my corpora). This is
  a definitional defect, not a demonstrated falsity.
  Fix: "SC* := the largest, over λ-runs R, number of re-entries of Even edges in R of class S (W-silent) or C (own-cycle) of P-N5-CUT §4
  (frame τ_{j−1}, smallest anchor)", or spell §4's definitions out.
- **"polynomial iff they are".** CUT-POLY proves only "if". The converse is TRUE and short, but not in the packet. For every run:
  - B* ≤ T and O* ≤ T;
  - REP* ≤ the late adoptions ≤ n·T (each transition has at most one adoption per Even vertex);
  - SC* ≤ the re-entries ≤ n·T (each re-entry is a transition at which one Even vertex switches).
  So T ≤ q(n) gives all four ≤ n·q(n). Fix: add the converse to the fixes file (I sign it as stated here), or drop "iff" and write "polynomial
  if they are". As the line stands, it claims more than the packet.
- **Standing premise (R57 (b) / G-N5T-1), the Lead's question, judged independently.**
  - OPT-OFF (i) needs that S4a's σ_new is the POINTWISE OPTIMUM of the one-player arena A and that its values are realised by the
    (σ_new, τ*)-plays.
  - Optimality of the VJ00 counterstrategy is RESULTS R57 (a) (VJ). That SPEC S1's procedure realises it is the standing SPEC premise of
    R57 / R51 (d) (1E-N3; R57's own words: «that S1's procedure realises an optimal σ̄ is VJ00 §6 …»). R88's W-MON and R89's ODD-FREEZE use
    the same premise (my N-GP-2; R89 FR-N1 / H1).
  - So YES: OPT-OFF (i), and through it every later item, uses that standing premise. The packet should name it (my N-CUT-2), and the line
    may say "under the standing SPEC premise of RESULTS R57" as R57's own line does.
  - G-N5T-1 (the code link n5.py ↔ SPEC, DATA) is NOT used by any proof. It matters only for the lane's data.
  - My checker tests the premise directly as DATA on its runs. OO1: Wn_t is ⊵ every single-switch and random strategy inside H_t, 0
    violations in 222,000+ checks (§4.2).
- **Verdict on the line.** The formula MATCHES. Three things are REQUIRED before landing: SC*'s definition, citations for λ-run / λ^U-run /
  W-run / late adoption, and "iff" either proved in the fixes or dropped. Precision: T, m_E, and naming the standing premise.
