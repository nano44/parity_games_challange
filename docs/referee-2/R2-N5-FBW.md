# R2-N5-FBW: second-referee check of packet P-N5-FBW (L-SI box 9: fallback gates and the Ξ/W gap; fallback levels along a scope run; the per-level count). REFEREE-2 (successor 6), 2026-10-25 06:05Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-FBW (Lead 05:53Z), pinned at trunk claude/vibrant-johnson-nxvvxo e69772b (merged into my branch
as 1b507af3). Object: docs/si/P-N5-FBW-box9.md, sha1 88337bd621d3467dde4b35aa93b254bf847bb330 (218 lines; checked at the pin and on my tree).
Background read: RESULTS R17 (a) (F1), R18 (d) Lemma S and G-1OA-6, R20 (b) FBL (u* ≠ none strong form; my lane's R2-N5-XA §2), R25,
R28-R30 (my R2-N5-OE, R2-N5-CLS, R2-N5-SN), SPEC S1 / S4a-c.
Independence: I have not read docs/referee/ for this packet (no FBW report is on my tree). I did not run or import fbw.py, reltrace.py,
the cls scripts, jclimb.py or any REFEREE probe. Lane instances are inputs only.
Tools (docs/referee-2/R2-N5-FBW/, own code on my R2-N5-LP / R2-N5-FB / R2-N5-SN tools): fbw_check.py, fbw_climb.py, run_all.sh,
totals.py, logs/, climb/. Every 𝒞^1O probe asserts exactly one Odd vertex with out-degree > 1. Phase key (λ_Ξ, τ).
Labels (D18 / L40): PROVED (L-SI succ. 4) is the packet's label. §6 is not to sign. Nothing here is a running-time bound, a TARGET.md
claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 premise P-OPT (and G-1OA-6) (the Lead's "hardest") | VALID | at an S4c fallback S4a ran at state k and returned σ_k, so σ_k is the arena optimum against τ_k. G-1OA-6 concerns σ_{k+1} (what S4c installs). R20 (b) FBL step 1 already rests on the same premise, signed |
| §1 Lemma FBW (every game) | SIGN | Step 2's case split (a) / (b1) / (b2) is complete; self-loops are covered |
| §2 Corollary FBW-S | SIGN | — |
| §2 Theorem CLS2 | SIGN | R29's (H-EQ) is closed by it |
| §3 Lemma FLAT-ALL | SIGN | — |
| §4 Lemma STRETCH | SIGN | N-FBW-1: PL (a) uses STRETCH also at k = e (a last block fallback f_N whose own transition changes COARSE_M). STRETCH's proof gives that (b stays good on [k+1, e], so no repeat at e), but the statement says k < e. One word |
| §5 Theorem PL (a)-(c) | SIGN | (b), (c) are vacuous in all data (0 dirty intervals, climbs included) |
| §5 Corollary PL-S | SIGN | — |
| §6 | not signed (as briefed) | NJB: 0 dirty intervals everywhere, including three climbs aimed at them |
No statement is NOT SIGNED. No counterexample.

## 0. P-OPT and G-1OA-6 (the Lead's "check hardest")
- SPEC S4a: σ′ := the pointwise optimum of the one-player arena A(σ_k) (Even on {σ_k(v)} ∪ Iσ_k(v), Odd fixed to τ_k), computed by
  the dual S1 procedure. R17 (a) (F1): that optimum dominates every arena strategy pointwise; R18 (d) Lemma S (c): it is what S4a
  computes.
- An S4c fallback fires exactly when S4a returned σ_k and S4b returned τ_k. So at state k, σ_k IS S4a's arena optimum. P-OPT,
  V_{σ′, τ_k} ⊴ W_k for every σ′ ∈ A(σ_k), is (F1) at the state k.
- G-1OA-6 (R18) says Lemma S (c)-(d) fails AT S4c fallbacks, in the sense that the transition k → k+1 does not install an arena optimum
  (S4c's switch-all is not one). P-OPT uses nothing about σ_{k+1}. The two are about different objects, and the packet's reading is
  right.
- The same premise is signed elsewhere. R20 (b) FBL step 1 reads "τ constant, the fallback is Even's, and S4a returned σ_k. So σ_k is the
  pointwise optimum of the arena in G_τ"; R23 (g) WM rests on it at S4a steps.
- One SPEC point: S4a's arena optimum is unique only up to tie-breaks (FIX 2 / FIX 4), and (F1) is about valuations. P-OPT is stated on
  valuations, so tie-breaks do not matter. Lemma DF (R27, FALSE) failed at an own cycle node through a length-only improvement that
  leaves that node's VALUE unchanged. That is exactly FBW's exceptional case, so the two are consistent.
- Mechanical, at every Even fallback (library, random general, climbs; 0 failures):
  - S4a's arena re-computed at the state returned σ_k at every one;
  - every single switch σ_k[y ↦ z] over the WHOLE arena failed to raise W(y): 44,611 library, 788 random, about 3.4 M in climbs.

## 1. Lemma FBW: SIGN
- Step 1. COARSE_δ agrees for Ξ and W at u and z. ℓ > δ makes the Ξ comparison strict above δ, so the W comparison is strict with the same
  level ℓ ((C1)-(C3)). ✓
- Step 2. I checked each case, writing V = W_k and V′ = V_{σ[y→z], τ_k}.
  - (a) z's play avoids y.
    - y its own cycle node: c_z ≠ y, and rew(c_z) > rew(y) from V z ▷ V u.
    - Otherwise: y ∉ P(V z) (play avoids y), and y ∉ P(V u) (if u's play meets y, y lies on its cycle below c). So y ⊕ is strict and
      cycle-node preserving. ✓
  - (b1) z's play meets y, y not on a cycle.
    - None of the q_i lies on y's cycle: from q_i the play reaches y, which would then be on the cycle.
    - u's play avoids the q_i and y. So P(V z) = P(V u) ⊔ D′.
    - D′ ≠ ∅: the even top of D′ is the top t of the new cycle, with pp(t) > pp(c).
    - D′ = ∅: length-only and longer, so c is odd, and t < c gives rew(t) > rew(c). ✓
  - (b2) y on its own cycle C_y with top c.
    - P(V z) ≠ ∅: t = the top of P(V z), even, above c.
    - P(V z) = ∅, c ∉ C: e lies after c and before y on C_y, so V z is longer; c is odd, t < c.
    - P(V z) = ∅, c ∈ C, y ≠ c: lengths +1 on both sides, the same parity rule.
    - y = c, P(V z) = ∅: V′(y) = V(y). The only non-strict case, with lev = −1. ✓
  - Self-loop z = y falls in (b1) (m = 0) or (b2) (a = 0, e = y). Checked.
- Step 3. Every strict case contradicts P-OPT. So ℓ > δ forces y = c (its own W-cycle node) and ℓ = −1. With δ = ⊥, Ξ(u) = W(u) has cycle
  node y, so λ_Ξ(y) = y by (P1). ✓
- Mechanical (0 failures), on Even fallbacks of random general games (4,000 + climbs), the library and random 𝒞^1O:
  - (a) on 3,921 library gates, 124 random general, 285 random 𝒞^1O, 16,257 + 123,788 in climbs;
  - (b) and Step 1 at every ℓ > δ: 45 library, 402 random, all with ℓ = −1 at an own cycle node;
  - the bound is tight (ℓ = δ ≥ 0) at 69,184 climb gates and never exceeded.

## 2. FBW-S, CLS2: SIGN
- FBW-S: δ ≤ r_k, because off R̄ Ξ = W, on R (C7) gives r_k, and at o it is r_k. FBW (a) then gives ℓ ≤ max(r_k, −1). At EQ, δ = ⊥ and every
  gate is case (b). ✓
- CLS2:
  - Fact R puts the r ≥ 0 fallbacks first; CLS1 (R29 (f)) orders them.
  - Later fallbacks have r ≤ −1, hence M = −1 (an Even fallback has a gate, of level ≥ −1).
  - So the sequence is non-increasing. ✓
- Mechanical:
  - Library: 627 scope runs, 981 fallbacks (956 THR u* ≠ none, 25 EQ, 0 u* = none).
  - Random 𝒞^1O: 148 EQ fallbacks.
  - Climbs: 77,213 in-scope fallbacks.
  - Order and bound: 0 failures.

## 3. FLAT-ALL: SIGN
- FBW-S gives r ≥ M ≥ 0, so THR with u* ≠ none, so FBL's strong form applies: switched edges are R → F leaves and flat F → F cycle-node
  switches. R vertices are not own cycle nodes under (h).
- (i)
  - The new cycle through a switched cycle node avoids o (H2 at k+1).
  - F_k vertices' plays stay inside F_k.
  - A play reaching o at k+1 meets no switched vertex, so it has the same route. ✓
- (ii) x0 ∈ F_k ⊆ F_{k+1}, so its H_{k+1}-play avoids o. Lemma S (a) with Odd fixed to x0 at o, R15 (a), OFF at x0, (C7) at o, then the
  sandwich. ✓
- (iii) OFF off R̄_{k+1}; on R̄_{k+1}, Lemma G (b) with the same route, (C7) and (ii). ✓
- (iv) TRANSFER with (iii). ✓
- Mechanical: 956 library + 77,192 climb checks of (i)-(iv), 0 failures.

## 4. STRETCH: SIGN (N-FBW-1)
- (1) A switch above M at a non-cycle-node y changes COARSE_M(Ξ y).
  - Ξ_{t+1}(y) = y ⊕ Ξ_{t+1}(z) and Ξ_t(y) = y ⊕ Ξ_t(u), with y on neither path ((P2) at each state).
  - COARSE_M of y ⊕ x is injective in COARSE_M(x) then, and COARSE_M(Ξ_{t+1} z) = COARSE_M(Ξ_t z) ≠ COARSE_M(Ξ_t u).
  - At cycle nodes the level is −1 (CN). ✓
- (2) and (3): the β bit, the best target, then b non-decreasing and frozen above M. ✓
- N-FBW-1. The proof shows that once y has been a level-M tail at k, it is not one at any k′ ∈ [k+1, e]. That includes k′ = e. PL (a)
  needs this for f_N, whose own transition may change COARSE_M (FLAT-ALL needs (h) at f_N + 1, which S need not give). The statement's
  "s ≤ k < e" should read "s ≤ k ≤ e". My checker tests k ≤ e.
- Mechanical: 1,328 library + 81,057 climb tail checks, 0 repeats.

## 5. PL and PL-S: SIGN
- (a) (h) at f_i + 1 for i < N, since S continues to f_N. FLAT-ALL (iii) at every block fallback but the last. So ≤ 1 + D_M constant runs,
  and STRETCH (with N-FBW-1) gives ≤ n_E fallbacks per run. ✓
- (b)
  - M ≤ M persists inside the interval (FLAT-ALL (iv), then TRANSFER).
  - The interval contains no fallback (blocks are consecutive by CLS2), so j is an S4a step.
  - U-loc with L = M needs a relevant change above M, i.e. σ̄(o) with O_j > M ≥ E_j.
  - Then OR (c) and TC-SPLIT for the θ level, and OR (a), (b) under H1 for the absorption. ✓
- (c)
  - (A_t) on each interval by CLS1's chain; no S4a leave (NL (ii)).
  - ABS-L: distinct absorptions that stay in R.
  - N_x ≤ d_o − 1 at every state of the block window (H1 throughout: all are in-scope states).
  - Releases only at the block fallbacks f_1 … f_{N−1}.
  - This is the count that ABS-COUNT lacked (R30); here H1 holds at the end. ✓
- PL-S: disjoint blocks, ≤ n levels ≥ 0, Σ REL_M ≤ REL(S). ✓
- Mechanical:
  - 249 library blocks (max 37 fallbacks, cl9_rep_b); PL (a) at every one; PL (c)'s hypothesis held on 129; PL-S on 45 scope runs.
  - 0 failures.
  - D_M = 0 in every block of every sample. Three climbs scoring dirty intervals (FIT=dirty from cl9_rep_b, jcl_x32_nest40,
    fb32_inr2_final; 8,000 runs) found none. So PL (b) and (c) are vacuous in data and rest on the proofs; NJB (§6) is unrefuted.

## 6. Data (DATA, not proof)
| batch | runs | key counts | violations |
| --- | --- | --- | --- |
| library (every 𝒞^1O experiments/**/*.pg, n ≤ 64; si/coarse instances incl. box9 up to n 128; 252 files), 3 starts | 756 | Even fallbacks 1,267; gates 3,921; P-OPT switches 44,611; scope runs 627; in-scope fallbacks 981; FLAT 956; blocks 249 | 0 |
| random general n 4-12 / 12-20 (seeds 9511, 9512) | 4,000 | Even fallbacks 110, gates 124 | 0 |
| random 𝒞^1O n 6-16 / 16-32 (seeds 9513, 9514) | 5,500 | in-scope fallbacks 148 (all EQ) | 0 |
| climbs (FIT=dirty ×3 on 𝒞^1O; FIT=fbw on general games from a random seed) | 24,000 | Even fallbacks 90,844; gates 140,045 (69,184 tight); P-OPT switches 3.44 M; FLAT 77,192; dirty intervals 0 | 0 |
- Thin spots:
  - PL (b), (c): no dirty interval anywhere.
  - FBW (b) is exercised only at length-only own-cycle-node gates (as it must be).
  - In-scope fallbacks with u* = none: 0 (they would have M ≤ −1).

## Signature
REFEREE-2 (successor 6), Opus 5.5 (D15), 2026-10-25:
- VALID: P-OPT (G-1OA-6 does not apply).
- SIGN: FBW, FBW-S, CLS2, FLAT-ALL, STRETCH (note N-FBW-1, closed: the statement's "k < e" should be "k ≤ e"), PL (a)-(c), PL-S.
After two signatures (D18/L40) these become PROVED (L-SI successor 4; REFEREE-2, and REFEREE if it signs). OPEN: NJB, NJ-INT, blocks
where r drops to M, level −1 counts, REL(S); G-N5-TIME.

## §C. Comparison with REFEREE (docs/referee/R-N5-FBW.md: report 9a94dc7b, §C a04615b5). REFEREE-2 successor 7, 2026-10-25 08:27Z (date -u)
Successor 6 wrote the report above and parked. I write this §C from that report (25962855) and from REFEREE's file at trunk c699d5b4,
which carries a04615b5. REFEREE-2's report was pushed before REFEREE's was read: successor 6 had not seen it, and I opened it only now.
Signature (Opus 5.5, D15).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| P-OPT / G-1OA-6 | VALID | VALID | VALID, for the same reason: G-1OA-6 is about S4c's installed σ_{k+1}, while P-OPT uses S4a's output σ_k at state k |
| FBW | SIGNED | SIGN | signed by both |
| FBW-S, CLS2 | SIGNED | SIGN | signed by both; (H-EQ) closed |
| FLAT-ALL | SIGNED WITH GAP FBW-1 | SIGN as written; now SIGN WITH GAP FBW-1 (citation, closed), see C.2 | signed by both with FBW-1 |
| STRETCH | SIGNED | SIGN (N-FBW-1) | signed by both |
| PL (a)-(c) | SIGNED WITH GAP FBW-2 | SIGN | signed by both; FBW-2 = N-FBW-1 |
| PL-S | SIGNED | SIGN | signed by both |
No verdict differs in substance. FLAT-ALL changes only in its gap column: I accept FBW-1, which my lane's §3 had missed. Neither referee
found a counterexample.

### C.2 Item by item
- FBW-1 (FLAT-ALL (i)): CONFIRMED. My lane's §3 repeated the packet's "H2 at k+1", and that was the wrong citation.
  - The packet derives "its new play is a cycle through y′" from λ(y′) = y′. λ is the honest cycle node, so the cycle is y′'s honest
    H_{k+1}-cycle.
  - If o lay on that cycle, the cycle would leave o by σ̄_{k+1}(o), not by τ(o). So it is not o's W-cycle, and H2 (o on no W-cycle)
    does not exclude it.
  - H1 at k+1 does exclude it: o lies on no honest cycle. H1 is part of the hypothesis "(h) at k+1". Off o the honest graph and the
    (σ, τ) graph agree, so the rest of (i) follows.
  - A second repair also works, and it too needs H1. With (h) at k+1, Fact 0 of P-N5-FRZ §2 (my R2-N5-FRZ §2: SIGN) gives W-cycle node =
    λ at every vertex. So y′'s (σ, τ)-play is also a cycle through y′, and H2 then excludes o from it. Fact 0's c_θ ∈ F step uses H1.
  - Either way the statement stands. REFEREE's fixes-file line ("honest H_{k+1}-cycle … else H1 would fail at k+1") is the shorter
    repair, and I adopt it.
  - DATA (fbw1_probe.py, own N5 of R2-N5-FRZ; logs/fbw1_probe_*.txt):
    - library: 682 in-phase Even fallbacks with (h) at k and k+1 (LIB × 3 starts), but none switched an own cycle node;
    - random 𝒞^1O: 4,000 games, 7 switched own cycle nodes;
    - o was on neither the honest cycle nor the W-cycle in every case: 0 failures, thin.
- FBW-2 = N-FBW-1: the same point, found independently. STRETCH must read "k ≤ e" so that PL (a) covers the block's last fallback f_N.
  - REFEREE accepts my lane's sharper reason: f_N's own transition may change COARSE_M, because FLAT-ALL (iii) needs (h) at f_N + 1,
    which the scope run need not give.
  - REFEREE filed it under PL (a), my lane under STRETCH. One fixes-file line (the STRETCH statement) covers both.
- Data: no disagreement.
  - P-OPT is checked by both, with complementary teeth: my lane checked every arena single switch (44,611 library, 3.44 M in climbs);
    REFEREE checked every gate switch with a non-fallback control (1,061 / 1,164).
  - D_M = 0 in every block for both. My lane's three dirty-interval climbs (8,000 runs) found none. So PL (b)/(c) are vacuous in all
    data, and NJB is unrefuted.
  - Block counts differ by starts and selection (my lane: 3 starts, 249 blocks; REFEREE: canonical start, 172). The statements agree.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | FBW-2 | N-FBW-1 | wording, closed | §4 STRETCH: "… at most once among the fallbacks k of S with s ≤ k ≤ e" (step (3) covers k′ = e; PL (a) needs it for f_N, whose own transition may change COARSE_M, since (h) at f_N + 1 is not given) |
| 2 | FBW-1 | accepted in this §C (my lane's §3 had repeated "H2") | citation, closed | §3 FLAT-ALL (i): "That cycle is y′'s honest H_{k+1}-cycle; it avoids o, else H1 would fail at k+1 (H2 alone does not exclude it: such a cycle leaves o by σ̄(o), not τ(o))" |

### C.4 Joint label (D18/L40)
- PROVED (L-SI successor 4; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER:
  - FBW on every game;
  - on 𝒞^1O: FBW-S, CLS2, FLAT-ALL (row 2), STRETCH (row 1), PL (a)-(c), PL-S.
- CONJECTURE: NJB, NJ-INT.
- OPEN: r-drop blocks, level −1 counts, REL(S), G-N5-TIME.
- Not a TARGET.md claim.

Signed: REFEREE-2 successor 7 (Opus 5.5, D15).
